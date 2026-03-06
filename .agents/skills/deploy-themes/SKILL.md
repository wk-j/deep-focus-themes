---
name: deploy-themes
description: Deploy editor and terminal themes from this repository to their local installation paths (Helix, Zed, Rio, Yazi, Lazygit, OpenCode, Lexer)
---

## Deployment Targets

### Helix

- **Target:** `/Users/wk/Source/helix/runtime/themes/`
- **Method:** Copy files (not symlinks)
- **Files per theme:**
  - `<theme-name>.toml` (base theme)
  - `<theme-name>-transparent.toml` (transparent variant)
- **Source:** `<theme-name>/editors/helix/`

### Zed

- **Target:** `~/Library/Application Support/Zed/extensions/installed/`
- **Method:** Symlink the `editors/zed/` directory as `<theme-name>-theme`
- **Symlink format:** `<theme-name>-theme -> /Users/wk/Source/deep-focus-themes/<theme-name>/editors/zed`

### Rio Terminal

- **Target:** `~/.config/rio/themes/`
- **Method:** Copy files (not symlinks)
- **Files per theme:** `<theme-name>.toml`
- **Source:** `<theme-name>/terminals/rio/themes/`
- **Note:** Not all themes have Rio support. Only deploy if the source file exists.

### Yazi

- **Target:** `~/.config/yazi/flavors/`
- **Method:** Copy the entire `<theme-name>.yazi/` directory
- **Source:** `<theme-name>/terminals/yazi/<theme-name>.yazi/`
- **Required files inside `<theme-name>.yazi/`:**
  - `flavor.toml` — UI theme config
  - `tmtheme.xml` — code preview syntax highlighting
  - `README.md` — description and usage
  - `LICENSE` — flavor license
  - `LICENSE-tmtheme` — tmTheme license
- **Note:** Not all themes have Yazi support. Only deploy if the source directory exists.

### Lazygit

- **Target:** `~/Library/Application Support/lazygit/` (macOS) or `~/.config/lazygit/` (Linux)
- **Method:** Merge into the user's `config.yml` using lazygit's multi-file config feature — do **not** overwrite `config.yml` directly.
- **Source:** `<theme-name>/terminals/lazygit/<theme-name>.yml`
- **Note:** Not all themes have lazygit support. Only deploy if the source file exists.

### OpenCode

- **Target:** `~/.config/opencode/themes/`
- **Method:** Copy file
- **Source:** `<theme-name>/editors/opencode/<theme-name>.json`
- **Activate:** Set `"theme": "<theme-name>"` in `~/.config/opencode/tui.json` — replace the existing `"theme"` value in place.
- **Note:** Not all themes have opencode support. Only deploy if the source file exists.

### Lexer

- **Target:** `~/.config/lexer/themes/`
- **Method:** Copy file
- **Source:** `<theme-name>/editors/lexer/<theme-name>.toml`
- **Activate:** Select with `Space t` in the app, or launch with `lexer --theme <theme-name>`.
- **Note:** Not all themes have Lexer support. Only deploy if the source file exists. Theme is hot-reloaded on save.

## Deployment Procedure

### 1. Deploy to Helix

For each theme directory in the repo:

```bash
cp <theme-name>/editors/helix/<theme-name>.toml /Users/wk/Source/helix/runtime/themes/
cp <theme-name>/editors/helix/<theme-name>-transparent.toml /Users/wk/Source/helix/runtime/themes/
```

### 2. Deploy to Zed

For each theme that has `editors/zed/`:

```bash
INSTALL_DIR="$HOME/Library/Application Support/Zed/extensions/installed"
rm -f "$INSTALL_DIR/<theme-name>-theme"
ln -s "/Users/wk/Source/deep-focus-themes/<theme-name>/editors/zed" "$INSTALL_DIR/<theme-name>-theme"
```

### 3. Deploy to Rio

For each theme that has `terminals/rio/themes/<theme-name>.toml`:

```bash
cp <theme-name>/terminals/rio/themes/<theme-name>.toml ~/.config/rio/themes/
```

### 4. Deploy to Yazi

For each theme that has `terminals/yazi/<theme-name>.yazi/`:

```bash
cp -r <theme-name>/terminals/yazi/<theme-name>.yazi ~/.config/yazi/flavors/
```

### 6. Deploy to OpenCode

For each theme that has `editors/opencode/<theme-name>.json`:

```bash
mkdir -p ~/.config/opencode/themes
cp <theme-name>/editors/opencode/<theme-name>.json ~/.config/opencode/themes/
```

Then activate by editing `~/.config/opencode/tui.json` — replace the `"theme"` value:

```json
{
  "$schema": "https://opencode.ai/tui.json",
  "theme": "<theme-name>"
}
```

**To switch themes**, update the `"theme"` value to a different theme name.

### 7. Deploy to Lexer

For each theme that has `editors/lexer/<theme-name>.toml`:

```bash
mkdir -p ~/.config/lexer/themes
cp <theme-name>/editors/lexer/<theme-name>.toml ~/.config/lexer/themes/
```

Then select the theme with `Space t` in Lexer, or launch with `lexer --theme <theme-name>`.

### 5. Deploy to Lazygit

Replace the `gui.theme` block in the user's existing `config.yml` directly.

**Config file location:**
- macOS: `~/Library/Application Support/lazygit/config.yml`
- Linux: `~/.config/lazygit/config.yml`

**Procedure:**
1. Read the current `config.yml` to locate the existing `gui.theme` block.
2. Replace only the `theme:` keys with the values from `<theme-name>/terminals/lazygit/<theme-name>.yml`.
3. Leave all other settings (`sidePanelWidth`, `pagers`, etc.) untouched.
4. No env vars or shell profile changes needed — lazygit picks up the change immediately on next launch.

**To switch themes**, repeat the procedure with a different theme's `.yml` file.

## Current Theme Inventory

| Theme | Helix | Zed | Rio | Yazi | Lazygit | OpenCode | Lexer |
|---|---|---|---|---|---|---|---|
| neon-city | yes | yes | yes | no | no | yes | no |
| crystal-city | yes | yes | yes | no | no | no | no |
| twilight-overclock | yes | yes | yes | no | no | no | no |
| cinder-grid | no | yes | yes | no | no | no | yes |
| stargazer | yes | no | no | yes | no | no | no |
| tallow-light | no | no | no | no | yes | yes | no |

## Verification

After deployment, confirm installed files match the repo:

```bash
# Helix
diff <theme>/editors/helix/<theme>.toml /Users/wk/Source/helix/runtime/themes/<theme>.toml

# Zed
readlink "$HOME/Library/Application Support/Zed/extensions/installed/<theme>-theme"

# Rio
diff <theme>/terminals/rio/themes/<theme>.toml ~/.config/rio/themes/<theme>.toml

# Yazi
ls ~/.config/yazi/flavors/<theme>.yazi/

# Lazygit
cat ~/.config/lazygit/themes/<theme>.yml
# or check the env var is set:
echo $LG_CONFIG_FILE

# OpenCode
ls ~/.config/opencode/themes/<theme>.json
cat ~/.config/opencode/tui.json

# Lexer
diff <theme>/editors/lexer/<theme>.toml ~/.config/lexer/themes/<theme>.toml
```

## Rollback

To remove a deployed theme:

```bash
# Helix
rm /Users/wk/Source/helix/runtime/themes/<theme-name>.toml
rm /Users/wk/Source/helix/runtime/themes/<theme-name>-transparent.toml

# Zed
rm "$HOME/Library/Application Support/Zed/extensions/installed/<theme-name>-theme"

# Rio
rm ~/.config/rio/themes/<theme-name>.toml

# Yazi
rm -rf ~/.config/yazi/flavors/<theme-name>.yazi

# Lazygit — remove copied file and unset/update LG_CONFIG_FILE in shell profile
rm ~/.config/lazygit/themes/<theme-name>.yml

# OpenCode — remove copied file and revert tui.json theme value
rm ~/.config/opencode/themes/<theme-name>.json

# Lexer
rm ~/.config/lexer/themes/<theme-name>.toml
```
