# Silica Haze — Color Scheme Concept

## Origin

The source is a science-fiction landscape of rolling sand dunes under a dust-saturated atmosphere on a planet with two moons. The air is not clear — it is thick with suspended silica, and the light passing through it arrives warm, diffused, and directionless. Two crescent moons hang in the upper atmosphere like pale ivory punctuation marks, the only objects in the scene with a defined edge. Everything else — the dune ridges, the far horizon, the sky itself — bleeds into everything else through gradients of cream, gold, sienna, and deep chocolate umber. A few distant stars penetrate the haze as tiny warm-yellow sparks. The foreground is coarse sand and gravel, the colour of fired terracotta.

---

## Vision

silica-haze is a coding color scheme drawn from a world where the atmosphere is made of the same material as the ground. The central tension is monochrome warmth against the need for chromatic differentiation — in the image, nearly everything shares the same warm gold-brown hue, yet the eye still reads depth, distance, and form through minute temperature shifts and value contrasts.

It resolves this tension through three design decisions:

- **Warm monochrome pushed to its limit** — The backgrounds (`#1C1410`, `#140E0A`) and foregrounds (`#E0D4C0`, `#B0A088`) all live in the same warm brown-cream family, the way every surface in the image shares sand's fundamental hue. The workspace feels thermally unified, not assembled from arbitrary colors.
- **One cool counterpoint** — Dust Teal (`#6AAAA0`) is the single cool accent, the colour you might glimpse if you could somehow see through the haze to a sky beyond it. It exists for types and structural annotations — the things that describe shape rather than content. Its coolness is deliberate isolation, not decoration.
- **Luminosity as hierarchy** — In the image, the brightest things are the moon crescents and the lit dune crests. In the editor, the brightest tokens are keywords (Pale Ivory `#EAE0CA`) and functions (Cream Gold `#D4B870`). The hierarchy is the same: brighter means more structurally important, darker means more contextual.

The result is a workspace that feels like working inside the atmosphere of the image — warm, enveloping, with depth emerging from value differences rather than hue jumps. The eye is not stimulated; it is settled.

---

## Design Principles

### 1. A Palette Fired in a Single Kiln

Every accent except Dust Teal comes from the warm side of the spectrum. Cream Gold (`#D4B870`) is the exact colour of sunlit sand grain at the dune crest — the highest-energy moment in the image. Copper (`#C8804A`) is the shadow side of that same dune, where the sand compacts and oxidises. Dune Sienna (`#A06838`) is the gravel in the foreground — coarser, heavier, less reflective than the wind-polished crest. Spore Green (`#8AAA68`) is not truly green — it is the yellow-green of a lichen or moss that could survive in this world, the single organic note in a mineral palette. These are not chosen for variety; they are the material states of a single substance (silica) under different conditions of light, compression, and age.

Dust Teal was chosen over blue because pure blue would read as sky — and there is no visible sky in this image. Teal carries enough green to read as mineral rather than atmospheric, like the verdigris that forms on copper exposed to dry wind.

### 2. Luminosity Tracks Structural Weight

In the reference image, the moons are the brightest objects and also the most geometrically precise — perfect crescents in a field of soft gradients. Keywords take this role: Pale Ivory (`#EAE0CA`) with bold weight, the brightest tokens in the file, geometrically precise structural markers. Functions take Cream Gold (`#D4B870`), the next brightest — the lit dune crests, the most visually active surfaces. From there the hierarchy descends:

| Role | Color | Hex | Why |
|---|---|---|---|
| Keywords | Pale Ivory | `#EAE0CA` | The crescent moons — brightest, most precise shapes in the haze |
| Functions | Cream Gold | `#D4B870` | Sunlit dune crests — the most active, visible surfaces |
| Strings | Spore Green | `#8AAA68` | The single organic note — content with biological warmth |
| Types | Dust Teal | `#6AAAA0` | The cool shape seen through haze — structural annotation, not content |
| Attributes | Copper | `#C8804A` | The shadow-side of the dune — modifier tone, still warm |
| Literals | Copper | `#C8804A` | Compressed sand — concrete, specific values with material weight |
| Constants | Dune Sienna | `#A06838` | Foreground gravel — heavier, darker, fixed in place |
| Comments | Buried Grain | `#7A6850` | Sand buried in its own shadow — present but receding |

### 3. Background as Stage, Not Void

The backgrounds carry warm umber undertones throughout — no blue, no grey, no neutral. The darkness in the image is not the darkness of space visible through atmosphere; it is the darkness of sand in shadow, sand piled deep enough to absorb its own light. Every dark pixel in the reference is still warm.

- **Editor surface** (`#1C1410`) — the colour of dune shadow at the base of a slip face, where compacted sand absorbs most of the ambient light but still reads as material, not emptiness.
- **Panel/sidebar** (`#140E0A`) — deeper still, the shadow inside a wind-carved trough where no direct light arrives. Recessed and quiet, the place where peripheral UI retreats.
- **Highlight** (`#2C2018`) — the moment a dune ridge catches a slightly brighter angle of haze-light; selection lifts content the way a ridge crest lifts above the surrounding field.
- **Errors** use Kiln Red (`#C05040`) — the colour of terracotta that has been fired too long, cracked and exposed. It breaks the warm gold spectrum without introducing an alien hue — still a fired-earth colour, but one that signals structural failure in the material.

### 4. The Cursor as Anchor

The caret uses Cream Gold (`#D4B870`). In the image, this is the colour of the brightest sand — the razor-thin line where a dune crest catches the maximum angle of diffused light. It is a line, not a surface: narrow, bright, and precisely located against the broader warm field. In the editor, the cursor serves the same function. It is the single brightest warm point, a crest-line in a landscape of umber, and the eye finds it the way it finds the lit edge of a dune — immediately, without searching, because luminosity difference in a monochrome field is the strongest possible signal.

---

## Color Palette Summary

### Backgrounds & UI

| Component | Hex | Role |
|---|---|---|
| Editor surface | `#1C1410` | Primary background |
| Panel / sidebar | `#140E0A` | Secondary background |
| Selection / hover | `#2C2018` | Highlight state |
| Border / separator | `#3A2C20` | Structural division |

### Syntax Tokens

| Token | Hex | Name |
|---|---|---|
| Keywords | `#EAE0CA` | Pale Ivory |
| Functions | `#D4B870` | Cream Gold |
| Strings | `#8AAA68` | Spore Green |
| Types | `#6AAAA0` | Dust Teal |
| Literals / Numbers | `#C8804A` | Copper |
| Constants / Booleans | `#A06838` | Dune Sienna |
| Variables | `#E0D4C0` | Sand White |
| Comments | `#7A6850` | Buried Grain |

### Supplementary Colors

| Use | Hex | Name |
|---|---|---|
| Attributes | `#C8804A` | Copper |
| Errors | `#C05040` | Kiln Red |
| Cursor | `#D4B870` | Cream Gold |
| Operators | `#B0A088` | Dimmed Sand |
| Constructors | `#F0E8D0` | Crescent |
| Info / Links | `#7090B0` | Haze Blue |

---

## Typography Pairing

The "Silica Haze" palette pairs with:

- **Primary:** JetBrains Mono — its uniform stroke weight reads like machine-cut inscription in stone; the regularity of the glyphs provides the geometric precision that the dune landscape lacks, anchoring code in a field of soft gradients.
- **Alternative:** Fira Code — slightly rounder terminals give the text a worn quality, like letterforms stamped into dried clay that have softened at the edges over time.

Ligatures like `=>`, `!==`, and `>=` reinforce the sense of ancient mechanism — operators that feel carved rather than typed, joining tokens the way wind-carved channels join one dune face to the next.

---

## How It Feels in Practice

Imagine opening a Rust module at two in the afternoon with the blinds half-drawn and the room already warm:

The editor surface is the first thing — not black but umber, the specific warmth of sand that has been in shadow for hours but has not yet cooled. The sidebar is darker still, a trough between dunes that your peripheral vision registers as depth rather than boundary. As you scan the file, keywords arrive in pale ivory, the brightest points in the warm field, bold and structurally unmissable the way two crescent moons are unmissable in a sky made of dust. Function calls glow in cream gold beneath them, the lit faces of dune crests — your eye tracks their rhythm across the file the way it would track the ridge-line of a dune sea from altitude. Strings appear in spore green, the only biological warmth in a mineral world, marking content that was written by a human for a human to read. Type annotations sit in dust teal, the single cool element, structurally important but chromatically recessed — the blueprint notation in a warm construction. Numbers and attributes arrive in copper, dense and specific, the colour of compacted sand on the shadow side. Constants are darker still, dune sienna, fixed values with the weight of gravel. Comments fade into buried grain, the same warm family as everything else but halved in luminosity — present in the stratigraphy but not in the current layer. And the cursor: cream gold, a thin bright line where the dune crest catches maximum light, the single point in the warm monochrome field where your eye is always, instantly, without effort, home.

That's Silica Haze.
