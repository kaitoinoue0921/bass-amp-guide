#!/usr/bin/env python3
"""index.html（Artifact用、doctypeなし）を GitHub Pages 用の docs/index.html に包む。"""
import pathlib
root = pathlib.Path(__file__).parent
body = (root / "index.html").read_text(encoding="utf-8")
head = """<!doctype html>
<html lang="ja">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex">
<style>:root{color-scheme:light;padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0;font:14px system-ui,-apple-system,"Hiragino Sans",sans-serif}img{max-width:100%}[hidden]{display:none!important}</style>
"""
out = root / "docs"
out.mkdir(exist_ok=True)
(out / "index.html").write_text(head + body, encoding="utf-8")
(out / ".nojekyll").write_text("")
print("wrote", out / "index.html", (out / "index.html").stat().st_size)
