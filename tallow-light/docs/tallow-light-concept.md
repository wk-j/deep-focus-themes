# Tallow Light — Color Scheme Concept

## Origin

The image is a plains farmstead caught at the exact moment between dusk and full dark. A silhouetted house sits against a horizon burning with deep ember-orange, storm clouds massed overhead with a pale moon cutting through them. A windmill tower stands to the left — skeletal against the sky. The windows of the house are the image's emotional center: four panes of amber-gold light, warm and contained, the only evidence of interior life in a vast, cooling landscape. The foreground grass is dry straw ochre, the mountains in the distance are snow-capped blue-slate, and the sky grades from moonlit charcoal through stormy grey-blue to the burning orange-sienna band at the horizon.

---

## Vision

Tallow Light is a coding color scheme drawn from the hour when a farmstead's candles and lamps become the brightest things in the landscape. The central tension is between the thermal and the geological — the burning amber of the windows and horizon set against the cold slate of the mountains, the grey-blue of the storm sky, and the near-black of the earth.

It resolves this tension through three design decisions:

- **The window as hero** — Functions use Tallow (`#E8B050`), the precise color of rendered animal fat burning in a glass — warmer than gold, less harsh than orange. In the image, this is the color that your eye finds first and returns to. In the editor, it serves the same purpose: wherever you are in the file, function calls are the brightest warm point.
- **Horizon ember for keywords** — Keywords use `#D45A20`, the burnt-sienna of the sunset band just below the cloud base. This is structural fire — lower intensity than the window glow, but persistent and directional. Keywords mark where the code is going.
- **Mountain slate for types** — Types and tags use `#7A8EA8`, extracted from the snow-capped mountain silhouettes in the mid-distance. Cool, load-bearing, geologically patient.

The result is a workspace that feels like coding by lamplight with a storm outside — contained warmth, vast darkness, the sense that the work is the only warm thing for miles.

---

## Design Principles

### 1. The Thermal Gradient: Tallow to Ember to Straw

Three warm accents descend in temperature from the foreground to the horizon:
- **Tallow `#E8B050`** → functions. The lit windows — the hottest, most contained light source.
- **Ember `#D45A20`** → keywords. The horizon burn — directional, structural, lower in the sky.
- **Straw `#A07838`** → strings and numbers. The dry prairie grass — organic, desiccated, holding the day's warmth without radiating it.

Each color belongs to a different distance in the image: window (close), horizon (far), grass (ground level). In the editor, they create depth by temperature rather than by hue rotation.

### 2. The Cool Distance: Slate, Mauve, Moonlight

| Role | Color | Hex | Why |
|---|---|---|---|
| Types | Slate | `#7A8EA8` | Snow-capped mountain color — structural, distant, cold |
| Attributes | Mauve | `#8A7888` | The dusky purple of the far right horizon — decorative and recessive |
| Constants | Moonlight | `#9AAEC0` | The pale blue-white where the moon breaks through cloud — fixed, overhead, bright but cold |
| Comments | Deep Ochre | `#4A4438` | Dark soil between grass stalks — present but below the visual plane |
| Errors | Coal Red | `#C03828` | Deeper than the ember horizon — a color that exists in the fire, not the sky |

### 3. Background as Stage, Not Void

The backgrounds carry a warm charcoal undertone that comes from the dark earth and dry grass of the foreground, not from blue-black space. Specifics:

- **Editor surface** (`#0E0D0B`) — the exact darkness of the house silhouette against the horizon: not pure black, but earth-dark, holding a faint brown warmth.
- **Panel/sidebar** (`#090807`) — deeper shadow, the underside of the storm where no light reaches.
- **Highlight** (`#1A1710`) — the faint illumination on the grass nearest the house, lit by spillover from the windows.
- **Errors** use Coal Red (`#C03828`) — a red that belongs to the fire side of the palette, darker and more contained than the horizon ember, readable as danger without the brightness of alarm.

### 4. The Cursor as Anchor

The caret uses Tallow (`#E8B050`). In the image, the amber windows are the single point in the landscape that tells you where the life is. No matter how dark the surrounding terrain, you can find the house. The tallow cursor serves exactly this function — no matter how dense the code, one amber point marks your exact position. It cannot be confused with a string (straw is darker and more muted) or a number (same color family, but strings are identifiable by context).

---

## Color Palette Summary

### Backgrounds & UI

| Component | Hex | Role |
|---|---|---|
| Editor background | `#0E0D0B` | Charcoal Earth |
| Panel / sidebar | `#090807` | Deep Shadow |
| Highlight / selection | `#1A1710` | Window Spillover |
| Border / ruler | `#252018` | Dry Soil |

### Syntax Tokens

| Token | Hex | Name |
|---|---|---|
| Keywords | `#D45A20` | Ember |
| Functions | `#E8B050` | Tallow |
| Strings | `#A07838` | Straw |
| Types | `#7A8EA8` | Slate |
| Numbers | `#A07838` | Straw |
| Constants | `#9AAEC0` | Moonlight |
| Variables | `#C8BCA8` | Prairie Linen |
| Comments | `#4A4438` | Deep Ochre |

### Supplementary Colors

| Use | Hex | Name |
|---|---|---|
| Attributes | `#8A7888` | Mauve |
| Errors | `#C03828` | Coal Red |
| Cursor / caret | `#E8B050` | Tallow |
| Warnings | `#D45A20` | Ember |
| Info / hints | `#7A8EA8` | Slate |
| Operators | `#7A7060` | Dimmed Linen |
| String escapes / regex | `#9AAEC0` | Moonlight |
| Prairie green | `#6A7848` | Prairie |

---

## Typography Pairing

The "Tallow Light" palette pairs with:

- **Primary:** JetBrains Mono — its dense geometric forms suit a palette built on contained warmth and geological patience. The amber functions glow against it the way lamplight holds steady in a drafty room.
- **Alternative:** Fira Code — its slightly more fluid construction suits the organic elements of the palette: the straw strings, the prairie variables, the mauve attributes.

Ligatures like `=>`, `!==`, and `>=` reinforce the economy of the palette — they compress operator noise into single glyphs, keeping the tallow functions and ember keywords as the dominant thermal events on each line.

---

## How It Feels in Practice

Imagine opening a TypeScript file at 11pm with the heating running and rain on the window: the background (`#0E0D0B`) settles in like the inside of a room where the lights have been on long enough that the darkness outside is complete, and your eye finds the first function declaration immediately — tallow amber `#E8B050`, warm and unwavering, the only thing glowing in that direction. Reading down through the function, ember keywords `#D45A20` mark the branch points and returns — `if`, `switch`, `return` — like the line of the horizon: lower than the main light, but directional, telling you where the land is going. Type annotations appear in slate `#7A8EA8`, the color of distant mountains, cool and structural, telling you what shape the data takes. Strings read in straw `#A07838`, dry and organic, the color of things left out in the weather — not urgent, just present. Constants float in moonlight `#9AAEC0`, pale and fixed, already resolved before the function ran. Comments are barely there, deep ochre `#4A4438` receding into the soil between the grass, readable only when you look directly at them. And through all of it, one amber point — the tallow cursor at `#E8B050` — holds position in the dark, the only thing you need to find to know where you are. That's Tallow Light.
