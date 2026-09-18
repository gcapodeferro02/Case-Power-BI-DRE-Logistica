from pathlib import Path

from PIL import Image, ImageChops

from sanitizar_assets import sanitize_image


def test_sanitize_blurs_declared_regions(tmp_path: Path) -> None:
    source = tmp_path / "source.png"
    destination = tmp_path / "out.png"
    image = Image.new("RGB", (80, 80), "#FFFFFF")
    for x in range(20, 60):
        for y in range(20, 60):
            color = (10, 40, 180) if (x + y) % 2 else (220, 230, 240)
            image.putpixel((x, y), color)
    image.save(source)

    output = sanitize_image(source, destination, regions=[(20, 20, 60, 60)])

    assert output.exists()
    assert ImageChops.difference(Image.open(source), Image.open(output)).getbbox() is not None
