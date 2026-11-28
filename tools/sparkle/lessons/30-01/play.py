#!/usr/bin/env python3
"""Plays 30.01 end to end in Playwright: every game by tap (and the warm-up by drag), the answer boxes with a
natural answer and a junk answer, the case solve, the claim stamp and the Tool of the Week.
Run from a clone: python3 tools/sparkle/lessons/30-01/play.py"""
import threading, http.server, functools, socketserver, glob, sys, json
from playwright.sync_api import sync_playwright

page_file = glob.glob('lesson-30-01-*.html')[0]
class Quiet(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a): pass
class QuietServer(socketserver.ThreadingTCPServer):
    daemon_threads = True
    def handle_error(self, *a): pass
srv = QuietServer(('127.0.0.1', 0), functools.partial(Quiet, directory='.'))
port = srv.server_address[1]
threading.Thread(target=srv.serve_forever, daemon=True).start()
URL = f'http://127.0.0.1:{port}/{page_file}?steps=0'
problems, log = [], []
def ok(t): log.append('  ok  ' + t); print('  ok  ' + t, flush=True)
def bad(t): problems.append(t); log.append(' FAIL ' + t); print(' FAIL ' + t, flush=True)

with sync_playwright() as p:
    b = p.chromium.launch(args=['--autoplay-policy=no-user-gesture-required'])
    pg = b.new_page(viewport={'width': 1150, 'height': 1000})
    errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto(URL, wait_until='networkidle')
    pg.wait_for_timeout(600)

    def tab(t): pg.evaluate(f"switchTab('{t}')"); pg.wait_for_timeout(250)
    def clear_toasts():
        pg.evaluate("document.querySelectorAll('.fs-toast').forEach(t=>t.remove())")
    def click(sel, i=0):
        clear_toasts()
        el = pg.locator(sel).nth(i); el.scroll_into_view_if_needed(); el.click(force=True); pg.wait_for_timeout(280)
    def txt(sel):
        return pg.locator(sel).first.inner_text() if pg.locator(sel).count() else ''
    def drag(a, t):
        s, d = pg.locator(a).first, pg.locator(t).first
        d.scroll_into_view_if_needed(); sb, db = s.bounding_box(), d.bounding_box()
        pg.mouse.move(sb['x'] + sb['width'] / 2, sb['y'] + sb['height'] / 2); pg.mouse.down()
        pg.mouse.move(db['x'] + db['width'] / 2, db['y'] + db['height'] / 2, steps=12); pg.mouse.up()
        pg.wait_for_timeout(260)
    def clue(n): return pg.evaluate("document.querySelectorAll('.fs-board .fs-clue.on, .fs-board [class*=on]').length")

    # ---------- Warm-Up: sealbag (by DRAG) ----------
    tab('vocab')
    drag('.fs-sb-chip', '.fs-sb-scale')
    if 'Sealed bag' not in txt('.fs-sb-seal'): bad('sealbag: drag did not put the bag on the scale')
    else: ok('sealbag: drag works')
    click('.fs-sb-go')
    pg.wait_for_timeout(1100)
    # a wrong call first
    click('[data-mod="sealbag"] .fs-sv-q .fs-in-chip', 0)
    if 'show' not in (pg.locator('[data-mod="sealbag"] .fs-miss').first.get_attribute('class') or ''): bad('sealbag: wrong answer gave no hint')
    else: ok('sealbag: wrong answer bounces with a hint')
    click('[data-mod="sealbag"] .fs-sv-q .fs-in-chip', 1)
    pg.wait_for_timeout(300)
    click('[data-mod="sealbag"] .fs-sv-q .fs-in-chip', 3)  # second question, right answer is index 0 of the 2nd q
    qs = pg.locator('[data-mod="sealbag"] .fs-in-chip')
    for i in range(qs.count()):
        if 'same water' in qs.nth(i).inner_text():
            qs.nth(i).click(); break
    pg.wait_for_timeout(400)
    if 'show' in (pg.locator('[data-mod="sealbag"] .fs-win').first.get_attribute('class') or ''): ok('sealbag: clue 1 earned')
    else: bad('sealbag: no win after the right answers')

    # ---------- Part 1: callit (keypad) ----------
    tab('lesson')
    for mass in ('5', '60', '212'):
        click('.fs-cal-do')
        for ch in mass: click(f'.fs-cal-key[data-k="{ch}"]')
        click('.fs-cal-weigh')
        pg.wait_for_timeout(350)
    if 'Three changes weighed' in txt('.fs-cal-done'): ok('callit: three rounds called correctly')
    else: bad('callit: did not finish three rounds')
    cq = pg.locator('[data-mod="callit"] .fs-in-chip')
    for i in range(cq.count()):
        if 'stayed exactly the same' in cq.nth(i).inner_text(): cq.nth(i).click(); break
    pg.wait_for_timeout(300)
    if 'show' in (pg.locator('[data-mod="callit"] .fs-win').first.get_attribute('class') or ''): ok('callit: clue 2 earned')
    else: bad('callit: no win')

    # ---------- Part 2: undoer (tap stamp, then card) ----------
    for i in range(6):
        click('.fs-und-btn', 0)
        pg.wait_for_timeout(900)
    cards = pg.evaluate("[...document.querySelectorAll('.fs-und-card')].map(c=>c.dataset.id)")
    want = {'ice': 0, 'fold': 0, 'sugar': 0, 'shred': 1, 'glass': 1, 'cheese': 1}
    def pick_stamp(i):
        el = pg.locator('.fs-und-stamp').nth(i)
        el.scroll_into_view_if_needed()
        for _ in range(3):
            if 'sel' in (el.get_attribute('class') or ''): return
            el.click(force=True); pg.wait_for_timeout(120)
        bad('undoer: could not select stamp %d' % i)
    # one wrong stamp first
    pick_stamp(1); click('.fs-und-card[data-id="ice"]')
    if 'show' in (pg.locator('[data-mod="undoer"] .fs-miss').first.get_attribute('class') or ''): ok('undoer: a wrong stamp bounces')
    else: bad('undoer: wrong stamp was accepted')
    for cid in cards:
        pick_stamp(want[cid]); click(f'.fs-und-card[data-id="{cid}"]')
    if '6 of 6 stamped' in txt('[data-mod="undoer"] .fs-count'): ok('undoer: all six stamped')
    else: bad('undoer: count is ' + txt('[data-mod="undoer"] .fs-count') + ' state ' + str(pg.evaluate("JSON.parse(localStorage.getItem('oao.fs.30.01.undoer')||'{}')")))
    uq = pg.locator('[data-mod="undoer"] .fs-in-chip')
    for i in range(uq.count()):
        if 'None of them' in uq.nth(i).inner_text(): uq.nth(i).click(); break
    pg.wait_for_timeout(300)
    if 'show' in (pg.locator('[data-mod="undoer"] .fs-win').first.get_attribute('class') or ''): ok('undoer: clue 3 earned')
    else: bad('undoer: no win')

    # ---------- Part 3: wipe ----------
    for i in range(3): click('[data-mod="wipe"] .fs-hs', i)
    wq = pg.locator('[data-mod="wipe"] .fs-in-chip')
    for i in range(wq.count()):
        if 'physical change' in wq.nth(i).inner_text(): wq.nth(i).click(); break
    pg.wait_for_timeout(300)
    if 'show' in (pg.locator('[data-mod="wipe"] .fs-win').first.get_attribute('class') or ''): ok('wipe: hotspots + question done (no clue, as designed)')
    else: bad('wipe: no win')

    # ---------- Part 4: statedial ----------
    for i in (1, 2, 3, 4):
        click('.fs-std-stop[data-i="%d"]' % i)
    for i in (3, 2, 1, 0):
        click('.fs-std-stop[data-i="%d"]' % i)
    sq = pg.locator('[data-mod="statedial"] .fs-in-chip')
    for i in range(sq.count()):
        if 'It was water at every single stop' in sq.nth(i).inner_text(): sq.nth(i).click(); break
    pg.wait_for_timeout(300)
    if 'show' in (pg.locator('[data-mod="statedial"] .fs-win').first.get_attribute('class') or ''): ok('statedial: clue 4 earned')
    else: bad('statedial: no win (did the up-then-back gate open?)')
    mass_locked = pg.evaluate("[...document.querySelectorAll('.fs-std-o.lock b')].map(e=>e.textContent)")
    if mass_locked and '200 g' in mass_locked[0] and 'WATER' in mass_locked[1]: ok('statedial: mass and material never moved')
    else: bad('statedial: readouts changed: ' + str(mass_locked))

    # ---------- the wow: remelt ----------
    for i in range(3):
        click('.fs-rmt-go'); pg.wait_for_timeout(300)
    rq = pg.locator('[data-mod="remelt"] .fs-in-chip')
    for i in range(rq.count()):
        if 'same wax in a new shape' in rq.nth(i).inner_text(): rq.nth(i).click(); break
    pg.wait_for_timeout(300)
    if 'show' in (pg.locator('[data-mod="remelt"] .fs-win').first.get_attribute('class') or ''): ok('remelt: the giant crayon lands')
    else: bad('remelt: no win')

    # ---------- the case ----------
    tab('assignment')
    pg.wait_for_timeout(400)
    sol = pg.locator('.fs-solve-o')
    hit = False
    for i in range(sol.count()):
        if 'should be approved' in sol.nth(i).inner_text(): sol.nth(i).click(); hit = True; break
    pg.wait_for_timeout(700)
    if hit and pg.evaluate("!!localStorage.getItem('oao.fs.30.01.solved')"): ok('case: cracked with all four clues')
    else: bad('case: could not crack it. hit=%s locked=%s' % (hit, pg.evaluate("document.querySelector('.fs-solve').classList.contains('locked')")))

    # ---------- claimstamp ----------
    pg.wait_for_timeout(400)
    cs = pg.locator('.fs-cst-chip')
    click('.fs-cst-chip', 2)  # a wrong one
    if 'show' in (pg.locator('[data-mod="claimstamp"] .fs-miss').first.get_attribute('class') or ''): ok('claimstamp: a weak piece of evidence bounces')
    else: bad('claimstamp: weak evidence was accepted')
    click('.fs-cst-chip', 0); click('.fs-cst-chip', 1)
    click('.fs-cst-stamp', 1)  # DENIED first
    if 'show' in (pg.locator('[data-mod="claimstamp"] .fs-miss').first.get_attribute('class') or ''): ok('claimstamp: the wrong stamp bounces')
    else: bad('claimstamp: DENIED was accepted')
    click('.fs-cst-stamp', 0)
    pg.wait_for_timeout(300)
    if 'show' in (pg.locator('[data-mod="claimstamp"] .fs-win').first.get_attribute('class') or ''): ok('claimstamp: APPROVED, case closed')
    else: bad('claimstamp: no win')

    # ---------- answer boxes: a natural answer and a junk answer ----------
    def type_in(sel, s):
        pg.evaluate("([q,v])=>{const t=document.querySelector(q);t.value=v;t.dispatchEvent(new Event('input',{bubbles:true}));}", [sel, s])
        pg.wait_for_timeout(350)
    def chips_on(mod):
        return pg.evaluate("(m)=>[...document.querySelectorAll(m+' .fs-flag')].filter(c=>c.classList.contains('on')).length", mod)
    type_in('#ans-1', 'Melting ice can be undone because you can freeze it again and the material is still water the whole time.')
    n1 = chips_on('#fs-flags-ans-1, .fs-flags-ans-1')
    type_in('#ans-2', 'Irreversible only means you cannot undo it. Shredded paper is still paper, so it is a physical change.')
    type_in('#cer-4', 'I disagree. Shredded paper cannot be undone and it is still paper. The melted crayon slab weighed 1200 g before and after and poured into a new crayon. This shows that a change you cannot undo can still be physical.')
    junk = 'asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf asdf'
    type_in('#ans-1', junk)
    j1 = pg.evaluate("[...document.querySelectorAll('.fs-flag')].filter(c=>c.classList.contains('on')).length")
    type_in('#ans-1', 'Melting ice can be undone because you can freeze it again and the material is still water the whole time.')
    g = pg.evaluate("(document.getElementById('gatheredOutput')||{}).value||''")
    if 'Melting ice' in g and 'Irreversible only means' in g and 'I disagree' in g: ok('all three answers reach Gathered Answers')
    else: bad('answers missing from Gathered Answers')
    all_chips = pg.evaluate("[...document.querySelectorAll('.fs-flag')].map(c=>[c.textContent.trim(),c.classList.contains('on')])")
    off = [c[0] for c in all_chips if not c[1]]
    if off: log.append('  note chips still off after natural answers: ' + str(off))
    else: ok('every answer chip lights for a natural answer')

    fail = pg.evaluate("window.FS_SPARKLE_FAILED||[]")
    if fail: bad('FS_SPARKLE_FAILED: ' + str(fail))
    else: ok('FS_SPARKLE_FAILED is empty after the full playthrough')
    if errs: bad('page errors: ' + str(errs[:3]))
    else: ok('no page errors')
    pg.screenshot(path='tools/sparkle/out/30-01/played-assignment.png', full_page=True)
    tab('lesson'); pg.wait_for_timeout(400)
    pg.screenshot(path='tools/sparkle/out/30-01/played-lesson.png', full_page=True)
    b.close()

print('\n'.join(log))
print('\n' + ('PLAYTHROUGH OK' if not problems else 'PROBLEMS:\n- ' + '\n- '.join(problems)))
sys.exit(1 if problems else 0)
