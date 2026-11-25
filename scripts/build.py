#!/usr/bin/env python3
"""Generate all 10 Rosé Pine Custom Zed themes in themes/rose-pine.json.

Usage: python3 scripts/build.py

Builds five curated dark Rosé Pine directions (Traditional, Espresso, Pine, Ink, Dusk),
each with both Bordered and Unbordered variants in a single themes/rose-pine.json file.
"""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "themes"
SCHEMA = "https://zed.dev/schema/themes/v0.2.0.json"
AUTHOR = "Dallas Gere"
TRANSPARENT = "#00000000"
GIT_DIM = 0.92


def blend(fg, alpha, bg):
    """Straight sRGB mix: alpha of fg over bg."""
    a = [int(fg[i : i + 2], 16) for i in (1, 3, 5)]
    b = [int(bg[i : i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(x * alpha + y * (1 - alpha)):02x}" for x, y in zip(a, b))


def tok(color, style="normal", weight=400):
    return {"color": color, "font_style": style, "font_weight": weight}


# Rosé Pine Moon's richer warm rose (#ea9a97) and clearer teal pine (#3e8fb0).
RP = {
    "love": "#eb6f92",
    "gold": "#f6c177",
    "rose": "#ea9a97",
    "pine": "#3e8fb0",
    "foam": "#9ccfd8",
    "iris": "#c4a7e7",
    "green": "#8cc296",
}

BASES = [
    {
        "name": "Rosé Pine",
        "editor": "#191724",     # traditional Rosé Pine twilight plum
        "shell": "#15131f",
        "elevated": "#232033",
        "line": "#1f1d2e",
        "hover": "#211e30",
        "selected": "#2b283f",
        "selection": "#36324d",
        "border": "#29263b",
        "border_v": "#201e2f",
        "text": "#d8d5eb",
        "subtle": "#908caa",
        "muted": "#6e6a86",
        "line_num": "#524f67",
    },
    {
        "name": "Rosé Pine: Espresso",
        "editor": "#1c1a19",     # warm smoked cocoa / volcanic basalt
        "shell": "#171514",
        "elevated": "#252220",
        "line": "#221f1e",
        "hover": "#24211f",
        "selected": "#2e2a28",
        "selection": "#38322f",
        "border": "#2b2725",
        "border_v": "#221f1d",
        "text": "#d6d1cc",
        "subtle": "#968e88",
        "muted": "#756d68",
        "line_num": "#544e4a",
    },
    {
        "name": "Rosé Pine: Pine",
        "editor": "#151c1e",     # deep dark evergreen slate
        "shell": "#111718",
        "elevated": "#1d2629",
        "line": "#1a2225",
        "hover": "#1b2426",
        "selected": "#243033",
        "selection": "#28393e",
        "border": "#222c2f",
        "border_v": "#1a2224",
        "text": "#cfd6d8",
        "subtle": "#839296",
        "muted": "#627175",
        "line_num": "#455256",
    },
    {
        "name": "Rosé Pine: Ink",
        "editor": "#19191a",     # pure achromatic graphite
        "shell": "#141415",
        "elevated": "#222224",
        "line": "#1f1f21",
        "hover": "#212123",
        "selected": "#2b2b2e",
        "selection": "#333338",
        "border": "#28282b",
        "border_v": "#202022",
        "text": "#d2d1d6",
        "subtle": "#8c8b92",
        "muted": "#6b6a72",
        "line_num": "#4e4d54",
    },
    {
        "name": "Rosé Pine: Dusk",
        "editor": "#1d1b1f",     # dark neutral charcoal with a hint of warm taupe
        "shell": "#18161a",
        "elevated": "#262329",
        "line": "#232026",
        "hover": "#252228",
        "selected": "#302c34",
        "selection": "#3a3440",
        "border": "#2c2930",
        "border_v": "#232026",
        "text": "#d4d1de",
        "subtle": "#908aa0",
        "muted": "#6e697d",
        "line_num": "#504c5c",
    },
]


def build_variant(ex, unbordered=False):
    ed = ex["editor"]
    sh = ed if unbordered else ex["shell"]
    el = ex["elevated"]
    bdr = TRANSPARENT if unbordered else ex["border"]
    bdr_v = TRANSPARENT if unbordered else ex["border_v"]

    g_add = blend(RP["green"], GIT_DIM, ed)
    g_mod = blend(RP["pine"], GIT_DIM, ed)
    g_del = blend(RP["love"], GIT_DIM, ed)
    g_con = blend("#e89a7a", GIT_DIM, ed)
    inv = blend(ex["text"], 0.42, ex["selection"])

    syntax_groups = [
        (tok(ex["muted"], "italic"), ("comment", "comment.doc")),
        (tok(ex["muted"]), ("hint", "predictive")),
        (tok(RP["pine"]), (
            "keyword", "keyword.conditional", "keyword.control", "keyword.coroutine",
            "keyword.directive", "keyword.export", "keyword.function", "keyword.import",
            "keyword.modifier", "keyword.repeat", "keyword.return", "keyword.storage",
            "keyword.type", "keyword.operator", "preproc", "string.escape", "string.regex",
        )),
        (tok(ex["subtle"]), (
            "operator", "punctuation", "punctuation.bracket", "punctuation.delimiter",
            "punctuation.list_marker", "punctuation.markup", "punctuation.special",
        )),
        (tok(RP["rose"]), (
            "function", "function.call", "function.definition", "function.method", "function.method.call",
        )),
        (tok(RP["love"]), (
            "variable.special", "boolean", "constant.builtin", "keyword.exception",
            "function.builtin", "function.special", "diff.minus",
        )),
        (tok(RP["green"]), ("diff.plus",)),
        (tok(RP["gold"]), (
            "string", "string.doc", "string.special", "text.literal", "link_text", "number",
        )),
        (tok(RP["iris"]), (
            "constant", "variant", "enum", "string.special.symbol",
            "variable.parameter", "attribute", "selector", "selector.pseudo",
        )),
        (tok(RP["foam"]), (
            "type", "type.builtin", "type.interface", "type.parameter", "constructor",
            "namespace", "tag", "tag.doctype", "title", "property", "variable.member",
            "property.json_key", "link_uri",
        )),
        (tok(ex["text"]), (
            "variable", "label", "embedded", "emphasis", "emphasis.strong", "primary",
        )),
    ]
    syntax = {k: dict(v) for v, ks in syntax_groups for k in ks}

    name = f"{ex['name']} Unbordered" if unbordered else ex["name"]
    return {
        "name": name,
        "appearance": "dark",
        "style": {
            "background.appearance": "opaque",
            "background": sh,
            "border": bdr,
            "border.variant": bdr_v,
            "border.focused": TRANSPARENT,
            "border.selected": TRANSPARENT,
            "border.transparent": TRANSPARENT,
            "border.disabled": bdr,
            "elevated_surface.background": el,
            "surface.background": sh,
            "element.background": el,
            "element.hover": ex["hover"],
            "element.active": ex["selected"],
            "element.selected": ex["selected"],
            "element.disabled": el,
            "drop_target.background": RP["rose"] + "2b",
            "ghost_element.background": TRANSPARENT,
            "ghost_element.hover": ex["hover"],
            "ghost_element.active": ex["selected"],
            "ghost_element.selected": ex["selected"],
            "ghost_element.disabled": TRANSPARENT,
            "text": ex["text"],
            "text.muted": ex["subtle"],
            "text.placeholder": ex["muted"],
            "text.disabled": ex["line_num"],
            "text.accent": RP["rose"],
            "icon": ex["text"],
            "icon.muted": ex["subtle"],
            "icon.disabled": ex["line_num"],
            "icon.placeholder": ex["muted"],
            "icon.accent": RP["rose"],
            "status_bar.background": sh,
            "title_bar.background": sh,
            "title_bar.inactive_background": sh,
            "toolbar.background": ed,
            "tab_bar.background": sh,
            "tab.inactive_background": sh,
            "tab.active_background": el if unbordered else ed,
            "search.match_background": RP["gold"] + "29",
            "search.active_match_background": RP["gold"] + "4d",
            "panel.background": sh,
            "panel.focused_border": TRANSPARENT,
            "panel.indent_guide": ex["border_v"],
            "panel.indent_guide_active": ex["selected"],
            "panel.indent_guide_hover": ex["selected"],
            "pane.focused_border": TRANSPARENT,
            "pane_group.border": bdr,
            "scrollbar.thumb.background": ex["subtle"] + "38",
            "scrollbar.thumb.hover_background": ex["subtle"] + "5c",
            "scrollbar.thumb.active_background": ex["subtle"] + "80",
            "scrollbar.thumb.border": TRANSPARENT,
            "scrollbar.track.background": TRANSPARENT,
            "scrollbar.track.border": TRANSPARENT,
            "minimap.thumb.background": ex["subtle"] + "30",
            "minimap.thumb.hover_background": ex["subtle"] + "50",
            "minimap.thumb.active_background": ex["subtle"] + "75",
            "minimap.thumb.border": TRANSPARENT,
            "editor.foreground": ex["text"],
            "editor.background": ed,
            "editor.gutter.background": ed,
            "editor.subheader.background": el,
            "editor.active_line.background": ex["line"],
            "editor.highlighted_line.background": ex["line"],
            "editor.line_number": ex["line_num"],
            "editor.active_line_number": ex["text"],
            "editor.hover_line_number": ex["text"],
            "editor.invisible": inv,
            "editor.wrap_guide": ex["border_v"],
            "editor.active_wrap_guide": ex["selected"],
            "editor.indent_guide": ex["border_v"],
            "editor.indent_guide_active": ex["selected"],
            "editor.document_highlight.read_background": RP["foam"] + "1c",
            "editor.document_highlight.write_background": RP["foam"] + "2e",
            "editor.document_highlight.bracket_background": RP["rose"] + "24",
            "link_text.hover": RP["foam"],
            "terminal.background": ed,
            "terminal.foreground": ex["text"],
            "terminal.ansi.background": ed,
            "terminal.bright_foreground": "#ebe8f2",
            "terminal.dim_foreground": ex["subtle"],
            "terminal.ansi.black": el,
            "terminal.ansi.bright_black": ex["muted"],
            "terminal.ansi.red": RP["love"],
            "terminal.ansi.bright_red": "#f285a4",
            "terminal.ansi.green": RP["green"],
            "terminal.ansi.bright_green": "#a4d4ad",
            "terminal.ansi.yellow": RP["gold"],
            "terminal.ansi.bright_yellow": "#fad091",
            "terminal.ansi.blue": RP["pine"],
            "terminal.ansi.bright_blue": "#56a6c7",
            "terminal.ansi.magenta": RP["iris"],
            "terminal.ansi.bright_magenta": "#d4bcf0",
            "terminal.ansi.cyan": RP["foam"],
            "terminal.ansi.bright_cyan": "#b3dce3",
            "terminal.ansi.white": ex["text"],
            "terminal.ansi.bright_white": "#ebe8f2",
            **{
                f"{k}{suffix}": c + (a or "")
                for k, c in {
                    "error": RP["love"], "warning": RP["gold"], "info": RP["foam"],
                    "hint": ex["subtle"], "success": RP["green"],
                    "created": RP["green"], "modified": RP["gold"], "deleted": RP["love"],
                    "renamed": RP["green"], "conflict": "#e89a7a", "ignored": ex["muted"],
                    "hidden": ex["line_num"], "unreachable": ex["subtle"], "predictive": ex["muted"],
                }.items()
                for suffix, a in (("", None), (".background", "2e" if k in ("created", "deleted", "modified") else "1f"), (".border", "66"))
            },
            "hint.background": el,
            "version_control.added": g_add,
            "version_control.modified": g_mod,
            "version_control.deleted": g_del,
            "version_control.renamed": g_mod,
            "version_control.conflict": g_con,
            "version_control.ignored": ex["muted"],
            "version_control.word_added": g_add + "5c",
            "version_control.word_deleted": g_del + "5c",
            "players": [
                {"cursor": "#ffffff", "background": RP["rose"], "selection": ex["selection"]},
                {"cursor": RP["foam"], "background": RP["foam"], "selection": RP["foam"] + "3d"},
                {"cursor": RP["gold"], "background": RP["gold"], "selection": RP["gold"] + "3d"},
                {"cursor": RP["iris"], "background": RP["iris"], "selection": RP["iris"] + "3d"},
                {"cursor": RP["love"], "background": RP["love"], "selection": RP["love"] + "3d"},
            ],
            "accents": [RP["rose"], RP["foam"], RP["gold"], RP["iris"], RP["pine"], RP["love"]],
            "syntax": dict(sorted(syntax.items())),
        },
    }


def main():
    OUT.mkdir(exist_ok=True)
    themes = []
    for base in BASES:
        for unbordered in (False, True):
            themes.append(build_variant(base, unbordered=unbordered))

    family = {"$schema": SCHEMA, "name": "Rosé Pine Custom", "author": AUTHOR, "themes": themes}
    (OUT / "rose-pine.json").write_text(json.dumps(family, indent=2, ensure_ascii=False) + "\n")
    for t in themes:
        print(f"themes/rose-pine.json: {t['name']}")


if __name__ == "__main__":
    main()
