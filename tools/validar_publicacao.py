from __future__ import annotations

import argparse
import re
from dataclasses import dataclass, field
from pathlib import Path


BLOCKED_EXTENSIONS = {".pbix", ".pbit", ".pbip", ".abf", ".bak", ".env"}
SENSITIVE_PATTERNS = (
    re.compile(r"(?i)(password|client_secret|access_token)\s*[:=]"),
    re.compile(r"(?i)https?://[^/\s]+\.sharepoint\.com"),
    re.compile(r"(?i)https?://[^/\s]+\.powerbi\.com"),
    re.compile(r"(?i)C:\\Users\\"),
)
EXCLUDED_PATH_PARTS = {".git", ".pytest_cache", "__pycache__", "superpowers", "artifacts"}


@dataclass
class ValidationResult:
    errors: list[str] = field(default_factory=list)


def _is_excluded(path: Path, root: Path) -> bool:
    relative_parts = set(path.relative_to(root).parts)
    return bool(relative_parts & EXCLUDED_PATH_PARTS)


def validate_publication(root: Path) -> ValidationResult:
    result = ValidationResult()
    for path in root.rglob("*"):
        if not path.is_file() or _is_excluded(path, root):
            continue
        if path.suffix.lower() in BLOCKED_EXTENSIONS:
            result.errors.append(f"arquivo proibido: {path.relative_to(root)}")
            continue
        if path.suffix.lower() not in {".md", ".mmd", ".png", ".py"} and path.name != ".gitignore":
            result.errors.append(f"arquivo fora da allowlist: {path.relative_to(root)}")
            continue
        if path.suffix.lower() in {".md", ".mmd", ".py"} and not path.name.startswith("test_"):
            text = path.read_text(encoding="utf-8", errors="replace")
            for pattern in SENSITIVE_PATTERNS:
                if pattern.search(text):
                    result.errors.append(f"padrao sensivel em: {path.relative_to(root)}")
                    break
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida se o case pode ser publicado.")
    parser.add_argument("root", type=Path)
    args = parser.parse_args()
    result = validate_publication(args.root)
    if result.errors:
        for error in result.errors:
            print(f"ERROR: {error}")
        return 1
    print("Publicacao validada: nenhum bloqueio encontrado.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
