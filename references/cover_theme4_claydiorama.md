---
name: cover_theme4_claydiorama
description: >
  主题四：生物医学粘土微缩剖面风。适用于细胞机制、递送链路、内吞与内涵体逃逸、
  药物作用过程及 3-7 步生物学机制。用手工软陶搭建血管、细胞膜、细胞器、受体和载荷，
  以连续剖面取代旧版圆台展柜与可爱角色方案。
---

# 主题四：生物医学粘土微缩剖面风

参考图：`assets/theme-previews/theme4-clay-diorama.png`

## 0. 风格定位

| 维度 | 设定 |
| --- | --- |
| 视觉调性 | 亲切、可触摸、机制清楚、像博物馆里的生物学微缩模型 |
| 画幅比例 | 约 2.35:1 横版，首选 1584x672 或 1260x540 |
| 核心工艺 | Polymer clay / plasticine 手工软陶，微距棚拍，真实指纹和捏塑痕迹 |
| 适用场景 | 细胞递送、受体结合、内吞、内涵体逃逸、RNA 翻译、药物机制、多阶段生物过程 |
| 不适用场景 | 资本交易、公司管线、严肃临床数据、纯产业格局、无生物结构的通用 Setup 指南 |

## 1. 视觉骨架

- 使用一个连续的生物医学剖面，而不是多个圆台或独立卡片。
- 将血管或组织通道置于上方/左上，将目标细胞膜的大型剖面置于右侧。
- 用 3-7 个空间节点表现机制：循环 → 结合 → 内吞 → 内体 → 逃逸 → 翻译 → 表型结果。
- 细胞膜必须有可辨认的脂质双层；细胞器、RNA、受体和颗粒均使用软陶材质，但结构关系要科学可信。
- 左侧可自然留出浅色桌面负空间，也可把标题放在顶部；不要强制所有封面左文右图。

## 2. 色板与材质

| 角色 | 色值 | 用途 |
| --- | --- | --- |
| 奶油背景 | `#F4E5CD` | 桌面与低细节标题区 |
| 组织陶土 | `#A84F4B` | 血管、细胞质、膜外结构 |
| 膜脂米黄 | `#E8C88C` | 脂质双层 |
| 蛋白青绿 | `#3E9E9A` | 受体、酶、核糖体 |
| 载荷金黄 | `#E8B52E` | RNA 与关键转化结果 |
| 内体酒红 | `#733848` | 内吞囊泡和内涵体 |
| 连接深蓝 | `#214B78` | 受体末端和信号节点 |

材质必须是哑光手捏软陶：轻微指纹、压痕、边缘不完全规则；使用柔和接触阴影和浅景深。禁止金属、玻璃、光滑 PBR 塑料和扁平矢量。

## 3. 内容 Schema

| 占位符 | 规则 |
| --- | --- |
| `{core_process}` | 一句话说明完整生物过程 |
| `{carrier}` | 递送载体或起始对象 |
| `{target}` | 靶细胞、受体或组织 |
| `{step_1..7}` | 3-7 个可视化步骤，每项只描述动作与对象 |
| `{payload}` | RNA、蛋白、药物或其他载荷 |
| `{outcome}` | 最终表达、清除、修复或治疗结果 |
| `{title_zone}` | fixed left tabletop field, 7%-43% canvas width and 23%-67% canvas height; keep it as untextured cream clay tabletop with only a thin hand-pressed clay rule |

## 4. Prompt 模板

```text
Create a finished WeChat Official Account cover at 2.35:1 aspect ratio (prefer 1584x672), using a handcrafted biomedical polymer-clay diorama to explain {core_process}.

Build one continuous cutaway scene, not separate cards. Show {carrier} moving through a clay blood vessel or tissue channel, interacting with {target}, then progressing spatially through {step_1}, {step_2}, {step_3}, {step_4}, {step_5}, {step_6}, and {step_7}. Inside the cell, show {payload} as a distinct hand-shaped clay strand and end with {outcome}. Preserve scientifically coherent membranes, receptors, vesicles, organelles, and direction of travel.

Everything must look physically hand-sculpted from matte polymer clay: visible fingerprints, slightly imperfect edges, tactile lipid bilayers, soft studio lighting, gentle contact shadows, macro tabletop photography, shallow but controlled depth of field. Use cream, terracotta, burgundy, teal, mustard yellow, and deep blue. Reserve {title_zone} as a quiet cream tabletop plane bounded only by a thin hand-pressed deep-blue clay rule; do not place cells, particles, receptor clusters, shadows, or strong texture there. The artwork must visibly flow around and toward this title plane.

No generated text. No labels, letters, numbers, logos, signatures, watermarks, or platform marks.

Negative prompt: round display pedestals, cute mascot faces, children's toy packaging, generic setup guide, flat vector, 2D cartoon, glossy plastic, metallic surfaces, glass, photorealistic wet tissue, gore, inaccurate cell anatomy, spiked virus cliché, readable text, fake typography, watermark, crowded composition
```

只有 3-5 步时删除多余步骤句，不得留下占位符。

## 5. 标题构图与文字策略

- **固定标题区**：左侧桌面字段，`x=7%-43%`、`y=23%-67%`。不得用半透明色块覆盖图像；标题直接印在预留的奶油软陶桌面上。
- **字形语气**：使用圆润但克制的无衬线粗体；深蓝主标题，陶土红小标题，像博物馆标本卡上的印刷信息，而非软件面板。
- **融合装置**：一条轻微手压痕的深蓝细线与标题左缘对齐；只有该线和小色点可作为装饰，不能加入矩形卡片。
- 默认生成无字底图，并在该标题字段后期叠加中文标题。
- 不在模型内生成机制标签；若用户需要标签，单独输出文字清单给排版工具。
- 重要结构放在中央 60% 垂直安全区，防止微信裁切。
- 平台强制水印无法通过 negative prompt 消除；将带水印结果标为预览稿。

## 6. 失败回退

| 现象 | 修正 |
| --- | --- |
| 变回旧版圆台展柜 | 追加 `one continuous cellular cutaway, no pedestals, no separate modules` |
| 过于儿童化 | 追加 `museum-quality biomedical model, no faces, no toy packaging` |
| 变成写实湿润组织 | 追加 `dry matte polymer clay, visible hand-sculpted texture, no biological wetness` |
| 机制不连贯 | 把步骤缩减到 3-5 个，并明确每一步的空间位置与动作 |
| 出现乱码 | 删除所有文字要求，保留 quiet zone 后期排版 |
