# Zed Theme Reference — Neon City

A comprehensive reference for Zed editor theme properties, showing how Neon City maps its palette to each scope. Derived from the [Zed theme schema](https://zed.dev/schema/themes/v0.2.0.json) and the official [One Dark/Light theme](https://github.com/zed-industries/zed/blob/main/assets/themes/one/one.json).

---

## Installation

### As an Extension

Place the following files in a Zed extension directory:

```
neon-city/
  extension.toml
  themes/
    neon-city.json
```

Then install via Zed's extension system or by placing it in `~/.config/zed/extensions/`.

### Theme Selection

Neon City ships with 4 variants in a single file:

| Variant | Description |
|---|---|
| **Neon City** | Fully opaque backgrounds |
| **Neon City Low Transparency** | ~84% opacity backgrounds (blurred) |
| **Neon City Medium Transparency** | ~60% opacity backgrounds (blurred) |
| **Neon City High Transparency** | ~30% opacity backgrounds (blurred) |

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
      "appearance": "dark",
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

Common alpha suffixes used in Neon City:

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

## Neon City Color Palette

| Name | Hex | Role |
|---|---|---|
| Midnight | `#0D0221` | Editor canvas, primary background |
| Void Black | `#07010F` | Sidebar, panels, title bar |
| Highlight | `#1A0A3E` | Active line, elevated surfaces |
| Border | `#2A1454` | Panel separators |
| Selection | `#2D1B69` | Text selection background |
| Neon White | `#E0D4FF` | Primary text, variables |
| Dusk Mauve | `#8B7BAE` | Operators, punctuation, muted text |
| Shadow Purple | `#5C4A82` | Inactive text, placeholders |
| Gutter | `#3D2E5C` | Line numbers |
| Electric Magenta | `#FF2CF1` | Functions, methods (hero color) |
| Plasma Green | `#39FF14` | Strings, raw text, created/success |
| Cyber Blue | `#00D4FF` | Types, tags, constructors, enums |
| Hot Pink | `#FF69B4` | Constants, booleans |
| Electric Cyan | `#00FFFF` | Cursor, focused borders, string escapes |
| Neon Orange | `#FF6B2B` | Numbers, warnings, conflicts |
| Signal Blue | `#448AFF` | Info, renamed items |
| Neon Yellow | `#FFE744` | Attributes, properties |
| Alarm Red | `#FF1744` | Errors, deletions |
| Twilight Indigo | `#6B5B95` | Comments (italic) |

---

## UI Properties

### Backgrounds & Surfaces

| Property | Neon City | Description |
|---|---|---|
| `background` | `#07010F` | App background (behind all panels) |
| `surface.background` | `#0D0221` | Editor surface |
| `elevated_surface.background` | `#1A0A3E` | Elevated panels, popovers |
| `panel.background` | `#07010F` | Side panels |
| `panel.overlay_background` | `#07010F` | Panel overlay (transparency variants) |

### Title Bar & Status Bar

| Property | Neon City | Description |
|---|---|---|
| `title_bar.background` | `#07010F` | Title bar background |
| `title_bar.inactive_background` | `#07010F` | Title bar when window unfocused |
| `status_bar.background` | `#07010F` | Bottom status bar |
| `toolbar.background` | `#0D0221` | Toolbar above editor |

### Tabs

| Property | Neon City | Description |
|---|---|---|
| `tab_bar.background` | `#07010F` | Tab strip background |
| `tab.active_background` | `#0D0221` | Active tab |
| `tab.inactive_background` | `#07010F` | Inactive tabs |

### Borders

| Property | Neon City | Description |
|---|---|---|
| `border` | `#2A1454` | Default border |
| `border.variant` | `#2A1454` | Secondary border variant |
| `border.focused` | `#00FFFF` | Focused element border (Electric Cyan) |
| `border.selected` | `#00FFFF` | Selected element border |
| `border.transparent` | `#00000000` | Invisible border |
| `border.disabled` | `#2A145480` | Disabled state border |
| `pane.focused_border` | `#00FFFF` | Focused pane border |
| `pane_group.border` | `#2A1454` | Pane group divider |
| `panel.focused_border` | `#00FFFF` | Focused panel border |

### Text

| Property | Neon City | Description |
|---|---|---|
| `text` | `#E0D4FF` | Default text |
| `text.muted` | `#8B7BAE` | Muted/secondary text |
| `text.placeholder` | `#5C4A82` | Placeholder text |
| `text.disabled` | `#3D2E5C` | Disabled text |
| `text.accent` | `#00FFFF` | Accent text (Electric Cyan) |

### Icons

| Property | Neon City | Description |
|---|---|---|
| `icon` | `#8B7BAE` | Default icon color |
| `icon.muted` | `#5C4A82` | Muted icon |
| `icon.disabled` | `#3D2E5C` | Disabled icon |
| `icon.placeholder` | `#5C4A82` | Placeholder icon |
| `icon.accent` | `#00FFFF` | Accent icon |

### Interactive Elements

| Property | Neon City | Description |
|---|---|---|
| `element.background` | `#1A0A3E` | Element resting state |
| `element.hover` | `#2A1454` | Element on hover |
| `element.active` | `#2D1B69` | Element when active/pressed |
| `element.selected` | `#2D1B69` | Element when selected |
| `element.disabled` | `#1A0A3E80` | Element when disabled |

### Ghost Elements (transparent resting state)

| Property | Neon City | Description |
|---|---|---|
| `ghost_element.background` | `#00000000` | Ghost element at rest (invisible) |
| `ghost_element.hover` | `#1A0A3E` | Ghost element on hover |
| `ghost_element.active` | `#2D1B69` | Ghost element when active |
| `ghost_element.selected` | `#2D1B69` | Ghost element when selected |
| `ghost_element.disabled` | `#1A0A3E80` | Ghost element when disabled |

### Editor

| Property | Neon City | Description |
|---|---|---|
| `editor.background` | `#0D0221` | Editor canvas |
| `editor.foreground` | `#E0D4FF` | Default editor text |
| `editor.gutter.background` | `#0D0221` | Gutter area |
| `editor.line_number` | `#3D2E5C` | Line numbers |
| `editor.active_line_number` | `#8B7BAE` | Active line number |
| `editor.active_line.background` | `#1A0A3E` | Active line highlight |
| `editor.highlighted_line.background` | `#1A0A3E` | Highlighted line |
| `editor.subheader.background` | `#07010F` | Subheader background |
| `editor.invisible` | `#2A1454` | Invisible characters |
| `editor.wrap_guide` | `#2A1454` | Wrap guide column |
| `editor.active_wrap_guide` | `#5C4A82` | Active wrap guide |
| `editor.indent_guide` | `#2A1454` | Indent guides |
| `editor.indent_guide_active` | `#5C4A82` | Active indent guide |

### Editor Document Highlights

| Property | Neon City | Description |
|---|---|---|
| `editor.document_highlight.read_background` | `#2D1B6960` | Read reference highlight |
| `editor.document_highlight.write_background` | `#2D1B6990` | Write reference highlight |
| `editor.document_highlight.bracket_background` | `#1A0A3E` | Matching bracket highlight |

### Scrollbar

| Property | Neon City | Description |
|---|---|---|
| `scrollbar.track.background` | `#07010F00` | Scrollbar track (transparent) |
| `scrollbar.track.border` | `#2A145400` | Track border |
| `scrollbar.thumb.background` | `#5C4A8240` | Thumb resting state |
| `scrollbar.thumb.hover_background` | `#5C4A8280` | Thumb on hover |
| `scrollbar.thumb.border` | `#5C4A8200` | Thumb border |

### Search

| Property | Neon City | Description |
|---|---|---|
| `search.match_background` | `#2D1B69` | Search match highlight |
| `drop_target.background` | `#2D1B6980` | Drag-and-drop target |
| `link_text.hover` | `#FF2CF1` | Hovered link text |

---

## Semantic Status Colors

These colors indicate file/item states throughout the UI:

| State | Color | Background | Border | Description |
|---|---|---|---|---|
| `created` / `success` | `#39FF14` | `#39FF1420` | `#39FF14` | New files, successful operations |
| `modified` / `conflict` / `warning` | `#FFE744` | `#FFE74420` | `#FFE744` | Changed files, warnings |
| `deleted` / `error` | `#FF1744` | `#FF174420` | `#FF1744` | Removed files, errors |
| `renamed` / `info` | `#448AFF` | `#448AFF20` | `#448AFF` | Renamed files, info messages |
| `hint` | `#FF2CF1` | `#FF2CF120` | `#FF2CF1` | Hints |
| `hidden` / `ignored` | `#5C4A82` | `#07010F` | `#2A1454` | Hidden/ignored files |
| `unreachable` | `#5C4A82` | `#1A0A3E` | `#2A1454` | Unreachable code |
| `predictive` | `#5C4A82` | `#1A0A3E` | `#2A1454` | AI/predictive text |

---

## Terminal ANSI Colors

| ANSI Color | Normal | Bright | Dim |
|---|---|---|---|
| Black | `#0D0221` | `#5C4A82` | `#07010F` |
| Red | `#FF1744` | `#FF5370` | `#CC1236` |
| Green | `#39FF14` | `#69FF54` | `#2DCC10` |
| Yellow | `#FFE744` | `#FFF176` | `#CCB936` |
| Blue | `#448AFF` | `#82B1FF` | `#366ECC` |
| Magenta | `#FF2CF1` | `#FF6FF8` | `#CC23C1` |
| Cyan | `#00D4FF` | `#4DE8FF` | `#00A9CC` |
| White | `#E0D4FF` | `#FFFFFF` | `#8B7BAE` |

---

## Players (Multi-cursor / Collaboration)

Each player gets a unique cursor, background, and selection color. Neon City defines 8 players:

| # | Cursor Color | Name |
|---|---|---|
| 1 | `#00FFFF` | Electric Cyan (primary) |
| 2 | `#FF2CF1` | Electric Magenta |
| 3 | `#FFE744` | Neon Yellow |
| 4 | `#39FF14` | Plasma Green |
| 5 | `#448AFF` | Signal Blue |
| 6 | `#FF69B4` | Hot Pink |
| 7 | `#FF6B2B` | Neon Orange |
| 8 | `#00D4FF` | Cyber Blue |

Background colors are the cursor color at 12.5% opacity (`20`), selection at 19% (`30`).

---

## Syntax Highlighting

### Neon City Token Mapping

| Scope | Neon City | Description |
|---|---|---|
| `attribute` | `#FFE744` italic | HTML/XML attributes |
| `boolean` | `#FF69B4` | `true`, `false` |
| `comment` | `#6B5B95` italic | Code comments |
| `comment.doc` | `#6B5B95` italic | Documentation comments |
| `constant` | `#FF69B4` | Named constants |
| `constructor` | `#00D4FF` | Constructor calls |
| `embedded` | `#E0D4FF` | Embedded code |
| `emphasis` | italic | Emphasis (markdown) |
| `emphasis.strong` | bold (700) | Strong emphasis |
| `enum` | `#00D4FF` | Enum types |
| `function` | `#FF2CF1` | Function names |
| `function.builtin` | `#FF2CF1` | Built-in functions |
| `function.definition` | `#FF2CF1` | Function definitions |
| `function.method` | `#FF2CF1` | Method names |
| `function.special` | `#FF2CF1` | Special functions |
| `hint` | `#FF2CF1` italic | Hint annotations |
| `keyword` | `#FFFFFF` bold | Language keywords |
| `label` | `#FF2CF1` | Labels |
| `link_text` | `#39FF14` | Link display text |
| `link_uri` | `#FF2CF1` | Link URLs |
| `number` | `#FF6B2B` | Numeric literals |
| `operator` | `#8B7BAE` | Operators |
| `predictive` | `#5C4A82` italic | AI predictions |
| `preproc` | `#FFFFFF` | Preprocessor directives |
| `primary` | `#E0D4FF` | Primary/default text |
| `property` | `#FFE744` | Object properties |
| `punctuation` | `#8B7BAE` | General punctuation |
| `punctuation.bracket` | `#8B7BAE` | Brackets/parens |
| `punctuation.delimiter` | `#8B7BAE` | Delimiters (commas, etc.) |
| `punctuation.list_marker` | `#FF2CF1` | Markdown list markers |
| `punctuation.special` | `#FF2CF1` | Interpolation brackets |
| `string` | `#39FF14` | String literals |
| `string.doc` | `#39FF14` | Doc strings |
| `string.escape` | `#00FFFF` | Escape sequences |
| `string.regex` | `#00FFFF` | Regular expressions |
| `string.special` | `#39FF14` | Special strings |
| `string.special.symbol` | `#FFE744` | Symbols (Ruby, Elixir) |
| `tag` | `#00D4FF` | HTML/XML tags |
| `text.literal` | `#39FF14` | Literal text blocks |
| `title` | `#FFFFFF` bold | Headings/titles |
| `type` | `#00D4FF` | Type names |
| `type.builtin` | `#00D4FF` | Built-in types |
| `variable` | `#E0D4FF` | Variables |
| `variable.member` | `#8B7BAE` | Object members |
| `variable.parameter` | `#E0D4FF` italic | Function parameters |
| `variable.special` | `#E0D4FF` italic | Special variables (`this`, `self`) |
| `variant` | `#00D4FF` | Enum variants |

---

## Transparency Variants

The transparent variants use `"background.appearance": "blurred"` and set UI backgrounds to various alpha levels:

| Element | Low (d7) | Medium (99) | High (4d) |
|---|---|---|---|
| App background | `#07010Fd7` | `#07010F99` | `#07010F4d` |
| Surface | `#0D0221d0` | `#0D02218c` | `#0D022140` |
| Editor/terminal/panel | `#00000000` | `#00000000` | `#00000000` |
| Active tab | `#1A0A3E60` | `#1A0A3E40` | `#1A0A3E30` |

Transparent variants also adjust:
- Line numbers use `#ffffff20` (white at 12.5%) for contrast on any wallpaper
- Active line number uses `#00FFFF90` (Electric Cyan at 56%)
- Borders become mostly invisible (`#2A145415`)
- Selections and highlights use Electric Cyan tints instead of fixed backgrounds

---

## Additional Scopes (from One Dark reference)

These scopes exist in Zed's One Dark but are not yet used by Neon City. They can be added for more complete theme support:

| Scope | Suggested Neon City |
|---|---|
| `namespace` | `#FF2CF1` italic |
| `selector` | `#FFE744` |
| `selector.pseudo` | `#00D4FF` |
| `punctuation.markup` | `#FF1744` |
| `editor.hover_line_number` | `#5C4A82` |
| `search.active_match_background` | `#00FFFF40` |
| `version_control.added` | `#39FF14` |
| `version_control.modified` | `#FFE744` |
| `version_control.deleted` | `#FF1744` |
