# Typography And Layout System

Use this deterministic layout for native-image post-production. In prompt-only mode, repeat the same coordinates, type hierarchy, and font direction inside the English image prompt.

## Canvas and fixed coordinates

- Output canvas: `1584x672` (approximately 2.35:1), crop-safe for WeChat.
- Default title field: `x=76..620`, `y=88..585`; keep all text left aligned.
- Eyebrow: one line, 22-26 px.
- Main title: `in vivo CAR-T`, one line, 64-76 px.
- Subtitle: `抗体偶联 LNP\n技术路径深度研究`, two lines, 36-44 px.
- Footer: `抗体精准定位 · mRNA 递送 · 体内生成 CAR-T`, one line, 17-20 px.
- Do not add a box, underline, divider, shadow, gradient, or translucent panel behind text.
- Place text directly on the source image's natural quiet field. If no quiet field exists, regenerate the background first.

## Generation-to-layout conversion

Use the same title field in two representations. Image prompts use percentages; post-production uses pixels on the canonical canvas.

| Canonical pixels (`1584x672`) | Prompt percentage |
| --- | --- |
| `x=76..620` | `x=4.8%..39.1%` |
| `y=88..585` | `y=13.1%..87.1%` |

For another 2.33-2.35:1 input image, `scripts/compose_cover.py` scales these coordinates and font sizes proportionally. Do not use a different title zone for generation and post-production.

## Prompt-only title requirement

When no image-generation capability exists, the final English prompt must request the exact title in this left field. It must state the title verbatim, reserve the left 39% of the canvas, use the Chinese and Latin font directions below, and prohibit any other text or objects in the field. Also provide the post-production fallback specification because model-rendered Chinese can be inaccurate.

## Bundled font library

Fonts live in `assets/fonts/`; default Chinese text uses `Hanchan-Zhengkai-Big5.ttf`, while all Latin/English text uses `PreTesto_it.ttf`.

| Key | Asset | Suggested use |
| --- | --- | --- |
| `yangrendong` | `YangRendongZhushi-Light.ttf` | Restrained scientific editorial alternative |
| `pixel` | `Chinese-Pixel-Fangdian.otf` | Swiss, archive, technical data |
| `baituxiaobai` | `Baitu-Xiaobai.ttf` | Clay and approachable biomedical |
| `hanchan_zhengkai` | `Hanchan-Zhengkai-Big5.ttf` | Default scientific editorial cover; Nature and classical journal tone |
| `qingliu_lishu` | `Qingliu-Lishu.ttf` | Business editorial and strong opinion |
| `xieling` | `Xieling-Futi-ExtraLight.otf` | Microscopic, clinical, airy technical |
| `yunfeng_hanchan` | `Yunfeng-Hanchan.ttf` | Archive, blueprint, engineering notes |
| `pretesto` | `PreTesto_it.ttf` | Fixed Latin/English title and acronym rendering |

English lockup: `in vivo CAR-T`, `LNP`, `mRNA`, and `CAR-T` are always rendered with `PreTesto_it.ttf` by `scripts/compose_cover.py`. Chinese text remains on the selected Chinese font, defaulting to Hanchan Zhengkai.

## Theme title profiles

Theme IDs begin at 1 and correspond to former themes 4-16. Use the source-specific quiet field when one is defined by the background; otherwise use the default title field.

| ID | Style | Text palette |
| --- | --- | --- |
| 1 | Clay diorama | terracotta + deep brown |
| 2 | Nature science | ice white + coral |
| 3 | Businessweek | black + clinical red |
| 4 | Monocle | forest green + brick red |
| 5 | Micro documentary | silver white + fluorescence green |
| 6 | Swiss poster | black + cobalt blue |
| 7 | Science archive | charcoal + oxide red |
| 8 | Pipeline map | navy + teal |
| 9 | Clinical evidence | navy + safety orange |
| 10 | Cell mechanism | ice white + RNA gold |
| 11 | Medical congress | cold white + magenta |
| 12 | Molecular blueprint | ice white + node yellow |
| 13 | Bioprocess | deep teal + amber |
