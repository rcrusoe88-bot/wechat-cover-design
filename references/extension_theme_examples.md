---
name: extension_theme_examples
description: >
  扩展主题种子库。从 wechat-title-summary 废弃的 image-prompts.md 提炼的 AI哲学风、行业洞察风，
  标注「未启用」。新增主题时的参考种子：可直接复制为 cover_themeN_xxx.md 启用。
---

# 扩展主题种子（未启用）

> 本文件收录从旧版 `image-prompts.md` 提炼的两个完整风格种子。它们**当前未启用**（不在 theme_registry.md 注册表中），
> 当用户希望新增主题时可复制本文件对应章节为 `cover_themeN_xxx.md` 启用（参照「如何新增主题」四步法）。
>
> 另有旧版「学术科学风」≈ 现主题一（学术机制图风），已覆盖，不再单独收录。

---

## 种子 A：AI 哲学风（Suprematist AI）— 未启用

**适用场景**：AI 技术应用、算法设计、人工智能与生命科学交叉类文章；偏"智能涌现/未来感"调性。

**视觉语言**：至上主义几何抽象 × 神经网络涌现感
- 深靛蓝色底面 `#0D1B2A`：未被探索的认知空间
- 发光几何节点：智能涌现/激活信号
- 边缘有机曲线：生物性与数字性的交界

**色彩系统**：
| 角色 | 色值 | 用途 |
| --- | --- | --- |
| 背景 | `#0D1B2A` | 深普鲁士蓝地面 |
| 节点发光 | 白 / 电光蓝 | 智能节点 |
| 强调 | 暖琥珀 | 信号焦点 |

**Prompt 模板（21:9 横版）**：
```
Suprematist geometric abstraction, deep prussian blue ground (#0D1B2A). Luminous white and electric cerulean geometric primitives — precise circles, orthogonal grids, thin radial lines — self-organizing into emergent lattice structures that suggest neural activation. Scattered warm amber accent nodes mark signal focal points. Style references: Malevich Suprematism, scientific connectome visualization, Mondrian rational composition. Subject context: [从文章核心提炼的场景词]. No text, no labels. High contrast, meditative precision. Faint biological organic curves dissolve at periphery, suggesting the boundary between digital logic and living systems. --ar 21:9 --style raw

Negative prompt: ...
```

**启用方式**：复制本节为 `cover_theme5_ai_suprematist.md`，补全「内容映射规则」「失败回退」等章节，再在 theme_registry.md 注册。

---

## 种子 B：行业洞察风（Editorial Shanshui）— 未启用

**适用场景**：行业趋势分析、竞争格局、会议综述、战略判断类文章。

**视觉语言**：中国山水画意境 × 当代编辑插画
- 水墨晕染底面：行业格局的模糊与清晰
- 层叠等高线地图：市场地形/赛道格局
- 俯瞰视角的孤独观察者：洞察者的战略高度
- 克制配色：墨黑 + 象牙白 + 深锈红点缀

**色彩系统**：
| 角色 | 色值 | 用途 |
| --- | --- | --- |
| 背景 | `#C8C8B8` / `#F5F0E8` | 淡石青 / 陈纸象牙白 |
| 主文字 | `#2C2C2C` | 墨黑 |
| 强调 | `#8B3A2A` | 单一深锈红 |

**Prompt 模板（21:9 横版）**：
```
Contemporary editorial illustration fusing Chinese ink landscape (shanshui painting) with modern data cartography. Muted ink-wash background in pale slate (#C8C8B8) and aged paper ivory (#F5F0E8). Layered topographic contour lines form an abstract terrain — valleys of uncertainty, ridgelines of emerging clarity — suggesting [从文章提炼的行业主题]. A solitary figure at an elevated vantage point observes the full landscape below. Style references: New Yorker editorial illustration, Song Dynasty landscape scroll (宋代山水), Nikkei Asian Review cover art. Restrained palette: charcoal ink (#2C2C2C), ivory (#F5F0E8), single deep rust red accent (#8B3A2A). Generous negative space. No decorative fills, no photorealism. Contemplative, long-view, strategic mood. --ar 21:9 --style raw

Negative prompt: ...
```

**启用方式**：同上。

---

## 启用种子时的通用提示

1. 补齐视觉骨架：色板色值（上表）+ negative prompt（可从主题三/主题二借鉴通用负向词：`flat vector, cartoon, white background, neon, cluttered, watermark` 等）。
2. 在 theme_registry.md 注册表加行，更新 SKILL.md Step 2 匹配规则。
3. 用真实文章实测 + 写入 evals/theme_match_eval.json。
