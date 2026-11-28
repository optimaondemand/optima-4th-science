  /* ======================= 30.01 "The Melted Box" (Case 30): case.claim, sealbag, callit, undoer, wipe, statedial, remelt, claimstamp, SIMS.evapdish ======================= */

  /* ---------- case: the freight damage claim (30.01). case.claim = {head, no, rows:[[k,v]], stamp, note, sign}. A carbon-copy claim form with a rubber stamp. Classes fs-cfm-*. ---------- */
  function claimCard(K) {
    return '<div class="fs-cfm"><div class="fs-cfm-h"><span>' + esc(K.head) + '</span><small>' + esc(K.no || '') + '</small></div>' +
      '<dl class="fs-cfm-rows">' + K.rows.map(function (r) { return '<dt>' + esc(r[0]) + '</dt><dd>' + esc(r[1]) + '</dd>'; }).join('') + '</dl>' +
      (K.note ? '<p class="fs-cfm-note">' + esc(K.note) + '</p>' : '') +
      (K.stamp ? '<div class="fs-cfm-stamp">' + esc(K.stamp) + '</div>' : '') +
      (K.sign ? '<div class="fs-cfm-sign">' + esc(K.sign) + '</div>' : '') + '</div>';
  }

  /* ---------- Warm-Up: "The sealed bag" — drag a sealed bag of ice onto a kitchen scale (or tap the scale), read the number, press Wait an hour, then CALL the
     new reading before it shows. The scale does not move (30.01) ----------
     D.sealbag = {afterText, kicker, title, todo[], why, bag:{icon, t}, scaleLabel, start, end, unit, dropLine, readLine ({n}), waitBtn, waitLine, ask, opts:[{t, ok, miss}],
                  revealLine, q, opts2, win, clue}. Classes fs-sb-*. */
  function buildSealbag() {
    var S = D.sealbag; if (!S) return;
    var at = anchorP(S.afterText); if (!at) { FAILED.push('sealbag anchor text not found'); return; }
    var g = gameShell(S.kicker || 'Warm-Up game', S.title, S.todo, S.why); g.dataset.mod = 'sealbag';
    var st = loadJ('sealbag', { on: 0, wait: 0, call: 0 });
    var row = el('div', 'fs-sb-row'), tray = el('div', 'fs-sb-tray'), scale = el('div', 'fs-sb-scale');
    var note = el('div', 'fs-hs-card fs-sb-note'), ah = el('div'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    row.appendChild(tray); row.appendChild(scale);
    [row, note, ah, miss, qh, win].forEach(function (e) { g.appendChild(e); });
    function readout(n) {
      return '<div class="fs-sb-pan">' + (st.on ? '<div class="fs-sb-bag' + (st.wait ? ' melted' : '') + '"><span>' + (st.wait ? '💧' : S.bag.icon) + '</span></div>' : '<em>' + esc(S.dropLine || 'Drop the bag here.') + '</em>') + '</div>' +
        '<div class="fs-sb-read' + (n == null ? ' off' : '') + '">' + (n == null ? '— — —' : n + ' ' + (S.unit || 'g')) + '</div>' +
        '<div class="fs-sb-lab">' + esc(S.scaleLabel || 'Kitchen scale') + '</div>';
    }
    function paint() {
      tray.innerHTML = '';
      if (!st.on) {
        var c = el('button', 'fs-in-chip fs-dragc fs-sb-chip', '<span>' + S.bag.icon + '</span> ' + esc(S.bag.t)); c.type = 'button'; tray.appendChild(c);
        dragDrop(c, function () { return [scale]; }, function () { put(); });
      } else tray.innerHTML = '<div class="fs-sb-seal">🔒 ' + esc(S.bag.t) + '</div>';
      scale.innerHTML = readout(st.on ? (st.wait && !st.call ? null : (st.wait ? S.end : S.start)) : null);
      if (!st.on) { note.innerHTML = '<em>' + esc(S.dropLine || 'Drag the bag onto the scale, or tap the scale.') + '</em>'; return; }
      if (!st.wait) {
        note.innerHTML = '<span class="fs-hs-n">⚖️</span><div>' + esc((S.readLine || 'The scale reads {n}.').replace('{n}', S.start)) + '</div>';
        if (!$('.fs-sb-go', g)) { var b = el('button', 'fs-btn fs-sb-go', esc(S.waitBtn || '⏱ Wait an hour')); b.type = 'button'; note.appendChild(b); b.addEventListener('click', wait); }
        return;
      }
      if (!st.call) { note.innerHTML = '<span class="fs-hs-n">💧</span><div>' + esc(S.waitLine || 'The ice melted.') + '</div>'; ask(); return; }
      note.innerHTML = '<span class="fs-hs-n">✅</span><div>' + esc(S.revealLine || 'Exactly the same.') + '</div>';
      askOnce(qh, S.q, S.opts2, 'sealbag-q', win, S.win, S.clue, 'sealbag', miss);
    }
    function put() { if (st.on) return; ac(); SFX.thud(); st.on = 1; saveJ('sealbag', st); paint(); }
    function wait() {
      if (st.wait) return; ac(); SFX.whoosh(); scale.classList.add('melting');
      setTimeout(function () { scale.classList.remove('melting'); st.wait = 1; saveJ('sealbag', st); paint(); }, reduceMotion ? 0 : 900);
    }
    function ask() {
      if (ah.dataset.on) return; ah.dataset.on = '1';
      chipsQ(ah, S.ask, S.opts, function () { st.call = 1; saveJ('sealbag', st); SFX.sparkle(); paint(); }, miss);
    }
    scale.addEventListener('click', function () { if (!st.on) put(); });
    paint(); placeAfter(g, at);
  }

  /* ---------- Part 1: "Call the number first" — read the scale, make the change, then TYPE the reading you expect on a keypad before you weigh it. Three rounds,
     three identical readings (30.01) ----------
     D.callit = {afterText, kicker, title, todo[], why, keyLabel, weighBtn, unit, startLine, callLine, realLine, hitLine, overLine, underLine, needLine,
                 rounds:[{id, icon, t, btn, mass, after, line, same}], q, opts, win, clue}. Classes fs-cal-*. */
  function buildCallit() {
    var C = D.callit; if (!C) return;
    var at = anchorP(C.afterText); if (!at) { FAILED.push('callit anchor text not found'); return; }
    var g = gameShell(C.kicker || 'Part 1 game', C.title, C.todo, C.why); g.dataset.mod = 'callit';
    var st = loadJ('callit', { i: 0, done: [] });
    var stage = el('div', 'fs-cal-stage'), log = el('div', 'fs-cal-log'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    [stage, log, miss, qh, win].forEach(function (e) { g.appendChild(e); });
    var typed = '', phase = 'start';
    function R() { return C.rounds[st.i]; }
    function drawLog() {
      log.innerHTML = st.done.length ? '<div class="fs-in-k">Your readings</div>' + st.done.map(function (d) {
        return '<div class="fs-cal-lrow"><span>' + d.icon + '</span><b>' + esc(d.t) + '</b><em>' + d.m + ' ' + (C.unit || 'g') + ' → ' + d.m + ' ' + (C.unit || 'g') + '</em></div>'; }).join('') : '';
    }
    function pad() {
      return '<div class="fs-cal-pad"><div class="fs-in-k">' + esc(C.keyLabel || 'Type your call') + '</div>' +
        '<div class="fs-cal-disp">' + (typed || '—') + ' <small>' + (C.unit || 'g') + '</small></div><div class="fs-cal-keys">' +
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '⌫', '0', '✓'].map(function (k) { return '<button type="button" class="fs-cal-key' + (k === '✓' ? ' go' : '') + '" data-k="' + k + '">' + k + '</button>'; }).join('') +
        '</div><button type="button" class="fs-btn fs-cal-weigh">' + esc(C.weighBtn || '⚖️ Weigh it') + '</button></div>';
    }
    function paint(flash) {
      if (st.i >= C.rounds.length) {
        stage.innerHTML = '<div class="fs-cal-done">✅ Three changes weighed.</div>'; drawLog();
        askOnce(qh, C.q, C.opts, 'callit-q', win, C.win, C.clue, 'callit', miss); return;
      }
      var r = R();
      stage.innerHTML = '<div class="fs-cal-thing"><span class="fs-cal-ic">' + r.icon + '</span><b>' + esc(phase === 'start' ? r.t : r.after) + '</b></div>' +
        '<div class="fs-cal-read' + (flash ? ' flash' : '') + '">' + r.mass + ' <small>' + (C.unit || 'g') + '</small></div>' +
        '<div class="fs-cal-sub">' + esc((C.startLine || 'On the scale now: {n}').replace('{n}', r.mass + ' ' + (C.unit || 'g'))) + '</div>' +
        (phase === 'start' ? '<button type="button" class="fs-btn fs-cal-do">' + esc(r.btn) + '</button>' :
          '<div class="fs-hs-card fs-cal-line"><span class="fs-hs-n">👀</span><div>' + esc(r.line) + '</div></div>' + pad());
      drawLog();
      var go = $('.fs-cal-do', stage); if (go) go.addEventListener('click', function () { ac(); SFX.pop(); phase = 'changed'; typed = ''; paint(); });
      $$('.fs-cal-key', stage).forEach(function (k) { k.addEventListener('click', function () {
        var v = k.dataset.k; SFX.blip();
        if (v === '⌫') typed = typed.slice(0, -1); else if (v === '✓') return weigh(); else if (typed.length < 4) typed += v;
        $('.fs-cal-disp', stage).innerHTML = (typed || '—') + ' <small>' + (C.unit || 'g') + '</small>';
      }); });
      var w = $('.fs-cal-weigh', stage); if (w) w.addEventListener('click', weigh);
    }
    function weigh() {
      var r = R(), n = parseInt(typed, 10);
      if (!typed) { bounce($('.fs-cal-disp', stage), miss, C.needLine || 'Type the number you expect first.'); return; }
      if (n !== r.mass) { bounce($('.fs-cal-disp', stage), miss, n > r.mass ? (C.overLine || 'Look again.') : (C.underLine || 'Look again.')); typed = ''; $('.fs-cal-disp', stage).innerHTML = '— <small>' + (C.unit || 'g') + '</small>'; return; }
      ac(); SFX.chime(); miss.classList.remove('show');
      st.done.push({ icon: r.icon, t: r.t, m: r.mass, same: r.same }); st.i++; saveJ('callit', st); phase = 'start'; typed = '';
      paint(true);
      if (st.i < C.rounds.length) { var c = el('div', 'fs-hs-card fs-cal-hit flash', '<span class="fs-hs-n">🎯</span><div>' + esc(C.hitLine || 'Called it!') + '</div>'); log.insertBefore(c, log.firstChild); }
    }
    paint(); placeAfter(g, at);
  }

  /* ---------- Part 2: "The UNDO button" — six changes, each with its own ↩ UNDO. Press it and watch: some come back, some are stuck that way. Then stamp each card.
     Every card shows the same material before AND after, which is the whole point (30.01) ----------
     D.undoer = {afterText, kicker, title, todo[], why, undoBtn, stampQ, stamps:[{k, icon, t}], cards:[{id, icon, t, from, to, k, line, mat}], miss:{k:hint}, matLine ({m}),
                 q, opts, win, clue}. Classes fs-und-*. */
  function buildUndoer() {
    var U = D.undoer; if (!U) return;
    var at = anchorP(U.afterText); if (!at) { FAILED.push('undoer anchor text not found'); return; }
    var g = gameShell(U.kicker || 'Part 2 game', U.title, U.todo, U.why); g.dataset.mod = 'undoer';
    var st = loadJ('undoer', { u: {}, s: {} });
    var stamps = el('div', 'fs-twn-tools fs-und-stamps'), grid = el('div', 'fs-und-grid'), count = el('div', 'fs-count'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    [stamps, grid, count, miss, qh, win].forEach(function (e) { g.appendChild(e); });
    function card(id) { return U.cards.filter(function (c) { return c.id === id; })[0]; }
    function paint() {
      stamps.innerHTML = '';
      U.stamps.forEach(function (s) {
        var b = el('button', 'fs-in-chip fs-dragc fs-und-stamp', '<span>' + s.icon + '</span> ' + esc(s.t)); b.type = 'button'; b.dataset.k = s.k; stamps.appendChild(b);
        dragDrop(b, function () { return $$('.fs-und-card', grid); }, function (it, t) { put(t.dataset.id, it.dataset.k); });
      });
      grid.innerHTML = U.cards.map(function (c) {
        var done = st.u[c.id], mark = st.s[c.id];
        return '<div class="fs-und-card' + (done ? ' undone' : '') + (mark ? ' stamped ' + mark : '') + '" data-id="' + c.id + '">' +
          '<div class="fs-und-t"><span>' + c.icon + '</span>' + esc(c.t) + '</div>' +
          '<div class="fs-und-pair"><span class="fs-und-a">' + c.from + '</span><em>→</em><span class="fs-und-b">' + c.to + '</span></div>' +
          (done ? '<div class="fs-und-line">' + esc(c.line) + '</div><div class="fs-und-mat">' + esc((U.matLine || 'Material: {m}.').replace('{m}', c.mat)) + '</div>' +
            (mark ? '<div class="fs-und-mark">' + esc((U.stamps.filter(function (s) { return s.k === mark; })[0] || {}).t || '') + '</div>' : '<div class="fs-und-ask">' + esc(U.stampQ || 'Now stamp it.') + '</div>')
            : '<button type="button" class="fs-btn fs-und-btn">' + esc(U.undoBtn || '↩ UNDO') + '</button>') + '</div>';
      }).join('');
      $$('.fs-und-card', grid).forEach(function (box) {
        var id = box.dataset.id, b = $('.fs-und-btn', box);
        if (b) b.addEventListener('click', function () { undo(id); });
        box.addEventListener('click', function () { var s = $('.fs-und-stamp.sel', stamps); if (s) { s.classList.remove('sel'); put(id, s.dataset.k); } });
      });
      var n = U.cards.filter(function (c) { return st.s[c.id]; }).length;
      count.textContent = '🗂 ' + n + ' of ' + U.cards.length + ' stamped'; count.classList.toggle('ok', n === U.cards.length);
      if (n === U.cards.length) askOnce(qh, U.q, U.opts, 'undoer-q', win, U.win, U.clue, 'undoer', miss);
    }
    function undo(id) {
      if (st.u[id]) return; var c = card(id); ac(); c.k === 'back' ? SFX.sparkle() : SFX.thud();
      var box = $('.fs-und-card[data-id="' + id + '"]', grid); if (box && !reduceMotion) box.classList.add(c.k === 'back' ? 'rewind' : 'shudder');
      setTimeout(function () { st.u[id] = 1; saveJ('undoer', st); paint(); }, reduceMotion ? 0 : 650);
    }
    function put(id, k) {
      var c = card(id); if (!c || st.s[id]) return;
      if (!st.u[id]) { bounce($('.fs-und-card[data-id="' + id + '"]', grid), miss, 'Press UNDO on that one first.'); return; }
      if (k !== c.k) { bounce($('.fs-und-card[data-id="' + id + '"]', grid), miss, (U.miss || {})[k] || 'Press UNDO again and watch what happens.'); return; }
      ac(); SFX.stamp(); miss.classList.remove('show'); st.s[id] = k; saveJ('undoer', st); paint();
    }
    paint(); placeAfter(g, at);
  }

  /* ---------- Part 3: "Where did the water go?" — a real before/after photo pair under a wipe slider, then a close-up photo with tap hotspots (30.01) ----------
     D.wipe = {afterText, kicker, title, todo[], why, before:{img, alt, cap}, after:{img, alt, cap}, hint, photo:{img, alt, hotspots:[{n, x, y, label, t}]}, credit, q, opts, win, clue?}.
     Classes fs-wp-*. */
  function buildWipe() {
    var W = D.wipe; if (!W) return;
    var at = anchorP(W.afterText); if (!at) { FAILED.push('wipe anchor text not found'); return; }
    var g = gameShell(W.kicker || 'Part 3 · real photos', W.title, W.todo, W.why); g.dataset.mod = 'wipe';
    var st = loadJ('wipe', { seen: {} });
    var box = el('div', 'fs-wp-box'), caps = el('div', 'fs-wp-caps'), ph = el('div', 'fs-wp-photo'), info = el('div', 'fs-hs-card fs-wp-info', '<em>Tap a number on the photo.</em>');
    var miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    [box, caps, ph, info, miss, qh, win].forEach(function (e) { g.appendChild(e); });
    box.innerHTML = '<img class="fs-wp-base" src="' + esc(W.after.img) + '" alt="' + esc(W.after.alt) + '" loading="lazy">' +
      '<div class="fs-wp-top"><img src="' + esc(W.before.img) + '" alt="' + esc(W.before.alt) + '" loading="lazy"></div>' +
      '<div class="fs-wp-handle" tabindex="0" role="slider" aria-label="Wipe between the two photos"><span>' + esc(W.hint || 'Drag me') + '</span></div>';
    caps.innerHTML = '<span>' + esc(W.before.cap) + '</span><span>' + esc(W.after.cap) + '</span>';
    var top = $('.fs-wp-top', box), handle = $('.fs-wp-handle', box), pct = 62;
    function setPct(p) { pct = Math.max(4, Math.min(96, p)); top.style.width = pct + '%'; handle.style.left = pct + '%'; }
    setPct(62);
    function fromX(x) { var r = box.getBoundingClientRect(); setPct(((x - r.left) / r.width) * 100); }
    var dragging = false;
    handle.addEventListener('pointerdown', function (e) { dragging = true; handle.setPointerCapture && handle.setPointerCapture(e.pointerId); handle.classList.add('on'); });
    handle.addEventListener('pointermove', function (e) { if (dragging) fromX(e.clientX); });
    handle.addEventListener('pointerup', function () { dragging = false; handle.classList.remove('on'); });
    handle.addEventListener('pointercancel', function () { dragging = false; });
    handle.addEventListener('keydown', function (e) { if (e.key === 'ArrowLeft') setPct(pct - 6); if (e.key === 'ArrowRight') setPct(pct + 6); });
    box.addEventListener('click', function (e) { if (e.target !== handle && !handle.contains(e.target)) fromX(e.clientX); });
    ph.innerHTML = '<div class="fs-wp-pic"><img src="' + esc(W.photo.img) + '" alt="' + esc(W.photo.alt) + '" loading="lazy">' +
      W.photo.hotspots.map(function (h, i) { return '<button type="button" class="fs-hs' + (st.seen[i] ? ' seen' : '') + '" style="left:' + h.x + '%;top:' + h.y + '%" data-i="' + i + '">' + h.n + '</button>'; }).join('') + '</div>';
    if (W.credit) g.appendChild(el('details', 'fs-credit fs-credit-fold', '<summary>📷 Photo credit</summary>' + esc(W.credit)));
    $$('.fs-hs', ph).forEach(function (b) { b.addEventListener('click', function () {
      var h = W.photo.hotspots[+b.dataset.i]; st.seen[b.dataset.i] = 1; saveJ('wipe', st); b.classList.add('seen'); SFX.chime();
      info.innerHTML = '<span class="fs-hs-n">' + h.n + '</span><div><b>' + esc(h.label) + '</b>' + esc(h.t) + '</div>';
      info.classList.remove('flash'); void info.offsetWidth; info.classList.add('flash');
      if (W.photo.hotspots.every(function (x, i) { return st.seen[i]; })) askOnce(qh, W.q, W.opts, 'wipe-q', win, W.win, W.clue, 'wipe', miss);
    }); });
    if (W.photo.hotspots.every(function (x, i) { return st.seen[i]; })) askOnce(qh, W.q, W.opts, 'wipe-q', win, W.win, W.clue, 'wipe', miss);
    placeAfter(g, at);
  }

  /* ---------- Part 4: "The state dial" — drag a dial (or tap a stop) from the freezer to the stovetop and back. The jar is sealed, so the mass readout and the
     material readout never move, whatever state the water is in (30.01) ----------
     D.statedial = {afterText, kicker, title, todo[], why, jarLabel, massLabel, mass, unit, matLabel, matValue, matNote, stops:[{k, t, sub, state, icon, line}],
                    needUp, needDown, backLine, q, opts, win, clue}. Classes fs-std-*. */
  function buildStatedial() {
    var S = D.statedial; if (!S) return;
    var at = anchorP(S.afterText); if (!at) { FAILED.push('statedial anchor text not found'); return; }
    var g = gameShell(S.kicker || 'Part 4 game', S.title, S.todo, S.why); g.dataset.mod = 'statedial';
    var st = loadJ('statedial', { i: 0, top: 0, back: 0 });
    var wrap = el('div', 'fs-std-wrap'), jar = el('div', 'fs-std-jar'), dial = el('div', 'fs-std-dial'), out = el('div', 'fs-std-out');
    var note = el('div', 'fs-hs-card fs-std-note'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    wrap.appendChild(dial); wrap.appendChild(jar);
    [wrap, out, note, miss, qh, win].forEach(function (e) { g.appendChild(e); });
    var last = S.stops.length - 1;
    function paint(moved) {
      var s = S.stops[st.i];
      dial.innerHTML = '<div class="fs-std-rail"><div class="fs-std-fill" style="height:' + (st.i / last * 100) + '%"></div>' +
        S.stops.map(function (p, i) { return '<button type="button" class="fs-std-stop' + (i === st.i ? ' on' : '') + '" data-i="' + i + '"><b>' + esc(p.t) + '</b><small>' + esc(p.sub) + '</small></button>'; }).reverse().join('') + '</div>';
      jar.innerHTML = '<div class="fs-std-glass s-' + s.k + (moved && !reduceMotion ? ' moved' : '') + '"><span class="fs-std-ic">' + s.icon + '</span></div><div class="fs-std-cap">' + esc(S.jarLabel || 'A sealed jar') + '</div>';
      out.innerHTML = '<div class="fs-std-o"><small>State</small><b>' + esc(s.state) + '</b></div>' +
        '<div class="fs-std-o lock"><small>' + esc(S.massLabel || 'Mass') + '</small><b>' + S.mass + ' ' + (S.unit || 'g') + '</b></div>' +
        '<div class="fs-std-o lock"><small>' + esc(S.matLabel || 'Material') + '</small><b>' + esc(S.matValue || 'WATER') + '</b><em>' + esc(S.matNote || '') + '</em></div>';
      note.innerHTML = '<span class="fs-hs-n">' + s.icon + '</span><div>' + esc(st.back ? S.backLine : s.line) + (st.top && !st.back ? ' <b>' + esc(S.needDown || '') + '</b>' : (!st.top ? ' <b>' + esc(S.needUp || '') + '</b>' : '')) + '</div>';
      $$('.fs-std-stop', dial).forEach(function (b) { b.addEventListener('click', function () { go(+b.dataset.i); }); });
      if (st.back) askOnce(qh, S.q, S.opts, 'statedial-q', win, S.win, S.clue, 'statedial', miss);
    }
    function go(i) {
      if (i === st.i) return; ac(); SFX.blip(); st.i = i;
      if (i === last) st.top = 1;
      if (st.top && i === 0) st.back = 1;
      saveJ('statedial', st); paint(true);
      if (st.back) SFX.sparkle();
    }
    var rail = null, drag = false;
    wrap.addEventListener('pointerdown', function (e) { rail = $('.fs-std-rail', dial); if (rail && e.target.closest && e.target.closest('.fs-std-rail') && !e.target.closest('.fs-std-stop')) drag = true; });
    wrap.addEventListener('pointermove', function (e) {
      if (!drag || !rail) return; var r = rail.getBoundingClientRect();
      var p = 1 - Math.max(0, Math.min(1, (e.clientY - r.top) / r.height));
      go(Math.round(p * last));
    });
    wrap.addEventListener('pointerup', function () { drag = false; });
    paint(); placeAfter(g, at);
  }

  /* ---------- Part 4, the wow: "One giant crayon" — press through melt, pour, cool. The scale reads the same at every step, so the slab the freight company
     called ruined turns into one usable crayon (30.01) ----------
     D.remelt = {afterText, kicker, title, todo[], why, massLabel, mass, unit, steps:[{k, icon, t, btn, line}], q, opts, win}. Classes fs-rmt-*. */
  function buildRemelt() {
    var R = D.remelt; if (!R) return;
    var at = anchorP(R.afterText); if (!at) { FAILED.push('remelt anchor text not found'); return; }
    var g = gameShell(R.kicker || 'Part 4 · the wow', R.title, R.todo, R.why); g.dataset.mod = 'remelt';
    var st = loadJ('remelt', { i: 0 });
    var strip = el('div', 'fs-rmt-strip'), stage = el('div', 'fs-rmt-stage'), miss = el('div', 'fs-miss'), qh = el('div'), win = el('div', 'fs-win');
    [strip, stage, miss, qh, win].forEach(function (e) { g.appendChild(e); });
    function paint(moved) {
      var s = R.steps[st.i];
      strip.innerHTML = R.steps.map(function (p, i) { return '<div class="fs-rmt-step' + (i < st.i ? ' done' : '') + (i === st.i ? ' on' : '') + '"><span>' + p.icon + '</span><small>' + esc(p.t) + '</small></div>'; }).join('');
      stage.innerHTML = '<div class="fs-rmt-art k-' + s.k + (moved && !reduceMotion ? ' moved' : '') + '"><span>' + s.icon + '</span></div>' +
        '<div class="fs-rmt-scale"><small>' + esc(R.massLabel || 'On the scale') + '</small><b>' + R.mass + ' ' + (R.unit || 'g') + '</b></div>' +
        '<div class="fs-hs-card fs-rmt-line"><span class="fs-hs-n">' + s.icon + '</span><div>' + esc(s.line) + '</div></div>' +
        (s.btn ? '<button type="button" class="fs-btn fs-rmt-go">' + esc(s.btn) + '</button>' : '');
      var b = $('.fs-rmt-go', stage); if (b) b.addEventListener('click', function () {
        ac(); st.i++; saveJ('remelt', st); st.i === R.steps.length - 1 ? SFX.sparkle() : SFX.whoosh(); paint(true);
      });
      if (st.i === R.steps.length - 1) askOnce(qh, R.q, R.opts, 'remelt-q', win, R.win, R.clue, 'remelt', miss);
    }
    paint(); placeAfter(g, at);
  }

  /* ---------- after the solve: "Stamp the claim" — pick the two pieces of evidence that settle the freight claim, then stamp the form yourself (30.01) ----------
     D.claimstamp = {afterSolve, after, lockLine, kicker, title, todo[], why, formHead, pickQ, need, chips:[{id, t, ok, miss}], stampQ, stamps:[{k, icon, t}], answer,
                     missStamp, win}. Classes fs-cst-*. */
  function buildClaimstamp() {
    var K = D.claimstamp; if (!K) return;
    var g = gameShell(K.kicker || 'Case closed', K.title, K.todo, K.why); g.dataset.mod = 'claimstamp';
    var ok = afterSolve(g, K.after, K.lockLine, function (body) {
      var st = loadJ('claimstamp', { picked: [], stamp: '' });
      var chips = el('div', 'fs-cst-chips'), form = el('div', 'fs-cst-form'), stamps = el('div', 'fs-twn-tools fs-cst-stamps'), miss = el('div', 'fs-miss'), win = el('div', 'fs-win');
      body.appendChild(el('div', 'fs-in-k', esc(K.pickQ || 'Pick your evidence.')));
      [chips, form, stamps, miss, win].forEach(function (e) { body.appendChild(e); });
      function paint() {
        chips.innerHTML = K.chips.map(function (c) { return '<button type="button" class="fs-in-chip fs-cst-chip' + (st.picked.indexOf(c.id) > -1 ? ' on ok' : '') + '" data-id="' + c.id + '">' + esc(c.t) + '</button>'; }).join('');
        $$('.fs-cst-chip', chips).forEach(function (b) { b.addEventListener('click', function () {
          var c = K.chips.filter(function (x) { return x.id === b.dataset.id; })[0];
          if (st.picked.indexOf(c.id) > -1 || st.stamp) return;
          if (!c.ok) { bounce(b, miss, c.miss); return; }
          if (st.picked.length >= (K.need || 2)) return;
          SFX.pop(); miss.classList.remove('show'); st.picked.push(c.id); saveJ('claimstamp', st); paint();
        }); });
        var full = st.picked.length >= (K.need || 2);
        form.innerHTML = '<div class="fs-cfm fs-cst-copy' + (st.stamp ? ' settled' : '') + '"><div class="fs-cfm-h"><span>' + esc(K.formHead || 'DAMAGE CLAIM') + '</span></div>' +
          '<dl class="fs-cfm-rows">' + st.picked.map(function (id, i) { var c = K.chips.filter(function (x) { return x.id === id; })[0]; return '<dt>Evidence ' + (i + 1) + '</dt><dd>' + esc(c.t) + '</dd>'; }).join('') +
          (full ? '' : '<dt>Evidence</dt><dd class="fs-cst-blank">waiting…</dd>') + '</dl>' +
          (st.stamp ? '<div class="fs-cfm-stamp ' + st.stamp + '">' + esc((K.stamps.filter(function (s) { return s.k === st.stamp; })[0] || {}).t || '') + '</div>' : '') + '</div>';
        stamps.innerHTML = full && !st.stamp ? '<div class="fs-in-k">' + esc(K.stampQ || 'Now stamp it.') + '</div>' +
          K.stamps.map(function (s) { return '<button type="button" class="fs-in-chip fs-cst-stamp" data-k="' + s.k + '"><span>' + s.icon + '</span> ' + esc(s.t) + '</button>'; }).join('') : '';
        $$('.fs-cst-stamp', stamps).forEach(function (b) { b.addEventListener('click', function () {
          if (b.dataset.k !== K.answer) { bounce(b, miss, K.missStamp || 'Look at your evidence again.'); return; }
          ac(); SFX.stamp(); miss.classList.remove('show'); st.stamp = b.dataset.k; saveJ('claimstamp', st); paint();
          winOnce(win, K.win, 'claimstamp', 'claimstamp');
        }); });
        if (st.stamp) winOnce(win, K.win, 'claimstamp', 'claimstamp');
      }
      paint();
    });
    if (!ok) FAILED.push('claimstamp: no solve box');
  }

  /* ---------- Tool of the Week: "Evaporating dish" — pour a liquid into the dish, warm it, and the water leaves as vapor. Weigh whatever is left behind (30.01).
     T.evapdish = {title, todo[], model, liquids:[{k, icon, t, grams, left, res}], onBtn, waitLine, weighBtn, q:{q, opts:[{t, ok, why}]}} ---------- */
  SIMS.evapdish = function (host, T) {
    var M = T.evapdish, st = loadJ('evapdish', { done: {} });
    host.innerHTML = '<div class="fs-game-k">' + esc(M.kicker || 'Try it: the evaporating dish') + '</div><div class="fs-game-t">' + esc(M.title) + '</div>' +
      '<ul class="fs-todo">' + M.todo.map(function (t) { return '<li>' + esc(t) + '</li>'; }).join('') + '</ul>' +
      '<div class="fs-twn-tools fs-evd-liq"></div><div class="fs-evd-bench"></div><div class="fs-evd-out"></div><div class="fs-evd-q"></div><div class="fs-miss fs-evd-miss"></div><div class="fs-win fs-evd-win"></div>' +
      '<p class="fs-pbal-model">' + esc(M.model) + '</p>';
    var liq = $('.fs-evd-liq', host), bench = $('.fs-evd-bench', host), out = $('.fs-evd-out', host), cur = null, phase = 'pick';
    function paintLiq() {
      liq.innerHTML = M.liquids.map(function (l) { return '<button type="button" class="fs-in-chip' + (cur === l.k ? ' on' : '') + (st.done[l.k] ? ' done' : '') + '" data-k="' + l.k + '"><span>' + l.icon + '</span> ' + esc(l.t) + (st.done[l.k] ? ' ✓' : '') + '</button>'; }).join('');
      $$('.fs-in-chip', liq).forEach(function (b) { b.addEventListener('click', function () { cur = b.dataset.k; phase = 'poured'; SFX.blip(); paint(); }); });
    }
    function L() { return M.liquids.filter(function (l) { return l.k === cur; })[0]; }
    function paint() {
      paintLiq();
      if (!cur) { bench.innerHTML = '<div class="fs-evd-dish empty"><em>Pick a liquid to pour in.</em></div>'; out.innerHTML = ''; return; }
      var l = L();
      bench.innerHTML = '<div class="fs-evd-dish ' + phase + '"><div class="fs-evd-liquid"></div><div class="fs-evd-left">' + (phase === 'dry' || phase === 'weighed' ? '✨' : '') + '</div></div>' +
        '<div class="fs-evd-warmer' + (phase === 'warm' || phase === 'dry' || phase === 'weighed' ? ' on' : '') + '">🔥</div>' +
        (phase === 'poured' ? '<button type="button" class="fs-btn fs-evd-go">' + esc(M.onBtn || '🔥 Warm it') + '</button>' : '') +
        (phase === 'dry' ? '<button type="button" class="fs-btn fs-evd-weigh">' + esc(M.weighBtn || '⚖️ Weigh what is left') + '</button>' : '');
      if (phase === 'warm') out.innerHTML = '<div class="fs-hs-card"><span class="fs-hs-n">♨️</span><div>' + esc(M.waitLine || 'The water is leaving as vapor…') + '</div></div>';
      if (phase === 'dry') out.innerHTML = '<div class="fs-hs-card"><span class="fs-hs-n">🍽️</span><div>In the dish: ' + esc(l.left) + '.</div></div>';
      if (phase === 'weighed') out.innerHTML = '<div class="fs-hs-card flash"><span class="fs-hs-n">⚖️</span><div><b>' + l.grams + ' g.</b> ' + esc(l.res) + '</div></div>';
      var go = $('.fs-evd-go', bench); if (go) go.addEventListener('click', function () {
        ac(); SFX.whoosh(); phase = 'warm'; paint(); setTimeout(function () { phase = 'dry'; paint(); }, reduceMotion ? 0 : 1200);
      });
      var w = $('.fs-evd-weigh', bench); if (w) w.addEventListener('click', function () {
        ac(); SFX.chime(); phase = 'weighed'; st.done[cur] = 1; saveJ('evapdish', st); paint();
        if (M.liquids.every(function (x) { return st.done[x.k]; })) ask();
      });
    }
    function ask() {
      var q = $('.fs-evd-q', host); if (q.dataset.on) return; q.dataset.on = '1';
      q.innerHTML = '<div class="fs-in-k">' + esc(M.q.q) + '</div><div class="fs-in-chips">' + M.q.opts.map(function (o, i) { return '<button type="button" class="fs-in-chip" data-i="' + i + '">' + esc(o.t) + '</button>'; }).join('') + '</div>';
      $$('.fs-in-chip', q).forEach(function (c) { c.addEventListener('click', function () {
        var o = M.q.opts[+c.dataset.i];
        if (!o.ok) { bounce(c, $('.fs-evd-miss', host), o.why); return; }
        $('.fs-evd-miss', host).classList.remove('show'); c.classList.add('on', 'ok');
        var w = $('.fs-evd-win', host); w.innerHTML = esc(o.why); w.classList.add('show'); SFX.win(); toolDone();
      }); });
    }
    paint();
    if (M.liquids.every(function (x) { return st.done[x.k]; })) ask();
  };

