---
name: create-theme-concept
description: Create a complete theme concept specification from a creative direction, reference image, or both. Extracts colors from images, proposes a theme name, and generates palette JSON, docs README, and concept document.
---

## What this skill does

Generate the **four** foundational files that define a new theme:

1. `<theme-name>/palette/<theme-name>.json` — canonical color palette
2. `<theme-name>/docs/README.md` — theme overview
3. `<theme-name>/docs/<theme-name>-concept.md` — full design rationale (English, literary tone)
4. `<theme-name>/docs/<theme-name>-concept-th.md` — plain-language rewrite (Thai, accessible tone)

## Inputs

The user may provide any combination of:
- **An image** — a screenshot, photograph, artwork, or any visual reference. Extract the dominant colors, mood, and atmosphere from the image to drive the palette design.
- **A theme name** (kebab-case, e.g. `solar-drift`) — optional. If not provided, propose a name based on the image mood and colors.
- **Creative direction** — mood, inspiration, color family, or any descriptive guidance. Optional if an image is provided.

### When an image is provided

1. Analyze the image to identify the dominant colors, color temperature, mood, and atmosphere.
2. Extract key hex colors from the image as starting points for accents.
3. If no theme name is given, generate a name following the naming rules below. Present the proposed name to the user for confirmation before generating files.
4. Adapt extracted colors for code readability — raw image colors may need saturation or lightness adjustments to work on dark backgrounds without halation or low contrast.

### When only a creative direction is provided

Design colors from scratch based on the described mood, inspiration, or color family.

## Naming rules

The theme name is a first-class creative artifact. It must be:

- **Specific, not generic.** It names a precise thing from the real world, not a broad category. `obsidian` is generic. `lava-shelf` is specific — it names a particular geological moment.
- **Evocative, not descriptive.** It should make someone feel something before they see the palette. `dark-blue` describes. `drowned-signal` evokes.
- **Unexpected.** Avoid the overused vocabulary of dark themes: `night`, `shadow`, `dark`, `void`, `abyss`, `midnight`, `phantom`, `ghost`. These words are exhausted. Find the angle no one else took.
- **Two words, kebab-case.** A noun and a modifier, or two nouns in tension. The combination should feel slightly surprising but immediately right.
- **Rooted in the source.** The name must come from the same visual or emotional world as the palette — not imposed from outside. If the reference is a film still, the name might echo the scene. If it's a material, the name might name the material's state or context.

### Name generation process

Generate **5 candidate names** before choosing. For each candidate, write one sentence explaining what specific element of the source it references. Then select the strongest — the one that is most unexpected while being most accurate. Discard names that:
- Use any of these words: `night`, `shadow`, `dark`, `void`, `abyss`, `midnight`, `phantom`, `ghost`, `neon`, `cyber`, `pixel`, `digital`, `vapor`, `retro`, `synthwave`
- Could belong to a different theme's palette without feeling wrong
- Sound like a product name or a band name rather than a place or material

### Examples of strong vs. weak names

| Weak | Strong | Why the strong name wins |
|---|---|---|
| `ember-skyline` | `slag-horizon` | Slag is a specific material with color and weight; skyline is generic |
| `glacier-dusk` | `meltwater-hour` | Names the exact transitional moment, not just a location + time |
| `neon-city` | `fluorescent-fail` | Names the specific phenomenon (a tube about to die) not the setting |
| `desert-night` | `fired-clay` | Names the material that holds the heat, not the environment |
| `brass-and-black` | `oxidized-stage` | The oxidation names the exact color state of aged brass; stage names its theatrical context |

## Step-by-step procedure

### 1. Design the palette

Create the color palette following these constraints:

- **Backgrounds:** 4 shades from darkest to lightest (`bg.primary`, `bg.secondary`, `bg.highlight`, `bg.border`). `bg.secondary` is darker than `bg.primary` (used for sidebars/panels). All must be very dark.
- **Foregrounds:** 4 levels (`fg.primary`, `fg.dimmed`, `fg.muted`, `fg.gutter`). Primary is near-white, gutter is most recessive.
- **Accents:** 6-11 named colors in `snake_case`. Must include a `red` for errors. Each accent has a distinct hue — no two accents should be perceptually similar.
- **ANSI:** Full 16-color terminal set (`black` through `bright_white`) using `snake_case` with `bright_` prefix.
- **Semantic roles:** 10-15 dot-path references mapping syntax roles to colors (e.g. `"functions": "accent.teal"`).

Color design rules:
- Every hex color is 6-digit uppercase (`#FF2CF1`)
- One accent is the **hero color** — used for functions/methods, the most visually dominant
- Keywords can be bold white or a strong accent — they mark structural flow
- Comments must be low-contrast and recessive
- Cursor color must be high-contrast and unmissable
- All colors must work well on the dark backgrounds without halation

### 2. Write palette JSON

Write to `<theme-name>/palette/<theme-name>.json`:

```json
{
  "name": "Human Readable Name",
  "description": "One-line: base description + spectrum summary + key features",

  "colors": {
    "bg": {
      "primary":    "#XXXXXX",
      "secondary":  "#XXXXXX",
      "highlight":  "#XXXXXX",
      "border":     "#XXXXXX"
    },
    "fg": {
      "primary":    "#XXXXXX",
      "dimmed":     "#XXXXXX",
      "muted":      "#XXXXXX",
      "gutter":     "#XXXXXX"
    },
    "accent": {
      ...
    },
    "ansi": {
      "black":          "#XXXXXX",
      "red":            "#XXXXXX",
      "green":          "#XXXXXX",
      "yellow":         "#XXXXXX",
      "blue":           "#XXXXXX",
      "magenta":        "#XXXXXX",
      "cyan":           "#XXXXXX",
      "white":          "#XXXXXX",
      "bright_black":   "#XXXXXX",
      "bright_red":     "#XXXXXX",
      "bright_green":   "#XXXXXX",
      "bright_yellow":  "#XXXXXX",
      "bright_blue":    "#XXXXXX",
      "bright_magenta": "#XXXXXX",
      "bright_cyan":    "#XXXXXX",
      "bright_white":   "#XXXXXX"
    }
  },

  "semantic_roles": {
    "keywords":     "accent.xxx or fg.xxx",
    "functions":    "accent.xxx",
    "strings":      "accent.xxx",
    "variables":    "fg.primary",
    "comments":     "accent.xxx or fg.muted",
    "types":        "accent.xxx",
    "tags":         "accent.xxx",
    "attributes":   "accent.xxx",
    "literals":     "accent.xxx",
    "constants":    "accent.xxx",
    "constructors": "accent.xxx",
    "errors":       "accent.red",
    "operators":    "fg.dimmed",
    "cursor":       "accent.xxx"
  }
}
```

Use 2-space indent. Column-align values within each section. Blank line between `"description"` and `"colors"`, and between `"colors"` and `"semantic_roles"`.

### 3. Write docs/README.md

Write to `<theme-name>/docs/README.md` (~30 lines):

```markdown
# Theme Name

A dark coding color scheme using a **Base Description** with a **Spectrum Description** — [function color] functions, [string color] strings, [type color] types, ... Built for [mood phrase].

## Palette

| Token | Hex | Name |
|---|---|---|
| Background | `#XXXXXX` | Base Name |
| Sidebar / Panels | `#XXXXXX` | Panel Name |
| Keywords | `#XXXXXX` | Keyword Color Name |
| Functions | `#XXXXXX` | Hero Color Name |
| Strings | `#XXXXXX` | String Color Name |
| Types & Tags | `#XXXXXX` | Type Color Name |
| Numbers | `#XXXXXX` | Number Color Name |
| Constants & Booleans | `#XXXXXX` | Constant Color Name |
| Variables | `#XXXXXX` | Variable Color Name |
| Comments | `#XXXXXX` | Comment Color Name |
| Attributes | `#XXXXXX` | Attribute Color Name |
| Errors | `#XXXXXX` | Error Color Name |

## Key Ideas

- **[Spectrum phrase].** [Explanation].
- **[Hero color phrase].** [Explanation].
- **[Keyword strategy].** [Explanation].
- **Depth over borders.** Panels separated by shade, not lines.
- **[Cursor color] cursor.** [Visibility statement].
- **Pair with:** JetBrains Mono or Fira Code (ligature support).

See [<theme-name>-concept.md](<theme-name>-concept.md) for the full design rationale.
```

### 4. Write docs/<theme-name>-concept.md

Write to `<theme-name>/docs/<theme-name>-concept.md` (~130-150 lines). The concept document must read as a strong, original creative piece — not a template fill-in. Each section must be written with specificity and conviction rooted in the theme's unique origin (the reference image, real-world source, or creative direction). Generic filler phrases ("polished high-tech aesthetic", "vivid, focused, and alive") are prohibited — every sentence must justify its existence with concrete visual or emotional detail tied to this specific theme.

Follow this structure:

```markdown
# Theme Name — Color Scheme Concept

## Origin

[2-3 sentences establishing the real-world or artistic source of the theme. Be specific and visual: name the place, scene, time of day, material, or cultural reference that anchors this palette. This is not a marketing blurb — it is a precise description of the visual world the theme comes from.]

Example depth targets:
- "The image is a browser chrome at night — the active tab blazes in acid yellow-green (`#C8B800`), the kind of color a fluorescent tube makes when it's about to fail."
- "A dune at 4am shot on film: the sand holds warmth from the day (`#C4A86A`), the sky overhead is the specific cold blue of pre-dawn before any orange enters (`#7BB5D0`)."
- NOT: "A dark theme inspired by the desert." (too vague)

---

## Vision

[Theme name] is a coding color scheme drawn from [specific source]. The central tension is [specific visual or emotional conflict in the reference — warm vs. cold, synthetic vs. organic, ancient vs. electric, etc.].

It resolves this tension through [two/three] design decisions:

- **[Decision name]** — [Specific explanation referencing actual hex colors and the visual world they come from. e.g. "The background (`#181818`) is the exact darkness between two lit buildings at night — not pure black, which reads as a void, but dark enough that accent colors float."]
- **[Decision name]** — [Same specificity.]
- **[Decision name]** — [Same specificity.]

The result is a workspace that [concrete sensory or cognitive description — how the developer's eye moves, what they feel, what the environment reminds them of].

---

## Design Principles

### 1. [Name that describes this theme's unique color strategy — not a generic phrase]

[Paragraph grounded in the specific accent colors chosen. Name the hues, explain why each was chosen over alternatives, and connect each back to the reference source. e.g. "Brass was chosen over gold because gold reads as reward-state; brass reads as material — it is the color of things that have been handled, that have weight."]

### 2. [Name that describes this theme's syntax hierarchy approach]

[Explain how the most important tokens are ranked and why. Reference the reference source to justify the hierarchy. e.g. "Keywords are parchment-white because stone faces in desert photographs hold the most neutral light — they are the structural elements that everything else is measured against."] This creates a clear visual hierarchy:

| Role | Color | Hex | Why |
|---|---|---|---|
[One row per major syntax token. The "Why" column must reference the source material or a specific visual logic, not just "for contrast".]

### 3. Background as Stage, Not Void

[Explain the specific background philosophy for this theme — what the darkness means, what undertone it carries, and why `bg.secondary` is darker than `bg.primary`. Connect to the reference source.] Specifics:

- **Editor surface** (`[bg.primary hex]`) — [one sentence describing what this darkness evokes from the source].
- **Panel/sidebar** (`[bg.secondary hex]`) — [one sentence on why it's recessed and what it represents].
- **Highlight** (`[bg.highlight hex]`) — [one sentence on how selection/hover lift works in this visual world].
- **Errors** use [error color name] (`[hex]`) — [explain why this specific red/orange was chosen and why it doesn't cause anxiety].

### 4. The Cursor as Anchor

The caret uses [cursor color name] (`[hex]`). [Explain specifically why this color was chosen as the cursor — tie it to something unmissable in the reference source. e.g. "The amber cursor is the exact color of afternoon light catching the edge of a standing stone — the single hottest point in an otherwise cool frame. In the editor, it serves the same function: a fixed warm point your eye returns to."]

---

## Color Palette Summary

### Backgrounds & UI

| Component | Hex | Role |
|---|---|---|
[4 rows: primary bg, secondary bg, gutter, caret/selection]

### Syntax Tokens

| Token | Hex | Name |
|---|---|---|
[8 rows: keywords, functions, strings, types, numbers, constants, variables, comments]

### Supplementary Colors

| Use | Hex | Name |
|---|---|---|
[6-8 rows: attributes, errors, cursor, warnings, info, operators, string escapes]

---

## Typography Pairing

The "[Theme Name]" palette pairs with:

- **Primary:** JetBrains Mono — [one sentence on why this font specifically suits this theme's visual character, not just "clean geometry"].
- **Alternative:** Fira Code — [one sentence specific to this theme].

Ligatures like `=>`, `!==`, and `>=` [explain how ligatures interact with the mood of this specific theme — do they reinforce the mechanical? the flowing? the ancient?].

---

## How It Feels in Practice

Imagine opening a [specific file type that fits the theme] at [specific time of day or night that fits the source]:

[Write this as a single flowing paragraph, 6-10 sentences. Walk through the editor experience as if describing a physical space: the background first, then the eye's movement through keywords, functions, strings, types, numbers, comments, and finally the cursor. Use the theme's source material as sensory reference throughout. Avoid bullet points in this section — it must read as prose. End on the cursor.]

That's [Theme Name].
```

### 5. Write docs/<theme-name>-concept-th.md

Write to `<theme-name>/docs/<theme-name>-concept-th.md`. This is **not a translation** of the English concept document. It is an independent rewrite of the same content in Thai, using plain, direct language that is easy to read and understand. The goal is clarity and accessibility — not literary fidelity to the English version.

Rewrite rules:
- **Write in simple, neutral Thai.** Avoid poetic or literary constructions that feel awkward when translated from English. Write as if explaining the theme to a Thai developer who wants to understand the design decisions, not experience the prose style.
- **Preserve all factual content** — every design decision, color rationale, palette table, and typographic note must appear. Do not omit information, only simplify its expression.
- **Color names and hex codes** remain in English/uppercase exactly as written (`#00C840`, `Phosphor Green`, `Cobalt`). Do not translate color names.
- **Theme name** (kebab-case) remains unchanged. Do not translate it.
- **Technical terms** with no natural Thai equivalent (e.g. `gutter`, `inlay hint`, `ligature`) may be kept in English with a brief Thai clarification in parentheses on first use.
- **Section headings** are written in Thai. Use the same heading level (`##`, `###`) as the English original.
- **Tables** use Thai column headers and Thai cell content, except for color names and hex codes.
- **Markdown structure** (headings, tables, bullet lists, code spans, horizontal rules) must be preserved exactly.
- The file ends with the theme name as a closing line: e.g. `นั่นคือ legacy-radiance.`

The Thai concept file uses the same filename convention with a `-th` suffix:
```
<theme-name>/docs/<theme-name>-concept-th.md
```

## After creation

Remind the user that the following files still need to be created to complete the theme:
- `<theme-name>/editors/helix/<theme-name>.toml` + `-transparent.toml`
- `<theme-name>/editors/zed/extension.toml` + `themes/<theme-name>.json` + `LICENSE`
- Optionally `<theme-name>/terminals/rio/themes/<theme-name>.toml`
- Update root `README.md` with the new theme
