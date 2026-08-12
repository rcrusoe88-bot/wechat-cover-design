---
name: cover_theme1_academic
description: >
  主题一：学术机制图风（Academic Mechanism Diagram）。
  适用场景：机制解析、概念逻辑链、技术原理拆解类内容。
  视觉语言：纯白背景 + 5 色科学配色 + 三栏布局（文字信息区 / 概念逻辑链 / 核心对象复合体）。
  与其它主题区分：信息密度最高、最克制专业；不用于认知转变叙事、不用于震撼大发现、不用于多步骤流程。
---

# 主题一：学术机制图风 — 文生图 prompt 设计规格

参考来源：植生笔记公众号封面设计风格（学术期刊配图审美）
适用比例：21:9（≈ 微信 2.35:1）横版，推荐渲染尺寸 1260 × 540px

---

## 0. 设计哲学

学术机制图风的核心是「克制」——去掉所有非必要的装饰，让核心对象本身的形态和色彩成为视觉焦点。参考 Nature/Cell 系列期刊的图注风格：纯白背景、矢量有机形状、固定 5 色科学配色系统、细线箭头、无阴影无描边框。

读者一眼看到封面，应该感受到「这是一篇有数据支撑的专业内容」，而不是「这是一张精心设计的海报」。

本主题的「机制」不限于生物机制：AI 模型的架构链路、数据流管线、算法逻辑链同样适用（见「内容映射规则」的 AI/科技示例）。

---

## 1. 色彩系统（固定，不随文章调整）

这 5 色覆盖暖冷中性色调，搭配协调且具有识别度：

| 色号 | 色值 | 用途 |
|------|------|------|
| 玫瑰粉 | `#BD7C78` | 主要核心对象 A、信号/主路径对象 |
| 天蓝 | `#B0D7E9` | 受体、通道、效应对象（第二层级对象） |
| 紫 | `#7767A1` | 复合体核心对象、调控对象 |
| 金 | `#D9BE67` | 配体、小分子、构成单元、活性分子 |
| 绿 | `#62B187` | 正向信号对象、激活型效应对象 |
| 主文字 | `#2C2C2C` | 全局正文、标题 |
| 次要标注 | `#555555` | 节点标注 |
| 分割线 | `#C8C8C8` | 区域分隔细线 |
| 正向标签背景 | `#EAF4EC` | 正向结果标签（如 "Enhanced"） |
| 正向标签文字 | `#2E7D52` | — |
| 警示标签背景 | `#FDECEA` | 警示结果标签（如 "Failure"） |
| 警示标签文字 | `#C0392B` | — |

**prompt 中必须明确写出这些色值**，不允许引入色系外颜色。

---

## 2. 三栏布局描述规范

prompt 中需要用自然语言精确描述三栏布局：

### 左栏（30%宽度）— 文字信息区
- 顶部：来源标注（机构/期刊名 + 年份，斜体灰色小字）
- 中部：文章主标题（大字加粗，2-3 行）
- 底部：核心结论副标题（灰色小字）
- 最底：5 色色板圆形横排展示

### 中栏（45%宽度）— 概念逻辑链图区
- 3-5 个有机 Blob 形状节点（代表核心对象/实体节点）
- 箭头连接（实心三角箭头，灰色细线）
- 虚线箭头表示推测/假设步骤
- 节点下方小字标注名称
- 末端可有标签盒（绿底正向 / 红底负向）

### 右栏（25%宽度）— 核心对象复合体展示区
- 3-4 色叠压有机 Blob 复合体（中心对象的组合形态）
- 对象名称标签
- 底部公众号名灰色小字

---

## 3. 关键视觉元素描述词汇

在 prompt 中描述以下元素时，使用对应的英文关键词：

| 元素 | prompt 描述关键词 |
|------|------------------|
| 核心对象节点 | "organic blob shape, smooth Bézier curves, no outline stroke, overlapping layers" |
| 小型构成单元 | "irregular hexagon, thin purple stroke, light fill, small structural unit" |
| 实心箭头 | "thin gray arrow with solid triangle arrowhead, clean vector line" |
| 虚线箭头 | "dashed arrow, stroke-dasharray pattern, indicating hypothetical step" |
| 标签盒 | "small rounded-rect tag box, colored background, short text label" |
| 色板 | "row of 5 small colored circles, palette swatch display" |
| 核心对象复合体 | "layered organic blob complex, 3-4 overlapping colored shapes, no borders" |

---

## 4. 禁止项（必须写入 negative prompt）

- 渐变背景（径向渐变、线性渐变）
- 阴影效果（drop shadow、box-shadow）
- Blob 上的描边轮廓
- 色系外颜色
- 装饰性几何图形（圆圈、三角、矩形背景块）
- 手写字体或粗装饰字体
- 3D 渲染、照片级写实
- 暗色背景、霓虹色
- 水印

## 4.1 文本与平台回退

- 主标题和关键结论可以要求 `Chinese text exactly: "..."`，但应保持短句并放在安全区。
- 节点标签、来源和品牌名属于小字；尽量控制为 4–6 个汉字或使用英文缩写。
- 需要准确显示的密集标签应留出空白区域，交由宿主的排版/图像编辑能力后期叠加。没有后期能力时，将其作为独立文字清单交付，不要承诺模型会准确渲染。
- `watermark` 只约束视觉内容。宿主或图像服务强制添加的平台水印无法可靠地通过 negative prompt 去除；带此类水印的结果应标记为预览稿。

---

## 5. Prompt 构建模板

组装 prompt 时，按以下顺序组织内容：

1. **画幅与比例**：开头明确 21:9 比例和尺寸
2. **整体风格**：学术期刊机制图、白底、矢量插画
3. **三栏布局描述**：左-中-右，每栏内容
4. **色彩指定**：5 色色值 + 文字色 + 标签色
5. **视觉元素细节**：Blob 形状、箭头、标签盒等
6. **字体提示**：Noto Sans SC、学术感
7. **Negative prompt**：排除不想要的风格

---

## 6. 内容映射规则

| 文章元素 | 通用对象角色 | prompt 中的表达 |
|---------|-------------|----------------|
| 核心对象 A（主体） | 右栏复合体主体，主色（玫瑰粉/紫） | 有机 Blob 复合体 |
| 核心对象 B（次主体） | 右栏叠压层，次色（天蓝/绿） | 叠压有机 Blob |
| 辅助构成单元 | 右栏最小结构域，金色 | 不规则六边形小单元 |
| 概念逻辑链起点→终点 | 中栏逻辑链，3-5 节点线性或分叉 | 箭头连接节点图 |
| 最重要数据 | 左栏副标题直接呈现（如「效率提升 8.3 倍」） | 灰色小字副标题 |
| 来源机构/期刊 | 左栏顶部来源标注，斜体 | 斜体灰色小字 |
| 正向/负向结论 | 中栏末端标签盒（绿底正向/红底负向） | 圆角标签盒 |

### 双领域填充示例

**生物医药示例**：核心对象 = LNP 递送载体、T 细胞受体；逻辑链 = "LNP uptake → endosomal escape → cargo release"；最重要数据 = "脾脏摄取提升 80 倍"；来源 = "AtomBio 2026"。

**AI/科技示例**：核心对象 = Transformer 模型组件、MoE 路由层；逻辑链 = "token 嵌入 → 注意力计算 → 稀疏路由 → 输出"；最重要数据 = "推理成本下降 7×"；来源 = "某实验室 2026"。

---

## 7. Prompt 模板（21:9 横版，英文可直接喂 DALL-E / Midjourney / Gemini）

> 使用方法：将 `{}` 替换为对应内容后，直接作为文生图 prompt 使用。四套主题统一 21:9（≈ 微信标准 2.35:1 / 900×383），推荐渲染尺寸 1260 × 540px。

```
A horizontal banner image at 21:9 aspect ratio (1260x540px), academic journal mechanism diagram style, clean white background (#FFFFFF), no texture, no gradient.

The composition uses a three-column layout:

LEFT COLUMN (30% width): A text information area. At the top, a small italic source citation in gray (#555555) reading "{作者/机构} et al. {来源} {年份}". Below it, the article title "{文章标题}" in large bold black text (#2C2C2C), 2-3 lines, using Noto Sans SC font. Under the title, a one-line subtitle in smaller gray text (#444444) stating the key conclusion: "{关键结论}". At the very bottom, a row of 5 small colored circles (28x28px each, 6px apart) showing the color palette: rose pink (#BD7C78), sky blue (#B0D7E9), purple (#7767A1), gold (#D9BE67), green (#62B187).

CENTER COLUMN (45% width): A simplified conceptual flow diagram. Three to five core-entity nodes are arranged left-to-right (or in a Y-branch), connected by thin gray arrows (stroke #777777, 1.5px, solid triangle arrowhead). Each node is an organic blob shape (smooth Bézier curves, no stroke outline) filled with one of the 5 palette colors. The nodes represent: {节点A名称}, {节点B名称}, {节点C名称}. Small 11px gray labels sit below each node. Small constituent sub-units are shown as irregular hexagons with thin purple (#7767A1) stroke and light fill. Dashed arrows (stroke-dasharray: 4 3) indicate hypothetical steps. Small tag boxes with rounded corners appear at pathway endpoints: green background (#EAF4EC) with green text (#2E7D52) for positive outcomes, or red-tinged background (#FDECEA) with red text (#C0392B) for negative outcomes.

RIGHT COLUMN (25% width): A large core-object complex illustration made of 3-4 overlapping organic blob shapes (smooth Bézier curves, no outlines), layered on top of each other with 10-20% overlap. Colors from the 5-palette system: base layer sky blue (#B0D7E9), middle layer rose pink (#BD7C78), top layer purple (#7767A1), small accent gold (#D9BE67). The overall structure is roughly 180x220px, centered. A bold 16px label "{核心对象名称}" sits near the top corner. At the bottom right, a small 12px gray text "{公众号名称}".

STYLE: Academic journal figure aesthetic (Nature/Cell supplementary illustration standard). No shadows, no decorative borders, no gradients, no hand-drawn texture. Everything is crisp, clean vector-style illustration. The 5-color scientific palette is used consistently throughout. A thin 1px gray (#C8C8C8) horizontal divider line may separate flow tiers in the center column.

Negative prompt: gradient background, drop shadow, decorative border, hand-drawn texture, 3D render, photorealistic, noisy, cluttered, dark background, neon colors, cartoon style, watermark
```

---

## 8. 失败回退

| 现象 | 处理 |
| --- | --- |
| 生成结果出现阴影/渐变 | 强化 negative prompt：`no shadow, no gradient, no depth` |
| 引入色系外颜色 | 强调 `color palette strictly limited to the 5 listed hex values` |
| 变成信息图/海报风 | 追加 `no infographic cards, no dashboard layout, pure scientific diagram` |
| 文字乱码 | 中文标签加引号包裹，并在 prompt 前置 `Chinese text labels exactly: "..."` |
