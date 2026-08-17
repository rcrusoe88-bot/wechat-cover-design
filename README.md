# WeChat Cover Design

面向生物制药与生命科学内容的公众号封面设计 Skill。它不是通用插画提示词库，而是一套将文章观点、科研对象和读者认知重点转化为稳定封面构图的工作流。

适用于药物发现、LNP 与核酸递送、抗体偶联、细胞治疗、临床证据、分子设计、BD 交易、产业链、CMC 与生物工艺等内容。所有主题都为左侧标题、右侧科学主体的公众号首图而设计，避免标题后期硬贴在图像上。

## 它会做什么

- 从文章的实际论点选择 13 种生物制药视觉主题之一，而不是只按关键词套图。
- 固定左侧标题区、字体规则与安全边界，保证不同文章输出的版式稳定。
- 宿主同时具备生图和排版能力时，直接生成成品封面：先无字底图，再固定坐标叠字。
- 其他宿主输出无字底图提示词与精确叠字规范；不再让生图模型直接渲染中文标题。

## 适用场景

| 内容类型 | 建议主题 |
| --- | --- |
| 递送机制、细胞内过程、CAR-T | 主题 1 或主题 10 |
| 平台突破、重要研究发现 | 主题 2 |
| 估值、交易、证据错配、商业判断 | 主题 3 |
| 产业链、研发到临床、公司全景 | 主题 4 或主题 8 |
| 微观结合、纳米递送、组织微环境 | 主题 5 |
| 核心命题、技术对比、关系表达 | 主题 6 |
| 专利、技术史、工程壁垒 | 主题 7 |
| 临床疗效、安全性、队列与剂量 | 主题 9 |
| 年度进展、医学会议、转化里程碑 | 主题 11 |
| 偶联化学、处方、结构设计 | 主题 12 |
| CMC、放大、纯化、质控、CDMO | 主题 13 |

## 两种工作路径

Skill 不会根据宿主能力自动选择路径。每次封面请求开始时，先让用户确认“直接生图”或“提供提示词”。

### 直接生图

Skill 直接调用可用的原生生图工具，先生成右侧科学主体与左侧自然留白的无字背景。背景必须通过安静区、对比度和结构侵入检查后，才用固定版式叠加标题。若宿主只能生图、不能后期排版，Skill 输出无字背景和精确叠字规范，避免交付不可控的模型中文字。

### 提供提示词

Skill 输出一段完整英文无字底图提示词，其中强制写明：

- 画布为 `1584x672`（约 `2.35:1`）；
- 左侧 `x=4.8%..39.1%, y=13.1%..87.1%` 为标题区，右侧为科学主体；
- 图像中不得出现可读文字、标签、logo 或水印；
- 标题区不能出现科学主体、高对比边缘或数据标记。

同时会附带同样坐标的后期排版说明，作为唯一的文字渲染方式。

每一份最终 prompt 包都会附带 Alignment Record，记录文章论点、读者收获、主题理由、视觉隐喻、对象来源与内容层禁止替代物。这能防止把“关键词相关但文章无关”的画面误当成正确封面。

## 固定版式与字体

- 统一画布：`1584x672`
- 标题区域：`x=76..620, y=88..585`；有效文字宽度为 `500px`
- 生成提示词坐标：`x=4.8%..39.1%, y=13.1%..87.1%`
- 中文默认字体：`Hanchan-Zhengkai-Big5.ttf`
- 英文固定字体：`PreTesto_it.ttf`

两款字体均按 SIL Open Font License 1.1 随项目分发；版权、来源和许可证见 `assets/fonts/NOTICE.md` 与 `assets/fonts/OFL.txt`。

标题直接进入背景图的自然留白，不使用卡片、下划线、分隔线、阴影或半透明蒙层。

## 主题画廊

| 主题 1 | 主题 2 | 主题 3 |
| --- | --- | --- |
| [![主题1](assets/theme-previews/titled-thumbs/theme1-clay-diorama.jpg)](assets/theme-previews/theme1-clay-diorama.png) | [![主题2](assets/theme-previews/titled-thumbs/theme2-nature-science.jpg)](assets/theme-previews/theme2-nature-science.png) | [![主题3](assets/theme-previews/titled-thumbs/theme3-businessweek.jpg)](assets/theme-previews/theme3-businessweek.png) |
| 黏土微缩剖面 | Nature 科学意象 | Businessweek 商业隐喻 |

| 主题 4 | 主题 5 | 主题 6 |
| --- | --- | --- |
| [![主题4](assets/theme-previews/titled-thumbs/theme4-monocle.jpg)](assets/theme-previews/theme4-monocle.png) | [![主题5](assets/theme-previews/titled-thumbs/theme5-micro-documentary.jpg)](assets/theme-previews/theme5-micro-documentary.png) | [![主题6](assets/theme-previews/titled-thumbs/theme6-swiss-poster.jpg)](assets/theme-previews/theme6-swiss-poster.png) |
| Monocle 产业观察 | 显微纪录摄影 | Swiss 极简海报 |

| 主题 7 | 主题 8 | 主题 9 |
| --- | --- | --- |
| [![主题7](assets/theme-previews/titled-thumbs/theme7-science-archive.jpg)](assets/theme-previews/theme7-science-archive.png) | [![主题8](assets/theme-previews/titled-thumbs/theme8-pipeline-map.jpg)](assets/theme-previews/theme8-pipeline-map.png) | [![主题9](assets/theme-previews/titled-thumbs/theme9-clinical-evidence.jpg)](assets/theme-previews/theme9-clinical-evidence.png) |
| 复古科学档案 | 药物管线地图 | 临床证据蓝图 |

| 主题 10 | 主题 11 | 主题 12 |
| --- | --- | --- |
| [![主题10](assets/theme-previews/titled-thumbs/theme10-cell-mechanism.jpg)](assets/theme-previews/theme10-cell-mechanism.png) | [![主题11](assets/theme-previews/titled-thumbs/theme11-medical-congress.jpg)](assets/theme-previews/theme11-medical-congress.png) | [![主题12](assets/theme-previews/titled-thumbs/theme12-molecular-blueprint.jpg)](assets/theme-previews/theme12-molecular-blueprint.png) |
| Cell 机制图谱 | 医学大会主视觉 | 分子蓝图 |

| 主题 13 |
| --- |
| [![主题13](assets/theme-previews/titled-thumbs/theme13-bioprocess.jpg)](assets/theme-previews/theme13-bioprocess.png) |
| 生物工艺工程 |

## 本地标题合成

在可运行 Python 的环境中，先审核约 `2.35:1` 的无字背景，再用固定脚本叠加精确文字。坐标和字号会按输入尺寸等比缩放：

```text
python -m pip install -r requirements.txt
```

```text
python scripts/validate_cover.py --input <background.png> --theme 9 --json
python scripts/compose_cover.py --input <background.png> --output <cover.png> --theme 9 --title-prefix "Ab-mRNA-LNP" --title "不是被配体打败" --title-line2 "而是被工艺惯性困住" --subtitle-line1 "SELI 与表面工程" --subtitle-line2 "如何撬动 T 细胞靶向" --footer "抗体修饰 · SELI 两步工艺 · T 细胞靶向"
```

若生图服务仅支持 `16:9`，先生成无字底图，再在叠字时使用 `--crop-16-9` 居中裁为 `1584x672`：

```text
python scripts/compose_cover.py --input <background-16x9.png> --output <cover.png> --crop-16-9 --theme 10 --title "..."
```

运行 `python scripts/run_evals.py` 可检查结构化 brief、完整 prompt 和临时 brief 的回归契约。

使用方式与完整规则见 [SKILL.md](SKILL.md)。
