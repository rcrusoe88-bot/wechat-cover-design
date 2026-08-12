---
name: cover_theme2_handdrawn
description: >
  主题二：手绘信息图风（Hand-drawn Infographic）。
  适用场景：认知转变（从X到Y）、痛点-解方叙事、技术对比类内容。
  视觉语言：暖米色纸质感 + 手绘插画 + 「问题→解决」双模块对比 + 关键数据柱状图。
  与其它主题区分：有温度、允许装饰元素（感叹号/星形/箭头），不用于深机制解析、不用于震撼大发现。
---

# 主题二：手绘信息图风 — 文生图 prompt 设计规格

参考来源：Au-LNP 机制解析横版信息图（NotebookLM 风格手绘科普插画）
适用比例：21:9（≈ 微信 2.35:1）横版，推荐渲染尺寸 1260 × 540px

---

## 0. 设计哲学

手绘信息图风的核心是「温度感」——用手绘质感消解学术内容的距离感，让读者在看到封面的瞬间感受到「有人在认真给我解释一件复杂的事」。

与主题一的「克制」不同，手绘风允许装饰性元素的存在（感叹号、星形、尺子图标），但每一个元素都应承担叙事功能——感叹号强调痛点，星形标记关键数据，箭头引导视线流动。

适用场景：「从X到Y」的认知转变、「为什么原来的方法不够好」的痛点-解方叙事、含有对比数据的机制类文章。X/Y 不限于技术：旧方法→新方法、被动等待→主动设计、单点模型→系统能力，均可。

---

## 1. 色彩系统

| 角色 | 色值 | 用途 |
|------|------|------|
| 全局背景 | `#F7EDD6` | 暖米色纸质感，模拟牛皮纸/素描本底色 |
| 标题栏背景 | `#FFF8C0` | 黄色便利贴感 |
| 标题栏边框 | `#6BA8D4` | 蓝色手绘描边 2.5px |
| 左模块背景 | `#D4EDDA` | 薄荷绿，暗示「问题」区域（冷色调） |
| 左模块边框 | `#5C9E6B` | 中绿描边 2.5px |
| 右模块背景 | `#FFF3E0` | 暖橙白，暗示「解决」区域（暖色调） |
| 右模块边框 | `#E8872A` | 橙色描边 2.5px |
| 主文字 | `#2B1810` | 深棕黑，比纯黑更柔和 |
| 次要文字 | `#5A4030` | 中棕，用于图注和说明 |
| 强调红 | `#E03030` | 感叹号、警示数字、痛点数据 |
| 强调蓝 | `#4A7FC0` | 箭头、灯泡图标、正向引导 |
| 强调绿 | `#5CA86A` | 结论性箭头、正向结果标注 |
| 数据柱（蓝） | `#7BACD4` | 柱状图对照组 |
| 数据柱（橙） | `#F09050` | 柱状图实验组（高值） |
| 星形填充 | `#FFDA00` | 4 角星，高亮关键节点 |
| 星形描边 | `#000000` | 1.5px |

---

## 2. 布局描述规范

prompt 中需要用自然语言精确描述两区域布局：

### 顶部标题栏（15%高度）
- 黄色便利贴感背景（#FFF8C0）+ 蓝色手绘边框（#6BA8D4）
- 左侧：主标题（Ma Shan Zheng 手写风格大字，32px，深棕黑）
- 右侧：黄色小框内副标题（18px）
- 整体轻微倾斜（-0.3 度），增加手绘随意感

### 左侧问题模块（42%宽度）
- 薄荷绿卡片（#D4EDDA）+ 绿色手绘边框（#5C9E6B）
- 轻微倾斜（-0.5 度）+ 纸质阴影
- 内含：模块标题 + 圆形图示（核心问题对象）+ 红色强调数据 + 标注文字

### 右侧解决模块（58%宽度）
- 暖橙白卡片（#FFF3E0）+ 橙色手绘边框（#E8872A）
- 轻微倾斜（+0.3 度）+ 纸质阴影
- 内含：模块标题 + 解决机制核心载体结构 + 机制说明 + 柱状对比数据

### 中央过渡
- 绿色手绘弯曲大箭头，从左指向右

---

## 3. 关键视觉元素描述词汇

| 元素 | prompt 描述关键词 |
|------|------------------|
| 圆形图示 | "large circle with light blue fill and dark brown hand-drawn border, containing concept label" |
| 解决机制核心载体 | "organic egg/capsule-shaped structure, outer shell with radiating lines, inner golden core, resembling a delivery vehicle" |
| 手绘箭头 | "curved hand-drawn arrow, slight wobble, green or dark brown, casual sketch style" |
| 感叹号装饰 | "tilted red exclamation mark, hand-drawn style, emphasis decoration" |
| 问号装饰 | "tilted blue question mark, hand-drawn style, curiosity decoration" |
| 星形装饰 | "small 4-pointed yellow star with black outline, hand-drawn, accent decoration" |
| 柱状图 | "simple two-bar chart, short blue bar vs tall orange bar, with multiplier label like 7×" |
| 统计强调框 | "hand-drawn red ellipse circling a key number, emphasis highlight" |
| 纸质纹理 | "warm beige paper texture background, subtle grain, sketchbook feel" |
| 模块卡片 | "rounded-rect card with hand-drawn border, slight rotation, paper shadow" |

---

## 4. 禁止项（必须写入 negative prompt）

- 照片级写实、3D 渲染
- 暗色背景、霓虹色
- 企业扁平设计（corporate flat design）
- 渐变、光泽感
- 锐利几何完美（所有边框应有手绘不规则感）
- 杂乱、低分辨率
- 文字模糊
- 水印

---

## 5. Prompt 构建模板

组装 prompt 时，按以下顺序组织内容：

1. **画幅与比例**：开头明确 21:9 比例和尺寸
2. **整体风格**：手绘信息图、暖米色纸质感、素描本风格
3. **顶部标题栏**：黄色便利贴、手写标题、副标题小框
4. **左侧问题模块**：薄荷绿卡片、圆形图示、红色强调数据
5. **右侧解决模块**：暖橙白卡片、核心载体结构、柱状对比数据
6. **中央过渡箭头**：绿色手绘弯曲箭头
7. **装饰元素**：感叹号、星形、纸质感
8. **色彩指定**：全部色值
9. **字体提示**：Ma Shan Zheng（标题）+ Noto Sans SC（正文）
10. **Negative prompt**：排除不想要的风格

---

## 6. 内容映射规则

| 文章元素 | 通用对象角色 | prompt 中的表达 |
|---------|-------------|----------------|
| 核心痛点/旧方法 | 问题对象（圆形图示 + 红色强调框显示问题数据） | 左模块圆形图示 |
| 关键负面数据（如"98% 失败"） | 红色圆圈强调，置于圆形图示内 | 强调红数字 |
| 解决方案名称 | 右模块标题，大字展示 | 模块标题 |
| 解决方案核心机制 | 解决机制核心载体 + 2-3 条说明文字 | 蛋形/胶囊结构 |
| 对比数据（如"100倍/7倍"） | 右模块底部柱状图，含倍数标注 | 双柱对比图 |
| 关键尺寸参数 | 右模块中部尺子图标 + 数值 | 尺子图标 |
| 文章主标题 | 顶部标题栏左侧，≤28 字 | 手写大字 |
| 核心问题/副标题 | 顶部标题栏右侧黄色小框 | 副标题小框 |

### 双领域填充示例

**生物医药示例**：问题 = "高盐沉淀纯化纯度仅 60%"，解决 = "连续 TFF 换液工艺"，对比数据 = "纯度 92% vs 60%"，倍数 = "回收率提升 1.5×"。

**AI/科技示例**：问题 = "全量微调每轮成本 10 万+",解决 = "LoRA 低秩适配 + 量化推理"，对比数据 = "训练成本降至 1/7"，倍数 = "7× 成本下降"。

---

## 7. 视觉流程（固定）

prompt 中应描述以下视线引导路径：

顶部标题 → 左侧圆形图示（问题）→ 中央向右箭头 → 右侧结构图（解决）→ 右下数据柱

---

## 8. Prompt 模板（21:9 横版，英文可直接喂 DALL-E / Midjourney / Gemini）

```
A horizontal banner image at 21:9 aspect ratio (1260x540px), hand-drawn infographic style on warm beige paper texture (#F7EDD6), resembling a sketchbook page with subtle paper grain.

The composition has a top title bar and a two-column content area below:

TOP TITLE BAR (15% height, ~81px): A yellow sticky-note-style banner (#FFF8C0 background) with a blue hand-drawn border (#6BA8D4, 2.5px). Inside, the main title "{文章标题}" is written in large bold hand-brushed Chinese text (Ma Shan Zheng style, ~32px, dark brown-black #2B1810). To the right of the title, a small yellow rounded-rect tag (#FFF8C0 with blue #6BA8D4 border) contains a subtitle in 18px text: "{副标题10-18字}". The banner has a very slight tilt (rotate -0.3 degrees) for a casual feel.

CONTENT AREA (85% height, ~459px): Split into two rounded-rect panels side by side with a hand-drawn green arrow (#5CA86A) pointing from left to right between them.

LEFT PANEL — "The Problem" (42% width): A mint green card (#D4EDDA background) with a green hand-drawn border (#5C9E6B, 2.5px), slightly tilted (rotate -0.5deg), with a subtle paper shadow (3px 4px offset, 15% opacity). Inside: a bold module title "{问题主题}" at 22px. Below it, a large circle (140px diameter) with light blue fill (#EDF5FB) and a dark brown (#2B1810, 3px) hand-drawn border, containing the core problem concept "{核心问题A}" labeled inside. A red (#E03030) hand-drawn ellipse highlights a key alarming statistic (e.g., "98%") inside or near the circle. A tilted red exclamation mark (!) decoration floats nearby. Below the circle, 2-3 short annotation lines in 14px brown text (#5A4030) explain the pain points.

RIGHT PANEL — "The Solution" (58% width): A warm orange-white card (#FFF3E0 background) with an orange hand-drawn border (#E8872A, 2.5px), slightly tilted (rotate +0.3deg), same paper shadow. Inside: a bold module title "{解决主题}" at 22px. Below it, an organic egg-shaped structure (the solution's core carrier): an outer orange shell ellipse (#F09050, 90% opacity, ~160x190px) with radiating lines, and an inner golden core ellipse (#F5C518). The structure represents "{核心解决对象}". Around it, 2-3 annotation lines in 14px brown text explain the mechanism. At the bottom right, a simple two-bar chart: a short blue bar (#7BACD4) for the control group and a tall orange bar (#F09050) for the experimental group, with a bold "7×" or "{倍数}" multiplier label in 20px dark text above the tall bar. A blue (#4A7FC0) tilted question mark decoration and small yellow 4-point stars (#FFDA00 with black stroke) add visual interest.

Between the two panels, a large curved hand-drawn arrow in green (#5CA86A, 4px stroke) points from left to right, connecting the problem to the solution.

STYLE: Hand-drawn sketch infographic aesthetic, warm and approachable. All borders and lines have slight irregularity from a hand-drawn SVG filter (subtle wobble). Modules have gentle rotation for a casual notebook feel. Paper texture grain is visible in the background. Typography mixes Ma Shan Zheng (brush-style headings) with Noto Sans SC (clean body text). The color palette is warm (beige, yellow, green, orange) with red and blue for emphasis.

Negative prompt: photorealistic, 3D render, dark background, neon colors, corporate flat design, gradient, glossy, sharp geometric perfection, cluttered, low resolution, blurry text, watermark
```

---

## 9. 失败回退

| 现象 | 处理 |
| --- | --- |
| 生成结果偏扁平矢量/无手绘感 | 追加 `more hand-drawn wobble, sketchbook texture, imperfect lines` |
| 颜色过于鲜艳刺眼 | 强调 `muted warm palette, aged paper feel, reduce saturation` |
| 变成纯排版/信息图 | 删除柱状图坐标描述，只保留视觉造型与箭头 |
| 中文手写乱码 | 标题加引号包裹，前置 `Chinese hand-brushed text exactly: "..."` |
