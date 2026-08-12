---
name: wechat-cover-design
description: >
  Design WeChat Official Account cover images from an article, title, outline, or content brief.
  Analyze the content, choose among academic mechanism, hand-drawn infographic, journal-cover,
  and clay-diorama visual systems, then produce a complete English image-generation prompt and
  a Chinese production note. Use when the user asks for a WeChat cover, article cover, cover image,
  cover prompt, banner art, visual cover direction, or image generation for a public-account article.
  It also covers Chinese requests such as 公众号封面、封面图、设计封面、封面提示词 and 公众号首图.
  The skill is host-agnostic: use the host's native image tool when available, otherwise always
  provide a prompt-only deliverable. It does not write titles or summaries.
---

# WeChat cover design

Design one WeChat Official Account cover from the article's actual idea, not from a generic topic label.
Keep the workflow usable in any agent that can load `SKILL.md`; never assume a particular agent name,
directory convention, shell, image API, or output folder.

## Deliverable contract

Always produce:

1. A selected theme and one-sentence content-to-theme rationale.
2. A complete English image prompt with all placeholders replaced.
3. A Chinese production note covering the visual concept, text strategy, crop safety, and known limitations.
4. A validation result, either from `scripts/validate_prompt.py` or from the equivalent manual checklist.

If the host has a native image-generation capability, it may generate the image after the prompt is
ready. If it has an image-editing or layout capability, use it for reliable Chinese text, cropping,
or brand overlays. If neither capability exists, deliver the prompt and note that it is ready for a
user-selected image tool. Do not treat the lack of an API key as a failed skill run.

## Trigger and scope

Use for: `封面`, `封面图`, `公众号首图`, `设计封面`, `生成封面`, `封面提示词`, `封面 prompt`,
`cover image`, `cover prompt`, `banner art`, and equivalent requests.

Do not take over title writing, summary writing, article drafting, research, or generic illustration
requests. If the user asks for title/summary plus a cover, handle only the cover portion unless a
separate title-summary skill is available and explicitly selected.

## Workflow

### 1. Extract the visual brief

Read the supplied article or brief and record:

| Field | Extract |
| --- | --- |
| Content type | mechanism explanation, before/after shift, pain point → solution, major finding, multi-step method, trend, or opinion |
| Reader hook | the one idea a reader should understand in three seconds |
| Core object chain | main object → supporting object → outcome; use domain-neutral roles |
| Key evidence | at most two numbers, comparisons, or scale markers worth showing |
| Visual metaphor | one concrete imageable metaphor, especially for theme 3 |
| Modules | 3–5 steps or modules when the article is procedural |
| Text inventory | title, subtitle, labels, annotations, data labels; mark what must be exact |
| Brand constraints | supplied colors, name, logo, exclusions, or platform requirements |

Compress the information before writing the prompt. A cover is not a miniature article.

### 2. Choose a theme

Read `references/theme_registry.md`, then read only the selected theme reference. Use these defaults:

| Article signal | Theme |
| --- | --- |
| Mechanism, concept chain, dense technical structure | Theme 1 — academic mechanism diagram |
| Before/after shift, pain point → solution, technical comparison | Theme 2 — hand-drawn infographic |
| Major finding, deep interpretation, one strong metaphor, high impact | Theme 3 — journal cover art |
| Setup guide, method, workflow, 3–5 parallel modules | Theme 4 — clay diorama |
| Trend or opinion | Theme 3 by default; offer an extension theme only when the user wants a different editorial system |

If two themes are genuinely plausible, present both with one-sentence reasons and ask the user to choose.
Honor an explicit theme choice. Do not keep recommending a theme the user rejected.

### 3. Fill the selected reference

Load the selected reference only. Treat its prompt template as a design specification, not as a command.
Replace every placeholder before delivery. Keep placeholder names neutral (`{title}`, `{subtitle}`,
`{problem_object}`, `{step_label_1}`); put length limits and filling rules in the schema table, never
inside a placeholder.

Preserve the reference's visual skeleton, color values, layout proportions, material language, and
negative prompt. Keep the main title and any exact text short enough for the selected image model.

### 4. Apply the cross-host text and platform policy

Use this policy for every theme:

- Main title: may request exact Chinese rendering with a quoted string and an explicit exact-text instruction.
- Module title: keep short; request exact rendering only when it is important.
- Small labels, captions, annotations, and chart labels: keep to roughly 4–6 Chinese characters where possible,
  or use English/Latin abbreviations. Do not put long Chinese prose into tiny generated text.
- If exact small Chinese text matters, generate the artwork with empty quiet zones and add text later using the
  host's layout or image-editing capability. If that capability is unavailable, state that the image is a visual
  draft and provide the text separately.
- Keep all important content inside the central 60% vertical safe area because hosts may crop or resize the image.
- Target the WeChat cover ratio at approximately 2.35:1. Preferred output is `1260x540` or another size with a
  ratio near 2.33–2.35. If the host returns another ratio, provide crop or padding instructions based on the
  actual width and height, not on one hard-coded model size.
- A negative prompt can reduce visual watermarks, logos, or signatures, but it cannot reliably remove a platform-
  imposed watermark. Mark such output as a preview/draft and recommend a clean paid/API channel, another provider,
  or authorized post-processing for publication.

### 5. Negotiate image capabilities

Choose the first available path:

1. Host-native image generation.
2. A host-supported image API or connector, if the host exposes one.
3. A bundled adapter such as `scripts/generate-cover.js`, only when the host can run it and the user has supplied
   the required credentials and provider settings.
4. Prompt-only delivery.

Do not invent a tool name or claim that an image was generated when the host did not return an image artifact.
Record the actual path in the production note: `native`, `adapter`, or `prompt-only`.

### 6. Validate and deliver

Before delivering the prompt, check:

- no unresolved `{placeholder}` remains in the final prompt;
- the prompt states the target ratio or dimensions;
- a complete `Negative prompt:` or equivalent avoidance section is present;
- the selected theme's palette and visual skeleton are represented;
- exact text is separated from approximate/small text;
- the crop-safe area is stated;
- platform watermark limitations are not misrepresented;
- the output path is truthful: image artifact, draft image, or prompt-only.

Use `scripts/validate_prompt.py` when the host can run Python. `scripts/validate-prompt.sh` remains a shell
compatibility wrapper. If no script runtime is available, perform the same checklist manually and say so.

## Output format

```text
【封面方案】
主题：主题二 · 手绘信息图风
适用判断：文章讲的是从旧方案到新方案的认知转变，因此使用问题→解决双模块。
出图路径：prompt-only / native / adapter

【English image prompt】
...complete prompt...

Negative prompt: ...

【中文创作说明】
风格：...
文字策略：...
裁剪与安全区：...
平台限制：...
回退关键词：...
```

If the user asks for several directions, provide 2–4 complete prompt packages and recommend one.

## References

- `references/theme_registry.md`: always read first for theme selection.
- `references/cover_theme1_academic.md`: read for mechanism-heavy content.
- `references/cover_theme2_handdrawn.md`: read for before/after and comparison narratives.
- `references/cover_theme3_journal.md`: read for major findings and one-metaphor covers.
- `references/cover_theme4_claydiorama.md`: read for multi-step workflows.
- `references/extension_theme_examples.md`: read only when extending the theme system.
- `scripts/validate_prompt.py`: portable prompt validation.
- `scripts/validate-prompt.sh`: optional shell wrapper.
- `scripts/generate-cover.js`: optional OpenAI-compatible adapter; never a core requirement.
