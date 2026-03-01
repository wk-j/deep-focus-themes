# Stargazer — Color Scheme Concept

## Vision

Stargazer is a high-performance coding color scheme built for developers who work deep into the night. The philosophy is simple: the silence of deep space meets the luminosity of a spiral galaxy.

It achieves this through three complementary ideas:

- **Void black grounds** — backgrounds drawn from the darkest regions of the night sky (`#090E1A` editor, `#060A12` panels), with no ambient light pollution to compete with code.
- **Galactic spectrum accents** — syntax colors extracted directly from the photograph: nebula cyan (`#29D7E8`) from the Milky Way arm, galactic gold (`#F5C842`) from the spiral core, aurora green (`#4DC98A`) from star clusters, sky blue (`#7EC8E3`) from the upper atmosphere.
- **Golden keywords, cool syntax** — warm gold for structural keywords creates a temperature contrast against the cool blue-teal spectrum of the code body, making flow control unmissable.

The result is a workspace that feels like sitting on the roof of a car at midnight, watching the cosmos turn overhead.

---

## Design Principles

### 1. Astrophotography as Palette Source

Every accent color in Stargazer is traceable to the reference image. The dominant teal-cyan of the Milky Way arm becomes functions — the code element you read most. The glowing gold-white spiral core becomes keywords — structural, warm, gravitationally important. The horizon's amber glow becomes number literals. The upper midnight blue becomes tags and HTML/XML structure. No color was invented; all were observed.

### 2. A Clear Visual Hierarchy Through Temperature

The palette is split by color temperature to encode semantic importance. This creates a clear visual hierarchy:

| Role | Color | Hex | Why |
|---|---|---|---|
| Keywords | Galactic Gold | `#F5C842` | Warm; structural anchors that define flow |
| Functions | Nebula Cyan | `#29D7E8` | Hero color; most frequent active element |
| Strings | Aurora Green | `#4DC98A` | Cool-warm bridge; content distinct from code |
| Types | Star Field Blue | `#7EC8E3` | Cool; stable, definitional |
| Literals / Numbers | Amber Core | `#E8922A` | Warm accent; immediate, concrete values |
| Constants | White Star | `#EDF4FF` | Near-white; fixed, luminous, absolute |
| Attributes | Twilight Violet | `#7B8FD4` | Mid-register; metadata, not logic |
| Variables | Moonlight | `#D6E8F5` | Near-white; readable but recessive |
| Comments | Dark Matter | `#4D6D88` | Low-contrast; present but invisible at speed |
| Errors | Red Giant | `#E85555` | Red; unmistakable, but not alarming |

### 3. Minimal Chrome, Maximum Depth

- **No harsh borders.** Panel separation comes from background shifts — `#090E1A` for the editor, `#060A12` for sidebar/panels, just enough to distinguish depth without drawing a visible line.
- **Active tab indicator.** A single nebula cyan mark identifies the current file.
- **Restrained error states.** Errors use Red Giant (`#E85555`) — clearly wrong, but warm enough to feel correctable rather than catastrophic.

### 4. The Cursor as Anchor

The caret and selection both use nebula cyan (`#29D7E8`). Against the void-black background, the cursor must be unmissable — it is the one point of light you always return to. Matching it to the function color creates a subconscious link: the cursor is where the next function begins.

---

## Color Palette Summary

### Backgrounds & UI

| Component | Hex | Role |
|---|---|---|
| Editor background | `#090E1A` | Deep Space — primary surface |
| Sidebar / panels | `#060A12` | Void Black — recessed panels |
| Selection / highlights | `#111B2E` | Nebula Dust — active region |
| Border / separator | `#1A2840` | Horizon — subtle structural lines |

### Syntax Tokens

| Token | Hex | Name |
|---|---|---|
| Keywords | `#F5C842` | Galactic Gold |
| Functions | `#29D7E8` | Nebula Cyan |
| Strings | `#4DC98A` | Aurora Green |
| Types & Tags | `#7EC8E3` | Star Field Blue |
| Numbers / Literals | `#E8922A` | Amber Core |
| Constants & Booleans | `#EDF4FF` | White Star |
| Variables | `#D6E8F5` | Moonlight |
| Comments | `#4D6D88` | Dark Matter |

### Supplementary Colors

| Use | Hex | Name |
|---|---|---|
| Attributes | `#7B8FD4` | Twilight Violet |
| Constructors | `#0ABFCC` | Deep Teal |
| Operators | `#8AAFC8` | Starlight |
| Errors | `#E85555` | Red Giant |
| Warnings | `#E8922A` | Amber Core |
| Cursor | `#29D7E8` | Nebula Cyan |
| Rose / punctuation alt | `#C97BA8` | Galactic Rose |

---

## Typography Pairing

The "Stargazer" identity is reinforced by pairing the palette with modern monospace fonts that support programming ligatures:

- **Primary recommendation:** JetBrains Mono — clean geometry, optimized for code readability at small sizes; the letterforms hold up against the deep dark background without blurring.
- **Alternative:** Fira Code — excellent ligature set (arrows, comparisons, lambda); the slightly warmer stroke weight complements the gold keyword strategy.

Ligatures like `=>`, `!==`, and `>=` rendered as single glyphs contribute to the polished, observatory-precise aesthetic the scheme targets.

---

## How It Feels in Practice

Imagine opening a TypeScript file at 1 AM, the room dark:

- The background is `#090E1A` — not pure black, but a deep, pressurized navy that feels like the sky an hour after sunset.
- Your eye finds `#F5C842` immediately — `function`, `const`, `import`, the golden structural pillars of the file.
- Functions bloom in `#29D7E8`, the brightest element in the editor, tracing every callable path like the lit arm of a galaxy.
- Strings sit in `#4DC98A` — cool green, grounded, the content within the code rather than the code itself.
- Types read in `#7EC8E3`, a quieter sky-blue that defines shapes without competing with active logic.
- Numbers and literals glow in amber `#E8922A`, warm and concrete, like the car's headlights in a dark field.
- Variable names are `#D6E8F5` — clear, near-white, never demanding attention but always legible.
- Comments are `#4D6D88` — they exist in the dark matter between tokens, present only when you look.
- Your cursor blazes in `#29D7E8`. In 10,000 lines of code, you always know where you are.

That's Stargazer.
