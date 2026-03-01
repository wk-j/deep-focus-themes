# AGENTS.md — Coding Agent Guidelines

This is a **content-only repository** of dark editor/terminal color themes.
There is no build system, no tests, no CI pipeline, and no package manager.
All files are static assets: JSON, TOML, Markdown, and HTML.

## Build / Lint / Test

There are no build, lint, or test commands. Validation is manual:

- **JSON:** Ensure valid JSON (no trailing commas). Use 2-space indent.
- **TOML:** Ensure valid TOML for Helix, Zed extension, and Rio terminal parsers.
- **Markdown:** No linter configured. Follow existing conventions below.
- **Quick check:** `python3 -m json.tool <file> > /dev/null` to validate JSON.

## Repository Structure

```
deep-focus-themes/
  README.md              # Collection overview with theme summaries
  AGENTS.md              # This file
  <theme-name>/          # One directory per theme (kebab-case)
    docs/
      README.md          # Theme overview, palette table, key ideas
      <theme>-concept.md # Full design rationale
      index.html         # Optional: interactive preview page
    editors/
      helix/
        THEME_REFERENCE.md         # Optional: scope reference
        <theme-name>.toml          # Base Helix theme (kebab-case)
        <theme-name>-transparent.toml  # Transparent variant
      zed/
        THEME_REFERENCE.md         # Optional: scope reference
        extension.toml             # Zed extension metadata
        LICENSE                    # MIT license
        themes/<theme-name>.json   # Zed theme (4 variants in one file)
    palette/
      <theme-name>.json  # Canonical color palette (source of truth)
    terminals/
      rio/
        themes/<theme-name>.toml   # Optional: Rio terminal theme
```

## File Naming Conventions

| Context | Convention | Example |
|---|---|---|
| Theme directories | `kebab-case` | `neon-city/` |
| Palette/Zed/Rio files | `kebab-case` | `neon-city.json` |
| Helix theme files | `kebab-case` | `neon-city.toml` |
| Concept docs | `kebab-case` | `neon-city-concept.md` |
| Reference docs | `SCREAMING_CASE` | `THEME_REFERENCE.md` |

## JSON Formatting (Palette & Zed Themes)

- 2-space indentation, no trailing commas.
- Column-align values in palette files for readability:
  ```json
  "primary":    "#0D0221",
  "secondary":  "#07010F"
  ```
- Hex colors: 6-digit uppercase (`#FF2CF1`). Alpha suffixes are lowercase (`#FF2CF120`).
- Palette JSON key order: `name`, `description`, `colors` (`bg`, `fg`, `accent`, `ansi`), `semantic_roles`.
- `semantic_roles` values are dot-path references into `colors` (e.g., `"accent.magenta"`).
- Zed theme JSON key order: `$schema`, `name`, `author`, `themes[]`.
  Each theme: `name`, `appearance`, `style` (surfaces -> chrome -> text -> editor -> semantic states -> terminal -> players -> syntax).
- Syntax keys in Zed JSON are **alphabetically sorted**.
- Zed themes define exactly **4 variants**: opaque, low/medium/high transparency.
- Exactly **8 players** per Zed theme, each with `cursor`, `background` (cursor + `20` alpha), `selection` (cursor + `30` alpha).
- Schema reference: `https://zed.dev/schema/themes/v0.2.0.json`.

## TOML Formatting

### Helix Themes

- Flat dotted-key syntax, NOT nested tables:
  ```toml
  "keyword" = { fg = "keyword_white", modifiers = ["bold"] }
  "type.builtin" = { fg = "cyber_blue" }
  ```
- Section order: Syntax Highlighting, Interface / UI, `[palette]`.
- Sections separated by box-drawing comment headers:
  ```toml
  # ─── Syntax Highlighting ─────────────────────────────────
  ```
- Palette color names use `snake_case` (`electric_magenta`, `bg_primary`).
- Background keys are standardized: `bg_primary`, `bg_secondary`, `bg_highlight`, `border`, `selection`, `gutter_fg`.
- Transparent variant uses `inherits = "<theme-name>"` and only overrides UI chrome scopes.

### Zed Extension (extension.toml)

```toml
id = "<theme-name>-theme"
name = "Human Readable Name"
version = "0.0.1"
schema_version = 1
authors = ["wk"]
description = "One-line description"
repository = "https://github.com/wk-j/<theme-name>"
```

### Rio Terminal Themes

- Single `[colors]` section, `kebab-case` keys (Rio requirement).
- Single-quoted hex values: `'#FF2CF1'`.
- Column-aligned values.
- Sections grouped by comments: Core, ANSI, Bright, Dim, Navigation/UI, Selection, Search, Hints.

## Palette JSON Schema

The `palette/<theme-name>.json` file is the **canonical source of truth** for a theme's colors. All editor/terminal theme files should derive from it.

```
{
  "name": "...",
  "description": "...",
  "colors": {
    "bg":     { "primary", "secondary", "highlight", "border" },
    "fg":     { "primary", "dimmed", "muted", "gutter" },
    "accent": { <theme-specific named colors, snake_case> },
    "ansi":   { "black".."white", "bright_black".."bright_white" }
  },
  "semantic_roles": {
    "keywords": "accent.xxx",    // dot-path references into colors
    "functions": "accent.xxx",
    ...
  }
}
```

ANSI keys use `snake_case` with `bright_` prefix. Accent colors vary per theme (6-11 colors). Semantic roles vary (10-15 entries).

## Markdown Conventions

- `# H1` for page title, `## H2` for major sections, `### H3` for subsections.
- No hard line wrapping — single long lines for prose.
- Tables: pipe-delimited with `|---|` separator, no padding alignment.
- Bulleted lists use `-` with **bold lead phrases**: `- **Key phrase.** Explanation.`
- Horizontal rules: `---` with blank lines before and after.
- Code blocks: triple backtick with language identifier.
- Links: inline style `[text](url)`.

### Per-Theme Documentation Pattern

**`docs/README.md`** (~30 lines): H1 title, one-paragraph description, `## Palette` table (Token | Hex | Name), `## Key Ideas` bullet list, link to concept doc.

**`docs/<theme>-concept.md`** (~100-112 lines): H1 title with `— Color Scheme Concept` suffix, `## Vision`, `## Design Principles` (4 numbered subsections), `## Color Palette Summary` (3 tables), `## Typography Pairing`, `## How It Feels in Practice`.

## Adding a New Theme

1. Create `<theme-name>/` directory (kebab-case).
2. Start with `palette/<theme-name>.json` — define all colors first.
3. Create `docs/README.md` and `docs/<theme-name>-concept.md` following existing patterns.
4. Create Helix themes: `editors/helix/<theme-name>.toml` + `-transparent.toml`.
5. Create Zed theme: `editors/zed/extension.toml` + `themes/<theme-name>.json` (4 variants) + `LICENSE`.
6. Optionally add `terminals/rio/themes/<theme-name>.toml`.
7. Update root `README.md`: add theme summary section and update the support matrix.

## Color Design Principles

All themes share these tenets — maintain them when editing or adding themes:

- **Depth over borders.** Panels separated by background shade, not lines.
- **Logical color hierarchy.** Each syntax role gets a distinct, purposeful color.
- **Unmissable cursor.** High-contrast caret color as constant anchor.
- **Soft error states.** Errors signal clearly without triggering anxiety.
- **Typography pairing.** Designed for JetBrains Mono or Fira Code with ligatures.
