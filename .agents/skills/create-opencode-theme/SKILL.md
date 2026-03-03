---
name: create-opencode-theme
description: Generate a complete opencode TUI theme JSON file for a theme that already has a palette JSON. Covers all UI, markdown, syntax, and diff keys.
---

## What this skill does

Generate an opencode theme JSON file from an existing palette JSON.

Output file: `<theme-name>/editors/opencode/<theme-name>.json`

The file is a complete opencode custom theme covering every documented theme key.

---

## Inputs

The user provides:
- **Theme name** (kebab-case, e.g. `tallow-light`)
- **Palette JSON** at `<theme-name>/palette/<theme-name>.json` — the canonical color source

Always read the palette file before generating any JSON. All colors must be derived from the palette's `colors` or `semantic_roles` objects.

---

## Opencode theme format reference

See built-in theme examples for reference: https://github.com/anomalyco/opencode/tree/dev/packages/opencode/src/cli/cmd/tui/context/theme

### File structure

```json
{
  "$schema": "https://opencode.ai/theme.json",
  "defs": {
    "<name>": "<hex>"
  },
  "theme": {
    "<key>": { "dark": "<color>", "light": "<color>" }
  }
}
```

- **`defs`** — named color aliases. Every palette color gets an entry here using its `snake_case` name from the palette. Reference them by name string in `theme` values.
- **`theme`** — every UI key, each with `"dark"` and `"light"` variants.
- Color values can be: a def name (string), a hex string (`"#FF2CF1"`), an ANSI index integer (`3`), or `"none"` for terminal default.
- Since all deep-focus themes are dark themes, both `"dark"` and `"light"` variants use the same palette colors (dark palette for both). Do not invent a separate light palette.

### `defs` section

Define every color from the palette as a named entry. Use the palette's own `snake_case` key names:

```json
"defs": {
  "bg_primary":   "#XXXXXX",
  "bg_secondary": "#XXXXXX",
  "bg_highlight": "#XXXXXX",
  "border":       "#XXXXXX",
  "fg_primary":   "#XXXXXX",
  "fg_dimmed":    "#XXXXXX",
  "fg_muted":     "#XXXXXX",
  "fg_gutter":    "#XXXXXX",
  "<accent_1>":   "#XXXXXX",
  "<accent_2>":   "#XXXXXX",
  ...all accent colors...,
  ...all ansi colors...
}
```

Map palette paths to def names:
- `colors.bg.primary` → `"bg_primary"`
- `colors.bg.secondary` → `"bg_secondary"`
- `colors.bg.highlight` → `"bg_highlight"`
- `colors.bg.border` → `"border"`
- `colors.fg.primary` → `"fg_primary"`
- `colors.fg.dimmed` → `"fg_dimmed"`
- `colors.fg.muted` → `"fg_muted"`
- `colors.fg.gutter` → `"fg_gutter"`
- `colors.accent.*` → use the accent key name directly (e.g. `"tallow"`, `"ember"`)
- `colors.ansi.*` → use `"ansi_<name>"` (e.g. `"ansi_red"`, `"ansi_bright_green"`)

---

## Color key mapping

Resolve all semantic roles from `semantic_roles` first, then apply the mapping below.

### Core UI

| Key | Maps to | Notes |
|---|---|---|
| `primary` | `semantic_roles.cursor` | Primary accent — buttons, active elements |
| `secondary` | `semantic_roles.types` | Secondary accent |
| `accent` | `semantic_roles.attributes` | Tertiary accent |
| `error` | `semantic_roles.errors` | Error state |
| `warning` | `colors.accent` color closest to orange/yellow | Warning state |
| `success` | `semantic_roles.strings` | Success state |
| `info` | `semantic_roles.types` | Info state |
| `text` | `colors.fg.primary` | Default foreground |
| `textMuted` | `colors.fg.muted` | Dimmed/secondary text |
| `background` | `"none"` | Empty chat area — transparent, lets terminal wallpaper show through below content |
| `backgroundPanel` | `colors.bg.primary` | Sidebar and panel chrome — solid, visually anchors the UI structure |
| `backgroundElement` | `colors.bg.highlight` | Code block background — solid, distinct from transparent background so blocks don't blend in |
| `border` | `colors.bg.border` | Inactive border |
| `borderActive` | `semantic_roles.cursor` | Focused panel border |
| `borderSubtle` | `colors.bg.border` | Subtle/decorative border |

### Diff

| Key | Maps to |
|---|---|
| `diffAdded` | `semantic_roles.strings` |
| `diffRemoved` | `semantic_roles.errors` |
| `diffContext` | `colors.fg.muted` |
| `diffHunkHeader` | `colors.fg.muted` |
| `diffHighlightAdded` | `semantic_roles.strings` |
| `diffHighlightRemoved` | `semantic_roles.errors` |
| `diffAddedBg` | `colors.bg.highlight` (hex directly, not def reference — needs to be a subtle bg) |
| `diffRemovedBg` | `colors.bg.highlight` (same rationale) |
| `diffContextBg` | `colors.bg.secondary` |
| `diffLineNumber` | `colors.fg.gutter` |
| `diffAddedLineNumberBg` | `colors.bg.highlight` |
| `diffRemovedLineNumberBg` | `colors.bg.highlight` |

### Markdown

| Key | Maps to |
|---|---|
| `markdownText` | `colors.fg.primary` |
| `markdownHeading` | `semantic_roles.keywords` |
| `markdownLink` | `semantic_roles.functions` |
| `markdownLinkText` | `semantic_roles.types` |
| `markdownCode` | `semantic_roles.strings` |
| `markdownBlockQuote` | `colors.fg.muted` |
| `markdownEmph` | `semantic_roles.attributes` |
| `markdownStrong` | `semantic_roles.keywords` |
| `markdownHorizontalRule` | `colors.bg.border` |
| `markdownListItem` | `semantic_roles.functions` |
| `markdownListEnumeration` | `semantic_roles.types` |
| `markdownImage` | `semantic_roles.functions` |
| `markdownImageText` | `semantic_roles.types` |
| `markdownCodeBlock` | `colors.fg.primary` |

### Syntax

| Key | Maps to |
|---|---|
| `syntaxComment` | `semantic_roles.comments` |
| `syntaxKeyword` | `semantic_roles.keywords` |
| `syntaxFunction` | `semantic_roles.functions` |
| `syntaxVariable` | `colors.fg.primary` |
| `syntaxString` | `semantic_roles.strings` |
| `syntaxNumber` | `semantic_roles.literals` |
| `syntaxType` | `semantic_roles.types` |
| `syntaxOperator` | `semantic_roles.operators` |
| `syntaxPunctuation` | `colors.fg.dimmed` |

---

## Output file format

```json
{
  "$schema": "https://opencode.ai/theme.json",

  "defs": {
    "bg_primary":   "#XXXXXX",
    "bg_secondary": "#XXXXXX",
    "bg_highlight": "#XXXXXX",
    "border":       "#XXXXXX",
    "fg_primary":   "#XXXXXX",
    "fg_dimmed":    "#XXXXXX",
    "fg_muted":     "#XXXXXX",
    "fg_gutter":    "#XXXXXX",
    "<accent_1>":   "#XXXXXX",
    ...
  },

  "theme": {
    "primary":            { "dark": "<def_name>", "light": "<def_name>" },
    "secondary":          { "dark": "<def_name>", "light": "<def_name>" },
    "accent":             { "dark": "<def_name>", "light": "<def_name>" },
    "error":              { "dark": "<def_name>", "light": "<def_name>" },
    "warning":            { "dark": "<def_name>", "light": "<def_name>" },
    "success":            { "dark": "<def_name>", "light": "<def_name>" },
    "info":               { "dark": "<def_name>", "light": "<def_name>" },
    "text":               { "dark": "<def_name>", "light": "<def_name>" },
    "textMuted":          { "dark": "<def_name>", "light": "<def_name>" },
    "background":        { "dark": "none",         "light": "none" },
    "backgroundPanel":   { "dark": "bg_primary",  "light": "bg_primary" },
    "backgroundElement": { "dark": "bg_highlight", "light": "bg_highlight" },
    "border":             { "dark": "<def_name>", "light": "<def_name>" },
    "borderActive":       { "dark": "<def_name>", "light": "<def_name>" },
    "borderSubtle":       { "dark": "<def_name>", "light": "<def_name>" },

    "diffAdded":                { "dark": "<def_name>", "light": "<def_name>" },
    "diffRemoved":              { "dark": "<def_name>", "light": "<def_name>" },
    "diffContext":              { "dark": "<def_name>", "light": "<def_name>" },
    "diffHunkHeader":           { "dark": "<def_name>", "light": "<def_name>" },
    "diffHighlightAdded":       { "dark": "<def_name>", "light": "<def_name>" },
    "diffHighlightRemoved":     { "dark": "<def_name>", "light": "<def_name>" },
    "diffAddedBg":              { "dark": "<hex>",      "light": "<hex>" },
    "diffRemovedBg":            { "dark": "<hex>",      "light": "<hex>" },
    "diffContextBg":            { "dark": "<def_name>", "light": "<def_name>" },
    "diffLineNumber":           { "dark": "<def_name>", "light": "<def_name>" },
    "diffAddedLineNumberBg":    { "dark": "<hex>",      "light": "<hex>" },
    "diffRemovedLineNumberBg":  { "dark": "<hex>",      "light": "<hex>" },

    "markdownText":             { "dark": "<def_name>", "light": "<def_name>" },
    "markdownHeading":          { "dark": "<def_name>", "light": "<def_name>" },
    "markdownLink":             { "dark": "<def_name>", "light": "<def_name>" },
    "markdownLinkText":         { "dark": "<def_name>", "light": "<def_name>" },
    "markdownCode":             { "dark": "<def_name>", "light": "<def_name>" },
    "markdownBlockQuote":       { "dark": "<def_name>", "light": "<def_name>" },
    "markdownEmph":             { "dark": "<def_name>", "light": "<def_name>" },
    "markdownStrong":           { "dark": "<def_name>", "light": "<def_name>" },
    "markdownHorizontalRule":   { "dark": "<def_name>", "light": "<def_name>" },
    "markdownListItem":         { "dark": "<def_name>", "light": "<def_name>" },
    "markdownListEnumeration":  { "dark": "<def_name>", "light": "<def_name>" },
    "markdownImage":            { "dark": "<def_name>", "light": "<def_name>" },
    "markdownImageText":        { "dark": "<def_name>", "light": "<def_name>" },
    "markdownCodeBlock":        { "dark": "<def_name>", "light": "<def_name>" },

    "syntaxComment":            { "dark": "<def_name>", "light": "<def_name>" },
    "syntaxKeyword":            { "dark": "<def_name>", "light": "<def_name>" },
    "syntaxFunction":           { "dark": "<def_name>", "light": "<def_name>" },
    "syntaxVariable":           { "dark": "<def_name>", "light": "<def_name>" },
    "syntaxString":             { "dark": "<def_name>", "light": "<def_name>" },
    "syntaxNumber":             { "dark": "<def_name>", "light": "<def_name>" },
    "syntaxType":               { "dark": "<def_name>", "light": "<def_name>" },
    "syntaxOperator":           { "dark": "<def_name>", "light": "<def_name>" },
    "syntaxPunctuation":        { "dark": "<def_name>", "light": "<def_name>" }
  }
}
```

### Formatting rules

- 2-space indentation, no trailing commas.
- Hex colors in `defs`: 6-digit uppercase (`#FF2CF1`).
- `defs` keys: `snake_case`.
- `theme` keys: `camelCase` (as per opencode schema).
- `defs` values are column-aligned within groups (bg, fg, accents, ansi).
- `diffAddedBg`, `diffRemovedBg`, `diffAddedLineNumberBg`, `diffRemovedLineNumberBg` use inline hex strings rather than def references, since they benefit from a slightly different shade than the standard `bg_highlight` (same hex is fine if it fits).

---

## File location

Write the output to:

```
<theme-name>/editors/opencode/<theme-name>.json
```

Create the directory `<theme-name>/editors/opencode/` if it does not exist.

---

## After generation

1. Show a color mapping summary table:

   | Key group | Key | Def name | Hex |
   |---|---|---|---|
   | Core | `primary` | e.g. `tallow` | `#E8B050` |
   | ... | ... | ... | ... |

2. Remind the user how to deploy:

   **User-wide (recommended):**
   ```bash
   mkdir -p ~/.config/opencode/themes
   cp <theme-name>/editors/opencode/<theme-name>.json ~/.config/opencode/themes/
   ```

   Then activate in `~/.config/opencode/tui.json`:
   ```json
   {
     "$schema": "https://opencode.ai/tui.json",
     "theme": "<theme-name>"
   }
   ```

   **Or directly edit the existing `tui.json`** — replace the `"theme"` value in place.

3. Update the following files:
   - `<theme-name>/docs/README.md` — add an opencode bullet under Key Ideas
   - Root `README.md` — add `opencode` column to the support matrix
   - `generate_pages.py` — `detect_support()` checks for `editors/opencode/`
   - `.agents/skills/deploy-themes/SKILL.md` — add opencode deployment section and inventory column
