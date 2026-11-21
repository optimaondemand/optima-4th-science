#!/usr/bin/env python3
"""Writes data.json and fixes.json for 23.02 (run from this folder). Case 23 part 2 "The Still Canal" (Sam Park, Pelican Canal, Palmetto Beach):
the Gazette's Bright Ideas contest; which reader idea can really get the still canal water moving, and what makes it work best?
New: case.paper.entries (contest entry forms under the front page), tiles (Warm-Up: uncover a real farm windmill tile by tile and guess),
droprace (Part 1: predict + let go; air pushes the flat paper; then a fan round), valve (Part 2: drag a valve handle around; the waterwheel
lights a lamp; "spin by itself" never works), redblade (Part 3 = the old Explore: count the red blade's spins yourself, change ONE thing),
zero (after the case: Florida's 0 wind farms + the real Jim Woodruff Dam), windribbon (after the case: one summer day on the dock, the sea
breeze), sail (bonus, folded). No tool (day 2)."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../18-01/data.json', encoding='utf-8'))
O = json.load(open('../23-01/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
PS = '<p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)
def I(n): return 'images/23-02-' + n + '.jpg'

# ---------------------------------------------------------------- labels (standing approval)
fx('fix', 'unit label: “Ecosystems & Energy” is a leftover; weeks 18–24 are Unit 5', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Energy, Motion &amp; Collisions</div>')
fx('fix', 'wind and water energy is physical science, not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standards label: the plan’s CPALMS codes, content benchmark first; TEKS is a Texas code that isn’t in the plan', '<div class="info-value">SC.4.N.1.1, SC.4.P.10.4 · TEKS 4.8(B)</div>', '<div class="info-value">SC.4.P.10.4, SC.4.N.1.1</div>')
fx('fix', 'footer: same order as the header (plan)', 'CPALMS SC.4.N.1.1, SC.4.P.10.4', 'CPALMS SC.4.P.10.4, SC.4.N.1.1')

# ---------------------------------------------------------------- ticked fixes (Bethany, 21 Nov 2026)
# 22.01 leftovers in the Warm-Up
fx('fix', '22.01 leftover: the Warm-Up title and subtitle named the toaster lesson', '<div class="act-title">🌅 Warm-Up: What Goes In, What Comes Out?</div>\n        <div class="act-subtitle">A familiar device, a hidden change</div>',
   '<div class="act-title">🌅 Warm-Up: The Mystery Tower</div>\n        <div class="act-subtitle">Lift the tiles, then guess</div>')
fx('fix', '22.01 leftover: the toaster warm-up → the uncover-the-tiles game',
   '<p>Think about a toaster. You drop in cold bread. A minute later, you pull out hot toast.</p>',
   '<p>Out in a field stands a tall tower with a wheel of blades on top. No wires run to it. What is it for? Lift the tiles to find out.</p>')
fx('fix', '22.01 leftover: the toaster sketch → a list of things moving air or water pushes (on the page)',
   "<p>In your notebook, draw a quick sketch of a toaster. On one side, label what goes IN. On the other, label what comes OUT. (Hint: bread on both sides — but something invisible is also going in. What is it?)</p>",
   '<p>Now look around you. What does moving air or moving water push near you?</p>')
fx('fix', '22.01 leftover: Notice & Wonder about the toaster',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Notice &amp; Wonder</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover: “energy can CONVERT … toasters” callout',
   r'<div class="callout callout-tip">\s*<span class="callout-icon">💡</span>\s*<p>Today you\'ll learn that energy can CONVERT.*?</p>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover: Stop & Reason about “the three devices above” (no such devices on this page)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
# 9.01 leftovers
fx('fix', '9.01 leftover: Part C was a food chain; the checklist already asks for a wind and water model', '🎨 Part C &mdash; Build Your Own Food Chain', '🎨 Part C &mdash; My Wind and Water Model')
fx('fix', '9.01 leftover: Part C task (now the two-panel model typed on the page + a required labeled sketch)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Show how moving air makes a pinwheel spin and how moving water makes a waterwheel spin. Fill in your model below, then sketch it.</p>', True)
fx('fix', '9.01 leftover: Reflect asked about a hawk; the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'supply list: a pinwheel to try it for real', r'<span class="need-chip"><span>✏️</span>Colored pencils</span>', '<span class="need-chip"><span>🌀</span>A pinwheel or a sheet of paper (to try it for real)</span>', True)
# wrong facts
fx('fix', 'wrong facts: Florida has no utility wind farms (EIA, 2025–26), and the Apalachicola River site is a hydroelectric dam (Jim Woodruff Dam, Florida’s only hydropower plant), not “pumps”; wind isn’t a growing source of Florida power',
   "<p>Florida uses both. The Sunshine State has wind farms along its coasts and hydroelectric pumps that move water at places like the Apalachicola River. Most of Florida's power still comes from natural gas, but more is coming from solar, wind, and water every year.</p>",
   "<p>How does Florida use them? Sailboats ride the wind, and old farm windmills pumped water for cattle. Florida has almost no wind farms, because its usual winds are gentle. But one dam on the Apalachicola River, at the Georgia line, uses moving water to make electricity.</p>")

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; plain words', r"<p>Hold this question in your head as you work\. By the end of the lesson.*?</p>",
   "<p>Keep this question in mind. By the end, you’ll explain what makes a wheel spin faster in wind or water, and how Florida uses them.</p>", True)
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
MOT = '<span class="vtip">motion<span class="vtip-box"><span class="vtip-word">Motion</span>Movement.</span></span>'
fx('plain', 'no dash (Part 1)', "<p>Air is real stuff — even though you can't see it. When air moves, it carries " + MOT + " energy. That moving air is what we call WIND.</p>",
   "<p>Air is real stuff, even though you can't see it. When air moves, it carries " + MOT + " energy. That moving air is what we call WIND.</p>")
fx('plain', 'no dash; the misconception moves here and leads into the game (Part 1)',
   'The wheel can then turn other things — a generator, a pump, even a flashlight.</p>',
   'The wheel can then turn other things, like a pump or a generator (a machine that makes electricity).</p>\n      <p><strong>Watch out:</strong> some people think air is nothing, because we can’t see it. Air is real stuff, and moving air can push. Try the drop race.</p>')
fx('cut', 'the misconception paragraph moved to Part 1 (next to the drop race)', r'\s*<p><strong>Common misconception:</strong> Some people think air "isn\'t real".*?</p>', '', True)
fx('plain', 'no dash; leads into the game (Part 2)', 'hits the cups of a water wheel, it pushes them — and the wheel spins.</p>', 'hits the cups of a water wheel, it pushes them, and the wheel spins. Turn the valve and see.</p>')
fx('plain', 'no dash (list)', '</span></strong> — using them doesn\'t use them up.</li>', '.</span></strong> Using them doesn\'t use them up.</li>')
fx('plain', 'no dash (figure caption)', 'When that motion hits a blade, the blade turns — and that turning can do useful work.', 'When that motion hits a blade, the blade turns, and that turning can do useful work.')
fx('plain', 'no dash (CER quote)', "\"Wind isn't real energy. It's just air moving — it doesn't do anything.\"", "\"Wind isn't real energy. It's just air moving. It doesn't do anything.\"")
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'no dash; plain closing', 'Noticed evidence.</span></span> — exactly what real scientists do. Next module we shift gears to HEAT — how it moves between objects, and which materials slow it down.',
   'Noticed evidence.</span></span>, just like real scientists. Next lesson: HEAT, how it moves between objects, and which materials slow it down.')
fx('plain', 'Part B question 6 label (Gathered Answers)', 'data-label="Explain how a pinwheel is like a wind turbine. Use..."', 'data-label="A pinwheel is like a wind turbine"')
fx('plain', 'Part B question 7 label (Gathered Answers)', 'data-label="Why are wind and water energy called RENEWABLE? Gi..."', 'data-label="Renewable, and how Florida uses them"')

fx('plain', 'define “transferred” where it is first seen', 'That spinning is energy being TRANSFERRED from the moving air to the wheel.', 'That spinning is energy being TRANSFERRED (passed along) from the moving air to the wheel.')
fx('fix', 'Lesson subtitle: Florida does not run on wind (0 wind farms)', '<div class="act-subtitle">Florida runs on wind, water, and sun</div>', '<div class="act-subtitle">Moving air and water can push</div>')
# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: Stop & Think (the drop race is Part 1’s thinking stop)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: Key Concept box (the games and the picture carry it)',
   r'<div style="background:#FFF6E5;border:2\.5px solid #F0C97A;[^"]*">\s*<div[^>]*>⭐ Key Concept</div>.*?</div>\s*', '', True)
fx('cut', 'removed: the Four Florida Power Sources tap diagram (its “coastal wind turbine” and “hydro pump” were wrong for Florida), Observe & Reason, the “1,500 homes” turbine fact, the “hurricane forecasting is our biggest wind farm” callout (not true) and Go Deeper (lean). Part 3 = the old Explore (the pinwheel test); the next button goes to Self-Check',
   r'<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">Four Florida Power Sources</h3>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 3 · The Pinwheel Test</h3>\n      ' + PS + 'Now test it like a scientist. A fan blows on a pinwheel. Change ONE thing at a time, the wind or the way the pinwheel faces, and count the spins yourself.</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its pinwheel steps are now Part 3; its “5 mph to 30 mph, how many times more pushy” puzzle, the turbine fact and Go Deeper go with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 5 removed (Bethany kept 6 and 7; Q5 named the removed diagram)', r'<div class="pq">\s*<span class="pq-num"[^>]*>5</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 6 and 7 answered')
fx('cut', 'lean: Part C typed on the page, plus the required sketch', 'A two-panel diagram showing a pinwheel pushed by wind and a water wheel pushed by water, with energy source and effect labeled.',
   'My model: a pinwheel pushed by wind and a waterwheel pushed by water, with the energy source and what it moves. Plus your labeled sketch.')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether wind has real energy, and supported it with two pieces of evidence.',
   '<strong>Use Your Evidence:</strong> My claim about whether wind is real energy, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Download your field journal (it has your answers and your sketch) and upload it to the Canvas assignment. Or copy your Gathered Answers (above) into Canvas.', True)

# ---------------------------------------------------------------- the story
SAM = Q['crew']['sam']
CANAL_SVG = ('<svg viewBox="0 0 300 150" role="img" aria-label="A drawing of houses along a still, green canal on a hot day."><rect width="300" height="150" fill="#CFE3EE"/>'
             '<circle cx="250" cy="30" r="16" fill="#F6D36B"/><path d="M20 92 V60 l30 -18 l30 18 V92z M110 92 V56 l34 -20 l34 20 V92z M200 92 V64 l26 -16 l26 16 V92z" fill="#7A6A58"/>'
             '<rect y="92" width="300" height="58" fill="#6E8A4E"/><path d="M0 108 h300 M0 126 h300" stroke="#58723C" stroke-width="2"/><path d="M60 104 l6 -4 l6 4 M180 120 l6 -4 l6 4" stroke="#3E4F2A" stroke-width="2" fill="none"/></svg>')
E1 = ('<svg viewBox="0 0 160 90" role="img" aria-label="A crayon-style drawing of a small windmill on a dock with a pipe into the water."><rect width="160" height="90" fill="#fff"/>'
      '<path d="M10 70 h90" stroke="#8A6B45" stroke-width="5"/><path d="M50 70 V25" stroke="#555" stroke-width="3"/><g stroke="#2D7AA6" stroke-width="4"><path d="M50 25 l-16 -12 M50 25 l18 -8 M50 25 l2 18 M50 25 l-18 8"/></g>'
      '<path d="M50 70 V84 h40" stroke="#2D7AA6" stroke-width="3" fill="none"/><path d="M0 80 q20 -4 40 0 t40 0 t40 0 t40 0" stroke="#4E86A8" stroke-width="3" fill="none"/><path d="M115 30 q8 -4 16 0 M112 40 q10 -4 20 0" stroke="#9CC3DA" stroke-width="3" fill="none"/></svg>')
E2 = ('<svg viewBox="0 0 160 90" role="img" aria-label="A crayon-style drawing of a waterwheel sitting in flat canal water."><rect width="160" height="90" fill="#fff"/>'
      '<circle cx="80" cy="52" r="24" fill="none" stroke="#8A6B45" stroke-width="4"/><path d="M80 28 v48 M56 52 h48 M63 35 l34 34 M97 35 l-34 34" stroke="#8A6B45" stroke-width="3"/>'
      '<rect y="66" width="160" height="24" fill="#6E8A4E" opacity=".7"/></svg>')
E3 = ('<svg viewBox="0 0 160 90" role="img" aria-label="A crayon-style drawing of a fan in the water with stars and the word magic."><rect width="160" height="90" fill="#fff"/>'
      '<circle cx="80" cy="45" r="18" fill="none" stroke="#C8553D" stroke-width="4"/><path d="M80 27 v36 M62 45 h36" stroke="#C8553D" stroke-width="4"/><rect y="62" width="160" height="28" fill="#4E86A8" opacity=".6"/>'
      '<path d="M30 20 l4 8 l8 1 l-6 6 l2 8 l-8 -4 l-7 4 l1 -8 l-6 -6 l8 -1z M130 18 l3 6 l6 1 l-4 4 l1 6 l-6 -3 l-5 3 l1 -6 l-4 -4 l6 -1z" fill="#F5B83D"/></svg>')
D = {
    'lesson': '23.02', 'week': 23, 'day': 2, 'guide': 'sam', 'prefix': 'g4sci-23-2', 'manifestKey': '23-02',
    'paths': P['paths'], 'crew': {'sam': SAM},
    'expedition': {'num': 23, 'title': 'The Still Canal'},
    'ambient': {'icon': '🌬️', 'label': 'Breezy dock'},
    'case': {
        'num': 23, 'title': 'The Still Canal (part 2)', 'style': 'gazette',
        'hook': 'The Gazette is back with a new job for me: judge their Bright Ideas contest. Pelican Canal needs its water moving, with no power bill. Which idea can really work?',
        'paper': {'name': 'The Palmetto Beach Gazette', 'date': 'Tuesday, June 16', 'price': '50¢',
                  'headline': 'Pelican Canal goes still and green', 'deck': 'Readers send Bright Ideas to get the water moving, with no power bill.',
                  'photo': {'svg': CANAL_SVG, 'cap': 'Pelican Canal on a hot afternoon (drawing).'},
                  'body': ['Pelican Canal is a dead end. Its water hardly moves, so on hot days it turns green and smelly.',
                           'Moving water picks up air at the surface, and fish need that air. Neighbors want to get the water moving without a power bill.'],
                  'entriesHead': 'Bright Ideas Contest: the entries', 'entryWord': 'ENTRY',
                  'entries': [{'n': 1, 'who': 'D. Lee', 't': 'A windmill on my dock', 'svg': E1, 'lines': ['The wind turns the blades. The blades work a pump that pushes canal water around.']},
                              {'n': 2, 'who': 'R. Ortiz', 't': 'A waterwheel in the canal', 'svg': E2, 'lines': ['The canal water will turn the wheel, and the wheel will stir the water.']},
                              {'n': 3, 'who': 'Pat, age 9', 't': 'A magic fan', 'svg': E3, 'lines': ['Put a fan in the water. It will spin forever and make its own energy. No wind needed!']}]},
        'stills': [],
        'question': 'Which Bright Idea can really get Pelican Canal’s water moving, and what makes it work best?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'tiles', 'icon': '🧩', 'where': 'Warm-Up: uncover the tiles', 't': 'Wind can do work. A farm windmill uses moving air to pump water, with no wires at all.'},
            {'id': 'droprace', 'icon': '🪶', 'where': 'The Lesson, Part 1: the drop race', 't': 'Air is real stuff. Moving air pushes on things, like the flat paper and the fan’s breeze.'},
            {'id': 'valve', 'icon': '🚰', 'where': 'The Lesson, Part 2: turn the valve', 't': 'A waterwheel turns only when water MOVES onto it. More moving water, faster wheel. A wheel can’t make its own energy.'},
            {'id': 'redblade', 'icon': '🌀', 'where': 'The Lesson, Part 3: count the red blade', 't': 'Stronger wind, hitting the blades head-on, made the pinwheel spin the most.'},
        ],
        'solve': {
            'title': 'Which Bright Idea wins?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Entry 2, the waterwheel. The canal water will turn it.', 'why': 'Check Clue 3. A waterwheel needs MOVING water to push it. Pelican Canal’s water hardly moves.'},
                {'t': 'Entry 1, the dock windmill, facing a strong, steady wind. Moving air pushes its blades, and the blades work the pump.', 'right': True,
                 'why': 'Case cracked! Moving air carries energy, and blades facing a strong wind spin fastest. Real ponds use windmill pumps just like this.'},
                {'t': 'Entry 3, the magic fan. It makes its own energy.', 'why': 'Check Clue 3. No wheel or fan makes its own energy. Moving air or water has to push it.'},
                {'t': 'None of them. Air is nothing, so wind can’t push a pump.', 'why': 'Check Clue 2. Air is real. The fan’s breeze pushed the paper right across.'},
            ]},
    },
    'tiles': {
        'afterText': 'Lift the tiles to find out', 'kicker': 'Warm-Up game', 'title': 'The mystery tower',
        'todo': ['Tap a tile to lift it (or swipe across the tiles).', 'Guess what the tower does.', 'Fewer tiles lifted = more stars.'],
        'img': I('windmill'), 'alt': 'A tall metal farm windmill with a wheel of blades, beside a round metal water tank in a green field. Water pours from a pipe into the tank.',
        'credit': 'Windmill on the Sheyenne National Grassland, North Dakota: USDA Forest Service, public domain, via Wikimedia Commons. Florida ranches and farms used the same kind.',
        'cols': 3, 'rows': 2, 'tileWord': 'tiles lifted', 'needTile': 'Lift one tile first, then guess.',
        'guessQ': 'What does the tower do?',
        'guesses': [{'t': 'It makes radio signals.', 'miss': 'Look for wires or antennas. Do you see any? Lift another tile.'},
                    {'t': 'Wind spins it, and it pumps water up from the ground.', 'ok': True},
                    {'t': 'It’s a lookout for spotting fires.', 'miss': 'Where would a person stand? Lift a tile near the bottom.'},
                    {'t': 'It’s a giant fan that blows wind.', 'miss': 'Is there a plug or a motor? What could be pushing those blades?'}],
        'starsLine': 'Solved! Tiles lifted: {n}.',
        'reveal': {'head': 'How a farm windmill works:', 'steps': [{'icon': '💨', 't': 'Wind pushes the blades'}, {'icon': '🌀', 't': 'The wheel spins'}, {'icon': '↕️', 't': 'A rod moves a pump up and down'}, {'icon': '💧', 't': 'Water pours into the tank'}]},
        'q': 'Where does the windmill get its energy?',
        'opts': [{'t': 'From the moving air pushing its blades.', 'ok': True},
                 {'t': 'It makes its own energy.', 'miss': 'Look at the steps. What pushes the blades first?'},
                 {'t': 'From the water in the tank.', 'miss': 'The water comes at the END. What starts it all?'}],
        'win': 'No wires, no plug: moving air did the work. Clue 1!'},
    'droprace': {
        'afterText': 'Try the drop race', 'kicker': 'Part 1 game', 'title': 'The drop race',
        'todo': ['Pick a pair.', 'Drag the 🏁 flag onto the one you think lands first (or tap it).', 'Press Let go! Drop all 3 pairs, then turn on the fan.'],
        'why': {'icon': '🪶', 'q': 'Why drop things?', 't': 'Falling things push through air. If air is real, it will push back.'},
        'model': 'a model: dropped from about 1 meter (3 feet)', 'flag': '🏁 Lands first', 'sameWord': 'Same time',
        'predictQ': 'Which lands first? Drag the flag onto your pick, or tap it.', 'dropBtn': '✋ Let go!', 'againBtn': '↺ Drop this pair again', 'needPredict': 'Predict first: drag the flag onto your pick.',
        'rightPre': 'You predicted it!', 'wrongPre': 'Surprise!',
        'pairs': [
            {'id': 'paper', 't': '📄 Flat paper vs. crumpled paper', 'a': {'icon': '📄', 't': 'Flat paper', 'fall': 2.2, 'flutter': True}, 'b': {'icon': '🗞️', 't': 'Same paper, crumpled', 'fall': 0.6}, 'first': 'b',
             'why': 'Same paper, same weight! The flat sheet pushes against lots of air, so the air pushes back up on it and slows it down.'},
            {'id': 'feather', 't': '🪶 Feather vs. rock', 'a': {'icon': '🪶', 't': 'Feather', 'fall': 3.0, 'flutter': True}, 'b': {'icon': '🪨', 't': 'Rock', 'fall': 0.5}, 'first': 'b',
             'why': 'The light, fluffy feather catches lots of air. The air pushes up on it, so it drifts down slowly.'},
            {'id': 'balls', 't': '⚾ Baseball vs. ping-pong ball', 'a': {'icon': '⚾', 't': 'Baseball', 'fall': 0.45}, 'b': {'icon': '🏓', 't': 'Ping-pong ball', 'fall': 0.47}, 'first': 'same',
             'why': 'Almost a tie! They are about the same size, so the air pushes on them about the same. Being heavy didn’t make the baseball much faster.'}],
        'fan': {'label': 'Round 2: a fan blows across', 'short': 'fan test', 'btn': '🌀 Fan on, let go!', 'lockLine': 'Drop all 3 pairs first.',
                'items': [{'icon': '📄', 't': 'Flat paper', 'fall': 2.2, 'drift': 120}, {'icon': '🪶', 't': 'Feather', 'fall': 2.4, 'drift': 150}, {'icon': '🗞️', 't': 'Crumpled', 'fall': 0.6, 'drift': 25}, {'icon': '🪨', 't': 'Rock', 'fall': 0.5, 'drift': 0}],
                'line': 'The moving air pushed the flat paper and the feather far to the side, but barely moved the rock. Air you can’t see did that!'},
        'q': 'What slowed the flat paper and pushed it sideways?',
        'opts': [{'t': 'Air. It is real stuff, and moving air pushes.', 'ok': True},
                 {'t': 'Nothing. Air is empty space.', 'miss': 'Then why did the flat paper and the crumpled paper fall differently?'},
                 {'t': 'The paper was heavier.', 'miss': 'It was the SAME paper. What was different?'}],
        'win': 'Air is real, and moving air pushes. Clue 2!'},
    'valve': {
        'afterText': 'Turn the valve and see', 'kicker': 'Part 2 game', 'title': 'Turn the valve',
        'todo': ['Drag the red valve handle around, or press Open and Close.', 'Watch the waterwheel, the stone and the lamp.', 'Close the valve all the way and press “Spin by itself”.'],
        'why': {'icon': '🚰', 'q': 'What is a valve?', 't': 'A valve is a handle that lets more or less water through a pipe, like a faucet.'},
        'model': 'a model',
        'levels': [{'k': 'off', 't': 'Closed', 'flow': 0, 'spin': 0, 'lamp': 0, 'wheelWord': 'Still', 'lampWord': 'Dark', 'note': 'No moving water. Nothing pushes the wheel.'},
                   {'k': 'low', 't': 'A little water', 'flow': 1, 'spin': 0.25, 'lamp': 0.25, 'wheelWord': 'Slow', 'lampWord': 'Dim', 'note': 'A little moving water gives the paddles a small push.'},
                   {'k': 'mid', 't': 'Half open', 'flow': 2, 'spin': 0.6, 'lamp': 0.6, 'wheelWord': 'Medium', 'lampWord': 'Brighter', 'note': 'More water hits the paddles, so the push is bigger.'},
                   {'k': 'high', 't': 'All the way open', 'flow': 3, 'spin': 1.1, 'lamp': 1, 'wheelWord': 'Fast', 'lampWord': 'Bright', 'note': 'Lots of moving water: the biggest push, the fastest wheel, the brightest lamp.'}],
        'openBtn': 'Open ↻', 'closeBtn': '↺ Close', 'handleLabel': 'Or drag the red valve handle around in a circle.',
        'spinBtn': '⚡ Spin by itself', 'spinNo': 'The wheel twitched and stopped. With no moving water, nothing pushes it. A wheel can’t make its own energy.',
        'spinYes': 'It is already spinning, because water is pushing it. Close the valve all the way, then try.',
        'tableLabel': 'My observations', 'cols': ['Water', 'Wheel', 'Lamp'],
        'taskLabel': 'Try all of these', 'tasks': {'self': 'Water off: press “Spin by itself”', 'low': 'Open it a little', 'high': 'Open it all the way'},
        'q': 'Where does the lamp’s energy come from?',
        'opts': [{'t': 'From the moving water, passed through the wheel.', 'ok': True},
                 {'t': 'The wheel makes it.', 'miss': 'Did the wheel make anything when the water was off?'},
                 {'t': 'The lamp makes it by itself.', 'miss': 'Did the lamp glow when the valve was closed?'}],
        'win': 'No moving water, no energy. More moving water, faster wheel. Clue 3!'},
    'redblade': {
        'afterText': 'count the spins yourself', 'kicker': 'Part 3 game', 'title': 'Count the red blade',
        'todo': ['Run Test 1 just as it is set.', 'Then change ONE thing: the wind, or the way the pinwheel faces.', 'Press Start. Tap every time the red blade passes the top, for 10 seconds.'],
        'why': {'icon': '🔬', 'q': 'Why only ONE change?', 't': 'If you change two things at once, you can’t tell which one made the difference. Scientists call this a fair test.'},
        'model': 'a slowed-down model', 'secs': 10, 'tol': 2,
        'base': {'wind': 'gentle', 'angle': 'head'},
        'winds': [{'k': 'gentle', 'icon': '🍃', 't': 'Gentle'}, {'k': 'strong', 'icon': '💨', 't': 'Strong'}],
        'angles': [{'k': 'head', 'icon': '🎯', 't': 'Head-on'}, {'k': 'side', 'icon': '↗️', 't': 'From the side'}],
        'rps': {'gentle-head': 0.6, 'strong-head': 1.4, 'gentle-side': 0.25, 'strong-side': 0.6},
        'windLabel': 'Wind:', 'angleLabel': 'The wind hits the pinwheel:',
        'startBtn': '▶ Start the 10-second test', 'tapBtn': '👆 Tap! Red blade at the top',
        'readyLine': 'Go! Tap every time the RED blade passes the top.',
        'countLine': 'You counted {n} spins (the model counted {m}). It goes in your table.',
        'recount': 'You counted {n}, but the model counted {m}. Try again, and watch only the red blade at the top.',
        'firstLine': 'Test 1 is the starting test: gentle wind, head-on. I set it for you. Press Start again.',
        'notFair': 'Not fair! You changed TWO things from Test 1. Change only ONE.',
        'sameAs': 'That’s the same as Test 1. Change ONE thing: the wind or the way it faces.',
        'tableLabel': 'My test table', 'cols': ['Test', 'Wind', 'Wind hits it', 'Spins I counted'],
        'q': 'What made the pinwheel spin the fastest?',
        'opts': [{'t': 'Strong wind hitting the blades head-on.', 'ok': True},
                 {'t': 'Wind hitting it from the side.', 'miss': 'Look at your table. Which test had the most spins?'},
                 {'t': 'The pinwheel spun by itself.', 'miss': 'What happened when the wind was gentle? Did it still spin the same?'}],
        'win': 'Stronger wind, facing the blades, means a bigger push and faster spins. Clue 4!'},
    'exploreMod': 'redblade',
    'zero': {
        'after': '.fs-solve', 'kicker': 'Case closed · Florida’s zero', 'title': 'How many wind farms?',
        'todo': ['Make your guess with the slider.', 'Read why.', 'Then tap each number on the real dam photo.'],
        'lockLine': 'Crack the case first.',
        'guessQ': 'Florida has ocean on three sides. How many wind farms (big groups of wind turbines that make electricity) does it have?',
        'max': 50, 'unit': 'wind farms', 'guessBtn': 'Check my guess', 'answer': 0, 'yourWord': 'Your guess: {g}', 'bigLabel': 'wind farms in Florida',
        'reasons': [{'icon': '🌬️', 't': 'Most days, Florida’s wind is gentle. Big turbines need strong wind almost all the time.'},
                    {'icon': '🌀', 't': 'Florida’s strongest winds come in hurricanes. Those come only once in a while, and they are too wild for turbines.'},
                    {'icon': '☀️', 't': 'So Florida makes more and more of its electricity from sunlight instead.'},
                    {'icon': '💧', 't': 'Florida DOES use moving water: one dam on the Apalachicola River makes electricity. Look!'}],
        'photoHead': 'The Jim Woodruff Dam, on the Apalachicola River at the Florida–Georgia line. Tap each number.',
        'img': I('dam'), 'alt': 'An airplane view of a long concrete dam across a wide blue lake, with a powerhouse building on the right and the river below.',
        'credit': 'Jim Woodruff Lock and Dam: U.S. Army Corps of Engineers, public domain, via Wikimedia Commons.',
        'spots': [{'n': 1, 'x': 50, 'y': 15, 'label': 'Lake Seminole', 't': 'The dam holds the river back, so this lake sits higher than the river below.'},
                  {'n': 2, 'x': 72, 'y': 45, 'label': 'The powerhouse', 't': 'Water rushes down through big pipes inside. It pushes the blades of wheels called turbines, and they spin.'},
                  {'n': 3, 'x': 66, 'y': 58, 'label': 'Water out', 't': 'After it pushes the turbines, the water flows on down the Apalachicola River.'},
                  {'n': 4, 'x': 89, 'y': 47, 'label': 'The switchyard', 't': 'The spinning turbines turn generators. The electricity leaves here on power lines.'}],
        'spotWord': 'spots', 'win': 'Moving water pushes turbines, and Florida gets electricity. That’s water energy at work!'},
    'windribbon': {
        'after': '.fs-solve', 'kicker': 'Case closed · when to pump', 'title': 'The wind ribbon',
        'todo': ['Drag the time slider (or press ◀ ▶) through one summer day on the dock.', 'Watch the ribbon and the windmill.', 'Then pick the best time to pump.'],
        'lockLine': 'Crack the case first.',
        'why': {'icon': '🎀', 'q': 'What does the ribbon show?', 't': 'A ribbon on a pole points the way the wind blows. The stronger the wind, the straighter it stands out.'},
        'model': 'a model of one summer day', 'minMph': 7, 'need': 6, 'needWord': 'times of day checked',
        'pumpYes': 'The windmill is pumping.', 'pumpNo': 'Too gentle: this windmill needs about 7 mph to pump.',
        'hours': [{'h': 6, 'label': '6 AM', 'mph': 3, 'from': 'land', 'fromWord': 'from the land', 'note': 'A light breeze drifts from the land out over the water. At night the land cooled off more than the water.'},
                  {'h': 9, 'label': '9 AM', 'mph': 4, 'from': 'calm', 'fromWord': '', 'note': 'Almost still. The Sun is warming the land.'},
                  {'h': 12, 'label': '12 noon', 'mph': 8, 'from': 'sea', 'fromWord': 'from the water', 'note': 'The sea breeze starts! The land is now warmer than the water.'},
                  {'h': 15, 'label': '3 PM', 'mph': 13, 'from': 'sea', 'fromWord': 'from the water', 'note': 'The sea breeze is strongest. Warm air rises over the hot land, and cooler air from the water rushes in.'},
                  {'h': 18, 'label': '6 PM', 'mph': 9, 'from': 'sea', 'fromWord': 'from the water', 'note': 'Still breezy, but the land is starting to cool.'},
                  {'h': 21, 'label': '9 PM', 'mph': 4, 'from': 'calm', 'fromWord': '', 'note': 'After sunset, the breeze fades.', 'dark': True}],
        'pickQ': 'When will the dock windmill pump the most water?',
        'picks': [{'t': '6 AM', 'miss': 'Check the ribbon at 6 AM. Is the wind strong enough?'},
                  {'t': '9 AM', 'miss': 'Check 9 AM again. How many mph?'},
                  {'t': '3 PM', 'ok': True},
                  {'t': '9 PM', 'miss': 'What happens to the breeze after sunset?'}],
        'q': 'Why is it windiest in the afternoon?',
        'opts': [{'t': 'The Sun heats the land faster than the water, so cooler air from the water rushes in.', 'ok': True},
                 {'t': 'The windmill makes the wind.', 'miss': 'Did the windmill spin when the air was still?'},
                 {'t': 'The water pushes the air.', 'miss': 'Read the 3 PM note again. What is the Sun doing?'}],
        'win': 'Florida’s afternoon sea breeze: the best time for the dock windmill!'},
    'sail': {
        'after': '.fs-solve', 'kicker': 'Bonus game', 'title': 'Sail the canal',
        'todo': ['Pick a level.', 'Turn the sail (drag on the canal, the slider, or ⟲ ⟳) so the wind fills it.', 'Press Sail! Keep turning it if the wind changes. Get to the dock fast for 3 stars.'],
        'lockLine': 'Crack the case first.', 'model': 'a simple model', 'goBtn': '⛵ Sail!',
        'stuckLine': 'Stuck! Turn the sail so the wind fills it.', 'doneLine': 'Docked in {t} seconds! {s}',
        'levels': [{'t': 'Level 1: wind behind', 'line': 'The wind blows down the canal, behind the boat.', 'winds': [{'at': 0, 'dir': 0, 's': 1}]},
                   {'t': 'Level 2: wind from the side', 'line': 'The wind blows at a slant. Turn the sail to face it.', 'winds': [{'at': 0, 'dir': -40, 's': 1}]},
                   {'t': 'Level 3: the wind shifts', 'line': 'Halfway down, the wind changes! Watch the arrows.', 'winds': [{'at': 0, 'dir': 35, 's': 1}, {'at': 0.5, 'dir': -35, 's': 1}]}],
        'win': 'All three levels! A sail is a big blade for catching moving air.'},
    'fold': {'sail': {'icon': '⛵', 'tease': 'Steer a little sailboat to the dock by turning the sail to catch the wind.', 'open': 'Play'}},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Think about Turn the Valve. Did the wheel make its own energy?', 'C': 'Think about the red blade test. What did stronger wind do?'},
        'q2': {'A': 'Think about the pinwheel. It still needed blades to catch the wind.', 'B': 'Think about Florida’s zero. Florida uses natural gas and sunlight, too.'},
        'q3': {'B': 'A gray sky doesn’t show a push. What moves when the wind pushes it?', 'C': 'Wet ground doesn’t show a push. What moves when the wind pushes it?'}},
    'flags': {
        'ans-2': [
            {'label': 'model', 're': 'model|modle|modal|small version|smaller|mini|tiny|copy'},
            {'label': 'wind spins it', 're': 'wind|air|blow|push|spin|turn'}],
        'ans-3': [
            {'label': 'renewable: doesn’t run out', 're': 'renew|run out|runs out|never end|keep|again|always|forever|use.? ?up|used up|come back'},
            {'label': 'a Florida example', 're': 'dam|apalach|river|sail|boat|windmill|pump|cattle|farm|electric|florida'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|is real|isn|is not|does do|it does'},
            {'label': 'two pieces of evidence', 'any': ['paper', 'feather', 'fall', 'drop', 'fan', 'push', 'pinwheel', 'windmill', 'pump', 'wheel', 'spin', 'blade', 'red', 'count', 'stronger', 'sail', 'tank', 'water'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-2': 15, 'ans-3': 15, 'cer-4': 30},
    'hints': {
        'ans-2': ['Think about Count the Red Blade: what made the pinwheel spin?', 'A MODEL is a small version of something real. What real thing is a pinwheel like?', 'Try: A pinwheel is a model of a wind turbine because ___. Both spin when ___.'],
        'ans-3': ['Does the wind ever get used up?', 'Think about Florida’s zero: what does the dam on the Apalachicola River do?', 'Try: Wind and water are renewable because ___. Florida uses ___ to ___.'],
        'cer-4': ['First decide: does moving air do anything?', 'Think about the flat paper, the fan and your red blade counts.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'In the drop race, the air pushed up on the flat paper, so it fell slower than the crumpled paper.',
                'The fan’s moving air pushed the flat paper and the feather far to the side.',
                'In my pinwheel test, stronger wind made the red blade spin more times.',
                'You can’t see air, so it can’t do anything.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · the still canal', 'length': '20–30 s'},
        'warmup': {'label': 'Warm-Up · the mystery tower (Clue 1)', 'length': '15–20 s',
                   'script': 'Sam here. I’m judging the Gazette’s Bright Ideas contest. Read the three entries first. Then, a mystery tower! Lift one tile at a time, and guess what it does. Fewer tiles, more stars.'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Blow on your hand for “wind energy”.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · the drop race (Clue 2)', 'length': '15–20 s',
                  'script': 'Can air push anything? Let’s test it. Pick a pair, then drag the flag onto the one you think lands first. Press Let go, and watch. Drop all three pairs, then turn on the fan.'},
        'part2': {'label': 'Part 2 · turn the valve (Clue 3)', 'length': '20–30 s'},
        'explore': {'label': 'Part 3 · count the red blade (Clue 4)', 'length': '15–20 s',
                    'script': 'Time for a fair test. Run Test 1 first. Then change only ONE thing: the wind, or the way the pinwheel faces. Press Start, and tap each time the red blade passes the top. Your counts fill the table.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · my wind and water model', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '15–20 s',
                     'script': 'A classmate says wind isn’t real energy. Is that true? Think about the flat paper, the fan, and your pinwheel counts. Pick your side, tap two pieces of evidence, then explain. That’s your C-E-R.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 24.01 (heat).'},
    },
    'videoOff': [],
    'lensVoice': False,
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'The three contest entries (Warm-Up)',
        'The flat paper drifting down (The Lesson)',
        'The lamp at its brightest (The Lesson)',
        'Your pinwheel table with 3 tests (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['The dock windmill', 'A spinning pinwheel', 'A waterwheel'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch and label your wind and water model', 'required': True, 'minLabels': 3,
                           'prompts': ['Draw the wind pushing a pinwheel', 'Draw water pushing a waterwheel', 'Label what moves and what gets pushed']}]},
    'hlCoach': copy.deepcopy(Q['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🎀', 'name': 'The Bright Idea ribbon',
                 'line': 'You cracked Case 23, part 2, and the contest’s Bright Idea ribbon goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next time: heat.'},
    'notebookTitle': 'Unit 5 · Energy, Motion & Collisions',
    'notebook': copy.deepcopy(O['notebook']),
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. Let the wind blow!',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to see what it means.']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '#tab-vocab p', 'text': 'What does moving air or moving water push near you?'},
         'label': 'Warm-Up: pushes around me', 'q': 'Warm-Up: Three things moving air or moving water pushes near you.', 'title': 'Pushes around me', 'compact': True,
         'fields': [{'t': 'Push 1', 'icon': '💨', 'ph': 'Moving ___ pushes the ___.'},
                    {'t': 'Push 2', 'icon': '💨', 'ph': 'Moving ___ pushes the ___.'},
                    {'t': 'Push 3', 'icon': '💧', 'ph': 'Moving ___ pushes the ___.'}]},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Fill in your model below'},
         'label': 'Part C: My wind and water model', 'q': 'Part C: My wind and water model (what moves, what gets pushed, what makes it faster)', 'title': 'My wind and water model',
         'fields': [{'t': 'Wind panel: what moves and what gets pushed', 'icon': '💨', 'ph': 'Moving ___ pushes the ___ of the pinwheel.'},
                    {'t': 'Wind panel: what makes it spin faster', 'icon': '🌀', 'ph': 'It spins faster when ___.'},
                    {'t': 'Water panel: what moves and what gets pushed', 'icon': '💧', 'ph': 'Moving ___ pushes the ___ of the waterwheel.'},
                    {'t': 'Water panel: what makes it spin faster', 'icon': '🚰', 'ph': 'It spins faster when ___.', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Is wind real energy that can do something?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-2': 'Part B · Question 6', 'ans-3': 'Part B · Question 7', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] == '23.02': n.update({'icon': '🎀', 'name': 'The Bright Idea ribbon'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'Moving air and moving water push on blades, and a bigger push makes the wheel spin faster.',
    'key': ['moving', 'air', 'water', 'push', 'bigger', 'faster', 'spin'],
    'small': ['and', 'on', 'a', 'the', 'makes'],
    'model': 'A scientist might highlight “moving air”, “moving water”, “bigger push” and “faster”. Those words hold the big idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me explain how moving air or water does work, or what makes a wheel spin faster?']

EV = '#tab-assignment .act-body > div:has(> .fs-plan)'
D['cues'] = {
    'warmup': [{'at': '^contest', 'sel': '.fs-gaz', 'fx': 'glow', 'scroll': True},
               {'at': '^entries', 'sel': '.fs-ent-row', 'fx': 'pop'},
               {'at': '^tower', 'sel': '.fs-tl-box', 'fx': 'glow', 'scroll': True},
               {'at': '^tile', 'sel': '.fs-tl-t', 'i': 0, 'fx': 'point'},
               {'at': '^guess', 'sel': '.fs-tl-gq', 'fx': 'pop'}],
    'part1': [{'at': '^pair', 'sel': '.fs-drp-tabs', 'fx': 'glow', 'scroll': True},
              {'at': '^flag', 'sel': '.fs-drp-flag', 'fx': 'point'},
              {'at': '^let', 'sel': '.fs-drp-go', 'fx': 'point'},
              {'at': '^fan', 'sel': '.fs-drp-fan', 'fx': 'pop'}],
    'explore': [{'at': '^test', 'sel': '.fs-rb-svg', 'fx': 'glow', 'scroll': True},
                {'at': '^wind', 'sel': '.fs-rb-set', 'i': 0, 'fx': 'pop'},
                {'at': '^faces', 'sel': '.fs-rb-set', 'i': 1, 'fx': 'pop'},
                {'at': '^start', 'sel': '.fs-rb-start', 'fx': 'point'},
                {'at': '^tap', 'sel': '.fs-rb-tap', 'fx': 'point'},
                {'at': '^table', 'sel': '.fs-game[data-mod="redblade"] .fs-vlv-tab', 'fx': 'pop'}],
    'evidence': [{'at': '^classmate', 'sel': EV + ' > p', 'i': 0, 'fx': 'trace', 'scroll': True},
                 {'at': '^paper', 'sel': '.fs-plan .fs-opt', 'i': 2, 'fx': 'glow'},
                 {'at': '^fan', 'sel': '.fs-plan .fs-opt', 'i': 3, 'fx': 'glow'},
                 {'at': '^pinwheel', 'sel': '.fs-plan .fs-opt', 'i': 4, 'fx': 'glow'},
                 {'at': '^side', 'sel': '.fs-plan .fs-plan-row', 'i': 0, 'fx': 'pop'},
                 {'at': '^explain', 'sel': '.fs-cer .fs-cer-row', 'i': 2, 'fx': 'glow', 'scroll': True}],
}
D['cueWords'] = json.load(open('cuewords.json', encoding='utf-8')) if os.path.exists('cuewords.json') else {}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
clips = {k: v['script'] for k, v in D['slots'].items() if v.get('script')}
tot = sum(len(t) for t in clips.values())
for k, t in clips.items(): print(f'  {k:10} {len(t):4}')
print(f'this page: {tot} / 1400 credits ({tot/1400:.0%})')
assert tot <= 1330
