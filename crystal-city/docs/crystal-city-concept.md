# Crystal City — Color Scheme Concept

## Vision

Crystal City is a high-performance coding color scheme built for developers who spend long hours in their editor. The philosophy is simple: obsidian depth meets crystalline clarity.

It achieves this through three complementary ideas:

- **Obsidian base** — a deep blue-black foundation that evokes the night sky between glass towers. Richer than pure black, less fatiguing than grey, with enough blue undertone to feel alive without competing with syntax.
- **Crystalline spectrum** — a harmonized cool-toned palette where each syntax role has its own distinct color. Crystal Teal (`#56D4C8`) leads as the hero for functions, while strings glow in Mint Glass (`#89DDCA`), types shine in Glacier Blue (`#7EC8E3`), numbers warm in City Gold (`#F0C674`), and constants pulse in Dusty Rose (`#E8A0BF`). Every token is distinguishable at a glance.
- **White keyword anchors** — bold white keywords (`#FFFFFF`) cut through the spectrum to mark structural flow control, making `import`, `const`, `return`, and `export` instantly scannable as the skeleton of your code.

The result is a workspace that feels like looking into a dark crystal — calm, focused, and sharp.

---

## Design Principles

### 1. Differentiated Spectrum

Each major syntax role gets its own color from a harmonized cool-toned palette. This provides maximum semantic information while maintaining visual cohesion — all colors sit comfortably together because they share the same cool undertone and saturation family.

### 2. Structural Anchors in White

Keywords are the only tokens rendered in bold white. This creates a clear visual hierarchy:

| Role | Color | Hex | Why |
|---|---|---|---|
| Keywords & flow control | Bold White | `#FFFFFF` | Structural anchors — the skeleton of logic. Bold white cuts through the spectrum to mark control flow. |
| Functions & methods | Crystal Teal | `#56D4C8` | The hero color — functions are the most frequent semantic token and get the dominant hue. |
| Strings & text | Mint Glass | `#89DDCA` | A warmer, greener teal — distinct from functions, reads as "data". |
| Numbers & numeric literals | City Gold | `#F0C674` | Warm amber stands out clearly in the cool palette — numbers are immediately scannable. |
| Types, tags & constructors | Glacier Blue | `#7EC8E3` | Cool blue separates type annotations from values — the structural scaffolding of your type system. |
| Constants & booleans | Dusty Rose | `#E8A0BF` | Soft pink marks immutable values — semantically "fixed" things deserve a unique color. |
| Variables & parameters | Frost White | `#D8DEE9` | Cool off-white keeps the most common tokens neutral and legible. |
| Comments | Sage Teal | `#5A8A7A` | A muted, organic teal — present when you look, recessive when you don't. |
| Attributes & props | Crystal Violet | `#B48EF0` | The violet highlight for HTML/JSX attributes and object properties. |

### 3. Minimal Chrome, Maximum Depth

- **No harsh borders.** Panel separation comes from background color shifts (#0A0E1A for editor, #060910 for sidebar/panels). This creates a sense of physical depth instead of flat dividing lines.
- **Active tab indicator.** A single Neon Rose bottom-border marks the active file — one bright line in a sea of muted tones.
- **Restrained error states.** Errors use Signal Red (`#E06C75`) instead of emergency red. Still clearly an error, but doesn't trigger an anxiety response during long sessions.

### 4. The Cursor as Anchor

The caret and selection both use Neon Rose (`#FF6B9D`). In a scheme this dark, the cursor must be unmissable. It serves as the constant anchor point — you should never have to hunt for where you're typing.

---

## Color Palette Summary

### Backgrounds & UI

| Component | Hex | Role |
|---|---|---|
| Primary Background | `#0A0E1A` | Editor canvas. Obsidian blue-black. |
| Sidebar / Panel Background | `#060910` | Darker offset for spatial depth. |
| Line Numbers / Gutter | `#2E3550` | Muted slate. Visible, recessive. |
| Caret / Selection | `#FF6B9D` | Neon rose. Unmissable anchor. |

### Syntax Tokens

| Token | Hex | Name |
|---|---|---|
| Keywords & flow control | `#FFFFFF` | Bold White |
| Functions & methods | `#56D4C8` | Crystal Teal |
| Strings & text | `#89DDCA` | Mint Glass |
| Types, tags & constructors | `#7EC8E3` | Glacier Blue |
| Numbers & literals | `#F0C674` | City Gold |
| Constants & booleans | `#E8A0BF` | Dusty Rose |
| Variables & parameters | `#D8DEE9` | Frost White |
| Comments & docs | `#5A8A7A` | Sage Teal |

### Supplementary Colors

| Use | Hex | Name |
|---|---|---|
| Attributes / props | `#B48EF0` | Crystal Violet |
| Error states | `#E06C75` | Signal Red |
| Cursor & active tab | `#FF6B9D` | Neon Rose |
| Warnings & conflicts | `#F0C674` | City Gold |
| Info diagnostics | `#61AFEF` | Glass Blue |
| Operators & punctuation | `#7B88A1` | Steel Grey |
| String escapes & regex | `#FF6B9D` | Neon Rose |

---

## Typography Pairing

The "Crystal City" identity is reinforced by pairing the palette with modern monospace fonts that support programming ligatures:

- **Primary recommendation:** JetBrains Mono — clean geometry, optimized for code readability at small sizes.
- **Alternative:** Fira Code — excellent ligature set (arrows, comparisons, lambda).

Ligatures like `=>`, `!==`, and `>=` rendered as single glyphs contribute to the polished, high-tech aesthetic the scheme targets.

---

## How It Feels in Practice

Imagine opening a React file at 11 PM:

- The background is dark but not void — it has a subtle obsidian depth.
- Your eye lands on **bold white keywords** first — they sketch out the control flow like a blueprint.
- Crystal Teal marks every function call. Mint Glass wraps every string in a slightly warmer glow. Glacier Blue traces the type annotations and JSX tags. City Gold punches through for numeric literals. Dusty Rose softly highlights your constants and booleans.
- Violet attributes provide rich contrast — `intensity`, `theme`, `className` glow in purple.
- Variables sit in neutral Frost White. Operators and brackets in Steel Grey form the connective tissue.
- Comments are there if you look — a muted sage teal that doesn't compete.
- Your cursor pulses in rose. You always know where you are.

That's Crystal City.
