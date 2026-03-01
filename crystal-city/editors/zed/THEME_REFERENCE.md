# Zed Theme Reference — Crystal City

A comprehensive reference for Zed editor theme properties, showing how Crystal City maps its palette to each scope. Derived from the [Zed theme schema](https://zed.dev/schema/themes/v0.2.0.json) and the official [One Dark/Light theme](https://github.com/zed-industries/zed/blob/main/assets/themes/one/one.json).

---

## Installation

### As an Extension

Place the following files in a Zed extension directory:

```
crystal-city/
  extension.toml
  themes/
    crystal-city.json
```

Then install via Zed's extension system or by placing it in `~/.config/zed/extensions/`.

### Theme Selection

Crystal City ships with 4 variants in a single file:

| Variant | Description |
|---|---|
| **Crystal City** | Fully opaque backgrounds |
| **Crystal City Low Transparency** | ~84% opacity backgrounds (blurred) |
| **Crystal City Medium Transparency** | ~60% opacity backgrounds (blurred) |
| **Crystal City High Transparency** | ~30% opacity backgrounds (blurred) |

Select via `Settings > Theme` or the command palette.

---

## Theme File Structure

```json
{
  "$schema": "https://zed.dev/schema/themes/v0.2.0.json",
  "name": "Theme Family Name",
  "author": "Author Name",
  "themes": [
    {
      "name": "Variant Name",
      "appearance": "dark",  // or "light"
      "style": {
        // ... all theme properties
      }
    }
  ]
}
```

Each theme variant lives inside the `themes` array. All variants share the same family name but can have different `appearance` and `style` properties.

---

## Color Format

All colors use hex format with optional alpha: `#RRGGBB` or `#RRGGBBAA`.

Common alpha suffixes used in Crystal City:

| Suffix | Opacity | Usage |
|---|---|---|
| `ff` | 100% | Fully opaque (often omitted) |
| `d7` | 84% | Low transparency backgrounds |
| `99` | 60% | Medium transparency backgrounds |
| `80` | 50% | Semi-transparent overlays |
| `4d` | 30% | High transparency backgrounds |
| `40` | 25% | Very transparent |
| `20` | 12.5% | Subtle tinted backgrounds |
| `00` | 0% | Fully transparent |

---

## Crystal City Color Palette

| Name | Hex | Role |
|---|---|---|
| Obsidian | `#0A0E1A` | Editor canvas, primary background |
| Deep Void | `#060910` | Sidebar, panels, title bar |
| Highlight | `#111728` | Active line, elevated surfaces |
| Border | `#1C2333` | Panel separators |
| Selection | `#1A2850` | Text selection background |
| Frost White | `#D8DEE9` | Primary text, variables |
| Steel Grey | `#7B88A1` | Operators, punctuation, muted text |
| Slate Indigo | `#4A5270` | Inactive text, placeholders |
| Gutter | `#2E3550` | Line numbers |
| Crystal Teal | `#56D4C8` | Functions, methods (hero color) |
| Mint Glass | `#89DDCA` | Strings, raw text, created/success |
| Glacier Blue | `#7EC8E3` | Types, tags, constructors, enums |
| Dusty Rose | `#E8A0BF` | Constants, booleans |
| Neon Rose | `#FF6B9D` | Cursor, focused borders, string escapes |
| City Gold | `#F0C674` | Numbers, warnings, conflicts |
| Glass Blue | `#61AFEF` | Info, renamed items |
| Crystal Violet | `#B48EF0` | Attributes, properties |
| Signal Red | `#E06C75` | Errors, deletions |
| Sage Teal | `#5A8A7A` | Comments (italic) |

---

## UI Properties

### Backgrounds & Surfaces

| Property | Crystal City | One Dark (reference) | Description |
|---|---|---|---|
| `background` | `#060910` | `#3b414d` | App background (behind all panels) |
| `surface.background` | `#0A0E1A` | `#2f343e` | Editor surface |
| `elevated_surface.background` | `#111728` | `#2f343e` | Elevated panels, popovers |
| `panel.background` | `#060910` | `#2f343e` | Side panels |
| `panel.overlay_background` | `#060910` | — | Panel overlay (transparency variants) |

### Title Bar & Status Bar

| Property | Crystal City | Description |
|---|---|---|
| `title_bar.background` | `#060910` | Title bar background |
| `title_bar.inactive_background` | `#060910` | Title bar when window unfocused |
| `status_bar.background` | `#060910` | Bottom status bar |
| `toolbar.background` | `#0A0E1A` | Toolbar above editor |

### Tabs

| Property | Crystal City | Description |
|---|---|---|
| `tab_bar.background` | `#060910` | Tab strip background |
| `tab.active_background` | `#0A0E1A` | Active tab |
| `tab.inactive_background` | `#060910` | Inactive tabs |

### Borders

| Property | Crystal City | Description |
|---|---|---|
| `border` | `#1C2333` | Default border |
| `border.variant` | `#1C2333` | Secondary border variant |
| `border.focused` | `#FF6B9D` | Focused element border (Neon Rose) |
| `border.selected` | `#FF6B9D` | Selected element border |
| `border.transparent` | `#00000000` | Invisible border |
| `border.disabled` | `#1C233380` | Disabled state border |
| `pane.focused_border` | `#FF6B9D` | Focused pane border |
| `pane_group.border` | `#1C2333` | Pane group divider |
| `panel.focused_border` | `#FF6B9D` | Focused panel border |

### Text

| Property | Crystal City | Description |
|---|---|---|
| `text` | `#D8DEE9` | Default text |
| `text.muted` | `#7B88A1` | Muted/secondary text |
| `text.placeholder` | `#4A5270` | Placeholder text |
| `text.disabled` | `#2E3550` | Disabled text |
| `text.accent` | `#FF6B9D` | Accent text (Neon Rose) |

### Icons

| Property | Crystal City | Description |
|---|---|---|
| `icon` | `#7B88A1` | Default icon color |
| `icon.muted` | `#4A5270` | Muted icon |
| `icon.disabled` | `#2E3550` | Disabled icon |
| `icon.placeholder` | `#4A5270` | Placeholder icon |
| `icon.accent` | `#FF6B9D` | Accent icon |

### Interactive Elements

| Property | Crystal City | Description |
|---|---|---|
| `element.background` | `#111728` | Element resting state |
| `element.hover` | `#1C2333` | Element on hover |
| `element.active` | `#1A2850` | Element when active/pressed |
| `element.selected` | `#1A2850` | Element when selected |
| `element.disabled` | `#11172880` | Element when disabled |

### Ghost Elements (transparent resting state)

| Property | Crystal City | Description |
|---|---|---|
| `ghost_element.background` | `#00000000` | Ghost element at rest (invisible) |
| `ghost_element.hover` | `#111728` | Ghost element on hover |
| `ghost_element.active` | `#1A2850` | Ghost element when active |
| `ghost_element.selected` | `#1A2850` | Ghost element when selected |
| `ghost_element.disabled` | `#11172880` | Ghost element when disabled |

### Editor

| Property | Crystal City | Description |
|---|---|---|
| `editor.background` | `#0A0E1A` | Editor canvas |
| `editor.foreground` | `#D8DEE9` | Default editor text |
| `editor.gutter.background` | `#0A0E1A` | Gutter area |
| `editor.line_number` | `#2E3550` | Line numbers |
| `editor.active_line_number` | `#7B88A1` | Active line number |
| `editor.active_line.background` | `#111728` | Active line highlight |
| `editor.highlighted_line.background` | `#111728` | Highlighted line |
| `editor.subheader.background` | `#060910` | Subheader background |
| `editor.invisible` | `#1C2333` | Invisible characters |
| `editor.wrap_guide` | `#1C2333` | Wrap guide column |
| `editor.active_wrap_guide` | `#4A5270` | Active wrap guide |
| `editor.indent_guide` | `#1C2333` | Indent guides |
| `editor.indent_guide_active` | `#4A5270` | Active indent guide |

### Editor Document Highlights

| Property | Crystal City | Description |
|---|---|---|
| `editor.document_highlight.read_background` | `#1A285060` | Read reference highlight |
| `editor.document_highlight.write_background` | `#1A285090` | Write reference highlight |
| `editor.document_highlight.bracket_background` | `#111728` | Matching bracket highlight |

### Panel Indent Guides

| Property | Crystal City | Description |
|---|---|---|
| `panel.indent_guide` | `#1C2333` | Panel indent guide |
| `panel.indent_guide_active` | `#4A5270` | Active panel indent guide |
| `panel.indent_guide_hover` | `#7B88A1` | Hovered panel indent guide |

### Scrollbar

| Property | Crystal City | Description |
|---|---|---|
| `scrollbar.track.background` | `#06091000` | Scrollbar track (transparent) |
| `scrollbar.track.border` | `#1C233300` | Track border |
| `scrollbar.thumb.background` | `#4A527040` | Thumb resting state |
| `scrollbar.thumb.hover_background` | `#4A527080` | Thumb on hover |
| `scrollbar.thumb.border` | `#4A527000` | Thumb border |

### Search

| Property | Crystal City | Description |
|---|---|---|
| `search.match_background` | `#1A2850` | Search match highlight |
| `drop_target.background` | `#1A285080` | Drag-and-drop target |
| `link_text.hover` | `#56D4C8` | Hovered link text |

---

## Semantic Status Colors

These colors indicate file/item states throughout the UI:

| State | Color | Background | Border | Description |
|---|---|---|---|---|
| `created` / `success` | `#89DDCA` | `#89DDCA20` | `#89DDCA` | New files, successful operations |
| `modified` / `conflict` / `warning` | `#F0C674` | `#F0C67420` | `#F0C674` | Changed files, warnings |
| `deleted` / `error` | `#E06C75` | `#E06C7520` | `#E06C75` | Removed files, errors |
| `renamed` / `info` | `#61AFEF` | `#61AFEF20` | `#61AFEF` | Renamed files, info messages |
| `hint` | `#56D4C8` | `#56D4C820` | `#56D4C8` | Hints |
| `hidden` / `ignored` | `#4A5270` | `#060910` | `#1C2333` | Hidden/ignored files |
| `unreachable` | `#4A5270` | `#111728` | `#1C2333` | Unreachable code |
| `predictive` | `#4A5270` | `#111728` | `#1C2333` | AI/predictive text |

---

## Terminal ANSI Colors

| ANSI Color | Normal | Bright | Dim |
|---|---|---|---|
| Black | `#0A0E1A` | `#4A5270` | `#060910` |
| Red | `#E06C75` | `#E88D94` | `#B4565E` |
| Green | `#89DDCA` | `#A8E8D8` | `#6DB3A2` |
| Yellow | `#F0C674` | `#F5D898` | `#C09F5D` |
| Blue | `#61AFEF` | `#8AC6F5` | `#4E8CBF` |
| Magenta | `#B48EF0` | `#CBACF5` | `#9072C0` |
| Cyan | `#56D4C8` | `#7FE3DA` | `#45A9A0` |
| White | `#D8DEE9` | `#FFFFFF` | `#7B88A1` |

---

## Players (Multi-cursor / Collaboration)

Each player gets a unique cursor, background, and selection color. Crystal City defines 8 players:

| # | Cursor Color | Name |
|---|---|---|
| 1 | `#FF6B9D` | Neon Rose (primary) |
| 2 | `#56D4C8` | Crystal Teal |
| 3 | `#F0C674` | City Gold |
| 4 | `#B48EF0` | Crystal Violet |
| 5 | `#61AFEF` | Glass Blue |
| 6 | `#E8A0BF` | Dusty Rose |
| 7 | `#89DDCA` | Mint Glass |
| 8 | `#7EC8E3` | Glacier Blue |

Background colors are the cursor color at 12.5% opacity (`20`), selection at 19% (`30`).

---

## Syntax Highlighting

### Crystal City Token Mapping

| Scope | Crystal City | One Dark (reference) | Description |
|---|---|---|---|
| `attribute` | `#B48EF0` italic | `#74ade8` | HTML/XML attributes |
| `boolean` | `#E8A0BF` | `#bf956a` | `true`, `false` |
| `comment` | `#5A8A7A` italic | `#5d636f` | Code comments |
| `comment.doc` | `#5A8A7A` italic | `#878e98` | Documentation comments |
| `constant` | `#E8A0BF` | `#dfc184` | Named constants |
| `constructor` | `#7EC8E3` | `#73ade9` | Constructor calls |
| `embedded` | `#D8DEE9` | `#dce0e5` | Embedded code |
| `emphasis` | italic | `#74ade8` | Emphasis (markdown) |
| `emphasis.strong` | bold (700) | `#bf956a` bold | Strong emphasis |
| `enum` | `#7EC8E3` | `#6eb4bf` | Enum types |
| `function` | `#56D4C8` | `#73ade9` | Function names |
| `function.builtin` | `#56D4C8` | — | Built-in functions |
| `function.definition` | `#56D4C8` | — | Function definitions |
| `function.method` | `#56D4C8` | — | Method names |
| `function.special` | `#56D4C8` | — | Special functions |
| `hint` | `#56D4C8` italic | `#788ca6` | Hint annotations |
| `keyword` | `#FFFFFF` bold | `#b477cf` | Language keywords |
| `label` | `#56D4C8` | `#74ade8` | Labels |
| `link_text` | `#89DDCA` | `#73ade9` | Link display text |
| `link_uri` | `#56D4C8` | `#6eb4bf` | Link URLs |
| `number` | `#F0C674` | `#bf956a` | Numeric literals |
| `operator` | `#7B88A1` | `#6eb4bf` | Operators |
| `predictive` | `#4A5270` italic | `#5a6a87` italic | AI predictions |
| `preproc` | `#FFFFFF` | `#dce0e5` | Preprocessor directives |
| `primary` | `#D8DEE9` | `#acb2be` | Primary/default text |
| `property` | `#B48EF0` | `#d07277` | Object properties |
| `punctuation` | `#7B88A1` | `#acb2be` | General punctuation |
| `punctuation.bracket` | `#7B88A1` | `#b2b9c6` | Brackets/parens |
| `punctuation.delimiter` | `#7B88A1` | `#b2b9c6` | Delimiters (commas, etc.) |
| `punctuation.list_marker` | `#56D4C8` | `#d07277` | Markdown list markers |
| `punctuation.special` | `#56D4C8` | `#b1574b` | Interpolation brackets |
| `string` | `#89DDCA` | `#a1c181` | String literals |
| `string.doc` | `#89DDCA` | — | Doc strings |
| `string.escape` | `#FF6B9D` | `#878e98` | Escape sequences |
| `string.regex` | `#FF6B9D` | `#bf956a` | Regular expressions |
| `string.special` | `#89DDCA` | `#bf956a` | Special strings |
| `string.special.symbol` | `#B48EF0` | `#bf956a` | Symbols (Ruby, Elixir) |
| `tag` | `#7EC8E3` | `#74ade8` | HTML/XML tags |
| `text.literal` | `#89DDCA` | `#a1c181` | Literal text blocks |
| `title` | `#FFFFFF` bold | `#d07277` | Headings/titles |
| `type` | `#7EC8E3` | `#6eb4bf` | Type names |
| `type.builtin` | `#7EC8E3` | — | Built-in types |
| `variable` | `#D8DEE9` | `#acb2be` | Variables |
| `variable.member` | `#7B88A1` | — | Object members |
| `variable.parameter` | `#D8DEE9` italic | — | Function parameters |
| `variable.special` | `#D8DEE9` italic | `#bf956a` | Special variables (`this`, `self`) |
| `variant` | `#7EC8E3` | `#73ade9` | Enum variants |

---

## Transparency Variants

The transparent variants use `"background.appearance": "blurred"` and set UI backgrounds to various alpha levels:

| Element | Low (d7) | Medium (99) | High (4d) |
|---|---|---|---|
| App background | `#060910d7` | `#06091099` | `#0609104d` |
| Surface | `#0A0E1Ad0` | `#0A0E1A8c` | `#0A0E1A40` |
| Editor/terminal/panel | `#00000000` | `#00000000` | `#00000000` |
| Active tab | `#11172860` | `#11172840` | `#11172830` |

Transparent variants also adjust:
- Line numbers use `#ffffff20` (white at 12.5%) for contrast on any wallpaper
- Active line number uses `#FF6B9D90` (Neon Rose at 56%)
- Borders become mostly invisible (`#1C233315`)
- Selections and highlights use Neon Rose tints instead of fixed backgrounds

---

## Additional Scopes (from One Dark reference)

These scopes exist in Zed's One Dark but are not yet used by Crystal City. They can be added for more complete theme support:

| Scope | One Dark Color | Suggested Crystal City |
|---|---|---|
| `namespace` | `#dce0e5` | `#56D4C8` italic |
| `selector` | `#dfc184` | `#F0C674` |
| `selector.pseudo` | `#74ade8` | `#7EC8E3` |
| `punctuation.markup` | `#d07277` | `#E06C75` |
| `editor.hover_line_number` | `#acb0b4` | `#4A5270` |
| `search.active_match_background` | `#e8af7466` | `#FF6B9D40` |
| `version_control.added` | `#27a657` | `#89DDCA` |
| `version_control.modified` | `#d3b020` | `#F0C674` |
| `version_control.deleted` | `#e06c76` | `#E06C75` |
