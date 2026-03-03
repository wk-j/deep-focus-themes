# Suspended Marl — Color Scheme Concept

## Origin

The source is a single impossible image: a cloaked figure standing at the edge of Irish-style sea cliffs in dense coastal fog, watching three inverted stone tetrahedra float motionless in the mist above cold blue-grey water. The floating bodies are geological — marl and slate, the actual material of these cliffsides — and their suspension is the precise uncanniness the theme is built around. The light is flat, diffused, overcast. There is no sun, only the pale luminosity of sky filtered through kilometres of Atlantic fog.

---

## Vision

Suspended Marl is a coding color scheme drawn from the visual grammar of that coastal stillness — the compression of distance into grey-blue haze, the way cliff faces reveal their rust and ochre only up close, the single dark figure as scale and witness. The central tension is geological weight against atmospheric lightness: stone should fall, but doesn't. The palette holds this tension through deliberate thermal conflict — a cool, recessive background atmosphere against warm accent points that feel as specific and local as a patch of dried cliff grass.

It resolves this tension through three design decisions:

- **Cold foundation, warm anchor** — The background (`#181B1F`) is the darkness of cliff shadow, not the darkness of empty space. It carries a slight blue-grey coolness, the specific tone of stone that has been wet for months. Against it, the rust-ochre cursor (`#C47A5A`) is the warmest point — the only color in the image that references direct heat, the iron-stained cliff face revealed where the fog thins.
- **Fog as function color** — Functions take fog-cyan (`#7DC4D4`), not a vivid electric blue. This is the exact color of diffused light through sea-mist at midday — luminous but soft, pervasive but not piercing. It reads immediately on the dark ground while carrying the atmospheric quality of the source.
- **Depth in receding planes** — The sidebar panel uses sea-cave dark (`#111417`), darker than the editor surface, creating the same depth-by-recession that separates the cliff faces from each other in fog: the more distant, the darker the grey.

The result is a workspace that feels like standing at the edge of something large and still — the eye moves across code the way it moves across a foggy landscape, drawn by points of warmth and clarity without distraction from the periphery.

---

## Design Principles

### 1. A Spectrum Pulled from Coastal Atmosphere

The accent palette maps directly to what is visually present in the scene, moving from cold to warm. Fog-cyan (`#7DC4D4`) is the haze itself — the most pervasive color in the image, dominating the upper two-thirds of the frame. Stone-mauve (`#9A8CB0`) is the grey-violet of the floating stone bodies' shadowed faces, a color that exists only where light fails to fully penetrate the rock's crystalline structure. Cliff-grass olive (`#8AAA60`) is the dry, mineral-fed grass at the cliff edge — not lush green, but the specific yellow-green of grass growing on chalk and limestone. Amber-dry (`#C4A050`) is the straw color of the same grass where it has dried out completely, and also the iron-tinged ochre seen in the cliff faces at mid-distance. Cliff-rust (`#C47A5A`) is the warmest tone in the image — the iron-oxide staining visible on the underside of the foreground floating stone, the only thermal accent in an otherwise cold frame.

Each color was chosen over alternatives because the alternatives did not exist in the source. There is no purple in this image, so stone-mauve is as purple as it can be while remaining rooted in grey. There is no vivid green, so olive is as green as it can be while remaining dry.

### 2. Hierarchy Modeled on Visual Distance

In the image, visual importance correlates with distance from the fog: the near figure is darkest and most legible, the floating stones at mid-distance have the most complex coloration, the cliffs behind are pale silhouettes, the sky is near-white. The syntax hierarchy follows the same logic:

| Role | Color | Hex | Why |
|---|---|---|---|
| Functions | Fog Cyan | `#7DC4D4` | Most pervasive hue in the image; functions are the most called-upon tokens |
| Keywords | Coastal White | `#C8D8DC` | Pale as cliff faces in mist; structural but recessive — they frame, not perform |
| Types | Stone Mauve | `#9A8CB0` | The shadowed face of the floating stone — present, distinct, not competing |
| Strings | Cliff Grass | `#8AAA60` | Organic, ground-level; strings hold content the way grass holds the cliff edge |
| Attributes | Amber Dry | `#C4A050` | Iron-warm, a modifier tint — the dried grass that qualifies the living green |
| Literals | Cliff Rust | `#C47A5A` | The warmest accent; numeric and boolean literals are the most concrete values |
| Comments | Figure Dim | `#4A5060` | The cloaked figure's dark body — present but recessive, reading as silhouette |
| Errors | Marl Red | `#C45860` | The only fully chromatic red in an otherwise desaturated palette; errors must break the fog |

### 3. Background as Stage, Not Void

The backgrounds are not pure black. Each carries the blue-grey undertone of wet stone — the specific dark that comes from rock that has never fully dried. The panel is darker than the editor surface not because it is lower in hierarchy, but because it represents the deeper shadow, the part of the cliff face the fog reaches first.

- **Editor surface** (`#181B1F`) — the shadow on the near cliff face at the moment the fog begins to lift; dark but with visible texture.
- **Panel/sidebar** (`#111417`) — the inside of a sea-level cave behind the cliff, where daylight never fully arrives.
- **Highlight** (`#252B30`) — the moment a patch of fog passes and the stone surface momentarily brightens; selection lifts content without breaking the atmospheric coherence.
- **Errors** use Marl Red (`#C45860`) — not a bright emergency red, but the specific colour of oxidised iron seams in limestone, which read as rupture in an otherwise cool stone face without triggering alarm.

### 4. The Cursor as Anchor

The caret uses Cliff Rust (`#C47A5A`). In the image, this is the iron-oxide colour visible on the underside of the nearest floating stone — the warmest, most chemically specific tone in a frame that is otherwise made of atmospheric grey and muted green. It is the only evidence of geological time made visible by colour: that rust took centuries of oxidation to arrive at that exact shade. In the editor, the cursor serves the same function: a single fixed warm point in a cool field, the thing your eye returns to instinctively because it holds more thermal weight than everything around it.

---

## Color Palette Summary

### Backgrounds & UI

| Component | Hex | Role |
|---|---|---|
| Editor surface | `#181B1F` | Primary background |
| Panel / sidebar | `#111417` | Secondary background |
| Selection / hover | `#252B30` | Highlight state |
| Border / separator | `#2F363C` | Structural division |

### Syntax Tokens

| Token | Hex | Name |
|---|---|---|
| Keywords | `#C8D8DC` | Coastal White |
| Functions | `#7DC4D4` | Fog Cyan |
| Strings | `#8AAA60` | Cliff Grass |
| Types | `#9A8CB0` | Stone Mauve |
| Literals / Numbers | `#C47A5A` | Cliff Rust |
| Constants / Booleans | `#C4A050` | Amber Dry |
| Variables | `#C8D8DC` | Coastal White |
| Comments | `#4A5060` | Figure Dim |

### Supplementary Colors

| Use | Hex | Name |
|---|---|---|
| Attributes | `#C4A050` | Amber Dry |
| Errors | `#C45860` | Marl Red |
| Cursor | `#C47A5A` | Cliff Rust |
| Operators | `#8FA8B0` | Fog Dimmed |
| Constructors | `#A8CDD8` | Sky Pale |
| Water / Info | `#4A9090` | Water Teal |

---

## Typography Pairing

The "Suspended Marl" palette pairs with:

- **Primary:** JetBrains Mono — its geometric precision suits the theme's geological specificity; the letterforms have the same structural clarity as cliff stratification seen from a distance, regular layers with occasional sharp interruption.
- **Alternative:** Fira Code — slightly warmer stroke weight that reinforces the ochre-and-rust end of the palette; where JetBrains Mono reads as basalt, Fira Code reads as sandstone.

Ligatures like `=>`, `!==`, and `>=` read as the connecting logic between stone layers — the strata that hold impossible weight in place. They are invisible infrastructure, the way geology is invisible until something floats.

---

## How It Feels in Practice

Imagine opening a large TypeScript module on a grey Tuesday morning when the window shows nothing but cloud:

The editor surface is the first thing — not black, but the dark that precedes rain, a blue-grey that has absorbed several days of overcast sky. The sidebar is darker still, a shadow at the edge of your peripheral vision that does not distract. As you scan the file, the function names arrive first in fog-cyan, the most pervasive tone, distributed through the code the way mist occupies a landscape — everywhere and between everything, the medium through which other things are perceived. Keywords are chalk-pale, the near-white of wet limestone in flat light: you read them without consciously registering them, the way you read topography before you read detail. Type annotations appear in stone-mauve, slightly recessive, slightly cooler than the fog — the color of the floating stone's shadowed underside, the part of the geometry that hasn't caught the sky. Strings are cliff-grass olive, ground-level and organic, the one token that carries biological rather than geological warmth. When a number or boolean appears, it arrives in amber-dry, the single warmest cool accent, the iron-stained straw color of a cliff edge in late autumn. Comments trail away in the near-black of the cloaked figure, present at the margin, readable when you look directly, invisible when you don't. And the cursor: rust-ochre, stationary until you move it, holding more thermal weight than anything else on the screen — the iron seam in the marl that reminds you that geological time is present in every surface you're resting on.

That's Suspended Marl.
