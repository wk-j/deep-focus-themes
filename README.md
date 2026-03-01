# Deep Focus Themes

A collection of dark coding color schemes designed for long sessions — low fatigue, high clarity. Each theme shares common design principles but brings its own distinct personality.

## Themes

### [Twilight Overclock](twilight-overclock/docs/README.md)

Deep Forest base with Bioluminescent accents. Charcoal-teal backgrounds with Electric Cyan functions, Sage Moss keywords, and Honey Amber strings. Calm at rest, instantly readable when scanning.

| Background | Keywords | Functions | Strings | Variables |
|---|---|---|---|---|
| `#0B1215` | `#7FB069` | `#00F5FF` | `#FFB347` | `#E0E0E0` |

### [Neon City](neon-city/docs/README.md)

Midnight base with an Electric Neon Spectrum. Purple-black backgrounds with Electric Magenta functions, Bold White keywords, and Plasma Green strings. Vivid, focused, and alive.

| Background | Keywords | Functions | Strings | Types |
|---|---|---|---|---|
| `#0D0221` | `#FFFFFF` | `#FF2CF1` | `#39FF14` | `#00D4FF` |

### [Crystal City](crystal-city/docs/README.md)

Obsidian base with a Crystalline Spectrum. Blue-black backgrounds with Crystal Teal functions, Bold White keywords, and Mint Glass strings. Calm, focused, and sharp.

| Background | Keywords | Functions | Strings | Types |
|---|---|---|---|---|
| `#0A0E1A` | `#FFFFFF` | `#56D4C8` | `#89DDCA` | `#7EC8E3` |

## Supported Editors & Terminals

| Platform | Twilight Overclock | Neon City | Crystal City |
|---|---|---|---|
| Zed | yes | yes | yes |
| Helix | yes | yes | yes |
| Rio terminal | - | yes | yes |

Each theme includes a standard and transparent variant for Helix.

## Design Principles

All themes in this collection share a common philosophy:

- **Depth over borders.** Panels are separated by background shade shifts, not lines.
- **Logical color hierarchy.** Every syntax color has a specific semantic job.
- **Unmissable cursor.** High-contrast caret that anchors your position.
- **Soft error states.** Error colors tuned to signal without causing anxiety.
- **Typography pairing.** Designed for JetBrains Mono or Fira Code with ligature support.

## Repository Structure

```
deep-focus-themes/
  <theme-name>/
    docs/           # README and design concept
    editors/
      helix/        # Helix theme files (.toml)
      zed/          # Zed extension and theme files (.json)
    palette/        # Canonical color palette (.json)
    terminals/
      rio/          # Rio terminal theme (.toml)
```

## License

See individual theme directories for license details.
