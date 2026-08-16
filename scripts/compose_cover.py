"""Compose deterministic bilingual cover typography on a 2.35:1 background."""
from __future__ import annotations

import argparse
import re
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


BASE_CANVAS = (1584, 672)
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

LATIN_RUN = re.compile(r"[A-Za-z0-9+./-]+|\s+")


def parse_color(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in (0, 2, 4))


def load_font(path: Path, base_size: int, scale: float) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), max(8, round(base_size * scale)))


def draw_bilingual(
    draw: ImageDraw.ImageDraw,
    position: tuple[int, int],
    text: str,
    chinese_font: ImageFont.FreeTypeFont,
    latin_font: ImageFont.FreeTypeFont,
    fill: tuple[int, int, int],
) -> None:
    """Draw Chinese and Latin runs with explicit fonts instead of fallback glyphs."""
    cursor = position[0]
    for run in re.findall(r"[A-Za-z0-9+./-]+|\s+|[^A-Za-z0-9+./\-\s]+", text):
        face = latin_font if LATIN_RUN.fullmatch(run) else chinese_font
        draw.text((cursor, position[1]), run, font=face, fill=fill)
        cursor += round(draw.textlength(run, font=face))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--theme", required=True, type=int, choices=range(1, 14))
    parser.add_argument("--font", default="assets/fonts/Hanchan-Zhengkai-Big5.ttf", help="Chinese font")
    parser.add_argument("--latin-font", default="assets/fonts/PreTesto_it.ttf", help="Latin/English font")
    parser.add_argument("--eyebrow", help="Optional eyebrow; defaults to the theme label")
    parser.add_argument("--title", default="in vivo CAR-T", help="Exact main title")
    parser.add_argument("--subtitle-line1", default="抗体偶联 LNP", help="First subtitle line; use an empty string to omit")
    parser.add_argument("--subtitle-line2", default="技术路径深度研究", help="Second subtitle line; use an empty string to omit")
    parser.add_argument("--footer", default="抗体精准定位  ·  mRNA  ·  体内生成 CAR-T", help="Short footer; use an empty string to omit")
    args = parser.parse_args()

    image = Image.open(args.input).convert("RGB")
    width, height = image.size
    scale_x = width / BASE_CANVAS[0]
    scale_y = height / BASE_CANVAS[1]
    scale_font = min(scale_x, scale_y)
    if not 2.25 <= width / height <= 2.45:
        raise ValueError(f"expected a roughly 2.35:1 input image, got {width}x{height}")

    root = Path(__file__).resolve().parents[1]
    chinese_path = Path(args.font)
    latin_path = Path(args.latin_font)
    if not chinese_path.is_absolute():
        chinese_path = root / chinese_path
    if not latin_path.is_absolute():
        latin_path = root / latin_path

    draw = ImageDraw.Draw(image)
    profile = THEMES[args.theme]
    zh_small, zh_main, zh_sub, zh_footer = (load_font(chinese_path, size, scale_font) for size in (25, 72, 41, 20))
    latin_small, latin_main, latin_sub, latin_footer = (load_font(latin_path, size, scale_font) for size in (25, 72, 41, 20))
    x = round(76 * scale_x)
    y = lambda base: round(base * scale_y)

    eyebrow = args.eyebrow if args.eyebrow is not None else profile["label"]
    if eyebrow:
        draw_bilingual(draw, (x, y(96)), eyebrow, zh_small, latin_small, parse_color(profile["accent"]))
    if args.title:
        draw_bilingual(draw, (x, y(152)), args.title, zh_main, latin_main, parse_color(profile["main"]))
    if args.subtitle_line1:
        draw_bilingual(draw, (x, y(246)), args.subtitle_line1, zh_sub, latin_sub, parse_color(profile["sub"]))
    if args.subtitle_line2:
        draw_bilingual(draw, (x, y(295)), args.subtitle_line2, zh_sub, latin_sub, parse_color(profile["sub"]))
    if args.footer:
        draw_bilingual(draw, (x, y(578)), args.footer, zh_footer, latin_footer, parse_color(profile["footer"]))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    image.save(args.output, quality=96)


if __name__ == "__main__":
    main()
