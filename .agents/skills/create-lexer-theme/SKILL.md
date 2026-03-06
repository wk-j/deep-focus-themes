---
name: create-lexer-theme
description: Generate a Lexer markdown reader theme TOML file for a theme that already has a palette JSON. Covers meta, colors, syntax, typography, and effects sections.
---

## What this skill does

Generate a Lexer theme TOML file from an existing palette JSON.

Output file: `<theme-name>/editors/lexer/<theme-name>.toml`

The file is a complete Lexer custom theme covering all documented TOML sections: `[meta]`, `[colors]`, `[syntax]`, `[typography]`, and `[effects]`.

---

## Inputs

The user provides:
- **Theme name** (kebab-case, e.g. `neon-city`)
- **Palette JSON** at `<theme-name>/palette/<theme-name>.json` — the canonical color source

Always read the palette file before generating any TOML. All colors must be derived from the palette's `colors` or `semantic_roles` objects.

---

## Lexer theme format reference

Lexer is a desktop markdown reader built with Tauri. Themes are single TOML files that map to CSS custom properties. The engine parses the TOML, merges missing values from a base theme (`lexer-dark` or `lexer-light`), and generates a `:root {}` CSS block injected into the webview.

File lookup order:
1. `~/.config/lexer/themes/{name}.toml` (user themes)
2. `$LEXER_THEMES_DIR/{name}.toml` (env override)
3. Built-in themes (embedded in binary)

Themes are hot-reloaded: save the TOML and the app updates instantly.

---

## TOML sections

### `[meta]`

```toml
[meta]
name = "Theme Display Name"    # Human-readable name for the theme picker
author = "wk"                  # Author name
base = "dark"                  # "dark" or "light" — inherit missing values from this
version = "1.0.0"              # Optional semver
```

All deep-focus themes are dark themes, so always use `base = "dark"`.

### `[colors]`

App chrome and UI surface colors. Every value is a CSS color string (hex, `rgba()`, `var()` references, or CSS values like `transparent`).

| TOML Field | Description | Mapping strategy |
|---|---|---|
| `bg_base` | Outermost background | `"transparent"` (enables vibrancy/blur) |
| `bg_base_opaque` | Opaque fallback for text-on-accent | `colors.bg.primary` |
| `bg_panel` | Content panel background | `colors.bg.primary` as `rgba()` with ~0.55 alpha |
| `bg_panel_border` | Panel border | `colors.bg.border` as `rgba()` with ~0.10 alpha |
| `text_primary` | Primary text | `colors.fg.primary` |
| `text_secondary` | Secondary text | `colors.fg.dimmed` |
| `text_muted` | Muted text | `colors.fg.muted` |
| `accent` | Primary accent (buttons, active states) | `semantic_roles.cursor` color |
| `link` | Link color | `semantic_roles.functions` color |
| `link_hover` | Link hover color | Lightened variant of `link` |
| `gradient_a` | Gradient mesh layer 1 | Primary accent as `rgba()` with ~0.08 alpha |
| `gradient_b` | Gradient mesh layer 2 | Secondary accent as `rgba()` with ~0.06 alpha |
| `gradient_c` | Gradient mesh layer 3 | Tertiary accent as `rgba()` with ~0.05 alpha |
| `code_bg` | Code block background | `colors.bg.secondary` as `rgba()` with ~0.45 alpha |
| `code_border` | Code block border | `colors.bg.border` as `rgba()` with ~0.08 alpha |
| `glow_color` | Ambient glow on code hover | Primary accent as `rgba()` with ~0.25 alpha |
| `glow_radius` | Glow blur radius | `"20px"` |
| `blockquote_border` | Blockquote left border | `semantic_roles.functions` color |
| `blockquote_bg` | Blockquote background | `semantic_roles.functions` color as `rgba()` with ~0.08 alpha |
| `hr_color` | Horizontal rule | `colors.bg.border` as `rgba()` with ~0.6 alpha |
| `table_header_bg` | Table header background | `colors.fg.muted` as `rgba()` with ~0.12 alpha |
| `table_border` | Table border | `colors.fg.muted` as `rgba()` with ~0.15 alpha |
| `table_row_alt` | Alternating table row | `colors.fg.muted` as `rgba()` with ~0.04 alpha |
| `spotlight_color` | Cursor spotlight radial glow | `"rgba(255, 255, 255, 0.02)"` |
| `heading_gradient` | Heading gradient text fill | `"linear-gradient(135deg, var(--accent), var(--text-primary))"` |
| `select_bar` | Block select left bar | `"var(--accent)"` |
| `select_bg` | Block select background | Primary accent as `rgba()` with ~0.08 alpha |
| `select_cursor_bar` | Cursor block left bar | `"var(--text-primary)"` |
| `select_cursor_bg` | Cursor block background | Primary accent as `rgba()` with ~0.15 alpha |
| `select_bar_width` | Selection bar width | `"3px"` |
| `select_bar_offset` | Selection bar offset | `"-16px"` |

#### Converting hex to rgba

When a palette hex color needs an alpha channel, convert `#RRGGBB` to `rgba(R, G, B, alpha)`.
For example: `#FF2CF1` at 0.08 alpha becomes `"rgba(255, 44, 241, 0.08)"`.

### `[syntax]`

Tree-sitter highlight token colors. These map to `.hl-{token}` CSS classes in rendered code blocks.

| TOML Field | Mapping |
|---|---|
| `keyword` | `semantic_roles.keywords` |
| `string` | `semantic_roles.strings` |
| `comment` | `semantic_roles.comments` |
| `function` | `semantic_roles.functions` |
| `type` | `semantic_roles.types` |
| `number` | `semantic_roles.literals` |
| `operator` | `semantic_roles.operators` |
| `variable` | `colors.fg.primary` |
| `punctuation` | `colors.fg.dimmed` |
| `constant` | `semantic_roles.constants` |
| `tag` | `semantic_roles.tags` |
| `attribute` | `semantic_roles.attributes` |
| `property` | `semantic_roles.types` |
| `constructor` | `semantic_roles.constructors` |
| `embedded` | `colors.fg.primary` |

All values are quoted 6-digit hex strings (e.g. `"#FF2CF1"`).

### `[typography]`

All fields optional. Only emit fields that differ from defaults. Since deep-focus themes are designed for JetBrains Mono / Fira Code:

```toml
[typography]
font_family_mono = "'JetBrains Mono', 'Fira Code', 'SF Mono', monospace"
code_font_size = 14
```

Typically omit `font_family`, `font_size`, and `line_height` to use Lexer's sensible defaults.

### `[effects]`

Boolean toggles and tuning for visual effects.

| TOML Field | Type | Description | Default |
|---|---|---|---|
| `frosted_glass` | bool | Backdrop blur on panels | `true` |
| `gradient_backdrop` | bool | Gradient mesh background | `true` |
| `noise_texture` | bool | Noise overlay | `true` |
| `heading_gradient_text` | bool | Gradient fill on h1-h3 | `true` |
| `scroll_animations` | bool | Fade-in on scroll | `true` |
| `frosted_blur` | string | Blur radius (e.g. `"20px"`) | from base |
| `frosted_saturate` | string | Saturation boost (e.g. `"180%"`) | from base |
| `noise_opacity` | float | Noise opacity (0.0-1.0) | from base |

For dark themes, enable all visual effects. Adjust `frosted_saturate` based on palette saturation — highly saturated palettes benefit from lower saturate values (~`"150%"`), while desaturated palettes can use higher values (~`"200%"`).

---

## Color mapping procedure

1. Read the palette JSON file.
2. Resolve all `semantic_roles` dot-path references into `colors` to get actual hex values.
3. For `[colors]` section, convert hex values to appropriate CSS formats:
   - Solid hex for opaque values (`bg_base_opaque`, `text_primary`, etc.)
   - `rgba()` for semi-transparent values (`bg_panel`, `code_bg`, gradients, etc.)
   - CSS variables for self-referencing values (`select_bar`, `heading_gradient`)
4. For `[syntax]` section, use resolved hex values directly.
5. For `[effects]`, enable all effects and tune based on palette character.

### Deriving gradient mesh colors

Choose 3 visually distinct accent colors from the palette for the gradient mesh layers:
- `gradient_a`: The primary accent / cursor color at ~0.08 alpha
- `gradient_b`: A secondary accent (e.g. functions or types color) at ~0.06 alpha
- `gradient_c`: A tertiary accent (e.g. strings or a contrasting color) at ~0.05 alpha

The goal is a subtle, multi-hue backdrop that adds depth without distracting from content.

---

## Output file format

```toml
# <Theme Display Name> — Lexer Theme
# <one-line description from palette>

[meta]
name = "<Theme Display Name>"
author = "wk"
base = "dark"
version = "1.0.0"

[colors]
# App chrome
bg_base = "transparent"
bg_base_opaque = "<hex>"
bg_panel = "<rgba>"
bg_panel_border = "<rgba>"
text_primary = "<hex>"
text_secondary = "<hex>"
text_muted = "<hex>"
accent = "<hex>"
link = "<hex>"
link_hover = "<hex>"

# Gradient mesh backdrop
gradient_a = "<rgba>"
gradient_b = "<rgba>"
gradient_c = "<rgba>"

# Code blocks
code_bg = "<rgba>"
code_border = "<rgba>"
glow_color = "<rgba>"
glow_radius = "20px"

# Content elements
blockquote_border = "<hex>"
blockquote_bg = "<rgba>"
hr_color = "<rgba>"
table_header_bg = "<rgba>"
table_border = "<rgba>"
table_row_alt = "<rgba>"

# Cursor spotlight
spotlight_color = "rgba(255, 255, 255, 0.02)"

# Heading gradient
heading_gradient = "linear-gradient(135deg, var(--accent), var(--text-primary))"

# Block select
select_bar = "var(--accent)"
select_bg = "<rgba>"
select_cursor_bar = "var(--text-primary)"
select_cursor_bg = "<rgba>"
select_bar_width = "3px"
select_bar_offset = "-16px"

[syntax]
keyword = "<hex>"
string = "<hex>"
comment = "<hex>"
function = "<hex>"
type = "<hex>"
number = "<hex>"
operator = "<hex>"
variable = "<hex>"
punctuation = "<hex>"
constant = "<hex>"
tag = "<hex>"
attribute = "<hex>"
property = "<hex>"
constructor = "<hex>"
embedded = "<hex>"

[typography]
font_family_mono = "'JetBrains Mono', 'Fira Code', 'SF Mono', monospace"
code_font_size = 14

[effects]
frosted_glass = true
gradient_backdrop = true
noise_texture = true
heading_gradient_text = true
scroll_animations = true
frosted_blur = "20px"
frosted_saturate = "<value>"
noise_opacity = 0.035
```

### Formatting rules

- Standard TOML formatting with inline comments for clarity.
- Hex colors: 6-digit lowercase in TOML values (Lexer convention — CSS custom properties are case-insensitive). Use the palette's original casing if it is already lowercase; otherwise lowercase.
- `rgba()` values: use spaces after commas for readability: `rgba(13, 2, 33, 0.55)`.
- Group related keys with blank lines and `# Comment` headers matching the template above.
- Use `snake_case` for all TOML keys (Lexer convention).
- String values are double-quoted.
- Boolean and numeric values are bare (no quotes).
- Column-align values within each group for readability.

---

## File location

Write the output to:

```
<theme-name>/editors/lexer/<theme-name>.toml
```

Create the directory `<theme-name>/editors/lexer/` if it does not exist.

---

## After generation

1. Show a color mapping summary table:

   | Section | Key | Source | Value |
   |---|---|---|---|
   | colors | `accent` | `semantic_roles.cursor` → `accent.cyan` | `#00FFFF` |
   | syntax | `keyword` | `semantic_roles.keywords` → `accent.white` | `#FFFFFF` |
   | ... | ... | ... | ... |

2. Remind the user how to deploy:

   ```bash
   mkdir -p ~/.config/lexer/themes
   cp <theme-name>/editors/lexer/<theme-name>.toml ~/.config/lexer/themes/
   ```

   Then select the theme with `Space t` in Lexer, or launch with:
   ```bash
   lexer --theme <theme-name>
   ```

   The theme is hot-reloaded — save the TOML and the app updates instantly.

3. Remind the user to update the `deploy-themes` skill's **Current Theme Inventory** table if they want this theme deployed automatically.
