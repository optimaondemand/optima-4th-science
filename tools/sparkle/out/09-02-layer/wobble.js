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

