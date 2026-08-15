---
name: wechat-cover-design
description: Design finished WeChat Official Account covers for biopharma and biomedical articles. Use when the user asks for a 公众号封面、封面图、文章首图、cover image、cover prompt or banner art about drug discovery, delivery, clinical evidence, molecular design, CMC, biotech industry, or related science. Select from thirteen biopharma visual systems, generate the cover directly when the host can generate images, and otherwise provide a copy-ready English prompt with an exact left-side title specification.
---

# WeChat Cover Design

Create one editorial WeChat cover from the article's actual claim. This skill is optimized for the biopharma workflow: mechanism explanation, delivery technology, clinical evidence, platform analysis, molecular design, industry landscape, and CMC/manufacturing.

## Execution rule

Decide the execution path before drafting the final answer.

| Host capability | Required action |
| --- | --- |
| Native image generation is available | **Generate the image directly.** Do not stop at a prompt. When layout/editing is also available, generate a text-free background with the fixed left title field and apply exact text afterward. When layout/editing is unavailable, generate directly from the full left-title prompt used in prompt-only mode. Return the image artifact and the production note. |
| No native image generation is available | Return one copy-ready English image-generation prompt. It must ask the target image model to render the exact title in the fixed left field and must include the full title layout specification in the same prompt. |

Never ask the user to choose between these paths when the host capability is known. Never claim an image was generated unless the host returned an image artifact.

## Input and visual brief

Extract only what is needed to make a cover specific to the article:

| Field | Requirement |
| --- | --- |
| Article thesis | One sentence stating the actual claim. |
| Reader takeaway | What a reader should grasp in three seconds. |
| Core object chain | Focal scientific object, supporting object, and outcome. |
| Evidence | At most two meaningful comparisons, measures, or stages. |
| Title inventory | Exact main title, optional subtitle, and any text that must remain verbatim. |
| Constraints | Brand colors, exclusions, or required theme. |

If the article does not provide enough information for a factual visual, ask up to three focused questions. Do not invent experimental results, clinical claims, company facts, or medical efficacy.

## Select one of the 13 themes

Read `references/theme_registry.md`, `references/typography_layout.md`, and the matching section in `references/theme_specs.md` before composing the prompt. Theme IDs are fixed at 1-13; do not refer to or restore any retired themes.

| Article signal | Theme |
| --- | --- |
| Biological mechanism or delivery chain | Theme 1: biomedical clay cutaway |
| Major scientific breakthrough or platform launch | Theme 2: Nature scientific concept |
| Valuation, transactions, or evidence mismatch | Theme 3: Businessweek metaphor |
| Industry ecosystem or R&D-to-clinic panorama | Theme 4: Monocle industry observation |
| Microscopic binding, nanodelivery, tissue microenvironment | Theme 5: microscopic documentary |
| One core proposition or binary relationship | Theme 6: Swiss poster |
| Patents, technical history, engineering barriers | Theme 7: science archive |
| Pipelines, competing routes, milestones, company landscape | Theme 8: pipeline map |
| Clinical evidence, efficacy/safety, cohorts, dose escalation | Theme 9: clinical evidence brief |
| Cellular mechanism, delivery chain, signaling pathway | Theme 10: Cell mechanism atlas |
| Annual review, congress recap, translational milestone | Theme 11: medical congress key visual |
| Molecular design, conjugation, formulation, structural IP | Theme 12: molecular blueprint |
| CMC, scale-up, TFF, purification, QC, CDMO | Theme 13: bioprocess engineering |

Honor an explicit theme choice unless it contradicts a factual constraint. When two themes are genuinely equally suitable, present two one-sentence options and ask the user to choose.

## Fixed title composition

All covers use a `1584x672` canvas (about 2.35:1). The title field is always on the left: `x=76..620`, `y=88..585` (roughly the left 39% of the canvas). Keep the right 60% for the focal biomedical scene.

- Use a natural quiet field, not a translucent card, underline, divider, shadow, or gradient panel.
- Reserve the left field before generating the background. Keep it low-detail, clear of focal objects, high-contrast edges, labels, and data marks.
- Use the selected theme's palette. Chinese defaults to `YangRendongZhushi-Light.ttf`; Latin/English uses `PreTesto_it.ttf`.
- Keep the hierarchy to eyebrow, main title, optional subtitle, and one short footer at most.
- If the source artwork has no usable left quiet field, regenerate the background. Do not move the title toward the scientific subject.

### Native-image path

Write a text-free image prompt that explicitly reserves the fixed left title field. Generate the artwork immediately with the host's native image tool. Then render the supplied exact title in the field using host layout/editing or `scripts/compose_cover.py`. If the host can generate but cannot overlay text, still generate the cover directly, but use the full prompt-only title instruction in that generation and state the possible Chinese-rendering limitation in the production note.

### Prompt-only path

Provide one self-contained English prompt that contains all of the following:

1. Target dimensions: `1584x672` or `2.35:1`.
2. The selected theme's visual scene, palette, materials, focal object, and right-side placement.
3. A left-side low-detail title field occupying 39% of the width.
4. A verbatim text instruction such as: `Render the following title exactly in the left title field: "{main title}".` Include the exact subtitle if supplied.
5. Typography instruction: left aligned; Chinese in Yang Rendong Zhushi Light or closest elegant brush-serif substitute; Latin/English in PreTesto or closest high-contrast italic serif; palette and line hierarchy matching the theme.
6. A `Subtitle:` instruction, using `None` only when the user supplied no subtitle.
7. A `Small labels:` instruction. Render only supplied labels, keep Chinese labels to 4-6 characters, and prefer scientific abbreviations such as `CD8+`, `VHH`, `LNP`, `mRNA`, or `CAR-T`. Do not invent labels or put long Chinese prose next to objects.
8. A negative prompt preventing watermarks, extra text, labels not supplied by the user, logos, and objects entering the title field.

The fallback prompt must contain the title, subtitle, and any supplied small labels. Also append a short `Post-production fallback` note with the same text, coordinates, fonts, and colors in case the target image model renders Chinese inaccurately.

## Deliverables

### When an image was generated

Return:

1. The image artifact.
2. Theme and one-sentence rationale.
3. A concise Chinese production note: title treatment, crop safety, and any text-rendering limitation.
4. The validation result.

### When only a prompt can be produced

Return:

1. Theme and one-sentence rationale.
2. A complete, copy-ready English image prompt containing the left title instructions above.
3. `Post-production fallback`: title, subtitle, `x=76..620, y=88..585`, Chinese font, English font, palette, and left alignment.
4. A concise Chinese production note and the validation result.

## Prompt package format

Use this package structure for both paths. It is also the required input to `scripts/validate_prompt.py --all`; replace every quoted value with article-specific content.

```text
Cover plan:
Theme: Theme 6 - Swiss poster
Generation path: native-image / prompt-only

Alignment Record:
Article thesis: "..."
Reader takeaway: "..."
Content class: mechanism / evidence / transaction / industry_landscape / other registered class
Theme rationale: "..."
Visual metaphor: "..."
Element provenance: "focal object: article section ...; supporting object: reader takeaway ..."
Forbidden substitutions: "article-irrelevant visual shortcuts only; do not repeat image-quality negative terms"

English image prompt:
Create a 1584x672 (2.35:1) WeChat cover in [selected theme] style. Place [focal scientific scene] in the right 60% of the canvas. Reserve left x=4.8%-39.1%, y=13.1%-87.1% as a low-detail, theme-native title field.
[Native-image path only: Generate text-free artwork in this field for exact post-production typography.]
[Prompt-only path only: Render the exact Chinese main title "..." in the left title field. Subtitle: "...". Small labels: "...". Render supplied labels only.]
Text-rendering strategy: [state the selected path and how exact text is rendered].
Negative prompt: watermark, logo, unsupplied text, gibberish, crowded composition, focal objects in the title field.

Chinese production note:
...
```

## Validation

Before delivery, confirm that the final prompt has no unresolved placeholders, states the 2.35:1 format, includes a negative prompt, names the theme's visual language, and preserves the left title field.

- For a native-image prompt, run `scripts/validate_prompt.py --all` when Python is available. Verify that exact title text is separated from the text-free image prompt and is available for post-production.
- For a prompt-only deliverable, run `scripts/validate_prompt.py --prompt-only`; it runs the same structural and Alignment Record checks and additionally requires an explicit left title field plus title, subtitle, and small-label instructions.
- If scripts cannot run, apply the equivalent checklist manually and state that fact.

## References

- `references/theme_registry.md`: theme names and article-signal mapping.
- `references/theme_specs.md`: detailed visual prompt skeletons.
- `references/typography_layout.md`: fixed coordinates, palette, and bundled fonts.
- `references/title_overlay_policy.md`: native-image and prompt-only title rules.
- `scripts/compose_cover.py`: deterministic title compositor.
- `scripts/validate_prompt.py`: prompt validator.
