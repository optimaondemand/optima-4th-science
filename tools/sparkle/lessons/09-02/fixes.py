#!/usr/bin/env python3
"""Writes fixes.json for 9.02. Each 'old' must match exactly once in original.html (build_lesson.py checks)."""
import json
F = []
def fix(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'

# ---------- repair: the stray </div> after the intro-video slot (build_lesson.py's repair looks for "09-02-intro"; this lesson's slot is "9-02-intro") ----------
fix('fix', 'repair: the stray </div> after the intro-video slot',
    r'(?<=</div>\n</div>\n)\s*</div>(?=\s*<div class="activity-card act-warmup)', '\n', regex=True)

# ---------- fix: Bethany ticked all four (19 Oct 2026) ----------
fix('fix', 'supply list: no notebook or colored pencils needed (answers are typed on the page)',
    r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>\s*<span class="need-chip"><span>✏️</span>Colored pencils</span>', '', regex=True)
fix('fix', 'supply list: “a sunny window” is a copy-paste leftover from 9.01',
    r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', regex=True)
fix('fix', 'the food web picture has arrows that point the wrong way (and shows a frog the text never draws in); removed. The hawk photo and the missing-link test show the web instead',
    r'\s*<div class="lesson-figure scroll-reveal">\s*<div class="lesson-figure-label">🕸️ Florida Wetland Food Web</div>.*?<div class="lesson-figure-caption">.*?</div>\s*</div>', '', regex=True)
fix('fix', 'Part C was copy-pasted from 9.01 (one producer, two consumers, no missing link); now matches the checklist: three consumers, remove one, predict',
    r"In your science notebook, draw a <strong>new</strong> food chain — different from the one in the lesson\. It can be from a Florida beach, a backyard, a pond, or a pine forest\. Include: <strong>the Sun · one producer · two consumers · labeled energy arrows between each</strong>\.</p>\s*<p[^>]*>Use colors\. Label every part\.</p>",
    "Pick a Florida food chain with one producer and <strong>three consumers</strong>. It can be from a beach, a backyard, a pond, or a pine forest. Then remove one link and predict what happens to the living thing it ate and the living thing that ate it.</p>", regex=True)
fix('fix', 'Part C checklist matches the new Part C (typed on the page; the sketch is a bonus)',
    'A food chain with at least three consumers, plus a second sketch showing what changes when one is removed.',
    'A Florida food chain with three consumers, one link removed, and what happens to the others.')
fix('fix', 'next-lesson teaser: 9.03 is a review day and 10.01 is about a fallen oak, not the gopher tortoise',
    r"(?<=back up your prediction with evidence)\. Next lesson, we'll zoom out to entire ecosystems and the role of the gopher tortoise as a Florida keystone species\.</p>",
    '. Coming up: a giant oak falls in a storm, and the whole forest around it changes.</p>', regex=True)
fix('plain', 'dash removed from the closing line', ' disappears — and back up your prediction with evidence', ' disappears, and back up your prediction with evidence')

# ---------- plain language ----------
fix('plain', 'shorter',
    "Hold this question in your head as you work. By the end of the lesson, you'll be able to use evidence to predict what happens when a producer or a consumer is missing from a Florida food chain.",
    "Keep this question in mind as you work. By the end, you’ll be able to use evidence to predict what happens when a producer or a consumer goes missing from a Florida food chain.")
fix('plain', 'cut filler',
    "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
    "You’ll use these six words all lesson. <strong>Tap a card to flip it</strong> and read what the word means.")
fix('plain', 'the warm-up is now the More or fewer? game (no drawing in a notebook)',
    r"<p>In your science notebook, draw three living things in a row.*?</p>\s*<p>Now imagine the middle one suddenly disappears\..*?</p>",
    "<p>Picture a food chain, like <em>grass → rabbit → fox</em>. Now one link suddenly disappears. Will the others have more, or fewer? Make some predictions before we test them in a real Florida marsh.</p>", regex=True)
fix('plain', 'clearer subtitle', 'Make a prediction before we test it', 'More or fewer? Predict first')
fix('plain', 'dash removed', 'removing one link doesn\'t always wipe out an ecosystem — animals can sometimes switch', 'removing one link doesn\'t always wipe out an ecosystem (a place where living things and their surroundings work together). Animals can sometimes switch')
fix('plain', 'dash removed; shorter',
    "Without predators, the prey usually grows quickly <em>at first</em> — then runs out of food and crashes. The system corrects itself, but not gently.",
    "Without predators, the prey usually grows quickly <em>at first</em>. Then it runs out of food and crashes.")
fix('plain', 'dash removed from the quote (same meaning)',
    'Who do you think is hit first — the sawgrass, the frogs, or the hawks?', 'Who do you think is hit first: the sawgrass, the frogs, or the hawks?')

fix('plain', '“dependencies” is a hard word', "It's a chain of <strong>dependencies</strong>.", "It's a chain of living things that <strong>depend</strong> on each other.")
fix('plain', '“misconception” is a hard word', '<strong>Common misconception:</strong> Some people think', '<strong>A common mix-up:</strong> Some people think')

# ---------- lean cuts (standing approval) ----------
fix('cut', 'lean: the Key Concept box repeats Part 2', r'<div style="background:#FFF6E5;border:2.5px solid #F0C97A;[^"]*">\s*<div[^>]*>⭐ Key Concept</div>\s*<p[^>]*>.*?</p>\s*</div>\s*', '', regex=True)
fix('cut', 'lean: one thinking stop per tab (Stop & Think in Part 1 stays)',
    r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', regex=True)
fix('cut', 'lean: the tap diagram becomes the Part 3 missing-link test',
    H3 + 'What If a Link is Missing?</h3>', H3 + 'Part 3 · What If a Link Is Missing?</h3>')
fix('cut', 'lean: Observe & Reason, the Yellowstone fact, the python callout and Go Deeper; Part 4 tests the volunteer’s note; next button goes to Self-Check',
    r'<div class="socratic-q">\s*<span class="sq-icon">👀</span>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
    H3 + 'Part 4 · Test the Volunteer’s Note</h3>\n'
    '      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">The volunteer made three predictions about the marsh with no frogs. A prediction is <strong>supported</strong> when the evidence agrees with it. Use what you saw in the hawk photo and the missing-link test to stamp each one.</p>\n'
    '      <div class="diagram-wrap" id="fs-vd-anchor"></div>\n'
    '      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', regex=True)
fix('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', regex=True)
fix('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fix('cut', 'lean: remove the whole Explore tab (testing the volunteer’s note is Lesson Part 4)',
    r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', regex=True)
fix('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', regex=True)
fix('cut', 'lean: Part B question 5 removed (Bethany kept 6 and 7; the diagram it asked about is gone)',
    r'<div class="pq">\s*<span class="pq-num"[^>]*>5</span>.*?</textarea>\s*', '', regex=True)
fix('cut', 'lean: Part B question 6 is now number 5', '<span class="pq-num" style="background:#D4772C;">6</span>', '<span class="pq-num" style="background:#D4772C;">5</span>')
fix('cut', 'lean: Part B question 7 is now number 6', '<span class="pq-num" style="background:#D4772C;">7</span>', '<span class="pq-num" style="background:#D4772C;">6</span>')
fix('cut', 'lean: no Reflect (it asked about 9.01’s hawk energy question)',
    r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', regex=True)
fix('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', regex=True)
fix('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fix('cut', 'lean: no separate Big Question answer',
    r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', regex=True)
fix('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', regex=True)
fix('plain', 'lean: shorter checklist',
    '<strong>Evidence Response:</strong> I made a claim about what happens when a predator disappears, and supported it with two pieces of evidence.',
    '<strong>CER:</strong> My claim, two pieces of evidence, and my reasoning.')
fix('cut', 'lean: answers are typed on the page, so one way to turn in (drops the photo and video options)',
    r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', regex=True)
fix('plain', 'dash removed from the quote (same meaning)',
    'the prey will just keep growing forever and the ecosystem will be fine.', 'the prey will just keep growing forever, and the ecosystem will be fine.')
fix('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
    "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
    "Do you agree or disagree? Prove it with at least <strong>two pieces of evidence</strong> from today’s lesson.")
fix('plain', 'shorter',
    'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.',
    'All your written answers in one place, so you can copy or download them to turn in on Canvas.')

json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(F), 'fixes written')
