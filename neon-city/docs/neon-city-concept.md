# Neon City — Color Scheme Concept

## Vision

Neon City is a high-performance coding color scheme built for developers who thrive in the dark. The philosophy is simple: midnight depth meets electric neon clarity.

It achieves this through three complementary ideas:

- **Midnight base** — a deep purple-black foundation that evokes rain-slicked streets under neon signs. Richer than pure black, with a purple undertone that creates a warm electronic atmosphere without competing with syntax.
- **Electric neon spectrum** — a vivid, high-saturation palette where each syntax role has its own unmistakable color. Electric Magenta (`#FF2CF1`) leads as the hero for functions, while strings glow in Plasma Green (`#39FF14`), types shine in Cyber Blue (`#00D4FF`), numbers burn in Neon Orange (`#FF6B2B`), and constants pulse in Hot Pink (`#FF69B4`). Every token is distinguishable at a glance.
- **White keyword anchors** — bold white keywords (`#FFFFFF`) cut through the neon to mark structural flow control, making `import`, `const`, `return`, and `export` instantly scannable as the skeleton of your code.

The result is a workspace that feels like coding inside a cyberpunk cityscape — vivid, focused, and alive.

---

## Design Principles

### 1. Differentiated Spectrum

Each major syntax role gets its own vivid neon color. Unlike muted palettes, Neon City embraces high saturation — every color is a distinct signal that pops against the midnight background. The purple-black base keeps the neon colors from clashing.

### 2. Structural Anchors in White

Keywords are the only tokens rendered in bold white. This creates a clear visual hierarchy:

| Role | Color | Hex | Why |
|---|---|---|---|
| Keywords & flow control | Bold White | `#FFFFFF` | Structural anchors — the skeleton of logic. Bold white cuts through the neon to mark control flow. |
| Functions & methods | Electric Magenta | `#FF2CF1` | The hero color — functions are the most frequent semantic token and get the dominant neon glow. |
| Strings & text | Plasma Green | `#39FF14` | Electric green — distinct from functions, reads as "data". Like neon tube lettering. |
| Numbers & numeric literals | Neon Orange | `#FF6B2B` | Hot orange stands out in the cool purple base — numbers are immediately scannable. |
| Types, tags & constructors | Cyber Blue | `#00D4FF` | Electric blue separates type annotations from values — the holographic scaffolding of your type system. |
| Constants & booleans | Hot Pink | `#FF69B4` | Bright pink marks immutable values — semantically "fixed" things deserve a vivid marker. |
| Variables & parameters | Neon White | `#E0D4FF` | Cool lavender-white keeps the most common tokens neutral and legible. |
| Comments | Twilight Indigo | `#6B5B95` | A muted purple — present when you look, recessive when you don't. |
| Attributes & props | Neon Yellow | `#FFE744` | The yellow neon highlight for HTML/JSX attributes and object properties. |

### 3. Minimal Chrome, Maximum Depth

- **No harsh borders.** Panel separation comes from background color shifts (#0D0221 for editor, #07010F for sidebar/panels). This creates a sense of physical depth instead of flat dividing lines.
- **Active tab indicator.** A single Electric Cyan bottom-border marks the active file — one bright line in a sea of dark tones.
- **Restrained error states.** Errors use Alarm Red (`#FF1744`) — clearly an error, but tuned to avoid triggering anxiety during long sessions.

### 4. The Cursor as Anchor

The caret and selection both use Electric Cyan (`#00FFFF`). In a scheme this dark, the cursor must be unmissable. It serves as the constant anchor point — you should never have to hunt for where you're typing.

---

## Color Palette Summary

### Backgrounds & UI

| Component | Hex | Role |
|---|---|---|
| Primary Background | `#0D0221` | Editor canvas. Midnight purple-black. |
| Sidebar / Panel Background | `#07010F` | Darker offset for spatial depth. |
| Line Numbers / Gutter | `#3D2E5C` | Muted purple. Visible, recessive. |
| Caret / Selection | `#00FFFF` | Electric cyan. Unmissable anchor. |

### Syntax Tokens

| Token | Hex | Name |
|---|---|---|
| Keywords & flow control | `#FFFFFF` | Bold White |
| Functions & methods | `#FF2CF1` | Electric Magenta |
| Strings & text | `#39FF14` | Plasma Green |
| Types, tags & constructors | `#00D4FF` | Cyber Blue |
| Numbers & literals | `#FF6B2B` | Neon Orange |
| Constants & booleans | `#FF69B4` | Hot Pink |
| Variables & parameters | `#E0D4FF` | Neon White |
| Comments & docs | `#6B5B95` | Twilight Indigo |

### Supplementary Colors

| Use | Hex | Name |
|---|---|---|
| Attributes / props | `#FFE744` | Neon Yellow |
| Error states | `#FF1744` | Alarm Red |
| Cursor & active tab | `#00FFFF` | Electric Cyan |
| Warnings & conflicts | `#FFE744` | Neon Yellow |
| Info diagnostics | `#448AFF` | Signal Blue |
| Operators & punctuation | `#8B7BAE` | Dusk Mauve |
| String escapes & regex | `#00FFFF` | Electric Cyan |

---

## Typography Pairing

The "Neon City" identity is reinforced by pairing the palette with modern monospace fonts that support programming ligatures:

- **Primary recommendation:** JetBrains Mono — clean geometry, optimized for code readability at small sizes.
- **Alternative:** Fira Code — excellent ligature set (arrows, comparisons, lambda).

Ligatures like `=>`, `!==`, and `>=` rendered as single glyphs contribute to the polished, high-tech aesthetic the scheme targets.

---

## How It Feels in Practice

Imagine opening a React file at 2 AM:

- The background is deep midnight — purple-black, like a rain-soaked alley between skyscrapers.
- Your eye lands on **bold white keywords** first — they sketch out the control flow like neon wireframes.
- Electric Magenta marks every function call. Plasma Green wraps every string in an electric glow. Cyber Blue traces the type annotations and JSX tags. Neon Orange punches through for numeric literals. Hot Pink softly highlights your constants and booleans.
- Yellow attributes provide vivid contrast — `intensity`, `theme`, `className` glow in neon yellow.
- Variables sit in neutral Neon White. Operators and brackets in Dusk Mauve form the connective tissue.
- Comments are there if you look — a muted twilight indigo that doesn't compete.
- Your cursor pulses in electric cyan. You always know where you are.

That's Neon City.
