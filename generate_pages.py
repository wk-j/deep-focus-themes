#!/usr/bin/env python3
"""
generate_pages.py — Deep Focus Themes static site generator

Reads every palette/<theme>.json and produces:
  - site/<theme-name>/index.html   per-theme preview page
  - site/index.html                gallery page listing all themes

Output directory: ./site/
Run: python3 generate_pages.py
"""

import json
import os
import re
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
SITE = ROOT / "site"

# ── Helpers ───────────────────────────────────────────────────────────────────


def slug_to_title(slug: str) -> str:
    return " ".join(w.capitalize() for w in slug.split("-"))


def resolve_color(palette: dict, dot_path: str) -> str:
    """Resolve a dot-path like 'accent.ember' into a hex color."""
    parts = dot_path.split(".")
    node = palette["colors"]
    for p in parts:
        node = node[p]
    return node


def get_semantic_colors(palette: dict) -> dict:
    """Return a flat dict of role -> hex for semantic_roles."""
    roles = palette.get("semantic_roles", {})
    result = {}
    for role, path in roles.items():
        try:
            result[role] = resolve_color(palette, path)
        except (KeyError, TypeError):
            result[role] = palette["colors"]["fg"]["primary"]
    return result


def luminance(hex_color: str) -> float:
    """Relative luminance of a hex color (0..1)."""
    h = hex_color.lstrip("#")
    r, g, b = (int(h[i : i + 2], 16) / 255 for i in (0, 2, 4))

    def lin(c):
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)


def contrast_ratio(a: str, b: str) -> float:
    la, lb = luminance(a), luminance(b)
    bright, dark = max(la, lb), min(la, lb)
    return (bright + 0.05) / (dark + 0.05)


def hex_with_alpha(hex_color: str, alpha: float) -> str:
    """Return rgba() CSS string from hex + 0..1 alpha."""
    h = hex_color.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"


# ── Code sample ───────────────────────────────────────────────────────────────


def build_code_lines(sem: dict, fg_primary: str) -> str:
    """Return HTML for the code preview lines using semantic colors."""
    kw = sem.get("keywords", "#FFFFFF")
    fn = sem.get("functions", "#FF00FF")
    st = sem.get("strings", "#00FF00")
    cm = sem.get("comments", "#666666")
    tp = sem.get("types", "#00FFFF")
    at = sem.get("attributes", "#FFFF00")
    nm = sem.get("literals", "#FF8800")
    cn = sem.get("constants", "#FF8800")
    vr = fg_primary
    pu = sem.get("operators", "#888888")

    def span(cls, color, text):
        return f'<span style="color:{color}{";font-weight:700" if cls == "kw" else ""}{";font-style:italic" if cls == "cm" else ""}">{text}</span>'

    lines = [
        (
            1,
            f'{span("kw", kw, "import")} {span("vr", vr, "React")} {span("kw", kw, "from")} {span("st", st, "&apos;react&apos;")}<span style="color:{pu}">;</span>',
        ),
        (
            2,
            f'{span("kw", kw, "import")} {span("kw", kw, "type")} <span style="color:{pu}">{{</span> {span("tp", tp, "ThemeConfig")} <span style="color:{pu}">}}</span> {span("kw", kw, "from")} {span("st", st, "&apos;@themes/core&apos;")}<span style="color:{pu}">;</span>',
        ),
        (3, ""),
        (4, f"{span('cm', cm, '// Resolve palette from canonical source')}"),
        (
            5,
            f'{span("kw", kw, "const")} {span("cn", cn, "MAX_LAYERS")} <span style="color:{pu}">=</span> {span("nm", nm, "8")}<span style="color:{pu}">;</span>',
        ),
        (6, ""),
        (
            7,
            f'{span("kw", kw, "const")} {span("vr", vr, "App")}<span style="color:{pu}">:</span> {span("tp", tp, "React.FC")}<span style="color:{pu}">&lt;</span>{span("tp", tp, "ThemeConfig")}<span style="color:{pu}">&gt;</span> <span style="color:{pu}">=</span> <span style="color:{pu}">()</span> <span style="color:{pu}">=&gt;</span> <span style="color:{pu}">{{</span>',
        ),
        (
            8,
            f'  {span("kw", kw, "const")} <span style="color:{pu}">[</span>{span("vr", vr, "active")}<span style="color:{pu}">,</span> {span("vr", vr, "setActive")}<span style="color:{pu}">]</span> <span style="color:{pu}">=</span> {span("fn", fn, "useState")}<span style="color:{pu}">(</span>{span("cn", cn, "true")}<span style="color:{pu}">);</span>',
        ),
        (
            9,
            f'  {span("kw", kw, "const")} {span("vr", vr, "depth")} <span style="color:{pu}">=</span> {span("fn", fn, "useMemo")}<span style="color:{pu}">(()</span> <span style="color:{pu}">=&gt;</span> {span("fn", fn, "calcDepth")}<span style="color:{pu}">(</span>{span("nm", nm, "0.85")}<span style="color:{pu}">),</span> <span style="color:{pu}">[]);</span>',
        ),
        (10, ""),
        (11, f'  {span("kw", kw, "return")} <span style="color:{pu}">(</span>'),
        (
            12,
            f'    <span style="color:{pu}">&lt;</span>{span("tp", tp, "ThemeProvider")} {span("at", at, "depth")}<span style="color:{pu}">={{</span>{span("nm", nm, "MAX_LAYERS")}<span style="color:{pu}">}}&gt;</span>',
        ),
        (
            13,
            f'      <span style="color:{pu}">&lt;</span>{span("tp", tp, "Layout")} {span("at", at, "theme")}<span style="color:{pu}">=</span>{span("st", st, "&quot;deep-focus&quot;")}<span style="color:{pu}">&gt;</span>',
        ),
        (
            14,
            f'        <span style="color:{pu}">&lt;</span>{span("tp", tp, "h1")}<span style="color:{pu}">&gt;</span><span style="color:{vr}">Deep Focus</span><span style="color:{pu}">&lt;/</span>{span("tp", tp, "h1")}<span style="color:{pu}">&gt;</span>',
        ),
        (
            15,
            f'      <span style="color:{pu}">&lt;/</span>{span("tp", tp, "Layout")}<span style="color:{pu}">&gt;</span>',
        ),
        (
            16,
            f'    <span style="color:{pu}">&lt;/</span>{span("tp", tp, "ThemeProvider")}<span style="color:{pu}">&gt;</span>',
        ),
        (17, f'  <span style="color:{pu}">);</span>'),
        (18, f'<span style="color:{pu}">}};</span>'),
        (19, ""),
        (
            20,
            f'{span("kw", kw, "export default")} {span("vr", vr, "App")}<span style="color:{pu}">;</span>',
        ),
    ]

    html = ""
    for n, content in lines:
        html += f'<div class="code-line"><span class="line-number">{n}</span><span class="code-content">{content}</span></div>\n'
    return html


# ── Per-theme page ────────────────────────────────────────────────────────────

THEME_PAGE_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} — Deep Focus Theme</title>
  <style>
    *, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}

    :root {{
      --bg-primary:   {bg_primary};
      --bg-secondary: {bg_secondary};
      --bg-highlight: {bg_highlight};
      --border:       {border};
      --fg-primary:   {fg_primary};
      --fg-dimmed:    {fg_dimmed};
      --fg-muted:     {fg_muted};
      --fg-gutter:    {fg_gutter};
      --hero-color:   {hero_color};
      --hero-glow:    {hero_glow};
    }}

    body {{
      background: var(--bg-secondary);
      color: var(--fg-primary);
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.6;
      min-height: 100vh;
    }}

    /* ── Nav ─────────────────────────────────────────────────────────── */
    .nav {{
      padding: 1rem 1.5rem;
      border-bottom: 1px solid var(--border);
      background: var(--bg-secondary);
    }}
    .nav a {{
      color: var(--fg-dimmed);
      text-decoration: none;
      font-size: 0.85rem;
      transition: color 0.15s;
    }}
    .nav a:hover {{ color: var(--fg-primary); }}
    .nav a::before {{ content: '← '; }}

    /* ── Hero ────────────────────────────────────────────────────────── */
    .hero {{
      text-align: center;
      padding: 4rem 1.5rem 3rem;
      position: relative;
      overflow: hidden;
    }}
    .hero::before {{
      content: '';
      position: absolute;
      top: 0; left: 50%;
      transform: translateX(-50%);
      width: 600px; height: 200px;
      background: radial-gradient(ellipse, var(--hero-glow) 0%, transparent 70%);
      pointer-events: none;
    }}
    .hero h1 {{
      font-size: clamp(2.5rem, 6vw, 4.5rem);
      font-weight: 900;
      letter-spacing: 0.08em;
      color: var(--hero-color);
      text-shadow: 0 0 20px var(--hero-glow), 0 0 60px var(--hero-glow);
      margin-bottom: 1rem;
      text-transform: uppercase;
    }}
    .hero p {{
      font-size: clamp(0.9rem, 2vw, 1.05rem);
      color: var(--fg-dimmed);
      max-width: 540px;
      margin: 0 auto 2.5rem;
      line-height: 1.75;
    }}

    /* ── Buttons ─────────────────────────────────────────────────────── */
    .buttons {{
      display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; margin-bottom: 3rem;
    }}
    .btn {{
      display: inline-block; padding: 0.65rem 1.75rem; border-radius: 8px;
      font-size: 0.95rem; font-weight: 600; cursor: pointer;
      transition: all 0.2s; text-decoration: none; border: 2px solid transparent;
      background: none;
    }}
    .btn-primary {{
      color: var(--hero-color); border-color: var(--hero-color);
    }}
    .btn-primary:hover {{
      background: var(--hero-glow); box-shadow: 0 0 20px var(--hero-glow);
    }}
    .btn-primary.copied {{ border-color: var(--fg-muted); color: var(--fg-muted); }}
    .btn-secondary {{
      background: var(--bg-highlight); color: var(--fg-primary); border-color: var(--border);
    }}
    .btn-secondary:hover {{ border-color: var(--fg-dimmed); background: var(--border); }}

    /* ── Color Swatches ──────────────────────────────────────────────── */
    .swatches {{
      display: flex; gap: 0.5rem; justify-content: center; flex-wrap: wrap;
      margin-bottom: 3rem; padding: 0 1.5rem;
    }}
    .swatch {{
      display: flex; flex-direction: column; align-items: center; gap: 0.4rem;
    }}
    .swatch-dot {{
      width: 32px; height: 32px; border-radius: 50%;
      border: 1px solid var(--border);
      box-shadow: 0 0 8px rgba(0,0,0,0.4);
    }}
    .swatch-label {{
      font-size: 0.65rem; color: var(--fg-muted); text-align: center; max-width: 60px;
    }}

    /* ── Editor Preview ──────────────────────────────────────────────── */
    .preview-container {{
      max-width: 860px; margin: 0 auto 4rem; padding: 0 1.5rem;
    }}
    .vscode {{
      background: var(--bg-primary); border-radius: 10px; overflow: hidden;
      box-shadow: 0 4px 30px rgba(0,0,0,0.5), 0 0 1px var(--hero-glow);
      border: 1px solid var(--border);
    }}
    .vscode-titlebar {{
      background: var(--bg-secondary); padding: 0.5rem 1rem;
      display: flex; align-items: center; border-bottom: 1px solid var(--border);
      position: relative;
    }}
    .traffic-lights {{ display: flex; gap: 6px; }}
    .traffic-lights span {{
      width: 12px; height: 12px; border-radius: 50%;
    }}
    .traffic-lights .red    {{ background: #FF5F57; }}
    .traffic-lights .yellow {{ background: #FEBC2E; }}
    .traffic-lights .green  {{ background: #28C840; }}
    .vscode-title {{
      position: absolute; left: 50%; transform: translateX(-50%);
      font-size: 0.75rem; color: var(--fg-muted);
    }}
    .vscode-tabs {{
      background: var(--bg-secondary); display: flex; border-bottom: 1px solid var(--border);
    }}
    .vscode-tab {{
      padding: 0.5rem 1rem; font-size: 0.8rem; color: var(--fg-muted);
      border-right: 1px solid var(--border); cursor: default; position: relative;
    }}
    .vscode-tab.active {{
      background: var(--bg-primary); color: var(--fg-primary);
    }}
    .vscode-tab.active::after {{
      content: ''; position: absolute; bottom: 0; left: 0; right: 0;
      height: 2px; background: var(--hero-color);
    }}
    .vscode-tab .close {{ margin-left: 0.5rem; opacity: 0.5; font-size: 0.7rem; }}
    .vscode-body {{ display: flex; min-height: 400px; }}
    .vscode-sidebar {{
      width: 180px; background: var(--bg-secondary);
      border-right: 1px solid var(--border); padding: 0.75rem 0; flex-shrink: 0;
    }}
    .sidebar-header {{
      font-size: 0.65rem; font-weight: 600; letter-spacing: 0.1em;
      color: var(--fg-muted); padding: 0 1rem 0.5rem; text-transform: uppercase;
    }}
    .file-tree {{ list-style: none; }}
    .file-tree li {{
      padding: 0.2rem 1rem; font-size: 0.8rem; color: var(--fg-muted);
      display: flex; align-items: center; gap: 0.4rem; cursor: default;
    }}
    .file-tree li.active {{ background: var(--bg-highlight); color: var(--fg-primary); }}
    .vscode-editor {{
      flex: 1; padding: 1rem 0; overflow-x: auto;
      font-family: 'JetBrains Mono', 'Fira Code', 'SF Mono', Consolas, monospace;
      font-size: 0.85rem; line-height: 1.75;
    }}
    .code-line {{ display: flex; padding: 0 1rem; white-space: pre; }}
    .line-number {{
      color: var(--fg-gutter); width: 2.5em; text-align: right;
      margin-right: 1.5em; user-select: none; flex-shrink: 0;
    }}
    .code-content {{ flex: 1; }}

    /* ── Palette Table ───────────────────────────────────────────────── */
    .palette-section {{
      max-width: 860px; margin: 0 auto 4rem; padding: 0 1.5rem;
    }}
    .palette-section h2 {{
      font-size: 1rem; font-weight: 600; letter-spacing: 0.08em;
      text-transform: uppercase; color: var(--fg-dimmed); margin-bottom: 1rem;
    }}
    .palette-grid {{
      display: grid; grid-template-columns: repeat(auto-fill, minmax(120px, 1fr)); gap: 0.75rem;
    }}
    .palette-cell {{
      border-radius: 8px; overflow: hidden; border: 1px solid var(--border);
    }}
    .palette-cell-color {{
      height: 48px;
    }}
    .palette-cell-info {{
      background: var(--bg-primary); padding: 0.4rem 0.6rem;
    }}
    .palette-cell-name {{
      font-size: 0.7rem; color: var(--fg-dimmed); text-transform: capitalize;
      white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
    }}
    .palette-cell-hex {{
      font-size: 0.7rem; color: var(--fg-muted);
      font-family: 'JetBrains Mono', 'Fira Code', monospace;
    }}

    /* ── Footer ──────────────────────────────────────────────────────── */
    footer {{
      text-align: center; padding: 2rem 1.5rem;
      color: var(--fg-muted); font-size: 0.8rem; border-top: 1px solid var(--border);
    }}
    footer a {{ color: var(--fg-dimmed); text-decoration: none; }}
    footer a:hover {{ color: var(--fg-primary); }}

    @media (max-width: 640px) {{
      .vscode-sidebar {{ display: none; }}
      .vscode-editor {{ font-size: 0.75rem; }}
    }}
  </style>
</head>
<body>
  <nav class="nav"><a href="../index.html">All Themes</a></nav>

  <div class="main-content">
    <section class="hero">
      <h1>{title}</h1>
      <p>{description}</p>
      <div class="buttons">
        <button class="btn btn-primary" id="copyBtn" onclick="copyHelixConfig()">Copy Helix Theme Name</button>
        <a class="btn btn-secondary" href="https://github.com/wk-j/deep-focus-themes" target="_blank">GitHub</a>
      </div>
    </section>

    <div class="swatches">
{swatch_html}
    </div>

    <section class="preview-container">
      <div class="vscode">
        <div class="vscode-titlebar">
          <div class="traffic-lights">
            <span class="red"></span><span class="yellow"></span><span class="green"></span>
          </div>
          <span class="vscode-title">{slug} — Helix</span>
        </div>
        <div class="vscode-tabs">
          <div class="vscode-tab active">App.tsx <span class="close">&times;</span></div>
          <div class="vscode-tab">theme.json</div>
        </div>
        <div class="vscode-body">
          <div class="vscode-sidebar">
            <div class="sidebar-header">Explorer</div>
            <ul class="file-tree">
              <li><span>&#128193;</span> src</li>
              <li class="active"><span>&#10070;</span> App.tsx</li>
              <li><span>#</span> styles.css</li>
            </ul>
          </div>
          <div class="vscode-editor">
{code_lines}
          </div>
        </div>
      </div>
    </section>

    <section class="palette-section">
      <h2>Full Palette</h2>
      <div class="palette-grid">
{palette_cells}
      </div>
    </section>
  </div>

  <footer>
    <p>Part of <a href="../index.html">Deep Focus Themes</a> &mdash; Dark coding color schemes for long sessions.</p>
  </footer>

  <script>
    function copyHelixConfig() {{
      const btn = document.getElementById('copyBtn');
      navigator.clipboard.writeText('{slug}').then(() => {{
        btn.textContent = 'Copied!';
        btn.classList.add('copied');
        setTimeout(() => {{
          btn.textContent = 'Copy Helix Theme Name';
          btn.classList.remove('copied');
        }}, 2000);
      }});
    }}
  </script>
</body>
</html>
"""

# ── Gallery page ──────────────────────────────────────────────────────────────

GALLERY_PAGE_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Deep Focus Themes</title>
  <style>
    *, *::before, *::after {{ margin: 0; padding: 0; box-sizing: border-box; }}
    :root {{
      --bg:        #0A0D14;
      --bg-card:   #0F131D;
      --border:    #1C2436;
      --fg:        #C8D0DE;
      --fg-dim:    #6A7A8E;
      --fg-muted:  #384456;
    }}
    body {{
      background: var(--bg);
      color: var(--fg);
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      line-height: 1.6;
      min-height: 100vh;
    }}

    /* ── Header ──────────────────────────────────────────────────────── */
    header {{
      text-align: center;
      padding: 5rem 1.5rem 3rem;
      border-bottom: 1px solid var(--border);
    }}
    header h1 {{
      font-size: clamp(2rem, 5vw, 3.5rem);
      font-weight: 900;
      letter-spacing: 0.06em;
      color: var(--fg);
      margin-bottom: 0.75rem;
    }}
    header p {{
      color: var(--fg-dim);
      font-size: 1.05rem;
      max-width: 480px;
      margin: 0 auto;
    }}
    header a {{
      color: var(--fg-dim);
      text-decoration: none;
      font-size: 0.85rem;
      margin-top: 1.5rem;
      display: inline-block;
      border: 1px solid var(--border);
      padding: 0.4rem 1.2rem;
      border-radius: 6px;
      transition: all 0.2s;
    }}
    header a:hover {{ color: var(--fg); border-color: var(--fg-dim); }}

    /* ── Grid ────────────────────────────────────────────────────────── */
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 1.5rem;
      max-width: 1200px;
      margin: 3rem auto;
      padding: 0 1.5rem;
    }}

    /* ── Card ────────────────────────────────────────────────────────── */
    .card {{
      background: var(--bg-card);
      border: 1px solid var(--border);
      border-radius: 12px;
      overflow: hidden;
      transition: border-color 0.2s, transform 0.2s;
      text-decoration: none;
      color: inherit;
      display: block;
    }}
    .card:hover {{
      border-color: var(--card-hero);
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(0,0,0,0.4);
    }}

    /* Mini editor preview */
    .mini-editor {{
      background: var(--card-bg);
      padding: 0.75rem 1rem;
      font-family: 'JetBrains Mono', 'Fira Code', monospace;
      font-size: 0.72rem;
      line-height: 1.7;
      height: 130px;
      overflow: hidden;
      position: relative;
    }}
    .mini-editor::after {{
      content: '';
      position: absolute;
      bottom: 0; left: 0; right: 0;
      height: 40px;
      background: linear-gradient(transparent, var(--card-bg));
    }}

    /* Swatch strip */
    .swatch-strip {{
      display: flex;
      height: 6px;
    }}
    .swatch-strip span {{
      flex: 1;
    }}

    /* Card body */
    .card-body {{
      padding: 1.25rem;
    }}
    .card-title {{
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--card-hero);
      margin-bottom: 0.4rem;
    }}
    .card-desc {{
      font-size: 0.8rem;
      color: var(--fg-dim);
      line-height: 1.6;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}
    .card-footer {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-top: 1rem;
      padding-top: 0.75rem;
      border-top: 1px solid var(--border);
    }}
    .card-tags {{
      display: flex; gap: 0.4rem; flex-wrap: wrap;
    }}
    .tag {{
      font-size: 0.65rem;
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
      background: var(--border);
      color: var(--fg-dim);
    }}
    .card-arrow {{
      color: var(--card-hero);
      font-size: 0.85rem;
    }}

    /* ── Footer ──────────────────────────────────────────────────────── */
    footer {{
      text-align: center; padding: 3rem 1.5rem;
      color: var(--fg-muted); font-size: 0.8rem;
      border-top: 1px solid var(--border);
    }}
    footer a {{ color: var(--fg-dim); text-decoration: none; }}
  </style>
</head>
<body>
  <header>
    <h1>Deep Focus Themes</h1>
    <p>Dark coding color schemes designed for long sessions — low fatigue, high clarity.</p>
    <a href="https://github.com/wk-j/deep-focus-themes" target="_blank">GitHub →</a>
  </header>

  <main class="grid">
{cards_html}
  </main>

  <footer>
    <p>Built for <a href="https://helix-editor.com">Helix</a>, <a href="https://zed.dev">Zed</a>, Rio, and Yazi &mdash; <a href="https://github.com/wk-j/deep-focus-themes">View on GitHub</a></p>
  </footer>
</body>
</html>
"""

# ── Build functions ───────────────────────────────────────────────────────────


def build_swatch_html(sem: dict, palette: dict) -> str:
    roles = [
        ("functions", "Functions"),
        ("keywords", "Keywords"),
        ("strings", "Strings"),
        ("types", "Types"),
        ("literals", "Numbers"),
        ("constants", "Constants"),
        ("attributes", "Attributes"),
        ("errors", "Errors"),
        ("cursor", "Cursor"),
    ]
    html = ""
    for role, label in roles:
        color = sem.get(role)
        if color:
            html += f'      <div class="swatch">\n'
            html += (
                f'        <div class="swatch-dot" style="background:{color}"></div>\n'
            )
            html += f'        <div class="swatch-label">{label}</div>\n'
            html += f"      </div>\n"
    return html


def build_palette_cells(palette: dict) -> str:
    html = ""
    for section, values in palette["colors"].items():
        for name, hex_val in values.items():
            display_name = f"{section}.{name}"
            html += f'        <div class="palette-cell">\n'
            html += f'          <div class="palette-cell-color" style="background:{hex_val}"></div>\n'
            html += f'          <div class="palette-cell-info">\n'
            html += f'            <div class="palette-cell-name">{display_name}</div>\n'
            html += f'            <div class="palette-cell-hex">{hex_val}</div>\n'
            html += f"          </div>\n"
            html += f"        </div>\n"
    return html


def build_card_mini_editor(sem: dict, bg: str) -> str:
    kw = sem.get("keywords", "#FFFFFF")
    fn = sem.get("functions", "#FF00FF")
    st = sem.get("strings", "#00FF00")
    cm = sem.get("comments", "#666666")
    tp = sem.get("types", "#00FFFF")
    nm = sem.get("literals", "#FF8800")
    pu = sem.get("operators", "#888888")

    def s(color, text, bold=False, italic=False):
        style = f"color:{color}"
        if bold:
            style += ";font-weight:700"
        if italic:
            style += ";font-style:italic"
        return f'<span style="{style}">{text}</span>'

    lines = [
        f"{s(kw, 'import', bold=True)} {s(fn, 'React')} {s(kw, 'from', bold=True)} {s(st, '&apos;react&apos;')}",
        f"{s(cm, '// Initialize palette engine', italic=True)}",
        f"{s(kw, 'const', bold=True)} {s(tp, 'ThemeConfig')} = {{",
        f"  {s(nm, 'depth')}: {s(nm, '8')}, {s(nm, 'layers')}: {s(nm, 'true')},",
        f"{s(kw, 'const', bold=True)} {s(fn, 'render')} = () => {{",
        f"  {s(kw, 'return', bold=True)} {s(st, '&lt;App theme=&quot;focus&quot;/&gt;')}",
    ]
    html = ""
    for line in lines:
        html += f"<div>{line}</div>\n"
    return html


def build_card_html(slug: str, palette: dict, sem: dict, support_tags: list) -> str:
    title = slug_to_title(slug)
    bg = palette["colors"]["bg"]["primary"]
    hero = sem.get("functions", palette["colors"]["fg"]["primary"])
    hero_glow = hex_with_alpha(hero, 0.12)
    desc = palette.get("description", "")[:120]

    # swatch strip: accent colors
    accents = list(palette["colors"]["accent"].values())[:8]
    strip = "".join(f'<span style="background:{c}"></span>' for c in accents)

    mini_lines = build_card_mini_editor(sem, bg)

    tags_html = "".join(f'<span class="tag">{t}</span>' for t in support_tags)

    return f"""\
    <a class="card" href="{slug}/index.html" style="--card-bg:{bg};--card-hero:{hero};">
      <div class="mini-editor" style="background:{bg};">{mini_lines}</div>
      <div class="swatch-strip">{strip}</div>
      <div class="card-body">
        <div class="card-title">{title}</div>
        <div class="card-desc">{desc}</div>
        <div class="card-footer">
          <div class="card-tags">{tags_html}</div>
          <span class="card-arrow">→</span>
        </div>
      </div>
    </a>
"""


def detect_support(theme_dir: Path) -> list:
    tags = []
    if (theme_dir / "editors" / "helix").exists():
        tags.append("Helix")
    if (theme_dir / "editors" / "zed").exists():
        tags.append("Zed")
    if (theme_dir / "terminals" / "rio").exists():
        tags.append("Rio")
    if (theme_dir / "terminals" / "yazi").exists():
        tags.append("Yazi")
    return tags


# ── Main ──────────────────────────────────────────────────────────────────────


def main():
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir()

    palette_files = sorted(ROOT.glob("*/palette/*.json"))
    cards = []

    for pf in palette_files:
        slug = pf.parent.parent.name
        theme_dir = pf.parent.parent

        with open(pf) as f:
            palette = json.load(f)

        sem = get_semantic_colors(palette)
        bg = palette["colors"]["bg"]
        fg = palette["colors"]["fg"]
        hero = sem.get("functions", fg["primary"])
        hero_glow = hex_with_alpha(hero, 0.15)

        title = slug_to_title(slug)
        description = palette.get("description", "")
        support = detect_support(theme_dir)

        code_lines = build_code_lines(sem, fg["primary"])
        swatch_html = build_swatch_html(sem, palette)
        palette_cells = build_palette_cells(palette)

        page_html = THEME_PAGE_TEMPLATE.format(
            slug=slug,
            title=title,
            description=description,
            bg_primary=bg["primary"],
            bg_secondary=bg["secondary"],
            bg_highlight=bg["highlight"],
            border=bg["border"],
            fg_primary=fg["primary"],
            fg_dimmed=fg["dimmed"],
            fg_muted=fg["muted"],
            fg_gutter=fg["gutter"],
            hero_color=hero,
            hero_glow=hero_glow,
            code_lines=code_lines,
            swatch_html=swatch_html,
            palette_cells=palette_cells,
        )

        theme_out = SITE / slug
        theme_out.mkdir()
        (theme_out / "index.html").write_text(page_html)
        print(f"  built: site/{slug}/index.html")

        cards.append(build_card_html(slug, palette, sem, support))

    # Gallery
    gallery = GALLERY_PAGE_TEMPLATE.format(cards_html="".join(cards))
    (SITE / "index.html").write_text(gallery)
    print(f"  built: site/index.html")
    print(f"\nDone — {len(palette_files)} themes → site/")


if __name__ == "__main__":
    main()
