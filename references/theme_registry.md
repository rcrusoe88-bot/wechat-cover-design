---
name: theme_registry
description: >
  主题注册表（唯一常驻上下文入口）。维护 wechat-cover-design 全部封面主题的索引、
  文章类型→主题匹配规则，以及「如何新增主题」四步法。完整主题规格按需 Read 对应文件。
---

# 主题注册表

本文件是 `wechat-cover-design` 的主题选择入口。SKILL.md 通过本表引用主题，具体主题规格文件按需读取，避免一次性加载全部主题导致上下文膨胀。

## 主题索引

| 主题ID | 主题名 | reference 文件 | 触发场景 | 内容 schema 核心 |
|--------|--------|----------------|----------|------------------|
| theme1 | 学术机制图风 | references/cover_theme1_academic.md | 机制解析 / 概念逻辑链 / 技术原理拆解 | 核心对象链 3-5 节点 + 中心对象复合体 |
| theme2 | 手绘信息图风 | references/cover_theme2_handdrawn.md | 认知转变（从X到Y）/ 痛点-解方 / 技术对比 | 问题对象 + 解决对象 + 对比数据 |
| theme3 | 顶刊科研封面风 | references/cover_theme3_journal.md | 重大发现 / 深度解读 / 强视觉冲击 | 1 个视觉隐喻 + 2-3 个领域锚点 + 色彩主题词 |
| theme4 | 生物医学粘土微缩剖面风 | references/cover_theme4_claydiorama.md | 细胞机制 / 递送链路 / 内吞与胞内过程 | 连续生物剖面中的 3-7 个空间步骤 |
| theme5 | Nature 科学意象风 | references/cover_themes5_16_selected.md | 重大突破 / 单一核心发现 / 平台发布 | 1 个宏大主体 + 1 个关键交互 |
| theme6 | Businessweek 商业隐喻风 | references/cover_themes5_16_selected.md | 估值 / 交易 / 商业争议 / 资本错配 | 1 个夸张比喻 + 小证据对象 |
| theme7 | Monocle 理性产业观察风 | references/cover_themes5_16_selected.md | 产业链 / 生态系统 / 研发到临床全景 | 4-6 个产业空间模块 |
| theme8 | 显微纪录摄影风 | references/cover_themes5_16_selected.md | 细胞结合 / 纳米递送 / 组织微环境 | 1 个真实微观交互 + 景深 |
| theme9 | Swiss 极简理性海报 | references/cover_themes5_16_selected.md | 核心命题 / 二元关系 / 方法宣言 | 2-4 个几何对象 + 严格网格 |
| theme10 | 复古科学档案风 | references/cover_themes5_16_selected.md | 专利 / 技术史 / 工程壁垒 / 调查研究 | 专利图 + 笔记 + 显微资料 |
| theme11 | 药物管线地图风 | references/cover_themes5_16_selected.md | 企业管线 / 路线竞争 / 研发阶段 | 起点 + 2-4 路线 + 证据终点 |
| theme12 | 临床证据蓝皮书风 | references/cover_themes5_16_selected.md | 临床数据 / 疗效安全性 / 队列比较 | 治疗主体 + 稀疏证据层 |
| theme13 | Cell 机制图谱风 | references/cover_themes5_16_selected.md | 细胞机制 / 递送链路 / 信号通路 | 连续剖面中的 4-7 步过程 |
| theme14 | 医学大会主视觉风 | references/cover_themes5_16_selected.md | 年度综述 / 会议总结 / 临床转化 | 粒子汇聚主体 + 突破结果 |
| theme15 | 分子蓝图风 | references/cover_themes5_16_selected.md | 分子设计 / 连接化学 / 配方拆解 | 中央剖面 + 3-5 放大窗 |
| theme16 | 生物工艺工程风 | references/cover_themes5_16_selected.md | CMC / 工艺放大 / TFF / 质控 | 连续生产线 + 成品 |

## 文章类型 → 主题匹配速查

| 文章类型 | 推荐主题 | 一句话理由 |
|----------|----------|-----------|
| 机制解析 / 概念逻辑链 | theme1 | 白底三栏，专业克制，讲清复杂链路 |
| 认知转变 / 痛点-解方 / 技术对比 | theme2 | 暖米纸感 + 对比数据，亲切有温度 |
| 重大发现 / 深度解读 | theme3 | 暗色发光主体，视觉隐喻，一眼震撼 |
| 生物机制 / 递送链路的亲和科普 | theme4 | 手工粘土连续剖面兼顾机制完整性与亲和感 |
| 行业趋势 / 观点判断 | theme3（默认）或扩展主题 | 默认用单一视觉隐喻；只有用户需要不同编辑体系时才读取扩展种子 |
| 重大科学突破 / 平台发布 | theme5 | 宏大单体科学意象比常规机制图更有封面冲击力 |
| 估值、交易与证据错配 | theme6 | 商业杂志式比喻能在三秒内表达尖锐判断 |
| 产业链 / 研发生产临床生态 | theme7 | 轴测场景可容纳多个产业模块且保持理性秩序 |
| 微观结合 / 纳米递送 / 细胞表面事件 | theme8 | 纪录式显微摄影强调真实性与尺度感 |
| 核心命题 / 二元技术关系 | theme9 | 极简几何适合把复杂文章压缩成一个关系 |
| 专利 / 技术史 / 工程壁垒 | theme10 | 科学档案拼贴带来溯源与调查感 |
| 管线 / 技术路线 / 企业竞争 | theme11 | 路线地图最适合展示分叉、里程碑与终点 |
| 临床证据 / 疗效安全性 / 队列 | theme12 | 蓝皮书视觉同时容纳治疗主体与证据层 |
| 细胞机制 / 信号通路 | theme13 | 连续生物剖面比卡片式流程更接近出版级机制图 |
| 年度综述 / 医学会议 / 转化里程碑 | theme14 | 宏大主视觉适合重磅总结与趋势发布 |
| 分子结构 / 偶联 / 配方 / 专利拆解 | theme15 | 蓝图语言突出结构、连接与工程精度 |
| CMC / 工艺放大 / 纯化 / 质量控制 | theme16 | 真实连续产线能直接传达可制造性 |

匹配规则：若两个候选主题都成立，各给一句话理由让用户二选一；用户指定则直接采用；否定后重新匹配，不重复推荐已否主题。

## 全部主题规格文件

| 文件 | 内容 |
|------|------|
| references/_theme_template.md | 新增主题的标准脚手架模板（复制改名后填写） |
| references/cover_theme{1..4}_*.md | 原有主题一至三，以及已替换的主题四生物医学粘土微缩剖面规格 |
| references/cover_themes5_16_selected.md | 用户选定的十二套扩展主题规格、Prompt 核心与禁止项 |
| references/extension_theme_examples.md | 扩展主题种子：AI哲学风、行业洞察风（未启用，供新增主题参考） |

---

## 如何新增主题（四步法）

用户或主 Agent 想加入新封面风格时，按以下四步操作：

**① 复制脚手架并填写**

从本 skill 目录复制 `references/_theme_template.md` 为新的 `cover_themeN_name.md`。按模板填写。**视觉骨架必须包含色板色值 + negative prompt**，并提供中文小字和平台水印的回退策略。

**② 注册表加行**
在本文档「主题索引」表追加一行（主题ID / 主题名 / reference 文件 / 触发场景 / 内容 schema 核心）。

**③ 更新匹配规则（按需）**
若新主题需要更强的自动匹配，更新 SKILL.md Step 2 的类型规则与触发词。新主题通常**不需要**改 SKILL.md frontmatter（避免常驻上下文膨胀）。

**④ 实测**
用一篇真实文章跑一次「主题 → 填占位符 → 输出英文 prompt → validate_prompt.py」，确认无残留 `{}`、可运行；可把该用例写入 `evals/theme_match_eval.json` 做回归。
