# Helix Theme Reference — Crystal City

A comprehensive reference for all Helix theme scopes, showing how Crystal City maps its palette to each one. Based on the [official Helix theme documentation](https://docs.helix-editor.com/themes.html).

---

## Installation

Copy the theme files into your Helix themes directory:

```
~/.config/helix/themes/crystal_city.toml
~/.config/helix/themes/crystal_city_transparent.toml
```

Then set it in `~/.config/helix/config.toml`:

```toml
theme = "crystal_city"
# or: theme = "crystal_city_transparent"
```

Or switch at runtime with `:theme crystal_city`.

---

## Theme File Format

Each line is a scope-to-style mapping:

```toml
key = { fg = "#ffffff", bg = "#000000", underline = { color = "#ff0000", style = "curl" }, modifiers = ["bold", "italic"] }
```

- `fg` — foreground color
- `bg` — background color (optional)
- `underline.style` — one of: `line`, `curl`, `dashed`, `dotted`, `double_line`
- `underline.color` — underline color
- `modifiers` — list of: `bold`, `dim`, `italic`, `underlined`, `slow_blink`, `rapid_blink`, `reversed`, `hidden`, `crossed_out`

Shorthand for fg-only: `key = "#ffffff"`

---

## Color Palette

Define named colors in a `[palette]` section at the end of the file. Crystal City defines:

| Palette Name | Hex | Role |
|---|---|---|
| `bg_primary` | `#0A0E1A` | Editor canvas (obsidian) |
| `bg_secondary` | `#060910` | Sidebar, panels (deep void) |
| `bg_highlight` | `#111728` | Active line, elevated surfaces |
| `border` | `#1C2333` | Panel separators |
| `selection` | `#1A2850` | Text selection background |
| `frost_white` | `#D8DEE9` | Primary text, variables |
| `steel_grey` | `#7B88A1` | Operators, punctuation |
| `slate_indigo` | `#4A5270` | Inactive text, placeholders |
| `gutter_fg` | `#2E3550` | Line numbers |
| `keyword_white` | `#FFFFFF` | Keywords (bold) |
| `crystal_teal` | `#56D4C8` | Functions, methods (hero color) |
| `mint_glass` | `#89DDCA` | Strings, raw text |
| `glacier_blue` | `#7EC8E3` | Types, tags, constructors |
| `dusty_rose` | `#E8A0BF` | Constants, booleans |
| `neon_rose` | `#FF6B9D` | Cursor, active indicators, regex, escapes |
| `city_gold` | `#F0C674` | Numbers, warnings |
| `glass_blue` | `#61AFEF` | Info diagnostics |
| `crystal_violet` | `#B48EF0` | Attributes, properties, special symbols |
| `signal_red` | `#E06C75` | Errors, diff deletions |
| `sage_teal` | `#5A8A7A` | Comments (italic) |
| `secondary_cursor` | `#A87CB8` | Multi-cursor |

---

## Syntax Highlighting Scopes

The longest matching key wins. For example, highlight `function.builtin.static` matches `function.builtin` over `function`.

### Attributes

| Scope | Crystal City Style |
|---|---|
| `attribute` | `crystal_violet` italic |

### Types

| Scope | Crystal City Style |
|---|---|
| `type` | `glacier_blue` |
| `type.builtin` | `glacier_blue` |
| `type.parameter` | `glacier_blue` italic |
| `type.enum` | `glacier_blue` |
| `type.enum.variant` | `glacier_blue` |

### Constructors

| Scope | Crystal City Style |
|---|---|
| `constructor` | `glacier_blue` |

### Constants

| Scope | Crystal City Style |
|---|---|
| `constant` | `dusty_rose` |
| `constant.builtin` | `dusty_rose` |
| `constant.builtin.boolean` | `dusty_rose` |
| `constant.character` | `dusty_rose` |
| `constant.character.escape` | `neon_rose` |
| `constant.numeric` | `city_gold` |
| `constant.numeric.integer` | `city_gold` |
| `constant.numeric.float` | `city_gold` |

### Strings

| Scope | Crystal City Style |
|---|---|
| `string` | `mint_glass` |
| `string.regexp` | `neon_rose` |
| `string.special` | `mint_glass` |
| `string.special.path` | `mint_glass` |
| `string.special.url` | `mint_glass` underline |
| `string.special.symbol` | `crystal_violet` |

### Comments

| Scope | Crystal City Style |
|---|---|
| `comment` | `sage_teal` italic |
| `comment.line.documentation` | `sage_teal` italic |
| `comment.block.documentation` | `sage_teal` italic |
| `comment.unused` | `gutter_fg` italic |

### Variables

| Scope | Crystal City Style |
|---|---|
| `variable` | `frost_white` |
| `variable.builtin` | `frost_white` italic |
| `variable.parameter` | `frost_white` italic |
| `variable.other` | `frost_white` |
| `variable.other.member` | `steel_grey` |
| `variable.other.member.private` | `steel_grey` italic |

### Labels

| Scope | Crystal City Style |
|---|---|
| `label` | `crystal_teal` |

### Punctuation

| Scope | Crystal City Style |
|---|---|
| `punctuation` | `steel_grey` |
| `punctuation.delimiter` | `steel_grey` |
| `punctuation.bracket` | `steel_grey` |
| `punctuation.special` | `crystal_teal` |

### Keywords

| Scope | Crystal City Style |
|---|---|
| `keyword` | `keyword_white` bold |
| `keyword.control` | `keyword_white` bold |
| `keyword.control.conditional` | `keyword_white` bold |
| `keyword.control.repeat` | `keyword_white` bold |
| `keyword.control.import` | `keyword_white` bold |
| `keyword.control.return` | `keyword_white` bold italic |
| `keyword.control.exception` | `keyword_white` bold |
| `keyword.operator` | `keyword_white` bold |
| `keyword.directive` | `keyword_white` bold |
| `keyword.function` | `keyword_white` bold |
| `keyword.storage.type` | `keyword_white` bold |
| `keyword.storage.modifier` | `keyword_white` bold |

### Operators

| Scope | Crystal City Style |
|---|---|
| `operator` | `steel_grey` |

### Functions

| Scope | Crystal City Style |
|---|---|
| `function` | `crystal_teal` |
| `function.builtin` | `crystal_teal` |
| `function.method` | `crystal_teal` |
| `function.method.private` | `crystal_teal` italic |
| `function.macro` | `crystal_teal` |
| `function.special` | `crystal_teal` |

### Tags

| Scope | Crystal City Style |
|---|---|
| `tag` | `glacier_blue` |
| `tag.builtin` | `glacier_blue` |

### Namespace

| Scope | Crystal City Style |
|---|---|
| `namespace` | `crystal_teal` italic |

### Special

| Scope | Crystal City Style |
|---|---|
| `special` | `crystal_violet` |

### Markup

| Scope | Crystal City Style |
|---|---|
| `markup.heading` | `keyword_white` bold |
| `markup.heading.marker` | `steel_grey` |
| `markup.heading.1` | `keyword_white` bold |
| `markup.heading.2` | `keyword_white` bold |
| `markup.heading.3` | `glacier_blue` bold |
| `markup.heading.4` | `glacier_blue` |
| `markup.heading.5` | `crystal_teal` |
| `markup.heading.6` | `crystal_teal` |
| `markup.list` | `crystal_teal` |
| `markup.list.unnumbered` | `crystal_teal` |
| `markup.list.numbered` | `city_gold` |
| `markup.list.checked` | `mint_glass` |
| `markup.list.unchecked` | `steel_grey` |
| `markup.bold` | bold |
| `markup.italic` | italic |
| `markup.strikethrough` | crossed_out |
| `markup.link` | `crystal_teal` |
| `markup.link.url` | `crystal_teal` underline |
| `markup.link.label` | `glacier_blue` |
| `markup.link.text` | `mint_glass` |
| `markup.quote` | `sage_teal` italic |
| `markup.raw` | `mint_glass` |
| `markup.raw.inline` | `mint_glass` |
| `markup.raw.block` | `mint_glass` |

### Diff

| Scope | Crystal City Style |
|---|---|
| `diff.plus` | `mint_glass` |
| `diff.plus.gutter` | `mint_glass` |
| `diff.minus` | `signal_red` |
| `diff.minus.gutter` | `signal_red` |
| `diff.delta` | `city_gold` |
| `diff.delta.gutter` | `city_gold` |

---

## Interface Scopes

### Background & Layout

| Scope | Crystal City Style | Notes |
|---|---|---|
| `ui.background` | fg: `frost_white`, bg: `bg_primary` | Main editor canvas |
| `ui.background.separator` | fg: `border` | Picker separator below input |

### Cursor

| Scope | Crystal City Style | Notes |
|---|---|---|
| `ui.cursor` | reversed | Fallback |
| `ui.cursor.normal` | fg: `bg_primary`, bg: `secondary_cursor` | Normal mode |
| `ui.cursor.insert` | fg: `bg_primary`, bg: `frost_white` | Insert mode |
| `ui.cursor.select` | fg: `bg_primary`, bg: `city_gold` | Select mode |
| `ui.cursor.match` | fg: `neon_rose`, bold | Matching bracket |
| `ui.cursor.primary` | fg: `bg_primary`, bg: `neon_rose` | Primary cursor |
| `ui.cursor.primary.normal` | fg: `bg_primary`, bg: `neon_rose` | Primary in normal |
| `ui.cursor.primary.insert` | fg: `bg_primary`, bg: `frost_white` | Primary in insert |
| `ui.cursor.primary.select` | fg: `bg_primary`, bg: `city_gold` | Primary in select |

### Selection

| Scope | Crystal City Style | Notes |
|---|---|---|
| `ui.selection` | bg: `selection` | Text selection |
| `ui.selection.primary` | bg: `selection` | Primary selection |

### Cursorline & Cursorcolumn

| Scope | Crystal City Style | Notes |
|---|---|---|
| `ui.cursorline.primary` | bg: `bg_highlight` | Line of primary cursor |
| `ui.cursorline.secondary` | bg: `bg_primary` | Lines of other cursors |
| `ui.cursorcolumn.primary` | bg: `bg_highlight` | Column of primary cursor |
| `ui.cursorcolumn.secondary` | bg: `bg_primary` | Columns of other cursors |

### Gutter & Line Numbers

| Scope | Crystal City Style | Notes |
|---|---|---|
| `ui.gutter` | fg: `gutter_fg` | Gutter area |
| `ui.gutter.selected` | fg: `slate_indigo`, bg: `bg_highlight` | Gutter for cursor line |
| `ui.linenr` | fg: `gutter_fg` | Line numbers |
| `ui.linenr.selected` | fg: `slate_indigo` | Current line number |

### Statusline

| Scope | Crystal City Style | Notes |
|---|---|---|
| `ui.statusline` | fg: `steel_grey`, bg: `bg_secondary` | Default statusline |
| `ui.statusline.inactive` | fg: `gutter_fg`, bg: `bg_secondary` | Unfocused document |
| `ui.statusline.normal` | fg: `bg_secondary`, bg: `crystal_teal`, bold | Normal mode (with `editor.color-modes`) |
| `ui.statusline.insert` | fg: `bg_secondary`, bg: `neon_rose`, bold | Insert mode |
| `ui.statusline.select` | fg: `bg_secondary`, bg: `city_gold`, bold | Select mode |
| `ui.statusline.separator` | fg: `border` | Separator character |

### Bufferline

| Scope | Crystal City Style | Notes |
|---|---|---|
| `ui.bufferline` | fg: `slate_indigo`, bg: `bg_secondary` | Buffer tabs |
| `ui.bufferline.active` | fg: `frost_white`, bg: `bg_primary`, underline: `neon_rose` | Active buffer |
| `ui.bufferline.background` | bg: `bg_secondary` | Bufferline background |

### Popup & Menus

| Scope | Crystal City Style | Notes |
|---|---|---|
| `ui.popup` | fg: `frost_white`, bg: `bg_secondary` | Doc popups (Space+k) |
| `ui.popup.info` | fg: `frost_white`, bg: `bg_secondary` | Multi-key prompts |
| `ui.window` | fg: `border` | Split borders |
| `ui.help` | fg: `frost_white`, bg: `bg_secondary` | Command descriptions |
| `ui.menu` | fg: `frost_white`, bg: `bg_secondary` | Completion menus |
| `ui.menu.selected` | fg: `bg_secondary`, bg: `neon_rose`, bold | Selected autocomplete |
| `ui.menu.scroll` | fg: `steel_grey`, bg: `border` | Scrollbar (thumb/track) |

### Picker

| Scope | Crystal City Style | Notes |
|---|---|---|
| `ui.picker.header` | fg: `steel_grey`, bold | Header row |
| `ui.picker.header.column` | fg: `steel_grey` | Column names |
| `ui.picker.header.column.active` | fg: `neon_rose`, bold | Active column |

### Text

| Scope | Crystal City Style | Notes |
|---|---|---|
| `ui.text` | fg: `frost_white` | Default text |
| `ui.text.focus` | fg: `frost_white`, bg: `bg_highlight`, bold | Selected picker line |
| `ui.text.inactive` | fg: `slate_indigo` | Inactive suggestions |
| `ui.text.info` | fg: `steel_grey` | Key:command text |
| `ui.text.directory` | fg: `glacier_blue` | Directory names in completion |

### Virtual Elements

| Scope | Crystal City Style | Notes |
|---|---|---|
| `ui.virtual` | fg: `border` | Default virtual |
| `ui.virtual.ruler` | bg: `bg_highlight` | Ruler columns |
| `ui.virtual.whitespace` | fg: `border` | Visible whitespace |
| `ui.virtual.indent-guide` | fg: `border` | Indent guides |
| `ui.virtual.inlay-hint` | fg: `gutter_fg`, bg: `bg_secondary` | Default inlay hints |
| `ui.virtual.inlay-hint.parameter` | fg: `gutter_fg`, italic | Parameter hints |
| `ui.virtual.inlay-hint.type` | fg: `gutter_fg`, italic | Type hints |
| `ui.virtual.wrap` | fg: `gutter_fg` | Soft-wrap indicator |
| `ui.virtual.jump-label` | fg: `city_gold`, bold | Jump labels |

### Highlight & Debug

| Scope | Crystal City Style | Notes |
|---|---|---|
| `ui.highlight` | bg: `bg_highlight` | Picker preview highlight |
| `ui.highlight.frameline` | bg: `bg_highlight` | Debug pause line |
| `ui.debug.breakpoint` | fg: `signal_red` | Breakpoint gutter |
| `ui.debug.active` | fg: `city_gold` | Active debug line |

### Diagnostics

| Scope | Crystal City Style | Notes |
|---|---|---|
| `warning` | `city_gold` | Gutter warning |
| `error` | `signal_red` | Gutter error |
| `info` | `glass_blue` | Gutter info |
| `hint` | `crystal_teal` | Gutter hint |
| `diagnostic` | underline: `city_gold` curl | Editing area fallback |
| `diagnostic.hint` | underline: `crystal_teal` curl | Editing area hint |
| `diagnostic.info` | underline: `glass_blue` curl | Editing area info |
| `diagnostic.warning` | underline: `city_gold` curl | Editing area warning |
| `diagnostic.error` | underline: `signal_red` curl | Editing area error |
| `diagnostic.unnecessary` | dim | Unused code |
| `diagnostic.deprecated` | crossed_out | Deprecated code |

### Snippet

| Scope | Crystal City Style | Notes |
|---|---|---|
| `tabstop` | italic, bg: `bg_highlight` | Snippet placeholder |

---

## Inheritance

The transparent variant uses inheritance:

```toml
inherits = "crystal_city"
```

It overrides only the UI background/chrome scopes to remove backgrounds, while keeping all syntax highlighting from the base theme.

---

## Modifiers Reference

| Modifier | Description |
|---|---|
| `bold` | Bold text |
| `dim` | Dimmed/faint text |
| `italic` | Italic text |
| `underlined` | (deprecated) Equivalent to `underline.style = "line"` |
| `slow_blink` | Slow blinking text |
| `rapid_blink` | Rapid blinking text |
| `reversed` | Swap foreground and background |
| `hidden` | Hidden text |
| `crossed_out` | Strikethrough text |

## Underline Styles

| Style | Description |
|---|---|
| `line` | Straight underline |
| `curl` | Wavy/curly underline (used for diagnostics) |
| `dashed` | Dashed underline |
| `dotted` | Dotted underline |
| `double_line` | Double straight underline |
