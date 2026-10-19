#!/usr/bin/env python3
"""Review & Lab day page generator (G4 Science).  Used by tools/sparkle/lessons/r<U>-<D>/make_page.py

A review day has no older lesson to sparkle, so its plain page (original.html) is written from a small content
dict, in the lean lesson shape (Warm-Up · The Lesson · Self-Check · Assignment), on the same page shell, CSS and
scripts as the unit's lessons (taken from a donor lesson). build_lesson.py r<U>-<D> then adds the sparkle layer.
Python 3 standard library only."""
import html, os, re, glob

def esc(t): return html.escape(str(t), quote=True)

def donor_html(donor):
    """The donor lesson's untouched page: its saved original.html once it is sparkled, else the live file."""
    W, L = donor.split('-')
    kit = os.path.join('tools', 'sparkle', 'lessons', f'{int(W):02d}-{L}', 'original.html')
    if os.path.exists(kit): return open(kit, encoding='utf-8').read()
    f = glob.glob(f'lesson-{int(W)}-{L}-*.html')[0]
    s = open(f, encoding='utf-8').read()
    if 'id="fs-data"' in s: raise SystemExit('donor lesson is sparkled but has no original.html')
    return s

def render(C):
    src = donor_html(C['donor'])
    head = src[:src.index('</head>')]
    head = re.sub(r'<title>.*?</title>', '<title>Optima Academy Online – ' + esc(C['title']) + '</title>', head, count=1, flags=re.S)
    head = re.sub(r'<!--.*?-->', '', head, count=1, flags=re.S)  # the donor's long comment block (its own slot list)
    body = src[src.index('<body'):]
    readaloud = body[body.index('<div id="optima-read-aloud">'):body.index('<!-- ═══ END OPTIMA READ-ALOUD PLAYER ═══ -->')]
    tail_scripts = body[body.index('<canvas id="confettiCanvas"></canvas>'):]
    tail_scripts = tail_scripts.replace("var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
    tail_scripts = re.sub(r"lines\.push\('  Lesson [^']*'\);", "lines.push('  " + C['gatherTitle'].replace("'", "\\'") + "');", tail_scripts)
    tail_scripts = re.sub(r"a\.download = '[^']*';", "a.download = '" + C['file'].replace('.html', '.txt') + "';", tail_scripts)
    tail_scripts = tail_scripts.replace("style.width = '20%'", "style.width = '25%'").replace("textContent = '20%'", "textContent = '25%'")
    tail_scripts = tail_scripts.replace('raw.githubusercontent.com/bbirchum1/optima-4th-science', 'raw.githubusercontent.com/optimaondemand/optima-4th-science')
    tail_scripts = tail_scripts.replace("var _lessonKey = (document.title || 'science-lesson')", "var _lessonKey = ('" + C['key'] + "-' + (document.title || 'science-lesson'))")

    def ican(i, t):
        col = ['#E8636B', '#D4772C', '#34B76F'][i]
        mb = 'margin-bottom:10px;' if i < 2 else ''
        return (f'<div style="display:flex;align-items:flex-start;gap:12px;padding:12px 16px;background:#FAFAF6;border-radius:14px;{mb}border:1.5px solid #E8DDD2;">'
                f'<div style="width:34px;height:34px;border-radius:50%;background:{col};color:#fff;font-size:16px;font-weight:800;display:flex;align-items:center;justify-content:center;flex-shrink:0;">{i + 1}</div>'
                f'<div style="font-size:17px;color:#0E1C42;line-height:1.6;padding-top:4px;"><strong>I can</strong> {esc(t)}</div></div>')

    def flip(i, w):
        return (f'<div class="flip-card fc-color-{i + 1}" onclick="this.classList.toggle(\'flipped\')"><div class="flip-card-inner"><div class="flip-card-front"><div class="fc-emoji">{w["emoji"]}</div>'
                f'<div class="fc-word">{esc(w["w"])}</div><div class="fc-tap">tap to flip</div></div><div class="flip-card-back"><div class="fc-word-back">{esc(w["w"])}</div>'
                f'<div class="fc-def">{esc(w["def"])}</div><div class="fc-tap-back">tap to flip back</div></div></div></div>')

    def ps(items): return '\n'.join(p if p.lstrip().startswith('<') else f'      <p>{p}</p>' for p in items)

    def quiz(i, q):
        letters = 'ABC'
        opts = ''.join(f'<div class="quiz-opt" data-val="{letters[j]}" onclick="checkQuiz(this)"><span class="quiz-letter">{letters[j]}</span><span class="quiz-text">{esc(o)}</span></div>\n        ' for j, o in enumerate(q['opts']))
        return (f'      <div class="quiz-q" data-answer="{q["ans"]}">\n        <div class="quiz-q-num">Q{i + 1}</div>\n        <p class="quiz-q-text">{esc(q["q"])}</p>\n        {opts}'
                f'<div class="quiz-feedback fb-correct">{esc(q["right"])}</div>\n        <div class="quiz-feedback fb-wrong">{esc(q["wrong"])}</div>\n      </div>\n')

    def check(t, last=False):
        return (f'<div class="checklist-item" onclick="this.classList.toggle(\'checked\')" style="display:flex;align-items:flex-start;gap:10px;padding:10px 14px;background:#FAFAF6;border:1.5px solid #E8DDD2;border-radius:12px;margin-bottom:{16 if last else 8}px;cursor:pointer;transition:background .2s,border-color .2s;user-select:none;">'
                f'<span class="check-icon" style="font-size:20px;flex-shrink:0;width:28px;height:28px;display:flex;align-items:center;justify-content:center;border-radius:8px;border:2px solid #D0C8BE;background:#fff;transition:all .2s;">☐</span>'
                f'<span style="font-size:16px;color:#2B1D12;line-height:1.55;">{t}</span></div>')

    H3 = 'font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;'
    lesson_parts = ''
    for part in C['lesson']['parts']:
        lesson_parts += f'      <h3 style="{H3}">{esc(part["h"])}</h3>\n' + ps(part['paras']) + '\n'
        if part.get('stop'):
            lesson_parts += ('      <div class="socratic-q">\n        <span class="sq-icon">🛑</span>\n        <div>\n          <div class="label">Stop &amp; Think</div>\n'
                             f'          <div class="question">"{esc(part["stop"])}"</div>\n        </div>\n      </div>\n')
    A = C['assign']
    partb = ''
    for i, q in enumerate(A['partB']):
        partb += (f'      <div class="pq">\n        <span class="pq-num" style="background:#D4772C;">{i + 1}</span>\n        <span class="pq-text">{esc(q)}</span>\n      </div>\n'
                  f'      <textarea class="response-textarea" id="ans-{i + 1}" data-label="Part B · Question {i + 1}" placeholder="Type your answer here..." oninput="refreshGathered()"></textarea>\n\n')
    checks = ''.join(check(t, i == len(A['checklist']) - 1) for i, t in enumerate(A['checklist']))
    I = C['info']

    page = f'''{head}</head>
<body>
<div class="page-wrap">

<!-- ═══ OPTIMA READ-ALOUD PLAYER ═══ -->
{readaloud}<!-- ═══ END OPTIMA READ-ALOUD PLAYER ═══ -->

<!-- ═══ PROGRESS BAR ═══ -->
<div class="progress-wrap">
  <span class="progress-label">{C["icon"]} Lesson Progress</span>
  <div class="progress-track"><div class="progress-fill" id="progressFill"></div></div>
  <span class="progress-pct" id="progressPct">0%</span>
</div>

<!-- ═══ HEADER ═══ -->
<div class="header">
  <div class="header-brand">
    <div class="header-logo">
      <img src="https://raw.githubusercontent.com/optimaondemand/optima-assets/eeb0b335630058906d52f478028361d352253a93/images/Optima%20Final%20Circle%20-%20Owl%20Only.png" alt="Optima Academy" />
    </div>
    <div>
      <div class="header-org">Optima Academy Online</div>
      <div class="header-sub">An Education Experience Company</div>
    </div>
  </div>
  <div class="header-title">{esc(C["headerTitle"])}</div>
  <div class="header-badge">
    <span>{C["icon"]}</span>
    <span>{esc(C["badge"])}</span>
  </div>
</div>

<!-- ═══ HERO (the sparkle layer draws the banner here) ═══ -->
<div class="hero-visual"></div>

<!-- ═══ INFO STRIP ═══ -->
<div class="info-strip">
  <div class="info-item"><div class="info-icon" style="background:#FFF5E1;">📅</div><div><div class="info-label">Quarter / Week</div><div class="info-value">{esc(I["when"])}</div><div class="info-detail">{esc(I["whenDetail"])}</div></div></div>
  <div class="info-item"><div class="info-icon" style="background:#EEF8F0;">📖</div><div><div class="info-label">Review Day</div><div class="info-value">{esc(I["day"])}</div><div class="info-detail">{esc(I["dayDetail"])}</div></div></div>
  <div class="info-item"><div class="info-icon" style="background:#FFF5E1;">🧭</div><div><div class="info-label">Science Focus</div><div class="info-value">{esc(I["focus"])}</div><div class="info-detail">{esc(I["focusDetail"])}</div></div></div>
  <div class="info-item"><div class="info-icon" style="background:#EEF8F0;">🌿</div><div><div class="info-label">Standards</div><div class="info-value">{esc(I["std"])}</div><div class="info-detail">{esc(I["stdDetail"])}</div></div></div>
</div>

<!-- ═══ INTRO 2-COL ═══ -->
<div class="intro-2col">
  <div class="card theme-earth scroll-reveal">
    <div class="card-head"><div class="card-head-icon">❓</div><div><div class="card-head-label">Key Question</div><div class="card-head-title">Our Big Question for Today</div></div></div>
    <div class="card-body">
      <div class="socratic-q" style="margin-top:0;"><span class="sq-icon">🤔</span><div><div class="label">Think about this…</div><div class="question">"{esc(C["bigQ"])}"</div></div></div>
      <p>{C["bigQnote"]}</p>
    </div>
  </div>
  <div class="card theme-sky scroll-reveal">
    <div class="card-head"><div class="card-head-icon">🎯</div><div><div class="card-head-label">Objectives</div><div class="card-head-title">I Can Statements</div></div></div>
    <div class="card-body">
      {"".join(ican(i, t) for i, t in enumerate(C["ican"]))}
    </div>
  </div>
</div>

<div class="need-strip">
  <span class="need-strip-label">🎒 You'll need:</span>
  <span class="need-chip"><span>💻</span>Just this page</span>
</div>

<!-- ═══ TAB BAR ═══ -->
<div class="tab-bar" id="tabBar">
  <button class="tab-btn active" data-tab="vocab" onclick="switchTab('vocab')">📚 Vocabulary<span class="tab-check">✓</span></button>
  <button class="tab-btn" data-tab="lesson" onclick="switchTab('lesson')">📘 The Lesson<span class="tab-check">✓</span></button>
  <button class="tab-btn" data-tab="quiz" onclick="switchTab('quiz')">🧠 Self-Check<span class="tab-check">✓</span></button>
  <button class="tab-btn" data-tab="assignment" onclick="switchTab('assignment')">✍️ Assignment<span class="tab-check">✓</span></button>
</div>

<!-- ═══ TAB 1: WARM-UP + WORDS ═══ -->
<div class="tab-panel active" id="tab-vocab">
<div class="video-placeholder-wrap">
<!-- slot: {C["key"]}-intro -->
<div class="video-placeholder-inner">
  <span class="vp-icon">&#x1F3AC;</span>
  <div class="vp-label">Introduction Video</div>
  <div class="vp-title">Optima Academy Online – {esc(C["title"])}</div>
  <div class="vp-slot">{C["key"]}-intro</div>
  <div class="vp-notes"><strong>Teacher recording notes:</strong> Introduction video for this review day.</div>
</div>
</div>
  <div class="activity-card act-warmup scroll-reveal">
    <div class="act-head">
      <div class="act-num" style="background:#E8636B;">1</div>
      <div style="flex:1;"><div class="act-title">{esc(C["warm"]["title"])}</div><div class="act-subtitle">{esc(C["warm"]["subtitle"])}</div></div>
      <div class="act-time" style="background:#E8636B;">⏱ 5 min</div>
    </div>
    <div class="act-body">
{ps(C["warm"]["paras"])}
    </div>
  </div>

  <div class="card theme-rock scroll-reveal">
    <div class="card-head"><div class="card-head-icon">📚</div><div><div class="card-head-label">Word Wall</div><div class="card-head-title">Words You'll Use Today</div></div></div>
    <div class="card-body">
      <p>These six words show up all through today's review. <strong>Tap a card to flip it</strong> and read what the word means.</p>
      <div class="vocab-grid">
        {"".join(flip(i, w) for i, w in enumerate(C["words"]))}
      </div>
    </div>
  </div>

  <div class="tab-next-wrap"><button class="tab-next-btn" onclick="switchTab('lesson')">Continue to 📘 The Lesson →</button></div>
</div>

<!-- ═══ TAB 2: THE LESSON ═══ -->
<div class="tab-panel" id="tab-lesson">
  <div class="activity-card act-lesson scroll-reveal">
    <div class="act-head">
      <div class="act-num" style="background:#D4772C;">2</div>
      <div style="flex:1;"><div class="act-title">{esc(C["lesson"]["title"])}</div><div class="act-subtitle">{esc(C["lesson"]["subtitle"])}</div></div>
      <div class="act-time" style="background:#D4772C;">⏱ 15 min</div>
    </div>
    <div class="act-body">
{lesson_parts}
      <div class="tab-next-wrap"><button class="tab-next-btn" onclick="switchTab('quiz')">Continue to 🧠 Self-Check →</button></div>
    </div>
  </div>
</div>

<!-- ═══ TAB 3: SELF-CHECK ═══ -->
<div class="tab-panel" id="tab-quiz">
  <div class="quiz-card scroll-reveal">
    <div style="display:flex;align-items:center;gap:12px;padding:16px 22px;background:linear-gradient(135deg,#FFF6E5,#FFEEC8);border-bottom:2px solid #F0DCC4;">
      <div style="font-size:28px;">🧠</div>
      <div><div style="font-size:11px;color:#9A6E10;text-transform:uppercase;letter-spacing:0.8px;font-weight:800;">Quick Self-Check</div><div style="font-size:22px;color:#0E1C42;font-weight:900;">Not graded — just for you!</div></div>
    </div>
    <div style="padding:20px 22px;">
{"".join(quiz(i, q) for i, q in enumerate(C["quiz"]))}
      <div id="quizScore" class="quiz-score">
        <div class="quiz-score-num"><span id="quizScoreNum">0</span>/3</div>
        <div id="quizScoreMsg" class="quiz-score-msg"></div>
        <div id="quizVideoCorrect" class="video-feedback" style="margin-top:18px;"></div>
        <div id="quizVideoReview" class="video-feedback" style="margin-top:18px;"></div>
      </div>
    </div>
  </div>
  <div class="tab-next-wrap"><button class="tab-next-btn" onclick="switchTab('assignment')">Continue to ✍️ Assignment →</button></div>
</div>

<!-- ═══ TAB 4: ASSIGNMENT ═══ -->
<div class="tab-panel" id="tab-assignment">
  <div class="activity-card act-practice scroll-reveal">
    <div class="act-head">
      <div class="act-num" style="background:#34B76F;">4</div>
      <div style="flex:1;"><div class="act-title">{esc(A["title"])}</div><div class="act-subtitle">{esc(A["subtitle"])}</div></div>
      <div class="act-time" style="background:#34B76F;">⏱ 12 min</div>
    </div>
    <div class="act-body">
      <p style="font-size:18px;color:#0E1C42;font-weight:800;margin-bottom:6px;">🌿 Part B &mdash; Short Answer</p>
      <p style="font-size:15px;color:#9A8E82;margin-bottom:14px;">Answer in <strong>complete sentences</strong>. Use words from the Word Wall.</p>
{partb}
      <p style="font-size:18px;color:#0E1C42;font-weight:800;margin-bottom:6px;margin-top:20px;">🧭 Part C &mdash; {esc(A["partC"]["title"])}</p>
      <p style="font-size:15px;color:#5A4D3E;margin-bottom:14px;">{A["partC"]["intro"]}</p>

      <div style="background:#FAF7F3;border:2px solid #8B6FC0;border-radius:16px;padding:22px 24px;margin-bottom:20px;">
        <div style="font-size:12px;color:#8B6FC0;text-transform:uppercase;letter-spacing:1px;font-weight:800;margin-bottom:8px;">✏️ Use Your Evidence</div>
        <p style="font-size:17px;color:#0E1C42;font-weight:700;margin-bottom:8px;">{A["cer"]["prompt"]}</p>
        <p style="font-size:16px;color:#2B1D12;margin-bottom:12px;">{A["cer"]["ask"]}</p>
        <textarea class="response-textarea ta-lg" id="cer-4" data-label="Use Your Evidence (CER)" placeholder="Type your answer here..." oninput="refreshGathered()"></textarea>
      </div>

  <!-- OAO-GATHERED-CARD v1 -->
  <div class="gathered-card">
    <div class="gathered-header"><div class="gathered-header-icon">📋</div><div><div class="gathered-header-label">{esc(C["badge"])}</div><div class="gathered-header-title">Gathered Answers</div></div></div>
    <div class="gathered-body">
      <div class="gathered-intro">All your answers in one place. Copy them or download them to turn in on Canvas.</div>
      <div class="gathered-name-row"><span class="gathered-name-label">Your name:</span><input type="text" class="gathered-name-input" id="student-name" placeholder="Type your name here" oninput="refreshGathered()" /></div>
      <textarea class="gathered-output" id="gatheredOutput" readonly></textarea>
      <div class="gathered-actions"><button class="gathered-btn" onclick="copyGathered()">📋 Copy to Clipboard</button><button class="gathered-btn gathered-btn-download" onclick="downloadGathered()">⬇ Download as Text</button></div>
      <div class="gathered-copied" id="copiedMsg">Copied! Paste into your Canvas text box to turn in.</div>
    </div>
  </div>

      <div style="background:#fff;border:2px solid #8B6FC0;border-radius:18px;margin-top:20px;overflow:hidden;">
        <div style="display:flex;align-items:center;gap:10px;padding:14px 20px;background:linear-gradient(135deg,#F0EDF6,#E8E2F2);border-bottom:2px solid #D8D0E8;">
          <div style="width:42px;height:42px;border-radius:50%;background:#8B6FC0;color:#fff;font-size:22px;display:flex;align-items:center;justify-content:center;flex-shrink:0;">☀️</div>
          <div><div style="font-size:10px;color:#9A8E82;text-transform:uppercase;letter-spacing:0.8px;font-weight:700;">Submission Checklist</div><div style="font-size:20px;color:#0E1C42;font-weight:800;line-height:1.2;">What to Turn In</div></div>
        </div>
        <div style="padding:18px 22px;">
          <p style="font-size:16px;color:#5A4D3E;line-height:1.65;margin-bottom:14px;">Check each box when that part is done.</p>
          {checks}
          <div style="background:#FFF7EE;border:2px solid #F0DCC4;border-radius:14px;padding:14px 18px;">
            <div style="font-size:13px;color:#C7922C;text-transform:uppercase;letter-spacing:0.5px;font-weight:800;margin-bottom:8px;">📎 How to Turn It In</div>
            <div style="font-size:15px;color:#2B1D12;line-height:1.7;">{A["submit"]}</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="card theme-earth scroll-reveal">
    <div class="card-head"><div class="card-head-icon">🔄</div><div><div class="card-head-label">Circle Back</div><div class="card-head-title">Back to the Big Question</div></div></div>
    <div class="card-body">
      <div class="socratic-q" style="margin-top:0;"><span class="sq-icon">🤔</span><div><div class="label">Now You Know!</div><div class="question">"{esc(C["bigQ"])}"</div></div></div>
      <div class="callout callout-tip"><span class="callout-icon">⭐</span><p>{C["circleTip"]}</p></div>
    </div>
  </div>
</div>

<!-- ═══ FOOTER ═══ -->
<div class="footer">
  <div class="footer-line1"><span>Optima Academy Online</span> &middot; Science &middot; {esc(I["quarter"])} &middot; Student Lesson Page</div>
  <div class="footer-line2">{esc(C["footer"])}</div>
  <div class="footer-line3">&copy; Optima Academy Online &middot; An Education Experience Company</div>
</div>

</div><!-- end page-wrap -->

<button class="back-to-top" id="backToTop" onclick="window.scrollTo({{top:0,behavior:'smooth'}})" title="Back to top"><span style="font-size:20px;">{C["icon"]}</span> Back to Top</button>
{tail_scripts}'''
    return page

def write(C, here):
    page = render(C)
    if page.count('<div') != page.count('</div>'): raise SystemExit(f'div mismatch {page.count("<div")} / {page.count("</div>")}')
    open(os.path.join(here, 'original.html'), 'w', encoding='utf-8', newline='').write(page)
    if not os.path.exists(C['file']):  # first time: the page itself, so build_lesson.py has a file to rebuild in place
        open(C['file'], 'w', encoding='utf-8', newline='').write(page)
    print('wrote', os.path.join(here, 'original.html'), len(page) // 1024, 'KB')
