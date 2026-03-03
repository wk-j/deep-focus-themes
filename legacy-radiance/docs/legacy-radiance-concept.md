# Legacy Radiance — Color Scheme Concept

## Origin

The image is a stock-library 3D render of COBOL source code floating in perspective planes against absolute black — the kind of visualization made to illustrate "legacy systems" in a business magazine. But look past the watermarks. Three distinct emission colors are happening simultaneously: phosphor green on the near-left panel (`#00C840`), the specific green of a P1 phosphor coating on a 1970s Hazeltine or ADM-3A terminal; deep cobalt blue on the mid-ground planes (`#2A7EE8`), the color of cold cathode backlighting; and ionized cyan at the far right and at the cursor blocks (`#00D4C8`), the highest-energy visible emission before blue-violet, the color of a terminal on its last percentage of contrast adjustment before the image bleaches out. The background is not dark — it is the complete absence of ambient light between self-luminous planes.

---

## Vision

Legacy Radiance is a coding color scheme drawn from the specific physics of CRT phosphor emission. The central tension is the ancient and the electric: code written before most developers were born, still radiating cold light into a lightless room.

It resolves this tension through three design decisions:

- **Void black ground** — The background (`#080808`) is not a dark gray or a near-black with a tint. It is the color of the space between the planes in the image — not empty, but lightless. The sidebar deepens to `#040404`, a distinction that reads as depth rather than color difference.
- **Three-frequency emission** — The accent palette is built on exactly three phosphor frequencies: green (`#00C840`) for functions, the things that execute; cobalt (`#2A7EE8`) for keywords, the structural commands that have not changed in forty years; and ionized cyan (`#00D4C8`) for types, the boundary layer where data is defined. Each frequency is chemically distinct — they do not blend at medium saturation.
- **Decay hierarchy** — Foreground text (`#C8E0D0`) is the color of phosphor screen glow seen through a slightly dusty CRT glass — not white, not green, but the green-shifted white of a screen that has been on for hours. Comments (`#304838`) are dead phosphor: the color of a screen area that has been written to so many times the coating has worn thin.

The result is a workspace that feels like sitting at a terminal in a data center at 3am — the only light source in the room is the code itself.

---

## Design Principles

### 1. Phosphor Frequency as Syntax Role

CRT monitors used different phosphor compounds to produce different colors — P1 for green, P4 for white, P31 for a blue-shifted green. Each compound emits at a specific wavelength under electron bombardment. Legacy Radiance assigns syntax roles by frequency: the lowest-energy visible phosphor (green, `#00C840`) for the most common token type (functions), the mid-frequency (cobalt blue, `#2A7EE8`) for structural anchors (keywords), and the highest-frequency sustained emission (cyan, `#00D4C8`) for type information. This is not arbitrary — green functions are called the most, blue keywords are read the most, cyan types are consulted when something is wrong. The frequency matches the usage pattern.

### 2. The Command Plane vs. The Data Plane

The image shows two distinct visual layers: the green near-plane (operational, imperative — what the program does) and the blue/cyan far-planes (structural, declarative — what the program is). This maps directly to the keyword/function split. Cobalt keywords (`#2A7EE8`) are the command plane — `IF`, `PERFORM`, `EXEC`, `END-IF` in the image, the verbs that have not changed since COBOL was standardized. Phosphor green functions (`#00C840`) are the data plane — the named procedures, the things being called. This creates a clear visual hierarchy:

| Role | Color | Hex | Why |
|---|---|---|---|
| Keywords | Cobalt | `#2A7EE8` | The blue mid-plane in the image — structural, heavy, authoritative |
| Functions | Phosphor Green | `#00C840` | P1 phosphor emission — the most common terminal green, the worker color |
| Types | Ionized Cyan | `#00D4C8` | Peak-charge emission — brightest sustained color, marks the type boundary |
| Strings | Plasma | `#00F0A0` | A green shifted toward cyan — data in transit, between the two planes |
| Constants | Phosphor White | `#D8F0E0` | Screen glow at maximum brightness — things that do not change |
| Numbers | Pale Green | `#80C898` | Half-charge phosphor — numeric, precise, quieter than full green |
| Variables | Screen Glow | `#C8E0D0` | The ambient light of the screen seen through dusty glass |
| Comments | Dead Phosphor | `#304838` | Worn coating — present but no longer emitting at full intensity |

### 3. Background as Stage, Not Void

The darkness in this theme is not decorative. It is the specific darkness of a room where the only light is the code.

- **Editor surface** (`#080808`) — eight counts above pure black, the minimum needed to avoid pure-black rendering artifacts on some displays. This is the space between the floating code planes in the image.
- **Panel/sidebar** (`#040404`) — two stops darker than the editor. The difference is not visible as color; it registers as depth. Panels feel further away because they are.
- **Highlight** (`#0E1A10`) — a green-tinted dark, as if the selection area is lit by nearby phosphor emission rather than a flat overlay color.
- **Errors** use Overload Red (`#E83840`) — not the saturated alarm red of modern UI, but the specific red-orange of a CRT that has been driven past its rated voltage: still red, but with the warmth of something about to fail rather than something that has already failed.

### 4. The Cursor as Anchor

The caret uses Ionized Cyan (`#00D4C8`). In the image, the cursor blocks glow cyan — the specific blue-green of a terminal cursor at maximum intensity, the block that shows you where the next character will go. On a physical terminal, the cursor is always the brightest point on the screen. In Legacy Radiance it serves the same function: `#00D4C8` is the highest-energy color in the palette that is not used for a major syntax role, which means the cursor is never confused with code and is always findable in any context.

---

## Color Palette Summary

### Backgrounds & UI

| Component | Hex | Role |
|---|---|---|
| Editor background | `#080808` | Void Black — the space between self-luminous planes |
| Sidebar / panels | `#040404` | Deep Void — further from the light source |
| Highlight / hover | `#0E1A10` | Phosphor Ambient — selection tinted by nearby emission |
| Border (if used) | `#162018` | Dim Screen Edge — the frame of the glass |

### Syntax Tokens

| Token | Hex | Name |
|---|---|---|
| Keywords | `#2A7EE8` | Cobalt |
| Functions | `#00C840` | Phosphor Green |
| Strings | `#00F0A0` | Plasma |
| Types | `#00D4C8` | Ionized Cyan |
| Numbers | `#80C898` | Pale Green |
| Constants | `#D8F0E0` | Phosphor White |
| Variables | `#C8E0D0` | Screen Glow |
| Comments | `#304838` | Dead Phosphor |

### Supplementary Colors

| Use | Hex | Name |
|---|---|---|
| Attributes | `#7AE830` | Chartreuse |
| Tags | `#40A8F0` | Arc Blue |
| Constructors | `#40A8F0` | Arc Blue |
| Errors | `#E83840` | Overload Red |
| Cursor | `#00D4C8` | Ionized Cyan |
| Warnings | `#C06020` | Ember |
| Operators | `#6A9078` | Dimmed Glow |
| String escapes | `#00D4C8` | Ionized Cyan |

---

## Typography Pairing

The "Legacy Radiance" palette pairs with:

- **Primary:** JetBrains Mono — its slightly extended letterforms at small sizes recall the chunky bitmap characters of a 80-column terminal. The phosphor green reads cleanest through its generous apertures.
- **Alternative:** Fira Code — the ligature forms for `=>` and `->` echo the way COBOL variable paths were written with hyphens, a visual echo of the source material without being literal.

Ligatures in this theme read as shortcuts carved into something that was not designed for shortcuts — they feel like the kind of optimizations a programmer makes after years on the same system, worn smooth with use.

---

## How It Feels in Practice

Imagine opening a SQL migration file at 2am in a data center with the overhead fluorescents switched off. The background is void — not the comfortable dark of a modern dark mode, but the dark of a room where the display is the only photon source for six meters in every direction. The cobalt blue keywords (`#2A7EE8`) appear first, heavy and structural: `SELECT`, `FROM`, `WHERE` — the same commands that have been typed into terminals since before you were born, rendered in the same cold blue the mid-ground planes float in. Functions surface in phosphor green (`#00C840`), the P1 phosphor emission that any programmer who used a VT100 knows without being able to name — it is the green, the original green, the green that means the machine is working. Type annotations glow in ionized cyan (`#00D4C8`), a frequency higher than the function green, marking the boundaries of what the data is allowed to be. Strings pool in plasma green (`#00F0A0`), slightly shifted toward cyan, data in transit between the operational and the structural planes. Numbers read in pale green (`#80C898`), half-charge, precise. Variables are screen glow (`#C8E0D0`) — the near-white of a screen that has been on for four hours, not clean white but white that has been tinted by everything around it. Comments are dead phosphor (`#304838`), still present, still legible if you look, but no longer emitting at the level of the live code. Your cursor burns in ionized cyan. You know exactly where you are because it is the brightest point in the room.

That's Legacy Radiance.
