---
name: create-helix-theme
description: Generate complete Helix editor theme files (base + transparent variant) for a theme that already has a palette JSON. Covers every Helix scope including rainbow brackets.
---

## What this skill does

Generate two Helix theme files from an existing palette:

1. `<theme-name>/editors/helix/<theme-name>.toml` — full opaque theme
2. `<theme-name>/editors/helix/<theme-name>-transparent.toml` — transparent variant

Both files must cover **every Helix scope** documented below, including rainbow bracket scopes.

---

## Inputs

The user provides:
- **Theme name** (kebab-case, e.g. `neon-city`) — used for filenames and the `inherits` key
- **Palette JSON** at `<theme-name>/palette/<theme-name>.json` — the canonical color source

Always read the palette file before generating any TOML. All palette color names used in the TOML must come from the palette's `colors` object. Map them to flat `snake_case` names for the `[palette]` section.

---

## File 1 — Base theme (`<theme-name>.toml`)

### Header

```toml
# Theme Name — Helix Editor Theme
# <one-line description matching the palette description>
```

### Section order

```
1. Syntax Highlighting
2. Interface / UI
3. [palette]
```

Each section is preceded by a box-drawing comment header:

```toml
# ─── Syntax Highlighting ─────────────────────────────────────────────────────
```

---

### Section 1 — Syntax Highlighting

Cover every scope in this exact grouping order. Within each group, list the parent scope first, then all sub-scopes. Use the palette's `semantic_roles` to assign the dominant color for each role, then apply it consistently to all child scopes unless a child has a documented differentiation (e.g. `constant.character.escape` uses `string_escape` rather than the constants color).

#### Attributes

```toml
attribute = { fg = "<attr_color>", modifiers = ["italic"] }
```

#### Types

```toml
type                  = { fg = "<type_color>" }
"type.builtin"        = { fg = "<type_color>" }
"type.parameter"      = { fg = "<type_color>", modifiers = ["italic"] }
"type.enum"           = { fg = "<type_color>" }
"type.enum.variant"   = { fg = "<type_color>" }
```

#### Constructor

```toml
constructor = { fg = "<type_color>" }
```

Constructor is type-adjacent — use the same color as `type`.

#### Constants

```toml
constant                    = { fg = "<constant_color>" }
"constant.builtin"          = { fg = "<constant_color>" }
"constant.builtin.boolean"  = { fg = "<constant_color>" }
"constant.character"        = { fg = "<constant_color>" }
"constant.character.escape" = { fg = "<escape_color>" }
"constant.numeric"          = { fg = "<number_color>" }
"constant.numeric.integer"  = { fg = "<number_color>" }
"constant.numeric.float"    = { fg = "<number_color>" }
```

`constant.character.escape` uses the string-escape/regex color. `constant.numeric` uses the numbers color (may differ from booleans/constants).

#### Strings

```toml
string                       = { fg = "<string_color>" }
"string.regexp"              = { fg = "<escape_color>" }
"string.special"             = { fg = "<string_color>" }
"string.special.path"        = { fg = "<string_color>" }
"string.special.url"         = { fg = "<string_color>", underline = { style = "line" } }
"string.special.symbol"      = { fg = "<attr_color>" }
```

#### Comments

```toml
comment                        = { fg = "<comment_color>", modifiers = ["italic"] }
"comment.line.documentation"   = { fg = "<comment_color>", modifiers = ["italic"] }
"comment.block.documentation"  = { fg = "<comment_color>", modifiers = ["italic"] }
"comment.unused"               = { fg = "gutter_fg", modifiers = ["italic"] }
```

`comment.unused` is always `gutter_fg` — most recessive foreground.

#### Variables

```toml
variable                          = { fg = "<var_color>" }
"variable.builtin"                = { fg = "<var_color>", modifiers = ["italic"] }
"variable.parameter"              = { fg = "<var_color>", modifiers = ["italic"] }
"variable.other"                  = { fg = "<var_color>" }
"variable.other.member"           = { fg = "<member_color>" }
"variable.other.member.private"   = { fg = "<member_color>", modifiers = ["italic"] }
```

`variable.other.member` uses the dimmed foreground or a muted accent to distinguish fields from locals.

#### Labels

```toml
label = { fg = "<label_color>" }
```

Use a distinctive accent (often the hero color or a bright secondary).

#### Punctuation & Rainbow Brackets

The base `punctuation.bracket` key provides the **fallback** color when rainbow brackets are disabled or not matched. The `rainbow.bracket` keys provide **6 rotating colors** when `editor.rainbow-brackets = true` is set in Helix config.

```toml
punctuation               = { fg = "<punct_color>" }
"punctuation.delimiter"   = { fg = "<punct_color>" }
"punctuation.bracket"     = { fg = "<punct_color>" }
"punctuation.special"     = { fg = "<hero_color>" }

# Rainbow brackets (6 levels, rotate with nesting depth)
"rainbow.bracket"   = { fg = "<punct_color>" }
"rainbow.bracket.1" = { fg = "<rb1>" }
"rainbow.bracket.2" = { fg = "<rb2>" }
"rainbow.bracket.3" = { fg = "<rb3>" }
"rainbow.bracket.4" = { fg = "<rb4>" }
"rainbow.bracket.5" = { fg = "<rb5>" }
"rainbow.bracket.6" = { fg = "<rb6>" }
```

**Rainbow bracket color selection rules:**
- Use 6 distinct accent colors from the palette — never repeat a color within the 6 levels.
- Order them so adjacent levels are maximally different in hue (not just value/saturation).
- Avoid using the error color or the comment color (they carry semantic meaning).
- Level 1 should be the most prominent accent (hero color or close) — it is the outermost bracket.
- Ensure all 6 colors have adequate contrast against `bg_primary`.
- Example mapping strategy: hero → type_color → string_color → attr_color → number_color → constant_color (adjust to the specific palette).

#### Keywords

```toml
keyword                       = { fg = "<keyword_color>", modifiers = ["bold"] }
"keyword.control"             = { fg = "<keyword_color>", modifiers = ["bold"] }
"keyword.control.conditional" = { fg = "<keyword_color>", modifiers = ["bold"] }
"keyword.control.repeat"      = { fg = "<keyword_color>", modifiers = ["bold"] }
"keyword.control.import"      = { fg = "<keyword_color>", modifiers = ["bold"] }
"keyword.control.return"      = { fg = "<keyword_color>", modifiers = ["bold", "italic"] }
"keyword.control.exception"   = { fg = "<keyword_color>", modifiers = ["bold"] }
"keyword.operator"            = { fg = "<keyword_color>", modifiers = ["bold"] }
"keyword.directive"           = { fg = "<keyword_color>", modifiers = ["bold"] }
"keyword.function"            = { fg = "<keyword_color>", modifiers = ["bold"] }
"keyword.storage.type"        = { fg = "<keyword_color>", modifiers = ["bold"] }
"keyword.storage.modifier"    = { fg = "<keyword_color>", modifiers = ["bold"] }
```

Keywords are always `bold`. `keyword.control.return` adds `italic` to signal flow-exit.

#### Operators

```toml
operator = { fg = "<punct_color>" }
```

Operators use the same color as punctuation — they are structural, not semantic.

#### Functions

```toml
function                    = { fg = "<func_color>" }
"function.builtin"          = { fg = "<func_color>" }
"function.method"           = { fg = "<func_color>" }
"function.method.private"   = { fg = "<func_color>", modifiers = ["italic"] }
"function.macro"            = { fg = "<func_color>" }
"function.special"          = { fg = "<func_color>" }
```

Functions use the hero color — the most visually dominant accent.

#### Tags

```toml
tag           = { fg = "<type_color>" }
"tag.builtin" = { fg = "<type_color>" }
```

Tags are type-adjacent — use the same color as `type`.

#### Namespace

```toml
namespace = { fg = "<func_color>", modifiers = ["italic"] }
```

Namespace uses the function/hero color with `italic` to reduce visual weight.

#### Special

```toml
special = { fg = "<attr_color>" }
```

#### Markup

```toml
"markup.heading"           = { fg = "<keyword_color>", modifiers = ["bold"] }
"markup.heading.marker"    = { fg = "<punct_color>" }
"markup.heading.1"         = { fg = "<keyword_color>", modifiers = ["bold"] }
"markup.heading.2"         = { fg = "<keyword_color>", modifiers = ["bold"] }
"markup.heading.3"         = { fg = "<type_color>", modifiers = ["bold"] }
"markup.heading.4"         = { fg = "<type_color>" }
"markup.heading.5"         = { fg = "<func_color>" }
"markup.heading.6"         = { fg = "<func_color>" }
"markup.list"              = { fg = "<func_color>" }
"markup.list.unnumbered"   = { fg = "<func_color>" }
"markup.list.numbered"     = { fg = "<number_color>" }
"markup.list.checked"      = { fg = "<string_color>" }
"markup.list.unchecked"    = { fg = "<punct_color>" }
"markup.bold"              = { modifiers = ["bold"] }
"markup.italic"            = { modifiers = ["italic"] }
"markup.strikethrough"     = { modifiers = ["crossed_out"] }
"markup.link"              = { fg = "<func_color>" }
"markup.link.url"          = { fg = "<func_color>", underline = { style = "line" } }
"markup.link.label"        = { fg = "<type_color>" }
"markup.link.text"         = { fg = "<string_color>" }
"markup.quote"             = { fg = "<comment_color>", modifiers = ["italic"] }
"markup.raw"               = { fg = "<string_color>" }
"markup.raw.inline"        = { fg = "<string_color>" }
"markup.raw.block"         = { fg = "<string_color>" }
```

Markup completion popup sub-scopes (documentation popup UI):

```toml
"markup.normal.completion"        = { fg = "<fg_primary>" }
"markup.normal.hover"             = { fg = "<fg_primary>" }
"markup.heading.completion"       = { fg = "<keyword_color>", modifiers = ["bold"] }
"markup.heading.hover"            = { fg = "<keyword_color>", modifiers = ["bold"] }
"markup.raw.inline.completion"    = { fg = "<string_color>" }
"markup.raw.inline.hover"         = { fg = "<string_color>" }
```

#### Diff

```toml
"diff.plus"          = "<string_color>"
"diff.plus.gutter"   = "<string_color>"
"diff.minus"         = "<error_color>"
"diff.minus.gutter"  = "<error_color>"
"diff.delta"         = "<number_color>"
"diff.delta.moved"   = "<attr_color>"
"diff.delta.conflict" = "<error_color>"
"diff.delta.gutter"  = "<number_color>"
```

---

### Section 2 — Interface / UI

#### Background

```toml
"ui.background"           = { fg = "<fg_primary>", bg = "bg_primary" }
"ui.background.separator" = { fg = "border" }
```

#### Cursor

```toml
"ui.cursor"                  = { modifiers = ["reversed"] }
"ui.cursor.normal"           = { fg = "bg_primary", bg = "secondary_cursor" }
"ui.cursor.insert"           = { fg = "bg_primary", bg = "<fg_primary>" }
"ui.cursor.select"           = { fg = "bg_primary", bg = "<number_color>" }
"ui.cursor.match"            = { fg = "<escape_color>", modifiers = ["bold"] }
"ui.cursor.primary"          = { fg = "bg_primary", bg = "<cursor_color>" }
"ui.cursor.primary.normal"   = { fg = "bg_primary", bg = "<cursor_color>" }
"ui.cursor.primary.insert"   = { fg = "bg_primary", bg = "<fg_primary>" }
"ui.cursor.primary.select"   = { fg = "bg_primary", bg = "<number_color>" }
```

`<cursor_color>` is the palette's `semantic_roles.cursor` color — must be high-contrast and unmissable.

#### Selection

```toml
"ui.selection"         = { bg = "selection" }
"ui.selection.primary" = { bg = "selection" }
```

#### Cursorline / Cursorcolumn

```toml
"ui.cursorline.primary"    = { bg = "bg_highlight" }
"ui.cursorline.secondary"  = { bg = "bg_primary" }
"ui.cursorcolumn.primary"  = { bg = "bg_highlight" }
"ui.cursorcolumn.secondary" = { bg = "bg_primary" }
```

#### Gutter & Line Numbers

```toml
"ui.gutter"          = { fg = "gutter_fg" }
"ui.gutter.selected" = { fg = "<muted_fg>", bg = "bg_highlight" }
"ui.linenr"          = { fg = "gutter_fg" }
"ui.linenr.selected" = { fg = "<muted_fg>" }
```

#### Statusline

```toml
"ui.statusline"          = { fg = "<dimmed_fg>", bg = "bg_secondary" }
"ui.statusline.inactive" = { fg = "gutter_fg", bg = "bg_secondary" }
"ui.statusline.normal"   = { fg = "bg_secondary", bg = "<func_color>", modifiers = ["bold"] }
"ui.statusline.insert"   = { fg = "bg_secondary", bg = "<cursor_color>", modifiers = ["bold"] }
"ui.statusline.select"   = { fg = "bg_secondary", bg = "<number_color>", modifiers = ["bold"] }
"ui.statusline.separator" = { fg = "border" }
```

#### Bufferline

```toml
"ui.bufferline"            = { fg = "<muted_fg>", bg = "bg_secondary" }
"ui.bufferline.active"     = { fg = "bg_secondary", bg = "<func_color>", modifiers = ["bold"] }
"ui.bufferline.background" = { bg = "bg_secondary" }
```

#### Popup & Menus

```toml
"ui.popup"       = { fg = "<fg_primary>", bg = "bg_secondary" }
"ui.popup.info"  = { fg = "<fg_primary>", bg = "bg_secondary" }
"ui.window"      = { fg = "border" }
"ui.help"        = { fg = "<fg_primary>", bg = "bg_secondary" }
"ui.menu"        = { fg = "<fg_primary>", bg = "bg_secondary" }
"ui.menu.selected" = { fg = "bg_secondary", bg = "<cursor_color>", modifiers = ["bold"] }
"ui.menu.scroll"   = { fg = "<dimmed_fg>", bg = "border" }
```

#### Picker

```toml
"ui.picker.header"               = { fg = "<dimmed_fg>", modifiers = ["bold"] }
"ui.picker.header.column"        = { fg = "<dimmed_fg>" }
"ui.picker.header.column.active" = { fg = "<cursor_color>", modifiers = ["bold"] }
```

#### Text

```toml
"ui.text"           = { fg = "<fg_primary>" }
"ui.text.focus"     = { fg = "<fg_primary>", bg = "bg_highlight", modifiers = ["bold"] }
"ui.text.inactive"  = { fg = "<muted_fg>" }
"ui.text.info"      = { fg = "<dimmed_fg>" }
"ui.text.directory" = { fg = "<type_color>" }
```

#### Virtual Elements

```toml
"ui.virtual"                    = { fg = "border" }
"ui.virtual.ruler"              = { bg = "bg_highlight" }
"ui.virtual.whitespace"         = { fg = "border" }
"ui.virtual.indent-guide"       = { fg = "border" }
"ui.virtual.inlay-hint"         = { fg = "gutter_fg", bg = "bg_secondary" }
"ui.virtual.inlay-hint.parameter" = { fg = "gutter_fg", modifiers = ["italic"] }
"ui.virtual.inlay-hint.type"    = { fg = "gutter_fg", modifiers = ["italic"] }
"ui.virtual.wrap"               = { fg = "gutter_fg" }
"ui.virtual.jump-label"         = { fg = "<number_color>", modifiers = ["bold"] }
```

#### Highlight

```toml
"ui.highlight"           = { bg = "bg_highlight" }
"ui.highlight.frameline" = { bg = "bg_highlight" }
```

#### Debug

```toml
"ui.debug.breakpoint" = { fg = "<error_color>" }
"ui.debug.active"     = { fg = "<number_color>" }
```

#### Snippet

```toml
tabstop = { modifiers = ["italic"], bg = "bg_highlight" }
```

#### Diagnostics (gutter)

```toml
warning = "<number_color>"
error   = "<error_color>"
info    = "<info_color>"
hint    = "<func_color>"
```

#### Diagnostics (editing area)

```toml
diagnostic                    = { underline = { color = "<number_color>", style = "curl" } }
"diagnostic.hint"             = { underline = { color = "<func_color>", style = "curl" } }
"diagnostic.info"             = { underline = { color = "<info_color>", style = "curl" } }
"diagnostic.warning"          = { underline = { color = "<number_color>", style = "curl" } }
"diagnostic.error"            = { underline = { color = "<error_color>", style = "curl" } }
"diagnostic.unnecessary"      = { modifiers = ["dim"] }
"diagnostic.deprecated"       = { modifiers = ["crossed_out"] }
```

---

### Section 3 — `[palette]`

Define a flat `snake_case` palette derived from the palette JSON. Include every color referenced in the scopes above.

**Required standard keys** (map from palette JSON paths):

| TOML key | Palette path |
|---|---|
| `bg_primary` | `colors.bg.primary` |
| `bg_secondary` | `colors.bg.secondary` |
| `bg_highlight` | `colors.bg.highlight` |
| `border` | `colors.bg.border` |
| `selection` | (derive: `bg.highlight` with extra alpha, or use a value between `bg.highlight` and `bg.border`) |
| `fg_primary` | `colors.fg.primary` |
| `dimmed_fg` | `colors.fg.dimmed` |
| `muted_fg` | `colors.fg.muted` |
| `gutter_fg` | `colors.fg.gutter` |
| all accent names | `colors.accent.*` (use palette's own `snake_case` names) |
| `secondary_cursor` | (derive: a muted/desaturated variant of the cursor color, for multi-cursor) |

Column-align hex values within each comment group:

```toml
[palette]

# Backgrounds
bg_primary   = "#XXXXXX"
bg_secondary = "#XXXXXX"
bg_highlight = "#XXXXXX"
border       = "#XXXXXX"
selection    = "#XXXXXX"

# Foregrounds
<fg_primary_name>  = "#XXXXXX"
<dimmed_fg_name>   = "#XXXXXX"
<muted_fg_name>    = "#XXXXXX"
gutter_fg          = "#XXXXXX"

# Accents
keyword_white    = "#FFFFFF"    # or the palette's keyword color if not white
<accent_1>       = "#XXXXXX"
<accent_2>       = "#XXXXXX"
...

# Multi-cursor
secondary_cursor = "#XXXXXX"
```

---

## File 2 — Transparent variant (`<theme-name>-transparent.toml`)

The transparent variant **inherits** the base theme and only overrides UI chrome scopes. It removes backgrounds from editor surfaces so a terminal wallpaper shows through, while keeping popups and statusline opaque for readability.

### Header

```toml
# Theme Name (Transparent) — Helix Editor Theme
# Inherits the base theme, removes all backgrounds to show terminal wallpaper.

inherits = "<theme-name>"
```

### Overrides to include

**Background:** remove bg

```toml
"ui.background"           = { fg = "<fg_primary>" }
"ui.background.separator" = { fg = "border" }
```

**Cursor:** keep functional, remove reversed where needed

```toml
"ui.cursor.normal"          = { modifiers = ["reversed"] }
"ui.cursor.insert"          = { fg = "bg_primary", bg = "<fg_primary>" }
"ui.cursor.select"          = { fg = "bg_primary", bg = "<number_color>" }
"ui.cursor.primary"         = { fg = "bg_primary", bg = "<cursor_color>" }
"ui.cursor.primary.normal"  = { fg = "bg_primary", bg = "<cursor_color>" }
"ui.cursor.primary.insert"  = { fg = "bg_primary", bg = "<fg_primary>" }
"ui.cursor.primary.select"  = { fg = "bg_primary", bg = "<number_color>" }
```

**Selection:** keep — needed over transparent background

```toml
"ui.selection"         = { bg = "selection" }
"ui.selection.primary" = { bg = "selection" }
```

**Cursorline:** keep primary, clear secondary

```toml
"ui.cursorline.primary"     = { bg = "bg_highlight" }
"ui.cursorline.secondary"   = {}
"ui.cursorcolumn.primary"   = { bg = "selection" }
"ui.cursorcolumn.secondary" = {}
```

**Gutter:** clear backgrounds

```toml
"ui.gutter"          = {}
"ui.gutter.selected" = {}
"ui.linenr"          = { fg = "gutter_fg" }
"ui.linenr.selected" = { fg = "<muted_fg>", modifiers = ["bold"] }
```

**Statusline:** keep opaque (use bg_secondary reference from palette)

```toml
"ui.statusline"           = { fg = "<dimmed_fg>", bg = "bg_secondary" }
"ui.statusline.inactive"  = { fg = "gutter_fg", bg = "bg_secondary" }
"ui.statusline.normal"    = { fg = "bg_secondary", bg = "<func_color>", modifiers = ["bold"] }
"ui.statusline.insert"    = { fg = "bg_secondary", bg = "<cursor_color>", modifiers = ["bold"] }
"ui.statusline.select"    = { fg = "bg_secondary", bg = "<number_color>", modifiers = ["bold"] }
```

**Bufferline:** keep opaque

```toml
"ui.bufferline"            = { fg = "<muted_fg>", bg = "bg_secondary" }
"ui.bufferline.active"     = { fg = "bg_secondary", bg = "<func_color>", modifiers = ["bold"] }
"ui.bufferline.background" = { bg = "bg_secondary" }
```

**Popup & Menus:** keep opaque

```toml
"ui.popup"         = { fg = "<fg_primary>", bg = "bg_secondary" }
"ui.popup.info"    = { fg = "<fg_primary>", bg = "bg_secondary" }
"ui.menu"          = { fg = "<fg_primary>", bg = "bg_secondary" }
"ui.menu.selected" = { fg = "bg_secondary", bg = "<cursor_color>", modifiers = ["bold"] }
"ui.menu.scroll"   = { fg = "<dimmed_fg>", bg = "border" }
"ui.help"          = { fg = "<fg_primary>", bg = "bg_secondary" }
"ui.window"        = { fg = "border" }
```

**Virtual elements:** remove backgrounds

```toml
"ui.virtual.ruler"              = { fg = "border" }
"ui.virtual.inlay-hint"         = { fg = "gutter_fg" }
"ui.virtual.inlay-hint.parameter" = { fg = "gutter_fg", modifiers = ["italic"] }
"ui.virtual.inlay-hint.type"    = { fg = "gutter_fg", modifiers = ["italic"] }
```

**Highlight:** reduce weight

```toml
"ui.highlight"           = { modifiers = ["bold"] }
"ui.highlight.frameline" = { underline = { color = "<number_color>", style = "line" } }
```

**Snippet:**

```toml
tabstop = { modifiers = ["italic", "underlined"] }
```

### Palette section in transparent variant

Re-declare only the colors needed for the overrides (those not inherited or those with new values):

```toml
[palette]

bg_secondary = "#XXXXXX"   # Opaque dark for UI elements
border       = "#XXXXXX"
selection    = "#XXXXXX"
bg_highlight = "#XXXXXX"

# Foregrounds
<fg_primary_name>  = "#XXXXXX"
<dimmed_fg_name>   = "#XXXXXX"
<muted_fg_name>    = "#XXXXXX"
gutter_fg          = "#XXXXXX"

# Accents (all needed for cursor/statusline references)
<accent_1> = "#XXXXXX"
...
```

---

## TOML formatting rules

- Flat dotted-key syntax — **no nested tables**.
- All keys with dots must be quoted: `"type.builtin" = ...`
- Values: `{ fg = "name", bg = "name", modifiers = ["bold"] }`
- Omit `bg` or `modifiers` when not needed — no empty keys.
- Section headers use box-drawing comment style:
  ```toml
  # ─── Section Name ────────────────────────────────────────────────────────────
  ```
- Within each sub-group, a short `# Comment` precedes the group.
- `[palette]` section is always last.
- Palette values are column-aligned within each comment group.
- Hex colors: 6-digit uppercase (`#FF2CF1`). No alpha suffixes in Helix themes.

---

## Rainbow brackets — enabling in Helix

After generating the theme, remind the user to enable rainbow brackets in their Helix `config.toml` if desired:

```toml
[editor]
rainbow-brackets = true
```

The `rainbow.bracket.1` through `rainbow.bracket.6` keys in the theme take effect only when this config option is set.

---

## Scope reference summary

The table below lists every scope this skill covers. Use it as a checklist — the generated file must include all of them.

### Syntax scopes

| Scope | Notes |
|---|---|
| `attribute` | |
| `type` | |
| `type.builtin` | |
| `type.parameter` | italic |
| `type.enum` | |
| `type.enum.variant` | |
| `constructor` | type-adjacent |
| `constant` | |
| `constant.builtin` | |
| `constant.builtin.boolean` | |
| `constant.character` | |
| `constant.character.escape` | escape color |
| `constant.numeric` | number color |
| `constant.numeric.integer` | |
| `constant.numeric.float` | |
| `string` | |
| `string.regexp` | escape color |
| `string.special` | |
| `string.special.path` | |
| `string.special.url` | underline |
| `string.special.symbol` | attr color |
| `comment` | italic |
| `comment.line.documentation` | italic |
| `comment.block.documentation` | italic |
| `comment.unused` | gutter_fg, italic |
| `variable` | |
| `variable.builtin` | italic |
| `variable.parameter` | italic |
| `variable.other` | |
| `variable.other.member` | member/dimmed color |
| `variable.other.member.private` | italic |
| `label` | |
| `punctuation` | |
| `punctuation.delimiter` | |
| `punctuation.bracket` | fallback bracket color |
| `punctuation.special` | hero color |
| `rainbow.bracket` | fallback (same as punctuation.bracket) |
| `rainbow.bracket.1` | level 1 |
| `rainbow.bracket.2` | level 2 |
| `rainbow.bracket.3` | level 3 |
| `rainbow.bracket.4` | level 4 |
| `rainbow.bracket.5` | level 5 |
| `rainbow.bracket.6` | level 6 |
| `keyword` | bold |
| `keyword.control` | bold |
| `keyword.control.conditional` | bold |
| `keyword.control.repeat` | bold |
| `keyword.control.import` | bold |
| `keyword.control.return` | bold + italic |
| `keyword.control.exception` | bold |
| `keyword.operator` | bold |
| `keyword.directive` | bold |
| `keyword.function` | bold |
| `keyword.storage.type` | bold |
| `keyword.storage.modifier` | bold |
| `operator` | punct color |
| `function` | hero color |
| `function.builtin` | |
| `function.method` | |
| `function.method.private` | italic |
| `function.macro` | |
| `function.special` | |
| `tag` | type color |
| `tag.builtin` | |
| `namespace` | hero + italic |
| `special` | attr color |
| `markup.heading` | keyword + bold |
| `markup.heading.marker` | punct |
| `markup.heading.1` | keyword + bold |
| `markup.heading.2` | keyword + bold |
| `markup.heading.3` | type + bold |
| `markup.heading.4` | type |
| `markup.heading.5` | hero |
| `markup.heading.6` | hero |
| `markup.list` | hero |
| `markup.list.unnumbered` | hero |
| `markup.list.numbered` | number color |
| `markup.list.checked` | string color |
| `markup.list.unchecked` | punct |
| `markup.bold` | bold |
| `markup.italic` | italic |
| `markup.strikethrough` | crossed_out |
| `markup.link` | hero |
| `markup.link.url` | hero + underline |
| `markup.link.label` | type color |
| `markup.link.text` | string color |
| `markup.quote` | comment + italic |
| `markup.raw` | string color |
| `markup.raw.inline` | string color |
| `markup.raw.block` | string color |
| `markup.normal.completion` | fg primary |
| `markup.normal.hover` | fg primary |
| `markup.heading.completion` | keyword + bold |
| `markup.heading.hover` | keyword + bold |
| `markup.raw.inline.completion` | string color |
| `markup.raw.inline.hover` | string color |
| `diff.plus` | string color |
| `diff.plus.gutter` | string color |
| `diff.minus` | error color |
| `diff.minus.gutter` | error color |
| `diff.delta` | number color |
| `diff.delta.moved` | attr color |
| `diff.delta.conflict` | error color |
| `diff.delta.gutter` | number color |

### UI scopes

| Scope | Notes |
|---|---|
| `ui.background` | fg + bg |
| `ui.background.separator` | border |
| `ui.cursor` | reversed |
| `ui.cursor.normal` | |
| `ui.cursor.insert` | |
| `ui.cursor.select` | |
| `ui.cursor.match` | matching bracket |
| `ui.cursor.primary` | |
| `ui.cursor.primary.normal` | |
| `ui.cursor.primary.insert` | |
| `ui.cursor.primary.select` | |
| `ui.selection` | |
| `ui.selection.primary` | |
| `ui.cursorline.primary` | |
| `ui.cursorline.secondary` | |
| `ui.cursorcolumn.primary` | |
| `ui.cursorcolumn.secondary` | |
| `ui.gutter` | |
| `ui.gutter.selected` | |
| `ui.linenr` | |
| `ui.linenr.selected` | |
| `ui.statusline` | |
| `ui.statusline.inactive` | |
| `ui.statusline.normal` | color-modes |
| `ui.statusline.insert` | color-modes |
| `ui.statusline.select` | color-modes |
| `ui.statusline.separator` | |
| `ui.bufferline` | |
| `ui.bufferline.active` | |
| `ui.bufferline.background` | |
| `ui.popup` | |
| `ui.popup.info` | |
| `ui.window` | |
| `ui.help` | |
| `ui.menu` | |
| `ui.menu.selected` | |
| `ui.menu.scroll` | |
| `ui.picker.header` | |
| `ui.picker.header.column` | |
| `ui.picker.header.column.active` | |
| `ui.text` | |
| `ui.text.focus` | |
| `ui.text.inactive` | |
| `ui.text.info` | |
| `ui.text.directory` | |
| `ui.virtual` | |
| `ui.virtual.ruler` | |
| `ui.virtual.whitespace` | |
| `ui.virtual.indent-guide` | |
| `ui.virtual.inlay-hint` | |
| `ui.virtual.inlay-hint.parameter` | italic |
| `ui.virtual.inlay-hint.type` | italic |
| `ui.virtual.wrap` | |
| `ui.virtual.jump-label` | bold |
| `ui.highlight` | |
| `ui.highlight.frameline` | |
| `ui.debug.breakpoint` | error color |
| `ui.debug.active` | number color |
| `tabstop` | snippet placeholder |
| `warning` | gutter diagnostic |
| `error` | gutter diagnostic |
| `info` | gutter diagnostic |
| `hint` | gutter diagnostic |
| `diagnostic` | curl underline |
| `diagnostic.hint` | curl underline |
| `diagnostic.info` | curl underline |
| `diagnostic.warning` | curl underline |
| `diagnostic.error` | curl underline |
| `diagnostic.unnecessary` | dim |
| `diagnostic.deprecated` | crossed_out |

---

## After generation

1. Verify JSON validity is not applicable (TOML — check syntax manually or with `taplo`).
2. Remind the user to copy the files to Helix's theme directory:
   ```bash
   cp <theme-name>/editors/helix/<theme-name>.toml ~/.config/helix/themes/
   cp <theme-name>/editors/helix/<theme-name>-transparent.toml ~/.config/helix/themes/
   ```
   Or use the `deploy-themes` skill if Helix is built from source at `/Users/wk/Source/helix/`.
3. To activate:
   ```toml
   # ~/.config/helix/config.toml
   theme = "<theme-name>"
   ```
4. To enable rainbow brackets:
   ```toml
   [editor]
   rainbow-brackets = true
   ```
