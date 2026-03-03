# Brass and Black — Color Scheme Concept

## Vision

Brass and Black is a high-performance coding color scheme built for developers who work in long, unbroken sessions. The philosophy is simple: absolute darkness meets orchestral brass.

It achieves this through three complementary ideas:

- **Stage Black** — The background (`#181818`) is near-total darkness with a warm charcoal undertone, like a concert stage before the lights hit. The panel shade (`#111111`) deepens further, creating panel separation without any border lines.
- **Brass Spectrum** — Accent colors move deliberately through the visible spectrum: brass gold (`#C8B800`) for functions, sage green (`#8CB87A`) for strings, steel blue (`#4E9ED4`) for types, teal (`#3AADA8`) for literals, lavender (`#9A88CC`) for constructors, amber (`#D4841A`) for tags. Each hue family is used exactly once.
- **Parchment Keywords** — Structural keywords (`if`, `for`, `return`, `class`) render in near-white `#F0EAD8` with bold weight. They mark the skeleton of the code without competing with the colored flesh.

The result is a workspace that feels like a score unfolding — each voice distinct, each instrument recognizable at a glance.

---

## Design Principles

### 1. One Hue Per Role

The spectrum is deliberately partitioned: no two major syntax roles share a hue family. A developer can learn within minutes which color means what, and thereafter reads structure without consciously decoding it. Brass is functions. Blue is types. Green is strings. Teal is literals. The map is intuitive because it mirrors spectral distance — similar roles are adjacent, dissimilar ones are far apart.

### 2. Hierarchy Through Contrast

Keywords anchor the visual hierarchy as the most structurally important tokens. This creates a clear visual hierarchy:

| Role | Color | Hex | Why |
|---|---|---|---|
| Keywords | Parchment White | `#F0EAD8` | Structural skeleton — must be immediately legible |
| Functions | Brass | `#C8B800` | Hero color — every call site lights up |
| Types | Steel Blue | `#4E9ED4` | Cool contrast against the warm brass |
| Strings | Sage | `#8CB87A` | Earthy, recessive — data that carries content |
| Constants | Gold | `#E8D000` | Brighter than brass — literals that never change |
| Literals | Teal | `#3AADA8` | Distinct from strings — numeric and boolean |
| Constructors | Lavender | `#9A88CC` | Softer hue — invocation without declaration |
| Variables | Warm Ivory | `#E8E0CC` | Near-white — the workhorses of the codebase |
| Comments | Scorched Oak | `#665C48` | Low-contrast — present but not competing |

### 3. Minimal Chrome, Maximum Depth

- **No harsh borders.** Panel separation comes from background color shifts (`#181818` for editor, `#111111` for sidebar/panels).
- **Active tab indicator.** A single brass `#C8B800` line marks the active file — matching the image's vivid tab highlight exactly.
- **Restrained error states.** Errors use Signal Red (`#E8363A`) — clearly an error, but the warm, slightly desaturated tone avoids the alarm-bell anxiety of pure `#FF0000`.

### 4. The Cursor as Anchor

The caret and selection both use Gold (`#E8D000`). In a scheme this dark, the cursor must be unmissable. The gold tone is one step brighter and more saturated than the brass hero, ensuring it always reads as the current position regardless of surrounding syntax color.

---

## Color Palette Summary

### Backgrounds & UI

| Component | Hex | Role |
|---|---|---|
| Editor background | `#181818` | Stage Black — primary canvas |
| Sidebar / panels | `#111111` | Pit Black — recessed chrome |
| Highlight / hover | `#242424` | Footlight — subtle surface lift |
| Borders (if used) | `#2E2E2E` | Truss Gray — structural separator |

### Syntax Tokens

| Token | Hex | Name |
|---|---|---|
| Keywords | `#F0EAD8` | Parchment White |
| Functions | `#C8B800` | Brass |
| Strings | `#8CB87A` | Sage |
| Types | `#4E9ED4` | Steel Blue |
| Literals / Numbers | `#3AADA8` | Teal |
| Constants | `#E8D000` | Gold |
| Variables | `#E8E0CC` | Warm Ivory |
| Comments | `#665C48` | Scorched Oak |

### Supplementary Colors

| Use | Hex | Name |
|---|---|---|
| Attributes | `#7ABCE8` | Sky |
| Tags (HTML/JSX) | `#D4841A` | Amber |
| Constructors | `#9A88CC` | Lavender |
| Errors | `#E8363A` | Signal Red |
| Cursor / selection | `#E8D000` | Gold |
| Operators | `#A89C80` | Dimmed Ivory |
| Muted text | `#665C48` | Scorched Oak |
| Gutter numbers | `#3D3828` | Deep Umber |

---

## Typography Pairing

The "Brass and Black" identity is reinforced by pairing the palette with modern monospace fonts that support programming ligatures:

- **Primary recommendation:** JetBrains Mono — clean geometry, optimized for code readability at small sizes. The slightly warm glyph shapes complement the parchment foreground.
- **Alternative:** Fira Code — excellent ligature set (arrows, comparisons, lambda). The open apertures pair well with the open, airy brass tones.

Ligatures like `=>`, `!==`, and `>=` rendered as single glyphs contribute to the scored, composed feeling the scheme targets.

---

## How It Feels in Practice

Imagine opening a TypeScript file at 11pm with the room lights off:

- The background is so dark it recedes — the code floats. There is no glare, no gray haze, just pure stage black.
- Your eye lands first on the parchment-white `if` and `return` keywords that scaffold the logic. They read like rehearsal marks on a score.
- Function names glow in brass — warm, authoritative, immediately recognizable as the things that *do* something.
- Type annotations sit in cool steel blue, a visual counterweight to the warm brass — you always know where the contract is declared.
- String literals are sage green, the quietest of the accent voices. They carry content without shouting.
- Numbers and booleans are teal — geometric, precise, clearly distinct from strings.
- Operators (`+`, `=`, `=>`) are dimmed ivory, present and legible but never grabbing attention.
- Comments are scorched oak — the color of pencil marks in a margin. They're there if you need them.
- Your cursor blazes in gold. You always know where you are.

That's Brass and Black.
