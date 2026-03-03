# Cinder Grid — Color Scheme Concept

## Origin

The image is a programmer's station at night, viewed from above and behind. The left monitor blazes with dense orange-red code — not the orange of a sunset, but the specific color of a tungsten filament at half-brightness, like slag pouring from a crucible. The room itself is a curved mosaic of small tiles, each tile a different shade of steel-blue and charcoal, holding embedded squares of amber light as if pixels were escaping the screens and crystallizing in the wall. The right monitor shows a city from altitude — ten thousand points of white and cyan light suspended in a darkness so complete it reads as vacuum.

---

## Vision

Cinder Grid is a coding color scheme drawn from a tiled control room where the walls are the display. The central tension is between the thermal — ember, amber, gold, the colors of things burning at low heat — and the architectural — steel blue, navy, the colors of tiles, facades, and city grids seen from distance.

It resolves this tension through three design decisions:

- **The ember hierarchy** — Functions burn in `#E8721A`, the dominant color of the left monitor. This is the color your eye goes to first in the reference image, so it is the color your eye goes to first in the editor. Everything else is cooler or dimmer.
- **The tile palette for structure** — Types and tags use `#4D8FCC`, extracted from the electric-blue tile highlights in the mosaic wall. This grounds structural declarations in the room's material texture — they feel load-bearing, not decorative.
- **Darkness with depth** — The background `#0B0F1A` is not pure black. It is the specific darkness between illuminated tiles — dark enough to disappear, blue-tinted enough to read as a material surface rather than an absence.

The result is a workspace that feels like coding inside the control room: surrounded by structure, lit by function, watched over by the city outside.

---

## Design Principles

### 1. The Thermal Spectrum: Ember to Amber to Gold

The three warmest accents — ember (`#E8721A`), amber (`#D4A827`), gold (`#C8901A`) — form a temperature gradient descending in visual weight. Ember is assigned to functions because functions are the hottest computational event: they execute, transform, return. Amber is assigned to keywords because keywords are structural markers — they define flow without doing work, like the floating gold squares in the mosaic ceiling, embedded in the architecture but not part of the computation. Gold governs numbers and constants — values that are fixed, material, the color of something cast rather than burning.

### 2. The Cool Grid: Type, Attribute, Sky

| Role | Color | Hex | Why |
|---|---|---|---|
| Types | Tile Blue | `#4D8FCC` | Matches the electric-blue highlights in the mosaic wall — structural, load-bearing |
| Attributes | Sky Blue | `#7BB5D0` | Lighter, more diffuse — the sky reflected in a tile, not the tile itself |
| Tags | Tile Blue | `#4D8FCC` | HTML/XML tags are architectural like type declarations |
| Strings | Moss | `#5FAD6E` | The only organic color in the palette — strings carry human-written content, not machine structure |
| Comments | Muted Slate | `#4E5A6E` | The shadow between two tiles — present but recessive, never competing |

### 3. Background as Stage, Not Void

The backgrounds are four stops on a single blue-dark gradient, each distinct enough to establish depth without using borders. Specifics:

- **Editor surface** (`#0B0F1A`) — the space between two lit tiles at 3am, dark enough to vanish but holding a blue undertone that says "room" not "space".
- **Panel/sidebar** (`#070B14`) — one stop darker, the shadow side of the same room. Panels recede without needing a separating line.
- **Highlight** (`#161D2E`) — the lift a tile gets when backlit from behind; used for cursorline and selection to indicate presence without glare.
- **Errors** use Coral Red (`#D45C5C`) — a warm red that registers as alarm without the anxiety of a saturated fire-engine red. It belongs to the thermal palette but signals stop rather than go.

### 4. The Cursor as Anchor

The caret uses Ember (`#E8721A`). In the reference image, the left monitor's blazing orange-red is the single hottest point in an otherwise cool, blue-grey room — the constant source of heat that everything else orbits. The editor caret serves the same function: wherever you look in the file, one ember-colored point marks where you are. It cannot be confused with a function name because it moves; it cannot be confused with a keyword because keywords are amber, not orange.

---

## Color Palette Summary

### Backgrounds & UI

| Component | Hex | Role |
|---|---|---|
| Editor background | `#0B0F1A` | Charcoal Navy |
| Panel / sidebar | `#070B14` | Deep Station |
| Highlight / selection | `#161D2E` | Backlit Tile |
| Border / ruler | `#1E2840` | Tile Grout |

### Syntax Tokens

| Token | Hex | Name |
|---|---|---|
| Keywords | `#D4A827` | Amber |
| Functions | `#E8721A` | Ember |
| Strings | `#5FAD6E` | Moss |
| Types | `#4D8FCC` | Tile Blue |
| Numbers | `#C8901A` | Gold |
| Constants | `#C8901A` | Gold |
| Variables | `#D8DDE8` | Near White |
| Comments | `#4E5A6E` | Muted Slate |

### Supplementary Colors

| Use | Hex | Name |
|---|---|---|
| Attributes | `#7BB5D0` | Sky Blue |
| Errors | `#D45C5C` | Coral Red |
| Cursor / caret | `#E8721A` | Ember |
| Warnings | `#D4A827` | Amber |
| Info / hints | `#4D8FCC` | Tile Blue |
| Operators | `#8A95A8` | Dimmed Slate |
| String escapes / regex | `#C8901A` | Gold |
| Constructors | `#4D8FCC` | Tile Blue |

---

## Typography Pairing

The "Cinder Grid" palette pairs with:

- **Primary:** JetBrains Mono — its geometric letterforms feel like the tile grid itself: modular, dense, each character occupying a precise cell. The ember functions glow against it like light sources behind a screen.
- **Alternative:** Fira Code — its slightly more fluid geometry softens the thermal palette without losing the structural feeling.

Ligatures like `=>`, `!==`, and `>=` reinforce the industrial aesthetic — they compact the visual noise of operators into single glyphs, keeping the amber keywords and ember functions as the dominant visual events on the line.

---

## How It Feels in Practice

Imagine opening a Rust file at 2am with a city view outside the window: the background (`#0B0F1A`) settles in like a room you've been in long enough to stop noticing the walls, and your eye finds the first `fn` declaration immediately — ember-orange (`#E8721A`), unmissable, the hottest thing on screen. As you read down the function body, amber `#D4A827` keywords mark the decision points — `if`, `match`, `return` — like structural beams you need to know the location of before you move around the room. Type annotations arrive in tile blue `#4D8FCC`, cooler and load-bearing, telling you what shape the data takes. String literals read in moss `#5FAD6E`, the only softness in the palette, the only organic color — they feel like handwriting in a room full of machinery. Numbers sit in gold `#C8901A`, fixed and material, already resolved. Comments are almost invisible, muted slate `#4E5A6E` retreating into the grout between tiles, there if you look, absent if you don't. And throughout all of it, one ember point — the cursor at `#E8721A` — moves with you, the single burning thread you follow through the grid. That's Cinder Grid.
