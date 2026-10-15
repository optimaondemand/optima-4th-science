#!/usr/bin/env python3
"""Field Station sparkle: build ONE lesson in place.   python3 tools/sparkle/build_lesson.py 12-02

Run from the repo root (optima-4th-science). Python 3 standard library only, so it runs on Bethany's computer.

Reads   tools/sparkle/lessons/<WW-LL>/
          data.json    the lesson's fs-data (DATA). "banner" may be omitted when banner.svg exists.
          fixes.json   [{"old","new","why","kind":"fix"|"plain","regex":false}]  applied in order, each must match once
          video.json   optional: {"slots":{slot:{label,length,want,parts,script}}, "pics":{key:{src,cap}}, "other":[]}
          banner.svg   optional: the lesson's banner (goes into DATA.banner)
          original.html  the untouched lesson. Saved automatically the first time (refuses if the file is already sparkled).
Writes  lesson-<W>-<LL>-*.html (in place)  and  data/videos/lesson-<WW>-<LL>.json (when video.json exists)
Every run starts again from original.html, so a rebuild never stacks edits.
"""
import json, re, sys, os, glob, hashlib, shutil

def die(msg): print('STOP:', msg); sys.exit(1)

if len(sys.argv) < 2 or not re.fullmatch(r'\d{1,2}-\d{2}', sys.argv[1]): die('usage: build_lesson.py <WW-LL>, e.g. 12-02')
key = sys.argv[1]; W, L = key.split('-'); W = str(int(W)); WW = W.zfill(2)
here = os.path.join('tools', 'sparkle', 'lessons', f'{WW}-{L}')
if not os.path.isdir(here): die(f'no folder {here}')
cands = glob.glob(f'lesson-{W}-{L}-*.html')
if len(cands) != 1: die(f'expected one lesson-{W}-{L}-*.html in the repo root, found {cands}')
OUT = cands[0]
orig = os.path.join(here, 'original.html')
if not os.path.exists(orig):
    cur = open(OUT, encoding='utf-8').read()
    if 'id="fs-data"' in cur: die('the lesson is already sparkled and there is no original.html; restore it from git history first')
    shutil.copyfile(OUT, orig); print('saved the untouched lesson to', orig)
s = open(orig, encoding='utf-8').read()

# 1. generic repairs every lesson needs (each only when present)
s, n = re.subn(r'(<!-- slot: ' + re.escape(f'{WW}-{L}') + r'-intro -->.*?</div>\s*</div>\s*)</div>(\s*<div class="activity-card act-warmup)', r'\1\2', s, count=1, flags=re.S)
if n: print('repair: removed the stray </div> after the intro-video slot')
if 'raw.githubusercontent.com/bbirchum1/optima-4th-science' in s:
    s = s.replace('raw.githubusercontent.com/bbirchum1/optima-4th-science', 'raw.githubusercontent.com/optimaondemand/optima-4th-science'); print('repair: manifest loader now points at optimaondemand')

# 2. the lesson's own fixes + plain-language edits, in order, each must match exactly once
fx = os.path.join(here, 'fixes.json')
for i, e in enumerate(json.load(open(fx, encoding='utf-8')) if os.path.exists(fx) else []):
    if e.get('regex'):
        m = list(re.finditer(e['old'], s, re.S))
        if len(m) != 1: die(f'fix {i} ({e.get("why","")}): regex matched {len(m)} times')
        s = s[:m[0].start()] + e['new'] + s[m[0].end():]
    else:
        c = s.count(e['old'])
        if c != 1: die(f'fix {i} ({e.get("why","")}): text found {c} times: {e["old"][:80]!r}')
        s = s.replace(e['old'], e['new'])

# 3. DATA + layer links (version-stamped so browsers never run a stale layer)
D = json.load(open(os.path.join(here, 'data.json'), encoding='utf-8'))
bn = os.path.join(here, 'banner.svg')
def clean_svg(t):  # file copies onto her computer can gain a C2PA <metadata> block; strip it
    t = t.replace('\r\n', '\n')
    t = re.sub(r'\s*xmlns:c2pa="[^"]*"', '', t)
    return re.sub(r'<metadata>\s*<c2pa:manifest>.*?</c2pa:manifest>\s*</metadata>', '', t, flags=re.S)
if os.path.exists(bn) and not D.get('banner'): D['banner'] = clean_svg(open(bn, encoding='utf-8').read())
if D.get('banner'): D['banner'] = clean_svg(D['banner'])
for k in ('mockup', 'video', 'art'): D.pop(k, None)
VER = hashlib.sha1(open('assets/sparkle/fs-sparkle.js', 'rb').read() + open('assets/sparkle/fs-sparkle.css', 'rb').read()).hexdigest()[:8]
data = json.dumps(D, ensure_ascii=False, separators=(',', ':')).replace('</', '<\\/')
head = ('<!-- Field Station sparkle layer (G4 Science). Lesson content lives in fs-data; the layer is shared. -->\n'
        '<script type="application/json" id="fs-data">' + data + '</script>\n'
        '<link rel="stylesheet" href="assets/sparkle/fs-sparkle.css?v=' + VER + '">\n')
if s.count('</head>') != 1 or s.count('</body>') != 1: die('lesson needs exactly one </head> and one </body>')
s = s.replace('</head>', head + '</head>', 1)
s = s.replace('</body>', '<script src="assets/sparkle/fs-sparkle.js?v=' + VER + '"></script>\n</body>', 1)
open(OUT, 'w', encoding='utf-8', newline='').write(s)

# 4. the Video Studio plan
vj = os.path.join(here, 'video.json')
if os.path.exists(vj):
    V = json.load(open(vj, encoding='utf-8'))
    V['other'] = [{'id': k, 'label': ((D.get('slots') or {}).get(k) or {}).get('label', k), 'length': ((D.get('slots') or {}).get(k) or {}).get('length', '')} for k in V.get('other', [])]
    os.makedirs(os.path.join('data', 'videos'), exist_ok=True)
    V['redo'] = list(D.get('videoOff') or [])  # recorded takes that no longer match the page: the studio lists them as Re-record
    json.dump({'lesson': D['lesson'], 'prefix': D['prefix'], 'manifestKey': D['manifestKey'], 'guide': D['guide'], **V},
              open(os.path.join('data', 'videos', f'lesson-{WW}-{L}.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('wrote', os.path.join('data', 'videos', f'lesson-{WW}-{L}.json'))
print('built', OUT, 'layer v=' + VER, 'divs', s.count('<div'), '/', s.count('</div>'))
if s.count('<div') != s.count('</div>'): print('WARNING: <div> and </div> counts differ; check the page structure')
