# WeChat Cover Design

一个宿主无关的公众号封面设计 Skill：从文章、标题、提纲或内容 brief 中提炼视觉核心，匹配四套视觉主题，输出可直接交给文生图工具的英文 prompt 和中文创作说明。

## 核心原则

- **Prompt-first**：任何能加载 `SKILL.md` 的 Agent 都能完成核心工作。
- **工具协商**：有宿主原生生图能力就用原生能力；没有就交付 prompt，不因缺少 API Key 失败。
- **后期优先处理精确小字**：生成模型适合标题级文字，不适合长中文注释、图表标签和小字号正文。
- **水印诚实标注**：negative prompt 只能约束视觉内容，通常不能去掉平台强制水印。
- **尺寸按比例处理**：目标约为 2.35:1，裁剪判断根据实际宽高，不绑定某个模型的固定尺寸。

## 四套主题

- 主题一：学术机制图风——机制解析、概念逻辑链、信息密度高。
- 主题二：手绘信息图风——从旧到新、痛点到解决方案、技术对比。
- 主题三：顶刊科研封面风——重大发现、深度解读、单一强视觉隐喻。
- 主题四：粘土泥塑微缩风——多步骤方法论、Setup 指南、工作流拆解。

## 使用方式

把文章或内容 brief 交给支持 Skill 的 Agent，并提出“设计公众号封面”或“生成封面 prompt”。Skill 会：

1. 抽取内容类型、读者钩子、核心对象链、关键数据和文字清单；
2. 读取主题注册表并选择一个主题；
3. 按选定主题填充 prompt；
4. 根据宿主能力选择原生出图、可选适配器或 prompt-only；
5. 在交付前检查占位符、画幅、主题骨架、文字策略和水印状态。

## 出图路径

优先级如下：

1. 宿主原生文生图工具；
2. 宿主提供的图像 API 或连接器；
3. 本仓库的可选 OpenAI-compatible 适配器；
4. 只交付英文 prompt。

本仓库不假设任何 Agent 名称、安装目录、命令行环境或输出目录。若使用适配器，路径和输出目录由宿主决定。

## 可选脚本

### Prompt 校验

推荐使用跨平台 Python 校验器：

```text
python scripts/validate_prompt.py --all < prompt.txt
```

没有 Python 时，可以使用 shell wrapper：

```text
bash scripts/validate-prompt.sh --all < prompt.txt
```

校验器检查残留占位符、画幅描述、Negative prompt、长度和文本策略提示。它是辅助工具，不是 Skill 的运行前提。

### OpenAI-compatible 适配器

`scripts/generate-cover.js` 只用于宿主明确支持 Node.js、网络请求和 OpenAI-compatible Images API 的情况。它需要 API Key 和 provider 配置；没有这些条件时，请走宿主原生工具或 prompt-only 路径。

适配器支持 `--size WIDTHxHEIGHT`。它会按照实际比例输出微信封面的裁剪或补边指引，不再只识别某一个固定尺寸。

## 目录结构

```text
wechat-cover-design/
├── SKILL.md
├── skill.json
├── README.md
├── references/
│   ├── theme_registry.md
│   ├── _theme_template.md
│   ├── cover_theme1_academic.md
│   ├── cover_theme2_handdrawn.md
│   ├── cover_theme3_journal.md
│   └── cover_theme4_claydiorama.md
├── scripts/
│   ├── generate-cover.js
│   ├── validate_prompt.py
│   └── validate-prompt.sh
└── evals/
    ├── trigger_eval.json
    └── theme_match_eval.json
```

新增主题时，复制 `references/_theme_template.md`，补齐色板、布局、内容 schema、英文 prompt、Negative prompt、回退策略和主题区分表，再登记到 `references/theme_registry.md` 并加入真实 eval。

## 与标题摘要 Skill 的关系

本 Skill 只负责封面设计，不负责标题和摘要。用户同时需要标题、摘要和封面时，可由宿主协调标题摘要 Skill，再把最终标题和内容 brief 交给本 Skill。
