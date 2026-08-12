# WeChat Cover Design — 公众号封面图设计 Skill

> 一个专注于**公众号封面图设计**的 Claude Code Skill：输入文章正文，分析内容类型并自动匹配视觉主题，输出可直接喂 DALL-E / Midjourney / Gemini 的英文文生图 prompt（模式A），或调用 OpenAI 兼容 Images API 直接出图保存 PNG（模式B）。
>
> 适用于 **AI / 科技、生物医药** 等多领域公众号内容。

## 功能特性

- 🎨 **4 套视觉主题**（按文章类型自动匹配）：
  - 主题一 · 学术机制图风（白底三栏、5 色科学配色，机制解析类）
  - 主题二 · 手绘信息图风（暖米纸感、「从X到Y」认知转变 + 对比数据）
  - 主题三 · 顶刊科研封面风（暗色背景 + 发光主体 + 视觉隐喻，重大发现类）
  - 主题四 · 粘土泥塑微缩风（圆台底座一字排开，多步骤方法论类）
- ✍️ **双模式交付**：英文 prompt（模式A）/ 调 API 直接出图（模式B）
- 📐 **微信标准尺寸**：21:9（≈ 微信 2.35:1 / 900×383）
- 🔌 **多 provider 兼容**：OpenAI 兼容 Images API，可接国内服务商
- ➕ **可扩展**：内置新增主题脚手架（`references/_theme_template.md`）+ 扩展种子（AI哲学风/行业洞察风）
- ✅ **质量自检**：内置 prompt 校验脚本（残留占位符 / negative prompt / 画幅 / 长度）

## 快速开始

### 模式A · 只输出 prompt

向 Claude 提供文章正文，说「设计封面」，即可获得匹配主题的英文 prompt + 中文创作说明，直接粘贴到 DALL-E / Midjourney / Gemini 使用。

### 模式B · 直接出图（需配置 API Key）

确认方案后，Claude 会执行：

```bash
node .claude/skills/wechat-cover-design/scripts/generate-cover.js \
  --prompt "<完整英文prompt>" \
  --theme theme3 \
  --name "LNP-delivery-cover"
```

图片保存到 `assets/covers/cover-{theme}-{时间戳}.png`，同时打印微信 2.35:1 裁剪指引。

## API 配置指南

脚本配置优先级：**CLI 参数 > 环境变量 > config.json**。

### 方式一：环境变量（推荐）

```bash
# Windows (CMD)
set OPENAI_API_KEY=sk-xxx
set OPENAI_BASE_URL=https://api.openai.com/v1

# Windows (PowerShell)
$env:OPENAI_API_KEY="sk-xxx"

# Git Bash / macOS / Linux
export OPENAI_API_KEY=sk-xxx
```

可选：`COVER_IMAGE_MODEL`（默认 `dall-e-3`）。

### 方式二：config.json

在 `scripts/` 目录创建 `config.json`（已被 .gitignore 忽略，key 不入库）：

```json
{
  "base_url": "https://api.openai.com/v1",
  "api_key": "sk-xxx",
  "model": "dall-e-3",
  "default_size": "1792x1024",
  "output_dir": "assets/covers"
}
```

### 方式三：国内兼容 provider

OpenAI 直连在中国大陆可能受限。多数国内服务商提供 OpenAI 兼容的 `/images/generations` 接口，只需切换 `base_url`（及对应 `api_key`、`model`、`size`）：

| 服务商 | base_url 示例 | 备注 |
|--------|---------------|------|
| OpenAI | `https://api.openai.com/v1` | 官方 |
| 阿里云百炼（通义万相） | `https://dashscope.aliyuncs.com/compatible-mode/v1` | 需查文生图 model 名 |
| 智谱 AI | `https://open.bigmodel.cn/api/paas/v4` | 需查 image model |
| 硅基流动 | `https://api.siliconflow.cn/v1` | 需查 image model |
| 其他 OpenAI 兼容服务 | 依其文档 | — |

> 各 provider 的 `model` 名与 `size` 支持需查其官方文档。不兼容时脚本会**透传 provider 的错误信息**，便于排查。若 provider 支持自定义比例（如 `900x383`），可用 `--size 900x383` 精确生成。

## 触发词

`封面`、`封面图`、`设计封面`、`生成封面`、`封面提示词`、`封面prompt`、`封面风格`、`配图`、`文生图`、`出图`、`cover image` 等。

> **消歧**：本 skill 只做封面图，不含标题与摘要。需要「标题+摘要+封面」时请用 `wechat-title-summary`。

## 校验命令

```bash
# 校验一个 prompt 是否合格（残留占位符 / negative / 画幅 / 长度）
echo "<prompt>" | bash .claude/skills/wechat-cover-design/scripts/validate-prompt.sh --all

# 单独校验
echo "<prompt>" | bash .claude/skills/wechat-cover-design/scripts/validate-prompt.sh --no-placeholders
```

## 目录结构

```
wechat-cover-design/
├── SKILL.md                        # 主定义：五步工作流、触发词、双模式交付、质量自检
├── skill.json                      # 元数据
├── README.md                       # 本文件
├── references/
│   ├── theme_registry.md           # 主题注册表 + 新增主题四步法
│   ├── _theme_template.md          # 新增主题脚手架模板
│   ├── cover_theme1_academic.md    # 主题一：学术机制图风
│   ├── cover_theme2_handdrawn.md   # 主题二：手绘信息图风
│   ├── cover_theme3_journal.md     # 主题三：顶刊科研封面风
│   ├── cover_theme4_claydiorama.md # 主题四：粘土泥塑微缩风
│   └── extension_theme_examples.md # 扩展主题种子（AI哲学风/行业洞察风，未启用）
├── scripts/
│   ├── generate-cover.js           # 模式B：OpenAI 兼容 Images API 出图
│   └── validate-prompt.sh          # prompt 质量校验
└── evals/
    ├── trigger_eval.json           # 触发词评估
    └── theme_match_eval.json       # 主题匹配评估
```

## 新增主题（四步法）

1. 复制脚手架：`cp references/_theme_template.md references/cover_theme5_xxx.md`，按 8 章节填写（**必须含色板 + negative prompt**）
2. 在 `references/theme_registry.md` 注册表加一行
3. 按需更新 SKILL.md Step 2 匹配规则
4. 用真实文章实测 + 写入 `evals/theme_match_eval.json`

扩展主题种子（AI哲学风 / 行业洞察风）见 `references/extension_theme_examples.md`。

## 与 wechat-title-summary 的关系

本 skill 从 `wechat-title-summary` 剥离并优化而来，**原 skill 保持不动**：
- `wechat-title-summary`：标题 + 摘要 + 封面（三合一，生物医药垂直，GitHub 托管）
- `wechat-cover-design`：仅封面（多领域泛化，双模式出图，可扩展）

> 迁移说明：本 skill 的 4 套主题视觉骨架（色板/布局/材质/negative prompt）与 `wechat-title-summary` 1:1 对应，仅将内容映射规则泛化为「通用对象角色」并补充 AI/科技示例。
