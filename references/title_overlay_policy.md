# Title Policy

All themes reserve the same natural left title field: `x=76..620`, `y=88..585` on a `1584x672` canvas. It is part of the background composition, not a floating UI panel.

## Native-image mode

Generate the background without text. Keep the left title field low-detail and free of focal objects. After generation, render exact typography with the host layout tool or `scripts/compose_cover.py`:

- Chinese: `YangRendongZhushi-Light.ttf` by default.
- Latin/English: `PreTesto_it.ttf`.
- No underline, divider, card, shadow, or translucent panel.

If the host can generate images but cannot perform layout or image editing, generate the cover directly from the prompt-only title instruction below. Record that model-rendered Chinese may need the supplied post-production correction.

## Prompt-only mode

The final English prompt must include the exact title, subtitle, and any supplied small labels, and ask the target model to render them in the left title field. Include all of the following in the prompt:

- `left 39% of the canvas reserved for a left-aligned title block`;
- the exact main title and optional subtitle in quotation marks;
- `Small labels: "..."` near their named objects; use short Chinese terms (4-6 characters) or scientific abbreviations such as `CD8+`, `VHH`, `LNP`, `mRNA`, and `CAR-T`;
- Chinese and Latin font direction;
- theme-matched color direction and hierarchy;
- `no other text, labels, watermark, logo, or object in the title field`.

Because image models can render Chinese inaccurately, state this limitation in the production note and also provide a post-production fallback containing the same exact text and coordinates. This fallback supplements the prompt; it does not replace the required in-prompt title instruction.
