# -*- coding: utf-8 -*-
"""実行済みノートブックの出力を検査: エラーの有無と主要な stdout を表示。"""
import sys
import io
import nbformat

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

path = sys.argv[1]
nb = nbformat.read(path, as_version=4)
n_err = 0
n_empty_code = 0
for i, c in enumerate(nb.cells):
    if c.cell_type != "code":
        continue
    outs = c.get("outputs", [])
    if not outs:
        n_empty_code += 1
    for o in outs:
        if o.output_type == "error":
            n_err += 1
            print(f"=== CELL {i} ERROR: {o.ename}: {o.evalue[:300]}")
        elif o.output_type == "stream":
            head = c.source.splitlines()[0][:50] if c.source else ""
            print(f"--- cell {i} [{head}] ({o.name})")
            print(o.text[:1200])
print(f"\n{path}: errors={n_err}")
