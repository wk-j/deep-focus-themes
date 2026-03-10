# Tidal Ember — Color Scheme Concept

## Origin

The image is a dark-furred cat sitting on a wide beach at golden hour. The sun hangs low over the sea, its light diffused through haze and thin cloud into a wash of amber-gold (`#D89840`) that spills across the wet sand. The cat is a near-silhouette — deep chocolate-brown fur against luminous sand — and a pale blue leash (`#8AA0C0`) runs from its harness toward the camera, the only cool-colored object in the entire frame. The sand is a gradient: dry warm beige closer to the viewer, wet reflective grey-brown near the waterline, punctuated by shallow pools that catch the sun like scattered amber coins. The sky is not blue but a warm grey-gold ceiling of haze, with darker cloud masses floating above the horizon.

---

## Vision

Tidal Ember is a coding color scheme drawn from the specific warmth of a Thai beach at 5:30 PM — the hour when the sun is low enough that everything becomes a gradient of amber, and the only contrast left is between warm light and dark silhouette. The central tension is between the pervasive golden warmth of the scene and the single cool note of the blue leash cutting through it.

It resolves this tension through three design decisions:

- **A sand-dark base** — The background (`#1A1410`) is not neutral grey or blue-black but the specific brown-dark of wet sand in shadow. It carries warmth even in its darkness, the way a beach at dusk still holds the day's heat in the ground. Code sits on this surface like footprints pressed into warm sand — embedded, not floating.
- **Warm accents from the light** — Amber (`#D89840`), gold (`#C4A050`), ochre (`#C87830`), driftwood (`#B8A888`), cream (`#E8D8C0`) are all taken from the gradient of sunset light on sand and water. They carry functions, strings, numbers, constants, and keywords: the living content of the program, rendered in the colors of heat and late light.
- **A single cool accent from the leash** — Periwinkle (`#8AA0C0`) is the blue of the cat's leash, the one cool object in a warm world. It carries types and tags: the structural definitions, the blueprints, the things that describe shape without being the shape itself. One cool color among many warm ones makes the structural layer instantly distinguishable.

The result is a workspace that feels like late afternoon on sand — warm, grounded, unhurried — where the eye separates structure (cool) from content (warm) with minimal effort because the contrast is natural, not forced.

---

## Design Principles

### 1. Golden-Hour Gradient — One Cool Thread in Warm Cloth

The palette is deliberately imbalanced: seven warm colors against one cool one. This ratio mirrors the photograph, where everything — sky, sand, water, cat, even the shadows — is warm, and only the leash is blue. Functions (`#D89840`) are amber because they are the brightest action in the code, the way the brightest point in the image is where sunlight hits wet sand directly. Strings (`#C4A050`) are gold — slightly more muted, like the diffused glow on dry sand further from the waterline. Numbers (`#C87830`) are burnt ochre — the concentrated warmth of the sun itself refracted through haze, deeper and more orange than the ambient gold. Types (`#8AA0C0`) are periwinkle — and this single cool accent does the structural work that three or four cool colors do in other themes, because isolation makes it more visible, not less.

### 2. Silhouette Logic — Dark Forms, Bright Fields

The cat in the image is nearly a silhouette — its dark fur absorbs the surrounding light, becoming a shape defined by absence. Keywords are cream-white (`#E8D8C0`) with bold weight — they are the bright structural forms, the bones visible against the warm field, the way the cat's outline is legible only because the sand behind it glows. This creates a clear visual hierarchy:

| Role | Color | Hex | Why |
|---|---|---|---|
| Keywords | Cream | `#E8D8C0` | The bright edge of the silhouette — structural, bold, warm-neutral |
| Functions | Tidal Amber | `#D89840` | The hero — direct sunlight on wet sand, the brightest warm action |
| Strings | Sunset Gold | `#C4A050` | Diffused glow on dry sand — data, literal, grounded |
| Types | Periwinkle | `#8AA0C0` | The leash — the one cool thread that defines structure |
| Numbers | Burnt Ochre | `#C87830` | Concentrated sun through haze — specific, deep, warm |
| Constants | Driftwood | `#B8A888` | Weathered wood on the tideline — fixed, present, muted |
| Comments | Steel Grey | `#6A7888` | The ocean at the horizon — visible but recessive, cool-neutral |
| Variables | Shore White | `#D8CCBA` | Dry sand in open light — the default surface, readable, warm |

### 3. Background as Stage, Not Void

The background is `#1A1410` — a brown-tinged dark that reads as material rather than emptiness. It is the color of wet sand after the tide has pulled back: dark, warm, with a faint organic richness that pure black lacks. The warm undertone connects it to the amber functions and gold strings, creating a visual continuity between surface and content — everything belongs to the same beach. Specifics:

- **Editor surface** (`#1A1410`) — Wet sand in the shadow of a cloud. Dark enough for long sessions, warm enough to feel like earth rather than screen.
- **Panel/sidebar** (`#110E0A`) — The tideline at dusk, where wet sand meets dry in the deepest shadow. Recessed, grounding, peripheral.
- **Highlight** (`#2A2218`) — A shallow pool catching a glint of amber. Selection and hover states lift with warmth, not brightness.
- **Errors** use Ember Red (`#C04838`) — the color of coals in a beach fire, visible and urgent but belonging to the same thermal world as the amber and ochre. It signals without screaming.

### 4. The Cursor as Anchor

The caret uses Tidal Amber (`#D89840`). In the photograph, the brightest point is where the low sun reflects off a slick of water left by the retreating tide — a streak of concentrated gold that the eye cannot avoid. The amber cursor is that streak: a warm, sharp line of late-afternoon light against the dark sand of the editor surface. In a palette where almost everything is warm, the cursor wins by being the most saturated warm — the purest expression of the golden hour. Your eye returns to it the way your eye returns to the sun's reflection on water: not because it contrasts in temperature, but because it concentrates the dominant energy into a single point.

---

## Color Palette Summary

### Backgrounds & UI

| Component | Hex | Role |
|---|---|---|
| Editor background | `#1A1410` | Wet sand dark with warm brown undertone |
| Sidebar / panels | `#110E0A` | Tideline deep — recessed peripheral surfaces |
| Gutter text | `#3E3630` | Most recessive foreground |
| Caret / cursor | `#D89840` | Tidal amber — sun reflected on retreating water |

### Syntax Tokens

| Token | Hex | Name |
|---|---|---|
| Keywords | `#E8D8C0` | Cream |
| Functions | `#D89840` | Tidal Amber |
| Strings | `#C4A050` | Sunset Gold |
| Types | `#8AA0C0` | Periwinkle |
| Numbers | `#C87830` | Burnt Ochre |
| Constants | `#B8A888` | Driftwood |
| Variables | `#D8CCBA` | Shore White |
| Comments | `#6A7888` | Steel Grey |

### Supplementary Colors

| Use | Hex | Name |
|---|---|---|
| Attributes | `#B8A888` | Driftwood |
| Errors | `#C04838` | Ember Red |
| Cursor | `#D89840` | Tidal Amber |
| Warnings | `#C87830` | Burnt Ochre |
| Info | `#68A898` | Seafoam |
| Operators | `#8A7E70` | Dimmed Sand |
| String escapes | `#68A898` | Seafoam |
| Member access | `#8A7E70` | Dimmed Sand |

---

## Typography Pairing

The "Tidal Ember" palette pairs with:

- **Primary:** JetBrains Mono — its even stroke weight keeps the many warm tones legible without blurring into each other at small sizes. The mechanical precision grounds the organic warmth of the palette the way a harness grounds a cat on a beach.
- **Alternative:** Fira Code — slightly softer terminals let the amber and gold breathe more naturally, trading precision for the slightly looser quality of late-afternoon light.

Ligatures like `=>`, `!==`, and `>=` reinforce the unhurried rhythm of the theme — they read as single gestures rather than sequences, the way a wave retreating over sand is one continuous motion, not a series of steps.

---

## How It Feels in Practice

Imagine opening a Rust file at dusk with warm light coming through a window behind you. The editor surface is not black — it is the deep warm brown of sand after the water has pulled back, a surface that holds heat. Your eye moves first to the amber functions: they are the brightest warm color, the sun-on-water streak, and they pull you into the code the way the reflection on a tidal flat pulls your eye toward the horizon. Between them, gold strings sit steady — the diffused glow of dry sand, carrying the literal data of the program in warm, grounded tones. Types appear in periwinkle, the single cool note in the warm field, and this isolation makes them immediately legible — you always know where a structural definition is because it is the one blue thing on a warm canvas. Numbers burn deeper in ochre, concentrated and specific, the color of the sun itself seen through haze. Constants rest in driftwood — muted, present, the weathered pale of wood that has been on the beach long enough to bleach. Keywords in cream hold the structure together with quiet warmth, bold but not colored, the bright edge of every silhouette. Comments recede into steel grey, the distant ocean at the horizon line, readable when you look but never competing. And the cursor blinks in tidal amber — the exact color of that one bright streak of sun on water that your eye always finds first.

That's Tidal Ember.
