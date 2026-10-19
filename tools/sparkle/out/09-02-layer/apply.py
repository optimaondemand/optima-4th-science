#!/usr/bin/env python3
"""Adds the 9.02 layer piece (wobble = Missing-link sim) to fs-sparkle.js/.css. Idempotent. usage: apply.py <js> <css>"""
import sys, os
here = os.path.dirname(os.path.abspath(__file__))
js_p, css_p = sys.argv[1], sys.argv[2]
js = open(js_p, encoding='utf-8').read(); css = open(css_p, encoding='utf-8').read()
def once(s, old, new, what):
    n = s.count(old)
    if n != 1: sys.exit(f'{what}: anchor found {n} times')
    return s.replace(old, new)
if 'function buildWobble' not in js:
    js = once(js, '  /* ---------- Lesson Part 4: "Pass it on?"', open(os.path.join(here, 'wobble.js'), encoding='utf-8').read() + '  /* ---------- Lesson Part 4: "Pass it on?"', 'wobble')
    js = once(js, "    guard('trace', buildTrace);\n", "    guard('trace', buildTrace);\n    guard('wobble', buildWobble);\n", 'guard')
if 'fs-wb-chart' not in css:
    css = css.rstrip('\n') + '\n' + open(os.path.join(here, 'add.css'), encoding='utf-8').read()
open(js_p, 'w', encoding='utf-8', newline='').write(js); open(css_p, 'w', encoding='utf-8', newline='').write(css)
print('layer patched (wobble)')
