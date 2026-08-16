"""Quality gates shared by the cover compositor and the standalone auditor."""
from __future__ import annotations

from dataclasses import dataclass

from PIL import Image, ImageFilter, ImageStat


BASE_CANVAS = (1584, 672)
TITLE_ZONE = (76, 88, 620, 585)


@dataclass(frozen=True)
class ThemePalette:
    label: str
    main: str
    accent: str
    sub: str
    footer: str


THEMES = {
    1: ThemePalette("主题 1 · 生物医学黏土封面", "#57392D", "#964A3C", "#57392D", "#57392D"),
    2: ThemePalette("主题 2 · Nature 科学意象", "#EDF8FA", "#FF7E73", "#EDF8FA", "#BFEFF5"),
    3: ThemePalette("主题 3 · Businessweek 商业隐喻", "#090909", "#B53732", "#090909", "#090909"),
    4: ThemePalette("主题 4 · Monocle 产业观察", "#285541", "#A94F3C", "#285541", "#285541"),
    5: ThemePalette("主题 5 · 显微纪录摄影", "#E6EEEE", "#36E562", "#E6EEEE", "#CCD2D1"),
    6: ThemePalette("主题 6 · Swiss 极简海报", "#111111", "#1749C6", "#111111", "#111111"),
    7: ThemePalette("主题 7 · 复古科学档案", "#22201D", "#A33D2E", "#22201D", "#22201D"),
    8: ThemePalette("主题 8 · 药物管线地图", "#123B69", "#1B9994", "#123B69", "#123B69"),
    9: ThemePalette("主题 9 · 临床证据蓝图", "#12375C", "#FF6B21", "#12375C", "#52616B"),
    # Themes 10 and 12 use a bright paper field; their title colors must be dark.
    10: ThemePalette("主题 10 · Cell 机制图谱", "#103B5C", "#9A6A16", "#103B5C", "#315A73"),
    11: ThemePalette("主题 11 · 医学大会主视觉", "#F0F8FA", "#D94A98", "#F0F8FA", "#48CED0"),
    12: ThemePalette("主题 12 · 分子蓝图", "#0E3D63", "#7C7200", "#0E3D63", "#315A73"),
    13: ThemePalette("主题 13 · 生物工艺工程", "#164B68", "#B37A28", "#164B68", "#164B68"),
}


def parse_color(value: str) -> tuple[int, int, int]:
    value = value.lstrip("#")
    return tuple(int(value[index : index + 2], 16) for index in (0, 2, 4))


def relative_luminance(color: tuple[int, int, int]) -> float:
    channels = []
    for channel in color:
        value = channel / 255
        channels.append(value / 12.92 if value <= 0.04045 else ((value + 0.055) / 1.055) ** 2.4)
    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]


def contrast_ratio(first: float, second: float) -> float:
    lighter, darker = max(first, second), min(first, second)
    return (lighter + 0.05) / (darker + 0.05)


def _scaled_title_zone(image: Image.Image) -> tuple[int, int, int, int]:
    width, height = image.size
    return (
        round(TITLE_ZONE[0] * width / BASE_CANVAS[0]),
        round(TITLE_ZONE[1] * height / BASE_CANVAS[1]),
        round(TITLE_ZONE[2] * width / BASE_CANVAS[0]),
        round(TITLE_ZONE[3] * height / BASE_CANVAS[1]),
    )


def audit_background(image: Image.Image, theme_id: int) -> list[str]:
    """Return blocking issues for a text-free source image before typography is drawn."""
    width, height = image.size
    ratio = width / height
    if not 2.25 <= ratio <= 2.45:
        return [f"expected a roughly 2.35:1 input image, got {width}x{height}"]

    zone = image.convert("RGB").crop(_scaled_title_zone(image))
    gray = zone.convert("L")
    values = list(gray.getdata())
    values.sort()
    low = values[max(0, round((len(values) - 1) * 0.10))]
    high = values[round((len(values) - 1) * 0.90)]
    texture = ImageStat.Stat(gray).stddev[0]
    edges = ImageStat.Stat(gray.filter(ImageFilter.FIND_EDGES)).mean[0]

    palette = THEMES[theme_id]
    color_luminance = relative_luminance(parse_color(palette.main))
    # The 10th/90th percentile avoids rejecting a clean field for one isolated pixel,
    # while still catching a field whose normal texture makes the title unreadable.
    background_gray = low if color_luminance < 0.5 else high
    background_luminance = relative_luminance((background_gray, background_gray, background_gray))
    contrast = contrast_ratio(color_luminance, background_luminance)

    issues: list[str] = []
    if texture > 54:
        issues.append(f"title field is too textured (grayscale deviation {texture:.1f}; maximum 54)")
    if edges > 48:
        issues.append(f"title field has too many edges (edge score {edges:.1f}; maximum 48)")
    if contrast < 4.5:
        issues.append(f"main title contrast is {contrast:.2f}:1; require at least 4.5:1")
    return issues
