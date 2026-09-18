import json
from pathlib import Path

from inventariar_pbip import build_inventory


def test_inventory_lists_tables_relationships_and_pages(tmp_path: Path) -> None:
    root = tmp_path / "pbip"
    tables = root / "BASE_OBZ.SemanticModel" / "definition" / "tables"
    pages = root / "BASE_OBZ.Report" / "definition" / "pages" / "summary"
    tables.mkdir(parents=True)
    pages.mkdir(parents=True)

    (tables / "dCalendario.tmdl").write_text(
        "table dCalendario\n\tcolumn Date\n\tpartition dCalendario = calculated\n",
        encoding="utf-8",
    )
    (tables / "fato.tmdl").write_text(
        "table fato\n\tcolumn valor\n\tmeasure Total = SUM(fato[valor])\n",
        encoding="utf-8",
    )
    (root / "BASE_OBZ.SemanticModel" / "definition" / "relationships.tmdl").write_text(
        "relationship abc\n"
        "\tfromColumn: fato.Date\n"
        "\ttoColumn: dCalendario.Date\n",
        encoding="utf-8",
    )
    (root / "BASE_OBZ.Report" / "definition" / "pages" / "pages.json").write_text(
        json.dumps({"pageOrder": ["summary"]}),
        encoding="utf-8",
    )
    (pages / "page.json").write_text(
        json.dumps({"displayName": "Resumo"}),
        encoding="utf-8",
    )

    inventory = build_inventory(root)

    assert inventory["tables"] == ["dCalendario", "fato"]
    assert inventory["relationships"][0]["from_table"] == "fato"
    assert inventory["pages"] == ["Resumo"]
