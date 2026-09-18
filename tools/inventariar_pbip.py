from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


TABLE_RE = re.compile(r"^\s*table\s+(?P<name>.+?)\s*$")
DEFINITION_RE = re.compile(r"^\s*(?P<kind>column|measure|partition)\s+(?P<name>.+?)(?:\s*=.*)?$")
RELATIONSHIP_RE = re.compile(r"^\s*relationship\s+(?P<id>\S+)")
ENDPOINT_RE = re.compile(r"^\s*(?P<kind>fromColumn|toColumn):\s*(?P<endpoint>.+?)\s*$")
EXPRESSION_RE = re.compile(r"^\s*expression\s+(?P<name>.+?)\s*=")


def _clean_name(value: str) -> str:
    value = value.strip()
    if value.startswith("'") and value.endswith("'"):
        return value[1:-1].replace("''", "'")
    return value


def _split_endpoint(value: str) -> tuple[str, str]:
    value = value.strip()
    if "." not in value:
        return _clean_name(value), ""
    table, column = value.split(".", 1)
    return _clean_name(table), _clean_name(column)


def _read_table(path: Path) -> dict[str, Any]:
    table_name = path.stem
    definitions: dict[str, list[str]] = {"columns": [], "measures": [], "partitions": []}
    for line in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        table_match = TABLE_RE.match(line)
        if table_match:
            table_name = _clean_name(table_match.group("name"))
            continue
        match = DEFINITION_RE.match(line)
        if match:
            name = _clean_name(match.group("name").strip())
            definitions[f"{match.group('kind')}s"].append(name)
    for values in definitions.values():
        values.sort(key=str.casefold)
    return {"name": table_name, **definitions}


def _read_relationships(path: Path) -> list[dict[str, Any]]:
    relationships: list[dict[str, Any]] = []
    current: dict[str, Any] | None = None
    for line in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        relationship_match = RELATIONSHIP_RE.match(line)
        if relationship_match:
            if current:
                relationships.append(current)
            current = {"id": relationship_match.group("id")}
            continue
        endpoint_match = ENDPOINT_RE.match(line)
        if current and endpoint_match:
            table, column = _split_endpoint(endpoint_match.group("endpoint"))
            prefix = "from" if endpoint_match.group("kind") == "fromColumn" else "to"
            current[f"{prefix}_table"] = table
            current[f"{prefix}_column"] = column
    if current:
        relationships.append(current)
    return sorted(
        relationships,
        key=lambda item: (
            item.get("from_table", ""),
            item.get("from_column", ""),
            item.get("to_table", ""),
            item.get("to_column", ""),
        ),
    )


def _read_pages(report_root: Path) -> list[str]:
    pages_root = report_root / "definition" / "pages"
    metadata_path = pages_root / "pages.json"
    if not metadata_path.exists():
        return []
    metadata = json.loads(metadata_path.read_text(encoding="utf-8-sig"))
    page_names: list[str] = []
    for page_id in metadata.get("pageOrder", []):
        page_path = pages_root / page_id / "page.json"
        if not page_path.exists():
            continue
        page = json.loads(page_path.read_text(encoding="utf-8-sig"))
        display_name = page.get("displayName") or page.get("name") or page_id
        page_names.append(str(display_name))
    return page_names


def _read_expressions(model_root: Path) -> dict[str, Any]:
    path = model_root / "definition" / "expressions.tmdl"
    if not path.exists():
        return {"names": [], "source_types": []}
    names: list[str] = []
    source_types: set[str] = set()
    for line in path.read_text(encoding="utf-8-sig", errors="replace").splitlines():
        match = EXPRESSION_RE.match(line)
        if match:
            names.append(_clean_name(match.group("name")))
        if "SharePoint.Contents" in line:
            source_types.add("SharePoint")
        if "Excel.Workbook" in line:
            source_types.add("Excel")
        if "Csv.Document" in line:
            source_types.add("CSV")
    return {"names": sorted(names, key=str.casefold), "source_types": sorted(source_types)}


def build_inventory(pbip_root: Path) -> dict[str, Any]:
    model_root = next(pbip_root.glob("*.SemanticModel"), None)
    report_root = next(pbip_root.glob("*.Report"), None)
    if model_root is None or report_root is None:
        raise FileNotFoundError("PBIP deve conter diretorios *.SemanticModel e *.Report")

    tables_root = model_root / "definition" / "tables"
    tables = [_read_table(path) for path in sorted(tables_root.glob("*.tmdl"), key=lambda item: item.name.casefold())]
    table_names = sorted((table["name"] for table in tables), key=str.casefold)
    relationships_path = model_root / "definition" / "relationships.tmdl"
    relationships = _read_relationships(relationships_path) if relationships_path.exists() else []

    return {
        "schema_version": 1,
        "tables": table_names,
        "table_details": tables,
        "relationships": relationships,
        "expressions": _read_expressions(model_root),
        "pages": _read_pages(report_root),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Inventaria metadados publicaveis de um projeto PBIP.")
    parser.add_argument("pbip_root", type=Path)
    parser.add_argument("--output", type=Path, default=Path("artifacts/model-inventory.json"))
    args = parser.parse_args()

    inventory = build_inventory(args.pbip_root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        json.dumps(inventory, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Inventario gerado: {args.output}")


if __name__ == "__main__":
    main()
