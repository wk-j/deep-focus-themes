# Helix Theme Reference — Neon City

A comprehensive reference for all Helix theme scopes, showing how Neon City maps its palette to each one. Based on the [official Helix theme documentation](https://docs.helix-editor.com/themes.html).

---

## Installation

Copy the theme files into your Helix themes directory:

```
~/.config/helix/themes/neon_city.toml
~/.config/helix/themes/neon_city_transparent.toml
```

Then set it in `~/.config/helix/config.toml`:

```toml
theme = "neon_city"
# or: theme = "neon_city_transparent"
```

Or switch at runtime with `:theme neon_city`.

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

Define named colors in a `[palette]` section at the end of the file. Neon City defines:

| Palette Name | Hex | Role |
|---|---|---|
| `bg_primary` | `#0D0221` | Editor canvas (midnight) |
| `bg_secondary` | `#07010F` | Sidebar, panels (void black) |
| `bg_highlight` | `#1A0A3E` | Active line, elevated surfaces |
| `border` | `#2A1454` | Panel separators |
| `selection` | `#2D1B69` | Text selection background |
| `neon_white` | `#E0D4FF` | Primary text, variables |
| `dusk_mauve` | `#8B7BAE` | Operators, punctuation |
| `shadow_purple` | `#5C4A82` | Inactive text, placeholders |
| `gutter_fg` | `#3D2E5C` | Line numbers |
| `keyword_white` | `#FFFFFF` | Keywords (bold) |
| `electric_magenta` | `#FF2CF1` | Functions, methods (hero color) |
| `plasma_green` | `#39FF14` | Strings, raw text |
| `cyber_blue` | `#00D4FF` | Types, tags, constructors |
| `hot_pink` | `#FF69B4` | Constants, booleans |
| `electric_cyan` | `#00FFFF` | Cursor, active indicators, regex, escapes |
| `neon_orange` | `#FF6B2B` | Numbers, warnings |
| `signal_blue` | `#448AFF` | Info diagnostics |
| `neon_yellow` | `#FFE744` | Attributes, properties, special symbols |
| `alarm_red` | `#FF1744` | Errors, diff deletions |
| `twilight_indigo` | `#6B5B95` | Comments (italic) |
| `secondary_cursor` | `#9B59B6` | Multi-cursor |

---

## Syntax Highlighting Scopes

The longest matching key wins. For example, highlight `function.builtin.static` matches `function.builtin` over `function`.

### Attributes

| Scope | Neon City Style |
|---|---|
| `attribute` | `neon_yellow` italic |

### Types

| Scope | Neon City Style |
|---|---|
| `type` | `cyber_blue` |
| `type.builtin` | `cyber_blue` |
| `type.parameter` | `cyber_blue` italic |
| `type.enum` | `cyber_blue` |
| `type.enum.variant` | `cyber_blue` |

### Constructors

| Scope | Neon City Style |
|---|---|
| `constructor` | `cyber_blue` |

### Constants

| Scope | Neon City Style |
|---|---|
| `constant` | `hot_pink` |
| `constant.builtin` | `hot_pink` |
| `constant.builtin.boolean` | `hot_pink` |
| `constant.character` | `hot_pink` |
| `constant.character.escape` | `electric_cyan` |
| `constant.numeric` | `neon_orange` |
| `constant.numeric.integer` | `neon_orange` |
| `constant.numeric.float` | `neon_orange` |

### Strings

| Scope | Neon City Style |
|---|---|
| `string` | `plasma_green` |
| `string.regexp` | `electric_cyan` |
| `string.special` | `plasma_green` |
| `string.special.path` | `plasma_green` |
| `string.special.url` | `plasma_green` underline |
| `string.special.symbol` | `neon_yellow` |

### Comments

| Scope | Neon City Style |
|---|---|
| `comment` | `twilight_indigo` italic |
| `comment.line.documentation` | `twilight_indigo` italic |
| `comment.block.documentation` | `twilight_indigo` italic |
| `comment.unused` | `gutter_fg` italic |

### Variables

| Scope | Neon City Style |
|---|---|
| `variable` | `neon_white` |
| `variable.builtin` | `neon_white` italic |
| `variable.parameter` | `neon_white` italic |
| `variable.other` | `neon_white` |
| `variable.other.member` | `dusk_mauve` |
| `variable.other.member.private` | `dusk_mauve` italic |

### Labels

| Scope | Neon City Style |
|---|---|
| `label` | `electric_magenta` |

### Punctuation

| Scope | Neon City Style |
|---|---|
| `punctuation` | `dusk_mauve` |
| `punctuation.delimiter` | `dusk_mauve` |
| `punctuation.bracket` | `dusk_mauve` |
| `punctuation.special` | `electric_magenta` |

### Keywords

| Scope | Neon City Style |
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

| Scope | Neon City Style |
|---|---|
| `operator` | `dusk_mauve` |

### Functions

| Scope | Neon City Style |
|---|---|
| `function` | `electric_magenta` |
| `function.builtin` | `electric_magenta` |
| `function.method` | `electric_magenta` |
| `function.method.private` | `electric_magenta` italic |
| `function.macro` | `electric_magenta` |
| `function.special` | `electric_magenta` |

### Tags

| Scope | Neon City Style |
|---|---|
| `tag` | `cyber_blue` |
| `tag.builtin` | `cyber_blue` |

### Namespace

| Scope | Neon City Style |
|---|---|
| `namespace` | `electric_magenta` italic |

### Special

| Scope | Neon City Style |
|---|---|
| `special` | `neon_yellow` |

### Markup

| Scope | Neon City Style |
|---|---|
| `markup.heading` | `keyword_white` bold |
| `markup.heading.marker` | `dusk_mauve` |
| `markup.heading.1` | `keyword_white` bold |
| `markup.heading.2` | `keyword_white` bold |
| `markup.heading.3` | `cyber_blue` bold |
| `markup.heading.4` | `cyber_blue` |
| `markup.heading.5` | `electric_magenta` |
| `markup.heading.6` | `electric_magenta` |
| `markup.list` | `electric_magenta` |
| `markup.list.unnumbered` | `electric_magenta` |
| `markup.list.numbered` | `neon_orange` |
| `markup.list.checked` | `plasma_green` |
| `markup.list.unchecked` | `dusk_mauve` |
| `markup.bold` | bold |
| `markup.italic` | italic |
| `markup.strikethrough` | crossed_out |
| `markup.link` | `electric_magenta` |
| `markup.link.url` | `electric_magenta` underline |
| `markup.link.label` | `cyber_blue` |
| `markup.link.text` | `plasma_green` |
| `markup.quote` | `twilight_indigo` italic |
| `markup.raw` | `plasma_green` |
| `markup.raw.inline` | `plasma_green` |
| `markup.raw.block` | `plasma_green` |

### Diff

| Scope | Neon City Style |
|---|---|
| `diff.plus` | `plasma_green` |
| `diff.plus.gutter` | `plasma_green` |
| `diff.minus` | `alarm_red` |
| `diff.minus.gutter` | `alarm_red` |
| `diff.delta` | `neon_orange` |
| `diff.delta.gutter` | `neon_orange` |

---

## Interface Scopes

### Background & Layout

| Scope | Neon City Style | Notes |
|---|---|---|
| `ui.background` | fg: `neon_white`, bg: `bg_primary` | Main editor canvas |
| `ui.background.separator` | fg: `border` | Picker separator below input |

### Cursor

| Scope | Neon City Style | Notes |
|---|---|---|
| `ui.cursor` | reversed | Fallback |
| `ui.cursor.normal` | fg: `bg_primary`, bg: `secondary_cursor` | Normal mode |
| `ui.cursor.insert` | fg: `bg_primary`, bg: `neon_white` | Insert mode |
| `ui.cursor.select` | fg: `bg_primary`, bg: `neon_orange` | Select mode |
| `ui.cursor.match` | fg: `electric_cyan`, bold | Matching bracket |
| `ui.cursor.primary` | fg: `bg_primary`, bg: `electric_cyan` | Primary cursor |
| `ui.cursor.primary.normal` | fg: `bg_primary`, bg: `electric_cyan` | Primary in normal |
| `ui.cursor.primary.insert` | fg: `bg_primary`, bg: `neon_white` | Primary in insert |
| `ui.cursor.primary.select` | fg: `bg_primary`, bg: `neon_orange` | Primary in select |

### Selection

| Scope | Neon City Style | Notes |
|---|---|---|
| `ui.selection` | bg: `selection` | Text selection |
| `ui.selection.primary` | bg: `selection` | Primary selection |

### Cursorline & Cursorcolumn

| Scope | Neon City Style | Notes |
|---|---|---|
| `ui.cursorline.primary` | bg: `bg_highlight` | Line of primary cursor |
| `ui.cursorline.secondary` | bg: `bg_primary` | Lines of other cursors |
| `ui.cursorcolumn.primary` | bg: `bg_highlight` | Column of primary cursor |
| `ui.cursorcolumn.secondary` | bg: `bg_primary` | Columns of other cursors |

### Gutter & Line Numbers

| Scope | Neon City Style | Notes |
|---|---|---|
| `ui.gutter` | fg: `gutter_fg` | Gutter area |
| `ui.gutter.selected` | fg: `shadow_purple`, bg: `bg_highlight` | Gutter for cursor line |
| `ui.linenr` | fg: `gutter_fg` | Line numbers |
| `ui.linenr.selected` | fg: `shadow_purple` | Current line number |

### Statusline

| Scope | Neon City Style | Notes |
|---|---|---|
| `ui.statusline` | fg: `dusk_mauve`, bg: `bg_secondary` | Default statusline |
| `ui.statusline.inactive` | fg: `gutter_fg`, bg: `bg_secondary` | Unfocused document |
| `ui.statusline.normal` | fg: `bg_secondary`, bg: `electric_magenta`, bold | Normal mode (with `editor.color-modes`) |
| `ui.statusline.insert` | fg: `bg_secondary`, bg: `electric_cyan`, bold | Insert mode |
| `ui.statusline.select` | fg: `bg_secondary`, bg: `neon_orange`, bold | Select mode |
| `ui.statusline.separator` | fg: `border` | Separator character |

### Bufferline

| Scope | Neon City Style | Notes |
|---|---|---|
| `ui.bufferline` | fg: `shadow_purple`, bg: `bg_secondary` | Buffer tabs |
| `ui.bufferline.active` | fg: `neon_white`, bg: `bg_primary`, underline: `electric_cyan` | Active buffer |
| `ui.bufferline.background` | bg: `bg_secondary` | Bufferline background |

### Popup & Menus

| Scope | Neon City Style | Notes |
|---|---|---|
| `ui.popup` | fg: `neon_white`, bg: `bg_secondary` | Doc popups (Space+k) |
| `ui.popup.info` | fg: `neon_white`, bg: `bg_secondary` | Multi-key prompts |
| `ui.window` | fg: `border` | Split borders |
| `ui.help` | fg: `neon_white`, bg: `bg_secondary` | Command descriptions |
| `ui.menu` | fg: `neon_white`, bg: `bg_secondary` | Completion menus |
| `ui.menu.selected` | fg: `bg_secondary`, bg: `electric_cyan`, bold | Selected autocomplete |
| `ui.menu.scroll` | fg: `dusk_mauve`, bg: `border` | Scrollbar (thumb/track) |

### Picker

| Scope | Neon City Style | Notes |
|---|---|---|
| `ui.picker.header` | fg: `dusk_mauve`, bold | Header row |
| `ui.picker.header.column` | fg: `dusk_mauve` | Column names |
| `ui.picker.header.column.active` | fg: `electric_cyan`, bold | Active column |

### Text

| Scope | Neon City Style | Notes |
|---|---|---|
| `ui.text` | fg: `neon_white` | Default text |
| `ui.text.focus` | fg: `neon_white`, bg: `bg_highlight`, bold | Selected picker line |
| `ui.text.inactive` | fg: `shadow_purple` | Inactive suggestions |
| `ui.text.info` | fg: `dusk_mauve` | Key:command text |
| `ui.text.directory` | fg: `cyber_blue` | Directory names in completion |

### Virtual Elements

| Scope | Neon City Style | Notes |
|---|---|---|
| `ui.virtual` | fg: `border` | Default virtual |
| `ui.virtual.ruler` | bg: `bg_highlight` | Ruler columns |
| `ui.virtual.whitespace` | fg: `border` | Visible whitespace |
| `ui.virtual.indent-guide` | fg: `border` | Indent guides |
| `ui.virtual.inlay-hint` | fg: `gutter_fg`, bg: `bg_secondary` | Default inlay hints |
| `ui.virtual.inlay-hint.parameter` | fg: `gutter_fg`, italic | Parameter hints |
| `ui.virtual.inlay-hint.type` | fg: `gutter_fg`, italic | Type hints |
| `ui.virtual.wrap` | fg: `gutter_fg` | Soft-wrap indicator |
| `ui.virtual.jump-label` | fg: `neon_orange`, bold | Jump labels |

### Highlight & Debug

| Scope | Neon City Style | Notes |
|---|---|---|
| `ui.highlight` | bg: `bg_highlight` | Picker preview highlight |
| `ui.highlight.frameline` | bg: `bg_highlight` | Debug pause line |
| `ui.debug.breakpoint` | fg: `alarm_red` | Breakpoint gutter |
| `ui.debug.active` | fg: `neon_orange` | Active debug line |

### Diagnostics

| Scope | Neon City Style | Notes |
|---|---|---|
| `warning` | `neon_orange` | Gutter warning |
| `error` | `alarm_red` | Gutter error |
| `info` | `signal_blue` | Gutter info |
| `hint` | `electric_magenta` | Gutter hint |
| `diagnostic` | underline: `neon_orange` curl | Editing area fallback |
| `diagnostic.hint` | underline: `electric_magenta` curl | Editing area hint |
| `diagnostic.info` | underline: `signal_blue` curl | Editing area info |
| `diagnostic.warning` | underline: `neon_orange` curl | Editing area warning |
| `diagnostic.error` | underline: `alarm_red` curl | Editing area error |
| `diagnostic.unnecessary` | dim | Unused code |
| `diagnostic.deprecated` | crossed_out | Deprecated code |

### Snippet

| Scope | Neon City Style | Notes |
|---|---|---|
| `tabstop` | italic, bg: `bg_highlight` | Snippet placeholder |

---

## Inheritance

The transparent variant uses inheritance:

```toml
inherits = "neon_city"
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
