// Re-records the VISUALS of a "Start here" screen tour against the current page, timed to the existing narration.
// usage: node tour.js <g4|g5> <pageUrl> <outDir>
const { chromium } = require('playwright');
const fs = require('fs');
const [GRADE, URL, OUT] = process.argv.slice(2);
const sleep = ms => new Promise(r => setTimeout(r, ms));
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const b = await chromium.launch();
  const ctx = await b.newContext({ viewport: { width: 1280, height: 720 }, deviceScaleFactor: 1, recordVideo: { dir: OUT, size: { width: 1280, height: 720 } } });
  const tPage = Date.now();
  const p = await ctx.newPage();
  await p.goto(URL, { waitUntil: 'domcontentloaded' });
  await p.waitForTimeout(5000);
  await p.evaluate(() => {
    const st = document.createElement('style');
    st.textContent = `#tr-cur{position:fixed;left:0;top:0;z-index:2147483647;width:26px;height:26px;pointer-events:none;transition:transform .7s cubic-bezier(.3,.1,.2,1);transform:translate(640px,360px)}
    #tr-cur:before{content:'';position:absolute;left:-12px;top:-12px;width:30px;height:30px;border-radius:50%;background:rgba(245,184,61,.45);border:2px solid #F5B83D}
    #tr-ring{position:fixed;z-index:2147483646;pointer-events:none;border:4px solid #F5B83D;border-radius:14px;box-shadow:0 0 0 4px rgba(245,184,61,.25),0 0 22px rgba(245,184,61,.7);opacity:0;transition:opacity .35s}`;
    document.head.appendChild(st);
    const c = document.createElement('div'); c.id = 'tr-cur';
    c.innerHTML = '<svg width="26" height="26" viewBox="0 0 26 26" style="position:absolute;left:0;top:0"><path d="M3 2 L3 20 L8 15.5 L11.5 23 L14.5 21.6 L11 14.2 L18 14 Z" fill="#fff" stroke="#111" stroke-width="1.6" stroke-linejoin="round"/></svg>';
    const r = document.createElement('div'); r.id = 'tr-ring'; document.body.appendChild(r); document.body.appendChild(c);
    let target = null;
    window.__ring = el => { target = el; r.style.opacity = el ? 1 : 0; };
    (function tick() { if (target) { const q = target.getBoundingClientRect(), pad = 6; r.style.left = (q.left - pad) + 'px'; r.style.top = (q.top - pad) + 'px'; r.style.width = (q.width + pad * 2 - 8) + 'px'; r.style.height = (q.height + pad * 2 - 8) + 'px'; } requestAnimationFrame(tick); })();
    window.__cur = (x, y) => { c.style.transform = 'translate(' + x + 'px,' + y + 'px)'; };
    window.__find = (sel, re) => { const els = [...document.querySelectorAll(sel)].filter(e => e.getClientRects().length); return re ? els.find(e => new RegExp(re, 'i').test((e.innerText || e.textContent || '').trim())) : els[0]; };
    window.__box = (el, minH, maxH) => { let e = el; while (e && e !== document.body) { const h = e.getBoundingClientRect().height; if (h >= minH && h <= maxH) return e; e = e.parentElement; } return el; };
    window.__go = (el, top) => { const y = el.getBoundingClientRect().top + scrollY - (top == null ? 150 : top); window.scrollTo({ top: Math.max(0, y), behavior: 'smooth' }); };
    window.__at = (el, fx, fy) => { const q = el.getBoundingClientRect(); window.__cur(q.left + q.width * (fx == null ? .5 : fx), q.top + q.height * (fy == null ? .5 : fy)); };
  });
  // helpers run in the page: S(selector, textRegex) picks an element; steps are [time, js]
  const run = js => p.evaluate(js).catch(e => console.log('step error', js.slice(0, 60), e.message.split('\n')[0]));
  const G4 = [
    [0.0, `window.scrollTo(0,0); __ring(null); __cur(640,330)`],
    [5.0, `__ring(document.querySelector('.intro-2col')); __at(document.querySelector('.intro-2col'),.2,.3)`],
    [6.5, `{const e=document.querySelector('.intro-2col .theme-earth'); __ring(e); __at(e,.5,.55)}`],
    [8.3, `{const e=document.querySelector('.intro-2col .theme-sky'); __ring(e); __at(e,.4,.5)}`],
    [9.9, `{const e=document.querySelector('.fs-id'); __go(e,260); __ring(e); setTimeout(()=>__at(document.querySelector('.fs-id-in'),.3,.5),700)}`],
    [10.9, `TYPE:.fs-id-in:Maya`],
    [12.3, `{const e=document.querySelector('.fs-id-go'); __at(e); setTimeout(()=>e.click(),450)}`],
    [13.3, `{const e=document.querySelector('.fs-casecard'); __go(e,170); __ring(e); setTimeout(()=>__at(e,.35,.3),600)}`],
    [17.3, `{const e=__box(__find('div,span','^.{0,3}My clues'),30,90); __go(e,300); __ring(e); setTimeout(()=>__at(e,.75,.5),600)}`],
    [22.3, `{const e=document.querySelector('#tabBar'); __go(e,120); __ring(e)}`],
    [23.9, `{const e=document.querySelector('.tab-btn[data-tab="vocab"]'); __ring(e); __at(e)}`],
    [25.0, `{const e=document.querySelector('.tab-btn[data-tab="lesson"]'); __ring(e); __at(e)}`],
    [26.1, `{const e=document.querySelector('.tab-btn[data-tab="quiz"]'); __ring(e); __at(e)}`],
    [27.3, `{const e=document.querySelector('.tab-btn[data-tab="assignment"]'); __ring(e); __at(e)}`],
    [28.4, `{const e=document.querySelector('.tab-btn[data-tab="lesson"]'); __ring(null); __at(e); setTimeout(()=>e.click(),350)}`],
    [29.3, `{const e=document.querySelector('#tab-lesson .fs-play'); __go(e,330); __ring(e); setTimeout(()=>__at(e),650)}`],
    [31.2, `{window.scrollTo({top:0,behavior:'smooth'}); const e=__find('.fs-pill','Read aloud'); __ring(e); setTimeout(()=>__at(e),700)}`],
    [34.3, `{const e=__find('.fs-fab button, .fs-fab > *','^.{0,3}Highlight'); __ring(e); __at(e)}`],
    [36.6, `{const e=__find('.fs-fab button, .fs-fab > *','^.{0,3}Sketch'); __ring(e); __at(e)}`],
    [38.5, `{const e=__find('.fs-fab button, .fs-fab > *','^.{0,3}Snap'); __ring(e); __at(e)}`],
    [41.5, `{const e=document.querySelector('#tab-lesson .fs-game'); __go(e,150); __ring(null); setTimeout(()=>{__ring(e.querySelector('.fs-game-t')||e); __at(e,.3,.2)},700)}`],
    [43.2, `{const e=document.querySelector('#tab-lesson .fs-game'); const t=e.querySelector('.fs-todo, ol, ul')||e; __ring(t); __at(t,.4,.5)}`],
    [46.6, `{const e=document.querySelector('.tab-btn[data-tab="assignment"]'); __ring(null); window.scrollTo({top:Math.max(0,document.querySelector('#tabBar').getBoundingClientRect().top+scrollY-120)}); __at(e); setTimeout(()=>e.click(),300)}`],
    [47.6, `{const e=document.querySelector('.fs-amap'); __go(e,240); __ring(e); setTimeout(()=>__at(e,.3,.7),600)}`],
    [49.7, `{const e=document.querySelector('#tab-assignment .response-textarea'); __go(e,300); __ring(__box(e,60,260)); setTimeout(()=>__at(e,.2,.5),600)}`],
    [50.4, `TYPE:#tab-assignment .response-textarea:Both players slow down`],
    [51.9, `{const e=__find('#tab-assignment div, #tab-assignment p','^.{0,4}Remember CER'); const bx=__box(e,300,720); __go(bx,170); __ring(bx); setTimeout(()=>__at(bx,.3,.3),700)}`],
    [55.7, `{const e=__find('.gathered-card'); __go(e,170); __ring(e); setTimeout(()=>__at(e,.4,.4),700)}`],
    [58.2, `{const e=__box(__find('#tab-assignment div, #tab-assignment h3, #tab-assignment span','^What to Turn In'),160,520); __go(e,170); __ring(e); setTimeout(()=>__at(e,.3,.5),700)}`],
    [60.6, `{const e=document.querySelector('.tab-btn[data-tab="vocab"]'); __ring(null); e.click(); window.scrollTo({top:0,behavior:'smooth'}); setTimeout(()=>{const c=document.querySelector('.fs-casecard'); __go(c,200); __ring(c); __at(c,.35,.3)},900)}`],
  ];
  const steps = GRADE === 'g4' ? G4 : G4;
  await run(steps[0][1]);
  await sleep(600);
  const t0 = Date.now();
  for (const [t, js] of steps) {
    const wait = t0 + t * 1000 - Date.now(); if (wait > 0) await sleep(wait);
    if (js.startsWith('TYPE:')) { const [, sel, text] = js.match(/^TYPE:(.*?):(.*)$/); const el = await p.$(sel); if (el) { await el.focus(); await p.keyboard.type(text, { delay: 55 }); } }
    else await run(js);
  }
  await sleep(t0 + 64200 - Date.now());
  const video = p.video();
  await ctx.close();
  const path = await video.path();
  fs.writeFileSync(OUT + '/meta.json', JSON.stringify({ path, offset: (t0 - tPage) / 1000 }));
  console.log(path, 'offset', (t0 - tPage) / 1000);
  await b.close();
})();
