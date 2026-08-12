---
name: cover_themes5_16_selected
description: >
  用户选定的十二套扩展主题规格：Nature 科学意象、Businessweek 商业隐喻、Monocle 产业观察、
  显微纪录摄影、瑞士极简海报、复古科学档案、药物管线地图、临床证据蓝皮书、Cell 机制图谱、
  医学大会主视觉、分子蓝图、生物工艺工程。按 theme_registry 选中主题后读取对应章节。
---

# 用户选定扩展主题（theme5-theme16）

统一输出约 `2.35:1` 横版，首选 `1584x672` 或 `1260x540`。先提取文章主体、动作、证据和结论，再将文章对象代入主题骨架；不要机械复刻示例中的 LNP。

## 共同规则

- 默认生成无字底图：`No text, letters, numbers, labels, logos, signatures, or watermarks.`
- 准确标题由后期排版叠加；quiet zone 必须服从主题构图，不得让所有主题固定成左文右图。
- 示例图只约束媒介、构图、色板和层级；不得复制示例中的乱码、错误结构或平台星形标记。
- 每个最终 Prompt 必须加入本文件末尾的通用 Negative prompt。

## Theme 5 — Nature 科学意象风

参考图：`assets/theme-previews/theme5-nature-science.png`

- **适用**：重大科研突破、前沿机制、单一核心发现、技术平台发布。
- **视觉骨架**：一个宏大科学主体占据中右区域；用尺度、空间和光线形成科学隐喻；暗部自然容纳标题。
- **色板**：午夜蓝 `#061724`、冰青 `#BFEFF5`、冷白 `#EDF8FA`、珊瑚红 `#FF7E73`。
- **媒介**：顶级科学期刊封面级概念性 3D 生物医学艺术；少解释、多意象。
- **Prompt 核心**：`Create a premium conceptual scientific-journal cover. Transform {core_object} into one monumental translucent scientific subject; show {payload_or_inner_structure} inside and one precise interaction with {target_object}. Use credible molecular anatomy, dramatic depth, restrained light, and a single coral focal point. Keep a naturally low-detail dark region for optional title overlay.`
- **避免**：机制步骤、信息面板、普通科幻球体、过度霓虹。

## Theme 6 — Bloomberg Businessweek 商业隐喻风

参考图：`assets/theme-previews/theme6-businessweek.png`

- **适用**：估值与证据错配、BD 交易、资本泡沫、商业争议、尖锐行业判断。
- **视觉骨架**：一个三秒可懂的夸张比喻；大物体与小证据形成尺度冲突；标题可压在高对比背景上。
- **色板**：酸性黄 `#F4F000`、纯黑 `#090909`、金属金 `#C89A23`、临床红 `#B53732`。
- **媒介**：棚拍静物 + 编辑拼贴 + 干涩幽默；不是严肃科研 3D。
- **Prompt 核心**：`Create a provocative international business-magazine cover about {industry_tension}. Use one instantly readable visual metaphor: {oversized_symbol} towers over {small_evidence_objects}, while a minimal {domain_anchor} keeps the subject scientifically recognizable. Sharp studio photography, editorial collage, dry humor, high contrast, thumbnail clarity.`
- **避免**：握手、火箭、美元符号、股票曲线、企业大楼。

## Theme 7 — Monocle 理性产业观察风

参考图：`assets/theme-previews/theme7-monocle.png`

- **适用**：产业链、生态系统、研发到临床全景、园区/CDMO/供应链、国际竞争格局。
- **视觉骨架**：等距建筑剖面，把研发、生产、质控、临床和城市生态放入安静场景；标题区融入建筑留白。
- **色板**：暖象牙 `#F2EBD8`、森林绿 `#285541`、砖红 `#A94F3C`、灰蓝 `#7897A4`、芥末黄 `#C7A542`。
- **媒介**：国际事务与设计杂志的建筑编辑插画；小人物只做尺度参照。
- **Prompt 核心**：`Create a refined panoramic editorial illustration of {industry_ecosystem}. Show connected architectural spaces for {module_1}, {module_2}, {module_3}, and {module_4}, with small human figures for scale. Flat geometric forms, precise axonometric perspective, restrained texture, calm intellectual storytelling.`
- **避免**：光滑 3D 实验室、全息 UI、拥挤人物、赛博朋克。

## Theme 8 — 显微纪录摄影风

参考图：`assets/theme-previews/theme8-micro-documentary.png`

- **适用**：递送、细胞结合、病原体与免疫、纳米颗粒、组织微环境、实验发现。
- **视觉骨架**：像一次真实显微发现；主交互精确对焦，其余依靠景深和颗粒感退后；标题放在失焦暗区。
- **色板**：石墨灰 `#5D6366`、深海蓝 `#183747`、银白 `#CCD2D1`、荧光绿 `#36E562`。
- **媒介**：冷冻电镜与超分辨荧光融合的科学纪录摄影。
- **Prompt 核心**：`Create an extraordinary documentary-style microscopic image of {micro_subject} interacting with {target_surface}. Preserve authentic membrane folds, particle scale, fluid suspension, depth of field, and restrained fluorescence at the exact binding site. Observational, credible, and tactile rather than cinematic fantasy.`
- **避免**：尖刺病毒误读、科幻灯光、装饰分子、卡通细胞、假比例尺。

## Theme 9 — Swiss International Style 极简理性海报

参考图：`assets/theme-previews/theme9-swiss-poster.png`

- **适用**：技术关系、二元对照、核心命题、方法论宣言、品牌化研究观点。
- **视觉骨架**：将文章压缩为 2-4 个圆、线和几何符号；严格网格与非对称平衡；后期标题占 35%-50%，成为构图主体。
- **色板**：纸白 `#F4F2EB`、纯黑 `#111111`、钴蓝 `#1749C6`、信号红 `#F01816`。
- **媒介**：1960s 瑞士科学海报、硬边几何、轻微胶印纸张肌理。
- **Prompt 核心**：`Create a rigorous Swiss modernist scientific poster. Reduce {core_relationship} to {shape_a}, {shape_b}, sparse black symbols, and {count} disciplined lines on a modular grid. Strong asymmetric balance, hard-edged geometry, bold negative space, offset-print texture.`
- **避免**：3D 细胞、写实分子、渐变、圆角 UI。

## Theme 10 — 复古科学档案风

参考图：`assets/theme-previews/theme10-science-archive.png`

- **适用**：专利、技术史、机制溯源、工程壁垒、老文献复盘、调查型深度研究。
- **视觉骨架**：专利图、实验笔记、显微照片、工艺草图和红色批注叠成档案拼贴；留出未印刷纸面放标题。
- **色板**：旧纸 `#EAE1CA`、炭黑 `#22201D`、褪色海军蓝 `#23394C`、氧化红 `#A33D2E`、实验绿 `#A9B9A2`。
- **媒介**：1970s 科研档案、丝网印刷、复印噪点、调查新闻气质。
- **Prompt 核心**：`Create an archival scientific collage about {technical_subject}. Layer patent-style line drawings of {core_object}, {connection_detail}, microfluidic plans, laboratory notebook fragments, and one monochrome microscopy plate. Add abstract red editorial marks and registration targets, but no readable writing.`
- **避免**：现代 HUD、光滑 3D、随机报纸、可读专利号。

## Theme 11 — 药物管线地图风

参考图：`assets/theme-previews/theme11-pipeline-map.png`

- **适用**：企业管线、路线竞争、靶点布局、研发阶段、国内外玩家与 BD 格局。
- **视觉骨架**：一个起点分叉为 2-4 条技术路线，经关键平台节点到不同证据终点；中央横带后期叠加标题。
- **色板**：暖灰 `#D8D4CB`、海军蓝 `#123B69`、青绿 `#1B9994`、酒红 `#7B243D`、金色 `#B79949`。
- **媒介**：战略咨询图 + 交通网络设计 + 生物医学切片；清晰但不照搬地铁图。
- **Prompt 核心**：`Create an abstract biopharma pipeline map. Start from {platform_origin}; split into routes for {route_a}, {route_b}, and {route_c}; pass through visual nodes representing {milestones}; end at distinct {evidence_or_product_outcomes}. Use clean transit-like curves, circular nodes, microscopy inserts, and a calm central title band without text.`
- **避免**：公司名、药物编号、国旗、真实地铁地图、拥挤标签。

## Theme 12 — 临床证据蓝皮书风

参考图：`assets/theme-previews/theme12-clinical-evidence.png`

- **适用**：临床数据、疗效安全性、队列比较、剂量递增、医学事务与投资研究。
- **视觉骨架**：中心治疗对象被克制的数据层、样本节点、随访轨迹和显微切片环绕；顶部 20%-25% 作为刊头区。
- **色板**：临床白 `#F4F7F8`、深海军蓝 `#12375C`、冷青 `#72C9CC`、石墨灰 `#52616B`、安全橙 `#FF6B21`。
- **媒介**：国际药企医学蓝皮书 + 高级数据新闻；不是软件 dashboard。
- **Prompt 核心**：`Create a rigorous clinical-evidence cover centered on {therapy_object}. Surround it with sparse cohort dots, dose-response trajectories, follow-up windows, microscopy slices, and translucent evidence planes derived from {key_evidence}. Preserve a generous low-detail masthead zone across the top.`
- **避免**：UI 卡片、传统柱状图、密集坐标、股票感、假数字。

## Theme 13 — Cell 机制图谱风

参考图：`assets/theme-previews/theme13-cell-mechanism.png`

- **适用**：细胞机制、递送链路、信号通路、药物作用机制、多步骤生物过程。
- **视觉骨架**：一幅连续细胞剖面承载完整机制；过程沿空间自然推进，不拆成多个框；标题横跨顶部或底部。
- **色板**：暖白 `#F6F2E8`、海军蓝 `#172945`、膜青 `#9FD3D2`、内体酒红 `#71334B`、RNA 金 `#CF9E43`。
- **媒介**：Cell 风格出版级机制插画，精确线条 + 克制体积阴影。
- **Prompt 核心**：`Create a continuous publication-grade cellular cutaway showing {step_1} -> {step_2} -> {step_3} -> {step_4} -> {outcome}. Integrate every stage into one flowing biological cross-section with accurate membranes, receptors, vesicles, payload, and expressed product. No separate panels.`
- **避免**：教科书卡通、框线面板、复杂标签、错误 DNA/mRNA 结构。

## Theme 14 — 医学大会主视觉风

参考图：`assets/theme-previews/theme14-medical-congress.png`

- **适用**：年度综述、重磅进展、会议总结、临床转化节点、前沿趋势发布。
- **视觉骨架**：粒子或分子汇聚成宏大细胞/器官/治疗对象；从暗到明表现突破；标题压在中央低细节区，底部留窄信息带。
- **色板**：深靛蓝 `#061B44`、医学青 `#48CED0`、冷白 `#F0F8FA`、品红 `#D94A98`。
- **媒介**：国际医学大会主视觉，宏大、有舞台感但保持专业。
- **Prompt 核心**：`Create a major international medical-congress key visual. Thousands of ordered {particles_or_fragments} converge to form {therapeutic_subject}; inside, {payload_path} glows and {clinical_outcome} emerges in the distance. Monumental scale, disciplined particle motion, soft volumetric light, central low-detail title zone.`
- **避免**：真实舞台、演讲者、观众、地球、火箭、能量爆炸。

## Theme 15 — 分子蓝图风

参考图：`assets/theme-previews/theme15-molecular-blueprint.png`

- **适用**：分子设计、抗体结构、脂质配方、连接化学、专利拆解、药物平台原理。
- **视觉骨架**：中央大剖面 + 3-5 个局部放大窗 + 测量线和结构草图；标题沿中心轴放主体上方或下方。
- **色板**：普鲁士蓝 `#06365B`、冰白 `#DCECF0`、结构青 `#3FC7CC`、节点黄 `#E5EA38`。
- **媒介**：建筑蓝图、航天工程图与现代药物化学可视化融合。
- **Prompt 核心**：`Create a precise molecular blueprint of {drug_system}. Center a large cutaway showing {component_1}, {component_2}, {component_3}, and {payload}; add clean magnification windows for {detail_a}, {detail_b}, and {detail_c}; use drafting grids, measurement lines, and icy technical linework.`
- **避免**：可读化学式、尺寸数字、专利号、科幻 HUD。

## Theme 16 — 生物工艺工程风

参考图：`assets/theme-previews/theme16-bioprocess.png`

- **适用**：CMC、工艺开发、放大生产、偶联、TFF、纯化、灌装、质量控制、CDMO。
- **视觉骨架**：真实连续产线从原料/成粒到反应、TFF、过滤和成品；流程占左中区域，右侧竖栏或顶部低细节区放标题。
- **色板**：洁净白 `#EAF1F2`、钛银 `#9EACB1`、冷蓝 `#79B2C5`、深青 `#164B68`、琥珀 `#B37A28`。
- **媒介**：国际生物制药工厂摄影 + 高级工业设计可视化；设备和管路必须可信。
- **Prompt 核心**：`Create a realistic biopharmaceutical process-engineering cover showing a continuous line from {input_materials} through {formation_step}, {conjugation_step}, {purification_step}, {filtration_or_fill_step}, and {final_product}. Use credible stainless-steel equipment, transparent process tubing, controlled fluid colors, cleanroom lighting, and a restrained title sidebar.`
- **避免**：未来全息工厂、错误设备连接、夸张防护服人物、试管堆、假设备标签。

## 通用 Negative prompt

`Negative prompt: readable text, fake typography, gibberish, letters, numbers, logos, signatures, watermarks, platform marks, low resolution, accidental cropping of the main subject, crowded composition, generic stock illustration, unrelated DNA helix, syringe cliché, medical misinformation`
