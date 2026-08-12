---
name: theme_registry
description: >
  主题注册表（唯一常驻上下文入口）。维护 wechat-cover-design 全部封面主题的索引、
  文章类型→主题匹配规则，以及「如何新增主题」四步法。完整主题规格按需 Read 对应文件。
---

# 主题注册表

本文件是 `wechat-cover-design` 的常驻上下文。SKILL.md 通过本表引用主题，具体主题规格文件按需 `Read`，避免一次性加载全部主题导致上下文膨胀。

## 主题索引

| 主题ID | 主题名 | reference 文件 | 触发场景 | 内容 schema 核心 |
|--------|--------|----------------|----------|------------------|
| theme1 | 学术机制图风 | references/cover_theme1_academic.md | 机制解析 / 概念逻辑链 / 技术原理拆解 | 核心对象链 3-5 节点 + 中心对象复合体 |
| theme2 | 手绘信息图风 | references/cover_theme2_handdrawn.md | 认知转变（从X到Y）/ 痛点-解方 / 技术对比 | 问题对象 + 解决对象 + 对比数据 |
| theme3 | 顶刊科研封面风 | references/cover_theme3_journal.md | 重大发现 / 深度解读 / 强视觉冲击 | 1 个视觉隐喻 + 2-3 个领域锚点 + 色彩主题词 |
| theme4 | 粘土泥塑微缩风 | references/cover_theme4_claydiorama.md | 多步骤方法论 / Setup 指南 / 多模块并列 | 3-5 个模块（小标签 / 图标 / 配文）|

## 文章类型 → 主题匹配速查

| 文章类型 | 推荐主题 | 一句话理由 |
|----------|----------|-----------|
| 机制解析 / 概念逻辑链 | theme1 | 白底三栏，专业克制，讲清复杂链路 |
| 认知转变 / 痛点-解方 / 技术对比 | theme2 | 暖米纸感 + 对比数据，亲切有温度 |
| 重大发现 / 深度解读 | theme3 | 暗色发光主体，视觉隐喻，一眼震撼 |
| 多步骤方法论 / Setup 指南 | theme4 | 圆台底座一字排开，治愈系展柜 |
| 行业趋势 / 观点判断 | theme3 或扩展主题 | 可用「行业洞察风」扩展种子（extension_theme_examples.md） |

匹配规则：若两个候选主题都成立，各给一句话理由让用户二选一；用户指定则直接采用；否定后重新匹配，不重复推荐已否主题。

## 全部主题规格文件

| 文件 | 内容 |
|------|------|
| references/_theme_template.md | 新增主题的标准脚手架模板（复制改名后填写） |
| references/cover_theme{1..4}_*.md | 各主题完整规格（设计哲学/色板/布局/词汇/禁止项/prompt 模板/内容映射/回退） |
| references/extension_theme_examples.md | 扩展主题种子：AI哲学风、行业洞察风（未启用，供新增主题参考） |

---

## 如何新增主题（四步法）

用户或主 Agent 想加入新封面风格时，按以下四步操作：

**① 复制脚手架并填写**
```bash
cp .claude/skills/wechat-cover-design/references/_theme_template.md \
   .claude/skills/wechat-cover-design/references/cover_theme5_你的主题.md
```
按模板的 8 章节填写。**视觉骨架必须包含色板色值 + negative prompt**（这是主题可运行性的底线）。

**② 注册表加行**
在本文档「主题索引」表追加一行（主题ID / 主题名 / reference 文件 / 触发场景 / 内容 schema 核心）。

**③ 更新匹配规则（按需）**
若新主题需要更强的自动匹配，更新 SKILL.md Step 2 的类型规则与触发词。新主题通常**不需要**改 SKILL.md frontmatter（避免常驻上下文膨胀）。

**④ 实测**
用一篇真实文章跑一次「主题 → 填占位符 → 输出英文 prompt → validate-prompt.sh」，确认无残留 `{}`、可运行；可把该用例写入 `evals/theme_match_eval.json` 做回归。
