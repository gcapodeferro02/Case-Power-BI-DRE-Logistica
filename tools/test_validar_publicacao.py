from pathlib import Path

from validar_publicacao import validate_publication


def test_rejects_pbix_and_sensitive_patterns(tmp_path: Path) -> None:
    (tmp_path / "report.pbix").write_bytes(b"x")
    (tmp_path / "secrets.md").write_text("password = 'hidden'", encoding="utf-8")

    result = validate_publication(tmp_path)

    assert len(result.errors) == 2


def test_accepts_documentation_and_png(tmp_path: Path) -> None:
    (tmp_path / "README.md").write_text("Case publico com dados ofuscados.", encoding="utf-8")
    (tmp_path / "diagram.mmd").write_text("flowchart LR\nA-->B", encoding="utf-8")
    (tmp_path / "image.png").write_bytes(b"png")

    result = validate_publication(tmp_path)

    assert result.errors == []
