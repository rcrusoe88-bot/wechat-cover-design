"""Deterministically compose cover text with separate Chinese and Latin fonts."""
from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


THEMES = {
    1: {"label": "主题 1 · 生物医学黏土封面", "main": "#57392D", "accent": "#964A3C", "sub": "#57392D", "footer": "#57392D"},
    2: {"label": "主题 2 · Nature 科学意象", "main": "#EDF8FA", "accent": "#FF7E73", "sub": "#EDF8FA", "footer": "#BFEFF5"},
    3: {"label": "主题 3 · Businessweek 商业隐喻", "main": "#090909", "accent": "#B53732", "sub": "#090909", "footer": "#090909"},
    4: {"label": "主题 4 · Monocle 产业观察", "main": "#285541", "accent": "#A94F3C", "sub": "#285541", "footer": "#285541"},
    5: {"label": "主题 5 · 显微纪录摄影", "main": "#E6EEEE", "accent": "#36E562", "sub": "#E6EEEE", "footer": "#CCD2D1"},
    6: {"label": "主题 6 · Swiss 极简海报", "main": "#111111", "accent": "#1749C6", "sub": "#111111", "footer": "#111111"},
    7: {"label": "主题 7 · 复古科学档案", "main": "#22201D", "accent": "#A33D2E", "sub": "#22201D", "footer": "#22201D"},
    8: {"label": "主题 8 · 药物管线地图", "main": "#123B69", "accent": "#1B9994", "sub": "#123B69", "footer": "#123B69"},
    9: {"label": "主题 9 · 临床证据蓝图", "main": "#12375C", "accent": "#FF6B21", "sub": "#12375C", "footer": "#52616B"},
    10: {"label": "主题 10 · Cell 机制图谱", "main": "#DCECF0", "accent": "#D7A84B", "sub": "#DCECF0", "footer": "#B7D2DA"},
    11: {"label": "主题 11 · 医学大会主视觉", "main": "#F0F8FA", "accent": "#D94A98", "sub": "#F0F8FA", "footer": "#48CED0"},
    12: {"label": "主题 12 · 分子蓝图", "main": "#DCECF0", "accent": "#E5EA38", "sub": "#DCECF0", "footer": "#DCECF0"},
    13: {"label": "主题 13 · 生物工艺工程", "main": "#164B68", "accent": "#B37A28", "sub": "#164B68", "footer": "#164B68"},
}


def parse_color(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


def draw_segments(draw: ImageDraw.ImageDraw, x: int, y: int, segments: list[tuple[str, ImageFont.FreeTypeFont]], fill: tuple[int, int, int]) -> None:
    """Draw mixed-script text left-to-right without relying on font fallback."""
    cursor = x
    for text, face in segments:
        draw.text((cursor, y), text, font=face, fill=fill)
        cursor += int(draw.textlength(text, font=face))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--theme", required=True, type=int, choices=range(1, 14))
    parser.add_argument("--font", default="assets/fonts/YangRendongZhushi-Light.ttf", help="Chinese font")
    parser.add_argument("--latin-font", default="assets/fonts/PreTesto_it.ttf", help="Latin/English font")
    args = parser.parse_args()

    image = Image.open(args.input).convert("RGB")
    draw = ImageDraw.Draw(image)
    profile = THEMES[args.theme]
    root = Path(__file__).resolve().parents[1]
    zh_path = Path(args.font)
    latin_path = Path(args.latin_font)
    if not zh_path.is_absolute():
        zh_path = root / zh_path
    if not latin_path.is_absolute():
        latin_path = root / latin_path

    zh_small, zh_main, zh_sub, zh_footer = (font(zh_path, n) for n in (25, 72, 41, 20))
    latin_main, latin_sub, latin_footer = (font(latin_path, n) for n in (72, 41, 20))
    x = 76
    draw.text((x, 96), profile["label"], font=zh_small, fill=parse_color(profile["accent"]))
    draw.text((x, 152), "in vivo CAR-T", font=latin_main, fill=parse_color(profile["main"]))

    # Keep the two-line subtitle field fixed while rendering the acronym in PreTesto.
    first = "抗体偶联 "
    draw.text((x, 246), first, font=zh_sub, fill=parse_color(profile["sub"]))
    draw.text((x + int(draw.textlength(first, font=zh_sub)), 246), "LNP", font=latin_sub, fill=parse_color(profile["sub"]))
    draw.text((x, 295), "技术路径深度研究", font=zh_sub, fill=parse_color(profile["sub"]))

    footer_y = 578
    prefix = "抗体精准定位  ·  "
    middle = "  ·  体内生成 "
    draw.text((x, footer_y), prefix, font=zh_footer, fill=parse_color(profile["footer"]))
    cursor = x + int(draw.textlength(prefix, font=zh_footer))
    draw.text((cursor, footer_y), "mRNA", font=latin_footer, fill=parse_color(profile["footer"]))
    cursor += int(draw.textlength("mRNA", font=latin_footer))
    draw.text((cursor, footer_y), middle, font=zh_footer, fill=parse_color(profile["footer"]))
    cursor += int(draw.textlength(middle, font=zh_footer))
    draw.text((cursor, footer_y), "CAR-T", font=latin_footer, fill=parse_color(profile["footer"]))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    image.save(args.output, quality=96)


if __name__ == "__main__":
    main()
