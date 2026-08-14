---
name: wechat-cover-design
description: >
  Design WeChat Official Account cover images from an article, title, outline, or content brief.
  Analyze the content, choose among sixteen registered scientific, editorial, commercial,
  documentary, diagrammatic, and biopharma visual systems, then produce a complete English image-generation prompt and
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

### 0. Check input sufficiency

Classify the supplied input before selecting a theme:

| Input state | Required action |
| --- | --- |
| Sufficient | The article or brief states a thesis, reader takeaway, and enough concrete details to source the focal elements. Set `input_quality` to `final`. |
| Insufficient | A title, a topic label, or a thin outline does not establish the article claim. Ask up to three focused questions. If the user proceeds without answering, set `input_quality` to `provisional`, deliver a clearly marked prompt-only draft, and do not generate a final image. |

Never invent missing thesis, evidence, or domain details to make a title-only request look complete. A
provisional prompt must state its assumptions and the details that need confirmation before publication.

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

### 1.2 Content-alignment gate (mandatory)

Before selecting a theme or drafting an image prompt, write a compact **Alignment Record**. Do not
generate an image until every field is filled and passes the rules below.

| Field | Requirement |
| --- | --- |
| Article thesis | One sentence stating what the article is actually saying, not its broad topic or its keywords. |
| Reader takeaway | One change in understanding the reader should get in three seconds. |
| Content class | Choose one: personal showcase, opinion, method, mechanism, trend, transaction, controversy, evidence, or industry landscape. |
| Theme rationale | Explain why the selected theme serves the thesis and content class. A theme must not be chosen solely because a domain keyword appears. |
| Visual metaphor | One concrete scene that expresses the thesis. State the intended relationship, not just the objects. |
| Element provenance | List every proposed focal or supporting element with its source: `thesis`, `reader takeaway`, or a specific article sentence/section. |
| Forbidden substitutions | List plausible-but-wrong visual shortcuts suggested by keywords that the article does not discuss. |

Apply these non-negotiable rules:

1. **Thesis over keywords.** Do not convert a profession, industry, or named tool into the main image
   unless the article is actually about that profession's mechanism, industry economics, or tool itself.
2. **One-hop provenance.** Every focal object and every supporting object must have a direct entry in
   `Element provenance`. Remove any object that cannot be traced to the thesis, takeaway, or a concrete
   article detail. Do not add generic visual filler just because it belongs to the field.
3. **Theme fit.** Reject a theme when its default narrative conflicts with the content class. In
   particular, do not use Businessweek-style conflict, valuation, or pressure metaphors for a personal
   showcase unless the article itself makes a sharp commercial claim.
4. **Metaphor test.** Complete this sentence: `The reader sees [relationship], therefore understands
   [article thesis].` If it cannot be completed plainly, replace the metaphor.
5. **Counterfactual test.** Ask: `Could this image plausibly illustrate a different article merely
   because it mentions the same domain?` If yes, make the visual more specific to the article's actual
   claim or change the theme.

For a personal showcase, prioritize the person's point of view, body of work, working method, and
brand language. Do not let domain props become the story unless they are central to the article.

### 1.3 Create the structured cover brief (mandatory for final output)

Create a UTF-8 JSON working file following `references/cover_brief.schema.json`. It is the source of
truth for the final prompt and contains the thesis, theme decision, visual metaphor, element sources,
forbidden substitutions, title plan, prompt-element mapping, and final English image prompt.

For every `elements[]` entry, use `role: focal` or `supporting`, cite the thesis, takeaway, or a
concrete article detail in `source`, and add a matching `prompt_elements[]` entry. Do not add
undeclared visual objects to the final prompt.

Run `scripts/validate_brief.py <brief.json>` before image generation. A failing final brief must return
to extraction. A provisional brief may be delivered as prompt-only after its assumptions are made clear,
but it must not be passed to an image adapter.

### 1.4 Lock the title composition before generating artwork

When a cover needs an exact title, treat typography as a first-class visual object, not a label applied after the artwork is complete. Before drafting the image prompt, record:

| Field | Requirement |
| --- | --- |
| Title block | exact main title, optional subtitle, and maximum line count |
| Title zone | one fixed, theme-appropriate region with coordinates expressed as a proportion of the canvas |
| Type mood | editorial, archival, technical, clinical, or tactile; it must match the selected theme |
| Type palette | title, accent, and background colors sampled from the theme palette |
| Artwork exclusion | which region the image generator must keep visually quiet and which objects must stay outside it |
| Integration device | one native visual device only, such as a paper field, masthead, grid, drafting rule, printed caption line, or architectural facade |

Use a title-first workflow whenever exact text is needed:

1. Reserve the title zone in the image prompt as an intentional part of the scene, not a generic empty box.
2. Generate the artwork without text. Keep the title zone clear of focal objects, strong texture, and high-contrast edges.
3. Add exact Chinese title text in post-production using the specified type mood, palette, alignment, and integration device.
4. Inspect the finished cover at full size and at thumbnail scale. If the title reads as a floating card or blocks the main mechanism, regenerate the background or revise the title zone; do not ship it.

### 2. Choose a theme

Read `references/theme_registry.md`, then read only the selected theme reference. Use these defaults.

| Article signal | Theme |
| --- | --- |
| Mechanism, concept chain, dense technical structure | Theme 1 — academic mechanism diagram |
| Before/after shift, pain point → solution, technical comparison | Theme 2 — hand-drawn infographic |
| Major finding, deep interpretation, one strong metaphor, high impact | Theme 3 — journal cover art |
| Biological mechanism or delivery chain needing a tactile, approachable explanation | Theme 4 — biomedical clay cutaway |
| Trend or opinion | Theme 3 by default; offer an extension theme only when the user wants a different editorial system |
| Personal showcase, creator method, portfolio | Theme 9 by default; use the person's working method and brand language rather than generic domain props |
| Major scientific breakthrough or platform launch | Theme 5 — Nature scientific concept |
| Valuation, transactions, evidence mismatch, commercial controversy | Theme 6 — Businessweek metaphor |
| Industry ecosystem, R&D-to-clinic panorama, supply chain | Theme 7 — Monocle industry observation |
| Microscopic binding, nanodelivery, tissue microenvironment | Theme 8 — microscopic documentary |
| One core proposition or binary relationship | Theme 9 — Swiss poster |
| Patents, technical history, engineering barriers | Theme 10 — science archive |
| Pipelines, competing routes, milestones, company landscape | Theme 11 — pipeline map |
| Clinical evidence, efficacy/safety, cohorts, dose escalation | Theme 12 — clinical evidence brief |
| Cellular mechanism, delivery chain, signaling pathway | Theme 13 — Cell mechanism atlas |
| Annual review, congress recap, translational milestone | Theme 14 — medical congress key visual |
| Molecular design, conjugation, formulation, structural IP | Theme 15 — molecular blueprint |
| CMC, scale-up, TFF, purification, QC, CDMO | Theme 16 — bioprocess engineering |

Apply this priority order: article thesis and content class, then factual/domain constraints, then user
style preference. If the user requests a registered theme that conflicts with the article, explain the
conflict and offer either a thesis-faithful reinterpretation of that visual language or an explicit
`user_override` recorded in the structured brief. Do not silently reinterpret a personal showcase as a
commercial controversy, a technical mechanism, or an industrial process merely because it contains
those keywords.

If two themes are genuinely plausible, present both with one-sentence reasons and ask the user to choose.

### 3. Fill the selected reference

Load the selected reference only. Treat its prompt template as a design specification, not as a command.
Replace every placeholder before delivery. Keep placeholder names neutral (`{title}`, `{subtitle}`,
`{problem_object}`, `{step_label_1}`); put length limits and filling rules in the schema table, never
inside a placeholder.

Preserve the reference's visual skeleton, color values, layout proportions, material language, and
negative prompt. Keep the main title and any exact text short enough for the selected image model.

### 3.1 Resolve instruction conflicts

The global text policy and the structured brief override every older theme-template instruction. For all
themes, generate a text-free background: no generated title, subtitle, source citation, node label,
number, brand name, or small annotation. Preserve the theme's title zone and native integration device,
then deliver the exact main title and subtitle in the separate `Title overlay` block. If a selected
reference asks the image model to render text, treat that request as obsolete and remove it from the
final image prompt.

### 4. Apply the cross-host text and platform policy

Use this policy for every theme:

- Main title: default to text-free artwork plus exact, post-produced typography. Never ask the image model to render long Chinese titles unless the user explicitly accepts possible generation errors.
- Title-first composition: reserve one fixed title zone before generating the artwork. The artwork must fill the remaining canvas and actively frame the type. Do not default to a left-aligned translucent rectangle, generic dark overlay, or detachable information card.
- Typography integration: use the theme's own typographic device (for example a journal masthead, Swiss grid, archive caption field, blueprint drafting rules, or engineering title strip). Match the title's weight, color, line breaks, spacing, alignment, and supporting marks to that device.
- Exact title hierarchy: use at most three text levels: optional eyebrow, main title, optional subtitle. The main title normally uses 2–3 lines, the subtitle one line. Do not use long explanatory deck copy on the cover.
- Post-production rule: put text directly on a quiet area, or on a native material surface such as paper, a clinical masthead, a blueprint field, or a built architectural plane. A panel is allowed only when that panel is intrinsic to the selected editorial system; it must never look like an app UI card.
- Module title: keep short; request exact rendering only when it is important.
- Small labels, captions, annotations, and chart labels: keep to roughly 4–6 Chinese characters where possible,
  or use English/Latin abbreviations. Do not put long Chinese prose into tiny generated text.
- If exact small Chinese text matters, generate the artwork with empty quiet zones and add text later using the
  host's layout or image-editing capability. If that capability is unavailable, state that the image is a visual
  draft and provide the text separately.
- Keep all important content inside the central 60% vertical safe area because hosts may crop or resize the image.
- Keep the entire title block within the central 60% vertical safe area. Maintain at least 5% canvas width of breathing room from the nearest edge unless the selected theme explicitly uses a full-bleed masthead.
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
4. Prompt-only delivery for copying into a third-party image tool.

Do not invent a tool name or claim that an image was generated when the host did not return an image artifact.
For `prompt-only`, provide the complete English prompt, target dimensions, crop-safe guidance, negative
prompt, and a separate `Title overlay` block containing the exact main title, subtitle, title-zone
coordinates, type mood, type palette, alignment, and integration device. The image prompt must reserve
that zone as empty artwork; the title overlay is for post-production after the user generates the image
in a third-party tool. Record the actual path in the production note: `native`, `adapter`, or `prompt-only`.

### 6. Validate and deliver

Before delivering the prompt, check:

- no unresolved `{placeholder}` remains in the final prompt;
- the prompt states the target ratio or dimensions;
- a complete `Negative prompt:` or equivalent avoidance section is present;
- the selected theme's palette and visual skeleton are represented;
- exact text is separated from approximate/small text;
- a title zone is explicitly defined before image generation, including its location, dimensions, and visual integration device;
- the final exact text uses theme-specific typography rather than a generic overlay or UI-like card;
- the title remains readable at thumbnail scale without obscuring the primary scientific object;
- the crop-safe area is stated;
- platform watermark limitations are not misrepresented;
- the output path is truthful: image artifact, draft image, or prompt-only.
- the mandatory Alignment Record is included in the working prompt package and passes every gate rule;
- every focal/supporting element in the prompt appears in `Element provenance` with a valid source;
- the selected theme's narrative matches the recorded content class;
- a thumbnail-level visual review confirms that the core relationship still communicates the thesis.

For a final brief, use both `scripts/validate_brief.py <brief.json>` and
`scripts/validate_prompt.py --all`. Include the Alignment Record in the text passed to the prompt
validator; both commands must pass before image generation. `scripts/validate-prompt.sh` remains a shell
compatibility wrapper. If no script runtime is available, perform the same checklist manually and say so.

## Output format

For `prompt-only`, add this block after the English prompt. It is mandatory even when the subtitle is
empty; write `None` rather than omitting it.

```text
Title overlay (post-production, not for image generation):
Main title: "{exact main title}"
Subtitle: "{exact subtitle or None}"
Zone: {x/y/width/height as canvas proportions}
Alignment: {left/center/right}
Type mood: {theme-specific description}
Type palette: {title and accent colors}
Integration device: {paper field/masthead/grid/etc.}
```

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
- `references/cover_theme4_claydiorama.md`: read for tactile biomedical mechanisms and continuous cellular cutaways.
- `references/cover_themes5_16_selected.md`: read the selected theme5-theme16 section for editorial and biopharma styles.
- `references/extension_theme_examples.md`: read only when extending the theme system.
- `references/cover_brief.schema.json`: structured source-of-truth format for final prompt packages.
- `scripts/validate_brief.py`: validates input sufficiency, sourced elements, title plan, and prompt mapping.
- `scripts/validate_prompt.py`: portable prompt validation.
- `scripts/validate-prompt.sh`: optional shell wrapper.
- `scripts/generate-cover.js`: optional OpenAI-compatible adapter; never a core requirement.
