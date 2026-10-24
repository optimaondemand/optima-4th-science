/* ===== Field Station sparkle layer — G4 Science (mockup v1) =====
   Holds NO lesson content. Everything lesson-specific comes from
   <script type="application/json" id="fs-data"> in the lesson's <head>.
   Every key is optional; a missing key costs only its own feature.       */
(function () {
  'use strict';
  var dataEl = document.getElementById('fs-data');
  var D = {};
  try { D = JSON.parse(dataEl ? dataEl.textContent : '{}'); } catch (e) { console.warn('fs-data unreadable', e); }
  var html = document.documentElement;
  var FAILED = window.FS_SPARKLE_FAILED = [];
  var REVIEW = /[?&]review\b/.test(location.search) || !!D.mockup;
  var reduceMotion = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  html.classList.add('fs-on');

  /* ---------- helpers ---------- */
  function $(s, r) { return (r || document).querySelector(s); }
  function $$(s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); }
  function el(tag, cls, inner) { var e = document.createElement(tag); if (cls) e.className = cls; if (inner != null) e.innerHTML = inner; return e; }
  function esc(t) { return String(t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function fsOnly(e) { e.classList.add('fs-only'); return e; }
  function guard(name, fn) { try { fn(); } catch (e) { FAILED.push(name + ': ' + e.message); console.error('[fs]', name, e); } }
  function crewOf(id) { var k = id || D.guide, c = (D.crew && D.crew[k]) || { name: 'Field Station', role: '' }; if (!c.id) c.id = k; return c; }
  function store(k, v) { try { if (v === undefined) return localStorage.getItem('oao.fs.' + D.lesson + '.' + k); localStorage.setItem('oao.fs.' + D.lesson + '.' + k, v); } catch (e) { return null; } }
  function shuffle(a) { a = a.slice(); for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(Math.random() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; } return a; }

  /* ---------- notifications: one stack at the bottom; a new one pushes older ones up ---------- */
  /* captions: a big, easy "Captions" button under each teacher video (the .vtt the Video Studio saves).
     Off by default; a student's choice is remembered for every video. Hidden if the lesson has no .vtt. */
  function capsOn() { try { return localStorage.getItem('oao.fs.captions') === '1'; } catch (e) { return false; } }
  function addCaptions(wrap) {
    var vid = wrap.querySelector('video'), tr = wrap.querySelector('track'); if (!vid || !tr) return;
    var btn = el('button', 'fs-cc', '<span class="fs-cc-i">CC</span> <span class="fs-cc-t">Captions: off</span>'); btn.type = 'button';
    btn.setAttribute('aria-pressed', 'false'); btn.style.display = 'none'; wrap.appendChild(btn);
    function apply(on) {
      var t = vid.textTracks && vid.textTracks[0]; if (t) t.mode = on ? 'showing' : 'hidden';
      btn.classList.toggle('on', on); btn.setAttribute('aria-pressed', on ? 'true' : 'false');
      $('.fs-cc-t', btn).textContent = on ? 'Captions: on' : 'Captions: off';
    }
    function ready(ok) { if (!ok) { tr.remove(); return; } btn.style.display = ''; apply(capsOn()); }
    try { fetch(tr.getAttribute('src'), { method: 'HEAD', cache: 'no-store' }).then(function (r) { ready(r.ok); }, function () { ready(false); }); } catch (e) { ready(false); }
    tr.addEventListener('load', function () { apply(capsOn()); });
    btn.addEventListener('click', function () {
      var on = !btn.classList.contains('on'); try { localStorage.setItem('oao.fs.captions', on ? '1' : '0'); } catch (e) {}
      Array.prototype.forEach.call(document.querySelectorAll('.fs-video'), function (w) { var b = w.querySelector('.fs-cc'); if (b && b !== btn && b.style.display !== 'none') b.__set && b.__set(on); });
      apply(on);
    });
    btn.__set = apply;
  }
  function pushToast(icon, title, text, ms) {
    var st = $('#fsToasts'); if (!st) { st = fsOnly(el('div', 'fs-toasts')); st.id = 'fsToasts'; st.setAttribute('aria-live', 'polite'); document.body.appendChild(st); }
    /* notes stay until the student closes them (some kids read slower); at most 3 at once, oldest closes first */
    var t = el('div', 'fs-toast', '<span>' + icon + '</span><div><b>' + esc(title) + '</b>' + esc(text) + '</div><button type="button" class="fs-toast-x" aria-label="Close this note">✕</button>');
    function close() { t.classList.remove('show'); t.classList.add('leave'); setTimeout(function () { t.remove(); }, 450); }
    $('.fs-toast-x', t).addEventListener('click', close);
    st.appendChild(t);
    var open = $$('.fs-toast:not(.leave)', st); if (open.length > 3) open[0].querySelector('.fs-toast-x').click();
    setTimeout(function () { t.classList.add('show'); SFX.win(); }, 30);
  }
  /* ---------- sound (WebAudio, generated, quiet, never on load) ---------- */
  var AC = null;
  function ac() { if (!AC) { try { AC = new (window.AudioContext || window.webkitAudioContext)(); } catch (e) { AC = null; } } return AC; }
  function tone(freq, t0, dur, type, vol) {
    var c = ac(); if (!c) return; var o = c.createOscillator(), g = c.createGain();
    o.type = type || 'sine'; o.frequency.value = freq; g.gain.setValueAtTime(0.0001, c.currentTime + t0);
    g.gain.exponentialRampToValueAtTime(vol || 0.08, c.currentTime + t0 + 0.015);
    g.gain.exponentialRampToValueAtTime(0.0001, c.currentTime + t0 + dur);
    o.connect(g); g.connect(c.destination); o.start(c.currentTime + t0); o.stop(c.currentTime + t0 + dur + 0.05);
  }
  function noise(dur, lo, hi, vol) {
    var c = ac(); if (!c) return; var n = Math.floor(c.sampleRate * dur), b = c.createBuffer(1, n, c.sampleRate), d = b.getChannelData(0);
    for (var i = 0; i < n; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / n, 3);
    var s = c.createBufferSource(); s.buffer = b; var f = c.createBiquadFilter(); f.type = 'bandpass'; f.frequency.value = (lo + hi) / 2; f.Q.value = 0.8;
    var g = c.createGain(); g.gain.value = vol || 0.4; s.connect(f); f.connect(g); g.connect(c.destination); s.start();
  }
  /* radio static with a flat body and a hard cut, like a squelch tail (not a soft crackle) */
  function squelch(t0, dur, vol) {
    var c = ac(); if (!c) return; var n = Math.floor(c.sampleRate * dur), b = c.createBuffer(1, n, c.sampleRate), d = b.getChannelData(0);
    for (var i = 0; i < n; i++) d[i] = (Math.random() * 2 - 1) * (i < n * 0.08 ? i / (n * 0.08) : 1);
    var s = c.createBufferSource(); s.buffer = b;
    var hp = c.createBiquadFilter(); hp.type = 'highpass'; hp.frequency.value = 900;
    var lp = c.createBiquadFilter(); lp.type = 'lowpass'; lp.frequency.value = 3400;
    var g = c.createGain(); g.gain.value = vol || 0.2;
    s.connect(hp); hp.connect(lp); lp.connect(g); g.connect(c.destination); s.start(c.currentTime + (t0 || 0));
  }
  var SFX = {
    snap: function () { noise(0.09, 1800, 4200, 0.9); setTimeout(function () { noise(0.05, 900, 2400, 0.5); }, 40); },
    chime: function () { tone(880, 0, 0.35, 'sine', 0.06); tone(1320, 0.09, 0.4, 'sine', 0.05); },
    win: function () { [660, 880, 990, 1320].forEach(function (f, i) { tone(f, i * 0.09, 0.4, 'triangle', 0.05); }); },
    thud: function () { tone(110, 0, 0.18, 'sine', 0.12); },
    blip: function () { tone(1500, 0, 0.08, 'square', 0.025); },
    crackle: function () { noise(0.18, 600, 2600, 0.12); },
    /* walkie-talkie: a burst of squelch static, then the two-tone key-up chirp */
    keyup: function () { squelch(0, 0.16, 0.22); tone(1046, 0.15, 0.07, 'square', 0.035); tone(1568, 0.22, 0.09, 'square', 0.035); },
    /* the "roger beep" when she lets go of the button, with a short static tail */
    roger: function () { tone(1318, 0, 0.11, 'square', 0.035); squelch(0.12, 0.12, 0.16); },
    stamp: function () { tone(70, 0, 0.25, 'sine', 0.2); noise(0.06, 300, 900, 0.3); },
    whoosh: function () { var c = ac(); if (!c) return; var o = c.createOscillator(), g = c.createGain(); o.type = 'sine'; o.frequency.setValueAtTime(220, c.currentTime); o.frequency.exponentialRampToValueAtTime(1300, c.currentTime + 0.28);
      g.gain.setValueAtTime(0.0001, c.currentTime); g.gain.exponentialRampToValueAtTime(0.05, c.currentTime + 0.1); g.gain.exponentialRampToValueAtTime(0.0001, c.currentTime + 0.3); o.connect(g); g.connect(c.destination); o.start(); o.stop(c.currentTime + 0.32); noise(0.25, 1500, 5000, 0.08); },
    pop: function () { tone(520, 0, 0.09, 'square', 0.04); noise(0.05, 800, 2400, 0.5); },
    sparkle: function () { [1568, 2093, 2637, 3136, 2637].forEach(function (f, i) { tone(f, i * 0.06, 0.25, 'sine', 0.025); }); }
  };

  /* ---------- drag + tap (both always work) ---------- */
  function dragDrop(item, getTargets, onDrop) {
    var start = null, ghost = null, moved = false;
    item.addEventListener('pointerdown', function (e) {
      if (item.classList.contains('placed')) return;
      start = { x: e.clientX, y: e.clientY }; moved = false;
      item.setPointerCapture && item.setPointerCapture(e.pointerId);
    });
    item.addEventListener('pointermove', function (e) {
      if (!start) return;
      if (!moved && Math.abs(e.clientX - start.x) + Math.abs(e.clientY - start.y) > 8) {
        moved = true; ghost = item.cloneNode(true); ghost.classList.add('ghost'); ghost.style.width = item.offsetWidth + 'px'; document.body.appendChild(ghost);
      }
      if (moved && ghost) {
        ghost.style.left = (e.clientX - ghost.offsetWidth / 2) + 'px'; ghost.style.top = (e.clientY - ghost.offsetHeight / 2) + 'px';
        getTargets().forEach(function (t) { var r = t.getBoundingClientRect(); t.classList.toggle('over', e.clientX > r.left && e.clientX < r.right && e.clientY > r.top && e.clientY < r.bottom); });
      }
    });
    function end(e) {
      if (!start) return; var wasMoved = moved; start = null;
      if (ghost) { ghost.remove(); ghost = null; }
      var hit = null;
      getTargets().forEach(function (t) { var r = t.getBoundingClientRect(); if (e.clientX > r.left && e.clientX < r.right && e.clientY > r.top && e.clientY < r.bottom) hit = t; t.classList.remove('over'); });
      if (wasMoved) { if (hit) onDrop(item, hit); }
      else {
        var on = !item.classList.contains('sel');
        $$('.sel', item.parentNode.closest('.fs-game') || document).forEach(function (s) { s.classList.remove('sel'); });
        if (on) { item.classList.add('sel'); SFX.blip(); }
      }
    }
    item.addEventListener('pointerup', end);
    item.addEventListener('pointercancel', function () { start = null; if (ghost) { ghost.remove(); ghost = null; } });
  }
  function tapTargets(game, targets, onDrop) {
    targets.forEach(function (t) {
      t.addEventListener('click', function () { var s = $('.sel', game); if (s) { s.classList.remove('sel'); onDrop(s, t); } });
    });
  }
  function bounce(item, missBox, text) {
    item.classList.remove('bounce'); void item.offsetWidth; item.classList.add('bounce'); SFX.thud();
    if (missBox && text) { missBox.innerHTML = '🔎 ' + esc(text); missBox.classList.remove('show'); void missBox.offsetWidth; missBox.classList.add('show'); }
  }

  /* ---------- shells ---------- */
  function gameShell(kicker, title, todo, why) {
    var g = fsOnly(el('div', 'fs-game'));
    g.appendChild(el('div', 'fs-game-k', esc(kicker)));
    g.appendChild(el('div', 'fs-game-t', esc(title)));
    if (why) g.appendChild(whyCard(why));
    if (todo && todo.length) { var ul = el('ul', 'fs-todo'); todo.forEach(function (t) { ul.appendChild(el('li', '', t)); }); g.appendChild(ul); }
    return g;
  }
  function whyCard(w) { return el('div', 'fs-why fs-kraft', '<span class="fs-why-ic">' + (w.icon || '🌿') + '</span><div><b>' + esc(w.q) + '</b>' + esc(w.t) + '</div>'); }

  /* =================== v7: crew portraits =================== */
  function avatar(who, cls) {
    var a = el('div', 'fs-av ' + (cls || ''));
    a.style.setProperty('--avc', who.color || '#2F5D3A');
    var ini = who.initials || who.name.replace(/^Dr\.\s*/, '').split(/\s+/).map(function (w) { return w[0]; }).join('').slice(0, 2);
    a.innerHTML = '<span class="fs-av-ini">' + esc(ini) + '</span>';
    var src = who.portrait || ((D.paths && D.paths.crew || 'assets/crew/') + (who.id || D.guide) + '.png');
    var img = new Image(); img.alt = who.name; img.className = 'fs-av-img';
    img.onload = function () { a.classList.add('has-img'); a.appendChild(img); };
    img.src = src;
    return a;
  }

  /* =================== v6: the walkie-talkie comes alive =================== */
  var WALKIE = '<svg class="fs-wt" viewBox="0 0 84 136" aria-hidden="true">' +
    '<g class="fs-waves" fill="none" stroke="#F5B83D" stroke-width="3" stroke-linecap="round"><path class="w1" d="M70 8 a8 8 0 0 1 0 14"/><path class="w2" d="M74 2 a15 15 0 0 1 0 26"/><path class="w3" d="M78 -4 a22 22 0 0 1 0 38"/></g>' +
    '<rect x="54" y="4" width="9" height="40" rx="4" fill="#1E2618"/><rect x="8" y="34" width="66" height="98" rx="14" fill="#47563A"/><rect x="8" y="34" width="66" height="98" rx="14" fill="none" stroke="#2C3622" stroke-width="3"/>' +
    '<rect x="2" y="60" width="8" height="26" rx="3" class="fs-ptt" fill="#2C3622"/>' +
    '<circle cx="20" cy="44" r="4" class="fs-led" fill="#5B6B4C"/><circle cx="62" cy="44" r="5" fill="#2C3622"/>' +
    '<rect x="16" y="52" width="50" height="26" rx="4" fill="#B9E3A6" stroke="#1E2618" stroke-width="2"/>' +
    '<g class="fs-bars" fill="#24451C"><rect x="21" y="70" width="4" height="4"/><rect x="27" y="70" width="4" height="4"/><rect x="33" y="70" width="4" height="4"/><rect x="39" y="70" width="4" height="4"/><rect x="45" y="70" width="4" height="4"/><rect x="51" y="70" width="4" height="4"/><rect x="57" y="70" width="4" height="4"/></g>' +
    '<g class="fs-grille"><circle cx="41" cy="106" r="17" fill="#2C3622"/><g fill="#47563A"><circle cx="35" cy="100" r="2"/><circle cx="41" cy="100" r="2"/><circle cx="47" cy="100" r="2"/><circle cx="35" cy="106" r="2"/><circle cx="41" cy="106" r="2"/><circle cx="47" cy="106" r="2"/><circle cx="35" cy="112" r="2"/><circle cx="41" cy="112" r="2"/><circle cx="47" cy="112" r="2"/></g></g></svg>';
  /* ---------- Spotlight: page parts light up, pop, point and reveal exactly when the crew voice names them (PowerPoint-style) ----------
     D.cues = { <slot>: [ {at: 'regex for the spoken word (first match after the previous cue)', sel: 'CSS selector', fx: 'glow'|'pop'|'point'|'reveal'|'wiggle'|'trace',
                           tag: 'optional short label shown on the part', scroll: true (bring it on screen if it is off screen), all: true (every match, not just the first)} ] }
     D.cueWords = { <slot>: [[start, end, 'word'], …] } (optional: word times from a transcription of the clip; without them the layer estimates from the clip length)
     Works for the real clip and the teacher's ▶ Demo (computer voice). Everything is off under reduced motion except a static highlight. */
  function cueRunner(id, script) {
    var C = (D.cues || {})[id]; if (!C || !C.length) return null;
    var toks = String(script || '').split(/\s+/).filter(Boolean);
    var from = 0, beats = [];
    C.forEach(function (c) {
      var re = new RegExp(c.at, 'i'), k = from;
      while (k < toks.length && !re.test(toks[k].replace(/^[^\w’']+|[^\w’']+$/g, ''))) k++;
      if (k >= toks.length) { FAILED.push('cue "' + c.at + '" not found in the ' + id + ' script'); return; }
      beats.push({ c: c, k: k }); from = k + 1;
    });
    var W = (D.cueWords || {})[id], fired = -1, live = [], timers = [];
    /* with a transcript: find each cue word in the transcript itself (same order), so the timing is exact */
    if (W && W.length) { var wf = 0; beats.forEach(function (b) { var re = new RegExp(b.c.at, 'i'), j = wf; while (j < W.length && !re.test(String(W[j][2]).replace(/^[^\w’']+|[^\w’']+$/g, ''))) j++; if (j < W.length) { b.t = W[j][0]; wf = j + 1; } }); }
    function els(c) { var a = $$(c.sel); if (c.i != null) return a[c.i] ? [a[c.i]] : []; return c.all ? a : a.slice(0, 1); }
    function timeOf(k, dur) {
      if (W && W.length) { var j = Math.min(W.length - 1, Math.round(k * W.length / Math.max(1, toks.length))); return W[j][0]; }
      var wt = function (t) { return t.length + 2 + (/[.!?]$/.test(t) ? 7 : /[,;:]$/.test(t) ? 3 : 0); };
      var tot = toks.reduce(function (n, t) { return n + wt(t); }, 0), before = 0;
      for (var i = 0; i < k; i++) before += wt(toks[i]);
      return Math.max(0, before / tot * (dur || 30) - 0.15);
    }
    function clearNow() { live.forEach(function (e) { e.classList.remove('fs-cue-now', 'fs-cue-pop', 'fs-cue-wiggle', 'fs-cue-point', 'fs-cue-trace'); var t = $('.fs-cue-tag', e); if (t) t.remove(); }); live = []; }
    function fire(i) {
      var b = beats[i]; if (!b) return; clearNow();
      els(b.c).forEach(function (e) {
        e.classList.remove('fs-cue-wait'); e.classList.add('fs-cue-lit', 'fs-cue-now');
        var fx = b.c.fx || 'glow'; if (fx !== 'glow' && fx !== 'reveal' && !reduceMotion) { void e.offsetWidth; e.classList.add('fs-cue-' + fx); }
        if ((b.c.tag || b.c.fx === 'point') && getComputedStyle(e).position === 'static') e.classList.add('fs-cue-rel');
        if (b.c.tag) { var t = el('span', 'fs-cue-tag', esc(b.c.tag)); t.setAttribute('aria-hidden', 'true'); e.appendChild(t); }
        if (b.c.scroll) { var r = e.getBoundingClientRect(); if (r.bottom < 60 || r.top > innerHeight - 60) e.scrollIntoView({ block: 'center', behavior: reduceMotion ? 'auto' : 'smooth' }); }
        live.push(e);
      });
    }
    return {
      start: function () { fired = -1; beats.forEach(function (b) { if ((b.c.fx || '') === 'reveal') els(b.c).forEach(function (e) { if (!e.classList.contains('fs-cue-lit')) e.classList.add('fs-cue-wait'); }); }); document.documentElement.classList.add('fs-cueing'); },
      atTime: function (t, dur) { var n = -1; beats.forEach(function (b, i) { if (t >= (b.t != null ? b.t - 0.1 : timeOf(b.k, dur))) n = i; }); while (fired < n) { fired++; fire(fired); } },
      atWord: function (k) { var n = -1; beats.forEach(function (b, i) { if (k >= b.k) n = i; }); while (fired < n) { fired++; fire(fired); } },
      stop: function (done) {
        document.documentElement.classList.remove('fs-cueing');
        $$('.fs-cue-wait').forEach(function (e) { e.classList.remove('fs-cue-wait'); });
        timers.push(setTimeout(clearNow, done ? 1600 : 0));
      }
    };
  }

  function makeRadio(info, who, src, demo, slotId) {
    var cue = cueRunner(slotId, info.script);
    var words = String(info.script || '').split(/(\s+)/);
    var row = el('div', 'fs-radio fs-radio2' + (demo ? ' demo' : ''));
    row.innerHTML = '<div class="fs-radio-dev"><div class="fs-av-slot"></div>' + WALKIE + '</div><div class="fs-radio-body">' +
      '<div class="fs-radio-who">📻 ' + esc(who.name) + (demo ? ' <span class="fs-pending">demo: computer voice</span>' : '') + '</div>' +
      '<div class="fs-radio-label">' + esc(info.label || '') + '</div>' +
      '<div class="fs-radio-ctl"><button class="fs-play" type="button">▶ ' + esc(info.audioLabel || 'Listen') + '</button><button class="fs-readalong" type="button">Read along</button><span class="fs-onair">● ON AIR</span></div>' +
      '<div class="fs-transcript">' + words.map(function (w, i) { return /^\s+$/.test(w) ? w : '<span data-w="' + i + '">' + esc(w) + '</span>'; }).join('') + '</div></div>';
    $('.fs-av-slot', row).appendChild(avatar(who, 'talk'));
    var b = $('.fs-play', row), tr = $('.fs-transcript', row), bars = $$('.fs-bars rect', row), grille = $('.fs-grille', row);
    var wordEls = $$('[data-w]', tr), playing = false, level = 0, raf = null, an = null, buf = null, lastW = -1;
    $('.fs-readalong', row).addEventListener('click', function () { tr.classList.toggle('open'); });
    function setWord(k) { if (k === lastW) return; if (wordEls[lastW]) wordEls[lastW].classList.remove('now'); for (var i = 0; i < wordEls.length; i++) wordEls[i].classList.toggle('said', i < k); if (wordEls[k]) wordEls[k].classList.add('now'); lastW = k; }
    function frame() {
      var amp = level;
      if (an) { an.getByteFrequencyData(buf); var s = 0; for (var i = 2; i < 40; i++) s += buf[i]; amp = Math.min(1, s / (38 * 150)); }
      else { level = level * 0.86 + (Math.random() < 0.3 ? Math.random() * 0.5 : 0); amp = Math.min(1, level + 0.15 * Math.random()); }
      bars.forEach(function (r, i) { var h = 4 + Math.round((amp * (0.55 + 0.45 * Math.sin(Date.now() / 90 + i * 1.3) ** 2)) * 16); r.setAttribute('height', h); r.setAttribute('y', 74 - h); });
      if (grille) grille.setAttribute('transform', 'translate(41 106) scale(' + (1 + amp * 0.08) + ') translate(-41 -106)');
      row.style.setProperty('--amp', amp.toFixed(2));
      if (audio && audio.duration) {
        var CW = (D.cueWords || {})[slotId];
        if (CW && CW.length === wordEls.length) { var t = audio.currentTime, k = -1; for (var q = 0; q < CW.length; q++) if (CW[q][0] <= t + 0.05) k = q; setWord(k); }
        else setWord(Math.floor(audio.currentTime / audio.duration * wordEls.length));
      }
      if (cue && audio && audio.duration) cue.atTime(audio.currentTime, audio.duration);
      if (playing) raf = requestAnimationFrame(frame);
    }
    function start() { if (cue) cue.start(); playing = true; row.classList.add('playing'); tr.classList.add('open'); b.textContent = '❚❚ Pause'; if (!reduceMotion) raf = requestAnimationFrame(frame); }
    function stop(done) { if (cue) cue.stop(done); playing = false; row.classList.remove('playing'); cancelAnimationFrame(raf); b.textContent = done ? '▶ Play again' : '▶ ' + (info.audioLabel || 'Listen'); bars.forEach(function (r) { r.setAttribute('height', 4); r.setAttribute('y', 70); }); if (done) { setWord(wordEls.length); setTimeout(SFX.crackle, 100); } }
    var audio = null;
    /* opened as a local file (file://), the browser mutes audio routed through the bar-meter analyser, so local previews skip it */
    if (src) {
      audio = new Audio(au(src));
      audio.addEventListener('play', function () {
        if (!an && location.protocol !== 'file:') { try { var c = ac(); var node = c.createMediaElementSource(audio); an = c.createAnalyser(); an.fftSize = 128; buf = new Uint8Array(an.frequencyBinCount); node.connect(an); an.connect(c.destination); } catch (e) { an = null; } }
        start();
      });
      audio.addEventListener('timeupdate', function () { if (cue && reduceMotion && audio.duration) cue.atTime(audio.currentTime, audio.duration); });
      audio.addEventListener('pause', function () { stop(false); });
      audio.addEventListener('ended', function () { stop(true); SFX.roger(); });
      b.addEventListener('click', function () { if (audio.paused) { SFX.keyup(); setTimeout(function () { audio.play(); }, 380); } else audio.pause(); });
    } else {
      // teacher-view demo: the browser's own voice reads the script, words light up as they are spoken
      b.addEventListener('click', function () {
        var ss = window.speechSynthesis; if (!ss) { toast('📻', 'No computer voice here', 'This browser can’t read aloud. The real clip will play here once it exists.'); return; }
        if (playing) { ss.cancel(); stop(false); return; }
        var u = new SpeechSynthesisUtterance(info.script || ''); u.rate = 0.95;
        var starts = []; var pos = 0; words.forEach(function (w, i) { if (!/^\s+$/.test(w)) starts.push([pos, i]); pos += w.length; });
        u.onboundary = function (e) { level = 0.9; var k = 0; for (var j = 0; j < starts.length; j++) if (starts[j][0] <= e.charIndex) k = j; setWord(k); if (cue) cue.atWord(k); };
        u.onend = function () { stop(true); };
        u.onend = function () { stop(true); SFX.roger(); };
        ss.cancel(); SFX.keyup(); setTimeout(function () { ss.speak(u); }, 380); start(); setWord(0);
      });
    }
    return row;
  }

  /* ---------- section slots: one VIDEO + one AUDIO per section, hidden until a file exists ----------
     The layer places a slot at every section of the science template (ELA pattern). DATA only adds
     labels, recording notes and scripts. A slot shows nothing to students until:
       video: assets/video/teacher/<prefix>-<slot>.mp4 exists, OR video-manifest.json has
              "<WW-0D>-<slot>" with status "ready" and an embed;
       audio: assets/audio/guide/<crew>/<prefix>-<slot>.mp3 exists.
     ?review (or the mockup toggle) reveals empty slots for the teacher.                           */
  var MANIFEST = null, manifestWait = [];
  function withManifest(cb) {
    if (MANIFEST !== null) return cb(MANIFEST);
    manifestWait.push(cb);
    if (manifestWait.length > 1) return;
    var url = (D.paths && D.paths.manifest) || '';
    function done(m) { MANIFEST = m || {}; manifestWait.forEach(function (f) { f(MANIFEST); }); manifestWait = []; }
    if (!url) return done({});
    try { fetch(url + '?v=' + Date.now()).then(function (r) { return r.json(); }).then(function (j) { done(j.videos || j); }).catch(function () { done({}); }); }
    catch (e) { done({}); }
  }
  // mockup: a single-file preview carries its media inline, keyed by file name
  function au(u) { var k = String(u).split('/').pop(); return (D.art && D.art.audio && D.art.audio[k]) || u; }
  /* Does this media file exist? A tiny HEAD request (no media download, no time limit),
     so a slow connection or many videos on one page never hides a recorded video. */
  function probe(url, kind, cb) {
    var done = false, u = au(url);
    function fin(ok) { if (done) return; done = true; cb(ok); }
    function viaMedia() {
      var m = document.createElement(kind);
      m.preload = 'metadata'; m.addEventListener('loadedmetadata', function () { fin(true); }); m.addEventListener('error', function () { fin(false); });
      setTimeout(function () { fin(false); }, 30000); m.src = u;
    }
    if (/^(data|blob):/.test(u)) return fin(true);
    if (!window.fetch || location.protocol === 'file:') return viaMedia();
    fetch(u, { method: 'HEAD', cache: 'no-cache' }).then(function (r) { if (r.ok) fin(true); else if (r.status === 404) fin(false); else viaMedia(); }).catch(viaMedia);
  }
  function slotBox(id) {
    var info = (D.slots && D.slots[id]) || {};
    var who = crewOf(info.crew);
    var pre = D.prefix || 'g4sci';
    var vfile = (D.paths && D.paths.video || 'assets/video/teacher/') + pre + '-' + id + '.mp4';
    var afile = (D.paths && D.paths.audio || 'assets/audio/guide/') + (D.guide || 'crew') + '/' + pre + '-' + id + '.mp3';
    var key = (D.manifestKey || '') + '-' + id;
    var box = fsOnly(el('div', 'fs-ms fs-empty'));
    box.dataset.slot = id;
    var label = info.label || id;
    // teacher-view placeholder (only visible with ?review / mockup toggle)
    var ph = el('div', 'fs-ms-ph',
      '<span class="fs-ms-ic">🎥</span><div><b>' + esc(label) + '</b> <span class="fs-ms-id">' + esc(pre + '-' + id) + '</span>' +
      (info.notes ? '<div class="fs-ms-n">🎥 ' + esc(info.notes) + (info.length ? ' <i>(' + esc(info.length) + ')</i>' : '') + '</div>' : '<div class="fs-ms-n">🎥 Video slot open: record if this section needs you.</div>') +
      (info.script ? '<div class="fs-ms-n">📻 ' + esc(who.name) + ': “' + esc(info.script) + '”</div>' : '') + '</div>');
    box.appendChild(ph);
    var live = el('div', 'fs-ms-live'); box.appendChild(live);
    function showVideo(node) { box.classList.remove('fs-empty'); live.insertBefore(node, live.firstChild); }
    /* D.videoOff: slots whose recorded video no longer matches the page (hidden until it is re-recorded) */
    if ((D.videoOff || []).indexOf(id) < 0) probe(vfile, 'video', function (ok) {
      if (ok) {
        var vtt = vfile.replace(/\.mp4$/, '.vtt');
        var v = el('div', 'fs-video', '<video controls playsinline preload="metadata" poster="' + vfile.replace(/\.mp4$/, '.jpg') + '" src="' + vfile + '">' +
          '<track kind="captions" srclang="en" label="English" src="' + vtt + '"></video>');
        showVideo(v); addCaptions(v); return;
      }
      withManifest(function (m) {
        var e = m[key]; if (!e || e.status !== 'ready' || !e.embed) return;
        var t = document.createElement('div'); t.innerHTML = e.embed; var f = t.querySelector('iframe'); if (!f) return;
        f.removeAttribute('width'); f.removeAttribute('height'); f.style.cssText = 'display:block;width:100%;aspect-ratio:16/9;border:0;border-radius:12px;';
        var v = el('div', 'fs-video'); v.appendChild(f); showVideo(v);
      });
    });
    if (info.script) probe(afile, 'audio', function (ok) {
      if (!ok) return;
      box.classList.remove('fs-empty'); live.appendChild(makeRadio(info, who, afile, false, id));
    });
    if (info.script) { // teacher view: demo the walkie-talkie with the computer's voice
      var demoBtn = el('button', 'fs-demo', '▶ Demo the radio'); demoBtn.type = 'button';
      $('.fs-ms-ph > div', box).appendChild(demoBtn);
      demoBtn.addEventListener('click', function () { var r = makeRadio(info, who, null, true, id); demoBtn.replaceWith(r); $('.fs-play', r).click(); });
    }
    return box;
  }
  function put(node, ref, where) {
    if (!ref) return false;
    if (where === 'before') ref.parentNode.insertBefore(node, ref);
    else if (where === 'after') ref.parentNode.insertBefore(node, ref.nextSibling);
    else if (where === 'prepend') ref.insertBefore(node, ref.firstChild);
    else ref.appendChild(node);
    return true;
  }
  function placeSlots() {
    var placed = [];
    function add(id, ref, where) { if (put(slotBox(id), ref, where)) placed.push(id); }
    var vocab = $('#tab-vocab');
    add('welcome', $('.fs-casecard') || vocab, $('.fs-casecard') ? 'after' : 'prepend');
    add('warmup', $('.act-warmup .act-body'), 'prepend');
    var ww = $$('.card').filter(function (c) { return /Word Wall/i.test(c.textContent.slice(0, 200)); })[0];
    if (ww) add('vocab', $('.card-body', ww), 'prepend');
    add('lesson', $('#tab-lesson .act-body'), 'prepend');
    $$('#tab-lesson .act-body > h3').forEach(function (h, i) { add('part' + (i + 1), h, 'after'); });
    add('figure', $('#tab-lesson .lesson-figure'), 'before');
    if ($('#tab-explore .act-body')) add('explore', $('#tab-explore .act-body'), 'prepend');
    else { /* no Explore tab (lean lessons): the explore video sits just before the Part 4 game's story paragraph (D.exploreMod, default the sort) */
      var sg = $('.fs-game[data-mod="' + (D.exploreMod || 'sort') + '"]'), sp = sg && sg.previousElementSibling;
      if (sg) add('explore', sp && sp.tagName === 'P' ? sp : sg, 'before'); }
    add('quiz', $('#tab-quiz .quiz-card'), 'before');
    add('assignment', $('#tab-assignment .act-body'), 'prepend');
    $$('#tab-assignment .act-body > p').filter(function (p) { return /^\W*Part [A-Z]\b/.test(p.textContent.trim()); })
      .forEach(function (p) { var L = p.textContent.match(/Part ([A-Z])/)[1]; add('part' + L.toLowerCase(), p, 'after'); });
    var ev = $$('#tab-assignment .act-body > div').filter(function (d) { return /Use Your Evidence/i.test(d.textContent.slice(0, 80)); })[0];
    if (ev) add('evidence', ev.children[1] || ev, ev.children[1] ? 'after' : 'prepend');
    var cb = $$('#tab-assignment .card').filter(function (c) { return /Circle Back/i.test(c.textContent.slice(0, 120)); })[0];
    if (cb) add('closing', $('.card-body', cb), 'prepend');
    window.FS_SLOTS = placed;
    Object.keys(D.slots || {}).forEach(function (k) { if (placed.indexOf(k) < 0 && k !== 'tool') FAILED.push('slot with no anchor: ' + k); });
  }

  /* ---------- compact header (SS pattern): one row, pills, banner + intro on the first tab only ---------- */
  function buildHeader() {
    var header = $('.header'); if (!header) return;
    header.classList.add('fs-hd');
    var title = $('.header-title', header);
    var exp = D.expedition || {}, cs = D.case || {}, who = crewOf();
    var meta = fsOnly(el('div', 'fs-hd-meta',
      '<span class="fs-exp-tag">' + esc(D.weekLabel || ('Week ' + (D.week || exp.num || ''))) + '</span> ' +
      (cs.title ? 'Case: <b>' + esc(cs.title) + '</b> · ' : '') + 'Guide: <b>' + esc(who.name) + '</b>'));
    if (title) title.appendChild(meta);
    var tools = fsOnly(el('div', 'fs-hd-tools'));
    header.appendChild(tools);
    var anchorNode = header;
    function panel(html) { var p = fsOnly(el('div', 'fs-hd-panel', html)); anchorNode.parentNode.insertBefore(p, anchorNode.nextSibling); anchorNode = p; return p; }
    function pill(txt, p, fn) {
      var b = el('button', 'fs-pill', txt); b.type = 'button';
      b.addEventListener('click', function () {
        if (fn) return fn();
        var open = !p.classList.contains('open');
        $$('.fs-hd-panel.open').forEach(function (x) { x.classList.remove('open'); });
        $$('.fs-pill[aria-expanded="true"]').forEach(function (x) { x.setAttribute('aria-expanded', 'false'); });
        if (open) { p.classList.add('open'); b.setAttribute('aria-expanded', 'true'); }
      });
      tools.appendChild(b); return b;
    }
    var ra = document.getElementById('optima-read-aloud');
    if (ra) {
      var rp = panel(''); var home = ra.parentNode, next = ra.nextSibling; rp.appendChild(ra);
      // layer off: put the read-aloud box back where it was
      document.addEventListener('fs:layer', function (e) { if (e.detail) rp.appendChild(ra); else home.insertBefore(ra, next); });
      pill('🔊 Read aloud', rp);
    }
    var strip = $('.info-strip');
    if (strip) {
      var dl = '<dl>';
      $$('.info-item', strip).forEach(function (it) {
        var l = $('.info-label', it), v = $('.info-value', it), d = $('.info-detail', it);
        dl += '<dt>' + (l ? l.textContent : '') + '</dt><dd>' + (v ? v.textContent : '') + (d ? ' · ' + d.textContent : '') + '</dd>';
      });
      pill('ⓘ Lesson details', panel(dl + '</dl>'));
    }
    /* the Field Notebook opens from the specimen card and the journal; no header pill (less clutter) */
    var hero = $('.hero-visual');
    if (hero && D.banner) {
      hero.classList.add('fs-has-banner');
      var b = fsOnly(el('div', 'fs-banner', D.banner)); hero.appendChild(b);
      if (reduceMotion) { var s = $('svg', b); if (s && s.pauseAnimations) s.pauseAnimations(); }
    }
    updateCount();
  }
  function cleanIntro() {
    $$('.intro-2col .question').forEach(function (q) { q.textContent = q.textContent.trim().replace(/^["“]\s*/, '').replace(/\s*["”]$/, ''); });
    var t = $$('.intro-2col .card-head-title'); if (t[0]) t[0].textContent = 'Big Question'; if (t[1]) t[1].textContent = 'I can';
  }
  function trackTabs() {
    html.setAttribute('data-fs-tab', 'vocab');
    var orig = window.switchTab;
    if (typeof orig !== 'function') return;
    window.switchTab = function (id) { orig(id); html.setAttribute('data-fs-tab', id); };
  }

  /* ---------- the case: a mystery that runs through the lesson ---------- */
  function cluesFound() { return (D.case && D.case.clues || []).filter(function (c) { return store('clue-' + c.id); }); }
  function earnClue(id) {
    var C = D.case; if (!C) return;
    var c = (C.clues || []).filter(function (x) { return x.id === id; })[0]; if (!c || store('clue-' + id)) return;
    store('clue-' + id, '1'); drawBoard();
    var n = cluesFound().length;
    pushToast(c.icon, 'Clue ' + n + ' of ' + C.clues.length + ' found!', c.t, 5200);
    shootStar(false);
    unlockSolve();
  }
  function drawBoard() {
    var C = D.case, b = $('.fs-board'); if (!C || !b) return;
    var found = cluesFound().map(function (c) { return c.id; });
    $('.fs-board-dots', b).innerHTML = C.clues.map(function (c) { return '<i class="' + (found.indexOf(c.id) > -1 ? 'on' : '') + '" title="' + esc(c.where) + '">' + (found.indexOf(c.id) > -1 ? c.icon : '?') + '</i>'; }).join('');
    $('.fs-board-n', b).textContent = (store('solved') ? 'Case cracked' : found.length + ' of ' + C.clues.length + ' clues'); setTimeout(progress, 0);
    var list = $('.fs-board-list', b);
    list.innerHTML = C.clues.map(function (c, i) {
      var have = found.indexOf(c.id) > -1;
      return '<li class="' + (have ? 'on' : '') + '"><span>' + (have ? c.icon : '🔒') + '</span><div><b>Clue ' + (i + 1) + '</b> ' + (have ? esc(c.t) : '<em>' + esc(c.where) + '</em> <button type="button" class="fs-goclue" data-id="' + esc(c.id) + '">Go there →</button>') + '</div></li>';
    }).join('');
    $$('.fs-goclue', list).forEach(function (btn) { btn.addEventListener('click', function (e) { e.stopPropagation(); goToClue(btn.dataset.id); }); });
    if (D.constellation) paintConstellation();
  }
  function scrollToEl(t) {
    var bar = $('#tabBar'), off = bar ? bar.getBoundingClientRect().height + 12 : 12;
    window.scrollTo({ top: t.getBoundingClientRect().top + window.scrollY - off, behavior: reduceMotion ? 'auto' : 'smooth' });
  }
  function goToClue(id) {
    var g = $('[data-mod="' + id + '"]'); if (!g) return;
    var tab = g.closest('[id^="tab-"]'); if (tab && window.switchTab) window.switchTab(tab.id.replace(/^tab-/, ''));
    var b = $('.fs-board'); if (b) b.classList.remove('open');
    setTimeout(function () { scrollToEl(g); g.classList.remove('fs-boardflash'); void g.offsetWidth; g.classList.add('fs-boardflash'); }, 120);
    SFX.blip();
  }
  function buildCase() {
    var C = D.case; if (!C) return;
    // the strip under the tabs: "the story so far" for a mystery
    var tabBar = $('#tabBar');
    var board = fsOnly(el('div', 'fs-board fs-kraft',
      '<button type="button" class="fs-board-row"><span class="fs-board-k">🗂 My clues</span><span class="fs-board-t">' + esc(C.title) + '</span>' +
      '<span class="fs-board-dots"></span><span class="fs-board-n"></span><span class="fs-board-c">▾</span></button>' +
      '<div class="fs-board-more"><p class="fs-board-q">' + esc(C.question) + '</p><ol class="fs-board-list"></ol></div>'));
    if (tabBar) tabBar.parentNode.insertBefore(board, tabBar.nextSibling);
    $('.fs-board-row', board).addEventListener('click', function () { board.classList.toggle('open'); });
    drawBoard();
    // the case file that opens the lesson (tab 1)
    var vocab = $('#tab-vocab'); if (!vocab) return;
    var card = fsOnly(el('div', 'fs-casecard' + (C.style ? ' fs-case-' + C.style : '')));
    function tagOf(s) { return s.tag != null ? s.tag : '● REC'; }
    var stills = (C.stills || []).map(function (s) {
      return '<div class="fs-still' + (s.kind ? ' fs-still-' + s.kind : '') + '"><div class="fs-still-img' + (s.img ? ' photo' : '') + '">' + (s.img ? '<img alt="' + esc(s.alt || s.cam) + '" src="' + esc(s.img) + '"><span class="fs-still-rec">' + esc(tagOf(s)) + '</span>' : s.svg) + '<span class="fs-still-q">?</span></div><div class="fs-still-cap"><b>' + esc(s.cam) + '</b> ' + esc(s.time) + '</div></div>';
    }).join('');
    card.innerHTML = '<div class="fs-folder-tab">CASE FILE ' + esc(C.num) + '</div><div class="fs-folder fs-kraft">' +
      '<div class="fs-case-k"><span class="fs-case-av"></span><span>From ' + esc(crewOf().name) + ', ' + esc(crewOf().role) + '</span></div>' +
      '<div class="fs-case-t">' + esc(C.title) + '</div>' +
      '<p class="fs-case-p">' + esc(C.hook) + '</p>' + (C.strip ? stripChart(C.strip) : '') + (C.thread ? '<div class="fs-th3"><div class="fs-th3-top"><span>' + esc(C.threadHead || 'Messages') + '</span><small>' + esc(C.threadSub || '') + '</small></div>' + C.thread.map(function (m) { return '<div class="fs-th3-m ' + (m.me ? 'me' : 'them') + '"><b>' + esc(m.who) + '</b><p>' + esc(m.t) + '</p>' + (m.time ? '<small>' + esc(m.time) + '</small>' : '') + '</div>'; }).join('') + '</div>' : '') + (C.letter ? '<div class="fs-letter"><div class="fs-letter-paper"><div class="fs-letter-to">' + esc(C.letter.to) + '</div>' + C.letter.body.map(function (t) { return '<p>' + esc(t) + '</p>'; }).join('') + '<div class="fs-letter-sign">' + esc(C.letter.sign) + '</div></div>' + (C.letter.pins && D.flmap ? '<div class="fs-letter-map">' + flMap({ cities: true, label: 'Marco\u2019s map of Florida with four numbered pins.' }).outerHTML.replace('<g class="fs-fl-top"></g>', '<g class="fs-fl-top">' + flPinsSVG(C.letter.pins) + '</g>') + '<div class="fs-letter-pins">' + C.letter.pins.map(function (p) { return '<span><b>' + p.n + '</b> ' + esc(p.name) + '</span>'; }).join('') + '</div></div>' : '') + '</div>' : '') + (C.plans ? '<div class="fs-bp">' + C.plans.map(function (p) { return '<div class="fs-bp-card"><div class="fs-bp-tag">' + esc(p.tag) + '</div><div class="fs-bp-svg">' + p.svg + '</div><b>' + p.icon + ' ' + esc(p.t) + '</b><ul>' + p.rows.map(function (r) { return '<li><span>' + esc(r[0]) + ':</span> ' + esc(r[1]) + '</li>'; }).join('') + '</ul></div>'; }).join('') + '</div>' : '') + (C.map && D.townmap ? '<div class="fs-sn-casemap">' + D.townmap + (C.mapCap ? '<div class="fs-sn-cap">' + esc(C.mapCap) + '</div>' : '') + '</div>' : '') + (C.notice ? '<div class="fs-notice"><div class="fs-notice-h">' + esc(C.notice.head) + '</div><div class="fs-notice-t">' + esc(C.notice.title) + '</div><dl>' + C.notice.rows.map(function (r) { return '<dt>' + esc(r[0]) + '</dt><dd>' + esc(r[1]) + '</dd>'; }).join('') + '</dl>' + (C.notice.line ? '<div class="fs-notice-line">' + esc(C.notice.line) + '</div>' : '') + '</div>' : '') + (C.wishes ? '<div class="fs-wishes">' + C.wishes.map(function (w, i) { return '<div class="fs-wish" style="--r:' + ((i % 2 ? 1 : -1) * (1.5 + i)) + 'deg"><span class="fs-wish-ic">' + (w.icon || '⭐') + '</span><p>' + esc(w.t) + '</p><b>' + esc(w.who) + '</b></div>'; }).join('') + '</div>' : '') + (stills ? '<div class="fs-stills">' + stills + '</div>' : '') + (C.logs ? '<div class="fs-logs">' + C.logs.map(function (lg) {
        return '<div class="fs-log">' + (lg.img ? '<div class="fs-log-img"><img alt="' + esc(lg.alt || '') + '" src="' + esc(lg.img) + '"></div>' : '') + '<div class="fs-log-h">' + esc(lg.head) + '</div><dl>' + lg.rows.map(function (r) { return '<dt>' + esc(r[0]) + '</dt><dd>' + esc(r[1]) + '</dd>'; }).join('') + '</dl>' + (lg.big ? '<div class="fs-log-big">' + esc(lg.big) + '</div>' : '') + '</div>';
      }).join('') + (C.sticky ? '<div class="fs-log-sticky">' + esc(C.sticky) + '</div>' : '') + '</div>' : '') + (C.stillsCredit ? '<details class="fs-credit fs-credit-fold"><summary>📷 Photo credits</summary>' + esc(C.stillsCredit) + '</details>' : '') +
      (C.smudge ? '<div class="fs-case-smudge" aria-label="' + esc(C.smudge.replace(/…$/, '') + '… (the rest is washed out)') + '"><span>' + esc(C.smudge) + '</span><i></i></div>' : '') +
      '<div class="fs-case-ask">🔎 ' + esc(C.question) + '</div>' +
      '<div class="fs-case-how">' + esc(C.how) + '</div></div>';
    $('.fs-case-av', card).appendChild(avatar(crewOf(), 'small'));
    // tap a camera still to see it big
    $$('.fs-still', card).forEach(function (st, i) {
      var s = (C.stills || [])[i]; if (!s || !s.img) { st.style.cursor = 'default'; return; }
      st.setAttribute('role', 'button'); st.tabIndex = 0; st.title = C.style ? 'Tap to see this photo bigger' : 'Tap to see this camera bigger';
      function open() {
        var m = modal(); SFX.blip();
        m.innerHTML = '<div class="fs-nb fs-kraft fs-still-big' + (C.style ? ' fs-case-' + C.style : '') + '"><button class="fs-x" type="button" aria-label="Close">✕</button>' +
          '<div class="fs-still-img photo"><img alt="' + esc(s.alt || s.cam) + '" src="' + esc(s.img) + '"><span class="fs-still-rec">' + esc(tagOf(s)) + '</span></div>' +
          '<div class="fs-still-cap"><b>' + esc(s.cam || '') + '</b> ' + esc(s.time || '') + '</div>' + (s.alt ? '<p class="fs-still-alt">' + esc(s.alt) + '</p>' : '') + '</div>';
        $('.fs-x', m).addEventListener('click', function () { m.classList.remove('open'); });
      }
      st.addEventListener('click', open);
      st.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(); } });
    });
    put(card, $('.video-placeholder-wrap', vocab) || vocab, $('.video-placeholder-wrap', vocab) ? 'after' : 'prepend');
  }
  function buildSolve() {
    var C = D.case; if (!C || !C.solve) return;
    var at = $('#tab-assignment .act-body'); if (!at) return;
    var S = C.solve;
    var g = gameShell('Crack the case', S.title, null, null);
    g.classList.add('fs-solve');
    g.innerHTML += '<div class="fs-lock">🔒 <span></span></div><p class="fs-solve-q">' + esc(S.q) + '</p><div class="fs-solve-opts">' +
      S.options.map(function (o, i) { return '<button type="button" class="fs-solve-o" data-i="' + i + '">' + esc(o.t) + '</button>'; }).join('') +
      '</div><div class="fs-miss"></div><div class="fs-win"></div>';
    put(g, at, 'prepend');
    var miss = $('.fs-miss', g), win = $('.fs-win', g);
    $$('.fs-solve-o', g).forEach(function (b) {
      b.addEventListener('click', function () {
        if (g.classList.contains('locked') || store('solved')) return;
        var o = S.options[+b.dataset.i];
        if (!o.right) { bounce(b, miss, o.why); return; }
        b.classList.add('right'); store('solved', '1'); miss.classList.remove('show');
        win.innerHTML = esc(o.why); win.classList.add('show'); SFX.win(); drawBoard(); shootStar(true); try { document.dispatchEvent(new Event('fs:solved')); } catch (e) {}
      });
    });
    if (store('solved')) { var r = S.options.map(function (o, i) { return o.right ? i : -1; }).filter(function (i) { return i > -1; })[0]; $$('.fs-solve-o', g)[r].classList.add('right'); win.innerHTML = esc(S.options[r].why); win.classList.add('show'); }
    unlockSolve();
  }
  function unlockSolve() {
    var g = $('.fs-solve'); if (!g || !D.case) return;
    var n = cluesFound().length, need = D.case.clues.length;
    g.classList.toggle('locked', n < need);
    var l = $('.fs-lock span', g);
    if (l) l.textContent = n < need ? 'You need all ' + need + ' clues to solve the case. You have ' + n + '.' : '';
    var cl = $('.fs-solve-clues', g);
    if (!cl) { cl = el('div', 'fs-solve-clues'); var qq = $('.fs-solve-q', g); qq.parentNode.insertBefore(cl, qq); }
    var got = cluesFound();
    cl.innerHTML = got.length ? '<div class="fs-in-k">Your clues</div><ol>' + got.map(function (c) { return '<li><span>' + c.icon + '</span>' + esc(c.t) + '</li>'; }).join('') + '</ol>' : '';
    var sb = $('.fs-lock .fs-showclues', g);
    if (!sb && $('.fs-lock', g)) { sb = el('button', 'fs-btn fs-showclues', '🔎 Show me where the clues are'); sb.type = 'button'; $('.fs-lock', g).appendChild(sb);
      sb.addEventListener('click', function () { var b = $('.fs-board'); if (!b) return; b.classList.add('open'); scrollToEl(b); b.classList.remove('fs-boardflash'); void b.offsetWidth; b.classList.add('fs-boardflash'); var more = $('.fs-board-more', b), bk = $('.fs-backcase', b);
        if (more && !bk) { bk = el('button', 'fs-btn alt fs-backcase', '↩ Back to Crack the Case'); bk.type = 'button'; more.appendChild(bk);
          bk.addEventListener('click', function (e) { e.stopPropagation(); b.classList.remove('open'); bk.style.display = 'none'; var sv = $('.fs-solve'); if (sv) scrollToEl(sv); SFX.blip(); }); }
        if (bk) bk.style.display = ''; SFX.blip(); }); }
    if (sb) sb.style.display = n < need ? '' : 'none';
  }

  /* ---------- Field Notebook ---------- */
  function collected() { var n = 0; (D.notebook || []).forEach(function (c) { if (c.have || (c.lesson === D.lesson && store('specimen'))) n++; }); return n; }
  function updateCount() { var c = $('.fs-hd-tools .fs-count'); if (c) c.textContent = collected(); }
  function openNotebook() {
    var m = $('#fsNotebook');
    if (!m) {
      m = fsOnly(el('div', 'fs-modal')); m.id = 'fsNotebook';
      m.addEventListener('click', function (e) { if (e.target === m) m.classList.remove('open'); });
      document.body.appendChild(m);
    }
    var who = crewOf();
    var h = '<div class="fs-nb fs-kraft"><button class="fs-x" type="button" aria-label="Close">✕</button><h3>📓 My Field Notebook</h3>' +
      '<div class="fs-nb-sub">' + esc((D.notebookTitle || 'Specimens') + ' · with ' + who.name) + '</div><div class="fs-nb-grid">';
    (D.notebook || []).forEach(function (c) {
      var mine = c.lesson === D.lesson, have = c.have || (mine && store('specimen'));
      h += '<div class="fs-nb-cell' + (have ? '' : ' empty') + (mine && have ? ' new' : '') + '"><span class="ic">' + (have ? c.icon : (mine ? '❔' : '🔒')) + '</span>' +
        esc(c.lesson) + '<br>' + (have ? esc(c.name) : (mine ? 'Finish today\'s lesson' : 'Coming up')) + '</div>';
    });
    m.innerHTML = h + (D.tool ? '<div class="fs-nb-cell' + (store('tool-done') ? ' new' : ' empty') + '" style="margin-top:10px"><span class="ic">' + (store('tool-done') ? (D.tool.icon || '🧰') : '⭐') + '</span>Bonus: ' + esc(D.tool.name) + '<br>' + (store('tool-done') ? 'Sticker earned' : 'Optional') + '</div>' : '') + '</div><div style="margin-top:12px"><button type="button" class="fs-btn fs-jr2">📓 Download my field journal</button></div>' + (D.mockup ? '<div class="fs-plan-note" style="margin-top:10px">Mockup: earlier specimens are shown as if already collected.</div>' : '') + '</div>';
    $('.fs-x', m).addEventListener('click', function () { m.classList.remove('open'); });
    var jr = $('.fs-jr2', m); if (jr) jr.addEventListener('click', downloadJournal);
    m.classList.add('open');
  }

  /* ---------- Warm-up: reaction test ---------- */
  function buildReaction() {
    var R = D.reaction; if (!R) return;
    var warm = $('.act-warmup .act-body'); if (!warm) return;
    var g = gameShell('Try it for real', R.title, R.todo, R.why); g.dataset.mod = 'reaction';
    var trail = el('div', 'fs-trail');
    trail.setAttribute('role', 'button'); trail.setAttribute('tabindex', '0');
    trail.innerHTML = '<svg viewBox="0 0 600 190" preserveAspectRatio="xMidYMax slice"><g fill="#0B1A10" opacity=".9">' +
      '<path d="M40,190 L52,40 L64,190Z"/><path d="M120,190 L130,60 L140,190Z"/><path d="M470,190 L482,30 L494,190Z"/><path d="M540,190 L548,70 L556,190Z"/></g>' +
      '<path d="M0,170 Q150,150 300,165 T600,160 L600,190 L0,190Z" fill="#3A2A18" opacity=".7"/>' +
      '<path d="M270,166 l26,-6 l4,4 l24,-4" stroke="#7A5A34" stroke-width="5" fill="none" stroke-linecap="round"/></svg>' +
      '<div class="fs-snapword">SNAP!</div><div class="fs-trail-msg">Tap here to start<small>Then wait. Tap again only when you hear the snap.</small></div>';
    var times = el('div', 'fs-times'), path = el('div', 'fs-path4'), win = el('div', 'fs-win'), miss = el('div', 'fs-miss');
    (R.path || []).forEach(function (p) { path.appendChild(el('div', '', '<span>' + p.icon + '</span>' + esc(p.t))); });
    g.appendChild(trail); g.appendChild(times); g.appendChild(path); g.appendChild(miss); g.appendChild(win);
    var state = 'idle', t0 = 0, timer = null, results = [];
    var msg = $('.fs-trail-msg', trail);
    function setMsg(a, b) { msg.innerHTML = esc(a) + (b ? '<small>' + esc(b) + '</small>' : ''); }
    function go() {
      if (state === 'idle' || state === 'done') {
        state = 'wait'; trail.className = 'fs-trail wait'; setMsg('Listen…', 'Wait for the snap. No guessing!'); miss.classList.remove('show');
        timer = setTimeout(function () { state = 'go'; trail.className = 'fs-trail go'; SFX.snap(); t0 = performance.now(); setMsg('TAP!'); }, 1600 + Math.random() * 2600);
      } else if (state === 'wait') {
        clearTimeout(timer); state = 'idle'; trail.className = 'fs-trail'; SFX.thud();
        setMsg('Too soon! Tap to try again'); miss.innerHTML = '🔎 ' + esc(R.tooSoon); miss.classList.add('show');
      } else if (state === 'go') {
        var ms = Math.round(performance.now() - t0); results.push(ms); state = 'done'; trail.className = 'fs-trail';
        setMsg((ms / 1000).toFixed(2) + ' seconds!', results.length < 3 ? 'Tap to try again (' + (3 - results.length) + ' more)' : 'Tap to try again any time');
        var best = Math.min.apply(null, results);
        times.innerHTML = results.map(function (r, i) { return '<span class="fs-time' + (r === best ? ' best' : '') + '">Try ' + (i + 1) + ': ' + (r / 1000).toFixed(2) + ' s</span>'; }).join('');
        $$('div', path).forEach(function (d, i) { setTimeout(function () { d.classList.add('lit'); }, 150 * i); });
        if (results.length >= 1 && !win.classList.contains('show')) { win.innerHTML = esc(R.win); win.classList.add('show'); SFX.chime(); store('reaction', '1'); setTimeout(function () { earnClue(R.clue || 'reaction'); }, 600); }
      }
    }
    trail.addEventListener('pointerdown', function (e) { e.preventDefault(); go(); });
    trail.addEventListener('keydown', function (e) { if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); go(); } });
    var firstP = $('p', warm);
    warm.insertBefore(g, firstP ? firstP.nextSibling : warm.firstChild);
  }

  /* ---------- Lesson: signal relay ---------- */
  function buildRelay() {
    var R = D.relay; if (!R) return;
    var body = $('#tab-lesson .act-body'); if (!body) return;
    var after = null;
    $$('p', body).some(function (p) { if (R.afterText && p.textContent.indexOf(R.afterText) > -1) { after = p; return true; } });
    if (!after) { FAILED.push('relay anchor text not found'); return; }
    var g = gameShell(R.kicker || 'Send the signal', R.title, R.todo, R.why); g.dataset.mod = 'relay';
    var relay = el('div', 'fs-relay n' + R.steps.length); relay.appendChild(el('div', 'fs-relay-wire')); var pulse = el('div', 'fs-relay-pulse'); relay.appendChild(pulse);
    R.steps.forEach(function (s, i) {
      var st = el('div', 'fs-station', '<div class="fs-slot" data-i="' + i + '">' + (i + 1) + '</div><div class="fs-station-n">Step ' + (i + 1) + '</div><div class="fs-station-l"></div>');
      relay.appendChild(st);
    });
    var tray = el('div', 'fs-tray'), miss = el('div', 'fs-miss'), win = el('div', 'fs-win');
    shuffle(R.steps.map(function (s, i) { return i; })).forEach(function (i) {
      var t = el('div', 'fs-tok', '<span>' + R.steps[i].icon + '</span>' + esc(R.steps[i].t)); t.dataset.i = i; tray.appendChild(t);
    });
    g.appendChild(relay); g.appendChild(tray); g.appendChild(miss); g.appendChild(win);
    var slots = $$('.fs-slot', relay), placed = 0;
    function drop(tok, slot) {
      var want = +slot.dataset.i, got = +tok.dataset.i;
      if (slot.classList.contains('filled')) return;
      if (want !== got) { bounce(tok, miss, (R.miss && R.miss[got]) || 'Not that step. Where does the message start?'); return; }
      slot.classList.add('filled'); slot.textContent = R.steps[got].icon; slot.parentNode.querySelector('.fs-station-l').textContent = R.steps[got].t;
      tok.remove(); SFX.chime(); miss.classList.remove('show'); placed++;
      if (placed === R.steps.length) runPulse();
    }
    function runPulse() {
      store('relay', '1');
      var w = relay.offsetWidth; pulse.style.opacity = 1;
      var anim = pulse.animate ? pulse.animate([{ left: '12%' }, { left: 'calc(88% - 16px)' }], { duration: reduceMotion ? 1 : 1600, easing: 'ease-in-out' }) : null;
      slots.forEach(function (s, i) { setTimeout(function () { s.classList.add('lit'); SFX.blip(); }, reduceMotion ? 0 : i * 450); });
      setTimeout(function () { pulse.style.opacity = 0; SFX.win(); win.innerHTML = esc(R.win); win.classList.add('show'); earnClue(R.clue || 'relay'); }, reduceMotion ? 10 : 1700);
    }
    $$('.fs-tok', tray).forEach(function (t) { dragDrop(t, function () { return slots; }, drop); });
    tapTargets(g, slots, drop);
    after.parentNode.insertBefore(g, after.nextSibling);
  }

  /* ---------- Lesson: field cams ---------- */
  function buildCams() {
    var C = D.cams; if (!C) return;
    var wrap = $('#tab-lesson .diagram-wrap'); if (!wrap) return;
    var g = gameShell(C.kicker || 'Trail cameras', C.title, C.todo, C.why); g.dataset.mod = 'cams';
    // the old heading + "Tap each animal" line describe the diagram this game replaces
    [wrap.previousElementSibling, wrap.previousElementSibling && wrap.previousElementSibling.previousElementSibling].forEach(function (x) { if (x && /^(H3|P)$/.test(x.tagName) && x.textContent.length < 120) x.classList.add('fs-hide-on'); });
    var grid = el('div', 'fs-cams'), panel = el('div', 'fs-cam-panel');
    C.animals.forEach(function (a, idx) {
      var b = el('button', 'fs-cam'); b.type = 'button';
      b.innerHTML = '<div class="fs-cam-rec">' + esc(a.cam || ('CAM ' + (idx + 1))) + (a.time ? ' · ' + esc(a.time) : '') + '</div><div class="fs-cam-view' + (a.img ? ' photo' : '') + '">' + (a.img ? '<img alt="' + esc(a.alt || a.name) + '" src="' + esc(a.img) + '">' : a.svg) + '</div><div class="fs-cam-cap">' + esc(a.name) + '<em>' + esc(a.sense) + '</em></div>';
      b.addEventListener('click', function () { open(a, b); });
      grid.appendChild(b);
    });
    var count = el('div', 'fs-count', ''), win = el('div', 'fs-win');
    g.appendChild(grid); if (C.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(C.credit))); g.appendChild(panel); g.appendChild(count); g.appendChild(win);
    var seen = {};
    function upd() { var n = Object.keys(seen).length; count.textContent = '📹 ' + n + ' of ' + C.animals.length + ' cameras checked'; count.classList.toggle('ok', n === C.animals.length);
      if (n === C.animals.length && !win.classList.contains('show')) { win.innerHTML = esc(C.win); win.classList.add('show'); SFX.win(); store('cams', '1'); earnClue(C.clue || 'cams'); } }
    upd();
    function open(a, btn) {
      SFX.crackle();
      var labels = C.stepNames || ['Stimulus', 'Sense organ', 'Brain', 'Response'];
      panel.innerHTML = '<div class="fs-game-k">' + esc(a.name) + ' · ' + esc(a.sense) + '</div><div class="fs-cam-steps">' +
        a.steps.map(function (s, i) { return '<div class="fs-cam-step"><b>' + (i + 1) + '. ' + esc(labels[i]) + '</b><span>' + esc(s) + '</span></div>'; }).join('') +
        '</div><button class="fs-btn" type="button">Next step ▶</button>' + (a.fact ? '<div class="fs-cam-fact">🌴 ' + esc(a.fact) + '</div>' : '');
      panel.classList.add('open');
      var steps = $$('.fs-cam-step', panel), i = 0, nb = $('.fs-btn', panel);
      function next() {
        if (i < steps.length) { steps[i].classList.add('on'); SFX.blip(); i++; }
        if (i === steps.length) { nb.style.display = 'none'; var f = $('.fs-cam-fact', panel); if (f) f.classList.add('show'); seen[a.name] = 1; btn.classList.add('done'); upd(); }
        else nb.textContent = 'Next step ▶ (' + (i + 1) + ' of 4)';
      }
      nb.addEventListener('click', next); next();
      panel.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'nearest' });
    }
    wrap.classList.add('fs-replaced');
    wrap.parentNode.insertBefore(g, wrap);
  }

  /* ---------- Explore: sort the heron moment ---------- */
  function buildSort() {
    var S = D.sort; if (!S) return;
    var body = $('#tab-explore .act-body'), firstP = body && $('p', body);
    if (S.afterText) { /* lean lessons: place the sort after the paragraph that holds this text, on any tab */
      firstP = null; $$('.tab-panel p').some(function (p) { if (p.textContent.indexOf(S.afterText) > -1) { firstP = p; return true; } });
      if (!firstP) { FAILED.push('sort anchor text not found'); return; } body = firstP.parentNode; }
    if (!body) return;
    var g = gameShell(S.kicker || ('Field cam: ' + (S.subject || '')), S.title, S.todo, S.why); g.dataset.mod = 'sort';
    var bins = el('div', 'fs-sort n' + S.bins.length);
    S.bins.forEach(function (b, i) {
      var bin = el('div', 'fs-bin' + (b.write ? ' brain' : ''), '<div class="fs-bin-h"><span>' + b.icon + '</span>' + esc(b.t) + '</div>' + (b.write ? '<p>' + esc(b.write) + '</p>' : ''));
      bin.dataset.i = i; if (!b.write) bin.dataset.drop = '1'; bins.appendChild(bin);
    });
    var deck = el('div', 'fs-deck'), miss = el('div', 'fs-miss'), win = el('div', 'fs-win');
    shuffle(S.cards).forEach(function (c) { var d = el('div', 'fs-card', esc(c.t)); d.dataset.bin = c.bin; d.dataset.miss = c.miss || ''; deck.appendChild(d); });
    g.appendChild(bins); g.appendChild(deck); g.appendChild(miss); g.appendChild(win);
    var targets = $$('.fs-bin[data-drop]', bins), left = S.cards.length;
    function drop(card, bin) {
      if (card.classList.contains('placed')) return;
      if (String(bin.dataset.i) !== String(card.dataset.bin)) { bounce(card, miss, card.dataset.miss || 'Look again: is this something in the world, a body part, or something the heron did?'); return; }
      card.classList.add('placed'); card.classList.remove('sel'); bin.appendChild(card); SFX.chime(); miss.classList.remove('show'); left--;
      if (!left) { win.innerHTML = esc(S.win); win.classList.add('show'); SFX.win(); store('sort', '1'); earnClue(S.clue || 'sort'); }
    }
    $$('.fs-card', deck).forEach(function (c) { dragDrop(c, function () { return targets; }, drop); });
    tapTargets(g, targets, drop);
    body.insertBefore(g, firstP ? firstP.nextSibling : body.firstChild);
  }

  /* ---------- Warm-Up: tie each visitor to the center with the right kind of thread (10.01) ----------
     D.thread = {afterText, kicker, title, todo[], why, center:{name, img, alt}, kinds:{key:{t, icon, c}},
                 visitors:[{id, icon, name, does, kind, x, y, miss:{kind:hint}, hint, ok}], win, clue} */
  function buildThread() {
    var T = D.thread; if (!T) return;
    var at = null;
    $$('.tab-panel p').some(function (p) { if (T.afterText && p.textContent.indexOf(T.afterText) > -1) { at = p; return true; } });
    if (!at) at = $('.act-warmup .act-body p');
    if (!at) { FAILED.push('thread anchor text not found'); return; }
    var g = gameShell(T.kicker || 'Try it', T.title, T.todo, T.why); g.dataset.mod = 'thread';
    var web = el('div', 'fs-web');
    var svg = '<svg class="fs-web-lines" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">' +
      T.visitors.map(function (v) { return '<line data-v="' + esc(v.id) + '" x1="' + T.center.x + '" y1="' + T.center.y + '" x2="' + v.x + '" y2="' + v.y + '" vector-effect="non-scaling-stroke"/>'; }).join('') + '</svg>';
    web.innerHTML = svg + '<div class="fs-web-center" style="left:' + T.center.x + '%;top:' + T.center.y + '%">' +
      (T.center.img ? '<img alt="' + esc(T.center.alt || T.center.name) + '" src="' + esc(T.center.img) + '">' : '') + '<b>' + esc(T.center.name) + '</b></div>';
    T.visitors.forEach(function (v) {
      var n = el('button', 'fs-web-node', '<span class="fs-web-ic">' + v.icon + '</span><span class="fs-web-nm">' + esc(v.name) + '</span><span class="fs-web-kd"></span>');
      n.type = 'button'; n.dataset.v = v.id; n.style.left = v.x + '%'; n.style.top = v.y + '%';
      n.title = v.does; web.appendChild(n);
    });
    var spools = el('div', 'fs-spools');
    Object.keys(T.kinds).forEach(function (k) {
      var K = T.kinds[k], s = el('div', 'fs-spool', '<i style="background:' + K.c + '"></i><span>' + K.icon + '</span>' + esc(K.t));
      s.dataset.k = k; spools.appendChild(s);
    });
    var info = el('div', 'fs-hs-card fs-web-info', '<em>' + esc(T.tapHint || 'Tap a visitor to see what it does with the oak.') + '</em>');
    var miss = el('div', 'fs-miss'), win = el('div', 'fs-win'), count = el('div', 'fs-count');
    g.appendChild(web); g.appendChild(info); g.appendChild(spools); g.appendChild(miss); g.appendChild(count); g.appendChild(win);
    var tied = {}; try { tied = JSON.parse(store('thread') || '{}'); } catch (e) {}
    function vOf(id) { return T.visitors.filter(function (v) { return v.id === id; })[0]; }
    function tie(v, animate) {
      var K = T.kinds[v.kind], n = $('.fs-web-node[data-v="' + v.id + '"]', web), ln = $('line[data-v="' + v.id + '"]', web);
      tied[v.id] = 1; n.classList.add('tied'); n.style.borderColor = K.c; $('.fs-web-kd', n).innerHTML = K.icon + ' ' + esc(K.t); $('.fs-web-kd', n).style.background = K.c;
      ln.style.stroke = K.c; ln.classList.add('on'); if (animate && !reduceMotion) { ln.classList.remove('draw'); void ln.getBoundingClientRect(); ln.classList.add('draw'); }
    }
    function upd() {
      var n = Object.keys(tied).length; count.textContent = '🧵 ' + n + ' of ' + T.visitors.length + ' threads tied'; count.classList.toggle('ok', n === T.visitors.length);
      if (n === T.visitors.length && !win.classList.contains('show')) { win.innerHTML = esc(T.win); win.classList.add('show'); earnClue(T.clue || 'thread'); }
    }
    Object.keys(tied).forEach(function (id) { var v = vOf(id); if (v) tie(v, false); });
    function show(v) { info.innerHTML = '<span class="fs-hs-n">' + v.icon + '</span><div><b>' + esc(v.name) + '</b>' + esc(v.does) + '</div>'; info.classList.remove('flash'); void info.offsetWidth; info.classList.add('flash'); }
    var targets = $$('.fs-web-node', web);
    targets.forEach(function (n) { n.addEventListener('click', function () { if (!$('.fs-spool.sel', g)) { show(vOf(n.dataset.v)); SFX.blip(); } }); });
    function drop(sp, node) {
      var v = vOf(node.dataset.v); if (tied[v.id]) { show(v); return; }
      show(v);
      if (sp.dataset.k !== v.kind) { bounce(sp, miss, (v.miss && v.miss[sp.dataset.k]) || v.hint || 'Read what this visitor does with the oak. Which kind of thread fits?'); return; }
      sp.classList.remove('sel'); miss.classList.remove('show'); tie(v, true); SFX.chime();
      if (v.ok) { $('div', info).insertAdjacentHTML('beforeend', '<div class="fs-web-ok">✅ ' + esc(v.ok) + '</div>'); }
      store('thread', JSON.stringify(tied)); upd(); if (Object.keys(tied).length === T.visitors.length) SFX.win();
    }
    $$('.fs-spool', spools).forEach(function (s) { dragDrop(s, function () { return targets; }, drop); });
    tapTargets(g, targets, drop);
    at.parentNode.insertBefore(g, at.nextSibling);
    upd();
  }

  /* ---------- Lesson: pull one thread of the web, predict, then watch what changes (10.01) ----------
     D.ripple = {kicker, title, todo[], why, nodes:[{id, icon, name, x, y}], links:[{a, b, kind}], kinds:{key:{t, c}},
                 pulls:[{id, btn, why, fx:{nodeId:{s:'hurt'|'grow'|'same', t}}}], win, clue} — replaces #tab-lesson .diagram-wrap */
  function buildRipple() {
    var R = D.ripple; if (!R) return;
    var wrap = $(R.replace || '#tab-lesson .diagram-wrap'); if (!wrap) { FAILED.push('ripple: no diagram to replace'); return; }
    var g = gameShell(R.kicker || 'Pull a thread', R.title, R.todo, R.why); g.dataset.mod = 'ripple';
    var pv = wrap.previousElementSibling; if (pv && pv.tagName === 'P' && pv.textContent.length < 160) pv.classList.add('fs-hide-on');
    function node(id) { return R.nodes.filter(function (n) { return n.id === id; })[0]; }
    var web = el('div', 'fs-web fs-ripple');
    web.innerHTML = '<svg class="fs-web-lines" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true">' + R.links.map(function (l, i) {
      var a = node(l.a), b = node(l.b); return '<line class="on" data-i="' + i + '" data-a="' + l.a + '" data-b="' + l.b + '" style="stroke:' + R.kinds[l.kind].c + '" x1="' + a.x + '" y1="' + a.y + '" x2="' + b.x + '" y2="' + b.y + '" vector-effect="non-scaling-stroke"/>';
    }).join('') + '</svg>';
    R.nodes.forEach(function (n) {
      var b = el('button', 'fs-web-node fs-rp-node', '<span class="fs-web-ic">' + n.icon + '</span><span class="fs-web-nm">' + esc(n.name) + '</span><span class="fs-rp-fx"></span>');
      b.type = 'button'; b.dataset.n = n.id; b.style.left = n.x + '%'; b.style.top = n.y + '%'; web.appendChild(b);
    });
    var legend = el('div', 'fs-rp-legend', Object.keys(R.kinds).map(function (k) { return '<span><i style="background:' + R.kinds[k].c + '"></i>' + esc(R.kinds[k].t) + '</span>'; }).join(''));
    var picks = el('div', 'fs-rp-picks', '<span class="fs-in-k">Pull a thread:</span>' + R.pulls.map(function (p, i) { return '<button type="button" class="fs-btn alt fs-rp-pick" data-i="' + i + '">' + esc(p.btn) + '</button>'; }).join(''));
    var stage = el('div', 'fs-rp-stage'), out = el('div', 'fs-rp-out'), win = el('div', 'fs-win'), count = el('div', 'fs-count');
    g.appendChild(picks); g.appendChild(web); g.appendChild(legend); g.appendChild(stage); g.appendChild(out); g.appendChild(count); g.appendChild(win);
    var done = {}; try { done = JSON.parse(store('ripple') || '{}'); } catch (e) {}
    var cur = null, phase = 'pick', guesses = {};
    function reset() {
      web.className = 'fs-web fs-ripple'; guesses = {};
      $$('.fs-rp-node', web).forEach(function (b) { b.className = 'fs-web-node fs-rp-node'; $('.fs-rp-fx', b).textContent = ''; });
      $$('line', web).forEach(function (l) { l.classList.remove('cut'); });
    }
    function upd() {
      var n = Object.keys(done).length; count.textContent = '🧵 ' + n + ' of ' + R.pulls.length + ' threads pulled'; count.classList.toggle('ok', n === R.pulls.length);
      $$('.fs-rp-pick', picks).forEach(function (b) { b.classList.toggle('done', !!done[R.pulls[+b.dataset.i].id]); });
      if (n === R.pulls.length && !win.classList.contains('show')) { win.innerHTML = esc(R.win); win.classList.add('show'); SFX.win(); earnClue(R.clue || 'ripple'); }
    }
    $$('.fs-rp-pick', picks).forEach(function (b) { b.addEventListener('click', function () {
      reset(); cur = R.pulls[+b.dataset.i]; phase = 'guess'; out.innerHTML = ''; SFX.blip();
      $$('.fs-rp-pick', picks).forEach(function (x) { x.classList.toggle('on', x === b); });
      var gone = node(cur.id); $('.fs-rp-node[data-n="' + cur.id + '"]', web).classList.add('target');
      web.classList.add('guessing');
      stage.innerHTML = '<div class="fs-rp-ask">🤔 <b>Predict first.</b> If the ' + esc(gone.name.toLowerCase()) + ' disappeared, which living things would change? <b>Tap them on the web.</b> Then pull the thread.</div>' +
        '<button type="button" class="fs-btn fs-rp-go">🧵 Pull the thread</button>';
      $('.fs-rp-go', stage).addEventListener('click', pull);
      stage.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'nearest' });
    }); });
    $$('.fs-rp-node', web).forEach(function (b) { b.addEventListener('click', function () {
      if (phase !== 'guess' || b.dataset.n === cur.id) return;
      guesses[b.dataset.n] = !guesses[b.dataset.n]; b.classList.toggle('guess', guesses[b.dataset.n]); SFX.blip();
    }); });
    function pull() {
      if (phase !== 'guess') return; phase = 'show'; web.classList.remove('guessing'); SFX.snap();
      var gb = $('.fs-rp-node[data-n="' + cur.id + '"]', web); gb.classList.add('gone');
      $$('line', web).forEach(function (l) { if (l.dataset.a === cur.id || l.dataset.b === cur.id) l.classList.add('cut'); });
      var ids = Object.keys(cur.fx), right = 0, changed = 0;
      ids.forEach(function (id, i) {
        var f = cur.fx[id], b = $('.fs-rp-node[data-n="' + id + '"]', web); if (!b) return;
        if (f.s !== 'same') changed++;
        if ((f.s !== 'same') === !!guesses[id]) right++;
        setTimeout(function () { b.classList.add(f.s); $('.fs-rp-fx', b).textContent = f.s === 'hurt' ? '⬇' : f.s === 'grow' ? '⬆' : '✓'; if (f.s === 'hurt') SFX.thud(); else if (f.s === 'grow') SFX.chime(); }, reduceMotion ? 0 : 500 + i * 380);
      });
      var missed = R.nodes.filter(function (n) { return n.id !== cur.id && !cur.fx[n.id] && guesses[n.id]; }).length;
      setTimeout(function () {
        stage.innerHTML = '<div class="fs-rp-score">🔮 You predicted <b>' + right + ' of ' + ids.length + '</b> of these right.' + (missed ? ' (' + missed + ' you tapped didn’t change much.)' : '') + '</div>';
        out.innerHTML = '<ul class="fs-rp-list">' + ids.map(function (id) { var f = cur.fx[id], n = node(id);
          return '<li class="' + f.s + '"><span>' + (f.s === 'hurt' ? '⬇' : f.s === 'grow' ? '⬆' : '✓') + '</span><div><b>' + n.icon + ' ' + esc(n.name) + '</b> ' + esc(f.t) + '</div></li>'; }).join('') + '</ul>' +
          (cur.why ? '' : '');
        if (cur.why) out.appendChild(whyCard(cur.why));
        done[cur.id] = 1; store('ripple', JSON.stringify(done)); upd();
      }, reduceMotion ? 10 : 700 + ids.length * 380);
    }
    wrap.classList.add('fs-replaced');
    wrap.parentNode.insertBefore(g, wrap);
    upd();
  }

  /* ---------- Warm-Up: "Count it or feel it?" — judge one statement at a time (10.02) ----------
     D.judge = {afterText, kicker, title, todo[], why, sides:[{k,icon,t}] ×2, cards:[{t, side, why}], win, clue} */
  function buildJudge() {
    var J = D.judge; if (!J) return;
    var at = null; $$('.tab-panel p').some(function (p) { if (J.afterText && p.textContent.indexOf(J.afterText) > -1) { at = p; return true; } });
    if (!at) { FAILED.push('judge anchor text not found'); return; }
    var g = gameShell(J.kicker || 'Warm-Up game', J.title, J.todo, J.why); g.dataset.mod = 'judge';
    var stage = el('div', 'fs-jd'), card = el('div', 'fs-jd-card'), sides = el('div', 'fs-jd-sides');
    J.sides.forEach(function (s) { var b = el('div', 'fs-jd-side', '<div class="fs-jd-h"><span>' + s.icon + '</span>' + esc(s.t) + '</div><div class="fs-jd-pile"></div>'); b.dataset.k = s.k; b.setAttribute('role', 'button'); b.tabIndex = 0; sides.appendChild(b); });
    var meter = el('div', 'fs-jd-meter', '<i></i>'), why = el('div', 'fs-hs-card fs-jd-why', '<em>' + esc(J.hint || 'Read the card, then drag it to a side, or tap a side.') + '</em>');
    var miss = el('div', 'fs-miss'), win = el('div', 'fs-win'), count = el('div', 'fs-count');
    stage.appendChild(card); stage.appendChild(sides); g.appendChild(stage); g.appendChild(meter); g.appendChild(why); g.appendChild(miss); g.appendChild(count); g.appendChild(win);
    var i = 0, saved = +store('judge') || 0, targets = $$('.fs-jd-side', sides);
    function show() {
      var c = J.cards[i];
      if (!c) { card.innerHTML = '<div class="fs-jd-done">✅ All ' + J.cards.length + ' sorted</div>'; card.className = 'fs-jd-card done'; return; }
      card.className = 'fs-jd-card'; card.innerHTML = '<span class="fs-jd-n">' + (i + 1) + ' of ' + J.cards.length + '</span><span class="fs-jd-t">' + esc(c.t) + '</span>';
      void card.offsetWidth; card.classList.add('in');
    }
    function upd() { count.textContent = '🧾 ' + i + ' of ' + J.cards.length + ' sorted'; count.classList.toggle('ok', i === J.cards.length); $('i', meter).style.width = (100 * i / J.cards.length) + '%';
      if (i === J.cards.length && !win.classList.contains('show')) { win.innerHTML = esc(J.win); win.classList.add('show'); SFX.win(); earnClue(J.clue || 'judge'); } }
    function place(c, side, animate) {
      var chip = el('span', 'fs-jd-chip', esc(c.t)); $('.fs-jd-pile', side).appendChild(chip);
      if (animate && !reduceMotion) { chip.classList.add('drop'); }
    }
    for (var k = 0; k < Math.min(saved, J.cards.length); k++) { place(J.cards[k], targets.filter(function (t) { return t.dataset.k === J.cards[k].side; })[0], false); }
    i = Math.min(saved, J.cards.length);
    function answer(side) {
      var c = J.cards[i]; if (!c) return;
      if (side.dataset.k !== c.side) { card.classList.remove('bounce'); void card.offsetWidth; card.classList.add('bounce'); SFX.thud(); miss.innerHTML = '🔎 ' + esc(c.miss || J.miss || 'Ask: could a scientist write down a number for this?'); miss.classList.add('show'); return; }
      miss.classList.remove('show'); SFX.chime(); place(c, side, true);
      why.innerHTML = '<span class="fs-hs-n">' + (c.side === J.sides[0].k ? J.sides[0].icon : J.sides[1].icon) + '</span><div>' + esc(c.why) + '</div>'; why.classList.remove('flash'); void why.offsetWidth; why.classList.add('flash');
      i++; store('judge', String(i)); show(); upd();
    }
    // drag the card, or tap a side
    var start = null, ghost = null;
    card.addEventListener('pointerdown', function (e) { if (!J.cards[i]) return; start = { x: e.clientX, y: e.clientY }; card.setPointerCapture && card.setPointerCapture(e.pointerId); });
    card.addEventListener('pointermove', function (e) {
      if (!start) return;
      if (!ghost && Math.abs(e.clientX - start.x) + Math.abs(e.clientY - start.y) > 8) { ghost = card.cloneNode(true); ghost.classList.add('ghost'); ghost.style.width = card.offsetWidth + 'px'; document.body.appendChild(ghost); }
      if (ghost) { ghost.style.left = (e.clientX - ghost.offsetWidth / 2) + 'px'; ghost.style.top = (e.clientY - 30) + 'px';
        targets.forEach(function (t) { var r = t.getBoundingClientRect(); t.classList.toggle('over', e.clientX > r.left && e.clientX < r.right && e.clientY > r.top && e.clientY < r.bottom); }); }
    });
    function end(e) { if (!start) return; start = null; if (ghost) { ghost.remove(); ghost = null; var hit = null; targets.forEach(function (t) { var r = t.getBoundingClientRect(); if (e.clientX > r.left && e.clientX < r.right && e.clientY > r.top && e.clientY < r.bottom) hit = t; t.classList.remove('over'); }); if (hit) answer(hit); } }
    card.addEventListener('pointerup', end); card.addEventListener('pointercancel', function () { start = null; if (ghost) { ghost.remove(); ghost = null; } });
    targets.forEach(function (t) { t.addEventListener('click', function () { answer(t); }); t.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); answer(t); } }); });
    at.parentNode.insertBefore(g, at.nextSibling);
    show(); upd();
  }

  /* ---------- Lesson: fly a survey (a model) — weather changes the count, not the manatees (10.02) ----------
     D.survey = {afterText, kicker, title, todo[], why, img, alt, credit, total, note, temps:[{k,icon,t,f}], winds:[{k,icon,t,f}], minFlights, q:{q, opts:[{t, ok, why}]}, win, clue} */
  function buildSurvey() {
    var S = D.survey; if (!S) return;
    var at = null; $$('.tab-panel p').some(function (p) { if (S.afterText && p.textContent.indexOf(S.afterText) > -1) { at = p; return true; } });
    if (!at) { FAILED.push('survey anchor text not found'); return; }
    var g = gameShell(S.kicker || 'Fly the survey', S.title, S.todo, S.why); g.dataset.mod = 'survey';
    var view = el('div', 'fs-sv-view', '<img alt="' + esc(S.alt) + '" src="' + esc(S.img) + '"><div class="fs-sv-glare"></div><div class="fs-sv-haze"></div><div class="fs-sv-plane">✈️</div><div class="fs-sv-tally"></div>');
    var credit = el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credit</summary>' + esc(S.credit));
    function chips(list, name) { return '<div class="fs-sv-row"><span class="fs-in-k">' + esc(name) + '</span>' + list.map(function (o) { return '<button type="button" class="fs-in-chip" data-k="' + o.k + '"><span>' + o.icon + '</span>' + esc(o.t) + '</button>'; }).join('') + '</div>'; }
    var ctl = el('div', 'fs-sv-ctl', chips(S.temps, S.tempLabel || 'Weather') + chips(S.winds, S.windLabel || 'Wind') + '<button type="button" class="fs-btn fs-sv-fly">✈️ Fly the survey</button>');
    var note = el('div', 'fs-sv-note', '🧪 ' + esc(S.note));
    var log = el('table', 'fs-sv-log', '<thead><tr><th>Flight</th><th>Weather</th><th>Wind</th><th>Manatees counted</th></tr></thead><tbody></tbody>');
    var qbox = el('div', 'fs-sv-q'), miss = el('div', 'fs-miss'), win = el('div', 'fs-win');
    g.appendChild(view); g.appendChild(credit); g.appendChild(note); g.appendChild(ctl); g.appendChild(log); g.appendChild(qbox); g.appendChild(miss); g.appendChild(win);
    var pick = { t: null, w: null }, flights = [];
    try { flights = JSON.parse(store('survey') || '[]'); } catch (e) {}
    $$('.fs-sv-row', ctl).forEach(function (row, ri) {
      $$('.fs-in-chip', row).forEach(function (c) { c.addEventListener('click', function () {
        $$('.fs-in-chip', row).forEach(function (x) { x.classList.toggle('on', x === c); }); pick[ri ? 'w' : 't'] = c.dataset.k; SFX.blip();
        var T = S.temps.filter(function (o) { return o.k === pick.t; })[0], Wd = S.winds.filter(function (o) { return o.k === pick.w; })[0];
        view.className = 'fs-sv-view' + (Wd && Wd.f < 0.8 ? ' windy' : '') + (T && T.f < 0.5 ? ' warm' : '');
      }); });
    });
    function drawLog() {
      $('tbody', log).innerHTML = flights.map(function (f, i) { return '<tr><td>' + (i + 1) + '</td><td>' + esc(f.t) + '</td><td>' + esc(f.w) + '</td><td><b>' + f.n + '</b></td></tr>'; }).join('');
      log.style.display = flights.length ? '' : 'none';
      var best = flights.some(function (f) { return f.best; });
      if (flights.length >= (S.minFlights || 3) && best) askQ(); else if (flights.length >= (S.minFlights || 3)) qbox.innerHTML = '<div class="fs-sv-hint">🔎 ' + esc(S.bestHint || 'Try one more flight: which weather would put the most manatees in the spring, where you can see them?') + '</div>';
    }
    $('.fs-sv-fly', ctl).addEventListener('click', function () {
      var T = S.temps.filter(function (o) { return o.k === pick.t; })[0], Wd = S.winds.filter(function (o) { return o.k === pick.w; })[0];
      if (!T || !Wd) { miss.innerHTML = '🔎 Pick the weather and the wind first.'; miss.classList.add('show'); SFX.thud(); return; }
      miss.classList.remove('show');
      var n = Math.round(S.total * T.f * Wd.f), tally = $('.fs-sv-tally', view), plane = $('.fs-sv-plane', view);
      plane.classList.remove('go'); void plane.offsetWidth; plane.classList.add('go'); SFX.whoosh();
      var t0 = performance.now(), dur = reduceMotion ? 1 : 1600;
      (function step(now) { var k = Math.min(1, (now - t0) / dur); tally.textContent = '🧮 ' + Math.round(n * k); if (k < 1) requestAnimationFrame(step); else {
        tally.textContent = '🧮 ' + n; SFX.chime();
        flights.push({ t: T.t, w: Wd.t, n: n, best: T.k === S.bestTemp && Wd.k === S.bestWind }); if (flights.length > 6) flights.shift();
        store('survey', JSON.stringify(flights)); drawLog(); } })(t0);
    });
    function askQ() {
      if (qbox.dataset.on) return; qbox.dataset.on = '1';
      qbox.innerHTML = '<div class="fs-in-k">' + esc(S.q.q) + '</div><div class="fs-in-chips">' + S.q.opts.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(o.t) + '</button>'; }).join('') + '</div>';
      $$('.fs-in-chip', qbox).forEach(function (c) { c.addEventListener('click', function () {
        var o = S.q.opts[+c.dataset.i]; if (!o.ok) { bounce(c, miss, o.why); return; }
        $$('.fs-in-chip', qbox).forEach(function (x) { x.classList.toggle('on', x === c); }); c.classList.add('ok'); miss.classList.remove('show');
        win.innerHTML = esc(o.why + ' ' + (S.win || '')); win.classList.add('show'); SFX.win(); store('survey-done', '1'); earnClue(S.clue || 'survey');
      }); });
    }
    at.parentNode.insertBefore(g, at.nextSibling);
    drawLog();
  }

  /* ---------- Lesson: four Florida stories — stamp each one and pick its proof (10.02) ----------
     D.verdict = {replace (selector), kicker, title, todo[], why, stamps:[{k,icon,t}], stories:[{id,name,img,alt,data:[], answer, proof:[{t, ok, miss}], why}], credit, win, clue} */
  function buildVerdict() {
    var V = D.verdict; if (!V) return;
    var wrap = $(V.replace || '#tab-lesson .diagram-wrap'); if (!wrap) { FAILED.push('verdict: nothing to replace'); return; }
    var g = gameShell(V.kicker || 'Case files', V.title, V.todo, V.why); g.dataset.mod = 'verdict';
    var pv = wrap.previousElementSibling; if (pv && pv.tagName === 'P' && pv.textContent.length < 200) pv.classList.add('fs-hide-on');
    var grid = el('div', 'fs-vd-grid'), panel = el('div', 'fs-vd-panel'), count = el('div', 'fs-count'), win = el('div', 'fs-win');
    V.stories.forEach(function (s) {
      var b = el('button', 'fs-vd-card', '<div class="fs-vd-img"><img alt="' + esc(s.alt) + '" src="' + esc(s.img) + '"><span class="fs-vd-stamp"></span></div><b>' + esc(s.name) + '</b>');
      b.type = 'button'; b.dataset.id = s.id; grid.appendChild(b);
      b.addEventListener('click', function () { open(s, b); });
    });
    g.appendChild(grid); if (V.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(V.credit))); g.appendChild(panel); g.appendChild(count); g.appendChild(win);
    var done = {}; try { done = JSON.parse(store('verdict') || '{}'); } catch (e) {}
    function stampOf(k) { return V.stamps.filter(function (x) { return x.k === k; })[0]; }
    function mark(s) { var b = $('.fs-vd-card[data-id="' + s.id + '"]', grid), st = stampOf(s.answer); b.classList.add('done', 'st-' + s.answer); $('.fs-vd-stamp', b).innerHTML = st.icon + ' ' + esc(st.t); }
    function upd() { var n = Object.keys(done).length; count.textContent = '🗂 ' + n + ' of ' + V.stories.length + ' stories decided'; count.classList.toggle('ok', n === V.stories.length);
      if (n === V.stories.length && !win.classList.contains('show')) { win.innerHTML = esc(V.win); win.classList.add('show'); SFX.win(); earnClue(V.clue || 'verdict'); } }
    V.stories.forEach(function (s) { if (done[s.id]) mark(s); });
    function open(s, btn) {
      SFX.blip(); $$('.fs-vd-card', grid).forEach(function (x) { x.classList.toggle('on', x === btn); });
      panel.className = 'fs-vd-panel open';
      panel.innerHTML = '<div class="fs-game-k">' + esc(s.name) + ' · the data</div><ul class="fs-vd-data">' + s.data.map(function (d) { return '<li>📊 ' + esc(d) + '</li>'; }).join('') + '</ul>' +
        '<div class="fs-in-k">1. Stamp it</div><div class="fs-vd-stamps">' + V.stamps.map(function (x) { return '<button type="button" class="fs-vd-sb st-' + x.k + '" data-k="' + x.k + '">' + x.icon + ' ' + esc(x.t) + '</button>'; }).join('') + '</div>' +
        '<div class="fs-vd-proof"><div class="fs-in-k">2. Which line is the best proof?</div><div class="fs-in-chips">' + s.proof.map(function (p, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(p.t) + '</button>'; }).join('') + '</div></div><div class="fs-miss"></div><div class="fs-vd-why"></div>';
      var miss = $('.fs-miss', panel), stamped = !!done[s.id];
      if (stamped) panel.classList.add('stamped');
      $$('.fs-vd-sb', panel).forEach(function (b) { b.addEventListener('click', function () {
        if (panel.classList.contains('stamped')) return;
        if (b.dataset.k !== s.answer) { bounce(b, miss, s.stampMiss || 'Look at the numbers again. Are they getting better or worse over the years?'); return; }
        miss.classList.remove('show'); b.classList.add('ok'); panel.classList.add('stamped'); SFX.stamp();
        var bs = $('.fs-vd-stamp', btn); bs.innerHTML = b.innerHTML; btn.classList.add('st-' + s.answer, 'stamping'); });
      });
      $$('.fs-vd-proof .fs-in-chip', panel).forEach(function (c) { c.addEventListener('click', function () {
        if (!panel.classList.contains('stamped')) { bounce(c, miss, 'Stamp it first: is this story recovering or out of balance?'); return; }
        var p = s.proof[+c.dataset.i]; if (!p.ok) { bounce(c, miss, p.miss || 'That’s not a number a scientist measured. Which line is real data?'); return; }
        c.classList.add('on', 'ok'); miss.classList.remove('show'); SFX.chime();
        $('.fs-vd-why', panel).appendChild(whyCard({ icon: stampOf(s.answer).icon, q: s.name, t: s.why }));
        done[s.id] = 1; store('verdict', JSON.stringify(done)); mark(s); upd();
      }); });
      panel.scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'nearest' });
    }
    wrap.classList.add('fs-replaced'); wrap.parentNode.insertBefore(g, wrap); upd();
  }

  /* ---------- Lesson Part 4: one year can fool you — then all the years (10.02) ----------
     D.trend = {afterText, kicker, title, todo[], why, yLabel, ymax, x0, x1, points:[{x, n}], pair:[x,x], pairText, est:[{x, lo, hi, t}], marks:[{x, t}], q:{q, opts:[{t, ok, why}]}, win, clue} */
  function buildTrend() {
    var T = D.trend; if (!T) return;
    var at = null; $$('.tab-panel p').some(function (p) { if (T.afterText && p.textContent.indexOf(T.afterText) > -1) { at = p; return true; } });
    if (!at) { FAILED.push('trend anchor text not found'); return; }
    var g = gameShell(T.kicker || 'Read the data', T.title, T.todo, T.why); g.dataset.mod = 'trend';
    var W = 640, H = 300, L = 54, R = 14, Tp = 14, B = 34, x0 = T.x0, x1 = T.x1, ym = T.ymax;
    function X(x) { return L + (x - x0) / (x1 - x0) * (W - L - R); } function Y(n) { return Tp + (1 - n / ym) * (H - Tp - B); }
    var axes = '';
    for (var n = 0; n <= ym; n += T.ystep || 2000) axes += '<line x1="' + L + '" x2="' + (W - R) + '" y1="' + Y(n) + '" y2="' + Y(n) + '" class="gl"/><text x="' + (L - 6) + '" y="' + (Y(n) + 4) + '" text-anchor="end">' + n.toLocaleString() + '</text>';
    for (var x = Math.ceil(x0 / 5) * 5; x <= x1; x += 5) axes += '<text x="' + X(x) + '" y="' + (H - 12) + '" text-anchor="middle">' + x + '</text>';
    var est = (T.est || []).map(function (e) { return '<g class="est"><rect x="' + (X(e.x) - 7) + '" y="' + Y(e.hi) + '" width="14" height="' + (Y(e.lo) - Y(e.hi)) + '" rx="4"/><text x="' + (X(e.x) - 10) + '" y="' + (Y(e.hi) - 6) + '" text-anchor="end">' + esc(e.t) + '</text></g>'; }).join('');
    var marks = (T.marks || []).map(function (m) { return '<g class="mk"><line x1="' + X(m.x) + '" x2="' + X(m.x) + '" y1="' + Tp + '" y2="' + (H - B) + '"/><text x="' + (X(m.x) - 4) + '" y="' + (Tp + 12) + '" text-anchor="end">' + esc(m.t) + '</text></g>'; }).join('');
    var dots = T.points.map(function (p, i) { var pair = T.pair.indexOf(p.x) > -1 && T.pair.indexOf(p.x) === T.pair.indexOf(p.x); return '<circle class="dt' + (T.pair.indexOf(p.x) > -1 && !p.skipPair ? ' pr' : '') + '" data-i="' + i + '" cx="' + X(p.x) + '" cy="' + Y(p.n) + '" r="5"><title>' + p.label + ': ' + p.n.toLocaleString() + '</title></circle>'; }).join('');
    // least-squares line through every flight
    var sx = 0, sy = 0, sxx = 0, sxy = 0, k = T.points.length; T.points.forEach(function (p) { sx += p.x; sy += p.n; sxx += p.x * p.x; sxy += p.x * p.n; });
    var m = (k * sxy - sx * sy) / (k * sxx - sx * sx), b = (sy - m * sx) / k, fx0 = T.points[0].x, fx1 = T.points[k - 1].x;
    var svg = '<svg class="fs-tr-svg" viewBox="0 0 ' + W + ' ' + H + '" role="img" aria-label="' + esc(T.alt || 'Chart of manatee counts') + '"><g class="ax">' + axes + '</g>' +
      '<text class="yl" transform="translate(12 ' + (H / 2) + ') rotate(-90)" text-anchor="middle">' + esc(T.yLabel) + '</text>' + marks + est +
      '<line class="fit" x1="' + X(fx0) + '" y1="' + Y(m * fx0 + b) + '" x2="' + X(fx1) + '" y2="' + Y(m * fx1 + b) + '"/>' + dots + '</svg>';
    var chart = el('div', 'fs-tr stage1', svg), msg = el('div', 'fs-hs-card fs-tr-msg', '<em>' + esc(T.pairText) + '</em>');
    var btns = el('div', 'fs-tr-btns', '<button type="button" class="fs-btn alt" data-a="up">📈 Went up</button><button type="button" class="fs-btn alt" data-a="down">📉 Went down</button>');
    var more = el('button', 'fs-btn fs-tr-more', T.moreBtn || '📊 Show every flight'); more.type = 'button'; more.style.display = 'none';
    var qbox = el('div', 'fs-sv-q'), miss = el('div', 'fs-miss'), win = el('div', 'fs-win');
    g.appendChild(chart); g.appendChild(msg); g.appendChild(btns); g.appendChild(more); g.appendChild(qbox); g.appendChild(miss); g.appendChild(win);
    var pts = T.pair.map(function (x) { return T.points.filter(function (p) { return p.x === x; })[0]; });
    var went = pts[1].n > pts[0].n ? 'up' : 'down', diff = Math.abs(pts[1].n - pts[0].n);
    $$('button', btns).forEach(function (bt) { bt.addEventListener('click', function () {
      if (bt.dataset.a !== went) { bounce(bt, miss, 'Look at the two dots again. Is the second one higher or lower?'); return; }
      miss.classList.remove('show'); SFX.chime(); btns.style.display = 'none';
      msg.innerHTML = '<span class="fs-hs-n">' + (went === 'up' ? '📈' : '📉') + '</span><div>' + esc(T.pairWin.replace('{diff}', diff.toLocaleString())) + '</div>'; more.style.display = '';
    }); });
    more.addEventListener('click', function () {
      chart.className = 'fs-tr stage2'; more.style.display = 'none'; SFX.whoosh();
      $$('.dt', chart).forEach(function (d, i) { d.style.animationDelay = (reduceMotion ? 0 : i * 60) + 'ms'; });
      msg.innerHTML = '<span class="fs-hs-n">📊</span><div>' + esc(T.allText) + '</div>';
      setTimeout(ask, reduceMotion ? 0 : 1600);
    });
    function ask() {
      qbox.innerHTML = '<div class="fs-in-k">' + esc(T.q.q) + '</div><div class="fs-in-chips">' + T.q.opts.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(o.t) + '</button>'; }).join('') + '</div>';
      $$('.fs-in-chip', qbox).forEach(function (c) { c.addEventListener('click', function () {
        var o = T.q.opts[+c.dataset.i]; if (!o.ok) { bounce(c, miss, o.why); return; }
        c.classList.add('on', 'ok'); miss.classList.remove('show'); win.innerHTML = esc(o.why + ' ' + (T.win || '')); win.classList.add('show'); SFX.win(); store('trend', '1'); earnClue(T.clue || 'trend');
      }); });
    }
    at.parentNode.insertBefore(g, at.nextSibling);
    // narrow screens: the chart slides sideways; start with the two flights in view and say so
    var slide = el('div', 'fs-tr-slide', '↔ Slide the chart to see every year.'); chart.parentNode.insertBefore(slide, chart.nextSibling);
    function centerPair() { if (chart.scrollWidth <= chart.clientWidth + 4) return; chart.scrollLeft = Math.max(0, X(T.pair[0]) / W * chart.scrollWidth - chart.clientWidth / 2); }
    var seen = false; function look() { if (seen || !chart.offsetParent) return; seen = true; centerPair(); }
    document.addEventListener('click', function () { setTimeout(look, 60); }, true); setTimeout(look, 400);
    if (store('trend')) { btns.style.display = 'none'; chart.className = 'fs-tr stage2'; msg.innerHTML = '<span class="fs-hs-n">📊</span><div>' + esc(T.allText) + '</div>'; ask(); }
  }

  /* ---------- Self-Check: one question at a time + miss lines ---------- */
  /* ---------- Warm-Up: "Beak or tool?" — drag a kitchen tool onto each real beak (11.01) ----------
     D.beaks = {afterText, kicker, title, todo[], why, tools:[{id,icon,t}], birds:[{id,name,img,alt,tool,job,miss:{toolId:hint}}], credit, win, clue} */
  function buildBeaks() {
    var B = D.beaks; if (!B) return;
    var at = null; $$('.tab-panel p').some(function (p) { if (B.afterText && p.textContent.indexOf(B.afterText) > -1) { at = p; return true; } });
    if (!at) { FAILED.push('beaks anchor text not found'); return; }
    var g = gameShell(B.kicker || 'Warm-Up game', B.title, B.todo, B.why); g.dataset.mod = 'beaks';
    var grid = el('div', 'fs-bk-grid'), tray = el('div', 'fs-bk-tray'), info = el('div', 'fs-hs-card fs-bk-info', '<em>' + esc(B.hint || 'Drag a tool onto a beak, or tap a tool and then tap a beak.') + '</em>');
    var miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), win = el('div', 'fs-win');
    B.birds.forEach(function (b) {
      var c = el('div', 'fs-bk-bird', '<div class="fs-bk-ph"><img alt="' + esc(b.alt) + '" src="' + esc(b.img) + '"><span class="fs-bk-slot">?</span></div><div class="fs-bk-n">' + esc(b.name) + '</div>');
      c.dataset.id = b.id; c.setAttribute('role', 'button'); c.tabIndex = 0; grid.appendChild(c);
    });
    shuffle(B.tools).forEach(function (t) { var d = el('div', 'fs-card fs-bk-tool', '<span>' + t.icon + '</span>' + esc(t.t)); d.dataset.id = t.id; tray.appendChild(d); });
    g.appendChild(tray); g.appendChild(grid); g.appendChild(info); g.appendChild(miss); g.appendChild(count); g.appendChild(win);
    if (B.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(B.credit)));
    var done = {}; try { done = JSON.parse(store('beaks') || '{}'); } catch (e) {}
    var targets = $$('.fs-bk-bird', grid);
    function bird(id) { return B.birds.filter(function (b) { return b.id === id; })[0]; }
    function tool(id) { return B.tools.filter(function (t) { return t.id === id; })[0]; }
    function place(b, animate) {
      var c = $('.fs-bk-bird[data-id="' + b.id + '"]', grid), t = tool(b.tool), s = $('.fs-bk-slot', c);
      c.classList.add('done'); s.innerHTML = t.icon; s.classList.add('on'); if (animate && !reduceMotion) { s.classList.remove('pop'); void s.offsetWidth; s.classList.add('pop'); }
      var tk = $('.fs-bk-tool[data-id="' + t.id + '"]', tray); if (tk) { tk.classList.add('placed'); tk.classList.remove('sel'); }
    }
    function upd() {
      var n = Object.keys(done).length; count.textContent = '🔧 ' + n + ' of ' + B.birds.length + ' beaks matched'; count.classList.toggle('ok', n === B.birds.length);
      if (n === B.birds.length && !win.classList.contains('show')) { win.innerHTML = esc(B.win); win.classList.add('show'); SFX.win(); earnClue(B.clue || 'beaks'); }
    }
    function drop(tk, c) {
      var b = bird(c.dataset.id); if (!b || done[b.id]) return;
      if (tk.dataset.id !== b.tool) { bounce(tk, miss, (b.miss && b.miss[tk.dataset.id]) || B.miss || 'Look at the shape of that beak. Which tool has the same shape?'); return; }
      miss.classList.remove('show'); done[b.id] = 1; store('beaks', JSON.stringify(done)); SFX.chime(); place(b, true);
      info.innerHTML = '<span class="fs-hs-n">' + tool(b.tool).icon + '</span><div><b>' + esc(b.name) + '</b>' + esc(b.job) + '</div>'; info.classList.remove('flash'); void info.offsetWidth; info.classList.add('flash');
      upd();
    }
    $$('.fs-bk-tool', tray).forEach(function (t) { dragDrop(t, function () { return targets.filter(function (x) { return !x.classList.contains('done'); }); }, drop); });
    tapTargets(g, targets, drop);
    targets.forEach(function (c) { c.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); var s = $('.sel', g); if (s) { s.classList.remove('sel'); drop(s, c); } } }); });
    B.birds.forEach(function (b) { if (done[b.id]) place(b, false); });
    at.parentNode.insertBefore(g, at.nextSibling);
    upd();
  }

  /* ---------- Lesson: "How deep can you go?" — raise the water, see which legs still work (11.01) ----------
     D.wade = {afterText, kicker, title, todo[], why, depths:[{k,t,h}], birds:[{id,name,img,alt,at:{k:{ok:'yes'|'no'|'swim', t}}}], q:{q, opts:[{t, ok, why}]}, credit, win, clue}
     h = how high the water band climbs the photo (0–100) — a picture of "deeper", not a measurement */
  function buildWade() {
    var Wd = D.wade; if (!Wd) return;
    var at = null; $$('.tab-panel p').some(function (p) { if (Wd.afterText && p.textContent.indexOf(Wd.afterText) > -1) { at = p; return true; } });
    if (!at) { FAILED.push('wade anchor text not found'); return; }
    var g = gameShell(Wd.kicker || 'Lesson game', Wd.title, Wd.todo, Wd.why); g.dataset.mod = 'wade';
    var ctl = el('div', 'fs-wd-ctl', '<span class="fs-in-k">' + esc(Wd.depthLabel || 'Water depth') + '</span>' + Wd.depths.map(function (d) { return '<button type="button" class="fs-in-chip" data-k="' + d.k + '"><span>💧</span>' + esc(d.t) + '<em></em></button>'; }).join(''));
    var row = el('div', 'fs-wd-row'), qbox = el('div', 'fs-sv-q'), miss = el('div', 'fs-miss'), win = el('div', 'fs-win');
    Wd.birds.forEach(function (b) {
      row.appendChild(el('div', 'fs-wd-bird', '<div class="fs-wd-ph"><img alt="' + esc(b.alt) + '" src="' + esc(b.img) + '"><i class="fs-wd-water"></i></div><div class="fs-wd-n">' + esc(b.name) + '</div><div class="fs-wd-st"><em>Pick a depth.</em></div>'));
    });
    g.appendChild(ctl); g.appendChild(row); g.appendChild(qbox); g.appendChild(miss); g.appendChild(win);
    if (Wd.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(Wd.credit)));
    var tried = {}; try { tried = JSON.parse(store('wade') || '{}'); } catch (e) {}
    var ICON = { yes: '✅', no: '🚫', swim: '🛟' };
    function show(k, animate) {
      var d = Wd.depths.filter(function (x) { return x.k === k; })[0]; if (!d) return;
      $$('.fs-in-chip', ctl).forEach(function (c) { c.classList.toggle('on', c.dataset.k === k); });
      $$('.fs-wd-bird', row).forEach(function (card, i) {
        var b = Wd.birds[i], r = b.at[k], w = $('.fs-wd-water', card), st = $('.fs-wd-st', card);
        w.style.height = d.h + '%'; card.className = 'fs-wd-bird st-' + r.ok;
        st.innerHTML = '<b>' + ICON[r.ok] + ' ' + esc(r.ok === 'yes' ? (Wd.yes || 'Stands and feeds') : r.ok === 'swim' ? (Wd.swim || 'Swims instead') : (Wd.no || 'Too deep to stand')) + '</b>' + esc(r.t);
        if (animate && !reduceMotion) { st.classList.remove('flash'); void st.offsetWidth; st.classList.add('flash'); }
      });
      tried[k] = 1; store('wade', JSON.stringify(tried));
      $$('.fs-in-chip', ctl).forEach(function (c) { if (tried[c.dataset.k]) { c.classList.add('done'); $('em', c).textContent = ' ✓'; } });
      if (Object.keys(tried).length >= Wd.depths.length) ask(); else qbox.innerHTML = '<div class="fs-sv-hint">🔎 ' + esc((Wd.depths.length - Object.keys(tried).length) + ' more ' + (Wd.depths.length - Object.keys(tried).length === 1 ? 'depth' : 'depths') + ' to try. Watch the long-legged bird.') + '</div>';
    }
    $$('.fs-in-chip', ctl).forEach(function (c) { c.addEventListener('click', function () { SFX.blip(); if (!reduceMotion) setTimeout(SFX.pop, 260); show(c.dataset.k, true); }); });
    function ask() {
      if (qbox.dataset.on) return; qbox.dataset.on = '1';
      qbox.innerHTML = '<div class="fs-in-k">' + esc(Wd.q.q) + '</div><div class="fs-in-chips">' + Wd.q.opts.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(o.t) + '</button>'; }).join('') + '</div>';
      $$('.fs-in-chip', qbox).forEach(function (c) { c.addEventListener('click', function () {
        var o = Wd.q.opts[+c.dataset.i]; if (!o.ok) { bounce(c, miss, o.why); return; }
        $$('.fs-in-chip', qbox).forEach(function (x) { x.classList.toggle('on', x === c); }); c.classList.add('ok'); miss.classList.remove('show');
        win.innerHTML = esc(o.why + ' ' + (Wd.win || '')); win.classList.add('show'); SFX.win(); store('wade-done', '1'); earnClue(Wd.clue || 'wade');
      }); });
      if (store('wade-done')) { var r = Wd.q.opts.map(function (o, i) { return o.ok ? i : -1; }).filter(function (i) { return i > -1; })[0]; var c = $$('.fs-in-chip', qbox)[r]; c.classList.add('on', 'ok'); win.innerHTML = esc(Wd.q.opts[r].why + ' ' + (Wd.win || '')); win.classList.add('show'); }
    }
    at.parentNode.insertBefore(g, at.nextSibling);
    var keys = Object.keys(tried); if (keys.length) show(keys[keys.length - 1], false);
    else qbox.innerHTML = '<div class="fs-sv-hint">🔎 ' + esc(Wd.start || 'Tap a water depth to start.') + '</div>';
  }

  /* ---------- Part 4: "Build a hiding head" — move the eyes and nostrils on a model, then sink it (11.01) ----------
     D.gator = {afterText, kicker, title, todo[], why, img, alt, credit, parts:[{k,icon,t,spots:[{k,t}], right}], waterK (the spot that stays above water),
               tests:[{k,icon,t,need:[partK…], yes, no}], q:{q,opts:[{t,ok,why}]}, win, clue}
     The model is a plain diagram (three bands: top of head, side, under the jaw), never a drawn animal; the real photo is the answer key. */
  function buildGator() {
    var G = D.gator; if (!G) return;
    var at = null; $$('.tab-panel p').some(function (p) { if (G.afterText && p.textContent.indexOf(G.afterText) > -1) { at = p; return true; } });
    if (!at) { FAILED.push('gator anchor text not found'); return; }
    var g = gameShell(G.kicker || 'Part 4 game', G.title, G.todo, G.why); g.dataset.mod = 'gator';
    var bands = G.bands; // [{k,t}] top→bottom
    var model = el('div', 'fs-gt-model', '<div class="fs-gt-head">' + bands.map(function (b) { return '<div class="fs-gt-band" data-k="' + b.k + '"><span class="fs-gt-bl">' + esc(b.t) + '</span><span class="fs-gt-drop"></span></div>'; }).join('') + '<i class="fs-gt-water"><span>' + esc(G.waterLabel || 'water') + '</span></i></div>');
    var parts = el('div', 'fs-gt-parts', G.parts.map(function (p) { return '<div class="fs-gt-prow"><span class="fs-in-k">' + p.icon + ' ' + esc(p.t) + '</span>' + bands.map(function (b) { return '<button type="button" class="fs-in-chip" data-p="' + p.k + '" data-b="' + b.k + '">' + esc(b.short || b.t) + '</button>'; }).join('') + '</div>'; }).join(''));
    var go = el('div', 'fs-gt-go', '<button type="button" class="fs-btn fs-gt-sink">🌊 Sink it to hide</button><button type="button" class="fs-btn alt fs-gt-up">⬆ Float back up</button>');
    var res = el('div', 'fs-gt-res'), photo = el('div', 'fs-gt-photo', '<img alt="' + esc(G.alt) + '" src="' + esc(G.img) + '"><div class="fs-gt-cap">' + esc(G.photoCap || '') + '</div>');
    var log = el('div', 'fs-count'), qbox = el('div', 'fs-sv-q'), miss = el('div', 'fs-miss'), win = el('div', 'fs-win');
    var wrap = el('div', 'fs-gt-wrap'); var left = el('div', 'fs-gt-left'); left.appendChild(parts); left.appendChild(go); left.appendChild(res);
    wrap.appendChild(model); wrap.appendChild(left);
    g.appendChild(wrap); g.appendChild(log); g.appendChild(photo); g.appendChild(qbox); g.appendChild(miss); g.appendChild(win);
    if (G.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credit</summary>' + esc(G.credit)));
    var pick = {}, designs = {}; try { designs = JSON.parse(store('gator') || '{}'); } catch (e) {}
    function drawModel() {
      $$('.fs-gt-drop', model).forEach(function (d) { d.innerHTML = ''; });
      G.parts.forEach(function (p) { if (!pick[p.k]) return; var d = $('.fs-gt-band[data-k="' + pick[p.k] + '"] .fs-gt-drop', model); d.insertAdjacentHTML('beforeend', '<span class="fs-gt-tok">' + p.icon + '</span>'); });
      $$('.fs-gt-parts .fs-in-chip', g).forEach(function (c) { c.classList.toggle('on', pick[c.dataset.p] === c.dataset.b); });
    }
    $$('.fs-gt-parts .fs-in-chip', g).forEach(function (c) { c.addEventListener('click', function () {
      pick[c.dataset.p] = c.dataset.b; SFX.blip(); model.classList.remove('sunk'); res.innerHTML = ''; drawModel(); }); });
    function sink() {
      if (G.parts.some(function (p) { return !pick[p.k]; })) { miss.innerHTML = '🔎 ' + esc(G.pickFirst || 'Put the eyes and the nostrils somewhere first.'); miss.classList.add('show'); SFX.thud(); return; }
      miss.classList.remove('show'); model.classList.add('sunk'); SFX.whoosh();
      var key = G.parts.map(function (p) { return pick[p.k]; }).join('-'), pass = 0;
      setTimeout(function () {
        res.innerHTML = G.tests.map(function (t) {
          var ok = t.need.every(function (pk) { return pick[pk] === G.waterK; }); if (ok) pass++;
          return '<div class="fs-gt-test ' + (ok ? 'ok' : 'no') + '"><span>' + t.icon + '</span><div><b>' + esc(t.t) + ' ' + (ok ? '✅' : '❌') + '</b>' + esc(ok ? t.yes : t.no) + '</div></div>';
        }).join('');
        designs[key] = pass; store('gator', JSON.stringify(designs)); SFX[pass === G.tests.length ? 'chime' : 'thud']();
        upd();
      }, reduceMotion ? 0 : 900);
    }
    $('.fs-gt-sink', g).addEventListener('click', sink);
    $('.fs-gt-up', g).addEventListener('click', function () { model.classList.remove('sunk'); res.innerHTML = ''; SFX.blip(); });
    function upd() {
      var n = Object.keys(designs).length, best = Object.keys(designs).some(function (k) { return designs[k] === G.tests.length; });
      log.textContent = '🧪 ' + n + (n === 1 ? ' design' : ' designs') + ' tested' + (best ? ' · you found one that passes every test' : '');
      log.classList.toggle('ok', best && n >= 2);
      if (best && n >= 2) { photo.classList.add('show'); ask(); }
      else if (best) qbox.innerHTML = '<div class="fs-sv-hint">🔎 ' + esc(G.tryAnother || 'Now test a different design, so you can compare.') + '</div>';
    }
    function ask() {
      if (qbox.dataset.on) return; qbox.dataset.on = '1';
      qbox.innerHTML = '<div class="fs-in-k">' + esc(G.q.q) + '</div><div class="fs-in-chips">' + G.q.opts.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(o.t) + '</button>'; }).join('') + '</div>';
      $$('.fs-in-chip', qbox).forEach(function (c) { c.addEventListener('click', function () {
        var o = G.q.opts[+c.dataset.i]; if (!o.ok) { bounce(c, miss, o.why); return; }
        $$('.fs-in-chip', qbox).forEach(function (x) { x.classList.toggle('on', x === c); }); c.classList.add('ok'); miss.classList.remove('show');
        win.innerHTML = esc(o.why + ' ' + (G.win || '')); win.classList.add('show'); SFX.win(); store('gator-done', '1'); earnClue(G.clue || 'gator');
      }); });
      if (store('gator-done')) { var r = G.q.opts.map(function (o, i) { return o.ok ? i : -1; }).filter(function (i) { return i > -1; })[0]; var c = $$('.fs-in-chip', qbox)[r]; c.classList.add('on', 'ok'); win.innerHTML = esc(G.q.opts[r].why + ' ' + (G.win || '')); win.classList.add('show'); }
    }
    at.parentNode.insertBefore(g, at.nextSibling);
    drawModel(); if (Object.keys(designs).length) upd();
  }


  /* ---------- shared: draw a model arrow on a photo (percent coords; the svg uses viewBox 0 0 100 100) ---------- */
  function modelArrow(svg, from, to, cls) {
    var id = 'fsah' + Math.random().toString(36).slice(2, 7);
    svg.insertAdjacentHTML('beforeend', '<defs><marker id="' + id + '" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M0 0L10 5L0 10z" fill="#F5B83D"/></marker></defs>' +
      '<line class="fs-ma ' + (cls || '') + '" x1="' + from.x + '" y1="' + from.y + '" x2="' + to.x + '" y2="' + to.y + '" marker-end="url(#' + id + ')" vector-effect="non-scaling-stroke"/>');
  }
  function photoBox(img, alt) {
    var b = el('div', 'fs-mp', '<img alt="' + esc(alt || '') + '" src="' + esc(img) + '"><svg class="fs-mp-svg" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden="true"></svg>');
    return b;
  }
  function tag(box, t, x, y, cls) { var s = el('span', 'fs-mp-tag ' + (cls || ''), esc(t)); s.style.left = x + '%'; s.style.top = y + '%'; box.appendChild(s); return s; }
  function chipsQ(host, q, opts, onRight, miss) {
    var w = el('div', 'fs-sv-q', '<div class="fs-in-k">' + esc(q) + '</div><div class="fs-in-chips">' + opts.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(o.t) + '</button>'; }).join('') + '</div>');
    host.appendChild(w);
    $$('.fs-in-chip', w).forEach(function (c) { c.addEventListener('click', function () {
      if (w.dataset.done) return; var o = opts[+c.dataset.i];
      if (!o.ok) { bounce(c, miss, o.miss || o.why); return; }
      miss.classList.remove('show'); c.classList.add('on', 'ok'); w.dataset.done = '1'; SFX.chime(); onRight(o, +c.dataset.i);
    }); });
    return w;
  }

  /* ---------- Warm-Up: "Point the arrow" — turn a labeled photo into a tiny model (11.02) ----------
     D.arrow = {afterText, kicker, title, todo[], why, img, alt, credit, label:{t,x,y}, from:{x,y}, targets:[{k,icon,t,ok,miss}], at:{x,y}, q1, q2, actions:[{t,ok,miss}], win, clue} */
  function buildArrow() {
    var A = D.arrow; if (!A) return;
    var at = null; $$('.tab-panel p').some(function (p) { if (A.afterText && p.textContent.indexOf(A.afterText) > -1) { at = p; return true; } });
    if (!at) { FAILED.push('arrow anchor text not found'); return; }
    var g = gameShell(A.kicker || 'Warm-Up game', A.title, A.todo, A.why); g.dataset.mod = 'arrow';
    var two = el('div', 'fs-ar-two'), c1 = el('div', 'fs-ar-col', '<div class="fs-in-k">' + esc(A.left || 'Drawing 1 · just a label') + '</div>'), c2 = el('div', 'fs-ar-col', '<div class="fs-in-k">' + esc(A.right || 'Drawing 2 · your tiny model') + '</div>');
    var p1 = photoBox(A.img, A.alt), p2 = photoBox(A.img, A.alt); tag(p1, A.label.t, A.label.x, A.label.y); tag(p2, A.label.t, A.label.x, A.label.y);
    c1.appendChild(p1); c2.appendChild(p2); two.appendChild(c1); two.appendChild(c2);
    var steps = el('div', 'fs-ar-steps'), miss = el('div', 'fs-miss'), win = el('div', 'fs-win');
    g.appendChild(two); g.appendChild(steps); g.appendChild(miss); g.appendChild(win);
    if (A.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credit</summary>' + esc(A.credit)));
    var tw = el('div', 'fs-sv-q', '<div class="fs-in-k">' + esc(A.q1) + '</div><div class="fs-ar-row"><div class="fs-card fs-ar-tok">➜ ' + esc(A.tokenLabel || 'Arrow') + '</div>' +
      A.targets.map(function (t) { return '<div class="fs-ar-tg" data-k="' + t.k + '" role="button" tabindex="0"><span>' + t.icon + '</span>' + esc(t.t) + '</div>'; }).join('') + '</div>');
    steps.appendChild(tw);
    var targets = $$('.fs-ar-tg', tw), tok = $('.fs-ar-tok', tw), svg = $('svg', p2);
    function drop(item, t) {
      var o = A.targets.filter(function (x) { return x.k === t.dataset.k; })[0]; if (tw.dataset.done) return;
      if (!o.ok) { bounce(t, miss, o.miss); return; }
      tw.dataset.done = '1'; miss.classList.remove('show'); t.classList.add('ok'); tok.classList.add('placed'); SFX.whoosh();
      modelArrow(svg, A.from, A.at, 'draw'); tag(p2, o.icon + ' ' + o.t, A.at.x, A.at.y, 'tgt');
      store('arrow1', '1'); step2();
    }
    dragDrop(tok, function () { return targets; }, drop);
    targets.forEach(function (t) { t.addEventListener('click', function () { tok.classList.remove('sel'); drop(tok, t); });
      t.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); drop(tok, t); } }); });
    function step2() {
      chipsQ(steps, A.q2, A.actions, function (o) {
        tag(p2, o.t, (A.from.x + A.at.x) / 2, (A.from.y + A.at.y) / 2 - 8, 'act');
        store('arrow', '1'); win.innerHTML = esc(A.win); win.classList.add('show'); SFX.win(); earnClue(A.clue || 'arrow');
      }, miss);
    }
    at.parentNode.insertBefore(g, at.nextSibling);
    if (store('arrow')) { var r = A.targets.filter(function (x) { return x.ok; })[0]; tw.dataset.done = '1'; tok.classList.add('placed'); $('.fs-ar-tg[data-k="' + r.k + '"]', tw).classList.add('ok'); modelArrow(svg, A.from, A.at); tag(p2, r.icon + ' ' + r.t, A.at.x, A.at.y, 'tgt');
      var a = A.actions.filter(function (x) { return x.ok; })[0]; tag(p2, a.t, (A.from.x + A.at.x) / 2, (A.from.y + A.at.y) / 2 - 8, 'act'); win.innerHTML = esc(A.win); win.classList.add('show'); }
  }

  /* ---------- Lesson: "Upgrade the drawing" — label → arrow → caption, one step at a time (11.02) ----------
     D.upgrade = {afterText, kicker, title, todo[], why, img, alt, credit, label:{t,x,y}, from:{x,y}, to:{x,y}, steps:[{k:'label'|'arrow'|'caption', q, opts:[{t,ok,miss}]}], meter:[t0,t1,t2,t3], win, clue} */
  function buildUpgrade() {
    var U = D.upgrade; if (!U) return;
    var at = null; $$('.tab-panel p').some(function (p) { if (U.afterText && p.textContent.indexOf(U.afterText) > -1) { at = p; return true; } });
    if (!at) { FAILED.push('upgrade anchor text not found'); return; }
    var g = gameShell(U.kicker || 'Lesson game', U.title, U.todo, U.why); g.dataset.mod = 'upgrade';
    var pb = photoBox(U.img, U.alt), svg = $('svg', pb), cap = el('div', 'fs-up-cap');
    var meter = el('div', 'fs-up-meter', '<div class="fs-up-bar"><i></i></div><div class="fs-up-lbl"></div>');
    var steps = el('div', 'fs-up-steps'), miss = el('div', 'fs-miss'), win = el('div', 'fs-win');
    g.appendChild(meter); g.appendChild(pb); g.appendChild(cap); g.appendChild(steps); g.appendChild(miss); g.appendChild(win);
    if (U.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credit</summary>' + esc(U.credit)));
    var n = 0;
    function setMeter() { $('i', meter).style.width = (100 * n / U.steps.length) + '%'; $('.fs-up-lbl', meter).textContent = U.meter[n] || ''; meter.classList.toggle('full', n === U.steps.length); }
    function apply(s, o, animate) {
      if (s.k === 'label') tag(pb, o.tag || o.t, U.label.x, U.label.y, animate ? 'pop' : '');
      if (s.k === 'arrow') { modelArrow(svg, U.from, U.to, animate ? 'draw' : ''); tag(pb, o.tag || o.t, U.to.x, U.to.y, 'act'); }
      if (s.k === 'caption') { cap.textContent = o.t; cap.classList.add('show'); }
    }
    function next() {
      setMeter(); var s = U.steps[n];
      if (!s) { win.innerHTML = esc(U.win); win.classList.add('show'); SFX.win(); earnClue(U.clue || 'upgrade'); return; }
      var w = chipsQ(steps, (n + 1) + '. ' + s.q, s.opts, function (o) { apply(s, o, true); n++; store('upgrade', String(n)); setTimeout(next, reduceMotion ? 0 : 450); }, miss);
      w.classList.add('fs-up-step');
    }
    at.parentNode.insertBefore(g, at.nextSibling);
    var saved = Math.min(+store('upgrade') || 0, U.steps.length);
    for (var k = 0; k < saved; k++) { var s = U.steps[k], o = s.opts.filter(function (x) { return x.ok; })[0]; apply(s, o, false);
      var w = el('div', 'fs-sv-q fs-up-step', '<div class="fs-in-k">' + (k + 1) + '. ' + esc(s.q) + '</div><div class="fs-in-chips"><button type="button" class="fs-in-chip on ok">' + esc(o.t) + '</button></div>'); steps.appendChild(w); }
    n = saved; if (n === U.steps.length) { setMeter(); win.innerHTML = esc(U.win); win.classList.add('show'); } else next();
  }

  /* ---------- Lesson: "Chain it" — structure → action → survival need, for four organisms (11.02) ----------
     D.chain = {replace, kicker, title, todo[], why, slots:[{k,icon,t}], orgs:[{id,name,icon,cards:[{t,k}] (k = slot key, or 'x' for a decoy), miss:{x:hint}, why}], win, clue} */
  function buildChain() {
    var C = D.chain; if (!C) return;
    var wrap = $(C.replace || '#tab-lesson .diagram-wrap'); if (!wrap) { FAILED.push('chain: nothing to replace'); return; }
    var g = gameShell(C.kicker || 'Lesson game', C.title, C.todo, C.why); g.dataset.mod = 'chain';
    var pv = wrap.previousElementSibling; if (pv && pv.tagName === 'P' && pv.textContent.length < 200) pv.classList.add('fs-hide-on');
    var tabs = el('div', 'fs-ch-tabs', C.orgs.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '"><span>' + o.icon + '</span>' + esc(o.name) + '<em></em></button>'; }).join(''));
    var row = el('div', 'fs-ch-row'), pool = el('div', 'fs-ch-pool'), why = el('div', 'fs-hs-card'), miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), win = el('div', 'fs-win');
    g.appendChild(tabs); g.appendChild(row); g.appendChild(pool); g.appendChild(miss); g.appendChild(why); g.appendChild(count); g.appendChild(win);
    var done = {}; try { done = JSON.parse(store('chain') || '{}'); } catch (e) {}
    var cur = null, filled = {};
    function upd() {
      var n = Object.keys(done).length; count.textContent = '🔗 ' + n + ' of ' + C.orgs.length + ' chains built'; count.classList.toggle('ok', n === C.orgs.length);
      $$('.fs-in-chip', tabs).forEach(function (b, i) { var ok = !!done[C.orgs[i].id]; b.classList.toggle('done', ok); $('em', b).textContent = ok ? ' ✓' : ''; });
      if (n === C.orgs.length && !win.classList.contains('show')) { win.innerHTML = esc(C.win); win.classList.add('show'); SFX.win(); earnClue(C.clue || 'chain'); }
    }
    function open(i) {
      cur = C.orgs[i]; filled = {}; SFX.blip(); miss.classList.remove('show');
      $$('.fs-in-chip', tabs).forEach(function (b, k) { b.classList.toggle('on', k === i); });
      row.innerHTML = C.slots.map(function (s, k) { return (k ? '<span class="fs-ch-arw">→</span>' : '') + '<div class="fs-ch-slot" data-k="' + s.k + '" role="button" tabindex="0"><div class="fs-ch-h"><span>' + s.icon + '</span>' + esc(s.t) + '</div><div class="fs-ch-in"></div></div>'; }).join('');
      pool.innerHTML = ''; why.innerHTML = '<span class="fs-hs-n">' + cur.icon + '</span><div><b>' + esc(cur.name) + '</b>' + esc(C.hint || 'Drag each card into its link, or tap a card and then a link. Two cards don\'t belong in the chain.') + '</div>';
      var slots = $$('.fs-ch-slot', row);
      if (done[cur.id]) { cur.cards.filter(function (c) { return c.k !== 'x'; }).forEach(function (c) { $('.fs-ch-in', $('.fs-ch-slot[data-k="' + c.k + '"]', row)).textContent = c.t; }); slots.forEach(function (s) { s.classList.add('full'); }); why.innerHTML = '<span class="fs-hs-n">✅</span><div>' + esc(cur.why) + '</div>'; return; }
      shuffle(cur.cards).forEach(function (c) { var d = el('div', 'fs-card', esc(c.t)); d.dataset.k = c.k; pool.appendChild(d); dragDrop(d, function () { return slots.filter(function (s) { return !s.classList.contains('full'); }); }, drop); });
      tapTargets(g, slots, drop);
    }
    function drop(card, slot) {
      if (!cur || slot.classList.contains('full')) return;
      if (card.dataset.k !== slot.dataset.k) { var m = card.dataset.k === 'x' ? (cur.miss && cur.miss.x) || C.missX : (C.missSlot && C.missSlot[card.dataset.k]) || 'That card fits a different link in the chain.'; bounce(card, miss, m); return; }
      miss.classList.remove('show'); $('.fs-ch-in', slot).textContent = card.textContent; slot.classList.add('full'); card.remove(); SFX.chime();
      filled[slot.dataset.k] = 1;
      if (Object.keys(filled).length === C.slots.length) {
        done[cur.id] = 1; store('chain', JSON.stringify(done)); pool.innerHTML = '';
        why.innerHTML = '<span class="fs-hs-n">✅</span><div>' + esc(cur.why) + '</div>'; why.classList.remove('flash'); void why.offsetWidth; why.classList.add('flash'); upd();
        var nx = C.orgs.map(function (o, i) { return done[o.id] ? -1 : i; }).filter(function (i) { return i > -1; })[0];
        if (nx != null) { var b = el('button', 'fs-btn alt fs-ch-next', 'Next organism →'); b.type = 'button'; b.addEventListener('click', function () { b.remove(); open(nx); }); pool.appendChild(b); }
      }
    }
    $$('.fs-in-chip', tabs).forEach(function (b) { b.addEventListener('click', function () { open(+b.dataset.i); }); });
    wrap.classList.add('fs-replaced'); wrap.parentNode.insertBefore(g, wrap);
    open(0); upd();
  }

  /* ---------- Part 4: "Model kit" — pick a part on a real photo, point its arrow, pick the action and the need (11.02) ----------
     D.kit = {afterText, kicker, title, todo[], why, orgs:[{id,name,icon,img,alt,credit, targets:[{k,t,x,y}], parts:[{k,label,x,y,target,actions:[{t,ok,miss}],needs:[{t,ok,miss}]}]}], qs:{target,action,need}, capTpl, win, clue}
     capTpl uses {part} {action} {org} {need}. */
  function buildKit() {
    var K = D.kit; if (!K) return;
    var at = null; $$('.tab-panel p').some(function (p) { if (K.afterText && p.textContent.indexOf(K.afterText) > -1) { at = p; return true; } });
    if (!at) { FAILED.push('kit anchor text not found'); return; }
    var g = gameShell(K.kicker || 'Part 4 game', K.title, K.todo, K.why); g.dataset.mod = 'kit';
    var tabs = el('div', 'fs-ch-tabs', K.orgs.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '"><span>' + o.icon + '</span>' + esc(o.name) + '<em></em></button>'; }).join(''));
    var stage = el('div', 'fs-kt-stage'), steps = el('div', 'fs-kt-steps'), cap = el('div', 'fs-up-cap'), miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), win = el('div', 'fs-win'), cred = el('div', 'fs-kt-cr');
    g.appendChild(tabs); g.appendChild(stage); g.appendChild(cap); g.appendChild(cred); g.appendChild(steps); g.appendChild(miss); g.appendChild(count); g.appendChild(win);
    var built = {}; try { built = JSON.parse(store('kit') || '{}'); } catch (e) {}
    function upd() {
      var n = Object.keys(built).length; count.textContent = '🧩 ' + n + (n === 1 ? ' model' : ' models') + ' built' + (n === 1 ? ' · try another organism' : '');
      count.classList.toggle('ok', n > 0);
      $$('.fs-in-chip', tabs).forEach(function (b, i) { var ok = Object.keys(built).some(function (k) { return k.indexOf(K.orgs[i].id + ':') === 0; }); b.classList.toggle('done', ok); $('em', b).textContent = ok ? ' ✓' : ''; });
      if (n && !win.classList.contains('show')) { win.innerHTML = esc(K.win); win.classList.add('show'); SFX.win(); earnClue(K.clue || 'kit'); }
    }
    function open(i) {
      var o = K.orgs[i]; SFX.blip(); miss.classList.remove('show'); cap.classList.remove('show'); cap.textContent = '';
      $$('.fs-in-chip', tabs).forEach(function (b, k) { b.classList.toggle('on', k === i); });
      stage.innerHTML = ''; var pb = photoBox(o.img, o.alt); stage.appendChild(pb); cred.textContent = '📷 ' + o.credit;
      o.parts.forEach(function (p) { var d = el('button', 'fs-hs', '+'); d.type = 'button'; d.style.left = p.x + '%'; d.style.top = p.y + '%'; d.setAttribute('aria-label', p.label); d.dataset.k = p.k; pb.appendChild(d); });
      steps.innerHTML = '<div class="fs-sv-hint">🔎 ' + esc(K.start || 'Tap a + on the photo to pick the part your model will explain.') + '</div>';
      $$('.fs-hs', pb).forEach(function (d) { d.addEventListener('click', function () {
        if (pb.dataset.lock) return; var p = o.parts.filter(function (x) { return x.k === d.dataset.k; })[0];
        $$('.fs-hs', pb).forEach(function (x) { x.classList.toggle('on', x === d); }); SFX.chime(); pb.dataset.lock = '1';
        $$('.fs-mp-tag', pb).forEach(function (t) { t.remove(); }); tag(pb, p.label, p.x, p.y - 9, 'pop');
        steps.innerHTML = ''; var ans = {};
        chipsQ(steps, K.qs.target, o.targets.map(function (t) { return { t: t.t, ok: t.k === p.target, miss: (p.tmiss && p.tmiss[t.k]) || K.tmiss || 'What does this part push, grab, touch or hide in?' }; }), function (r, idx) {
          var t = o.targets[idx]; modelArrow($('svg', pb), { x: p.x, y: p.y }, { x: t.x, y: t.y }, 'draw'); tag(pb, t.t, t.x, t.y, 'tgt'); SFX.whoosh();
          chipsQ(steps, K.qs.action, p.actions, function (a) {
            ans.action = a.t; tag(pb, a.t, (p.x + t.x) / 2, (p.y + t.y) / 2 - 7, 'act');
            chipsQ(steps, K.qs.need, p.needs, function (nd) {
              cap.textContent = K.capTpl.replace('{part}', p.label.toLowerCase()).replace('{action}', a.t).replace('{org}', o.capName || o.name.toLowerCase()).replace('{need}', nd.t); cap.classList.add('show');
              built[o.id + ':' + p.k] = 1; store('kit', JSON.stringify(built)); delete pb.dataset.lock; SFX.sparkle(); upd();
              var again = el('div', 'fs-sv-hint', '✅ ' + esc(K.doneLine || 'That\'s a real model! Tap another + or pick another organism to build one more.')); steps.appendChild(again);
            }, miss);
          }, miss);
        }, miss);
      }); });
    }
    $$('.fs-in-chip', tabs).forEach(function (b) { b.addEventListener('click', function () { open(+b.dataset.i); }); });
    at.parentNode.insertBefore(g, at.nextSibling);
    open(0); if (Object.keys(built).length) { upd(); }
    else count.textContent = '🧩 0 models built';
  }

  /* ---------- Warm-Up: "Echo hunt" — click, time the echo, work out where the moth is (12.02) ----------
     D.echo = {afterText, kicker, title, todo[], why, img, alt, mothImg, credit, marks:[m,…] (meters), rounds:[m,…] (moth distance each round),
               wall:{m, t}, clickBtn, ask, needClick, closer, farther, foundLine, win, clue}
     Echo time = 2 × distance ÷ 343 m/s (the speed of sound in air), shown in ms (thousandths of a second). */
  function buildEcho() {
    var E = D.echo; if (!E) return;
    var at = null; $$('.tab-panel p').some(function (p) { if (E.afterText && p.textContent.indexOf(E.afterText) > -1) { at = p; return true; } });
    if (!at) { FAILED.push('echo anchor text not found'); return; }
    var g = gameShell(E.kicker || 'Warm-Up game', E.title, E.todo, E.why); g.dataset.mod = 'echo';
    var marks = E.marks || [1, 3, 6], far = Math.max.apply(null, marks) * 1.12;
    function xOf(m) { return 28 + 64 * m / far; }
    function ms(m) { return Math.round(2 * m / 343 * 1000); }
    var lane = el('div', 'fs-ec-lane', '<div class="fs-ec-bat"><img alt="' + esc(E.alt || '') + '" src="' + esc(E.img) + '"></div>' +
      marks.map(function (m) { return '<div class="fs-ec-mark" data-m="' + m + '" role="button" tabindex="0" style="left:' + xOf(m) + '%"><span class="fs-ec-fog">?</span><b>' + m + ' m</b></div>'; }).join('') +
      '<i class="fs-ec-ping"></i><i class="fs-ec-back"></i>');
    var wall = el('div', 'fs-ec-wall', '📏 ' + esc(E.wall.t));
    var ctl = el('div', 'fs-ec-ctl', '<button type="button" class="fs-btn fs-ec-click">' + esc(E.clickBtn || '🔊 Click!') + '</button><div class="fs-ec-read">—</div><div class="fs-card fs-ec-pin">📍 ' + esc(E.pin || 'The moth is here') + '</div>');
    var ask = el('div', 'fs-in-k fs-ec-ask'), miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), win = el('div', 'fs-win');
    g.appendChild(wall); g.appendChild(lane); g.appendChild(ctl); g.appendChild(ask); g.appendChild(miss); g.appendChild(count); g.appendChild(win);
    if (E.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(E.credit)));
    var rounds = E.rounds, r = Math.min(+store('echo') || 0, rounds.length), clicked = false, busy = false;
    var markEls = $$('.fs-ec-mark', lane), pin = $('.fs-ec-pin', ctl), read = $('.fs-ec-read', ctl);
    function upd() {
      count.textContent = '🦋 Moths found: ' + r + ' of ' + rounds.length; count.classList.toggle('ok', r === rounds.length);
      ask.textContent = r < rounds.length ? 'Round ' + (r + 1) + ': ' + (E.ask || 'Click, read the echo time, then show where the moth is.') : '';
      if (r === rounds.length) markEls.forEach(function (k) { k.classList.add('found'); $('.fs-ec-fog', k).innerHTML = '<img alt="" src="' + esc(E.mothImg) + '">'; });
      if (r === rounds.length && !win.classList.contains('show')) { win.innerHTML = esc(E.win); win.classList.add('show'); lane.classList.add('done'); $('.fs-ec-click', ctl).disabled = true; pin.classList.add('placed'); earnClue(E.clue || 'echo'); }
    }
    function reset() { clicked = false; read.textContent = '—'; markEls.forEach(function (k) { k.classList.remove('found', 'bad'); $('.fs-ec-fog', k).innerHTML = '?'; }); }
    $('.fs-ec-click', ctl).addEventListener('click', function () {
      if (busy || r >= rounds.length) return; busy = true; miss.classList.remove('show');
      var m = rounds[r], t = ms(m), vis = reduceMotion ? 0 : 220 + t * 34;
      tone(2600, 0, 0.03, 'square', 0.05);
      var ping = $('.fs-ec-ping', lane), back = $('.fs-ec-back', lane);
      [ping, back].forEach(function (p) { p.style.transition = 'none'; p.style.opacity = '0'; p.style.left = '12%'; });
      void lane.offsetWidth;
      if (vis) { ping.style.transition = 'left ' + vis / 2 + 'ms linear'; ping.style.opacity = '1'; ping.style.left = xOf(m) + '%'; }
      setTimeout(function () {
        ping.style.opacity = '0'; tone(2600, 0, 0.03, 'square', 0.018);
        if (vis) { back.style.transition = 'none'; back.style.left = xOf(m) + '%'; void back.offsetWidth; back.style.transition = 'left ' + vis / 2 + 'ms linear'; back.style.opacity = '1'; back.style.left = '12%'; }
        setTimeout(function () { back.style.opacity = '0'; read.innerHTML = 'Echo back in <b>' + t + ' ms</b>'; read.classList.remove('flash'); void read.offsetWidth; read.classList.add('flash'); clicked = true; busy = false; }, vis / 2);
      }, vis / 2);
    });
    function guess(item, mk) {
      if (r >= rounds.length) return;
      if (!clicked) { bounce(mk, miss, E.needClick || 'Click first, then read how long the echo took.'); return; }
      var m = +mk.dataset.m, real = rounds[r];
      if (m !== real) { mk.classList.add('bad'); bounce(mk, miss, (m < real ? E.farther : E.closer) || ''); return; }
      miss.classList.remove('show'); mk.classList.add('found'); $('.fs-ec-fog', mk).innerHTML = '<img alt="" src="' + esc(E.mothImg) + '">';
      SFX.whoosh(); lane.classList.remove('swoop'); void lane.offsetWidth; lane.classList.add('swoop'); lane.style.setProperty('--fs-ec-x', xOf(m) + '%');
      r++; store('echo', String(r)); clicked = false;
      var line = el('div', 'fs-sv-hint fs-ec-line', '✅ ' + esc((E.foundLine || 'Found it! {ms} ms means {m} m away.').replace('{ms}', ms(m)).replace('{m}', m)));
      ask.parentNode.insertBefore(line, miss); setTimeout(function () { line.remove(); if (r < rounds.length) reset(); upd(); }, reduceMotion ? 900 : 1700);
      if (r === rounds.length) upd();
    }
    dragDrop(pin, function () { return markEls; }, guess);
    markEls.forEach(function (k) {
      k.addEventListener('click', function () { pin.classList.remove('sel'); guess(pin, k); });
      k.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); guess(pin, k); } });
    });
    at.parentNode.insertBefore(g, at.nextSibling);
    upd();
  }

  /* ---------- Lesson: "Build a strong model" — steps in order, then arrows, then a caption, with a meter (12.02) ----------
     D.build = {afterText, kicker, title, todo[], why, img, alt, credit, name, slots:[{k,icon,t}]×4, cards:[{t,k}] (k 'x' = decoy), hint, missX, missSlot:{k:hint},
                arrows:[{q, opts:[{t,ok,miss}]}]×3, caption:{q, opts}, meter:[6 labels], win, clue} */
  function buildBuild() {
    var B = D.build; if (!B) return;
    var at = null; $$('.tab-panel p, .tab-panel ul').some(function (p) { if (B.afterText && p.textContent.indexOf(B.afterText) > -1) { at = p; return true; } });
    if (!at) { FAILED.push('build anchor text not found'); return; }
    if (at.tagName === 'P' && at.nextElementSibling && at.nextElementSibling.tagName === 'UL') at = at.nextElementSibling;
    var g = gameShell(B.kicker || 'Lesson game', B.title, B.todo, B.why); g.dataset.mod = 'build';
    var meter = el('div', 'fs-up-meter', '<div class="fs-up-bar"><i></i></div><div class="fs-up-lbl"></div>');
    var head = el('div', 'fs-bd-head', '<img alt="' + esc(B.alt || '') + '" src="' + esc(B.img) + '"><div><b>' + esc(B.name) + '</b><span>' + esc(B.sub || '') + '</span></div>');
    var row = el('div', 'fs-ch-row fs-bd-row'), pool = el('div', 'fs-ch-pool'), steps = el('div', 'fs-up-steps'), cap = el('div', 'fs-up-cap'), miss = el('div', 'fs-miss'), win = el('div', 'fs-win');
    g.appendChild(meter); g.appendChild(head); g.appendChild(row); g.appendChild(cap); g.appendChild(pool); g.appendChild(steps); g.appendChild(miss); g.appendChild(win);
    if (B.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credit</summary>' + esc(B.credit)));
    row.innerHTML = B.slots.map(function (s, k) { return (k ? '<span class="fs-ch-arw fs-bd-arw" data-a="' + (k - 1) + '"><i>→</i><em></em></span>' : '') + '<div class="fs-ch-slot" data-k="' + s.k + '" role="button" tabindex="0"><div class="fs-ch-h"><span>' + s.icon + '</span>' + esc(s.t) + '</div><div class="fs-ch-in"></div></div>'; }).join('');
    var slots = $$('.fs-ch-slot', row), arws = $$('.fs-bd-arw', row);
    var total = 2 + B.arrows.length, n = 0;
    function setMeter() { $('i', meter).style.width = (100 * n / total) + '%'; $('.fs-up-lbl', meter).textContent = B.meter[n] || ''; meter.classList.toggle('full', n === total); }
    var right = B.cards.filter(function (c) { return c.k !== 'x'; });
    function fillAll() { right.forEach(function (c) { var s = $('.fs-ch-slot[data-k="' + c.k + '"]', row); $('.fs-ch-in', s).textContent = c.t; s.classList.add('full'); }); }
    function setArrow(i, o) { var a = arws[i]; a.classList.add('on'); $('em', a).textContent = o.tag || o.t; }
    function finish(animate) { cap.textContent = B.caption.opts.filter(function (o) { return o.ok; })[0].t; cap.classList.add('show'); n = total; setMeter(); win.innerHTML = esc(B.win); win.classList.add('show'); if (animate) { SFX.win(); earnClue(B.clue || 'build'); } }
    function askArrow(i) {
      if (i >= B.arrows.length) { var w = chipsQ(steps, B.caption.q, B.caption.opts, function () { store('build', String(total)); finish(true); }, miss); w.classList.add('fs-up-step'); return; }
      arws.forEach(function (a, k) { a.classList.toggle('ask', k === i); });
      var w2 = chipsQ(steps, B.arrows[i].q, B.arrows[i].opts, function (o) { arws[i].classList.remove('ask'); setArrow(i, o); SFX.whoosh(); n = 2 + i; store('build', String(n)); setMeter(); setTimeout(function () { askArrow(i + 1); }, reduceMotion ? 0 : 350); }, miss);
      w2.classList.add('fs-up-step');
    }
    function drop(card, slot) {
      if (slot.classList.contains('full')) return;
      if (card.dataset.k !== slot.dataset.k) { bounce(card, miss, card.dataset.k === 'x' ? B.missX : (B.missSlot && B.missSlot[card.dataset.k]) || 'That card is a different step.'); return; }
      miss.classList.remove('show'); $('.fs-ch-in', slot).textContent = card.textContent; slot.classList.add('full'); card.remove(); SFX.chime();
      if (slots.every(function (s) { return s.classList.contains('full'); })) { pool.innerHTML = ''; n = 1; store('build', '1'); setMeter(); setTimeout(function () { askArrow(0); }, reduceMotion ? 0 : 350); }
    }
    at.parentNode.insertBefore(g, at.nextSibling);
    var saved = Math.min(+store('build') || 0, total);
    if (saved >= 1) {
      fillAll(); for (var i = 0; i < saved - 1 && i < B.arrows.length; i++) setArrow(i, B.arrows[i].opts.filter(function (o) { return o.ok; })[0]);
      n = saved; setMeter(); if (saved === total) finish(false); else askArrow(saved - 1);
      return;
    }
    setMeter();
    pool.appendChild(el('div', 'fs-sv-hint', '🔎 ' + esc(B.hint || 'Drag each card into its step, or tap a card and then a step.')));
    shuffle(B.cards).forEach(function (c) { var d = el('div', 'fs-card', esc(c.t)); d.dataset.k = c.k; pool.appendChild(d); dragDrop(d, function () { return slots.filter(function (s) { return !s.classList.contains('full'); }); }, drop); });
    tapTargets(g, slots, drop);
  }

  /* ---------- Lesson: "Match the sense" — four real pathway models; drop the sense organ that can pick up each stimulus, then compare (12.02) ----------
     D.compare = {replace, kicker, title, todo[], why, rows:[{k,icon,t}] (k: stim|sense|brain|resp), senseK, animals:[{id,name,img,alt,stim,sense,brain,resp,miss}], senses:[{id,t}], q, opts, credit, win, clue} */
  function buildCompare() {
    var C = D.compare; if (!C) return;
    var wrap = $(C.replace || '#tab-lesson .diagram-wrap'); if (!wrap) { FAILED.push('compare: nothing to replace'); return; }
    var g = gameShell(C.kicker || 'Lesson game', C.title, C.todo, C.why); g.dataset.mod = 'compare';
    var pv = wrap.previousElementSibling; if (pv && pv.tagName === 'P' && pv.textContent.length < 200) pv.classList.add('fs-hide-on');
    var grid = el('div', 'fs-cp-grid'), pool = el('div', 'fs-ch-pool fs-cp-pool'), qbox = el('div', 'fs-cp-q'), miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), win = el('div', 'fs-win');
    grid.innerHTML = C.animals.map(function (a) {
      return '<div class="fs-cp-card" data-id="' + a.id + '"><div class="fs-cp-top"><img alt="' + esc(a.alt || '') + '" src="' + esc(a.img) + '"><b>' + esc(a.name) + '</b></div>' +
        C.rows.map(function (rw) {
          var t = a[rw.k];
          return '<div class="fs-cp-row' + (rw.k === 'sense' ? ' fs-cp-drop' : '') + '" data-k="' + rw.k + '"' + (rw.k === 'sense' ? ' role="button" tabindex="0"' : '') + '><span class="fs-cp-h">' + rw.icon + ' ' + esc(rw.t) + '</span><span class="fs-cp-t">' + (rw.k === 'sense' ? '<i>' + esc(C.dropHere || 'Drop the sense organ here') + '</i>' : esc(t)) + '</span></div>';
        }).join('') + '</div>';
    }).join('');
    g.appendChild(grid); g.appendChild(pool); g.appendChild(miss); g.appendChild(count); g.appendChild(qbox); g.appendChild(win);
    if (C.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(C.credit)));
    var done = {}; try { done = JSON.parse(store('compare') || '{}'); } catch (e) {}
    var drops = $$('.fs-cp-drop', grid);
    function place(id) { var a = C.animals.filter(function (x) { return x.id === id; })[0], d = $('.fs-cp-card[data-id="' + id + '"] .fs-cp-drop', grid); $('.fs-cp-t', d).textContent = a.sense; d.classList.add('full'); }
    function upd() {
      var n = Object.keys(done).length; count.textContent = '👂 ' + n + ' of ' + C.animals.length + ' sense organs placed'; count.classList.toggle('ok', n === C.animals.length);
      if (n === C.animals.length && !qbox.dataset.on) {
        qbox.dataset.on = '1'; grid.classList.add('all'); pool.innerHTML = '';
        if (store('compare-q')) { var r = C.opts.filter(function (o) { return o.ok; })[0]; qbox.innerHTML = '<div class="fs-sv-q"><div class="fs-in-k">' + esc(C.q) + '</div><div class="fs-in-chips"><button type="button" class="fs-in-chip on ok">' + esc(r.t) + '</button></div></div>'; win.innerHTML = esc(C.win); win.classList.add('show'); return; }
        chipsQ(qbox, C.q, C.opts, function () { store('compare-q', '1'); win.innerHTML = esc(C.win); win.classList.add('show'); SFX.win(); earnClue(C.clue || 'compare'); }, miss);
      }
    }
    function drop(card, d) {
      if (d.classList.contains('full')) return;
      var id = d.parentNode.dataset.id, a = C.animals.filter(function (x) { return x.id === id; })[0];
      if (card.dataset.id !== id) { var s = C.senses.filter(function (x) { return x.id === card.dataset.id; })[0]; bounce(card, miss, (a.miss && a.miss[card.dataset.id]) || a.missAny || (s && s.miss) || 'Can that body part pick up this kind of stimulus?'); return; }
      miss.classList.remove('show'); card.remove(); done[id] = 1; store('compare', JSON.stringify(done)); place(id); SFX.chime(); upd();
    }
    Object.keys(done).forEach(place);
    shuffle(C.senses).forEach(function (s) { if (done[s.id]) return; var c = el('div', 'fs-card', esc(s.t)); c.dataset.id = s.id; pool.appendChild(c); dragDrop(c, function () { return drops.filter(function (x) { return !x.classList.contains('full'); }); }, drop); });
    tapTargets(g, drops, drop);
    wrap.classList.add('fs-replaced'); wrap.parentNode.insertBefore(g, wrap);
    upd();
  }

  /* ---------- Part 4: "Fix the broken models" — spot what's wrong, add the missing steps, run the model (12.02) ----------
     D.fix = {afterText, kicker, title, todo[], why, slots:[{k,icon,t}]×4, models:[{id,name,icon,img,alt,drawn:[t…], q, opts:[{t,ok,miss}], have:{k:t}, pool:[{t,k}], ran, why}], missX, missSlot, runBtn, credit, win, clue} */
  function buildFix() {
    var X = D.fix; if (!X) return;
    var at = null; $$('.tab-panel p').some(function (p) { if (X.afterText && p.textContent.indexOf(X.afterText) > -1) { at = p; return true; } });
    if (!at) { FAILED.push('fix anchor text not found'); return; }
    var g = gameShell(X.kicker || 'Part 4 game', X.title, X.todo, X.why); g.dataset.mod = 'fix';
    var tabs = el('div', 'fs-ch-tabs', X.models.map(function (m, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '"><span>' + m.icon + '</span>' + esc(m.name) + '<em></em></button>'; }).join(''));
    var stage = el('div', 'fs-fx-stage'), miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), win = el('div', 'fs-win');
    g.appendChild(tabs); g.appendChild(stage); g.appendChild(miss); g.appendChild(count); g.appendChild(win);
    if (X.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(X.credit)));
    var fixed = {}; try { fixed = JSON.parse(store('fix') || '{}'); } catch (e) {}
    function upd() {
      var n = Object.keys(fixed).length; count.textContent = '🛠 ' + n + ' of ' + X.models.length + ' models fixed'; count.classList.toggle('ok', n === X.models.length);
      $$('.fs-in-chip', tabs).forEach(function (b, i) { var ok = !!fixed[X.models[i].id]; b.classList.toggle('done', ok); $('em', b).textContent = ok ? ' ✓' : ''; });
      if (n === X.models.length && !win.classList.contains('show')) { win.innerHTML = esc(X.win); win.classList.add('show'); SFX.win(); earnClue(X.clue || 'fix'); }
    }
    function frame(m) {
      return '<div class="fs-ch-row fs-fx-row">' + X.slots.map(function (s, k) { var have = m.have[s.k]; return (k ? '<span class="fs-ch-arw">→</span>' : '') + '<div class="fs-ch-slot' + (have ? ' full given' : '') + '" data-k="' + s.k + '" role="button" tabindex="0"><div class="fs-ch-h"><span>' + s.icon + '</span>' + esc(s.t) + '</div><div class="fs-ch-in">' + (have ? esc(have) : '') + '</div></div>'; }).join('') + '<i class="fs-fx-pulse"></i></div>';
    }
    function ran(m, animate) {
      var res = el('div', 'fs-hs-card', '<span class="fs-hs-n">✅</span><div><b>' + esc(X.runOk || 'It runs!') + '</b>' + esc(m.why) + '</div>'); stage.appendChild(res);
      if (animate) { var row = $('.fs-fx-row', stage); row.classList.remove('run'); void row.offsetWidth; row.classList.add('run'); SFX.sparkle(); }
      var nx = X.models.map(function (o, i) { return fixed[o.id] ? -1 : i; }).filter(function (i) { return i > -1; })[0];
      if (nx != null) { var b = el('button', 'fs-btn alt fs-ch-next', 'Next model →'); b.type = 'button'; b.addEventListener('click', function () { open(nx); }); stage.appendChild(b); }
    }
    function open(i) {
      var m = X.models[i]; SFX.blip(); miss.classList.remove('show');
      $$('.fs-in-chip', tabs).forEach(function (b, k) { b.classList.toggle('on', k === i); });
      stage.innerHTML = '<div class="fs-fx-drawn"><img alt="' + esc(m.alt || '') + '" src="' + esc(m.img) + '"><div><div class="fs-fx-by">' + esc(m.by || 'A volunteer drew this model:') + '</div><div class="fs-fx-line">' + m.drawn.map(esc).join(' <b>→</b> ') + '</div></div></div>';
      if (fixed[m.id]) {
        var full = {}; X.slots.forEach(function (s) { full[s.k] = m.have[s.k] || m.pool.filter(function (c) { return c.k === s.k; })[0].t; });
        stage.insertAdjacentHTML('beforeend', frame({ have: full })); ran(m, false); return;
      }
      chipsQ(stage, m.q, m.opts, function () {
        stage.insertAdjacentHTML('beforeend', frame(m));
        var slots = $$('.fs-fx-row .fs-ch-slot:not(.given)', stage), pool = el('div', 'fs-ch-pool');
        pool.appendChild(el('div', 'fs-sv-hint', '🔎 ' + esc(X.hint || 'Drag the missing step into its box, or tap a card and then a box.')));
        stage.appendChild(pool);
        shuffle(m.pool).forEach(function (c) { var d = el('div', 'fs-card', esc(c.t)); d.dataset.k = c.k; pool.appendChild(d); dragDrop(d, function () { return slots.filter(function (s) { return !s.classList.contains('full'); }); }, drop); });
        tapTargets(stage, slots, drop);
        function drop(card, slot) {
          if (slot.classList.contains('full')) return;
          if (card.dataset.k !== slot.dataset.k) { bounce(card, miss, card.dataset.k === 'x' ? X.missX : (X.missSlot && X.missSlot[card.dataset.k]) || 'That card is a different step.'); return; }
          miss.classList.remove('show'); $('.fs-ch-in', slot).textContent = card.textContent; slot.classList.add('full'); card.remove(); SFX.chime();
          if (slots.every(function (s) { return s.classList.contains('full'); })) {
            pool.innerHTML = ''; var b = el('button', 'fs-btn', esc(X.runBtn || '▶ Run the model')); b.type = 'button'; pool.appendChild(b);
            b.addEventListener('click', function () { pool.remove(); fixed[m.id] = 1; store('fix', JSON.stringify(fixed)); ran(m, true); upd(); });
          }
        }
      }, miss);
    }
    $$('.fs-in-chip', tabs).forEach(function (b) { b.addEventListener('click', function () { open(+b.dataset.i); }); });
    at.parentNode.insertBefore(g, at.nextSibling);
    open(0); upd();
  }

  /* ---------- Warm-Up: "Find the family" — match each baby to its parent by inherited traits (13.01) ----------
     D.lineup = {afterText, kicker, title, todo[], why, hint, babies:[{id,name,img,alt}], parents:[{id,name,img,alt,same,diff,miss}], q, opts:[{t,ok,miss}], credit, win, clue}
     a baby's id equals its parent's id */
  function buildLineup() {
    var L = D.lineup; if (!L) return;
    var at = null; $$('.tab-panel p').some(function (p) { if (L.afterText && p.textContent.indexOf(L.afterText) > -1) { at = p; return true; } });
    if (!at) { FAILED.push('lineup anchor text not found'); return; }
    var g = gameShell(L.kicker || 'Warm-Up game', L.title, L.todo, L.why); g.dataset.mod = 'lineup';
    var tray = el('div', 'fs-lu-tray'), grid = el('div', 'fs-lu-grid'), info = el('div', 'fs-hs-card fs-lu-info', '<em>' + esc(L.hint || 'Drag a baby onto its parent, or tap a baby and then a parent.') + '</em>');
    var miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    tray.appendChild(el('div', 'fs-lu-lab', '🐣 The babies'));
    shuffle(L.babies).forEach(function (b) { var d = el('div', 'fs-card fs-lu-baby', '<img alt="' + esc(b.alt) + '" src="' + esc(b.img) + '"><span>' + esc(b.name) + '</span>'); d.dataset.id = b.id; tray.appendChild(d); });
    grid.appendChild(el('div', 'fs-lu-lab', '👪 The parents'));
    var row = el('div', 'fs-lu-row'); grid.appendChild(row);
    shuffle(L.parents).forEach(function (p) {
      var c = el('div', 'fs-lu-par', '<div class="fs-lu-ph"><img alt="' + esc(p.alt) + '" src="' + esc(p.img) + '"><span class="fs-lu-kid"></span></div><div class="fs-lu-n">' + esc(p.name) + '</div>');
      c.dataset.id = p.id; c.setAttribute('role', 'button'); c.tabIndex = 0; row.appendChild(c);
    });
    g.appendChild(tray); g.appendChild(grid); g.appendChild(info); g.appendChild(miss); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    if (L.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(L.credit)));
    var done = {}; try { done = JSON.parse(store('lineup') || '{}'); } catch (e) {}
    var targets = $$('.fs-lu-par', row);
    function par(id) { return L.parents.filter(function (p) { return p.id === id; })[0]; }
    function baby(id) { return L.babies.filter(function (b) { return b.id === id; })[0]; }
    function place(id, animate) {
      var c = $('.fs-lu-par[data-id="' + id + '"]', row), k = $('.fs-lu-kid', c), b = baby(id);
      c.classList.add('done'); k.innerHTML = '<img alt="" src="' + esc(b.img) + '">'; k.classList.add('on');
      if (animate && !reduceMotion) { k.classList.remove('pop'); void k.offsetWidth; k.classList.add('pop'); }
      var t = $('.fs-lu-baby[data-id="' + id + '"]', tray); if (t) { t.classList.add('placed'); t.classList.remove('sel'); }
    }
    function ask() {
      if (qh.dataset.on) return; qh.dataset.on = '1';
      chipsQ(qh, L.q, L.opts, function () { store('lineup-q', '1'); finish(); }, miss);
      if (store('lineup-q')) { var ok = L.opts.map(function (o, i) { return o.ok ? i : -1; }).filter(function (i) { return i > -1; })[0]; var c = $$('.fs-in-chip', qh)[ok]; if (c) c.classList.add('on', 'ok'); $('.fs-sv-q', qh).dataset.done = '1'; finish(); }
    }
    function finish() { if (win.classList.contains('show')) return; win.innerHTML = esc(L.win); win.classList.add('show'); SFX.win(); earnClue(L.clue || 'lineup'); }
    function upd() {
      var n = Object.keys(done).length; count.textContent = '👪 ' + n + ' of ' + L.parents.length + ' families found'; count.classList.toggle('ok', n === L.parents.length);
      if (n === L.parents.length) ask();
    }
    function drop(tk, c) {
      var p = par(c.dataset.id); if (!p || done[p.id]) return;
      if (tk.dataset.id !== p.id) { var b = baby(tk.dataset.id); bounce(tk, miss, (b && b.miss) || p.miss || 'Look at the body shape, not the color. Which parent has the same shape?'); return; }
      miss.classList.remove('show'); done[p.id] = 1; store('lineup', JSON.stringify(done)); SFX.chime(); place(p.id, true);
      info.innerHTML = '<span class="fs-hs-n">✓</span><div><b>' + esc(p.name) + ' family</b><span class="fs-lu-same">👪 Same as the parent: ' + esc(p.same) + '</span><span class="fs-lu-diff">🔄 Different for now: ' + esc(p.diff) + '</span></div>';
      info.classList.remove('flash'); void info.offsetWidth; info.classList.add('flash'); upd();
    }
    $$('.fs-lu-baby', tray).forEach(function (t) { dragDrop(t, function () { return targets.filter(function (x) { return !x.classList.contains('done'); }); }, drop); });
    tapTargets(g, targets, drop);
    targets.forEach(function (c) { c.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); var s = $('.sel', g); if (s) { s.classList.remove('sel'); drop(s, c); } } }); });
    Object.keys(done).forEach(function (id) { if (par(id)) place(id, false); });
    at.parentNode.insertBefore(g, at.nextSibling);
    upd();
  }

  /* ---------- Lesson: "Grow the twins" — two seeds from one parent, change the garden (13.01) ----------
     D.grow = {afterText, kicker, title, todo[], why, model, dials:[{k,t,opts:[{k,icon,t}]}], results:{"<opt>-<opt>":{img,h,w,flowers,note}}, fixed:[{t,v}], measures:[{k,t,unit}],
               need:{dialK:[optK,optK]}, needLine, growBtn, weeks, q, opts:[{t,ok,miss}], credit, win, clue}
     results keys are the dial option keys joined with "-" in dial order; h = height in cm (also scales the photo) */
  function buildGrow() {
    var G = D.grow; if (!G) return;
    var at = null; $$('.tab-panel p').some(function (p) { if (G.afterText && p.textContent.indexOf(G.afterText) > -1) { at = p; return true; } });
    if (!at) { FAILED.push('grow anchor text not found'); return; }
    var g = gameShell(G.kicker || 'Part 2 game', G.title, G.todo, G.why); g.dataset.mod = 'grow';
    if (G.model) g.appendChild(el('div', 'fs-gr-model', '🧪 ' + esc(G.model)));
    var pots = el('div', 'fs-gr-pots'), log = el('div', 'fs-gr-log'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(pots); g.appendChild(log); g.appendChild(miss); g.appendChild(qh); g.appendChild(win);
    if (G.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(G.credit)));
    var tried = {}; try { tried = JSON.parse(store('grow') || '{}'); } catch (e) {}
    var maxH = Math.max.apply(null, Object.keys(G.results).map(function (k) { return G.results[k].h; }));
    ['A', 'B'].forEach(function (name, pi) {
      var p = el('div', 'fs-gr-pot');
      p.innerHTML = '<div class="fs-gr-h">🌱 ' + esc(G.potLabel || 'Pot') + ' ' + name + ' <small>' + esc(G.seedLine || 'a seed from the same parent plant') + '</small></div>' +
        G.dials.map(function (d) { return '<div class="fs-gr-dial" data-k="' + d.k + '"><span>' + esc(d.t) + '</span>' + d.opts.map(function (o, oi) { return '<button type="button" class="fs-in-chip' + (oi === (pi === 0 ? 0 : d.opts.length - 1) ? ' on' : '') + '" data-o="' + o.k + '">' + o.icon + ' ' + esc(o.t) + '</button>'; }).join('') + '</div>'; }).join('') +
        '<div class="fs-gr-bed"><div class="fs-gr-ruler"></div><div class="fs-gr-plant"><img alt="" src=""></div><div class="fs-gr-seed">🌰</div></div><div class="fs-gr-res"><em>' + esc(G.startLine || 'Pick a garden, then press Grow.') + '</em></div>';
      $$('.fs-gr-dial', p).forEach(function (row) { $$('.fs-in-chip', row).forEach(function (b) { b.addEventListener('click', function () { $$('.fs-in-chip', row).forEach(function (x) { x.classList.toggle('on', x === b); }); SFX.blip(); reset(p); }); }); });
      pots.appendChild(p);
    });
    var btn = el('button', 'fs-btn fs-gr-go', esc(G.growBtn || '▶ Grow both pots')); btn.type = 'button'; g.insertBefore(btn, log);
    function keyOf(p) { return G.dials.map(function (d) { return $('.fs-gr-dial[data-k="' + d.k + '"] .on', p).dataset.o; }).join('-'); }
    function reset(p) { p.classList.remove('grown'); $('.fs-gr-plant', p).style.height = '0%'; $('.fs-gr-res', p).innerHTML = '<em>Press Grow to see what happens.</em>'; }
    function show(p, r, animate) {
      var pl = $('.fs-gr-plant', p), im = $('img', pl);
      im.src = r.img; im.alt = r.alt || '';
      pl.style.width = (r.w || 80) + '%';
      if (animate && !reduceMotion) { pl.style.transition = 'none'; pl.style.height = '0%'; void pl.offsetWidth; pl.style.transition = ''; }
      pl.style.height = Math.round(18 + 82 * r.h / maxH) + '%'; p.classList.add('grown');
      $('.fs-gr-res', p).innerHTML = '<table>' + G.measures.map(function (m) { return '<tr><th>' + esc(m.t) + '</th><td>' + esc(String(r[m.k])) + (m.unit ? ' ' + esc(m.unit) : '') + '</td></tr>'; }).join('') +
        (G.fixed || []).map(function (f) { return '<tr class="fs-gr-fx"><th>' + esc(f.t) + '</th><td>' + esc(f.v) + '</td></tr>'; }).join('') + '</table>' + (r.note ? '<p>' + esc(r.note) + '</p>' : '');
    }
    function enough() {
      return Object.keys(G.need || {}).every(function (dk) { var di = G.dials.map(function (d) { return d.k; }).indexOf(dk); return G.need[dk].every(function (ok) { return Object.keys(tried).some(function (k) { return k.split('-')[di] === ok; }); }); });
    }
    function upd() {
      var keys = Object.keys(tried);
      log.innerHTML = keys.length ? '<b>📒 ' + esc(G.logLabel || 'Gardens you tried:') + '</b> ' + keys.map(function (k) { var r = G.results[k]; return '<span class="fs-gr-chip">' + esc(r.label || k) + ': ' + r.h + ' cm, ' + (G.logK ? esc(String(r[G.logK])) : r.flowers + ' 🌼') + '</span>'; }).join(' ') : '';
      if (enough() && !qh.dataset.on) {
        qh.dataset.on = '1';
        chipsQ(qh, G.q, G.opts, function () { store('grow-q', '1'); finish(); }, miss);
        if (store('grow-q')) { var i = G.opts.map(function (o, j) { return o.ok ? j : -1; }).filter(function (j) { return j > -1; })[0]; $$('.fs-in-chip', qh)[i].classList.add('on', 'ok'); $('.fs-sv-q', qh).dataset.done = '1'; finish(); }
      } else if (keys.length && !enough()) { miss.innerHTML = '🔎 ' + esc(G.needLine || 'Try a sunny pot AND a shady pot.'); miss.classList.add('show'); }
    }
    function finish() { if (win.classList.contains('show')) return; miss.classList.remove('show'); win.innerHTML = esc(G.win); win.classList.add('show'); SFX.win(); earnClue(G.clue || 'grow'); }
    btn.addEventListener('click', function () {
      $$('.fs-gr-pot', pots).forEach(function (p) { var k = keyOf(p), r = G.results[k]; if (!r) return; tried[k] = 1; show(p, r, true); });
      store('grow', JSON.stringify(tried)); SFX.sparkle(); upd();
    });
    at.parentNode.insertBefore(g, at.nextSibling);
    upd();
  }

  /* ---------- Warm-Up: "Trace your lunch" — pick a food, then step backward until you reach the Sun (9.01) ----------
     D.trace = {afterText, kicker, title, todo[], why, pick, need, sunLine, arrowNote,
                foods:[{id, icon, name, steps:[{q, opts:[{t, icon, ok, miss}]}], end}], count, win, clue}
     each right answer adds its icon to the LEFT of the trail; the last step's right answer is the Sun */
  function buildTrace() {
    var T = D.trace; if (!T) return;
    var at = null; $$('.tab-panel p').some(function (p) { if (T.afterText && p.textContent.indexOf(T.afterText) > -1) { at = p; return true; } });
    if (!at) { FAILED.push('trace anchor text not found'); return; }
    var g = gameShell(T.kicker || 'Warm-Up game', T.title, T.todo, T.why); g.dataset.mod = 'trace';
    var picks = el('div', 'fs-tc-picks', '<div class="fs-in-k">' + esc(T.pick || 'Pick a food:') + '</div><div class="fs-in-chips">' + T.foods.map(function (f, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '"><span>' + f.icon + '</span> ' + esc(f.name) + '<em></em></button>'; }).join('') + '</div>');
    var trail = el('div', 'fs-tc-trail'), note = el('div', 'fs-tc-note', esc(T.arrowNote || 'The arrows show which way the energy moved.'));
    var stage = el('div', 'fs-tc-stage'), miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), win = el('div', 'fs-win');
    g.appendChild(picks); g.appendChild(trail); g.appendChild(note); g.appendChild(stage); g.appendChild(miss); g.appendChild(count); g.appendChild(win);
    var done = {}; try { done = JSON.parse(store('trace') || '{}'); } catch (e) {}
    var need = Math.min(T.need || 2, T.foods.length);
    function rights(f) { return f.steps.map(function (s) { return s.opts.filter(function (o) { return o.ok; })[0]; }); }
    function drawTrail(f, n, animate) {
      var items = rights(f).slice(0, n).reverse().map(function (o) { return { icon: o.icon, t: o.short || o.t }; });
      items.push({ icon: f.icon, t: f.name, food: true });
      trail.innerHTML = items.map(function (it, k) {
        var sun = k === 0 && n === f.steps.length;
        return (k ? '<span class="fs-tc-arw">→</span>' : '') + '<div class="fs-tc-node' + (it.food ? ' food' : '') + (sun ? ' sun' : '') + (animate && k === 0 && n > 0 ? ' pop' : '') + '"><span>' + it.icon + '</span><b>' + esc(it.t) + '</b></div>';
      }).join('');
      if (n === f.steps.length && animate) { trail.classList.remove('glow'); void trail.offsetWidth; trail.classList.add('glow'); }
    }
    function upd() {
      var n = Object.keys(done).length;
      count.textContent = '☀️ ' + n + ' of ' + need + ' foods traced to the start';
      count.classList.toggle('ok', n >= need);
      $$('.fs-in-chip', picks).forEach(function (b) { var ok = !!done[T.foods[+b.dataset.i].id]; b.classList.toggle('done', ok); $('em', b).textContent = ok ? ' ✓' : ''; });
      if (n >= need && !win.classList.contains('show')) { win.innerHTML = esc(T.win); win.classList.add('show'); SFX.win(); earnClue(T.clue || 'trace'); }
    }
    function open(i) {
      var f = T.foods[i]; SFX.blip(); miss.classList.remove('show');
      $$('.fs-in-chip', picks).forEach(function (b) { b.classList.toggle('on', +b.dataset.i === i); });
      stage.innerHTML = '';
      if (done[f.id]) { drawTrail(f, f.steps.length, false); stage.appendChild(el('div', 'fs-hs-card', '<span class="fs-hs-n">☀️</span><div>' + esc(f.end || T.sunLine) + '</div>')); return; }
      drawTrail(f, 0, false);
      (function ask(s) {
        if (s >= f.steps.length) {
          done[f.id] = 1; store('trace', JSON.stringify(done)); SFX.sparkle();
          stage.appendChild(el('div', 'fs-hs-card', '<span class="fs-hs-n">☀️</span><div>' + esc(f.end || T.sunLine) + '</div>'));
          var nx = T.foods.map(function (o, k) { return done[o.id] ? -1 : k; }).filter(function (k) { return k > -1; })[0];
          if (nx != null) { var b = el('button', 'fs-btn alt fs-ch-next', 'Trace another food →'); b.type = 'button'; b.addEventListener('click', function () { open(nx); }); stage.appendChild(b); }
          upd(); return;
        }
        var w = chipsQ(stage, f.steps[s].q, f.steps[s].opts, function () {
          w.classList.add('fs-tc-done'); drawTrail(f, s + 1, true); SFX.whoosh();
          setTimeout(function () { ask(s + 1); }, reduceMotion ? 0 : 300);
        }, miss);
      })(0);
    }
    $$('.fs-in-chip', picks).forEach(function (b) { b.addEventListener('click', function () { open(+b.dataset.i); }); });
    trail.innerHTML = '<div class="fs-tc-empty">' + esc(T.empty || '👆 Pick a food to start your trail.') + '</div>';
    at.parentNode.insertBefore(g, at.nextSibling);
    upd();
  }

  /* ---------- Lesson: "Missing link" sim — remove one link, predict, run four seasons (9.02) ----------
     D.wobble = {replace (default '#tab-lesson .diagram-wrap'), kicker, title, todo[], why, model, seasons:[labels], seasonsShort:[phone labels], seasonsHead, nodes:[{id,icon,name}],
                 opts:[{k:'up'|'down'|'same', icon, t}], removes:[{id, btn, series:{nodeId:[n…]}, answer:{nodeId:k}, notes:{nodeId:t}, why}],
                 need:[removeId…], needLine, runBtn, q, opts2:[{t,ok,miss}], win, clue}
     answers are about the FIRST season; the bars keep going so students see what happens later (boom, then crash) */
  function buildWobble() {
    var W = D.wobble; if (!W) return;
    var wrap = $(W.replace || '#tab-lesson .diagram-wrap'); if (!wrap) { FAILED.push('wobble: nothing to replace'); return; }
    var g = gameShell(W.kicker || 'Lesson game', W.title, W.todo, W.why); g.dataset.mod = 'wobble';
    var pv = wrap.previousElementSibling; if (pv && pv.tagName === 'P' && pv.textContent.length < 200) pv.classList.add('fs-hide-on');
    if (W.model) g.appendChild(el('div', 'fs-gr-model', '🧪 ' + esc(W.model)));
    var picks = el('div', 'fs-wb-picks', '<div class="fs-in-k">' + esc(W.pickLine || '1. Pick one living thing to remove:') + '</div><div class="fs-in-chips">' + W.removes.map(function (r, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(r.btn) + '<em></em></button>'; }).join('') + '</div>');
    var stage = el('div', 'fs-wb-stage', '<div class="fs-hs-card"><em>' + esc(W.startLine || 'Pick a living thing to remove. Then predict what happens to the others.') + '</em></div>');
    var miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(picks); g.appendChild(stage); g.appendChild(miss); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    var ran = {}; try { ran = JSON.parse(store('wobble') || '{}'); } catch (e) {}
    var OPT = {}; W.opts.forEach(function (o) { OPT[o.k] = o; });
    function node(id) { return W.nodes.filter(function (n) { return n.id === id; })[0]; }
    function upd() {
      var n = Object.keys(ran).length, need = W.need || W.removes.map(function (r) { return r.id; });
      count.textContent = '🧪 ' + n + ' of ' + W.removes.length + ' tests run';
      $$('.fs-in-chip', picks).forEach(function (b) { var ok = !!ran[W.removes[+b.dataset.i].id]; b.classList.toggle('done', ok); $('em', b).textContent = ok ? ' ✓' : ''; });
      var enough = need.every(function (id) { return ran[id]; });
      count.classList.toggle('ok', enough);
      if (enough && !qh.dataset.on) {
        qh.dataset.on = '1';
        chipsQ(qh, W.q, W.opts2, function () { store('wobble-q', '1'); finish(); }, miss);
        if (store('wobble-q')) { var i = W.opts2.map(function (o, j) { return o.ok ? j : -1; }).filter(function (j) { return j > -1; })[0]; $$('.fs-in-chip', qh)[i].classList.add('on', 'ok'); $('.fs-sv-q', qh).dataset.done = '1'; finish(); }
      } else if (!enough && n) { miss.innerHTML = '🔎 ' + esc(W.needLine || 'Run another test.'); miss.classList.add('show'); }
    }
    function finish() { if (win.classList.contains('show')) return; miss.classList.remove('show'); win.innerHTML = esc(W.win); win.classList.add('show'); SFX.win(); earnClue(W.clue || 'wobble'); }
    function chart(r) {
      var max = 100;
      return '<div class="fs-wb-chart"><div class="fs-wb-seasons"><span>' + esc(W.seasonsHead || 'Season →') + '</span>' + W.seasons.map(function (s, i) { var sh = (W.seasonsShort || [])[i]; return '<b data-s="' + i + '">' + (sh ? '<i class="l">' + esc(s) + '</i><i class="s">' + esc(sh) + '</i>' : esc(s)) + '</b>'; }).join('') + '</div>' +
        W.nodes.map(function (n) {
          var gone = n.id === r.id, ser = gone ? W.seasons.map(function (s, i) { return i ? 0 : (r.start || 50); }) : (r.series[n.id] || []);
          return '<div class="fs-wb-row' + (gone ? ' gone' : '') + '" data-id="' + n.id + '"><span class="fs-wb-n">' + n.icon + ' ' + esc(n.name) + (gone ? ' <small>removed</small>' : '') + '</span>' +
            ser.map(function (v, i) { return '<span class="fs-wb-cell" data-s="' + i + '"><i style="height:' + Math.max(2, 100 * v / max) + '%"></i></span>'; }).join('') + '</div>';
        }).join('') + '</div>';
    }
    function results(r) {
      return '<ul class="fs-wb-out">' + W.nodes.filter(function (n) { return n.id !== r.id; }).map(function (n) {
        var a = OPT[r.answer[n.id]], gs = r.guess && r.guess[n.id], right = gs ? gs === r.answer[n.id] : true;
        return '<li class="' + (right ? 'right' : 'wrong') + '"><b>' + n.icon + ' ' + esc(n.name) + ': ' + a.icon + ' ' + esc(a.t) + ' first</b>' + esc(r.notes[n.id] || '') + (gs && !right ? ' <em class="fs-pi-oops">(Your guess was different. Now you know why!)</em>' : '') + '</li>';
      }).join('') + '</ul>' + (r.why ? '' : '');
    }
    function play(r, animate) {
      var box = $('.fs-wb-res', stage); box.innerHTML = chart(r);
      var cells = $$('.fs-wb-cell', box), heads = $$('.fs-wb-seasons b', box), S = W.seasons.length;
      function show(k) { cells.forEach(function (c) { c.classList.toggle('on', +c.dataset.s <= k); }); heads.forEach(function (h) { h.classList.toggle('on', +h.dataset.s === k); }); }
      function done() { box.insertAdjacentHTML('beforeend', results(r)); if (r.why) box.appendChild(whyCard(r.why)); ran[r.id] = 1; store('wobble', JSON.stringify(ran)); upd(); }
      if (!animate || reduceMotion) { show(S - 1); done(); return; }
      var k = 0; show(0); SFX.whoosh();
      (function step() { k++; if (k >= S) { SFX.chime(); done(); return; } setTimeout(function () { show(k); SFX.blip(); step(); }, 650); })();
    }
    function open(i) {
      var r = W.removes[i]; SFX.blip(); miss.classList.remove('show'); r.guess = {};
      $$('.fs-in-chip', picks).forEach(function (b) { b.classList.toggle('on', +b.dataset.i === i); });
      var others = W.nodes.filter(function (n) { return n.id !== r.id; });
      stage.innerHTML = '<div class="fs-in-k">' + esc(W.predictLine || '2. Predict: after the first season, will each of the others have more, fewer, or about the same?') + '</div>' +
        '<div class="fs-wb-pred">' + others.map(function (n) { return '<div class="fs-pi-tr" data-id="' + n.id + '"><div class="fs-pi-t"><span>' + n.icon + '</span>' + esc(n.name) + '</div><div class="fs-pi-bt">' +
          W.opts.map(function (o) { return '<button type="button" class="fs-in-chip" data-k="' + o.k + '">' + o.icon + ' ' + esc(o.t) + '</button>'; }).join('') + '</div></div>'; }).join('') + '</div>' +
        '<div class="fs-pi-go"><button type="button" class="fs-btn"' + (ran[r.id] ? '' : ' disabled') + '>' + esc(W.runBtn || '▶ Run 4 seasons') + '</button><small>' + esc(W.guessFirst || 'Make a guess for each one first.') + '</small></div><div class="fs-wb-res"></div>';
      var go = $('.fs-pi-go .fs-btn', stage);
      $$('.fs-pi-tr', stage).forEach(function (row) { $$('.fs-in-chip', row).forEach(function (b) { b.addEventListener('click', function () {
        if (stage.classList.contains('ran')) return;
        $$('.fs-in-chip', row).forEach(function (x) { x.classList.toggle('on', x === b); }); r.guess[row.dataset.id] = b.dataset.k; SFX.blip();
        go.disabled = Object.keys(r.guess).length < others.length;
      }); }); });
      stage.classList.remove('ran');
      go.addEventListener('click', function () { stage.classList.add('ran'); go.disabled = true; play(r, true); });
      if (ran[r.id]) { stage.classList.add('ran'); go.disabled = true; play(r, false); }
    }
    $$('.fs-in-chip', picks).forEach(function (b) { b.addEventListener('click', function () { open(+b.dataset.i); }); });
    wrap.classList.add('fs-replaced'); wrap.parentNode.insertBefore(g, wrap);
    upd();
  }

  /* ---------- Lesson Part 4: "Pass it on?" — predict which of a parent's traits the babies get (13.01) ----------
     D.passiton = {afterText, kicker, title, todo[], why, parent:{name,img,alt}, kids:{name,img,alt}, yes, no, traits:[{id,icon,t,pass,why}], nextBtn, q, opts, credit, win, clue} */
  function buildPassiton() {
    var P = D.passiton; if (!P) return;
    var at = null; $$('.tab-panel p').some(function (p) { if (P.afterText && p.textContent.indexOf(P.afterText) > -1) { at = p; return true; } });
    if (!at) { FAILED.push('passiton anchor text not found'); return; }
    var g = gameShell(P.kicker || 'Part 4 game', P.title, P.todo, P.why); g.dataset.mod = 'passiton';
    var stage = el('div', 'fs-pi-stage'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    stage.innerHTML = '<div class="fs-pi-gen"><div class="fs-pi-ph"><img alt="' + esc(P.parent.alt) + '" src="' + esc(P.parent.img) + '"></div><b>' + esc(P.parent.name) + '</b></div>' +
      '<div class="fs-pi-list">' + P.traits.map(function (t, i) { return '<div class="fs-pi-tr" data-i="' + i + '"><div class="fs-pi-t"><span>' + t.icon + '</span>' + esc(t.t) + '</div><div class="fs-pi-bt"><button type="button" class="fs-in-chip" data-v="1">✅ ' + esc(P.yes || 'Passed to the kittens') + '</button><button type="button" class="fs-in-chip" data-v="0">✋ ' + esc(P.no || 'Stays with mom') + '</button></div></div>'; }).join('') + '</div>' +
      '<div class="fs-pi-go"><button type="button" class="fs-btn" disabled>' + esc(P.nextBtn || '▶ Next generation') + '</button><small>Make a guess for every trait first.</small></div>' +
      '<div class="fs-pi-gen fs-pi-kids"><div class="fs-pi-ph"><img alt="' + esc(P.kids.alt) + '" src="' + esc(P.kids.img) + '"><span class="fs-pi-veil">?</span></div><b>' + esc(P.kids.name) + '</b><ul class="fs-pi-out"></ul></div>';
    g.appendChild(stage); g.appendChild(miss); g.appendChild(qh); g.appendChild(win);
    if (P.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(P.credit)));
    var guess = {}, go = $('.fs-pi-go .fs-btn', stage), kids = $('.fs-pi-kids', stage), out = $('.fs-pi-out', stage);
    $$('.fs-pi-tr', stage).forEach(function (row) { $$('.fs-in-chip', row).forEach(function (b) { b.addEventListener('click', function () {
      if (stage.classList.contains('ran')) return;
      $$('.fs-in-chip', row).forEach(function (x) { x.classList.toggle('on', x === b); }); guess[row.dataset.i] = b.dataset.v === '1'; SFX.blip();
      go.disabled = Object.keys(guess).length < P.traits.length;
    }); }); });
    function run(animate) {
      stage.classList.add('ran'); go.disabled = true; kids.classList.add('born');
      if (animate) { SFX.whoosh(); }
      out.innerHTML = '';
      P.traits.forEach(function (t, i) {
        var right = guess[i] === undefined ? true : guess[i] === t.pass;
        var li = el('li', t.pass ? 'yes' : 'no', '<b>' + t.icon + ' ' + (t.pass ? '✅ ' : '✋ ') + esc(t.short || t.t) + '</b>' + esc(t.why) + (right ? '' : ' <em class="fs-pi-oops">(Your guess was different. Now you know why!)</em>'));
        if (animate && !reduceMotion) li.style.animationDelay = (0.25 + i * 0.35) + 's';
        out.appendChild(li);
        var row = $('.fs-pi-tr[data-i="' + i + '"]', stage); row.classList.add(t.pass ? 'yes' : 'no');
        if (guess[i] !== undefined) row.classList.add(right ? 'right' : 'wrong');
      });
      store('passiton', '1');
      if (!qh.dataset.on) { qh.dataset.on = '1'; chipsQ(qh, P.q, P.opts, function () { store('passiton-q', '1'); finish(); }, miss);
        if (store('passiton-q')) { var i = P.opts.map(function (o, j) { return o.ok ? j : -1; }).filter(function (j) { return j > -1; })[0]; $$('.fs-in-chip', qh)[i].classList.add('on', 'ok'); $('.fs-sv-q', qh).dataset.done = '1'; finish(); } }
    }
    function finish() { if (win.classList.contains('show')) return; win.innerHTML = esc(P.win); win.classList.add('show'); SFX.win(); earnClue(P.clue || 'passiton'); }
    go.addEventListener('click', function () { run(true); });
    at.parentNode.insertBefore(g, at.nextSibling);
    if (store('passiton')) run(false);
  }

  /* ---------- Warm-Up: "Pollen pass" — fly a bee from flower to flower (13.02) ----------
     D.pollen = {afterText, kicker, title, todo[], why, bee:{img,alt}, start, flowers:[{id,name,img,alt,kind}], kind, wrongKind, needPollen, done, q, opts, credit, win, clue}
     the bee starts on flower `start` dusted with pollen; dropping it on another flower of `kind` pollinates it */
  function buildPollen() {
    var P = D.pollen; if (!P) return;
    var at = null; $$('.tab-panel p').some(function (p) { if (P.afterText && p.textContent.indexOf(P.afterText) > -1) { at = p; return true; } });
    if (!at) { FAILED.push('pollen anchor text not found'); return; }
    var g = gameShell(P.kicker || 'Warm-Up game', P.title, P.todo, P.why); g.dataset.mod = 'pollen';
    var field = el('div', 'fs-po-field'), info = el('div', 'fs-hs-card fs-po-info', '<em>' + esc(P.hint || 'Drag the bee to a flower, or tap the bee and then a flower.') + '</em>');
    var miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    P.flowers.forEach(function (f) {
      var c = el('div', 'fs-po-fl', '<div class="fs-po-ph"><img alt="' + esc(f.alt) + '" src="' + esc(f.img) + '"><span class="fs-po-mark"></span></div><div class="fs-po-n">' + esc(f.name) + '</div>');
      c.dataset.id = f.id; c.setAttribute('role', 'button'); c.tabIndex = 0; field.appendChild(c);
    });
    var bee = el('div', 'fs-po-bee', '<img alt="' + esc(P.bee.alt) + '" src="' + esc(P.bee.img) + '"><span class="fs-po-dust"></span>'); bee.setAttribute('role', 'button'); bee.tabIndex = 0;
    g.appendChild(field); g.appendChild(info); g.appendChild(miss); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    if (P.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(P.credit)));
    var done = {}; try { done = JSON.parse(store('pollen') || '{}'); } catch (e) {}
    var targets = $$('.fs-po-fl', field), need = P.flowers.filter(function (f) { return f.kind === P.kind && f.id !== P.start; });
    function fl(id) { return P.flowers.filter(function (f) { return f.id === id; })[0]; }
    function sitOn(id, animate) {
      var c = $('.fs-po-fl[data-id="' + id + '"] .fs-po-ph', field); if (!c) return;
      c.appendChild(bee); bee.classList.add('dusty'); if (animate && !reduceMotion) { bee.classList.remove('land'); void bee.offsetWidth; bee.classList.add('land'); }
    }
    function mark(id) { var c = $('.fs-po-fl[data-id="' + id + '"]', field); c.classList.add('done'); $('.fs-po-mark', c).textContent = '🌰'; }
    function upd() {
      var n = need.filter(function (f) { return done[f.id]; }).length;
      count.textContent = '🌼 ' + n + ' of ' + need.length + ' ' + (P.countWord || 'flowers pollinated'); count.classList.toggle('ok', n === need.length);
      if (n === need.length && !qh.dataset.on) {
        qh.dataset.on = '1'; chipsQ(qh, P.q, P.opts, function () { store('pollen-q', '1'); finish(); }, miss);
        if (store('pollen-q')) { var i = P.opts.map(function (o, j) { return o.ok ? j : -1; }).filter(function (j) { return j > -1; })[0]; $$('.fs-in-chip', qh)[i].classList.add('on', 'ok'); $('.fs-sv-q', qh).dataset.done = '1'; finish(); }
      }
    }
    function finish() { if (win.classList.contains('show')) return; win.innerHTML = esc(P.win); win.classList.add('show'); SFX.win(); earnClue(P.clue || 'pollen'); }
    function visit(c) {
      var f = fl(c.dataset.id); if (!f) return; bee.classList.remove('sel');
      sitOn(f.id, true); SFX.blip();
      if (f.kind !== P.kind) { miss.innerHTML = '🔎 ' + esc(f.miss || P.wrongKind); miss.classList.remove('show'); void miss.offsetWidth; miss.classList.add('show'); info.innerHTML = '<span class="fs-hs-n">🐝</span><div><b>' + esc(f.name) + '</b>' + esc(f.t || '') + '</div>'; return; }
      miss.classList.remove('show');
      if (f.id === P.start || done[f.id]) { info.innerHTML = '<span class="fs-hs-n">🐝</span><div><b>' + esc(f.name) + '</b>' + esc(f.id === P.start ? P.startLine : P.again) + '</div>'; return; }
      done[f.id] = 1; store('pollen', JSON.stringify(done)); mark(f.id); SFX.chime();
      info.innerHTML = '<span class="fs-hs-n">✓</span><div><b>' + esc(f.name) + '</b>' + esc(P.done) + '</div>'; info.classList.remove('flash'); void info.offsetWidth; info.classList.add('flash');
      upd();
    }
    /* drag the bee (pointer) or tap bee then flower */
    var start = null, ghost = null;
    bee.addEventListener('pointerdown', function (e) { start = { x: e.clientX, y: e.clientY }; bee.setPointerCapture && bee.setPointerCapture(e.pointerId); e.stopPropagation(); });
    bee.addEventListener('pointermove', function (e) {
      if (!start) return;
      if (!ghost && Math.abs(e.clientX - start.x) + Math.abs(e.clientY - start.y) > 8) { ghost = bee.cloneNode(true); ghost.className = 'fs-po-bee ghost dusty'; document.body.appendChild(ghost); }
      if (ghost) { ghost.style.left = (e.clientX - 28) + 'px'; ghost.style.top = (e.clientY - 28) + 'px';
        targets.forEach(function (t) { var r = t.getBoundingClientRect(); t.classList.toggle('over', e.clientX > r.left && e.clientX < r.right && e.clientY > r.top && e.clientY < r.bottom); }); }
    });
    function end(e) {
      if (!start) return; start = null;
      if (ghost) { ghost.remove(); ghost = null; var hit = null; targets.forEach(function (t) { var r = t.getBoundingClientRect(); if (e.clientX > r.left && e.clientX < r.right && e.clientY > r.top && e.clientY < r.bottom) hit = t; t.classList.remove('over'); }); if (hit) visit(hit); }
      else { bee.classList.toggle('sel'); SFX.blip(); }
    }
    bee.addEventListener('pointerup', end); bee.addEventListener('pointercancel', function () { start = null; if (ghost) { ghost.remove(); ghost = null; } });
    targets.forEach(function (t) {
      t.addEventListener('click', function (e) { if (bee.contains(e.target)) return; if (bee.classList.contains('sel')) visit(t); });
      t.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); visit(t); } });
    });
    Object.keys(done).forEach(function (id) { if (fl(id)) mark(id); });
    sitOn(P.start, false);
    at.parentNode.insertBefore(g, at.nextSibling);
    upd();
  }

  /* ---------- Lesson: "Bag test" — a fair test: bag some flower heads, leave others open, count seeds (13.02) ----------
     D.bagtest = {afterText, kicker, title, todo[], why, img, alt, credit, heads:[{id,name}], open:{label,seeds,note}, bag:{label,seeds,note}, total, runBtn, needBoth, q1, opts1, q2, opts2, win, clue}
     seeds = full seeds per head (out of `total` tiny flowers) — the rest are drawn hollow */
  function buildBagtest() {
    var B = D.bagtest; if (!B) return;
    var at = null; $$('.tab-panel p').some(function (p) { if (B.afterText && p.textContent.indexOf(B.afterText) > -1) { at = p; return true; } });
    if (!at) { FAILED.push('bagtest anchor text not found'); return; }
    var g = gameShell(B.kicker || 'Part 2 game', B.title, B.todo, B.why); g.dataset.mod = 'bagtest';
    if (B.model) g.appendChild(el('div', 'fs-gr-model', '🧪 ' + esc(B.model)));
    var row = el('div', 'fs-bt-row'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    B.heads.forEach(function (h, i) {
      var c = el('div', 'fs-bt-head', '<div class="fs-bt-h">' + esc(h.name) + '</div><div class="fs-bt-ph"><img alt="' + esc(B.alt) + '" src="' + esc(B.img) + '"><span class="fs-bt-mesh"></span></div>' +
        '<div class="fs-bt-pick"><button type="button" class="fs-in-chip on" data-v="open">🐝 ' + esc(B.open.label) + '</button><button type="button" class="fs-in-chip" data-v="bag">🕸 ' + esc(B.bag.label) + '</button></div><div class="fs-bt-res"></div>');
      c.dataset.i = i; row.appendChild(c);
      $$('.fs-bt-pick .fs-in-chip', c).forEach(function (b) { b.addEventListener('click', function () {
        $$('.fs-bt-pick .fs-in-chip', c).forEach(function (x) { x.classList.toggle('on', x === b); }); c.classList.toggle('bagged', b.dataset.v === 'bag'); $('.fs-bt-res', c).innerHTML = ''; c.classList.remove('ran'); SFX.blip(); }); });
    });
    var btn = el('button', 'fs-btn fs-bt-go', esc(B.runBtn || '▶ Wait 3 weeks, then count')); btn.type = 'button';
    g.appendChild(row); g.appendChild(btn); g.appendChild(miss); g.appendChild(qh); g.appendChild(win);
    if (B.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(B.credit)));
    var tried = {}; try { tried = JSON.parse(store('bagtest') || '{}'); } catch (e) {}
    function seeds(n) { var s = ''; for (var k = 0; k < B.total; k++) s += '<i class="' + (k < n ? 'full' : '') + '"></i>'; return s; }
    function show(c, v, animate) {
      var r = B[v]; c.classList.add('ran');
      $('.fs-bt-res', c).innerHTML = '<div class="fs-bt-seeds' + (animate && !reduceMotion ? ' grow' : '') + '">' + seeds(r.seeds) + '</div><b>' + r.seeds + ' full seeds</b> out of ' + B.total + ' tiny flowers<p>' + esc(r.note) + '</p>';
    }
    function ask() {
      if (qh.dataset.on) return; qh.dataset.on = '1';
      chipsQ(qh, B.q1, B.opts1, function () {
        store('bagtest-q1', '1');
        chipsQ(qh, B.q2, B.opts2, function () { store('bagtest-q2', '1'); finish(); }, miss);
        if (store('bagtest-q2')) restore(1);
      }, miss);
      if (store('bagtest-q1')) restore(0);
    }
    function restore(k) { var opts = k ? B.opts2 : B.opts1, w = $$('.fs-sv-q', qh)[k]; var i = opts.map(function (o, j) { return o.ok ? j : -1; }).filter(function (j) { return j > -1; })[0]; $$('.fs-in-chip', w)[i].classList.add('on', 'ok'); w.dataset.done = '1'; if (k === 0) { chipsQ(qh, B.q2, B.opts2, function () { store('bagtest-q2', '1'); finish(); }, miss); if (store('bagtest-q2')) restore(1); } else finish(); }
    function finish() { if (win.classList.contains('show')) return; win.innerHTML = esc(B.win); win.classList.add('show'); SFX.win(); earnClue(B.clue || 'bagtest'); }
    btn.addEventListener('click', function () {
      var vs = $$('.fs-bt-head', row).map(function (c) { var v = $('.fs-bt-pick .on', c).dataset.v; show(c, v, true); tried[v] = 1; return v; });
      store('bagtest', JSON.stringify(tried)); SFX.sparkle();
      if (vs.indexOf('open') > -1 && vs.indexOf('bag') > -1) { miss.classList.remove('show'); ask(); }
      else { miss.innerHTML = '🔎 ' + esc(B.needBoth || 'A fair test compares: bag at least one head and leave at least one open.'); miss.classList.remove('show'); void miss.offsetWidth; miss.classList.add('show'); }
    });
    at.parentNode.insertBefore(g, at.nextSibling);
    if (tried.open && tried.bag) ask();
  }

  /* ---------- Warm-Up: "What comes next?" — see a stage, pick the next one; the strip fills, the circle closes (14.01) ----------
     D.nextup = {afterText, kicker, title, todo[], why, name, stages:[{id,t,img,alt}], whys:[one line per step, i -> i+1 (last = adult -> egg)],
                 hint, q, opts:[{t,ok,miss}], credit, win, clue} */
  function buildNextup() {
    var N = D.nextup; if (!N) return;
    var at = anchorP(N.afterText); if (!at) { FAILED.push('nextup anchor text not found'); return; }
    var g = gameShell(N.kicker || 'Warm-Up game', N.title, N.todo, N.why); g.dataset.mod = 'nextup';
    var strip = el('div', 'fs-nu-strip'), stage = el('div', 'fs-nu-stage'), info = el('div', 'fs-hs-card fs-nu-info', '<em>' + esc(N.hint || 'Drag the stage that comes next into the empty box, or tap it.') + '</em>');
    var miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(strip); g.appendChild(stage); g.appendChild(info); g.appendChild(miss); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    if (N.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(N.credit)));
    var S = N.stages, n = S.length, step = Math.min(+store('nextup') || 0, n);
    function card(s, cls) { return '<div class="fs-nu-card ' + (cls || '') + '"><img alt="' + esc(s.alt) + '" src="' + esc(s.img) + '"><span>' + esc(s.t) + '</span></div>'; }
    function drawStrip(pop) {
      var h = '';
      for (var i = 0; i <= Math.min(step, n - 1); i++) h += (i ? '<i class="fs-nu-arr">➜</i>' : '') + card(S[i], i === step && pop ? 'pop' : '');
      if (step >= n) h += '<i class="fs-nu-arr back">↩</i><div class="fs-nu-loop">' + esc(S[0].t) + ' again</div>';
      strip.innerHTML = h;
    }
    function round() {
      count.textContent = '🔄 ' + Math.min(step, n) + ' of ' + n + ' steps'; count.classList.toggle('ok', step >= n);
      if (step >= n) { stage.innerHTML = ''; ask(); return; }
      var cur = S[step], nextI = (step + 1) % n;
      var choices = shuffle(S.map(function (s, i) { return i; }).filter(function (i) { return i !== step; }));
      stage.innerHTML = '<div class="fs-nu-now"><div class="fs-nu-lab">Now</div>' + card(cur) + '</div><i class="fs-nu-arr big">➜</i>' +
        '<div class="fs-nu-slot" role="button" tabindex="0"><div class="fs-nu-lab">What comes next?</div><div class="fs-nu-q">?</div></div>' +
        '<div class="fs-nu-pick"><div class="fs-nu-lab">Pick one</div>' + choices.map(function (i) { return '<div class="fs-card fs-nu-ch" data-i="' + i + '"><img alt="' + esc(S[i].alt) + '" src="' + esc(S[i].img) + '"><span>' + esc(S[i].t) + '</span></div>'; }).join('') + '</div>';
      var slot = $('.fs-nu-slot', stage);
      function drop(tk) {
        var i = +tk.dataset.i;
        if (i !== nextI) { bounce(tk, miss, (S[i].miss && S[i].miss[step]) || N.miss || 'Not yet. Which stage grows out of this one? Look at the pictures in the strip.'); return; }
        miss.classList.remove('show'); SFX.chime();
        info.innerHTML = '<span class="fs-hs-n">' + (step + 1) + '</span><div><b>' + esc(cur.t) + ' → ' + esc(S[nextI].t) + '</b>' + esc(N.whys[step]) + '</div>';
        info.classList.remove('flash'); void info.offsetWidth; info.classList.add('flash');
        step++; store('nextup', String(step)); drawStrip(!reduceMotion); round();
      }
      $$('.fs-nu-ch', stage).forEach(function (c) { dragDrop(c, function () { return [slot]; }, drop); });
      slot.addEventListener('click', function () { var s = $('.sel', stage); if (s) { s.classList.remove('sel'); drop(s); } });
      slot.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); var s = $('.sel', stage); if (s) { s.classList.remove('sel'); drop(s); } } });
    }
    function ask() {
      if (qh.dataset.on) return; qh.dataset.on = '1';
      chipsQ(qh, N.q, N.opts, function () { store('nextup-q', '1'); winOnce(win, N.win, N.clue, 'nextup'); }, miss);
      if (store('nextup-q')) { var ok = N.opts.map(function (o, i) { return o.ok ? i : -1; }).filter(function (i) { return i > -1; })[0]; var c = $$('.fs-in-chip', qh)[ok]; if (c) c.classList.add('on', 'ok'); $('.fs-sv-q', qh).dataset.done = '1'; winOnce(win, N.win, N.clue, 'nextup'); }
    }
    at.parentNode.insertBefore(g, at.nextSibling);
    drawStrip(false); round();
  }

  /* ---------- Lesson: "Side by side" — drag the day slider; two young animals grow next to each other (14.01) ----------
     D.morph = {afterText, kicker, title, todo[], why, unit ('day'), max, lanes:[{name, parent, frames:[{d, img, alt, stage, like (looks like its parent?), note}]}],
                checks:[d,...] (days the student must visit), q, opts:[{t,ok,miss}], credit, win, clue} */
  function buildMorph() {
    var M = D.morph; if (!M) return;
    var at = anchorP(M.afterText); if (!at) { FAILED.push('morph anchor text not found'); return; }
    var g = gameShell(M.kicker || 'Lesson game', M.title, M.todo, M.why); g.dataset.mod = 'morph';
    var lanes = el('div', 'fs-mo-lanes'), ctl = el('div', 'fs-mo-ctl'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    ctl.innerHTML = '<label class="fs-mo-lab">📅 <b class="fs-mo-day"></b></label><input type="range" class="fs-mo-range" min="0" max="' + M.max + '" step="1" value="0" aria-label="Days"><div class="fs-mo-ticks"><span>' + esc(M.start || 'Day 0') + '</span><span>Day ' + M.max + '</span></div><div class="fs-mo-need"></div>';
    M.lanes.forEach(function (L, li) {
      var ln = el('div', 'fs-mo-lane', '<div class="fs-mo-name">' + esc(L.name) + '</div><div class="fs-mo-ph"><img alt=""><span class="fs-mo-stage"></span></div><div class="fs-mo-like"></div><div class="fs-mo-note"></div><div class="fs-mo-dots">' + L.frames.map(function (f, k) { return '<i data-k="' + k + '" title="' + esc(f.stage) + '"></i>'; }).join('') + '</div>');
      lanes.appendChild(ln);
    });
    g.appendChild(ctl); g.appendChild(lanes); g.appendChild(miss); g.appendChild(qh); g.appendChild(win);
    if (M.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(M.credit)));
    var range = $('.fs-mo-range', ctl), seen = loadJ('morph', {}), checks = M.checks || [];
    function frameAt(L, d) { var f = L.frames[0], k = 0; L.frames.forEach(function (x, i) { if (x.d <= d) { f = x; k = i; } }); return { f: f, k: k }; }
    function show(d, fromUser) {
      $('.fs-mo-day', ctl).textContent = d === 0 ? (M.start || 'Day 0') : 'Day ' + d;
      $$('.fs-mo-lane', lanes).forEach(function (ln, li) {
        var L = M.lanes[li], r = frameAt(L, d), img = $('img', ln);
        if (img.getAttribute('src') !== r.f.img) { img.src = r.f.img; img.alt = r.f.alt; if (!reduceMotion && fromUser) { img.classList.remove('in'); void img.offsetWidth; img.classList.add('in'); } }
        $('.fs-mo-stage', ln).textContent = r.f.stage;
        var like = $('.fs-mo-like', ln); like.className = 'fs-mo-like ' + (r.f.like ? 'yes' : 'no');
        like.textContent = r.f.like == null ? '' : (r.f.like ? '✓ Looks like a small ' + L.parent : '✗ Looks nothing like a ' + L.parent);
        $('.fs-mo-note', ln).textContent = r.f.note || '';
        $$('.fs-mo-dots i', ln).forEach(function (dot, k) { dot.classList.toggle('on', k <= r.k); });
      });
      checks.forEach(function (c) { if (Math.abs(d - c) <= 2) seen[c] = 1; }); saveJ('morph', seen);
      var left = checks.filter(function (c) { return !seen[c]; });
      $('.fs-mo-need', ctl).innerHTML = left.length ? '👀 Slide to ' + left.map(function (c) { return '<b>day ' + c + '</b>'; }).join(', ') + ' and compare.' : '✅ You watched both grow up.';
      if (!left.length) ask();
    }
    var lastBlip = -1;
    range.addEventListener('input', function () { var d = +range.value; var k = frameAt(M.lanes[0], d).k * 10 + frameAt(M.lanes[1], d).k; if (k !== lastBlip) { lastBlip = k; SFX.blip(); } show(d, true); });
    function ask() {
      if (qh.dataset.on) return; qh.dataset.on = '1';
      chipsQ(qh, M.q, M.opts, function () { store('morph-q', '1'); winOnce(win, M.win, M.clue, 'morph'); }, miss);
      if (store('morph-q')) { var ok = M.opts.map(function (o, i) { return o.ok ? i : -1; }).filter(function (i) { return i > -1; })[0]; var c = $$('.fs-in-chip', qh)[ok]; if (c) c.classList.add('on', 'ok'); $('.fs-sv-q', qh).dataset.done = '1'; winOnce(win, M.win, M.clue, 'morph'); }
    }
    at.parentNode.insertBefore(g, at.nextSibling);
    show(0, false);
  }

  /* ---------- Lesson Part 3: "Close the circle" — put stage photos on a life-cycle wheel, then stamp the kind of cycle (14.01) ----------
     D.wheel = {replace, kicker, title, todo[], why, kinds:[{k,icon,t}], orgs:[{id,name,icon,stages:[{t,img,alt}], kind, kindMiss, why}], hint, credit, win, clue}
     stage 0 is placed for the student; the rest go in order around the circle */
  function buildWheel() {
    var W = D.wheel; if (!W) return;
    var wrap = $(W.replace || '#tab-lesson .diagram-wrap'); if (!wrap) { FAILED.push('wheel: nothing to replace'); return; }
    var g = gameShell(W.kicker || 'Lesson game', W.title, W.todo, W.why); g.dataset.mod = 'wheel';
    var pv = wrap.previousElementSibling; if (pv && pv.tagName === 'P' && pv.textContent.length < 200) pv.classList.add('fs-hide-on');
    var tabs = el('div', 'fs-wh-tabs'), board = el('div', 'fs-wh-board'), info = el('div', 'fs-hs-card fs-wh-info', '<em>' + esc(W.hint || 'Drag the next stage onto the glowing spot, or tap the card and then the spot.') + '</em>');
    var miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), win = el('div', 'fs-win');
    W.orgs.forEach(function (o, i) { var b = el('button', 'fs-in-chip', '<span>' + o.icon + '</span>' + esc(o.name) + '<em></em>'); b.type = 'button'; b.dataset.i = i; tabs.appendChild(b); });
    g.appendChild(tabs); g.appendChild(board); g.appendChild(info); g.appendChild(miss); g.appendChild(count); g.appendChild(win);
    if (W.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(W.credit)));
    var st = loadJ('wheel', {});   // {id: {n: placed count, kind: true}}
    function done(o) { var s = st[o.id]; return s && s.n >= o.stages.length && s.kind; }
    function upd() {
      var n = W.orgs.filter(done).length; count.textContent = '🔄 ' + n + ' of ' + W.orgs.length + ' life cycles closed'; count.classList.toggle('ok', n === W.orgs.length);
      $$('.fs-in-chip', tabs).forEach(function (b, i) { var ok = done(W.orgs[i]); b.classList.toggle('done', ok); $('em', b).textContent = ok ? ' ✓' : ''; });
      if (n === W.orgs.length) winOnce(win, W.win, W.clue, 'wheel');
    }
    function pos(k, N) { var a = -Math.PI / 2 + k * 2 * Math.PI / N; return { x: 50 + 36 * Math.cos(a), y: 50 + 36 * Math.sin(a) }; }
    function open(i) {
      var o = W.orgs[i], N = o.stages.length, s = st[o.id] || (st[o.id] = { n: 1 }); if (s.n < 1) s.n = 1;
      $$('.fs-in-chip', tabs).forEach(function (b) { b.classList.toggle('on', +b.dataset.i === i); }); SFX.blip();
      var arcs = '';
      for (var k = 0; k < N; k++) { var p = pos(k, N), q = pos((k + 1) % N, N); var mx = 50 + 44 * Math.cos(-Math.PI / 2 + (k + .5) * 2 * Math.PI / N), my = 50 + 44 * Math.sin(-Math.PI / 2 + (k + .5) * 2 * Math.PI / N);
        arcs += '<path class="fs-wh-arc' + (k === N - 1 ? ' last' : '') + '" data-k="' + k + '" d="M' + p.x + ',' + p.y + ' Q' + mx + ',' + my + ' ' + q.x + ',' + q.y + '" marker-end="url(#fsWhHead)"/>'; }
      board.innerHTML = '<div class="fs-wh-ring"><svg viewBox="0 0 100 100" class="fs-wh-svg" aria-hidden="true"><defs><marker id="fsWhHead" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="4" markerHeight="4" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#2E9E5E"/></marker></defs>' + arcs + '</svg>' +
        o.stages.map(function (x, k) { var p = pos(k, N); return '<div class="fs-wh-spot" data-k="' + k + '" style="left:' + p.x + '%;top:' + p.y + '%"><span class="fs-wh-num">' + (k + 1) + '</span></div>'; }).join('') +
        '<div class="fs-wh-mid"><b>' + esc(o.name) + '</b><span class="fs-wh-kind"></span></div></div>' +
        '<div class="fs-wh-side"><div class="fs-lu-lab">Stage cards</div><div class="fs-wh-tray"></div><div class="fs-wh-stamp"></div></div>';
      var tray = $('.fs-wh-tray', board), spots = $$('.fs-wh-spot', board);
      shuffle(o.stages.map(function (x, k) { return k; }).filter(function (k) { return k > 0; })).forEach(function (k) {
        var c = el('div', 'fs-card fs-wh-card', '<img alt="' + esc(o.stages[k].alt) + '" src="' + esc(o.stages[k].img) + '"><span>' + esc(o.stages[k].t) + '</span>'); c.dataset.k = k; tray.appendChild(c);
      });
      function paint(animate) {
        spots.forEach(function (sp, k) {
          var x = o.stages[k], has = k < s.n;
          sp.classList.toggle('filled', has); sp.classList.toggle('next', k === s.n);
          if (has && !$('img', sp)) { sp.insertAdjacentHTML('afterbegin', '<img alt="' + esc(x.alt) + '" src="' + esc(x.img) + '"><span class="fs-wh-t">' + esc(x.t) + '</span>'); if (animate && k === s.n - 1 && !reduceMotion) { sp.classList.remove('pop'); void sp.offsetWidth; sp.classList.add('pop'); } }
        });
        $$('.fs-wh-arc', board).forEach(function (a) { var k = +a.dataset.k; a.classList.toggle('on', k < s.n - 1 || (s.n >= N && k === N - 1)); });
        $$('.fs-wh-card', tray).forEach(function (c) { if (+c.dataset.k < s.n) c.classList.add('placed'); });
        if (s.n >= N) stamp();
      }
      function drop(tk, sp) {
        var k = +tk.dataset.k, want = s.n;
        if (sp && +sp.dataset.k !== want) { bounce(tk, miss, 'Fill the spots in order. Find the glowing spot ' + (want + 1) + ' first.'); return; }
        if (k !== want) { bounce(tk, miss, 'Look at spot ' + want + ': ' + o.stages[want - 1].t + '. Which stage grows out of it?'); return; }
        miss.classList.remove('show'); s.n++; saveJ('wheel', st); SFX.chime(); paint(true);
        info.innerHTML = s.n >= N ? '<span class="fs-hs-n">↩</span><div><b>The circle closes</b>The adult makes offspring, and the life cycle starts over.</div>' : '<span class="fs-hs-n">' + s.n + '</span><div><b>' + esc(o.stages[k].t) + '</b>Next: what comes after it?</div>';
        info.classList.remove('flash'); void info.offsetWidth; info.classList.add('flash');
      }
      $$('.fs-wh-card', tray).forEach(function (c) { dragDrop(c, function () { return spots.filter(function (x) { return !x.classList.contains('filled'); }); }, drop); });
      spots.forEach(function (sp) { sp.addEventListener('click', function () { var sel = $('.sel', tray); if (sel) { sel.classList.remove('sel'); drop(sel, sp); } }); });
      function stamp() {
        var box = $('.fs-wh-stamp', board); if (box.dataset.on) return; box.dataset.on = '1';
        box.innerHTML = '<div class="fs-in-k">What kind of life cycle is it?</div><div class="fs-in-chips">' + W.kinds.map(function (x) { return '<button type="button" class="fs-in-chip" data-k="' + x.k + '"><span>' + x.icon + '</span>' + esc(x.t) + '</button>'; }).join('') + '</div>';
        function mark() { var kd = W.kinds.filter(function (x) { return x.k === o.kind; })[0]; $('.fs-wh-kind', board).textContent = kd.icon + ' ' + kd.t; $$('.fs-in-chip', box).forEach(function (c) { if (c.dataset.k === o.kind) c.classList.add('on', 'ok'); }); }
        if (s.kind) { mark(); return; }
        $$('.fs-in-chip', box).forEach(function (c) { c.addEventListener('click', function () {
          if (s.kind) return;
          if (c.dataset.k !== o.kind) { bounce(c, miss, o.kindMiss || 'Count the stages. Does the young look like the adult?'); return; }
          miss.classList.remove('show'); s.kind = true; saveJ('wheel', st); SFX.stamp(); mark();
          info.innerHTML = '<span class="fs-hs-n">✓</span><div><b>' + esc(o.name) + '</b>' + esc(o.why) + '</div>'; info.classList.remove('flash'); void info.offsetWidth; info.classList.add('flash'); upd();
        }); });
      }
      paint(false); upd();
    }
    $$('.fs-in-chip', tabs).forEach(function (b) { b.addEventListener('click', function () { open(+b.dataset.i); }); });
    wrap.parentNode.insertBefore(g, wrap); wrap.classList.add('fs-hide-on');
    open(0); upd();
  }

  /* ---------- Lesson Part 4: "Alike and different" — pick a pair, drag facts into Only A / Both / Only B (14.01) ----------
     D.venn = {afterText, kicker, title, todo[], why, pairs:[{id, a:{name,img,alt}, b:{...}, cards:[{t, z:'a'|'both'|'b', miss}], q, opts:[{t,ok,miss}], done}], credit, win, clue}
     the clue is earned when any one pair is finished */
  function buildVenn() {
    var V = D.venn; if (!V) return;
    var at = anchorP(V.afterText); if (!at) { FAILED.push('venn anchor text not found'); return; }
    var g = gameShell(V.kicker || 'Lesson game', V.title, V.todo, V.why); g.dataset.mod = 'venn';
    var tabs = el('div', 'fs-vn-tabs'), body = el('div', 'fs-vn-body'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    V.pairs.forEach(function (p, i) { var b = el('button', 'fs-in-chip', esc(p.a.name) + ' vs. ' + esc(p.b.name) + '<em></em>'); b.type = 'button'; b.dataset.i = i; tabs.appendChild(b); });
    g.appendChild(el('div', 'fs-in-k', 'Pick two Florida living things to compare'));
    g.appendChild(tabs); g.appendChild(body); g.appendChild(miss); g.appendChild(qh); g.appendChild(win);
    if (V.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(V.credit)));
    var st = loadJ('venn', {});
    function upd() { $$('.fs-in-chip', tabs).forEach(function (b, i) { var p = V.pairs[i], s = st[p.id], ok = s && s.q; b.classList.toggle('done', !!ok); $('em', b).textContent = ok ? ' ✓' : ''; }); }
    function open(i) {
      var p = V.pairs[i], s = st[p.id] || (st[p.id] = { put: {} });
      $$('.fs-in-chip', tabs).forEach(function (b) { b.classList.toggle('on', +b.dataset.i === i); }); SFX.blip(); qh.innerHTML = ''; delete qh.dataset.on;
      body.innerHTML = '<div class="fs-vn-heads"><div class="fs-vn-who"><img alt="' + esc(p.a.alt) + '" src="' + esc(p.a.img) + '"><b>' + esc(p.a.name) + '</b></div><div class="fs-vn-who"><img alt="' + esc(p.b.alt) + '" src="' + esc(p.b.img) + '"><b>' + esc(p.b.name) + '</b></div></div>' +
        '<div class="fs-vn-zones"><div class="fs-vn-z" data-z="a" role="button" tabindex="0"><div class="fs-vn-zt">Only the ' + esc(p.a.name.toLowerCase()) + '</div><div class="fs-vn-pile"></div></div>' +
        '<div class="fs-vn-z both" data-z="both" role="button" tabindex="0"><div class="fs-vn-zt">Both (alike)</div><div class="fs-vn-pile"></div></div>' +
        '<div class="fs-vn-z" data-z="b" role="button" tabindex="0"><div class="fs-vn-zt">Only the ' + esc(p.b.name.toLowerCase()) + '</div><div class="fs-vn-pile"></div></div></div>' +
        '<div class="fs-lu-lab">Fact cards</div><div class="fs-vn-tray"></div><div class="fs-count fs-vn-n"></div>';
      var tray = $('.fs-vn-tray', body), zones = $$('.fs-vn-z', body);
      shuffle(p.cards.map(function (c, k) { return k; })).forEach(function (k) { var c = el('div', 'fs-card fs-vn-card', esc(p.cards[k].t)); c.dataset.k = k; tray.appendChild(c); });
      function placeK(k, animate) {
        var c = p.cards[k], z = $('.fs-vn-z[data-z="' + c.z + '"] .fs-vn-pile', body), chip = el('span', 'fs-vn-chip' + (animate && !reduceMotion ? ' pop' : ''), esc(c.t)); z.appendChild(chip);
        var t = $('.fs-vn-card[data-k="' + k + '"]', tray); if (t) t.remove();
      }
      function cnt() {
        var n = Object.keys(s.put).length; $('.fs-vn-n', body).textContent = '🧩 ' + n + ' of ' + p.cards.length + ' facts sorted'; $('.fs-vn-n', body).classList.toggle('ok', n === p.cards.length);
        if (n === p.cards.length) ask();
      }
      function drop(tk, z) {
        var k = +tk.dataset.k, c = p.cards[k];
        if (z.dataset.z !== c.z) { bounce(tk, miss, c.miss || 'Ask: is this true for the ' + p.a.name.toLowerCase() + ', the ' + p.b.name.toLowerCase() + ', or both?'); return; }
        miss.classList.remove('show'); s.put[k] = 1; saveJ('venn', st); SFX.chime(); placeK(k, true); cnt();
      }
      $$('.fs-vn-card', tray).forEach(function (c) { dragDrop(c, function () { return zones; }, drop); });
      zones.forEach(function (z) { z.addEventListener('click', function () { var sel = $('.sel', tray); if (sel) { sel.classList.remove('sel'); drop(sel, z); } }); });
      Object.keys(s.put).forEach(function (k) { placeK(+k, false); });
      function ask() {
        if (qh.dataset.on) return; qh.dataset.on = '1';
        chipsQ(qh, p.q, p.opts, function () { s.q = 1; saveJ('venn', st); upd(); var w = el('div', 'fs-hs-card flash', '<span class="fs-hs-n">✓</span><div>' + esc(p.done || '') + '</div>'); qh.appendChild(w); winOnce(win, V.win, V.clue, 'venn'); }, miss);
        if (s.q) { var ok = p.opts.map(function (o, i) { return o.ok ? i : -1; }).filter(function (i) { return i > -1; })[0]; var c = $$('.fs-in-chip', qh)[ok]; if (c) c.classList.add('on', 'ok'); $('.fs-sv-q', qh).dataset.done = '1'; }
      }
      cnt();
    }
    $$('.fs-in-chip', tabs).forEach(function (b) { b.addEventListener('click', function () { open(+b.dataset.i); }); });
    at.parentNode.insertBefore(g, at.nextSibling);
    open(0); upd();
    if (V.pairs.some(function (p) { return st[p.id] && st[p.id].q; })) winOnce(win, V.win, V.clue, 'venn');
  }

  /* ---------- Warm-Up: "Two winters" — sort real January photos into Florida or the cold region (14.02) ----------
     D.twowinters = {afterText, kicker, title, todo[], why, sides:[{k, icon, t, sub}], cards:[{id, t, img, alt, z, why, miss}], q, opts:[{t,ok,miss}], credit, win, clue} */
  function buildTwowinters() {
    var T = D.twowinters; if (!T) return;
    var at = anchorP(T.afterText); if (!at) { FAILED.push('twowinters anchor text not found'); return; }
    var g = gameShell(T.kicker || 'Warm-Up game', T.title, T.todo, T.why); g.dataset.mod = 'twowinters';
    var sides = el('div', 'fs-tw-sides'), tray = el('div', 'fs-tw-tray'), info = el('div', 'fs-hs-card fs-tw-info', '<em>' + esc(T.hint || 'Drag a photo to the place where you would see it in January, or tap the photo and then the place.') + '</em>');
    var miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    T.sides.forEach(function (s) { sides.appendChild(el('div', 'fs-tw-side fs-tw-' + s.k, '<div class="fs-tw-head"><span>' + s.icon + '</span><div><b>' + esc(s.t) + '</b><small>' + esc(s.sub || '') + '</small></div></div><div class="fs-tw-pile"></div>')); $$('.fs-tw-side', sides).slice(-1)[0].dataset.z = s.k; });
    g.appendChild(sides); g.appendChild(el('div', 'fs-lu-lab', 'Photo cards')); g.appendChild(tray); g.appendChild(info); g.appendChild(miss); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    if (T.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(T.credit)));
    var put = loadJ('twowinters', {}), zones = $$('.fs-tw-side', sides);
    function place(c, animate) {
      var pile = $('.fs-tw-pile', $('.fs-tw-side[data-z="' + c.z + '"]', sides));
      pile.appendChild(el('div', 'fs-tw-got' + (animate && !reduceMotion ? ' pop' : ''), '<img alt="' + esc(c.alt) + '" src="' + esc(c.img) + '"><span>' + esc(c.t) + '</span>'));
      var t = $('.fs-tw-card[data-id="' + c.id + '"]', tray); if (t) t.remove();
    }
    function upd() {
      var n = Object.keys(put).length; count.textContent = '🗂 ' + n + ' of ' + T.cards.length + ' photos sorted'; count.classList.toggle('ok', n === T.cards.length);
      if (n === T.cards.length) ask();
    }
    shuffle(T.cards).forEach(function (c) { if (put[c.id]) return; var k = el('div', 'fs-card fs-tw-card', '<img alt="' + esc(c.alt) + '" src="' + esc(c.img) + '"><span>' + esc(c.t) + '</span>'); k.dataset.id = c.id; tray.appendChild(k); });
    function drop(tk, z) {
      var c = T.cards.filter(function (x) { return x.id === tk.dataset.id; })[0];
      if (z.dataset.z !== c.z) { bounce(tk, miss, c.miss || 'Think about January there. Is the water frozen or open? Are plants growing?'); return; }
      miss.classList.remove('show'); put[c.id] = 1; saveJ('twowinters', put); SFX.chime(); place(c, true);
      info.innerHTML = '<span class="fs-hs-n">✓</span><div><b>' + esc(c.t) + '</b>' + esc(c.why) + '</div>'; info.classList.remove('flash'); void info.offsetWidth; info.classList.add('flash'); upd();
    }
    $$('.fs-tw-card', tray).forEach(function (k) { dragDrop(k, function () { return zones; }, drop); });
    tapTargets(g, zones, drop);
    function ask() {
      if (qh.dataset.on) return; qh.dataset.on = '1';
      chipsQ(qh, T.q, T.opts, function () { store('twowinters-q', '1'); winOnce(win, T.win, T.clue, 'twowinters'); }, miss);
      if (store('twowinters-q')) { var ok = T.opts.map(function (o, i) { return o.ok ? i : -1; }).filter(function (i) { return i > -1; })[0]; var c = $$('.fs-in-chip', qh)[ok]; if (c) c.classList.add('on', 'ok'); $('.fs-sv-q', qh).dataset.done = '1'; winOnce(win, T.win, T.clue, 'twowinters'); }
    }
    T.cards.forEach(function (c) { if (put[c.id]) place(c, false); });
    at.parentNode.insertBefore(g, at.nextSibling); upd();
  }

  /* ---------- Lesson: "Turn the calendar" — flip through four seasons; each living thing stays, leaves, sleeps or moves, in Florida and the cold region (14.02) ----------
     D.calendar = {afterText, kicker, title, todo[], why, regions:[{k, icon, t}], seasons:[{k, icon, t, temps:{k:'about 61°F'}, notes:{k:''}}],
                   rows:[{icon, name, cells:{k:[{s:'here'|'gone'|'sleep'|'warm'|'none'|'busy', t}] one per season}}], q, opts, win, clue} */
  function buildCalendar() {
    var K = D.calendar; if (!K) return;
    var at = anchorP(K.afterText); if (!at) { FAILED.push('calendar anchor text not found'); return; }
    var g = gameShell(K.kicker || 'Lesson game', K.title, K.todo, K.why); g.dataset.mod = 'calendar';
    var pages = el('div', 'fs-ca-pages'), board = el('div', 'fs-ca-board'), need = el('div', 'fs-mo-need'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    K.seasons.forEach(function (s, i) { var b = el('button', 'fs-ca-page', '<span class="fs-ca-rings"><i></i><i></i></span><b>' + s.icon + '</b>' + esc(s.t)); b.type = 'button'; b.dataset.i = i; pages.appendChild(b); });
    var SIC = { here: '✅', gone: '✈️', sleep: '😴', warm: '♨️', none: '—', busy: '🍽', rest: '💤' };
    g.appendChild(pages); g.appendChild(board); g.appendChild(need); g.appendChild(miss); g.appendChild(qh); g.appendChild(win);
    if (K.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Credits</summary>' + esc(K.credit)));
    var seen = loadJ('calendar', {});
    function show(i, user) {
      var s = K.seasons[i]; seen[s.k] = 1; saveJ('calendar', seen);
      $$('.fs-ca-page', pages).forEach(function (b) { b.classList.toggle('on', +b.dataset.i === i); b.classList.toggle('seen', !!seen[K.seasons[+b.dataset.i].k]); });
      board.innerHTML = '<div class="fs-ca-grid' + (user && !reduceMotion ? ' flip' : '') + '"><div class="fs-ca-corner">' + s.icon + ' ' + esc(s.t) + '</div>' +
        K.regions.map(function (r) { return '<div class="fs-ca-rh fs-ca-' + r.k + '"><b>' + r.icon + ' ' + esc(r.t) + '</b><span class="fs-ca-temp">🌡 ' + esc(s.temps[r.k]) + '</span><small>' + esc((s.notes || {})[r.k] || '') + '</small></div>'; }).join('') +
        K.rows.map(function (row) {
          return '<div class="fs-ca-name"><span>' + row.icon + '</span>' + esc(row.name) + '</div>' + K.regions.map(function (r) { var c = row.cells[r.k][i]; return '<div class="fs-ca-cell s-' + c.s + '"><span class="fs-ca-ic">' + (SIC[c.s] || '') + '</span>' + esc(c.t) + '</div>'; }).join('');
        }).join('') + '</div><div class="fs-ca-key">' + (K.key || '✅ here and active · ✈️ moved away (migrated) · 😴 hibernating · ♨️ huddled in warm water · 🍽 eating a lot to get ready') + '</div>';
      if (user) SFX.whoosh();
      var left = K.seasons.filter(function (x) { return !seen[x.k]; });
      need.innerHTML = left.length ? '📅 Turn to ' + left.map(function (x) { return '<b>' + esc(x.t) + '</b>'; }).join(', ') + ' too.' : '✅ You turned all four calendar pages.';
      if (!left.length) ask();
    }
    $$('.fs-ca-page', pages).forEach(function (b) { b.addEventListener('click', function () { show(+b.dataset.i, true); }); });
    function ask() {
      if (qh.dataset.on) return; qh.dataset.on = '1';
      chipsQ(qh, K.q, K.opts, function () { store('calendar-q', '1'); winOnce(win, K.win, K.clue, 'calendar'); }, miss);
      if (store('calendar-q')) { var ok = K.opts.map(function (o, i) { return o.ok ? i : -1; }).filter(function (i) { return i > -1; })[0]; var c = $$('.fs-in-chip', qh)[ok]; if (c) c.classList.add('on', 'ok'); $('.fs-sv-q', qh).dataset.done = '1'; winOnce(win, K.win, K.clue, 'calendar'); }
    }
    at.parentNode.insertBefore(g, at.nextSibling);
    show(0, false);
  }

  /* ---------- Lesson: "Manatee water test" — change one thing (the river temperature), run the morning, log where the manatees go (14.02) ----------
     D.manatee = {replace | afterText, kicker, title, todo[], why, min, max, start, cold, springT, river:{img,alt,t}, spring:{img,alt,t}, cold/warm results {where, t},
                  q, opts, credit, win, clue}; the student must log at least one cold and one warm morning */
  function buildManatee() {
    var M = D.manatee; if (!M) return;
    var wrap = M.replace ? $(M.replace) : null, at = M.replace ? null : anchorP(M.afterText);
    if (!wrap && !at) { FAILED.push('manatee: no anchor'); return; }
    var g = gameShell(M.kicker || 'Lesson game', M.title, M.todo, M.why); g.dataset.mod = 'manatee';
    if (wrap) { var pv = wrap.previousElementSibling; if (pv && pv.tagName === 'P' && pv.textContent.length < 200) pv.classList.add('fs-hide-on'); }
    var map = el('div', 'fs-mt-map', '<div class="fs-mt-zone fs-mt-river"><img alt="' + esc(M.river.alt) + '" src="' + esc(M.river.img) + '"><span class="fs-mt-lab">' + esc(M.river.t) + ' · <b class="fs-mt-rt"></b></span></div>' +
      '<div class="fs-mt-zone fs-mt-spring"><img alt="' + esc(M.spring.alt) + '" src="' + esc(M.spring.img) + '"><span class="fs-mt-lab">' + esc(M.spring.t) + ' · <b>' + M.springT + '°F all year</b></span></div><img class="fs-mt-cow" alt="" aria-hidden="true" src="' + esc(M.token) + '">');
    var ctl = el('div', 'fs-mo-ctl', '<label class="fs-mo-lab">🌡 River water this morning: <b class="fs-mt-val"></b></label><input type="range" class="fs-mo-range fs-mt-range" min="' + M.min + '" max="' + M.max + '" step="1" aria-label="River water temperature in degrees Fahrenheit"><div class="fs-mo-ticks"><span>' + M.min + '°F (cold)</span><span>' + M.max + '°F (warm)</span></div>' +
      '<button type="button" class="fs-btn fs-mt-go">▶ Run the morning</button>');
    var log = el('div', 'fs-mt-log', '<div class="fs-lu-lab">Test log</div><table><thead><tr><th>River water</th><th>Where the manatees went</th></tr></thead><tbody></tbody></table>');
    var need = el('div', 'fs-mo-need'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(map); g.appendChild(ctl); g.appendChild(log); g.appendChild(need); g.appendChild(miss); g.appendChild(qh); g.appendChild(win);
    if (M.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(M.credit)));
    var range = $('.fs-mt-range', ctl), st = loadJ('manatee', { rows: [] }), cow = $('.fs-mt-cow', map);
    range.value = M.start;
    function val() { var v = +range.value; $('.fs-mt-val', ctl).textContent = v + '°F'; $('.fs-mt-rt', map).textContent = v + '°F'; map.classList.toggle('cold', v < M.cold); }
    function row(r) { $('tbody', log).insertAdjacentHTML('beforeend', '<tr class="' + (r.c ? 'c' : 'w') + '"><td>' + r.v + '°F</td><td>' + esc(r.c ? M.coldResult : M.warmResult) + '</td></tr>'); }
    function check() {
      var c = st.rows.some(function (r) { return r.c; }), w = st.rows.some(function (r) { return !r.c; });
      need.innerHTML = c && w ? '✅ You tested a cold morning and a warm morning.' : '🧪 Test ' + (c ? '' : '<b>a cold morning (below ' + M.cold + '°F)</b>') + (!c && !w ? ' and ' : '') + (w ? '' : '<b>a warm morning (' + M.cold + '°F or warmer)</b>') + '.';
      if (c && w) ask();
    }
    range.addEventListener('input', function () { val(); SFX.blip(); });
    $('.fs-mt-go', ctl).addEventListener('click', function () {
      var v = +range.value, c = v < M.cold, r = { v: v, c: c };
      cow.classList.remove('to-spring', 'to-river'); void cow.offsetWidth; cow.classList.add(c ? 'to-spring' : 'to-river');
      SFX.whoosh(); st.rows.push(r); if (st.rows.length > 6) st.rows.shift(); saveJ('manatee', st);
      $('tbody', log).innerHTML = ''; st.rows.forEach(row); check();
    });
    function ask() {
      if (qh.dataset.on) return; qh.dataset.on = '1';
      chipsQ(qh, M.q, M.opts, function () { store('manatee-q', '1'); winOnce(win, M.win, M.clue, 'manatee'); }, miss);
      if (store('manatee-q')) { var ok = M.opts.map(function (o, i) { return o.ok ? i : -1; }).filter(function (i) { return i > -1; })[0]; var c = $$('.fs-in-chip', qh)[ok]; if (c) c.classList.add('on', 'ok'); $('.fs-sv-q', qh).dataset.done = '1'; winOnce(win, M.win, M.clue, 'manatee'); }
    }
    if (wrap) { wrap.parentNode.insertBefore(g, wrap); wrap.classList.add('fs-hide-on'); } else at.parentNode.insertBefore(g, at.nextSibling);
    val(); st.rows.forEach(row); if (st.rows.length) cow.classList.add(st.rows[st.rows.length - 1].c ? 'to-spring' : 'to-river'); check();
  }

  /* ---------- Lesson Part 4: "Build the seasonal model" — fill two region circles, draw food-energy arrows, add the migration arrow; a meter grows (14.02) ----------
     D.seasonmodel = {afterText, kicker, title, todo[], why, regions:[{k, icon, t}], roles:[{k, t}], cards:[{id, t, img, alt, z ('no' = wrong season), role, miss}],
                      arrows:{k:[[foodId, eaterId]]}, arrowMiss, migrant:{id, t, img, alt, q, opts}, steps:[3 labels], q, opts, credit, win, clue} */
  function buildSeasonmodel() {
    var S = D.seasonmodel; if (!S) return;
    var at = anchorP(S.afterText); if (!at) { FAILED.push('seasonmodel anchor text not found'); return; }
    var g = gameShell(S.kicker || 'Lesson game', S.title, S.todo, S.why); g.dataset.mod = 'seasonmodel';
    var meter = el('div', 'fs-sm-meter', '<div class="fs-sm-bar"><i></i></div><div class="fs-sm-steps">' + S.steps.map(function (t, i) { return '<span data-i="' + i + '">' + (i + 1) + '. ' + esc(t) + '</span>'; }).join('') + '</div>');
    var stage = el('div', 'fs-sm-stage'), tray = el('div', 'fs-sm-tray'), info = el('div', 'fs-hs-card fs-sm-info', '<em>' + esc(S.hint || 'Drag each card into the right circle, or tap the card and then the circle.') + '</em>');
    var miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    stage.innerHTML = S.regions.map(function (r, i) {
      return (i === 1 ? '<div class="fs-sm-mid"><div class="fs-sm-mig" role="button" tabindex="0"><span class="fs-sm-migarr">⟷</span><small>migration arrow</small></div></div>' : '') +
        '<div class="fs-sm-ring fs-sm-' + r.k + '" data-z="' + r.k + '" role="button" tabindex="0"><div class="fs-sm-rt">' + r.icon + ' ' + esc(r.t) + '</div><div class="fs-sm-need"></div><div class="fs-sm-pile"></div><div class="fs-sm-arrows"></div></div>';
    }).join('');
    g.appendChild(meter); g.appendChild(stage); g.appendChild(el('div', 'fs-lu-lab', 'Model cards')); g.appendChild(tray); g.appendChild(info); g.appendChild(miss); g.appendChild(qh); g.appendChild(win);
    if (S.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(S.credit)));
    var st = loadJ('seasonmodel', { put: {}, arr: {}, mig: 0 }), rings = $$('.fs-sm-ring', stage), mig = $('.fs-sm-mig', stage), pick = null;
    function card(id) { return S.cards.filter(function (c) { return c.id === id; })[0]; }
    function smPic(c) { return c.img ? '<img alt="' + esc(c.alt) + '" src="' + esc(c.img) + '">' : '<b class="fs-sm-ic" aria-hidden="true">' + (c.icon || '🌤') + '</b>'; }
    function full(k) { return S.roles.every(function (ro) { return S.cards.some(function (c) { return st.put[c.id] && c.z === k && c.role === ro.k; }); }); }
    function step() { if (!S.regions.every(function (r) { return full(r.k); })) return 0; if (!S.regions.every(function (r) { return (S.arrows[r.k] || []).every(function (a) { return st.arr[a.join('>')]; }); })) return 1; return st.mig ? 3 : 2; }
    function draw(anim) {
      var n = step();
      $('.fs-sm-bar i', meter).style.width = Math.round(n / 3 * 100) + '%';
      $$('.fs-sm-steps span', meter).forEach(function (s, i) { s.classList.toggle('ok', i < n); s.classList.toggle('now', i === n); });
      rings.forEach(function (rg) {
        var k = rg.dataset.z, pile = $('.fs-sm-pile', rg);
        pile.innerHTML = S.cards.filter(function (c) { return st.put[c.id] && c.z === k; }).map(function (c) { return '<button type="button" class="fs-sm-got' + (pick === c.id ? ' pick' : '') + '" data-id="' + c.id + '">' + smPic(c) + '<span>' + esc(c.t) + '</span></button>'; }).join('');
        $('.fs-sm-need', rg).innerHTML = S.roles.map(function (ro) { var ok = S.cards.some(function (c) { return st.put[c.id] && c.z === k && c.role === ro.k; }); return '<i class="' + (ok ? 'ok' : '') + '">' + (ok ? '✓ ' : '') + esc(ro.t) + '</i>'; }).join('');
        $('.fs-sm-arrows', rg).innerHTML = (S.arrows[k] || []).filter(function (a) { return st.arr[a.join('>')]; }).map(function (a) { return '<div class="fs-sm-arrow' + (anim && !reduceMotion ? ' pop' : '') + '">' + esc(card(a[0]).t) + ' <b>➜</b> ' + esc(card(a[1]).t) + '<small>food energy</small></div>'; }).join('');
        $$('.fs-sm-got', rg).forEach(function (b) { b.addEventListener('click', function (e) { if ($('.sel', tray)) return; e.stopPropagation(); tapArrow(b.dataset.id); }); });
      });
      mig.classList.toggle('ready', n >= 2); mig.classList.toggle('done', !!st.mig);
      if (st.mig) mig.innerHTML = '<img alt="' + esc(S.migrant.alt) + '" src="' + esc(S.migrant.img) + '"><span class="fs-sm-migarr">' + esc(S.migrant.done) + '</span>';
      var lab = tray.previousSibling; tray.style.display = n >= 1 ? 'none' : ''; if (lab) lab.style.display = n >= 1 ? 'none' : '';
      if (n === 3) { info.innerHTML = '<span class="fs-hs-n">✓</span><div><b>' + esc(S.doneTitle || 'Your model is complete') + '</b>' + esc(S.doneLine || '') + '</div>'; ask(); } else if (n === 2) setTimeout(migQ, 0);
    }
    function tapArrow(id) {
      if (step() !== 1) { if (step() === 0) { bounce($('.fs-sm-got[data-id="' + id + '"]', stage), miss, 'First fill both circles: each needs a plant, an animal and the weather.'); } return; }
      var c = card(id);
      if (!pick) { if (c.role !== 'plant') { bounce($('.fs-sm-got[data-id="' + id + '"]', stage), miss, S.startMiss || 'Food energy starts with a plant. Tap a plant first.'); return; } pick = id; SFX.blip(); miss.classList.remove('show'); draw(false); info.innerHTML = '<span class="fs-hs-n">➜</span><div><b>' + esc(c.t) + '</b>Now tap the animal that gets food energy from it.</div>'; return; }
      var p = card(pick), key = pick + '>' + id, ok = (S.arrows[p.z] || []).some(function (a) { return a.join('>') === key; });
      pick = null;
      if (!ok) { draw(false); bounce($('.fs-sm-got[data-id="' + id + '"]', stage), miss, c.arrowMiss || S.arrowMiss); return; }
      st.arr[key] = 1; saveJ('seasonmodel', st); SFX.chime(); miss.classList.remove('show');
      info.innerHTML = '<span class="fs-hs-n">⚡</span><div><b>' + esc(p.t) + ' ➜ ' + esc(c.t) + '</b>' + esc(c.eatWhy || '') + '</div>'; info.classList.remove('flash'); void info.offsetWidth; info.classList.add('flash');
      draw(true);
      if (step() === 2) info.innerHTML = '<span class="fs-hs-n">↔</span><div><b>Last step</b>' + esc(S.migrant.ask) + '</div>';
    }
    shuffle(S.cards).forEach(function (c) { if (st.put[c.id]) return; var k = el('div', 'fs-card fs-sm-card', smPic(c) + '<span>' + esc(c.t) + '</span>'); k.dataset.id = c.id; tray.appendChild(k); });
    function drop(tk, z) {
      var c = card(tk.dataset.id);
      if (c.z === 'no' || z.dataset.z !== c.z) { bounce(tk, miss, c.miss || 'Which place is this true for in January?'); return; }
      st.put[c.id] = 1; saveJ('seasonmodel', st); SFX.chime(); miss.classList.remove('show'); tk.remove();
      info.innerHTML = '<span class="fs-hs-n">✓</span><div><b>' + esc(c.t) + '</b>' + esc(c.why || '') + '</div>'; info.classList.remove('flash'); void info.offsetWidth; info.classList.add('flash');
      draw(false);
      if (step() === 1) info.innerHTML = '<span class="fs-hs-n">⚡</span><div><b>Now draw the food-energy arrows</b>In each circle, tap a plant, then the animal that eats it.</div>';
    }
    $$('.fs-sm-card', tray).forEach(function (k) { dragDrop(k, function () { return rings; }, drop); });
    tapTargets(g, rings, drop);
    function migQ() {
      if (st.mig || step() !== 2 || $('.fs-sm-mq', g)) return;
      var h = el('div', 'fs-sm-mq'); stage.parentNode.insertBefore(h, tray.previousSibling);
      chipsQ(h, S.migrant.q, S.migrant.opts, function () { st.mig = 1; saveJ('seasonmodel', st); SFX.whoosh(); h.remove(); draw(true); }, miss);
    }
    mig.addEventListener('click', function () { if (step() < 2) { bounce(mig, miss, 'Finish the circles and the food-energy arrows first.'); return; } migQ(); });
    function ask() {
      if (qh.dataset.on) return; qh.dataset.on = '1';
      chipsQ(qh, S.q, S.opts, function () { store('seasonmodel-q', '1'); winOnce(win, S.win, S.clue, 'seasonmodel'); }, miss);
      if (store('seasonmodel-q')) { var ok = S.opts.map(function (o, i) { return o.ok ? i : -1; }).filter(function (i) { return i > -1; })[0]; var c = $$('.fs-in-chip', qh)[ok]; if (c) c.classList.add('on', 'ok'); $('.fs-sv-q', qh).dataset.done = '1'; winOnce(win, S.win, S.clue, 'seasonmodel'); }
    }
    at.parentNode.insertBefore(g, at.nextSibling);
    draw(false);
  }

  /* ---------- shared: one chip question that opens once, remembers a right answer, then shows the win (15.01) ---------- */
  function askOnce(qh, q, opts, key, win, winText, clue, mod, miss) {
    if (qh.dataset.on) return; qh.dataset.on = '1';
    chipsQ(qh, q, opts, function () { store(key, '1'); winOnce(win, winText, clue, mod); }, miss);
    if (store(key)) { var ok = opts.map(function (o, i) { return o.ok ? i : -1; }).filter(function (i) { return i > -1; })[0]; var c = $$('.fs-in-chip', qh)[ok]; if (c) c.classList.add('on', 'ok'); var w = $('.fs-sv-q', qh); if (w) w.dataset.done = '1'; winOnce(win, winText, clue, mod); }
  }

  /* ---------- Warm-Up: "Take it apart" — pick an everyday thing, then drag each of its parts to the place on Earth it came from (15.01) ----------
     D.unmake = {afterText, kicker, title, todo[], why, hint, sources:[{k, icon, t, sub}], items:[{id, icon, name, parts:[{id, icon, t, src, why, miss}]}], q, opts, win, clue} */
  function buildUnmake() {
    var U = D.unmake; if (!U) return;
    var at = anchorP(U.afterText); if (!at) { FAILED.push('unmake anchor text not found'); return; }
    var g = gameShell(U.kicker || 'Warm-Up game', U.title, U.todo, U.why); g.dataset.mod = 'unmake';
    var pick = el('div', 'fs-um-items'), stage = el('div', 'fs-um-stage'), srcs = el('div', 'fs-um-srcs');
    var info = el('div', 'fs-hs-card fs-um-info', '<em>' + esc(U.hint || 'Drag a part onto the place it came from, or tap the part and then the place.') + '</em>');
    var miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    U.items.forEach(function (it, i) { var b = el('button', 'fs-in-chip fs-um-item', '<span>' + it.icon + '</span> ' + esc(it.name) + '<em></em>'); b.type = 'button'; b.dataset.i = i; pick.appendChild(b); });
    U.sources.forEach(function (s) { var z = el('div', 'fs-um-src', '<div class="fs-um-sh"><span>' + s.icon + '</span><div><b>' + esc(s.t) + '</b><small>' + esc(s.sub || '') + '</small></div></div><div class="fs-um-pile"></div>'); z.dataset.k = s.k; srcs.appendChild(z); });
    g.appendChild(el('div', 'fs-lu-lab', '1. Pick a thing to take apart')); g.appendChild(pick); g.appendChild(stage);
    g.appendChild(el('div', 'fs-lu-lab', '2. Where on Earth did each part start?')); g.appendChild(srcs);
    g.appendChild(info); g.appendChild(miss); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    var done = loadJ('unmake', {}), cur = -1, zones = $$('.fs-um-src', srcs), total = 0;
    U.items.forEach(function (it) { total += it.parts.length; });
    function partOf(id) { var r = null; U.items.forEach(function (it) { it.parts.forEach(function (p) { if (p.id === id) r = { it: it, p: p }; }); }); return r; }
    function pileAdd(p, it, animate) { var z = $('.fs-um-src[data-k="' + p.src + '"] .fs-um-pile', srcs); if (z) z.appendChild(el('span', 'fs-um-got' + (animate && !reduceMotion ? ' pop' : ''), it.icon + ' ' + esc(p.t))); }
    function emptyNote(box) { if (box && !box.children.length) { var all = U.items.every(function (it) { return it.parts.every(function (p) { return done[p.id]; }); }); box.innerHTML = '<em class="fs-um-empty">' + (all ? '✓ All three things are taken apart!' : '✓ Every part is sorted. Pick another thing above.') + '</em>'; } }
    function show(i, user) {
      cur = i; var it = U.items[i];
      $$('.fs-um-item', pick).forEach(function (b) { b.classList.toggle('on', +b.dataset.i === i); });
      stage.innerHTML = '<div class="fs-um-big' + (user && !reduceMotion ? ' split' : '') + '"><span class="fs-um-ic">' + it.icon + '</span><b>' + esc(it.name) + '</b><small>' + esc(it.sub || 'Its parts:') + '</small></div><div class="fs-um-parts"></div>';
      var box = $('.fs-um-parts', stage);
      it.parts.forEach(function (p) {
        if (done[p.id]) return;
        var c = el('div', 'fs-card fs-um-card', '<span class="fs-um-pi">' + p.icon + '</span>' + esc(p.t)); c.dataset.id = p.id; box.appendChild(c);
        dragDrop(c, function () { return zones; }, drop);
      });
      emptyNote(box);
      if (user) SFX.pop();
    }
    function drop(card, z) {
      var r = partOf(card.dataset.id); if (!r) return;
      if (z.dataset.k !== r.p.src) { bounce(card, miss, r.p.miss || 'Think about where it started. Did it grow, come from the sky, or come out of the ground?'); return; }
      miss.classList.remove('show'); done[r.p.id] = 1; saveJ('unmake', done); SFX.chime(); card.remove(); pileAdd(r.p, r.it, true);
      info.innerHTML = '<span class="fs-hs-n">' + r.p.icon + '</span><div><b>' + esc(r.p.t) + '</b>' + esc(r.p.why) + '</div>'; info.classList.remove('flash'); void info.offsetWidth; info.classList.add('flash');
      emptyNote($('.fs-um-parts', stage)); upd();
    }
    tapTargets(g, zones, drop);
    $$('.fs-um-item', pick).forEach(function (b) { b.addEventListener('click', function () { show(+b.dataset.i, true); }); });
    function upd() {
      var n = Object.keys(done).filter(function (k) { return partOf(k); }).length;
      count.textContent = '🧩 ' + n + ' of ' + total + ' parts sorted'; count.classList.toggle('ok', n === total);
      $$('.fs-um-item', pick).forEach(function (b) { var it = U.items[+b.dataset.i], all = it.parts.every(function (p) { return done[p.id]; }); b.classList.toggle('done', all); $('em', b).textContent = all ? ' ✓' : ''; });
      if (n === total) askOnce(qh, U.q, U.opts, 'unmake-q', win, U.win, U.clue, 'unmake', miss);
    }
    U.items.forEach(function (it) { it.parts.forEach(function (p) { if (done[p.id]) pileAdd(p, it, false); }); });
    at.parentNode.insertBefore(g, at.nextSibling);
    var first = 0; U.items.some(function (it, i) { if (!it.parts.every(function (p) { return done[p.id]; })) { first = i; return true; } });
    show(first, false); upd();
  }

  /* ---------- Lesson: "Refill race" — use every resource up, then drag time forward and watch which ones come back (15.01) ----------
     D.refill = {afterText, kicker, title, todo[], why, stops:[t…], useBtn, rows:[{id, icon, name, levels:[% per stop], fast:[% per stop] (pump twist), kind:'re'|'non', why, miss}],
                 pump:{id, slow, fast, note}, stampQ, stamps:[{k, icon, t}], q, opts, win, clue} */
  function buildRefill() {
    var R = D.refill; if (!R) return;
    var at = anchorP(R.afterText); if (!at) { FAILED.push('refill anchor text not found'); return; }
    var g = gameShell(R.kicker || 'Lesson game', R.title, R.todo, R.why); g.dataset.mod = 'refill';
    var st = loadJ('refill', { used: 0, stop: 0, seen: {}, pump: 'slow', pumps: {}, stamp: {} });
    var top = el('div', 'fs-rf-top', '<button type="button" class="fs-btn fs-rf-use">' + esc(R.useBtn || '⚡ Use them all up') + '</button>' +
      '<div class="fs-rf-time"><label class="fs-mo-lab">⏩ Time since they were used up: <b class="fs-rf-val"></b></label>' +
      '<input type="range" class="fs-mo-range fs-rf-range" min="0" max="' + (R.stops.length - 1) + '" step="1" aria-label="Time since the resources were used up">' +
      '<div class="fs-rf-ticks">' + R.stops.map(function (s, i) { return '<span data-i="' + i + '">' + esc(s) + '</span>'; }).join('') + '</div></div>');
    var rows = el('div', 'fs-rf-rows'), need = el('div', 'fs-mo-need'), stampBox = el('div', 'fs-rf-stamps'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    R.rows.forEach(function (r) {
      var row = el('div', 'fs-rf-row', '<div class="fs-rf-name"><span>' + r.icon + '</span><b>' + esc(r.name) + '</b></div>' +
        '<div class="fs-rf-bar"><i></i></div><div class="fs-rf-st"></div>' +
        (R.pump && R.pump.id === r.id ? '<div class="fs-rf-pump"><span>' + esc(R.pump.label || 'Pumping:') + '</span><button type="button" class="fs-in-chip" data-p="slow">' + esc(R.pump.slow) + '</button><button type="button" class="fs-in-chip" data-p="fast">' + esc(R.pump.fast) + '</button></div>' : ''));
      row.dataset.id = r.id; rows.appendChild(row);
    });
    g.appendChild(top); g.appendChild(rows); g.appendChild(need); g.appendChild(stampBox); g.appendChild(miss); g.appendChild(qh); g.appendChild(win);
    var range = $('.fs-rf-range', top);
    function lvl(r, s) { var a = (R.pump && R.pump.id === r.id && st.pump === 'fast' && r.fast) ? r.fast : r.levels; return st.used ? a[s] : 100; }
    function draw(anim) {
      var s = +st.stop;
      $('.fs-rf-val', top).textContent = st.used ? R.stops[s] : '(use them up first)';
      range.disabled = !st.used; range.value = s; top.classList.toggle('used', !!st.used);
      $$('.fs-rf-ticks span', top).forEach(function (t) { t.classList.toggle('on', st.used && +t.dataset.i === s); t.classList.toggle('seen', !!st.seen[t.dataset.i]); });
      R.rows.forEach(function (r) {
        var row = $('.fs-rf-row[data-id="' + r.id + '"]', rows), v = lvl(r, s), bar = $('.fs-rf-bar i', row);
        bar.style.width = Math.max(v, 0) + '%'; row.classList.toggle('full', v >= 100); row.classList.toggle('gone', v <= 0); row.classList.toggle('anim', !!anim && !reduceMotion);
        $('.fs-rf-st', row).textContent = !st.used ? 'Full' : v >= 100 ? '✅ Back to full' : v <= 0 ? '❌ Still used up' : (v < (lvl(r, Math.max(0, s - 1)) || 0) ? '⬇ Going down' : '🔄 Coming back');
        $$('.fs-rf-pump .fs-in-chip', row).forEach(function (b) { b.classList.toggle('on', b.dataset.p === st.pump); });
      });
      var last = R.stops.length - 1, pumps = R.pump ? (st.pumps.slow && st.pumps.fast) : true;
      var left = [];
      if (!st.used) left.push('press <b>' + esc(R.useBtn || 'Use them all up') + '</b>');
      else {
        if (!st.seen[last]) left.push('drag time all the way to <b>' + esc(R.stops[last]) + '</b>');
        if (!pumps) left.push('try the water at <b>both</b> pumping speeds');
      }
      need.innerHTML = left.length ? '🧪 Next: ' + left.join(', then ') + '.' : '✅ You ran the race. Now stamp each resource below.';
      if (!left.length) stamps();
    }
    $('.fs-rf-use', top).addEventListener('click', function () {
      if (st.used) { st.stop = 0; } st.used = 1; st.seen = { 0: 1 }; st.pumps[st.pump] = 1; saveJ('refill', st); SFX.thud(); draw(true);
    });
    range.addEventListener('input', function () { st.stop = +range.value; st.seen[st.stop] = 1; if (st.stop > 0) st.pumps[st.pump] = 1; saveJ('refill', st); SFX.blip(); draw(true); });
    $$('.fs-rf-pump .fs-in-chip', rows).forEach(function (b) { b.addEventListener('click', function () { st.pump = b.dataset.p; if (st.used && st.stop > 0) st.pumps[st.pump] = 1; saveJ('refill', st); SFX.blip(); draw(true);
      if (R.pump.note && st.used) { var n = R.pump.note[st.pump]; if (n) { miss.classList.remove('show'); var c = $('.fs-rf-pnote', rows) || el('div', 'fs-hs-card fs-rf-pnote'); c.innerHTML = '<span class="fs-hs-n">💧</span><div>' + esc(n) + '</div>'; b.closest('.fs-rf-row').appendChild(c); } } }); });
    function stamps() {
      if (stampBox.dataset.on) return; stampBox.dataset.on = '1';
      stampBox.innerHTML = '<div class="fs-in-k">' + esc(R.stampQ || 'Stamp each one: renewable or nonrenewable?') + '</div>' + R.rows.map(function (r) {
        return '<div class="fs-rf-srow" data-id="' + r.id + '"><span class="fs-rf-sn">' + r.icon + ' ' + esc(r.name) + '</span><span class="fs-rf-sb">' + R.stamps.map(function (s) { return '<button type="button" class="fs-in-chip" data-k="' + s.k + '">' + s.icon + ' ' + esc(s.t) + '</button>'; }).join('') + '</span><span class="fs-rf-why"></span></div>';
      }).join('');
      $$('.fs-rf-srow', stampBox).forEach(function (row) {
        var r = R.rows.filter(function (x) { return x.id === row.dataset.id; })[0];
        function set(animate) { row.classList.add('done'); $$('.fs-in-chip', row).forEach(function (b) { if (b.dataset.k === r.kind) b.classList.add('on', 'ok'); }); $('.fs-rf-why', row).textContent = r.why; if (animate && !reduceMotion) row.classList.add('pop'); }
        $$('.fs-in-chip', row).forEach(function (b) { b.addEventListener('click', function () {
          if (row.classList.contains('done')) return;
          if (b.dataset.k !== r.kind) { bounce(b, miss, r.miss || 'Look at its bar at the end of the race. Did it come back?'); return; }
          miss.classList.remove('show'); st.stamp[r.id] = 1; saveJ('refill', st); SFX.chime(); set(true); check();
        }); });
        if (st.stamp[r.id]) set(false);
      });
      check();
    }
    function check() { if (R.rows.every(function (r) { return st.stamp[r.id]; })) askOnce(qh, R.q, R.opts, 'refill-q', win, R.win, R.clue, 'refill', miss); }
    at.parentNode.insertBefore(g, at.nextSibling); draw(false);
  }

  /* ---------- Lesson: "Impact check" — four real Florida resource photos: stamp renewable or not, then find what using it changes (15.01) ----------
     D.impact = {replace, kicker, title, todo[], why, kinds:[{k, icon, t}], cards:[{id, name, img, alt, kind, kindMiss, use, q, opts:[{t, ok, miss}], fact}], q, opts, credit, win, clue} */
  function buildImpact() {
    var M = D.impact; if (!M) return;
    var wrap = M.replace ? $(M.replace) : null, at = wrap ? null : anchorP(M.afterText);
    if (!wrap && !at) { FAILED.push('impact: no anchor'); return; }
    var g = gameShell(M.kicker || 'Lesson game', M.title, M.todo, M.why); g.dataset.mod = 'impact';
    if (wrap) { var pv = wrap.previousElementSibling; if (pv && pv.tagName === 'P' && pv.textContent.length < 200) pv.classList.add('fs-hide-on'); }
    var tabs = el('div', 'fs-im-tabs'), view = el('div', 'fs-im-view'), miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    M.cards.forEach(function (c, i) { var b = el('button', 'fs-im-tab', '<img alt="" src="' + esc(c.img) + '"><span>' + esc(c.name) + '</span><em></em>'); b.type = 'button'; b.dataset.i = i; tabs.appendChild(b); });
    g.appendChild(tabs); g.appendChild(view); g.appendChild(miss); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    if (M.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(M.credit)));
    var st = loadJ('impact', {});
    function show(i, user) {
      var c = M.cards[i], s = st[c.id] || {};
      $$('.fs-im-tab', tabs).forEach(function (b) { b.classList.toggle('on', +b.dataset.i === i); });
      view.innerHTML = '<div class="fs-im-card' + (user && !reduceMotion ? ' in' : '') + '"><div class="fs-im-photo"><img alt="' + esc(c.alt) + '" src="' + esc(c.img) + '"><span class="fs-im-stamp"></span></div>' +
        '<div class="fs-im-side"><b class="fs-im-name">' + esc(c.name) + '</b><p class="fs-im-use">' + esc(c.use) + '</p><div class="fs-im-s1"></div><div class="fs-im-s2"></div><div class="fs-im-fact"></div></div></div>';
      var s1 = $('.fs-im-s1', view), s2 = $('.fs-im-s2', view), stamp = $('.fs-im-stamp', view), fact = $('.fs-im-fact', view);
      s1.innerHTML = '<div class="fs-in-k">1. Renewable or nonrenewable?</div><div class="fs-in-chips">' + M.kinds.map(function (k) { return '<button type="button" class="fs-in-chip" data-k="' + k.k + '">' + k.icon + ' ' + esc(k.t) + '</button>'; }).join('') + '</div>';
      function kindDone(animate) {
        var k = M.kinds.filter(function (x) { return x.k === c.kind; })[0]; stamp.textContent = k.icon + ' ' + k.t; stamp.className = 'fs-im-stamp on k-' + c.kind + (animate && !reduceMotion ? ' thump' : '');
        $$('.fs-in-chip', s1).forEach(function (b) { if (b.dataset.k === c.kind) b.classList.add('on', 'ok'); }); s1.dataset.done = '1';
        if (!s2.dataset.on) { s2.dataset.on = '1'; var w = chipsQ(s2, '2. ' + c.q, c.opts, function () { s.q = 1; st[c.id] = s; saveJ('impact', st); factOn(true); upd(); }, miss);
          if (s.q) { var ok = c.opts.map(function (o, j) { return o.ok ? j : -1; }).filter(function (j) { return j > -1; })[0]; $$('.fs-in-chip', w)[ok].classList.add('on', 'ok'); w.dataset.done = '1'; factOn(false); } }
      }
      function factOn(animate) { fact.innerHTML = '<span class="fs-hs-n">🔎</span><div>' + esc(c.fact) + '</div>'; fact.className = 'fs-im-fact fs-hs-card' + (animate && !reduceMotion ? ' flash' : ''); }
      $$('.fs-in-chip', s1).forEach(function (b) { b.addEventListener('click', function () {
        if (s1.dataset.done) return;
        if (b.dataset.k !== c.kind) { bounce(b, miss, c.kindMiss); return; }
        miss.classList.remove('show'); s.k = 1; st[c.id] = s; saveJ('impact', st); SFX.chime(); kindDone(true);
      }); });
      if (s.k) kindDone(false);
      if (user) SFX.blip();
    }
    function upd() {
      var n = M.cards.filter(function (c) { return st[c.id] && st[c.id].q; }).length;
      count.textContent = '🔎 ' + n + ' of ' + M.cards.length + ' resources checked'; count.classList.toggle('ok', n === M.cards.length);
      $$('.fs-im-tab', tabs).forEach(function (b) { var c = M.cards[+b.dataset.i], ok = st[c.id] && st[c.id].q; b.classList.toggle('done', !!ok); $('em', b).textContent = ok ? '✓' : ''; });
      if (n === M.cards.length) askOnce(qh, M.q, M.opts, 'impact-q', win, M.win, M.clue, 'impact', miss);
    }
    $$('.fs-im-tab', tabs).forEach(function (b) { b.addEventListener('click', function () { show(+b.dataset.i, true); }); });
    if (wrap) { wrap.parentNode.insertBefore(g, wrap); wrap.classList.add('fs-hide-on'); } else at.parentNode.insertBefore(g, at.nextSibling);
    var first = 0; M.cards.some(function (c, i) { if (!(st[c.id] && st[c.id].q)) { first = i; return true; } });
    show(first, false); upd();
  }

  /* ---------- Lesson Part 4: "Two sources, one claim" — sort the facts from two sources, find what one left out, then pick the fair claim (15.01) ----------
     D.twosources = {afterText, kicker, title, todo[], why, sources:[{k, tag, t, by, img, alt, facts:[{id, t, side, miss}]}], bins:[{k, icon, t}], steps:[{q, opts:[{t, ok, miss}]}], credit, win, clue} */
  function buildTwosources() {
    var T = D.twosources; if (!T) return;
    var at = anchorP(T.afterText); if (!at) { FAILED.push('twosources anchor text not found'); return; }
    var g = gameShell(T.kicker || 'Lesson game', T.title, T.todo, T.why); g.dataset.mod = 'twosources';
    var docs = el('div', 'fs-ts-docs'), bins = el('div', 'fs-ts-bins'), miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), qh = el('div', 'fs-ts-steps'), win = el('div', 'fs-win');
    T.sources.forEach(function (s) {
      docs.appendChild(el('div', 'fs-ts-doc fs-ts-' + s.k, '<div class="fs-ts-tag">' + esc(s.tag) + '</div><div class="fs-ts-h">' + esc(s.t) + '</div><div class="fs-ts-by">' + esc(s.by) + '</div>' +
        (s.img ? '<div class="fs-ts-img"><img alt="' + esc(s.alt || '') + '" src="' + esc(s.img) + '"></div>' : '') +
        '<div class="fs-ts-facts">' + s.facts.map(function (f) { return '<div class="fs-card fs-ts-fact" data-id="' + f.id + '">' + esc(f.t) + '</div>'; }).join('') + '</div>'));
    });
    T.bins.forEach(function (b) { var z = el('div', 'fs-ts-bin fs-ts-b-' + b.k, '<div class="fs-ts-bh"><span>' + b.icon + '</span><b>' + esc(b.t) + '</b></div><div class="fs-ts-pile"></div>'); z.dataset.k = b.k; bins.appendChild(z); });
    g.appendChild(docs); g.appendChild(el('div', 'fs-lu-lab', 'Sort every fact: does it tell a benefit or a cost?')); g.appendChild(bins); g.appendChild(miss); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    if (T.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Credits</summary>' + esc(T.credit)));
    var st = loadJ('twosources', { put: {}, step: 0 }), zones = $$('.fs-ts-bin', bins), all = [];
    T.sources.forEach(function (s) { s.facts.forEach(function (f) { all.push({ s: s, f: f }); }); });
    function factOf(id) { return all.filter(function (x) { return x.f.id === id; })[0]; }
    function placed(x, animate) {
      var card = $('.fs-ts-fact[data-id="' + x.f.id + '"]', docs); if (card) { card.classList.add('placed', 'side-' + x.f.side); card.setAttribute('aria-disabled', 'true'); }
      $('.fs-ts-bin[data-k="' + x.f.side + '"] .fs-ts-pile', bins).appendChild(el('span', 'fs-ts-got' + (animate && !reduceMotion ? ' pop' : ''), '<b>' + esc(x.s.k.toUpperCase()) + '</b> ' + esc(x.f.t)));
    }
    function drop(card, z) {
      var x = factOf(card.dataset.id); if (!x || st.put[x.f.id]) return;
      if (z.dataset.k !== x.f.side) { bounce(card, miss, x.f.miss || 'Ask: is this good for people, or does it hurt the land, water or wildlife?'); return; }
      miss.classList.remove('show'); st.put[x.f.id] = 1; saveJ('twosources', st); SFX.chime(); placed(x, true); upd();
    }
    $$('.fs-ts-fact', docs).forEach(function (c) { dragDrop(c, function () { return zones; }, drop); });
    tapTargets(g, zones, drop);
    function upd() {
      var n = all.filter(function (x) { return st.put[x.f.id]; }).length;
      count.textContent = '🗂 ' + n + ' of ' + all.length + ' facts sorted'; count.classList.toggle('ok', n === all.length);
      if (n === all.length) steps();
    }
    function steps() {
      if (qh.dataset.on) return; qh.dataset.on = '1';
      function next(i) {
        if (i >= T.steps.length) { winOnce(win, T.win, T.clue, 'twosources'); return; }
        var S = T.steps[i], w = chipsQ(qh, (i + 1) + '. ' + S.q, S.opts, function () { if (st.step < i + 1) { st.step = i + 1; saveJ('twosources', st); } next(i + 1); }, miss);
        if (st.step > i) { var ok = S.opts.map(function (o, j) { return o.ok ? j : -1; }).filter(function (j) { return j > -1; })[0]; $$('.fs-in-chip', w)[ok].classList.add('on', 'ok'); w.dataset.done = '1'; next(i + 1); }
      }
      next(0);
    }
    all.forEach(function (x) { if (st.put[x.f.id]) placed(x, false); });
    at.parentNode.insertBefore(g, at.nextSibling); upd();
  }

  /* ---------- shared: a real Florida map (U.S. Census shapes, projected at build time) with resource layers (15.02) ----------
     D.flmap = {viewBox, outline, counties, coast, citrus (paths), perMile, springs, mines, beaches, citrusPts, coastPts (points [x,y]), cities:{name:[x,y]}, pins:{id:[x,y]},
                layers:{k:{t, icon, kind:'area'|'coast'|'dots', c}}} */
  var FL_NS = 'http://www.w3.org/2000/svg';
  function flLayerSVG(k) {
    var M = D.flmap, L = M.layers[k]; if (!L) return '';
    var g = '<g class="fs-fl-layer fs-fl-' + k + '" data-k="' + k + '">';
    if (k === 'citrus') g += '<path d="' + M.citrus + '" fill="' + L.c + '" opacity=".55"/>' + M.citrusPts.map(function (p) { return '<circle cx="' + p[0] + '" cy="' + p[1] + '" r="5" fill="#F08A1C" stroke="#fff" stroke-width="1.5"/>'; }).join('');
    else if (k === 'beaches') g += '<path d="' + M.coast + '" fill="none" stroke="' + L.c + '" stroke-width="6" stroke-linejoin="round" opacity=".9"/>' + M.beaches.map(function (p) { return '<rect x="' + (p[0] - 4) + '" y="' + (p[1] - 4) + '" width="8" height="8" rx="2" fill="#E2574C" stroke="#fff" stroke-width="1.5"/>'; }).join('');
    else if (k === 'phosphate') g += M.mines.map(function (p) { return '<rect x="' + (p[0] - 5) + '" y="' + (p[1] - 5) + '" width="10" height="10" fill="' + L.c + '" stroke="#fff" stroke-width="1.5" transform="rotate(45 ' + p[0] + ' ' + p[1] + ')"/>'; }).join('');
    else if (k === 'springs') g += M.springs.map(function (p) { return '<circle cx="' + p[0] + '" cy="' + p[1] + '" r="5.5" fill="' + L.c + '" stroke="#fff" stroke-width="2"/>'; }).join('');
    return g + '</g>';
  }
  function flSymbol(k) {
    var L = D.flmap.layers[k], c = L.c;
    var s = k === 'citrus' ? '<rect x="2" y="4" width="16" height="12" rx="2" fill="' + c + '" opacity=".7"/><circle cx="10" cy="10" r="4" fill="#F08A1C" stroke="#fff"/>' :
      k === 'beaches' ? '<path d="M1 14 Q10 4 19 14" stroke="' + c + '" stroke-width="5" fill="none"/><rect x="7" y="9" width="6" height="6" rx="1" fill="#E2574C"/>' :
      k === 'phosphate' ? '<rect x="5" y="5" width="10" height="10" fill="' + c + '" transform="rotate(45 10 10)"/>' :
      '<circle cx="10" cy="10" r="6" fill="' + c + '" stroke="#fff" stroke-width="2"/>';
    return '<svg class="fs-fl-sym" viewBox="0 0 20 20" aria-hidden="true">' + s + '</svg>';
  }
  function flMap(opts) {
    var M = D.flmap; opts = opts || {};
    var s = '<svg class="fs-fl-map" viewBox="' + (opts.viewBox || M.viewBox) + '" role="img" aria-label="' + esc(opts.label || 'A map of Florida') + '">' +
      '<rect class="fs-fl-sea" x="-200" y="-200" width="1000" height="960"/>' +
      '<path class="fs-fl-land" d="' + M.outline + '"/><path class="fs-fl-county" d="' + M.counties + '"/>' +
      (opts.layers || []).map(flLayerSVG).join('') +
      (opts.cities === false ? '' : '<g class="fs-fl-cities">' + Object.keys(M.cities).map(function (n) { var p = M.cities[n]; return '<circle cx="' + p[0] + '" cy="' + p[1] + '" r="2.4"/><text x="' + (p[0] + 5) + '" y="' + (p[1] + 4) + '">' + esc(n) + '</text>'; }).join('') + '</g>') +
      '<g class="fs-fl-top"></g></svg>';
    var w = el('div', 'fs-fl-wrap', s);
    return w;
  }
  function flPinsSVG(pins) { var M = D.flmap; return pins.map(function (p) { var xy = M.pins[p.id]; return '<g class="fs-pn-pin" data-id="' + p.id + '"><path d="M' + xy[0] + ' ' + xy[1] + ' l-9 -16 a10 10 0 1 1 18 0z" class="fs-pn-head"/><text x="' + xy[0] + '" y="' + (xy[1] - 19) + '">' + p.n + '</text></g>'; }).join(''); }
  function flShow(wrap, k, on) { var g = $('.fs-fl-' + k, wrap); if (g) g.classList.toggle('on', on !== false); }
  function flPoint(svg, e) { var pt = svg.createSVGPoint(); pt.x = e.clientX; pt.y = e.clientY; var m = svg.getScreenCTM(); if (!m) return null; var q = pt.matrixTransform(m.inverse()); return [q.x, q.y]; }
  function flMiles(k, p, svg) {
    var M = D.flmap, pts = k === 'citrus' ? M.citrusPts : k === 'beaches' ? M.coastPts : k === 'phosphate' ? M.mines : M.springs;
    if (k === 'citrus' && svg) { var pa = $('.fs-fl-citrus path', svg); try { var sp = svg.createSVGPoint(); sp.x = p[0]; sp.y = p[1]; if (pa && pa.isPointInFill && pa.isPointInFill(sp)) return 0; } catch (e) {} }
    var best = 1e9; pts.forEach(function (q) { var d = Math.hypot(q[0] - p[0], q[1] - p[1]); if (d < best) best = d; });
    return Math.round(best / M.perMile);
  }

  /* ---------- Warm-Up: "Guess first" — drop a star for each resource on a blank Florida map, then reveal the real data (15.02) ----------
     D.guessmap = {afterText, kicker, title, todo[], why, tokens:[k…], revealBtn, near, far, q, opts, win, clue} */
  function buildGuessmap() {
    var G = D.guessmap; if (!G || !D.flmap) return;
    var at = anchorP(G.afterText); if (!at) { FAILED.push('guessmap anchor text not found'); return; }
    var g = gameShell(G.kicker || 'Warm-Up game', G.title, G.todo, G.why); g.dataset.mod = 'guessmap';
    var L = D.flmap.layers, st = loadJ('guessmap', { at: {}, shown: 0 }), cur = null;
    var chips = el('div', 'fs-gm-chips'), wrap = flMap({ layers: G.tokens, label: 'A blank map of Florida. Tap to place a star.' }), res = el('div', 'fs-gm-res');
    var btn = el('button', 'fs-btn fs-gm-go', esc(G.revealBtn || '🗺 Show me the real map')); btn.type = 'button';
    var miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    G.tokens.forEach(function (k) { var b = el('button', 'fs-in-chip fs-gm-chip', flSymbol(k) + ' ' + esc(L[k].t) + '<em></em>'); b.type = 'button'; b.dataset.k = k; chips.appendChild(b); });
    wrap.classList.add('fs-gm-map');
    g.appendChild(chips); g.appendChild(wrap); g.appendChild(btn); g.appendChild(res); g.appendChild(miss); g.appendChild(qh); g.appendChild(win);
    var svg = $('svg', wrap), top = $('.fs-fl-top', svg);
    function stars() {
      top.innerHTML = G.tokens.filter(function (k) { return st.at[k]; }).map(function (k) { var p = st.at[k]; return '<g class="fs-gm-star" data-k="' + k + '"><path d="M' + p[0] + ' ' + (p[1] - 11) + ' l3.4 7 7.6 1.1 -5.5 5.3 1.3 7.6 -6.8 -3.6 -6.8 3.6 1.3 -7.6 -5.5 -5.3 7.6 -1.1z" fill="' + L[k].c + '" stroke="#0E1C42" stroke-width="1.6"/></g>'; }).join('') +
        (st.shown ? G.tokens.map(function (k) { var p = st.at[k]; if (!p) return ''; var M = D.flmap, pts = k === 'citrus' ? M.citrusPts : k === 'beaches' ? M.coastPts : k === 'phosphate' ? M.mines : M.springs, b = null, bd = 1e9; pts.forEach(function (q) { var d = Math.hypot(q[0] - p[0], q[1] - p[1]); if (d < bd) { bd = d; b = q; } }); return b && bd > 6 ? '<line class="fs-gm-line" x1="' + p[0] + '" y1="' + p[1] + '" x2="' + b[0] + '" y2="' + b[1] + '"/>' : ''; }).join('') : '');
      $$('.fs-gm-chip', chips).forEach(function (b) { var k = b.dataset.k; b.classList.toggle('done', !!st.at[k]); b.classList.toggle('on', cur === k); $('em', b).textContent = st.at[k] ? ' ★' : ''; });
      btn.disabled = !G.tokens.every(function (k) { return st.at[k]; }) || !!st.shown;
      btn.style.display = st.shown ? 'none' : '';
    }
    $$('.fs-gm-chip', chips).forEach(function (b) { b.addEventListener('click', function () { if (st.shown) return; cur = b.dataset.k; SFX.blip(); stars(); }); });
    svg.addEventListener('click', function (e) {
      if (st.shown) return;
      if (!cur) { cur = G.tokens.filter(function (k) { return !st.at[k]; })[0] || null; if (!cur) return; }
      var p = flPoint(svg, e); if (!p) return; st.at[cur] = [Math.round(p[0]), Math.round(p[1])]; saveJ('guessmap', st); SFX.pop();
      cur = G.tokens.filter(function (k) { return !st.at[k]; })[0] || null; stars();
    });
    function reveal(anim) {
      G.tokens.forEach(function (k, i) { if (anim && !reduceMotion) setTimeout(function () { flShow(wrap, k); SFX.chime(); }, 350 * i); else flShow(wrap, k); });
      res.innerHTML = '<div class="fs-in-k">How close were you?</div>' + G.tokens.map(function (k) {
        var mi = flMiles(k, st.at[k], svg);
        return '<div class="fs-gm-row">' + flSymbol(k) + '<b>' + esc(L[k].t) + '</b><span>' + (mi <= (G.near || 25) ? '🎯 Right on it!' : mi <= (G.far || 90) ? '👍 About ' + mi + ' miles off' : '🧭 About ' + mi + ' miles off') + '</span></div>';
      }).join('') + '<div class="fs-gm-keynote">' + G.tokens.map(function (k) { return '<span>' + flSymbol(k) + esc(L[k].t) + '</span>'; }).join('') + '</div>';
      stars(); askOnce(qh, G.q, G.opts, 'guessmap-q', win, G.win, G.clue, 'guessmap', miss);
    }
    btn.addEventListener('click', function () { st.shown = 1; saveJ('guessmap', st); SFX.whoosh(); reveal(true); });
    at.parentNode.insertBefore(g, at.nextSibling); stars(); if (st.shown) reveal(false);
  }

  /* ---------- Lesson: "Map layers" — turn on one layer at a time with the map key, then stamp each pattern (15.02) ----------
     D.maplayers = {afterText, kicker, title, todo[], why, layers:[k…], patterns:[{k, icon, t}], answer:{k: patternK}, note:{k: t}, miss:{k: t}, q, opts, win, clue} */
  function buildMaplayers() {
    var Y = D.maplayers; if (!Y || !D.flmap) return;
    var at = anchorP(Y.afterText); if (!at) { FAILED.push('maplayers anchor text not found'); return; }
    var g = gameShell(Y.kicker || 'Lesson game', Y.title, Y.todo, Y.why); g.dataset.mod = 'maplayers';
    var L = D.flmap.layers, st = loadJ('maplayers', { on: {}, ok: {} });
    var box = el('div', 'fs-ml-box'), wrap = flMap({ layers: Y.layers, label: 'A map of Florida with resource layers you can turn on.' }), key = el('div', 'fs-ml-key');
    key.innerHTML = '<div class="fs-ml-kh">🔑 Map key</div>' + Y.layers.map(function (k) {
      return '<div class="fs-ml-row" data-k="' + k + '"><label class="fs-ml-tog"><input type="checkbox"> ' + flSymbol(k) + '<b>' + esc(L[k].t) + '</b></label>' +
        '<div class="fs-ml-pat"><span class="fs-ml-q">Pattern:</span>' + Y.patterns.map(function (p) { return '<button type="button" class="fs-in-chip" data-p="' + p.k + '">' + p.icon + ' ' + esc(p.t) + '</button>'; }).join('') + '</div><div class="fs-ml-note"></div></div>';
    }).join('');
    box.appendChild(wrap); box.appendChild(key);
    var miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(box); g.appendChild(miss); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    $$('.fs-ml-row', key).forEach(function (row) {
      var k = row.dataset.k, cb = $('input', row);
      function setOk(anim) { row.classList.add('ok'); $$('.fs-in-chip', row).forEach(function (b) { if (b.dataset.p === Y.answer[k]) b.classList.add('on', 'ok'); }); $('.fs-ml-note', row).textContent = Y.note[k]; if (anim && !reduceMotion) row.classList.add('pop'); }
      cb.checked = !!st.on[k]; flShow(wrap, k, cb.checked); row.classList.toggle('open', cb.checked);
      cb.addEventListener('change', function () { st.on[k] = cb.checked ? 1 : 0; saveJ('maplayers', st); flShow(wrap, k, cb.checked); row.classList.toggle('open', cb.checked); SFX.blip(); upd(); });
      $$('.fs-in-chip', row).forEach(function (b) { b.addEventListener('click', function () {
        if (row.classList.contains('ok')) return;
        if (!cb.checked) { cb.checked = true; cb.dispatchEvent(new Event('change')); }
        if (b.dataset.p !== Y.answer[k]) { bounce(b, miss, Y.miss[k]); return; }
        miss.classList.remove('show'); st.ok[k] = 1; saveJ('maplayers', st); SFX.chime(); setOk(true); upd();
      }); });
      if (st.ok[k]) setOk(false);
    });
    function upd() {
      var n = Y.layers.filter(function (k) { return st.ok[k]; }).length;
      count.textContent = '🗺 ' + n + ' of ' + Y.layers.length + ' patterns read'; count.classList.toggle('ok', n === Y.layers.length);
      if (n === Y.layers.length) askOnce(qh, Y.q, Y.opts, 'maplayers-q', win, Y.win, Y.clue, 'maplayers', miss);
    }
    at.parentNode.insertBefore(g, at.nextSibling); upd();
  }

  /* ---------- Lesson Part 3: "Why here?" — each resource's pattern (a small map) gets the cause that explains it (15.02) ----------
     D.whyhere = {replace, kicker, title, todo[], why, causes:[{id, icon, t}], items:[{k, cause, why, miss}], q, opts, win, clue} */
  function buildWhyhere() {
    var W = D.whyhere; if (!W || !D.flmap) return;
    var wrap = W.replace ? $(W.replace) : null, at = wrap ? null : anchorP(W.afterText);
    if (!wrap && !at) { FAILED.push('whyhere: no anchor'); return; }
    var g = gameShell(W.kicker || 'Lesson game', W.title, W.todo, W.why); g.dataset.mod = 'whyhere';
    if (wrap) { var pv = wrap.previousElementSibling; if (pv && pv.tagName === 'P' && pv.textContent.length < 200) pv.classList.add('fs-hide-on'); }
    var L = D.flmap.layers, st = loadJ('whyhere', {});
    var grid = el('div', 'fs-wy-grid'), tray = el('div', 'fs-wy-tray'), miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    W.items.forEach(function (it) {
      var c = el('div', 'fs-wy-card', '<div class="fs-wy-h">' + flSymbol(it.k) + '<b>' + esc(L[it.k].t) + '</b></div>');
      var m = flMap({ layers: [it.k], cities: false, label: 'Where ' + L[it.k].t.toLowerCase() + ' are found in Florida.' }); flShow(m, it.k); c.appendChild(m);
      c.appendChild(el('div', 'fs-wy-slot', '<em>Drop the reason here</em>')); c.dataset.k = it.k; grid.appendChild(c);
    });
    shuffle(W.causes).forEach(function (cz) { if (Object.keys(st).some(function (k) { return st[k] === cz.id; })) return; var k = el('div', 'fs-card fs-wy-cause', '<span>' + cz.icon + '</span> ' + esc(cz.t)); k.dataset.id = cz.id; tray.appendChild(k); });
    g.appendChild(grid); g.appendChild(el('div', 'fs-lu-lab', 'Reasons (one is a trick)')); g.appendChild(tray); g.appendChild(miss); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    var zones = $$('.fs-wy-card', grid);
    function placed(it, anim) {
      var cz = W.causes.filter(function (x) { return x.id === it.cause; })[0], card = $('.fs-wy-card[data-k="' + it.k + '"]', grid);
      card.classList.add('done'); $('.fs-wy-slot', card).innerHTML = '<b>' + cz.icon + ' ' + esc(cz.t) + '</b><span>' + esc(it.why) + '</span>'; if (anim && !reduceMotion) card.classList.add('pop');
      var t = $('.fs-wy-cause[data-id="' + cz.id + '"]', tray); if (t) t.remove();
    }
    function drop(tk, z) {
      var it = W.items.filter(function (x) { return x.k === z.dataset.k; })[0]; if (!it || st[it.k]) return;
      if (tk.dataset.id !== it.cause) { var dec = W.causes.filter(function (x) { return x.id === tk.dataset.id; })[0]; bounce(tk, miss, (dec && dec.miss) || it.miss); return; }
      miss.classList.remove('show'); st[it.k] = it.cause; saveJ('whyhere', st); SFX.chime(); placed(it, true); upd();
    }
    $$('.fs-wy-cause', tray).forEach(function (k) { dragDrop(k, function () { return zones; }, drop); });
    tapTargets(g, zones, drop);
    function upd() {
      var n = W.items.filter(function (it) { return st[it.k]; }).length;
      count.textContent = '🧩 ' + n + ' of ' + W.items.length + ' patterns explained'; count.classList.toggle('ok', n === W.items.length);
      if (n === W.items.length) askOnce(qh, W.q, W.opts, 'whyhere-q', win, W.win, W.clue, 'whyhere', miss);
    }
    W.items.forEach(function (it) { if (st[it.k]) placed(it, false); });
    if (wrap) { wrap.parentNode.insertBefore(g, wrap); wrap.classList.add('fs-hide-on'); } else at.parentNode.insertBefore(g, at.nextSibling);
    upd();
  }

  /* ---------- Lesson Part 4: "Test the pins" — check each of the volunteer's map pins against the layers: rule it in or out, then pick the evidence (15.02) ----------
     D.pins = {afterText, kicker, title, todo[], why, layers:[k…], verdicts:[{k, icon, t}], pins:[{id, n, name, note, verdict, vmiss, q, opts:[{t, ok, miss}], why}], q, opts, win, clue} */
  function buildPins() {
    var P = D.pins; if (!P || !D.flmap) return;
    var at = anchorP(P.afterText); if (!at) { FAILED.push('pins anchor text not found'); return; }
    var g = gameShell(P.kicker || 'Lesson game', P.title, P.todo, P.why); g.dataset.mod = 'pins';
    var st = loadJ('pins', {}), M = D.flmap;
    var box = el('div', 'fs-pn-box'), wrap = flMap({ layers: P.layers, label: 'A map of Florida with resource layers and four numbered pins.' }), side = el('div', 'fs-pn-side');
    P.layers.forEach(function (k) { flShow(wrap, k); });
    var svg = $('svg', wrap), top = $('.fs-fl-top', svg);
    top.innerHTML = P.pins.map(function (p) { var xy = M.pins[p.id]; return '<g class="fs-pn-pin" data-id="' + p.id + '" tabindex="0" role="button" aria-label="Pin ' + p.n + ': ' + esc(p.name) + '"><circle class="fs-pn-ring" cx="' + xy[0] + '" cy="' + xy[1] + '" r="16"/><path d="M' + xy[0] + ' ' + xy[1] + ' l-9 -16 a10 10 0 1 1 18 0z" class="fs-pn-head"/><text x="' + xy[0] + '" y="' + (xy[1] - 19) + '">' + p.n + '</text></g>'; }).join('');
    box.appendChild(wrap); box.appendChild(side);
    var keyRow = el('div', 'fs-gm-keynote', P.layers.map(function (k) { return '<span>' + flSymbol(k) + esc(M.layers[k].t) + '</span>'; }).join(''));
    var miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(keyRow); g.appendChild(box); g.appendChild(miss); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    function zoom(p) {
      if (!p) { svg.setAttribute('viewBox', M.viewBox); return; }
      var xy = M.pins[p.id], z = 200; svg.setAttribute('viewBox', (xy[0] - z / 2) + ' ' + (xy[1] - z / 2) + ' ' + z + ' ' + z);
    }
    function show(p) {
      $$('.fs-pn-pin', svg).forEach(function (x) { x.classList.toggle('on', x.dataset.id === p.id); });
      var s = st[p.id] || {};
      side.innerHTML = '<div class="fs-pn-card' + (reduceMotion ? '' : ' in') + '"><div class="fs-pn-n">📍 Pin ' + p.n + '</div><b>' + esc(p.name) + '</b><p class="fs-pn-note">“' + esc(p.note) + '”</p>' +
        '<div class="fs-in-k">1. Could Marco find phosphate here?</div><div class="fs-in-chips fs-pn-v">' + P.verdicts.map(function (v) { return '<button type="button" class="fs-in-chip" data-k="' + v.k + '">' + v.icon + ' ' + esc(v.t) + '</button>'; }).join('') + '</div><div class="fs-pn-q"></div><div class="fs-pn-why"></div>' +
        '<button type="button" class="fs-btn alt fs-pn-back">🗺 Back to the whole map</button></div>';
      var vbox = $('.fs-pn-v', side), qbox = $('.fs-pn-q', side), why = $('.fs-pn-why', side);
      $('.fs-pn-back', side).addEventListener('click', function () { zoom(null); $$('.fs-pn-pin', svg).forEach(function (x) { x.classList.remove('on'); }); side.innerHTML = '<em class="fs-pn-hint">' + esc(P.hint || 'Tap a numbered pin on the map.') + '</em>'; SFX.blip(); });
      function vDone() { $$('.fs-in-chip', vbox).forEach(function (b) { if (b.dataset.k === p.verdict) b.classList.add('on', 'ok'); }); vbox.dataset.done = '1';
        if (!qbox.dataset.on) { qbox.dataset.on = '1'; var w = chipsQ(qbox, '2. ' + p.q, p.opts, function () { s.q = 1; st[p.id] = s; saveJ('pins', st); whyOn(true); upd(); }, miss);
          if (s.q) { var ok = p.opts.map(function (o, j) { return o.ok ? j : -1; }).filter(function (j) { return j > -1; })[0]; $$('.fs-in-chip', w)[ok].classList.add('on', 'ok'); w.dataset.done = '1'; whyOn(false); } } }
      function whyOn(anim) { why.innerHTML = '<span class="fs-hs-n">' + (p.verdict === 'yes' ? '✅' : '❌') + '</span><div>' + esc(p.why) + '</div>'; why.className = 'fs-pn-why fs-hs-card' + (anim && !reduceMotion ? ' flash' : ''); }
      $$('.fs-in-chip', vbox).forEach(function (b) { b.addEventListener('click', function () {
        if (vbox.dataset.done) return;
        if (b.dataset.k !== p.verdict) { bounce(b, miss, p.vmiss); return; }
        miss.classList.remove('show'); s.v = 1; st[p.id] = s; saveJ('pins', st); SFX.chime(); vDone();
      }); });
      if (s.v) vDone();
      zoom(p); SFX.whoosh();
    }
    $$('.fs-pn-pin', svg).forEach(function (el2) {
      function go() { show(P.pins.filter(function (x) { return x.id === el2.dataset.id; })[0]); }
      el2.addEventListener('click', go); el2.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); go(); } });
    });
    function upd() {
      var n = P.pins.filter(function (p) { return st[p.id] && st[p.id].q; }).length;
      count.textContent = '📍 ' + n + ' of ' + P.pins.length + ' pins tested'; count.classList.toggle('ok', n === P.pins.length);
      $$('.fs-pn-pin', svg).forEach(function (x) { var s = st[x.dataset.id]; x.classList.toggle('done', !!(s && s.q)); });
      if (n === P.pins.length) askOnce(qh, P.q, P.opts, 'pins-q', win, P.win, P.clue, 'pins', miss);
    }
    side.innerHTML = '<em class="fs-pn-hint">' + esc(P.hint || 'Tap a numbered pin on the map.') + '</em>';
    at.parentNode.insertBefore(g, at.nextSibling); upd();
  }

  function buildQuiz() {
    var qs = $$('#tab-quiz .quiz-q'); if (!qs.length) return;
    var Q = D.quizMiss || {};
    qs.forEach(function (q, i) {
      if (i > 0) q.classList.add('fs-later');
      q.insertBefore(fsOnly(el('div', 'fs-qprog', (D.quizKicker ? esc(D.quizKicker) + ' · ' : '') + 'Question ' + (i + 1) + ' of ' + qs.length)), q.firstChild);
      var nb = fsOnly(el('button', 'fs-btn fs-qnext', i < qs.length - 1 ? 'Next question ▶' : 'See my score ▶')); nb.type = 'button';
      q.appendChild(nb);
      nb.addEventListener('click', function () { nb.classList.remove('show'); if (qs[i + 1]) { qs[i + 1].classList.remove('fs-later'); qs[i + 1].scrollIntoView({ behavior: reduceMotion ? 'auto' : 'smooth', block: 'center' }); } });
      $$('.quiz-opt', q).forEach(function (o) {
        o.addEventListener('click', function () {
          setTimeout(function () {
            if (!q.classList.contains('answered')) return;
            var v = o.getAttribute('data-val'), key = 'q' + (i + 1);
            if (o.classList.contains('wrong') && Q[key] && Q[key][v] && !$('.fs-qmiss', q)) {
              var m = fsOnly(el('div', 'fs-miss show fs-qmiss', '🔎 ' + esc(Q[key][v]))); var fb = $('.fb-wrong', q); fb.parentNode.insertBefore(m, fb); SFX.thud();
            } else if (o.classList.contains('correct')) SFX.chime();
            if (i < qs.length - 1) nb.classList.add('show');
          }, 30);
        });
      });
    });
    var score = $('#quizScore'); if (score) score.classList.add('fs-scorebox');
  }

  /* ---------- Assignment: chips, counters, hint ladders, planner ---------- */
  function words(t) { t = t.replace(/“[^”]*”/g, ' ').replace(/"[^"]*"/g, ' ').replace(/\([^)]*\)/g, ' '); return (t.trim().match(/[A-Za-z0-9'’]+/g) || []).length; }
  function chipOn(c, text) {
    var t = text.toLowerCase();
    if (c.any) { var hits = 0; c.any.forEach(function (r) { if (new RegExp(r, 'i').test(t)) hits++; }); return hits >= (c.min || 1); }
    return new RegExp(c.re, 'i').test(t);
  }
  function buildHelpers() {
    var F = D.flags || {}, H = D.hints || {}, M = D.minWords || {}, S = D.scholar || {};
    Object.keys(Object.assign({}, F, H, M)).forEach(helpFor);
    buildPlanner();
  }
  function helpFor(id) {
    var F = D.flags || {}, H = D.hints || {}, M = D.minWords || {}, S = D.scholar || {};
    (function () {
      var ta = document.getElementById(id); if (!ta || ta.dataset.fsHelp) return; ta.dataset.fsHelp = '1';
      var box = fsOnly(el('div', 'fs-help'));
      var chips = null, count = null;
      if (F[id]) { chips = el('div', 'fs-chips', '<span class="fs-chips-k">Your answer needs:</span>'); F[id].forEach(function (c) { var s = el('span', 'fs-chip', esc(c.label)); chips.appendChild(s); }); box.appendChild(chips); }
      if (M[id]) { count = el('div', 'fs-count'); box.appendChild(count); }
      if (H[id]) {
        var hb = el('button', 'fs-hintbtn', '💡 Need a hint?'); hb.type = 'button'; var hl = el('div', 'fs-hints'); var n = 0;
        hb.addEventListener('click', function () { if (n < H[id].length) { hl.appendChild(el('div', 'fs-hint', '<b>Hint ' + (n + 1) + ':</b> ' + esc(H[id][n]))); n++; SFX.blip(); } if (n >= H[id].length) { hb.disabled = true; hb.textContent = 'That\'s all the hints'; } else hb.textContent = '💡 Another hint (' + (n + 1) + ' of ' + H[id].length + ')'; });
        box.appendChild(hb); box.appendChild(hl);
      }
      if (S[id]) box.appendChild(el('div', 'fs-scholar', '🔭 Go further: ' + esc(S[id])));
      ta.parentNode.insertBefore(box, ta.nextSibling);
      function upd() {
        var v = ta.value || '';
        if (chips) $$('.fs-chip', chips).forEach(function (s, i) { var was = s.classList.contains('on'); var on = chipOn(F[id][i], v); s.classList.toggle('on', on); if (on && !was) SFX.blip(); });
        if (count) { var w = words(v); count.textContent = '📝 ' + Math.min(w, M[id]) + ' of ' + M[id] + ' words' + (w >= M[id] ? ' ✓' : w > 0 ? '. Keep going…' : ''); count.classList.toggle('ok', w >= M[id]); }
      }
      ta.addEventListener('input', upd); setTimeout(upd, 300);
    })();
  }
  function buildPlanner() {
    var P = D.planner; if (!P) return;
    var ta = document.getElementById(P.before); if (!ta) return;
    var plan = fsOnly(el('div', 'fs-plan fs-kraft'));
    var h = '<div class="fs-game-k" style="color:#7A5F2C">Plan before you write</div><div class="fs-game-t" style="font-size:18px">' + esc(P.title) + '</div>';
    P.rows.forEach(function (r, ri) { h += '<div class="fs-plan-row" data-r="' + ri + '" data-max="' + (r.pick || 1) + '"><b>' + esc(r.label) + '</b>' + r.options.map(function (o) { return '<button type="button" class="fs-opt">' + esc(o) + '</button>'; }).join('') + '</div>'; });
    plan.innerHTML = h + '<div class="fs-plan-note">' + esc(P.note) + '</div>';
    $$('.fs-plan-row', plan).forEach(function (row) {
      var max = +row.dataset.max;
      $$('.fs-opt', row).forEach(function (b) { b.addEventListener('click', function () {
        if (b.classList.contains('on')) { b.classList.remove('on'); return; }
        var on = $$('.fs-opt.on', row); if (on.length >= max) on[0].classList.remove('on');
        b.classList.add('on'); SFX.blip();
      }); });
    });
    ta.parentNode.insertBefore(plan, ta);
  }

  /* ---------- Specimen: earned when the checklist is done ---------- */
  function buildSpecimen() {
    var Sp = D.specimen; if (!Sp) return;
    var items = $$('#tab-assignment .checklist-item'); if (!items.length) return;
    var box = fsOnly(el('div', 'fs-specimen fs-kraft'));
    box.innerHTML = '<div class="fs-game-k" style="color:#7A5F2C">' + esc(Sp.kicker || 'Specimen collected') + '</div><div class="fs-tag"><div class="fs-tag-ic">' + Sp.icon + '</div><div class="fs-tag-k">Specimen ' + esc(D.label || D.lesson) + '</div><div class="fs-tag-t">' + esc(Sp.name) + '</div><div class="fs-stamp">' + esc(Sp.stamp || 'LOGGED') + '</div></div>' +
      '<p style="margin:14px 0 10px;font-size:15px;line-height:1.55">' + esc(Sp.line) + '</p><button class="fs-btn alt" type="button">📓 Open my Field Notebook</button>';
    $('.fs-btn', box).addEventListener('click', openNotebook);
    var list = items[items.length - 1].parentNode;
    list.parentNode.insertBefore(box, list.nextSibling);
    function check() {
      var all = items.every(function (it) { return it.classList.contains('checked'); });
      if (all && !box.classList.contains('show')) { box.classList.add('show'); setTimeout(SFX.stamp, 500); store('specimen', '1'); updateCount(); progress(); }
    }
    items.forEach(function (it) { it.addEventListener('click', function () { setTimeout(check, 80); }); });
    if (store('specimen')) { box.classList.add('show'); }
  }

  /* =================== v3: ID badge, marsh sounds, field camera, field journal =================== */
  function progress() { document.dispatchEvent(new Event('fs:progress')); }

  /* ---------- name: asked once, shared with ELA/SS ---------- */
  function getName() {
    var keys = ['oao.fs.profile', 'oao.ff.profile', 'oao.profile'];
    for (var i = 0; i < keys.length; i++) {
      try { var v = localStorage.getItem(keys[i]); if (!v) continue; var n = v; try { var j = JSON.parse(v); n = (j && (j.name || j.first || j.firstName)) || (typeof j === 'string' ? j : ''); } catch (e) {} if (n && !unkind(n)) return String(n).slice(0, 24); } catch (e) {}
    }
    var g = document.getElementById('student-name'); return g && g.value.trim() && !unkind(g.value) ? g.value.trim().slice(0, 24) : '';
  }
  /* ---------- kind-name check (names show in badges, the journal and Gathered Answers) ----------
     WORDS: whole words only (so Cassie, Bob, Kshitij and Hancock are fine).
     START: also caught at the start of a word (Shithead).  ANY: caught anywhere, even with spaces or
     symbols in between (f.u.c.k, b1tch). Repeated letters are allowed (fuuuck, poooop). */
  var NAME_WORDS = ['ass','arse','butt','butts','booty','bum','poo','poop','poopy','pee','peepee','wee','weewee','piss','pp',
    'dick','cock','tit','tits','titty','boob','boobs','balls','nut','nuts','weiner','wiener','sex','crap','damn','hell',
    'turd','doodoo','dookie','fart','farts','puke','barf','booger','boogers','snot','toilet','diaper','suck','sucks',
    'shit','shits','shitty','stupid','dumb','idiot','loser','ugly','fat','kill','die','dead','hate','kys','noob','sus'];
  var NAME_START = ['butt','poop','fart','boob','crap','piss'];
  var NAME_ANY = ['fuck','fuk','fck','bitch','biatch','cunt','nigg','niga','faggot','slut','whore','penis','vagina','pussy',
    'porn','dildo','asshole','dumbass','jackass','badass','retard','nazi','hitler','sexy','poophead','butthead','buttface',
    'fartface','poopface','shithead','shitface','dickhead','wtf','stfu','bastard','motherf','kkk'];
  var LEET = { '0': 'o', '1': 'i', '!': 'i', '|': 'i', '3': 'e', '4': 'a', '@': 'a', '5': 's', '$': 's', '7': 't', '8': 'b', '9': 'g', '+': 't' };
  function wordRe(w, how) { var r = w.split('').map(function (c) { return c + '+'; }).join(''); return new RegExp(how === 'any' ? r : how === 'start' ? '^' + r : '^' + r + '$'); }
  var NAME_RES = NAME_WORDS.map(function (w) { return wordRe(w, 'word'); }), NAME_RES_S = NAME_START.map(function (w) { return wordRe(w, 'start'); }),
      NAME_RES_A = NAME_ANY.map(function (w) { return wordRe(w, 'any'); });
  function unkind(n) {
    var low = String(n || '').toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '').replace(/[0-9!|@$+]/g, function (c) { return LEET[c] || c; });
    var toks = low.split(/[^a-z]+/).filter(Boolean), squash = toks.join('');
    if (NAME_RES_A.some(function (r) { return r.test(squash); })) return true;
    var all = toks.concat(toks.length > 1 ? [squash] : []);
    return all.some(function (t) { return NAME_RES.some(function (r) { return r.test(t); }) || NAME_RES_S.some(function (r) { return r.test(t); }); });
  }
  window.fsUnkindName = unkind;
  var KIND_MSG = 'Let’s keep it kind. Please type your real first name.';
  function nameProblem(n) {
    if (!n || n.length < 2) return 'Type your first name (at least 2 letters).';
    if (!/^[A-Za-zÀ-ÿ' -]+$/.test(n)) return 'Use letters only, please.';
    if (unkind(n)) return KIND_MSG;
    return '';
  }
  /* guard the page's own "Your name" box in Gathered Answers too */
  function guardNameBox() {
    var g = document.getElementById('student-name'); if (!g || g.dataset.fsKind) return; g.dataset.fsKind = '1';
    var note = el('div', 'fs-name-note'); note.setAttribute('role', 'alert'); var row = g.closest('.gathered-name-row') || g; row.parentNode.insertBefore(note, row.nextSibling);
    function check(final) {
      var v = g.value;
      if (unkind(v)) {
        g.value = ''; g.dispatchEvent(new Event('input', { bubbles: true }));
        note.textContent = KIND_MSG; note.classList.add('on'); try { SFX.thud(); } catch (e) {}
        try { localStorage.removeItem(g.id); } catch (e) {}
      } else if (v.trim()) { note.classList.remove('on'); }
    }
    g.addEventListener('input', function () { if (/[\s'-]$/.test(g.value)) check(false); });
    g.addEventListener('blur', function () { check(true); });
    g.addEventListener('change', function () { check(true); });
    check(true);
  }
  function setName(n) { try { localStorage.setItem('oao.fs.profile', JSON.stringify({ name: n })); } catch (e) {} var g = document.getElementById('student-name'); if (g && !g.value) { g.value = n; g.dispatchEvent(new Event('input', { bubbles: true })); } }

  /* ---------- Field Station ID + rank ---------- */
  function rank() {
    var R = D.ranks || [
      { at: 'start', icon: '🥾', t: 'Trainee' }, { at: 'clue1', icon: '🔦', t: 'Field Scout' },
      { at: 'allclues', icon: '🔬', t: 'Field Scientist' }, { at: 'solved', icon: '🕵️', t: 'Case Cracker' }, { at: 'closed', icon: '🏅', t: 'Lead Investigator' }];
    var n = cluesFound().length, all = D.case ? D.case.clues.length : 0, r = R[0];
    if (n >= 1) r = R[1]; if (all && n >= all) r = R[2]; if (store('solved')) r = R[3]; if (store('specimen')) r = R[4];
    return r;
  }
  function buildID() {
    var card = $('.fs-casecard .fs-folder'); if (!card) return;
    var id = fsOnly(el('div', 'fs-id'));
    card.insertBefore(id, card.firstChild);
    function draw() {
      var n = getName(), r = rank();
      if (!n) {
        id.innerHTML = '<div class="fs-id-h">FIELD STATION ID</div><div class="fs-id-ask">What’s your first name, scientist?</div>' +
          '<input class="fs-id-in" maxlength="20" placeholder="First name"><button type="button" class="fs-btn fs-id-go">Get my badge</button><div class="fs-id-err"></div>';
        var inp = $('.fs-id-in', id), err = $('.fs-id-err', id);
        function go() { var v = inp.value.trim(); var p = nameProblem(v); if (p) { err.textContent = p; SFX.thud(); return; } setName(v); SFX.stamp(); draw(); }
        $('.fs-id-go', id).addEventListener('click', go);
        inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') go(); });
        return;
      }
      id.innerHTML = '<div class="fs-id-h">FIELD STATION ID</div><div class="fs-id-row"><div class="fs-id-ph">' + r.icon + '</div><div><div class="fs-id-n">' + esc(n) + '</div>' +
        '<div class="fs-id-r">' + esc(r.t) + '</div><div class="fs-id-c">Case ' + esc(D.case ? D.case.num : '') + ' · ' + cluesFound().length + '/' + (D.case ? D.case.clues.length : 0) + ' clues</div></div></div>';
      var hd = $('.fs-hd-rank'); if (hd) hd.innerHTML = r.icon + ' <span>' + esc(r.t) + '</span>';
    }
    var last = rank().t;
    document.addEventListener('fs:progress', function () { var r = rank(); draw(); if (r.t !== last) { last = r.t; toast(r.icon, 'New rank: ' + r.t + '!', D.rankLine || 'Keep going, scientist.'); } });
    draw();
  }
  function toast(icon, title, text) { pushToast(icon, title, text, 4600); }

  /* ---------- marsh sounds (generated, off by default, never on load) ---------- */
  function buildAmbient() {
    var tools = $('.fs-hd-tools'); if (!tools) return;
    var b = el('button', 'fs-pill', esc((D.ambient && D.ambient.icon) || '🦗') + ' <span class="fs-nb-l">' + esc((D.ambient && D.ambient.label) || 'Marsh sounds') + '</span>'); b.type = 'button';
    tools.appendChild(b);
    var on = false, timers = [];
    function chirp(t) { var c = ac(); if (!c) return; for (var k = 0; k < 3; k++) tone(4400 + Math.random() * 300, t + k * 0.045, 0.03, 'sine', 0.012); }
    function croak() { var c = ac(); if (!c) return; var o = c.createOscillator(), f = c.createBiquadFilter(), g = c.createGain();
      o.type = 'sawtooth'; o.frequency.setValueAtTime(120, c.currentTime); o.frequency.linearRampToValueAtTime(90, c.currentTime + 0.25);
      f.type = 'lowpass'; f.frequency.value = 500; g.gain.setValueAtTime(0.0001, c.currentTime); g.gain.exponentialRampToValueAtTime(0.03, c.currentTime + 0.04); g.gain.exponentialRampToValueAtTime(0.0001, c.currentTime + 0.3);
      o.connect(f); f.connect(g); g.connect(c.destination); o.start(); o.stop(c.currentTime + 0.35); }
    b.addEventListener('click', function () {
      on = !on; b.setAttribute('aria-expanded', on ? 'true' : 'false');
      timers.forEach(clearInterval); timers = [];
      if (on) { timers.push(setInterval(function () { chirp(0); }, 650)); timers.push(setInterval(function () { if (Math.random() < 0.5) croak(); }, 2300)); }
    });
  }


  /* v14: drawn icons for the floating tools (emoji vary by device and read as clip art) */
  var FAB_ICON = {
    hl: '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M5 27h14" stroke="#FFE14D" stroke-width="4.5" stroke-linecap="round" opacity=".95"/><g transform="rotate(40 18 14)"><rect x="14" y="2.5" width="8" height="15" rx="2" fill="currentColor"/><path d="M14 17.5h8l-1.5 4h-5z" fill="currentColor"/><path d="M15.5 21.5h5l-1 3.2h-3z" fill="#FFE14D"/><rect x="15.6" y="5" width="2" height="9" rx="1" fill="#fff" opacity=".35"/></g></svg>',
    sk: '<svg viewBox="0 0 32 32" aria-hidden="true"><g transform="rotate(45 16 16)"><rect x="12.5" y="2" width="7" height="5" rx="1.4" fill="#FF9DB3"/><rect x="12.5" y="6.6" width="7" height="2.2" fill="#E9E4F5"/><rect x="12.5" y="8.8" width="7" height="14" fill="currentColor"/><rect x="14.6" y="8.8" width="1.6" height="14" fill="#fff" opacity=".3"/><path d="M12.5 22.8h7L16 30z" fill="#F6D7A7"/><path d="M14.9 27.2h2.2L16 30z" fill="#3B2A5A"/></g></svg>',
    cam: '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M11.5 7.5h9l1.8 3H27a2.5 2.5 0 0 1 2.5 2.5v11A2.5 2.5 0 0 1 27 26.5H5A2.5 2.5 0 0 1 2.5 24V13A2.5 2.5 0 0 1 5 10.5h4.7z" fill="currentColor"/><circle cx="16" cy="18" r="6" fill="#0E1C42"/><circle cx="16" cy="18" r="4.2" fill="#5B8FD6"/><circle cx="14.6" cy="16.6" r="1.4" fill="#fff" opacity=".8"/><circle cx="25.5" cy="14" r="1.3" fill="#F5B83D"/></svg>'
  };
  /* ---------- field camera: drag a box, snap it, caption it ---------- */
  function photos() { try { return JSON.parse(store('photos') || '[]'); } catch (e) { return []; } }
  var MEMPHOTOS = null;
  function savePhotos(a) { MEMPHOTOS = a; try { store('photos', JSON.stringify(a)); return true; } catch (e) { return false; } }
  function allPhotos() { return MEMPHOTOS || photos(); }
  function ensureH2C(cb) {
    if (window.html2canvas) return cb();
    var s = document.createElement('script'); s.src = (D.paths && D.paths.h2c) || 'assets/sparkle/vendor/html2canvas.min.js';
    s.onload = cb; s.onerror = function () { toast('📷', 'Camera can’t load', 'Ask your teacher. The camera file is missing.'); }; document.head.appendChild(s);
  }
  function buildCamera() {
    var CAM = D.camera || {}; var MAX = CAM.max || 8;
    var fab = fsOnly(el('div', 'fs-fab'));
    fab.innerHTML = '<button type="button" class="fs-fab-btn fs-fab-snap" title="Field camera: drag a box to snap what you see">' + FAB_ICON.cam + '<span>Snap</span><b class="fs-fab-n"></b></button>' +
      '<button type="button" class="fs-fab-roll" title="My camera roll">🖼️ <b>0</b></button>';
    document.body.appendChild(fab);
    var rollBtn = $('.fs-fab-roll', fab);
    function count() { $('b', rollBtn).textContent = allPhotos().length; rollBtn.classList.toggle('has', allPhotos().length > 0); }
    count();
    $('.fs-fab-snap', fab).addEventListener('click', startSnap);
    rollBtn.addEventListener('click', openRoll);
    /* v13: Photo Hunt card at the top so students know the missions exist */
    var hunt = null, MS = CAM.missions || [];
    if (MS.length) {
      hunt = fsOnly(el('div', 'fs-hunt',
        '<div class="fs-hunt-l"><div class="fs-hunt-cam">📷<i></i></div></div>' +
        '<div class="fs-hunt-r"><div class="fs-game-k">Bonus · Photo Hunt <span class="fs-hunt-opt">optional</span></div>' +
        '<div class="fs-hunt-t">' + esc(CAM.huntTitle || 'Your field camera is ready. Can you complete all ' + MS.length + ' photo missions?') + '</div>' +
        '<ol class="fs-hunt-list"></ol>' +
        '<div class="fs-hunt-ctl"><button type="button" class="fs-btn fs-hunt-try">📷 Try the camera</button><span class="fs-hunt-how">' + esc(CAM.huntHow || 'Tap 📷 Snap at the bottom right, then drag a box around what you want. Your photos print in your field journal.') + '</span></div></div>'));
      var after = $('.fs-casecard'); var wtab = $('#tab-welcome .act-body') || $('#tab-welcome');
      if (after && after.parentNode) after.parentNode.insertBefore(hunt, after.nextSibling); else if (wtab) wtab.insertBefore(hunt, wtab.firstChild);
      $('.fs-hunt-try', hunt).addEventListener('click', startSnap);
      if (!allPhotos().length) fab.classList.add('fs-fab-hint');
    }
    function huntUpd() {
      if (!hunt) return; var a = allPhotos(), n = 0;
      $('.fs-hunt-list', hunt).innerHTML = MS.map(function (ms, i) { var d = a.some(function (p) { return p.mission === i; }); if (d) n++; return '<li class="' + (d ? 'on' : '') + '"><span>' + (d ? '✅' : '🎯') + '</span>' + esc(ms) + '</li>'; }).join('');
      hunt.classList.toggle('done', n === MS.length);
      var sn = $('.fs-fab-snap .fs-fab-n', fab); if (sn) { sn.textContent = n + '/' + MS.length; sn.style.display = n ? 'flex' : 'none'; }
      if (a.length) fab.classList.remove('fs-fab-hint');
    }
    huntUpd();
    var ov = null;
    function startSnap() {
      if (allPhotos().length >= MAX) { toast('🖼️', 'Camera roll is full', 'Delete a photo in your camera roll to make room (' + MAX + ' max).'); return; }
      /* camera mode is unmistakable: a viewfinder frame, a big banner, a centered hint, and the Snap button lit up */
      ov = fsOnly(el('div', 'fs-snapov', '<div class="fs-vf"><i class="tl"></i><i class="tr"></i><i class="bl"></i><i class="br"></i></div>' +
        '<div class="fs-snap-tip"><span class="fs-snap-rec">● CAMERA ON</span><b>Drag a box around what you want to snap.</b><button type="button">✕ Cancel</button></div>' +
        '<div class="fs-snap-mid"><span>📷</span>Press, hold and drag to draw your box</div><div class="fs-snap-box"></div>'));
      document.body.appendChild(ov); SFX.blip();
      var sb = $('.fs-fab-snap'); if (sb) sb.classList.add('on');
      var box = $('.fs-snap-box', ov), st = null;
      $('.fs-snap-tip button', ov).addEventListener('click', function (e) { e.stopPropagation(); end(); });
      document.addEventListener('keydown', esc1);
      function esc1(e) { if (e.key === 'Escape') end(); }
      function end() { if (ov) { ov.remove(); ov = null; } document.removeEventListener('keydown', esc1); var b = $('.fs-fab-snap'); if (b) b.classList.remove('on'); }
      ov.addEventListener('pointerdown', function (e) { if (e.target.closest('.fs-snap-tip')) return; st = { x: e.clientX, y: e.clientY }; ov.classList.add('drag'); ov.setPointerCapture && ov.setPointerCapture(e.pointerId); box.style.display = 'block'; draw(e); });
      ov.addEventListener('pointermove', function (e) { if (st) draw(e); });
      ov.addEventListener('pointerup', function (e) {
        if (!st) return; var r = rect(e); st = null;
        if (r.w < 24 || r.h < 24) { box.style.display = 'none'; ov.classList.remove('drag'); return; }
        end(); snap(r);
      });
      function rect(e) { return { x: Math.min(st.x, e.clientX), y: Math.min(st.y, e.clientY), w: Math.abs(e.clientX - st.x), h: Math.abs(e.clientY - st.y) }; }
      function draw(e) { var r = rect(e); box.style.left = r.x + 'px'; box.style.top = r.y + 'px'; box.style.width = r.w + 'px'; box.style.height = r.h + 'px'; }
    }
    function snap(r) {
      var flash = fsOnly(el('div', 'fs-flash')); document.body.appendChild(flash);
      var dev = fsOnly(el('div', 'fs-snap-dev', '<span>📷</span> Developing your photo…')); document.body.appendChild(dev);
      window.__fsDev = dev;
      SFX.snap(); setTimeout(function () { flash.remove(); }, 450);
      ensureH2C(function () {
        // render the page column, then crop to the box (more reliable than x/y offsets with sticky bars and scroll)
        var wrapEl = document.querySelector('.page-wrap') || document.body;
        // a reference element under the box, to correct any layout drift in html2canvas's copy of the page
        var ref = document.elementFromPoint(r.x + r.w / 2, r.y + r.h / 2) || wrapEl, lr = ref.getBoundingClientRect();
        // render only the smallest block around the box: a full long page blows past the browser's canvas size limit
        var root = ref;
        while (root && root !== wrapEl && root.parentElement) {
          var q = root.getBoundingClientRect();
          if (q.left <= r.x + 1 && q.top <= r.y + 1 && q.right >= r.x + r.w - 1 && q.bottom >= r.y + r.h - 1 && root.tagName !== 'SPAN' && root.tagName !== 'B') break;
          root = root.parentElement;
        }
        if (!root || !wrapEl.contains(root)) root = wrapEl;
        var rr = root.getBoundingClientRect();
        // keep the canvas well under every browser's limit (iPad Safari is about 16 million pixels)
        var sc = Math.min(2, window.devicePixelRatio || 1, Math.sqrt(12e6 / Math.max(1, rr.width * rr.height)), 8000 / Math.max(1, rr.height), 8000 / Math.max(1, rr.width));
        ref.setAttribute('data-fs-ref', '1'); root.setAttribute('data-fs-root', '1');
        var drift = { x: 0, y: 0 };
        window.html2canvas(root, {
          onclone: function (doc) {
            var cr = doc.querySelector('[data-fs-ref]'), cw = doc.querySelector('[data-fs-root]') || doc.body;
            if (cr && cw) { var a = cr.getBoundingClientRect(), b = cw.getBoundingClientRect();
              drift.x = (a.left - b.left) - (lr.left - rr.left); drift.y = (a.top - b.top) - (lr.top - rr.top); }
            ref.removeAttribute('data-fs-ref'); root.removeAttribute('data-fs-root');
          },
          scale: sc, useCORS: true, logging: false, imageTimeout: 3000, backgroundColor: '#FAF7F3',
          windowWidth: document.documentElement.clientWidth, windowHeight: window.innerHeight, scrollX: 0, scrollY: -window.scrollY,
          ignoreElements: function (n) { return n.classList && (n.classList.contains('fs-fab') || n.classList.contains('fs-mock') || n.classList.contains('fs-toasts') || n.classList.contains('fs-flash') || n.classList.contains('fs-snap-dev') || n.classList.contains('fs-modal') || n.classList.contains('fs-snapov')); }
        }).then(function (full) {
          window.FS_DRIFT = drift; var cx = Math.max(0, r.x - rr.left + drift.x), cy = Math.max(0, r.y - rr.top + drift.y);
          var cv = document.createElement('canvas'); cv.width = Math.round(r.w * sc); cv.height = Math.round(r.h * sc);
          cv.getContext('2d').drawImage(full, cx * sc, cy * sc, r.w * sc, r.h * sc, 0, 0, cv.width, cv.height);
          return cv;
        }).then(function (cv) {
          var maxW = 760, s = Math.min(1, maxW / cv.width), out = document.createElement('canvas');
          out.width = Math.round(cv.width * s); out.height = Math.round(cv.height * s);
          out.getContext('2d').drawImage(cv, 0, 0, out.width, out.height);
          caption(out.toDataURL('image/jpeg', 0.72));
        }).catch(function (e) { ref.removeAttribute('data-fs-ref'); root.removeAttribute('data-fs-root'); FAILED.push('camera: ' + (e && e.message)); if (window.__fsDev) { window.__fsDev.remove(); window.__fsDev = null; } window.FS_SNAP_ERR = String(e && (e.stack || e.message) || e); toast('📷', 'That snap didn’t work', 'Scroll a little and try again.'); });
      });
    }
    function caption(src) {
      if (window.__fsDev) { window.__fsDev.remove(); window.__fsDev = null; }
      var m = modal();
      var tabLabel = (function () { var b = $('.tab-btn.active'); return b ? b.textContent.replace('✓', '').trim() : ''; })();
      var missions = (CAM.missions || []).map(function (ms, i) { var done = allPhotos().some(function (p) { return p.mission === i; }); return '<button type="button" class="fs-opt' + (done ? ' done' : '') + '" data-m="' + i + '">' + (done ? '✓ ' : '') + esc(ms) + '</button>'; }).join('');
      m.innerHTML = '<div class="fs-nb fs-kraft"><button class="fs-x" type="button" aria-label="Close">✕</button><h3>📷 New field photo</h3>' +
        '<div class="fs-pola big"><img alt="" src="' + src + '"><input class="fs-cap" maxlength="80" placeholder="What does this show? (a few words)"></div>' +
        (missions ? '<div class="fs-plan-row"><b>Is it for a photo mission? (optional)</b>' + missions + '</div>' : '') +
        '<div style="display:flex;gap:8px;margin-top:12px"><button type="button" class="fs-btn fs-save">Add to my camera roll</button><button type="button" class="fs-btn alt fs-toss">Toss it</button></div></div>';
      var pick = null;
      $$('.fs-opt', m).forEach(function (b) { b.addEventListener('click', function () { $$('.fs-opt', m).forEach(function (x) { if (x !== b) x.classList.remove('on'); }); b.classList.toggle('on'); pick = b.classList.contains('on') ? +b.dataset.m : null; SFX.blip(); }); });
      function close() { m.classList.remove('open'); }
      $('.fs-x', m).addEventListener('click', close); $('.fs-toss', m).addEventListener('click', close);
      $('.fs-save', m).addEventListener('click', function () {
        var a = allPhotos().slice(); a.push({ src: src, cap: $('.fs-cap', m).value.trim(), tab: tabLabel, mission: pick, t: Date.now() });
        var ok = savePhotos(a); close(); count(); huntUpd(); SFX.chime();
        rollBtn.classList.remove('pop'); void rollBtn.offsetWidth; rollBtn.classList.add('pop');
        var done = (CAM.missions || []).filter(function (x, i) { return a.some(function (p) { return p.mission === i; }); }).length;
        if (pick !== null) toast('🎯', 'Photo mission done! (' + done + ' of ' + CAM.missions.length + ')', CAM.missions[pick]);
        else toast('🖼️', 'Saved to your camera roll', ok ? 'It will print at the end of your field journal.' : 'Saved for now. Download your journal before you leave this page.');
      });
      setTimeout(function () { var c = $('.fs-cap', m); c && c.focus(); }, 50);
    }
    function openRoll() {
      var m = modal(), a = allPhotos(), CAMm = CAM.missions || [];
      m.innerHTML = '<div class="fs-nb fs-kraft"><button class="fs-x" type="button" aria-label="Close">✕</button><h3>🖼️ My camera roll</h3>' +
        '<div class="fs-nb-sub">' + a.length + ' of ' + MAX + ' photos · they print at the end of your field journal</div>' +
        (CAMm.length ? '<div class="fs-missions"><b>Photo missions</b>' + CAMm.map(function (ms, i) { var d = a.some(function (p) { return p.mission === i; }); return '<div class="' + (d ? 'on' : '') + '">' + (d ? '✅' : '⬜') + ' ' + esc(ms) + '</div>'; }).join('') + '</div>' : '') +
        '<div class="fs-roll">' + (a.length ? a.map(function (p, i) { return '<div class="fs-pola"><img alt="" src="' + p.src + '"><div class="fs-pola-c">' + esc(p.cap || '(no caption)') + '</div><button type="button" class="fs-del" data-i="' + i + '" title="Delete">🗑</button></div>'; }).join('') : '<p class="fs-empty-roll">No photos yet. Tap 📷 Snap, then drag a box around anything on the page.</p>') + '</div>' +
        '<div style="margin-top:12px"><button type="button" class="fs-btn fs-jr">📓 Download my field journal</button></div></div>';
      $('.fs-x', m).addEventListener('click', function () { m.classList.remove('open'); });
      $$('.fs-del', m).forEach(function (b) { b.addEventListener('click', function () { var x = allPhotos().slice(); x.splice(+b.dataset.i, 1); savePhotos(x); count(); huntUpd(); openRoll(); }); });
      $('.fs-jr', m).addEventListener('click', downloadJournal);
    }
  }
  function modal() {
    var m = $('#fsModal2');
    if (!m) { m = fsOnly(el('div', 'fs-modal')); m.id = 'fsModal2'; m.addEventListener('click', function (e) { if (e.target === m) m.classList.remove('open'); }); document.body.appendChild(m); }
    m.classList.add('open'); return m;
  }


  /* ---------- v13: answer right on the page (gathered at the end) ---------- */
  function findEl(f) {
    var list = $$(f.sel || 'p');
    for (var i = 0; i < list.length; i++) if (!f.text || list[i].textContent.indexOf(f.text) > -1) return list[i];
    return null;
  }
  function refreshG() { try { if (window.refreshGathered) window.refreshGathered(); } catch (e) {} }
  // a gathered field: a real .response-textarea so the page's Gathered Answers and the journal both pick it up
  function gField(id, label, q, visible) {
    var ta = el('textarea', 'response-textarea fs-gfield' + (visible ? '' : ' fs-gmirror')); ta.id = id;
    ta.setAttribute('data-label', label); if (q) ta.dataset.q = q;
    if (visible) { ta.placeholder = visible === true ? 'Type your answer here…' : visible; ta.rows = 3; }
    else { ta.tabIndex = -1; ta.setAttribute('aria-hidden', 'true'); }
    var v = store('ans.' + id); if (v) ta.value = v;
    ta.addEventListener('input', function () { store('ans.' + id, ta.value); refreshG(); });
    return ta;
  }
  function setG(ta, v) { ta.value = v; store('ans.' + ta.id, v); refreshG(); ta.dispatchEvent(new Event('input')); }
  function swapText(node, sw) {
    if (!node || !sw) return;
    (Array.isArray(sw[0]) ? sw : [sw]).forEach(function (x) {
      // prefer a single text node so nothing else in the element is rebuilt
      var w = document.createTreeWalker(node, NodeFilter.SHOW_TEXT), t;
      while ((t = w.nextNode())) if (t.nodeValue.indexOf(x[0]) > -1 && x[1].indexOf('<') < 0) { t.nodeValue = t.nodeValue.replace(x[0], x[1]); return; }
      if (!$('.fs-only', node) && node.innerHTML.indexOf(x[0]) > -1) node.innerHTML = node.innerHTML.replace(x[0], x[1]);
    });
  }
  var INPUTS = {
    swap: function () {},
    hide: function (I, at) { at.classList.add('fs-hide-on'); },
    // numbered list (warm-up)
    list: function (I, at) {
      var box = fsOnly(el('div', 'fs-in fs-in-list')), mir = gField(I.id, I.label, I.q, false);
      var saved = []; try { saved = JSON.parse(store('ans.' + I.id + '.rows') || '[]'); } catch (e) {}
      if (I.title) box.appendChild(el('div', 'fs-in-k', esc(I.title)));
      var rows = el('ol', 'fs-in-rows'); box.appendChild(rows);
      var add = el('button', 'fs-hintbtn fs-in-add', esc(I.addLabel || '+ Add a step')); add.type = 'button'; box.appendChild(add);
      var cnt = el('span', 'fs-count'); box.appendChild(cnt); box.appendChild(mir);
      function sync() {
        var vals = $$('input', rows).map(function (x) { return x.value.trim(); });
        store('ans.' + I.id + '.rows', JSON.stringify(vals));
        var f = vals.filter(Boolean); setG(mir, f.map(function (v, i) { return (i + 1) + '. ' + v; }).join('\n'));
        cnt.textContent = '📝 ' + Math.min(f.length, I.min || 3) + ' of ' + (I.min || 3) + ' ' + (I.unit || 'steps') + (f.length >= (I.min || 3) ? ' ✓' : '');
        cnt.classList.toggle('ok', f.length >= (I.min || 3));
      }
      function row(v, ph) { var li = el('li'); var x = el('input'); x.type = 'text'; x.value = v || ''; x.placeholder = ph || 'Next…'; x.addEventListener('input', sync); li.appendChild(x); rows.appendChild(li); return x; }
      var n = Math.max((I.ph || []).length, saved.length, 3);
      for (var i = 0; i < n; i++) row(saved[i], (I.ph || [])[i]);
      add.addEventListener('click', function () { if ($$('li', rows).length < 8) row('', 'Next…').focus(); SFX.blip(); });
      at.parentNode.insertBefore(box, at.nextSibling); sync();
    },
    // one labelled box per step (stimulus / sense organ / brain / response)
    frame: function (I, at) {
      var box = fsOnly(el('div', 'fs-in fs-in-frame' + (I.compact ? ' compact' : ''))), mir = gField(I.id, I.label, I.q, false);
      var saved = {}; try { saved = JSON.parse(store('ans.' + I.id + '.f') || '{}'); } catch (e) {}
      if (I.title) box.appendChild(el('div', 'fs-in-k', esc(I.title)));
      I.fields.forEach(function (f, i) {
        var r = el('label', 'fs-in-f', '<span class="fs-in-fl">' + (f.icon ? f.icon + ' ' : '') + esc(f.t) + '</span>');
        var x = el(f.long ? 'textarea' : 'input'); if (!f.long) x.type = 'text'; else x.rows = 2;
        x.placeholder = f.ph || ''; x.value = saved[i] || ''; x.dataset.i = i; r.appendChild(x); box.appendChild(r);
        x.addEventListener('input', sync);
      });
      box.appendChild(mir);
      function sync() {
        var o = {}, out = [];
        $$('.fs-in-f input, .fs-in-f textarea', box).forEach(function (x) { o[x.dataset.i] = x.value; if (x.value.trim()) out.push(I.fields[+x.dataset.i].t + ': ' + x.value.trim()); });
        store('ans.' + I.id + '.f', JSON.stringify(o)); setG(mir, out.join('\n'));
      }
      if (I.inside) { var host = $('.question', at) ? $('.question', at).parentNode : at; host.appendChild(box); }
      else at.parentNode.insertBefore(box, at.nextSibling);
    },
    // plain typing box, optionally tucked behind a "Jot my answer" button
    write: function (I, at) {
      var box = fsOnly(el('div', 'fs-in fs-in-write' + (I.tuck ? ' tucked' : ''))), ta = gField(I.id, I.label, I.q, I.ph || true);
      if (I.rows) ta.rows = I.rows;
      if (I.tuck) {
        var b = el('button', 'fs-hintbtn fs-in-jot', '✏️ ' + esc(I.tuck)); b.type = 'button'; box.appendChild(b);
        if (ta.value) box.classList.remove('tucked');
        b.addEventListener('click', function () { box.classList.remove('tucked'); ta.focus(); SFX.blip(); });
      }
      box.appendChild(ta);
      setTimeout(function () { helpFor(I.id); }, 0);
      if (I.inside) { var host = $('.question', at) ? $('.question', at).parentNode : at; host.appendChild(box); }
      else at.parentNode.insertBefore(box, at.nextSibling);
    },
    // tap a choice (with a gentle check)
    pick: function (I, at) {
      var box = fsOnly(el('div', 'fs-in fs-in-pick')), mir = gField(I.id, I.label, I.q, false), miss = el('div', 'fs-miss');
      var row = el('div', 'fs-in-chips'); box.appendChild(row); box.appendChild(miss); box.appendChild(mir);
      I.opts.forEach(function (o) {
        var c = el('button', 'fs-in-chip', (o.icon ? '<span>' + o.icon + '</span>' : '') + esc(o.t)); c.type = 'button'; row.appendChild(c);
        if (mir.value === o.t) c.classList.add('on', 'ok');
        c.addEventListener('click', function () {
          if (o.ok) { $$('.fs-in-chip', row).forEach(function (x) { x.classList.remove('on', 'ok'); }); c.classList.add('on', 'ok'); miss.classList.remove('show'); SFX.chime(); setG(mir, o.t + (I.why ? ' (' + I.why + ')' : '')); }
          else bounce(c, miss, o.miss || I.miss || 'Look again.');
        });
      });
      at.parentNode.insertBefore(box, at.nextSibling);
    },

    // CER frame: Claim / Evidence / Reasoning boxes that feed the page's own answer box
    cer: function (I, at) {
      var orig = document.getElementById(I.target); if (!orig) return;
      orig.classList.add('fs-cer-src');
      var box = fsOnly(el('div', 'fs-in fs-cer'));
      box.innerHTML = '<div class="fs-cer-rem">🔬 <b>Remember CER?</b> ' + esc(I.reminder || '') + '</div>';
      var saved = {}; try { saved = JSON.parse(store('ans.' + I.id + '.f') || '{}'); } catch (e) {}
      I.parts.forEach(function (pt) {
        var r = el('div', 'fs-cer-row', '<div class="fs-cer-h"><span class="fs-cer-l">' + pt.k + '</span><b>' + esc(pt.t) + '</b><span>' + esc(pt.ask) + '</span></div>');
        var x = el('textarea'); x.rows = pt.rows || 2; x.placeholder = pt.ph || ''; x.dataset.k = pt.k; x.value = saved[pt.k] || ''; r.appendChild(x); box.appendChild(r);
        x.addEventListener('input', sync);
      });
      function sync() {
        var o = {}, out = [];
        $$('.fs-cer-row textarea', box).forEach(function (x) { o[x.dataset.k] = x.value; var pt = I.parts.filter(function (p) { return p.k === x.dataset.k; })[0]; if (x.value.trim()) out.push(pt.t + ': ' + x.value.trim()); });
        store('ans.' + I.id + '.f', JSON.stringify(o));
        orig.value = out.join('\n'); orig.dispatchEvent(new Event('input', { bubbles: true }));
      }
      orig.parentNode.insertBefore(box, orig);
      // planner picks drop straight into the boxes
      var plan = $('.fs-plan', orig.parentNode);
      if (plan) $$('.fs-plan-row', plan).forEach(function (row, ri) {
        $$('.fs-opt', row).forEach(function (b) { b.addEventListener('click', function () {
          var k = ri === 0 ? 'C' : 'E', x = $('.fs-cer-row textarea[data-k="' + k + '"]', box); if (!x) return;
          var t = b.textContent.trim();
          if (k === 'C') { if (!x.value.trim() || /^I (dis)?agree\./.test(x.value)) x.value = x.value.replace(/^I (dis)?agree\.\s*/, '').replace(/^/, t + '. '); }
          else if (b.classList.contains('on') && x.value.indexOf(t) < 0) x.value = (x.value.trim() ? x.value.trim() + ' ' : '') + t;
          sync(); x.classList.remove('fs-flashin'); void x.offsetWidth; x.classList.add('fs-flashin');
        }); });
      });
      if (plan) box.parentNode.insertBefore(box, plan.nextSibling);
      sync();
    },
    // recap: bring what students need from another tab to this spot (photos + one line each)
    recap: function (I, at) {
      var box = fsOnly(el('div', 'fs-recap'));
      box.innerHTML = (I.title ? '<div class="fs-in-k">' + esc(I.title) + '</div>' : '') + '<div class="fs-recap-row">' + I.items.map(function (it) {
        return '<figure>' + (it.img ? '<img alt="' + esc(it.name) + '" src="' + it.img + '">' : '<div class="fs-recap-ic">' + (it.icon || '') + '</div>') + '<figcaption><b>' + esc(it.name) + '</b>' + esc(it.t) + '</figcaption></figure>';
      }).join('') + '</div>';
      var host = at.closest('.pq') || at; host.parentNode.insertBefore(box, host);
    },
    // a tiny line graph students build by tapping (Part C, 10.02): one dot per column, snapped to a step, then a sentence
    graph: function (I, at) {
      var box = fsOnly(el('div', 'fs-in fs-in-graph')), mir = gField(I.id, I.label, I.q, false);
      var saved = {}; try { saved = JSON.parse(store('ans.' + I.id + '.g') || '{}'); } catch (e) {}
      var W = 420, H = 260, L = 58, R = 20, Tp = 16, B = 34, cols = I.points.length;
      function X(i) { return L + (i + 0.5) * (W - L - R) / cols; } function Y(v) { return Tp + (1 - v / I.ymax) * (H - Tp - B); }
      var grid = ''; for (var v = 0; v <= I.ymax; v += I.ystep) grid += '<line x1="' + L + '" x2="' + (W - R) + '" y1="' + Y(v) + '" y2="' + Y(v) + '" class="gl"/><text x="' + (L - 6) + '" y="' + (Y(v) + 4) + '" text-anchor="end">' + v.toLocaleString() + '</text>';
      var colw = (W - L - R) / cols;
      box.innerHTML = (I.title ? '<div class="fs-in-k">' + esc(I.title) + '</div>' : '') + '<p class="fs-gr-how">' + esc(I.how) + '</p>' +
        '<svg class="fs-gr-svg" viewBox="0 0 ' + W + ' ' + H + '"><g class="ax">' + grid + '</g><text class="yl" transform="translate(12 ' + (H / 2) + ') rotate(-90)" text-anchor="middle">' + esc(I.yLabel) + '</text>' +
        I.points.map(function (p, i) { return '<rect class="col" data-i="' + i + '" x="' + (L + i * colw + 4) + '" y="' + Tp + '" width="' + (colw - 8) + '" height="' + (H - Tp - B) + '"/><text x="' + X(i) + '" y="' + (H - 12) + '" text-anchor="middle" class="xl">' + esc(p.x) + '</text>'; }).join('') +
        '<polyline class="ln" points=""/>' + I.points.map(function (p, i) { return '<g class="pt" data-i="' + i + '" style="display:none"><circle r="7"/><text y="-12" text-anchor="middle"></text></g>'; }).join('') + '</svg>' +
        '<div class="fs-gr-chips">' + I.points.map(function (p, i) { return '<span class="fs-chip" data-i="' + i + '">' + esc(p.x) + ' dot</span>'; }).join('') + '</div><div class="fs-miss"></div>';
      var ta = gField(I.id + '-s', I.sLabel || I.label + ' (trend)', I.sQ || '', I.ph || 'One sentence about the trend…'); ta.classList.remove('response-textarea'); ta.removeAttribute('data-label');
      box.appendChild(ta); box.appendChild(mir);
      var svg = $('svg', box), miss = $('.fs-miss', box);
      function sync() {
        var pts = [];
        I.points.forEach(function (p, i) { var g = $('.pt[data-i="' + i + '"]', svg), v = saved[i];
          if (v == null) { g.style.display = 'none'; return; }
          g.style.display = ''; g.setAttribute('transform', 'translate(' + X(i) + ',' + Y(v) + ')'); $('text', g).textContent = v.toLocaleString(); pts.push(X(i) + ',' + Y(v));
          var ok = v >= p.lo && v <= p.hi, ch = $('.fs-chip[data-i="' + i + '"]', box); ch.classList.toggle('on', ok); });
        $('.ln', svg).setAttribute('points', pts.length === cols ? pts.join(' ') : '');
        store('ans.' + I.id + '.g', JSON.stringify(saved));
        setG(mir, I.points.map(function (p, i) { return p.x + ' dot: ' + (saved[i] == null ? '___' : saved[i].toLocaleString()); }).join('\n') + (ta.value.trim() ? '\nTrend: ' + ta.value.trim() : ''));
      }
      function setAt(e, i) {
        var r = svg.getBoundingClientRect(), y = (e.clientY - r.top) * (H / r.height), v = (1 - (y - Tp) / (H - Tp - B)) * I.ymax;
        v = Math.max(0, Math.min(I.ymax, Math.round(v / I.step) * I.step)); saved[i] = v; sync();
        var p = I.points[i]; if (v < p.lo || v > p.hi) { miss.innerHTML = '🔎 ' + esc(p.hint); miss.classList.add('show'); } else { miss.classList.remove('show'); SFX.blip(); }
      }
      $$('.col', svg).forEach(function (c) { var dn = false, i = +c.dataset.i;
        c.addEventListener('pointerdown', function (e) { dn = true; c.setPointerCapture && c.setPointerCapture(e.pointerId); setAt(e, i); });
        c.addEventListener('pointermove', function (e) { if (dn) setAt(e, i); });
        c.addEventListener('pointerup', function () { dn = false; }); });
      ta.addEventListener('input', sync);
      at.parentNode.insertBefore(box, at.nextSibling); sync();
    },
    // live recap of something the student wrote on another tab
    echo: function (I, at) {
      var src = document.getElementById(I.from); var box = fsOnly(el('div', 'fs-echo'));
      function upd() { var v = src ? src.value.trim() : ''; box.innerHTML = '<div class="fs-in-k">' + esc(I.title) + '</div>' + (I.scene ? '<p>' + esc(I.scene) + '</p>' : '') + (v ? '<div class="fs-echo-mine"><b>' + esc(I.mine || 'What you wrote:') + '</b><br>' + esc(v).replace(/\n/g, '<br>') + '</div>' : ''); }
      upd(); if (src) { src.addEventListener('input', upd); document.addEventListener('fs:tab', upd); }
      var host = $('.question', at) ? $('.question', at) : at; host.parentNode.insertBefore(box, host.nextSibling);
    },
    // word bank: drag or tap a word into each blank
    bank: function (I) {
      var items = $$(I.sel).filter(function (x) { return x.textContent.indexOf(I.blank || '___') > -1; }); if (!items.length) return;
      var first = items[0].closest('.pq') || items[0];
      var g = fsOnly(el('div', 'fs-in fs-in-bank')), mir = gField(I.id, I.label, I.q, false), miss = el('div', 'fs-miss'), win = el('div', 'fs-win');
      var deck = el('div', 'fs-in-chips fs-bankdeck', '<span class="fs-in-bk">' + esc(I.bankLabel || 'Word bank') + '</span>');
      first.parentNode.insertBefore(g, first); g.appendChild(deck);
      var slots = items.map(function (t, i) {
        var slot = fsOnly(el('span', 'fs-blank', '<i>' + esc(I.hole || 'drop a word') + '</i>')); slot.dataset.i = i;
        t.innerHTML = t.innerHTML.replace(/_{3,}/, '<span class="fs-blank-hold"></span>');
        var hold = $('.fs-blank-hold', t); hold.appendChild(slot); hold.insertAdjacentHTML('beforeend', '<span class="fs-blank-orig">___________</span>');
        return slot;
      });
      var after = items[items.length - 1].closest('.pq') || items[items.length - 1]; after.parentNode.insertBefore(miss, after.nextSibling); miss.parentNode.insertBefore(win, miss.nextSibling); win.parentNode.insertBefore(mir, win.nextSibling);
      var done = {}; try { done = JSON.parse(store('ans.' + I.id + '.b') || '{}'); } catch (e) {}
      function sync() {
        store('ans.' + I.id + '.b', JSON.stringify(done));
        setG(mir, items.map(function (t, i) { return (i + 1) + '. ' + (done[i] || '___'); }).join('\n'));
        if (Object.keys(done).length === items.length) { win.innerHTML = esc(I.win || 'All four blanks filled!'); win.classList.add('show'); }
      }
      I.words.forEach(function (w) {
        var c = el('div', 'fs-card fs-bankcard', esc(w)); c.dataset.w = w; deck.appendChild(c);
        dragDrop(c, function () { return slots.filter(function (s) { return !s.classList.contains('full'); }); }, drop);
      });
      function place(slot, w) { slot.classList.add('full'); slot.innerHTML = esc(w); var c = $('.fs-bankcard[data-w="' + w + '"]', deck); if (c) { c.classList.add('placed'); c.classList.remove('sel'); } }
      function drop(card, slot) {
        var i = +slot.dataset.i, w = card.dataset.w;
        if (slot.classList.contains('full')) return;
        if (I.answers[i] !== w) { bounce(card, miss, (I.miss && I.miss[w]) || 'Not that one. Read the clue again.'); return; }
        place(slot, w); done[i] = w; SFX.chime(); miss.classList.remove('show'); sync();
      }
      tapTargets(g.parentNode, slots, drop);
      Object.keys(done).forEach(function (i) { if (slots[i]) place(slots[i], done[i]); });
      sync();
    }
  };
  function buildInputs() {
    (D.inputs || []).forEach(function (I) {
      guard('input:' + I.id, function () {
        if (I.type === 'relabel') { Object.keys(I.map).forEach(function (id) { var t = document.getElementById(id); if (t) t.setAttribute('data-label', I.map[id]); }); return; }
        var at = I.type === 'bank' ? null : findEl(I.find || {});
        if (I.type !== 'bank' && !at) { console.warn('fs input: no anchor for', I.id); return; }
        if (I.swap) swapText(at || findEl(I.swapAt || {}), I.swap);
        if (I.swapAt && at) swapText(findEl(I.swapAt), I.swap2);
        INPUTS[I.type] && INPUTS[I.type](I, at);
      });
    });
    refreshG();
  }
  /* ---------- field journal: answers + case + photos, printable ---------- */
  function questionFor(ta) {
    if (ta.dataset.q) return ta.dataset.q;
    var p = ta.previousElementSibling;
    while (p && (p.classList.contains('fs-only') || p.tagName === 'TEXTAREA')) p = p.previousElementSibling;
    if (p && p.classList.contains('pq')) { var t = $('.pq-text', p); return (t || p).textContent.trim(); }
    var box = ta.closest('div[style]'); if (box) { var ps = $$(':scope > p', box).map(function (x) { return x.textContent.trim(); }); if (ps.length) return ps.join(' '); }
    return ta.getAttribute('data-label') || 'Answer';
  }
  function downloadJournal() {
    var n = getName() || '(add your name)', C = D.case || {}, a = allPhotos();
    var title = ($('.header-title') ? $('.header-title').childNodes[0].textContent : document.title).trim();
    var bq = $('.intro-2col .question'); bq = bq ? bq.textContent.trim() : '';
    var found = cluesFound();
    var answers = $$('textarea.response-textarea').map(function (ta) { return '<div class="q"><b>' + esc(questionFor(ta)) + '</b><p>' + (ta.value.trim() ? esc(ta.value.trim()).replace(/\n/g, '<br>') : '<i>(not answered yet)</i>') + '</p></div>'; }).join('');
    var h = '<!doctype html><html><head><meta charset="utf-8"><title>Field journal · ' + esc(D.label || D.lesson) + ' · ' + esc(n) + '</title><style>' +
      'body{font-family:Nunito,Arial,sans-serif;color:#2B1D12;max-width:760px;margin:24px auto;padding:0 18px;line-height:1.5}' +
      'h1{font-size:24px;margin:0;color:#0E1C42}h2{font-size:17px;color:#0E1C42;border-bottom:2px solid #C9B489;padding-bottom:3px;margin:22px 0 8px}' +
      '.k{font-size:11px;letter-spacing:1.2px;text-transform:uppercase;color:#7A5F2C;font-weight:800}.bq{background:#F4EBD6;border-left:4px solid #F5B83D;padding:8px 12px;border-radius:6px;font-weight:700}' +
      '.q{margin:10px 0;page-break-inside:avoid}.q b{display:block;font-size:14px}.q p{margin:4px 0 0;border:1px solid #DDD;border-radius:6px;padding:6px 10px}' +
      'ul{margin:4px 0;padding-left:20px}.ph{display:grid;grid-template-columns:1fr 1fr;gap:14px}.pol{border:1px solid #CCC;padding:8px 8px 6px;border-radius:4px;page-break-inside:avoid;box-shadow:0 2px 6px rgba(0,0,0,.12)}' +
      '.sk{margin:8px 0 14px;page-break-inside:avoid}.sk b{display:block;margin-bottom:4px}.sk img{width:100%;border:1px solid #CCC;border-radius:6px}.pol img{width:100%;display:block}.pol div{font-size:13px;margin-top:5px}.pol small{color:#7A5F2C}@media print{button{display:none}}</style></head><body>' +
      '<div class="k">Optima Academy Online · 4th Grade Science · Field journal</div><h1>' + esc(D.label || D.lesson) + ' · ' + esc(title) + '</h1>' +
      '<p><b>Scientist:</b> ' + esc(n) + ' &nbsp; <b>Rank:</b> ' + esc(rank().t) + ' &nbsp; <b>Date:</b> ' + new Date().toLocaleDateString() + '</p>' +
      (bq ? '<div class="bq">Big Question: ' + esc(bq) + '</div>' : '') +
      (C.title ? '<h2>🗂 Case ' + esc(C.num) + ': ' + esc(C.title) + (store('solved') ? ' (cracked)' : '') + '</h2><p>' + esc(C.question) + '</p><ul>' +
        (found.length ? found.map(function (c) { return '<li>' + c.icon + ' ' + esc(c.t) + '</li>'; }).join('') : '<li><i>No clues found yet.</i></li>') + '</ul>' : '') +
      (store('specimen') && D.specimen ? '<p>' + D.specimen.icon + ' Specimen logged: <b>' + esc(D.specimen.name) + '</b></p>' : '') +
      '<h2>✍️ My answers</h2>' + answers +
      notesHTML() + sketchesHTML() +
      '<h2>📷 My field photos</h2>' + (a.length ? '<div class="ph">' + a.map(function (p) { var ms = (p.mission != null && D.camera && D.camera.missions) ? D.camera.missions[p.mission] : ''; return '<div class="pol"><img src="' + p.src + '"><div>' + esc(p.cap || '') + (ms ? '<br><small>🎯 ' + esc(ms) + '</small>' : '') + (p.tab ? '<br><small>' + esc(p.tab) + '</small>' : '') + '</div></div>'; }).join('') + '</div>' : '<p><i>No photos yet.</i></p>') +
      '<p style="margin-top:24px"><button onclick="print()">🖨 Print or save as PDF</button></p></body></html>';
    var w = null; try { w = window.open('', '_blank'); } catch (e) {}
    if (w && w.document) { w.document.open(); w.document.write(h); w.document.close(); setTimeout(function () { try { w.focus(); w.print(); } catch (e) {} }, 700); }
    else { var bl = new Blob([h], { type: 'text/html' }), x = document.createElement('a'); x.href = URL.createObjectURL(bl); x.download = 'lesson-' + String(D.lesson).replace('.', '-') + '-field-journal.html'; document.body.appendChild(x); x.click(); x.remove(); }
    window.FS_LAST_JOURNAL = h;
  }
  function notesHTML() {
    var H = highlights(), E = evidence(), F = $$('.mind-blow.fs-open .mind-blow-text').map(function (x) { return x.textContent.trim(); });
    function g(c) { var a = H.filter(function (h) { return h.c === c; }); return a.length ? '<p><b>' + HL_COLORS[c].n + '</b></p><ul>' + a.map(function (h) { return '<li><span style="background:' + HL_COLORS[c].c + '">“' + esc(h.t) + '”</span> <small>(' + esc(h.where) + ')</small></li>'; }).join('') + '</ul>' : ''; }
    return '<h2>🖍 My highlights</h2>' + (H.length ? g('g') + g('y') + g('p') : '<p><i>No highlights yet.</i></p>') +
      '<h2>📎 Photo evidence</h2>' + (E.length ? '<ul>' + E.map(function (x) { return '<li>' + esc(x.t) + ' <small>(' + esc(x.where) + ')</small></li>'; }).join('') + '</ul>' : '<p><i>None yet.</i></p>') +
      (D.tool && (store('thermo') || store('fool')) ? '<h2>' + (D.tool.icon || '🧰') + ' Bonus: ' + esc(D.tool.name) + '</h2><p>' + (store('tool-done') ? 'Finished the tool lab.' : 'Started the tool lab.') + '</p>' : '') +
      (F.length ? '<h2>🤯 Field facts I unlocked</h2><ul>' + F.map(function (f) { return '<li>' + esc(f) + '</li>'; }).join('') + '</ul>' : '');
  }
  function sketchesHTML() {
    var ids = ((D.sketch && D.sketch.inline) || []).map(function (x) { return x.id; }).concat(['free']);
    var parts = ids.map(function (id) { var img = sketchImage(id); if (!img) return ''; var st = sketchGet(id);
      return '<div class="sk"><b>' + esc(st.title || 'Untitled sketch') + '</b><img src="' + img + '"></div>'; }).filter(Boolean);
    return '<h2>✏️ My scientific sketches</h2>' + (parts.length ? parts.join('') : '<p><i>No sketches yet.</i></p>');
  }
  function buildJournal() {
    window.fsDownloadJournal = downloadJournal; window.fsToast = function (a, b, c) { toast(a, b, c); };
    var acts = $('.gathered-actions');
    if (acts) { var b = fsOnly(el('button', 'gathered-btn fs-jbtn', '📓 Download my field journal (with photos)')); b.type = 'button'; b.addEventListener('click', downloadJournal); acts.insertBefore(b, acts.firstChild); }
  }

  /* =================== v4: scientific sketch pad =================== */
  var SK_W = 900, SK_H = 560;
  function sketchState(id) { try { return JSON.parse(store('sketch-' + id) || 'null') || { ops: [], title: '' }; } catch (e) { return { ops: [], title: '' }; } }
  function sketchSave(id, st) { try { store('sketch-' + id, JSON.stringify(st)); } catch (e) { /* too big for storage: keep in memory */ } SKMEM[id] = st; }
  var SKMEM = {};
  function sketchGet(id) { return SKMEM[id] || (SKMEM[id] = sketchState(id)); }
  function renderOps(ctx, ops, w, h) {
    ctx.fillStyle = '#fff'; ctx.fillRect(0, 0, w, h);
    ops.forEach(function (o) {
      if (o.t === 's') {
        ctx.strokeStyle = o.c; ctx.lineWidth = o.w; ctx.lineCap = 'round'; ctx.lineJoin = 'round';
        ctx.beginPath(); o.p.forEach(function (pt, i) { if (i) ctx.lineTo(pt[0], pt[1]); else ctx.moveTo(pt[0], pt[1]); });
        if (o.p.length === 1) ctx.lineTo(o.p[0][0] + .1, o.p[0][1]);
        ctx.stroke();
      } else if (o.t === 'l') {
        var fs = o.f || 20; ctx.font = '700 ' + fs + 'px Nunito, Arial, sans-serif';
        var tw = ctx.measureText(o.x).width, bx = o.b[0], by = o.b[1];
        if (o.a) { // leader line + dot on the part
          ctx.strokeStyle = o.c; ctx.lineWidth = Math.max(2, (o.f || 20) / 10); ctx.beginPath(); ctx.moveTo(o.a[0], o.a[1]); ctx.lineTo(bx, by); ctx.stroke();
          ctx.fillStyle = o.c; ctx.beginPath(); ctx.arc(o.a[0], o.a[1], 4, 0, 6.3); ctx.fill();
        }
        var px = bx + (o.a && o.a[0] > bx ? -tw - 14 : 0); px = Math.max(4, Math.min(w - tw - 18, px)); by = Math.max(fs, Math.min(h - fs, by)); var py;
        ctx.fillStyle = 'rgba(255,255,255,.92)'; ctx.strokeStyle = o.c; ctx.lineWidth = 2;
        var bh = Math.round(fs * 1.5); py = by - bh / 2; ctx.beginPath(); if (ctx.roundRect) ctx.roundRect(px, py, tw + 14, bh, 7); else ctx.rect(px, py, tw + 14, bh); ctx.fill(); ctx.stroke();
        ctx.fillStyle = '#1F2A44'; ctx.textBaseline = 'middle'; ctx.fillText(o.x, px + 7, by);
      }
    });
  }
  function sketchImage(id) {
    var st = sketchGet(id); if (!st.ops.length) return '';
    var cv = document.createElement('canvas'); cv.width = SK_W; cv.height = SK_H; renderOps(cv.getContext('2d'), st.ops, SK_W, SK_H);
    return cv.toDataURL('image/jpeg', 0.82);
  }
  function hsl(h, s, l) { return 'hsl(' + Math.round(h) + ',' + Math.round(s) + '%,' + Math.round(l) + '%)'; }
  function sketchPad(id, opts) {
    opts = opts || {};
    var SKD = D.sketch || {}, st = sketchGet(id);
    var pad = fsOnly(el('div', 'fs-sk'));
    var prompts = (opts.prompts || SKD.prompts || []);
    pad.innerHTML =
      '<div class="fs-sk-top"><div><div class="fs-game-k">' + esc(opts.kicker || 'Scientific sketch') + ' <span class="fs-sk-req ' + (opts.required ? 'req' : '') + '">' + (opts.required ? 'Required' : 'Optional') + '</span></div>' +
      '<input class="fs-sk-title" maxlength="60" placeholder="Title your sketch (what is it?)"></div></div>' +
      (prompts.length ? '<div class="fs-sk-ideas"><b>💡 Sketch ideas:</b> ' + prompts.map(function (p, i) { return '<button type="button" class="fs-sk-idea" data-i="' + i + '">' + esc(p) + '</button>'; }).join('') + '</div>' : '') +
      '<div class="fs-sk-bar">' +
        '<div class="fs-sk-tools"><button type="button" data-tool="pen" class="on" title="Pen">✏️ Pen</button><button type="button" data-tool="label" title="Label: drag from the part to where the words go, then type">🏷️ Label</button><button type="button" data-tool="eraser" title="Eraser">🧽 Eraser</button></div>' +
        '<div class="fs-sk-sizes"><button type="button" data-w="3" title="Thin">•</button><button type="button" data-w="7" class="on" title="Medium">●</button><button type="button" data-w="14" title="Thick">⬤</button></div>' +
        '<div class="fs-sk-color"><span class="fs-sk-sw"></span><div class="fs-sk-bars"><div class="fs-sk-hue" title="Pick a color"><i></i></div><div class="fs-sk-shade" title="Lighter or darker"><i></i></div></div></div>' +
        '<div class="fs-sk-acts"><button type="button" class="fs-sk-undo" title="Undo">↶ Undo</button><button type="button" class="fs-sk-clear" title="Clear">🗑 Clear</button></div>' +
      '</div>' +
      '<div class="fs-sk-stage"><canvas width="' + SK_W + '" height="' + SK_H + '"></canvas><div class="fs-sk-hint">' + esc(SKD.tip || 'Draw with the pen. Then use 🏷️ Label: drag from a part of your sketch to an empty spot, and type its name.') + '</div></div>' +
      '<div class="fs-sk-status"></div>';
    var cv = $('canvas', pad), ctx = cv.getContext('2d');
    var tool = 'pen', width = 7, hue = 210, shade = 35, sat = 75;
    var title = $('.fs-sk-title', pad); title.value = st.title || opts.title || '';
    title.addEventListener('input', function () { st.title = title.value; sketchSave(id, st); });
    function color() { return shade <= 2 ? '#111' : shade >= 98 ? '#fff' : hsl(hue, sat, shade); }
    function sw() { $('.fs-sk-sw', pad).style.background = color(); $('.fs-sk-shade', pad).style.background = 'linear-gradient(90deg,#000,' + hsl(hue, sat, 50) + ',#fff)'; }
    function bar(sel, set) {
      var b = $(sel, pad), knob = $('i', b), down = false;
      function at(e) { var r = b.getBoundingClientRect(); var f = Math.max(0, Math.min(1, (e.clientX - r.left) / r.width)); knob.style.left = (f * 100) + '%'; set(f); sw(); if (tool === 'eraser') pick('pen'); }
      b.addEventListener('pointerdown', function (e) { down = true; b.setPointerCapture && b.setPointerCapture(e.pointerId); at(e); });
      b.addEventListener('pointermove', function (e) { if (down) at(e); });
      b.addEventListener('pointerup', function () { down = false; });
    }
    bar('.fs-sk-hue', function (f) { hue = f * 360; });
    bar('.fs-sk-shade', function (f) { shade = f * 100; });
    $('.fs-sk-hue i', pad).style.left = (hue / 360 * 100) + '%'; $('.fs-sk-shade i', pad).style.left = shade + '%'; sw();
    function pick(t) { tool = t; $$('.fs-sk-tools button', pad).forEach(function (b) { b.classList.toggle('on', b.dataset.tool === t); }); cv.dataset.tool = t; }
    $$('.fs-sk-tools button', pad).forEach(function (b) { b.addEventListener('click', function () { pick(b.dataset.tool); SFX.blip(); }); });
    $$('.fs-sk-sizes button', pad).forEach(function (b) { b.addEventListener('click', function () { width = +b.dataset.w; $$('.fs-sk-sizes button', pad).forEach(function (x) { x.classList.toggle('on', x === b); }); }); });
    $$('.fs-sk-idea', pad).forEach(function (b) { b.addEventListener('click', function () { title.value = prompts[+b.dataset.i]; st.title = title.value; sketchSave(id, st); $$('.fs-sk-idea', pad).forEach(function (x) { x.classList.toggle('on', x === b); }); status(); SFX.blip(); }); });
    function redraw(extra) { renderOps(ctx, extra ? st.ops.concat([extra]) : st.ops, SK_W, SK_H); }
    function status() {
      var drew = st.ops.some(function (o) { return o.t === 's' && o.c !== '#fff'; }), labels = st.ops.filter(function (o) { return o.t === 'l'; }).length, need = opts.minLabels || 0;
      var s = $('.fs-sk-status', pad);
      s.innerHTML = '<span class="' + (drew ? 'ok' : '') + '">' + (drew ? '✓' : '○') + ' drawing</span>' +
        '<span class="' + (labels >= need && labels ? 'ok' : '') + '">' + (labels >= need && labels ? '✓' : '○') + ' ' + (need ? labels + ' of ' + need + ' labels' : labels + ' label' + (labels === 1 ? '' : 's')) + '</span>' +
        '<span class="' + (title.value.trim() ? 'ok' : '') + '">' + (title.value.trim() ? '✓' : '○') + ' title</span>' +
        '<span class="fs-sk-saved">Saves by itself · prints in your field journal</span>';
      pad.classList.toggle('done', drew && labels >= need && !!title.value.trim());
    }
    title.addEventListener('input', status);
    function pt(e) { var r = cv.getBoundingClientRect(); return [Math.round((e.clientX - r.left) / r.width * SK_W), Math.round((e.clientY - r.top) / r.height * SK_H)]; }
    var cur = null, la = null;
    function k() { var cw = cv.clientWidth || SK_W; return Math.max(1, SK_W / cw / 1.3); }
    function lf() { var cw = cv.clientWidth || SK_W; return Math.max(20, Math.min(44, Math.round(SK_W / cw * 14))); }
    cv.addEventListener('pointerdown', function (e) {
      e.preventDefault(); cv.setPointerCapture && cv.setPointerCapture(e.pointerId); $('.fs-sk-hint', pad).style.display = 'none';
      if (tool === 'label') { la = { a: pt(e), b: pt(e) }; return; }
      cur = { t: 's', c: tool === 'eraser' ? '#fff' : color(), w: Math.round((tool === 'eraser' ? Math.max(18, width * 3) : width) * k()), p: [pt(e)] }; redraw(cur);
    });
    cv.addEventListener('pointermove', function (e) {
      if (cur) { cur.p.push(pt(e)); redraw(cur); }
      else if (la) { la.b = pt(e); redraw({ t: 'l', a: la.a, b: la.b, x: '…', c: color(), f: lf() }); }
    });
    cv.addEventListener('pointerup', function (e) {
      if (cur) { if (cur.p.length > 2) cur.p = cur.p.filter(function (p, i) { return i % 2 === 0 || i === cur.p.length - 1; }); st.ops.push(cur); cur = null; sketchSave(id, st); redraw(); status(); return; }
      if (la) { var a = la.a, b = la.b, moved = Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]) > 14; la = null; askLabel(moved ? a : null, b); }
    });
    function askLabel(a, b) {
      redraw(a ? { t: 'l', a: a, b: b, x: '…', c: color(), f: lf() } : null);
      var r = cv.getBoundingClientRect(), stage = $('.fs-sk-stage', pad);
      var box = el('div', 'fs-sk-lbl', '<input maxlength="28" placeholder="Type a label"><button type="button">Add</button>');
      box.style.left = Math.min(r.width - 190, Math.max(0, b[0] / SK_W * r.width - 10)) + 'px'; box.style.top = Math.max(0, b[1] / SK_H * r.height - 18) + 'px';
      stage.appendChild(box); var inp = $('input', box); setTimeout(function () { inp.focus(); }, 30);
      var done = false;
      function finish(keep) {
        if (done) return; done = true; var v = inp.value.trim(); box.remove();
        if (keep && v) { st.ops.push({ t: 'l', a: a, b: b, x: v, c: color(), f: lf() }); sketchSave(id, st); SFX.chime(); }
        redraw(); status();
      }
      $('button', box).addEventListener('click', function () { finish(true); });
      inp.addEventListener('keydown', function (e) { if (e.key === 'Enter') finish(true); if (e.key === 'Escape') finish(false); });
      inp.addEventListener('blur', function () { setTimeout(function () { finish(true); }, 150); });
    }
    $('.fs-sk-undo', pad).addEventListener('click', function () { st.ops.pop(); sketchSave(id, st); redraw(); status(); SFX.blip(); });
    var armed = false, clr = $('.fs-sk-clear', pad);
    clr.addEventListener('click', function () {
      if (!armed) { armed = true; clr.textContent = 'Tap again to clear'; clr.classList.add('arm'); setTimeout(function () { armed = false; clr.textContent = '🗑 Clear'; clr.classList.remove('arm'); }, 2500); return; }
      st.ops = []; sketchSave(id, st); redraw(); status(); armed = false; clr.textContent = '🗑 Clear'; clr.classList.remove('arm');
    });
    redraw(); status(); pick('pen');
    if (st.ops.length) $('.fs-sk-hint', pad).style.display = 'none';
    return pad;
  }
  function buildSketch() {
    var S = D.sketch; if (!S) return;
    (S.inline || []).forEach(function (spot) {
      var ref = null;
      if (spot.afterPart) {
        var hdr = $$('#tab-assignment .act-body > p').filter(function (p) { return new RegExp('Part ' + spot.afterPart + '\\b').test(p.textContent); })[0];
        if (hdr) { ref = hdr.nextElementSibling; while (ref && ref.classList.contains('fs-only')) ref = ref.nextElementSibling; }
      }
      if (!ref) { FAILED.push('sketch: no anchor for ' + spot.id); return; }
      while (ref.nextElementSibling && ref.nextElementSibling.classList.contains('fs-in')) ref = ref.nextElementSibling; /* the answer frame comes first; the sketch is the bonus */
      put(sketchPad(spot.id, spot), ref, 'after');
    });
    // free sketch pad from the floating tools
    var fab = $('.fs-fab'); if (!fab) return;
    var b = el('button', 'fs-fab-btn fs-fab-sketch', FAB_ICON.sk + '<span>Sketch</span>'); b.type = 'button'; b.title = 'Make a scientific sketch';
    fab.insertBefore(b, fab.firstChild);
    b.addEventListener('click', function () {
      var m = modal(); m.innerHTML = '<div class="fs-nb fs-kraft fs-nb-wide"><button class="fs-x" type="button" aria-label="Close">✕</button><h3>✏️ Field sketch</h3></div>';
      $('.fs-nb', m).appendChild(sketchPad('free', { kicker: 'Free sketch', required: false }));
      $('.fs-x', m).addEventListener('click', function () { m.classList.remove('open'); });
    });
  }

  /* =================== v5: sealed fact capsules, photo evidence, highlighter =================== */
  function evidence() { try { return JSON.parse(store('evidence') || '[]'); } catch (e) { return []; } }
  function addEvidence(item) { var a = evidence(); if (a.some(function (x) { return x.id === item.id; })) return; a.push(item); store('evidence', JSON.stringify(a)); document.dispatchEvent(new Event('fs:evidence')); }
  function whereAmI(node) {
    var p = node.closest && node.closest('.tab-panel'); var tab = p ? ($('.tab-btn[data-tab="' + p.id.replace('tab-', '') + '"]') || {}).textContent : '';
    tab = (tab || '').replace('✓', '').replace(/^[^A-Za-z]+/, '').trim();
    var h = null, n = node;
    while (n && n !== document.body) { var s = n.previousElementSibling; while (s) { if (/^H3$/.test(s.tagName) || s.classList.contains('act-head')) { h = s; break; } s = s.previousElementSibling; } if (h) break; n = n.parentElement; }
    var ht = h ? (h.querySelector ? (h.querySelector('.act-title') || h).textContent : h.textContent).replace(/^[^A-Za-z]+/, '').split('·').pop().split(':').pop().trim() : '';
    return tab + (ht ? ', ' + ht : '');
  }

  /* ---------- sealed fact capsules ---------- */
  function buildFacts() {
    var facts = $$('.mind-blow'); if (!facts.length) return;
    facts.forEach(function (mb, i) {
      mb.classList.add('fs-sealed');
      var key = 'fact-' + i, txt = $('.mind-blow-text', mb);
      var cover = fsOnly(el('button', 'fs-capsule'));
      cover.type = 'button';
      cover.innerHTML = '<span class="fs-jar"><svg viewBox="0 0 60 70" aria-hidden="true"><rect x="14" y="4" width="32" height="10" rx="3" fill="#C9B489"/><path d="M12 16 h36 v40 a10 10 0 0 1 -10 10 h-16 a10 10 0 0 1 -10 -10z" fill="rgba(185,227,166,.25)" stroke="#B9E3A6" stroke-width="2.5"/><circle cx="24" cy="42" r="4" fill="#F5B83D"/><circle cx="35" cy="34" r="3" fill="#55C8E8"/><circle cx="32" cy="50" r="2.5" fill="#E8636B"/><path d="M20 24 q4 6 0 12" stroke="#fff" stroke-opacity=".5" stroke-width="2" fill="none"/></svg></span>' +
        '<span class="fs-cap-t"><b>Sealed field fact #' + (i + 1) + '</b><span>Tap to crack it open</span></span><span class="fs-cap-lock">🔒</span>';
      mb.appendChild(cover);
      function open(quiet) {
        mb.classList.add('fs-open'); cover.classList.add('pop'); store(key, '1');
        if (quiet) { cover.remove(); return; }
        SFX.whoosh(); setTimeout(SFX.pop, 260); setTimeout(SFX.sparkle, 380);
        burst(mb); setTimeout(function () { cover.remove(); }, 500);
        if (txt && !reduceMotion) typeOut(txt);
        $$('.mind-blow-text strong', mb).forEach(countUp);
        document.dispatchEvent(new Event('fs:evidence'));
      }
      cover.addEventListener('click', function () { open(false); });
      if (store(key)) open(true);
    });
  }
  function burst(host) {
    var r = host.getBoundingClientRect(), cols = ['#F5B83D', '#55C8E8', '#E8636B', '#B9E3A6', '#fff', '#8B6FC0'];
    var layer = fsOnly(el('div', 'fs-burst')); host.appendChild(layer);
    for (var k = 0; k < 26; k++) {
      var s = el('i'); var a = Math.random() * 6.28, d = 60 + Math.random() * 120;
      s.style.setProperty('--dx', Math.cos(a) * d + 'px'); s.style.setProperty('--dy', Math.sin(a) * d * .7 - 30 + 'px');
      s.style.background = cols[k % cols.length]; s.style.left = '50%'; s.style.top = '50%'; s.style.animationDelay = (Math.random() * .12) + 's';
      if (k % 3 === 0) { s.className = 'star'; s.textContent = '✦'; s.style.background = 'none'; s.style.color = cols[k % cols.length]; }
      layer.appendChild(s);
    }
    setTimeout(function () { layer.remove(); }, 1400);
  }
  function typeOut(node) {
    var html = node.innerHTML, plain = node.textContent; node.style.minHeight = node.offsetHeight + 'px';
    var i = 0; node.textContent = ''; node.classList.add('fs-typing');
    var t = setInterval(function () { i += 3; node.textContent = plain.slice(0, i); if (i >= plain.length) { clearInterval(t); node.innerHTML = html; node.classList.remove('fs-typing'); node.style.minHeight = ''; $$('strong', node).forEach(countUp); } }, 16);
  }
  function countUp(s) {
    var m = s.textContent.match(/^(\D*)(\d[\d,]*)(.*)$/); if (!m || reduceMotion) return;
    var target = +m[2].replace(/,/g, ''), t0 = performance.now();
    (function step(now) { var f = Math.min(1, (now - t0) / 900); s.textContent = m[1] + Math.round(target * (1 - Math.pow(1 - f, 3))).toLocaleString() + m[3]; if (f < 1) requestAnimationFrame(step); })(t0);
  }

  /* ---------- real photos with numbered hotspots + an evidence match (SS pattern) ---------- */
  function buildPhotos() {
    (D.photos || []).forEach(function (P) {
      var anchorGame = P.after ? $$('.fs-game').filter(function (g) { return g.dataset.mod === P.after; })[0] : null;
      if (!anchorGame && P.afterText) $$('.tab-panel p').some(function (p) { if (p.textContent.indexOf(P.afterText) > -1) { anchorGame = p; return true; } });
      if (!anchorGame) { FAILED.push('photo: no anchor ' + (P.after || P.afterText)); return; }
      var g = gameShell(P.kicker || 'Look closer', P.title, P.todo, P.why);
      g.classList.add('fs-photo-game'); if (P.clue) g.dataset.mod = P.clue;
      var fig = el('div', 'fs-photo');
      fig.innerHTML = '<div class="fs-photo-img"><img alt="' + esc(P.alt || P.title) + '" src="' + esc(P.img) + '">' +
        P.hotspots.map(function (h) { return '<button type="button" class="fs-hs" data-n="' + h.n + '" style="left:' + h.x + '%;top:' + h.y + '%" aria-label="Label ' + h.n + ': ' + esc(h.label) + '">' + h.n + '</button>'; }).join('') + '</div>' +
        '<div class="fs-srcbar">📷 ' + esc(P.credit) + ' · ' + esc(P.license) + (P.note ? ' · ' + esc(P.note) : '') + '</div>' +
        '<div class="fs-hs-card"><em>Tap a number on the photo.</em></div><div class="fs-count"></div>';
      g.appendChild(fig);
      var card = $('.fs-hs-card', fig), cnt = $('.fs-count', fig), seen = {};
      function upd() { var n = Object.keys(seen).length; cnt.textContent = '🔎 ' + n + ' of ' + P.hotspots.length + ' labels opened'; cnt.classList.toggle('ok', n === P.hotspots.length); if (n === P.hotspots.length) task.classList.add('open'); }
      $$('.fs-hs', fig).forEach(function (b) {
        b.addEventListener('click', function () {
          var h = P.hotspots.filter(function (x) { return String(x.n) === b.dataset.n; })[0];
          $$('.fs-hs', fig).forEach(function (x) { x.classList.remove('on'); }); b.classList.add('on', 'seen'); seen[h.n] = 1; SFX.blip();
          card.innerHTML = '<span class="fs-hs-n">' + h.n + '</span><div><b>' + esc(h.label) + '</b>' + esc(h.t) + '</div>'; card.classList.remove('flash'); void card.offsetWidth; card.classList.add('flash');
          upd();
        });
      });
      // evidence match: which label shows each step?
      var task = el('div', 'fs-ev-task');
      task.innerHTML = '<div class="fs-ev-h">🔎 ' + esc(P.task.q) + '</div>' + P.task.items.map(function (it, i) {
        return '<div class="fs-ev-row" data-i="' + i + '"><span class="fs-ev-step">' + it.icon + ' ' + esc(it.step) + '</span><span class="fs-ev-btns">' +
          P.hotspots.map(function (h) { return '<button type="button" data-n="' + h.n + '">' + h.n + '</button>'; }).join('') + '</span><span class="fs-ev-ok"></span></div>';
      }).join('') + '<div class="fs-miss"></div><div class="fs-win"></div><div class="fs-ev-lock">Open every label first, then match them here.</div>';
      g.appendChild(task);
      var miss = $('.fs-miss', task), win = $('.fs-win', task), left = P.task.items.length;
      $$('.fs-ev-row', task).forEach(function (row) {
        var it = P.task.items[+row.dataset.i];
        $$('button', row).forEach(function (b) {
          b.addEventListener('click', function () {
            if (row.classList.contains('done') || !task.classList.contains('open')) return;
            if ([].concat(it.ans).map(String).indexOf(b.dataset.n) < 0) { bounce(b, miss, it.miss || 'Look at that label again. Which one shows this step?'); return; }
            b.classList.add('right'); row.classList.add('done'); $('.fs-ev-ok', row).textContent = '📎 added to your evidence'; SFX.chime(); miss.classList.remove('show'); left--;
            addEvidence({ id: P.id + '-' + it.step, kind: 'photo', t: it.evid, where: P.short || P.title });
            if (!left) { win.innerHTML = esc(P.task.win); win.classList.add('show'); SFX.win(); store('photo-' + P.id, '1'); if (P.clue) earnClue(P.clue); }
          });
        });
      });
      anchorGame.parentNode.insertBefore(g, anchorGame.nextSibling);
      upd();
    });
  }

  /* ---------- highlighter: select words, tap a colour; feeds the evidence drawer + journal ---------- */
  var HL_SEL = 'p, li, .question, .mind-blow-text, .fc-def, .pq-text, .lesson-figure-caption, .fs-case-p';
  var HL_COLORS = { y: { n: 'Important', c: '#FFE58A' }, g: { n: 'Evidence', c: '#B8EBC6' }, p: { n: 'I wonder', c: '#FFC9DE' } };
  function hlBlocks() {
    return $$(HL_SEL).filter(function (b) {
      if (b.closest('.fs-ms, .fs-hd-panel, .fs-mock, .fs-modal, .fs-hlbar, .gathered-card, textarea, .fs-sk, .fs-board, .fs-hs-card, script, style, .fs-toast')) return false;
      if (b.closest('.fs-only') && !b.classList.contains('fs-case-p')) return false;
      if (!b.closest('.tab-panel, .intro-2col, .fs-casecard')) return false;
      if (b.parentElement && b.parentElement.closest(HL_SEL)) return false; // outermost blocks only
      return b.textContent.trim().length > 2;
    });
  }
  function tnodes(block) {
    var w = document.createTreeWalker(block, NodeFilter.SHOW_TEXT, { acceptNode: function (n) {
      var p = n.parentElement; if (p.closest('.vtip-box')) return NodeFilter.FILTER_REJECT;
      var fo = p.closest('.fs-only'); if (fo && !fo.classList.contains('fs-casecard')) return NodeFilter.FILTER_REJECT;
      return NodeFilter.FILTER_ACCEPT; } });
    var a = [], n; while ((n = w.nextNode())) a.push(n); return a;
  }
  function blockText(block) { return tnodes(block).map(function (n) { return n.nodeValue; }).join(''); }
  function offsetIn(block, node, off) {
    var ns = tnodes(block), sum = 0;
    if (node.nodeType !== 3) { // element boundary: convert to the text node at that child index
      var child = node.childNodes[off]; var probe = child ? (function f(x) { if (x.nodeType === 3) return x; for (var c = x.firstChild; c; c = c.nextSibling) { var r = f(c); if (r) return r; } return null; })(child) : null;
      if (!probe) return blockText(block).length; node = probe; off = 0;
    }
    for (var i = 0; i < ns.length; i++) { if (ns[i] === node) return sum + off; sum += ns[i].nodeValue.length; }
    return -1;
  }
  function wrap(block, s, e, color, id) {
    var ns = tnodes(block), pos = 0;
    ns.forEach(function (n) {
      var len = n.nodeValue.length, a = Math.max(s, pos), b = Math.min(e, pos + len);
      if (a < b) {
        var start = a - pos, end = b - pos, mid = n;
        if (start > 0) mid = n.splitText(start);
        if (end - start < mid.nodeValue.length) mid.splitText(end - start);
        var m = document.createElement('mark'); m.className = 'fs-hl fs-hl-' + color; m.dataset.hl = id; m.title = HL_COLORS[color].n + ' · tap to remove';
        mid.parentNode.insertBefore(m, mid); m.appendChild(mid);
      }
      pos += len;
    });
  }
  function unwrap(id) { $$('mark[data-hl="' + id + '"]').forEach(function (m) { var p = m.parentNode; while (m.firstChild) p.insertBefore(m.firstChild, m); p.removeChild(m); p.normalize(); }); }
  function highlights() { try { return JSON.parse(store('hl') || '[]'); } catch (e) { return []; } }
  function saveHL(a) { store('hl', JSON.stringify(a)); document.dispatchEvent(new Event('fs:evidence')); }
  function buildHighlighter() {
    var bar = fsOnly(el('div', 'fs-hlbar'));
    bar.innerHTML = '<span>🖍</span>' + Object.keys(HL_COLORS).map(function (k) { return '<button type="button" data-c="' + k + '"><i style="background:' + HL_COLORS[k].c + '"></i>' + HL_COLORS[k].n + '</button>'; }).join('');
    document.body.appendChild(bar);
    var pending = null;
    function hide() { bar.classList.remove('show'); pending = null; }
    function check() {
      if (!html.classList.contains('fs-on') || !html.classList.contains('fs-hlmode')) return hide();
      var sel = window.getSelection(); if (!sel || sel.isCollapsed || !sel.rangeCount) return hide();
      var r = sel.getRangeAt(0), sn = r.startContainer.nodeType === 3 ? r.startContainer.parentElement : r.startContainer;
      var block = sn.closest && sn.closest(HL_SEL); var blocks = hlBlocks();
      while (block && blocks.indexOf(block) < 0) block = block.parentElement && block.parentElement.closest(HL_SEL);
      if (!block) return hide();
      var s = offsetIn(block, r.startContainer, r.startOffset), e = block.contains(r.endContainer) ? offsetIn(block, r.endContainer, r.endOffset) : blockText(block).length;
      if (s < 0 || e <= s) return hide();
      var full = blockText(block), t = full.slice(s, e);
      var lead = t.length - t.replace(/^\s+/, '').length; s += lead; t = t.trim(); e = s + t.length;
      if (t.length < 3) return hide();
      pending = { block: block, b: blocks.indexOf(block), s: s, e: e, t: t };
      var rr = r.getBoundingClientRect();
      bar.style.left = Math.max(8, Math.min(window.innerWidth - 330, rr.left + rr.width / 2 - 160)) + 'px';
      bar.style.top = (rr.bottom + window.scrollY + 10) + 'px';
      bar.classList.add('show');
    }
    var tmr = null;
    document.addEventListener('selectionchange', function () { clearTimeout(tmr); tmr = setTimeout(check, 260); });
    $$('button', bar).forEach(function (b) {
      b.addEventListener('pointerdown', function (e) { e.preventDefault(); });
      b.addEventListener('click', function () {
        if (!pending) return; var id = 'h' + Date.now().toString(36), c = b.dataset.c;
        var a = highlights(); a.push({ id: id, b: pending.b, s: pending.s, e: pending.e, t: pending.t, c: c, where: whereAmI(pending.block) }); saveHL(a);
        wrap(pending.block, pending.s, pending.e, c, id); window.getSelection().removeAllRanges(); hide(); SFX.chime();
        if (!store('hl-tip')) { store('hl-tip', '1'); toast('🖍', 'Saved to My notes', c === 'g' ? 'Evidence highlights show up in the 📎 My evidence drawer on the Assignment tab.' : 'Your highlights print in your field journal.'); }
      });
    });
    document.addEventListener('click', function (e) {
      var m = e.target.closest && e.target.closest('mark.fs-hl'); if (!m) return;
      var id = m.dataset.hl; if (!confirmInline(m)) return;
      unwrap(id); saveHL(highlights().filter(function (h) { return h.id !== id; }));
    });
    // restore saved highlights
    var blocks = hlBlocks();
    highlights().forEach(function (h) {
      var b = blocks[h.b];
      if (!b || blockText(b).slice(h.s, h.e) !== h.t) { b = blocks.filter(function (x) { return blockText(x).indexOf(h.t) > -1; })[0]; if (!b) return; h.s = blockText(b).indexOf(h.t); h.e = h.s + h.t.length; }
      wrap(b, h.s, h.e, h.c, h.id);
    });
    // header pill: the Highlighter (first open = a short lesson on how to highlight)
    // floating tool, stacked with Sketch and Snap (first open = a short lesson on how to highlight)
    var fab = $('.fs-fab');
    if (fab) {
      var p = el('button', 'fs-fab-btn fs-fab-hl', FAB_ICON.hl + '<span>Highlight</span><b class="fs-count fs-fab-n">0</b>'); p.type = 'button'; p.title = 'Highlighter: mark the words that matter';
      fab.insertBefore(p, fab.firstChild);
      p.addEventListener('click', function () { if (html.classList.contains('fs-hlmode')) { setMode(false); return; } if (!store('hl-coached')) openCoach(); else setMode(true); });
      function c() { var n = highlights().length + evidence().length; $('.fs-count', p).textContent = n; p.classList.toggle('has', n > 0); } c(); document.addEventListener('fs:evidence', c);
    }
    var banner = fsOnly(el('div', 'fs-hlbanner', '🖍 <b>Highlighter on.</b> Drag your mouse across some words, then pick a color. <button type="button" data-a="tips">Tips</button><button type="button" data-a="notes">My notes</button><button type="button" data-a="off">Turn off</button>'));
    document.body.appendChild(banner);
    $('[data-a="tips"]', banner).addEventListener('click', openCoach);
    $('[data-a="notes"]', banner).addEventListener('click', openNotes);
    $('[data-a="off"]', banner).addEventListener('click', function () { setMode(false); });
    var notesBtn = el('button', 'fs-hl-notes', '📝'); notesBtn.type = 'button'; notesBtn.title = 'My notes'; bar.appendChild(notesBtn);
    notesBtn.addEventListener('pointerdown', function (e) { e.preventDefault(); }); notesBtn.addEventListener('click', function () { hide(); openNotes(); });
  }
  function setMode(on) {
    html.classList.toggle('fs-hlmode', on); var p = $('.fs-fab-hl'); if (p) p.setAttribute('aria-expanded', on ? 'true' : 'false');
    SFX.blip(); if (!on) { var b = $('.fs-hlbar'); if (b) b.classList.remove('show'); }
  }
  function openCoach() {
    var C = D.hlCoach || {}, P = C.practice || {}, m = modal();
    var toks = (P.text || '').split(' ');
    m.innerHTML = '<div class="fs-nb fs-kraft fs-coach"><button class="fs-x" type="button" aria-label="Close">✕</button><h3>🖍 ' + esc(C.title || 'Highlight like a scientist') + '</h3>' +
      '<div class="fs-coach-tips">' + (C.tips || []).map(function (t) { return '<div class="fs-tip"><span>' + t[0] + '</span><div><b>' + esc(t[1]) + '</b>' + esc(t[2]) + '</div></div>'; }).join('') + '</div>' +
      (P.text ? '<div class="fs-practice"><div class="fs-pr-q">' + esc(P.q) + '</div><div class="fs-pr-s">' + toks.map(function (w, i) { return '<button type="button" data-i="' + i + '">' + esc(w) + '</button>'; }).join(' ') + '</div>' +
        '<div class="fs-pr-fb"></div><button type="button" class="fs-btn alt fs-pr-check">Check my highlights</button></div>' : '') +
      (C.outside ? '<p class="fs-coach-out">🌎 ' + esc(C.outside) + '</p>' : '') +
      '<div style="display:flex;gap:8px;flex-wrap:wrap;margin-top:12px"><button type="button" class="fs-btn fs-go">Start highlighting</button><button type="button" class="fs-btn alt fs-nt">📝 My notes</button></div></div>';
    $('.fs-x', m).addEventListener('click', function () { m.classList.remove('open'); });
    $('.fs-nt', m).addEventListener('click', openNotes);
    $('.fs-go', m).addEventListener('click', function () { store('hl-coached', '1'); m.classList.remove('open'); setMode(true); toast('🖍', 'Highlighter on', 'Drag your mouse across some words, then pick a color.'); });
    function clean(w) { return w.replace(/[^A-Za-z’']/g, '').toLowerCase(); }
    $$('.fs-pr-s button', m).forEach(function (b) { b.addEventListener('click', function () { b.classList.toggle('on'); SFX.blip(); }); });
    var ck = $('.fs-pr-check', m), tries = 0;
    if (ck) ck.addEventListener('click', function () {
      tries++;
      var on = $$('.fs-pr-s button.on', m).map(function (b) { return clean(b.textContent); });
      var key = (P.key || []).map(function (w) { return w.toLowerCase(); }), small = (P.small || []).map(function (w) { return w.toLowerCase(); });
      var hit = on.filter(function (w) { return key.indexOf(w) > -1; }).length, smalls = on.filter(function (w) { return small.indexOf(w) > -1; });
      var fb = $('.fs-pr-fb', m), msg;
      if (!on.length) msg = 'Tap a few words first.';
      else if (on.length > 6) msg = 'That’s a lot of the sentence. Try picking only the words that carry the idea (3 to 5).';
      else if (smalls.length) msg = '“' + smalls[0] + '” is a small word that doesn’t carry the idea. Try skipping it.';
      else if (hit >= 3) msg = '✓ Nice! You found the words that carry the idea.';
      else msg = 'Close. Ask: who is it about, which sense, and what does it notice?';
      var showModel = (hit >= 3 && !smalls.length && on.length <= 6) || tries >= 2;
      fb.innerHTML = esc(msg) + (showModel ? '<div class="fs-pr-model">' + esc(P.model || '') + '</div>' : '');
      fb.className = 'fs-pr-fb show' + (hit >= 3 && !smalls.length && on.length <= 6 ? ' ok' : '');
      $$('.fs-pr-s button', m).forEach(function (b) { b.classList.toggle('key', key.indexOf(clean(b.textContent)) > -1 && showModel); });
      if (hit >= 3) SFX.chime(); else SFX.thud();
    });
  }
  function confirmInline(m) {
    if (m.classList.contains('arm')) return true;
    $$('mark.fs-hl.arm').forEach(function (x) { x.classList.remove('arm'); });
    $$('mark[data-hl="' + m.dataset.hl + '"]').forEach(function (x) { x.classList.add('arm'); });
    setTimeout(function () { $$('mark[data-hl="' + m.dataset.hl + '"]').forEach(function (x) { x.classList.remove('arm'); }); }, 2500);
    return false;
  }
  function openNotes() {
    var m = modal(), H = highlights(), E = evidence();
    function group(c) { var a = H.filter(function (h) { return h.c === c; }); return a.length ? '<h4><i style="background:' + HL_COLORS[c].c + '"></i>' + HL_COLORS[c].n + '</h4>' + a.map(function (h) { return '<div class="fs-note">“' + esc(h.t) + '” <small>' + esc(h.where) + '</small></div>'; }).join('') : ''; }
    m.innerHTML = '<div class="fs-nb fs-kraft"><button class="fs-x" type="button" aria-label="Close">✕</button><h3>🖍 My notes</h3>' +
      '<div class="fs-nb-sub">Drag your mouse across any words in the lesson, then pick a color. Click a highlight twice to remove it.</div>' +
      (H.length ? group('g') + group('y') + group('p') : '<p class="fs-empty-roll">No highlights yet.</p>') +
      '<h4>📎 Photo evidence</h4>' + (E.length ? E.map(function (x) { return '<div class="fs-note">' + esc(x.t) + ' <small>' + esc(x.where) + '</small></div>'; }).join('') : '<p class="fs-empty-roll">Match labels on the real photos to collect photo evidence.</p>') +
      '<div style="margin-top:12px"><button type="button" class="fs-btn fs-jr3">📓 Download my field journal</button></div></div>';
    $('.fs-x', m).addEventListener('click', function () { m.classList.remove('open'); });
    $('.fs-jr3', m).addEventListener('click', downloadJournal);
  }
  /* evidence drawer under each written answer: cite a highlight or photo evidence */
  function buildDrawers() {
    $$('#tab-assignment textarea.response-textarea:not(.fs-gmirror)').forEach(function (ta) {
      var help = ta.nextElementSibling && ta.nextElementSibling.classList.contains('fs-help') ? ta.nextElementSibling : null;
      var host = help || ta.parentNode;
      var btn = fsOnly(el('button', 'fs-hintbtn fs-evbtn', '📎 My evidence <b>0</b>')); btn.type = 'button';
      var dr = fsOnly(el('div', 'fs-drawer'));
      if (help) help.insertBefore(btn, help.querySelector('.fs-hintbtn')); else ta.parentNode.insertBefore(btn, ta.nextSibling);
      btn.parentNode.insertBefore(dr, btn.nextSibling);
      function items() { return highlights().filter(function (h) { return h.c !== 'p'; }).map(function (h) { return { t: h.t, where: h.where, kind: h.c === 'g' ? 'Evidence' : 'Important', q: true }; }).concat(evidence().map(function (x) { return { t: x.t, where: x.where, kind: 'Photo', q: false }; })); }
      function count() { $('b', btn).textContent = items().length; }
      function draw() {
        var a = items();
        dr.innerHTML = a.length ? '<div class="fs-dr-h">Tap <b>Cite</b> to put it in your answer. Then explain how it supports your idea, in your own words.</div>' +
          a.map(function (x, i) { return '<div class="fs-dr-i"><span class="fs-dr-k">' + esc(x.kind) + '</span><span class="fs-dr-t">' + (x.q ? '“' + esc(x.t) + '”' : esc(x.t)) + ' <small>' + esc(x.where) + '</small></span><button type="button" data-i="' + i + '">Cite</button></div>'; }).join('')
          : '<div class="fs-dr-h">No evidence yet. Highlight words in the lesson (🖍 green = Evidence), or match labels on the real photos.</div>';
        $$('button', dr).forEach(function (b) { b.addEventListener('click', function () {
          var x = a[+b.dataset.i], ins = x.q ? '“' + x.t + '” (' + x.where + ') ' : '(' + x.t + ') ';
          var p = ta.selectionStart != null ? ta.selectionStart : ta.value.length;
          ta.value = ta.value.slice(0, p) + (p && !/\s$/.test(ta.value.slice(0, p)) ? ' ' : '') + ins + ta.value.slice(p);
          ta.dispatchEvent(new Event('input', { bubbles: true })); ta.focus(); SFX.blip();
        }); });
      }
      btn.addEventListener('click', function () { dr.classList.toggle('open'); draw(); });
      document.addEventListener('fs:evidence', function () { count(); if (dr.classList.contains('open')) draw(); });
      count();
    });
  }

  /* =================== v8: Tool of the Week (optional bonus) =================== */
  var SIMS = {};
  function buildTool() {
    var T = D.tool; if (!T) return;
    var anchor = T.after ? $(T.after) : ($('#tab-' + (T.tab || 'explore') + ' .tab-next-wrap') || $('#tab-' + (T.tab || 'explore') + ' .activity-card')); if (!anchor) { FAILED.push('tool: no anchor'); return; }
    var before = !T.after && anchor.classList.contains('tab-next-wrap');
    var box = fsOnly(el('div', 'fs-tool'));
    box.innerHTML = '<button type="button" class="fs-tool-head"><span class="fs-tool-ic">' + (T.icon || '🧰') + '</span><span><span class="fs-tool-k">' + esc(T.kicker || 'Bonus · Tool of the Week') + ' <span class="fs-sk-req">Optional</span></span>' +
      '<b>' + esc(T.name) + '</b><small>' + esc(T.teaser || '') + '</small></span><span class="fs-tool-c">▾</span></button><div class="fs-tool-body"></div>';
    anchor.parentNode.insertBefore(box, before ? anchor : anchor.nextSibling);
    var body = $('.fs-tool-body', box);
    $('.fs-tool-head', box).addEventListener('click', function () { box.classList.toggle('open'); if (box.classList.contains('open')) SFX.blip(); });
    if (T.why) body.appendChild(whyCard(T.why));
    body.appendChild(slotBox('tool'));
    // 3D model from Sketchfab, through the same manifest as videos; invisible until it is embedded
    var model = el('div', 'fs-model fs-empty');
    model.innerHTML = '<div class="fs-model-ph"><span>🧊</span><div><b>3D model slot</b> <span class="fs-ms-id">' + esc(T.key) + '</span><div class="fs-ms-n">Add an entry "' + esc(T.key) + '" to video-manifest.json with the Sketchfab embed code (status "ready"). Students never see this box.</div></div></div>';
    body.appendChild(model);
    if (T.model) { /* a .glb in the repo, shown with model-viewer (loaded only when a student opens it) */
      model.classList.remove('fs-empty');
      model.innerHTML = '<div class="fs-model-cover"><span>🧊</span><b>Look closer: a 3D ' + esc(T.name.toLowerCase()) + '</b><small>Drag to spin it. Scroll or pinch to zoom in on the parts.</small><button type="button" class="fs-btn">Open the 3D model</button></div>';
      $('.fs-btn', model).addEventListener('click', function () {
        var btn = this; btn.disabled = true; btn.style.display = 'none';
        /* loading bar: first the 3D viewer (0–30%, estimated), then the model itself (30–100%, real progress) */
        var bar = el('div', 'fs-mv-load', '<div class="fs-mv-lt">Loading the 3D model… <span>0%</span></div><div class="fs-mv-track"><i></i></div>');
        $('.fs-model-cover', model).appendChild(bar);
        var fill = $('i', bar), pct = $('span', bar), shown = 0;
        function setP(v) { v = Math.max(shown, Math.min(100, v)); shown = v; fill.style.width = v + '%'; pct.textContent = Math.round(v) + '%'; }
        var est = setInterval(function () { if (shown < 28) setP(shown + 2); }, 120);
        function show() {
          clearInterval(est); setP(30);
          var mv = document.createElement('model-viewer');
          mv.setAttribute('src', T.model); mv.setAttribute('alt', '3D model of a ' + T.name);
          ['camera-controls', 'auto-rotate'].forEach(function (k) { mv.setAttribute(k, ''); });
          mv.setAttribute('touch-action', 'pan-y'); mv.setAttribute('shadow-intensity', '1'); mv.setAttribute('exposure', '1.1');
          mv.setAttribute('interaction-prompt', 'auto'); mv.className = 'fs-mv';
          mv.innerHTML = '<div slot="progress-bar"></div>';
          mv.setAttribute('loading', 'eager'); model.classList.add('fs-mv-wait'); model.appendChild(mv); /* the cover + bar sit on top until the model is ready */
          mv.addEventListener('progress', function (e) { setP(30 + 70 * ((e.detail && e.detail.totalProgress) || 0)); });
          mv.addEventListener('load', function () {
            setP(100);
            setTimeout(function () { var cv = $('.fs-model-cover', model); if (cv) cv.remove(); model.classList.remove('fs-mv-wait'); }, 300);
          });
          mv.addEventListener('error', function () { clearInterval(est); $('.fs-mv-lt', bar).textContent = 'The 3D model couldn’t load. Try again later.'; });
          if (T.modelCredit) model.appendChild(el('div', 'fs-mv-cr', esc(T.modelCredit)));
          SFX.blip();
        }
        if (window.customElements && customElements.get('model-viewer')) return show();
        var sc = document.createElement('script'); sc.src = (D.paths && D.paths.mv) || 'assets/sparkle/vendor/model-viewer-umd.min.js';
        sc.onload = show; sc.onerror = function () { clearInterval(est); $('.fs-mv-lt', bar).textContent = 'The 3D model couldn’t load here.'; };
        document.head.appendChild(sc);
      });
    } else withManifest(function (m) {
      var e = m[T.key]; if (!e || e.status !== 'ready' || !e.embed) return;
      var t = document.createElement('div'); t.innerHTML = e.embed; var f = t.querySelector('iframe'); if (!f) return;
      var src = f.getAttribute('src'); model.classList.remove('fs-empty');
      model.innerHTML = '<div class="fs-model-cover"><span>🧊</span><b>Look closer: a 3D ' + esc(T.name.toLowerCase()) + '</b><small>Drag to spin it. Scroll or pinch to zoom in on the parts.</small><button type="button" class="fs-btn">Open the 3D model</button></div>';
      $('.fs-btn', model).addEventListener('click', function () {
        var fr = document.createElement('iframe'); fr.src = src + (src.indexOf('?') > -1 ? '&' : '?') + 'autostart=1&ui_infos=0&ui_watermark_link=0';
        fr.title = '3D model of a ' + T.name; fr.setAttribute('allow', 'autoplay; fullscreen; xr-spatial-tracking'); fr.setAttribute('allowfullscreen', '');
        model.innerHTML = ''; model.appendChild(fr); SFX.blip();
      });
    });
    var simHost = el('div', 'fs-sim'); body.appendChild(simHost);
    if (SIMS[T.sim]) guard('sim ' + T.sim, function () { SIMS[T.sim](simHost, T); });
  }
  function toolDone() { var T = D.tool; if (!T || store('tool-done')) return; store('tool-done', '1'); toast(T.icon || '🧰', 'Bonus sticker earned!', T.done || 'Tool of the Week: done.'); updateCount(); document.dispatchEvent(new Event('fs:evidence')); }


  /* ----- trail camera simulation (v16): parts, "Will it snap?", and the camera's own four steps ----- */
  var TRAILCAM_SVG = '<svg viewBox="0 0 220 300" class="fs-tc-svg" role="img" aria-label="A trail camera">' +
    '<defs><linearGradient id="tcBody" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#6E7A4E"/><stop offset="1" stop-color="#4C5636"/></linearGradient>' +
    '<radialGradient id="tcLens" cx=".38" cy=".35" r=".7"><stop offset="0" stop-color="#5D7FA8"/><stop offset=".45" stop-color="#1D2C44"/><stop offset="1" stop-color="#0A1220"/></radialGradient>' +
    '<linearGradient id="tcPir" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F4F1E6"/><stop offset="1" stop-color="#CFC9B4"/></linearGradient>' +
    '<pattern id="tcCamo" width="60" height="60" patternUnits="userSpaceOnUse"><path d="M4 10q12-8 20 2t18 0 14 12M0 40q10-6 22 2t16-4 22 8" fill="none" stroke="#3E4729" stroke-width="7" stroke-linecap="round" opacity=".55"/><path d="M30 26q8-6 16 0M8 52q8-5 14 1" fill="none" stroke="#8C9663" stroke-width="5" stroke-linecap="round" opacity=".5"/></pattern></defs>' +
    '<rect x="38" y="6" width="22" height="40" rx="4" fill="#2E3424"/><rect x="160" y="6" width="22" height="40" rx="4" fill="#2E3424"/>' +
    '<rect x="20" y="24" width="180" height="262" rx="26" fill="url(#tcBody)" stroke="#2E3424" stroke-width="4"/>' +
    '<rect x="20" y="24" width="180" height="262" rx="26" fill="url(#tcCamo)"/>' +
    '<rect x="44" y="40" width="132" height="56" rx="10" fill="#1A1F16" stroke="#2E3424" stroke-width="3"/>' +
    (function () { var d = ''; for (var r = 0; r < 4; r++) for (var c = 0; c < 11; c++) d += '<circle class="fs-tc-ir" cx="' + (55 + c * 11) + '" cy="' + (51 + r * 11) + '" r="3.6" fill="#5A1E1E"/>'; return d; })() +
    '<circle cx="110" cy="138" r="34" fill="#20261A" stroke="#2E3424" stroke-width="3"/><circle cx="110" cy="138" r="25" fill="url(#tcLens)"/>' +
    '<circle cx="110" cy="138" r="12" fill="#0A1220"/><circle cx="101" cy="129" r="5" fill="#fff" opacity=".7"/><circle cx="117" cy="146" r="2" fill="#fff" opacity=".5"/>' +
    '<circle class="fs-tc-led" cx="160" cy="118" r="4.5" fill="#3A1414"/>' +
    '<rect x="72" y="186" width="76" height="46" rx="23" fill="#1A1F16"/><path d="M78 209a32 20 0 0 1 64 0a32 20 0 0 1-64 0z" fill="url(#tcPir)"/>' +
    '<path d="M86 209h48M94 197l8 24M118 197l-8 24M126 199l-6 20M94 221l-4-20" stroke="#B3AC94" stroke-width="1.4" fill="none"/>' +
    '<rect x="88" y="248" width="44" height="22" rx="4" fill="#2E3424"/><rect x="96" y="253" width="18" height="12" rx="2" fill="#2F6FD6"/><path d="M110 253h4v4" fill="#2F6FD6"/><rect x="99" y="256" width="2" height="5" fill="#C9DAF5"/><rect x="103" y="256" width="2" height="5" fill="#C9DAF5"/>' +
    '<g class="fs-tc-arcs" fill="none" stroke="#F5B83D" stroke-width="3" stroke-linecap="round"><path d="M70 222q-16-13 0-26"/><path d="M58 230q-26-21 0-42"/><path d="M150 222q16-13 0-26"/><path d="M162 230q26-21 0-42"/></g>' +
    '</svg>';
  SIMS.trailcam = function (host, T) {
    var S = T.cam;
    host.innerHTML = '<div class="fs-game-k">Try it: the trail camera lab</div><div class="fs-game-t">' + esc(S.title) + '</div>' +
      '<ul class="fs-todo">' + S.todo.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>' +
      '<div class="fs-tc"><div class="fs-tc-cam">' + TRAILCAM_SVG + S.parts.map(function (p, i) { return '<button type="button" class="fs-hs fs-tc-hs" style="left:' + p.x + '%;top:' + p.y + '%" data-i="' + i + '">' + (i + 1) + '</button>'; }).join('') +
      '</div><div class="fs-tc-info"><div class="fs-tc-pk">Tap a number on the camera.</div><div class="fs-tc-pt"></div><div class="fs-count fs-tc-pn"></div></div></div>' +
      '<div class="fs-tc-play"><div class="fs-game-k">Will it snap?</div><div class="fs-tc-scene"><div class="fs-tc-mini">' + TRAILCAM_SVG + '</div><div class="fs-tc-walker"></div><div class="fs-tc-photo"></div></div>' +
      '<div class="fs-tc-q"></div><div class="fs-tc-btns"><button type="button" class="fs-btn" data-a="1">📸 It will snap</button><button type="button" class="fs-btn alt" data-a="0">🚫 No picture</button></div>' +
      '<div class="fs-miss fs-tc-fb"></div><div class="fs-tc-roll"></div></div>' +
      '<div class="fs-tc-path"><div class="fs-game-k">The camera’s four steps</div><div class="fs-game-t" style="font-size:18px">' + esc(S.pathTitle) + '</div>' +
      '<div class="fs-sort fs-tc-bins"></div><div class="fs-deck fs-tc-deck"></div><div class="fs-miss fs-tc-miss"></div><div class="fs-win fs-tc-win"></div></div>';
    // 1) parts
    var seen = {}, info = $('.fs-tc-pt', host), pk = $('.fs-tc-pk', host), pn = $('.fs-tc-pn', host);
    function pcount() { var n = Object.keys(seen).length; pn.textContent = '🔎 ' + n + ' of ' + S.parts.length + ' parts'; pn.classList.toggle('ok', n === S.parts.length); if (n === S.parts.length) host.classList.add('parts-done'); }
    $$('.fs-tc-hs', host).forEach(function (b) { b.addEventListener('click', function () {
      var p = S.parts[+b.dataset.i]; seen[b.dataset.i] = 1; $$('.fs-tc-hs', host).forEach(function (x) { x.classList.toggle('on', x === b); }); b.classList.add('seen');
      pk.textContent = (+b.dataset.i + 1) + ' · ' + p.label; info.textContent = p.t; SFX.blip(); pcount();
      if (p.fx === 'ir') { var c = $('.fs-tc-cam', host); c.classList.remove('ir'); void c.offsetWidth; c.classList.add('ir'); }
      if (p.fx === 'pir') { var c2 = $('.fs-tc-cam', host); c2.classList.remove('pir'); void c2.offsetWidth; c2.classList.add('pir'); }
    }); });
    pcount();
    // 2) will it snap?
    var k = 0, right = 0, busy = false, q = $('.fs-tc-q', host), fb = $('.fs-tc-fb', host), walker = $('.fs-tc-walker', host), scene = $('.fs-tc-scene', host), roll = $('.fs-tc-roll', host), photo = $('.fs-tc-photo', host);
    function ask() {
      var sc = S.scenes[k]; if (!sc) { q.innerHTML = '<b>' + esc(S.playWin) + '</b>'; $('.fs-tc-btns', host).style.display = 'none'; host.classList.add('play-done'); return; }
      q.innerHTML = '<span class="fs-tc-n">' + (k + 1) + ' of ' + S.scenes.length + '</span> ' + esc(sc.q); walker.textContent = ''; walker.className = 'fs-tc-walker'; scene.className = 'fs-tc-scene'; photo.className = 'fs-tc-photo';
    }
    $$('.fs-tc-btns button', host).forEach(function (b) { b.addEventListener('click', function () {
      if (busy || !S.scenes[k]) return; busy = true; var sc = S.scenes[k], guess = b.dataset.a === '1';
      walker.textContent = sc.icon; walker.className = 'fs-tc-walker go ' + (sc.far ? 'far' : '') + (sc.wind ? ' wind' : '');
      setTimeout(function () {
        if (sc.snap) { scene.classList.add('snap'); SFX.snap(); photo.innerHTML = '<span>' + sc.icon + '</span><small>' + esc(sc.time) + '</small>'; photo.className = 'fs-tc-photo show';
          var r = el('div', 'fs-tc-shot', '<span>' + sc.icon + '</span><small>' + esc(sc.time) + '</small>'); roll.appendChild(r); }
        else scene.classList.add('nosnap');
        var ok = guess === sc.snap; if (ok) right++;
        fb.innerHTML = (ok ? '✅ ' : '🔎 ') + '<b>' + (sc.snap ? 'Snap! ' : 'No picture. ') + '</b>' + esc(sc.why); fb.classList.remove('show'); void fb.offsetWidth; fb.classList.add('show');
        if (ok) SFX.chime(); else SFX.thud();
        setTimeout(function () { busy = false; k++; ask(); maybeDone(); }, 2600);
      }, 1400);
    }); });
    ask();
    // 3) the camera's four steps: drag each camera card into its step
    var bins = $('.fs-tc-bins', host), deck = $('.fs-tc-deck', host), miss = $('.fs-tc-miss', host), win = $('.fs-tc-win', host);
    ['⚡ Stimulus', '👂 Sense organ', '🧠 Brain', '🏃 Response'].forEach(function (t, i) { var b = el('div', 'fs-bin', '<div class="fs-bin-h">' + esc(t) + '</div>'); b.dataset.i = i; b.dataset.drop = '1'; bins.appendChild(b); });
    var left = S.steps.length;
    shuffle(S.steps).forEach(function (c) { var d = el('div', 'fs-card', esc(c.t)); d.dataset.bin = c.bin; d.dataset.miss = c.miss || ''; deck.appendChild(d); });
    var targets = $$('.fs-bin', bins);
    function drop(card, bin) {
      if (card.classList.contains('placed')) return;
      if (String(bin.dataset.i) !== String(card.dataset.bin)) { bounce(card, miss, card.dataset.miss || 'Look again.'); return; }
      card.classList.add('placed'); card.classList.remove('sel'); bin.appendChild(card); SFX.chime(); miss.classList.remove('show'); left--;
      if (!left) { win.innerHTML = esc(S.pathWin); win.classList.add('show'); SFX.win(); host.classList.add('path-done'); maybeDone(); }
    }
    $$('.fs-card', deck).forEach(function (c) { dragDrop(c, function () { return targets; }, drop); });
    tapTargets(host.querySelector('.fs-tc-path'), targets, drop);
    function maybeDone() { if (host.classList.contains('play-done') && host.classList.contains('path-done')) toolDone(); }
  };

  /* ----- Berlese funnel simulation (10.01): parts, predict, run the lamp, meet what fell into the jar -----
     T.berlese = {title, todo[], parts:[{x,y,label,t}], predict:{q, opts:[{t, ok, why}]}, days:[{t, n}], critters:[{name, count, job, t}], runWin, meetWin} */
  var BERLESE_SVG = '<svg viewBox="0 0 220 320" class="fs-bf-svg" role="img" aria-label="A Berlese funnel: a lamp over a funnel of leaf litter, with a jar underneath">' +
    '<defs><linearGradient id="bfGlass" x1="0" x2="1"><stop offset="0" stop-color="#DDEFF5"/><stop offset=".5" stop-color="#F7FCFE"/><stop offset="1" stop-color="#CFE5EE"/></linearGradient>' +
    '<radialGradient id="bfGlow" cx=".5" cy="0" r="1"><stop offset="0" stop-color="#FFE9A8" stop-opacity=".95"/><stop offset="1" stop-color="#FFE9A8" stop-opacity="0"/></radialGradient></defs>' +
    '<path class="fs-bf-glow" d="M70 52 L30 150 L190 150 L150 52Z" fill="url(#bfGlow)" opacity="0"/>' +
    '<rect x="104" y="0" width="12" height="18" fill="#5C6670"/><path d="M68 18 h84 l12 34 h-108z" fill="#3E4A55"/><ellipse class="fs-bf-bulb" cx="110" cy="54" rx="16" ry="7" fill="#C9C2A8"/>' +
    '<path d="M22 112 h176 l-74 104 h-28z" fill="#E9EEF1" stroke="#7D8C95" stroke-width="3"/>' +
    '<g class="fs-bf-litter"><path d="M30 112 q20 -16 40 -4 q16 -14 34 -2 q18 -12 36 0 q20 -12 50 6 v16 h-160z" fill="#8A5A2B"/>' +
    '<path d="M40 104 l14 -6 l6 8z M84 100 l16 -4 l-4 9z M128 102 l14 -5 l2 9z M160 106 l12 -3 l-2 8z" fill="#B07A3E"/></g>' +
    '<path d="M28 128 h164" stroke="#5C6670" stroke-width="2.5" stroke-dasharray="4 3"/>' +
    '<rect x="96" y="216" width="28" height="22" fill="#E9EEF1" stroke="#7D8C95" stroke-width="3"/>' +
    '<path d="M74 240 h72 v62 q0 14 -14 14 h-44 q-14 0 -14 -14z" fill="url(#bfGlass)" stroke="#7D8C95" stroke-width="3"/>' +
    '<g class="fs-bf-specks"></g>' +
    '</svg>';
  SIMS.berlese = function (host, T) {
    var S = T.berlese;
    host.innerHTML = '<div class="fs-game-k">Try it: the soil-critter lab</div><div class="fs-game-t">' + esc(S.title) + '</div>' +
      '<ul class="fs-todo">' + S.todo.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>' +
      '<div class="fs-bf"><div class="fs-bf-rig">' + BERLESE_SVG + S.parts.map(function (p, i) { return '<button type="button" class="fs-hs fs-bf-hs" style="left:' + p.x + '%;top:' + p.y + '%" data-i="' + i + '">' + (i + 1) + '</button>'; }).join('') + '</div>' +
      '<div class="fs-bf-side"><div class="fs-hs-card fs-bf-info"><em>Tap a number to learn each part.</em></div><div class="fs-count fs-bf-pn"></div>' +
      '<div class="fs-bf-step fs-bf-predict"><div class="fs-in-k">' + esc(S.predict.q) + '</div><div class="fs-in-chips">' + S.predict.opts.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(o.t) + '</button>'; }).join('') + '</div><div class="fs-miss fs-bf-pm"></div></div>' +
      '<div class="fs-bf-step fs-bf-run"><button type="button" class="fs-btn fs-bf-go">💡 Turn on the lamp</button><div class="fs-bf-day"></div></div>' +
      '</div></div>' +
      '<div class="fs-bf-jar"><div class="fs-in-k">What fell into the jar (looked at with a hand lens)</div><div class="fs-bf-crits"></div><div class="fs-hs-card fs-bf-cinfo" style="display:none"></div><div class="fs-count fs-bf-cn"></div></div>' +
      '<div class="fs-win fs-bf-win"></div>';
    var info = $('.fs-bf-info', host), pn = $('.fs-bf-pn', host), seen = {}, predicted = false, day = 0, met = {};
    function pcount() { var n = Object.keys(seen).length; pn.textContent = '🔎 ' + n + ' of ' + S.parts.length + ' parts'; pn.classList.toggle('ok', n === S.parts.length); if (n === S.parts.length) host.classList.add('bf-parts'); }
    $$('.fs-bf-hs', host).forEach(function (b) { b.addEventListener('click', function () {
      var p = S.parts[+b.dataset.i]; seen[b.dataset.i] = 1; $$('.fs-bf-hs', host).forEach(function (x) { x.classList.toggle('on', x === b); }); b.classList.add('seen');
      info.innerHTML = '<span class="fs-hs-n">' + (+b.dataset.i + 1) + '</span><div><b>' + esc(p.label) + '</b>' + esc(p.t) + '</div>'; SFX.blip(); pcount();
    }); });
    pcount();
    var pm = $('.fs-bf-pm', host);
    $$('.fs-bf-predict .fs-in-chip', host).forEach(function (c) { c.addEventListener('click', function () {
      var o = S.predict.opts[+c.dataset.i];
      $$('.fs-bf-predict .fs-in-chip', host).forEach(function (x) { x.classList.toggle('on', x === c); });
      pm.innerHTML = (o.ok ? '✅ ' : '🔎 ') + esc(o.why); pm.classList.add('show'); pm.classList.toggle('ok', !!o.ok);
      if (o.ok) { predicted = true; host.classList.add('bf-predicted'); SFX.chime(); } else SFX.thud();
    }); });
    var go = $('.fs-bf-go', host), dayBox = $('.fs-bf-day', host), specks = $('.fs-bf-specks', host), rig = $('.fs-bf-rig', host);
    var total = S.critters.reduce(function (a, c) { return a + c.count; }, 0);
    go.addEventListener('click', function () {
      if (!predicted) { pm.innerHTML = '🔎 ' + esc(S.predictFirst || 'Make your prediction first.'); pm.classList.add('show'); pm.classList.remove('ok'); SFX.thud(); return; }
      if (day >= S.days.length) return;
      var d = S.days[day]; day++; rig.classList.add('lamp'); rig.style.setProperty('--dry', day / S.days.length); SFX.blip();
      dayBox.innerHTML = '<b>' + esc(d.t) + '</b> · ' + d.n + ' tiny animals in the jar so far';
      var have = specks.childNodes.length, want = Math.round(d.n / total * 40);
      for (var i = have; i < want; i++) { var c = document.createElementNS('http://www.w3.org/2000/svg', 'circle'); c.setAttribute('cx', 84 + Math.random() * 52); c.setAttribute('cy', 268 + Math.random() * 40); c.setAttribute('r', 1.4 + Math.random() * 1.4); c.setAttribute('fill', '#3B2F1E'); c.style.animationDelay = (Math.random() * 0.8) + 's'; specks.appendChild(c); }
      go.textContent = day < S.days.length ? 'Next day ▶' : '✅ The leaves are dry';
      if (day >= S.days.length) { go.disabled = true; showCrits(); }
    });
    var crits = $('.fs-bf-crits', host), cinfo = $('.fs-bf-cinfo', host), cn = $('.fs-bf-cn', host);
    function showCrits() {
      host.classList.add('bf-ran'); SFX.chime();
      crits.innerHTML = S.critters.map(function (c, i) { return '<button type="button" class="fs-bf-crit" data-i="' + i + '"><b>' + c.count + '</b>' + esc(c.name) + '</button>'; }).join('');
      $$('.fs-bf-crit', crits).forEach(function (b) { b.addEventListener('click', function () {
        var c = S.critters[+b.dataset.i]; met[b.dataset.i] = 1; b.classList.add('seen', c.job); SFX.blip();
        cinfo.style.display = ''; cinfo.innerHTML = '<span class="fs-hs-n">' + (c.job === 'recycler' ? '♻️' : '🎯') + '</span><div><b>' + esc(c.name) + ' · ' + (c.job === 'recycler' ? 'recycler' : 'hunter') + '</b>' + esc(c.t) + '</div>';
        var n = Object.keys(met).length; cn.textContent = '🔎 ' + n + ' of ' + S.critters.length + ' kinds met'; cn.classList.toggle('ok', n === S.critters.length);
        if (n === S.critters.length) { var w = $('.fs-bf-win', host); if (!w.classList.contains('show')) { w.innerHTML = esc(S.meetWin); w.classList.add('show'); SFX.win(); toolDone(); } }
      }); });
      cn.textContent = '🔎 0 of ' + S.critters.length + ' kinds met';
    }
  };

  /* ----- Secchi disk simulation (10.02): lower the disk, call it when it disappears, compare three waters -----
     T.secchi = {title, todo[], parts:[{label, t}], sites:[{k, name, icon, clear, bottom, tint, note}], q:{q, opts:[{t, ok, why}]}, done} */
  SIMS.secchi = function (host, T) {
    var S = T.secchi, FT = 22, maxD = 20;
    host.innerHTML = '<div class="fs-game-k">Try it: the water-clarity lab</div><div class="fs-game-t">' + esc(S.title) + '</div>' +
      '<ul class="fs-todo">' + S.todo.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>' +
      '<div class="fs-sd-parts">' + S.parts.map(function (p, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(p.label) + '</button>'; }).join('') + '</div><div class="fs-hs-card fs-sd-pinfo"><em>Tap a part of the Secchi disk to learn what it does.</em></div>' +
      '<div class="fs-sd-sites">' + S.sites.map(function (s, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '"><span>' + s.icon + '</span>' + esc(s.name) + '<em></em></button>'; }).join('') + '</div>' +
      '<div class="fs-sd"><svg class="fs-sd-svg" viewBox="0 0 220 330" role="img" aria-label="A Secchi disk on a rope, lowered into water">' +
        '<rect x="0" y="0" width="220" height="30" fill="#CFE8F6"/><rect class="fs-sd-water" x="0" y="30" width="220" height="300" fill="#3A9AC4"/>' +
        '<g class="fs-sd-ticks"></g><line class="fs-sd-rope" x1="110" y1="0" x2="110" y2="40" stroke="#C9A877" stroke-width="3"/>' +
        '<g class="fs-sd-disk"><circle cx="110" cy="0" r="22" fill="#fff" stroke="#222" stroke-width="2"/><path d="M110,0 L110,-22 A22,22 0 0 1 132,0 Z M110,0 L110,22 A22,22 0 0 1 88,0 Z" fill="#111"/><rect x="104" y="8" width="12" height="16" fill="#555" rx="2"/></g>' +
        '<rect class="fs-sd-murk" x="0" y="30" width="220" height="300" fill="#3A9AC4" opacity="0"/><rect class="fs-sd-bottom" x="0" y="318" width="220" height="12" fill="#D9C79E"/></svg>' +
        '<div class="fs-sd-side"><div class="fs-sd-depth">Pick a place to test.</div><div class="fs-sd-btns"><button type="button" class="fs-btn alt" data-d="-1">⬆ Up 1 foot</button><button type="button" class="fs-btn alt" data-d="1">⬇ Down 1 foot</button></div>' +
        '<button type="button" class="fs-btn fs-sd-call">👀 I can’t see it anymore!</button><div class="fs-miss fs-sd-fb"></div><table class="fs-sv-log fs-sd-log"><thead><tr><th>Place</th><th>Disk disappeared at</th></tr></thead><tbody></tbody></table></div></div>' +
      '<div class="fs-sv-q fs-sd-q"></div><div class="fs-win fs-sd-win"></div>';
    var pinfo = $('.fs-sd-pinfo', host), seenP = {};
    $$('.fs-sd-parts .fs-in-chip', host).forEach(function (c) { c.addEventListener('click', function () { var p = S.parts[+c.dataset.i]; seenP[c.dataset.i] = 1; c.classList.add('on'); pinfo.innerHTML = '<span class="fs-hs-n">⚪</span><div><b>' + esc(p.label) + '</b>' + esc(p.t) + '</div>'; SFX.blip(); }); });
    var site = null, d = 0, results = {}, fb = $('.fs-sd-fb', host), disk = $('.fs-sd-disk', host), rope = $('.fs-sd-rope', host), murk = $('.fs-sd-murk', host), water = $('.fs-sd-water', host), depthBox = $('.fs-sd-depth', host);
    var ticks = ''; for (var f = 0; f <= maxD; f += 2) ticks += '<line x1="140" x2="150" y1="' + (30 + f * 14) + '" y2="' + (30 + f * 14) + '" stroke="#fff" opacity=".7"/><text x="154" y="' + (34 + f * 14) + '" fill="#fff" font-size="10">' + f + ' ft</text>';
    $('.fs-sd-ticks', host).innerHTML = ticks;
    function draw() {
      if (!site) return; var y = 30 + d * 14; disk.setAttribute('transform', 'translate(0,' + y + ')'); rope.setAttribute('y2', y - 22);
      var vis = site.clear >= site.bottom ? 1 : Math.max(0, 1 - d / site.clear); disk.style.opacity = vis < 0.08 ? 0 : (0.15 + 0.85 * vis);
      depthBox.innerHTML = '<b>' + site.icon + ' ' + esc(site.name) + '</b><br>Disk depth: <b>' + d + ' ft</b>' + (d >= site.bottom ? ' (the bottom)' : '');
    }
    $$('.fs-sd-sites .fs-in-chip', host).forEach(function (c) { c.addEventListener('click', function () {
      site = S.sites[+c.dataset.i]; d = 0; $$('.fs-sd-sites .fs-in-chip', host).forEach(function (x) { x.classList.toggle('on', x === c); });
      water.setAttribute('fill', site.tint); murk.setAttribute('fill', site.tint); var bt = $('.fs-sd-bottom', host); bt.setAttribute('y', 30 + site.bottom * 14); bt.setAttribute('height', 300 - site.bottom * 14);
      fb.classList.remove('show'); SFX.blip(); draw(); }); });
    $$('.fs-sd-btns button', host).forEach(function (b) { b.addEventListener('click', function () { if (!site) { fb.innerHTML = '🔎 Pick a place to test first.'; fb.classList.add('show'); return; }
      d = Math.max(0, Math.min(site.bottom, d + (+b.dataset.d))); SFX.blip(); draw();
      if (d === site.bottom && site.clear >= site.bottom) { record('Still visible on the bottom (' + site.bottom + ' ft)!'); fb.innerHTML = '✅ ' + esc(site.note); fb.classList.add('show'); SFX.chime(); } }); });
    $('.fs-sd-call', host).addEventListener('click', function () {
      if (!site) { fb.innerHTML = '🔎 Pick a place to test first.'; fb.classList.add('show'); return; }
      if (site.clear >= site.bottom) { fb.innerHTML = '🔎 Look closely: can you still see the disk? Keep lowering it.'; fb.classList.add('show'); SFX.thud(); return; }
      if (d < site.clear - 1) { fb.innerHTML = '🔎 You can still see it. Lower it a little more.'; fb.classList.add('show'); SFX.thud(); return; }
      record('about ' + site.clear + ' ft'); fb.innerHTML = '✅ ' + esc(site.note); fb.classList.add('show'); SFX.chime();
    });
    function record(txt) {
      results[site.k] = txt;
      $('.fs-sd-log tbody', host).innerHTML = S.sites.filter(function (s) { return results[s.k]; }).map(function (s) { return '<tr><td>' + s.icon + ' ' + esc(s.name) + '</td><td><b>' + esc(results[s.k]) + '</b></td></tr>'; }).join('');
      var c = $$('.fs-sd-sites .fs-in-chip', host)[S.sites.indexOf(site)]; c.classList.add('done'); $('em', c).textContent = ' ✓';
      if (Object.keys(results).length === S.sites.length) ask();
    }
    function ask() {
      var q = $('.fs-sd-q', host); if (q.dataset.on) return; q.dataset.on = '1';
      q.innerHTML = '<div class="fs-in-k">' + esc(S.q.q) + '</div><div class="fs-in-chips">' + S.q.opts.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(o.t) + '</button>'; }).join('') + '</div>';
      $$('.fs-in-chip', q).forEach(function (c) { c.addEventListener('click', function () { var o = S.q.opts[+c.dataset.i];
        if (!o.ok) { bounce(c, fb, o.why); return; } c.classList.add('on', 'ok'); var w = $('.fs-sd-win', host); w.innerHTML = esc(o.why); w.classList.add('show'); SFX.win(); toolDone(); }); });
    }
  };
  /* ----- X-ray viewer (11.01): put a film on the light box, tap the numbers to see what's inside ----- 
     T.xray = {title, todo[], films:[{k,name,icon,img,alt,credit,spots:[{n,x,y,label,kind:'inside'|'outside',t}]}], q:{q,opts:[{t,ok,why}]}} */
  SIMS.xray = function (host, T) {
    var S = T.xray;
    host.innerHTML = '<div class="fs-game-k">Try it: the X-ray light box</div><div class="fs-game-t">' + esc(S.title) + '</div>' +
      '<ul class="fs-todo">' + S.todo.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>' +
      '<div class="fs-xr-films">' + S.films.map(function (f, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '"><span>' + f.icon + '</span>' + esc(f.name) + '<em></em></button>'; }).join('') + '</div>' +
      '<div class="fs-xr-box"><div class="fs-xr-light"><div class="fs-xr-empty">💡 Pick a film to clip onto the light box.</div></div></div>' +
      '<div class="fs-hs-card fs-xr-info"><em>Tap a number on the X-ray.</em></div><div class="fs-sv-q fs-xr-q"></div><div class="fs-miss fs-xr-miss"></div><div class="fs-win fs-xr-win"></div>';
    var light = $('.fs-xr-light', host), info = $('.fs-xr-info', host), seen = {};
    try { seen = JSON.parse(store('xray') || '{}'); } catch (e) {}
    function film(i) {
      var f = S.films[i]; SFX.blip();
      $$('.fs-xr-films .fs-in-chip', host).forEach(function (c) { c.classList.toggle('on', +c.dataset.i === i); });
      light.innerHTML = '<div class="fs-xr-film"><img alt="' + esc(f.alt) + '" src="' + esc(f.img) + '">' + f.spots.map(function (s, k) { return '<button type="button" class="fs-hs' + (seen[f.k + k] ? ' seen' : '') + '" style="left:' + s.x + '%;top:' + s.y + '%" data-k="' + k + '">' + s.n + '</button>'; }).join('') + '</div><div class="fs-xr-cr">' + esc(f.credit) + '</div>';
      if (!reduceMotion) { light.classList.remove('on'); void light.offsetWidth; light.classList.add('on'); }
      info.innerHTML = '<em>' + esc(f.intro || 'Tap a number on the X-ray.') + '</em>';
      $$('.fs-hs', light).forEach(function (d) { d.addEventListener('click', function () {
        var s = f.spots[+d.dataset.k]; seen[f.k + d.dataset.k] = 1; store('xray', JSON.stringify(seen)); d.classList.add('seen'); SFX.chime();
        info.innerHTML = '<span class="fs-hs-n">' + s.n + '</span><div><b>' + esc(s.label) + ' <span class="fs-xr-kind ' + s.kind + '">' + (s.kind === 'inside' ? 'internal' : 'external') + '</span></b>' + esc(s.t) + '</div>';
        info.classList.remove('flash'); void info.offsetWidth; info.classList.add('flash'); check();
      }); });
      check();
    }
    function check() {
      S.films.forEach(function (f, i) { var all = f.spots.every(function (s, k) { return seen[f.k + k]; }); var c = $$('.fs-xr-films .fs-in-chip', host)[i]; c.classList.toggle('done', all); $('em', c).textContent = all ? ' ✓' : ''; });
      var every = S.films.every(function (f) { return f.spots.every(function (s, k) { return seen[f.k + k]; }); });
      if (every) ask();
    }
    function ask() {
      var q = $('.fs-xr-q', host); if (q.dataset.on) return; q.dataset.on = '1';
      q.innerHTML = '<div class="fs-in-k">' + esc(S.q.q) + '</div><div class="fs-in-chips">' + S.q.opts.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(o.t) + '</button>'; }).join('') + '</div>';
      $$('.fs-in-chip', q).forEach(function (c) { c.addEventListener('click', function () { var o = S.q.opts[+c.dataset.i];
        if (!o.ok) { bounce(c, $('.fs-xr-miss', host), o.why); return; } $('.fs-xr-miss', host).classList.remove('show');
        c.classList.add('on', 'ok'); var w = $('.fs-xr-win', host); w.innerHTML = esc(o.why); w.classList.add('show'); SFX.win(); toolDone(); }); });
    }
    $$('.fs-xr-films .fs-in-chip', host).forEach(function (c) { c.addEventListener('click', function () { film(+c.dataset.i); }); });
    check();
  };

  /* ----- digital calipers (13.01): measure leaves from one parent plant grown in sun and in shade ----- */
  SIMS.calipers = function (host, T) {
    var S = T.calipers;
    host.innerHTML = '<div class="fs-game-k">Try it: digital calipers</div><div class="fs-game-t">' + esc(S.title) + '</div>' +
      '<ul class="fs-todo">' + S.todo.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>' +
      '<div class="fs-cp-tool"><svg viewBox="0 0 400 120" class="fs-cp-svg" role="img" aria-label="Digital calipers: a steel ruler bar with a fixed jaw on the left, a sliding jaw, and a small screen that shows the length.">' +
      '<rect x="20" y="30" width="370" height="16" rx="3" fill="#C9D1D6" stroke="#6E7A82" stroke-width="2"/>' +
      (function () { var d = ''; for (var i = 0; i <= 34; i++) d += '<line x1="' + (40 + i * 10) + '" y1="30" x2="' + (40 + i * 10) + '" y2="' + (i % 5 ? 36 : 41) + '" stroke="#55606A" stroke-width="1.2"/>'; return d; })() +
      '<path d="M24 24h16v92h-8l-8-8z" fill="#AEB8BE" stroke="#6E7A82" stroke-width="2"/>' +
      '<g class="fs-cp-jaw"><path d="M0 20h66v36h-54v60h-4l-8-8z" fill="#8E9AA2" stroke="#55606A" stroke-width="2"/><rect x="16" y="24" width="46" height="20" rx="3" fill="#1D2B22"/><text class="fs-cp-read" x="39" y="39" text-anchor="middle" font-family="Courier New,monospace" font-size="12" font-weight="900" fill="#9EF0A8">0.0</text><text x="39" y="52" text-anchor="middle" font-family="Nunito,sans-serif" font-size="7" font-weight="800" fill="#24313A">mm</text></g>' +
      '</svg><div class="fs-cp-leafbox"><img class="fs-cp-leaf" alt="" src="' + esc(S.leafImg) + '"></div></div>' +
      '<div class="fs-cp-picks">' + S.groups.map(function (gr) { return '<div class="fs-cp-g"><b>' + gr.icon + ' ' + esc(gr.t) + '</b>' + gr.leaves.map(function (mm, i) { return '<button type="button" class="fs-in-chip" data-g="' + gr.k + '" data-i="' + i + '">🍃 Leaf ' + (i + 1) + '<em></em></button>'; }).join('') + '</div>'; }).join('') + '</div>' +
      '<div class="fs-cp-plot"></div><div class="fs-sv-q fs-cp-q"></div><div class="fs-miss fs-cp-miss"></div><div class="fs-win fs-cp-win"></div>' +
      (S.credit ? '<div class="fs-xr-cr">' + esc(S.credit) + '</div>' : '');
    var jaw = $('.fs-cp-jaw', host), read = $('.fs-cp-read', host), leaf = $('.fs-cp-leaf', host), plot = $('.fs-cp-plot', host);
    var got = {}; try { got = JSON.parse(store('calipers') || '{}'); } catch (e) {}
    var MAX = S.maxMm || 100, PX = 330 / MAX; /* svg units per mm; jaw 0 sits at x=40 */
    function setJaw(mm, animate) {
      jaw.style.transition = animate && !reduceMotion ? 'transform .9s cubic-bezier(.3,1.2,.5,1)' : 'none';
      jaw.style.transform = 'translateX(' + (40 + mm * PX) + 'px)'; /* SVG user units: the sliding jaw's face sits at x = 40 + mm */
    }
    function count(target, ms) {
      if (reduceMotion || !ms) { read.textContent = target.toFixed(1); return; }
      var t0 = performance.now(); (function f(t) { var k = Math.min(1, (t - t0) / ms); read.textContent = (target * k).toFixed(1); if (k < 1) requestAnimationFrame(f); })(t0);
    }
    setJaw(0, false);
    function draw() {
      var all = S.groups.map(function (gr) {
        var vals = gr.leaves.filter(function (mm, i) { return got[gr.k + i]; });
        var avg = vals.length ? (vals.reduce(function (a, b) { return a + b; }, 0) / vals.length) : null;
        return '<div class="fs-cp-row"><span class="fs-cp-rl">' + gr.icon + ' ' + esc(gr.short || gr.t) + '</span><div class="fs-cp-line">' +
          vals.map(function (mm) { return '<i style="left:' + (100 * mm / MAX) + '%" title="' + mm + ' mm"></i>'; }).join('') +
          (avg != null && vals.length === gr.leaves.length ? '<u style="left:' + (100 * avg / MAX) + '%"></u>' : '') + '</div><span class="fs-cp-avg">' + (avg != null && vals.length === gr.leaves.length ? 'average ' + avg.toFixed(0) + ' mm' : vals.length + ' of ' + gr.leaves.length) + '</span></div>';
      }).join('');
      plot.innerHTML = '<div class="fs-cp-axis"><span>0 mm</span><span>' + (MAX / 2) + ' mm</span><span>' + MAX + ' mm</span></div>' + all;
      $$('.fs-cp-picks .fs-in-chip', host).forEach(function (b) { var k = b.dataset.g + b.dataset.i; b.classList.toggle('done', !!got[k]); $('em', b).textContent = got[k] ? ' ' + S.groups.filter(function (gr) { return gr.k === b.dataset.g; })[0].leaves[+b.dataset.i] + ' mm' : ''; });
      var every = S.groups.every(function (gr) { return gr.leaves.every(function (mm, i) { return got[gr.k + i]; }); });
      if (every) ask();
    }
    function ask() {
      var q = $('.fs-cp-q', host); if (q.dataset.on) return; q.dataset.on = '1';
      q.innerHTML = '<div class="fs-in-k">' + esc(S.q.q) + '</div><div class="fs-in-chips">' + S.q.opts.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(o.t) + '</button>'; }).join('') + '</div>';
      $$('.fs-in-chip', q).forEach(function (c) { c.addEventListener('click', function () { var o = S.q.opts[+c.dataset.i];
        if (!o.ok) { bounce(c, $('.fs-cp-miss', host), o.why); return; } $('.fs-cp-miss', host).classList.remove('show');
        c.classList.add('on', 'ok'); var w = $('.fs-cp-win', host); w.innerHTML = esc(o.why); w.classList.add('show'); SFX.win(); toolDone(); }); });
    }
    $$('.fs-cp-picks .fs-in-chip', host).forEach(function (b) { b.addEventListener('click', function () {
      var gr = S.groups.filter(function (x) { return x.k === b.dataset.g; })[0], mm = gr.leaves[+b.dataset.i];
      $$('.fs-cp-picks .fs-in-chip', host).forEach(function (x) { x.classList.toggle('on', x === b); });
      leaf.style.width = (100 * mm / MAX * 330 / 400) + '%';
      setJaw(0, false); read.textContent = '0.0';
      setTimeout(function () { setJaw(mm, true); count(mm, 900); }, 60);
      SFX.blip(); setTimeout(function () { SFX.snap(); got[gr.k + b.dataset.i] = 1; store('calipers', JSON.stringify(got)); draw(); }, reduceMotion ? 0 : 950);
    }); });
    draw();
  };

  /* ----- light meter simulation (9.01): carry the meter to each place, read the number, compare -----
     T.lightmeter = {title, todo[], unit, places:[{k, icon, name, lux, show, note}], q:{q, opts:[{t, ok, why}]}} */
  SIMS.lightmeter = function (host, T) {
    var S = T.lightmeter, MAX = Math.max.apply(null, S.places.map(function (p) { return p.lux; }));
    host.innerHTML = '<div class="fs-game-k">Try it: a light meter</div><div class="fs-game-t">' + esc(S.title) + '</div>' +
      '<ul class="fs-todo">' + S.todo.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>' +
      '<div class="fs-lm-tool"><svg viewBox="0 0 150 230" class="fs-lm-svg" role="img" aria-label="A handheld light meter: a gray box with a white light sensor on top and a small screen that shows a number.">' +
      '<rect x="20" y="40" width="110" height="180" rx="16" fill="#3E4A52" stroke="#24313A" stroke-width="3"/>' +
      '<rect x="48" y="6" width="54" height="40" rx="8" fill="#5B6870" stroke="#24313A" stroke-width="3"/><ellipse cx="75" cy="18" rx="20" ry="9" fill="#F4F6F2" stroke="#B9C2C6" stroke-width="2"/>' +
      '<g class="fs-lm-rays"><path d="M75 -14v10M52 -8l6 8M98 -8l-6 8" stroke="#F2B630" stroke-width="3" stroke-linecap="round"/></g>' +
      '<rect x="34" y="62" width="82" height="44" rx="6" fill="#1D2B22"/><text class="fs-lm-read" x="75" y="92" text-anchor="middle" font-family="Courier New,monospace" font-size="20" font-weight="900" fill="#9EF0A8">0</text>' +
      '<text x="75" y="122" text-anchor="middle" font-family="Nunito,sans-serif" font-size="12" font-weight="900" fill="#DCE3E6">' + esc(S.unit || 'lux') + '</text>' +
      '<circle cx="55" cy="160" r="12" fill="#E07B2E"/><circle cx="95" cy="160" r="12" fill="#6E7A82"/><rect x="45" y="190" width="60" height="10" rx="5" fill="#24313A"/></svg>' +
      '<div class="fs-lm-places">' + S.places.map(function (p, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '"><span>' + p.icon + '</span> ' + esc(p.name) + '<em></em></button>'; }).join('') + '<div class="fs-lm-note"><em>Tap a place to carry the meter there.</em></div></div></div>' +
      '<div class="fs-lm-bars"></div><div class="fs-sv-q fs-lm-q"></div><div class="fs-miss fs-lm-miss"></div><div class="fs-win fs-lm-win"></div>';
    var read = $('.fs-lm-read', host), bars = $('.fs-lm-bars', host), noteBox = $('.fs-lm-note', host);
    var got = {}; try { got = JSON.parse(store('lightmeter') || '{}'); } catch (e) {}
    function fmt(n) { return n >= 1 ? Math.round(n).toLocaleString('en-US') : String(n); }
    function count(target) {
      if (reduceMotion) { read.textContent = fmt(target); return; }
      var t0 = performance.now(); (function f(t) { var k = Math.min(1, (t - t0) / 900); read.textContent = fmt(target < 1 ? target : target * k * k); if (k < 1) requestAnimationFrame(f); })(t0);
    }
    function draw() {
      bars.innerHTML = S.places.filter(function (p) { return got[p.k]; }).map(function (p) {
        return '<div class="fs-lm-row"><span class="fs-lm-rl">' + p.icon + ' ' + esc(p.name) + '</span><div class="fs-lm-line"><i style="width:' + Math.max(0.6, 100 * p.lux / MAX) + '%"></i></div><b>' + esc(p.show || fmt(p.lux)) + '</b></div>';
      }).join('');
      $$('.fs-lm-places .fs-in-chip', host).forEach(function (b) { var ok = !!got[S.places[+b.dataset.i].k]; b.classList.toggle('done', ok); $('em', b).textContent = ok ? ' ✓' : ''; });
      if (S.places.every(function (p) { return got[p.k]; })) ask();
    }
    function ask() {
      var q = $('.fs-lm-q', host); if (q.dataset.on) return; q.dataset.on = '1';
      q.innerHTML = '<div class="fs-in-k">' + esc(S.q.q) + '</div><div class="fs-in-chips">' + S.q.opts.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(o.t) + '</button>'; }).join('') + '</div>';
      $$('.fs-in-chip', q).forEach(function (c) { c.addEventListener('click', function () { var o = S.q.opts[+c.dataset.i];
        if (!o.ok) { bounce(c, $('.fs-lm-miss', host), o.why); return; } $('.fs-lm-miss', host).classList.remove('show');
        c.classList.add('on', 'ok'); var w = $('.fs-lm-win', host); w.innerHTML = esc(o.why); w.classList.add('show'); SFX.win(); store('lightmeter-q', '1'); toolDone(); }); });
      if (store('lightmeter-q')) { var i = S.q.opts.map(function (o, j) { return o.ok ? j : -1; }).filter(function (j) { return j > -1; })[0]; $$('.fs-in-chip', q)[i].classList.add('on', 'ok'); var w = $('.fs-lm-win', host); w.innerHTML = esc(S.q.opts[i].why); w.classList.add('show'); }
    }
    $$('.fs-lm-places .fs-in-chip', host).forEach(function (b) { b.addEventListener('click', function () {
      var p = S.places[+b.dataset.i];
      $$('.fs-lm-places .fs-in-chip', host).forEach(function (x) { x.classList.toggle('on', x === b); });
      host.style.setProperty('--fs-lm-glow', String(Math.max(0.08, Math.pow(p.lux / MAX, 0.35))));
      read.textContent = '0'; count(p.lux); SFX.blip();
      noteBox.innerHTML = '<b>' + p.icon + ' ' + esc(p.name) + ': about ' + esc(p.show || fmt(p.lux)) + ' ' + esc(S.unit || 'lux') + '.</b> ' + esc(p.note);
      setTimeout(function () { SFX.chime(); got[p.k] = 1; store('lightmeter', JSON.stringify(got)); draw(); }, reduceMotion ? 0 : 950);
    }); });
    draw();
  };

  /* ----- thermometer simulation ----- */
  /* ----- dip net (14.01): sweep three spots in a pond, look at the catch in a white tray, learn each young animal's life stage, then release ----- 
     T.dipnet = {title, todo[], parts:[{label,t}], spots:[{k,name,icon,where,catch:[critterId,...]}], critters:{id:{name,img,alt,stage,note}}, q:{q,opts:[{t,ok,why}]}, credit} */
  SIMS.dipnet = function (host, T) {
    var S = T.dipnet, swept = loadJ('dipnet', {}), seen = loadJ('dipnet-seen', {});
    host.innerHTML = '<div class="fs-game-k">Try it: pond sampling</div><div class="fs-game-t">' + esc(S.title) + '</div>' +
      '<ul class="fs-todo">' + S.todo.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>' +
      '<div class="fs-dn-parts">' + S.parts.map(function (p, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(p.label) + '</button>'; }).join('') + '</div>' +
      '<div class="fs-hs-card fs-dn-pinfo"><em>Tap a part of the dip net to learn what it does.</em></div>' +
      '<div class="fs-in-k">Pick a spot to sweep</div><div class="fs-dn-spots">' + S.spots.map(function (s, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '"><span>' + s.icon + '</span>' + esc(s.name) + '<em></em></button>'; }).join('') + '</div>' +
      '<div class="fs-dn-pond"><div class="fs-dn-water"><span class="fs-dn-net">🥅</span><div class="fs-dn-where">Pick a spot, then sweep.</div></div><button type="button" class="fs-btn fs-dn-go" disabled>🥅 Sweep the net</button></div>' +
      '<div class="fs-in-k">The sorting tray</div><div class="fs-dn-tray"><em>Your catch goes here. Tap each animal to find out what it is.</em></div>' +
      '<div class="fs-hs-card fs-dn-info"><em>Tap an animal in the tray.</em></div><div class="fs-sv-q fs-dn-q"></div><div class="fs-miss fs-dn-miss"></div><div class="fs-win fs-dn-win"></div>' +
      (S.credit ? '<details class="fs-credit fs-credit-fold"><summary>📷 Photo credits</summary>' + esc(S.credit) + '</details>' : '');
    var pinfo = $('.fs-dn-pinfo', host), info = $('.fs-dn-info', host), tray = $('.fs-dn-tray', host), go = $('.fs-dn-go', host), water = $('.fs-dn-water', host), spot = null;
    $$('.fs-dn-parts .fs-in-chip', host).forEach(function (c) { c.addEventListener('click', function () { var p = S.parts[+c.dataset.i]; c.classList.add('on'); pinfo.innerHTML = '<span class="fs-hs-n">🥅</span><div><b>' + esc(p.label) + '</b>' + esc(p.t) + '</div>'; SFX.blip(); }); });
    $$('.fs-dn-spots .fs-in-chip', host).forEach(function (c) { c.addEventListener('click', function () {
      spot = S.spots[+c.dataset.i]; $$('.fs-dn-spots .fs-in-chip', host).forEach(function (x) { x.classList.toggle('on', x === c); });
      $('.fs-dn-where', host).textContent = spot.icon + ' ' + spot.where; water.dataset.k = spot.k; go.disabled = false; SFX.blip(); }); });
    function drawTray() {
      var ids = []; S.spots.forEach(function (s) { if (swept[s.k]) s.catch.forEach(function (id) { if (ids.indexOf(id) < 0) ids.push(id); }); });
      if (!ids.length) return;
      tray.innerHTML = ids.map(function (id) { var c = S.critters[id]; return '<button type="button" class="fs-dn-crit' + (seen[id] ? ' seen' : '') + '" data-id="' + id + '"><img alt="' + esc(c.alt) + '" src="' + esc(c.img) + '"><span>' + (seen[id] ? esc(c.name) : '?') + '</span></button>'; }).join('');
      $$('.fs-dn-crit', tray).forEach(function (b) { b.addEventListener('click', function () {
        var c = S.critters[b.dataset.id]; seen[b.dataset.id] = 1; saveJ('dipnet-seen', seen); b.classList.add('seen'); $('span', b).textContent = c.name; SFX.chime();
        info.innerHTML = '<span class="fs-hs-n">🔎</span><div><b>' + esc(c.name) + ' <span class="fs-dn-stage">' + esc(c.stage) + '</span></b>' + esc(c.note) + '</div>'; info.classList.remove('flash'); void info.offsetWidth; info.classList.add('flash'); check(); }); });
    }
    function check() {
      S.spots.forEach(function (s, i) { var c = $$('.fs-dn-spots .fs-in-chip', host)[i]; c.classList.toggle('done', !!swept[s.k]); $('em', c).textContent = swept[s.k] ? ' ✓' : ''; });
      var all = S.spots.every(function (s) { return swept[s.k]; }) && Object.keys(S.critters).every(function (id) { return seen[id]; });
      if (all) ask();
    }
    go.addEventListener('click', function () {
      if (!spot) return; go.disabled = true; noise(0.6, 250, 1200, 0.25);
      water.classList.remove('sweep'); void water.offsetWidth; water.classList.add('sweep');
      setTimeout(function () { swept[spot.k] = 1; saveJ('dipnet', swept); go.disabled = false; drawTray(); check(); }, reduceMotion ? 0 : 1100);
    });
    function ask() {
      var q = $('.fs-dn-q', host); if (q.dataset.on) return; q.dataset.on = '1';
      q.innerHTML = '<div class="fs-in-k">' + esc(S.q.q) + '</div><div class="fs-in-chips">' + S.q.opts.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(o.t) + '</button>'; }).join('') + '</div>';
      $$('.fs-in-chip', q).forEach(function (c) { c.addEventListener('click', function () { var o = S.q.opts[+c.dataset.i];
        if (!o.ok) { bounce(c, $('.fs-dn-miss', host), o.why); return; } $('.fs-dn-miss', host).classList.remove('show');
        c.classList.add('on', 'ok'); var w = $('.fs-dn-win', host); w.innerHTML = esc(o.why); w.classList.add('show'); SFX.win(); toolDone(); }); });
    }
    drawTray(); check();
  };

  /* ----- core drill (15.01): drill three Florida spots, pull up a core of layers, tap each layer to read it, then answer one question -----
     T.coredrill = {title, todo[], parts:[{label, t}], sites:[{k, name, icon, where, layers:[{k, t, from, to, col, note}]}], deepest, need:{site, layer}, q:{q, opts:[{t, ok, why}]}} */
  /* =================== 16.01: tradeoffs (Gained or used up?, Load the scale, Strategy toolbox, Town hall) =================== */

  /* ---------- Warm-Up: "Gained or used up?" — pick an everyday activity, then sort each card into GAINED or USED UP (16.01) ----------
     D.twocol = {afterText, kicker, title, todo[], why, cols:[{k, icon, t}], items:[{id, icon, name, chips:[{id, t, side, miss}]}], q, opts, win, clue} */
  function buildTwocol() {
    var T = D.twocol; if (!T) return;
    var at = anchorP(T.afterText); if (!at) { FAILED.push('twocol anchor text not found'); return; }
    var g = gameShell(T.kicker || 'Warm-Up game', T.title, T.todo, T.why); g.dataset.mod = 'twocol';
    var st = loadJ('twocol', {}), cur = null;
    var pick = el('div', 'fs-gu-pick'), tray = el('div', 'fs-gu-tray'), cols = el('div', 'fs-gu-cols'), miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    T.items.forEach(function (it) { var b = el('button', 'fs-in-chip fs-gu-item', '<span>' + it.icon + '</span>' + esc(it.name) + '<em></em>'); b.type = 'button'; b.dataset.id = it.id; pick.appendChild(b); });
    T.cols.forEach(function (c) { var z = el('div', 'fs-gu-col', '<div class="fs-gu-h"><span>' + c.icon + '</span>' + esc(c.t) + '</div><ul></ul>'); z.dataset.k = c.k; cols.appendChild(z); });
    g.appendChild(el('div', 'fs-in-k', '1. Pick something you might do in the morning')); g.appendChild(pick);
    g.appendChild(el('div', 'fs-in-k fs-gu-k2', '2. Sort each card')); g.appendChild(tray); g.appendChild(cols);
    g.appendChild(miss); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    var zones = $$('.fs-gu-col', cols), total = 0; T.items.forEach(function (it) { total += it.chips.length; });
    function itemOf(id) { return T.items.filter(function (x) { return x.id === id; })[0]; }
    function addTo(it, ch, anim) {
      var li = el('li', anim && !reduceMotion ? 'pop' : '', '<span>' + it.icon + '</span>' + esc(ch.t)); $('ul', $('.fs-gu-col[data-k="' + ch.side + '"]', cols)).appendChild(li);
    }
    function show(it) {
      cur = it; tray.innerHTML = '';
      $$('.fs-gu-item', pick).forEach(function (b) { b.classList.toggle('on', b.dataset.id === it.id); });
      shuffle(it.chips).forEach(function (ch) { if (st[it.id + ':' + ch.id]) return; var k = el('div', 'fs-card fs-gu-card', '<span>' + it.icon + '</span> ' + esc(ch.t)); k.dataset.id = ch.id; tray.appendChild(k); dragDrop(k, function () { return zones; }, drop); });
      if (!tray.children.length) tray.appendChild(el('div', 'fs-gu-done', '✓ All sorted. Pick another one above.'));
    }
    function drop(k, z) {
      if (!cur) return; var ch = cur.chips.filter(function (x) { return x.id === k.dataset.id; })[0]; if (!ch) return;
      if (ch.side !== z.dataset.k) { bounce(k, miss, ch.miss); return; }
      miss.classList.remove('show'); st[cur.id + ':' + ch.id] = 1; saveJ('twocol', st); SFX.chime(); k.remove(); addTo(cur, ch, true);
      if (!$('.fs-gu-card', tray)) { tray.appendChild(el('div', 'fs-gu-done', '✓ All sorted. Pick another one above.')); }
      upd();
    }
    tapTargets(g, zones, drop);
    $$('.fs-gu-item', pick).forEach(function (b) { b.addEventListener('click', function () { show(itemOf(b.dataset.id)); SFX.blip(); }); });
    function upd() {
      var n = Object.keys(st).length;
      T.items.forEach(function (it) { var done = it.chips.every(function (ch) { return st[it.id + ':' + ch.id]; }); var b = $('.fs-gu-item[data-id="' + it.id + '"]', pick); b.classList.toggle('done', done); $('em', b).textContent = done ? ' ✓' : ''; });
      count.textContent = '⚖️ ' + n + ' of ' + total + ' cards sorted'; count.classList.toggle('ok', n === total);
      if (n === total) askOnce(qh, T.q, T.opts, 'twocol-q', win, T.win, T.clue, 'twocol', miss);
    }
    T.items.forEach(function (it) { it.chips.forEach(function (ch) { if (st[it.id + ':' + ch.id]) addTo(it, ch, false); }); });
    tray.appendChild(el('div', 'fs-gu-done', 'Pick one above to start.'));
    at.parentNode.insertBefore(g, at.nextSibling);
    upd();
  }

  /* ---------- Lesson Part 1: "Load the scale" — drag the benefits and costs of one plan onto a balance scale, then add protection strategies and watch the costs shrink (16.01) ----------
     D.scale = {replace | afterText, kicker, title, todo[], why, sides:{benefit:{icon,t}, cost:{icon,t}}, weights:[{id, icon, t, side, w, miss}], strategies:[{id, icon, t, lowers, to, why}], q, opts, credit, win, clue} */
  function buildScale() {
    var S = D.scale; if (!S) return;
    var wrap = S.replace ? $(S.replace) : null, at = wrap ? null : anchorP(S.afterText);
    if (!wrap && !at) { FAILED.push('scale: no anchor'); return; }
    if (at && at.nextElementSibling && at.nextElementSibling.tagName === 'UL') at = at.nextElementSibling;
    var g = gameShell(S.kicker || 'Lesson game', S.title, S.todo, S.why); g.dataset.mod = 'scale';
    var st = loadJ('scale', { on: {}, str: {} });
    var stage = el('div', 'fs-bal-stage', '<div class="fs-bal-post"></div><div class="fs-bal-beam"><i></i></div>' +
      ['benefit', 'cost'].map(function (k) { return '<div class="fs-bal-pan" data-k="' + k + '"><div class="fs-bal-cord"></div><div class="fs-bal-dish"><div class="fs-bal-h"><span>' + S.sides[k].icon + '</span>' + esc(S.sides[k].t) + '</div><div class="fs-bal-load"><em>Drop here</em></div></div></div>'; }).join('') +
      '<div class="fs-bal-base"></div>');
    var tray = el('div', 'fs-bal-tray'), miss = el('div', 'fs-miss'), read = el('div', 'fs-bal-read'), strat = el('div', 'fs-bal-strat'), info = el('div', 'fs-hs-card fs-bal-info'), qh = el('div'), win = el('div', 'fs-win');
    shuffle(S.weights).forEach(function (w) { var k = el('div', 'fs-card fs-bal-w', '<span>' + w.icon + '</span> ' + esc(w.t) + ' <b class="fs-bal-kg">' + '●'.repeat(w.w) + '</b>'); k.dataset.id = w.id; tray.appendChild(k); });
    g.appendChild(stage); g.appendChild(read); g.appendChild(tray); g.appendChild(miss); g.appendChild(strat); g.appendChild(info); g.appendChild(qh); g.appendChild(win);
    if (S.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📚 Where these facts come from</summary>' + esc(S.credit)));
    var pans = $$('.fs-bal-pan', stage), beam = $('.fs-bal-beam', stage);
    function wOf(id) { return S.weights.filter(function (x) { return x.id === id; })[0]; }
    function weightNow(w) { var s = S.strategies.filter(function (x) { return x.lowers === w.id && st.str[x.id]; })[0]; return s ? s.to : w.w; }
    function sum(side) { return S.weights.filter(function (w) { return w.side === side && st.on[w.id]; }).reduce(function (a, w) { return a + weightNow(w); }, 0); }
    function draw(anim) {
      ['benefit', 'cost'].forEach(function (k) {
        var load = $('.fs-bal-load', $('.fs-bal-pan[data-k="' + k + '"]', stage)), ws = S.weights.filter(function (w) { return w.side === k && st.on[w.id]; });
        load.innerHTML = ws.length ? ws.map(function (w) { var n = weightNow(w), lowered = n < w.w; return '<div class="fs-bal-blk' + (lowered ? ' low' : '') + '"><span>' + w.icon + '</span> ' + esc(w.t) + ' <b class="fs-bal-kg">' + '●'.repeat(n) + '</b>' + (lowered ? ' <small>🛡️ lowered</small>' : '') + '</div>'; }).join('') : '<em>Drop here</em>';
      });
      var b = sum('benefit'), c = sum('cost'), ang = Math.max(-12, Math.min(12, (c - b) * 2.4));
      beam.style.transform = 'rotate(' + ang + 'deg)';
      var dy = Math.round(Math.sin(ang * Math.PI / 180) * 150);
      pans[0].style.transform = 'translateY(' + (-dy) + 'px)'; pans[1].style.transform = 'translateY(' + dy + 'px)';
      var hmax = Math.max(pans[0].offsetHeight, pans[1].offsetHeight); if (hmax) stage.style.height = (hmax + 33 + Math.abs(dy) + 34) + 'px';
      var placed = S.weights.every(function (w) { return st.on[w.id]; });
      read.innerHTML = '<span>👍 ' + esc(S.sides.benefit.t) + ': <b>' + b + '</b></span><span>' + (Math.abs(b - c) < 1 ? '⚖️ About even' : b > c ? '⬅ Tips toward the benefits' : 'Tips toward the costs ➡') + '</span><span>🌫️ ' + esc(S.sides.cost.t) + ': <b>' + c + '</b></span>';
      if (placed) stepTwo();
    }
    function drop(k, z) {
      var w = wOf(k.dataset.id); if (!w || st.on[w.id]) return;
      if (w.side !== z.dataset.k) { bounce(k, miss, w.miss); return; }
      miss.classList.remove('show'); st.on[w.id] = 1; saveJ('scale', st); SFX.thud(); k.remove(); draw(true);
    }
    $$('.fs-bal-w', tray).forEach(function (k) { if (st.on[k.dataset.id]) { k.remove(); return; } dragDrop(k, function () { return pans; }, drop); });
    tapTargets(g, pans, drop);
    function stepTwo() {
      if (strat.dataset.on) { upd2(); return; } strat.dataset.on = '1';
      strat.innerHTML = '<div class="fs-in-k">Now add a protection strategy. Tap each one.</div><div class="fs-in-chips">' + S.strategies.map(function (s) { return '<button type="button" class="fs-in-chip" data-id="' + s.id + '"><span>' + s.icon + '</span> ' + esc(s.t) + '</button>'; }).join('') + '</div>';
      $$('.fs-in-chip', strat).forEach(function (c) { c.addEventListener('click', function () {
        var s = S.strategies.filter(function (x) { return x.id === c.dataset.id; })[0]; if (st.str[s.id]) return;
        st.str[s.id] = 1; saveJ('scale', st); SFX.chime(); show(s, true); draw(true);
      }); });
      upd2();
    }
    function show(s, anim) { info.innerHTML = '<span class="fs-hs-n">🛡️</span><div><b>' + esc(s.t) + '</b>' + esc(s.why) + '</div>'; if (anim && !reduceMotion) { info.classList.remove('flash'); void info.offsetWidth; info.classList.add('flash'); } }
    function upd2() {
      $$('.fs-in-chip', strat).forEach(function (c) { c.classList.toggle('on', !!st.str[c.dataset.id]); c.classList.toggle('ok', !!st.str[c.dataset.id]); });
      if (S.strategies.every(function (s) { return st.str[s.id]; })) askOnce(qh, S.q, S.opts, 'scale-q', win, S.win, S.clue, 'scale', miss);
    }
    if (wrap) { wrap.parentNode.insertBefore(g, wrap); wrap.classList.add('fs-hide-on'); } else at.parentNode.insertBefore(g, at.nextSibling);
    draw(false);
    var last = S.strategies.filter(function (s) { return st.str[s.id]; }).pop(); if (last) show(last, false);
    if (window.IntersectionObserver) new IntersectionObserver(function (es) { if (es[0].isIntersecting) draw(false); }).observe(stage);
  }

  /* ---------- Lesson Part 2: "Strategy toolbox" — drop each real action into the drawer for its kind of protection strategy; round 2 is the case (16.01) ----------
     D.toolbox = {afterText, kicker, title, todo[], why, kinds:[{k, icon, t, sub}], rounds:[{title, cards:[{id, icon, t, k, why, miss}]}], q, opts, win, clue} */
  function buildToolbox() {
    var T = D.toolbox; if (!T) return;
    var at = anchorP(T.afterText); if (!at) { FAILED.push('toolbox anchor text not found'); return; }
    if (at.nextElementSibling && at.nextElementSibling.tagName === 'UL') at = at.nextElementSibling;
    var g = gameShell(T.kicker || 'Lesson game', T.title, T.todo, T.why); g.dataset.mod = 'toolbox';
    var st = loadJ('toolbox', {});
    var box = el('div', 'fs-tb-box'), rh = el('div', 'fs-tb-round'), tray = el('div', 'fs-tb-tray'), miss = el('div', 'fs-miss'), info = el('div', 'fs-hs-card fs-tb-info', '<em>Drop a card in a drawer to learn about it.</em>'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    T.kinds.forEach(function (kd) { var d = el('div', 'fs-tb-drawer', '<div class="fs-tb-h"><span>' + kd.icon + '</span><b>' + esc(kd.t) + '</b><small>' + esc(kd.sub) + '</small></div><ul></ul>'); d.dataset.k = kd.k; box.appendChild(d); });
    g.appendChild(rh); g.appendChild(tray); g.appendChild(box); g.appendChild(miss); g.appendChild(info); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    var drawers = $$('.fs-tb-drawer', box), all = [], r = 0;
    T.rounds.forEach(function (rd) { all = all.concat(rd.cards); });
    function cardOf(id) { return all.filter(function (x) { return x.id === id; })[0]; }
    function put(c, anim) { var li = el('li', anim && !reduceMotion ? 'pop' : '', '<span>' + c.icon + '</span>' + esc(c.t)); $('ul', $('.fs-tb-drawer[data-k="' + c.k + '"]', box)).appendChild(li); }
    function round() {
      r = 0; while (r < T.rounds.length && T.rounds[r].cards.every(function (c) { return st[c.id]; })) r++;
      tray.innerHTML = '';
      if (r >= T.rounds.length) { rh.innerHTML = '<b>✓ Every card is in its drawer.</b>'; return; }
      rh.innerHTML = '<span class="fs-tb-rn">Round ' + (r + 1) + ' of ' + T.rounds.length + '</span> ' + esc(T.rounds[r].title);
      shuffle(T.rounds[r].cards).forEach(function (c) { if (st[c.id]) return; var k = el('div', 'fs-card fs-tb-card', '<span>' + c.icon + '</span> ' + esc(c.t)); k.dataset.id = c.id; tray.appendChild(k); dragDrop(k, function () { return drawers; }, drop); });
    }
    function drop(k, d) {
      var c = cardOf(k.dataset.id); if (!c || st[c.id]) return;
      if (c.k !== d.dataset.k) { bounce(k, miss, c.miss); return; }
      miss.classList.remove('show'); st[c.id] = 1; saveJ('toolbox', st); SFX.chime(); k.remove(); put(c, true);
      var kd = T.kinds.filter(function (x) { return x.k === c.k; })[0];
      info.innerHTML = '<span class="fs-hs-n">' + kd.icon + '</span><div><b>' + esc(kd.t) + ': ' + esc(c.t) + '</b>' + esc(c.why) + '</div>'; if (!reduceMotion) { info.classList.remove('flash'); void info.offsetWidth; info.classList.add('flash'); }
      if (!$('.fs-tb-card', tray)) setTimeout(round, reduceMotion ? 0 : 500);
      upd();
    }
    tapTargets(g, drawers, drop);
    function upd() {
      var n = all.filter(function (c) { return st[c.id]; }).length;
      count.textContent = '🧰 ' + n + ' of ' + all.length + ' cards in the toolbox'; count.classList.toggle('ok', n === all.length);
      if (n === all.length) askOnce(qh, T.q, T.opts, 'toolbox-q', win, T.win, T.clue, 'toolbox', miss);
    }
    all.forEach(function (c) { if (st[c.id]) put(c, false); });
    at.parentNode.insertBefore(g, at.nextSibling);
    round(); upd();
  }

  /* ---------- Lesson Part 4: "Town hall" — stamp each neighbor's comment as a benefit, a cost or a protection strategy, then match each strategy to the cost it lowers (16.01) ----------
     D.townhall = {afterText, kicker, title, todo[], why, tags:[{k, icon, t}], comments:[{id, who, icon, t, tag, miss, lowers}], matchQ, q, opts, win, clue} */
  function buildTownhall() {
    var T = D.townhall; if (!T) return;
    var at = anchorP(T.afterText); if (!at) { FAILED.push('townhall anchor text not found'); return; }
    var g = gameShell(T.kicker || 'Lesson game', T.title, T.todo, T.why); g.dataset.mod = 'townhall';
    var st = loadJ('townhall', { tag: {}, match: {} });
    var wall = el('div', 'fs-th2-wall'), miss = el('div', 'fs-miss'), step2 = el('div', 'fs-th2-step2'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    T.comments.forEach(function (c) {
      var k = el('div', 'fs-th2-card', '<div class="fs-th2-who"><span>' + c.icon + '</span>' + esc(c.who) + '</div><p>“' + esc(c.t) + '”</p><div class="fs-th2-tags">' + T.tags.map(function (tg) { return '<button type="button" class="fs-th2-tag" data-k="' + tg.k + '">' + tg.icon + ' ' + esc(tg.t) + '</button>'; }).join('') + '</div><div class="fs-th2-stamp"></div><div class="fs-th2-fix"></div>');
      k.dataset.id = c.id; wall.appendChild(k);
    });
    g.appendChild(wall); g.appendChild(miss); g.appendChild(count); g.appendChild(step2); g.appendChild(qh); g.appendChild(win);
    function cOf(id) { return T.comments.filter(function (x) { return x.id === id; })[0]; }
    function tagOf(k) { return T.tags.filter(function (x) { return x.k === k; })[0]; }
    function stamp(c, anim) {
      var k = $('.fs-th2-card[data-id="' + c.id + '"]', wall), tg = tagOf(c.tag); k.classList.add('done', 'is-' + c.tag); if (anim && !reduceMotion) k.classList.add('pop');
      $('.fs-th2-stamp', k).innerHTML = tg.icon + ' ' + esc(tg.t);
    }
    $$('.fs-th2-tag', wall).forEach(function (b) { b.addEventListener('click', function () {
      var k = b.closest('.fs-th2-card'), c = cOf(k.dataset.id); if (st.tag[c.id]) return;
      if (b.dataset.k !== c.tag) { bounce(b, miss, c.miss); return; }
      miss.classList.remove('show'); st.tag[c.id] = 1; saveJ('townhall', st); SFX.chime(); stamp(c, true); upd();
    }); });
    var strats = T.comments.filter(function (c) { return c.lowers; });
    function fixed(s, anim) {
      var k = $('.fs-th2-card[data-id="' + s.lowers + '"]', wall); $('.fs-th2-fix', k).innerHTML = '🛡️ Lowered by: ' + esc(s.who); k.classList.add('fixed'); if (anim && !reduceMotion) { k.classList.remove('pop'); void k.offsetWidth; k.classList.add('pop'); }
      var t = $('.fs-th2-s[data-id="' + s.id + '"]', step2); if (t) t.remove();
    }
    function drop(t, z) {
      var s = cOf(t.dataset.id); if (!s || st.match[s.id]) return;
      if (z.dataset.id !== s.lowers) { var c = cOf(z.dataset.id); bounce(t, miss, c && c.tag !== 'cost' ? 'Drop it on a cost card (the ones stamped 🌫️).' : s.matchMiss); return; }
      miss.classList.remove('show'); st.match[s.id] = 1; saveJ('townhall', st); SFX.chime(); fixed(s, true); upd();
    }
    function showStep2() {
      if (step2.dataset.on) return; step2.dataset.on = '1';
      step2.innerHTML = '<div class="fs-in-k">' + esc(T.matchQ) + '</div><div class="fs-th2-tray"></div>';
      var tray = $('.fs-th2-tray', step2), zones = $$('.fs-th2-card', wall).filter(function (k) { return cOf(k.dataset.id).tag === 'cost'; });
      strats.forEach(function (s) { if (st.match[s.id]) return; var t = el('div', 'fs-card fs-th2-s', '<span>' + s.icon + '</span> ' + esc(s.who) + ': ' + esc(s.short || s.t)); t.dataset.id = s.id; tray.appendChild(t); dragDrop(t, function () { return zones; }, drop); });
      tapTargets(g, zones, drop);
    }
    function upd() {
      var nt = Object.keys(st.tag).length, nm = Object.keys(st.match).length;
      count.textContent = '🗳️ ' + nt + ' of ' + T.comments.length + ' comments stamped' + (nt === T.comments.length ? ' · ' + nm + ' of ' + strats.length + ' strategies matched' : '');
      count.classList.toggle('ok', nt === T.comments.length && nm === strats.length);
      if (nt === T.comments.length) showStep2();
      if (nt === T.comments.length && nm === strats.length) askOnce(qh, T.q, T.opts, 'townhall-q', win, T.win, T.clue, 'townhall', miss);
    }
    T.comments.forEach(function (c) { if (st.tag[c.id]) stamp(c, false); });
    at.parentNode.insertBefore(g, at.nextSibling);
    upd();
    strats.forEach(function (s) { if (st.match[s.id]) fixed(s, false); });
  }

  /* ---------- Tool of the Week: a home water meter (16.01) ----------
     T.watermeter = {title, todo[], parts:[{label, t}], perTurn, uses:[{k, icon, name, gal, leak, note}], q:{q, opts:[{t, ok, why}]}} */
  SIMS.watermeter = function (host, T) {
    var S = T.watermeter, done = loadJ('watermeter', {}), total = 0, busy = false, per = S.perTurn || 10;
    S.uses.forEach(function (u) { if (done[u.k]) total += u.gal; });
    var max = Math.max.apply(null, S.uses.map(function (u) { return u.gal; }));
    host.innerHTML = '<div class="fs-game-k">Try it: a water meter</div><div class="fs-game-t">' + esc(S.title) + '</div>' +
      '<ul class="fs-todo">' + S.todo.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>' +
      '<div class="fs-dn-parts fs-wm-parts">' + S.parts.map(function (p, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(p.label) + '</button>'; }).join('') + '</div>' +
      '<div class="fs-hs-card fs-wm-pinfo"><em>Tap a part of the meter to learn what it does.</em></div>' +
      '<div class="fs-wm-row"><div class="fs-wm-meter"><svg viewBox="0 0 220 220" role="img" aria-label="A water meter: a counter in gallons, a big sweep hand and a small leak triangle.">' +
        '<circle cx="110" cy="110" r="104" fill="#3B4A52"/><circle cx="110" cy="110" r="94" fill="#F7F4EC" stroke="#9AA7AD" stroke-width="3"/>' +
        Array.apply(null, Array(10)).map(function (_, i) { var a = i * 36 * Math.PI / 180; return '<line x1="' + (110 + Math.sin(a) * 80) + '" y1="' + (110 - Math.cos(a) * 80) + '" x2="' + (110 + Math.sin(a) * 90) + '" y2="' + (110 - Math.cos(a) * 90) + '" stroke="#55646A" stroke-width="3"/><text x="' + (110 + Math.sin(a) * 68) + '" y="' + (114 - Math.cos(a) * 68) + '" text-anchor="middle" font-size="12" font-weight="800" fill="#55646A">' + i + '</text>'; }).join('') +
        '<rect x="62" y="54" width="96" height="26" rx="4" fill="#1E2B30"/><text class="fs-wm-odo" x="110" y="73" text-anchor="middle" font-size="17" font-weight="900" fill="#F2F5F6" font-family="monospace">00000</text>' +
        '<text x="110" y="94" text-anchor="middle" font-size="10" font-weight="900" fill="#55646A">GALLONS</text>' +
        '<g class="fs-wm-leak" transform="translate(110 150)"><polygon points="0,-11 10,7 -10,7" fill="#D9342B"/></g>' +
        '<g class="fs-wm-hand"><line x1="110" y1="110" x2="110" y2="30" stroke="#D9342B" stroke-width="4" stroke-linecap="round"/><circle cx="110" cy="110" r="7" fill="#D9342B"/></g>' +
      '</svg></div><div class="fs-wm-side"><div class="fs-in-k">Run water and watch the meter</div><div class="fs-wm-uses">' +
        S.uses.map(function (u, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '"><span>' + u.icon + '</span>' + esc(u.name) + '<em></em></button>'; }).join('') + '</div>' +
        '<div class="fs-hs-card fs-wm-info"><em>Pick one to run it.</em></div></div></div>' +
      '<div class="fs-in-k">Gallons used</div><div class="fs-wm-bars">' + S.uses.map(function (u) { return '<div class="fs-wm-bar" data-k="' + u.k + '"><span>' + u.icon + ' ' + esc(u.name) + '</span><i><b></b></i><em></em></div>'; }).join('') + '</div>' +
      '<div class="fs-sv-q fs-wm-q"></div><div class="fs-miss fs-wm-miss"></div><div class="fs-win fs-wm-win"></div>';
    var odo = $('.fs-wm-odo', host), hand = $('.fs-wm-hand', host), leak = $('.fs-wm-leak', host), info = $('.fs-wm-info', host);
    function setMeter(g) { odo.textContent = ('00000' + Math.floor(g)).slice(-5); hand.setAttribute('transform', 'rotate(' + ((g % per) / per * 360) + ' 110 110)'); }
    function bars() { S.uses.forEach(function (u) { var b = $('.fs-wm-bar[data-k="' + u.k + '"]', host); $('b', b).style.width = (done[u.k] ? Math.max(1.5, 100 * Math.sqrt(u.gal / max)) : 0) + '%'; $('em', b).textContent = done[u.k] ? 'about ' + u.gal.toLocaleString() + ' gal' : '—'; }); }
    $$('.fs-wm-parts .fs-in-chip', host).forEach(function (c) { c.addEventListener('click', function () { var p = S.parts[+c.dataset.i]; c.classList.add('on'); $('.fs-wm-pinfo', host).innerHTML = '<span class="fs-hs-n">🔎</span><div><b>' + esc(p.label) + '</b>' + esc(p.t) + '</div>'; SFX.blip(); }); });
    $$('.fs-wm-uses .fs-in-chip', host).forEach(function (c) { c.addEventListener('click', function () {
      if (busy) return; var u = S.uses[+c.dataset.i]; SFX.blip();
      if (done[u.k]) { $$('.fs-wm-uses .fs-in-chip', host).forEach(function (x) { x.classList.toggle('on', x === c); }); info.innerHTML = '<span class="fs-hs-n">' + u.icon + '</span><div><b>' + esc(u.name) + ': about ' + u.gal.toLocaleString() + ' gallons</b>' + esc(u.note) + '</div>'; return; }
      busy = true;
      $$('.fs-wm-uses .fs-in-chip', host).forEach(function (x) { x.classList.toggle('on', x === c); });
      info.innerHTML = '<span class="fs-hs-n">' + u.icon + '</span><div><b>' + esc(u.name) + '</b>Watch the meter…</div>';
      leak.classList.add('spin'); var from = total, to = total + u.gal, t0 = performance.now(), dur = reduceMotion ? 0 : 1800;
      noise(dur / 1000 || .2, 900, 3200, .12);
      function step(now) {
        var p = dur ? Math.min(1, (now - t0) / dur) : 1;
        setMeter(from + u.gal * p);
        if (p < 1) { requestAnimationFrame(step); return; }
        leak.classList.remove('spin'); busy = false;
        done[u.k] = 1; saveJ('watermeter', done); total = to; SFX.chime();
        setMeter(total); c.classList.add('done'); $('em', c).textContent = ' ✓';
        info.innerHTML = '<span class="fs-hs-n">' + u.icon + '</span><div><b>' + esc(u.name) + ': about ' + u.gal.toLocaleString() + ' gallons</b>' + esc(u.note) + '</div>';
        bars(); check();
      }
      requestAnimationFrame(step);
    }); });
    function check() { if (S.uses.every(function (u) { return done[u.k]; })) ask(); }
    function ask() {
      var q = $('.fs-wm-q', host); if (q.dataset.on) return; q.dataset.on = '1';
      q.innerHTML = '<div class="fs-in-k">' + esc(S.q.q) + '</div><div class="fs-in-chips">' + S.q.opts.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(o.t) + '</button>'; }).join('') + '</div>';
      $$('.fs-in-chip', q).forEach(function (c) { c.addEventListener('click', function () { var o = S.q.opts[+c.dataset.i];
        if (!o.ok) { bounce(c, $('.fs-wm-miss', host), o.why); return; } $('.fs-wm-miss', host).classList.remove('show');
        c.classList.add('on', 'ok'); var w = $('.fs-wm-win', host); w.innerHTML = esc(o.why); w.classList.add('show'); SFX.win(); store('watermeter-q', '1'); toolDone(); }); });
      if (store('watermeter-q')) { var i = S.q.opts.map(function (o, j) { return o.ok ? j : -1; }).filter(function (j) { return j > -1; })[0]; $$('.fs-in-chip', q)[i].classList.add('on', 'ok'); var w = $('.fs-wm-win', host); w.innerHTML = esc(S.q.opts[i].why); w.classList.add('show'); }
    }
    S.uses.forEach(function (u, i) { if (done[u.k]) { var c = $$('.fs-wm-uses .fs-in-chip', host)[i]; c.classList.add('done'); $('em', c).textContent = ' ✓'; } });
    setMeter(total); bars(); check();
  };

  /* =================== 16.02: engineering (Limit or goal?, Build the matrix, Make it better, Test it small) =================== */

  /* ---------- Warm-Up: "Limit or goal?" — one card at a time: a limit is a yes-or-no gate, a goal gets scored (16.02) ----------
     D.limits = {afterText, kicker, title, todo[], why, zones:{limit:{icon,t,sub}, goal:{icon,t,sub}}, cards:[{id, icon, t, k, why, miss}], q, opts, win, clue} */
  function buildLimits() {
    var T = D.limits; if (!T) return;
    var at = anchorP(T.afterText); if (!at) { FAILED.push('limits anchor text not found'); return; }
    if (at.nextElementSibling && at.nextElementSibling.tagName === 'UL') at = at.nextElementSibling;
    var g = gameShell(T.kicker || 'Warm-Up game', T.title, T.todo, T.why); g.dataset.mod = 'limits';
    var st = loadJ('limits', {});
    var board = el('div', 'fs-lq-board'), deck = el('div', 'fs-lq-deck'), miss = el('div', 'fs-miss'), info = el('div', 'fs-hs-card fs-lq-info', '<em>Sort the first card.</em>'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    ['limit', 'goal'].forEach(function (k) { var z = T.zones[k]; var d = el('div', 'fs-lq-zone', '<div class="fs-lq-h"><span>' + z.icon + '</span><b>' + esc(z.t) + '</b><small>' + esc(z.sub) + '</small></div><ul></ul>'); d.dataset.k = k; board.appendChild(d); });
    g.appendChild(deck); g.appendChild(board); g.appendChild(miss); g.appendChild(info); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    var zones = $$('.fs-lq-zone', board), order = T.cards.slice();
    function put(c, anim) { $('ul', $('.fs-lq-zone[data-k="' + c.k + '"]', board)).appendChild(el('li', anim && !reduceMotion ? 'pop' : '', '<span>' + c.icon + '</span>' + esc(c.t))); }
    function next() {
      deck.innerHTML = ''; var left = order.filter(function (c) { return !st[c.id]; });
      if (!left.length) { deck.appendChild(el('div', 'fs-lq-done', '✓ The brief is sorted.')); return; }
      var c = left[0], n = order.length - left.length + 1;
      var k = el('div', 'fs-card fs-lq-card', '<small>Card ' + n + ' of ' + order.length + '</small><span>' + c.icon + '</span> ' + esc(c.t)); k.dataset.id = c.id; deck.appendChild(k);
      if (!reduceMotion) k.classList.add('in');
      dragDrop(k, function () { return zones; }, drop);
    }
    function drop(k, z) {
      var c = order.filter(function (x) { return x.id === k.dataset.id; })[0]; if (!c || st[c.id]) return;
      if (c.k !== z.dataset.k) { bounce(k, miss, c.miss); return; }
      miss.classList.remove('show'); st[c.id] = 1; saveJ('limits', st); SFX.chime(); put(c, true);
      var zz = T.zones[c.k]; info.innerHTML = '<span class="fs-hs-n">' + zz.icon + '</span><div><b>' + esc(c.t) + '</b>' + esc(c.why) + '</div>'; if (!reduceMotion) { info.classList.remove('flash'); void info.offsetWidth; info.classList.add('flash'); }
      next(); upd();
    }
    tapTargets(g, zones, drop);
    zones.forEach(function (z) { z.addEventListener('click', function () { var k = $('.fs-lq-card', deck); if (k && !$('.sel', g)) { k.classList.add('sel'); drop(k, z); } }); });
    function upd() {
      var n = Object.keys(st).length; count.textContent = '🗂️ ' + n + ' of ' + order.length + ' cards sorted'; count.classList.toggle('ok', n === order.length);
      if (n === order.length) askOnce(qh, T.q, T.opts, 'limits-q', win, T.win, T.clue, 'limits', miss);
    }
    order.forEach(function (c) { if (st[c.id]) put(c, false); });
    at.parentNode.insertBefore(g, at.nextSibling);
    next(); upd();
  }

  /* ---------- Lesson Part 2: "Build the matrix" — tap each cell, read the evidence, give 1–3 stars; then check the limit and rule out a design (16.02) ----------
     D.matrix = {replace | afterSel | afterText, kicker, title, todo[], why, designs:[{id, icon, t}], rows:[{id, icon, t}], cells:{design:{row:{stars, fact}}}, limit:{icon, t, check, values:{design:{t, ok}}}, q, opts, credit, win, clue} */
  function buildMatrix() {
    var M = D.matrix; if (!M) return;
    var wrap = M.replace ? $(M.replace) : null, at = wrap ? null : (M.afterSel ? $(M.afterSel) : anchorP(M.afterText));
    if (!wrap && !at) { FAILED.push('matrix: no anchor'); return; }
    var g = gameShell(M.kicker || 'Lesson game', M.title, M.todo, M.why); g.dataset.mod = 'matrix';
    var st = loadJ('matrix', { c: {}, lim: 0 }), cur = null;
    var tbl = el('div', 'fs-mx-wrap'), panel = el('div', 'fs-mx-panel', '<em>Tap a ? box in the matrix to read its evidence.</em>'), miss = el('div', 'fs-miss'), lim = el('div', 'fs-mx-lim'), qh = el('div'), win = el('div', 'fs-win');
    function stars(n) { return '⭐'.repeat(n); }
    function total(d) { return M.rows.reduce(function (a, r) { return a + (st.c[d.id + ':' + r.id] ? M.cells[d.id][r.id].stars : 0); }, 0); }
    function draw() {
      var all = M.designs.every(function (d) { return M.rows.every(function (r) { return st.c[d.id + ':' + r.id]; }); });
      var h = '<table class="fs-mx"><thead><tr><th></th>' + M.designs.map(function (d) { var out = st.lim && !M.limit.values[d.id].ok; return '<th class="' + (out ? 'out' : '') + '"><span>' + d.icon + '</span>' + esc(d.t) + '</th>'; }).join('') + '</tr></thead><tbody>' +
        M.rows.map(function (r) { return '<tr><th><span>' + r.icon + '</span>' + esc(r.t) + '</th>' + M.designs.map(function (d) { var k = d.id + ':' + r.id, done = st.c[k], out = st.lim && !M.limit.values[d.id].ok; return '<td class="' + (out ? 'out' : '') + '"><button type="button" class="fs-mx-cell' + (done ? ' done' : '') + (cur === k ? ' on' : '') + '" data-k="' + k + '">' + (done ? stars(M.cells[d.id][r.id].stars) : '?') + '</button></td>'; }).join('') + '</tr>'; }).join('') +
        '<tr class="fs-mx-tot"><th>Total</th>' + M.designs.map(function (d) { var out = st.lim && !M.limit.values[d.id].ok; return '<td class="' + (out ? 'out' : '') + '">' + (all ? total(d) + ' ⭐' : '…') + '</td>'; }).join('') + '</tr>' +
        (st.lim ? '<tr class="fs-mx-limrow"><th><span>' + M.limit.icon + '</span>' + esc(M.limit.t) + '</th>' + M.designs.map(function (d) { var v = M.limit.values[d.id]; return '<td class="' + (v.ok ? 'ok' : 'out') + '">' + (v.ok ? '✅ ' : '❌ ') + esc(v.t) + (v.ok ? '' : '<b>OUT</b>') + '</td>'; }).join('') + '</tr>' : '') + '</tbody></table>';
      tbl.innerHTML = h;
      $$('.fs-mx-cell', tbl).forEach(function (b) { b.addEventListener('click', function () { open(b.dataset.k); }); });
      if (all && !st.lim) { lim.innerHTML = '<button type="button" class="fs-btn">' + M.limit.icon + ' ' + esc(M.limit.check) + '</button>'; $('button', lim).addEventListener('click', function () { st.lim = 1; saveJ('matrix', st); SFX.stamp(); lim.innerHTML = ''; draw(); }); }
      if (st.lim) askOnce(qh, M.q, M.opts, 'matrix-q', win, M.win, M.clue, 'matrix', miss);
    }
    function open(k) {
      cur = k; var p = k.split(':'), d = M.designs.filter(function (x) { return x.id === p[0]; })[0], r = M.rows.filter(function (x) { return x.id === p[1]; })[0], c = M.cells[p[0]][p[1]];
      panel.innerHTML = '<div class="fs-mx-ev"><b>' + d.icon + ' ' + esc(d.t) + ' · ' + r.icon + ' ' + esc(r.t) + '</b><p>📄 ' + esc(c.fact) + '</p></div>' +
        (st.c[k] ? '<div class="fs-mx-got">You gave it ' + stars(c.stars) + '</div>' : '<div class="fs-in-k">How well does it meet this goal?</div><div class="fs-in-chips">' + [1, 2, 3].map(function (n) { return '<button type="button" class="fs-in-chip" data-n="' + n + '">' + stars(n) + ' ' + ['Poor', 'OK', 'Great'][n - 1] + '</button>'; }).join('') + '</div>');
      $$('.fs-in-chip', panel).forEach(function (b) { b.addEventListener('click', function () {
        if (+b.dataset.n !== c.stars) { bounce(b, miss, (+b.dataset.n > c.stars ? 'Too many stars? ' : 'Too few stars? ') + 'Read the evidence again: does it meet the goal well, just OK, or poorly?'); return; }
        miss.classList.remove('show'); st.c[k] = 1; saveJ('matrix', st); SFX.chime(); open(k); draw();
        var nxt = null; M.rows.some(function (rr) { return M.designs.some(function (dd) { if (!st.c[dd.id + ':' + rr.id]) { nxt = dd.id + ':' + rr.id; return true; } }); });
        if (nxt) setTimeout(function () { if (cur === k) open(nxt); draw(); }, reduceMotion ? 0 : 900);
      }); });
      draw(); if (!reduceMotion) { panel.classList.remove('flash'); void panel.offsetWidth; panel.classList.add('flash'); }
    }
    g.appendChild(tbl); g.appendChild(panel); g.appendChild(miss); g.appendChild(lim); g.appendChild(qh); g.appendChild(win);
    if (M.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📚 Where these facts come from</summary>' + esc(M.credit)));
    if (wrap) { wrap.parentNode.insertBefore(g, wrap); wrap.classList.add('fs-hide-on'); } else at.parentNode.insertBefore(g, at.nextSibling);
    draw();
  }

  /* ---------- Lesson Part 2b: "Make it better" — start from a tied design, add features from the others, keep every goal at 2+ stars and stay inside the budget (16.02) ----------
     D.improve = {afterText, kicker, title, todo[], why, budget, unit, rows:[{id, icon, t}], bases:[{id, icon, t, scores:{row:n}, cost}], adds:[{id, icon, t, from, cost, boosts:{row:n}, why}], need, q, opts, win, clue} */
  function buildImprove() {
    var I = D.improve; if (!I) return;
    var anchorGame = I.after ? $$('.fs-game').filter(function (x) { return x.dataset.mod === I.after; })[0] : null, at = anchorGame || anchorP(I.afterText);
    if (!at) { FAILED.push('improve: no anchor'); return; }
    var g = gameShell(I.kicker || 'Lesson game', I.title, I.todo, I.why); g.dataset.mod = 'improve';
    var st = loadJ('improve', { base: null, on: {}, won: 0 });
    var pick = el('div', 'fs-mb-pick'), board = el('div', 'fs-mb-board'), adds = el('div', 'fs-mb-adds'), msg = el('div', 'fs-hs-card fs-mb-msg'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    pick.innerHTML = '<div class="fs-in-k">1. Pick the design to start from</div><div class="fs-in-chips">' + I.bases.map(function (b) { return '<button type="button" class="fs-in-chip" data-id="' + b.id + '"><span>' + b.icon + '</span>' + esc(b.t) + '</button>'; }).join('') + '</div>';
    g.appendChild(pick); g.appendChild(board); g.appendChild(adds); g.appendChild(msg); g.appendChild(miss); g.appendChild(qh); g.appendChild(win);
    function baseOf() { return I.bases.filter(function (b) { return b.id === st.base; })[0]; }
    function now() {
      var b = baseOf(), s = {}, cost = b.cost; I.rows.forEach(function (r) { s[r.id] = b.scores[r.id]; });
      I.adds.forEach(function (a) { if (!st.on[a.id] || a.from === b.id) return; cost += a.cost; Object.keys(a.boosts).forEach(function (r) { s[r] = Math.min(3, s[r] + a.boosts[r]); }); });
      return { s: s, cost: Math.round(cost * 10) / 10 };
    }
    function draw(anim) {
      $$('.fs-in-chip', pick).forEach(function (c) { c.classList.toggle('on', c.dataset.id === st.base); });
      if (!st.base) { board.innerHTML = ''; adds.innerHTML = ''; msg.innerHTML = '<em>Pick a design above. Both tied at the top of the matrix.</em>'; return; }
      var b = baseOf(), n = now(), tot = 0, low = false;
      board.innerHTML = '<div class="fs-mb-title">' + b.icon + ' ' + esc(b.t) + (Object.keys(st.on).some(function (k) { return st.on[k]; }) ? ' <small>(improved)</small>' : '') + '</div>' + I.rows.map(function (r) {
        var v = n.s[r.id]; tot += v; if (v < (I.need || 2)) low = true; var up = v > b.scores[r.id];
        return '<div class="fs-mb-row' + (up ? ' up' : '') + (v < (I.need || 2) ? ' low' : '') + '"><span>' + r.icon + ' ' + esc(r.t) + '</span><b>' + '⭐'.repeat(v) + '<i>' + '☆'.repeat(3 - v) + '</i></b></div>';
      }).join('') + '<div class="fs-mb-cost' + (n.cost > I.budget ? ' over' : '') + '"><span>💵 Cost</span><i><b style="width:' + Math.min(100, 100 * n.cost / (I.budget * 1.5)) + '%"></b><em style="left:' + (100 / 1.5) + '%"></em></i><strong>' + I.unit.replace('#', n.cost) + ' of ' + I.unit.replace('#', I.budget) + '</strong></div>' +
        '<div class="fs-mb-tot">Total: <b>' + tot + ' ⭐</b> (it started at ' + I.rows.reduce(function (a, r) { return a + b.scores[r.id]; }, 0) + ')</div>';
      adds.innerHTML = '<div class="fs-in-k">2. Add features from the other designs (tap to add or remove)</div><div class="fs-mb-list">' + I.adds.filter(function (a) { return a.from !== b.id; }).map(function (a) {
        return '<button type="button" class="fs-in-chip fs-mb-add' + (st.on[a.id] ? ' on' : '') + '" data-id="' + a.id + '"><span>' + a.icon + '</span>' + esc(a.t) + ' <small>+' + I.unit.replace('#', a.cost) + '</small></button>'; }).join('') + '</div>';
      $$('.fs-mb-add', adds).forEach(function (c) { c.addEventListener('click', function () {
        var a = I.adds.filter(function (x) { return x.id === c.dataset.id; })[0]; st.on[a.id] = !st.on[a.id]; saveJ('improve', st); SFX.blip();
        msg.innerHTML = '<span class="fs-hs-n">' + a.icon + '</span><div><b>' + esc(a.t) + (st.on[a.id] ? ' added' : ' removed') + '</b>' + esc(a.why) + '</div>'; draw(true);
      }); });
      var good = !low && n.cost <= I.budget && tot > I.rows.reduce(function (a, r) { return a + b.scores[r.id]; }, 0);
      if (n.cost > I.budget) { miss.innerHTML = '🔎 Over the budget! That breaks the limit. Take something off.'; miss.classList.add('show'); }
      else if (low && Object.keys(st.on).some(function (k) { return st.on[k]; })) { miss.innerHTML = '🔎 Every goal needs at least ⭐⭐. Which goal is still low?'; miss.classList.add('show'); }
      else miss.classList.remove('show');
      if (good) { if (!st.won) { st.won = 1; saveJ('improve', st); SFX.chime(); } askOnce(qh, I.q, I.opts, 'improve-q', win, I.win, I.clue, 'improve', miss); }
    }
    $$('.fs-in-chip', pick).forEach(function (c) { c.addEventListener('click', function () { if (st.base !== c.dataset.id) { st.base = c.dataset.id; st.on = {}; saveJ('improve', st); } SFX.blip(); msg.innerHTML = '<em>Now add a feature. Watch the stars and the cost.</em>'; draw(); }); });
    if (anchorGame) at.parentNode.insertBefore(g, at.nextSibling); else at.parentNode.insertBefore(g, at.nextSibling);
    draw();
  }

  /* ---------- Lesson Part 4: "Test it small" — run tests on a model of the design, see the problem, pick the revision that fixes it, test again (16.02) ----------
     D.pilot = {afterText, kicker, title, todo[], why, tests:[{id, icon, name, level, problem, fixes:[{t, ok, miss, why}], fixLevel, pass}], q, opts, win, clue} */
  function buildPilot() {
    var P = D.pilot; if (!P) return;
    var at = anchorP(P.afterText); if (!at) { FAILED.push('pilot anchor text not found'); return; }
    var g = gameShell(P.kicker || 'Lesson game', P.title, P.todo, P.why); g.dataset.mod = 'pilot';
    var st = loadJ('pilot', {}), busy = false;
    var svg = '<svg class="fs-pt-svg" viewBox="0 0 400 200" role="img" aria-label="A model of the pit seen from the side: a deep middle full of water, a planted shelf on the left edge, and the canal on the right.">' +
      '<rect width="400" height="200" fill="#DCEFF7"/><rect y="40" width="400" height="160" fill="#D9CDA9"/>' +
      '<path class="fs-pt-pit" d="M30,40 L30,70 L120,70 L120,180 L360,180 L360,40Z" fill="#C7B88C"/>' +
      '<path class="fs-pt-ramp" d="M30,40 L120,100 L120,180 L360,180 L360,40Z" fill="#C7B88C" style="display:none"/>' +
      '<clipPath id="fsPtClip"><path class="fs-pt-clip" d="M30,40 L30,70 L120,70 L120,180 L360,180 L360,40Z"/></clipPath>' +
      '<g clip-path="url(#fsPtClip)"><rect class="fs-pt-water" x="0" y="0" width="400" height="200" fill="#3C8DB0" opacity=".85"/></g>' +
      '<g class="fs-pt-plants" fill="#4E8A3C"><path d="M40,70 l3,-14 l3,14z M58,70 l3,-11 l3,11z M78,70 l3,-15 l3,15z M98,70 l3,-12 l3,12z"/></g>' +
      '<g class="fs-pt-plants2" fill="#4E8A3C" style="display:none"><path d="M48,52 l3,-12 l3,12z M66,64 l3,-12 l3,12z M84,76 l3,-12 l3,12z M102,88 l3,-12 l3,12z"/></g>' +
      '<g class="fs-pt-pipe" style="display:none"><rect x="356" y="48" width="44" height="8" fill="#7A8A90"/><text x="378" y="44" text-anchor="middle" font-size="10" font-weight="800" fill="#3E4A52">spillway</text></g>' +
      '<rect x="360" y="40" width="40" height="18" fill="#5B9BB7" opacity=".6"/><text x="380" y="34" text-anchor="middle" font-size="10" font-weight="800" fill="#3E4A52">canal</text>' +
      '<g class="fs-pt-rain" style="display:none" stroke="#5B8FB0" stroke-width="2">' + Array.apply(null, Array(14)).map(function (_, i) { return '<line x1="' + (40 + i * 24) + '" y1="4" x2="' + (34 + i * 24) + '" y2="22"/>'; }).join('') + '</g>' +
      '<g class="fs-pt-sun" style="display:none"><circle cx="370" cy="20" r="12" fill="#F5B83D"/></g>' +
      '<text class="fs-pt-lab" x="75" y="196" text-anchor="middle" font-size="11" font-weight="800" fill="#5E4A2B">planted shelf</text></svg>';
    var stage = el('div', 'fs-pt-stage', svg), runs = el('div', 'fs-pt-runs'), res = el('div', 'fs-hs-card fs-pt-res', '<em>Run the first test.</em>'), fixes = el('div'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(stage); g.appendChild(runs); g.appendChild(res); g.appendChild(fixes); g.appendChild(miss); g.appendChild(qh); g.appendChild(win);
    var water = $('.fs-pt-water', stage);
    function setLevel(y) { water.setAttribute('y', y); }
    function look() {
      $('.fs-pt-pipe', stage).style.display = st.fix1 ? '' : 'none';
      var ramp = !!st.fix2; $('.fs-pt-pit', stage).style.display = ramp ? 'none' : ''; $('.fs-pt-ramp', stage).style.display = ramp ? '' : 'none';
      $('.fs-pt-clip', stage).setAttribute('d', ramp ? 'M30,40 L120,100 L120,180 L360,180 L360,40Z' : 'M30,40 L30,70 L120,70 L120,180 L360,180 L360,40Z');
      $('.fs-pt-plants', stage).style.display = ramp ? 'none' : ''; $('.fs-pt-plants2', stage).style.display = ramp ? '' : 'none';
    }
    function drawRuns() {
      runs.innerHTML = '<div class="fs-in-k">Run each test on the model</div><div class="fs-in-chips">' + P.tests.map(function (t, i) {
        var open = i === 0 || st[P.tests[i - 1].id + ':pass']; var done = st[t.id + ':pass'];
        return '<button type="button" class="fs-in-chip' + (done ? ' ok on' : '') + '" data-i="' + i + '"' + (open ? '' : ' disabled') + '><span>' + t.icon + '</span>' + esc(t.name) + (done ? ' ✓' : '') + '</button>'; }).join('') + '</div>';
      $$('.fs-in-chip', runs).forEach(function (b) { b.addEventListener('click', function () { run(P.tests[+b.dataset.i]); }); });
    }
    function animate(y, cb) { if (reduceMotion) { setLevel(y); cb(); return; } water.style.transition = 'none'; var from = +water.getAttribute('y'), t0 = performance.now(); (function step(n) { var p = Math.min(1, (n - t0) / 1400); setLevel(from + (y - from) * p); if (p < 1) requestAnimationFrame(step); else cb(); })(t0); }
    function weather(t) { $('.fs-pt-rain', stage).style.display = t.kind === 'rain' ? '' : 'none'; $('.fs-pt-sun', stage).style.display = t.kind === 'dry' ? '' : 'none'; }
    function run(t) {
      if (busy) return; busy = true; weather(t); fixes.innerHTML = ''; miss.classList.remove('show');
      var fixed = st[t.id + ':fix'];
      if (t.kind === 'rain') noise(1.2, 900, 3000, .1); SFX.blip();
      animate(fixed ? t.fixLevel : t.level, function () {
        busy = false;
        if (fixed) { st[t.id + ':pass'] = 1; saveJ('pilot', st); SFX.chime(); res.innerHTML = '<span class="fs-hs-n">✅</span><div><b>' + esc(t.name) + ': passed!</b>' + esc(t.pass) + '</div>'; drawRuns(); check(); return; }
        res.innerHTML = '<span class="fs-hs-n">⚠️</span><div><b>' + esc(t.name) + ': a problem!</b>' + esc(t.problem) + '</div>';
        fixes.innerHTML = '<div class="fs-in-k">Pick the revision that fixes it</div><div class="fs-in-chips fs-pt-fix">' + t.fixes.map(function (f, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(f.t) + '</button>'; }).join('') + '</div>';
        $$('.fs-in-chip', fixes).forEach(function (b) { b.addEventListener('click', function () {
          var f = t.fixes[+b.dataset.i]; if (!f.ok) { bounce(b, miss, f.miss); return; }
          miss.classList.remove('show'); st[t.id + ':fix'] = 1; st[t.fixKey] = 1; saveJ('pilot', st); SFX.chime(); look();
          res.innerHTML = '<span class="fs-hs-n">🛠️</span><div><b>Revised!</b>' + esc(f.why) + ' Now run the test again.</div>'; fixes.innerHTML = ''; drawRuns();
        }); });
      });
    }
    function check() { if (P.tests.every(function (t) { return st[t.id + ':pass']; })) { weather({}); askOnce(qh, P.q, P.opts, 'pilot-q', win, P.win, P.clue, 'pilot', miss); } }
    at.parentNode.insertBefore(g, at.nextSibling);
    look(); setLevel(P.start || 80); drawRuns(); check();
  }

  SIMS.coredrill = function (host, T) {
    var S = T.coredrill, drilled = loadJ('coredrill', {}), read = loadJ('coredrill-read', {}), cur = null, MAXD = S.deepest || 80;
    host.innerHTML = '<div class="fs-game-k">Try it: a core drill</div><div class="fs-game-t">' + esc(S.title) + '</div>' +
      '<ul class="fs-todo">' + S.todo.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>' +
      '<div class="fs-dn-parts fs-cd-parts">' + S.parts.map(function (p, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(p.label) + '</button>'; }).join('') + '</div>' +
      '<div class="fs-hs-card fs-cd-pinfo"><em>Tap a part of the core drill to learn what it does.</em></div>' +
      '<div class="fs-in-k">Pick a spot in Florida to drill</div><div class="fs-dn-spots fs-cd-sites">' + S.sites.map(function (s, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '"><span>' + s.icon + '</span>' + esc(s.name) + '<em></em></button>'; }).join('') + '</div>' +
      '<div class="fs-cd-rig"><div class="fs-cd-ground"><div class="fs-cd-where">Pick a spot, then drill.</div><div class="fs-cd-bit"></div></div><button type="button" class="fs-btn fs-cd-go" disabled>⬇ Drill down ' + MAXD + ' feet</button></div>' +
      '<div class="fs-in-k">The core box <small class="fs-cd-hint">(top of the ground at the top)</small></div><div class="fs-cd-box"><em>Your cores go here. Tap a layer to read it.</em></div>' +
      '<div class="fs-hs-card fs-cd-info"><em>Tap a layer in a core.</em></div><div class="fs-sv-q fs-cd-q"></div><div class="fs-miss fs-cd-miss"></div><div class="fs-win fs-cd-win"></div>';
    var pinfo = $('.fs-cd-pinfo', host), info = $('.fs-cd-info', host), box = $('.fs-cd-box', host), go = $('.fs-cd-go', host), ground = $('.fs-cd-ground', host);
    $$('.fs-cd-parts .fs-in-chip', host).forEach(function (c) { c.addEventListener('click', function () { var p = S.parts[+c.dataset.i]; c.classList.add('on'); pinfo.innerHTML = '<span class="fs-hs-n">🔩</span><div><b>' + esc(p.label) + '</b>' + esc(p.t) + '</div>'; SFX.blip(); }); });
    $$('.fs-cd-sites .fs-in-chip', host).forEach(function (c) { c.addEventListener('click', function () {
      cur = S.sites[+c.dataset.i]; $$('.fs-cd-sites .fs-in-chip', host).forEach(function (x) { x.classList.toggle('on', x === c); });
      $('.fs-cd-where', host).textContent = cur.icon + ' ' + cur.where; ground.dataset.k = cur.k; go.disabled = false; SFX.blip(); }); });
    function core(s) {
      return '<div class="fs-cd-core" data-k="' + s.k + '"><div class="fs-cd-ch">' + s.icon + ' ' + esc(s.name) + '</div><div class="fs-cd-tube">' + s.layers.map(function (L) {
        var h = Math.max(8, 100 * (Math.min(L.to, MAXD) - L.from) / MAXD);
        return '<button type="button" class="fs-cd-layer' + (read[s.k + ':' + L.k] ? ' seen' : '') + '" data-l="' + L.k + '" style="height:' + h + '%;--c:' + L.col + '"><span>' + esc(L.t) + '</span><small>' + L.from + '–' + (L.to >= MAXD ? MAXD + '+' : L.to) + ' ft</small></button>';
      }).join('') + '</div></div>';
    }
    function drawBox() {
      var got = S.sites.filter(function (s) { return drilled[s.k]; }); if (!got.length) return;
      box.innerHTML = got.map(core).join('');
      $$('.fs-cd-layer', box).forEach(function (b) { b.addEventListener('click', function () {
        var k = b.closest('.fs-cd-core').dataset.k, s = S.sites.filter(function (x) { return x.k === k; })[0], L = s.layers.filter(function (x) { return x.k === b.dataset.l; })[0];
        read[k + ':' + L.k] = 1; saveJ('coredrill-read', read); b.classList.add('seen'); SFX.chime();
        $$('.fs-cd-layer', box).forEach(function (x) { x.classList.toggle('on', x === b); });
        info.innerHTML = '<span class="fs-hs-n">🔎</span><div><b>' + esc(s.name) + ': ' + esc(L.t) + ' (about ' + L.from + '–' + (L.to >= MAXD ? MAXD + '+' : L.to) + ' feet down)</b>' + esc(L.note) + '</div>'; info.classList.remove('flash'); void info.offsetWidth; info.classList.add('flash'); check(); }); });
    }
    function check() {
      S.sites.forEach(function (s, i) { var c = $$('.fs-cd-sites .fs-in-chip', host)[i]; c.classList.toggle('done', !!drilled[s.k]); $('em', c).textContent = drilled[s.k] ? ' ✓' : ''; });
      var all = S.sites.every(function (s) { return drilled[s.k]; }) && (!S.need || read[S.need.site + ':' + S.need.layer]);
      var hint = $('.fs-cd-hint', host); if (hint && S.need && S.sites.every(function (s) { return drilled[s.k]; }) && !read[S.need.site + ':' + S.need.layer]) hint.textContent = '(tap the layers to read them)';
      if (all) ask();
    }
    go.addEventListener('click', function () {
      if (!cur) return; go.disabled = true; noise(0.9, 80, 400, 0.3);
      ground.classList.remove('drill'); void ground.offsetWidth; ground.classList.add('drill');
      var k = cur.k; setTimeout(function () { drilled[k] = 1; saveJ('coredrill', drilled); go.disabled = false; drawBox(); check(); var c = $('.fs-cd-core[data-k="' + k + '"]', box); if (c && !reduceMotion) c.classList.add('in'); }, reduceMotion ? 0 : 1200);
    });
    function ask() {
      var q = $('.fs-cd-q', host); if (q.dataset.on) return; q.dataset.on = '1';
      q.innerHTML = '<div class="fs-in-k">' + esc(S.q.q) + '</div><div class="fs-in-chips">' + S.q.opts.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(o.t) + '</button>'; }).join('') + '</div>';
      $$('.fs-in-chip', q).forEach(function (c) { c.addEventListener('click', function () { var o = S.q.opts[+c.dataset.i];
        if (!o.ok) { bounce(c, $('.fs-cd-miss', host), o.why); return; } $('.fs-cd-miss', host).classList.remove('show');
        c.classList.add('on', 'ok'); var w = $('.fs-cd-win', host); w.innerHTML = esc(o.why); w.classList.add('show'); SFX.win(); store('coredrill-q', '1'); toolDone(); }); });
      if (store('coredrill-q')) { var i = S.q.opts.map(function (o, j) { return o.ok ? j : -1; }).filter(function (j) { return j > -1; })[0]; $$('.fs-in-chip', q)[i].classList.add('on', 'ok'); var w = $('.fs-cd-win', host); w.innerHTML = esc(S.q.opts[i].why); w.classList.add('show'); }
    }
    drawBox(); check();
  };

  SIMS.thermometer = function (host, T) {
    var S = T.thermo, places = S.places, Fmin = -20, Fmax = 220;
    function yOf(F) { return 330 - (F - Fmin) / (Fmax - Fmin) * 290; }
    var ticks = '', labsF = '', labsC = '';
    for (var F = Fmin; F <= Fmax; F += 10) { var y = yOf(F); ticks += '<line x1="' + (F % 20 === 0 ? 52 : 58) + '" y1="' + y + '" x2="66" y2="' + y + '"/>'; if (F % 20 === 0 && F !== 220) labsF += '<text x="48" y="' + (y + 4) + '" text-anchor="end">' + F + '</text>'; }
    [[32, '#1F8FB0'], [212, '#D9342B']].forEach(function (m) { var y = yOf(m[0]); ticks += '<line x1="50" y1="' + y + '" x2="68" y2="' + y + '" stroke="' + m[1] + '" stroke-width="2.5"/>'; labsF += '<text x="30" y="' + (y + 4) + '" text-anchor="end" fill="' + m[1] + '" style="font-weight:900">' + m[0] + '</text>'; });
    for (var C = -20; C <= 100; C += 20) { var yc = yOf(C * 9 / 5 + 32); ticks += '<line x1="94" y1="' + yc + '" x2="104" y2="' + yc + '"/>'; labsC += '<text x="108" y="' + (yc + 4) + '">' + C + '</text>'; }
    host.innerHTML =
      '<div class="fs-game-k">Try it: the thermometer lab</div><div class="fs-game-t">' + esc(S.title) + '</div>' +
      '<ul class="fs-todo">' + S.todo.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>' +
      '<div class="fs-thermo">' +
        '<div class="fs-th-stage"><div class="fs-th-scene"><span class="fs-th-emoji">🏠</span><span class="fs-th-name">Pick a place →</span><div class="fs-th-fx"></div></div>' +
        '<svg class="fs-th-svg" viewBox="0 0 160 420" role="img" aria-label="Thermometer">' +
          '<text x="40" y="22" text-anchor="middle" class="u">°F</text><text x="112" y="22" text-anchor="middle" class="u">°C</text>' +
          '<rect x="68" y="26" width="24" height="330" rx="12" fill="#F4F8FA" stroke="#8FA3AA" stroke-width="2.5"/>' +
          '<circle cx="80" cy="370" r="27" fill="#F4F8FA" stroke="#8FA3AA" stroke-width="2.5"/>' +
          '<circle cx="80" cy="370" r="20" fill="#D9342B"/>' +
          '<rect class="fs-th-liq" x="74" y="200" width="12" height="170" rx="6" fill="#D9342B"/>' +
          '<rect x="71" y="34" width="5" height="300" rx="2.5" fill="#fff" opacity=".7"/>' +
          '<g stroke="#3B4A52" stroke-width="1.5">' + ticks + '</g><g class="lab">' + labsF + labsC + '</g>' +
          S.parts.map(function (p, i) { return '<g class="fs-th-part" data-i="' + i + '" tabindex="0"><circle cx="' + p.x + '" cy="' + p.y + '" r="11"/><text x="' + p.x + '" y="' + (p.y + 4.5) + '" text-anchor="middle">' + (i + 1) + '</text></g>'; }).join('') +
        '</svg></div>' +
        '<div class="fs-th-side"><div class="fs-th-places">' + places.map(function (p, i) { return '<button type="button" class="fs-th-place" data-i="' + i + '"><span>' + p.icon + '</span>' + esc(p.name) + '<em></em></button>'; }).join('') + '</div>' +
        '<div class="fs-th-read"></div><div class="fs-hs-card fs-th-info"><em>Tap a number on the thermometer to learn its parts.</em></div></div>' +
      '</div><div class="fs-count fs-th-count"></div><div class="fs-win fs-th-win"></div>' +
      '<div class="fs-fool"><div class="fs-game-k">' + esc(S.fool.kicker) + '</div><div class="fs-game-t">' + esc(S.fool.title) + '</div>' +
        '<div class="fs-fool-row"><div class="fs-bowl" data-b="cold">🧊<small>' + esc(S.fool.cold) + '</small></div><div class="fs-bowl" data-b="room">💧<small>' + esc(S.fool.room) + '</small></div></div>' +
        '<div class="fs-fool-steps"></div></div>';
    var liq = $('.fs-th-liq', host), scene = $('.fs-th-scene', host), read = $('.fs-th-read', host), info = $('.fs-th-info', host), cnt = $('.fs-th-count', host), win = $('.fs-th-win', host);
    var cur = 70, anim = null, doneP = {};
    try { doneP = JSON.parse(store('thermo') || '{}'); } catch (e) {}
    function setLiquid(F) { var y = yOf(F); liq.setAttribute('y', y); liq.setAttribute('height', 370 - y); }
    setLiquid(cur);
    function moveTo(F, cb) {
      cancelAnimationFrame(anim); var F0 = cur, t0 = performance.now(), tau = reduceMotion ? 1 : 700;
      (function step(now) { var t = now - t0; cur = F + (F0 - F) * Math.exp(-t / tau); setLiquid(cur); if (t < (reduceMotion ? 0 : 3200)) anim = requestAnimationFrame(step); else { cur = F; setLiquid(F); cb && cb(); } })(t0);
    }
    function upd() { var n = Object.keys(doneP).length; cnt.textContent = '🌡️ ' + n + ' of ' + places.length + ' places measured'; cnt.classList.toggle('ok', n === places.length);
      $$('.fs-th-place', host).forEach(function (b) { var p = doneP[b.dataset.i]; b.classList.toggle('done', !!p); $('em', b).textContent = p ? places[b.dataset.i].F + '°F' : ''; });
      if (n === places.length && !win.classList.contains('show')) { win.innerHTML = esc(S.win); win.classList.add('show'); maybeDone(); } }
    $$('.fs-th-place', host).forEach(function (b) {
      b.addEventListener('click', function () {
        var p = places[+b.dataset.i]; $$('.fs-th-place', host).forEach(function (x) { x.classList.toggle('on', x === b); });
        $('.fs-th-emoji', scene).textContent = p.icon; $('.fs-th-name', scene).textContent = p.name; scene.style.background = p.bg; scene.className = 'fs-th-scene fx-' + (p.fx || 'none');
        read.innerHTML = '<em>Watch the red liquid… wait for it to stop moving.</em>'; SFX.blip(); if (p.fx === 'steam') SFX.whoosh();
        moveTo(p.F, function () {
          var opts = [p.F].concat(p.wrong).sort(function (a, c) { return a - c; });
          read.innerHTML = '<b>It stopped. What does it read?</b><div class="fs-th-opts">' + opts.map(function (o) { return '<button type="button" data-v="' + o + '">' + o + '°F</button>'; }).join('') + '</div><div class="fs-miss"></div>';
          var miss = $('.fs-miss', read);
          $$('.fs-th-opts button', read).forEach(function (ob) { ob.addEventListener('click', function () {
            if (+ob.dataset.v !== p.F) { bounce(ob, miss, S.readMiss); return; }
            ob.classList.add('right'); SFX.chime(); doneP[b.dataset.i] = 1; store('thermo', JSON.stringify(doneP));
            read.innerHTML = '<div class="fs-th-ok">✓ ' + esc(p.name) + ': about <b>' + p.F + '°F</b> (' + p.C + '°C). ' + esc(p.note) + '</div>'; upd();
          }); });
        });
      });
    });
    $$('.fs-th-part', host).forEach(function (g) {
      function show() { var p = S.parts[+g.dataset.i]; $$('.fs-th-part', host).forEach(function (x) { x.classList.toggle('on', x === g); }); info.innerHTML = '<span class="fs-hs-n">' + (+g.dataset.i + 1) + '</span><div><b>' + esc(p.label) + '</b>' + esc(p.t) + '</div>'; SFX.blip(); }
      g.addEventListener('click', show); g.addEventListener('keydown', function (e) { if (e.key === 'Enter') show(); });
    });
    // can your skin be fooled?
    var fs = $('.fs-fool-steps', host), stage = 0, cold = $('[data-b="cold"]', host), room = $('[data-b="room"]', host);
    function foolStep() {
      var F = S.fool;
      if (stage === 0) fs.innerHTML = '<p>' + esc(F.s1) + '</p>';
      if (stage === 1) fs.innerHTML = '<p class="fs-fool-hand">🖐️ ' + esc(F.s2) + '</p>';
      if (stage === 2) fs.innerHTML = '<p class="fs-fool-hand">🖐️ <b>' + esc(F.feels) + '</b></p><button type="button" class="fs-btn fs-fool-th">🌡️ ' + esc(F.check) + '</button>';
      if (stage === 3) { fs.innerHTML = '<p class="fs-fool-hand">🖐️ <b>' + esc(F.feels) + '</b></p><p class="fs-th-ok">🌡️ ' + esc(F.reads) + '</p><div class="fs-win show">' + esc(F.why) + '</div>'; store('fool', '1'); maybeDone(); }
      var t = $('.fs-fool-th', fs); if (t) t.addEventListener('click', function () { stage = 3; SFX.chime(); foolStep(); });
      cold.classList.toggle('next', stage === 0); room.classList.toggle('next', stage === 1);
    }
    cold.addEventListener('click', function () { if (stage !== 0) return; stage = 1; cold.classList.add('in'); SFX.blip(); setTimeout(function () { cold.classList.remove('in'); }, 1200); foolStep(); });
    room.addEventListener('click', function () { if (stage !== 1) return; stage = 2; room.classList.add('in'); SFX.pop(); foolStep(); });
    if (store('fool')) { stage = 3; } foolStep();
    function maybeDone() { if (Object.keys(doneP).length === places.length && store('fool')) toolDone(); }
    upd();
  };

  /* =================== v9: ornaments (decorative, invisible until each file exists) =================== */
  var ORN_KEYS = ['corner', 'divider', 'divider-tracks', 'compass', 'specimen-tag', 'feather', 'fieldnotes', 'fern-sprig'];
  function orn(key, pos) { var s = fsOnly(el('span', 'fs-orn ' + pos)); s.dataset.o = key; s.setAttribute('aria-hidden', 'true'); s.dataset.label = key + '.png'; return s; }
  function buildOrnaments() {
    var base = (D.paths && D.paths.ornaments) || 'assets/ornaments/';
    var css = el('style'); css.id = 'fs-orn-css'; document.head.appendChild(css);
    ORN_KEYS.forEach(function (k) {
      var img = new Image();
      var u = (D.art && D.art.ornaments && D.art.ornaments[k]) || (base + k + '.png');
      img.onload = function () { css.textContent += '.fs-orn[data-o="' + k + '"]{display:block;background-image:url("' + u + '")}'; };
      img.src = u;
    });
    // 1 corner: a palmetto curling out of the bottom-left of each activity card
    $$('.activity-card').forEach(function (c) { c.appendChild(orn('corner', 'pos-corner')); });
    // 2 + 3 dividers: before each Part heading, alternating
    var n = 0;
    $$('#tab-lesson .act-body > h3, #tab-explore .act-body > h3').forEach(function (h) { if (n === 0 && h === $('#tab-lesson .act-body > h3')) { n++; return; } h.parentNode.insertBefore(orn(n++ % 2 ? 'divider-tracks' : 'divider', 'pos-divider'), h); });
    $$('#tab-assignment .act-body > p').filter(function (p) { return /^\W*Part [B-Z]\b/.test(p.textContent.trim()); }).forEach(function (p) { p.parentNode.insertBefore(orn(n++ % 2 ? 'divider-tracks' : 'divider', 'pos-divider'), p); });
    // 4 compass: a faint watermark in the header and on the case file
    var hd = $('.header.fs-hd'); if (hd) hd.appendChild(orn('compass', 'pos-compass-hd'));
    var fo = $('.fs-folder'); if (fo) fo.appendChild(orn('compass', 'pos-compass-case'));
    // 5 specimen tag: on the specimen reveal
    var sp = $('.fs-specimen'); if (sp) sp.appendChild(orn('specimen-tag', 'pos-tag'));
    // 6 feather: beside each Continue button
    $$('.tab-next-wrap').forEach(function (w) { w.insertBefore(orn('feather', 'pos-feather'), w.firstChild); });
    // 7 field notes: very faint behind the Assignment writing
    var ab = $('#tab-assignment .act-body'); if (ab) ab.appendChild(orn('fieldnotes', 'pos-notes'));
    // 8 fern sprig: on the real-photo games
    $$('.fs-photo-game').forEach(function (g) { g.appendChild(orn('fern-sprig', 'pos-fern')); });
  }

  /* =================== v12: Word Lens — the guide reads each word, in their own scientist's style =================== */
  var LENS = {
    binoculars: { icon: '🔭', verb: 'Focus the binoculars', tip: 'Tap a word to focus the binoculars on it.' },
    telescope:  { icon: '🔭', verb: 'Look through the telescope', tip: 'Tap a word to point the telescope at it.' },
    handlens:   { icon: '🔍', verb: 'Look through the hand lens', tip: 'Tap a word to slide the hand lens over it.' },
    blueprint:  { icon: '📐', verb: 'Draw it on the blueprint', tip: 'Tap a word to draw it on the blueprint.' },
    beaker:     { icon: '🧪', verb: 'Mix it in the beaker', tip: 'Tap a word to watch it bubble up in the beaker.' }
  };
  LENS.binoculars.icon = '👀';

  /* v14: cute, bright Word Lens art, one tool per crew member */
  var LENS_ART = {
    binoculars: '<svg viewBox="0 0 120 80"><path d="M30 14 Q60 -4 90 14" stroke="#B5543A" stroke-width="4" fill="none" stroke-linecap="round"/><rect x="14" y="18" width="38" height="44" rx="12" fill="#5E7F4E" stroke="#2E3B2A" stroke-width="3"/><rect x="68" y="18" width="38" height="44" rx="12" fill="#5E7F4E" stroke="#2E3B2A" stroke-width="3"/><rect x="48" y="28" width="24" height="14" rx="5" fill="#46603B" stroke="#2E3B2A" stroke-width="3"/><circle cx="33" cy="60" r="16" fill="#8FD3F4" stroke="#2E3B2A" stroke-width="3.5"/><circle cx="87" cy="60" r="16" fill="#8FD3F4" stroke="#2E3B2A" stroke-width="3.5"/><path d="M25 54 a9 9 0 0 1 8 -6" stroke="#fff" stroke-width="3.5" fill="none" stroke-linecap="round"/><path d="M79 54 a9 9 0 0 1 8 -6" stroke="#fff" stroke-width="3.5" fill="none" stroke-linecap="round"/></svg>',
    telescope: '<svg viewBox="0 0 120 80"><path d="M58 50 L44 78 M62 50 L62 78 M66 50 L80 78" stroke="#6B4A2A" stroke-width="4" stroke-linecap="round"/><g transform="rotate(-24 60 40)"><rect x="18" y="30" width="70" height="20" rx="6" fill="#E4A93C" stroke="#5A3A12" stroke-width="3"/><rect x="84" y="26" width="16" height="28" rx="5" fill="#C9862A" stroke="#5A3A12" stroke-width="3"/><rect x="8" y="34" width="12" height="12" rx="3" fill="#C9862A" stroke="#5A3A12" stroke-width="3"/><rect x="40" y="30" width="6" height="20" fill="#5A3A12" opacity=".35"/></g><g fill="#FFE68A"><circle cx="104" cy="10" r="3"/><circle cx="14" cy="12" r="2"/><circle cx="92" cy="66" r="2"/></g></svg>',
    handlens: '<svg viewBox="0 0 120 80"><rect x="70" y="50" width="40" height="13" rx="6" transform="rotate(35 70 50)" fill="#B9773E" stroke="#5A3A12" stroke-width="3"/><circle cx="52" cy="34" r="27" fill="#BFE8F7" stroke="#3B4A55" stroke-width="7"/><path d="M36 26 a18 18 0 0 1 14 -12" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round"/></svg>',
    blueprint: '<svg viewBox="0 0 120 80"><rect x="10" y="12" width="78" height="58" rx="4" fill="#2F6DB5" stroke="#173E6B" stroke-width="3"/><path d="M10 26h78M10 40h78M10 54h78M26 12v58M42 12v58M58 12v58M74 12v58" stroke="#8DB9EA" stroke-width="1.2"/><path d="M24 58 L44 30 L70 50" stroke="#fff" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"/><g transform="rotate(35 100 40)"><rect x="94" y="8" width="11" height="52" rx="2" fill="#FFC94A" stroke="#7A5300" stroke-width="2.5"/><path d="M94 60h11l-5.5 10z" fill="#F6D7A7" stroke="#7A5300" stroke-width="2.5" stroke-linejoin="round"/></g></svg>',
    beaker: '<svg viewBox="0 0 120 80"><path d="M46 6h28M50 6v22L28 70a6 6 0 0 0 5 8h54a6 6 0 0 0 5-8L70 28V6" fill="#fff" stroke="#4E3B78" stroke-width="3.5" stroke-linejoin="round"/><path d="M38 52h44l10 18a6 6 0 0 1-5 8H33a6 6 0 0 1-5-8z" fill="#B48DEB"/><g fill="#fff" opacity=".9"><circle cx="52" cy="62" r="4"/><circle cx="66" cy="58" r="3"/><circle cx="60" cy="70" r="2.5"/></g><g fill="#B48DEB"><circle cx="64" cy="22" r="4"><animate attributeName="cy" values="40;6;40" dur="2.4s" repeatCount="indefinite"/></circle><circle cx="56" cy="30" r="3"><animate attributeName="cy" values="44;10;44" dur="3s" repeatCount="indefinite"/></circle></g></svg>'
  };
  var LENS_COLORS = ['#FFE08A', '#BDE7C9', '#FFC9C2', '#C9DEFF', '#E5D3FF', '#FFD9A8'];
  function buildWordLens() {
    var grid = $('.vocab-grid'); if (!grid) return;
    var cards = $$('.flip-card', grid); if (!cards.length) return;
    var who = crewOf(), style = (D.lensStyle || who.lens || 'binoculars'), L = LENS[style] || LENS.binoculars;
    var words = cards.map(function (c, i) { return { n: i + 1, emoji: ($('.fc-emoji', c) || {}).textContent || '', w: ($('.fc-word', c) || {}).textContent || '', d: ($('.fc-def', c) || {}).textContent || '' }; });
    var box = fsOnly(el('div', 'fs-lens'));
    box.dataset.style = style;
    var first = esc(who.name.replace(/^Dr\.\s*/, '').split(' ')[0]);
    box.innerHTML = '<div class="fs-lens-top"><span class="fs-lens-who"></span><div class="fs-lens-say"><div class="fs-game-k">Word Lens</div><div class="fs-lens-tip">' + esc(L.tip) + ' I’ll read it to you!</div></div></div>' +
      '<div class="fs-lens-stage"><div class="fs-lens-view"><div class="fs-lens-bg"></div><div class="fs-lens-tool">' + (LENS_ART[style] || LENS_ART.binoculars) + '</div>' +
      '<div class="fs-lens-inner"><span class="fs-lens-e">' + L.icon + '</span><b class="fs-lens-w">Pick a word</b><p class="fs-lens-d">Tap a word sticker below.</p></div><div class="fs-lens-fx"></div></div></div>' +
      '<div class="fs-lens-chips">' + words.map(function (w, i) { return '<button type="button" data-n="' + w.n + '" style="--lc:' + LENS_COLORS[i % LENS_COLORS.length] + ';--rot:' + (i % 2 ? 2 : -2) + 'deg"><span>' + w.emoji + '</span>' + esc(w.w) + '</button>'; }).join('') + '</div>' +
      '<div class="fs-lens-ctl"><button type="button" class="fs-play fs-lens-play" style="display:none">▶ Hear it again</button><button type="button" class="fs-demo fs-lens-demo">▶ Demo the voice</button><span class="fs-count fs-lens-count"></span></div><div class="fs-win fs-lens-win"></div>';
    $('.fs-lens-who', box).appendChild(avatar(who, 'big'));
    grid.parentNode.insertBefore(box, grid);
    grid.closest('.card').classList.add('fs-has-lens');
    var seen = {}; try { seen = JSON.parse(store('lens') || '{}'); } catch (e) {}
    var view = $('.fs-lens-view', box), inner = $('.fs-lens-inner', box), we = $('.fs-lens-w', box), de = $('.fs-lens-d', box), ee = $('.fs-lens-e', box);
    var play = $('.fs-lens-play', box), demo = $('.fs-lens-demo', box), cnt = $('.fs-lens-count', box), win = $('.fs-lens-win', box);
    var cur = null, audio = null, files = {};
    var pre = D.prefix || 'g4sci', base = (D.paths && D.paths.audio || 'assets/audio/guide/') + (D.guide || 'crew') + '/';
    words.forEach(function (w) { probe(base + pre + '-word-' + w.n + '.mp3', 'audio', function (ok) { if (ok) files[w.n] = base + pre + '-word-' + w.n + '.mp3'; }); });
    function upd() { var n = Object.keys(seen).length; cnt.innerHTML = words.map(function (w) { return '<i class="' + (seen[w.n] ? 'on' : '') + '"></i>'; }).join('') + ' <b>' + n + ' of ' + words.length + ' words</b>'; cnt.classList.toggle('ok', n === words.length);
      $$('.fs-lens-chips button', box).forEach(function (b) { b.classList.toggle('seen', !!seen[b.dataset.n]); b.classList.toggle('on', cur && String(cur.n) === b.dataset.n); });
      if (n === words.length && !win.classList.contains('show')) { win.innerHTML = esc(D.lensWin || 'All the words are in focus. You’ll use every one of them today.'); win.classList.add('show'); } }
    function setDef(w) { de.innerHTML = w.d.split(/(\s+)/).map(function (t, i) { return /^\s+$/.test(t) ? t : '<span>' + esc(t) + '</span>'; }).join(''); }
    function speakHighlight(k) { var sp = $$('span', de); sp.forEach(function (s, i) { s.classList.toggle('said', i < k); s.classList.toggle('now', i === k); }); }
    function show(w) {
      cur = w; seen[w.n] = 1; store('lens', JSON.stringify(seen));
      view.classList.remove('focus'); void view.offsetWidth; view.classList.add('focus');
      ee.textContent = w.emoji; ee.style.setProperty('--lc', LENS_COLORS[(w.n - 1) % LENS_COLORS.length]); we.textContent = w.w; setDef(w); SFX[style === 'beaker' ? 'pop' : style === 'blueprint' ? 'blip' : 'whoosh']();
      upd(); playWord(false);
    }
    function playWord(demoVoice) {
      if (!cur) return; if (audio) { audio.pause(); audio = null; }
      if (window.speechSynthesis) window.speechSynthesis.cancel();
      var spans = $$('span', de);
      if (files[cur.n] && !demoVoice) {
        play.style.display = '';
        audio = new Audio(au(files[cur.n])); box.classList.add('talking');
        audio.addEventListener('timeupdate', function () { if (audio && audio.duration) speakHighlight(Math.floor(audio.currentTime / audio.duration * (spans.length + 2)) - 2); });
        audio.addEventListener('ended', function () { box.classList.remove('talking'); speakHighlight(spans.length); });
        audio.play().catch(function () { box.classList.remove('talking'); });
      } else if (demoVoice && window.speechSynthesis) {
        var text = cur.w + '. ' + cur.d, u = new SpeechSynthesisUtterance(text); u.rate = 0.92; box.classList.add('talking');
        var offs = [], pos = cur.w.length + 2; cur.d.split(/(\s+)/).forEach(function (t) { if (!/^\s+$/.test(t)) offs.push(pos); pos += t.length; });
        u.onboundary = function (e) { var k = -1; offs.forEach(function (o, j) { if (o <= e.charIndex) k = j; }); speakHighlight(k); };
        u.onend = function () { box.classList.remove('talking'); speakHighlight(spans.length); };
        window.speechSynthesis.speak(u);
      } else { speakHighlight(spans.length); }
    }
    $$('.fs-lens-chips button', box).forEach(function (b) { b.addEventListener('click', function () { show(words[+b.dataset.n - 1]); }); });
    play.addEventListener('click', function () { playWord(false); });
    demo.addEventListener('click', function () { if (!cur) show(words[0]); playWord(true); });
    upd();
    window.fsSetLens = function (s) { box.dataset.style = s; L = LENS[s] || LENS.binoculars; $('.fs-lens-tip', box).textContent = L.tip + ' I’ll read it to you!'; $('.fs-lens-tool', box).innerHTML = LENS_ART[s] || LENS_ART.binoculars; if (!cur) ee.textContent = L.icon; upd(); };
  }

  /* ---------- mockup review panel ---------- */
  function buildMock() {
    if (!D.mockup) return;
    var M = D.mockup;
    var w = el('div', 'fs-mock');
    var p = el('div', 'fs-mock-panel');
    var h = '<b style="font-size:16px;color:#0E1C42">' + esc(M.title || 'Mockup notes') + '</b>' +
      '<label><input type="checkbox" id="fsLayer" checked> Sparkle layer on</label>' +
      '<label><input type="checkbox" id="fsEmpty"> Show empty video/audio slots (teacher view)</label>' +
      '<label><input type="checkbox" id="fsFix"> Outline proposed text fixes (purple)</label>' +
      '<label><input type="checkbox" id="fsPlain"> Outline plain-language edits (teal)</label>' +
      '<label><input type="checkbox" id="fsOrnPv"> Show where the ornaments go</label>' +
      '<label>Word Lens style: <select id="fsLensSel"><option value="binoculars">Binoculars (Lena, biologist)</option><option value="telescope">Telescope (Theo, astronomer)</option><option value="handlens">Hand lens (June, geologist)</option><option value="blueprint">Blueprint (Sam, engineer)</option><option value="beaker">Beaker (Priya, materials)</option></select></label>' +
      '<label><button type="button" id="fsReset" class="fs-hintbtn" style="margin:0">↺ Reset clues and progress</button></label>';
    (M.sections || []).forEach(function (s) { h += '<h4>' + esc(s.h) + '</h4><ul>' + s.items.map(function (i) { return '<li>' + esc(i) + '</li>'; }).join('') + '</ul>'; });
    p.innerHTML = h;
    var b = el('button', 'fs-mock-btn', '🧪 Mockup v' + esc(M.version || 1) + ' notes'); b.type = 'button';
    b.addEventListener('click', function () { p.classList.toggle('open'); });
    w.appendChild(p); w.appendChild(b); document.body.appendChild(w);
    $('#fsLayer', p).addEventListener('change', function () { html.classList.toggle('fs-on', this.checked); document.dispatchEvent(new CustomEvent('fs:layer', { detail: this.checked })); });
    $('#fsEmpty', p).addEventListener('change', function () { html.classList.toggle('fs-review', this.checked); });
    $('#fsFix', p).addEventListener('change', function () { html.classList.toggle('fs-showfix', this.checked); });
    $('#fsPlain', p).addEventListener('change', function () { html.classList.toggle('fs-showplain', this.checked); });
    $('#fsOrnPv', p).addEventListener('change', function () { html.classList.toggle('fs-orn-preview', this.checked); });
    $('#fsLensSel', p).addEventListener('change', function () { if (window.fsSetLens) window.fsSetLens(this.value); });
    $('#fsReset', p).addEventListener('click', function () { try { Object.keys(localStorage).forEach(function (k) { if (k.indexOf('oao.fs.') === 0) localStorage.removeItem(k); }); } catch (e) {} location.reload(); });
  }

  /* =================== Review & Lab days (Unit 4 pilot, Oct 2026) =================== */
  function anchorP(txt) { var at = null; $$('.tab-panel p').some(function (p) { if (txt && p.textContent.indexOf(txt) > -1) { at = p; return true; } }); return at; }
  function saveJ(k, v) { store(k, JSON.stringify(v)); }
  function loadJ(k, d) { try { return JSON.parse(store(k) || 'null') || d; } catch (e) { return d; } }
  function showMiss(miss, t) { miss.innerHTML = '🔎 ' + esc(t); miss.classList.remove('show'); void miss.offsetWidth; miss.classList.add('show'); }
  function winOnce(win, t, clue, mod) { if (win.classList.contains('show')) return; win.innerHTML = esc(t); win.classList.add('show'); SFX.win(); earnClue(clue || mod); }

  /* ---------- Warm-Up: "Word Rescue" — the storm scattered the word cards; drag (or tap) each word onto its meaning ----------
     D.words = {afterText, kicker, title, todo[], why, hint, words:[{id,icon,t,miss}], meanings:[{id,t}], win, clue} */
  function buildWords() {
    var W = D.words; if (!W) return;
    var at = anchorP(W.afterText); if (!at) { FAILED.push('words anchor text not found'); return; }
    var g = gameShell(W.kicker || 'Warm-Up game', W.title, W.todo, W.why); g.dataset.mod = 'words';
    var pile = el('div', 'fs-wr-pile'), list = el('div', 'fs-wr-list'), miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), win = el('div', 'fs-win');
    var done = loadJ('words', {});
    shuffle(W.words).forEach(function (w, i) {
      var c = el('div', 'fs-wr-card', '<span>' + (w.icon || '') + '</span>' + esc(w.t)); c.dataset.id = w.id; c.tabIndex = 0;
      c.style.setProperty('--r', ((i % 2 ? 1 : -1) * (2 + (i * 7) % 6)) + 'deg'); pile.appendChild(c);
    });
    shuffle(W.meanings).forEach(function (m) {
      var r = el('div', 'fs-wr-row', '<span class="fs-wr-slot"></span><span class="fs-wr-def">' + esc(m.t) + '</span>'); r.dataset.id = m.id; list.appendChild(r);
    });
    if (W.hint) g.appendChild(el('div', 'fs-hs-card', '<em>' + esc(W.hint) + '</em>'));
    g.appendChild(pile); g.appendChild(list); g.appendChild(miss); g.appendChild(count); g.appendChild(win);
    var rows = $$('.fs-wr-row', list);
    function place(card, row, animate) {
      var chip = el('span', 'fs-wr-chip' + (animate && !reduceMotion ? ' drop' : ''), card.innerHTML);
      $('.fs-wr-slot', row).appendChild(chip); row.classList.add('done'); card.classList.add('placed'); card.style.display = 'none';
    }
    function upd() { var n = Object.keys(done).length; count.textContent = '🧩 ' + n + ' of ' + W.words.length + ' words rescued'; count.classList.toggle('ok', n === W.words.length);
      if (n === W.words.length) winOnce(win, W.win, W.clue, 'words'); }
    function drop(card, row) {
      if (row.classList.contains('done')) return;
      if (card.dataset.id !== row.dataset.id) { var w = W.words.filter(function (x) { return x.id === card.dataset.id; })[0]; bounce(card, miss, (w && w.miss) || 'Read the meaning again. Which word fits it?'); return; }
      miss.classList.remove('show'); SFX.chime(); place(card, row, true); done[card.dataset.id] = 1; saveJ('words', done); upd();
    }
    $$('.fs-wr-card', pile).forEach(function (c) { dragDrop(c, function () { return rows; }, drop); if (done[c.dataset.id]) place(c, rows.filter(function (r) { return r.dataset.id === c.dataset.id; })[0], false); });
    tapTargets(g, rows, drop);
    at.parentNode.insertBefore(g, at.nextSibling);
    upd();
  }

  /* ---------- Lesson: "Three layers" — one event, many effects: sort each effect into LAND, LIVING THINGS or PEOPLE (more than one card per bin) ----------
     D.layers = {afterText, kicker, title, todo[], why, bins:[{k,icon,t}], events:[{id,icon,name,cards:[{t,bin,miss}]}], q, opts:[{t,ok,miss}], win, clue} */
  function buildLayers() {
    var L = D.layers; if (!L) return;
    var at = anchorP(L.afterText); if (!at) { FAILED.push('layers anchor text not found'); return; }
    var g = gameShell(L.kicker || 'Lesson game', L.title, L.todo, L.why); g.dataset.mod = 'layers';
    var tabs = el('div', 'fs-ly-tabs'), pool = el('div', 'fs-ly-pool'), bins = el('div', 'fs-ly-bins'), miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    L.bins.forEach(function (b) { var d = el('div', 'fs-ly-bin', '<div class="fs-ly-h"><span>' + b.icon + '</span>' + esc(b.t) + '</div><div class="fs-ly-in"></div>'); d.dataset.k = b.k; d.setAttribute('role', 'button'); d.tabIndex = 0; bins.appendChild(d); });
    L.events.forEach(function (e, i) { var t = el('button', 'fs-btn alt fs-ly-tab', e.icon + ' ' + esc(e.name)); t.type = 'button'; t.dataset.i = i; tabs.appendChild(t); });
    g.appendChild(tabs); g.appendChild(pool); g.appendChild(bins); g.appendChild(miss); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    var done = loadJ('layers', {}), cur = 0, binEls = $$('.fs-ly-bin', bins);
    var total = L.events.reduce(function (n, e) { return n + e.cards.length; }, 0);
    function key(ei, ci) { return ei + '-' + ci; }
    function show(ei) {
      cur = ei; pool.innerHTML = ''; $$('.fs-ly-in', bins).forEach(function (x) { x.innerHTML = ''; });
      $$('.fs-ly-tab', tabs).forEach(function (t) { t.classList.toggle('on', +t.dataset.i === ei); });
      var ev = L.events[ei];
      ev.cards.forEach(function (c, ci) {
        if (done[key(ei, ci)]) { $('.fs-ly-in', binEls.filter(function (b) { return b.dataset.k === c.bin; })[0]).appendChild(el('span', 'fs-ly-chip', esc(c.t))); return; }
        var card = el('div', 'fs-ly-card', esc(c.t)); card.dataset.ci = ci; card.tabIndex = 0; pool.appendChild(card);
        dragDrop(card, function () { return binEls; }, drop);
      });
      if (!$('.fs-ly-card', pool)) pool.innerHTML = '<div class="fs-ly-done">✅ ' + esc(ev.icon + ' ' + ev.name) + ': every effect sorted.</div>';
    }
    function drop(card, bin) {
      var c = L.events[cur].cards[+card.dataset.ci];
      if (c.bin !== bin.dataset.k) { bounce(card, miss, c.miss || 'Ask: does this change the ground, the plants and animals, or the people?'); return; }
      miss.classList.remove('show'); SFX.chime(); card.remove();
      var chip = el('span', 'fs-ly-chip' + (reduceMotion ? '' : ' drop'), esc(c.t)); $('.fs-ly-in', bin).appendChild(chip);
      done[key(cur, card.dataset.ci)] = 1; saveJ('layers', done); upd();
      if (!$('.fs-ly-card', pool)) { pool.innerHTML = '<div class="fs-ly-done">✅ ' + esc(L.events[cur].icon + ' ' + L.events[cur].name) + ': every effect sorted.</div>'; var nx = L.events.map(function (e, i) { return i; }).filter(function (i) { return !L.events[i].cards.every(function (x, ci) { return done[key(i, ci)]; }); })[0]; if (nx != null) setTimeout(function () { show(nx); }, reduceMotion ? 0 : 900); }
    }
    tapTargets(g, binEls, drop);
    $$('.fs-ly-tab', tabs).forEach(function (t) { t.addEventListener('click', function () { SFX.blip(); show(+t.dataset.i); }); });
    function upd() {
      var n = Object.keys(done).length; count.textContent = '🗂 ' + n + ' of ' + total + ' effects sorted'; count.classList.toggle('ok', n === total);
      $$('.fs-ly-tab', tabs).forEach(function (t) { var i = +t.dataset.i; t.classList.toggle('done', L.events[i].cards.every(function (x, ci) { return done[key(i, ci)]; })); });
      if (n === total && !qh.dataset.on) { qh.dataset.on = '1'; chipsQ(qh, L.q, L.opts, function () { store('layers-q', '1'); winOnce(win, L.win, L.clue, 'layers'); }, miss); if (store('layers-q')) { var i = L.opts.map(function (o, j) { return o.ok ? j : -1; }).filter(function (j) { return j > -1; })[0]; $$('.fs-in-chip', qh)[i].classList.add('on', 'ok'); $('.fs-sv-q', qh).dataset.done = '1'; winOnce(win, L.win, L.clue, 'layers'); } }
    }
    at.parentNode.insertBefore(g, at.nextSibling);
    show(0); upd();
  }

  /* ---------- Lab: "Shoreline test tank" — pick a plan and a storm, run it, read how much water reaches the homes (a model) ----------
     D.tank = {afterText, kicker, title, model, todo[], why, plans:[{k,icon,name,img,alt,cost,wild,ready,res:{stormK:{ft,t}}}], storms:[{k,icon,t,surge}],
               need:[[planK,stormK]…], needLine, runBtn, q, opts, credit, win, clue}  (ft = feet of water at the homes) */
  function buildTank() {
    var T = D.tank; if (!T) return;
    var at = anchorP(T.afterText); if (!at) { FAILED.push('tank anchor text not found'); return; }
    var g = gameShell(T.kicker || 'Lab', T.title, T.todo, T.why); g.dataset.mod = 'tank';
    if (T.model) g.appendChild(el('div', 'fs-gr-model', '🧪 ' + esc(T.model)));
    var picks = el('div', 'fs-tk-picks'), storms = el('div', 'fs-tk-storms'), scene = el('div', 'fs-tk-scene'), res = el('div', 'fs-tk-res'), log = el('div', 'fs-tk-log'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    picks.innerHTML = '<div class="fs-in-k">1. Pick a plan</div>' + T.plans.map(function (p, i) { return '<button type="button" class="fs-tk-plan' + (i ? '' : ' on') + '" data-k="' + p.k + '"><img alt="' + esc(p.alt || p.name) + '" src="' + esc(p.img) + '"><b>' + p.icon + ' ' + esc(p.name) + '</b><small>' + esc(p.cost) + '</small></button>'; }).join('');
    storms.innerHTML = '<div class="fs-in-k">2. Pick a storm</div>' + T.storms.map(function (s, i) { return '<button type="button" class="fs-in-chip' + (i ? '' : ' on') + '" data-k="' + s.k + '">' + s.icon + ' ' + esc(s.t) + '</button>'; }).join('') +
      '<button type="button" class="fs-btn fs-tk-go">' + esc(T.runBtn || '▶ Run the storm') + '</button>';
    scene.innerHTML = '<div class="fs-tk-sky"></div><div class="fs-tk-water"><i></i></div><div class="fs-tk-land"></div><div class="fs-tk-barrier"></div>' +
      '<div class="fs-tk-homes"><span>🏠</span><span>🏠</span><span>🏫</span></div><div class="fs-tk-flood"></div><div class="fs-tk-tag fs-tk-sea">OCEAN</div><div class="fs-tk-tag fs-tk-town">TOWN</div><div class="fs-tk-ft"></div>';
    scene.setAttribute('role', 'img'); scene.setAttribute('aria-label', 'A side view model: the ocean on the left, the plan in the middle, and the town on the right.');
    g.appendChild(picks); g.appendChild(storms); g.appendChild(scene); g.appendChild(res); g.appendChild(log); g.appendChild(miss); g.appendChild(qh); g.appendChild(win);
    if (T.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(T.credit)));
    var ran = loadJ('tank', {}), plan = T.plans[0].k, storm = T.storms[0].k;
    function P(k) { return T.plans.filter(function (p) { return p.k === k; })[0]; }
    function S(k) { return T.storms.filter(function (s) { return s.k === k; })[0]; }
    function setBarrier() { var b = $('.fs-tk-barrier', scene); b.className = 'fs-tk-barrier fs-tk-b-' + plan; b.innerHTML = '<span>' + P(plan).icon + '</span>'; }
    function drawLog() {
      log.innerHTML = '<table><tr><th>Plan</th>' + T.storms.map(function (s) { return '<th>' + s.icon + ' ' + esc(s.t) + '</th>'; }).join('') + '<th>Cost</th><th>Wildlife</th><th>Ready</th></tr>' +
        T.plans.map(function (p) { return '<tr><td>' + p.icon + ' ' + esc(p.name) + '</td>' + T.storms.map(function (s) { var k = p.k + '|' + s.k; return '<td class="' + (ran[k] ? (p.res[s.k].ft > 1 ? 'wet' : 'dry') : '') + '">' + (ran[k] ? p.res[s.k].ft + ' ft' : '·') + '</td>'; }).join('') +
          '<td>' + esc(p.cost) + '</td><td>' + esc(p.wild) + '</td><td>' + esc(p.ready) + '</td></tr>'; }).join('') + '</table><div class="fs-tk-key">Feet of water that reached the homes. 1 ft or less = mostly dry.</div>';
    }
    function needMet() { return (T.need || []).every(function (n) { return ran[n[0] + '|' + n[1]]; }); }
    function ask() {
      if (qh.dataset.on || !needMet()) return; qh.dataset.on = '1'; miss.classList.remove('show');
      chipsQ(qh, T.q, T.opts, function () { store('tank-q', '1'); winOnce(win, T.win, T.clue, 'tank'); }, miss);
      if (store('tank-q')) { var i = T.opts.map(function (o, j) { return o.ok ? j : -1; }).filter(function (j) { return j > -1; })[0]; $$('.fs-in-chip', qh)[i].classList.add('on', 'ok'); $('.fs-sv-q', qh).dataset.done = '1'; winOnce(win, T.win, T.clue, 'tank'); }
    }
    $$('.fs-tk-plan', picks).forEach(function (b) { b.addEventListener('click', function () { plan = b.dataset.k; $$('.fs-tk-plan', picks).forEach(function (x) { x.classList.toggle('on', x === b); }); setBarrier(); scene.classList.remove('ran'); res.innerHTML = ''; SFX.blip(); }); });
    $$('.fs-in-chip', storms).forEach(function (b) { b.addEventListener('click', function () { storm = b.dataset.k; $$('.fs-in-chip', storms).forEach(function (x) { x.classList.toggle('on', x === b); }); scene.classList.remove('ran'); res.innerHTML = ''; SFX.blip(); }); });
    $('.fs-tk-go', storms).addEventListener('click', function () {
      var p = P(plan), s = S(storm), r = p.res[storm], wmax = 24;
      scene.classList.remove('ran'); void scene.offsetWidth;
      scene.style.setProperty('--surge', Math.min(100, 30 + s.surge / wmax * 60) + '%');
      scene.style.setProperty('--flood', Math.min(100, r.ft / 6 * 100) + '%');
      scene.classList.add('ran'); SFX.whoosh();
      $('.fs-tk-ft', scene).textContent = '';
      setTimeout(function () {
        $('.fs-tk-ft', scene).textContent = r.ft > 0 ? '💧 ' + r.ft + ' ft at the homes' : '✅ Homes stayed dry';
        if (r.ft > 1) SFX.thud(); else SFX.chime();
        res.innerHTML = '<div class="fs-hs-card flash"><span class="fs-hs-n">' + p.icon + '</span><div><b>' + esc(p.name) + ' · ' + s.icon + ' ' + esc(s.t) + '</b>' + esc(r.t) + '</div></div>';
        ran[plan + '|' + storm] = 1; saveJ('tank', ran); drawLog();
        if (needMet()) ask(); else if (T.needLine) showMiss(miss, T.needLine);
      }, reduceMotion ? 0 : 1700);
    });
    at.parentNode.insertBefore(g, at.nextSibling);
    setBarrier(); drawLog(); ask();
  }

  /* ---------- Lab: "Score the plans" — tap ✓ or ✗ for each plan on each row, from the test data ----------
     D.score = {afterText, kicker, title, todo[], why, plans:[{k,icon,name}], rows:[{t,kind:'goal'|'limit',ans:{k:true|false},miss}], q, opts, win, clue} */
  function buildScore() {
    var C = D.score; if (!C) return;
    var at = anchorP(C.afterText); if (!at) { FAILED.push('score anchor text not found'); return; }
    var g = gameShell(C.kicker || 'Lab', C.title, C.todo, C.why); g.dataset.mod = 'score';
    var tbl = el('div', 'fs-sc'), miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    tbl.innerHTML = '<div class="fs-sc-r fs-sc-head"><span></span>' + C.plans.map(function (p) { return '<b>' + p.icon + ' ' + esc(p.name) + '</b>'; }).join('') + '</div>' +
      C.rows.map(function (r, i) { return '<div class="fs-sc-r" data-i="' + i + '"><span class="fs-sc-t"><em class="fs-sc-kind ' + r.kind + '">' + (r.kind === 'limit' ? '🚧 LIMIT' : '✅ GOAL') + '</em>' + esc(r.t) + '</span>' +
        C.plans.map(function (p) { return '<span class="fs-sc-c" data-k="' + p.k + '"><button type="button" class="fs-in-chip" data-v="1">✓</button><button type="button" class="fs-in-chip" data-v="0">✗</button></span>'; }).join('') + '</div>'; }).join('') +
      '<div class="fs-sc-r fs-sc-tot"><span>Total ✓</span>' + C.plans.map(function (p) { return '<b data-k="' + p.k + '">0</b>'; }).join('') + '</div>';
    g.appendChild(tbl); g.appendChild(miss); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    var got = loadJ('score', {}), cells = C.rows.length * C.plans.length;
    function mark(i, k, v) { var c = $('.fs-sc-r[data-i="' + i + '"] .fs-sc-c[data-k="' + k + '"]', tbl); $$('.fs-in-chip', c).forEach(function (b) { b.classList.toggle('on', +b.dataset.v === +v); b.classList.toggle('ok', +b.dataset.v === +v); }); c.classList.add('done'); }
    function upd() {
      var n = Object.keys(got).length; count.textContent = '📋 ' + n + ' of ' + cells + ' boxes scored'; count.classList.toggle('ok', n === cells);
      C.plans.forEach(function (p) { $('.fs-sc-tot b[data-k="' + p.k + '"]', tbl).textContent = C.rows.filter(function (r, i) { return got[i + p.k] && r.ans[p.k]; }).length; });
      if (n === cells && !qh.dataset.on) { qh.dataset.on = '1'; chipsQ(qh, C.q, C.opts, function () { store('score-q', '1'); winOnce(win, C.win, C.clue, 'score'); }, miss);
        if (store('score-q')) { var j = C.opts.map(function (o, x) { return o.ok ? x : -1; }).filter(function (x) { return x > -1; })[0]; $$('.fs-in-chip', qh)[j].classList.add('on', 'ok'); $('.fs-sv-q', qh).dataset.done = '1'; winOnce(win, C.win, C.clue, 'score'); } }
    }
    $$('.fs-sc-c', tbl).forEach(function (c) {
      var i = +c.parentNode.dataset.i, k = c.dataset.k;
      if (got[i + k]) mark(i, k, C.rows[i].ans[k] ? 1 : 0);
      $$('.fs-in-chip', c).forEach(function (b) { b.addEventListener('click', function () {
        if (c.classList.contains('done')) return;
        var right = (+b.dataset.v === 1) === !!C.rows[i].ans[k];
        if (!right) { bounce(b, miss, C.rows[i].miss || 'Look at your test results and the plan cards again.'); return; }
        miss.classList.remove('show'); SFX.chime(); mark(i, k, b.dataset.v); got[i + k] = 1; saveJ('score', got); upd();
      }); });
    });
    at.parentNode.insertBefore(g, at.nextSibling);
    upd();
  }

  /* ---------- Lab: "Make it better" — name the winning plan's weakness, pick a fix, re-run the big storm ----------
     D.revise = {afterText, kicker, title, todo[], why, weakQ, weak:[{t,ok,miss}], fixQ, budget, budgetT, fixes:[{k,icon,t,cost,costT,ft,ok,why}], runBtn, win, clue} */
  function buildRevise() {
    var R = D.revise; if (!R) return;
    var at = anchorP(R.afterText); if (!at) { FAILED.push('revise anchor text not found'); return; }
    var g = gameShell(R.kicker || 'Lab', R.title, R.todo, R.why); g.dataset.mod = 'revise';
    var step1 = el('div'), step2 = el('div', 'fs-rv-fixes'), out = el('div', 'fs-rv-out'), miss = el('div', 'fs-miss'), win = el('div', 'fs-win');
    g.appendChild(step1); g.appendChild(step2); g.appendChild(out); g.appendChild(miss); g.appendChild(win);
    var st = loadJ('revise', {});
    function fixes() {
      if (step2.dataset.on) return; step2.dataset.on = '1';
      step2.innerHTML = '<div class="fs-in-k">' + esc(R.fixQ) + '</div><div class="fs-rv-grid">' + R.fixes.map(function (f) { return '<button type="button" class="fs-rv-fix" data-k="' + f.k + '"><span>' + f.icon + '</span><b>' + esc(f.t) + '</b><small>' + esc(f.costT) + '</small></button>'; }).join('') + '</div>' +
        '<button type="button" class="fs-btn fs-rv-go" disabled>' + esc(R.runBtn || '▶ Re-run the big storm') + '</button>';
      var pick = null;
      $$('.fs-rv-fix', step2).forEach(function (b) { b.addEventListener('click', function () { pick = b.dataset.k; $$('.fs-rv-fix', step2).forEach(function (x) { x.classList.toggle('on', x === b); }); $('.fs-rv-go', step2).disabled = false; out.innerHTML = ''; SFX.blip(); }); });
      $('.fs-rv-go', step2).addEventListener('click', function () {
        var f = R.fixes.filter(function (x) { return x.k === pick; })[0]; if (!f) return;
        var over = f.cost > R.budget;
        out.innerHTML = '<div class="fs-rv-card ' + (f.ok ? 'ok' : 'no') + (reduceMotion ? '' : ' in') + '"><div class="fs-rv-meter"><span>💧 Water at the homes</span><b>' + f.ft + ' ft</b></div><div class="fs-rv-meter"><span>💵 Total cost</span><b class="' + (over ? 'over' : '') + '">' + esc(f.totalT) + '</b></div><p>' + esc(f.why) + '</p></div>';
        if (f.ok) { SFX.sparkle(); st.fix = f.k; saveJ('revise', st); miss.classList.remove('show'); winOnce(win, R.win, R.clue, 'revise'); }
        else { SFX.thud(); }
      });
      if (st.fix) { var b = $('.fs-rv-fix[data-k="' + st.fix + '"]', step2); if (b) { b.click(); $('.fs-rv-go', step2).click(); } }
    }
    chipsQ(step1, R.weakQ, R.weak, function () { st.weak = 1; saveJ('revise', st); fixes(); }, miss);
    if (st.weak) { var i = R.weak.map(function (o, j) { return o.ok ? j : -1; }).filter(function (j) { return j > -1; })[0]; $$('.fs-in-chip', step1)[i].classList.add('on', 'ok'); $('.fs-sv-q', step1).dataset.done = '1'; fixes(); }
    at.parentNode.insertBefore(g, at.nextSibling);
  }

  /* ----- ground-penetrating radar (Unit 4 review): push the cart along the road, read the radar picture, flag the hidden hollows ----- */
  SIMS.gpr = function (host, T) {
    var S = T.gpr, N = S.spots.length;
    host.innerHTML = '<div class="fs-game-k">Try it: ground-penetrating radar</div><div class="fs-game-t">' + esc(S.title) + '</div>' +
      (S.img ? '<div class="fs-gp-photo"><img alt="' + esc(S.alt || '') + '" src="' + esc(S.img) + '"></div>' : '') +
      '<ul class="fs-todo">' + S.todo.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>' +
      '<div class="fs-gp-road"><div class="fs-gp-label">' + esc(S.road || 'Main Street') + '</div><div class="fs-gp-track">' + S.spots.map(function (s, i) { return '<button type="button" class="fs-gp-spot" data-i="' + i + '" aria-label="Spot ' + (i + 1) + '">' + (i + 1) + '</button>'; }).join('') + '</div><div class="fs-gp-cart">📡</div></div>' +
      '<div class="fs-gp-scan"><svg viewBox="0 0 ' + (N * 40) + ' 120" preserveAspectRatio="none" class="fs-gp-svg" role="img" aria-label="The radar picture: what the radar sees under each spot."></svg><div class="fs-gp-depth"><span>surface</span><span>deeper</span></div></div>' +
      '<div class="fs-gp-key">' + esc(S.key || '') + '</div><div class="fs-hs-card fs-gp-note"><em>' + esc(S.start || 'Tap spot 1 to roll the cart there.') + '</em></div>' +
      '<div class="fs-count fs-gp-count"></div><div class="fs-sv-q fs-gp-q"></div><div class="fs-miss fs-gp-miss"></div><div class="fs-win fs-gp-win"></div>' +
      (S.credit ? '<div class="fs-xr-cr">' + esc(S.credit) + '</div>' : '');
    var svg = $('.fs-gp-svg', host), cart = $('.fs-gp-cart', host), note = $('.fs-gp-note', host), cnt = $('.fs-gp-count', host);
    var st = loadJ('gpr', { scan: {}, flag: {} });
    function col(i) {
      var x = i * 40, s = S.spots[i], d = '';
      for (var k = 0; k < 4; k++) { var y = 18 + k * 26; d += '<path d="M' + x + ' ' + y + ' q10 ' + (k % 2 ? 3 : -3) + ' 20 0 t20 0" stroke="#5E6B73" stroke-width="2" fill="none" opacity=".75"/>'; }
      if (s.hollow) { var y0 = 30 + (s.depth || 1) * 18; d += '<path d="M' + (x + 2) + ' ' + (y0 + 26) + ' Q' + (x + 20) + ' ' + (y0 - 22) + ' ' + (x + 38) + ' ' + (y0 + 26) + '" stroke="#F2C230" stroke-width="5" fill="none"/><path d="M' + (x + 6) + ' ' + (y0 + 34) + ' Q' + (x + 20) + ' ' + (y0 - 6) + ' ' + (x + 34) + ' ' + (y0 + 34) + '" stroke="#F2C230" stroke-width="3" fill="none" opacity=".7"/>'; }
      return '<g class="fs-gp-col">' + d + '</g>';
    }
    function draw() {
      svg.innerHTML = '<rect width="100%" height="120" fill="#1C2328"/>' + S.spots.map(function (s, i) { return st.scan[i] ? col(i) : ''; }).join('');
      $$('.fs-gp-spot', host).forEach(function (b) { var i = +b.dataset.i; b.classList.toggle('scanned', !!st.scan[i]); b.classList.toggle('flag', !!st.flag[i]); b.textContent = st.flag[i] ? '🚩' : (i + 1); });
      var sc = Object.keys(st.scan).length, hol = S.spots.filter(function (s) { return s.hollow; }).length, fl = Object.keys(st.flag).length;
      cnt.textContent = '📡 ' + sc + ' of ' + N + ' spots scanned · 🚩 ' + fl + ' flagged'; cnt.classList.toggle('ok', sc === N);
      if (sc === N) {
        var right = S.spots.every(function (s, i) { return !!s.hollow === !!st.flag[i]; });
        if (right) ask(); else note.innerHTML = '<em>' + esc(S.flagHint || 'All scanned! Now tap each spot with a bright upside-down U to flag it 🚩. Tap a flag again to take it off.') + '</em>';
      }
    }
    function ask() {
      var q = $('.fs-gp-q', host); if (q.dataset.on) return; q.dataset.on = '1';
      note.innerHTML = '<em>' + esc(S.found || 'You found every hidden hollow.') + '</em>';
      q.innerHTML = '<div class="fs-in-k">' + esc(S.q.q) + '</div><div class="fs-in-chips">' + S.q.opts.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(o.t) + '</button>'; }).join('') + '</div>';
      $$('.fs-in-chip', q).forEach(function (c) { c.addEventListener('click', function () { var o = S.q.opts[+c.dataset.i];
        if (!o.ok) { bounce(c, $('.fs-gp-miss', host), o.why); return; } $('.fs-gp-miss', host).classList.remove('show');
        c.classList.add('on', 'ok'); var w = $('.fs-gp-win', host); w.innerHTML = esc(o.why); w.classList.add('show'); SFX.win(); toolDone(); }); });
    }
    $$('.fs-gp-spot', host).forEach(function (b) { b.addEventListener('click', function () {
      var i = +b.dataset.i;
      cart.style.left = ((i + 0.5) / N * 100) + '%';
      if (!st.scan[i]) { st.scan[i] = 1; SFX.blip(); setTimeout(SFX.snap, 250); note.innerHTML = S.spots[i].hollow ? '<em>' + esc(S.spotHollow || 'Whoa: a bright upside-down U! The radar waves bounced back hard from something under this spot.') + '</em>' : '<em>' + esc(S.spotSolid || 'Flat, even lines: layers of sand, clay and rock. Nothing hiding here.') + '</em>'; }
      else if (Object.keys(st.scan).length === N) { if (st.flag[i]) delete st.flag[i]; else st.flag[i] = 1; SFX.pop(); }
      else { note.innerHTML = '<em>' + esc(S.scanFirst || 'Scan every spot first. Then flag the hollows.') + '</em>'; }
      saveJ('gpr', st); draw();
    }); });
    draw();
  };


  /* =================== 17.01: Storm Night (the bulletin, the storm clock, the morning flyover, trace the chain, rain gauge) =================== */

  /* the Palmetto Springs town map (D.townmap: an SVG string from DATA, viewBox 0 0 600 380), used by the case file and the storm clock */
  function townMap(cls) { var w = el('div', 'fs-sn-map ' + (cls || '')); w.innerHTML = D.townmap || ''; return w; }

  /* ---------- Warm-Up: "The weather radio" — play the bulletin, then tap the three dangers in it (17.01) ----------
     D.bulletin = {afterText, kicker, title, todo[], why, device, station, audio (slot name: <prefix>-<audio>.mp3), playBtn,
                   lines:["text with [[id|phrase]] marks; id 'x:hint' marks a decoy phrase"], dangers:[{id, icon, t, does}], waitLine, win, clue} */
  function buildBulletin() {
    var B = D.bulletin; if (!B) return;
    var at = anchorP(B.afterText); if (!at) { FAILED.push('bulletin anchor text not found'); return; }
    var g = gameShell(B.kicker || 'Warm-Up game', B.title, B.todo, B.why); g.dataset.mod = 'bulletin';
    var st = loadJ('bulletin', {});
    var mark = /\[\[([^|\]]+)\|([^\]]+)\]\]/g;
    var paper = B.lines.map(function (ln) {
      return '<p>' + esc(ln).replace(/\[\[([^|\]]+)\|([^\]]+)\]\]/g, function (m, id, t) { return '<button type="button" class="fs-bn-w" data-id="' + esc(id) + '">' + t + '</button>'; }) + '</p>';
    }).join('');
    var dev = B.skin === 'radio' ? el('div', 'fs-bn-dev fs-bn-wt', '<div class="fs-bn-wt-set" aria-hidden="true"><i class="fs-bn-wt-ant"></i><div class="fs-bn-wt-body"><div class="fs-bn-wt-lcd"><span class="fs-bn-led"></span><b>' + esc(B.device || 'CH 7') + '</b><small>' + esc(B.deviceSub || '') + '</small></div><div class="fs-bn-wt-grille"></div><i class="fs-bn-wt-ptt"></i></div></div>' +
      '<div class="fs-bn-side"><button type="button" class="fs-btn fs-bn-play">▶ ' + esc(B.playBtn || 'Play the call') + '</button><div class="fs-bn-st">' + esc(B.station || '') + '</div></div>') : B.skin === 'phone' ? el('div', 'fs-bn-dev fs-bn-ph', '<div class="fs-bn-phone" aria-hidden="true"><div class="fs-bn-ph-scr"><span class="fs-bn-led"></span><b>' + esc(B.device || 'Voicemail') + '</b><small>' + esc(B.deviceSub || '') + '</small><i class="fs-bn-ph-wave"><i></i><i></i><i></i><i></i><i></i><i></i><i></i></i></div></div>' +
      '<div class="fs-bn-side"><button type="button" class="fs-btn fs-bn-play">▶ ' + esc(B.playBtn || 'Play') + '</button><div class="fs-bn-st">' + esc(B.station || '') + '</div></div>') :
      el('div', 'fs-bn-dev',
      '<div class="fs-bn-radio" aria-hidden="true"><div class="fs-bn-ant"></div><div class="fs-bn-body"><div class="fs-bn-grille"></div><div class="fs-bn-screen"><span class="fs-bn-led"></span><span class="fs-bn-scr">' + esc(B.device || 'WEATHER RADIO') + '</span></div></div></div>' +
      '<div class="fs-bn-side"><button type="button" class="fs-btn fs-bn-play">▶ ' + esc(B.playBtn || 'Play the bulletin') + '</button><div class="fs-bn-st">' + esc(B.station || '') + '</div></div>');
    var tape = el('div', 'fs-bn-paper', '<div class="fs-bn-head">⚠️ ' + esc(B.paperHead || 'HURRICANE WARNING') + '</div>' + paper);
    var found = el('div', 'fs-bn-found'), miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), win = el('div', 'fs-win');
    B.dangers.forEach(function (d, i) { var c = el('div', 'fs-bn-slot', '<span class="fs-bn-ic">❓</span><div><b>' + esc((B.dangerWord || 'Danger') + ' ' + (i + 1)) + '</b><small>' + esc(B.notYet || 'not found yet') + '</small></div>'); c.dataset.id = d.id; found.appendChild(c); });
    g.appendChild(dev); g.appendChild(tape); g.appendChild(el('div', 'fs-in-k', esc(B.foundLabel || 'The dangers you found'))); g.appendChild(found);
    g.appendChild(miss); g.appendChild(count); g.appendChild(win);
    function show(id, anim) {
      var d = B.dangers.filter(function (x) { return x.id === id; })[0]; if (!d) return;
      var s = $('.fs-bn-slot[data-id="' + id + '"]', found); s.classList.add('on'); if (anim && !reduceMotion) s.classList.add('pop');
      $('small', s).textContent = d.does; $('b', s).textContent = d.t; $('.fs-bn-ic', s).textContent = d.icon;
      $$('.fs-bn-w[data-id="' + id + '"]', tape).forEach(function (w) { w.classList.add('ok'); });
    }
    function upd() {
      var n = B.dangers.filter(function (d) { return st[d.id]; }).length;
      count.textContent = (B.countIcon || '⚠️') + ' ' + n + ' of ' + B.dangers.length + ' ' + (B.countWord || 'dangers found'); count.classList.toggle('ok', n === B.dangers.length);
      if (n === B.dangers.length) winOnce(win, B.win, B.clue, 'bulletin');
    }
    $$('.fs-bn-w', tape).forEach(function (w) { w.addEventListener('click', function () {
      var id = w.dataset.id;
      if (id.indexOf('x:') === 0) { bounce(w, miss, id.slice(2)); return; }
      if (st[id]) return; st[id] = 1; saveJ('bulletin', st); miss.classList.remove('show'); SFX.chime(); show(id, true); upd();
    }); });
    /* the bulletin: an alert tone (two tones, like a weather radio), then the recorded voice; the page's own voice if the clip isn't there */
    var playB = $('.fs-bn-play', dev), led = $('.fs-bn-led', dev), audio = null, busy = false;
    function alertTone() { var c = ac(); if (!c) return; for (var i = 0; i < 3; i++) { tone(853, i * 0.5, 0.42, 'sine', 0.05); tone(960, i * 0.5, 0.42, 'sine', 0.05); } }
    function done() { if (busy && B.tone === 'squelch') SFX.roger(); busy = false; dev.classList.remove('on'); playB.textContent = '▶ ' + (B.againBtn || 'Play it again'); }
    function speakIt() {
      var ss = window.speechSynthesis; if (!ss) { done(); return; }
      var u = new SpeechSynthesisUtterance(B.lines.join(' ').replace(mark, '$2')); u.rate = 0.95; u.onend = done; ss.cancel(); ss.speak(u);
    }
    playB.addEventListener('click', function () {
      if (busy) { if (audio) audio.pause(); if (window.speechSynthesis) speechSynthesis.cancel(); done(); return; }
      busy = true; dev.classList.add('on'); playB.textContent = '❚❚ Stop'; if (B.tone === 'squelch') { SFX.keyup(); } else if (B.tone === 'ring') { [0, 0.45, 1.2, 1.65].forEach(function (t) { tone(440, t, 0.35, 'sine', 0.04); tone(480, t, 0.35, 'sine', 0.04); }); } else if (B.tone === 'start') { [0, 0.55, 1.1].forEach(function (t, i) { tone(i < 2 ? 587 : 1175, t, i < 2 ? 0.28 : 0.6, 'square', 0.03); }); } else if (B.tone !== 'none') alertTone();
      var src = (D.paths && D.paths.audio || 'assets/audio/guide/') + (D.guide || 'crew') + '/' + D.prefix + '-' + (B.audio || 'bulletin') + '.mp3';
      setTimeout(function () {
        if (!busy) return;
        audio = new Audio(au(src));
        audio.addEventListener('ended', done);
        audio.addEventListener('error', function () { if (busy) speakIt(); });
        var p = audio.play(); if (p && p.catch) p.catch(function () { if (busy) speakIt(); });
      }, B.tone === 'squelch' ? 450 : 1600);
    });
    led.title = 'on air';
    at.parentNode.insertBefore(g, at.nextSibling);
    B.dangers.forEach(function (d) { if (st[d.id]) show(d.id, false); });
    upd();
  }

  /* ---------- Lesson Part 1: "The storm clock" — step through the night; gauges climb, calls light up the town map; drag a cause onto each call (17.01) ----------
     D.stormclock = {afterText, kicker, title, todo[], why, hours:[{t, wind, rain, tide, note}], tideMax, tideNormal, causes:[{k, icon, t}],
                     calls:[{id, at (hour index), icon, place, t, x, y (map coords), cause, miss, why}], notice:{t}, nextBtn, waitLine, q, opts, win, clue} */
  function buildStormclock() {
    var S = D.stormclock; if (!S) return;
    var at = anchorP(S.afterText); if (!at) { FAILED.push('stormclock anchor text not found'); return; }
    var g = gameShell(S.kicker || 'Part 1 game', S.title, S.todo, S.why); g.dataset.mod = 'stormclock';
    var st = loadJ('stormclock', { h: 0, link: {} }), H = S.hours, last = H.length - 1;
    var top = el('div', 'fs-stc-top', '<div class="fs-stc-clock"><span class="fs-stc-time"></span><small class="fs-stc-note"></small></div><button type="button" class="fs-btn fs-stc-next"></button>');
    var dots = el('div', 'fs-stc-dots', H.map(function (h, i) { return '<i data-i="' + i + '">' + esc(h.t) + '</i>'; }).join(''));
    var row = el('div', 'fs-stc-row'), mapBox = townMap('fs-stc-map'), gauges = el('div', 'fs-stc-g');
    gauges.innerHTML = '<div class="fs-stc-meter"><span>💨</span><div><small>Wind</small><b class="fs-stc-wind"></b></div></div>' +
      '<div class="fs-stc-meter"><span>🌧️</span><div><small>Rain so far</small><b class="fs-stc-rain"></b></div></div>' +
      '<div class="fs-stc-tide"><div class="fs-stc-tk">🌊 Tide gauge on the dock <small>(how high the bay water is)</small></div><svg viewBox="0 0 300 150" class="fs-stc-chart" role="img" aria-label="A line chart of the water level at the dock through the night."></svg></div>';
    row.appendChild(mapBox); row.appendChild(gauges);
    var causeBar = el('div', 'fs-stc-causes', '<span class="fs-in-k">Causes:</span>' + S.causes.map(function (c) { return '<div class="fs-card fs-stc-cause" data-k="' + c.k + '"><span>' + c.icon + '</span> ' + esc(c.t) + '</div>'; }).join(''));
    var board = el('div', 'fs-stc-board', '<div class="fs-stc-bh">☎️ ' + esc(S.boardTitle || 'Storm-call board') + '</div><div class="fs-stc-calls"></div>');
    var miss = el('div', 'fs-miss'), info = el('div', 'fs-hs-card fs-stc-info', '<em>' + esc(S.startLine || 'Press the button to start the night.') + '</em>'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(top); g.appendChild(dots); g.appendChild(row); g.appendChild(causeBar); g.appendChild(board); g.appendChild(miss); g.appendChild(info); g.appendChild(qh); g.appendChild(win);
    var calls = $('.fs-stc-calls', board), svgMap = $('svg', mapBox), chart = $('.fs-stc-chart', gauges), nextB = $('.fs-stc-next', top);
    function causeOf(k) { return S.causes.filter(function (c) { return c.k === k; })[0]; }
    function drawChart(h) {
      var W = 300, Hh = 150, L = 34, R = 10, T = 12, B2 = 26, mx = S.tideMax || 9;
      function x(i) { return L + i * (W - L - R) / last; } function y(v) { return T + (1 - v / mx) * (Hh - T - B2); }
      var s = '<rect x="' + L + '" y="' + T + '" width="' + (W - L - R) + '" height="' + (Hh - T - B2) + '" fill="#F3F8FB" stroke="#C9D8E2"/>';
      for (var v = 0; v <= mx; v += 2) s += '<line x1="' + L + '" x2="' + (W - R) + '" y1="' + y(v) + '" y2="' + y(v) + '" stroke="#DCE7EE"/><text x="' + (L - 5) + '" y="' + (y(v) + 4) + '" text-anchor="end" font-size="10" fill="#5C6F75">' + v + ' ft</text>';
      s += '<line x1="' + L + '" x2="' + (W - R) + '" y1="' + y(S.tideNormal || 2) + '" y2="' + y(S.tideNormal || 2) + '" stroke="#2E9E5E" stroke-dasharray="5 4" stroke-width="2"/><text x="' + (W - R - 2) + '" y="' + (y(S.tideNormal || 2) - 4) + '" text-anchor="end" font-size="10" font-weight="800" fill="#2E7A4E">' + esc(S.normalLabel || 'normal high tide') + '</text>';
      H.forEach(function (hh, i) { if (i % 2 === 0 || i === last) s += '<text x="' + x(i) + '" y="' + (Hh - 8) + '" text-anchor="middle" font-size="10" fill="#5C6F75">' + esc(hh.t) + '</text>'; });
      var pts = H.slice(0, h + 1).map(function (hh, i) { return x(i) + ',' + y(hh.tide); }).join(' ');
      s += '<polyline points="' + pts + '" fill="none" stroke="#1F6FB2" stroke-width="3.5" stroke-linejoin="round" stroke-linecap="round" class="fs-stc-line"/>';
      s += '<circle cx="' + x(h) + '" cy="' + y(H[h].tide) + '" r="5.5" fill="#1F6FB2" stroke="#fff" stroke-width="2"/><text x="' + (x(h) + (h === last ? -8 : 8)) + '" y="' + (y(H[h].tide) - 8) + '" text-anchor="' + (h === last ? 'end' : 'start') + '" font-size="12" font-weight="900" fill="#123F66">' + H[h].tide + ' ft</text>';
      chart.innerHTML = s;
    }
    function pins(h) {
      if (!svgMap) return; var gp = svgMap.querySelector('.fs-sn-pins'); if (!gp) { gp = document.createElementNS('http://www.w3.org/2000/svg', 'g'); gp.setAttribute('class', 'fs-sn-pins'); svgMap.appendChild(gp); }
      gp.innerHTML = S.calls.filter(function (c) { return c.at <= h; }).map(function (c, i) {
        var ok = st.link[c.id], cc = ok ? causeOf(c.cause) : null;
        return '<g class="fs-sn-pin' + (ok ? ' ok' : '') + (c.at === h && !ok ? ' new' : '') + '" transform="translate(' + c.x + ' ' + c.y + ')"><circle r="15" class="fs-sn-ring"/><circle r="12" class="fs-sn-dot"/><text y="5" text-anchor="middle" font-size="13">' + (ok ? cc.icon : '☎️') + '</text></g>';
      }).join('');
    }
    function card(c, anim) {
      var ok = st.link[c.id], cc = ok ? causeOf(c.cause) : null;
      var d = el('div', 'fs-stc-call' + (ok ? ' ok' : '') + (anim && !reduceMotion ? ' in' : ''), '<div class="fs-stc-ct"><b>' + esc(H[c.at].t) + '</b> · ' + c.icon + ' ' + esc(c.place) + '</div><p>' + esc(c.t) + '</p><div class="fs-stc-drop">' + (ok ? cc.icon + ' ' + esc(cc.t) : esc(S.dropHere || 'Drop the cause here')) + '</div>');
      d.dataset.id = c.id; return d;
    }
    function drawCalls(anim) {
      calls.innerHTML = '';
      if (S.notice) calls.appendChild(el('div', 'fs-stc-call fs-stc-notice', '<div class="fs-stc-ct">📄 ' + esc(S.notice.head) + '</div><p>' + esc(S.notice.t) + '</p>'));
      S.calls.filter(function (c) { return c.at <= st.h; }).sort(function (a, b) { return b.at - a.at; }).forEach(function (c) { calls.appendChild(card(c, anim && c.at === st.h)); });
    }
    function targets() { return $$('.fs-stc-call:not(.ok):not(.fs-stc-notice)', calls); }
    function openNow() { return S.calls.filter(function (c) { return c.at <= st.h && !st.link[c.id]; }); }
    function draw(anim) {
      var h = H[st.h];
      $('.fs-stc-time', top).textContent = h.t; $('.fs-stc-note', top).textContent = h.note || '';
      $('.fs-stc-wind', gauges).textContent = h.wind + ' mph'; $('.fs-stc-rain', gauges).textContent = h.rain + ' in.';
      $$('i', dots).forEach(function (d, i) { d.classList.toggle('on', i <= st.h); d.classList.toggle('now', i === st.h); });
      g.classList.toggle('fs-stc-peak', h.wind >= 90);
      drawChart(st.h); pins(st.h); drawCalls(anim);
      var open = openNow();
      nextB.disabled = st.h >= last || open.length > 0;
      nextB.textContent = st.h >= last ? '🌅 ' + (S.endBtn || 'Morning') : '▶ ' + (S.nextBtn || 'Next') + ': ' + H[st.h + 1].t;
      if (open.length) info.innerHTML = '<em>' + esc(S.waitLine || 'A new call came in. Drag the cause onto it (or tap a cause, then the call).') + '</em>';
      if (st.h >= last && !open.length) askOnce(qh, S.q, S.opts, 'stormclock-q', win, S.win, S.clue, 'stormclock', miss);
    }
    function drop(k, t) {
      var c = S.calls.filter(function (x) { return x.id === t.dataset.id; })[0]; if (!c || st.link[c.id]) return;
      if (k.dataset.k !== c.cause) { bounce(k, miss, (c.miss && c.miss[k.dataset.k]) || c.missAny || 'Read the call again. Which danger could do that?'); return; }
      miss.classList.remove('show'); st.link[c.id] = 1; saveJ('stormclock', st); SFX.chime();
      var cc = causeOf(c.cause); info.innerHTML = '<span class="fs-hs-n">' + cc.icon + '</span><div><b>' + esc(cc.t) + ' → ' + esc(c.place) + '</b>' + esc(c.why) + '</div>';
      if (!reduceMotion) { info.classList.remove('flash'); void info.offsetWidth; info.classList.add('flash'); }
      draw(false);
    }
    $$('.fs-stc-cause', causeBar).forEach(function (k) {
      dragDrop(k, targets, drop);
      /* a cause chip stays in the bar (it can be used again) */
    });
    calls.addEventListener('click', function (e) { var t = e.target.closest('.fs-stc-call'); if (!t || t.classList.contains('ok') || t.classList.contains('fs-stc-notice')) return; var s = $('.fs-stc-cause.sel', causeBar); if (s) { s.classList.remove('sel'); drop(s, t); } });
    nextB.addEventListener('click', function () {
      if (st.h >= last || openNow().length) return;
      st.h++; saveJ('stormclock', st); SFX.whoosh();
      var nw = S.calls.filter(function (c) { return c.at === st.h; });
      if (nw.length) { setTimeout(function () { tone(1180, 0, 0.12, 'square', 0.03); tone(1180, 0.2, 0.12, 'square', 0.03); }, 250); if (window.innerWidth < 640) setTimeout(function () { scrollToEl(causeBar); }, 120); }
      else info.innerHTML = '<em>' + esc(H[st.h].quiet || S.quietLine || 'No new calls this hour.') + '</em>';
      draw(true);
    });
    at.parentNode.insertBefore(g, at.nextSibling);
    draw(false);
  }

  /* ---------- Lesson Part 2: "Morning flyover" — a real before/after aerial pair with a slider; open each numbered spot and stamp its layer (17.01) ----------
     D.flyover = {afterText, kicker, title, todo[], why, before:{img, alt, label}, after:{img, alt, label}, credit, license, stamps:[{k, icon, t}],
                  spots:[{n, x, y, label, t, k, miss}], q, opts, win, clue} */
  function buildFlyover() {
    var F = D.flyover; if (!F) return;
    var at = anchorP(F.afterText); if (!at) { FAILED.push('flyover anchor text not found'); return; }
    var g = gameShell(F.kicker || 'Part 2 game', F.title, F.todo, F.why); g.dataset.mod = 'flyover';
    var st = loadJ('flyover', {}), cur = null;
    var box = el('div', 'fs-fo-box',
      '<img class="fs-fo-after" alt="' + esc(F.after.alt) + '" src="' + esc(F.after.img) + '">' +
      '<img class="fs-fo-before" alt="' + esc(F.before.alt) + '" src="' + esc(F.before.img) + '">' +
      '<div class="fs-fo-line"><span>⟺</span></div>' +
      '<span class="fs-fo-lab b">' + esc(F.before.label) + '</span><span class="fs-fo-lab a">' + esc(F.after.label) + '</span>' +
      F.spots.map(function (s) { return '<button type="button" class="fs-hs fs-fo-hs" data-n="' + s.n + '" style="left:' + s.x + '%;top:' + s.y + '%" aria-label="Spot ' + s.n + ': ' + esc(s.label) + '">' + s.n + '</button>'; }).join(''));
    var range = el('div', 'fs-fo-range', '<span>◀ ' + esc(F.before.short || 'Before') + '</span><input type="range" min="0" max="100" value="50" aria-label="Slide to compare before and after"><span>' + esc(F.after.short || 'After') + ' ▶</span>');
    var src = el('div', 'fs-srcbar', '📷 ' + esc(F.credit) + ' · ' + esc(F.license));
    var card = el('div', 'fs-hs-card fs-fo-card', '<em>' + esc(F.startLine || 'Tap a number on the photo.') + '</em>');
    var stamps = el('div', 'fs-fo-stamps', F.stamps.map(function (s) { return '<button type="button" class="fs-in-chip fs-fo-st" data-k="' + s.k + '"><span>' + s.icon + '</span>' + esc(s.t) + '</button>'; }).join(''));
    var miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(box); g.appendChild(range); g.appendChild(src); g.appendChild(card); g.appendChild(stamps); g.appendChild(miss); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    var clip = $('.fs-fo-before', box), line = $('.fs-fo-line', box), inp = $('input', range);
    function setX(p) { p = Math.max(0, Math.min(100, p)); clip.style.clipPath = 'inset(0 ' + (100 - p) + '% 0 0)'; clip.style.webkitClipPath = clip.style.clipPath; line.style.left = p + '%'; inp.value = Math.round(p); }
    inp.addEventListener('input', function () { setX(+inp.value); });
    /* drag the line itself, too */
    var dragging = false;
    line.addEventListener('pointerdown', function (e) { dragging = true; line.setPointerCapture && line.setPointerCapture(e.pointerId); e.preventDefault(); });
    line.addEventListener('pointermove', function (e) { if (!dragging) return; var r = box.getBoundingClientRect(); setX((e.clientX - r.left) / r.width * 100); });
    line.addEventListener('pointerup', function () { dragging = false; });
    function stampOf(k) { return F.stamps.filter(function (s) { return s.k === k; })[0]; }
    function mark(s) { var b = $('.fs-fo-hs[data-n="' + s.n + '"]', box); b.classList.add('seen', 'done'); b.textContent = stampOf(s.k).icon; }
    function upd() {
      var n = F.spots.filter(function (s) { return st[s.n]; }).length;
      count.textContent = '🛩️ ' + n + ' of ' + F.spots.length + ' spots stamped'; count.classList.toggle('ok', n === F.spots.length);
      stamps.classList.toggle('off', !cur || !!st[cur.n]);
      if (n === F.spots.length) askOnce(qh, F.q, F.opts, 'flyover-q', win, F.win, F.clue, 'flyover', miss);
    }
    $$('.fs-fo-hs', box).forEach(function (b) { b.addEventListener('click', function (e) {
      e.stopPropagation(); var s = F.spots.filter(function (x) { return String(x.n) === b.dataset.n; })[0]; cur = s; SFX.blip();
      $$('.fs-fo-hs', box).forEach(function (x) { x.classList.toggle('on', x === b); });
      card.innerHTML = '<span class="fs-hs-n">' + (st[s.n] ? stampOf(s.k).icon : s.n) + '</span><div><b>' + esc(s.label) + '</b>' + esc(s.t) + (st[s.n] ? '' : '<br><i>' + esc(F.askLine || 'Which layer is this? Stamp it below.') + '</i>') + '</div>';
      card.classList.remove('flash'); void card.offsetWidth; card.classList.add('flash'); upd();
    }); });
    $$('.fs-fo-st', stamps).forEach(function (b) { b.addEventListener('click', function () {
      if (!cur || st[cur.n]) return;
      if (b.dataset.k !== cur.k) { bounce(b, miss, (cur.miss && cur.miss[b.dataset.k]) || 'Ask: did this change the ground, the living things, or the people?'); return; }
      miss.classList.remove('show'); st[cur.n] = 1; saveJ('flyover', st); SFX.stamp(); mark(cur);
      card.innerHTML = '<span class="fs-hs-n">' + stampOf(cur.k).icon + '</span><div><b>' + esc(cur.label) + ' · ' + esc(stampOf(cur.k).t) + '</b>' + esc(cur.t) + '</div>';
      upd();
    }); });
    F.spots.forEach(function (s) { if (st[s.n]) mark(s); });
    at.parentNode.insertBefore(g, at.nextSibling);
    setX(50); upd();
  }

  /* ---------- Lesson Part 4: "Trace the chain" — drag the night's evidence into CAUSE → LAND → ECOSYSTEM → PEOPLE; then one last reading (the twist) (17.01) ----------
     D.stormchain = {afterText, kicker, title, todo[], why, slots:[{k, icon, t}], cards:[{id, icon, art, t, k ('x' = not in this chain), miss}], links:[t, t, t],
                     doneLine, twist:{btn, icon, head, rows:[[k, v]], t}, q, opts, fact, win, clue} */
  function buildStormchain() {
    var C = D.stormchain; if (!C) return;
    var at = anchorP(C.afterText); if (!at) { FAILED.push('stormchain anchor text not found'); return; }
    var g = gameShell(C.kicker || 'Part 4 game', C.title, C.todo, C.why); g.dataset.mod = 'stormchain';
    var st = loadJ('stormchain', { s: {}, tw: 0 });
    var chain = el('div', 'fs-stc2-chain'), tray = el('div', 'fs-stc2-tray'), miss = el('div', 'fs-miss'), twist = el('div', 'fs-stc2-tw'), qh = el('div'), win = el('div', 'fs-win');
    C.slots.forEach(function (s, i) {
      if (i) chain.appendChild(el('div', 'fs-stc2-arrow', '<span>➜</span><small>' + esc(C.links[i - 1] || '') + '</small>'));
      var d = el('div', 'fs-stc2-slot', '<div class="fs-stc2-h"><span>' + s.icon + '</span>' + esc(s.t) + '</div><div class="fs-stc2-in">' + esc(C.dropHere || 'drop here') + '</div>'); d.dataset.k = s.k; chain.appendChild(d);
    });
    g.appendChild(chain); g.appendChild(el('div', 'fs-in-k', esc(C.trayLabel || 'The night’s evidence'))); g.appendChild(tray); g.appendChild(miss); g.appendChild(twist); g.appendChild(qh); g.appendChild(win);
    var slots = $$('.fs-stc2-slot', chain);
    function cardHTML(c) { return '<small>' + esc(c.art) + '</small><span>' + c.icon + '</span> ' + esc(c.t); }
    function fill(k, c, anim) { var s = slots.filter(function (x) { return x.dataset.k === k; })[0]; s.classList.add('ok'); var inn = $('.fs-stc2-in', s); inn.innerHTML = cardHTML(c); if (anim && !reduceMotion) { inn.classList.remove('drop'); void inn.offsetWidth; inn.classList.add('drop'); } }
    function full() { return C.slots.every(function (s) { return st.s[s.k]; }); }
    function drop(k, s) {
      var c = C.cards.filter(function (x) { return x.id === k.dataset.id; })[0]; if (!c || st.s[s.dataset.k]) return;
      if (c.k !== s.dataset.k) { bounce(k, miss, c.k === 'x' ? c.miss : ((c.missSlot && c.missSlot[s.dataset.k]) || c.miss || 'Read the card again. Which link of the chain is it?')); return; }
      miss.classList.remove('show'); st.s[s.dataset.k] = c.id; saveJ('stormchain', st); SFX.chime(); k.remove(); fill(s.dataset.k, c, true); upd(true);
    }
    shuffle(C.cards).forEach(function (c) { if (c.k !== 'x' && st.s[c.k] === c.id) return; var k = el('div', 'fs-card fs-stc2-card', cardHTML(c)); k.dataset.id = c.id; tray.appendChild(k); dragDrop(k, function () { return slots; }, drop); });
    tapTargets(g, slots, drop);
    function showTwist(anim) {
      var T = C.twist;
      twist.innerHTML = '<div class="fs-stc2-twc' + (anim && !reduceMotion ? ' in' : '') + '"><div class="fs-stc2-twh">' + T.icon + ' ' + esc(T.head) + '</div><dl>' + T.rows.map(function (r) { return '<dt>' + esc(r[0]) + '</dt><dd>' + esc(r[1]) + '</dd>'; }).join('') + '</dl><p>' + esc(T.t) + '</p></div>';
      if (!qh.dataset.on) { qh.dataset.on = '1';
        chipsQ(qh, C.q, C.opts, function () { store('stormchain-q', '1'); if (C.fact) qh.appendChild(el('div', 'fs-hs-card fs-stc2-fact', '<span class="fs-hs-n">📰</span><div>' + esc(C.fact) + '</div>')); winOnce(win, C.win, C.clue, 'stormchain'); }, miss);
        if (store('stormchain-q')) { var i = C.opts.map(function (o, j) { return o.ok ? j : -1; }).filter(function (j) { return j > -1; })[0]; $$('.fs-in-chip', qh)[i].classList.add('on', 'ok'); $('.fs-sv-q', qh).dataset.done = '1'; if (C.fact) qh.appendChild(el('div', 'fs-hs-card fs-stc2-fact', '<span class="fs-hs-n">📰</span><div>' + esc(C.fact) + '</div>')); winOnce(win, C.win, C.clue, 'stormchain'); }
      }
    }
    function upd(anim) {
      chain.classList.toggle('full', full());
      if (!full()) return;
      if (!$('.fs-stc2-done', tray)) { $$('.fs-stc2-card', tray).forEach(function (k) { k.remove(); }); tray.appendChild(el('div', 'fs-stc2-done', '✓ ' + esc(C.doneLine || 'The chain is complete.'))); }
      if (st.tw) { showTwist(false); return; }
      if (!$('.fs-stc2-twb', twist)) { var b = el('button', 'fs-btn fs-stc2-twb', C.twist.btn); b.type = 'button'; twist.innerHTML = ''; twist.appendChild(b);
        b.addEventListener('click', function () { st.tw = 1; saveJ('stormchain', st); SFX.sparkle(); showTwist(true); }); }
    }
    C.slots.forEach(function (s) { var id = st.s[s.k]; if (id) fill(s.k, C.cards.filter(function (c) { return c.id === id; })[0], false); });
    at.parentNode.insertBefore(g, at.nextSibling);
    upd(false);
  }

  /* ----- rain gauge (17.01): read the tube after each part of the storm, empty it, log it; then add it all up -----
     T.raingauge = {title, todo[], parts:[{label, t}], max, periods:[{k, t, inches, opts:[n, n, n], note}], unit, q:{q, opts:[{t, ok, why}]}} */
  SIMS.raingauge = function (host, T) {
    var S = T.raingauge, st = loadJ('raingauge', {}), cur = null, max = S.max || 8;
    host.innerHTML = '<div class="fs-game-k">Try it: a rain gauge</div><div class="fs-game-t">' + esc(S.title) + '</div>' +
      '<ul class="fs-todo">' + S.todo.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>' +
      '<div class="fs-dn-parts fs-rg-parts">' + S.parts.map(function (p, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(p.label) + '</button>'; }).join('') + '</div>' +
      '<div class="fs-hs-card fs-rg-pinfo"><em>Tap a part of the gauge to learn what it does.</em></div>' +
      '<div class="fs-rg-row"><div class="fs-rg-gauge"><svg viewBox="0 0 160 300" role="img" aria-label="A clear rain gauge: a funnel on top of a measuring tube marked in inches."></svg></div>' +
      '<div class="fs-rg-side"><div class="fs-in-k">Check the gauge after each part of the storm</div><div class="fs-rg-per">' +
      S.periods.map(function (p, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '"><span>🕒</span>' + esc(p.t) + '<em></em></button>'; }).join('') + '</div>' +
      '<div class="fs-rg-read"></div></div></div>' +
      '<div class="fs-in-k">Rain in each part of the storm</div><div class="fs-wm-bars fs-rg-bars">' + S.periods.map(function (p) { return '<div class="fs-wm-bar" data-k="' + p.k + '"><span>' + esc(p.t) + '</span><i><b></b></i><em></em></div>'; }).join('') + '</div>' +
      '<div class="fs-rg-total"></div><div class="fs-sv-q fs-rg-q"></div><div class="fs-miss fs-rg-miss"></div><div class="fs-win fs-rg-win"></div>';
    var svg = $('svg', host), read = $('.fs-rg-read', host), miss = $('.fs-rg-miss', host);
    function gauge(level) {
      var top = 70, bot = 280, h = Math.max(0, (bot - top) * Math.min(level, max) / max), s = '';
      s += '<path d="M28 8 h104 l-34 52 h-36 z" fill="#E7F2F8" stroke="#6A8796" stroke-width="3"/><text x="80" y="34" text-anchor="middle" font-size="11" font-weight="900" fill="#456270">FUNNEL</text>';
      s += '<rect x="56" y="' + top + '" width="48" height="' + (bot - top) + '" rx="6" fill="#F7FBFD" stroke="#6A8796" stroke-width="3"/>';
      s += '<rect class="fs-rg-water" x="59" y="' + (bot - h) + '" width="42" height="' + h + '" fill="#4A9BD6" opacity=".75"/>';
      for (var i = 0; i <= max * 2; i++) { var yy = bot - (bot - top) * i / (max * 2), whole = i % 2 === 0; s += '<line x1="104" x2="' + (whole ? 122 : 114) + '" y1="' + yy + '" y2="' + yy + '" stroke="#30495A" stroke-width="' + (whole ? 2 : 1.2) + '"/>' + (whole ? '<text x="126" y="' + (yy + 4) + '" font-size="12" font-weight="800" fill="#30495A">' + (i / 2) + '</text>' : ''); }
      s += '<text x="140" y="' + (top - 6) + '" text-anchor="middle" font-size="10" font-weight="800" fill="#30495A">in.</text>';
      svg.innerHTML = s;
    }
    function total() { return S.periods.reduce(function (n, p) { return n + (st[p.k] ? p.inches : 0); }, 0); }
    function bars() { S.periods.forEach(function (p) { var b = $('.fs-wm-bar[data-k="' + p.k + '"]', host); $('b', b).style.width = (st[p.k] ? 100 * p.inches / max : 0) + '%'; $('em', b).textContent = st[p.k] ? p.inches + ' in.' : '—'; });
      $('.fs-rg-total', host).innerHTML = Object.keys(st).length ? '🌧️ ' + esc(S.totalLabel || 'Rain logged so far') + ': <b>' + total() + ' in.</b>' : ''; }
    $$('.fs-rg-parts .fs-in-chip', host).forEach(function (c) { c.addEventListener('click', function () { var p = S.parts[+c.dataset.i]; c.classList.add('on'); $('.fs-rg-pinfo', host).innerHTML = '<span class="fs-hs-n">🔎</span><div><b>' + esc(p.label) + '</b>' + esc(p.t) + '</div>'; SFX.blip(); }); });
    $$('.fs-rg-per .fs-in-chip', host).forEach(function (c) { c.addEventListener('click', function () {
      var p = S.periods[+c.dataset.i]; cur = p; SFX.blip();
      $$('.fs-rg-per .fs-in-chip', host).forEach(function (x) { x.classList.toggle('on', x === c); });
      if (st[p.k]) { gauge(p.inches); read.innerHTML = '<div class="fs-hs-card"><span class="fs-hs-n">🌧️</span><div><b>' + esc(p.t) + ': ' + p.inches + ' inches</b>' + esc(p.note) + '</div></div>'; return; }
      gauge(0); var t0 = performance.now(), dur = reduceMotion ? 0 : 1400; if (dur) noise(1.2, 2500, 6000, .08);
      (function step(now) { var k = dur ? Math.max(0, Math.min(1, (now - t0) / dur)) : 1; gauge(p.inches * k); if (k < 1) requestAnimationFrame(step); else ask(p); })(performance.now());
    }); });
    function ask(p) {
      read.innerHTML = '<div class="fs-in-k">' + esc(S.readQ || 'Read the gauge. How many inches?') + '</div><div class="fs-in-chips">' + p.opts.map(function (o) { return '<button type="button" class="fs-in-chip" data-v="' + o + '">' + o + ' in.</button>'; }).join('') + '</div>';
      $$('.fs-in-chip', read).forEach(function (b) { b.addEventListener('click', function () {
        if (+b.dataset.v !== p.inches) { bounce(b, miss, +b.dataset.v > p.inches ? 'The water is below that mark. Find the top of the blue water and read the number beside it.' : 'The water is above that mark. Find the top of the blue water and read the number beside it.'); return; }
        miss.classList.remove('show'); st[p.k] = 1; saveJ('raingauge', st); SFX.chime();
        var c = $$('.fs-rg-per .fs-in-chip', host)[S.periods.indexOf(p)]; c.classList.add('done'); $('em', c).textContent = ' ✓';
        read.innerHTML = '<div class="fs-hs-card"><span class="fs-hs-n">🌧️</span><div><b>' + esc(p.t) + ': ' + p.inches + ' inches</b>' + esc(p.note) + ' ' + esc(S.emptyLine || 'You wrote it down and emptied the gauge.') + '</div></div>';
        setTimeout(function () { gauge(0); }, reduceMotion ? 0 : 900); bars(); check();
      }); });
    }
    function check() { if (S.periods.every(function (p) { return st[p.k]; })) final(); }
    function final() {
      var q = $('.fs-rg-q', host); if (q.dataset.on) return; q.dataset.on = '1';
      q.innerHTML = '<div class="fs-in-k">' + esc(S.q.q) + '</div><div class="fs-in-chips">' + S.q.opts.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(o.t) + '</button>'; }).join('') + '</div>';
      $$('.fs-in-chip', q).forEach(function (c) { c.addEventListener('click', function () { var o = S.q.opts[+c.dataset.i];
        if (!o.ok) { bounce(c, miss, o.why); return; } miss.classList.remove('show');
        c.classList.add('on', 'ok'); var w = $('.fs-rg-win', host); w.innerHTML = esc(o.why); w.classList.add('show'); SFX.win(); store('raingauge-q', '1'); toolDone(); }); });
      if (store('raingauge-q')) { var i = S.q.opts.map(function (o, j) { return o.ok ? j : -1; }).filter(function (j) { return j > -1; })[0]; $$('.fs-in-chip', q)[i].classList.add('on', 'ok'); var w = $('.fs-rg-win', host); w.innerHTML = esc(S.q.opts[i].why); w.classList.add('show'); }
    }
    S.periods.forEach(function (p, i) { if (st[p.k]) { var c = $$('.fs-rg-per .fs-in-chip', host)[i]; c.classList.add('done'); $('em', c).textContent = ' ✓'; } });
    gauge(0); bars(); check();
  };


  /* =================== 17.02: The House That Stood (three kinds of mitigation, build it then storm it, fix the town) =================== */

  /* ---------- Lesson Part 1: "Three kinds of mitigation" — drag real photo cards onto BUILT / NATURAL / PLAN shelves (17.02) ----------
     D.mitsort = {afterText, kicker, title, todo[], why, shelves:[{k, icon, t, sub}], cards:[{id, img, alt, icon, t, k, why, miss}], q, opts, credit, win, clue} */
  function buildMitsort() {
    var M = D.mitsort; if (!M) return;
    var at = anchorP(M.afterText); if (!at) { FAILED.push('mitsort anchor text not found'); return; }
    if (at.nextElementSibling && at.nextElementSibling.tagName === 'UL') at = at.nextElementSibling;
    var g = gameShell(M.kicker || 'Part 1 game', M.title, M.todo, M.why); g.dataset.mod = 'mitsort';
    var st = loadJ('mitsort', {});
    var deck = el('div', 'fs-mk-deck'), shelves = el('div', 'fs-mk-shelves'), miss = el('div', 'fs-miss'), info = el('div', 'fs-hs-card fs-mk-info', '<em>' + esc(M.startLine || 'Drag a card onto a shelf (or tap a card, then a shelf).') + '</em>'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    if (M.cols) shelves.style.setProperty('--mk-cols', M.cols);
    M.shelves.forEach(function (s) { var d = el('div', 'fs-mk-shelf', '<div class="fs-mk-h"><span>' + s.icon + '</span><b>' + esc(s.t) + '</b><small>' + esc(s.sub || '') + '</small></div><div class="fs-mk-in"></div>'); d.dataset.k = s.k; shelves.appendChild(d); });
    g.appendChild(deck); g.appendChild(shelves); g.appendChild(miss); g.appendChild(info); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    if (M.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(M.credit)));
    var zones = $$('.fs-mk-shelf', shelves);
    function face(c) { return (c.img ? '<span class="fs-mk-ph"><img alt="' + esc(c.alt || c.t) + '" src="' + esc(c.img) + '"></span>' : '<span class="fs-mk-ic">' + c.icon + '</span>') + '<span class="fs-mk-t">' + esc(c.t) + '</span>'; }
    function place(c, anim) { var z = zones.filter(function (x) { return x.dataset.k === c.k; })[0]; var it = el('div', 'fs-mk-got' + (anim && !reduceMotion ? ' pop' : ''), face(c)); $('.fs-mk-in', z).appendChild(it); }
    function drop(k, z) {
      var c = M.cards.filter(function (x) { return x.id === k.dataset.id; })[0]; if (!c || st[c.id]) return;
      if (c.k !== z.dataset.k) { bounce(k, miss, c.miss); return; }
      miss.classList.remove('show'); st[c.id] = 1; saveJ('mitsort', st); SFX.chime(); k.remove(); place(c, true);
      var s = M.shelves.filter(function (x) { return x.k === c.k; })[0];
      info.innerHTML = '<span class="fs-hs-n">' + s.icon + '</span><div><b>' + esc(c.t) + '</b>' + esc(c.why) + '</div>'; if (!reduceMotion) { info.classList.remove('flash'); void info.offsetWidth; info.classList.add('flash'); }
      upd();
    }
    shuffle(M.cards).forEach(function (c) { if (st[c.id]) return; var k = el('div', 'fs-card fs-mk-card', face(c)); k.dataset.id = c.id; deck.appendChild(k); dragDrop(k, function () { return zones; }, drop); });
    tapTargets(g, zones, drop);
    function upd() {
      var n = Object.keys(st).length; count.textContent = '🗂️ ' + n + ' of ' + M.cards.length + ' cards on a shelf'; count.classList.toggle('ok', n === M.cards.length);
      if (n === M.cards.length) { if (!$('.fs-mk-done', deck)) deck.appendChild(el('div', 'fs-mk-done', '✓ ' + esc(M.doneLine || 'Every card is on a shelf.'))); askOnce(qh, M.q, M.opts, 'mitsort-q', win, M.win, M.clue, 'mitsort', miss); }
    }
    M.cards.forEach(function (c) { if (st[c.id]) place(c, false); });
    at.parentNode.insertBefore(g, at.nextSibling);
    upd();
  }

  /* ---------- Lesson Part 2: "Build it, then storm it" — pick a foundation, windows and roof inside a budget, run the storm, read the tests, revise (17.02) ----------
     D.buildhouse = {afterText, kicker, title, todo[], why, budget, unit, surge (ft), wind (mph), parts:[{k, icon, t, opts:[{k, t, cost, pass, note}]}],
                     tests:[{part, icon, t, pass, fail}], runBtn, againBtn, overLine, reviseLine, q, opts, win, clue}
     foundation option keys: 'slab' (floor 0 ft), 'posts' (floor 4 ft), 'pilings' (floor 10 ft); windows: 'plain' | 'shutters' | 'impact'; roof: 'nails' | 'straps' */
  function buildBuildhouse() {
    var B = D.buildhouse; if (!B) return;
    var at = anchorP(B.afterText); if (!at) { FAILED.push('buildhouse anchor text not found'); return; }
    if (at.nextElementSibling && at.nextElementSibling.tagName === 'UL') at = at.nextElementSibling;
    var g = gameShell(B.kicker || 'Part 2 game', B.title, B.todo, B.why); g.dataset.mod = 'buildhouse';
    var st = loadJ('buildhouse', { pick: {}, runs: 0, won: 0 });
    B.parts.forEach(function (p) { if (!st.pick[p.k]) st.pick[p.k] = p.opts[0].k; });
    var row = el('div', 'fs-bh-row'), pick = el('div', 'fs-bh-pick'), view = el('div', 'fs-bh-view');
    B.parts.forEach(function (p) {
      var d = el('div', 'fs-bh-part', '<div class="fs-in-k">' + p.icon + ' ' + esc(p.t) + '</div><div class="fs-in-chips">' + p.opts.map(function (o) { return '<button type="button" class="fs-in-chip" data-p="' + p.k + '" data-o="' + o.k + '">' + esc(o.t) + ' <em>' + '●'.repeat(o.cost) + '</em></button>'; }).join('') + '</div>');
      pick.appendChild(d);
    });
    var budget = el('div', 'fs-bh-budget', '<span class="fs-in-k">💰 ' + esc(B.budgetLabel || 'Budget') + '</span><i><b></b></i><em></em>');
    pick.appendChild(budget);
    var runB = el('button', 'fs-btn fs-bh-run', '▶ ' + esc(B.runBtn || 'Run the storm')); runB.type = 'button'; pick.appendChild(runB);
    view.innerHTML = '<svg viewBox="0 0 400 300" class="fs-bh-svg" role="img" aria-label="' + esc(B.svgLabel || 'A model of the house on Bay Street, the ground, and a line showing how high the storm surge reaches.') + '"></svg>';
    row.appendChild(pick); row.appendChild(view);
    var results = el('div', 'fs-bh-res'), miss = el('div', 'fs-miss'), info = el('div', 'fs-hs-card fs-bh-info', '<em>' + esc(B.startLine || 'Pick each part, then run the storm.') + '</em>'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(row); g.appendChild(results); g.appendChild(miss); g.appendChild(info); g.appendChild(qh); g.appendChild(win);
    var svg = $('svg', view), busy = false;
    function opt(pk, ok) { var p = B.parts.filter(function (x) { return x.k === pk; })[0]; return p.opts.filter(function (o) { return o.k === (ok || st.pick[pk]); })[0]; }
    function cost() { return B.parts.reduce(function (n, p) { return n + opt(p.k).cost; }, 0); }
    function floorFt() { var f = st.pick.foundation; return f === 'pilings' ? 10 : f === 'posts' ? 4 : 0; }
    var PX = 13, GROUND = 262;
    function draw(water, fx) {
      fx = fx || {}; var fl = GROUND - floorFt() * PX, s = '';
      s += '<rect width="400" height="300" fill="' + (fx.storm ? '#3A4A63' : '#DCEFFA') + '"/>';
      if (fx.storm && !reduceMotion) s += '<g stroke="#9FB7D6" stroke-width="1.5" opacity=".6">' + Array.apply(null, Array(18)).map(function (_, i) { var x = (i * 23) % 400, y = (i * 37) % 200; return '<path d="M' + x + ' ' + y + 'l-7 18"/>'; }).join('') + '</g>';
      s += '<rect y="' + GROUND + '" width="400" height="' + (300 - GROUND) + '" fill="#D9C89B"/>';
      // surge line
      var sy = GROUND - (B.surge || 8) * PX;
      s += '<line x1="0" x2="400" y1="' + sy + '" y2="' + sy + '" stroke="#1F6FB2" stroke-width="2" stroke-dasharray="7 5"/><text x="6" y="' + (sy - 5) + '" font-size="11" font-weight="900" fill="#1F4F82">' + esc(B.surgeLabel || 'Storm surge: 8 ft') + '</text>';
      // ruler
      for (var f = 0; f <= 12; f += 2) s += '<line x1="372" x2="384" y1="' + (GROUND - f * PX) + '" y2="' + (GROUND - f * PX) + '" stroke="#30495A" stroke-width="1.5"/><text x="388" y="' + (GROUND - f * PX + 4) + '" font-size="9" fill="#30495A">' + f + '</text>';
      // foundation
      if (st.pick.foundation === 'pilings') [130, 175, 225, 270].forEach(function (x) { s += '<rect x="' + (x - 4) + '" y="' + fl + '" width="8" height="' + (GROUND - fl + 34) + '" fill="#8C7B5A"/>'; });
      else if (st.pick.foundation === 'posts') [130, 175, 225, 270].forEach(function (x) { s += '<rect x="' + (x - 5) + '" y="' + fl + '" width="10" height="' + (GROUND - fl) + '" fill="#A9967A"/>'; });
      else s += '<rect x="112" y="' + (GROUND - 6) + '" width="176" height="8" fill="#A7A7A7"/>';
      if (st.pick.foundation === 'pilings') s += '<text x="200" y="' + (GROUND + 30) + '" text-anchor="middle" font-size="10" font-weight="800" fill="#5A4430">' + esc(B.deepLabel || 'pilings go deep into the ground') + '</text>';
      // house
      var top = fl - 80, flooded = water > floorFt() + 0.01;
      s += '<g class="fs-bh-house"><rect x="115" y="' + top + '" width="170" height="80" fill="#F2EAD6" stroke="#6B5A3E" stroke-width="2"/>';
      if (flooded) { var wl = Math.min(80, (water - floorFt()) * PX); s += '<rect x="117" y="' + (fl - wl) + '" width="166" height="' + wl + '" fill="#4A9BD6" opacity=".55"/>'; }
      s += '<rect x="185" y="' + (fl - 46) + '" width="28" height="46" fill="#8C6A44"/>';
      [[135, top + 18], [235, top + 18]].forEach(function (w) {
        s += '<rect x="' + w[0] + '" y="' + w[1] + '" width="32" height="26" fill="#BFE0F2" stroke="#6B5A3E" stroke-width="2"/>';
        if (st.pick.windows === 'shutters') s += '<g fill="#5E7356">' + [0, 1, 2, 3, 4].map(function (i) { return '<rect x="' + w[0] + '" y="' + (w[1] + i * 5.2) + '" width="32" height="4"/>'; }).join('') + '</g>';
        if (st.pick.windows === 'impact') s += '<rect x="' + (w[0] + 2) + '" y="' + (w[1] + 2) + '" width="28" height="22" fill="none" stroke="#2B7BB9" stroke-width="2"/>';
        if (fx.crack && st.pick.windows === 'plain') s += '<path d="M' + (w[0] + 6) + ' ' + (w[1] + 4) + 'l10 9-6 4 14 9M' + (w[0] + 22) + ' ' + (w[1] + 3) + 'l-5 10" stroke="#30495A" stroke-width="1.5" fill="none"/>';
      });
      var lift = fx.roofOff ? ' transform="translate(30 -46) rotate(14 200 ' + top + ')"' : '';
      s += '<g class="fs-bh-roof"' + lift + '><path d="M105 ' + top + 'L200 ' + (top - 52) + 'L295 ' + top + 'z" fill="#B66A4A" stroke="#6B3A2A" stroke-width="2"/>';
      if (st.pick.roof === 'straps') [130, 270].forEach(function (x) { s += '<rect x="' + (x - 3) + '" y="' + (top - 8) + '" width="6" height="18" fill="#9AA7AD" stroke="#55646A"/>'; });
      s += '</g></g>';
      // water
      if (water > 0) { var wy = GROUND - water * PX; s += '<rect y="' + wy + '" width="400" height="' + (GROUND - wy) + '" fill="#2C6E9E" opacity=".55"/><path d="M0 ' + wy + 'q12-6 24 0t24 0 24 0 24 0 24 0 24 0 24 0 24 0 24 0 24 0 24 0 24 0 24 0 24 0 24 0 24 0 24 0" fill="none" stroke="#BFD8EC" stroke-width="2"/>'; }
      if (fx.storm) s += '<text x="200" y="22" text-anchor="middle" font-size="14" font-weight="900" fill="#FFE58A">💨 ' + (B.wind || 130) + ' mph wind · 🌊 ' + (B.surge || 8) + ' ft surge</text>';
      svg.innerHTML = s;
    }
    function upd() {
      $$('.fs-bh-part .fs-in-chip', pick).forEach(function (c) { c.classList.toggle('on', st.pick[c.dataset.p] === c.dataset.o); });
      var c = cost(), over = c > B.budget;
      $('b', budget).style.width = Math.min(100, 100 * c / B.budget) + '%'; budget.classList.toggle('over', over);
      $('em', budget).textContent = c + ' of ' + B.budget + ' ' + (B.unit || 'coins') + (over ? ' · ' + (B.overShort || 'over budget!') : '');
      draw(0);
    }
    $$('.fs-bh-part .fs-in-chip', pick).forEach(function (c) { c.addEventListener('click', function () { if (busy) return; st.pick[c.dataset.p] = c.dataset.o; saveJ('buildhouse', st); SFX.blip(); var o = opt(c.dataset.p); info.innerHTML = '<span class="fs-hs-n">🔧</span><div><b>' + esc(o.t) + '</b>' + esc(o.note) + '</div>'; results.innerHTML = ''; upd(); }); });
    function testsFor() { return B.tests.map(function (t) { var o = opt(t.part); return { t: t, ok: !!o.pass, o: o }; }); }
    function showResults(rs, over) {
      results.innerHTML = '<div class="fs-in-k">' + esc(B.resultsLabel || 'Test results') + '</div>' + rs.map(function (r) { return '<div class="fs-bh-r ' + (r.ok ? 'ok' : 'no') + '"><span>' + (r.ok ? '✅' : '❌') + '</span><div><b>' + r.t.icon + ' ' + esc(r.t.t) + '</b>' + esc(r.ok ? r.t.pass : r.t.fail) + '</div></div>'; }).join('') +
        (over ? '<div class="fs-bh-r no"><span>❌</span><div><b>💰 ' + esc(B.budgetLabel || 'Budget') + '</b>' + esc(B.overLine) + '</div></div>' : '<div class="fs-bh-r ok"><span>✅</span><div><b>💰 ' + esc(B.budgetLabel || 'Budget') + '</b>' + esc(B.inLine || 'It fits the budget.') + '</div></div>');
    }
    runB.addEventListener('click', function () {
      if (busy) return; busy = true; runB.disabled = true; st.runs++; SFX.whoosh(); if (window.innerWidth < 700) scrollToEl(view);
      var rs = testsFor(), over = cost() > B.budget, t0 = performance.now(), dur = reduceMotion ? 0 : 2200, surge = B.surge || 8;
      if (dur) noise(2, 300, 1400, .18);
      (function step(now) {
        var k = dur ? Math.max(0, Math.min(1, (now - t0) / dur)) : 1;
        draw(surge * k, { storm: true, roofOff: k > .6 && !opt('roof').pass, crack: k > .45 && !opt('windows').pass });
        if (k < 1) { requestAnimationFrame(step); return; }
        busy = false; runB.disabled = false; runB.textContent = '▶ ' + (B.againBtn || 'Run the storm again');
        showResults(rs, over);
        var all = rs.every(function (r) { return r.ok; }) && !over;
        if (all) { st.won = 1; SFX.win(); info.innerHTML = '<span class="fs-hs-n">🏠</span><div><b>' + esc(B.passHead || 'The house stood!') + '</b>' + esc(B.passLine || '') + '</div>'; askOnce(qh, B.q, B.opts, 'buildhouse-q', win, B.win, B.clue, 'buildhouse', miss); }
        else { SFX.thud(); info.innerHTML = '<span class="fs-hs-n">🔁</span><div><b>' + esc(B.reviseHead || 'Time to revise') + '</b>' + esc(B.reviseLine) + '</div>'; }
        saveJ('buildhouse', st);
        setTimeout(function () { draw(st.won ? surge : 0, { roofOff: !opt('roof').pass, crack: !opt('windows').pass }); }, reduceMotion ? 0 : 1600);
      })(performance.now());
    });
    at.parentNode.insertBefore(g, at.nextSibling);
    upd();
    if (st.won) { showResults(testsFor(), cost() > B.budget); askOnce(qh, B.q, B.opts, 'buildhouse-q', win, B.win, B.clue, 'buildhouse', miss); }
  }

  /* ---------- Lesson Part 4: "Fix the town" — the Storm Night map returns; for each problem pick the best fix, then stamp its kind (17.02) ----------
     D.fixtown = {afterText, kicker, title, todo[], why, kinds:[{k, icon, t}], spots:[{id, icon, place, x, y, problem, fixes:[{t, ok, miss}], kind, kindMiss, why}], q, opts, win, clue} */
  function buildFixtown() {
    var F = D.fixtown; if (!F) return;
    var at = anchorP(F.afterText); if (!at) { FAILED.push('fixtown anchor text not found'); return; }
    var g = gameShell(F.kicker || 'Part 4 game', F.title, F.todo, F.why); g.dataset.mod = 'fixtown';
    var st = loadJ('fixtown', {}), cur = null;
    var row = el('div', 'fs-fxt-row'), mapBox = townMap('fs-fxt-map'), list = el('div', 'fs-fxt-list'), panel = el('div', 'fs-fxt-panel'), miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    row.appendChild(mapBox); row.appendChild(list);
    g.appendChild(row); g.appendChild(panel); g.appendChild(miss); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    var svgMap = $('svg', mapBox);
    function kindOf(k) { return F.kinds.filter(function (x) { return x.k === k; })[0]; }
    function stage(id) { return (st[id] || 0); } /* 0 = open, 1 = fix picked, 2 = kind stamped */
    function pins() {
      if (!svgMap) return; var gp = svgMap.querySelector('.fs-sn-pins'); if (!gp) { gp = document.createElementNS('http://www.w3.org/2000/svg', 'g'); gp.setAttribute('class', 'fs-sn-pins'); svgMap.appendChild(gp); }
      gp.innerHTML = F.spots.map(function (s) { var done = stage(s.id) === 2; return '<g class="fs-sn-pin' + (done ? ' ok' : (cur && cur.id === s.id ? ' new' : '')) + '" data-id="' + s.id + '" transform="translate(' + s.x + ' ' + s.y + ')" style="cursor:pointer"><circle r="15" class="fs-sn-ring"/><circle r="12" class="fs-sn-dot"/><text y="5" text-anchor="middle" font-size="13">' + (done ? kindOf(s.kind).icon : s.icon) + '</text></g>'; }).join('');
      $$('.fs-sn-pin', gp).forEach(function (p) { p.addEventListener('click', function () { open(F.spots.filter(function (s) { return s.id === p.dataset.id; })[0]); }); });
    }
    function drawList() {
      list.innerHTML = F.spots.map(function (s) { var d = stage(s.id) === 2; return '<button type="button" class="fs-fxt-item' + (d ? ' done' : '') + (cur && cur.id === s.id ? ' on' : '') + '" data-id="' + s.id + '"><span>' + (d ? kindOf(s.kind).icon : s.icon) + '</span><b>' + esc(s.place) + '</b><small>' + esc(s.problem) + '</small>' + (d ? '<em>✓ ' + esc(s.fixes.filter(function (f) { return f.ok; })[0].short || '') + '</em>' : '') + '</button>'; }).join('');
      $$('.fs-fxt-item', list).forEach(function (b) { b.addEventListener('click', function () { open(F.spots.filter(function (s) { return s.id === b.dataset.id; })[0]); }); });
    }
    function open(s) {
      cur = s; SFX.blip(); miss.classList.remove('show');
      var good = s.fixes.filter(function (f) { return f.ok; })[0];
      var h = '<div class="fs-fxt-h">' + s.icon + ' <b>' + esc(s.place) + '</b> · ' + esc(s.problem) + '</div>';
      if (stage(s.id) === 0) {
        h += '<div class="fs-in-k">' + esc(F.fixQ || 'Which fix would help most?') + '</div><div class="fs-in-chips fs-fxt-fixes">' + s.fixes.map(function (f, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(f.t) + '</button>'; }).join('') + '</div>';
      } else if (stage(s.id) === 1) {
        h += '<div class="fs-fxt-chosen">✓ ' + esc(good.t) + '</div><div class="fs-in-k">' + esc(F.kindQ || 'What kind of mitigation is it?') + '</div><div class="fs-in-chips fs-fxt-kinds">' + F.kinds.map(function (k) { return '<button type="button" class="fs-in-chip" data-k="' + k.k + '"><span>' + k.icon + '</span>' + esc(k.t) + '</button>'; }).join('') + '</div>';
      } else {
        h += '<div class="fs-fxt-chosen">' + kindOf(s.kind).icon + ' ' + esc(good.t) + ' <em>(' + esc(kindOf(s.kind).t) + ')</em></div><p>' + esc(s.why) + '</p>';
      }
      panel.innerHTML = h; panel.classList.add('open'); if (!reduceMotion) { panel.classList.remove('flash'); void panel.offsetWidth; panel.classList.add('flash'); }
      $$('.fs-fxt-fixes .fs-in-chip', panel).forEach(function (b) { b.addEventListener('click', function () { var f = s.fixes[+b.dataset.i]; if (!f.ok) { bounce(b, miss, f.miss); return; } st[s.id] = 1; saveJ('fixtown', st); SFX.chime(); open(s); }); });
      $$('.fs-fxt-kinds .fs-in-chip', panel).forEach(function (b) { b.addEventListener('click', function () { if (b.dataset.k !== s.kind) { bounce(b, miss, (s.kindMiss && s.kindMiss[b.dataset.k]) || 'Is it something people build, something living, or a plan people follow?'); return; } st[s.id] = 2; saveJ('fixtown', st); SFX.stamp(); open(s); upd(); }); });
      pins(); drawList();
    }
    function upd() {
      var n = F.spots.filter(function (s) { return stage(s.id) === 2; }).length;
      count.textContent = '🗺️ ' + n + ' of ' + F.spots.length + ' problems fixed'; count.classList.toggle('ok', n === F.spots.length);
      if (n === F.spots.length) askOnce(qh, F.q, F.opts, 'fixtown-q', win, F.win, F.clue, 'fixtown', miss);
      pins(); drawList();
    }
    panel.innerHTML = '<em>' + esc(F.startLine || 'Tap a problem on the list or a pin on the map.') + '</em>';
    at.parentNode.insertBefore(g, at.nextSibling);
    upd();
  }

  /* =================== 18.01: The Red Water Sample (zoom machine, tool pick, virtual microscope + lab report, hand lens) =================== */

  /* =================== 19.01: The Downhill Derby (flick drop, scrub the replay, pinball, slow motion, draw the path, radar gun) =================== */

  /* ---------- Warm-Up: "Flick to drop" — flick the marble down into a pan of flour (a model); the faster it falls, the bigger the crater (19.01) ----------
     D.flick = {afterText, kicker, title, todo[], why, alt, slowMax, fastMin, gentle:{t, v}, hard:{t, v}, slowLabel, fastLabel, midLine, meterLabel, unit,
                photo:{img, alt, cap, credit}, q, opts, win, clue}. Speed is 1–10 (a model, not mph). */
  function buildFlick() {
    var K = D.flick; if (!K) return;
    var at = anchorP(K.afterText); if (!at) { FAILED.push('flick anchor text not found'); return; }
    var g = gameShell(K.kicker || 'Warm-Up game', K.title, K.todo, K.why); g.dataset.mod = 'flick';
    var st = loadJ('flick', {}), TOPY = 52, HITY = 252;
    var stage = el('div', 'fs-fk-stage');
    stage.innerHTML = '<svg viewBox="0 0 600 330" class="fs-fk-svg" role="img" aria-label="' + esc(K.alt || 'A model: a marble held above a pan of flour') + '">' +
      '<defs><radialGradient id="fsFkM" cx="35%" cy="30%" r="70%"><stop offset="0" stop-color="#E9F6FF"/><stop offset=".45" stop-color="#4E9BD6"/><stop offset="1" stop-color="#173E73"/></radialGradient>' +
      '<radialGradient id="fsFkC" cx="50%" cy="40%" r="60%"><stop offset="0" stop-color="#C9BC9F"/><stop offset="1" stop-color="#EFE7D6"/></radialGradient></defs>' +
      '<rect x="0" y="0" width="600" height="330" fill="#FBF6EC"/>' +
      '<line x1="300" y1="70" x2="300" y2="236" class="fs-fk-guide"/>' +
      '<path d="M62 250 L538 250 L512 312 L88 312 Z" fill="#9AA6B2"/><path d="M62 250 L538 250 L534 260 L66 260 Z" fill="#C3CCD5"/>' +
      '<ellipse cx="300" cy="254" rx="232" ry="20" fill="#F7F2E6" stroke="#D9CDB4" stroke-width="2"/>' +
      '<g class="fs-fk-crater"></g><g class="fs-fk-puff"></g>' +
      '<g class="fs-fk-ball" style="cursor:grab"><circle cx="300" cy="' + TOPY + '" r="15" fill="url(#fsFkM)" stroke="#123056" stroke-width="1.5"/></g>' +
      '<text x="300" y="22" class="fs-fk-hint" text-anchor="middle">' + esc(K.flickHint || 'Press on the marble and flick DOWN') + '</text>' +
      '<g class="fs-fk-meter" transform="translate(556 40)"><rect x="0" y="0" width="18" height="200" rx="9" fill="#E8E1D2"/><rect class="fs-fk-mfill" x="0" y="200" width="18" height="0" rx="9" fill="#E8636B"/><text x="9" y="222" text-anchor="middle" class="fs-fk-mlbl">' + esc(K.meterLabel || 'speed') + '</text></g>' +
      '<text x="16" y="322" class="fs-fk-model">' + esc(K.model || 'a model') + '</text></svg>';
    var btns = el('div', 'fs-fk-btns', '<button type="button" class="fs-btn alt" data-v="' + K.gentle.v + '">🪶 ' + esc(K.gentle.t) + '</button><button type="button" class="fs-btn alt" data-v="' + K.hard.v + '">💨 ' + esc(K.hard.t) + '</button>');
    var read = el('div', 'fs-hs-card fs-fk-read', '<span class="fs-hs-n">⚪</span><div>' + esc(K.startLine || 'No drops yet.') + '</div>');
    var cards = el('div', 'fs-fk-cards', '<div class="fs-fk-card" data-k="slow"><b>' + esc(K.slowLabel || 'Slow drop') + '</b><span>—</span><svg viewBox="0 0 120 40"><ellipse cx="60" cy="20" rx="0" ry="0" class="fs-fk-cc"/></svg></div>' +
      '<div class="fs-fk-card" data-k="fast"><b>' + esc(K.fastLabel || 'Fast drop') + '</b><span>—</span><svg viewBox="0 0 120 40"><ellipse cx="60" cy="20" rx="0" ry="0" class="fs-fk-cc"/></svg></div>');
    var miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win'), photo = el('div', 'fs-fk-photo');
    g.appendChild(stage); g.appendChild(btns); g.appendChild(read); g.appendChild(cards); g.appendChild(miss); g.appendChild(qh); g.appendChild(win); g.appendChild(photo);
    var svg = $('svg', stage), ball = $('.fs-fk-ball', stage), bc = $('circle', ball), crater = $('.fs-fk-crater', stage), puff = $('.fs-fk-puff', stage), mfill = $('.fs-fk-mfill', stage), busy = false;
    function cm(v) { return +(1.8 + 0.55 * v).toFixed(1); }
    function rxOf(v) { return cm(v) * 9; }
    function meter(v) { var h = v * 20; mfill.setAttribute('y', 200 - h); mfill.setAttribute('height', h); }
    function smooth() { crater.innerHTML = ''; puff.innerHTML = ''; bc.setAttribute('cy', TOPY); bc.setAttribute('cx', 300); }
    function paintCards() {
      ['slow', 'fast'].forEach(function (k) {
        var c = $('.fs-fk-card[data-k="' + k + '"]', cards), v = st[k];
        c.classList.toggle('on', !!v);
        $('span', c).textContent = v ? (K.speedWord || 'Speed') + ' ' + v + ' of 10 · ' + (K.craterWord || 'crater') + ' ' + cm(v) + ' ' + (K.unit || 'cm') + ' ' + (K.wideWord || 'wide') : '—';
        var e = $('ellipse', c); e.setAttribute('rx', v ? cm(v) * 6 : 0); e.setAttribute('ry', v ? cm(v) * 1.8 : 0);
      });
      if (st.slow && st.fast) {
        askOnce(qh, K.q, K.opts, 'flick-q', win, K.win, K.clue, 'flick', miss);
        if (K.photo && !photo.innerHTML) photo.innerHTML = '<figure><img alt="' + esc(K.photo.alt) + '" src="' + esc(K.photo.img) + '"><figcaption>' + esc(K.photo.cap) + '</figcaption></figure>' + (K.photo.credit ? '<details class="fs-credit fs-credit-fold"><summary>📷 Photo credit</summary>' + esc(K.photo.credit) + '</details>' : '');
      }
    }
    function drop(v) {
      if (busy) return; busy = true; v = Math.max(1, Math.min(10, Math.round(v))); smooth(); meter(v); miss.classList.remove('show');
      var dur = reduceMotion ? 1 : Math.round(950 / Math.pow(v, 0.65)), t0 = null;
      SFX.whoosh();
      function fall(ts) {
        if (t0 == null) t0 = ts; var p = Math.min(1, (ts - t0) / dur), y = TOPY + (HITY - TOPY) * p * p;
        bc.setAttribute('cy', y.toFixed(1));
        if (p < 1) { requestAnimationFrame(fall); return; }
        hit(v);
      }
      requestAnimationFrame(fall);
    }
    function hit(v) {
      var rx = rxOf(v);
      crater.innerHTML = '<ellipse cx="300" cy="256" rx="' + (rx + 6) + '" ry="' + ((rx + 6) * 0.3).toFixed(1) + '" fill="#FFFDF7" stroke="#E2D6BC" stroke-width="1.5"/>' +
        '<ellipse cx="300" cy="257" rx="' + rx + '" ry="' + (rx * 0.27).toFixed(1) + '" fill="url(#fsFkC)"/>';
      bc.setAttribute('cy', 250);
      var n = 4 + v * 2, s = '';
      for (var i = 0; i < n; i++) { var a = Math.PI * (0.1 + 0.8 * (i / (n - 1))), d = 18 + v * 9 * (0.6 + Math.random() * 0.4); s += '<circle cx="300" cy="250" r="' + (2 + Math.random() * 3).toFixed(1) + '" fill="#FFFCF3" stroke="#E6DCC7" style="--dx:' + (-Math.cos(a) * d).toFixed(0) + 'px;--dy:' + (-Math.sin(a) * d * 0.8).toFixed(0) + 'px"/>'; }
      puff.innerHTML = s; puff.classList.remove('go'); void puff.getBoundingClientRect(); puff.classList.add('go');
      tone(140 - v * 4, 0, 0.12 + v * 0.02, 'sine', 0.05 + v * 0.012); noise(0.08 + v * 0.02, 300, 1600, 0.12 + v * 0.05);
      var k = v <= K.slowMax ? 'slow' : (v >= K.fastMin ? 'fast' : null);
      $('div', read).innerHTML = '<b>' + esc((K.speedWord || 'Speed') + ' ' + v + ' of 10') + '</b>' + esc((K.craterWord || 'crater') + ': ' + cm(v) + ' ' + (K.unit || 'cm') + ' ' + (K.wideWord || 'wide') + '. ') + (k ? '' : esc(K.midLine || ''));
      if (k) { st[k] = v; saveJ('flick', st); SFX.chime(); }
      setTimeout(function () { busy = false; paintCards(); }, reduceMotion ? 0 : 500);
    }
    /* flick: the marble follows the pointer down; letting go with a fast downward swipe = a fast drop */
    var pts = null, holding = false;
    function svgY(e) { var r = svg.getBoundingClientRect(); return (e.clientY - r.top) * 330 / r.height; }
    ball.addEventListener('pointerdown', function (e) { if (busy) return; e.preventDefault(); holding = true; pts = [[performance.now(), svgY(e)]]; smooth(); ball.setPointerCapture && ball.setPointerCapture(e.pointerId); ball.style.cursor = 'grabbing'; });
    ball.addEventListener('pointermove', function (e) {
      if (!holding) return; var y = Math.max(TOPY - 20, Math.min(TOPY + 60, svgY(e))); pts.push([performance.now(), svgY(e)]); if (pts.length > 12) pts.shift();
      bc.setAttribute('cy', y.toFixed(1));
    });
    function letGo() {
      if (!holding) return; holding = false; ball.style.cursor = 'grab';
      var now = performance.now(), recent = pts.filter(function (p) { return now - p[0] < 120; }); if (recent.length < 2) recent = pts.slice(-2);
      var a = recent[0], b = recent[recent.length - 1], vy = b && a && b[0] > a[0] ? (b[1] - a[1]) / (b[0] - a[0]) : 0;
      var v = vy <= 0.05 ? 1 : 1 + vy * 5;
      drop(v);
    }
    ball.addEventListener('pointerup', letGo); ball.addEventListener('pointercancel', function () { holding = false; });
    $$('button', btns).forEach(function (b) { b.addEventListener('click', function () { drop(+b.dataset.v); }); });
    at.parentNode.insertBefore(g, at.nextSibling);
    paintCards();
  }

  /* ---------- Lesson Part 1: "Scrub the replay" — a marble rolls into a pencil (a drawn model, 4 frames); at each frame tap every place the energy is right now (19.01) ----------
     D.replay = {afterText, kicker, title, todo[], why, model, places:[{k, icon, t}], frames:[{cap, m, p, mv, pv, sound, warm, ans:[k], allow:[k], hint, gone, ok}], checkBtn, q, opts, win, clue} */
  function buildReplay() {
    var R = D.replay; if (!R) return;
    var at = anchorP(R.afterText); if (!at) { FAILED.push('replay anchor text not found'); return; }
    var g = gameShell(R.kicker || 'Part 1 game', R.title, R.todo, R.why); g.dataset.mod = 'replay';
    var F = R.frames, st = loadJ('replay', { done: 0 }), cur = Math.min(st.done, F.length - 1), sel = {};
    var scene = el('div', 'fs-rpl-scene');
    scene.innerHTML = '<svg viewBox="0 0 600 210" role="img" aria-label="' + esc(R.alt || 'A model: a marble rolling toward a pencil on a table') + '">' +
      '<defs><radialGradient id="fsRplM" cx="35%" cy="30%" r="70%"><stop offset="0" stop-color="#E9F6FF"/><stop offset=".45" stop-color="#4E9BD6"/><stop offset="1" stop-color="#173E73"/></radialGradient></defs>' +
      '<rect width="600" height="210" fill="#FBF6EC"/><rect x="0" y="170" width="600" height="40" fill="#C99B67"/><rect x="0" y="170" width="600" height="6" fill="#B07F4C"/>' +
      '<g class="fs-rpl-warm"><path d="M0 0 q6 -8 0 -16 q-6 -8 0 -16" /><path d="M14 0 q6 -8 0 -16 q-6 -8 0 -16"/><path d="M28 0 q6 -8 0 -16 q-6 -8 0 -16"/></g>' +
      '<g class="fs-rpl-pencil"><g class="fs-rpl-plines"><line x1="-14" y1="-6" x2="-40" y2="-6"/><line x1="-14" y1="4" x2="-34" y2="4"/></g><rect x="0" y="-9" width="104" height="14" rx="2" fill="#F5C33B" stroke="#8A6512" stroke-width="1.5"/><rect x="0" y="-9" width="14" height="14" fill="#E8A2A8" stroke="#8A6512" stroke-width="1.5"/><path d="M104 -9 L126 -2 L104 5 Z" fill="#EBD3A8" stroke="#8A6512" stroke-width="1.5"/><path d="M119 -4 L126 -2 L119 0Z" fill="#333"/></g>' +
      '<g class="fs-rpl-marble"><g class="fs-rpl-mlines"><line x1="-18" y1="-4" x2="-48" y2="-4"/><line x1="-18" y1="6" x2="-40" y2="6"/></g><circle r="12" fill="url(#fsRplM)" stroke="#123056" stroke-width="1.5"/></g>' +
      '<g class="fs-rpl-sound"><path d="M0 -30 q14 14 0 28"/><path d="M10 -40 q22 22 0 46"/><text x="-14" y="-46">CLICK!</text></g>' +
      '<text x="12" y="200" class="fs-rpl-model">' + esc(R.model || 'a model') + '</text></svg>';
    var strip = el('div', 'fs-rpl-strip');
    var range = el('input'); range.type = 'range'; range.min = 0; range.max = F.length - 1; range.step = 1; range.className = 'fs-rpl-range'; range.setAttribute('aria-label', R.rangeLabel || 'Replay frame');
    var nav = el('div', 'fs-rpl-nav', '<button type="button" class="fs-btn alt fs-rpl-prev">◀</button><div class="fs-rpl-cap"></div><button type="button" class="fs-btn alt fs-rpl-next">▶</button>');
    var ask = el('div', 'fs-sv-q fs-rpl-ask'), miss = el('div', 'fs-miss'), okBox = el('div', 'fs-hs-card fs-rpl-ok'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(scene); g.appendChild(range); g.appendChild(strip); g.appendChild(nav); g.appendChild(ask); g.appendChild(miss); g.appendChild(okBox); g.appendChild(qh); g.appendChild(win);
    var mar = $('.fs-rpl-marble', scene), pen = $('.fs-rpl-pencil', scene), snd = $('.fs-rpl-sound', scene), warm = $('.fs-rpl-warm', scene);
    function draw(f) {
      mar.setAttribute('transform', 'translate(' + f.m + ' 158)'); pen.setAttribute('transform', 'translate(' + f.p + ' 163)');
      mar.classList.toggle('moving', !!f.mv); pen.classList.toggle('moving', !!f.pv);
      snd.setAttribute('transform', 'translate(' + (f.m + 14) + ' 150)'); snd.classList.toggle('on', !!f.sound);
      warm.setAttribute('transform', 'translate(' + (f.p + 30) + ' 166)'); warm.classList.toggle('on', !!f.warm);
    }
    function paint() {
      var f = F[cur]; draw(f); range.value = cur; range.max = F.length - 1;
      strip.innerHTML = F.map(function (x, i) { return '<button type="button" data-i="' + i + '" class="' + (i === cur ? 'on ' : '') + (i < st.done ? 'done' : (i > st.done ? 'locked' : '')) + '">' + (i < st.done ? '✓' : (i > st.done ? '🔒' : i + 1)) + '</button>'; }).join('');
      $$('button', strip).forEach(function (b) { b.addEventListener('click', function () { go(+b.dataset.i); }); });
      $('.fs-rpl-cap', nav).innerHTML = '<b>' + esc((R.frameWord || 'Frame') + ' ' + (cur + 1) + ' of ' + F.length) + '</b> ' + esc(f.cap);
      $('.fs-rpl-prev', nav).disabled = cur === 0; $('.fs-rpl-next', nav).disabled = cur >= Math.min(st.done, F.length - 1);
      var solved = cur < st.done; sel = {};
      ask.innerHTML = '<div class="fs-in-k">' + esc(R.ask || 'Where is the energy right now? Tap every place.') + '</div><div class="fs-in-chips">' + R.places.map(function (p) { return '<button type="button" class="fs-in-chip" data-k="' + p.k + '">' + p.icon + ' ' + esc(p.t) + '</button>'; }).join('') + '</div>' +
        (solved ? '' : '<button type="button" class="fs-btn fs-rpl-check">' + esc(R.checkBtn || 'Check') + '</button>');
      $$('.fs-in-chip', ask).forEach(function (c) {
        if (solved && (f.ans.indexOf(c.dataset.k) > -1)) c.classList.add('on', 'ok');
        c.addEventListener('click', function () { if (cur < st.done) return; var k = c.dataset.k; sel[k] = !sel[k]; c.classList.toggle('on', sel[k]); SFX.blip(); });
      });
      var chk = $('.fs-rpl-check', ask); if (chk) chk.addEventListener('click', check);
      okBox.style.display = solved ? '' : 'none'; if (solved) okBox.innerHTML = '<span class="fs-hs-n">✓</span><div>' + esc(f.ok) + '</div>';
      miss.classList.remove('show');
      if (st.done >= F.length) askOnce(qh, R.q, R.opts, 'replay-q', win, R.win, R.clue, 'replay', miss);
    }
    function check() {
      var f = F[cur], picked = Object.keys(sel).filter(function (k) { return sel[k]; }), allow = f.allow || [];
      if (!picked.length) { showMiss(miss, R.pickOne || 'Tap at least one place first.'); return; }
      if (sel.gone && f.gone) { bounce($('.fs-in-chip[data-k="gone"]', ask), miss, f.gone); return; }
      var missing = f.ans.filter(function (k) { return !sel[k]; }), extra = picked.filter(function (k) { return f.ans.indexOf(k) < 0 && allow.indexOf(k) < 0; });
      if (missing.length || extra.length) { bounce($('.fs-rpl-check', ask), miss, f.hint); return; }
      st.done = Math.max(st.done, cur + 1); saveJ('replay', st); SFX.chime();
      if (cur < F.length - 1) { paint(); okBox.classList.remove('flash'); void okBox.offsetWidth; okBox.classList.add('flash'); } else paint();
    }
    function go(i) { if (i < 0 || i > Math.min(st.done, F.length - 1)) return; cur = i; SFX.blip(); paint(); }
    range.addEventListener('input', function () { var i = +range.value; if (i > Math.min(st.done, F.length - 1)) { range.value = cur; showMiss(miss, R.lockLine || 'Answer this frame first. Then the next one opens.'); return; } cur = i; paint(); });
    $('.fs-rpl-prev', nav).addEventListener('click', function () { go(cur - 1); });
    $('.fs-rpl-next', nav).addEventListener('click', function () { go(cur + 1); });
    at.parentNode.insertBefore(g, at.nextSibling);
    paint();
  }

  /* ---------- Lesson Part 2: "Pinball" — pull the plunger (drag it, or tap a pull), predict the light the ball will reach, launch; the ball climbs a tilted table
     to a height set by its energy (pull² for a spring). Round 2: a big slow ball vs a small fast ball at the drop targets (19.01) ----------
     D.pinball = {afterText, replace, kicker, title, todo[], why, model, pulls:[{k, t, f}], rows:[{k, t, h, pts}], predictQ, noneT, launchBtn, needLine, startLine,
                  round2:{title, todo, q1, balls:[{k, icon, name, sub, knock, line}], runBtn, why}, q, opts, win, clue} */
  function buildPinball() {
    var B = D.pinball; if (!B) return;
    var at = anchorP(B.afterText); if (!at) { FAILED.push('pinball anchor text not found'); return; }
    if (B.replace) $$(B.replace).forEach(function (r) { r.classList.add('fs-replaced'); });
    var g = gameShell(B.kicker || 'Part 2 game', B.title, B.todo, B.why); g.dataset.mod = 'pinball';
    var st = loadJ('pinball', { runs: {}, r2: '' }), pull = 0, pred = null, busy = false, TOP = 52, BOT = 420, LX = 252;
    function yOf(h) { return BOT - h * (BOT - TOP); }
    var rows = B.rows.map(function (r, i) { return '<g class="fs-pb-row" data-k="' + r.k + '"><line x1="38" y1="' + yOf(r.h) + '" x2="240" y2="' + yOf(r.h) + '" class="fs-pb-rl"/>' +
      [0, 1, 2].map(function (j) { return '<circle cx="' + (70 + j * 60) + '" cy="' + (yOf(r.h) - 0) + '" r="11" class="fs-pb-lt"/>'; }).join('') +
      '<text x="44" y="' + (yOf(r.h) - 15) + '" class="fs-pb-rt">' + esc(r.t) + ' · ' + r.pts + '</text></g>'; }).join('');
    var tbl = el('div', 'fs-pb-wrap');
    tbl.innerHTML = '<svg viewBox="0 0 300 500" class="fs-pb-svg" role="img" aria-label="' + esc(B.alt || 'A model pinball table tilted up, with a plunger lane on the right and three rows of lights') + '">' +
      '<defs><linearGradient id="fsPbT" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1E2A6B"/><stop offset="1" stop-color="#3B1E5E"/></linearGradient><radialGradient id="fsPbB" cx="35%" cy="30%" r="70%"><stop offset="0" stop-color="#fff"/><stop offset=".5" stop-color="#C9D1DA"/><stop offset="1" stop-color="#6B7682"/></radialGradient></defs>' +
      '<path d="M20 488 L20 70 Q20 22 70 22 L230 22 Q280 22 280 70 L280 488 Z" fill="url(#fsPbT)" stroke="#F5B83D" stroke-width="5"/>' +
      '<line x1="240" y1="488" x2="240" y2="90" stroke="#F5B83D" stroke-width="3"/>' +
      '<circle cx="90" cy="440" r="14" class="fs-pb-bump"/><circle cx="190" cy="452" r="12" class="fs-pb-bump"/>' + rows +
      '<g class="fs-pb-flag"><path d="M0 0 L0 -22 L16 -16 L0 -10" fill="#F5B83D" stroke="#fff"/></g>' +
      '<g class="fs-pb-plunger"><rect x="' + (LX - 7) + '" y="440" width="14" height="40" rx="4" fill="#C0C7CF"/><path class="fs-pb-spring" d="" fill="none" stroke="#E8EDF2" stroke-width="2.5"/><rect class="fs-pb-knob" x="' + (LX - 13) + '" y="476" width="26" height="14" rx="6" fill="#E8636B" stroke="#fff" stroke-width="2" style="cursor:grab"/></g>' +
      '<circle class="fs-pb-ball" cx="' + LX + '" cy="' + (BOT + 8) + '" r="9" fill="url(#fsPbB)"/>' +
      '<text x="150" y="498" text-anchor="middle" class="fs-pb-model">' + esc(B.model || 'a model') + '</text></svg>' +
      '<div class="fs-pb-side"><div class="fs-in-k">' + esc(B.pullLabel || '1. Pull the plunger') + '</div><div class="fs-in-chips fs-pb-pulls">' + B.pulls.map(function (p) { return '<button type="button" class="fs-in-chip" data-f="' + p.f + '">' + esc(p.t) + '</button>'; }).join('') + '</div>' +
      '<div class="fs-pb-pullread"></div>' +
      '<div class="fs-in-k">' + esc(B.predictQ || '2. Predict: which light will the ball reach?') + '</div><div class="fs-in-chips fs-pb-preds">' + B.rows.slice().reverse().map(function (r) { return '<button type="button" class="fs-in-chip" data-k="' + r.k + '">' + esc(r.t) + '</button>'; }).join('') + '<button type="button" class="fs-in-chip" data-k="none">' + esc(B.noneT || 'None of them') + '</button></div>' +
      '<button type="button" class="fs-btn fs-pb-go">🚀 ' + esc(B.launchBtn || '3. Let go!') + '</button><div class="fs-pb-log"></div></div>';
    var info = el('div', 'fs-hs-card fs-pb-info', '<span class="fs-hs-n">🎯</span><div>' + esc(B.startLine || '') + '</div>'), miss = el('div', 'fs-miss'), r2 = el('div', 'fs-pb-r2'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(tbl); g.appendChild(info); g.appendChild(miss); g.appendChild(r2); g.appendChild(qh); g.appendChild(win);
    var svg = $('svg', tbl), knob = $('.fs-pb-knob', tbl), spring = $('.fs-pb-spring', tbl), ball = $('.fs-pb-ball', tbl), flag = $('.fs-pb-flag', tbl), goB = $('.fs-pb-go', tbl);
    function bucket(f) { return f < 0.45 ? B.pulls[0].k : (f < 0.8 ? B.pulls[1].k : B.pulls[2].k); }
    function reach(h) { var k = 'none'; B.rows.forEach(function (r) { if (h >= r.h - 0.005) k = r.k; }); return k; }
    function drawPull(f) {
      var y = 440 + 36 * f, s = 'M' + LX + ' 420'; for (var i = 1; i <= 8; i++) s += ' L' + (LX + (i % 2 ? 6 : -6)) + ' ' + (420 + (y - 420) * i / 8).toFixed(1);
      spring.setAttribute('d', s); knob.setAttribute('y', y); ball.setAttribute('cy', (BOT + 8 + 26 * f).toFixed(1));
      $('.fs-pb-pullread', tbl).innerHTML = f > 0 ? '<b>' + esc(B.pullWord || 'Pull') + ': ' + Math.round(f * 100) + '%</b> <span>' + esc((B.pulls.filter(function (p) { return p.k === bucket(f); })[0] || {}).t || '') + '</span>' : '';
      $$('.fs-pb-pulls .fs-in-chip', tbl).forEach(function (c) { c.classList.toggle('on', f > 0 && Math.abs(+c.dataset.f - f) < 0.02); });
    }
    function setPred(k) { pred = k; $$('.fs-pb-preds .fs-in-chip', tbl).forEach(function (c) { c.classList.toggle('on', c.dataset.k === k); });
      var r = B.rows.filter(function (x) { return x.k === k; })[0]; flag.style.display = r ? '' : 'none'; if (r) flag.setAttribute('transform', 'translate(226 ' + yOf(r.h) + ')'); }
    function lights(h) { $$('.fs-pb-row', tbl).forEach(function (g2) { var r = B.rows.filter(function (x) { return x.k === g2.dataset.k; })[0]; g2.classList.toggle('lit', h >= r.h - 0.005); }); }
    function log() {
      $('.fs-pb-log', tbl).innerHTML = B.pulls.map(function (p) { var r = st.runs[p.k]; return '<div class="' + (r ? 'ok' : '') + '">' + (r ? '✓ ' : '◻ ') + esc(p.t) + (r ? ': ' + esc((B.rows.filter(function (x) { return x.k === r; })[0] || { t: B.noneT || 'none' }).t) : '') + '</div>'; }).join('');
      var all = B.pulls.every(function (p) { return st.runs[p.k]; }); if (all) round2();
    }
    function launch() {
      if (busy) return;
      if (!(pull > 0.05)) { showMiss(miss, B.needPull || 'Pull the plunger back first.'); return; }
      if (!pred) { showMiss(miss, B.needPred || 'Make a prediction first: tap the light you think it will reach.'); return; }
      busy = true; miss.classList.remove('show'); lights(-1);
      var f = pull, h = Math.min(1.04, f * f), peak = yOf(h), start = BOT + 8 + 26 * f, t0 = null, up = reduceMotion ? 1 : 260 + 900 * Math.sqrt(h), k = reach(h);
      drawPull(0); SFX.snap(); tone(220 + 500 * f, 0, 0.2, 'triangle', 0.05);
      function anim(ts) {
        if (t0 == null) t0 = ts; var p = Math.min(1, (ts - t0) / up), e = 1 - (1 - p) * (1 - p), y = start + (peak - start) * e;
        ball.setAttribute('cy', y.toFixed(1)); lights((BOT - y) / (BOT - TOP));
        if (p < 1) { requestAnimationFrame(anim); return; }
        setTimeout(function () { fallBack(peak, k, f, h); }, 380);
      }
      requestAnimationFrame(anim);
    }
    function fallBack(peak, k, f, h) {
      var t0 = null, dn = reduceMotion ? 1 : 260 + 900 * Math.sqrt(h);
      function anim(ts) { if (t0 == null) t0 = ts; var p = Math.min(1, (ts - t0) / dn), y = peak + (BOT + 8 - peak) * p * p; ball.setAttribute('cy', y.toFixed(1)); if (p < 1) requestAnimationFrame(anim); else done(k, f); }
      requestAnimationFrame(anim);
    }
    function done(k, f) {
      busy = false; var row = B.rows.filter(function (x) { return x.k === k; })[0], right = pred === k;
      var line = (row ? (B.reachedLine || 'It reached {row}!').replace('{row}', row.t) : (B.noneLine || 'It didn’t reach any light.')) + ' ' + (right ? (B.rightLine || 'Your prediction was right.') : (B.wrongLine || 'Not what you predicted. That’s what tests are for!'));
      $('div', info).innerHTML = '<b>' + esc((B.pulls.filter(function (p) { return p.k === bucket(f); })[0] || {}).t || '') + '</b>' + esc(line) + (row ? ' <span class="fs-pb-pts">+' + row.pts + '</span>' : '');
      info.classList.remove('flash'); void info.offsetWidth; info.classList.add('flash');
      if (row) SFX.sparkle(); else SFX.thud();
      st.runs[bucket(f)] = k; saveJ('pinball', st); pull = 0; pred = null; setPred(null); log();
    }
    /* drag the knob down to pull (or tap a pull chip); letting go of the knob after a drag launches if there is a prediction */
    var dragging = false;
    knob.addEventListener('pointerdown', function (e) { if (busy) return; e.preventDefault(); dragging = true; knob.setPointerCapture && knob.setPointerCapture(e.pointerId); });
    knob.addEventListener('pointermove', function (e) { if (!dragging) return; var r = svg.getBoundingClientRect(), y = (e.clientY - r.top) * 500 / r.height; pull = Math.max(0, Math.min(1, (y - 440) / 36)); drawPull(pull); });
    knob.addEventListener('pointerup', function () { if (!dragging) return; dragging = false; if (pull > 0.05 && pred) launch(); else if (pull > 0.05) showMiss(miss, B.holdLine || 'Good pull! Now predict which light it will reach, then press Let go.'); });
    $$('.fs-pb-pulls .fs-in-chip', tbl).forEach(function (c) { c.addEventListener('click', function () { if (busy) return; pull = +c.dataset.f; drawPull(pull); SFX.blip(); }); });
    $$('.fs-pb-preds .fs-in-chip', tbl).forEach(function (c) { c.addEventListener('click', function () { if (busy) return; setPred(c.dataset.k); SFX.blip(); }); });
    goB.addEventListener('click', launch);
    /* round 2: big and slow vs small and fast */
    function round2() {
      if (r2.dataset.on) return; r2.dataset.on = '1'; var R = B.round2;
      r2.innerHTML = '<div class="fs-game-k">' + esc(R.kicker || 'Round 2') + '</div><div class="fs-pb-r2t">' + esc(R.title) + '</div>' + (R.todo ? '<ul class="fs-todo">' + R.todo.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>' : '') +
        '<div class="fs-pb-lanes">' + R.balls.map(function (b) { return '<button type="button" class="fs-pb-lane" data-k="' + b.k + '"><span class="fs-pb-ic">' + b.icon + '</span><b>' + esc(b.name) + '</b><small>' + esc(b.sub) + '</small><span class="fs-pb-tg"><i></i><i></i><i></i></span><em></em></button>'; }).join('') + '</div>' +
        '<div class="fs-in-k">' + esc(R.q1) + '</div><button type="button" class="fs-btn fs-pb-run">▶ ' + esc(R.runBtn || 'Run the test') + '</button>' + (R.why ? '<div class="fs-hs-card fs-pb-why" style="display:none"><span class="fs-hs-n">⚡</span><div>' + esc(R.why) + '</div></div>' : '');
      var pick = st.r2pick || null;
      function paintPick() { $$('.fs-pb-lane', r2).forEach(function (l) { l.classList.toggle('on', l.dataset.k === pick); }); }
      $$('.fs-pb-lane', r2).forEach(function (l) { l.addEventListener('click', function () { if (st.r2) return; pick = l.dataset.k; paintPick(); SFX.blip(); }); });
      function show(anim) {
        R.balls.forEach(function (b) { var l = $('.fs-pb-lane[data-k="' + b.k + '"]', r2); l.classList.add('ran', b.knock ? 'knock' : 'wobble'); if (!anim) l.classList.add('still'); $('em', l).textContent = b.line; });
        $('.fs-pb-run', r2).style.display = 'none'; var w = $('.fs-pb-why', r2); if (w) w.style.display = '';
        askOnce(qh, B.q, B.opts, 'pinball-q', win, B.win, B.clue, 'pinball', miss);
      }
      $('.fs-pb-run', r2).addEventListener('click', function () {
        if (!pick) { showMiss(miss, R.needPick || 'Predict first: tap the ball you think will knock the targets down.'); return; }
        st.r2 = 1; st.r2pick = pick; saveJ('pinball', st); miss.classList.remove('show'); SFX.whoosh(); setTimeout(function () { SFX.pop(); }, 600);
        var right = R.balls.filter(function (b) { return b.knock; })[0].k === pick;
        show(true); showMiss(miss, right ? (R.right || 'Your prediction was right!') : (R.wrong || 'Surprise! Look at what happened.')); miss.classList.toggle('fs-pb-good', right);
      });
      paintPick(); if (st.r2) show(false);
    }
    at.parentNode.insertBefore(g, at.nextSibling);
    drawPull(0); setPred(null); log();
  }

  /* ---------- Lesson Part 3: "Slow motion" — a real high-speed photo sequence played like a flip book (not a clue) (19.01) ----------
     D.slowmo = {afterText, kicker, title, todo[], why, strip, n, alt, caps:[{from, t}], playBtn, againBtn, q, opts, credit, win} (strip = one image, n frames side by side) */
  function buildSlowmo() {
    var S = D.slowmo; if (!S) return;
    var at = anchorP(S.afterText); if (!at) { FAILED.push('slowmo anchor text not found'); return; }
    var g = gameShell(S.kicker || 'Slow motion', S.title, S.todo, S.why); g.dataset.mod = 'slowmo';
    var view = el('div', 'fs-smo-view', '<div class="fs-smo-img" role="img" aria-label="' + esc(S.alt) + '"></div><span class="fs-smo-n"></span><span class="fs-smo-rec">● ' + esc(S.rec || 'HIGH-SPEED CAMERA') + '</span>');
    var range = el('input'); range.type = 'range'; range.min = 0; range.max = S.n - 1; range.step = 1; range.value = 0; range.className = 'fs-smo-range'; range.setAttribute('aria-label', S.rangeLabel || 'Frame');
    var ctl = el('div', 'fs-smo-ctl', '<button type="button" class="fs-btn fs-smo-play">▶ ' + esc(S.playBtn || 'Play in slow motion') + '</button><div class="fs-smo-cap"></div>');
    var miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(view); g.appendChild(range); g.appendChild(ctl); g.appendChild(miss); g.appendChild(qh); g.appendChild(win);
    if (S.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credit</summary>' + esc(S.credit)));
    var img = $('.fs-smo-img', view), num = $('.fs-smo-n', view), cap = $('.fs-smo-cap', ctl), play = $('.fs-smo-play', ctl), timer = null, cur = 0;
    img.style.backgroundImage = 'url("' + S.strip + '")'; img.style.backgroundSize = (S.n * 100) + '% 100%';
    function show(i) {
      cur = i; range.value = i; img.style.backgroundPosition = (S.n > 1 ? i / (S.n - 1) * 100 : 0) + '% 0';
      num.textContent = (S.frameWord || 'Frame') + ' ' + (i + 1) + ' / ' + S.n;
      var c = ''; S.caps.forEach(function (x) { if (i >= x.from) c = x.t; }); cap.textContent = c;
      if (i === S.n - 1) { store('slowmo-seen', '1'); askOnce(qh, S.q, S.opts, 'slowmo-q', win, S.win, null, 'slowmo', miss); }
    }
    function stop() { clearInterval(timer); timer = null; view.classList.remove('on'); play.textContent = '▶ ' + (cur === S.n - 1 ? (S.againBtn || 'Play it again') : (S.playBtn || 'Play in slow motion')); }
    play.addEventListener('click', function () {
      if (timer) { stop(); return; }
      if (cur >= S.n - 1) show(0); view.classList.add('on'); play.textContent = '❚❚ ' + (S.pauseBtn || 'Pause'); SFX.blip();
      timer = setInterval(function () { if (cur >= S.n - 1) { stop(); return; } show(cur + 1); }, reduceMotion ? 700 : (S.ms || 330));
    });
    range.addEventListener('input', function () { if (timer) stop(); show(+range.value); });
    at.parentNode.insertBefore(g, at.nextSibling);
    show(0); if (store('slowmo-seen')) askOnce(qh, S.q, S.opts, 'slowmo-q', win, S.win, null, 'slowmo', miss);
  }

  /* ---------- Lesson Part 4: "Draw the path" — draw a derby hill from a Low, Middle or High start (drag to draw, or tap to place points), press Play; the car's
     speed comes from how far it has dropped (a little lost to rubbing); at the bottom it pushes a hay bale; measure the push with the tape; after all three
     starts, drag each bar of the chart to match; then a chip question (19.01) ----------
     D.drawpath = {afterText, kicker, title, todo[], why, model, starts:[{k, t, h}], unit, scale (inches per unit of drop), loss, playBtn, eraseBtn, lines:{…}, chartQ, q, opts, win, clue} */
  function buildDrawpath() {
    var P = D.drawpath; if (!P) return;
    var at = anchorP(P.afterText); if (!at) { FAILED.push('drawpath anchor text not found'); return; }
    var g = gameShell(P.kicker || 'Part 4 game', P.title, P.todo, P.why); g.dataset.mod = 'drawpath';
    var L = P.lines || {}, W = 640, H = 340, FLOOR = 300, TX = 70, BALE = 452, PX_IN = 4.2, st = loadJ('drawpath', { runs: {}, bars: {} });
    function yOfH(h) { return FLOOR - h * 240; }
    var marks = P.starts.map(function (s) { return '<g class="fs-dp-mark" data-k="' + s.k + '"><line x1="20" y1="' + yOfH(s.h) + '" x2="' + (TX + 6) + '" y2="' + yOfH(s.h) + '"/><circle cx="' + TX + '" cy="' + yOfH(s.h) + '" r="9"/><text x="18" y="' + (yOfH(s.h) - 12) + '">' + esc(s.t) + '</text></g>'; }).join('');
    var ticks = ''; for (var i = 0; i <= 8; i++) ticks += '<line x1="' + (BALE + 40 + i * 5 * PX_IN) + '" y1="' + (FLOOR + 2) + '" x2="' + (BALE + 40 + i * 5 * PX_IN) + '" y2="' + (FLOOR + (i % 2 ? 8 : 12)) + '"/>' + (i % 2 ? '' : '<text x="' + (BALE + 40 + i * 5 * PX_IN) + '" y="' + (FLOOR + 36) + '">' + (i * 5) + '</text>');
    var box = el('div', 'fs-dp-box');
    box.innerHTML = '<svg viewBox="0 0 ' + W + ' ' + H + '" class="fs-dp-svg" role="img" aria-label="' + esc(P.alt || 'A drawing area: a start tower on the left with three start marks, the ground, and a hay bale on the right') + '">' +
      '<rect width="' + W + '" height="' + H + '" fill="#EAF4FB"/><rect x="0" y="' + FLOOR + '" width="' + W + '" height="' + (H - FLOOR) + '" fill="#E9D8A6"/><line x1="0" y1="' + FLOOR + '" x2="' + W + '" y2="' + FLOOR + '" stroke="#B9A06A" stroke-width="3"/>' +
      '<rect x="' + (TX - 14) + '" y="40" width="10" height="' + (FLOOR - 40) + '" fill="#A7B4C2"/>' + marks +
      '<g class="fs-dp-ticks">' + ticks + '</g>' +
      '<polyline class="fs-dp-path" points=""/><g class="fs-dp-dots"></g>' +
      '<g class="fs-dp-bale"><rect x="0" y="-30" width="40" height="30" rx="4" fill="#E2B84A" stroke="#9A7420" stroke-width="2"/><path d="M4 -22 H36 M4 -14 H36 M4 -6 H36" stroke="#B48A2A" stroke-width="2"/></g>' +
      '<g class="fs-dp-tape"><line class="fs-dp-tl" x1="0" y1="0" x2="0" y2="0"/><circle class="fs-dp-th" r="9"/><text class="fs-dp-tt" x="0" y="0"></text></g>' +
      '<g class="fs-dp-car"><path d="M-14 -6 Q-12 -14 0 -14 Q12 -14 16 -6 Z" fill="#E8636B" stroke="#7A2A30" stroke-width="1.5"/><circle cx="-9" cy="-3" r="4" fill="#333"/><circle cx="10" cy="-3" r="4" fill="#333"/></g>' +
      '<text x="' + (W - 10) + '" y="22" text-anchor="end" class="fs-dp-model">' + esc(P.model || 'a model') + '</text><text x="' + (W / 2) + '" y="22" text-anchor="middle" class="fs-dp-hint"></text></svg>';
    var ctl = el('div', 'fs-dp-ctl', '<button type="button" class="fs-btn fs-dp-play">▶ ' + esc(P.playBtn || 'Play') + '</button><button type="button" class="fs-btn alt fs-dp-erase">🧽 ' + esc(P.eraseBtn || 'Erase my track') + '</button><div class="fs-dp-speed"></div>');
    var table = el('div', 'fs-dp-table'), chart = el('div', 'fs-dp-chart'), miss = el('div', 'fs-miss'), info = el('div', 'fs-hs-card fs-dp-info', '<span class="fs-hs-n">✏️</span><div>' + esc(L.start || '') + '</div>'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(box); g.appendChild(ctl); g.appendChild(info); g.appendChild(miss); g.appendChild(table); g.appendChild(chart); g.appendChild(qh); g.appendChild(win);
    var svg = $('svg', box), poly = $('.fs-dp-path', box), dots = $('.fs-dp-dots', box), car = $('.fs-dp-car', box), bale = $('.fs-dp-bale', box), tape = $('.fs-dp-tape', box), hint = $('.fs-dp-hint', box), speedBox = $('.fs-dp-speed', ctl);
    var pts = [], startK = null, drawing = false, tapMode = false, busy = false, pending = null, downAt = null;
    function sp(e) { var r = svg.getBoundingClientRect(); return { x: (e.clientX - r.left) * W / r.width, y: (e.clientY - r.top) * H / r.height }; }
    function render() {
      poly.setAttribute('points', pts.map(function (p) { return p.x.toFixed(1) + ',' + p.y.toFixed(1); }).join(' '));
      dots.innerHTML = tapMode ? pts.map(function (p) { return '<circle cx="' + p.x.toFixed(1) + '" cy="' + p.y.toFixed(1) + '" r="4"/>'; }).join('') : '';
      $$('.fs-dp-mark', box).forEach(function (m) { m.classList.toggle('on', m.dataset.k === startK); });
    }
    function placeBale(x) { bale.setAttribute('transform', 'translate(' + x + ' ' + FLOOR + ')'); }
    function placeCar(x, y, a) { car.setAttribute('transform', 'translate(' + x.toFixed(1) + ' ' + y.toFixed(1) + ') rotate(' + (a || 0).toFixed(1) + ')'); }
    function reset() { pts = []; startK = null; drawing = false; tapMode = false; pending = null; tape.style.display = 'none'; placeBale(BALE); placeCar(TX, FLOOR - 250, 0); car.style.display = 'none'; hint.textContent = L.hint || 'Start at a flag on the tower'; render(); speedBox.textContent = ''; }
    function snapStart(p) {
      if (p.x > TX + 60) return null; var best = null;
      P.starts.forEach(function (s) { var d = Math.abs(p.y - yOfH(s.h)); if (d < 26 && (!best || d < best.d)) best = { s: s, d: d }; });
      return best ? best.s : null;
    }
    function finished() { return pts.length > 1 && pts[pts.length - 1].y >= FLOOR - 12; }
    function closeTrack() { var last = pts[pts.length - 1]; last.y = FLOOR; pts.push({ x: Math.max(last.x + 1, BALE - 2), y: FLOOR }); hint.textContent = L.ready || 'Track ready. Press Play!'; render(); }
    svg.addEventListener('pointerdown', function (e) {
      if (busy || pending) return; var p = sp(e); downAt = { p: p, t: performance.now() };
      if (finished()) return;
      if (!pts.length) {
        var s = snapStart(p); if (!s) { showMiss(miss, L.needStart || 'Start your track at one of the flags on the tower: Low, Middle or High.'); return; }
        startK = s.k; pts = [{ x: TX, y: yOfH(s.h) }]; drawing = true; render(); miss.classList.remove('show');
        svg.setPointerCapture && svg.setPointerCapture(e.pointerId); e.preventDefault(); return;
      }
      if (tapMode) { e.preventDefault(); }
    });
    svg.addEventListener('pointermove', function (e) {
      if (!drawing) return; var p = sp(e), last = pts[pts.length - 1];
      p.x = Math.max(TX, Math.min(BALE - 4, p.x)); p.y = Math.max(30, Math.min(FLOOR, p.y));
      if (Math.hypot(p.x - last.x, p.y - last.y) > 6) { pts.push(p); render(); }
    });
    svg.addEventListener('pointerup', function (e) {
      var p = sp(e), wasTap = downAt && Math.hypot(p.x - downAt.p.x, p.y - downAt.p.y) < 6 && performance.now() - downAt.t < 450;
      if (drawing) {
        drawing = false;
        if (pts.length === 1 && wasTap) { tapMode = true; hint.textContent = L.tapMore || 'Now tap points down to the ground'; render(); return; }
        if (finished()) closeTrack(); else if (pts.length > 1) { tapMode = true; hint.textContent = L.notDown || 'Keep going: bring your track down to the ground'; render(); }
        return;
      }
      if (tapMode && wasTap && pts.length && !finished()) {
        p.x = Math.max(pts[pts.length - 1].x + 2, Math.min(BALE - 4, p.x)); p.y = Math.max(30, Math.min(FLOOR, p.y)); pts.push(p); render(); SFX.blip();
        if (finished()) closeTrack();
      }
    });
    /* physics (a model): speed² ∝ (start height − height now) − a little lost to rubbing along the track */
    function play() {
      if (busy) return;
      if (!finished()) { showMiss(miss, pts.length ? (L.notDown || 'Bring your track all the way down to the ground first.') : (L.needStart || 'Draw a track first. Start at a flag on the tower.')); return; }
      if (pending) { showMiss(miss, L.measureFirst || 'Measure the push first: drag the tape to the bale.'); return; }
      busy = true; miss.classList.remove('show'); car.style.display = ''; placeBale(BALE); tape.style.display = 'none';
      var seg = [], tot = 0; for (var i = 1; i < pts.length; i++) { var d = Math.hypot(pts[i].x - pts[i - 1].x, pts[i].y - pts[i - 1].y); seg.push(d); tot += d; }
      var h0 = FLOOR - pts[0].y, mu = P.loss || 0.025, s = 0, k = 0, last = performance.now(), maxV = 0, stopped = null;
      function heightAt(si) { var acc = 0; for (var j = 0; j < seg.length; j++) { if (acc + seg[j] >= si) { var u = (si - acc) / (seg[j] || 1); return { x: pts[j].x + (pts[j + 1].x - pts[j].x) * u, y: pts[j].y + (pts[j + 1].y - pts[j].y) * u, a: Math.atan2(pts[j + 1].y - pts[j].y, pts[j + 1].x - pts[j].x) * 180 / Math.PI }; } acc += seg[j]; } var q = pts[pts.length - 1]; return { x: q.x, y: q.y, a: 0 }; }
      function e2(si, y) { return (h0 - (FLOOR - y)) - mu * si; }
      function step(ts) {
        var dt = Math.min(40, ts - last) / 1000; last = ts;
        var here = heightAt(s), E = e2(s, here.y), v = Math.sqrt(Math.max(0, E)) * (reduceMotion ? 60 : 22);
        if (E < -3 && s > 2) { stopped = here; return stall(here); }
        maxV = Math.max(maxV, v); s += Math.max(v, 30) * dt; placeCar(here.x, here.y, here.a);
        speedBox.textContent = (L.speedWord || 'Speed') + ': ' + Math.round(Math.sqrt(Math.max(0, E)) * (P.mph || 1.6)) + ' mph';
        if (s >= tot) return arrive(Math.max(0, e2(tot, FLOOR)));
        requestAnimationFrame(step);
      }
      requestAnimationFrame(function (ts) { last = ts; step(ts); }); SFX.whoosh();
    }
    function stall(here) {
      busy = false; SFX.thud(); placeCar(here.x, here.y, 0);
      $('div', info).innerHTML = '<b>' + esc(L.stallHead || 'Stuck!') + '</b>' + esc(L.stall || 'The car ran out of speed. It can’t climb higher than where it started. Erase and try again.');
    }
    function arrive(E) {
      var push = Math.max(1, Math.round(E * (P.scale || 0.12)));
      SFX.pop(); tone(90, 0, 0.3, 'sine', 0.12); speedBox.textContent = '';
      var x0 = BALE, x1 = BALE + push * PX_IN, t0 = null;
      function slide(ts) { if (t0 == null) t0 = ts; var p = Math.min(1, (ts - t0) / (reduceMotion ? 1 : 500 + push * 18)), e = 1 - Math.pow(1 - p, 3); placeBale(x0 + (x1 - x0) * e); placeCar(BALE - 18, FLOOR, 0); if (p < 1) requestAnimationFrame(slide); else measureNow(push); }
      requestAnimationFrame(slide);
    }
    function measureNow(push) {
      busy = false; pending = { k: startK, push: push }; tape.style.display = '';
      var tl = $('.fs-dp-tl', tape), th = $('.fs-dp-th', tape), tt = $('.fs-dp-tt', tape), y = FLOOR + 20, x0 = BALE + 40, cur = x0;
      function setT(x) { cur = Math.max(x0, Math.min(W - 10, x)); tl.setAttribute('x1', x0); tl.setAttribute('y1', y); tl.setAttribute('x2', cur); tl.setAttribute('y2', y); th.setAttribute('cx', cur); th.setAttribute('cy', y); tt.setAttribute('x', Math.min(cur + 12, W - 60)); tt.setAttribute('y', y - 12); tt.textContent = Math.round((cur - x0) / PX_IN) + ' ' + (P.unit || 'in'); }
      setT(x0 + 12);
      $('div', info).innerHTML = '<b>' + esc(L.measureHead || 'Measure the push') + '</b>' + esc(L.measure || 'Drag the red tape end to where the bale stopped (or tap the bale).');
      var drag = false;
      function check() { var got = Math.round((cur - x0) / PX_IN); if (Math.abs(got - pending.push) <= 1) record(); }
      th.onpointerdown = function (e) { drag = true; th.setPointerCapture && th.setPointerCapture(e.pointerId); e.preventDefault(); e.stopPropagation(); };
      th.onpointermove = function (e) { if (drag) setT(sp(e).x); };
      th.onpointerup = function () { drag = false; check(); if (pending) showMiss(miss, L.measureMiss || 'Line the tape end up with the front edge of the bale.'); };
      bale.onclick = function () { if (!pending) return; setT(x0 + pending.push * PX_IN); record(); };
    }
    function record() {
      if (!pending) return; st.runs[pending.k] = pending.push; saveJ('drawpath', st); SFX.chime();
      var s = P.starts.filter(function (x) { return x.k === pending.k; })[0];
      $('div', info).innerHTML = '<b>' + esc(s.t + ': ' + pending.push + ' ' + (P.unit || 'in')) + '</b>' + esc(L.recorded || 'Recorded! Erase and draw a track from a different start.');
      pending = null; paintTable();
    }
    function paintTable() {
      table.innerHTML = '<table><tr><th>' + esc(L.colStart || 'Start') + '</th><th>' + esc(L.colPush || 'How far the bale slid') + '</th></tr>' + P.starts.map(function (s) { var v = st.runs[s.k]; return '<tr class="' + (v ? 'ok' : '') + '"><td>' + esc(s.t) + '</td><td>' + (v ? v + ' ' + esc(P.unit || 'in') : '…') + '</td></tr>'; }).join('') + '</table>';
      if (P.starts.every(function (s) { return st.runs[s.k]; })) paintChart();
    }
    function paintChart() {
      var MAX = P.chartMax || 40;
      if (!chart.dataset.on) {
        chart.dataset.on = '1';
        chart.innerHTML = '<div class="fs-in-k">' + esc(P.chartQ || 'Build your bar chart: drag each bar up to match your table.') + '</div><div class="fs-dp-plot"><div class="fs-dp-grid">' + [40, 30, 20, 10, 0].filter(function (v) { return v <= MAX; }).map(function (v) { return '<span style="bottom:' + (v / MAX * 100) + '%">' + v + '</span>'; }).join('') + '</div>' +
          P.starts.map(function (s) { return '<div class="fs-dp-col" data-k="' + s.k + '"><div class="fs-dp-area"><div class="fs-dp-bar"><b></b></div></div><small>' + esc(s.t) + '</small></div>'; }).join('') + '</div>';
        $$('.fs-dp-col', chart).forEach(function (c) {
          var area = $('.fs-dp-area', c), dragging = false;
          function set(e) { var r = area.getBoundingClientRect(), v = Math.round(Math.max(0, Math.min(MAX, (r.bottom - e.clientY) / r.height * MAX))); st.bars[c.dataset.k] = v; draw(); }
          c.addEventListener('pointerdown', function (e) { dragging = true; c.setPointerCapture && c.setPointerCapture(e.pointerId); set(e); e.preventDefault(); });
          c.addEventListener('pointermove', function (e) { if (dragging) set(e); });
          c.addEventListener('pointerup', function () { dragging = false; saveJ('drawpath', st); judge(); });
        });
      }
      function draw() { $$('.fs-dp-col', chart).forEach(function (c) { var v = st.bars[c.dataset.k] || 0, bar = $('.fs-dp-bar', c); bar.style.height = (v / MAX * 100) + '%'; $('b', bar).textContent = v ? v : ''; c.classList.toggle('ok', Math.abs(v - st.runs[c.dataset.k]) <= 1); }); }
      function judge() {
        var ok = P.starts.every(function (s) { return Math.abs((st.bars[s.k] || 0) - st.runs[s.k]) <= 1; });
        if (ok) { SFX.chime(); askOnce(qh, P.q, P.opts, 'drawpath-q', win, P.win, P.clue, 'drawpath', miss); }
        else if (P.starts.every(function (s) { return st.bars[s.k]; })) showMiss(miss, L.barMiss || 'Check each bar against your table. A bar turns green when it matches.');
      }
      chart.__draw = draw; draw(); judge();
    }
    $('.fs-dp-play', ctl).addEventListener('click', play);
    $('.fs-dp-erase', ctl).addEventListener('click', function () { if (busy) return; if (pending) { showMiss(miss, L.measureFirst || 'Measure the push first: drag the tape to the bale.'); return; } reset(); SFX.blip(); $('div', info).textContent = L.start || ''; });
    at.parentNode.insertBefore(g, at.nextSibling);
    reset(); paintTable();
  }

  /* ----- Tool of the Week (19.01): radar speed gun — things cross the beam; press the trigger while one is in the beam to read its speed ----- */
  SIMS.radargun = function (host, T) {
    var R = T.radargun, st = loadJ('radargun', {}), cur = R.targets[0], x = -10, raf = null, last = 0;
    host.innerHTML = '<div class="fs-game-k">Try it: a radar speed gun</div><div class="fs-game-t">' + esc(R.title) + '</div>' +
      '<ul class="fs-todo">' + R.todo.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>' +
      (R.img ? '<figure class="fs-rdr-photo"><img alt="' + esc(R.alt) + '" src="' + esc(R.img) + '"><figcaption>' + esc(R.cap || '') + '</figcaption></figure>' : '') +
      '<div class="fs-in-chips fs-rdr-pick">' + R.targets.map(function (t, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + t.icon + ' ' + esc(t.name) + '</button>'; }).join('') + '</div>' +
      '<div class="fs-rdr-lane"><div class="fs-rdr-beam"></div><div class="fs-rdr-obj"></div><div class="fs-rdr-gun"><span>📡</span><b class="fs-rdr-read">-- mph</b></div></div>' +
      '<button type="button" class="fs-btn fs-rdr-trig">🔫 ' + esc(R.trigger || 'Pull the trigger') + '</button>' +
      '<div class="fs-rdr-log"></div><div class="fs-sv-q fs-rdr-q"></div><div class="fs-miss fs-rdr-miss"></div><div class="fs-win fs-rdr-win"></div>' +
      (R.credit ? '<details class="fs-credit fs-credit-fold"><summary>📷 Photo credit</summary>' + esc(R.credit) + '</details>' : '');
    var lane = $('.fs-rdr-lane', host), obj = $('.fs-rdr-obj', host), read = $('.fs-rdr-read', host), miss = $('.fs-rdr-miss', host);
    function pick(i) { cur = R.targets[i]; x = -10; obj.textContent = cur.icon; $$('.fs-rdr-pick .fs-in-chip', host).forEach(function (c, j) { c.classList.toggle('on', j === i); }); read.textContent = '-- mph'; }
    function loop(ts) {
      var dt = last ? Math.min(50, ts - last) : 16; last = ts;
      x += dt * (reduceMotion ? 0.02 : cur.pace || 0.03); if (x > 110) x = -10;
      obj.style.left = x + '%'; raf = host.isConnected ? requestAnimationFrame(loop) : null;
    }
    function logs() {
      $('.fs-rdr-log', host).innerHTML = '<div class="fs-in-k">' + esc(R.logLabel || 'Speeds you measured') + '</div><ul>' + R.targets.map(function (t) { return '<li class="' + (st[t.k] ? 'ok' : '') + '">' + t.icon + ' ' + esc(t.name) + ': ' + (st[t.k] ? t.mph + ' mph ✓' : '—') + '</li>'; }).join('') + '</ul>';
      if (R.targets.every(function (t) { return st[t.k]; })) check();
    }
    function check() {
      var q = $('.fs-rdr-q', host); if (q.dataset.on) return; q.dataset.on = '1';
      q.innerHTML = '<div class="fs-in-k">' + esc(R.q.q) + '</div><div class="fs-in-chips">' + R.q.opts.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(o.t) + '</button>'; }).join('') + '</div>';
      function ok(i) { $$('.fs-in-chip', q)[i].classList.add('on', 'ok'); var w = $('.fs-rdr-win', host); w.innerHTML = esc(R.q.opts[i].why); w.classList.add('show'); }
      $$('.fs-in-chip', q).forEach(function (c) { c.addEventListener('click', function () { var o = R.q.opts[+c.dataset.i]; if (!o.ok) { bounce(c, miss, o.why); return; } miss.classList.remove('show'); ok(+c.dataset.i); SFX.win(); store('radargun-q', '1'); toolDone(); }); });
      if (store('radargun-q')) ok(R.q.opts.map(function (o, j) { return o.ok ? j : -1; }).filter(function (j) { return j > -1; })[0]);
    }
    function trigger() {
      var inBeam = x > 38 && x < 62;
      if (!inBeam) { read.textContent = '-- mph'; bounce($('.fs-rdr-trig', host), miss, R.missLine || 'Nothing in the beam. Wait until it crosses the yellow beam, then pull the trigger.'); return; }
      miss.classList.remove('show'); read.textContent = cur.mph + ' mph'; tone(1800, 0, 0.12, 'square', 0.03); tone(2400, 0.12, 0.12, 'square', 0.03);
      lane.classList.remove('hit'); void lane.offsetWidth; lane.classList.add('hit');
      if (!st[cur.k]) { st[cur.k] = 1; saveJ('radargun', st); logs(); }
      var info = $('.fs-rdr-log', host); if (cur.note) { var n = el('div', 'fs-hs-card', '<span class="fs-hs-n">' + cur.icon + '</span><div><b>' + esc(cur.name + ': ' + cur.mph + ' mph') + '</b>' + esc(cur.note) + '</div>'); var old = $('.fs-rdr-note', host); if (old) old.remove(); n.classList.add('fs-rdr-note'); info.parentNode.insertBefore(n, info); }
    }
    $$('.fs-rdr-pick .fs-in-chip', host).forEach(function (c) { c.addEventListener('click', function () { pick(+c.dataset.i); SFX.blip(); }); });
    $('.fs-rdr-trig', host).addEventListener('click', trigger);
    lane.addEventListener('click', trigger);
    pick(0); logs(); raf = requestAnimationFrame(loop);
  };

  /* =================== 19.02: The Rematch (stopwatch, lock it down, dot plot drop, data detective, bullseye derby) =================== */

  /* ---------- Warm-Up: "The stopwatch race" — a derby car rolls between two flags in exactly the same time every run (a model);
     the student times it with Start/Stop 3 times and sees their own times differ (reaction time). Then a chip question (19.02) ----------
     D.stopwatch = {afterText, kicker, title, todo[], why, alt, model, real (seconds), tries, goBtn, tapBtn, flagA, flagB, early, missLine, logLabel, realLine, q, opts, win, clue} */
  function buildStopwatch() {
    var S = D.stopwatch; if (!S) return;
    var at = anchorP(S.afterText); if (!at) { FAILED.push('stopwatch anchor text not found'); return; }
    var g = gameShell(S.kicker || 'Warm-Up game', S.title, S.todo, S.why); g.dataset.mod = 'stopwatch';
    var st = loadJ('stopwatch', { t: [] }), N = S.tries || 3, AX = 150, BX = 470, X0 = 30, X1 = 600, real = S.real || 2.5;
    var spd = (BX - AX) / real; /* px per second, constant (a model with no friction between the flags) */
    var stage = el('div', 'fs-sw-stage');
    stage.innerHTML = '<svg viewBox="0 0 640 170" class="fs-sw-svg" role="img" aria-label="' + esc(S.alt || 'A model: a derby car rolling past two flags on a flat track') + '">' +
      '<rect width="640" height="170" fill="#EAF4FB"/><rect y="120" width="640" height="50" fill="#E9D8A6"/><line x1="0" y1="120" x2="640" y2="120" stroke="#B9A06A" stroke-width="3"/>' +
      [[AX, S.flagA || 'START'], [BX, S.flagB || 'STOP']].map(function (f, i) { return '<g class="fs-sw-flag"><line x1="' + f[0] + '" y1="120" x2="' + f[0] + '" y2="52" stroke="#5B7A99" stroke-width="3"/><path d="M' + f[0] + ' 52 l30 8 l-30 8z" fill="' + (i ? '#E8636B' : '#34B76F') + '"/><text x="' + f[0] + '" y="44" text-anchor="middle">' + esc(f[1]) + '</text><line x1="' + f[0] + '" y1="120" x2="' + f[0] + '" y2="160" stroke="#8A7A50" stroke-dasharray="4 4"/></g>'; }).join('') +
      '<g class="fs-sw-car"><path d="M-22 -9 Q-18 -22 0 -22 Q18 -22 24 -9 Z" fill="#E8636B" stroke="#7A2A30" stroke-width="2"/><circle cx="-13" cy="-4" r="6" fill="#333"/><circle cx="14" cy="-4" r="6" fill="#333"/></g>' +
      '<text x="14" y="160" class="fs-sw-model">' + esc(S.model || 'a model') + '</text></svg>' +
      '<div class="fs-sw-watch"><div class="fs-sw-face"><span class="fs-sw-num">0.00</span><small>s</small></div><button type="button" class="fs-btn fs-sw-tap">⏱ ' + esc(S.tapBtn || 'Start') + '</button></div>';
    var go = el('button', 'fs-btn alt fs-sw-go', '▶ ' + esc(S.goBtn || 'Roll the car')); go.type = 'button';
    var log = el('div', 'fs-sw-log'), miss = el('div', 'fs-miss'), info = el('div', 'fs-hs-card fs-sw-info'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(stage); g.appendChild(go); g.appendChild(log); g.appendChild(miss); g.appendChild(info); g.appendChild(qh); g.appendChild(win);
    var car = $('.fs-sw-car', stage), num = $('.fs-sw-num', stage), tap = $('.fs-sw-tap', stage), running = false, t0 = null, x = X0, startAt = null, raf = null, phase = 0;
    info.style.display = 'none';
    function place() { car.setAttribute('transform', 'translate(' + x.toFixed(1) + ' 120)'); }
    function paintLog() {
      log.innerHTML = '<div class="fs-in-k">' + esc(S.logLabel || 'Your times') + '</div><div class="fs-sw-rows">' + Array.apply(null, Array(N)).map(function (_, i) { var v = st.t[i]; return '<span class="' + (v != null ? 'ok' : '') + '"><b>' + esc((S.tryWord || 'Try') + ' ' + (i + 1)) + '</b>' + (v != null ? v.toFixed(2) + ' s' : '—') + '</span>'; }).join('') + '</div>';
      if (st.t.length >= N) {
        info.style.display = ''; info.innerHTML = '<span class="fs-hs-n">📡</span><div><b>' + esc((S.realWord || 'Laser timer') + ': ' + real.toFixed(2) + ' s ' + (S.everyWord || 'every time')) + '</b>' + esc(S.realLine || '') + '</div>';
        go.style.display = 'none'; askOnce(qh, S.q, S.opts, 'stopwatch-q', win, S.win, S.clue, 'stopwatch', miss);
      }
    }
    function frame(ts) {
      if (!running) return; var dt = t0 == null ? 0 : (ts - t0) / 1000; t0 = ts; x += spd * dt; place();
      if (phase === 1) num.textContent = ((ts - startAt) / 1000).toFixed(2);
      if (x > X1) { running = false; if (phase !== 2) { showMiss(miss, S.missLine || 'The car got away! Roll it again and press Start at the green flag, Stop at the red flag.'); reset(); } return; }
      raf = requestAnimationFrame(frame);
    }
    function reset() { phase = 0; tap.textContent = '⏱ ' + (S.tapBtn || 'Start'); tap.disabled = true; go.disabled = st.t.length >= N; }
    go.addEventListener('click', function () {
      if (running || st.t.length >= N) return; miss.classList.remove('show'); x = X0; place(); num.textContent = '0.00'; running = true; t0 = null; phase = 0; tap.disabled = false; go.disabled = true; SFX.whoosh();
      raf = requestAnimationFrame(frame);
    });
    function press() {
      if (!running || tap.disabled) return;
      if (phase === 0) { phase = 1; startAt = performance.now(); tap.textContent = '⏹ ' + (S.stopBtn || 'Stop'); SFX.blip(); if (x < AX - 60) showMiss(miss, S.early || 'That was early! The car hadn’t reached the green flag yet. It still counts. Real scientists make small timing errors too.'); return; }
      if (phase === 1) { phase = 2; var t = (performance.now() - startAt) / 1000; num.textContent = t.toFixed(2); st.t.push(+t.toFixed(2)); saveJ('stopwatch', st); SFX.chime(); tap.disabled = true; paintLog(); setTimeout(function () { if (st.t.length < N) go.disabled = false; }, 200); }
    }
    tap.addEventListener('click', press);
    stage.addEventListener('keydown', function (e) { if (e.key === ' ') { e.preventDefault(); press(); } });
    at.parentNode.insertBefore(g, at.nextSibling);
    x = X0; place(); reset(); go.disabled = st.t.length >= N; paintLog();
  }

  /* ---------- Lesson Part 1: "Lock it down" — Coach Dee's two runs changed several things at once; lock every row except the one being tested,
     the stamp flips UNFAIR → FAIR; run her test and the fair test (a model) (19.02) ----------
     D.lockdown = {afterText, kicker, title, todo[], why, runA, runB, rows:[{k, icon, t, a, b}], testK, testMiss, stampFair, stampUnfair, deeBtn, deeResult:{a,b,t}, fairBtn, fairResult:{a,b,t}, unit, q, opts, win, clue} */
  function buildLockdown() {
    var L = D.lockdown; if (!L) return;
    var at = anchorP(L.afterText); if (!at) { FAILED.push('lockdown anchor text not found'); return; }
    var g = gameShell(L.kicker || 'Part 1 game', L.title, L.todo, L.why); g.dataset.mod = 'lockdown';
    var st = loadJ('lockdown', { lock: {}, dee: 0, fair: 0 });
    var panel = el('div', 'fs-ld-panel'), stamp = el('div', 'fs-ld-stamp'), btns = el('div', 'fs-ld-btns'), race = el('div', 'fs-ld-race'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(panel); g.appendChild(stamp); g.appendChild(btns); g.appendChild(race); g.appendChild(miss); g.appendChild(qh); g.appendChild(win);
    function same(r) { return r.a === r.b || st.lock[r.k]; }
    function fair() { return L.rows.every(function (r) { return r.k === L.testK || same(r); }); }
    function paint() {
      panel.innerHTML = '<div class="fs-ld-h"><span></span><b>' + esc(L.runA) + '</b><b>' + esc(L.runB) + '</b><span></span></div>' + L.rows.map(function (r) {
        var s = same(r), test = r.k === L.testK;
        return '<div class="fs-ld-row' + (s ? ' same' : ' diff') + (test ? ' test' : '') + '" data-k="' + r.k + '"><span class="fs-ld-t">' + r.icon + ' ' + esc(r.t) + (test ? ' <em>' + esc(L.testTag || 'what we test') + '</em>' : '') + '</span><span class="fs-ld-v">' + esc(r.a) + '</span><span class="fs-ld-v">' + esc(st.lock[r.k] ? r.a : r.b) + '</span>' +
          '<button type="button" class="fs-ld-lk' + (test ? ' tst' : '') + '" aria-label="' + esc(test ? r.t + ': this is what we test' : (s ? 'Locked: ' : 'Lock ') + r.t) + '">' + (test ? '🎯' : (s ? '🔒' : '🔓')) + '</button></div>';
      }).join('');
      $$('.fs-ld-lk', panel).forEach(function (b) { b.addEventListener('click', function () {
        var r = L.rows.filter(function (x) { return x.k === b.closest('.fs-ld-row').dataset.k; })[0];
        if (same(r)) return;
        if (r.k === L.testK) { bounce(b, miss, L.testMiss); return; }
        st.lock[r.k] = 1; saveJ('lockdown', st); miss.classList.remove('show'); SFX.stamp(); paint();
        var row = $('.fs-ld-row[data-k="' + r.k + '"]', panel); if (row && !reduceMotion) row.classList.add('pop');
      }); });
      var f = fair(); stamp.className = 'fs-ld-stamp ' + (f ? 'fair' : 'unfair'); stamp.textContent = f ? (L.stampFair || 'FAIR TEST') : (L.stampUnfair || 'UNFAIR TEST');
      btns.innerHTML = '<button type="button" class="fs-btn alt fs-ld-dee">▶ ' + esc(L.deeBtn) + '</button><button type="button" class="fs-btn fs-ld-fair"' + (f ? '' : ' disabled') + '>▶ ' + esc(L.fairBtn) + '</button>';
      $('.fs-ld-dee', btns).addEventListener('click', function () { run(L.deeResult, 'dee'); });
      $('.fs-ld-fair', btns).addEventListener('click', function () { if (!fair()) return; run(L.fairResult, 'fair'); });
    }
    function bars(R, anim) {
      var mx = Math.max(R.a, R.b, 1);
      race.innerHTML = '<div class="fs-ld-lane"><b>' + esc(L.runA) + '</b><div class="fs-ld-track"><i style="width:' + (anim ? 0 : R.a / 30 * 100) + '%"></i></div><span>' + R.a + ' ' + esc(L.unit || 'in') + '</span></div>' +
        '<div class="fs-ld-lane"><b>' + esc(L.runB) + '</b><div class="fs-ld-track"><i style="width:' + (anim ? 0 : R.b / 30 * 100) + '%"></i></div><span>' + R.b + ' ' + esc(L.unit || 'in') + '</span></div><p>' + esc(R.t) + '</p>';
      if (anim) setTimeout(function () { var w = $$('.fs-ld-track i', race); w[0].style.width = (R.a / 30 * 100) + '%'; w[1].style.width = (R.b / 30 * 100) + '%'; }, 40);
    }
    function run(R, k) { st[k] = 1; saveJ('lockdown', st); SFX.whoosh(); bars(R, !reduceMotion); race.className = 'fs-ld-race on ' + k; if (k === 'fair') askOnce(qh, L.q, L.opts, 'lockdown-q', win, L.win, L.clue, 'lockdown', miss); }
    at.parentNode.insertBefore(g, at.nextSibling);
    paint(); if (st.fair) { bars(L.fairResult, false); race.className = 'fs-ld-race on fair'; askOnce(qh, L.q, L.opts, 'lockdown-q', win, L.win, L.clue, 'lockdown', miss); }
  }

  /* ---------- Lesson Part 2: "Dot plot drop" — each trial drops a dot on a number line; drag the gold marker to the middle of the dots (19.02) ----------
     D.dotplot = {afterText, kicker, title, todo[], why, min, max, step, unit, trials[], need, runBtn, markerLabel, tol, trust:[{n, t}], checkLine, q, opts, win, clue} */
  function buildDotplot() {
    var P = D.dotplot; if (!P) return;
    var at = anchorP(P.afterText); if (!at) { FAILED.push('dotplot anchor text not found'); return; }
    var g = gameShell(P.kicker || 'Part 2 game', P.title, P.todo, P.why); g.dataset.mod = 'dotplot';
    var st = loadJ('dotplot', { n: 0, m: null, ok: 0 }), W = 600, L0 = 40, L1 = 560, Y = 150;
    function xOf(v) { return L0 + (v - P.min) / (P.max - P.min) * (L1 - L0); }
    function vOf(x) { return P.min + (x - L0) / (L1 - L0) * (P.max - P.min); }
    var ticks = ''; for (var v = P.min; v <= P.max; v += (P.step || 1)) ticks += '<line x1="' + xOf(v) + '" y1="' + Y + '" x2="' + xOf(v) + '" y2="' + (Y + ((v % 5) ? 6 : 12)) + '"/>' + ((v % 5) ? '' : '<text x="' + xOf(v) + '" y="' + (Y + 28) + '">' + v + '</text>');
    var box = el('div', 'fs-dpl-box', '<svg viewBox="0 0 ' + W + ' 200" class="fs-dpl-svg" role="img" aria-label="' + esc(P.alt || 'A number line of inches with dots for each trial and a gold marker') + '"><line x1="' + L0 + '" y1="' + Y + '" x2="' + L1 + '" y2="' + Y + '" class="fs-dpl-axis"/><g class="fs-dpl-ticks">' + ticks + '</g><text x="' + ((L0 + L1) / 2) + '" y="196" class="fs-dpl-unit">' + esc(P.unit || 'inches') + '</text><g class="fs-dpl-dots"></g><g class="fs-dpl-mk"><line y1="20" y2="' + (Y + 4) + '"/><path d="M-10 6 L10 6 L0 20 Z"/><text y="0" text-anchor="middle">' + esc(P.markerLabel || 'middle') + '</text></g></svg>');
    var ctl = el('div', 'fs-dpl-ctl', '<button type="button" class="fs-btn fs-dpl-run">▶ ' + esc(P.runBtn || 'Run a trial') + '</button><span class="fs-dpl-n"></span>');
    var trust = el('div', 'fs-hs-card fs-dpl-trust'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(box); g.appendChild(ctl); g.appendChild(trust); g.appendChild(miss); g.appendChild(qh); g.appendChild(win);
    var svg = $('svg', box), dots = $('.fs-dpl-dots', box), mk = $('.fs-dpl-mk', box), run = $('.fs-dpl-run', ctl);
    function data() { return P.trials.slice(0, st.n); }
    function median(a) { var s = a.slice().sort(function (x, y) { return x - y; }), h = Math.floor(s.length / 2); return s.length % 2 ? s[h] : (s[h - 1] + s[h]) / 2; }
    function paint(newest) {
      var cnt = {}; dots.innerHTML = data().map(function (v, i) { cnt[v] = (cnt[v] || 0) + 1; return '<circle class="' + (i === newest && !reduceMotion ? 'drop' : '') + '" cx="' + xOf(v) + '" cy="' + (Y - 10 - (cnt[v] - 1) * 18) + '" r="8"/>'; }).join('');
      var m = st.m == null ? (P.markerStart != null ? P.markerStart : P.min + 2) : st.m; mk.setAttribute('transform', 'translate(' + xOf(m) + ' 0)'); $('text', mk).textContent = (P.markerLabel || 'middle') + ': ' + Math.round(m);
      $('.fs-dpl-n', ctl).textContent = st.n + ' ' + (st.n === 1 ? (P.trialWord || 'trial') : (P.trialsWord || 'trials'));
      var tr = null; (P.trust || []).forEach(function (x) { if (st.n >= x.n) tr = x; }); trust.innerHTML = tr ? '<span class="fs-hs-n">' + (tr.icon || '🔎') + '</span><div><b>' + esc(tr.head || '') + '</b>' + esc(tr.t) + '</div>' : '<span class="fs-hs-n">🔎</span><div>' + esc(P.startLine || 'Run the first trial.') + '</div>';
      run.disabled = st.n >= P.trials.length;
      mk.classList.toggle('ok', !!st.ok);
    }
    function judge() {
      if (st.n < P.need) { if (st.m != null) showMiss(miss, (P.moreLine || 'Run at least {n} trials first. One or two dots can fool you.').replace('{n}', P.need)); return; }
      var md = median(data());
      if (Math.abs(st.m - md) <= (P.tol || 1)) { st.ok = 1; saveJ('dotplot', st); miss.classList.remove('show'); SFX.chime(); paint(); askOnce(qh, P.q, P.opts, 'dotplot-q', win, P.win, P.clue, 'dotplot', miss); }
      else { st.ok = 0; showMiss(miss, st.m < md ? (P.lowLine || 'Most dots are to the right of your marker. Slide it toward the middle of the pile.') : (P.highLine || 'Most dots are to the left of your marker. Slide it toward the middle of the pile.')); paint(); }
    }
    run.addEventListener('click', function () { if (st.n >= P.trials.length) return; st.n++; st.ok = 0; saveJ('dotplot', st); tone(300 + P.trials[st.n - 1] * 30, 0, 0.15, 'triangle', 0.05); paint(st.n - 1); if (st.m != null && st.n >= P.need) judge(); });
    var drag = false;
    function setX(e) { var r = svg.getBoundingClientRect(), x = (e.clientX - r.left) * W / r.width; st.m = Math.max(P.min, Math.min(P.max, Math.round(vOf(x) * 2) / 2)); paint(); }
    svg.addEventListener('pointerdown', function (e) { drag = true; svg.setPointerCapture && svg.setPointerCapture(e.pointerId); setX(e); e.preventDefault(); });
    svg.addEventListener('pointermove', function (e) { if (drag) setX(e); });
    svg.addEventListener('pointerup', function () { if (!drag) return; drag = false; saveJ('dotplot', st); judge(); });
    at.parentNode.insertBefore(g, at.nextSibling);
    paint(); if (st.ok) askOnce(qh, P.q, P.opts, 'dotplot-q', win, P.win, P.clue, 'dotplot', miss);
  }

  /* ---------- Lesson Part 4: "Data detective" — Coach Dee's 9-trial notebook; tap the odd number, pick keep / throw out / check and redo;
     check plays a replay that shows what went wrong (the fluke), redo gives a new number, averages snap into bars (19.02) ----------
     D.detective = {afterText, kicker, title, todo[], why, head, sub, note, unit, rows:[{k, t, trials:[]}], fluke:{row, i, redo}, fitLine, choiceQ, choices:[{k, t, ok, miss}],
                    replay:{alt, cap, line}, redoBtn, avgLabel, q, opts, win, clue} */
  function buildDetective() {
    var T = D.detective; if (!T) return;
    var at = anchorP(T.afterText); if (!at) { FAILED.push('detective anchor text not found'); return; }
    var g = gameShell(T.kicker || 'Part 4 game', T.title, T.todo, T.why); g.dataset.mod = 'detective';
    var st = loadJ('detective', { found: 0, checked: 0, redo: 0 }), F = T.fluke, U = T.unit || 'in';
    var book = el('div', 'fs-dt-book'), act = el('div', 'fs-dt-act'), rep = el('div', 'fs-dt-rep'), avg = el('div', 'fs-dt-avg'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(book); g.appendChild(act); g.appendChild(rep); g.appendChild(avg); g.appendChild(miss); g.appendChild(qh); g.appendChild(win);
    function val(r, i) { return (r.k === F.row && i === F.i && st.redo) ? F.redo : r.trials[i]; }
    function mean(r) { var s = 0; r.trials.forEach(function (_, i) { s += val(r, i); }); return Math.round(s / r.trials.length); }
    function paintBook() {
      book.innerHTML = '<div class="fs-dt-head">' + esc(T.head) + '</div><div class="fs-dt-sub">' + esc(T.sub || '') + '</div><table><tr><th>' + esc(T.colStart || 'Start') + '</th>' + T.rows[0].trials.map(function (_, i) { return '<th>' + esc((T.trialWord || 'Trial') + ' ' + (i + 1)) + '</th>'; }).join('') + '</tr>' +
        T.rows.map(function (r) { return '<tr><td>' + esc(r.t) + '</td>' + r.trials.map(function (_, i) { var fl = r.k === F.row && i === F.i; return '<td><button type="button" class="fs-dt-cell' + (fl && st.found ? ' found' : '') + (fl && st.redo ? ' redone' : '') + '" data-r="' + r.k + '" data-i="' + i + '">' + (fl && st.redo ? '<s>' + r.trials[i] + '</s> ' : '') + val(r, i) + ' ' + esc(U) + '</button></td>'; }).join('') + '</tr>'; }).join('') + '</table>' + (T.note ? '<div class="fs-dt-note">' + esc(T.note) + '</div>' : '');
      $$('.fs-dt-cell', book).forEach(function (c) { c.addEventListener('click', function () {
        if (st.found) return; var fl = c.dataset.r === F.row && +c.dataset.i === F.i;
        if (!fl) { bounce(c, miss, T.fitLine || 'That number fits with the others in its row. Look for one that doesn’t.'); return; }
        st.found = 1; saveJ('detective', st); miss.classList.remove('show'); SFX.chime(); paintBook(); paintAct();
      }); });
    }
    function paintAct() {
      if (!st.found) { act.innerHTML = ''; return; }
      if (act.dataset.on) return; act.dataset.on = '1';
      act.innerHTML = '<div class="fs-in-k">' + esc(T.choiceQ) + '</div><div class="fs-in-chips">' + T.choices.map(function (c, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(c.t) + '</button>'; }).join('') + '</div>';
      $$('.fs-in-chip', act).forEach(function (b) { b.addEventListener('click', function () {
        if (st.checked) return; var c = T.choices[+b.dataset.i];
        if (!c.ok) { bounce(b, miss, c.miss); return; }
        b.classList.add('on', 'ok'); st.checked = 1; saveJ('detective', st); miss.classList.remove('show'); SFX.chime(); replay(true);
      }); });
      if (st.checked) { var k = T.choices.map(function (c, i) { return c.ok ? i : -1; }).filter(function (i) { return i > -1; })[0]; $$('.fs-in-chip', act)[k].classList.add('on', 'ok'); }
    }
    function replay(anim) {
      var R = T.replay;
      rep.innerHTML = '<div class="fs-in-k">' + esc(R.head || 'Replay of the odd trial') + '</div><div class="fs-dt-screen"><svg viewBox="0 0 600 160" role="img" aria-label="' + esc(R.alt) + '"><rect width="600" height="160" fill="#1B2430"/><rect y="112" width="600" height="48" fill="#3A3226"/><path d="M0 112 L120 112 Q150 112 170 100 L40 40 L0 40 Z" fill="#4A4032" opacity=".9"/>' +
        '<g class="fs-dt-sock" transform="translate(300 112)"><path d="M-14 -2 Q-14 -12 -4 -12 L6 -12 L6 -20 L16 -20 L16 -2 Z" fill="#F4F4F4" stroke="#999" stroke-width="1.5"/><path d="M-14 -5 H6" stroke="#E8636B" stroke-width="3"/></g>' +
        '<g class="fs-dt-car"><path d="M-22 -9 Q-18 -22 0 -22 Q18 -22 24 -9 Z" fill="#E8636B" stroke="#7A2A30" stroke-width="2"/><circle cx="-13" cy="-4" r="6" fill="#ddd"/><circle cx="14" cy="-4" r="6" fill="#ddd"/></g>' +
        '<text x="12" y="20" class="fs-dt-rec">● ' + esc(R.rec || 'REPLAY · TRIAL 6') + '</text></svg></div><div class="fs-hs-card fs-dt-cap"><span class="fs-hs-n">🧦</span><div>' + esc(R.cap) + '</div></div>' +
        '<button type="button" class="fs-btn fs-dt-redo">🔁 ' + esc(T.redoBtn || 'Redo the trial') + '</button>';
      var car = $('.fs-dt-car', rep), cap = $('.fs-dt-cap', rep), redo = $('.fs-dt-redo', rep), sock = $('.fs-dt-sock', rep);
      cap.style.visibility = 'hidden'; redo.style.display = st.redo ? 'none' : '';
      var x = 40, y = 40, t0 = null, D1 = reduceMotion || !anim ? 1 : 2200;
      function pos(p) { /* down the slope (0-0.35), along the track to the sock (0.35-1), stopping there */ if (p < 0.35) { var q = p / 0.35; return [40 + 130 * q, 40 + 72 * q * q]; } var r = (p - 0.35) / 0.65, e = 1 - Math.pow(1 - r, 2.2); return [170 + (276 - 170) * e, 112]; }
      function step(ts) { if (t0 == null) t0 = ts; var p = Math.min(1, (ts - t0) / D1), xy = pos(p); car.setAttribute('transform', 'translate(' + xy[0].toFixed(1) + ' ' + xy[1].toFixed(1) + ')'); if (p < 1) requestAnimationFrame(step); else { cap.style.visibility = ''; sock.classList.add('hit'); if (anim) SFX.thud(); } }
      requestAnimationFrame(step);
      redo.addEventListener('click', function () { st.redo = 1; saveJ('detective', st); SFX.sparkle(); sock.style.display = 'none'; redo.style.display = 'none'; paintBook(); averages(true); });
    }
    function averages(anim) {
      var mx = Math.max.apply(null, T.rows.map(mean)) || 1;
      avg.innerHTML = '<div class="fs-in-k">' + esc(T.avgLabel || 'Averages (the typical push for each start)') + '</div><div class="fs-dt-bars">' + T.rows.map(function (r) { return '<div class="fs-dt-col"><div class="fs-dt-area"><i style="height:' + (anim ? 0 : mean(r) / 30 * 100) + '%"><b>' + mean(r) + '</b></i></div><small>' + esc(r.t) + '</small></div>'; }).join('') + '</div>';
      if (anim) setTimeout(function () { $$('.fs-dt-area i', avg).forEach(function (b, i) { b.style.height = (mean(T.rows[i]) / 30 * 100) + '%'; }); }, 60);
      askOnce(qh, T.q, T.opts, 'detective-q', win, T.win, T.clue, 'detective', miss);
    }
    at.parentNode.insertBefore(g, at.nextSibling);
    paintBook(); paintAct(); if (st.checked) replay(false); if (st.redo) averages(false);
  }

  /* ---------- Bonus after the case: "Bullseye Derby" — pick a start height so the car rolls out and stops on the bullseye (a model:
     the rollout distance grows with the start height; rougher ground stops it sooner). 3 levels, stars, best score saved (19.02) ----------
     D.bullseye = {kicker, title, todo[], why, after, hMin, hMax, hStep, levels:[{name, surface, k, target, tip}], unit, goBtn, nextBtn, lockLine, lines:{…}, credit} */
  function buildBullseye() {
    var B = D.bullseye; if (!B) return;
    var sv = $(B.after || '.fs-solve'); if (!sv) { FAILED.push('bullseye: anchor not found'); return; }
    var g = gameShell(B.kicker || 'Bonus game', B.title, B.todo, B.why); g.dataset.mod = 'bullseye'; g.classList.add('fs-bx');
    var st = loadJ('bullseye', { lv: 0, stars: {}, best: 0 }), Lz = B.lines || {}, U = B.unit || 'ft';
    var lock = el('div', 'fs-lock', '🔒 <span>' + esc(B.lockLine || 'Crack the case first. Then the game opens.') + '</span>');
    var hud = el('div', 'fs-bx-hud'), stage = el('div', 'fs-bx-stage'), ctl = el('div', 'fs-bx-ctl'), msg = el('div', 'fs-hs-card fs-bx-msg');
    g.appendChild(lock); g.appendChild(hud); g.appendChild(stage); g.appendChild(ctl); g.appendChild(msg);
    var W = 640, H = 220, GY = 180, HX = 120, PX = 4.6; /* PX = pixels per foot of rollout */
    var h = Math.round((B.hMin + B.hMax) / 2), busy = false;
    function lv() { return B.levels[Math.min(st.lv, B.levels.length - 1)]; }
    function hy(hh) { return GY - hh * 13; }
    function total() { var s = 0; Object.keys(st.stars).forEach(function (k) { s += st.stars[k]; }); return s; }
    function draw() {
      var L = lv(), tx = HX + L.target * PX, surf = L.surface === 'sand' ? '#E9D8A6' : (L.surface === 'grass' ? '#9CCB7A' : '#A9B1BA');
      stage.innerHTML = '<svg viewBox="0 0 ' + W + ' ' + H + '" class="fs-bx-svg" role="img" aria-label="' + esc(B.alt || 'A hill on the left, a flat track and a bullseye target') + '"><rect width="' + W + '" height="' + H + '" fill="#EAF4FB"/>' +
        '<rect x="' + HX + '" y="' + GY + '" width="' + (W - HX) + '" height="' + (H - GY) + '" fill="' + surf + '"/><path d="M0 ' + GY + ' L0 ' + hy(B.hMax + 1) + ' L' + HX + ' ' + GY + ' Z" fill="#C9B48A"/>' +
        '<g class="fs-bx-target" transform="translate(' + tx + ' ' + (GY + 14) + ')"><ellipse rx="30" ry="9" fill="#fff"/><ellipse rx="21" ry="6.3" fill="#E8636B"/><ellipse rx="12" ry="3.6" fill="#fff"/><ellipse rx="5" ry="1.6" fill="#E8636B"/></g>' +
        [0, 20, 40, 60, 80, 100].map(function (f) { var x = HX + f * PX; return x > W - 10 ? '' : '<line x1="' + x + '" y1="' + GY + '" x2="' + x + '" y2="' + (GY + 6) + '" stroke="#555"/><text x="' + x + '" y="' + (GY + 34) + '" class="fs-bx-tk">' + f + '</text>'; }).join('') +
        '<g class="fs-bx-start"><line x1="0" y1="' + hy(h) + '" x2="' + (HX - (HX * (hy(h) - hy(B.hMax + 1)) / (GY - hy(B.hMax + 1)))) + '" y2="' + hy(h) + '" stroke="#E8636B" stroke-dasharray="4 4"/></g>' +
        '<g class="fs-bx-car"><path d="M-16 -7 Q-13 -16 0 -16 Q13 -16 17 -7 Z" fill="#2D7AA6" stroke="#123" stroke-width="1.5"/><circle cx="-9" cy="-3" r="4.5" fill="#333"/><circle cx="10" cy="-3" r="4.5" fill="#333"/></g>' +
        '<g class="fs-bx-puff"></g><text x="' + (W - 10) + '" y="20" text-anchor="end" class="fs-bx-model">' + esc(B.model || 'a model') + '</text></svg>';
      var c = $('.fs-bx-car', stage); var sx = HX * (1 - (GY - hy(h)) / (GY - hy(B.hMax + 1))); c.setAttribute('transform', 'translate(' + Math.max(14, sx) + ' ' + hy(h) + ')');
      hud.innerHTML = '<span><b>' + esc((Lz.level || 'Level') + ' ' + (st.lv + 1) + ' of ' + B.levels.length) + '</b> ' + esc(L.name) + '</span><span>🎯 ' + esc((Lz.target || 'Target') + ': ' + L.target + ' ' + U) + '</span><span>⭐ ' + total() + ' / ' + (B.levels.length * 3) + (st.best ? ' · ' + esc(Lz.best || 'best') + ' ' + st.best : '') + '</span>';
    }
    function paintCtl() {
      ctl.innerHTML = '<label class="fs-bx-h"><span>' + esc(Lz.height || 'Start height') + ': <b>' + h + ' ' + esc(U) + '</b></span><input type="range" min="' + B.hMin + '" max="' + B.hMax + '" step="' + (B.hStep || 1) + '" value="' + h + '"></label><button type="button" class="fs-btn fs-bx-go">🏁 ' + esc(B.goBtn || 'Let it roll') + '</button>';
      var r = $('input', ctl); r.addEventListener('input', function () { if (busy) return; h = +r.value; $('b', ctl).textContent = h + ' ' + U; draw(); });
      $('.fs-bx-go', ctl).addEventListener('click', roll);
    }
    function roll() {
      if (busy || !store('solved')) return; busy = true; var L = lv(), d = L.k * h, carEl = $('.fs-bx-car', stage), t0 = null;
      var sx0 = Math.max(14, HX * (1 - (GY - hy(h)) / (GY - hy(B.hMax + 1)))), y0 = hy(h), endX = Math.min(W - 14, HX + d * PX), D1 = reduceMotion ? 1 : 700, D2 = reduceMotion ? 1 : 900 + d * 22;
      SFX.whoosh();
      function down(ts) { if (t0 == null) t0 = ts; var p = Math.min(1, (ts - t0) / D1), q = p * p; carEl.setAttribute('transform', 'translate(' + (sx0 + (HX - sx0) * q).toFixed(1) + ' ' + (y0 + (GY - y0) * q).toFixed(1) + ')'); if (p < 1) requestAnimationFrame(down); else { t0 = null; requestAnimationFrame(out); } }
      function out(ts) { if (t0 == null) t0 = ts; var p = Math.min(1, (ts - t0) / D2), e = 1 - Math.pow(1 - p, 2); carEl.setAttribute('transform', 'translate(' + (HX + (endX - HX) * e).toFixed(1) + ' ' + GY + ')'); if (p < 1) requestAnimationFrame(out); else land(d); }
      requestAnimationFrame(down);
    }
    function land(d) {
      busy = false; var L = lv(), off = Math.abs(d - L.target), s = off <= 1 ? 3 : off <= 3 ? 2 : off <= 6 ? 1 : 0;
      var line = s ? (Lz['s' + s] || '') : (d < L.target ? (Lz.short || 'Too slow! Not enough energy to reach the target. Start higher.') : (Lz.long || 'Too fast! Too much energy. It blasted past the target. Start lower.'));
      if (!s && d > L.target) { var pf = $('.fs-bx-puff', stage); pf.innerHTML = '<circle cx="' + Math.min(W - 20, HX + d * PX) + '" cy="' + (GY - 6) + '" r="14" fill="#F2E3B8"/>'; tone(90, 0, 0.3, 'sine', 0.1); }
      else if (s) SFX.win(); else SFX.thud();
      if (s > (st.stars[st.lv] || 0)) { st.stars[st.lv] = s; } var tt = total(); if (tt > st.best) st.best = tt; saveJ('bullseye', st);
      msg.innerHTML = '<span class="fs-hs-n">' + (s ? s + '⭐' : '🎯') + '</span><div><b>' + esc((Lz.stopped || 'It stopped at') + ' ' + Math.round(d) + ' ' + U + ' (' + (Lz.target || 'target') + ' ' + L.target + ' ' + U + ')') + '</b>' + esc(line) + (L.tip && s ? ' ' + esc(L.tip) : '') + '</div>';
      msg.classList.remove('flash'); void msg.offsetWidth; msg.classList.add('flash');
      hud.innerHTML = hud.innerHTML; draw(); $('.fs-bx-car', stage).setAttribute('transform', 'translate(' + Math.min(W - 14, HX + d * PX) + ' ' + GY + ')');
      if (s && st.lv < B.levels.length - 1) { var nb = el('button', 'fs-btn alt fs-bx-next', '➡ ' + esc(B.nextBtn || 'Next level')); nb.type = 'button'; msg.appendChild(nb); nb.addEventListener('click', function () { st.lv++; saveJ('bullseye', st); h = Math.round((B.hMin + B.hMax) / 2); paintCtl(); draw(); msg.innerHTML = '<span class="fs-hs-n">🏁</span><div>' + esc(lv().tip0 || '') + '</div>'; }); }
      else if (s && st.lv === B.levels.length - 1) { msg.appendChild(el('div', 'fs-bx-done', esc(Lz.done || 'You beat every level!'))); var again = el('button', 'fs-btn alt', '🔁 ' + esc(Lz.again || 'Play again for more stars')); again.type = 'button'; msg.appendChild(again); again.addEventListener('click', function () { st.lv = 0; saveJ('bullseye', st); paintCtl(); draw(); }); }
    }
    function gate() { g.classList.toggle('locked', !store('solved')); }
    sv.parentNode.insertBefore(g, sv.nextSibling);
    document.addEventListener('fs:solved', gate);
    paintCtl(); draw(); gate(); msg.innerHTML = '<span class="fs-hs-n">🏁</span><div>' + esc(lv().tip0 || '') + '</div>';
  }

  /* ---------- Fold extras (18.02): an optional piece starts closed as a calm, inviting card. D.fold = {mod: {icon, tease, open}} ---------- */
  function foldExtras() {
    var Fo = D.fold; if (!Fo) return;
    Object.keys(Fo).forEach(function (k) {
      var g = $('.fs-game[data-mod="' + k + '"]'); if (!g || g.querySelector('.fs-fold')) return;
      var f = Fo[k], kick = $('.fs-game-k', g), title = $('.fs-game-t', g);
      var d = el('details', 'fs-fold'), sm = el('summary', 'fs-fold-s', '<span class="fs-fold-ic">' + (f.icon || '✨') + '</span><span class="fs-fold-tx"><small>' + esc(kick ? kick.textContent : '') + '</small><b>' + esc(title ? title.textContent : '') + '</b><em>' + esc(f.tease || '') + '</em></span><span class="fs-fold-go">' + esc(f.open || 'Open') + ' ▸</span>');
      d.appendChild(sm); var body = el('div', 'fs-fold-b'); d.appendChild(body);
      Array.prototype.slice.call(g.childNodes).forEach(function (n) { if (n !== kick && n !== title) body.appendChild(n); });
      if (kick) kick.remove(); if (title) title.remove();
      g.appendChild(d); g.classList.add('fs-folded');
      d.addEventListener('toggle', function () { if (d.open) SFX.blip(); });
    });
  }

  /* ---------- Night sky page (18.02): the lesson sits under a slow, twinkling sky; a shooting star crosses on every clue. D.nightsky = {stars, shoot:true} ---------- */
  function buildNightSky() {
    var N = D.nightsky; if (!N) return;
    html.classList.add('fs-night');
    var seed = 4242, s = '', tw = '';
    function rnd() { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }
    for (var i = 0; i < (N.stars || 260); i++) {
      var x = (rnd() * 100).toFixed(2), y = (rnd() * 100).toFixed(2), r = (0.4 + Math.pow(rnd(), 3) * 1.6).toFixed(2), o = (0.35 + rnd() * 0.6).toFixed(2);
      if (i % 9 === 0) tw += '<circle class="fs-ns-tw" style="animation-delay:-' + (rnd() * 6).toFixed(1) + 's" cx="' + x + '%" cy="' + y + '%" r="' + (+r + 0.4) + '"/>';
      else s += '<circle cx="' + x + '%" cy="' + y + '%" r="' + r + '" opacity="' + o + '"/>';
    }
    var sky = fsOnly(el('div', 'fs-ns', '<svg width="100%" height="100%" aria-hidden="true"><defs><radialGradient id="fsNsMw" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="#9FB4FF" stop-opacity=".16"/><stop offset="1" stop-color="#9FB4FF" stop-opacity="0"/></radialGradient></defs>' +
      '<ellipse cx="50%" cy="40%" rx="70%" ry="12%" fill="url(#fsNsMw)" transform="rotate(-24)" style="transform-origin:50% 40%"/><g fill="#fff">' + s + '</g><g fill="#FFF6DA">' + tw + '</g></svg>'));
    sky.setAttribute('aria-hidden', 'true');
    document.body.insertBefore(sky, document.body.firstChild);
  }
  function shootStar(big) {
    if (!D.nightsky || reduceMotion) return;
    var n = big ? 3 : 1;
    for (var i = 0; i < n; i++) (function (k) {
      setTimeout(function () {
        var m = fsOnly(el('i', 'fs-ns-shoot'));
        m.style.top = (6 + Math.random() * 30) + 'vh'; m.style.left = (8 + Math.random() * 50) + 'vw';
        document.body.appendChild(m); setTimeout(function () { m.remove(); }, 1800);
      }, k * 380);
    })(i);
  }

  /* ---------- Clue constellation (18.02): the 🗂 My clues dots become stars that join into a real constellation when the case cracks.
     D.constellation = {name, meaning, note, stars:[{x, y}] (one per clue, viewBox 0 0 120 40), lines:[[i, j]]} ---------- */
  function constellationSVG(found, solved, big) {
    var K = D.constellation, S = K.stars;
    var lines = K.lines.map(function (l) { var a = S[l[0]], b = S[l[1]], on = found[l[0]] && found[l[1]]; return '<line x1="' + a.x + '" y1="' + a.y + '" x2="' + b.x + '" y2="' + b.y + '" class="' + (on ? 'on' : '') + '"/>'; }).join('');
    var stars = S.map(function (p, i) { return '<circle cx="' + p.x + '" cy="' + p.y + '" r="' + (found[i] ? 3.4 : 2.2) + '" class="' + (found[i] ? 'on' : '') + '"/>'; }).join('');
    return '<svg viewBox="0 0 120 40" class="fs-cn' + (solved ? ' whole' : '') + (big ? ' big' : '') + '" role="img" aria-label="' + esc((solved ? 'The constellation ' + K.name : 'Your clue stars') + ': ' + found.filter(Boolean).length + ' of ' + S.length + ' lit') + '">' + lines + stars + (solved ? '<text x="60" y="38" text-anchor="middle">' + esc(K.name) + '</text>' : '') + '</svg>';
  }
  function paintConstellation() {
    var K = D.constellation, C = D.case, b = $('.fs-board'); if (!K || !C || !b) return;
    var ids = cluesFound().map(function (c) { return c.id; }), found = C.clues.map(function (c) { return ids.indexOf(c.id) > -1; }), solved = !!store('solved');
    $('.fs-board-dots', b).innerHTML = constellationSVG(found, solved, false);
    var more = $('.fs-board-more', b), card = $('.fs-cn-card', b);
    if (!card) { card = el('div', 'fs-cn-card'); more.insertBefore(card, more.firstChild); }
    card.innerHTML = constellationSVG(found, solved, true) + '<p>' + (solved ? '<b>' + esc(K.name) + '</b> ' + esc(K.meaning) + ' ' + esc(K.note) : esc(K.hint || 'Each clue you find lights a star. Find all four and see what they draw.')) + '</p>';
  }

  /* ---------- Bonus: my star party sky chart (18.02) — a real chart of the Florida sky (positions computed offline), with the student's name; print it.
     D.starchart = {after, kicker, title, teaser, when, where, how, pts:[{t, x, y, mag, kind:'star'|'planet'|'cluster'|'galaxy', label}], lines:[[a, b]] (point indexes), dirs, checks[], note, btn, printTitle} ---------- */
  function chartSVG(cls) {
    var C = D.starchart, R = 200, pts = C.pts;
    var dir = C.dirs || { N: 'NORTH', S: 'SOUTH', E: 'EAST', W: 'WEST' };
    var s = '<svg viewBox="-26 -26 452 452" class="' + cls + '" role="img" aria-label="' + esc(C.alt || 'A round sky chart') + '"><defs><radialGradient id="fsScG"><stop offset="0" stop-color="#1B2D63"/><stop offset="1" stop-color="#0A1330"/></radialGradient></defs>' +
      '<circle cx="200" cy="200" r="' + R + '" fill="url(#fsScG)" stroke="#C9B489" stroke-width="3"/>' +
      [30, 60].map(function (a) { return '<circle cx="200" cy="200" r="' + ((90 - a) / 90 * R) + '" fill="none" stroke="#2E4078" stroke-dasharray="3 5"/>'; }).join('');
    s += C.lines.map(function (l) { var a = pts[l[0]], b = pts[l[1]]; return '<line x1="' + a.x + '" y1="' + a.y + '" x2="' + b.x + '" y2="' + b.y + '" stroke="#8FA6E8" stroke-width="1.2" opacity=".7"/>'; }).join('');
    s += pts.map(function (p) {
      var r = Math.max(1.4, 5 - p.mag * 1.3);
      var g = p.kind === 'planet' ? '<circle cx="' + p.x + '" cy="' + p.y + '" r="5.5" fill="#F3D27A" stroke="#fff" stroke-width="1.5"/>' :
        p.kind === 'galaxy' ? '<ellipse cx="' + p.x + '" cy="' + p.y + '" rx="9" ry="3.5" fill="#C9B9FF" opacity=".8" transform="rotate(-30 ' + p.x + ' ' + p.y + ')"/>' :
        p.kind === 'cluster' ? [[0, 0], [4, -2], [-3, 2], [2, 4], [-2, -4], [5, 3]].map(function (d) { return '<circle cx="' + (p.x + d[0]) + '" cy="' + (p.y + d[1]) + '" r="1.4" fill="#CFE3FF"/>'; }).join('') :
        '<circle cx="' + p.x + '" cy="' + p.y + '" r="' + r.toFixed(1) + '" fill="#fff"/>';
      return g + (p.label ? '<text x="' + (p.x + (p.lx || 7)) + '" y="' + (p.y + (p.ly || 4)) + '"' + (p.anchor ? ' text-anchor="' + p.anchor + '"' : '') + ' class="lb' + (p.kind === 'planet' ? ' pl' : '') + '">' + esc(p.label) + '</text>' : '');
    }).join('');
    s += '<text x="200" y="-8" class="dir">' + dir.N + '</text><text x="200" y="420" class="dir">' + dir.S + '</text><text x="-12" y="200" class="dir" transform="rotate(-90 -12 200)">' + dir.E + '</text><text x="412" y="200" class="dir" transform="rotate(90 412 200)">' + dir.W + '</text></svg>';
    return s;
  }
  function buildStarchart() {
    var C = D.starchart; if (!C) return;
    var at = $(C.after); if (!at) { FAILED.push('starchart: anchor not found'); return; }
    var g = gameShell(C.kicker || 'Bonus', C.title, null, C.why); g.dataset.mod = 'starchart'; g.classList.add('fs-sc2');
    g.innerHTML += '<p class="fs-sc2-teaser">' + esc(C.teaser) + '</p><div class="fs-sc2-row"><div class="fs-sc2-chart">' + chartSVG('fs-sc2-svg') + '<div class="fs-sc2-when">🕗 ' + esc(C.when) + ' · ' + esc(C.where) + '</div></div>' +
      '<div class="fs-sc2-side"><div class="fs-in-k">' + esc(C.checkLabel || 'Can you find…') + '</div><ul class="fs-sc2-list">' + C.checks.map(function (c, i) { return '<li><label><input type="checkbox" data-i="' + i + '"> ' + esc(c) + '</label></li>'; }).join('') + '</ul>' +
      '<div class="fs-sc2-how">' + esc(C.how) + '</div><button type="button" class="fs-btn fs-sc2-print">🖨️ ' + esc(C.btn || 'Print my star chart') + '</button><div class="fs-sc2-note">' + esc(C.note) + '</div></div></div>' +
      (C.credit ? '<details class="fs-credit fs-credit-fold"><summary>🔭 Where these positions come from</summary>' + esc(C.credit) + '</details>' : '');
    var st = loadJ('starchart', {});
    $$('.fs-sc2-list input', g).forEach(function (b) { b.checked = !!st[b.dataset.i]; b.addEventListener('change', function () { st[b.dataset.i] = b.checked ? 1 : 0; saveJ('starchart', st); if (b.checked) { SFX.sparkle(); shootStar(false); } }); });
    $('.fs-sc2-print', g).addEventListener('click', function () {
      var name = getName(), w = window.open('', '_blank');
      if (!w) { showMiss(miss, C.blocked || 'Your browser blocked the print window. Allow pop-ups for this page, then try again.'); return; }
      w.document.write('<!doctype html><html><head><meta charset="utf-8"><title>' + esc(C.printTitle || 'My star chart') + '</title><style>body{font-family:Nunito,Arial,sans-serif;color:#0E1C42;margin:24px;text-align:center}h1{margin:0 0 2px;font-size:26px}h2{margin:0 0 10px;font-size:15px;color:#5C6F75;font-weight:700}svg{width:520px;max-width:100%;height:auto}.lb{font:700 11px Arial;fill:#fff}.lb.pl{fill:#F3D27A}.dir{font:800 13px Arial;fill:#0E1C42;text-anchor:middle}ul{display:inline-block;text-align:left;font-size:15px;line-height:1.8;margin:10px 0}p{font-size:13px;color:#555;max-width:560px;margin:6px auto}@media print{button{display:none}}</style></head><body>' +
        '<h1>⭐ ' + esc(name ? name + '’s star party sky' : (C.printTitle || 'My star party sky')) + '</h1><h2>' + esc(C.when) + ' · ' + esc(C.where) + '</h2>' + chartSVG('') +
        '<p><b>How to use it:</b> ' + esc(C.how) + '</p><ul>' + C.checks.map(function (c) { return '<li>☐ ' + esc(c) + '</li>'; }).join('') + '</ul><p>' + esc(C.note) + '</p><p style="font-size:11px">' + esc(C.credit || '') + '</p><button onclick="print()">🖨️ Print</button></body></html>');
      w.document.close(); setTimeout(function () { try { w.focus(); w.print(); } catch (e) {} }, 400); SFX.chime();
    });
    var miss = el('div', 'fs-miss'); g.appendChild(miss);
    at.parentNode.insertBefore(g, at.nextSibling);
  }

  /* ---------- Warm-Up: "Race the light" — guess how long ago each sky object's light left it, then send the light home and see (18.02) ----------
     D.racelight = {afterText, kicker, title, todo[], why, marks:[{k, t}], objs:[{id, name, img, alt, mark, left, dist}], sendBtn, earth, q, opts, credit, win, clue} */
  function buildRacelight() {
    var R = D.racelight; if (!R) return;
    var at = anchorP(R.afterText); if (!at) { FAILED.push('racelight anchor text not found'); return; }
    var g = gameShell(R.kicker || 'Warm-Up game', R.title, R.todo, R.why); g.dataset.mod = 'racelight';
    var st = loadJ('racelight', { at: {}, sent: 0 });
    var tray = el('div', 'fs-rl-tray'), rib = el('div', 'fs-rl-rib'), track = el('div', 'fs-rl-track', '<div class="fs-rl-src"></div><div class="fs-rl-line"><i class="fs-rl-beam"></i></div><div class="fs-rl-earth">' + esc(R.earth || '🌎 You') + '</div>');
    var send = el('button', 'fs-btn fs-rl-send', '✨ ' + esc(R.sendBtn || 'Send the light')); send.type = 'button';
    var miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    R.marks.forEach(function (m) { var z = el('div', 'fs-rl-mark', '<div class="fs-rl-tick"></div><b>' + esc(m.t) + '</b><div class="fs-rl-drop"></div>'); z.dataset.k = m.k; rib.appendChild(z); });
    function card(o) { var c = el('div', 'fs-card fs-rl-card', '<img alt="' + esc(o.alt) + '" src="' + esc(o.img) + '"><span>' + esc(o.name) + '</span><small class="fs-rl-stamp"></small>'); c.dataset.id = o.id; return c; }
    var cards = {}; R.objs.forEach(function (o) { cards[o.id] = card(o); });
    g.appendChild(el('div', 'fs-in-k', esc(R.trayLabel || 'Drag each one onto your guess:'))); g.appendChild(tray); g.appendChild(rib); g.appendChild(track);
    g.appendChild(send); g.appendChild(miss); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    if (R.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(R.credit)));
    var zones = $$('.fs-rl-mark', rib);
    function obj(id) { return R.objs.filter(function (o) { return o.id === id; })[0]; }
    function layout() {
      R.objs.forEach(function (o) {
        var c = cards[o.id], k = st.sent ? o.mark : st.at[o.id];
        var z = k ? zones.filter(function (z) { return z.dataset.k === k; })[0] : null;
        (z ? $('.fs-rl-drop', z) : tray).appendChild(c);
        c.classList.toggle('placed', !!st.sent);
      });
      var n = Object.keys(st.at).length;
      send.disabled = st.sent || n < R.objs.length;
      send.style.display = st.sent ? 'none' : '';
      if (!st.sent) count.textContent = n < R.objs.length ? '⏳ ' + n + ' of ' + R.objs.length + ' guesses placed' : '✨ All guesses placed. Now send the light!';
    }
    function drop(c, z) {
      if (st.sent) return; var k = z.dataset.k, id = c.dataset.id;
      Object.keys(st.at).forEach(function (o) { if (st.at[o] === k && o !== id) delete st.at[o]; });
      st.at[id] = k; saveJ('racelight', st); SFX.thud(); miss.classList.remove('show'); layout();
    }
    R.objs.forEach(function (o) { dragDrop(cards[o.id], function () { return zones; }, drop); });
    tapTargets(g, zones, drop);
    function stampAll(anim) {
      var right = 0;
      R.objs.forEach(function (o) {
        var c = cards[o.id], ok = st.at[o.id] === o.mark; if (ok) right++;
        c.classList.add(ok ? 'ok' : 'moved'); $('.fs-rl-stamp', c).textContent = (ok ? '✓ ' : '↪ ') + o.left;
        if (anim && !reduceMotion) { c.classList.remove('pop'); void c.offsetWidth; c.classList.add('pop'); }
      });
      count.textContent = '✨ You guessed ' + right + ' of ' + R.objs.length + ' right. Every one of these lights is old!'; count.classList.add('ok');
      askOnce(qh, R.q, R.opts, 'racelight-q', win, R.win, R.clue, 'racelight', miss);
    }
    send.addEventListener('click', function () {
      if (st.sent || Object.keys(st.at).length < R.objs.length) return;
      send.disabled = true; var src = $('.fs-rl-src', track), beam = $('.fs-rl-beam', track), i = 0;
      track.classList.add('on');
      (function next() {
        if (i >= R.objs.length) { track.classList.remove('on'); st.sent = 1; saveJ('racelight', st); layout(); stampAll(true); SFX.win(); return; }
        var o = R.objs[i], dur = reduceMotion ? 200 : [700, 1300, 2000, 2900][Math.min(i, 3)];
        src.innerHTML = '<img alt="" src="' + esc(o.img) + '"><span>' + esc(o.name) + '<small>' + esc(o.dist) + '</small></span>';
        beam.style.transition = 'none'; beam.style.left = '0%'; void beam.offsetWidth;
        beam.style.transition = 'left ' + dur + 'ms linear'; beam.style.left = '100%'; SFX.whoosh();
        var c = cards[o.id]; $('.fs-rl-stamp', c).textContent = '…';
        setTimeout(function () { SFX.chime(); var ok = st.at[o.id] === o.mark; $('.fs-rl-stamp', c).textContent = (ok ? '✓ ' : '↪ ') + o.left; c.classList.add(ok ? 'ok' : 'moved'); i++; setTimeout(next, 350); }, dur + 60);
      })();
    });
    at.parentNode.insertBefore(g, at.nextSibling);
    layout(); if (st.sent) stampAll(false);
  }

  /* ---------- Lesson Part 1: "Open wider" — a dark sky model; widen the opening (eye → owl → binoculars → telescope) and fainter stars appear; "Zoom only" makes things bigger, never brighter (18.02) ----------
     D.openwide = {afterText, kicker, title, todo[], why, stops:[{k, icon, name, img, alt, size, r (opening radius 0-100), limit (faintest star seen, 0-1), gain, note}], galaxyAt (stop index that shows the galaxy smudge), zoomBtn, zoomNote, needZoom, q, opts, credit, win, clue}
     The sky is a MODEL drawn in SVG (made-up star positions), not a photo. */
  function buildOpenwide() {
    var O = D.openwide; if (!O) return;
    var at = anchorP(O.afterText); if (!at) { FAILED.push('openwide anchor text not found'); return; }
    var g = gameShell(O.kicker || 'Part 1 game', O.title, O.todo, O.why); g.dataset.mod = 'openwide';
    var st = loadJ('openwide', { s: 0, zoom: 0 }), S = O.stops, last = S.length - 1, zoomed = false;
    /* made-up, repeatable star field: brightness m (0 = brightest) */
    var seed = 18021, stars = [];
    function rnd() { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }
    for (var i = 0; i < 320; i++) { var m = Math.pow(rnd(), 0.55); stars.push({ x: 6 + rnd() * 588, y: 6 + rnd() * 248, m: m }); }
    var starSvg = stars.map(function (s, i) { var r = (1.9 - s.m * 1.3).toFixed(2); return '<circle class="fs-ow-s" data-i="' + i + '" cx="' + s.x.toFixed(1) + '" cy="' + s.y.toFixed(1) + '" r="' + r + '"/>'; }).join('');
    var wrap = el('div', 'fs-ow-wrap');
    wrap.innerHTML = '<div class="fs-ow-ap"><svg viewBox="0 0 120 120" class="fs-ow-apsvg" aria-hidden="true"><circle cx="60" cy="60" r="56" class="fs-ow-rim"/><circle cx="60" cy="60" r="8" class="fs-ow-hole"/><circle cx="60" cy="60" r="8" class="fs-ow-handle" tabindex="0"/></svg>' +
      '<div class="fs-ow-who"></div><button type="button" class="fs-btn fs-ow-more">⭕ Open wider</button></div>' +
      '<div class="fs-ow-skybox"><div class="fs-ow-k">Palmetto Beach sky tonight <small>(a model)</small></div><svg viewBox="0 0 600 260" class="fs-ow-sky" role="img" aria-label="A model of a dark night sky. More stars appear as the opening gets wider."><g class="fs-ow-g"><ellipse class="fs-ow-gal" cx="430" cy="92" rx="16" ry="6" transform="rotate(-25 430 92)"/>' + starSvg + '</g></svg>' +
      '<div class="fs-ow-n"></div><button type="button" class="fs-btn alt fs-ow-zoom">🔍 ' + esc(O.zoomBtn || 'Zoom only') + '</button></div>';
    var info = el('div', 'fs-hs-card fs-ow-info'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(wrap); g.appendChild(info); g.appendChild(miss); g.appendChild(qh); g.appendChild(win);
    if (O.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(O.credit)));
    var hole = $('.fs-ow-hole', wrap), handle = $('.fs-ow-handle', wrap), apsvg = $('.fs-ow-apsvg', wrap), who = $('.fs-ow-who', wrap), more = $('.fs-ow-more', wrap), zoomB = $('.fs-ow-zoom', wrap), nBox = $('.fs-ow-n', wrap), gsky = $('.fs-ow-g', wrap), gal = $('.fs-ow-gal', wrap);
    var sEls = $$('.fs-ow-s', wrap), curR = S[st.s].r;
    function rOf(r) { return 8 + r / 100 * 46; }
    function setHole(r) { var rr = rOf(r); hole.setAttribute('r', rr); handle.setAttribute('cx', 60 + rr); }
    function paint(anim) {
      var s = S[st.s], lim = s.limit, n = 0;
      sEls.forEach(function (c) { var on = stars[+c.dataset.i].m <= lim; if (on) n++; c.classList.toggle('on', on); });
      gal.classList.toggle('on', O.galaxyAt != null && st.s >= O.galaxyAt);
      setHole(s.r); curR = s.r;
      who.innerHTML = (s.img ? '<img alt="' + esc(s.alt || s.name) + '" src="' + esc(s.img) + '">' : '<span class="fs-ow-ic">' + s.icon + '</span>') + '<b>' + esc(s.name) + '</b><small>' + esc(s.size) + '</small>';
      nBox.innerHTML = '⭐ Stars you can see: <b>' + n + '</b>';
      info.innerHTML = '<span class="fs-hs-n">' + s.icon + '</span><div><b>' + esc(s.gain) + '</b>' + esc(s.note) + '</div>';
      more.style.display = st.s < last ? '' : 'none';
      if (anim && !reduceMotion) { nBox.classList.remove('pop'); void nBox.offsetWidth; nBox.classList.add('pop'); }
      check();
    }
    function step() {
      if (st.s >= last) return; st.s++; saveJ('openwide', st); SFX.sparkle(); if (zoomed) toggleZoom(); paint(true);
    }
    more.addEventListener('click', step);
    /* drag the gold handle outward: the opening grows, and at the next size the next stop opens */
    var dragging = false;
    handle.addEventListener('pointerdown', function (e) { e.preventDefault(); dragging = true; handle.setPointerCapture && handle.setPointerCapture(e.pointerId); });
    handle.addEventListener('pointermove', function (e) {
      if (!dragging) return; var b = apsvg.getBoundingClientRect(), sx = 120 / b.width, dx = (e.clientX - b.left) * sx - 60, dy = (e.clientY - b.top) * sx - 60;
      var rr = Math.max(8, Math.min(54, Math.sqrt(dx * dx + dy * dy))), r = (rr - 8) / 46 * 100;
      if (st.s < last && r >= S[st.s + 1].r) { step(); return; }
      hole.setAttribute('r', Math.max(rOf(curR), rr)); handle.setAttribute('cx', 60 + Math.max(rOf(curR), rr));
    });
    function endDrag() { if (!dragging) return; dragging = false; setHole(S[st.s].r); }
    handle.addEventListener('pointerup', endDrag); handle.addEventListener('pointercancel', endDrag);
    handle.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ' || e.key === 'ArrowRight' || e.key === 'ArrowUp') { e.preventDefault(); step(); } });
    function toggleZoom() {
      zoomed = !zoomed; gsky.classList.toggle('zoomed', zoomed); wrap.classList.toggle('fs-ow-zoomed', zoomed);
      zoomB.textContent = zoomed ? '↩ Zoom back out' : '🔍 ' + (O.zoomBtn || 'Zoom only');
      $$('.fs-ow-try', info).forEach(function (x) { x.remove(); });
      if (zoomed) { if (!st.zoom) { st.zoom = 1; saveJ('openwide', st); } showMiss(miss, O.zoomNote); SFX.whoosh(); } else miss.classList.remove('show');
      check();
    }
    zoomB.addEventListener('click', toggleZoom);
    function check() { if (st.s >= last && (st.zoom || !O.needZoom)) askOnce(qh, O.q, O.opts, 'openwide-q', win, O.win, O.clue, 'openwide', miss); else if (st.s >= last && !st.zoom) info.innerHTML += '<div class="fs-ow-try">' + esc(O.tryZoom || 'Now press Zoom only. Does zooming in show you any NEW stars?') + '</div>'; }
    at.parentNode.insertBefore(g, at.nextSibling);
    paint(false);
  }

  /* ---------- Lesson Part 2: "Find it in the sky" — drag a binocular or telescope viewfinder over a sky model; the eyepiece shows each target through that tool (18.02) ----------
     D.skyhunt = {afterText, replace, kicker, title, todo[], why, tools:[{k, icon, t, power, r (view radius, sky units), hit}], targets:[{id, name, icon, x, y, draw, views:{<toolK>:{img, size, pos, html, note}}, best, q, opts}], credit, win, clue}
     The sky and the target dots are a MODEL; the eyepiece views use real photos. */
  function buildSkyhunt() {
    var H = D.skyhunt; if (!H) return;
    var at = anchorP(H.afterText); if (!at) { FAILED.push('skyhunt anchor text not found'); return; }
    if (H.replace) $$(H.replace).forEach(function (x) { x.classList.add('fs-replaced'); });
    var g = gameShell(H.kicker || 'Part 2 game', H.title, H.todo, H.why); g.dataset.mod = 'skyhunt';
    var st = loadJ('skyhunt', { seen: {}, best: {} }), tool = H.tools[0].k, cx = 500, cy = 420;
    var seed = 1802, stars = '';
    function rnd() { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }
    for (var i = 0; i < 170; i++) stars += '<circle cx="' + (rnd() * 1000).toFixed(0) + '" cy="' + (rnd() * 560).toFixed(0) + '" r="' + (0.6 + rnd() * 1.6).toFixed(1) + '" opacity="' + (0.35 + rnd() * 0.6).toFixed(2) + '"/>';
    function drawT(t) {
      if (t.draw === 'moon') return '<circle cx="' + t.x + '" cy="' + t.y + '" r="24" fill="#E9E6DA"/><circle cx="' + (t.x - 7) + '" cy="' + (t.y - 5) + '" r="6" fill="#CFCABB"/><circle cx="' + (t.x + 8) + '" cy="' + (t.y + 7) + '" r="4" fill="#CFCABB"/>';
      if (t.draw === 'cluster') return [[0, 0], [9, -4], [-8, 5], [4, 9], [-3, -9], [13, 6], [-12, -3]].map(function (p, i) { return '<circle cx="' + (t.x + p[0]) + '" cy="' + (t.y + p[1]) + '" r="' + (i < 3 ? 2.2 : 1.5) + '" fill="#CFE3FF"/>'; }).join('');
      return '<circle cx="' + t.x + '" cy="' + t.y + '" r="' + (t.draw === 'bright' ? 4.2 : 3.4) + '" fill="' + (t.draw === 'bright' ? '#FFF7E0' : '#F3D9A0') + '"/>';
    }
    var sky = el('div', 'fs-sh-skywrap');
    sky.innerHTML = '<svg viewBox="0 0 1000 560" class="fs-sh-sky" role="img" aria-label="A model of the night sky over the beach with the Moon, two planets and a small star cluster. Drag the viewfinder circle."><rect width="1000" height="560" fill="url(#fsShG)"/><defs><linearGradient id="fsShG" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#050B1E"/><stop offset="1" stop-color="#14254D"/></linearGradient></defs><g fill="#fff">' + stars + '</g>' +
      H.targets.map(function (t) { return '<g class="fs-sh-t" data-id="' + t.id + '">' + drawT(t) + '<text x="' + t.x + '" y="' + (t.y + (t.draw === 'moon' ? 44 : 22)) + '" text-anchor="middle">' + esc(t.name) + '</text></g>'; }).join('') +
      '<path d="M0,540 Q250,515 500,532 T1000,526 L1000,560 L0,560Z" fill="#0A1426"/><circle class="fs-sh-vf" r="60"/><line class="fs-sh-x1"/><line class="fs-sh-x2"/></svg>';
    var side = el('div', 'fs-sh-side', '<div class="fs-sh-tools">' + H.tools.map(function (t) { return '<button type="button" class="fs-sh-tool" data-k="' + t.k + '"><span>' + t.icon + '</span><b>' + esc(t.t) + '</b><small>' + esc(t.power) + '</small></button>'; }).join('') + '</div>' +
      '<div class="fs-sh-eye"><div class="fs-sh-view"></div><span class="fs-sh-eyek"></span></div><div class="fs-sh-note"></div>');
    var row = el('div', 'fs-sh-row'); row.appendChild(sky); row.appendChild(side);
    var list = el('div', 'fs-sh-list'), miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), win = el('div', 'fs-win');
    H.targets.forEach(function (t) { var c = el('div', 'fs-sh-card', '<div class="fs-sh-ch"><span>' + t.icon + '</span><b>' + esc(t.name) + '</b><i class="fs-sh-chk"></i></div><div class="fs-sh-cq"></div>'); c.dataset.id = t.id; list.appendChild(c); });
    g.appendChild(row); g.appendChild(el('div', 'fs-in-k', esc(H.listLabel || 'Your sky list'))); g.appendChild(list); g.appendChild(miss); g.appendChild(count); g.appendChild(win);
    if (H.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(H.credit)));
    var svg = $('.fs-sh-sky', sky), vf = $('.fs-sh-vf', sky), x1 = $('.fs-sh-x1', sky), x2 = $('.fs-sh-x2', sky), view = $('.fs-sh-view', side), eyek = $('.fs-sh-eyek', side), note = $('.fs-sh-note', side);
    function T(k) { return H.tools.filter(function (t) { return t.k === k; })[0]; }
    function target(id) { return H.targets.filter(function (t) { return t.id === id; })[0]; }
    function onTarget() { var tl = T(tool), hit = null, w = svg.getBoundingClientRect().width || 1000, r = Math.max(tl.hit || 40, 20 * 1000 / w); H.targets.forEach(function (t) { var d = Math.sqrt((t.x - cx) * (t.x - cx) + (t.y - cy) * (t.y - cy)); if (d <= r) hit = t; }); return hit; }
    function paint(fresh) {
      var tl = T(tool); vf.setAttribute('cx', cx); vf.setAttribute('cy', cy); vf.setAttribute('r', tl.r);
      x1.setAttribute('x1', cx - 8); x1.setAttribute('x2', cx + 8); x1.setAttribute('y1', cy); x1.setAttribute('y2', cy);
      x2.setAttribute('y1', cy - 8); x2.setAttribute('y2', cy + 8); x2.setAttribute('x1', cx); x2.setAttribute('x2', cx);
      $$('.fs-sh-tool', side).forEach(function (b) { b.classList.toggle('on', b.dataset.k === tool); });
      eyek.textContent = tl.icon + ' ' + tl.t;
      var t = onTarget();
      $$('.fs-sh-t', sky).forEach(function (n) { n.classList.toggle('on', !!t && n.dataset.id === t.id); });
      if (!t) { view.className = 'fs-sh-view empty'; view.style.backgroundImage = ''; view.innerHTML = '<span>' + esc(H.emptyLine || 'Just dark sky. Move the circle onto something.') + '</span>'; note.innerHTML = ''; return; }
      var v = t.views[tool]; view.className = 'fs-sh-view' + (v.img ? ' photo' : '');
      view.style.backgroundImage = v.img ? 'url("' + v.img + '")' : ''; view.style.backgroundSize = v.size || 'cover'; view.style.backgroundPosition = v.pos || 'center';
      view.innerHTML = v.html || ''; note.innerHTML = '<b>' + t.icon + ' ' + esc(t.name) + ' · ' + esc(tl.t) + '</b>' + esc(v.note);
      if (fresh && !reduceMotion) { view.classList.remove('fs-sh-in'); void view.offsetWidth; view.classList.add('fs-sh-in'); }
      var sk = st.seen[t.id] || {}; if (!sk[tool]) { sk[tool] = 1; st.seen[t.id] = sk; saveJ('skyhunt', st); SFX.chime(); upd(); }
    }
    function moveTo(e) { var b = svg.getBoundingClientRect(), s = 1000 / b.width; cx = Math.max(10, Math.min(990, (e.clientX - b.left) * s)); cy = Math.max(10, Math.min(550, (e.clientY - b.top) * s)); }
    var down = false, lastId = null;
    svg.addEventListener('pointerdown', function (e) { e.preventDefault(); down = true; svg.setPointerCapture && svg.setPointerCapture(e.pointerId); moveTo(e); var t = onTarget(); lastId = t && t.id; paint(true); });
    svg.addEventListener('pointermove', function (e) { if (!down) return; moveTo(e); var t = onTarget(), id = t && t.id; paint(id !== lastId); lastId = id; });
    svg.addEventListener('pointerup', function () { down = false; }); svg.addEventListener('pointercancel', function () { down = false; });
    $$('.fs-sh-tool', side).forEach(function (b) { b.addEventListener('click', function () { tool = b.dataset.k; SFX.blip(); paint(true); }); });
    function upd() {
      var done = 0;
      H.targets.forEach(function (t) {
        var c = $('.fs-sh-card[data-id="' + t.id + '"]', list), sk = st.seen[t.id] || {}, both = H.tools.every(function (tl) { return sk[tl.k]; });
        $('.fs-sh-chk', c).textContent = H.tools.map(function (tl) { return (sk[tl.k] ? '✓' : '○') + ' ' + tl.icon; }).join('  ');
        c.classList.toggle('ready', both);
        var qh = $('.fs-sh-cq', c);
        if (both && !qh.dataset.on) {
          qh.dataset.on = '1';
          chipsQ(qh, t.q, t.opts, function () { st.best[t.id] = 1; saveJ('skyhunt', st); c.classList.add('done'); upd(); }, miss);
          if (st.best[t.id]) { var k = t.opts.map(function (o, i) { return o.ok ? i : -1; }).filter(function (i) { return i > -1; })[0]; $$('.fs-in-chip', qh)[k].classList.add('on', 'ok'); $('.fs-sv-q', qh).dataset.done = '1'; c.classList.add('done'); }
        }
        if (st.best[t.id]) done++;
      });
      count.textContent = '🔭 ' + done + ' of ' + H.targets.length + ' sky targets matched to the best tool'; count.classList.toggle('ok', done === H.targets.length);
      if (done === H.targets.length) winOnce(win, H.win, H.clue, 'skyhunt');
    }
    at.parentNode.insertBefore(g, at.nextSibling);
    paint(false); upd();
  }

  /* ---------- Lesson Part 3: "On TV" — an old TV news report (a second ElevenLabs voice) over real photos, with captions and a crawl; then one chip question (18.02) ----------
     D.tv = {afterText, kicker, title, todo[], why, channel, live, headline, place, date, slides:[{img, alt, cap}], lineSlides[], audio, lines[], ticker, playBtn, againBtn, q, opts, credit, win} */
  function buildTv() {
    var V = D.tv; if (!V) return;
    var at = anchorP(V.afterText); if (!at) { FAILED.push('tv anchor text not found'); return; }
    var g = gameShell(V.kicker || 'Breaking news', V.title, V.todo, V.why); g.dataset.mod = 'tv';
    var set = el('div', 'fs-tv-set');
    set.innerHTML = '<div class="fs-tv-screen">' + V.slides.map(function (s, i) { return '<img class="fs-tv-slide' + (i === 0 ? ' on' : '') + '" alt="' + esc(s.alt) + '" src="' + esc(s.img) + '">'; }).join('') +
      '<div class="fs-tv-bug"><span class="fs-tv-live">' + esc(V.live || 'LIVE') + '</span><span class="fs-tv-ch">' + esc(V.channel) + '</span></div>' +
      '<div class="fs-tv-cap" aria-live="polite"></div>' +
      '<div class="fs-tv-lower"><b>' + esc(V.headline) + '</b><span>' + esc(V.place) + ' · ' + esc(V.date) + '</span></div>' +
      '<div class="fs-tv-crawl"><span>' + esc(V.ticker) + '</span></div>' +
      '<button type="button" class="fs-tv-play">▶ ' + esc(V.playBtn || 'Watch the report') + '</button><div class="fs-tv-scan"></div></div>' +
      '<div class="fs-tv-base"><i></i><i></i><span>' + esc(V.channel) + '</span></div>';
    var slideCap = el('div', 'fs-tv-slidecap'), tr = el('details', 'fs-tv-tr', '<summary>📄 Read the report</summary><p>' + V.lines.map(esc).join(' ') + '</p>');
    var miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(set); g.appendChild(slideCap); g.appendChild(tr); g.appendChild(miss); g.appendChild(qh); g.appendChild(win);
    if (V.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(V.credit)));
    var scr = $('.fs-tv-screen', set), cap = $('.fs-tv-cap', set), play = $('.fs-tv-play', set), slides = $$('.fs-tv-slide', set), audio = null, busy = false, timer = null;
    function showSlide(i) { slides.forEach(function (s, j) { s.classList.toggle('on', j === i); }); slideCap.textContent = '📷 ' + (V.slides[i] && V.slides[i].cap || ''); }
    showSlide(0);
    var words = V.lines.map(function (l) { return l.split(/\s+/).length; }), total = words.reduce(function (a, b) { return a + b; }, 0);
    function lineAt(frac) { var acc = 0; for (var i = 0; i < words.length; i++) { acc += words[i] / total; if (frac < acc) return i; } return words.length - 1; }
    function show(i) { cap.textContent = V.lines[i]; var s = (V.lineSlides || [])[i]; if (s != null) showSlide(s); }
    function done() {
      busy = false; clearInterval(timer); scr.classList.remove('on'); play.style.display = ''; play.textContent = '▶ ' + (V.againBtn || 'Watch it again'); cap.textContent = '';
      store('tv-seen', '1'); askOnce(qh, V.q, V.opts, 'tv-q', win, V.win, null, 'tv', miss);
    }
    function speakIt() {
      var ss = window.speechSynthesis; if (!ss) { done(); return; }
      var i = 0; (function say() { if (!busy) return; if (i >= V.lines.length) { done(); return; } show(i); var u = new SpeechSynthesisUtterance(V.lines[i]); u.rate = 0.98; u.onend = function () { i++; say(); }; ss.speak(u); })();
    }
    play.addEventListener('click', function () {
      if (busy) return; busy = true; play.style.display = 'none'; scr.classList.add('on'); SFX.chime();
      var src = (D.paths && D.paths.audio || 'assets/audio/guide/') + (D.guide || 'crew') + '/' + D.prefix + '-' + (V.audio || 'tv') + '.mp3';
      audio = new Audio(au(src));
      audio.addEventListener('ended', done);
      audio.addEventListener('error', function () { if (busy) { clearInterval(timer); speakIt(); } });
      timer = setInterval(function () { if (audio.duration) show(lineAt(audio.currentTime / audio.duration)); }, 150);
      var p = audio.play(); if (p && p.catch) p.catch(function () { if (busy) { clearInterval(timer); speakIt(); } });
    });
    scr.addEventListener('click', function (e) { if (busy && e.target !== play) { if (audio) audio.pause(); if (window.speechSynthesis) speechSynthesis.cancel(); done(); } });
    at.parentNode.insertBefore(g, at.nextSibling);
    if (store('tv-seen')) askOnce(qh, V.q, V.opts, 'tv-q', win, V.win, null, 'tv', miss);
  }

  /* ---------- Lesson Part 4: "Stare at nothing" — one empty-looking speck of sky through each tool; then press and HOLD Webb's shutter and the real deep field fades in; tap three galaxy shapes (18.02) ----------
     D.deepfield = {afterText, kicker, title, todo[], why, tools:[{k, icon, t, view:'empty'|'smudge'|'webb', note}], hold:{btn, hours, ms, label}, img, alt, shapes:[{k, t, x, y, r, found}], star:{x, y, r, t}, hint, findLabel, q, opts, credit, win, clue} */
  function buildDeepfield() {
    var F = D.deepfield; if (!F) return;
    var at = anchorP(F.afterText); if (!at) { FAILED.push('deepfield anchor text not found'); return; }
    var g = gameShell(F.kicker || 'Part 4 game', F.title, F.todo, F.why); g.dataset.mod = 'deepfield';
    var st = loadJ('deepfield', { t: 0, p: 0, f: {} }), T = F.tools, lastT = T.length - 1, hrs = F.hold.hours, ms = F.hold.ms || 6000, misses = 0;
    var dial = el('div', 'fs-df-tools', T.map(function (t, i) { return '<button type="button" class="fs-df-tool" data-i="' + i + '"><span>' + t.icon + '</span><b>' + esc(t.t) + '</b><i class="fs-zm-lock">🔒</i></button>'; }).join(''));
    var view = el('div', 'fs-df-view', '<div class="fs-df-sky"><i style="left:22%;top:30%"></i><i style="left:71%;top:64%"></i><i style="left:44%;top:81%"></i></div><div class="fs-df-smudge"><i style="left:38%;top:42%"></i><i style="left:63%;top:58%"></i></div><img class="fs-df-img" alt="' + esc(F.alt) + '" src="' + esc(F.img) + '"><div class="fs-df-rings"></div><span class="fs-df-tag"></span>');
    var holdB = el('button', 'fs-btn fs-df-hold', '📸 ' + esc(F.hold.btn || 'Press and hold to open Webb’s shutter')); holdB.type = 'button';
    var clock = el('div', 'fs-df-clock'), info = el('div', 'fs-hs-card fs-df-info'), finds = el('div', 'fs-df-finds'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(dial); g.appendChild(view); g.appendChild(holdB); g.appendChild(clock); g.appendChild(info); g.appendChild(finds); g.appendChild(miss); g.appendChild(qh); g.appendChild(win);
    if (F.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(F.credit)));
    var img = $('.fs-df-img', view), tag = $('.fs-df-tag', view), rings = $('.fs-df-rings', view), cur = Math.min(st.t, lastT);
    F.shapes.forEach(function (s) { var r = el('i', 'fs-df-ring'); r.style.left = s.x + '%'; r.style.top = s.y + '%'; r.style.width = r.style.height = (2 * s.r) + '%'; r.dataset.k = s.k; rings.appendChild(r); });
    function exposed() { return st.p >= 1; }
    function paint() {
      var t = T[cur];
      $$('.fs-df-tool', dial).forEach(function (b, i) { b.classList.toggle('on', i === cur); b.classList.toggle('locked', i > st.t); b.classList.toggle('done', i < st.t || (i === lastT && exposed())); });
      view.className = 'fs-df-view v-' + t.view + (t.view === 'webb' && exposed() ? ' exposed' : '');
      img.style.opacity = t.view === 'webb' ? Math.pow(st.p, 1.4) : 0; img.style.filter = t.view === 'webb' ? 'brightness(' + (0.4 + 0.6 * st.p) + ')' : '';
      tag.textContent = t.icon + ' ' + t.t;
      holdB.style.display = t.view === 'webb' && !exposed() ? '' : 'none';
      clock.style.display = t.view === 'webb' ? '' : 'none';
      clock.innerHTML = '⏱ ' + esc(F.hold.label || 'Shutter open') + ': <b>' + (hrs * st.p).toFixed(1) + ' hours</b> of ' + hrs;
      info.innerHTML = '<span class="fs-hs-n">' + t.icon + '</span><div><b>' + esc(t.t) + '</b>' + esc(t.view === 'webb' && exposed() ? F.doneNote : t.note) + '</div>';
      if (t.view !== 'webb') { var nx = $$('.fs-df-tool', dial)[cur + 1]; if (nx && cur === st.t) { st.t = cur + 1; saveJ('deepfield', st); setTimeout(paint, 0); } }
      finds.style.display = exposed() && t.view === 'webb' ? '' : 'none';
      drawFinds();
    }
    $$('.fs-df-tool', dial).forEach(function (b) { b.addEventListener('click', function () { var i = +b.dataset.i; if (i > st.t) { bounce(b, miss, F.lockLine || 'Look through the tool before this one first.'); return; } cur = i; SFX.whoosh(); miss.classList.remove('show'); paint(); }); });
    /* press and hold: the shutter stays open only while held */
    var t0 = null, raf = null, p0 = 0;
    function tick(now) { if (t0 == null) return; st.p = Math.min(1, p0 + (now - t0) / ms); paint(); if (st.p >= 1) { stop(true); return; } raf = requestAnimationFrame(tick); }
    function start(e) { if (e) e.preventDefault(); if (exposed() || t0 != null) return; t0 = performance.now(); p0 = st.p; holdB.classList.add('down'); view.classList.add('holding'); SFX.blip(); raf = requestAnimationFrame(tick); }
    function stop(fin) { if (t0 == null) return; t0 = null; cancelAnimationFrame(raf); holdB.classList.remove('down'); view.classList.remove('holding'); saveJ('deepfield', st); if (fin) { SFX.sparkle(); paint(); } else if (st.p < 1) showMiss(miss, F.hold.letGo || 'You let go, so the shutter closed. Press and hold again to keep collecting light.'); }
    holdB.addEventListener('pointerdown', start);
    ['pointerup', 'pointerleave', 'pointercancel'].forEach(function (ev) { holdB.addEventListener(ev, function () { stop(false); }); });
    holdB.addEventListener('keydown', function (e) { if ((e.key === ' ' || e.key === 'Enter') && !e.repeat) start(e); });
    holdB.addEventListener('keyup', function (e) { if (e.key === ' ' || e.key === 'Enter') stop(false); });
    holdB.addEventListener('contextmenu', function (e) { e.preventDefault(); });
    function drawFinds() {
      var n = F.shapes.filter(function (s) { return st.f[s.k]; }).length;
      finds.innerHTML = '<div class="fs-in-k">' + esc(F.findLabel || 'Tap three galaxy shapes:') + '</div><div class="fs-df-list">' + F.shapes.map(function (s) { return '<span class="' + (st.f[s.k] ? 'on' : '') + '">' + (st.f[s.k] ? '✓ ' : '○ ') + esc(s.t) + '</span>'; }).join('') + '</div>';
      $$('.fs-df-ring', rings).forEach(function (r) { r.classList.toggle('found', !!st.f[r.dataset.k]); });
      if (n === F.shapes.length) askOnce(qh, F.q, F.opts, 'deepfield-q', win, F.win, F.clue, 'deepfield', miss);
    }
    view.addEventListener('click', function (e) {
      if (T[cur].view !== 'webb' || !exposed()) return;
      var b = view.getBoundingClientRect(), x = (e.clientX - b.left) / b.width * 100, y = (e.clientY - b.top) / b.height * 100;
      function near(s) { var dx = x - s.x, dy = y - s.y; return Math.sqrt(dx * dx + dy * dy) <= s.r; }
      var hit = F.shapes.filter(near)[0];
      if (hit) { if (!st.f[hit.k]) { st.f[hit.k] = 1; saveJ('deepfield', st); SFX.chime(); showMiss(miss, hit.found); miss.classList.add('good'); drawFinds(); } return; }
      if (F.star && near(F.star)) { miss.classList.remove('good'); showMiss(miss, F.star.t); return; }
      misses++; miss.classList.remove('good'); showMiss(miss, F.hint); if (misses >= 2) rings.classList.add('hint');
    });
    at.parentNode.insertBefore(g, at.nextSibling);
    paint();
  }

  /* ---------- Assignment: the star party permit — unlocked after the case is cracked: tap the darkest place on a real photo of Florida at night, pick why, stamp APPROVED; then Sam's P.S. card (18.02) ----------
     D.permit = {kicker, title, todo[], head, sub, rows:[[k, v]], placeLabel, mapQ, img, alt, spots:[{k, t, x, y, ok, miss, why}], whyLabel, whyQ, whyOpts, stamp, sign, lockLine, ps:{head, img, alt, t, credit}, credit} */
  function buildPermit() {
    var P = D.permit; if (!P) return;
    var sv = $('.fs-solve'); if (!sv) { FAILED.push('permit: no Crack the case box'); return; }
    var g = gameShell(P.kicker || 'Case closed', P.title, P.todo, P.why); g.dataset.mod = 'permit'; g.classList.add('fs-pm');
    var st = loadJ('permit', {});
    var form = el('div', 'fs-pm-form', '<div class="fs-pm-head">' + esc(P.head) + '</div><div class="fs-pm-sub">' + esc(P.sub || '') + '</div><dl>' + P.rows.map(function (r) { return '<dt>' + esc(r[0]) + '</dt><dd>' + esc(r[1]) + '</dd>'; }).join('') +
      '<dt>' + esc(P.placeLabel || 'Place') + '</dt><dd class="fs-pm-place">______</dd><dt>' + esc(P.whyLabel || 'Why there') + '</dt><dd class="fs-pm-why">______</dd></dl><div class="fs-pm-stamp">' + esc(P.stamp || 'APPROVED') + '</div><div class="fs-pm-sign"></div></div>');
    var map = el('div', 'fs-pm-map', '<div class="fs-in-k">' + esc(P.mapQ) + '</div><div class="fs-pm-photo"><img alt="' + esc(P.alt) + '" src="' + esc(P.img) + '">' + P.spots.map(function (s) { return '<button type="button" class="fs-pm-spot' + (s.side ? ' ' + s.side : '') + '" data-k="' + s.k + '" style="left:' + s.x + '%;top:' + s.y + '%"><i></i><span>' + esc(s.t) + '</span></button>'; }).join('') + '</div>');
    var lock = el('div', 'fs-lock', '🔒 <span>' + esc(P.lockLine || 'Crack the case first. Then Sam’s permit opens.') + '</span>');
    var qh = el('div'), miss = el('div', 'fs-miss'), ps = el('div', 'fs-pm-ps');
    g.appendChild(lock); g.appendChild(form); g.appendChild(map); g.appendChild(qh); g.appendChild(miss); g.appendChild(ps);
    if (P.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(P.credit)));
    if (P.ps) ps.innerHTML = '<details class="fs-fold"><summary class="fs-fold-s"><span class="fs-fold-ic">✉️</span><span class="fs-fold-tx"><small>' + esc(P.ps.kicker || 'One more thing') + '</small><b>' + esc(P.ps.head) + '</b><em>' + esc(P.ps.tease || '') + '</em></span><span class="fs-fold-go">Open ▸</span></summary><div class="fs-fold-b"><div class="fs-pm-psrow"><img alt="' + esc(P.ps.alt) + '" src="' + esc(P.ps.img) + '"><p>' + esc(P.ps.t) + '</p></div>' + (P.ps.credit ? '<div class="fs-credit">' + esc(P.ps.credit) + '</div>' : '') + '</div></details>';
    function spot(k) { return P.spots.filter(function (s) { return s.k === k; })[0]; }
    function paint(anim) {
      var open = !!store('solved'); g.classList.toggle('locked', !open);
      var right = P.spots.filter(function (s) { return s.ok; })[0];
      if (st.place) { $('.fs-pm-place', form).textContent = right.t; $$('.fs-pm-spot', map).forEach(function (b) { b.classList.toggle('ok', b.dataset.k === right.k); }); }
      if (st.place && !qh.dataset.on) { qh.dataset.on = '1'; chipsQ(qh, P.whyQ, P.whyOpts, function (o) { st.why = 1; saveJ('permit', st); paint(true); }, miss); }
      if (st.why) { var k = P.whyOpts.map(function (o, i) { return o.ok ? i : -1; }).filter(function (i) { return i > -1; })[0], o = P.whyOpts[k]; $('.fs-pm-why', form).textContent = o.fill || o.t; var c = $$('.fs-in-chip', qh)[k]; if (c) c.classList.add('on', 'ok'); var w = $('.fs-sv-q', qh); if (w) w.dataset.done = '1'; }
      var done = st.place && st.why; form.classList.toggle('stamped', !!done); $('.fs-pm-sign', form).textContent = done ? P.sign : '';
      if (done && anim && !reduceMotion) { form.classList.remove('thump'); void form.offsetWidth; form.classList.add('thump'); SFX.stamp(); setTimeout(SFX.win, 350); }
      ps.style.display = done && P.ps ? '' : 'none';
      if (done) store('permit-done', '1');
    }
    $$('.fs-pm-spot', map).forEach(function (b) { b.addEventListener('click', function () {
      if (!store('solved') || st.place) return; var s = spot(b.dataset.k);
      if (!s.ok) { bounce(b, miss, s.miss); return; }
      miss.classList.remove('show'); st.place = 1; saveJ('permit', st); SFX.chime(); showMiss(miss, s.why); miss.classList.add('good'); paint(true);
    }); });
    sv.parentNode.insertBefore(g, sv.nextSibling);
    document.addEventListener('fs:solved', function () { paint(false); });
    paint(false);
  }

  /* ---------- Warm-Up: "The zoom machine" — turn the dial from your eyes to a hand lens, a light microscope and an electron microscope; at each stop, tap the new detail you can see (18.01) ----------
     D.zoom = {afterText | afterSel, kicker, title, todo[], why, stops:[{k, icon, tool, power, img, alt, see, hint, spot:{x, y, r, t}}], lockLine, q, opts, credit, win, clue} */
  function buildZoom() {
    var Z = D.zoom; if (!Z) return;
    var at = Z.afterSel ? $(Z.afterSel) : anchorP(Z.afterText); if (!at) { FAILED.push('zoom anchor not found'); return; }
    var g = gameShell(Z.kicker || 'Warm-Up game', Z.title, Z.todo, Z.why); g.dataset.mod = 'zoom';
    var st = loadJ('zoom', {}), cur = 0, misses = 0;
    var dial = el('div', 'fs-zm-dial');
    Z.stops.forEach(function (s, i) {
      var b = el('button', 'fs-zm-stop', '<span class="fs-zm-ic">' + s.icon + '</span><b>' + esc(s.tool) + '</b><small>' + esc(s.power) + '</small><i class="fs-zm-lock">🔒</i>');
      b.type = 'button'; b.dataset.i = i; dial.appendChild(b);
      if (i < Z.stops.length - 1) dial.appendChild(el('span', 'fs-zm-arrow', '›'));
    });
    var view = el('div', 'fs-zm-view', '<div class="fs-zm-lens"><img alt=""><button type="button" class="fs-zm-spot" aria-label="Tap the new detail"></button><span class="fs-zm-pow"></span></div>');
    var info = el('div', 'fs-hs-card fs-zm-info'), miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(dial); g.appendChild(view); g.appendChild(info); g.appendChild(miss); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    if (Z.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(Z.credit)));
    var lens = $('.fs-zm-lens', view), img = $('img', view), spot = $('.fs-zm-spot', view), pow = $('.fs-zm-pow', view);
    function open(i) { return i === 0 || !!st[Z.stops[i - 1].k]; }
    function paintDial() {
      $$('.fs-zm-stop', dial).forEach(function (b, i) {
        b.classList.toggle('on', i === cur); b.classList.toggle('done', !!st[Z.stops[i].k]); b.classList.toggle('locked', !open(i));
      });
    }
    function show(i, anim) {
      var s = Z.stops[i]; cur = i; misses = 0; paintDial();
      img.src = s.img; img.alt = s.alt; pow.textContent = s.icon + ' ' + s.power;
      spot.style.left = s.spot.x + '%'; spot.style.top = s.spot.y + '%'; spot.style.width = spot.style.height = (s.spot.r || 18) + '%';
      spot.classList.toggle('found', !!st[s.k]); spot.classList.remove('hint');
      if (anim && !reduceMotion) { lens.classList.remove('zoomin'); void lens.offsetWidth; lens.classList.add('zoomin'); }
      if (st[s.k]) info.innerHTML = '<span class="fs-hs-n">' + s.icon + '</span><div><b>' + esc(s.spot.t) + '</b>' + esc(s.see) + '</div>';
      else info.innerHTML = '<span class="fs-hs-n">🔎</span><div><b>' + esc(s.tool + ' · ' + s.power) + '</b>' + esc(s.ask || 'Look closely. Tap the new detail you can see now.') + '</div>';
      miss.classList.remove('show');
    }
    $$('.fs-zm-stop', dial).forEach(function (b) { b.addEventListener('click', function () {
      var i = +b.dataset.i;
      if (!open(i)) { bounce(b, miss, Z.lockLine || 'Find the new detail at this stop first. Then turn the dial.'); return; }
      SFX.whoosh(); show(i, true);
    }); });
    spot.addEventListener('click', function (e) {
      e.stopPropagation(); var s = Z.stops[cur]; if (st[s.k]) return;
      st[s.k] = 1; saveJ('zoom', st); SFX.chime(); spot.classList.add('found'); spot.classList.remove('hint'); show(cur, false); upd();
      var nx = $$('.fs-zm-stop', dial)[cur + 1]; if (nx && !reduceMotion) { nx.classList.remove('nudge'); void nx.offsetWidth; nx.classList.add('nudge'); }
    });
    lens.addEventListener('click', function () {
      var s = Z.stops[cur]; if (st[s.k]) return; misses++;
      bounce(lens, miss, s.hint); if (misses >= 2) spot.classList.add('hint');
    });
    function upd() {
      var n = Z.stops.filter(function (s) { return st[s.k]; }).length;
      count.textContent = '🔍 ' + n + ' of ' + Z.stops.length + ' zoom stops explored'; count.classList.toggle('ok', n === Z.stops.length);
      paintDial();
      if (n === Z.stops.length) askOnce(qh, Z.q, Z.opts, 'zoom-q', win, Z.win, Z.clue, 'zoom', miss);
    }
    at.parentNode.insertBefore(g, at.nextSibling);
    show(0, false); upd();
  }

  /* ---------- Lesson Part 3: "Pick the right tool" — lab requests (real photos); drag the tool that fits each question onto its request (18.01) ----------
     D.bench = {afterText, replace (selector removed), kicker, title, todo[], why, tools:[{k, icon, t, power}], jobs:[{id, img, alt, t, k, why, miss:{toolKey: text}}], q, opts, credit, win, clue} */
  function buildBench() {
    var B = D.bench; if (!B) return;
    var at = anchorP(B.afterText); if (!at) { FAILED.push('bench anchor text not found'); return; }
    if (B.replace) $$(B.replace).forEach(function (x) { x.classList.add('fs-replaced'); });
    var g = gameShell(B.kicker || 'Part 3 game', B.title, B.todo, B.why); g.dataset.mod = 'bench';
    var st = loadJ('bench', {});
    var tools = el('div', 'fs-tp-tools'), jobs = el('div', 'fs-tp-jobs'), miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    B.tools.forEach(function (t) { var k = el('div', 'fs-card fs-tp-tool', '<span class="fs-tp-ti">' + t.icon + '</span><b>' + esc(t.t) + '</b><small>' + esc(t.power) + '</small>'); k.dataset.k = t.k; tools.appendChild(k); });
    B.jobs.forEach(function (j, i) {
      var c = el('div', 'fs-tp-job', '<div class="fs-tp-ph"><img alt="' + esc(j.alt) + '" src="' + esc(j.img) + '"></div><div class="fs-tp-body"><div class="fs-tp-no">LAB REQUEST #' + (i + 1) + '</div><p>' + esc(j.t) + '</p><div class="fs-tp-drop">' + esc(B.dropHere || 'Drop a tool here') + '</div></div>');
      c.dataset.id = j.id; jobs.appendChild(c);
    });
    g.appendChild(el('div', 'fs-in-k', esc(B.toolsLabel || 'Sam’s tools'))); g.appendChild(tools); g.appendChild(jobs); g.appendChild(miss); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    if (B.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(B.credit)));
    var zones = $$('.fs-tp-job', jobs);
    function tool(k) { return B.tools.filter(function (t) { return t.k === k; })[0]; }
    function stamp(j, anim) {
      var c = zones.filter(function (z) { return z.dataset.id === j.id; })[0], t = tool(j.k);
      c.classList.add('done'); if (anim && !reduceMotion) c.classList.add('pop');
      $('.fs-tp-drop', c).outerHTML = '<div class="fs-tp-ok"><span class="fs-tp-stamp">' + t.icon + ' ' + esc(t.t) + '</span><small>' + esc(j.why) + '</small></div>';
    }
    function drop(k, z) {
      var j = B.jobs.filter(function (x) { return x.id === z.dataset.id; })[0]; if (!j || st[j.id]) return;
      if (k.dataset.k !== j.k) { bounce(k, miss, (j.miss && j.miss[k.dataset.k]) || 'Think about how small it is, and what the question asks you to do.'); z.classList.remove('shake'); void z.offsetWidth; z.classList.add('shake'); return; }
      miss.classList.remove('show'); st[j.id] = 1; saveJ('bench', st); SFX.chime(); stamp(j, true); upd();
    }
    $$('.fs-tp-tool', tools).forEach(function (k) { dragDrop(k, function () { return zones.filter(function (z) { return !z.classList.contains('done'); }); }, drop); });
    tapTargets(g, zones, drop);
    function upd() {
      var n = B.jobs.filter(function (j) { return st[j.id]; }).length;
      count.textContent = '🧪 ' + n + ' of ' + B.jobs.length + ' lab requests done'; count.classList.toggle('ok', n === B.jobs.length);
      if (n === B.jobs.length) askOnce(qh, B.q, B.opts, 'bench-q', win, B.win, B.clue, 'bench', miss);
    }
    B.jobs.forEach(function (j) { if (st[j.id]) stamp(j, false); });
    at.parentNode.insertBefore(g, at.nextSibling);
    upd();
  }

  /* ---------- Lesson Part 4: "Sam's microscope" — put the slide on, turn to 40x, focus, count the cells in the square; then fill in the lab report and match the real FWC level chart (18.01) ----------
     D.scope = {afterText, kicker, title, todo[], why, eyepiece, objectives:[{x, focus}], target (cells in the square), steps[], slideBtn, lines:{...},
                rule:{t}, report:{head, sub, rows:[{k, label, q, opts:[{t, ok, miss}]}], levelQ, levels:[{k, t, range, eff}], level, stamp, sign}, photo:{img, alt, cap}, credit, win, clue}
     The field of view is a MODEL drawn in SVG (cell shapes, not a photo); D.scope.photo is the real electron-microscope photo of one cell. */
  function buildScope() {
    var S = D.scope; if (!S) return;
    var at = anchorP(S.afterText); if (!at) { FAILED.push('scope anchor text not found'); return; }
    var g = gameShell(S.kicker || 'Part 4 game', S.title, S.todo, S.why); g.dataset.mod = 'scope';
    var st = loadJ('scope', { n: [] }); if (!st.n) st.n = [];
    var L = S.lines || {}, objs = S.objectives, ep = S.eyepiece || 10, N = S.target || 12;
    var obj = st.obj != null ? st.obj : 0, foc = 10;
    /* ---- the slide: seeded cells. 12 inside the square (±65), the rest around it; a pattern fills the far parts of the slide ---- */
    var seed = 18011; function rnd() { seed = (seed * 16807) % 2147483647; return (seed - 1) / 2147483646; }
    var cells = [], tries = 0;
    function free(x, y, d) { return cells.every(function (c) { return (c.x - x) * (c.x - x) + (c.y - y) * (c.y - y) > d * d; }); }
    while (cells.filter(function (c) { return c.inq; }).length < N && tries++ < 5000) { var x = -56 + rnd() * 112, y = -56 + rnd() * 112; if (free(x, y, 25)) cells.push({ x: x, y: y, a: rnd() * 180, inq: true }); }
    tries = 0;
    while (cells.length < N + 46 && tries++ < 8000) { var x2 = -150 + rnd() * 300, y2 = -150 + rnd() * 300; if (Math.abs(x2) < 76 && Math.abs(y2) < 76) continue; if (x2 * x2 + y2 * y2 > 158 * 158) continue; if (free(x2, y2, 25)) cells.push({ x: x2, y: y2, a: rnd() * 180 }); }
    cells.forEach(function (c, i) { c.id = i; });
    function cellSVG(c, cls) {
      return '<g class="' + (cls || 'fs-vm-cell') + '" data-id="' + c.id + '" transform="translate(' + c.x.toFixed(1) + ' ' + c.y.toFixed(1) + ') rotate(' + c.a.toFixed(0) + ')">' +
        (cls ? '' : '<circle r="13" fill="#000" fill-opacity="0"/>') + '<ellipse rx="10" ry="8.2" fill="#D9A441" fill-opacity=".82" stroke="#8C5A14" stroke-width="1.3"/>' +
        '<path d="M-9 1 Q0 -3 9 1" fill="none" stroke="#8C5A14" stroke-width="1.1"/><circle cx="-3" cy="2.5" r="2.4" fill="#A86E1E" opacity=".75"/></g>';
    }
    var pat = '';
    for (var pi = 0; pi < 14; pi++) { pat += cellSVG({ x: rnd() * 150, y: rnd() * 150, a: rnd() * 180, id: 'p' + pi }, 'fs-vm-pc'); }
    var diatoms = [{ x: 22, y: -30, a: 30 }, { x: -110, y: 70, a: -20 }, { x: 95, y: 105, a: 70 }];
    var field = '<svg class="fs-vm-svg" viewBox="-150 -150 300 300" role="img" aria-label="' + esc(L.fieldAlt || 'The view through the microscope: a circle of light with tiny golden cells.') + '">' +
      '<defs><clipPath id="fsVmClip"><circle r="148"/></clipPath><filter id="fsVmBlur" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="4"/></filter>' +
      '<pattern id="fsVmPat" width="150" height="150" patternUnits="userSpaceOnUse">' + pat + '</pattern>' +
      '<radialGradient id="fsVmLight"><stop offset="0" stop-color="#FFF8E6"/><stop offset=".8" stop-color="#F3E3BC"/><stop offset="1" stop-color="#C9B68C"/></radialGradient></defs>' +
      '<g clip-path="url(#fsVmClip)"><rect x="-150" y="-150" width="300" height="300" fill="url(#fsVmLight)"/>' +
      '<g class="fs-vm-slide" filter="url(#fsVmBlur)"><g class="fs-vm-zoom">' +
      '<rect x="-1500" y="-1500" width="3000" height="3000" fill="url(#fsVmPat)"/><rect x="-162" y="-162" width="324" height="324" fill="#F6EACB"/>' +
      diatoms.map(function (d, i) { return '<g class="fs-vm-dia" data-i="' + i + '" transform="translate(' + d.x + ' ' + d.y + ') rotate(' + d.a + ')"><rect x="-22" y="-4" width="44" height="8" rx="4" fill="#B9C98E" stroke="#6E7F45" stroke-width="1.2"/><path d="M-16 -4v8M-8 -4v8M0 -4v8M8 -4v8M16 -4v8" stroke="#6E7F45" stroke-width=".8"/></g>'; }).join('') +
      cells.map(function (c) { return cellSVG(c); }).join('') +
      '</g></g><g class="fs-vm-sq"><rect x="-65" y="-65" width="130" height="130" fill="none" stroke="#1F4F82" stroke-width="2" stroke-dasharray="6 4"/><rect x="-65" y="-80" width="78" height="13" rx="3" fill="#FFFFFF" fill-opacity=".85"/><text x="-61" y="-70" font-size="9.5" font-weight="900" fill="#1F4F82">COUNT SQUARE</text></g>' +
      '<g class="fs-vm-marks"></g></g><circle r="148" fill="none" stroke="#1B222C" stroke-width="5"/></svg>';
    var scopeArt = '<svg class="fs-vm-art" viewBox="0 0 160 230" role="img" aria-label="A light microscope: an eyepiece on top, a turret with three objective lenses, a stage that holds the slide, a focus knob and a light underneath.">' +
      '<rect x="20" y="206" width="120" height="16" rx="6" fill="#33475B"/><path d="M100 206 V96 Q100 70 78 62" stroke="#33475B" stroke-width="16" fill="none" stroke-linecap="round"/>' +
      '<rect x="56" y="14" width="22" height="34" rx="4" fill="#4A6178" transform="rotate(-18 67 31)"/><rect x="50" y="8" width="26" height="10" rx="3" fill="#2A3A4A" transform="rotate(-18 63 13)"/>' +
      '<rect x="52" y="50" width="34" height="26" rx="6" fill="#4A6178"/>' +
      '<g class="fs-vm-objs"><rect data-o="0" x="54" y="76" width="8" height="12" rx="2"/><rect data-o="1" x="65" y="76" width="8" height="18" rx="2"/><rect data-o="2" x="76" y="76" width="8" height="24" rx="2"/></g>' +
      '<rect x="34" y="128" width="78" height="9" rx="2" fill="#2A3A4A"/><rect class="fs-vm-slidepic" x="44" y="123" width="58" height="6" rx="1" fill="#E9F3F7" stroke="#8FA7B4"/><circle class="fs-vm-drop" cx="73" cy="126" r="5" fill="#C48A2C" opacity=".85"/>' +
      '<circle cx="70" cy="168" r="9" fill="#FFE9A6" stroke="#B88B2A" stroke-width="2"/><g class="fs-vm-knob"><circle cx="112" cy="150" r="14" fill="#5D7285" stroke="#2A3A4A" stroke-width="2"/><rect x="110.5" y="137" width="3" height="10" rx="1.5" fill="#FFD866"/></g></svg>';
    var row = el('div', 'fs-vm-row',
      '<div class="fs-vm-left">' + scopeArt + '<button type="button" class="fs-btn fs-vm-place">' + esc(S.slideBtn || '🧫 Put the slide on the stage') + '</button>' +
      '<div class="fs-in-k">' + esc(L.objLabel || 'Objective lens') + '</div><div class="fs-in-chips fs-vm-ob">' + objs.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + o.x + 'x</button>'; }).join('') + '</div>' +
      '<label class="fs-vm-fk"><span>' + esc(L.focusLabel || 'Focus knob') + '</span><input type="range" min="0" max="100" value="10" aria-label="' + esc(L.focusLabel || 'Focus knob') + '"></label></div>' +
      '<div class="fs-vm-right"><div class="fs-vm-eye">' + field + '<div class="fs-vm-empty">' + esc(L.empty || 'No slide yet') + '</div></div><div class="fs-vm-read"></div></div>');
    var steps = el('ol', 'fs-vm-steps', S.steps.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join(''));
    var msg = el('div', 'fs-hs-card fs-vm-msg'), miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), after = el('div', 'fs-vm-after'), win = el('div', 'fs-win');
    g.appendChild(steps); g.appendChild(row); g.appendChild(msg); g.appendChild(miss); g.appendChild(count); g.appendChild(after); g.appendChild(win);
    if (S.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo and data credits</summary>' + esc(S.credit)));
    var svg = $('.fs-vm-svg', row), zoom = $('.fs-vm-zoom', row), blur = $('feGaussianBlur', row), marks = $('.fs-vm-marks', row), sq = $('.fs-vm-sq', row), eye = $('.fs-vm-eye', row), read = $('.fs-vm-read', row), range = $('input', row), knob = $('.fs-vm-knob', row);
    function stage() { return !st.slide ? 0 : obj !== objs.length - 1 ? 1 : !focused() ? 2 : st.n.length < N ? 3 : 4; }
    function focused() { return Math.abs(foc - objs[obj].focus) <= 4; }
    function say(icon, b, t) { msg.innerHTML = '<span class="fs-hs-n">' + icon + '</span><div><b>' + esc(b) + '</b>' + esc(t || '') + '</div>'; }
    function paint() {
      var o = objs[obj], s = o.x / objs[objs.length - 1].x, d = Math.abs(foc - o.focus), sd = Math.min(7, d / 3.2);
      zoom.setAttribute('transform', 'scale(' + s + ')'); blur.setAttribute('stdDeviation', d <= 4 ? 0 : sd.toFixed(2));
      eye.classList.toggle('noslide', !st.slide); sq.style.display = (st.slide && obj === objs.length - 1) ? '' : 'none';
      knob.setAttribute('transform', 'rotate(' + (foc * 3.2).toFixed(0) + ' 112 150)');
      $$('.fs-vm-objs rect', row).forEach(function (r, i) { r.setAttribute('fill', i === obj ? '#E0A92E' : '#8FA2B4'); });
      $$('.fs-vm-ob .fs-in-chip', row).forEach(function (c, i) { c.classList.toggle('on', i === obj); });
      $('.fs-vm-slidepic', row).style.display = $('.fs-vm-drop', row).style.display = st.slide ? '' : 'none';
      read.innerHTML = st.slide ? '<b>' + ep + 'x</b> eyepiece × <b>' + o.x + 'x</b> lens = <b>' + (ep * o.x) + 'x</b>' + (focused() ? ' <span class="fs-vm-sharp">✓ in focus</span>' : ' <span class="fs-vm-fuzzy">blurry</span>') : '';
      $$('li', steps).forEach(function (li, i) { li.classList.toggle('done', i < stage()); li.classList.toggle('now', i === stage()); });
      var n = st.n.length; count.textContent = '🔢 ' + n + ' of ' + N + ' cells counted in the square'; count.classList.toggle('ok', n === N);
    }
    function guide() {
      var s = stage();
      if (s === 0) say('🧫', L.s0 || 'Step 1', L.s0t || 'Put Sam’s slide on the stage.');
      else if (s === 1) say('🔭', L.s1 || 'Step 2', L.s1t || 'Turn to the strongest objective lens.');
      else if (s === 2) say('🌀', L.s2 || 'Step 3', L.s2t || 'Turn the focus knob slowly until the cells look sharp.');
      else if (s === 3) say('👆', L.s3 || 'Step 4', L.s3t || 'Tap each red tide cell inside the square. Cells touching the line count only if most of the cell is inside.');
    }
    $('.fs-vm-place', row).addEventListener('click', function (e) { if (st.slide) return; st.slide = 1; saveJ('scope', st); SFX.pop(); placed(); paint(); guide(); });
    function placed() { var b = $('.fs-vm-place', row); b.disabled = true; b.textContent = L.placed || '✓ The slide is on the stage'; }
    if (st.slide) placed();
    $$('.fs-vm-ob .fs-in-chip', row).forEach(function (c, i) { c.addEventListener('click', function () {
      if (!st.slide) { bounce(c, miss, L.noSlide || 'Put the slide on the stage first.'); return; }
      obj = i; st.obj = i; saveJ('scope', st); SFX.blip(); paint(); miss.classList.remove('show');
      if (i < objs.length - 1) say('🔭', objs[i].x + 'x lens: ' + (ep * objs[i].x) + 'x in all', (i === 0 ? L.low : L.mid) || 'The cells look like tiny specks. Too small to count. Try a stronger lens.'); else guide();
    }); });
    range.addEventListener('input', function () { foc = +range.value; paint(); if (stage() >= 3 && !st.focusSaid) { st.focusSaid = 1; SFX.chime(); guide(); } });
    range.addEventListener('change', function () { if (st.slide && obj === objs.length - 1 && !focused()) say('🌀', L.blurTitle || 'Still blurry', L.blurT || 'Keep turning the knob, slowly. Watch the edges of the cells get sharp.'); });
    function mark(c, anim) { var m = document.createElementNS('http://www.w3.org/2000/svg', 'g'); m.setAttribute('class', 'fs-vm-mk' + (anim && !reduceMotion ? ' pop' : '')); m.setAttribute('transform', 'translate(' + c.x.toFixed(1) + ' ' + c.y.toFixed(1) + ')'); m.innerHTML = '<circle r="12" fill="none" stroke="#1F7A3A" stroke-width="2.4"/><text y="-14" text-anchor="middle" font-size="11" font-weight="900" fill="#1F7A3A">' + (st.n.indexOf(c.id) + 1) + '</text>'; marks.appendChild(m); }
    svg.addEventListener('click', function (e) {
      var t = e.target.closest ? e.target.closest('.fs-vm-cell, .fs-vm-dia') : null;
      if (stage() < 3) { if (st.slide) bounce(eye, miss, stage() === 1 ? (L.needLens || 'These cells are too small to count at this power. Turn to the 40x lens.') : (L.needFocus || 'It’s too blurry to count. Turn the focus knob first.')); return; }
      if (!t) return;
      if (t.classList.contains('fs-vm-dia')) { bounce(eye, miss, L.diatom || 'That long, striped shape is a diatom, a different tiny living thing. Count only the round golden red tide cells.'); return; }
      var c = cells[+t.dataset.id]; if (!c) return;
      if (!c.inq) { bounce(eye, miss, L.outside || 'That cell is outside the square. Count only the cells inside the dashed square.'); return; }
      if (st.n.indexOf(c.id) > -1) { bounce(eye, miss, L.twice || 'You already counted that one. Look for a cell without a green circle.'); return; }
      miss.classList.remove('show'); st.n.push(c.id); saveJ('scope', st); SFX.blip(); mark(c, true); paint();
      if (st.n.length === N) { SFX.chime(); say('✅', L.doneTitle || 'All counted!', L.doneT || ''); report(); }
    });
    /* ---- the lab report ---- */
    function report() {
      if (after.dataset.on) return; after.dataset.on = '1'; var R = S.report;
      if (!st.r) st.r = {};
      after.innerHTML = (S.rule ? '<div class="fs-hs-card fs-vm-rule"><span class="fs-hs-n">🧮</span><div><b>' + esc(S.rule.head || 'Sam’s rule') + '</b>' + esc(S.rule.t) + '</div></div>' : '') +
        '<div class="fs-lr"><div class="fs-lr-head"><b>' + esc(R.head) + '</b><small>' + esc(R.sub || '') + '</small></div><dl class="fs-lr-form">' +
        R.rows.map(function (r) { return '<dt>' + esc(r.label) + '</dt><dd data-k="' + r.k + '">' + (r.fixed ? '<span class="fs-lr-val">' + esc(r.fixed) + '</span>' : '<span class="fs-lr-blank">________</span>') + '</dd>'; }).join('') +
        '<dt>' + esc(R.levelLabel || 'Red tide level') + '</dt><dd data-k="level"><span class="fs-lr-blank">________</span></dd></dl><div class="fs-lr-ask"></div><div class="fs-lr-stamp" aria-hidden="true"></div>' +
        (R.sign ? '<div class="fs-lr-sign">' + esc(R.sign) + '</div>' : '') + '</div>' +
        (S.photo ? '<figure class="fs-vm-photo"><img alt="' + esc(S.photo.alt) + '" src="' + esc(S.photo.img) + '"><figcaption>' + esc(S.photo.cap) + '</figcaption></figure>' : '');
      var ask = $('.fs-lr-ask', after);
      function fill(k, v, anim) { var dd = $('dd[data-k="' + k + '"]', after); dd.innerHTML = '<span class="fs-lr-val' + (anim && !reduceMotion ? ' pop' : '') + '">' + esc(v) + '</span>'; }
      function next() {
        var r = R.rows.filter(function (x) { return !x.fixed && !st.r[x.k]; })[0];
        if (r) {
          ask.innerHTML = '';
          chipsQ(ask, r.q, r.opts, function (o) { st.r[r.k] = 1; saveJ('scope', st); fill(r.k, o.fill || o.t, true); setTimeout(next, reduceMotion ? 0 : 500); }, miss);
          return;
        }
        if (!st.r.level) { levels(); return; }
        done(false);
      }
      function levels() {
        ask.innerHTML = '<div class="fs-in-k">' + esc(R.levelQ) + '</div><table class="fs-lr-chart"><thead><tr><th>' + esc(R.colLevel || 'Level') + '</th><th>' + esc(R.colRange || 'Cells in 1 liter') + '</th><th>' + esc(R.colEff || 'What can happen') + '</th></tr></thead><tbody>' +
          R.levels.map(function (lv) { return '<tr tabindex="0" data-k="' + lv.k + '"><td><b>' + esc(lv.t) + '</b></td><td>' + esc(lv.range) + '</td><td>' + esc(lv.eff) + '</td></tr>'; }).join('') + '</tbody></table>' + (R.chartSrc ? '<div class="fs-lr-src">' + esc(R.chartSrc) + '</div>' : '');
        $$('tbody tr', ask).forEach(function (tr) {
          function pick() {
            if (st.r.level) return; var lv = R.levels.filter(function (x) { return x.k === tr.dataset.k; })[0];
            if (lv.k !== R.level) { bounce(tr, miss, lv.miss || 'Find your number in the middle column. Is it bigger or smaller than this row?'); return; }
            miss.classList.remove('show'); st.r.level = 1; saveJ('scope', st); tr.classList.add('ok'); SFX.chime(); done(true);
          }
          tr.addEventListener('click', pick); tr.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); pick(); } });
        });
      }
      function done(anim) {
        var lv = R.levels.filter(function (x) { return x.k === R.level; })[0]; fill('level', lv.t, anim);
        var stp = $('.fs-lr-stamp', after); stp.textContent = R.stamp || lv.t; stp.classList.add('on'); if (anim && !reduceMotion) stp.classList.add('thunk');
        if (anim && $$('tbody tr', ask).length) { $$('tbody tr', ask).forEach(function (tr) { tr.classList.toggle('ok', tr.dataset.k === R.level); }); }
        else ask.innerHTML = '';
        winOnce(win, S.win, S.clue, 'scope');
      }
      R.rows.forEach(function (r) { if (st.r[r.k]) { var o = r.opts.filter(function (x) { return x.ok; })[0]; fill(r.k, o.fill || o.t, false); } });
      next();
    }
    at.parentNode.insertBefore(g, at.nextSibling);
    st.n.forEach(function (id) { if (cells[id]) mark(cells[id], false); });
    if (st.n.length === N) { foc = objs[objs.length - 1].focus; range.value = foc; obj = objs.length - 1; }
    paint(); guide();
    if (st.n.length === N) { say('✅', L.doneTitle || 'All counted!', L.doneT || ''); report(); }
  }

  /* ---------- Tool of the Week: a hand lens — drag the lens over a real photo, pick 2x / 5x / 10x, move it closer or farther until it's sharp, log the details you find (18.01) ----------
     T.handlens = {title, todo[], objects:[{k, t, img, alt, w (% of the table), details:[{x, y (0-1), t, power}]}], powers:[{x, f (cm)}], logBtn, q:{q, opts}} */
  SIMS.handlens = function (host, T) {
    var H = T.handlens, st = loadJ('handlens', { f: {}, d: {} }), ob = H.objects[0], pw = H.powers[0], dist = 15;
    if (!st.f) st.f = {}; if (!st.d) st.d = {};
    host.innerHTML = '<div class="fs-game-k">Try it: a hand lens</div><div class="fs-game-t">' + esc(H.title) + '</div>' +
      '<ul class="fs-todo">' + H.todo.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>' +
      '<div class="fs-in-chips fs-lz-objs">' + H.objects.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(o.t) + '</button>'; }).join('') + '</div>' +
      '<div class="fs-lz-table"><img class="fs-lz-obj" alt=""><div class="fs-lz-lens" aria-hidden="true"><div class="fs-lz-glass"></div></div><div class="fs-lz-tip">' + esc(H.dragTip || 'Drag the lens (or tap where you want it).') + '</div></div>' +
      '<div class="fs-lz-ctl"><div><div class="fs-in-k">Lens power</div><div class="fs-in-chips fs-lz-pw">' + H.powers.map(function (p, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + p.x + 'x</button>'; }).join('') + '</div></div>' +
      '<label class="fs-lz-d"><span>' + esc(H.distLabel || 'How far the lens is from the object') + ': <b></b></span><input type="range" min="1" max="15" step="0.5" value="15"></label></div>' +
      '<div class="fs-lz-read"></div><button type="button" class="fs-btn fs-lz-log">' + esc(H.logBtn || '📝 Log what I see') + '</button>' +
      '<div class="fs-lz-logs"></div><div class="fs-sv-q fs-lz-q"></div><div class="fs-miss fs-lz-miss"></div><div class="fs-win fs-lz-win"></div>' +
      (H.credit ? '<details class="fs-credit fs-credit-fold"><summary>📷 Photo credits</summary>' + esc(H.credit) + '</details>' : '');
    var table = $('.fs-lz-table', host), oimg = $('.fs-lz-obj', host), lens = $('.fs-lz-lens', host), glass = $('.fs-lz-glass', host), range = $('.fs-lz-d input', host), read = $('.fs-lz-read', host), miss = $('.fs-lz-miss', host);
    var cx = null, cy = null;
    function R() { return lens.offsetWidth / 2 || 70; }
    function focused() { return Math.abs(dist - pw.f) <= 0.5; }
    function paint() {
      var tr = table.getBoundingClientRect(), or = oimg.getBoundingClientRect(), r = R();
      if (cx == null) { cx = or.left - tr.left + or.width * 0.5; cy = or.top - tr.top + or.height * 0.45; }
      cx = Math.max(r * 0.4, Math.min(tr.width - r * 0.4, cx)); cy = Math.max(r * 0.4, Math.min(tr.height - r * 0.4, cy));
      lens.style.left = (cx - r) + 'px'; lens.style.top = (cy - r) + 'px';
      var u = (cx - (or.left - tr.left)) / or.width, v = (cy - (or.top - tr.top)) / or.height, bw = or.width * pw.x, bh = or.height * pw.x;
      glass.style.backgroundImage = 'url("' + ob.img + '")'; glass.style.backgroundSize = bw + 'px ' + bh + 'px';
      glass.style.backgroundPosition = (r - u * bw) + 'px ' + (r - v * bh) + 'px';
      var d = Math.abs(dist - pw.f); glass.style.filter = d <= 0.5 ? 'none' : 'blur(' + Math.min(9, d * 1.6).toFixed(1) + 'px)';
      $('.fs-lz-d b', host).textContent = dist + ' cm';
      $$('.fs-lz-pw .fs-in-chip', host).forEach(function (c, i) { c.classList.toggle('on', H.powers[i] === pw); c.classList.toggle('done', !!st.f[H.powers[i].x]); });
      $$('.fs-lz-objs .fs-in-chip', host).forEach(function (c, i) { c.classList.toggle('on', H.objects[i] === ob); });
      read.innerHTML = focused() ? '<span class="fs-vm-sharp">✓ Sharp at ' + pw.x + 'x</span>' : '<span class="fs-vm-fuzzy">Blurry. Move the lens ' + (dist > pw.f ? 'closer' : 'farther') + '.</span>';
      return { u: u, v: v };
    }
    function logs() {
      var fp = H.powers.map(function (p) { return '<li class="' + (st.f[p.x] ? 'ok' : '') + '">' + p.x + 'x: ' + (st.f[p.x] ? 'sharp at ' + p.f + ' cm ✓' : '—') + '</li>'; }).join('');
      var dp = H.objects.map(function (o) { return o.details.map(function (d, i) { var k = o.k + i; return '<li class="' + (st.d[k] ? 'ok' : '') + '">' + (st.d[k] ? '✓ ' + esc(d.t) : '❓ ' + esc(o.t) + ': a detail to find') + '</li>'; }).join(''); }).join('');
      $('.fs-lz-logs', host).innerHTML = '<div><div class="fs-in-k">Where each lens gets sharp</div><ul>' + fp + '</ul></div><div><div class="fs-in-k">Details logged</div><ul>' + dp + '</ul></div>';
    }
    function all() { return H.powers.every(function (p) { return st.f[p.x]; }) && H.objects.every(function (o) { return o.details.every(function (d, i) { return st.d[o.k + i]; }); }); }
    function check() {
      if (!all()) return; var q = $('.fs-lz-q', host); if (q.dataset.on) return; q.dataset.on = '1';
      q.innerHTML = '<div class="fs-in-k">' + esc(H.q.q) + '</div><div class="fs-in-chips">' + H.q.opts.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(o.t) + '</button>'; }).join('') + '</div>';
      function ok(i) { $$('.fs-in-chip', q)[i].classList.add('on', 'ok'); var w = $('.fs-lz-win', host); w.innerHTML = esc(H.q.opts[i].why); w.classList.add('show'); }
      $$('.fs-in-chip', q).forEach(function (c) { c.addEventListener('click', function () { var o = H.q.opts[+c.dataset.i]; if (!o.ok) { bounce(c, miss, o.why); return; } miss.classList.remove('show'); ok(+c.dataset.i); SFX.win(); store('handlens-q', '1'); toolDone(); }); });
      if (store('handlens-q')) ok(H.q.opts.map(function (o, j) { return o.ok ? j : -1; }).filter(function (j) { return j > -1; })[0]);
    }
    function setObj(i) { ob = H.objects[i]; oimg.src = ob.img; oimg.alt = ob.alt; oimg.style.width = (ob.w || 36) + '%'; cx = null; }
    oimg.addEventListener('load', function () { paint(); });
    var drag = false;
    function at(e) { var tr = table.getBoundingClientRect(); cx = e.clientX - tr.left; cy = e.clientY - tr.top; paint(); }
    table.addEventListener('pointerdown', function (e) { drag = true; table.setPointerCapture && table.setPointerCapture(e.pointerId); at(e); e.preventDefault(); });
    table.addEventListener('pointermove', function (e) { if (drag) at(e); });
    table.addEventListener('pointerup', function () { drag = false; });
    table.addEventListener('pointercancel', function () { drag = false; });
    $$('.fs-lz-objs .fs-in-chip', host).forEach(function (c, i) { c.addEventListener('click', function () { setObj(i); SFX.blip(); }); });
    $$('.fs-lz-pw .fs-in-chip', host).forEach(function (c, i) { c.addEventListener('click', function () { pw = H.powers[i]; SFX.blip(); paint(); }); });
    range.addEventListener('input', function () {
      dist = +range.value; paint();
      if (focused() && !st.f[pw.x]) { st.f[pw.x] = 1; saveJ('handlens', st); SFX.chime(); logs(); check(); }
    });
    $('.fs-lz-log', host).addEventListener('click', function (e) {
      var p = paint(), b = e.currentTarget;
      if (!focused()) { bounce(b, miss, 'It’s too blurry to see details. Move the lens closer or farther first.'); return; }
      var near = null;
      ob.details.forEach(function (d, i) { var du = (d.x - p.u), dv = (d.y - p.v), reach = 0.55 / pw.x + 0.03; if (du * du + dv * dv < reach * reach && !near) near = { d: d, k: ob.k + i }; });
      if (!near) { bounce(b, miss, H.nothing || 'Nothing new right under the lens. Slide it around the object, slowly.'); return; }
      if (st.d[near.k]) { bounce(b, miss, 'You already logged that one. Look somewhere else on the object.'); return; }
      if (pw.x < near.d.power) { bounce(b, miss, 'Something is there, but it’s too small to make out. Try a stronger lens.'); return; }
      miss.classList.remove('show'); st.d[near.k] = 1; saveJ('handlens', st); SFX.chime(); logs(); check();
    });
    window.addEventListener('resize', function () { if (host.offsetParent) paint(); });
    setObj(0); logs(); check();
  };

  /* =================== 20.01: 9:41 PM (feel it + rate it, block the path, which way does heat go, storm watch, circuit tester) =================== */

  /* ---------- Warm-Up: "Feel it, rate it" — the student really does each move (rub hands, hum, look at a light); a slider rates how much the
     receiver changed, then a chip question names where the energy ended up; a tally builds source → receiver rows (20.01) ----------
     D.rateit = {afterText, kicker, title, todo[], why, scale:[4 labels], zeroLine, doneBtn, tallyLabel, moves:[{id, icon, t, do, rate, recQ, recs:[{t, ok, miss}], form, formIcon, path, why}], q, opts, win, clue} */
  function buildRateit() {
    var R = D.rateit; if (!R) return;
    var at = anchorP(R.afterText); if (!at) { FAILED.push('rateit anchor text not found'); return; }
    var g = gameShell(R.kicker || 'Warm-Up game', R.title, R.todo, R.why); g.dataset.mod = 'rateit';
    var st = loadJ('rateit', { r: {}, ok: {} }), cur = 0;
    var tabs = el('div', 'fs-in-chips fs-rt-tabs'), card = el('div', 'fs-rt-card'), tally = el('div', 'fs-rt-tally'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    R.moves.forEach(function (m, i) { var b = el('button', 'fs-in-chip fs-rt-tab', '<span>' + m.icon + '</span> ' + esc(m.t)); b.type = 'button'; b.dataset.i = i; tabs.appendChild(b); });
    g.appendChild(tabs); g.appendChild(card); g.appendChild(miss); g.appendChild(tally); g.appendChild(qh); g.appendChild(win);
    var scale = R.scale || ['😐 Nothing', '🙂 A little', '😮 Some', '🤩 A lot'];
    function paintTabs() { $$('.fs-rt-tab', tabs).forEach(function (b, i) { b.classList.toggle('on', i === cur); b.classList.toggle('ok', !!st.ok[R.moves[i].id]); }); }
    function paintTally() {
      var done = R.moves.filter(function (m) { return st.ok[m.id]; });
      tally.innerHTML = '<div class="fs-in-k">' + esc(R.tallyLabel || 'Energy you sent') + '</div>' + R.moves.map(function (m) {
        var ok = st.ok[m.id];
        return '<div class="fs-rt-row' + (ok ? ' ok' : '') + '"><span class="fs-rt-ic">' + (ok ? m.formIcon : '❔') + '</span><b>' + (ok ? esc(m.form) : '…') + '</b><span>' + (ok ? esc(m.path) : esc(m.t)) + '</span><span class="fs-rt-meter">' + (ok ? scale[st.r[m.id] || 0].split(' ')[0] : '') + '</span></div>';
      }).join('');
      if (done.length === R.moves.length) askOnce(qh, R.q, R.opts, 'rateit-q', win, R.win, R.clue, 'rateit', miss);
    }
    function paint() {
      var m = R.moves[cur], r = st.r[m.id], ok = st.ok[m.id];
      card.innerHTML = '<div class="fs-rt-do"><span class="fs-rt-big">' + m.icon + '</span><div><b>' + esc(m.t) + '</b><p>' + esc(m.do) + '</p></div></div>' +
        '<button type="button" class="fs-btn fs-rt-did"' + (r != null ? ' hidden' : '') + '>✋ ' + esc(R.doneBtn || 'I did it!') + '</button>' +
        '<div class="fs-rt-rate"' + (r == null ? ' hidden' : '') + '><div class="fs-in-k">' + esc(m.rate) + '</div><input type="range" class="fs-rt-range" min="0" max="3" step="1" value="' + (r || 0) + '" aria-label="' + esc(m.rate) + '"><div class="fs-rt-scale">' + scale.map(function (s, i) { return '<span data-i="' + i + '" class="' + (r === i ? 'on' : '') + '">' + esc(s) + '</span>'; }).join('') + '</div></div>' +
        '<div class="fs-rt-rec"></div>' + (ok ? '<div class="fs-hs-card fs-rt-why"><span class="fs-hs-n">' + m.formIcon + '</span><div><b>' + esc(m.form + ': ' + m.path) + '</b>' + esc(m.why) + '</div></div>' : '');
      var did = $('.fs-rt-did', card), rate = $('.fs-rt-rate', card), range = $('.fs-rt-range', card);
      did.addEventListener('click', function () { st.r[m.id] = st.r[m.id] || 0; saveJ('rateit', st); SFX.blip(); paint(); });
      function setR(v) {
        st.r[m.id] = v; saveJ('rateit', st); range.value = v;
        $$('.fs-rt-scale span', card).forEach(function (s, i) { s.classList.toggle('on', i === v); });
        if (v === 0) { showMiss(miss, R.zeroLine || 'Nothing yet? Try it again a little longer, then rate it.'); return; }
        miss.classList.remove('show'); tone(400 + v * 160, 0, 0.12, 'triangle', 0.04); askRec();
      }
      range.addEventListener('change', function () { setR(+range.value); });
      range.addEventListener('input', function () { $$('.fs-rt-scale span', card).forEach(function (s, i) { s.classList.toggle('on', i === +range.value); }); });
      $$('.fs-rt-scale span', card).forEach(function (s) { s.addEventListener('click', function () { setR(+s.dataset.i); }); });
      function askRec() {
        var host = $('.fs-rt-rec', card); if (host.dataset.on) return; host.dataset.on = '1';
        var w = chipsQ(host, m.recQ, m.recs, function () { st.ok[m.id] = 1; saveJ('rateit', st); paintTabs(); paintTally(); paint();
          var nx = -1; R.moves.some(function (mm, j) { if (!st.ok[mm.id]) { nx = j; return true; } }); if (nx > -1) setTimeout(function () { cur = nx; paintTabs(); paint(); }, reduceMotion ? 0 : 1400); }, miss);
        if (ok) { var oi = m.recs.map(function (o, j) { return o.ok ? j : -1; }).filter(function (j) { return j > -1; })[0]; $$('.fs-in-chip', w)[oi].classList.add('on', 'ok'); w.dataset.done = '1'; }
      }
      if (r != null && r > 0) askRec();
    }
    $$('.fs-rt-tab', tabs).forEach(function (b) { b.addEventListener('click', function () { cur = +b.dataset.i; miss.classList.remove('show'); SFX.blip(); paintTabs(); paint(); }); });
    at.parentNode.insertBefore(g, at.nextSibling);
    R.moves.some(function (m, j) { if (!st.ok[m.id]) { cur = j; return true; } });
    paintTabs(); paint(); paintTally();
  }

  /* ---------- Lesson Part 1: "Block the path" — four source → receiver scenes with a moving energy path; tap the gap to see what is in it
     (only air, or a wire), then drag (or tap) a blocker into the gap: the path stops and the receiver stops changing (20.01) ----------
     D.blockpath = {afterText, kicker, title, todo[], why, gapBtn, tapFirst, trayLabel, blockers:[{k, icon, t}], scenes:[{id, form, formIcon, c, src:{icon,t}, rec:{icon,t}, fx ('warm'|'glow'|'buzz'|'lit'), gap, on, off, ok:[k], miss:{k:t}, missAny}], q, opts, win, clue} */
  function buildBlockpath() {
    var B = D.blockpath; if (!B) return;
    var at = anchorP(B.afterText); if (!at) { FAILED.push('blockpath anchor text not found'); return; }
    var g = gameShell(B.kicker || 'Part 1 game', B.title, B.todo, B.why); g.dataset.mod = 'blockpath';
    var st = loadJ('blockpath', { gap: {}, blk: {} });
    var grid = el('div', 'fs-blk-grid'), tray = el('div', 'fs-blk-tray'), miss = el('div', 'fs-miss'), count = el('div', 'fs-count'), qh = el('div'), win = el('div', 'fs-win');
    B.scenes.forEach(function (s) {
      var c = el('div', 'fs-blk-scene fx-' + (s.fx || 'glow'), '<div class="fs-blk-form" style="--c:' + s.c + '">' + s.formIcon + ' ' + esc(s.form) + '</div>' +
        '<div class="fs-blk-row"><div class="fs-blk-end"><span class="fs-blk-big">' + s.src.icon + '</span><small>' + esc(s.src.t) + '</small><em>source</em></div>' +
        '<button type="button" class="fs-blk-gap" style="--c:' + s.c + '" aria-label="' + esc((B.gapBtn || 'Tap the gap') + ': ' + s.form) + '"><span class="fs-blk-flow"><i></i><i></i><i></i><i></i></span><span class="fs-blk-q">' + esc(B.gapBtn || 'Tap the gap') + '</span><span class="fs-blk-wall"></span></button>' +
        '<div class="fs-blk-end fs-blk-rec"><span class="fs-blk-big">' + s.rec.icon + '</span><small>' + esc(s.rec.t) + '</small><em>receiver</em></div></div><div class="fs-blk-note"></div>');
      c.dataset.id = s.id; grid.appendChild(c);
    });
    tray.innerHTML = '<div class="fs-in-k">' + esc(B.trayLabel || 'Blockers (drag one into a gap, or tap it and then a gap)') + '</div><div class="fs-blk-items">' + B.blockers.map(function (b) { return '<button type="button" class="fs-blk-item" data-k="' + b.k + '"><span>' + b.icon + '</span>' + esc(b.t) + '</button>'; }).join('') + '</div>';
    g.appendChild(grid); g.appendChild(tray); g.appendChild(miss); g.appendChild(count); g.appendChild(qh); g.appendChild(win);
    function sc(id) { return B.scenes.filter(function (s) { return s.id === id; })[0]; }
    function blkOf(k) { return B.blockers.filter(function (b) { return b.k === k; })[0]; }
    function paint(id, anim) {
      var s = sc(id), c = $('.fs-blk-scene[data-id="' + id + '"]', grid), bk = st.blk[id];
      c.classList.toggle('blocked', !!bk); c.classList.toggle('seen', !!st.gap[id]);
      $('.fs-blk-wall', c).innerHTML = bk ? blkOf(bk).icon : '';
      $('.fs-blk-q', c).textContent = st.gap[id] ? '' : (B.gapBtn || 'Tap the gap');
      $('.fs-blk-note', c).innerHTML = bk ? '<b>' + esc(blkOf(bk).t) + ':</b> ' + esc(s.off) : (st.gap[id] ? esc(s.gap) : esc(s.on));
      if (anim && !reduceMotion) { c.classList.remove('pop'); void c.offsetWidth; c.classList.add('pop'); }
    }
    function upd() {
      var n = B.scenes.filter(function (s) { return st.blk[s.id]; }).length;
      count.textContent = '🚧 ' + n + ' of ' + B.scenes.length + ' paths blocked'; count.classList.toggle('ok', n === B.scenes.length);
      if (n === B.scenes.length) askOnce(qh, B.q, B.opts, 'blockpath-q', win, B.win, B.clue, 'blockpath', miss);
    }
    function drop(item, gap) {
      var c = gap.closest('.fs-blk-scene'), id = c.dataset.id, s = sc(id), k = item.dataset.k;
      item.classList.remove('sel');
      if (st.blk[id]) return;
      if (!st.gap[id]) { bounce(gap, miss, B.tapFirst || 'First tap the gap. What is in there between the source and the receiver?'); return; }
      if (s.ok.indexOf(k) < 0) { bounce(item, miss, (s.miss && s.miss[k]) || s.missAny || 'That won’t stop this kind of energy. Try another blocker.'); return; }
      st.blk[id] = k; saveJ('blockpath', st); miss.classList.remove('show'); SFX.thud(); setTimeout(SFX.chime, 180); paint(id, true); upd();
    }
    $$('.fs-blk-gap', grid).forEach(function (gap) {
      gap.addEventListener('click', function () {
        var s = $('.fs-blk-item.sel', tray); if (s) { drop(s, gap); return; }
        var id = gap.closest('.fs-blk-scene').dataset.id; if (st.gap[id]) return;
        st.gap[id] = 1; saveJ('blockpath', st); SFX.blip(); paint(id, true);
      });
    });
    $$('.fs-blk-item', tray).forEach(function (it) { dragDrop(it, function () { return $$('.fs-blk-gap', grid); }, drop); });
    at.parentNode.insertBefore(g, at.nextSibling);
    B.scenes.forEach(function (s) { paint(s.id); }); upd();
  }

  /* ---------- Lesson Part 2: "Which way does heat go?" — iced lemonade on a hot porch (a model): pick the arrow (heat IN or cold OUT), wait an hour,
     the drink's thermometer climbs and the ice melts while the porch air stays put; a wrong arrow is shown failing. Then name the form for 4 Florida
     scenes by dragging a form tile into each path (20.01) ----------
     D.heatflow = {afterText, replace[], kicker, title, todo[], why, alt, model, airT, drinkT, endT, airLabel, drinkLabel, arrowQ, arrows:[{k, t, ok}], runBtn, timeLabel,
                   wrongAfter, rightAfter, cardsHead, forms:[{k, icon, t, c}], cards:[{id, src:{icon,t}, rec:{icon,t}, form, why, miss:{k:t}}], q, opts, win, clue} */
  function buildHeatflow() {
    var H = D.heatflow; if (!H) return;
    var at = anchorP(H.afterText); if (!at) { FAILED.push('heatflow anchor text not found'); return; }
    (H.replace || []).forEach(function (s) { $$(s).forEach(function (n) { n.classList.add('fs-replaced'); }); });
    var g = gameShell(H.kicker || 'Part 2 game', H.title, H.todo, H.why); g.dataset.mod = 'heatflow';
    var st = loadJ('heatflow', { arrow: null, ran: 0, ok: 0, f: {} }), A = H.airT || 90, T0 = H.drinkT || 38, T1 = H.endT || 80;
    function therm(x, label, id) {
      return '<g class="fs-hf-th" transform="translate(' + x + ' 30)"><rect x="-9" y="0" width="18" height="120" rx="9" fill="#fff" stroke="#8A9AA8" stroke-width="2"/><circle cx="0" cy="132" r="15" fill="#E8636B" stroke="#8A9AA8" stroke-width="2"/>' +
        '<rect class="fs-hf-mer" id="' + id + '" x="-4" width="8" rx="4" fill="#E8636B"/>' + [40, 60, 80, 100].map(function (t) { var y = 120 - (t - 30) * 1.4; return '<line x1="9" x2="15" y1="' + y + '" y2="' + y + '" stroke="#8A9AA8"/><text x="18" y="' + (y + 4) + '" class="fs-hf-tick">' + t + '°</text>'; }).join('') +
        '<text x="0" y="168" text-anchor="middle" class="fs-hf-lab">' + esc(label) + '</text><text x="0" y="-8" text-anchor="middle" class="fs-hf-read"></text></g>';
    }
    var stage = el('div', 'fs-hf-stage', '<svg viewBox="0 0 640 230" class="fs-hf-svg" role="img" aria-label="' + esc(H.alt || 'A model: a glass of iced lemonade on a sunny porch with two thermometers') + '">' +
      '<rect width="640" height="230" fill="#FFF3D6"/><circle cx="590" cy="38" r="26" fill="#FFC93C"/><g stroke="#FFC93C" stroke-width="4" stroke-linecap="round">' + [0, 45, 90, 135, 180, 225, 270, 315].map(function (a) { var r = a * Math.PI / 180; return '<line x1="' + (590 + Math.cos(r) * 34) + '" y1="' + (38 + Math.sin(r) * 34) + '" x2="' + (590 + Math.cos(r) * 44) + '" y2="' + (38 + Math.sin(r) * 44) + '"/>'; }).join('') + '</g>' +
      '<rect y="186" width="640" height="44" fill="#C9965C"/>' + [0, 1, 2, 3, 4, 5, 6, 7].map(function (i) { return '<line x1="' + (i * 80) + '" y1="186" x2="' + (i * 80) + '" y2="230" stroke="#A97A44" stroke-width="2"/>'; }).join('') +
      '<g transform="translate(300 70)"><path d="M0 0 L80 0 L72 116 L8 116 Z" fill="rgba(255,255,255,.55)" stroke="#9FB7C8" stroke-width="3"/><path class="fs-hf-lem" d="M4 30 L76 30 L72 116 L8 116 Z" fill="#FFE680"/>' +
      '<g class="fs-hf-ice"><rect x="14" y="36" width="22" height="22" rx="4" fill="#E8F7FF" stroke="#A8D8F0"/><rect x="42" y="44" width="22" height="22" rx="4" fill="#E8F7FF" stroke="#A8D8F0"/><rect x="26" y="66" width="22" height="22" rx="4" fill="#E8F7FF" stroke="#A8D8F0"/></g>' +
      '<g class="fs-hf-drops" fill="#9FD3F0"><circle cx="84" cy="50" r="3"/><circle cx="-3" cy="70" r="3"/><circle cx="82" cy="92" r="2.5"/></g></g>' +
      '<g class="fs-hf-arrow" transform="translate(300 128)"></g>' + therm(110, H.airLabel || 'Porch air', 'fsHfA') + therm(500, H.drinkLabel || 'Lemonade', 'fsHfD') +
      '<text x="12" y="222" class="fs-hf-model">' + esc(H.model || 'a model') + '</text><text x="320" y="24" text-anchor="middle" class="fs-hf-clock"></text></svg>');
    var ask = el('div', 'fs-hf-ask', '<div class="fs-in-k">' + esc(H.arrowQ) + '</div><div class="fs-in-chips">' + H.arrows.map(function (a, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(a.t) + '</button>'; }).join('') + '</div>');
    var run = el('button', 'fs-btn fs-hf-run', '▶ ' + esc(H.runBtn || 'Wait one hour')); run.type = 'button';
    var info = el('div', 'fs-hs-card fs-hf-info'), cards = el('div', 'fs-hf-cards'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(stage); g.appendChild(ask); g.appendChild(run); g.appendChild(info); g.appendChild(miss); g.appendChild(cards); g.appendChild(qh); g.appendChild(win);
    info.style.display = 'none';
    var svg = $('svg', stage);
    function setT(id, t) { var m = $('#' + id, svg), h = (t - 30) * 1.4; m.setAttribute('y', 120 - h); m.setAttribute('height', h + 12); $('.fs-hf-read', m.parentNode).textContent = Math.round(t) + '°F'; }
    function setTime(f) {
      setT('fsHfA', A - f * 1); setT('fsHfD', T0 + (T1 - T0) * (1 - Math.pow(1 - f, 2)));
      $$('.fs-hf-ice rect', svg).forEach(function (r, i) { var s = Math.max(0, 1 - f * (1.3 + i * 0.25)), x0 = [14, 42, 26][i], y0 = [36, 44, 66][i]; r.setAttribute('width', (22 * s).toFixed(1)); r.setAttribute('height', (22 * s).toFixed(1)); r.setAttribute('x', (x0 + 11 * (1 - s)).toFixed(1)); r.setAttribute('y', (y0 + 11 * (1 - s)).toFixed(1)); r.style.opacity = s > 0.02 ? 1 : 0; });
      $('.fs-hf-lem', svg).setAttribute('fill', f > 0.6 ? '#FFEFA8' : '#FFE680');
      $('.fs-hf-clock', svg).textContent = f > 0 ? (H.timeLabel || 'Minutes waited') + ': ' + Math.round(f * 60) : '';
    }
    function drawArrow() {
      var a = H.arrows.filter(function (x) { return x.k === st.arrow; })[0], ag = $('.fs-hf-arrow', svg); if (!a) { ag.innerHTML = ''; return; }
      var into = a.ok; /* the right arrow points from the air INTO the glass */
      ag.innerHTML = '<g class="fs-hf-arr ' + (into ? 'in' : 'out') + '"><path d="' + (into ? 'M-150 0 L-20 0' : 'M-20 0 L-150 0') + '" stroke="' + (into ? '#E8636B' : '#4A90C8') + '" stroke-width="8" stroke-linecap="round"/><path d="' + (into ? 'M-20 0 l-16 -12 v24z' : 'M-150 0 l16 -12 v24z') + '" fill="' + (into ? '#E8636B' : '#4A90C8') + '"/>' +
        '<text x="-85" y="-14" text-anchor="middle" class="fs-hf-at">' + (into ? '🔥 heat' : '❄️ cold') + '</text></g>';
    }
    function paintAsk() { $$('.fs-in-chip', ask).forEach(function (c, i) { c.classList.toggle('on', H.arrows[i].k === st.arrow); c.classList.toggle('ok', !!(st.ok && H.arrows[i].ok)); }); run.disabled = !st.arrow; drawArrow(); }
    function result(anim) {
      var a = H.arrows.filter(function (x) { return x.k === st.arrow; })[0]; info.style.display = '';
      if (a && a.ok) { st.ok = 1; saveJ('heatflow', st); info.innerHTML = '<span class="fs-hs-n">🔥</span><div><b>' + esc(H.rightHead || 'Heat moved IN.') + '</b>' + esc(H.rightAfter) + '</div>'; miss.classList.remove('show'); if (anim) SFX.chime(); showCards(); }
      else { info.innerHTML = '<span class="fs-hs-n">🤔</span><div><b>' + esc(H.wrongHead || 'Look at the lemonade thermometer.') + '</b>' + esc(H.wrongAfter) + '</div>'; if (anim) SFX.thud(); }
      paintAsk();
    }
    $$('.fs-in-chip', ask).forEach(function (c, i) { c.addEventListener('click', function () { if (st.ok) return; st.arrow = H.arrows[i].k; saveJ('heatflow', st); SFX.blip(); paintAsk(); if (st.ran) result(true); }); });
    run.addEventListener('click', function () {
      if (!st.arrow) return; run.disabled = true; SFX.whoosh();
      var t0 = null, dur = reduceMotion ? 1 : 3600;
      function fr(ts) { if (t0 == null) t0 = ts; var f = Math.min(1, (ts - t0) / dur); setTime(f); if (f < 1) requestAnimationFrame(fr); else { st.ran = 1; saveJ('heatflow', st); run.textContent = '↺ ' + (H.againBtn || 'Run it again'); run.disabled = false; result(true); } }
      setTime(0); requestAnimationFrame(fr);
    });
    function showCards() {
      if (cards.dataset.on) return; cards.dataset.on = '1';
      cards.innerHTML = '<div class="fs-lu-lab">' + esc(H.cardsHead || 'Now name the way energy travels in each Florida scene') + '</div><div class="fs-hf-forms">' + H.forms.map(function (f) { return '<button type="button" class="fs-hf-form" data-k="' + f.k + '" style="--c:' + f.c + '"><span>' + f.icon + '</span>' + esc(f.t) + '</button>'; }).join('') + '</div><div class="fs-hf-grid">' +
        H.cards.map(function (c) { return '<div class="fs-hf-card" data-id="' + c.id + '"><div class="fs-hf-row"><span class="fs-hf-end"><b>' + c.src.icon + '</b><small>' + esc(c.src.t) + '</small></span><span class="fs-hf-slot">' + esc(H.dropHere || 'Drop the way') + '</span><span class="fs-hf-end"><b>' + c.rec.icon + '</b><small>' + esc(c.rec.t) + '</small></span></div><div class="fs-hf-why"></div></div>'; }).join('') + '</div>';
      function fill(id, anim) { var c = H.cards.filter(function (x) { return x.id === id; })[0], f = H.forms.filter(function (x) { return x.k === c.form; })[0], box = $('.fs-hf-card[data-id="' + id + '"]', cards);
        box.classList.add('ok'); box.style.setProperty('--c', f.c); $('.fs-hf-slot', box).innerHTML = f.icon + ' ' + esc(f.t); $('.fs-hf-why', box).textContent = c.why; if (anim && !reduceMotion) box.classList.add('pop'); }
      function drop(item, slot) {
        item.classList.remove('sel'); var box = slot.closest('.fs-hf-card'), id = box.dataset.id, c = H.cards.filter(function (x) { return x.id === id; })[0];
        if (st.f[id]) return;
        if (item.dataset.k !== c.form) { bounce(item, miss, (c.miss && c.miss[item.dataset.k]) || 'Not quite. What traveled from the source to the receiver?'); return; }
        st.f[id] = 1; saveJ('heatflow', st); miss.classList.remove('show'); SFX.chime(); fill(id, true);
        if (H.cards.every(function (x) { return st.f[x.id]; })) askOnce(qh, H.q, H.opts, 'heatflow-q', win, H.win, H.clue, 'heatflow', miss);
      }
      $$('.fs-hf-form', cards).forEach(function (it) { dragDrop(it, function () { return $$('.fs-hf-slot', cards); }, drop); });
      tapTargets(cards, $$('.fs-hf-slot', cards), drop);
      H.cards.forEach(function (c) { if (st.f[c.id]) fill(c.id, false); });
      if (H.cards.every(function (x) { return st.f[x.id]; })) askOnce(qh, H.q, H.opts, 'heatflow-q', win, H.win, H.clue, 'heatflow', miss);
    }
    at.parentNode.insertBefore(g, at.nextSibling);
    setTime(st.ran ? 1 : 0); paintAsk(); if (st.ran) { run.textContent = '↺ ' + (H.againBtn || 'Run it again'); result(false); }
  }

  /* ---------- Lesson Part 4: "Storm watch" — real lightning photos; watch the dark sky, tap when you SEE the flash, tap again when you HEAR the thunder;
     the gap in seconds ÷ 5 = miles away; three strikes, each closer (20.01) ----------
     D.stormwatch = {afterText, kicker, title, todo[], why, strikes:[{img, alt, gap, far}], startBtn, seeBtn, hearBtn, nextBtn, waitLine, earlyLine, lateLine, perMile, logLabel, youWord, realWord, mileLine, safety, q, opts, credit, win, clue} */
  function rumble(close) {
    var c = ac(); if (!c) return; var dur = close ? 2.6 : 3.4, n = Math.floor(c.sampleRate * dur), b = c.createBuffer(1, n, c.sampleRate), d = b.getChannelData(0), last = 0;
    for (var i = 0; i < n; i++) { var w = Math.random() * 2 - 1; last = (last + 0.02 * w) / 1.02; var p = i / n; d[i] = last * 3.5 * (p < 0.04 ? p / 0.04 : Math.pow(1 - p, 1.6)) * (1 + 0.5 * Math.sin(p * 40)); }
    var s = c.createBufferSource(); s.buffer = b; var f = c.createBiquadFilter(); f.type = 'lowpass'; f.frequency.value = close ? 600 : 260;
    var g = c.createGain(); g.gain.value = close ? 1.1 : 0.8; s.connect(f); f.connect(g); g.connect(c.destination); s.start();
    if (close) noise(0.12, 1500, 5000, 0.5);
  }
  function buildStormwatch() {
    var S = D.stormwatch; if (!S) return;
    var at = anchorP(S.afterText); if (!at) { FAILED.push('stormwatch anchor text not found'); return; }
    var g = gameShell(S.kicker || 'Part 4 game', S.title, S.todo, S.why); g.dataset.mod = 'stormwatch';
    var st = loadJ('stormwatch', { r: [] }), cur = Math.min(st.r.length, S.strikes.length - 1), per = S.perMile || 5;
    var view = el('div', 'fs-stw-view', '<img alt=""><div class="fs-stw-flash"></div><div class="fs-stw-hud"><span class="fs-stw-n"></span><span class="fs-stw-clock">0.0 s</span></div><div class="fs-stw-msg"></div>');
    var btns = el('div', 'fs-stw-btns', '<button type="button" class="fs-btn alt fs-stw-start">▶ ' + esc(S.startBtn || 'Start watching') + '</button><button type="button" class="fs-btn fs-stw-see" disabled>⚡ ' + esc(S.seeBtn || 'I SAW the flash') + '</button><button type="button" class="fs-btn fs-stw-hear" disabled>🔊 ' + esc(S.hearBtn || 'I HEARD the thunder') + '</button>');
    var log = el('div', 'fs-stw-log'), miss = el('div', 'fs-miss'), safe = el('div', 'fs-hs-card fs-stw-safe'), qh = el('div'), win = el('div', 'fs-win');
    g.appendChild(view); g.appendChild(btns); g.appendChild(log); g.appendChild(miss); g.appendChild(safe); g.appendChild(qh); g.appendChild(win);
    if (S.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credits</summary>' + esc(S.credit)));
    safe.style.display = 'none';
    var img = $('img', view), msg = $('.fs-stw-msg', view), clock = $('.fs-stw-clock', view), bStart = $('.fs-stw-start', btns), bSee = $('.fs-stw-see', btns), bHear = $('.fs-stw-hear', btns);
    var phase = 'idle', tFlash = 0, tSaw = null, timer = null, raf = null;
    function load() { var k = S.strikes[cur]; img.src = k.img; img.alt = k.alt; view.className = 'fs-stw-view dark'; $('.fs-stw-n', view).textContent = (S.strikeWord || 'Strike') + ' ' + (cur + 1) + ' / ' + S.strikes.length; clock.textContent = '0.0 s'; msg.textContent = S.readyLine || 'Press Start watching, then keep your eyes on the sky.'; }
    function paintLog() {
      log.innerHTML = '<div class="fs-in-k">' + esc(S.logLabel || 'Your storm log') + '</div><div class="fs-stw-rows">' + S.strikes.map(function (k, i) { var r = st.r[i];
        return '<div class="fs-stw-row' + (r ? ' ok' : '') + '"><b>' + esc((S.strikeWord || 'Strike') + ' ' + (i + 1)) + '</b>' + (r ? '<span>' + esc(S.youWord || 'You counted') + ' ' + r.you.toFixed(1) + ' s</span><span>' + esc(S.realWord || 'Real gap') + ' ' + k.gap + ' s</span><span class="fs-stw-mi">≈ ' + esc(k.far) + '</span>' : '<span>—</span>') + '</div>'; }).join('') + '</div>';
      if (st.r.length >= S.strikes.length) { safe.style.display = ''; safe.innerHTML = '<span class="fs-hs-n">🏠</span><div><b>' + esc(S.safetyHead || 'When thunder roars, go indoors!') + '</b>' + esc(S.safety || '') + '</div>'; askOnce(qh, S.q, S.opts, 'stormwatch-q', win, S.win, S.clue, 'stormwatch', miss); }
    }
    function tick() { if (phase !== 'counting' && phase !== 'heard') return; clock.textContent = ((performance.now() - tSaw) / 1000).toFixed(1) + ' s'; raf = requestAnimationFrame(tick); }
    function flash() {
      phase = 'flash'; tFlash = performance.now(); view.className = 'fs-stw-view lit' + (reduceMotion ? ' still' : ''); msg.textContent = '';
      setTimeout(function () { if (!reduceMotion) view.className = 'fs-stw-view dim'; }, 900);
      var k = S.strikes[cur];
      timer = setTimeout(function () { rumble(k.gap <= 2); var saw = phase === 'counting'; phase = 'heard'; view.classList.add('boom'); if (!saw) { tSaw = tFlash; bSee.disabled = true; tick(); } }, k.gap * 1000);
    }
    bStart.addEventListener('click', function () {
      if (phase !== 'idle' && phase !== 'done') return; if (st.r.length >= S.strikes.length) return;
      load(); phase = 'wait'; tSaw = null; bStart.disabled = true; bSee.disabled = false; bHear.disabled = false; miss.classList.remove('show'); msg.textContent = S.waitLine || 'Watch the sky…';
      timer = setTimeout(flash, 1500 + Math.random() * 2500);
    });
    bSee.addEventListener('click', function () {
      if (phase === 'wait') { bounce(bSee, miss, S.earlyLine || 'No flash yet! Wait until the sky lights up.'); return; }
      if (phase !== 'flash') return; tSaw = performance.now(); phase = 'counting'; SFX.blip(); bSee.disabled = true; msg.textContent = S.countLine || 'Counting… now listen for the thunder!'; tick();
    });
    bHear.addEventListener('click', function () {
      if (phase === 'wait') { bounce(bHear, miss, S.earlyLine || 'No flash yet! Wait until the sky lights up.'); return; }
      if (phase === 'flash' || phase === 'counting') { bounce(bHear, miss, S.lateLine || 'Not yet! Listen. Tap when you HEAR the boom.'); return; }
      if (phase !== 'heard') return;
      var you = (performance.now() - (tSaw || tFlash)) / 1000; phase = 'done'; cancelAnimationFrame(raf); clock.textContent = you.toFixed(1) + ' s';
      st.r[cur] = { you: +you.toFixed(1) }; saveJ('stormwatch', st); SFX.chime(); miss.classList.remove('show');
      var k = S.strikes[cur]; msg.textContent = (S.mileLine || '{s} seconds ÷ 5 = about {far}').replace('{s}', k.gap).replace('{far}', k.far);
      bSee.disabled = true; bHear.disabled = true; paintLog();
      if (cur < S.strikes.length - 1) { cur++; bStart.disabled = false; bStart.textContent = '▶ ' + (S.nextBtn || 'Next strike'); } else { bStart.disabled = true; }
    });
    at.parentNode.insertBefore(g, at.nextSibling);
    load(); paintLog(); if (st.r.length >= S.strikes.length) { bStart.disabled = true; view.className = 'fs-stw-view dim'; msg.textContent = S.doneLine || ''; }
    else if (st.r.length) bStart.textContent = '▶ ' + (S.nextBtn || 'Next strike');
  }

  /* ---------- Tool of the Week: a circuit tester (continuity probe). Drag (or tap) a thing onto the probe tips, predict light or no light, then
     the bulb lights and it beeps only for conductors; every object gets logged, then a chip question (20.01) ----------
     tool.circuittester = {title, todo[], img, alt, cap, objects:[{k, icon, t, c (true = conductor), note}], predictQ, yes, no, dropHere, logLabel, yesWord, noWord, q:{q, opts:[{t, ok, why}]}, credit} */
  SIMS.circuittester = function (host, T) {
    var C = T.circuittester, st = loadJ('circuittester', {}), cur = null;
    host.innerHTML = '<div class="fs-game-k">Try it: a circuit tester</div><div class="fs-game-t">' + esc(C.title) + '</div>' +
      '<ul class="fs-todo">' + C.todo.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>' +
      (C.img ? '<figure class="fs-rdr-photo"><img alt="' + esc(C.alt) + '" src="' + esc(C.img) + '"><figcaption>' + esc(C.cap || '') + '</figcaption></figure>' : '') +
      '<div class="fs-ctt-bench"><svg viewBox="0 0 520 170" class="fs-ctt-svg" role="img" aria-label="A model of a circuit tester: a battery, a bulb and two probe tips with a gap between them">' +
      '<rect x="20" y="60" width="90" height="46" rx="8" fill="#2E3A4A"/><rect x="110" y="72" width="8" height="22" rx="2" fill="#B9C2CC"/><text x="64" y="88" text-anchor="middle" class="fs-ctt-bt">1.5 V</text>' +
      '<path d="M118 83 C170 83 170 30 220 30" class="fs-ctt-w"/><g transform="translate(240 30)"><circle class="fs-ctt-glow" r="34"/><circle r="16" class="fs-ctt-bulb"/><rect x="-8" y="14" width="16" height="12" fill="#9AA5B1"/></g>' +
      '<path d="M256 30 C330 30 330 120 360 120" class="fs-ctt-w"/><path d="M20 83 C0 83 0 150 60 150 C200 150 330 150 330 150" class="fs-ctt-w"/>' +
      '<g><rect x="330" y="143" width="40" height="14" rx="7" fill="#D9534F"/><path d="M370 150 L438 140" stroke="#9AA5B1" stroke-width="5" stroke-linecap="round"/></g>' +
      '<g><rect x="360" y="113" width="40" height="14" rx="7" fill="#2E3A4A"/><path d="M400 120 L438 126" stroke="#9AA5B1" stroke-width="5" stroke-linecap="round"/></g>' +
      '<text x="466" y="148" text-anchor="middle" class="fs-ctt-obj"></text><text x="30" y="20" class="fs-ctt-model">' + esc(C.model || 'a model') + '</text></svg>' +
      '<div class="fs-ctt-drop">' + esc(C.dropHere || 'Drop a thing on the probe tips') + '</div></div>' +
      '<div class="fs-ctt-tray">' + C.objects.map(function (o) { return '<button type="button" class="fs-ctt-it" data-k="' + o.k + '"><span>' + o.icon + '</span>' + esc(o.t) + '</button>'; }).join('') + '</div>' +
      '<div class="fs-ctt-pred"></div><div class="fs-ctt-res"></div><div class="fs-ctt-log"></div><div class="fs-sv-q fs-ctt-q"></div><div class="fs-miss fs-ctt-miss"></div><div class="fs-win fs-ctt-win"></div>' +
      (C.credit ? '<details class="fs-credit fs-credit-fold"><summary>📷 Photo credit</summary>' + esc(C.credit) + '</details>' : '');
    var bench = $('.fs-ctt-bench', host), drop = $('.fs-ctt-drop', host), miss = $('.fs-ctt-miss', host), pred = $('.fs-ctt-pred', host), res = $('.fs-ctt-res', host);
    function obj(k) { return C.objects.filter(function (o) { return o.k === k; })[0]; }
    function place(k) {
      cur = obj(k); bench.classList.remove('on', 'off'); $('.fs-ctt-obj', host).textContent = cur.icon; drop.textContent = cur.t; res.innerHTML = ''; SFX.blip();
      pred.innerHTML = '<div class="fs-in-k">' + esc(C.predictQ || 'Predict: will the bulb light up?') + '</div><div class="fs-in-chips"><button type="button" class="fs-in-chip" data-v="1">💡 ' + esc(C.yes || 'It will light') + '</button><button type="button" class="fs-in-chip" data-v="0">⚫ ' + esc(C.no || 'It won’t light') + '</button></div>';
      $$('.fs-in-chip', pred).forEach(function (b) { b.addEventListener('click', function () { test(b.dataset.v === '1'); }); });
    }
    function test(guess) {
      var o = cur; if (!o) return; bench.classList.add(o.c ? 'on' : 'off');
      if (o.c) { tone(1760, 0, 0.35, 'square', 0.03); } else tone(140, 0, 0.12, 'sine', 0.06);
      var right = guess === !!o.c;
      res.innerHTML = '<div class="fs-hs-card"><span class="fs-hs-n">' + o.icon + '</span><div><b>' + esc(o.t + ': ' + (o.c ? (C.yesWord || 'CONDUCTOR, it lit up!') : (C.noWord || 'INSULATOR, no light.'))) + '</b>' + esc((right ? (C.rightPre || 'Your prediction was right. ') : (C.wrongPre || 'Surprise! ')) + o.note) + '</div></div>';
      pred.innerHTML = ''; st[o.k] = { c: o.c ? 1 : 0, g: right ? 1 : 0 }; saveJ('circuittester', st); logs();
    }
    function logs() {
      $('.fs-ctt-log', host).innerHTML = '<div class="fs-in-k">' + esc(C.logLabel || 'Your test log') + '</div><div class="fs-ctt-cols"><div><b>💡 ' + esc(C.colYes || 'Conductors (lit up)') + '</b><ul>' + C.objects.filter(function (o) { return st[o.k] && o.c; }).map(function (o) { return '<li>' + o.icon + ' ' + esc(o.t) + '</li>'; }).join('') + '</ul></div><div><b>⚫ ' + esc(C.colNo || 'Insulators (no light)') + '</b><ul>' + C.objects.filter(function (o) { return st[o.k] && !o.c; }).map(function (o) { return '<li>' + o.icon + ' ' + esc(o.t) + '</li>'; }).join('') + '</ul></div></div>';
      $$('.fs-ctt-it', host).forEach(function (b) { b.classList.toggle('done', !!st[b.dataset.k]); });
      if (C.objects.every(function (o) { return st[o.k]; })) check();
    }
    function check() {
      var q = $('.fs-ctt-q', host); if (q.dataset.on) return; q.dataset.on = '1';
      q.innerHTML = '<div class="fs-in-k">' + esc(C.q.q) + '</div><div class="fs-in-chips">' + C.q.opts.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(o.t) + '</button>'; }).join('') + '</div>';
      function ok(i) { $$('.fs-in-chip', q)[i].classList.add('on', 'ok'); var w = $('.fs-ctt-win', host); w.innerHTML = esc(C.q.opts[i].why); w.classList.add('show'); }
      $$('.fs-in-chip', q).forEach(function (c) { c.addEventListener('click', function () { var o = C.q.opts[+c.dataset.i]; if (!o.ok) { bounce(c, miss, o.why); return; } miss.classList.remove('show'); ok(+c.dataset.i); SFX.win(); store('circuittester-q', '1'); toolDone(); }); });
      if (store('circuittester-q')) ok(C.q.opts.map(function (o, j) { return o.ok ? j : -1; }).filter(function (j) { return j > -1; })[0]);
    }
    $$('.fs-ctt-it', host).forEach(function (b) {
      dragDrop(b, function () { return [bench]; }, function (item) { item.classList.remove('sel'); place(item.dataset.k); });
      b.addEventListener('click', function () { if (b.classList.contains('sel')) { b.classList.remove('sel'); place(b.dataset.k); } });
    });
    bench.addEventListener('click', function () { var s = $('.fs-ctt-it.sel', host); if (s) { s.classList.remove('sel'); place(s.dataset.k); } });
    logs();
  };

  /* ---------- Case file: a data-logger strip chart (20.01). C.strip = {head, sub, times[], mark (index), markLabel, traces:[{icon, t, c, vals:[0–1]}], note} ---------- */
  function stripChart(S) {
    var W = 640, L = 132, R = 16, top = 26, rowH = 52, n = S.times.length, H = top + rowH * S.traces.length + 26;
    function x(i) { return L + i * (W - L - R) / (n - 1); }
    var grid = ''; for (var i = 0; i < n; i++) grid += '<line x1="' + x(i) + '" y1="' + top + '" x2="' + x(i) + '" y2="' + (H - 26) + '" class="fs-strip-g"/>';
    var rows = S.traces.map(function (t, k) {
      var y0 = top + k * rowH, base = y0 + rowH - 10, amp = rowH - 18;
      var pts = t.vals.map(function (v, i) { return x(i).toFixed(1) + ',' + (base - v * amp).toFixed(1); }).join(' ');
      return '<line x1="' + L + '" y1="' + (y0 + rowH) + '" x2="' + (W - R) + '" y2="' + (y0 + rowH) + '" class="fs-strip-sep"/><text x="10" y="' + (y0 + rowH / 2 + 2) + '" class="fs-strip-lab"><tspan class="fs-strip-ic">' + t.icon + '</tspan> ' + esc(t.t) + '</text>' +
        (t.sub ? '<text x="10" y="' + (y0 + rowH / 2 + 18) + '" class="fs-strip-sub">' + esc(t.sub) + '</text>' : '') + '<polyline points="' + pts + '" class="fs-strip-line" style="stroke:' + t.c + '"/>';
    }).join('');
    var tl = S.times.map(function (t, i) { return (i % (S.every || 1)) ? '' : '<text x="' + x(i) + '" y="' + (H - 8) + '" text-anchor="middle" class="fs-strip-t">' + esc(t) + '</text>'; }).join('');
    var mk = S.mark != null ? '<line x1="' + x(S.mark) + '" y1="' + (top - 6) + '" x2="' + x(S.mark) + '" y2="' + (H - 22) + '" class="fs-strip-mk"/><rect x="' + (x(S.mark) - 38) + '" y="2" width="76" height="20" rx="6" class="fs-strip-mkb"/><text x="' + x(S.mark) + '" y="16" text-anchor="middle" class="fs-strip-mkt">' + esc(S.markLabel || '') + '</text>' : '';
    return '<div class="fs-strip"><div class="fs-strip-h"><b>' + esc(S.head) + '</b><small>' + esc(S.sub || '') + '</small></div><svg viewBox="0 0 ' + W + ' ' + H + '" class="fs-strip-svg" role="img" aria-label="' + esc(S.alt || S.head) + '">' + grid + rows + tl + mk + '</svg>' + (S.note ? '<div class="fs-strip-note">' + esc(S.note) + '</div>' : '') + '</div>';
  }

  function init() {
    if (/[?&]review\b/.test(location.search)) html.classList.add('fs-review');
    guard('tabs', trackTabs);
    guard('intro', cleanIntro);
    guard('header', buildHeader);
    guard('case', buildCase);
    guard('reaction', buildReaction);
    guard('relay', buildRelay);
    guard('cams', buildCams);
    guard('sort', buildSort);
    guard('thread', buildThread);
    guard('ripple', buildRipple);
    guard('judge', buildJudge);
    guard('survey', buildSurvey);
    guard('verdict', buildVerdict);
    guard('trend', buildTrend);
    guard('beaks', buildBeaks);
    guard('wade', buildWade);
    guard('gator', buildGator);
    guard('arrow', buildArrow);
    guard('upgrade', buildUpgrade);
    guard('chain', buildChain);
    guard('kit', buildKit);
    guard('echo', buildEcho);
    guard('build', buildBuild);
    guard('compare', buildCompare);
    guard('fix', buildFix);
    guard('lineup', buildLineup);
    guard('grow', buildGrow);
    guard('passiton', buildPassiton);
    guard('pollen', buildPollen);
    guard('bagtest', buildBagtest);
    guard('trace', buildTrace);
    guard('wobble', buildWobble);
    guard('nextup', buildNextup);
    guard('morph', buildMorph);
    guard('wheel', buildWheel);
    guard('venn', buildVenn);
    guard('twowinters', buildTwowinters);
    guard('calendar', buildCalendar);
    guard('manatee', buildManatee);
    guard('seasonmodel', buildSeasonmodel);
    guard('unmake', buildUnmake);
    guard('refill', buildRefill);
    guard('impact', buildImpact);
    guard('twosources', buildTwosources);
    guard('guessmap', buildGuessmap);
    guard('maplayers', buildMaplayers);
    guard('whyhere', buildWhyhere);
    guard('pins', buildPins);
    guard('twocol', buildTwocol);
    guard('scale', buildScale);
    guard('toolbox', buildToolbox);
    guard('townhall', buildTownhall);
    guard('limits', buildLimits);
    guard('matrix', buildMatrix);
    guard('improve', buildImprove);
    guard('pilot', buildPilot);
    guard('bulletin', buildBulletin);
    guard('stormclock', buildStormclock);
    guard('flyover', buildFlyover);
    guard('stormchain', buildStormchain);
    guard('mitsort', buildMitsort);
    guard('buildhouse', buildBuildhouse);
    guard('fixtown', buildFixtown);
    guard('zoom', buildZoom);
    guard('bench', buildBench);
    guard('scope', buildScope);
    guard('nightsky', buildNightSky);
    guard('racelight', buildRacelight);
    guard('openwide', buildOpenwide);
    guard('skyhunt', buildSkyhunt);
    guard('tv', buildTv);
    guard('deepfield', buildDeepfield);
    guard('flick', buildFlick);
    guard('replay', buildReplay);
    guard('pinball', buildPinball);
    guard('slowmo', buildSlowmo);
    guard('drawpath', buildDrawpath);
    guard('stopwatch', buildStopwatch);
    guard('lockdown', buildLockdown);
    guard('dotplot', buildDotplot);
    guard('detective', buildDetective);
    guard('rateit', buildRateit);
    guard('blockpath', buildBlockpath);
    guard('heatflow', buildHeatflow);
    guard('stormwatch', buildStormwatch);
    guard('words', buildWords);
    guard('layers', buildLayers);
    guard('tank', buildTank);
    guard('score', buildScore);
    guard('revise', buildRevise);
    guard('quiz', buildQuiz);
    guard('solve', buildSolve);
    guard('permit', buildPermit);
    guard('bullseye', buildBullseye);
    guard('starchart', buildStarchart);
    guard('fold', foldExtras);
    guard('helpers', buildHelpers);
    guard('inputs', buildInputs);
    guard('specimen', buildSpecimen);
    guard('lens', buildWordLens);
    guard('slots', placeSlots);
    guard('id', buildID);
    guard('name', guardNameBox);
    guard('ambient', buildAmbient);
    guard('camera', buildCamera);
    guard('journal', buildJournal);
    guard('sketch', buildSketch);
    guard('facts', buildFacts);
    guard('photos', buildPhotos);
    guard('drawers', buildDrawers);
    guard('highlighter', buildHighlighter);
    guard('tool', buildTool);
    guard('ornaments', buildOrnaments);
    guard('mock', buildMock);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
})();
