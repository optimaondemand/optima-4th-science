#!/usr/bin/env python3
"""Writes data.json and fixes.json for 17.02 (run from this folder). Case 17 part 2 "The House That Stood" (June Calloway, Palmetto Springs).
New modules: mitsort, buildhouse, fixtown; case.style 'permit' (a building permit notice + a real photo print). Reuses D.townmap from 17-01."""
import json, copy, sys
sys.path.insert(0, '../17-01')
from townmap import MAP
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../17-01/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

# ---------------------------------------------------------------- ticked fixes (Bethany, 22 Oct 2026)
fx('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist already asks for a mitigation plan',
   '🎨 Part C &mdash; Build Your Own Food Chain', '🛡️ Part C &mdash; Design a Mitigation Plan')
fx('fix', 'copy-paste leftover: Part C task from 9.01 (typed on the page now; a sketch is a bonus)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   "Pick one Florida hazard (hurricane wind, wildfire, urban flooding or coastal erosion). Plan like an engineer: criteria, a constraint, one built and one natural solution, the winner and a revision.</p>", True)
fx('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'this is an Earth science lesson (4-ESS3), not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Earth Science</div>')
fx('fix', 'wrong quarter in the closing: this is the last Unit 4 lesson (review days next), not the end of Quarter 3',
   "<p><strong>You've closed out Quarter 3.</strong>", "<p><strong>You’ve finished the Unit 4 lessons.</strong>")
fx('fix', 'wrong caption: the image shows the seawall winning on safety, so mangroves don’t win “across all three criteria”',
   'The decision matrix shows that the smaller natural solution actually scores higher across all three criteria — then a revision adds a backup for the slowest one.',
   'The natural solution scores higher overall, even though the seawall wins on safety. Then a revision adds a backup while the mangroves grow.')
fx('fix', 'shaky fact: “wind-buffer trees” don’t protect homes in a hurricane; the safer advice is wind-resistant trees planted away from the house',
   'SOLUTION B: Plant wind-buffer trees and improve neighborhood landscaping.', 'SOLUTION B: Plant wind-resistant trees (like live oaks and sabal palms) away from the house, and trim dead branches before storm season.')
fx('fix', 'shaky fact (same diagram, the revision line)', 'with wind-buffer landscaping (natural) so homes are protected by both.', 'with wind-resistant trees planted away from the house (natural) so homes are protected by both.')
fx('fix', 'plain and accurate: wetlands are protected by law, so you can’t just fill one in', "(you can't bulldoze a wetland, for example)", '(you can’t just fill in a protected wetland, for example)')

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; dash removed',
   "Hold this question in your head as you work. By the end of the lesson, you'll be able to compare two ways to protect a Florida community from one natural hazard — and choose and revise the best plan.",
   "Keep this question in mind. By the end, you’ll be able to compare two ways to protect a Florida town from a natural hazard, then choose and revise the best plan.")
fx('plain', 'dash removed',
   "A small Florida coastal town keeps getting hit by hurricane storm surge — ocean water pushing inland and flooding streets and homes. Engineers have two ideas for what to do:",
   "A small Florida coastal town keeps getting hit by storm surge: ocean water pushed onto land by hurricanes, flooding streets and homes. Engineers have two ideas:")
fx('plain', 'a lead-in line for the photo game (the warm-up looks at real houses first)',
   "<li><strong>Idea B:</strong> Restore the mangrove forests and dunes that used to protect this coastline.</li>\n      </ul>",
   "<li><strong>Idea B:</strong> Restore the mangrove forests and dunes that used to protect this coastline.</li>\n      </ul>\n      <p>Before you choose for a whole town, look at what a real storm did to real houses.</p>")
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', 'dash removed; shorter',
   "Mitigation isn't about stopping nature — you can't stop a hurricane. It's about lowering the harm by being ready: stronger buildings, better drainage, smarter rules, healthy natural barriers. Florida communities use a mix of all of these.",
   "Mitigation isn’t about stopping nature. You can’t stop a hurricane! It’s about lowering the harm by being ready. Florida towns use a mix of three kinds:")
fx('plain', 'dash removed', 'mangrove forests, sand dunes, healthy wetlands — they all absorb storm energy.', 'mangrove forests, sand dunes and healthy wetlands soak up the energy of storm waves.')
fx('plain', 'dash removed', '<li><strong>Compare solutions</strong> in a decision matrix — same as the resource lessons.</li>', '<li><strong>Compare solutions</strong> in a decision matrix, like the one below.</li>')
fx('plain', 'the diagram is Part 3 now', 'margin-top:22px;">Four Hazard Mitigation Challenges</h3>', 'margin-top:22px;">Part 3 · Four Hazard Mitigation Challenges</h3>')
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'shorter closing; points to the review days',
   "That's real engineering — and it's the same thinking you'll bring to bigger and bigger problems as you move through the year.</p>",
   "That’s real engineering. Next come two review days, starting with a mystery on Main Street.</p>")

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: Stop & Think (the shelves game is the thinking stop for Part 1)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: the Watch out box (the CER asks the same question)', r'<p><strong>Common misconception:</strong> Some people think the bigger.*?</p>\s*', '', True)
fx('cut', 'lean: the Key Concept box repeats Part 1', r'<div style="background:#FFF6E5;border:2.5px solid #F0C97A;[^"]*">\s*<div[^>]*>⭐ Key Concept</div>\s*<p[^>]*>.*?</p>\s*</div>\s*', '', True)
fx('cut', 'lean: Stop & Reason (one thinking stop per tab)', r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its matrix task becomes Part C; the 72-hour fact and the 100-year flood Go Deeper go with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: Observe & Reason, the mangrove fact, the Andrew callout and Go Deeper at the end of the Lesson (the first two had shaky numbers); Part 4 = the old Explore; next button goes to Self-Check',
   r'<div class="socratic-q">\s*<span class="sq-icon">👀</span>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 4 · Fix the Whole Town</h3>\n      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">The Riveras have a plan. Now the town council asks June: what about everything else that broke on Storm Night? Open each problem on the map and pick the fix that would help most.</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 5 removed (Bethany kept 6 and 7; Part C asks for criteria and a constraint)', r'<div class="pq">\s*<span class="pq-num"[^>]*>5</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: renumber Part B (6 → 5)', '<span class="pq-num" style="background:#D4772C;">6</span>', '<span class="pq-num" style="background:#D4772C;">5</span>')
fx('cut', 'lean: renumber Part B (7 → 6)', '<span class="pq-num" style="background:#D4772C;">7</span>', '<span class="pq-num" style="background:#D4772C;">6</span>')
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C typed on the page; the sketch is a bonus',
   "A hazard mitigation plan with a decision matrix (1 built + 1 natural solution), criteria, constraints, a winner, and a revision suggestion.",
   "A mitigation plan for one Florida hazard: criteria, a constraint, a built and a natural solution, the winner and a revision. (A matrix sketch is a bonus.)")
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether the tallest wall is the only protection, and supported it with two pieces of evidence from the lesson.',
   '<strong>Use Your Evidence:</strong> My claim about whether the tallest wall is the only way to protect a town, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', True)

# ---------------------------------------------------------------- the story
I = lambda n: 'images/17-02-' + n + '.jpg'
PHOTO_CREDIT = 'Damaged houses after Hurricane Michael, Mexico Beach, Florida, 14 October 2018: Voice of America (VOA), via Wikimedia Commons'
SHELF_CREDIT = ('Storm shutters, Vero Beach, 2004: Mark Wolfe, FEMA (public domain). Hurricane straps at a Habitat for Humanity home, Pensacola, 2008: U.S. Navy photo by Gary Nichols (public domain). '
                'Mangrove shoreline, Biscayne National Park: National Park Service (public domain). Sea oats on a sand dune, John U. Lloyd Beach State Park: Georgialh, CC BY-SA 4.0, via Wikimedia Commons. '
                'Evacuation route sign near Boca Raton: Juliancolton (public domain), via Wikimedia Commons.')

D = {
    'lesson': '17.02', 'week': 17, 'day': 2, 'guide': 'june', 'prefix': 'g4sci-17-2', 'manifestKey': '17-02',
    'paths': P['paths'], 'crew': Q['crew'],
    'expedition': {'num': 17, 'title': 'The House That Stood'},
    'ambient': {'icon': '🌊', 'label': 'Ocean sounds'},
    'townmap': MAP,
    'case': {
        'num': '17 · part 2', 'title': 'The House That Stood', 'style': 'permit',
        'hook': 'It’s June. Storm Night is over, and the Rivera family has to rebuild their house on Bay Street. Remember the Mexico Beach photos? A few houses were still standing. The Riveras asked me: how do we build a house that stands up to the next storm? Let’s find out, then design one.',
        'notice': {'head': 'Building permit · Palmetto Springs', 'title': 'Rebuild the Rivera house, 214 Bay Street',
                   'rows': [['What happened', 'On Storm Night, seawater filled the house 4 feet deep. The family had evacuated and was safe.'],
                            ['Town rule', 'A new house on Bay Street must keep its floor above the storm-surge line.'],
                            ['Budget', '7 coins for storm protection (pretend money for this lesson).']],
                   'line': 'The town signs the permit when the plan passes the storm tests.'},
        'stills': [{'cam': 'Mexico Beach, Florida', 'time': 'four days after Hurricane Michael', 'tag': '📷 Real place', 'kind': 'print', 'img': I('raised-houses'),
                    'alt': 'Two beach houses still standing after Hurricane Michael. A window is covered with wood boards, a blue tarp covers part of a roof, and the deck and steps below are broken.'}],
        'stillsCredit': PHOTO_CREDIT + ' (public domain). The Riveras, Palmetto Springs and the permit are made up for this lesson.',
        'question': 'How should the Riveras rebuild so their house stands up to the next storm?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'raised', 'icon': '📷', 'where': 'Warm-Up: what helped, what failed?', 't': 'The storm hit hardest near the ground: waves broke the deck and steps. Boards kept a window safe, but wind tore up part of a roof.'},
            {'id': 'mitsort', 'icon': '🧱', 'where': 'The Lesson, Part 1: three kinds of mitigation', 't': 'There are three kinds of mitigation: built (shutters, roof straps), natural (mangroves, dunes) and planning (evacuation routes, storm plans).'},
            {'id': 'buildhouse', 'icon': '🏗️', 'where': 'The Lesson, Part 2: build it, then storm it', 't': 'The house stood when its floor was on deep pilings above the surge, its roof was strapped down and its windows were covered, all inside the budget.'},
            {'id': 'fixtown', 'icon': '🗺️', 'where': 'The Lesson, Part 4: fix the whole town', 't': 'One fix can’t solve every problem. Palmetto Springs needs a mix of built, natural and planning fixes.'},
        ],
        'solve': {
            'title': 'How should the Riveras rebuild?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Build the same house again, just bigger.', 'why': 'Check Clue 1. Where did the storm do the most damage?'},
                {'t': 'Build a tall wall around the house. That’s all it needs.', 'why': 'Check Clue 3. What did the house need to pass every test?'},
                {'t': 'Raise it on deep pilings above the surge, strap the roof down, cover the windows, stay inside the budget, and test the plan first. One fix isn’t enough.', 'right': True,
                 'why': 'Case cracked! You combined several kinds of mitigation and tested your design, just like real engineers. Now write your case report: it’s the questions below.'},
            ]},
    },
    'photos': [{
        'id': 'raised', 'clue': 'raised', 'afterText': 'look at what a real storm did to real houses', 'kicker': 'Warm-Up game · a real Florida street', 'short': 'Mexico Beach houses',
        'title': 'What helped? What failed?',
        'todo': ['Tap each number on the photo and read what happened there.', 'Then match each clue to a number.'],
        'why': {'icon': '📷', 'q': 'Where is this?', 't': 'Mexico Beach, Florida, four days after Hurricane Michael. These houses are still standing, but the storm hit them hard.'},
        'img': I('raised-houses'), 'alt': 'Two beach houses still standing after Hurricane Michael. A window is covered with wood boards, a blue tarp covers part of a roof, and the deck and steps below are broken.',
        'credit': PHOTO_CREDIT, 'license': 'Public domain',
        'hotspots': [
            {'n': 1, 'x': 28, 'y': 25, 'label': 'Boards on the window', 't': 'Before the storm, someone covered this window with plywood boards. Boards stop flying branches and trash from breaking the glass. The window made it.'},
            {'n': 2, 'x': 60, 'y': 21, 'label': 'Blue tarp on the roof', 't': 'The wind tore up part of this roof. A blue tarp keeps the rain out until it can be fixed. This roof needed a stronger tie-down.'},
            {'n': 3, 'x': 45, 'y': 57, 'label': 'The fallen deck', 't': 'The deck under the house fell down. Waves and storm surge hit hardest close to the ground.'},
            {'n': 4, 'x': 22, 'y': 80, 'label': 'Broken steps', 't': 'Waves broke these concrete steps and blocks apart and pushed them around.'}],
        'task': {'q': 'Match each clue to a number on the photo.', 'win': 'The storm hit hardest near the ground, and wind went after the roof. That’s a clue.',
                 'items': [{'icon': '🪵', 'step': 'Something that protected the house', 'ans': 1, 'evid': 'Plywood boards kept a window from breaking.'},
                           {'icon': '💨', 'step': 'Damage from strong wind', 'ans': 2, 'evid': 'The wind tore up part of a roof.'},
                           {'icon': '🌊', 'step': 'Damage from waves near the ground', 'ans': [3, 4], 'evid': 'Waves broke the deck and steps near the ground.'}]}}],
    'mitsort': {
        'afterText': 'Florida towns use a mix of three kinds', 'kicker': 'Part 1 game', 'title': 'Three kinds of mitigation',
        'todo': ['Drag each card onto its shelf (or tap a card, then a shelf).', 'Then answer the question.'],
        'shelves': [{'k': 'built', 'icon': '🧱', 't': 'Built', 'sub': 'things people build'},
                    {'k': 'natural', 'icon': '🌿', 't': 'Natural', 'sub': 'living things and land that slow storms'},
                    {'k': 'plan', 'icon': '📋', 't': 'Planning', 'sub': 'plans and rules people follow'}],
        'cards': [
            {'id': 'shutters', 'img': I('mit-shutters'), 'alt': 'Dark wooden shutters closed over two tall windows of a yellow house.', 't': 'Storm shutters over windows', 'k': 'built',
             'why': 'People hang shutters so flying trash can’t break the windows.', 'miss': 'Shutters are made and put up by people. Which shelf is for things people build?'},
            {'id': 'straps', 'img': I('mit-straps'), 'alt': 'A builder hammers nails into the wooden frame of a new house’s roof.', 't': 'Metal hurricane straps that tie the roof to the walls', 'k': 'built',
             'why': 'Florida’s building code says new houses need roof ties like these, so wind can’t lift the roof off.', 'miss': 'Builders nail these into the house. Which shelf is that?'},
            {'id': 'mangroves', 'img': 'images/r4-2-mangroves.jpg', 'alt': 'Mangrove trees with tangled roots growing along calm water.', 't': 'A mangrove shoreline', 'k': 'natural',
             'why': 'Tangled mangrove roots slow down waves before they reach land.', 'miss': 'Mangroves are living trees. Which shelf is for living things?'},
            {'id': 'dune', 'img': 'images/r4-2-dune.jpg', 'alt': 'Sea oats growing on a sandy dune.', 't': 'Sand dunes held by sea oats', 'k': 'natural',
             'why': 'Waves hit the dune first. Sea oat roots hold the sand in place.', 'miss': 'Dunes and sea oats are land and plants. Which shelf is that?'},
            {'id': 'evac', 'img': I('mit-evac'), 'alt': 'A blue Evacuation Route sign with an arrow, next to palm trees.', 't': 'Evacuation route signs', 'k': 'plan',
             'why': 'Signs show the safest roads away from the coast. A plan keeps people safe even when buildings can’t.', 'miss': 'The sign is part of a plan that tells people where to go. Which shelf is that?'},
            {'id': 'kit', 'icon': '📋', 't': 'A family storm plan: where to go, what to pack, who to call', 'k': 'plan',
             'why': 'A plan made before storm season helps a family leave quickly and safely.', 'miss': 'This is something a family decides ahead of time. Which shelf is that?'}],
        'doneLine': 'Every card is on a shelf.',
        'q': 'Why do Florida towns use all three kinds?',
        'opts': [{'t': 'Each kind protects in a different way, so together they cover more.', 'ok': True},
                 {'t': 'One kind always works best, so towns try to find it.', 'miss': 'If one kind always worked best, would towns bother with the others?'},
                 {'t': 'Natural mitigation is free, so it doesn’t count.', 'miss': 'Planting and caring for dunes and mangroves takes work and money, too.'}],
        'credit': SHELF_CREDIT,
        'win': 'Built, natural and planning: three kinds of mitigation. That’s a clue.',
        'clue': 'mitsort'},
    'buildhouse': {
        'afterText': 'then compare at least two possible solutions', 'kicker': 'Part 2 game', 'title': 'Build it, then storm it',
        'todo': ['Pick a foundation, windows and a roof for the Riveras’ house. Each ● costs a coin.', 'Press Run the storm. If a test fails, change one part and run it again.'],
        'why': {'icon': '🏠', 'q': 'A real house that stood', 't': 'In Mexico Beach, the “Sand Palace” sat on 40-foot pilings, with its first floor 15 feet up, strong concrete walls and few windows. It stood while most houses around it were destroyed.'},
        'budget': 7, 'unit': 'coins', 'budgetLabel': 'Budget', 'surge': 8, 'wind': 130, 'surgeLabel': 'Storm surge: 8 ft',
        'parts': [
            {'k': 'foundation', 'icon': '🏗️', 't': 'Foundation', 'opts': [
                {'k': 'slab', 't': 'On the ground', 'cost': 1, 'pass': False, 'note': 'The floor sits right on the ground. It’s cheap, but any flood water comes right in.'},
                {'k': 'posts', 't': 'Short posts (4 ft up)', 'cost': 3, 'pass': False, 'note': 'Better, but the storm surge here reaches 8 feet.'},
                {'k': 'pilings', 't': 'Deep pilings (10 ft up)', 'cost': 4, 'pass': True, 'note': 'Long poles driven deep into the ground lift the floor above the surge. Water flows underneath.'}]},
            {'k': 'windows', 'icon': '🪟', 't': 'Windows', 'opts': [
                {'k': 'plain', 't': 'Plain glass', 'cost': 0, 'pass': False, 'note': 'Flying branches can break plain glass. Then wind and rain rush in.'},
                {'k': 'shutters', 't': 'Storm shutters', 'cost': 1, 'pass': True, 'note': 'Shutters close over the glass before a storm.'},
                {'k': 'impact', 't': 'Impact glass', 'cost': 3, 'pass': True, 'note': 'Extra-strong glass that doesn’t shatter. Nothing to close before a storm, but it costs more.'}]},
            {'k': 'roof', 'icon': '🔩', 't': 'Roof', 'opts': [
                {'k': 'nails', 't': 'Nails only', 'cost': 0, 'pass': False, 'note': 'The roof is held on only by nails.'},
                {'k': 'straps', 't': 'Hurricane straps', 'cost': 1, 'pass': True, 'note': 'Metal straps tie the roof to the walls so wind can’t lift it.'}]}],
        'tests': [
            {'part': 'foundation', 'icon': '🌊', 't': 'Stays dry in an 8-foot surge', 'pass': 'The floor is 10 feet up. The surge flowed under the house.', 'fail': 'Seawater came inside. The floor is below the 8-foot surge line.'},
            {'part': 'windows', 'icon': '🪟', 't': 'Windows hold against flying branches', 'pass': 'The covered windows didn’t break.', 'fail': 'A flying branch broke the glass. Wind and rain blew inside.'},
            {'part': 'roof', 'icon': '💨', 't': 'Roof stays on in 130 mph wind', 'pass': 'The straps held the roof down.', 'fail': 'The wind lifted the roof off. It was only nailed down.'}],
        'runBtn': 'Run the storm', 'againBtn': 'Run the storm again', 'resultsLabel': 'Test results', 'overShort': 'over budget!',
        'startLine': 'Pick each part, then run the storm.',
        'overLine': 'Over budget! That breaks the constraint (the limit). Can a cheaper part still pass its test?', 'inLine': 'It fits the budget.',
        'reviseHead': 'Time to revise', 'reviseLine': 'Look at the red ❌ tests. Change one part at a time, then run the storm again.',
        'passHead': 'The house stood!', 'passLine': 'Every test passed, and it fits the budget. The town can sign the permit.',
        'deepLabel': 'pilings go deep into the ground',
        'q': 'Why didn’t impact glass make it into the final design?',
        'opts': [{'t': 'It costs too much for the budget, and shutters passed the same test.', 'ok': True},
                 {'t': 'Impact glass breaks easily.', 'miss': 'Look at its note: impact glass doesn’t shatter. What was the problem?'},
                 {'t': 'Windows don’t matter in a storm.', 'miss': 'What happened to the plain glass in the test?'}],
        'win': 'Raise it, strap it, cover it, and stay in budget. That’s a clue.',
        'clue': 'buildhouse'},
    'fixtown': {
        'afterText': 'Open each problem on the map', 'kicker': 'Part 4 game', 'title': 'Fix the whole town',
        'todo': ['Tap a problem on the list or a pin on the map.', 'Pick the fix that would help most. Then stamp it: built, natural or planning.'],
        'kinds': [{'k': 'built', 'icon': '🧱', 't': 'Built'}, {'k': 'natural', 'icon': '🌿', 't': 'Natural'}, {'k': 'plan', 'icon': '📋', 't': 'Planning'}],
        'fixQ': 'Which fix would help most?', 'kindQ': 'What kind of mitigation is it?',
        'spots': [
            {'id': 'pine', 'icon': '🌳', 'place': 'Pine Ave', 'x': 300, 'y': 118, 'problem': 'A big branch snapped and blocked the road.', 'kind': 'natural',
             'fixes': [{'t': 'Plant wind-resistant trees, like live oaks, away from the road', 'short': 'wind-resistant trees', 'ok': True},
                       {'t': 'Cut down every tree in town', 'miss': 'That would lose shade and homes for birds. Is there a smarter way?'},
                       {'t': 'Close the road forever', 'miss': 'People need the road. What could keep it clear?'}],
             'kindMiss': {'built': 'Trees aren’t built by people. They’re living things.', 'plan': 'Planting is an action, but the fix itself is a living thing. Which kind is that?'},
             'why': 'Some trees, like live oaks, hold up better in strong wind. Planting them away from roads keeps falling branches out of the way.'},
            {'id': 'oak', 'icon': '💡', 'place': 'Oak Street', 'x': 470, 'y': 140, 'problem': 'A power line came down, and the power went out.', 'kind': 'built',
             'fixes': [{'t': 'Bury the power lines underground', 'short': 'buried power lines', 'ok': True},
                       {'t': 'Turn off the power every summer', 'miss': 'Families need power all summer. What could protect the lines?'},
                       {'t': 'Paint the poles a brighter color', 'miss': 'Paint won’t stop wind. What would keep the lines away from the wind?'}],
             'kindMiss': {'natural': 'Power lines and pipes are made by people. Which kind is that?', 'plan': 'Workers dig and lay new lines. Is that a plan or something built?'},
             'why': 'Lines under the ground can’t be blown down by wind or hit by falling trees.'},
            {'id': 'elm', 'icon': '🌧️', 'place': 'Elm Street', 'x': 430, 'y': 80, 'problem': 'The street flooded when the storm drains overflowed.', 'kind': 'natural',
             'fixes': [{'t': 'Add rain gardens: low gardens with plants that soak up rainwater', 'short': 'rain gardens', 'ok': True},
                       {'t': 'Pave the yards so water runs off faster', 'miss': 'Pavement sends MORE water into the street. What would soak it up?'},
                       {'t': 'Ask people to stay inside when it rains', 'miss': 'The street would still flood. What could hold the water?'}],
             'kindMiss': {'built': 'A rain garden is made of soil and plants. Which kind is that?', 'plan': 'A rain garden is plants and soil, not a plan. Which kind is that?'},
             'why': 'Plants and loose soil soak up rain like a sponge, so less water rushes into the drains at once.'},
            {'id': 'bay', 'icon': '🏠', 'place': 'Bay Street', 'x': 380, 'y': 278, 'problem': 'Seawater filled the houses.', 'kind': 'built',
             'fixes': [{'t': 'Rebuild the houses on deep pilings, like the Riveras’', 'short': 'houses on pilings', 'ok': True},
                       {'t': 'Paint the houses with waterproof paint', 'miss': 'Paint won’t keep 8 feet of water out. What would lift the house above it?'},
                       {'t': 'Move the bay farther away', 'miss': 'The bay can’t move! What can change about the houses?'}],
             'kindMiss': {'natural': 'Pilings are made by people. Which kind is that?', 'plan': 'Pilings are part of the building. Which kind is that?'},
             'why': 'Raised floors let the surge flow under the house, like the Riveras’ design in Part 2.'},
            {'id': 'town', 'icon': '📣', 'place': 'The whole town', 'x': 252, 'y': 140, 'problem': 'Some families waited too long to leave.', 'kind': 'plan',
             'fixes': [{'t': 'Practice the evacuation plan every June and post route signs', 'short': 'evacuation practice', 'ok': True},
                       {'t': 'Wait until the water arrives, then decide', 'miss': 'By then the roads may be flooded. When should families decide?'},
                       {'t': 'Build a bigger town hall', 'miss': 'A building doesn’t tell people when and where to go. What would?'}],
             'kindMiss': {'built': 'Practice and signs tell people what to do. Is that built, or a plan?', 'natural': 'Practice isn’t a living thing. Which kind is it?'},
             'why': 'Families who practice know when to leave and which road to take, so they get out before the storm arrives.'}],
        'q': 'What makes the best plan for Palmetto Springs?',
        'opts': [{'t': 'A mix of built, natural and planning fixes, one for each problem.', 'ok': True},
                 {'t': 'One giant seawall around the whole town.', 'miss': 'Would a wall stop a falling branch or a flooded Elm Street?'},
                 {'t': 'Only planning, because buildings always fail.', 'miss': 'The Riveras’ house passed every test. Do buildings always fail?'}],
        'win': 'Each problem needed its own fix. Together they make a plan. That’s your last clue.',
        'clue': 'fixtown'},
    'exploreMod': 'fixtown',
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'You can’t stop a hurricane. What CAN engineers change?', 'B': 'Forecasters predict storms. What does mitigation do?'},
        'q2': {'A': 'Built means people make it out of concrete or wood. Are mangroves built?', 'C': 'A plan is something people agree to follow. Are mangroves a plan?'},
        'q3': {'B': 'A criterion is a goal. Is the berm a goal, or a change to the design?', 'C': 'A constraint is a limit, like a budget. Is the berm a limit?'}},
    'flags': {
        'ans-2': [
            {'label': 'a built solution', 're': 'seawall|wall|shutter|strap|piling|drain|built|concrete|road|power line|pipe|build'},
            {'label': 'a natural solution', 're': 'mangrove|dune|wetland|tree|natural|plant|sea oat|rain garden|nature'},
            {'label': 'why compare them', 're': 'because|so |each|different|better|cost|balance|weak|strong|together|compare|best'}],
        'ans-3': [
            {'label': 'what revising does', 're': 'revis|improv|change|fix|better|again|stronger'},
            {'label': 'two solutions combined', 're': 'combin|both|together|and also|plus|with|mix'},
            {'label': 'a Florida example', 're': 'hurricane|surge|flood|wildfire|fire|mangrove|dune|seawall|wall|piling|strap|shutter|rain garden|drain|house|town|beach'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|not the only|isn|is not'},
            {'label': 'two pieces of evidence', 'any': ['wall', 'piling', 'strap', 'shutter', 'mangrove', 'dune', 'plan', 'evacuat', 'branch', 'power', 'rain', 'drain', 'budget', 'natural', 'built', 'combin', 'rivera', 'garden', 'tree'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-2': 15, 'ans-3': 20, 'cer-4': 30},
    'hints': {
        'ans-2': ['Think about the three shelves. What does a built solution do well? A natural one?', 'What could a seawall do that mangroves can’t, and the other way around?', 'Try: It is useful to compare them because ___. For example, ___.'],
        'ans-3': ['What happened when one of your house tests failed?', 'Think of two fixes that cover each other’s weak spots, like shutters AND roof straps.', 'Try: Revision is important because ___. For example, a town could combine ___ and ___.'],
        'cer-4': ['First decide: is a tall wall the ONLY way to protect a town?', 'Think about the Riveras’ house and the problems on the town map.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'The Riveras’ house stood because of pilings, roof straps and shutters, not a wall.',
                'A wall can’t stop a falling branch, a downed power line or rain flooding Elm Street.',
                'Mangroves and dunes are natural mitigation that slow waves before they reach land.',
                'Evacuation plans keep people safe even when buildings get damaged.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · the house that stood', 'length': '30–40 s',
                    'script': 'Hi, it’s June. Storm Night is over, and the Rivera family needs to rebuild their house on Bay Street. Remember those Mexico Beach photos? A few houses were still standing. The Riveras asked me a big question: how do we build a house that stands up to the next storm? Let’s find out together, then design one.'},
        'warmup': {'label': 'Warm-Up · what helped, what failed? (Clue 1)', 'length': '20–30 s',
                   'script': 'This is a real street in Mexico Beach, four days after the storm. Tap each number on the photo and read what happened there. Then match the clues. Look closely: where did the storm do the most damage?'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Hold up a cardboard “budget” of 7 coins for “constraint”; act out “revise” by fixing a paper house and trying again.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · three kinds of mitigation (Clue 2)', 'length': '20–30 s',
                  'script': 'Engineers have three kinds of tools for a storm: things we build, natural helpers like dunes and mangroves, and plans people follow. Drag each photo onto the right shelf. Which kind do you think Florida towns use most?'},
        'part2': {'label': 'Part 2 · build it, then storm it (Clue 3)', 'length': '25–35 s',
                  'script': 'Time to design the Riveras’ house. Pick a foundation, windows and a roof, but watch the budget. Then run the storm. If a test fails, don’t worry. Change one part and try again. That’s what engineers do.'},
        'explore': {'label': 'Part 4 · fix the whole town (Clue 4)', 'length': '25–35 s',
                    'script': 'The Riveras have their plan. Now the town council wants one for the whole town. Tap each problem from Storm Night on the map. Pick the fix that would help most, then decide: is it built, natural or a plan?'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s',
                       'script': 'Do you have all four clues? Crack the case at the top of this tab: how should the Riveras rebuild? Then answer two questions, plan a fix for any Florida hazard in Part C, and write your CER. Your answers save as you type.'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · design a mitigation plan', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says the only way to protect a town is the tallest, strongest wall you can build. Hmm. Think about the Riveras’ house, and think about Elm Street. Pick your side, tap two pieces of evidence in the planner, then explain how they prove your claim.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease the review days (17.R1: a mystery on Main Street).',
                    'script': 'Case closed! You studied a real storm, built a house that passed every test, and made a plan for the whole town. That’s what engineers do: they can’t stop a hurricane, but they can lower the harm. Next time, it’s review time. Get ready for a mystery on Main Street.'},
    },
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'The photo with all four numbers opened (Warm-Up)',
        'Your three shelves (The Lesson)',
        'Your house passing the storm test (The Lesson)',
        'The town map with every problem fixed (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['My decision matrix', 'The Riveras’ new house', 'My fix for one Florida hazard'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 3,
                           'prompts': ['Draw a small table: solutions across the top, criteria down the side', 'Give each box ⭐ to ⭐⭐⭐', 'Circle the winner and write your revision']}]},
    'hlCoach': copy.deepcopy(Q['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🔩', 'name': 'Hurricane strap',
                 'line': 'You cracked Case 17, part 2, and a hurricane strap goes in your Field Notebook. (A specimen is something a scientist collects to study.) Next time: review day, and a mystery on Main Street.'},
    'notebookTitle': Q['notebookTitle'],
    'notebook': [dict(x) for x in Q['notebook']],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You’ll use every one of them to help the Riveras.',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '.act-warmup p', 'text': 'look at what a real storm did'},
         'label': 'Warm-Up: the town’s two ideas', 'q': 'Warm-Up: The idea that catches my attention first, one question I’d ask, and what could go wrong',
         'title': 'Your turn: the town’s two ideas (seawall or mangroves and dunes)',
         'fields': [{'t': 'The idea that catches my attention first', 'icon': '👀', 'ph': 'Idea ___ catches my attention because…'},
                    {'t': 'One question I’d ask before choosing', 'icon': '❓', 'ph': 'I’d want to know…', 'long': True},
                    {'t': 'One thing that could go wrong', 'icon': '⚠️', 'ph': 'Something that could go wrong is…', 'long': True}]},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'hide-nw', 'type': 'hide', 'find': {'sel': '.act-warmup .socratic-q', 'text': 'Notice'}},
        {'id': 'hide-tip', 'type': 'hide', 'find': {'sel': '.act-warmup .callout', 'text': 'Engineers protect'}},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Plan like an engineer'},
         'label': 'Part C: Design a mitigation plan', 'q': 'Part C: A mitigation plan for one Florida hazard: criteria, a constraint, a built and a natural solution, the winner and a revision',
         'title': 'My mitigation plan',
         'fields': [{'t': 'The hazard, two criteria (goals) and one constraint (limit)', 'icon': '🎯', 'ph': 'Hazard: … Goals: … and … Limit: …', 'long': True},
                    {'t': 'Solution 1 (BUILT) and Solution 2 (NATURAL)', 'icon': '🧱', 'ph': 'Built: … Natural: …', 'long': True},
                    {'t': 'The winner, with stars for each goal', 'icon': '⭐', 'ph': 'I choose ___ because it got ⭐⭐⭐ for…', 'long': True},
                    {'t': 'My revision: how I would make the winner better', 'icon': '🔁', 'ph': 'I would make it better by…', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Is the tallest, strongest wall the ONLY way to protect a town?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-2': 'Part B · Question 5', 'ans-3': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] == '17.02': n.update({'icon': '🔩', 'name': 'Hurricane strap'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'Deep pilings lift the floor above the storm surge.',
    'key': ['Deep', 'pilings', 'lift', 'floor', 'above', 'surge'],
    'small': ['the', 'storm'],
    'model': 'A scientist might highlight “pilings”, “floor above” and “surge”. Those words tell how the design beats the hazard. Small words like “the” don’t carry the idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me explain how people design ways to lower the harm of a natural hazard?']
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
