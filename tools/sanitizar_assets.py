from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFilter, ImageFont


Color = tuple[int, int, int]
Region = tuple[int, int, int, int]


def sanitize_image(source: Path, destination: Path, regions: Iterable[Region]) -> Path:
    image = Image.open(source).convert("RGB")
    for left, top, right, bottom in regions:
        crop = image.crop((left, top, right, bottom)).filter(ImageFilter.GaussianBlur(radius=18))
        image.paste(crop, (left, top))
    destination.parent.mkdir(parents=True, exist_ok=True)
    image.save(destination, format="PNG", optimize=True)
    return destination


def _font(size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    candidates = [
        Path("C:/Windows/Fonts/segoeui.ttf"),
        Path("C:/Windows/Fonts/arial.ttf"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size)
    return ImageFont.load_default()


def _arrow(draw: ImageDraw.ImageDraw, start: tuple[int, int], end: tuple[int, int], color: Color) -> None:
    draw.line((*start, *end), fill=color, width=4)
    x, y = end
    draw.polygon([(x, y), (x - 12, y - 7), (x - 12, y + 7)], fill=color)


def create_diagram(destination: Path, title: str, boxes: list[str]) -> Path:
    width, height = 1600, 680
    image = Image.new("RGB", (width, height), "#F6F8FB")
    draw = ImageDraw.Draw(image)
    draw.text((60, 40), title, fill="#132238", font=_font(38))
    box_width, box_height = 250, 120
    gap = 55
    y = 260
    total = len(boxes) * box_width + (len(boxes) - 1) * gap
    x = (width - total) // 2
    for index, label in enumerate(boxes):
        left = x + index * (box_width + gap)
        draw.rounded_rectangle((left, y, left + box_width, y + box_height), radius=20, fill="#FFFFFF", outline="#3D6EA8", width=4)
        lines = label.split("\n")
        for line_index, line in enumerate(lines):
            bbox = draw.textbbox((0, 0), line, font=_font(24))
            draw.text(
                (left + (box_width - (bbox[2] - bbox[0])) / 2, y + 32 + line_index * 32),
                line,
                fill="#132238",
                font=_font(24),
            )
        if index < len(boxes) - 1:
            _arrow(draw, (left + box_width + 8, y + box_height // 2), (left + box_width + gap - 8, y + box_height // 2), "#6C87A8")
    destination.parent.mkdir(parents=True, exist_ok=True)
    image.save(destination, format="PNG", optimize=True)
    return destination


def create_report_mockup(destination: Path, title: str, subtitle: str) -> Path:
    width, height = 1600, 900
    image = Image.new("RGB", (width, height), "#F7F8FA")
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, width, 92), fill="#17395C")
    draw.text((55, 28), title, fill="#FFFFFF", font=_font(34))
    draw.text((55, 125), subtitle, fill="#52677D", font=_font(24))
    cards = [(55, 190, 360, 325), (390, 190, 695, 325), (725, 190, 1030, 325), (1060, 190, 1365, 325)]
    for left, top, right, bottom in cards:
        draw.rounded_rectangle((left, top, right, bottom), radius=14, fill="#FFFFFF", outline="#D7E0E9", width=3)
        draw.rectangle((left + 24, top + 24, right - 24, top + 58), fill="#E5EAF0")
        draw.rectangle((left + 24, top + 78, right - 80, top + 106), fill="#D1DAE4")
    draw.rounded_rectangle((55, 370, 1000, 820), radius=16, fill="#FFFFFF", outline="#D7E0E9", width=3)
    draw.rounded_rectangle((1040, 370, 1545, 820), radius=16, fill="#FFFFFF", outline="#D7E0E9", width=3)
    for index in range(7):
        y = 430 + index * 48
        draw.rectangle((95, y, 410, y + 18), fill="#DDE5ED")
        draw.rectangle((450, y, 910, y + 18), fill="#B8C7D6")
    for index in range(5):
        y = 440 + index * 68
        draw.ellipse((1100, y, 1140, y + 40), fill="#7EA3C9")
        draw.rectangle((1170, y + 8, 1460, y + 28), fill="#DDE5ED")
    draw.rectangle((55, 845, 1545, 870), fill="#E6EBF1")
    destination.parent.mkdir(parents=True, exist_ok=True)
    image.save(destination, format="PNG", optimize=True)
    return destination


def main() -> None:
    parser = argparse.ArgumentParser(description="Gera assets ilustrativos e sanitiza imagens.")
    parser.add_argument("--output", type=Path, default=Path("assets"))
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=True)
    create_diagram(args.output / "arquitetura-dados.png", "Arquitetura do case", ["Arquivos", "Power Query", "Modelo", "Medidas", "Relatório"])
    create_diagram(args.output / "fluxo-atualizacao.png", "Fluxo de atualização", ["Arquivo novo", "Leitura", "Limpeza", "Refresh", "Validação"])
    create_diagram(args.output / "modelo-relacionamentos.png", "Relacionamentos", ["Dimensões", "Fatos", "Medidas", "Visão final"])
    mockups = args.output / "telas-ofuscadas"
    create_report_mockup(mockups / "01-resumo.png", "Visão executiva DRE", "Layout demonstrativo com dados removidos")
    create_report_mockup(mockups / "02-detalhamento.png", "Detalhamento por categoria", "Layout demonstrativo com dados removidos")
    print(f"Assets gerados em: {args.output}")


if __name__ == "__main__":
    main()
