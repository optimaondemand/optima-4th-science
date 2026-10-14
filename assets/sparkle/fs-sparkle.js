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
  function pushToast(icon, title, text, ms) {
    var st = $('#fsToasts'); if (!st) { st = fsOnly(el('div', 'fs-toasts')); st.id = 'fsToasts'; st.setAttribute('aria-live', 'polite'); document.body.appendChild(st); }
    var t = el('div', 'fs-toast', '<span>' + icon + '</span><div><b>' + esc(title) + '</b>' + esc(text) + '</div>');
    st.appendChild(t);
    setTimeout(function () { t.classList.add('show'); SFX.win(); }, 30);
    setTimeout(function () { t.classList.remove('show'); t.classList.add('leave'); setTimeout(function () { t.remove(); }, 450); }, ms || 4600);
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
  function makeRadio(info, who, src, demo) {
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
      if (audio && audio.duration) setWord(Math.floor(audio.currentTime / audio.duration * wordEls.length));
      if (playing) raf = requestAnimationFrame(frame);
    }
    function start() { playing = true; row.classList.add('playing'); tr.classList.add('open'); b.textContent = '❚❚ Pause'; if (!reduceMotion) raf = requestAnimationFrame(frame); }
    function stop(done) { playing = false; row.classList.remove('playing'); cancelAnimationFrame(raf); b.textContent = done ? '▶ Play again' : '▶ ' + (info.audioLabel || 'Listen'); bars.forEach(function (r) { r.setAttribute('height', 4); r.setAttribute('y', 70); }); if (done) { setWord(wordEls.length); setTimeout(SFX.crackle, 100); } }
    var audio = null;
    if (src) {
      audio = new Audio(au(src));
      audio.addEventListener('play', function () {
        if (!an) { try { var c = ac(); var node = c.createMediaElementSource(audio); an = c.createAnalyser(); an.fftSize = 128; buf = new Uint8Array(an.frequencyBinCount); node.connect(an); an.connect(c.destination); } catch (e) { an = null; } }
        start();
      });
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
        u.onboundary = function (e) { level = 0.9; var k = 0; for (var j = 0; j < starts.length; j++) if (starts[j][0] <= e.charIndex) k = j; setWord(k); };
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
  function probe(url, kind, cb) {
    var m = document.createElement(kind); var done = false;
    function fin(ok) { if (done) return; done = true; cb(ok); }
    m.preload = 'metadata'; m.addEventListener('loadedmetadata', function () { fin(true); }); m.addEventListener('error', function () { fin(false); });
    setTimeout(function () { fin(false); }, 8000); m.src = au(url);
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
    probe(vfile, 'video', function (ok) {
      if (ok) {
        var v = el('div', 'fs-video', '<video controls playsinline preload="metadata" poster="' + vfile.replace(/\.mp4$/, '.jpg') + '" src="' + vfile + '"></video>');
        showVideo(v); return;
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
      box.classList.remove('fs-empty'); live.appendChild(makeRadio(info, who, afile, false));
    });
    if (info.script) { // teacher view: demo the walkie-talkie with the computer's voice
      var demoBtn = el('button', 'fs-demo', '▶ Demo the radio'); demoBtn.type = 'button';
      $('.fs-ms-ph > div', box).appendChild(demoBtn);
      demoBtn.addEventListener('click', function () { var r = makeRadio(info, who, null, true); demoBtn.replaceWith(r); $('.fs-play', r).click(); });
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
    add('explore', $('#tab-explore .act-body'), 'prepend');
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
      '<span class="fs-exp-tag">Week ' + esc(D.week || exp.num || '') + '</span> ' +
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
    var nb = pill('📓 <span class="fs-nb-l">Field Notebook</span> <span class="fs-count">0</span>', null, openNotebook);
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
    var card = fsOnly(el('div', 'fs-casecard'));
    var stills = (C.stills || []).map(function (s) {
      return '<div class="fs-still"><div class="fs-still-img' + (s.img ? ' photo' : '') + '">' + (s.img ? '<img alt="' + esc(s.alt || s.cam) + '" src="' + esc(s.img) + '"><span class="fs-still-rec">● REC</span>' : s.svg) + '<span class="fs-still-q">?</span></div><div class="fs-still-cap"><b>' + esc(s.cam) + '</b> ' + esc(s.time) + '</div></div>';
    }).join('');
    card.innerHTML = '<div class="fs-folder-tab">CASE FILE ' + esc(C.num) + '</div><div class="fs-folder fs-kraft">' +
      '<div class="fs-case-k"><span class="fs-case-av"></span><span>From ' + esc(crewOf().name) + ', ' + esc(crewOf().role) + '</span></div>' +
      '<div class="fs-case-t">' + esc(C.title) + '</div>' +
      '<p class="fs-case-p">' + esc(C.hook) + '</p><div class="fs-stills">' + stills + '</div>' + (C.stillsCredit ? '<details class="fs-credit fs-credit-fold"><summary>📷 Photo credits</summary>' + esc(C.stillsCredit) + '</details>' : '') +
      '<div class="fs-case-ask">🔎 ' + esc(C.question) + '</div>' +
      '<div class="fs-case-how">' + esc(C.how) + '</div></div>';
    $('.fs-case-av', card).appendChild(avatar(crewOf(), 'small'));
    // tap a camera still to see it big
    $$('.fs-still', card).forEach(function (st, i) {
      var s = (C.stills || [])[i]; if (!s || !s.img) { st.style.cursor = 'default'; return; }
      st.setAttribute('role', 'button'); st.tabIndex = 0; st.title = 'Tap to see this camera bigger';
      function open() {
        var m = modal(); SFX.blip();
        m.innerHTML = '<div class="fs-nb fs-kraft fs-still-big"><button class="fs-x" type="button" aria-label="Close">✕</button>' +
          '<div class="fs-still-img photo"><img alt="' + esc(s.alt || s.cam) + '" src="' + esc(s.img) + '"><span class="fs-still-rec">● REC</span></div>' +
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
        win.innerHTML = esc(o.why); win.classList.add('show'); SFX.win(); drawBoard();
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
    var g = gameShell('Send the signal', R.title, R.todo, R.why); g.dataset.mod = 'relay';
    var relay = el('div', 'fs-relay'); relay.appendChild(el('div', 'fs-relay-wire')); var pulse = el('div', 'fs-relay-pulse'); relay.appendChild(pulse);
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
    var body = $('#tab-explore .act-body'); if (!body) return;
    var firstP = $('p', body);
    var g = gameShell(S.kicker || ('Field cam: ' + (S.subject || '')), S.title, S.todo, S.why); g.dataset.mod = 'sort';
    var bins = el('div', 'fs-sort');
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

  /* ---------- Self-Check: one question at a time + miss lines ---------- */
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
    box.innerHTML = '<div class="fs-game-k" style="color:#7A5F2C">' + esc(Sp.kicker || 'Specimen collected') + '</div><div class="fs-tag"><div class="fs-tag-ic">' + Sp.icon + '</div><div class="fs-tag-k">Specimen ' + esc(D.lesson) + '</div><div class="fs-tag-t">' + esc(Sp.name) + '</div><div class="fs-stamp">' + esc(Sp.stamp || 'LOGGED') + '</div></div>' +
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
      try { var v = localStorage.getItem(keys[i]); if (!v) continue; var n = v; try { var j = JSON.parse(v); n = (j && (j.name || j.first || j.firstName)) || (typeof j === 'string' ? j : ''); } catch (e) {} if (n) return String(n).slice(0, 24); } catch (e) {}
    }
    var g = document.getElementById('student-name'); return g && g.value.trim() ? g.value.trim().slice(0, 24) : '';
  }
  function nameProblem(n) {
    if (!n || n.length < 2) return 'Type your first name (at least 2 letters).';
    if (!/^[A-Za-zÀ-ÿ' -]+$/.test(n)) return 'Use letters only, please.';
    return '';
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
    var b = el('button', 'fs-pill', '🦗 <span class="fs-nb-l">Marsh sounds</span>'); b.type = 'button';
    var rk = el('span', 'fs-pill fs-hd-rank'); tools.insertBefore(rk, tools.firstChild); rk.innerHTML = rank().icon + ' <span>' + esc(rank().t) + '</span>';
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
      ov = fsOnly(el('div', 'fs-snapov', '<div class="fs-snap-tip">📷 Drag a box around what you want to snap. <button type="button">Cancel</button></div><div class="fs-snap-box"></div>'));
      document.body.appendChild(ov); SFX.blip();
      var box = $('.fs-snap-box', ov), st = null;
      $('.fs-snap-tip button', ov).addEventListener('click', function (e) { e.stopPropagation(); end(); });
      document.addEventListener('keydown', esc1);
      function esc1(e) { if (e.key === 'Escape') end(); }
      function end() { if (ov) { ov.remove(); ov = null; } document.removeEventListener('keydown', esc1); }
      ov.addEventListener('pointerdown', function (e) { if (e.target.closest('.fs-snap-tip')) return; st = { x: e.clientX, y: e.clientY }; ov.setPointerCapture && ov.setPointerCapture(e.pointerId); box.style.display = 'block'; draw(e); });
      ov.addEventListener('pointermove', function (e) { if (st) draw(e); });
      ov.addEventListener('pointerup', function (e) {
        if (!st) return; var r = rect(e); st = null;
        if (r.w < 24 || r.h < 24) { box.style.display = 'none'; return; }
        end(); snap(r);
      });
      function rect(e) { return { x: Math.min(st.x, e.clientX), y: Math.min(st.y, e.clientY), w: Math.abs(e.clientX - st.x), h: Math.abs(e.clientY - st.y) }; }
      function draw(e) { var r = rect(e); box.style.left = r.x + 'px'; box.style.top = r.y + 'px'; box.style.width = r.w + 'px'; box.style.height = r.h + 'px'; }
    }
    function snap(r) {
      var flash = fsOnly(el('div', 'fs-flash')); document.body.appendChild(flash);
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
          ignoreElements: function (n) { return n.classList && (n.classList.contains('fs-fab') || n.classList.contains('fs-mock') || n.classList.contains('fs-toasts') || n.classList.contains('fs-flash') || n.classList.contains('fs-modal') || n.classList.contains('fs-snapov')); }
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
        }).catch(function (e) { ref.removeAttribute('data-fs-ref'); root.removeAttribute('data-fs-root'); FAILED.push('camera: ' + (e && e.message)); window.FS_SNAP_ERR = String(e && (e.stack || e.message) || e); toast('📷', 'That snap didn’t work', 'Scroll a little and try again.'); });
      });
    }
    function caption(src) {
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
      var rows = el('ol', 'fs-in-rows'); box.appendChild(rows);
      var add = el('button', 'fs-hintbtn fs-in-add', '+ Add a step'); add.type = 'button'; box.appendChild(add);
      var cnt = el('span', 'fs-count'); box.appendChild(cnt); box.appendChild(mir);
      function sync() {
        var vals = $$('input', rows).map(function (x) { return x.value.trim(); });
        store('ans.' + I.id + '.rows', JSON.stringify(vals));
        var f = vals.filter(Boolean); setG(mir, f.map(function (v, i) { return (i + 1) + '. ' + v; }).join('\n'));
        cnt.textContent = '📝 ' + Math.min(f.length, I.min || 3) + ' of ' + (I.min || 3) + ' steps' + (f.length >= (I.min || 3) ? ' ✓' : '');
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
    var h = '<!doctype html><html><head><meta charset="utf-8"><title>Field journal · ' + esc(D.lesson) + ' · ' + esc(n) + '</title><style>' +
      'body{font-family:Nunito,Arial,sans-serif;color:#2B1D12;max-width:760px;margin:24px auto;padding:0 18px;line-height:1.5}' +
      'h1{font-size:24px;margin:0;color:#0E1C42}h2{font-size:17px;color:#0E1C42;border-bottom:2px solid #C9B489;padding-bottom:3px;margin:22px 0 8px}' +
      '.k{font-size:11px;letter-spacing:1.2px;text-transform:uppercase;color:#7A5F2C;font-weight:800}.bq{background:#F4EBD6;border-left:4px solid #F5B83D;padding:8px 12px;border-radius:6px;font-weight:700}' +
      '.q{margin:10px 0;page-break-inside:avoid}.q b{display:block;font-size:14px}.q p{margin:4px 0 0;border:1px solid #DDD;border-radius:6px;padding:6px 10px}' +
      'ul{margin:4px 0;padding-left:20px}.ph{display:grid;grid-template-columns:1fr 1fr;gap:14px}.pol{border:1px solid #CCC;padding:8px 8px 6px;border-radius:4px;page-break-inside:avoid;box-shadow:0 2px 6px rgba(0,0,0,.12)}' +
      '.sk{margin:8px 0 14px;page-break-inside:avoid}.sk b{display:block;margin-bottom:4px}.sk img{width:100%;border:1px solid #CCC;border-radius:6px}.pol img{width:100%;display:block}.pol div{font-size:13px;margin-top:5px}.pol small{color:#7A5F2C}@media print{button{display:none}}</style></head><body>' +
      '<div class="k">Optima Academy Online · 4th Grade Science · Field journal</div><h1>' + esc(D.lesson) + ' · ' + esc(title) + '</h1>' +
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
      var anchorGame = $$('.fs-game').filter(function (g) { return g.dataset.mod === P.after; })[0];
      if (!anchorGame) { FAILED.push('photo: no anchor ' + P.after); return; }
      var g = gameShell(P.kicker || 'Look closer', P.title, P.todo, P.why);
      g.classList.add('fs-photo-game');
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
            if (!left) { win.innerHTML = esc(P.task.win); win.classList.add('show'); SFX.win(); store('photo-' + P.id, '1'); }
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
    var anchor = $('#tab-' + (T.tab || 'explore') + ' .tab-next-wrap') || $('#tab-' + (T.tab || 'explore') + ' .activity-card'); if (!anchor) return;
    var before = anchor.classList.contains('tab-next-wrap');
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
    withManifest(function (m) {
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
  /* ----- thermometer simulation ----- */
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
    guard('quiz', buildQuiz);
    guard('solve', buildSolve);
    guard('helpers', buildHelpers);
    guard('inputs', buildInputs);
    guard('specimen', buildSpecimen);
    guard('lens', buildWordLens);
    guard('slots', placeSlots);
    guard('id', buildID);
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
