# Lantern Static — Color Scheme Concept

## Origin

The image is a Tokyo backstreet at night — specifically the moment where a ramen shop and an electronics repair stall share a single alley wall. On the left, a paper lantern burns amber-yellow (`#E8922A`) above a food-ticket machine, casting warm light onto dusty concrete etched with kanji graffiti. On the right, a robot welder crouches over a workbench, its plasma discharge throwing cold blue-white light (`#52C8F0`) across stacked crates and coiled cables. The overhead neon sign bleeds crimson-red (`#E8314A`) into the mist. The alley floor is indistinguishable from the space between the two zones — a deep blue-black that absorbs both light sources without resolving them.

---

## Vision

Lantern Static is a coding color scheme drawn from the tension between analog warmth and machine cold in the same physical space. The central conflict is a paper lantern versus a plasma welder — the oldest and newest forms of light coexisting in an alley no wider than a doorframe.

It resolves this tension through three design decisions:

- **Warm hero, cold structure** — Functions use amber (`#E8922A`), the lantern's exact color. Types and tags use plasma-blue (`#52C8F0`), the robot's discharge. Both are vivid but occupy opposite ends of the color temperature spectrum, so they never compete for the same eye movement.
- **Crimson strings as neon signage** — String literals in crimson-red (`#E8314A`) reference the kanji sign above the alley entrance — the one piece of language in the scene that isn't code but communicates like it. Strings carry meaning the way signs do: declaratively, in one line.
- **Concrete mid-tones** — The dusty violet-grey of the alley walls becomes the comment color (`#8B72BE`) and the dimmed foreground. It's not cold, not warm — it's the residue of both, the color of plaster that has absorbed decades of neon and lantern light.

The result is a workspace that reads like the alley itself: warmth pulling the eye to functions, cold precision marking structure, and everything else settling into the textured dark between.

---

## Design Principles

### 1. The Lantern-Plasma Axis

Every accent color in the palette falls on the warm-to-cold spectrum of the alley's two light sources. Amber (`#E8922A`) and lantern-yellow (`#F5C842`) occupy the warm pole — functions, constants, attributes, numbers. Plasma-blue (`#52C8F0`) and mist-grey (`#8FAABB`) occupy the cold pole — types, tags, constructors. Crimson (`#E8314A`) is the one color that belongs to neither axis: it is the sign, the language, the declaration. This three-pole structure — warm, cold, declarative — means that any token's color communicates its semantic role before the developer reads it.

### 2. Syntax Hierarchy from the Scene's Light

The scene's brightest element is not the neon sign but the lantern — the oldest technology present, still the most human. That hierarchy drives the syntax ranking:

| Role | Color | Hex | Why |
|---|---|---|---|
| Keywords | Smoke White | `#F2EEF8` | Load-bearing structure, like the concrete columns — neutral, present everywhere |
| Functions | Lantern Amber | `#E8922A` | The warmest point; the lantern is the scene's most human light source |
| Strings | Neon Crimson | `#E8314A` | Kanji neon signage — language that declares |
| Types | Plasma Blue | `#52C8F0` | Robot discharge — precise, cold, machine-readable |
| Constants | Sign Yellow | `#F5C842` | Price tags and labels in the stall window |
| Numbers | Rust Glow | `#C46B3A` | Oxidized metal under lamplight |
| Comments | Indigo Haze | `#8B72BE` | Absorbed neon in plaster — present but not read |
| Variables | Dusty White | `#D8D0E8` | The ambient light level — everything that isn't specifically lit |

### 3. Background as Stage, Not Void

The alley in the image is not simply dark — it has texture, depth, and absorbed color. The backgrounds carry this.

- **Editor surface** (`#0E0D15`) — the specific darkness of concrete between two lit storefronts: not black, which would make the scene feel empty, but a deep blue-tinged dark that suggests material without announcing it.
- **Panel/sidebar** (`#090810`) — the interior of the alley further back, where neither the lantern nor the plasma reaches. Recessed without being absent.
- **Highlight** (`#1A1826`) — the brief glow on a wall surface when both light sources catch the same patch of plaster. Used for cursorline and selections, so the lit-surface logic holds.
- **Errors** use Alarm Red (`#E83040`) — the color of a fire warning sticker on a fuse box in the stall, familiar enough to read immediately, specific enough not to be generic.

### 4. The Cursor as Anchor

The caret uses Plasma Blue (`#52C8F0`). In the scene, the robot's plasma discharge is the only light source that moves — it tracks the robot's work, always marking where something is being made or repaired. In the editor, the cursor serves the same function: it marks where the work is happening. Plasma blue is also the coldest color in the palette, which makes it unmissable against the warm amber and neutral white mid-tones surrounding it. The eye finds it without looking for it.

---

## Color Palette Summary

### Backgrounds & UI

| Component | Hex | Role |
|---|---|---|
| Editor background | `#0E0D15` | Alley Dark — textured deep blue-black |
| Sidebar / panels | `#090810` | Deep Corridor — recessed, further from light |
| Selection / highlight | `#1A1826` | Wall Glow — surface briefly lit |
| Border / separator | `#252338` | Plaster Line — barely visible structure |

### Syntax Tokens

| Token | Hex | Name |
|---|---|---|
| Keywords | `#F2EEF8` | Smoke White |
| Functions | `#E8922A` | Lantern Amber |
| Strings | `#E8314A` | Neon Crimson |
| Types | `#52C8F0` | Plasma Blue |
| Numbers | `#C46B3A` | Rust Glow |
| Constants | `#F5C842` | Sign Yellow |
| Variables | `#D8D0E8` | Dusty White |
| Comments | `#8B72BE` | Indigo Haze |

### Supplementary Colors

| Use | Hex | Name |
|---|---|---|
| Cursor | `#52C8F0` | Plasma Blue |
| Attributes | `#F5C842` | Sign Yellow |
| Constructors | `#8FAABB` | Alley Mist |
| Errors | `#E83040` | Alarm Red |
| Warnings | `#C46B3A` | Rust Glow |
| Info | `#52C8F0` | Plasma Blue |
| Operators | `#7A7090` | Dusty Violet |
| String escapes | `#52C8F0` | Plasma Blue |

---

## Typography Pairing

The "Lantern Static" palette pairs with:

- **Primary:** JetBrains Mono — its angular, mechanical letterforms echo the bolted-metal aesthetic of the repair stall, while the amber and plasma accents have enough saturation to carry against its clean geometry without halation.
- **Alternative:** Fira Code — the slightly rounder stroke weight softens the amber accents, pushing the theme slightly warmer and closer to the lantern side of the spectrum.

Ligatures like `=>`, `!==`, and `>=` reinforce the mechanical character of the theme — in a scene full of cables, connectors, and wiring, the joined symbols read as circuits completing rather than operators abstractly applied.

---

## How It Feels in Practice

Imagine opening a deeply nested TypeScript file at 11pm, the kind of file with three layers of abstraction and a comment block that someone wrote when they were too tired to be precise. The background settles immediately — `#0E0D15` has enough blue in it to feel intentional, not accidental, like a room that was designed to be dim rather than just unlit. Keywords appear first: `const`, `function`, `return` in near-white bold, the concrete columns that hold the file's shape. Then the functions light up in amber — `processOrder`, `fetchUser`, `handleError` — each name glowing with the specific warmth of something that is burning rather than shining, sustained combustion rather than electrical discharge. Strings follow in crimson, brief and declarative, like the kanji sign above the alley: "table_name", "api/v2/orders", they state and stop. Types arrive in plasma-blue, cool and exact — `Promise<Order>`, `UserRecord`, `RequestHandler` — the machine-readable half of the file. Numbers and constants carry the warm yellow of price-tag labels on a shop shelf. Comments dissolve into indigo haze, present but receding, like the text on a graffiti'd wall you stop reading after the first word. And through all of it, the plasma-blue cursor moves: the one point in the scene that is both cold and alive, marking where the work is being done.

That's Lantern Static.
