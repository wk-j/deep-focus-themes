# Thermal Shelf — Color Scheme Concept

## Origin

The image is an astronaut standing on a dark platform above an immense cloudscape. The clouds are sunlit from behind — their surfaces hold warm cream-gold (`#D4A856`), their shadows sink into teal-grey. The sky overhead transitions from a pale green-teal horizon to deep stratospheric blue (`#0F1B24`) at the zenith. The astronaut's suit catches cool blue-grey light on its panels and warm edge-light on its contours. The entire scene sits at the thermal boundary: the altitude where rising warm air meets cold upper atmosphere and condensation builds towering cumulus walls.

---

## Vision

Thermal Shelf is a coding color scheme drawn from the moment before the atmosphere ends. The central tension is thermal — warm golden light pushing upward through clouds against the cold blue-black of near-space pressing down.

It resolves this tension through three design decisions:

- **A stratospheric base** — The background (`#0F1B24`) is not neutral black but the specific dark blue-green of the sky at 40,000 feet. It carries the cold of altitude without the emptiness of space. Code sits in this atmosphere like the astronaut sits on the ledge — grounded but elevated.
- **Warm accents from the cloud layer** — Gold (`#D4A856`), amber (`#E8943A`), ivory (`#E8DCC8`) come directly from the sunlit cloud surfaces. These are the colors of thermal energy made visible — the warm air that built these clouds. In the editor, they carry strings, numbers, and constants: the literal data, the concrete values.
- **Cool accents from the upper air** — Teal (`#4EC9B0`), cirrus blue (`#A8D8EA`), cyan (`#56C8D8`) come from the sky and the diffused light in the cloud shadows. These are the structural colors — functions, types, the architecture of code. They belong to the cold side of the thermal divide.

The result is a workspace where the eye naturally separates data (warm) from structure (cool), with the dark stratospheric background providing depth behind both layers.

---

## Design Principles

### 1. Thermal Divide — Warm Data, Cool Structure

Every accent color in the palette comes from one side of the temperature boundary visible in the image. Functions (`#4EC9B0`) are teal because they are structural — they define the architecture of execution, like the cold upper atmosphere defines the ceiling of the cloud layer. Strings (`#D4A856`) are gold because they are data — literal values carrying meaning upward into the program, like warm air carrying moisture into the sky. This is not a metaphor imposed on the palette; it is the actual physics of the scene, mapped onto the actual semantics of code. Types are cirrus blue (`#A8D8EA`) — lighter, more diffuse, like the thin high clouds that form at the very top of the thermal column. Numbers are amber (`#E8943A`) — the hottest point of sunlight breaking through a cloud gap.

### 2. Quiet Structure, Bright Payload

Keywords are cream-white (`#F0E6D0`) with bold weight — they mark the structural skeleton of code (if/else, return, function) without drawing the eye away from the semantic content. They are the platform the astronaut stands on: necessary, solid, but not the subject of the photograph. This creates a clear visual hierarchy:

| Role | Color | Hex | Why |
|---|---|---|---|
| Keywords | Cream White | `#F0E6D0` | The solid platform — structural, bold, neutral-warm |
| Functions | Thermal Teal | `#4EC9B0` | The hero — the dominant atmospheric color at altitude |
| Strings | Cloud Gold | `#D4A856` | Sunlit cloud surfaces — warm, literal, data-carrying |
| Types | Cirrus Blue | `#A8D8EA` | Thin high-altitude ice — structural but lighter than functions |
| Numbers | Warm Amber | `#E8943A` | The hottest light — concentrated, specific, bright |
| Constants | Ivory | `#E8DCC8` | Cloud-white — fixed values, present but not dynamic |
| Comments | Altitude Slate | `#6B8FA0` | The haze between cloud layers — visible but recessive |
| Variables | Frost White | `#D8E4E8` | The astronaut's visor — neutral, clear, reflective |

### 3. Background as Stage, Not Void

The background is `#0F1B24` — a blue-tinged dark that reads as depth rather than absence. It is the color of the sky just above the cloud layer: not space-black, not monitor-off, but atmospheric dark. The teal undertone connects it to the function color, creating a visual continuity between structure and environment. Specifics:

- **Editor surface** (`#0F1B24`) — The stratosphere above the clouds. Dark enough for long sessions, blue enough to feel like altitude rather than emptiness.
- **Panel/sidebar** (`#091318`) — Deeper than the editor, like looking down through the gap between clouds where the ground is invisible. Recessed, peripheral.
- **Highlight** (`#1A2D3A`) — The subtle brightening when a cloud catches light from the side. Selection and hover states lift gently without breaking the atmospheric unity.
- **Errors** use Coral Red (`#E05252`) — warm enough to belong to the thermal palette, distinct enough from the amber/gold family to signal a problem without triggering alarm. It is the color of sunset light on the underside of a storm cloud: a warning, not a siren.

### 4. The Cursor as Anchor

The caret uses Warm Amber (`#E8943A`). In the image, the brightest point is where direct sunlight breaks through a gap in the cloud wall and catches the edge of a cumulus tower — a single line of concentrated gold against the surrounding blue-grey. The amber cursor reproduces this effect exactly: a warm, sharp point of light against the cool stratospheric background. Your eye returns to it the way the eye returns to the brightest point in a landscape. It is the visual anchor that says "you are here" in a field of cool blue syntax.

---

## Color Palette Summary

### Backgrounds & UI

| Component | Hex | Role |
|---|---|---|
| Editor background | `#0F1B24` | Stratospheric dark with blue undertone |
| Sidebar / panels | `#091318` | Deep altitude — recessed peripheral surfaces |
| Gutter text | `#3B5060` | Most recessive foreground |
| Caret / cursor | `#E8943A` | Warm amber — sunlight breaking through cloud |

### Syntax Tokens

| Token | Hex | Name |
|---|---|---|
| Keywords | `#F0E6D0` | Cream White |
| Functions | `#4EC9B0` | Thermal Teal |
| Strings | `#D4A856` | Cloud Gold |
| Types | `#A8D8EA` | Cirrus Blue |
| Numbers | `#E8943A` | Warm Amber |
| Constants | `#E8DCC8` | Ivory |
| Variables | `#D8E4E8` | Frost White |
| Comments | `#6B8FA0` | Altitude Slate |

### Supplementary Colors

| Use | Hex | Name |
|---|---|---|
| Attributes | `#E8DCC8` | Ivory |
| Errors | `#E05252` | Coral Red |
| Cursor | `#E8943A` | Warm Amber |
| Warnings | `#E8943A` | Warm Amber |
| Info | `#56C8D8` | Altitude Cyan |
| Operators | `#8A9EAA` | Dimmed Frost |
| String escapes | `#56C8D8` | Altitude Cyan |
| Member access | `#8A9EAA` | Dimmed Frost |

---

## Typography Pairing

The "Thermal Shelf" palette pairs with:

- **Primary:** JetBrains Mono — its mechanical precision suits the astronaut's engineered environment. The uniform stroke width keeps the warm/cool accent colors legible at small sizes against the dark stratospheric base.
- **Alternative:** Fira Code — slightly rounder terminals soften the palette's industrial edge, letting the gold and amber accents breathe more naturally.

Ligatures like `=>`, `!==`, and `>=` reinforce the theme's sense of engineered systems — they read as the control-panel typography on the astronaut's backpack, functional glyphs in a high-altitude instrument cluster.

---

## How It Feels in Practice

Imagine opening a TypeScript file at 2 AM with the room dark and a low-frequency hum in your headphones. The editor surface is not black — it is the deep blue-green of a sky that still has atmosphere in it, still has depth. Your eye moves first to the teal functions: they are the loudest color, the structural skeleton, and they pull you into the code the way the horizon line pulls your eye in the photograph. Between them, gold strings catch the light — warm, grounded, carrying the actual data of the program. Types float in cirrus blue, lighter and more diffuse, marking the boundaries of what things are without competing with what things do. Numbers burn in amber: specific, hot, concentrated, the brightest semantic content on the screen. Keywords in cream-white hold the lines together with quiet authority — bold but not colorful, structural but not decorative. Comments recede into altitude slate, present but atmospheric, readable only when you look for them. And at the center of it all, the amber cursor blinks: a single warm point against the cool field, the exact color of sunlight breaking through a cloud wall. Your eye always knows where it is.

That's Thermal Shelf.
