#!/usr/bin/env python3
"""Writes data.json and fixes.json for 25.01 (run from this folder). Case 25 "The Lost Time Capsule" (Sam Park, Palmetto Beach, the morning
after the lighted boat parade): Teo buried the parade time capsule and wrote "Start at the rowboat. Walk 5 steps. Dig!" Nobody can find it.
New: case.tmap (a hand-drawn treasure map + a sticky note), the shared beach map + direction cards, trainwin (Warm-Up: which train moved?),
findit (Part 1: tap the square a position clue names; the rowboat clue fails), helper (Part 2: program Scoot the delivery robot), ferris (the
wow: a real long-exposure Ferris wheel photo), diagram (Part 3 = the old Explore: build a motion diagram from a replay), redirect + nightrun
(after the case; nightrun is folded), SIMS.compass (Tool of the Week).
SCRIPTS ONLY (week 25 on): every clip script is written and budgeted, nothing is generated. cueWords stays empty and lensVoice is off."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../18-01/data.json', encoding='utf-8'))
O = json.load(open('../24-02/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
PS = '<p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)
def I(n): return 'images/25-01-' + n + '.jpg'

# ---------------------------------------------------------------- labels (standing approval)
fx('fix', 'unit label: “Ecosystems & Energy” is a leftover; the plan puts Module 25 in “Energy, Motion, and Waves”', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Energy, Motion &amp; Waves</div>')
fx('fix', 'motion is physical science, not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standards label: the plan’s CPALMS code; TEKS is a Texas code that isn’t in the plan', '<div class="info-value">SC.4.P.12.1 · TEKS 4.7(A), 4.7(B)</div>', '<div class="info-value">SC.4.P.12.1</div>')
fx('fix', 'ticked: gravity and friction are not in the plan row, so the header no longer names them', '<div class="info-detail">NGSS 4-PS3-1 · Gravity & Friction</div>', '<div class="info-detail">NGSS 4-PS3-1 (support)</div>')

# ---------------------------------------------------------------- ticked fixes (Bethany, 22 Nov 2026)
# 22.01 leftovers in the Warm-Up
fx('fix', '22.01 leftover: the Warm-Up title and subtitle named the toaster lesson', '<div class="act-title">🌅 Warm-Up: What Goes In, What Comes Out?</div>\n        <div class="act-subtitle">A familiar device, a hidden change</div>',
   '<div class="act-title">🌅 Warm-Up: Which Train Moved?</div>\n        <div class="act-subtitle">You can’t always tell by looking</div>')
fx('fix', '22.01 leftover: the toaster warm-up → the train window',
   '<p>Think about a toaster. You drop in cold bread. A minute later, you pull out hot toast.</p>',
   '<p>You are sitting on a train at Palmetto Beach station. Another train sits right outside your window. Then something starts to move. But which train is it? Watch and vote.</p>')
fx('fix', '22.01 leftover: the toaster sketch → three things you can see right now (on the page)',
   "<p>In your notebook, draw a quick sketch of a toaster. On one side, label what goes IN. On the other, label what comes OUT. (Hint: bread on both sides — but something invisible is also going in. What is it?)</p>",
   '<p>Now look around you. What is moving, and what is staying in one place?</p>')
fx('fix', '22.01 leftover: Notice & Wonder about the toaster',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Notice &amp; Wonder</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover: “energy can CONVERT … toasters” callout',
   r'<div class="callout callout-tip">\s*<span class="callout-icon">💡</span>\s*<p>Today you\'ll learn that energy can CONVERT.*?</p>\s*</div>\s*', '', True)
# 9.01 leftovers
fx('fix', '9.01 leftover: Part C was a food chain; the checklist already asks for a motion diagram', '🎨 Part C &mdash; Build Your Own Food Chain', '🎨 Part C &mdash; My Motion Diagram')
fx('fix', '9.01 leftover: Part C task (now the lesson’s own motion diagram, drawn on the page, + its one-sentence description)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Watch something move at home: a toy car, a pet or a rolling ball. Pick a reference point that stays put. Then draw your motion diagram and describe it.</p>', True)
fx('fix', '9.01 leftover: Reflect asked about a hawk; the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'supply list: something to watch for Part C', r'<span class="need-chip"><span>✏️</span>Colored pencils</span>', '<span class="need-chip"><span>🚗</span>Something that moves: a toy car, a ball or a pet</span>', True)
# wrong fact
fx('fix', 'wrong fact (ticked): a swing goes back and forth along a curve, it is not a circular path. No dashes; examples trimmed',
   '<li><strong>Curved path:</strong> a Frisbee turning in the wind, a runner rounding a corner.</li>\n        <li><strong>Circular path:</strong> a swing going back and forth, Earth orbiting the Sun.</li>\n        <li><strong>Up-and-down:</strong> a basketball dribbled in place.</li>',
   '<li><strong>Curved path:</strong> a Frisbee turning in the wind.</li>\n        <li><strong>Circular path:</strong> a Ferris wheel car, or Earth going around the Sun.</li>')
# Word Wall (ticked): Device -> Reference point
fx('fix', 'Word Wall (ticked): “Device” is an energy-lesson leftover this lesson never uses; “Reference point” is the key term and had no card',
   '<div class="fc-emoji">⚙️</div><div class="fc-word">Device</div><div class="fc-tap">tap to flip</div></div><div class="flip-card-back"><div class="fc-word-back">Device</div><div class="fc-def">A tool or machine designed to do a job. Most devices convert energy from one form to another — a flashlight, a toaster, a fan are all devices.</div>',
   '<div class="fc-emoji">📌</div><div class="fc-word">Reference point</div><div class="fc-tap">tap to flip</div></div><div class="flip-card-back"><div class="fc-word-back">Reference point</div><div class="fc-def">Something that stays put, which you compare to. A lamp post, a tree or a doorway makes a good reference point.</div>')

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; plain words; no dash', r"<p>Hold this question in your head as you work\. By the end of the lesson.*?</p>",
   "<p>Keep this question in mind. By the end, you’ll describe how something moved so clearly that someone else could draw it.</p>", True)
fx('plain', 'cut filler', r"<p>These six words show up all through the lesson\. <strong>Tap a card to flip it</strong>.*?</p>",
   "<p><strong>Tap a card to flip it</strong> and read what the word means.</p>", True)
fx('plain', 'Part 1: no dash; one idea per sentence; the true Florida line (sailors use things on land that stay put) kept as one sentence; leads into the game',
   ' is where something IS — but only compared to something else. You might say "the toy car is 3 feet from the door" or "the soccer ball is 2 steps to the left of the tree." That something-else you compare to is the ',
   ' is where something IS, compared to something else. You might say "the toy car is 3 feet from the door." The thing you compare to is the ')
fx('plain', 'Part 1: “relative to” is a hard phrase; same meaning. The Florida line and the lead-in to the game sit here',
   ' relative to that reference point. If its position has changed, it\'s in ', ' compared to that reference point. If its position has changed, it\'s in ')
fx('plain', 'Part 1: the Florida connection (true) as one sentence, then the lead-in to Find it from the clue',
   'Changing position over time.</span></span>.</p>',
   'Changing position over time.</span></span>.</p>\n\n      <p><strong>In Florida:</strong> sailors and surfers pick things on land that stay put, like a lighthouse or a pier, as their reference points. Try it on the beach: find each lost thing from its position clue.</p>')
fx('plain', 'Part 2: no dash; plain words', 'Motion has two big pieces: how MUCH something moves, and in what ', 'To describe motion, say how FAR something moved and in what ')
fx('plain', 'Part 2: no dash; plain words', '. Saying "the toy car moved 5 feet" isn\'t complete — you have to add "to the right" or "toward the wall" to fully describe it.</p>',
   '. "The toy car moved 5 feet" isn\'t enough. You have to add which way: "to the right" or "toward the wall."</p>')
fx('plain', 'Part 2: shorter; no dash; leads into Program the helper',
   '<p>A clear description names ALL of it: the object, the starting position, the ending position, the direction, and the path. "The toy car started at the tree, moved 3 feet in a straight path to the right, and ended at the fence" — anyone reading that could draw it.</p>',
   '<p>A clear description names ALL of it: where it started, which way it went, its path and where it ended. Sam’s delivery robot, Scoot, will test your descriptions. Scoot does exactly what your words say.</p>')
fx('plain', 'plain words: “misconception” is a hard word; no dashes; same idea',
   '<p><strong>Common misconception:</strong> Some people think motion is something an object "has." Motion is actually a COMPARISON — it only exists relative to a reference point. The same object can be at rest AND in motion at the same time, just compared to different things.</p>',
   '<p><strong>Watch out:</strong> some people think an object is either moving or not, and that’s that. But motion is a COMPARISON. On the train, you were at rest compared to your seat and in motion compared to the station sign, both at once.</p>')
fx('plain', 'Part B question 5 named the removed tap diagram; the same task now points at the two replays in Part 3 (same question, same kind of answer)',
   'Pick ONE scene from the diagram (runner, swing, toy car ramp, or bird). Name the REFERENCE POINT, DIRECTION, and PATH.',
   'Think about the crab that walked along the sand or the seagull that glided over the beach. Pick ONE. Name a REFERENCE POINT you could use, its DIRECTION, and its PATH.')
fx('plain', 'Part B question 5 label (Gathered Answers)', 'data-label="Pick ONE scene from the diagram (runner, swing, to..."', 'data-label="The crab or the seagull: reference point, direction, path"')
fx('plain', 'Part B question 6 label (Gathered Answers)', 'data-label="A pencil sits still on your desk while the school ..."', 'data-label="The pencil on your desk: in motion or at rest?"')
fx('plain', 'no dash in question 6 (same question)', 'Is the pencil in MOTION or AT REST? Explain — and name your reference point.', 'Is the pencil in MOTION or AT REST? Explain, and name your reference point.')
fx('plain', 'no dash in the classmate’s claim (same claim)', 'You can describe motion without a reference point — just say how far it moved.', 'You can describe motion without a reference point. Just say how far it moved.')
fx('plain', 'no dash in the Lesson subtitle', '<div class="act-subtitle">Position, direction, and a reference point</div>', '<div class="act-subtitle">Position, direction and a reference point</div>')
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'closing: no dashes; plain words (same meaning; the teaser for 25.02 is right)',
   ' — clear enough for someone else to draw what you saw. Next lesson, we add SPEED — using distance and time to measure how fast.</p>',
   '. Your description is clear enough for someone else to draw what you saw. Next lesson, we add SPEED: using distance and time to measure how fast.</p>')
fx('plain', 'figure caption: no change in meaning; names the flaw-free reading order', '<strong>A good motion diagram answers four questions:</strong> Where did it start? Where did it end? Which way did it go? What was the path?',
   '<strong>A good motion diagram answers four questions:</strong> Where did it start? Where did it end? Which way did it go? What was its path?')

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: Stop & Think (the train window is the same idea, played)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'removed: Key Concept, the gravity and friction box (ticked: not in the plan row), the Stop & Reason about “the three devices above” (a 22.01 leftover), the Four Motion Scenes tap diagram, Observe & Reason, the “Amazing Florida Fact” (not about Florida, and its football-field number was far too small: Earth moves about 18 miles every second), the Florida callout (kept as one sentence in Part 1) and Go Deeper. Part 3 = the old Explore (Draw a Motion Diagram); the next button goes to Self-Check. The sample motion diagram picture stays, right above Part 3',
   r'\s*<div style="background:#FFF6E5;border:2\.5px solid #F0C97A;[^>]*>\s*<div[^>]*>⭐ Key Concept</div>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   '\n\n      ' + H3 + 'Part 3 · Draw a Motion Diagram</h3>\n      ' + PS + 'Sam filmed two things moving on the beach this morning. Watch each replay, then turn it into a motion diagram.</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its motion diagram is now Part 3 and Part C; its speed “Amazing Florida Fact” (alligators do not run 35 mph; about 11 mph is the usual figure), Think like a scientist and Go Deeper go with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 7 removed (Bethany kept 5 and 6; Q7 repeats the CER claim)', r'<div class="pq">\s*<span class="pq-num"[^>]*>7</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C drawn and typed on the page', 'A motion diagram of a real object with starting/ending positions, direction arrow, reference point, and a one-sentence description.',
   'What I watched, my reference point and my one-sentence description. Plus your labeled sketch: your motion diagram.')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether motion needs a reference point or not, supported with two pieces of evidence.',
   '<strong>Use Your Evidence:</strong> My claim about whether motion needs a reference point, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a 9.01 leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Download your field journal (it has your answers and your motion diagram) and upload it to the Canvas assignment. Or copy your Gathered Answers (above) into Canvas.', True)

# ---------------------------------------------------------------- Teo's treasure map (hand-drawn look; it shows no direction on purpose)
INK = 'stroke="#6B3F1D" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"'
TMAP = ('<svg viewBox="0 0 420 250" role="img" aria-label="Teo’s hand-drawn map: wavy water on the left, a pier, a small rowboat on the sand, a palm tree, a loopy dotted line and a big red X. Nothing shows which way to walk.">'
  '<g ' + INK + '>'
  '<path d="M38 12 q16 20 0 40 t0 40 t0 40 t0 40 t0 40 t0 40"/><path d="M18 30 q8 8 0 16 M16 96 q8 8 0 16 M18 170 q8 8 0 16" stroke-width="2"/>'
  '<path d="M4 118 h70 M4 138 h70 M20 118 v20 M40 118 v20 M60 118 v20"/>'
  '<path d="M96 196 q34 26 68 0 l-8 -12 h-52z"/><path d="M112 184 l-14 -18 M148 184 l14 -18"/>'
  '<path d="M330 214 q-6 -50 6 -86 M336 128 q-30 -16 -46 6 M336 128 q-10 -30 -40 -30 M336 128 q26 -22 50 -6 M336 128 q8 -30 38 -32 M336 128 q-2 -26 14 -40"/>'
  '<circle cx="388" cy="30" r="12"/><path d="M388 10 v-6 M388 50 v6 M368 30 h-6 M408 30 h6 M374 16 l-5 -5 M402 16 l5 -5 M374 44 l-5 5 M402 44 l5 5" stroke-width="2"/>'
  '<path d="M170 176 q30 -60 -10 -80 q-34 -14 -30 22 q6 30 56 6 q40 -22 60 -56" stroke-dasharray="3 9"/>'
  '</g>'
  '<path d="M236 44 l28 28 M264 44 l-28 28" stroke="#C0392B" stroke-width="7" stroke-linecap="round"/>'
  '<g font-family="Comic Sans MS, Chalkboard SE, Nunito, sans-serif" fill="#6B3F1D" font-size="15" font-weight="700">'
  '<text x="92" y="232">rowboat</text><text x="58" y="110">pier</text><text x="272" y="66" fill="#C0392B" font-size="16">TREASURE!</text><text x="188" y="150">5 steps</text><text x="318" y="236">palm</text>'
  '</g></svg>')

# ---------------------------------------------------------------- the story
SAM = Q['crew']['sam']
D = {
    'lesson': '25.01', 'week': 25, 'day': 1, 'guide': 'sam', 'prefix': 'g4sci-25-1', 'manifestKey': '25-01',
    'paths': P['paths'], 'crew': {'sam': SAM},
    'expedition': {'num': 25, 'title': 'The Lost Time Capsule'},
    'ambient': {'icon': '🌊', 'label': 'Beach morning'},
    'beach': {
        'cols': 10, 'rows': 7, 'pierY': 3, 'model': 'north is up · 1 square = 1 step',
        'alt': 'A map of Palmetto Beach seen from above. North is up. The Gulf and the pier are on the west side. The boardwalk is on the east side. Each square is one step.',
        'dirs': {'N': {'t': 'north', 'icon': '⬆'}, 'E': {'t': 'east', 'icon': '➡'}, 'S': {'t': 'south', 'icon': '⬇'}, 'W': {'t': 'west', 'icon': '⬅'}},
        'goBtn': '▶ Go', 'clearBtn': '↺ Start over', 'whichWay': 'which way?', 'thenWord': 'then', 'stepWord': 'step', 'stepsWord': 'steps',
        'emptyLine': 'Tap an arrow card to add it here, or drag it in.', 'fullLine': 'That is the most cards you can use. Take one out first.',
        'marks': [
            {'id': 'lamp', 'icon': '💡', 't': 'lamp post', 'the': 'the lamp post', 'x': 1, 'y': 3, 'fixed': True},
            {'id': 'tower', 'icon': '🛖', 't': 'lifeguard tower', 'the': 'the lifeguard tower', 'x': 3, 'y': 4, 'fixed': True},
            {'id': 'palm', 'icon': '🌴', 't': 'palm tree', 'the': 'the palm tree', 'x': 8, 'y': 5, 'fixed': True},
            {'id': 'boat', 'icon': '🛶', 't': 'rowboat', 'the': 'the rowboat', 'x': 6, 'y': 1, 'fixed': False},
            {'id': 'cart', 'icon': '🍦', 't': 'ice cream cart', 'the': 'the ice cream cart', 'x': 9, 'y': 2, 'fixed': False}]},
    'case': {
        'num': 25, 'title': 'The Lost Time Capsule', 'style': 'tmap', 'stills': [],
        'hook': 'After the boat parade, Rosa’s cousin Teo buried a time capsule in the sand at Palmetto Beach. (A time capsule is a box of things you save to open years later.) He drew a map so the town can dig it up next December. This morning six people tried the map. Nobody found a thing.',
        'tmap': {'svg': TMAP, 'head': 'How to find it', 'lines': ['Start at the rowboat.', 'Walk 5 steps.', 'Dig!'], 'sign': 'by Teo',
                 'sticky': 'Six holes. No capsule. What is wrong with these directions?', 'stickySign': 'Sam'},
        'question': 'Why can’t anyone find the time capsule with Teo’s directions, and what would fix them?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'trainwin', 'icon': '🚆', 'where': 'Warm-Up: which train moved?', 't': 'You can’t tell what moved until you compare it to something that stays put. That thing is a reference point.'},
            {'id': 'findit', 'icon': '📍', 'where': 'The Lesson, Part 1: find it from the clue', 't': 'A position is where something is, compared to a reference point. The rowboat moved, so its clue led to an empty square.'},
            {'id': 'helper', 'icon': '🤖', 'where': 'The Lesson, Part 2: program the helper', 't': '“4 steps” is not enough. A description needs the direction, too. The path is the route something takes.'},
            {'id': 'diagram', 'icon': '🗺️', 'where': 'The Lesson, Part 3: diagram the replay', 't': 'A motion diagram shows the start, the end, the direction and a reference point that stays put.'},
        ],
        'solve': {
            'title': 'What is wrong with Teo’s directions?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Teo counted wrong. People should walk more steps from the rowboat.', 'why': 'Check Clue 2. The rowboat moved. More steps from the wrong starting place won’t help.'},
                {'t': 'The rowboat moved, so it is a bad reference point, and Teo never said which way to walk. Start from something that stays put, and name the direction and the steps.', 'right': True,
                 'why': 'Case cracked! Good directions need a reference point that stays put, a direction and a distance.'},
                {'t': 'Someone dug up the capsule and took it away.', 'why': 'Nothing shows that. Check Clue 2: what moved overnight?'},
                {'t': 'Directions can’t work on a beach, because sand looks the same everywhere.', 'why': 'Check Clue 4. A reference point that stays put works anywhere, even on sand.'},
            ]},
    },
    'trainwin': {
        'afterText': 'Watch and vote.', 'kicker': 'Warm-Up game', 'title': 'Which train moved?',
        'todo': ['Press Watch and look out the left window.', 'Vote: who moved?', 'Look out the right window to find out. Then take trip 2.'],
        'model': 'a model', 'sign': 'PALMETTO BEACH', 'leftLabel': 'Left window: the train next to you', 'rightLabel': 'Right window: the station',
        'tripWord': 'Trip', 'watchBtn': '▶ Watch out the left window', 'againBtn': '↺ Watch again', 'voteQ': 'Who moved?',
        'votes': [{'k': 'mine', 't': 'My train moved'}, {'k': 'other', 't': 'The other train moved'}, {'k': 'unsure', 't': 'I can’t tell yet'}],
        'votedLine': 'Your vote: {v}. Now check it.', 'lookBtn': '👀 Look out the right window', 'nextBtn': 'Trip 2 ▸', 'doneBtn': 'Finish ▸',
        'trips': [
            {'mover': 'other', 'still': 'The station sign did not move.', 'verdict': 'So YOUR train is at rest (not changing position). The other train pulled away.'},
            {'mover': 'mine', 'still': 'The station sign slid past!', 'verdict': 'So this time YOUR train is in motion. Out the left window, it looked exactly the same as trip 1.'}],
        'unsureLine': 'You were smart to wait. With only another train to look at, nobody can tell.',
        'rightLine': 'Your vote was right, but it was a lucky guess. Both trips looked the same out the left window.',
        'wrongLine': 'Fooled you! It happens on real trains, too.',
        'q': 'How did you finally know which train moved?',
        'opts': [{'t': 'I compared it to the station sign, which stays put.', 'ok': True},
                 {'t': 'I looked harder at the other train.', 'miss': 'The other train looked the same on both trips. What did you see out the right window?'},
                 {'t': 'I could feel it.', 'miss': 'A smooth train is hard to feel. What settled it both times?'}],
        'win': 'To know what moved, compare it to something that stays put: a reference point. Clue 1!'},
    'findit': {
        'afterText': 'find each lost thing', 'kicker': 'Part 1 game', 'title': 'Find it from the clue',
        'todo': ['Read the clue. Find its reference point on the map.', 'Count the steps. East is toward the boardwalk. West is toward the Gulf.', 'Tap that square, or drag the 📍 pin onto it.'],
        'why': {'icon': '🧭', 'q': 'How do I read this map?', 't': 'You are looking down from above. North is up. Each square is one step.'},
        'pin': '📍 Drag me onto a square, or just tap a square', 'clueWord': 'Clue', 'foundWord': 'clues tried',
        'rounds': [
            {'icon': '🏐', 'name': 'beach ball', 'clue': 'The beach ball is 3 steps east of the lifeguard tower.', 'at': [6, 4],
             'hint': 'Find the lifeguard tower. Count 3 squares toward the boardwalk (east).', 'found': 'Found it! Its position: 3 steps east of the lifeguard tower.'},
            {'icon': '🕶️', 'name': 'sunglasses', 'clue': 'The sunglasses are 2 steps north of the lamp post.', 'at': [1, 1],
             'hint': 'Find the lamp post. North is up. Count 2 squares.', 'found': 'Found them! Their position: 2 steps north of the lamp post.'},
            {'icon': '🪣', 'name': 'bucket', 'clue': 'The bucket is 4 steps west of the palm tree.', 'at': [4, 5],
             'hint': 'Find the palm tree. Count 4 squares toward the Gulf (west).', 'found': 'Found it! Its position: 4 steps west of the palm tree.'}],
        'trick': {'icon': '⛏️', 'name': 'shovel', 'boat': 'boat', 'clue': 'Teo wrote this one yesterday: The shovel is 2 steps east of the rowboat.', 'wrong': [8, 1], 'at': [3, 6], 'ghost': [1, 6], 'ghostLabel': 'yesterday',
                  'hint': 'Find the rowboat. Count 2 squares toward the boardwalk (east).', 'emptyLine': 'Nothing here! You counted right. So what went wrong?', 'whyBtn': '🔎 Find out why',
                  'reveal': 'Look at the drag marks in the sand. Yesterday the rowboat sat by the water. Last night someone pulled it up the beach. The shovel is 2 steps east of where the rowboat WAS.'},
        'q': 'Which makes the best reference point for a clue you will use next year?',
        'opts': [{'t': 'The lamp post. It stays put.', 'ok': True},
                 {'t': 'The rowboat.', 'miss': 'The rowboat moved overnight. What happened to its clue?'},
                 {'t': 'The ice cream cart.', 'miss': 'A cart has wheels. Will it be in the same place next year?'},
                 {'t': 'A seagull.', 'miss': 'A seagull flies off in seconds. Pick something that stays put.'}],
        'win': 'A position only works if its reference point stays put. The rowboat moved, so its clue failed. Clue 2!'},
    'helper': {
        'afterText': 'Scoot does exactly what your words say.', 'kicker': 'Part 2 game', 'title': 'Program the helper',
        'todo': ['Read the order slip.', 'Tap an arrow card to add it (or drag it in). Set its steps with − and +.', 'Press Go. Scoot starts at the lamp post every time.'],
        'start': 'lamp', 'show': ['lamp', 'tower', 'palm'], 'cart': '🤖', 'levelWord': 'Delivery', 'countWord': 'deliveries done', 'nextBtn': 'Next delivery ▸',
        'needDir': 'Scoot is stuck. The slip says 4 steps, but which way? Tap an arrow card to fill in the direction.', 'needCard': 'Add an arrow card first.',
        'reportLine': 'Scoot followed your words exactly. ', 'saidLine': 'You said: {c}.', 'edgeLine': 'Scoot stopped at the edge of the map after {n}.',
        'endLine': 'Scoot ended {p}.', 'missLine': '{who} is {p}. Change a card and try again.', 'trackWord': 'Scoot’s tracks in the sand: {n}',
        'levels': [
            {'id': 'mia', 'icon': '🧾', 't': 'Order for Mia', 'slip': 'Rosa wrote: “Take the cocoa 4 steps.” Something is missing. Fix the card, then press Go.',
             'preset': [{'d': None, 'n': 4, 'lock': True}], 'max': 1, 'target': [5, 3], 'mark': {'icon': '🏖️', 't': 'Mia'}, 'ok': 'Delivered! The slip needed a direction.'},
            {'id': 'lopez', 'icon': '🧾', 't': 'Order for Mr. Lopez', 'slip': 'This one is yours to write. Mr. Lopez is not straight east, so you will need a turn: two cards.',
             'preset': [], 'target': [5, 1], 'mark': {'icon': '⛱️', 't': 'Mr. Lopez'}, 'ok': 'Delivered! Scoot’s path had one turn in it.'},
            {'id': 'loop', 'icon': '🧾', 't': 'The test lap', 'slip': 'Sam wrote these four cards to test Scoot: a lap around the lifeguard tower. Press Go and watch where Scoot ends.',
             'preset': [{'d': 'E', 'n': 4}, {'d': 'S', 'n': 2}, {'d': 'W', 'n': 4}, {'d': 'N', 'n': 2}], 'lockAll': True, 'loop': True,
             'q': 'Scoot ended exactly where it started. Did Scoot move?',
             'opts': [{'t': 'Yes. Its position kept changing the whole way around.', 'ok': True, 'why': 'Right. Motion is a change of position over time. The 12 steps of tracks show Scoot’s path, even though it ended at the lamp post again.'},
                      {'t': 'No. It ended in the same spot, so it never moved.', 'miss': 'Look at the tracks in the sand. Could Scoot make those without moving?'}]}],
        'win': 'A helper needs the whole description: where to start, which way, how far. Leave one out and it fails. Clue 3!'},
    'ferris': {
        'after': 'helper', 'kicker': 'Wow!', 'title': 'The Ferris wheel',
        'todo': ['Vote first.', 'Press Ride and watch Mia’s gold car.', 'Then see a real photo.'],
        'model': 'a model', 'voteQ': 'Mia gets on a Ferris wheel, rides once around and gets off right where she got on. Did she move?',
        'votes': [{'k': 'yes', 't': 'Yes, she moved'}, {'k': 'no', 't': 'No, she ended where she started'}], 'needVote': 'Vote first: did she move?',
        'rideBtn': '▶ Ride once around', 'againBtn': '↺ Ride again',
        'changeLabel': 'Start to end', 'changeVal': 'Same spot', 'pathLabel': 'Her path', 'pathVal': 'One big circle',
        'yesLine': 'You voted yes, and the gold trail proves it. Her position kept changing all the way around, even though she ended where she started.',
        'noLine': 'You voted no. But look at the gold trail! Her position kept changing all the way around, even though she ended where she started. She moved.',
        'photoBtn': '📷 See a real camera do this',
        'photo': {'img': I('ferris-wheel'), 'alt': 'A real Ferris wheel on a pier at night. The camera stayed open while the wheel turned, so its lights drew bright rings.',
                  'cap': 'The Seattle Great Wheel, 175 feet tall. The camera kept its shutter open while the wheel turned, so every light drew its own path: a circle. One trip around carries a rider about 500 feet. Photo: Diego Delso, CC BY-SA 4.0, via Wikimedia Commons.'},
        'done': 'Wow! Ending where you started does not mean you never moved. The path tells the story.'},
    'diagram': {
        'afterText': 'turn it into a motion diagram', 'kicker': 'Part 3 game', 'title': 'Diagram the replay',
        'todo': ['Press Watch the replay.', 'Plant the 🟢 Start flag, then the 🔴 End flag: tap the square, or drag the flag.', 'Name the arrow’s direction and the path.', 'Tap a reference point: something that stays put.'],
        'why': {'icon': '🗺️', 'q': 'What is a motion diagram?', 't': 'A picture that shows how something moved: where it started, where it ended, an arrow for the direction, and a reference point.'},
        'watchBtn': '▶ Watch the replay', 'againBtn': '↺ Watch the replay again', 'sceneWord': 'motion diagrams built', 'sentLabel': 'Your motion description',
        'flagStart': '🟢 Start flag: drag me to where it started, or tap that square', 'flagEnd': '🔴 End flag: drag me to where it ended, or tap that square',
        'steps': {'start': '1. Where did it start?', 'end': '2. Where did it end?', 'dir': '3. Which way does the arrow point?', 'path': '4. What was its path?', 'ref': '5. Tap a reference point on the map: something that stays put'},
        'missWatch': 'Watch the replay first.', 'missStart': 'Not there. Watch the replay again and look at the very beginning.', 'missEnd': 'Not there. Watch the replay again and look at where it stops.',
        'dirMiss': 'Look at the arrow’s tip. East is toward the boardwalk. West is toward the Gulf.', 'pathMiss': 'Watch the replay again. Did it go in a line, or did it bend?',
        'refMiss': '{The} can move. Pick something that stays put.',
        'paths': [{'k': 'straight', 't': 'Straight', 'word': 'straight'}, {'k': 'curved', 't': 'Curved', 'word': 'curved'}, {'k': 'circle', 't': 'A full circle', 'word': 'circular'}],
        'sentence': 'The {the} started {start}, moved {dir} in a {path} path, and ended {end}.',
        'scenes': [
            {'id': 'crab', 'icon': '🦀', 'name': 'The crab', 'the': 'crab', 'from': [7, 5], 'to': [4, 5], 'bend': 0, 'dir': 'W', 'path': 'straight'},
            {'id': 'gull', 'icon': '🕊️', 'name': 'The seagull', 'the': 'seagull', 'from': [2, 3], 'to': [8, 3], 'bend': -2.4, 'dir': 'E', 'path': 'curved'}],
        'q': 'What does every motion diagram need?',
        'opts': [{'t': 'A start, an end, an arrow for the direction, and a reference point.', 'ok': True},
                 {'t': 'Only how far it moved.', 'miss': 'Think about Scoot. Was “4 steps” enough?'},
                 {'t': 'A drawing of the object in bright colors.', 'miss': 'Colors are nice. But what four things did you add to each diagram?'}],
        'win': 'Start, end, direction arrow, reference point: that is a motion diagram. Clue 4!'},
    'exploreMod': 'diagram',
    'redirect': {
        'after': '.fs-solve', 'kicker': 'Case closed · Fix the map', 'title': 'Rewrite the directions',
        'todo': ['Pick where the new directions should start.', 'Line up arrow cards from there to the ✕.', 'Press Send Scoot. If the words are right, Scoot digs it up.'],
        'lockLine': 'Crack the case first.',
        'why': {'icon': '✕', 'q': 'How do we know where the ✕ is?', 't': 'The drag marks show where the rowboat sat when Teo buried the capsule. Teo walked 5 steps east from there. The ✕ marks that spot.'},
        'cart': '🤖', 'x': [6, 6], 'xMark': {'icon': '✕', 't': 'the capsule'},
        'startQ': '1. Where should the new directions start, so they still work next December?',
        'starts': [{'k': 'lamp', 't': 'At the lamp post', 'ok': True},
                   {'k': 'boat', 't': 'At the rowboat', 'miss': 'That is what Teo did. Will the rowboat be in the same place next December?'},
                   {'k': 'cart', 't': 'At the ice cream cart', 'miss': 'The cart rolls away every night. Pick something that stays put.'},
                   {'k': 'water', 't': 'At the edge of the water', 'miss': 'The water’s edge moves in and out with the tide all day. Pick something that stays put.'}],
        'cardsLab': '2. Line up the cards from the lamp post to the ✕', 'goBtn': '▶ Send Scoot',
        'missLine': 'Scoot dug {p}. Nothing there. The capsule is {x}.', 'edgeLine': 'Scoot hit the edge of the map {p}. The capsule is {x}.',
        'found': 'Scoot found the time capsule!', 'insideHead': 'Inside the cocoa tin:',
        'inside': ['A boat parade program', 'One bulb from the string lights', 'Order slip #15', 'Teo’s napkin plan'],
        'stamp': 'FOUND', 'cardHead': 'How to find it (new and improved)', 'cardStart': 'Start at {the}.', 'cardTpl': 'Walk {n} {d}.', 'cardEnd': 'Dig!',
        'win': 'These directions will still work next December: a reference point that stays put, a direction and a distance.'},
    'nightrun': {
        'after': '.fs-solve', 'kicker': 'Bonus game', 'title': 'Night Delivery',
        'todo': ['Program Scoot around the sandcastles to the order.', 'Scoot stops if it bumps a sandcastle.', 'Fewer cards means more stars.'],
        'lockLine': 'Crack the case first.', 'start': 'lamp', 'cart': '🤖', 'levelWord': 'Route', 'blockIcon': '🏰', 'nextBtn': 'Next route ▸',
        'blockLine': 'Bump! Scoot ran into a sandcastle and stopped. Go around it.', 'edgeLine': 'Scoot reached the edge of the map and stopped. Check your steps.',
        'missLine': 'Scoot ended {p}. That is not the order. Change a card.', 'homeLine': 'Delivered, but Scoot ended {p}. This order says to come back to the lamp post.',
        'okLine': 'Delivered with {n} cards and {s} of tracks.', 'fewerLine': 'Can you do it with fewer cards?',
        'levels': [
            {'id': 'n1', 't': 'Cocoa for the night guard', 'slip': 'The guard is 5 steps east of the lamp post, but a sandcastle is in the way.', 'target': [6, 3], 'mark': {'icon': '🔦', 't': 'night guard'}, 'blocks': [[4, 3]], 'par': 3},
            {'id': 'n2', 't': 'Cocoa for the fishing crew', 'slip': 'A wall of sandcastles crosses the beach. Find the gap.', 'target': [7, 6], 'mark': {'icon': '🎣', 't': 'fishing crew'},
             'blocks': [[0, 5], [1, 5], [2, 5], [3, 5], [4, 5], [6, 5], [7, 5], [8, 5], [9, 5]], 'par': 3},
            {'id': 'n3', 't': 'There and back', 'slip': 'Take cocoa to the stargazers, then bring Scoot back to the lamp post.', 'target': [5, 1], 'mark': {'icon': '🔭', 't': 'stargazers'}, 'blocks': [[3, 2]], 'par': 4, 'home': True}],
        'win': 'Three night routes delivered. Scoot only knows what your words say!'},
    'fold': {'nightrun': {'icon': '🌙', 'tease': 'Optional: three tricky routes in the dark. How few cards can you use?', 'open': 'Play'}},
    'tool': {
        'name': 'Compass', 'icon': '🧭', 'kicker': 'Bonus · Tool of the Week', 'teaser': 'Find north, east, south and west anywhere.',
        'key': '25-tool', 'sim': 'compass', 'after': '#tab-assignment .activity-card',
        'why': {'icon': '🧭', 'q': 'What is a compass?', 't': 'A compass tells you which way you are facing. Its needle is a tiny magnet. Earth acts like a giant magnet, so the needle always swings to point north.'},
        'done': 'You can name a direction anywhere on Earth!',
        'compass': {
            'kicker': 'Try it: a compass', 'title': 'Turn and read',
            'todo': ['You are standing at the lamp post. Press Turn left or Turn right (or the ← → keys).', 'When something is straight ahead, read the letter under the red mark.', 'Log all four directions.'],
            'photo': {'img': I('compass'), 'alt': 'A real pocket compass: a round black dial with the letters N, E, S and W and a thin needle.',
                      'cap': 'A real pocket compass. Its needle is a tiny magnet that swings until it lines up north and south. Photo: Evan-Amos, public domain, via Wikimedia Commons.'},
            'model': 'a model', 'alt': 'A model of a compass. The dial with N, E, S and W stays pointing north while you turn. A red mark at the top shows the way you face.',
            'leftBtn': '⟲ Turn left', 'rightBtn': 'Turn right ⟳', 'aheadLabel': 'Straight ahead of you', 'nothing': 'Just sand and sky. Keep turning.', 'nothingIcon': '🏖️',
            'readQ': 'You are facing {the}. Which letter is under the red mark?', 'readMiss': 'Look at the very top of the compass, under the red mark.',
            'gotLine': 'Logged: {the} is to the {d}.', 'logLabel': 'My compass log', 'whatWord': 'I faced', 'dirWord': 'Direction',
            'marks': [{'id': 'jetty', 'icon': '🚨', 't': 'The jetty light', 'the': 'the jetty light', 'deg': 0},
                      {'id': 'walk', 'icon': '🍦', 't': 'The boardwalk', 'the': 'the boardwalk', 'deg': 90},
                      {'id': 'band', 'icon': '🎪', 't': 'The band shell', 'the': 'the band shell', 'deg': 180},
                      {'id': 'pier', 'icon': '🌊', 't': 'The pier and the Gulf', 'the': 'the pier', 'deg': 270}],
            'q': {'q': 'You turned all the way around. What did the N on the compass do?',
                  'opts': [{'t': 'It kept pointing the same way: north.', 'ok': True, 'why': 'Right! North stays put, so everyone, everywhere, can use it to name a direction. Most maps put north at the top.'},
                           {'t': 'It turned with me.', 'why': 'Turn again and watch the N. Does it follow you?'},
                           {'t': 'It pointed at whatever I faced.', 'why': 'The RED MARK shows what you face. Watch the N.'}]}}},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Think about Find it from the clue. Every clue named something to count from.', 'B': 'Think about Find it from the clue. Every clue named something to count from.'},
        'q2': {'A': 'Think about the train. Compared to your seat, did your position change?', 'C': 'Pick one thing to compare to: the seat. Does your position change compared to it?'},
        'q3': {'B': 'Think about Scoot’s lap and the Ferris wheel. Did ending at the start mean nothing moved?', 'C': 'The car went AROUND a chair leg. Is that a line or a bend?'}},
    'flags': {
        'ans-1': [
            {'label': 'a reference point', 're': 'palm|lamp|tower|post|tree|pier|boardwalk|light ?house|sign|rock|reference'},
            {'label': 'a direction', 're': 'north|south|east|west|toward|left|right|away'},
            {'label': 'the path', 're': 'straight|strait|curv|bend|bent|line|circ|arc'}],
        'ans-2': [
            {'label': 'at rest or in motion', 're': 'rest|motion|moving|still|not mov|move'},
            {'label': 'your reference point', 're': 'desk|bus|road|ground|floor|room|table|sun|window|school'},
            {'label': 'compared to', 're': 'compar|relative|from the|than the|next to|same place|position'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|need|can.?t|cannot|isn|is not'},
            {'label': 'two pieces of evidence', 'any': ['train', 'sign', 'station', 'window', 'rowboat', 'boat', 'empty', 'shovel', 'scoot', 'robot', 'direction', 'steps', 'lamp', 'ferris', 'stays put', 'stay put', 'moved', 'clue'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-1': 15, 'ans-2': 15, 'cer-4': 30},
    'hints': {
        'ans-1': ['A reference point is something that stays put, like the palm tree or the lamp post.', 'The Gulf is west. The boardwalk is east. Which way did yours go?', 'Try: I pick the ___. A reference point is the ___. It moved ___ in a ___ path.'],
        'ans-2': ['Compared to the desk, is the pencil’s position changing?', 'Motion is a comparison. Name what you are comparing the pencil to.', 'Try: The pencil is ___ compared to the ___, because its position ___.'],
        'cer-4': ['First decide: is “how far” enough?', 'Think about the train window and Scoot’s order slip that said “4 steps”.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'From the train window, nobody could tell which train moved until they looked at the station sign.',
                'The rowboat clue led to an empty square, because the rowboat had moved.',
                'Scoot could not deliver with only “4 steps”. It needed a direction, too.',
                'The Ferris wheel in the photo is 175 feet tall.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · the lost time capsule', 'length': '20–30 s'},
        'warmup': {'label': 'Warm-Up · which train moved? (Clue 1)', 'length': '15–20 s',
                   'script': 'Sam here, on the beach with a puzzle. Read Teo’s map and my sticky note first. Then hop on the train. Press Watch, vote for who moved, and look out the right window. Check the station sign!'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Point at something in the room for “reference point”.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · find it from the clue (Clue 2)', 'length': '20–30 s'},
        'part2': {'label': 'Part 2 · program the helper (Clue 3)', 'length': '15–20 s',
                  'script': 'Meet Scoot, my delivery robot. Scoot does exactly what your words say. Read the order slip. Tap an arrow card, set the steps, then press Go. Wrong spot? Change a card and try again.'},
        'explore': {'label': 'Part 3 · diagram the replay (Clue 4)', 'length': '15–20 s',
                    'script': 'Time to build a motion diagram. Press Watch the replay. Plant the Start flag, then the End flag. Name the direction and the path. Last, tap a reference point: something that stays put.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · my motion diagram', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '15–20 s',
                     'script': 'A classmate says you only need how far something moved. True? Think about the train window, and Scoot with only four steps. Pick your side, tap two facts, then explain. That’s your C-E-R.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 25.02 (speed).'},
    },
    'videoOff': [],
    'lensVoice': False,
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Teo’s treasure map (Warm-Up)',
        'The station sign out the right window (Warm-Up)',
        'Scoot’s tracks around the lifeguard tower (The Lesson)',
        'One finished motion diagram (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['A toy car rolling', 'A pet walking', 'A ball rolling'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · draw and label your motion diagram', 'required': True, 'minLabels': 4,
                           'prompts': ['Draw your object where it STARTED and where it ENDED', 'Draw an arrow for its direction and path', 'Draw your reference point', 'Label all four: start, end, direction, reference point']}]},
    'hlCoach': copy.deepcopy(O['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🗺️', 'name': 'Teo’s treasure map',
                 'line': 'You cracked Case 25, and Teo’s map goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next time: how fast did it move?'},
    'notebookTitle': O['notebookTitle'],
    'notebook': copy.deepcopy(O['notebook']) + [{'lesson': '25.01', 'icon': '🗺️', 'name': 'Teo’s treasure map'}],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You know where you stand!',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to see what it means.']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '#tab-vocab p', 'text': 'What is moving, and what is staying in one place?'},
         'label': 'Warm-Up: moving or staying put', 'q': 'Warm-Up: One thing I see moving, one thing staying in one place, and how I can tell.', 'title': 'Moving or staying put?', 'compact': True,
         'fields': [{'t': 'Something moving', 'icon': '🏃', 'ph': 'The ___ is moving.'},
                    {'t': 'Something staying in one place', 'icon': '🪑', 'ph': 'The ___ is staying in one place.'},
                    {'t': 'How I can tell', 'icon': '👀', 'ph': 'I compared them to the ___.'}]},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Then draw your motion diagram and describe it.'},
         'label': 'Part C: My motion diagram', 'q': 'Part C: My motion diagram (my object, my reference point and my one-sentence description)', 'title': 'My motion diagram',
         'fields': [{'t': 'What I watched', 'icon': '🚗', 'ph': 'I watched a ___.'},
                    {'t': 'My reference point (something that stays put)', 'icon': '📌', 'ph': 'My reference point is the ___.'},
                    {'t': 'My one-sentence description', 'icon': '✏️', 'ph': 'The ___ started ___, moved ___ in a ___ path, and ended ___.', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Can you describe motion with only how far it moved?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-1': 'Part B · Question 5', 'ans-2': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'To describe motion, name a reference point, the direction and the path.',
    'key': ['motion', 'reference', 'point', 'direction', 'path'],
    'small': ['to', 'a', 'the', 'and', 'name'],
    'model': 'A scientist might highlight “motion”, “reference point”, “direction” and “path”. Those words hold the big idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me say where it started, where it ended and which way it went?']

EV = '#tab-assignment .act-body > div:has(> .fs-plan)'
D['cues'] = {
    'warmup': [{'at': '^map', 'sel': '.fs-tmap-paper', 'fx': 'glow', 'scroll': True},
               {'at': '^sticky', 'sel': '.fs-tmap-note', 'fx': 'pop'},
               {'at': '^watch', 'sel': '.fs-trn-watch', 'fx': 'point', 'scroll': True},
               {'at': '^vote', 'sel': '[data-mod="trainwin"] .fs-todo li', 'i': 1, 'fx': 'trace'},
               {'at': '^sign', 'sel': '.fs-trn-svg', 'fx': 'glow'}],
    'part2': [{'at': '^slip', 'sel': '.fs-hlp-slip', 'fx': 'glow', 'scroll': True},
              {'at': '^arrow', 'sel': '[data-mod="helper"] .fs-prg-pal', 'fx': 'pop'},
              {'at': '^steps', 'sel': '[data-mod="helper"] .fs-prg-strip', 'fx': 'glow'},
              {'at': '^go', 'sel': '[data-mod="helper"] .fs-prg-go', 'fx': 'point'},
              {'at': '^change', 'sel': '[data-mod="helper"] .fs-prg-strip', 'fx': 'wiggle'}],
    'explore': [{'at': '^replay', 'sel': '.fs-dgm-watch', 'fx': 'point', 'scroll': True},
                {'at': '^start', 'sel': '[data-mod="diagram"] .fs-todo li', 'i': 1, 'fx': 'trace'},
                {'at': '^direction', 'sel': '[data-mod="diagram"] .fs-todo li', 'i': 2, 'fx': 'trace'},
                {'at': '^reference', 'sel': '[data-mod="diagram"] .fs-bch-m.fixed small', 'all': True, 'fx': 'pop'}],
    'evidence': [{'at': '^classmate', 'sel': EV + ' > p', 'i': 0, 'fx': 'trace', 'scroll': True},
                 {'at': '^train', 'sel': '.fs-plan .fs-opt', 'i': 2, 'fx': 'glow'},
                 {'at': '^four', 'sel': '.fs-plan .fs-opt', 'i': 4, 'fx': 'glow'},
                 {'at': '^side', 'sel': '.fs-plan .fs-plan-row', 'i': 0, 'fx': 'pop'},
                 {'at': '^explain', 'sel': '.fs-cer .fs-cer-row', 'i': 2, 'fx': 'glow', 'scroll': True}],
}
D['cueWords'] = json.load(open('cuewords.json', encoding='utf-8')) if os.path.exists('cuewords.json') else {}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
# budget counter (oao-audio-budget): G4 science = 1,400 credits per lesson; scripts are written to 95% (1,330). Nothing is generated in week 25.
clips = {k: v['script'] for k, v in D['slots'].items() if v.get('script')}
tot = sum(len(t) for t in clips.values())
for k, t in clips.items(): print(f'  {k:10} {len(t):4}')
print(f'this page: {tot} / 1400 credits ({tot/1400:.0%}), scripts only, 0 generated')
assert tot <= 1330
json.dump(clips, open('clip-scripts.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
