# Rosé Pine Custom Theme

Five curated dark **Rosé Pine** directions for [Zed](https://zed.dev) (each in **Bordered** and **Unbordered** styles — 10 variants total) packaged in a single `themes/rose-pine.json` file, with Rosé Pine Moon's richer syntax hues, harmonized git diff colors, clean file explorer selection, legible whitespace dots, and a `#ffffff` cursor.

## Variants (10 total)

- **Rosé Pine** / **Rosé Pine Unbordered** — Traditional twilight plum (`#191724`)
- **Rosé Pine: Espresso** / **Rosé Pine: Espresso Unbordered** — Warm smoked cocoa (`#1c1a19`)
- **Rosé Pine: Pine** / **Rosé Pine: Pine Unbordered** — Deep evergreen slate (`#151c1e`)
- **Rosé Pine: Ink** / **Rosé Pine: Ink Unbordered** — Pure neutral graphite (`#19191a`)
- **Rosé Pine: Dusk** / **Rosé Pine: Dusk Unbordered** — Dark neutral charcoal with a hint of warm taupe (`#1d1b1f`)

## Install locally

1. In Zed, open the command palette and run `zed: install dev extension`.
2. Select this folder.
3. Run `theme selector: toggle` and pick any `Rosé Pine` variant.

Or copy `themes/rose-pine.json` into `~/.config/zed/themes/`.

## Regenerating

```bash
python3 scripts/build.py
```
