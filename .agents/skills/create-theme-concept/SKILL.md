---
name: create-theme-concept
description: Create a complete theme concept specification from a creative direction, reference image, or both. Extracts colors from images, proposes a theme name, and generates palette JSON, docs README, and concept document.
---

## What this skill does

Generate the three foundational files that define a new theme:

1. `<theme-name>/palette/<theme-name>.json` — canonical color palette
2. `<theme-name>/docs/README.md` — theme overview
3. `<theme-name>/docs/<theme-name>-concept.md` — full design rationale

## Inputs

The user may provide any combination of:
- **An image** — a screenshot, photograph, artwork, or any visual reference. Extract the dominant colors, mood, and atmosphere from the image to drive the palette design.
- **A theme name** (kebab-case, e.g. `solar-drift`) — optional. If not provided, propose a name based on the image mood and colors.
- **Creative direction** — mood, inspiration, color family, or any descriptive guidance. Optional if an image is provided.

### When an image is provided

1. Analyze the image to identify the dominant colors, color temperature, mood, and atmosphere.
2. Extract key hex colors from the image as starting points for accents.
3. If no theme name is given, propose an evocative kebab-case name that captures the image's mood (e.g. a sunset cityscape might become `ember-skyline`, a frozen lake might become `glacier-dusk`). Present the proposed name to the user for confirmation before generating files.
4. Adapt extracted colors for code readability — raw image colors may need saturation or lightness adjustments to work on dark backgrounds without halation or low contrast.

### When only a creative direction is provided

Design colors from scratch based on the described mood, inspiration, or color family.

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

Write to `<theme-name>/docs/<theme-name>-concept.md` (~100-112 lines). Follow this exact structure:

```markdown
# Theme Name — Color Scheme Concept

## Vision

[Theme name] is a high-performance coding color scheme built for [audience]. The philosophy is simple: [base quality] meets [accent quality].

It achieves this through [two/three] complementary ideas:

- **[Base name]** — [description of background philosophy and undertone].
- **[Spectrum name]** — [description of accent strategy with hex codes inline].
- **[Keyword strategy]** — [description of keyword approach].

The result is a workspace that feels [evocative description].

---

## Design Principles

### 1. [Spectrum Philosophy Name]

[Paragraph explaining how colors differentiate syntax roles].

### 2. [Hierarchy Strategy Name]

[Intro paragraph about keyword strategy]. This creates a clear visual hierarchy:

| Role | Color | Hex | Why |
|---|---|---|---|
[One row per major syntax token with rationale]

### 3. Minimal Chrome, Maximum Depth

- **No harsh borders.** Panel separation comes from background color shifts ([bg.primary hex] for editor, [bg.secondary hex] for sidebar/panels).
- **Active tab indicator.** A single [accent color] marks the active file.
- **Restrained error states.** Errors use [error color name] (`[hex]`) — clearly an error, but tuned to avoid anxiety.

### 4. The Cursor as Anchor

The caret and selection both use [cursor color] (`[hex]`). In a scheme this dark, the cursor must be unmissable. It serves as the constant anchor point.

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

The "[Theme Name]" identity is reinforced by pairing the palette with modern monospace fonts that support programming ligatures:

- **Primary recommendation:** JetBrains Mono — clean geometry, optimized for code readability at small sizes.
- **Alternative:** Fira Code — excellent ligature set (arrows, comparisons, lambda).

Ligatures like `=>`, `!==`, and `>=` rendered as single glyphs contribute to the polished, high-tech aesthetic the scheme targets.

---

## How It Feels in Practice

Imagine opening a [file type] file at [late hour]:

- The background is [evocative description of bg].
- Your eye lands on [keyword/function description].
- [Walk through each major syntax color in one flowing paragraph].
- [Describe neutral elements].
- Comments are there if you look — [description].
- Your cursor [verb] in [color]. You always know where you are.

That's [Theme Name].
```

## After creation

Remind the user that the following files still need to be created to complete the theme:
- `<theme-name>/editors/helix/<theme-name>.toml` + `-transparent.toml`
- `<theme-name>/editors/zed/extension.toml` + `themes/<theme-name>.json` + `LICENSE`
- Optionally `<theme-name>/terminals/rio/themes/<theme-name>.toml`
- Update root `README.md` with the new theme
