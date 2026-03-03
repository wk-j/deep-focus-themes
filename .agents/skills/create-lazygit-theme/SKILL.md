---
name: create-lazygit-theme
description: Generate a lazygit color theme config snippet for a theme that already has a palette JSON. Produces a ready-to-paste YAML block for the lazygit config file.
---

## What this skill does

Generate a lazygit `gui.theme` YAML block from an existing palette JSON.

Output file: `<theme-name>/terminals/lazygit/<theme-name>.yml`

The file contains **only the `gui:` section** so it can be used standalone with `--use-config-file` or merged into the user's main `config.yml`.

---

## Inputs

The user provides:
- **Theme name** (kebab-case, e.g. `neon-city`)
- **Palette JSON** at `<theme-name>/palette/<theme-name>.json` — the canonical color source

Always read the palette file before generating any YAML. All colors must be derived from the palette's `colors` or `semantic_roles` objects.

---

## Lazygit theme config reference

Config file location:
- **macOS:** `~/Library/Application Support/lazygit/config.yml`
- **Linux:** `~/.config/lazygit/config.yml`

The theme lives under `gui.theme`. Every color key takes a **YAML sequence** of one or more values. Valid values:

### Named colors
`black`, `red`, `green`, `yellow`, `blue`, `magenta`, `cyan`, `white`, `default`

### Hex colors
Quoted 6-digit hex: `'#FF2CF1'`

### Modifiers (can be combined with a color)
`bold`, `reverse`, `underline`, `strikethrough`, `default`

A sequence may combine **at most one color** with one or more modifiers:
```yaml
- '#FF2CF1'
- bold
```

---

## Color key mapping

| lazygit key | Semantic role | Notes |
|---|---|---|
| `activeBorderColor` | `cursor` accent | Border of the focused panel. Use the cursor/hero accent + `bold`. |
| `inactiveBorderColor` | `fg.muted` | Border of unfocused panels. Use a mid-grey/muted foreground. |
| `searchingActiveBorderColor` | `types` accent | Border when searching in a panel. Distinct from active. |
| `optionsTextColor` | `attributes` accent | Keybinding help text at the bottom. |
| `selectedLineBgColor` | `bg.highlight` | Background of the selected line in a list. |
| `inactiveViewSelectedLineBgColor` | — | Selected line when view lacks focus. Use `bold` with `default` bg. |
| `cherryPickedCommitFgColor` | `functions` accent | Foreground of a cherry-picked commit. |
| `cherryPickedCommitBgColor` | `strings` accent | Background of a cherry-picked commit. |
| `markedBaseCommitFgColor` | `functions` accent | Foreground of marked rebase base commit. |
| `markedBaseCommitBgColor` | `literals` accent (numbers/orange) | Background of marked rebase base commit. |
| `unstagedChangesColor` | `errors` accent | Color for files with unstaged changes. |
| `defaultFgColor` | `fg.primary` | Default text color. |

### Mapping strategy

1. Read `semantic_roles` from the palette JSON.
2. Follow `dot-path` references into `colors` to get the actual hex.
3. Apply the mapping table above to assign each lazygit key.
4. For `selectedLineBgColor`, use `colors.bg.highlight` directly.
5. For `inactiveViewSelectedLineBgColor`, use `['bold']` only (no color — relies on terminal's bold rendering for a subtle lift).

---

## Output file format

```yaml
# <Theme Name> — Lazygit Theme
# Paste this into ~/Library/Application Support/lazygit/config.yml
# or use: lazygit --use-config-file="$HOME/.config/lazygit/config.yml,<path-to-this-file>"

gui:
  theme:
    activeBorderColor:
      - '<hex>'
      - bold
    inactiveBorderColor:
      - '<hex>'
    searchingActiveBorderColor:
      - '<hex>'
      - bold
    optionsTextColor:
      - '<hex>'
    selectedLineBgColor:
      - '<hex>'
    inactiveViewSelectedLineBgColor:
      - bold
    cherryPickedCommitFgColor:
      - '<hex>'
    cherryPickedCommitBgColor:
      - '<hex>'
    markedBaseCommitFgColor:
      - '<hex>'
    markedBaseCommitBgColor:
      - '<hex>'
    unstagedChangesColor:
      - '<hex>'
    defaultFgColor:
      - '<hex>'
```

Rules:
- 2-space YAML indentation throughout.
- Hex values are single-quoted: `'#FF2CF1'`.
- Hex colors are 6-digit uppercase.
- Do not include any keys outside `gui.theme`.
- Do not include other `gui` settings (scroll, borders, etc.) — theme only.

---

## File location

Write the output to:

```
<theme-name>/terminals/lazygit/<theme-name>.yml
```

Create the directory `<theme-name>/terminals/lazygit/` if it does not exist.

---

## After generation

1. Show the user the resolved color mapping as a summary table:

   | Key | Color name | Hex |
   |---|---|---|
   | `activeBorderColor` | e.g. `accent.cyan` | `#00FFFF` |
   | ... | ... | ... |

2. Remind the user how to apply the theme:

   **Option A — Merge into main config:**
   Copy the `gui.theme` block into `~/Library/Application Support/lazygit/config.yml` (macOS) or `~/.config/lazygit/config.yml` (Linux).

   **Option B — Use as supplementary file:**
   ```sh
   lazygit --use-config-file="$HOME/Library/Application Support/lazygit/config.yml,$(pwd)/<theme-name>/terminals/lazygit/<theme-name>.yml"
   ```

   Or set the env var:
   ```sh
   LG_CONFIG_FILE="$HOME/Library/Application Support/lazygit/config.yml,<path>/<theme-name>/terminals/lazygit/<theme-name>.yml" lazygit
   ```

3. Remind the user to update the `deploy-themes` skill's **Current Theme Inventory** table if they want this theme deployed automatically.
