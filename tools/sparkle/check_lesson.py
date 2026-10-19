#!/usr/bin/env python3
"""Field Station playthrough check (runs in the cloud container, needs Playwright + Chromium).
   python3 tools/sparkle/check_lesson.py 12-02            (run from a clone of optima-4th-science with the new files copied in)
Writes tools/sparkle/out/<WW-LL>/: screenshots of every tab at 1150 and 420 px, text-<tab>.txt (what a student reads),
and report.txt. Exit code 1 if anything failed. LOOK at the screenshots and READ the text files afterwards."""
import sys, os, re, json, glob, threading, http.server, functools, socketserver
from playwright.sync_api import sync_playwright
key = sys.argv[1]
if key.startswith('r'):  # review day r<unit>-<day>
    U, Dn = key[1:].split('-'); page_file = f'review-unit-{U}-day-{Dn}.html'; out = os.path.join('tools', 'sparkle', 'out', key)
else:
    W, L = key.split('-'); W = str(int(W)); WW = W.zfill(2)
    page_file = glob.glob(f'lesson-{W}-{L}-*.html')[0]; out = os.path.join('tools', 'sparkle', 'out', f'{WW}-{L}')
os.makedirs(out, exist_ok=True)
class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
class QuietServer(socketserver.ThreadingTCPServer):
    daemon_threads = True
    def handle_error(self, *a): pass  # browsers drop media requests mid-stream; that's fine
H = functools.partial(Quiet, directory='.')
srv = QuietServer(('127.0.0.1', 0), H); port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
URL = f'http://127.0.0.1:{port}/{page_file}'
TABS = ['vocab', 'lesson', 'explore', 'quiz', 'assignment']
# words a 4th grader may not know: each hit must be defined where students first meet it
JARGON = r'\b(module|scenario|stimul\w*|process(es|ed)?|trigger\w*|organism\w*|specific|vibration|misconception|predator\w*|prey|adapt\w*|function|structure|internal|external|interdepend\w*|migrat\w*|hibernat\w*|metamorphosis|germinat\w*|fertiliz\w*|pollinat\w*|photosynthesis|nonrenewable|renewable|fossil fuel|distribution|availability|invasive|native species|conservation|population|ecosystem|habitat|nutrients?|decompos\w*|consumer|producer|evidence|claim|reasoning|model|annotate|camouflage|trait|inherited|offspring|variation|energy|transfer|collision|friction|gravity|matter|property|properties|magnet\w*|conduct\w*|insulat\w*|circuit|wave|amplitude|wavelength)\b'
fails, notes = [], []
with sync_playwright() as p:
    b = p.chromium.launch()
    for w in (1150, 420):
        pg = b.new_page(viewport={'width': w, 'height': 900}); errs = []
        pg.on('pageerror', lambda e: errs.append(str(e)))
        pg.goto(URL); pg.wait_for_timeout(3500)
        st = pg.evaluate("""()=>({on:document.documentElement.classList.contains('fs-on'), failed:window.FS_SPARKLE_FAILED||[],
            slots:window.FS_SLOTS||[], games:[...document.querySelectorAll('.fs-game')].map(g=>g.dataset.mod),
            sw:document.documentElement.scrollWidth})""")
        if not st['on']: fails.append(f'{w}px: the layer did not turn on')
        if st['failed']: fails.append(f'{w}px: FS_SPARKLE_FAILED {st["failed"]}')
        if st['sw'] > w + 1: fails.append(f'{w}px: page scrolls sideways ({st["sw"]}px wide)')
        if w == 1150: notes.append(f'slots placed: {st["slots"]}'); notes.append(f'games: {st["games"]}')
        for t in TABS:
            if not pg.evaluate(f"!!document.getElementById('tab-{t}')"): continue
            pg.evaluate(f"window.switchTab && switchTab('{t}')"); pg.wait_for_timeout(500)
            pg.screenshot(path=os.path.join(out, f'{t}-{w}.png'), full_page=True)
            if w == 1150:
                txt = pg.evaluate(f"(document.getElementById('tab-{t}')||document.body).innerText")
                open(os.path.join(out, f'text-{t}.txt'), 'w', encoding='utf-8').write(txt)
                hits = sorted({m.group(0).lower() for m in re.finditer(JARGON, txt, re.I)})
                if hits: notes.append(f'{t}: hard words to check are defined where first seen: {", ".join(hits)}')
                for bad in ('notebook', 'Q1', 'Q2', 'Q3', 'Tap to toggle', 'Submission Packet', 'go back', 'previous tab', 'finger'):
                    if re.search(r'\b' + re.escape(bad) + r'\b', txt, re.I): notes.append(f'{t}: says “{bad}”, check it')
        if w == 1150:
            # every answer box ends up in Gathered Answers, in page order
            labels = pg.evaluate("""()=>{const out=[];document.querySelectorAll('textarea.response-textarea[data-label]').forEach((t,i)=>{
                t.value='check answer '+i; t.dispatchEvent(new Event('input',{bubbles:true})); out.push(t.dataset.label);}); window.refreshGathered&&refreshGathered(); return out;}""")
            g = pg.evaluate("(document.getElementById('gatheredOutput')||{}).value||''")
            lost = [l for l in labels if l.upper() not in g.upper()]
            if lost: fails.append(f'answers missing from Gathered Answers: {lost}')
            notes.append(f'{len(labels)} answer boxes feed Gathered Answers')
            # layer off = original page
            pg.evaluate("document.documentElement.classList.remove('fs-on')"); pg.wait_for_timeout(300)
            left = pg.evaluate("[...document.querySelectorAll('[class*=fs-]')].filter(e=>e.offsetParent&&!e.closest('[id=fs-data]')&&getComputedStyle(e).display!=='none').length")
            if left: notes.append(f'layer off: {left} layer elements still visible (check they are meant to be)')
        if errs: fails.append(f'{w}px page errors: {errs[:3]}')
        pg.close()
    b.close()
tw = sum(len(open(os.path.join(out, f), encoding='utf-8').read().split()) for f in os.listdir(out) if f.startswith('text-'))
notes.append(f'words a student reads (all tabs): {tw}' + ('  (OVER the lean budget of about 2,100; trim)' if tw > 2300 else '  (within the lean budget)'))
rep = '\n'.join(['FAIL: ' + f for f in fails] + ['note: ' + n for n in notes]) or 'all good'
open(os.path.join(out, 'report.txt'), 'w', encoding='utf-8').write(rep); print(rep); print('screenshots + text in', out)
srv.shutdown(); sys.exit(1 if fails else 0)
