#!/usr/bin/env python3
"""Writes data.json and fixes.json for 29.02 (run from this folder). Case 29 part 2 "Kai's Treasure Pouch" (Dr. Priya Nair, Unit 7 in Canvas, Palmetto Springs):
the morning after Campfire Night, Kai pans the creek and tags 4 finds GOLD!, SILVER bolt, DIAMOND, old COIN. What is each one really made of?
New (Bethany's brainstorm, 27 Nov 2026): case.pouch, tower (Warm-Up: the claim tower, real gold vs pyrite photos), barcode (Part 1: fingerprint barcode),
knockout (Part 2: knock out the suspects), streak (Part 3: the fool's gold wow, real photos), claimtiles (Part 4 = the old Explore: tests fill a data table, then
claims from tiles), ringtwist + mlabel (after the solve), SIMS.hardness (Tool: scratch kit). SCRIPTS ONLY: nothing generated."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
O = json.load(open('../27-01/data.json', encoding='utf-8'))
Q = json.load(open('../29-01/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

# ---------------------------------------------------------------- labels (standing approval)
fx('fix', 'unit label: “Ecosystems & Energy” is a leftover; the plan puts Module 29 under “Matter, Magnets, and Changes”', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Matter, Magnets &amp; Changes</div>')
fx('fix', 'science label: identifying materials by their properties is physical science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standards label: the plan’s CPALMS codes, content benchmark first; TEKS is a Texas code that isn’t in the plan', '<div class="info-value">SC.4.N.1.1, SC.4.P.8.1 · TEKS 4.6(A)</div>', '<div class="info-value">SC.4.P.8.1, SC.4.N.1.1</div>')
fx('fix', 'footer standards in the same order as the header', 'CPALMS SC.4.N.1.1, SC.4.P.8.1', 'CPALMS SC.4.P.8.1, SC.4.N.1.1')
fx('fix', 'quarter label in the footer: week 29 is Q4 (the header already says Q4)', 'Science &middot; Quarter 3 &middot; Student Lesson Page', 'Science &middot; Quarter 4 &middot; Student Lesson Page')
fx('plain', 'shorter; no dashes', r"<p>Hold this question in your head as you work\. Near the end of the year.*?</p>",
   "<p>Keep this question in mind. Today you’ll work like a detective: test a mystery material, compare it to a property guide, and back up every answer with evidence.</p>", True)

# ---------------------------------------------------------------- ticked: energy-lesson leftovers (22.01)
fx('fix', '22.01 leftover (ticked): the Warm-Up title named the toaster lesson', '<div class="act-title">🌅 Warm-Up: What Goes In, What Comes Out?</div>\n        <div class="act-subtitle">A familiar device, a hidden change</div>',
   '<div class="act-title">🌅 Warm-Up: Gold or Not?</div>\n        <div class="act-subtitle">Two nuggets, one question</div>')
fx('fix', '22.01 leftover (ticked): the toaster warm-up → Kai’s nugget',
   '<p>Think about a toaster. You drop in cold bread. A minute later, you pull out hot toast.</p>',
   '<p>Kai found a shiny nugget in the creek and shouted, “GOLD! I’m rich!” Dr. Nair held up a photo of a real gold nugget from a museum.</p>')
fx('fix', '22.01 leftover (ticked): the toaster sketch → the claim tower (played and answered on the page)',
   "<p>In your notebook, draw a quick sketch of a toaster. On one side, label what goes IN. On the other, label what comes OUT. (Hint: bread on both sides — but something invisible is also going in. What is it?)</p>",
   '<p>Same color. Same shine. Is Kai’s nugget gold? Try to prove it.</p>')
fx('fix', '22.01 leftover (ticked): Notice & Wonder about the toaster',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Notice &amp; Wonder</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover (ticked): “energy can CONVERT … toasters” callout',
   r'<div class="callout callout-tip">\s*<span class="callout-icon">💡</span>\s*<p>Today you\'ll learn that energy can CONVERT.*?</p>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover (ticked): “Device” meant converting energy',
   'A tool or machine designed to do a job. Most devices convert energy from one form to another — a flashlight, a toaster, a fan are all devices.',
   'A tool or machine made to do a job, like a scale for measuring mass.')
fx('fix', '22.01 leftover (ticked): the Stop & Reason asked about “the three devices above … INPUT and OUTPUT”',
   r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)

# ---------------------------------------------------------------- ticked: food-chain leftovers (9.01) → the checklist's own task
fx('fix', '9.01 leftover (ticked): Part C was a food chain; the checklist already describes a 3-sample mystery investigation', '🎨 Part C &mdash; Build Your Own Food Chain', '🎨 Part C &mdash; Your Own Mystery')
fx('fix', '9.01 leftover (ticked): Part C task → the checklist’s home investigation (typed on the page, sketched in a required drawing)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Ask a family member to secretly pick 3 small, safe things from home and call them A, B and C. Test each one: color, a magnet, does it float, how hard it is. Then identify each one with evidence.</p>', True)
fx('fix', '9.01 leftover (ticked): Reflect asked about a hawk; the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list (ticked): “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list (ticked): no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'supply list (ticked): Part C needs 3 things from home, not colored pencils', r'<span class="need-chip"><span>✏️</span>Colored pencils</span>', '<span class="need-chip"><span>🏠</span>3 small things from home and a magnet</span>', True)

# ---------------------------------------------------------------- Part 1, Part 2
fx('plain', 'Part 1: no dash', 'properties — like a fingerprint.', 'properties, like a fingerprint.')
fx('plain', 'Part 1: no dash', ' — lists of common materials and their properties.', ': lists of common materials and their properties.')
fx('plain', 'Part 1: a lead-in for the barcode game', 'they collect property data and match it to the guide.</p>',
   'they collect property data and match it to the guide.</p>\n      <p>Try it: print the fingerprint of Kai’s “SILVER” bolt.</p>')
fx('cut', 'lean: the Stop & Think (could a gray, hard, magnetic material be aluminum?) is played by the barcode and the knock-out board',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('plain', 'Part 2: plain words, no semicolon; anchor for the knock-out board',
   'The best matches usually rely on 3+ properties agreeing. One property can be misleading (lots of things are gray); three or four properties together build a strong case.',
   'The best matches use 3 or more properties that agree. One property can fool you, because lots of things are gray. Three or four properties together build a strong case.')
fx('cut', 'lean: the misconception (one property is enough) is played by the knock-out board (gray alone leaves 5 suspects)',
   r'\s*<p><strong>Common misconception:</strong> Some people think one property is enough to identify a material\..*?</p>', '', True)
fx('fix', 'figure (ticked): the picture lists glass hardness as “smooth” (a texture). Same 4 mysteries as an on-page table; glass is hard',
   r'<img src="images/29-02-mystery-table\.png".*?<div class="lesson-figure-caption">',
   '<table style="width:100%;border-collapse:collapse;font-size:15px;background:#fff;border-radius:10px;overflow:hidden;">'
   '<tr style="background:#F0806B;color:#fff;"><th style="padding:7px;text-align:left;">Mystery</th><th style="padding:7px;">Color</th><th style="padding:7px;">Hardness</th><th style="padding:7px;">Magnetic?</th><th style="padding:7px;">Floats?</th><th style="padding:7px;">Identified</th></tr>'
   + ''.join('<tr style="background:%s;"><td style="padding:7px;font-weight:800;">%s</td><td style="padding:7px;text-align:center;">%s</td><td style="padding:7px;text-align:center;">%s</td><td style="padding:7px;text-align:center;">%s</td><td style="padding:7px;text-align:center;">%s</td><td style="padding:7px;text-align:center;font-weight:900;color:#0E1C42;">%s</td></tr>' % r for r in [
       ('#EAF2FB', '🔍 A', 'silver-gray', 'hard', 'YES', 'no', 'IRON'), ('#EEF8F0', '🔍 B', 'clear', 'hard', 'no', 'no', 'GLASS'),
       ('#FFF6E0', '🔍 C', 'brown', 'soft', 'no', 'yes', 'WOOD'), ('#F3EEFA', '🔍 D', 'silver-gray', 'softer than iron', 'no', 'no', 'ALUMINUM')])
   + '</table>\n        <div class="lesson-figure-caption">', True)
fx('cut', 'lean: Key Concept (the games teach it)',
   r'<div style="background:#FFF6E5;border:2\.5px solid #F0C97A;[^>]*>\s*<div[^>]*>⭐ Key Concept</div>.*?</p>\s*</div>\s*', '', True)
fx('cut', 'lean: the Four Mystery Samples tap diagram repeats the table (and the claim tiles play it); with it go Observe & Reason, the police-lab Amazing Fact, the marine-biologist Florida connection and the Titanic Go Deeper. A new Part 3 holds the fool’s gold wow',
   H3 + 'Four Mystery Samples</h3>.*?(?=<div class="tab-next-wrap">)',
   H3 + 'Part 3 · Fool’s Gold!</h3>\n      <p>Kai’s nugget looked like gold. So did the museum nugget. Time to run the tests that looking can’t do.</p>\n\n      ', True)

# ---------------------------------------------------------------- Word Wall: no dashes
fx('plain', 'Word Wall: no dash', 'A property you notice with your senses — color, shape, texture, smell (if safe), how it sounds when tapped.', 'A property you notice with your senses: color, shape, texture, smell (if safe), or how it sounds when tapped.')
fx('plain', 'Word Wall: no dash', 'A property you can put a number on — mass, length, volume, temperature.', 'A property you can put a number on: mass, length, volume or temperature.')
fx('plain', 'Word Wall: no dash', 'A specific kind of matter — iron, water, glass, plastic, wood. Each has a unique property "fingerprint."', 'A specific kind of matter, like iron, water, glass, plastic or wood. Each has its own property “fingerprint.”')
fx('plain', 'cut filler; no dash', r"<p>These six words show up all through the lesson\. <strong>Tap a card to flip it</strong>.*?</p>",
   "<p><strong>Tap a card to flip it</strong> and read what the word means.</p>", True)

# ---------------------------------------------------------------- Part 4 = the old Explore
fx('cut', 'Part 4 = the old Explore (Identify the Mystery → the claim tiles: test 3 unknowns, fill a data table, identify and justify); the next button goes to Self-Check',
   '''<div class="tab-next-wrap">
        <button class="tab-next-btn" onclick="switchTab('explore')">Continue to 🔬 Explore →</button>''',
   H3 + 'Part 4 · Build Your Claim</h3>\n      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">Time to prove it. Test Kai’s “GOLD!” nugget, his “DIAMOND” and a black lump from the fire pit. Then build a claim for each one.</p>\n  <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>')
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (the home investigation lives on as Part C; the ancient-pottery Amazing Fact, the gray-sample Think like a scientist and the density Go Deeper go with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)

# ---------------------------------------------------------------- Assignment
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('plain', 'Part B question 5 no longer points at the cut diagram (same task, Kai’s finds)',
   'Pick ONE mystery sample from the diagram. Name the 2 most useful pieces of evidence and the material identification.',
   'Pick ONE of Kai’s finds: the “GOLD!” nugget, the “SILVER” bolt, the “DIAMOND” or the old “COIN”. Name the 2 most useful pieces of evidence and what it really is.')
fx('plain', 'Part B question 5 label (Gathered Answers)', 'data-label="Pick ONE mystery sample from the diagram. Name the..."', 'data-label="One of Kai’s finds: the 2 best pieces of evidence"')
fx('plain', 'Part B question 7 label (Gathered Answers)', 'data-label="An unknown sample is gray and hard. Name THREE mor..."', 'data-label="Gray and hard: three more tests and why"')
fx('cut', 'lean: Part B question 6 removed (Bethany kept 5 and 7; the CER argues why one property isn’t enough)', r'<div class="pq">\s*<span class="pq-num"[^>]*>6</span>.*?</textarea>\s*', '', True)
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 7 answered')
fx('cut', 'lean: Part C checklist ends with the required sketch', 'A real 3-sample mystery investigation with data table, identifications, and answer key from a family member.',
   'My 3 mystery things, each tested and identified with evidence. Plus your labeled sketch.')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether one property is enough to identify a material, supported with two pieces of evidence.',
   '<strong>Use Your Evidence:</strong> My claim about whether gray and hard means iron, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a 9.01 leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Download your field journal (it has your answers and your sketch) and upload it to the Canvas assignment. Or copy your Gathered Answers (above) into Canvas.', True)
fx('plain', 'closing: no dash; shorter', "Next lesson is our second-to-last — exploring how matter can CHANGE without becoming something new.",
   "Next lesson: how matter can CHANGE without becoming something new.")
fx('plain', 'closing: no dash', "You've just done what real scientists, archaeologists, and detectives do — collected", "You did what real scientists and detectives do. You collected")

# ---------------------------------------------------------------- the story
PRIYA = O['crew']['priya']
IMG = {'gold': 'images/29-02-gold-nugget.jpg', 'pyrite': 'images/29-02-pyrite.jpg', 'pstreak': 'images/29-02-pyrite-streak.jpg', 'gstreak': 'images/29-02-gold-streak.jpg'}
CR_NUG = 'Kai’s nugget (pyrite from Peru): James St. John, CC BY 2.0 · Museum gold nugget from Australia: James St. John, CC BY 2.0 · both via Wikimedia Commons'
CR_ALL = CR_NUG + ' · Pyrite streak plate: Ra’ike, CC BY-SA 3.0 · Gold streak: Ra’ike, CC BY-SA 3.0 DE · via Wikimedia Commons'
GRAY, GOLD, BROWN, ORANGE, CLEAR = '#A9B1B8', '#E2B640', '#8A5A2B', '#C46A3A', '#DDEFF5'
D = {
    'lesson': '29.02', 'week': 29, 'day': 2, 'guide': 'priya', 'prefix': 'g4sci-29-2', 'manifestKey': '29-02',
    'paths': P['paths'], 'crew': {'priya': PRIYA},
    'expedition': {'num': 29, 'title': 'Campfire Night, part 2'},
    'ambient': {'icon': '🏞️', 'label': 'The creek at sunrise'},
    'case': {
        'num': 29, 'title': 'Kai’s Treasure Pouch', 'style': 'order',
        'hook': 'Dr. Priya Nair here. It’s the morning after Campfire Night. Kai panned the creek at sunrise (he swirled creek sand in a pan, hunting for gold) and came back with a pouch of treasure! He tied a tag on every find. But Kai only LOOKED at them. What is each one really made of?',
        'pouch': {'head': 'PALMETTO SPRINGS CREEK', 'title': 'Kai’s Treasure Pouch',
                  'tags': [{'icon': '🟡', 't': 'GOLD!', 'sub': 'a shiny yellow nugget'}, {'icon': '🔩', 't': 'SILVER bolt', 'sub': 'silver-gray and hard'},
                           {'icon': '💎', 't': 'DIAMOND', 'sub': 'a clear, sparkly pebble'}, {'icon': '🪙', 't': 'old COIN', 'sub': 'a gray metal disc'}],
                  'note': '“I’m going to be RICH!”', 'sign': 'Kai'},
        'stills': [],
        'question': 'What is each of Kai’s finds really made of?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'tower', 'icon': '🏗️', 'where': 'Warm-Up: the claim tower', 't': 'Looks can’t prove what a material is. Gold and fool’s gold look almost the same. Kai’s tags need TESTS.'},
            {'id': 'barcode', 'icon': '🧬', 'where': 'The Lesson, Part 1: fingerprint barcode', 't': 'The “SILVER” bolt is silver-gray, hard, magnetic and sinks. That fingerprint matches steel. Silver is NOT magnetic.'},
            {'id': 'knockout', 'icon': '🕵️', 'where': 'The Lesson, Part 2: knock out the suspects', 't': 'The “old COIN” is gray, NOT magnetic and light for its size: aluminum. Gray alone left 5 suspects!'},
            {'id': 'claimtiles', 'icon': '🧾', 'where': 'The Lesson, Part 4: build your claim', 't': 'The “GOLD!” nugget has a greenish-black streak and weighs only 5 g: pyrite, fool’s gold. The “DIAMOND” weighs 2.5 g and leaves a white streak: glass.'},
        ],
        'solve': {
            'title': 'What did Kai really find?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Gold, silver, a diamond and an old coin, just like his tags say.', 'why': 'Check Clue 1. Kai only looked. The tests tell a different story.'},
                {'t': 'Fool’s gold (pyrite), a steel bolt, a piece of glass and an aluminum disc.', 'right': True,
                 'why': 'Case cracked! Every tag was wrong, and every answer has two or more tests behind it.'},
                {'t': 'Fool’s gold, steel, glass and silver, because the coin is gray and shiny.', 'why': 'Check Clue 3. Silver is heavy for its size. The coin was light, so it’s aluminum.'},
                {'t': 'Fool’s gold, silver, glass and iron, because every metal sticks to a magnet.', 'why': 'Check Clues 2 and 3. The bolt stuck, so it isn’t silver. The coin didn’t stick, and it’s still a metal.'},
            ]},
    },
    'tower': {
        'afterText': 'Is Kai’s nugget gold? Try to prove it.', 'kicker': 'Warm-Up game', 'title': 'The claim tower',
        'why': {'icon': '🏗️', 'q': 'What is a claim?', 't': 'Something you say is true. A strong claim stands on evidence, like a tower on strong blocks.'},
        'todo': ['Look at the two nuggets.', 'Drag a block under Kai’s sign (or tap a block, then the tower).', 'Watch what happens. The 🔒 blocks are tests: you’ll run them in Part 3.'],
        'photos': [{'img': IMG['pyrite'], 'alt': 'Kai’s nugget: a shiny, brassy yellow cluster.', 'cap': 'Kai’s nugget, from the creek'},
                   {'img': IMG['gold'], 'alt': 'A large, shiny gold nugget in a museum.', 'cap': 'A real gold nugget in a museum'}],
        'credit': CR_NUG, 'sign': 'IT’S GOLD!', 'dropLine': 'Drop evidence here',
        'blocks': [{'id': 'color', 'icon': '🟡', 't': 'It’s gold-colored', 'kind': 'look'}, {'id': 'shine', 'icon': '✨', 't': 'It’s shiny', 'kind': 'look'},
                   {'id': 'creek', 'icon': '🏞️', 't': 'It was in a creek', 'kind': 'look'}, {'id': 'sure', 'icon': '😤', 't': 'Kai is SURE', 'kind': 'look'},
                   {'id': 'streak', 'icon': '✏️', 't': 'A streak test', 'kind': 'test', 'lock': 'Locked! You’ll run the streak test in Part 3.'},
                   {'id': 'scratch', 'icon': '🔩', 't': 'A scratch test', 'kind': 'test', 'lock': 'Locked! You’ll run the scratch test in Part 3.'},
                   {'id': 'weigh', 'icon': '⚖️', 't': 'A weigh test', 'kind': 'test', 'lock': 'Locked! You’ll run the weigh test in Part 3.'}],
        'need': 3, 'startLine': 'Pick a block to hold up Kai’s sign.', 'wobbleLine': 'Wobble! Blocks so far: {n}. Is it strong enough?',
        'fallLine': 'CRASH! Color, shine and Kai’s word can’t hold up the claim. Fool’s gold has all of those too. You need TESTS.',
        'q': 'Why did the tower fall?',
        'opts': [{'t': 'Looks alone can’t prove what a material is.', 'ok': True},
                 {'t': 'The blocks were too small.', 'miss': 'It’s not the size of the blocks. Fool’s gold is gold-colored and shiny too!'},
                 {'t': 'Kai’s nugget isn’t shiny.', 'miss': 'It IS shiny. But so is fool’s gold. Shine can’t tell them apart.'}],
        'win': 'Looks can’t prove it. Tests can. Clue 1!', 'clue': 'tower'},
    'barcode': {
        'afterText': 'print the fingerprint of Kai’s “SILVER” bolt.', 'kicker': 'Part 1 game', 'title': 'Fingerprint barcode',
        'why': {'icon': '🧬', 'q': 'What is a material’s fingerprint?', 't': 'Its own set of properties. Two materials can share one or two, but the whole set is different, like your fingerprint.'},
        'todo': ['Run each test on the bolt. Then flip the switch to match.', 'Each switch prints a stripe.', 'Drag the strip over the shelf (or tap a card) until every stripe lines up.'],
        'thing': {'icon': '🔩', 't': 'Kai’s “SILVER” bolt'}, 'printLabel': 'The bolt’s fingerprint', 'printLine': 'Each switch you set prints a stripe.',
        'slideLine': 'Drag the strip over a card on the shelf, or tap a card.',
        'props': [
            {'k': 'color', 'icon': '🎨', 't': 'Color', 'test': '👀 Look', 'result': 'Silver-gray', 'val': GRAY,
             'opts': [{'v': GRAY, 't': 'Silver-gray'}, {'v': GOLD, 't': 'Gold-yellow'}, {'v': BROWN, 't': 'Brown'}], 'miss': 'Look again: what color did the test show?'},
            {'k': 'hard', 'icon': '💪', 't': 'Hard?', 'test': '✋ Press a fingernail in', 'result': 'No dent at all. It’s hard.', 'val': True,
             'opts': [{'v': True, 't': 'Yes'}, {'v': False, 't': 'No'}], 'miss': 'Your fingernail couldn’t dent it. Is it hard?'},
            {'k': 'mag', 'icon': '🧲', 't': 'Magnetic?', 'test': '🧲 Bring a magnet close', 'result': 'CLICK! The magnet grabs it.', 'val': True,
             'opts': [{'v': True, 't': 'Yes'}, {'v': False, 't': 'No'}], 'miss': 'The magnet grabbed it. Is it magnetic?'},
            {'k': 'float', 'icon': '💧', 't': 'Floats?', 'test': '💧 Drop it in water', 'result': 'Plop. It sinks to the bottom.', 'val': False,
             'opts': [{'v': True, 't': 'Yes'}, {'v': False, 't': 'No'}], 'miss': 'It sank. Does it float?'}],
        'shelf': [
            {'id': 'silver', 'icon': '🥄', 't': 'Silver', 'fp': {'color': GRAY, 'hard': True, 'mag': False, 'float': False}, 'why': 'So close! But the magnet stripe doesn’t match. Silver is NOT magnetic, and the bolt is.'},
            {'id': 'wood', 'icon': '🪵', 't': 'Wood', 'fp': {'color': BROWN, 'hard': False, 'mag': False, 'float': True}, 'why': 'Wood is brown, a fingernail can dent it, and it floats. Most stripes don’t match!'},
            {'id': 'steel', 'icon': '🔧', 't': 'Steel (iron)', 'fp': {'color': GRAY, 'hard': True, 'mag': True, 'float': False}, 'why': 'Every stripe lines up! The bolt is steel. Steel is mostly iron, so the magnet grabbed it.'},
            {'id': 'copper', 'icon': '🟠', 't': 'Copper', 'fp': {'color': ORANGE, 'hard': True, 'mag': False, 'float': False}, 'why': 'The color stripe doesn’t match. Copper is orange-brown, and it isn’t magnetic.'},
            {'id': 'glass', 'icon': '🫙', 't': 'Glass', 'fp': {'color': CLEAR, 'hard': True, 'mag': False, 'float': False}, 'why': 'Glass is clear, and a magnet doesn’t pull it.'}],
        'q': 'Kai’s tag says SILVER. Which stripe proves it isn’t silver?',
        'opts': [{'t': 'The magnet stripe: silver isn’t magnetic, but the bolt is.', 'ok': True},
                 {'t': 'The color stripe', 'miss': 'Both are silver-gray. Color can’t tell them apart!'},
                 {'t': 'The float stripe', 'miss': 'Steel and silver both sink.'}],
        'win': 'The “SILVER” bolt is steel. Clue 2!', 'clue': 'barcode'},
    'knockout': {
        'afterText': 'Three or four properties together build a strong case.', 'kicker': 'Part 2 game', 'title': 'Knock out the suspects',
        'why': {'icon': '🕵️', 'q': 'Why knock out suspects?', 't': 'Each test rules some materials out. Keep testing until only one material fits ALL the evidence.'},
        'todo': ['Drag a test onto the board (or tap a test, then the board).', 'Every suspect that doesn’t match flips down.', 'Keep testing until ONE suspect is left.'],
        'mystery': {'icon': '🪙', 't': 'Mystery: Kai’s “old COIN”'},
        'suspects': [
            {'id': 'iron', 'icon': '🔩', 't': 'Iron', 'p': {'color': 'gray', 'mag': True, 'heft': 'heavy', 'sink': True}},
            {'id': 'nickel', 'icon': '⚪', 't': 'Nickel', 'p': {'color': 'gray', 'mag': True, 'heft': 'heavy', 'sink': True}},
            {'id': 'alum', 'icon': '🥫', 't': 'Aluminum', 'p': {'color': 'gray', 'mag': False, 'heft': 'light', 'sink': True}},
            {'id': 'silver', 'icon': '🥄', 't': 'Silver', 'p': {'color': 'gray', 'mag': False, 'heft': 'heavy', 'sink': True}},
            {'id': 'lead', 'icon': '🎣', 't': 'Lead', 'p': {'color': 'gray', 'mag': False, 'heft': 'heavy', 'sink': True}},
            {'id': 'copper', 'icon': '🟠', 't': 'Copper', 'p': {'color': 'orange', 'mag': False, 'heft': 'heavy', 'sink': True}},
            {'id': 'gold', 'icon': '🟡', 't': 'Gold', 'p': {'color': 'yellow', 'mag': False, 'heft': 'heavy', 'sink': True}},
            {'id': 'wood', 'icon': '🪵', 't': 'Wood', 'p': {'color': 'brown', 'mag': False, 'heft': 'light', 'sink': False}}],
        'tests': [
            {'k': 'color', 'icon': '🎨', 't': 'Color', 'v': 'gray', 'res': 'Gray and shiny.', 'line': 'Every suspect that isn’t gray flips down. Look how many gray ones are left!'},
            {'k': 'mag', 'icon': '🧲', 't': 'Magnet', 'v': False, 'res': 'No pull at all.', 'line': 'The magnetic ones flip down. Surprise: aluminum, silver, lead, copper and gold are metals too, and a magnet doesn’t pull any of them. Only iron, nickel and steel stick.'},
            {'k': 'heft', 'icon': '⚖️', 't': 'Weigh it (same size)', 'v': 'light', 'res': 'Light for its size.', 'line': 'It weighs about one third as much as the same size of steel. The heavy suspects flip down.'},
            {'k': 'sink', 'icon': '💧', 't': 'Water', 'v': True, 'res': 'It sinks.', 'line': 'Anything that floats flips down.'}],
        'answer': 'alum', 'leftWord': 'suspects left', 'noneLine': 'Nobody flipped down. That test can’t split the suspects that are left. Try another one.',
        'q': 'Why did the color test leave so many suspects?',
        'opts': [{'t': 'Lots of different materials are gray.', 'ok': True},
                 {'t': 'Color is a measurable property.', 'miss': 'Color is observable: you see it. And lots of materials share the same color.'},
                 {'t': 'The coin is too old.', 'miss': 'Age doesn’t matter. Iron, nickel, aluminum, silver and lead are all gray.'}],
        'win': 'The coin is aluminum: gray, not magnetic and light for its size. Clue 3!', 'clue': 'knockout'},
    'streak': {
        'afterText': 'Time to run the tests that looking can’t do.', 'kicker': 'Part 3 · the wow', 'title': 'The streak plate',
        'why': {'icon': '✏️', 'q': 'What is a streak?', 't': 'The color of a mineral’s powder. Rub it on a rough white tile and look. The streak can be a different color than the mineral itself!'},
        'todo': ['Drag each nugget across the white tile (or tap a nugget, then the tile).', 'Then drag the steel nail onto each nugget.', 'Then weigh each one. Both pieces are the same size.'],
        'steps': {'streak': 'Streak test', 'scratch': 'Scratch test', 'heft': 'Weigh test'},
        'nuggets': [
            {'id': 'kai', 't': 'Kai’s nugget', 'img': IMG['pyrite'], 'alt': 'Kai’s brassy yellow nugget.', 'col': '#2F3A2E', 'colName': 'greenish black', 'scratch': False, 'grams': 5,
             'streakLine': 'A greenish-black streak! Hmm. Is that what gold does?', 'scratchLine': 'Screech… the nail slid right off. Not a scratch!', 'heftLine': '5 grams.'},
            {'id': 'gold', 't': 'Museum gold', 'img': IMG['gold'], 'alt': 'The museum’s gold nugget.', 'col': '#D9A92A', 'colName': 'gold-yellow', 'scratch': True, 'grams': 19,
             'streakLine': 'A gold-yellow streak.', 'scratchLine': 'The nail left a scratch. Gold is soft!', 'heftLine': '19 grams. Heavy for its size!'}],
        'plateAlt': 'A white streak plate', 'plateLine': 'Drag a nugget onto the white tile, or tap a nugget and then the tile.',
        'nail': 'Steel nail', 'nailLine': 'Drag the nail onto a nugget, or tap the nail and then a nugget.',
        'scaleLine': 'Both pieces are the same size (a 1-centimeter cube). Drag one onto the scale, or tap it and then the scale.',
        'yesScratch': 'scratched', 'noScratch': 'no scratch',
        'reveal': [{'img': IMG['pyrite'], 'alt': 'Kai’s nugget', 'cap': 'Kai’s nugget'}, {'img': IMG['pstreak'], 'alt': 'A real streak test on a white tile: a dark streak next to a small brassy cube.', 'cap': 'Its real streak: dark'},
                   {'img': IMG['gold'], 'alt': 'A real gold nugget', 'cap': 'Museum gold'}, {'img': IMG['gstreak'], 'alt': 'Real gold flakes beside a gold-yellow streak on a dark tile.', 'cap': 'Its real streak: gold-yellow'}],
        'credit': CR_ALL,
        'q': 'Is Kai’s nugget gold?',
        'opts': [{'t': 'No. Its streak is dark, a nail can’t scratch it, and it’s too light. It’s pyrite: fool’s gold!', 'ok': True},
                 {'t': 'Yes, it’s gold-colored and shiny.', 'miss': 'Remember the tower? Looks can’t prove it. Check the streak.'},
                 {'t': 'Yes, because it’s hard.', 'miss': 'Real gold is soft. The nail scratched the museum gold, but not Kai’s nugget.'}],
        'fact': {'q': 'Why is it called fool’s gold?', 't': 'During gold rushes, some miners found shiny pyrite and thought they were rich. A streak test would have told them the truth: gold leaves a gold-yellow streak, and pyrite leaves a dark one.'},
        'win': 'Kai’s nugget is pyrite: fool’s gold!'},
    'claimtiles': {
        'afterText': 'Then build a claim for each one.', 'kicker': 'Part 4 game', 'title': 'Build your claim',
        'why': {'icon': '🧾', 'q': 'What makes a strong claim?', 't': 'It names the material AND gives two pieces of evidence from tests. One clue alone could fit a lookalike.'},
        'todo': ['Drag a test onto a sample’s row (or tap a test, then the row). Run at least 3 tests on each sample.', 'Compare the results with the property guide.', 'Build a claim for each sample: drag tiles into the blanks.'],
        'tests': [{'k': 'color', 'icon': '🎨', 't': 'Look'}, {'k': 'streak', 'icon': '✏️', 't': 'Streak'}, {'k': 'nail', 'icon': '🔩', 't': 'Steel nail'},
                  {'k': 'mag', 'icon': '🧲', 't': 'Magnet'}, {'k': 'water', 'icon': '💧', 't': 'Water'}, {'k': 'weigh', 'icon': '⚖️', 't': 'Weigh (same size)'}],
        'samples': [
            {'id': 'nug', 'icon': '🟡', 't': 'The “GOLD!” nugget', 'answer': 'pyrite', 'key': ['streak', 'nail', 'weigh'],
             'res': {'color': 'brassy yellow', 'streak': 'greenish-black streak', 'nail': 'no scratch', 'mag': 'no pull', 'water': 'sinks', 'weigh': '5 g'},
             'wrongWhy': 'Check the guide. Gold leaves a gold-yellow streak and weighs 19 g.', 'keyLine': 'True, but gold could match that too. Add the streak, the nail or the weigh test.', 'doneLine': 'Identified: {m}!'},
            {'id': 'dia', 'icon': '💎', 't': 'The “DIAMOND”', 'answer': 'glass', 'key': ['weigh', 'streak'],
             'res': {'color': 'clear', 'streak': 'white streak', 'nail': 'no scratch', 'mag': 'no pull', 'water': 'sinks', 'weigh': '2.5 g'},
             'wrongWhy': 'Check the guide. A diamond weighs 3.5 g and leaves no streak.', 'keyLine': 'True, but a diamond could match that too. The weigh test or the streak tells them apart.', 'doneLine': 'Identified: {m}!'},
            {'id': 'lump', 'icon': '⚫', 't': 'The black lump', 'answer': 'charcoal', 'key': ['color', 'streak', 'nail'],
             'res': {'color': 'black', 'streak': 'black streak', 'nail': 'it crumbles', 'mag': 'no pull', 'water': 'floats', 'weigh': 'less than 1 g'},
             'wrongWhy': 'Check the guide. Wood is brown and leaves no streak.', 'keyLine': 'True, but wood matches that too. Add the color, the streak or the nail test.', 'doneLine': 'Identified: {m}! Wood that burned in the fire.'}],
        'guide': [{'id': 'gold', 'icon': '🟡', 't': 'Gold', 'fp': 'gold-yellow · gold-yellow streak · a nail scratches it · 19 g'},
                  {'id': 'pyrite', 'icon': '✨', 't': 'Pyrite', 'fp': 'brassy yellow · greenish-black streak · a nail can’t scratch it · 5 g'},
                  {'id': 'glass', 'icon': '🫙', 't': 'Glass', 'fp': 'clear · white streak · a nail can’t scratch it · 2.5 g'},
                  {'id': 'diamond', 'icon': '💎', 't': 'Diamond', 'fp': 'clear · no streak (it scratches the tile!) · 3.5 g'},
                  {'id': 'charcoal', 'icon': '⚫', 't': 'Charcoal', 'fp': 'black · black streak · crumbles · floats · less than 1 g'},
                  {'id': 'wood', 'icon': '🪵', 't': 'Wood', 'fp': 'brown · no streak · floats · less than 1 g'}],
        'guideTitle': 'The property guide (same-size pieces)',
        'decoys': [{'t': 'it is shiny', 'miss': 'Lots of materials are shiny. Use a test result from the table.'}, {'t': 'Kai said so', 'miss': 'Kai only looked! Use a test result from the table.'}],
        'tpl': ['I identify', 'as', 'because of this evidence:', 'and'], 'need': 3, 'countWord': 'claims built',
        'waitLine': 'Run at least {n} tests on a sample. Then you can build its claim.', 'oneLine': 'That’s the same test twice. Use two different tests.',
        'win': 'Three claims, each with two pieces of evidence. Clue 4!', 'clue': 'claimtiles'},
    'exploreMod': 'claimtiles',
    'ringtwist': {
        'after': '.fs-solve', 'kicker': 'Case closed · a twist', 'title': 'The “silver” ring', 'lockLine': 'Crack the case first.',
        'why': {'icon': '💍', 'q': 'One more find!', 't': 'Kai found a ring on the dock. “This one’s SILVER for sure!” Ranger Bell hands you a magnet.'},
        'todo': ['Bring the magnet to the ring.', 'Then decide: is it silver?'],
        'magnet': 'Magnet', 'ringT': 'Kai’s “silver” ring', 'clingLine': 'CLICK! The magnet grabbed the ring.',
        'q': 'Real silver is never pulled by a magnet. So what is the ring?',
        'opts': [{'t': 'Not silver. Probably steel with a silver-colored coating.', 'ok': True},
                 {'t': 'Silver, because it’s shiny.', 'miss': 'Shine can’t prove it. Silver doesn’t stick to magnets, and this ring did.'},
                 {'t': 'Gold', 'miss': 'Gold isn’t magnetic either, and the ring isn’t gold-colored.'}],
        'fact': {'q': 'A jeweler’s trick', 't': 'Jewelers often start with a magnet. Real silver and real gold don’t stick. If a “silver” ring sticks, there’s iron or steel in it.'},
        'win': 'One magnet test, and the tag was wrong again!'},
    'mlabel': {
        'after': '.fs-solve', 'kicker': 'Case closed · one more job', 'title': 'The museum label', 'lockLine': 'Crack the case first.',
        'why': {'icon': '🏛️', 'q': 'A museum label?', 't': 'Ranger Bell wants Kai’s fool’s gold in the nature center. A good museum label names the find and gives the evidence.'},
        'todo': ['Pick the name.', 'Pick two pieces of evidence.', 'Print the label.'],
        'img': IMG['pyrite'], 'alt': 'Kai’s pyrite nugget.',
        'rows': [{'k': 'name', 'label': 'Name', 'opts': [{'t': 'Pyrite (fool’s gold)', 'ok': True}, {'t': 'Gold', 'miss': 'The tests said no!'}, {'t': 'Brass', 'miss': 'Brass is made by people. Kai’s nugget came out of the ground.'}]},
                 {'k': 'e1', 'label': 'Evidence 1', 'opts': [{'t': 'Greenish-black streak', 'ok': True}, {'t': 'Gold-colored', 'miss': 'Real gold is gold-colored too, so that can’t prove it.'}, {'t': 'A steel nail can’t scratch it', 'ok': True}]},
                 {'k': 'e2', 'label': 'Evidence 2', 'opts': [{'t': 'Only 5 g, not 19 g like gold', 'ok': True}, {'t': 'Very shiny', 'miss': 'Gold is shiny too.'}, {'t': 'A steel nail can’t scratch it', 'ok': True}]}],
        'head': 'Palmetto Springs Nature Center', 'foundBy': 'Found by Kai in the Palmetto Springs creek. Identified by the Field Station crew.',
        'printBtn': '🖨️ Print the label', 'win': 'Printed! Kai’s fool’s gold has a home.'},
    'tool': {
        'name': 'Scratch kit', 'icon': '🪛', 'tab': 'assignment', 'after': '#tab-assignment .activity-card', 'key': '29-02-tool', 'sim': 'hardness',
        'kicker': 'Bonus · Tool of the Week', 'teaser': 'A real geologist’s kit: find out how hard a mystery sample is.',
        'done': 'Tool of the Week: you used a real scratch kit.',
        'why': {'icon': '🪛', 'q': 'What is a scratch kit?', 't': 'Tools of known hardness. If a tool scratches a sample, the sample is softer than the tool. Geologists carry one into the field.'},
        'hardness': {
            'title': 'Scratch and see', 'todo': ['Drag a tool onto a sample (or tap the tool, then the sample).', 'Try every tool on every sample.', 'Then answer the question.'],
            'model': 'A model. Try a fingernail and a penny on a piece of chalk at home.',
            'tools': [{'k': 'nail', 'icon': '✋', 't': 'Fingernail'}, {'k': 'penny', 'icon': '🪙', 't': 'Copper penny'}, {'k': 'steel', 'icon': '🔩', 't': 'Steel nail'}],
            'samples': [{'k': 'chalk', 'icon': '🖍️', 't': 'Chalk', 'res': {'nail': True, 'penny': True, 'steel': True}, 'band': 'Very soft: even a fingernail scratches it.'},
                        {'k': 'shell', 'icon': '🐚', 't': 'Seashell', 'res': {'nail': False, 'penny': True, 'steel': True}, 'band': 'Soft: a penny scratches it, a fingernail can’t.'},
                        {'k': 'marble', 'icon': '🔵', 't': 'Glass marble', 'res': {'nail': False, 'penny': False, 'steel': False}, 'band': 'Hard: nothing in the kit scratches it.'},
                        {'k': 'pyrite', 'icon': '✨', 't': 'Kai’s nugget', 'res': {'nail': False, 'penny': False, 'steel': False}, 'band': 'Hard: nothing in the kit scratches it.'}],
            'yes': 'scratched', 'no': 'no scratch',
            'q': {'q': 'Real gold is soft: a copper penny scratches it. What did the kit show about Kai’s nugget?',
                  'opts': [{'t': 'Nothing scratched it, so it’s much harder than gold.', 'ok': True, 'why': 'Right! Gold is soft. Pyrite is hard. One more piece of evidence that Kai found fool’s gold.'},
                           {'t': 'It’s as soft as chalk.', 'why': 'Look again: even the steel nail couldn’t scratch it.'},
                           {'t': 'It’s gold, because it’s hard.', 'why': 'Real gold is soft. A penny scratches it.'}]}}},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Plastic isn’t hard and doesn’t sink. And this one is magnetic!', 'B': 'Aluminum is silver-gray, but a magnet doesn’t pull it. Remember Kai’s coin?'},
        'q2': {'A': 'Properties don’t lie. But one property can match lots of materials.', 'C': 'Tests aren’t expensive. Gray alone left 5 suspects!'},
        'q3': {'B': 'A guess isn’t evidence. Kai guessed GOLD!', 'C': 'Start simple: look closely first.'}},
    'flags': {
        'ans-1': [
            {'label': 'one of Kai’s finds', 're': 'gold|nugget|bolt|silver|diamond|coin|pyrite'},
            {'label': 'two pieces of evidence', 'any': ['streak', 'magnet', 'scratch', 'nail', 'weigh', 'gram', ' g ', 'heavy', 'light', 'sink', 'float', 'color', 'colour', 'hard', 'clear', 'gray', 'grey', 'black'], 'min': 2},
            {'label': 'what it really is', 're': 'pyrite|fool|steel|iron|glass|alumin'}],
        'ans-3': [
            {'label': 'three more tests', 'any': ['magnet', 'float', 'water', 'sink', 'streak', 'scratch', 'weigh', 'mass', 'scale', 'heavy', 'light', 'bend', 'nail', 'file', 'shin', 'color', 'colour'], 'min': 3},
            {'label': 'why each one', 're': 'because|so |to see|to find|to check|tells|shows|if it|would'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|wrong|right|true|not true|false|not always|not every|could be|might|not iron'},
            {'label': 'two pieces of evidence', 'any': ['aluminum', 'aluminium', 'silver', 'lead', 'nickel', 'steel', 'magnet', 'coin', 'bolt', 'gray', 'grey', 'heavy', 'light', 'weigh', 'suspect', 'test'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-1': 15, 'ans-3': 18, 'cer-4': 30},
    'hints': {
        'ans-1': ['Pick one: the “GOLD!” nugget, the “SILVER” bolt, the “DIAMOND” or the old “COIN”.', 'Which two tests told you the most?', 'Try: Kai’s ___ is really ___. The best evidence is ___ and ___.'],
        'ans-3': ['Think about the tests from the lesson: magnet, water, weigh, streak, scratch.', 'Gray and hard could be iron, aluminum, silver or lead. Which test splits them?', 'Try: First I would ___ because ___. Next I would ___ because ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'Kai’s “old COIN” was gray, but a magnet didn’t pull it. It was aluminum.',
                'Gray left 5 suspects: iron, nickel, aluminum, silver and lead.',
                'Kai’s “SILVER” bolt was gray and hard, and only the magnet test showed it was steel.',
                'Iron is a cool metal.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · Kai’s treasure pouch', 'length': '40–50 s'},
        'warmup': {'label': 'Warm-Up · the claim tower (Clue 1)', 'length': '15–20 s',
                   'script': 'Dr. Nair here! Look at the two nuggets. Same color, same shine. Kai says his is GOLD. Drag a block under his sign and see if it holds. The locked blocks are tests. You’ll get those later!'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · fingerprint barcode (Clue 2)', 'length': '15–20 s',
                  'script': 'Let’s print a fingerprint for Kai’s silver bolt. Run each test, then flip the switch to match. Then drag the strip along the shelf until every stripe lines up. Which stripe gives it away?'},
        'part2': {'label': 'Part 2 · knock out the suspects (Clue 3)', 'length': '20–30 s'},
        'part3': {'label': 'Part 3 · fool’s gold!', 'length': '15–20 s',
                  'script': 'Here’s the test that looking can’t do. Drag each nugget across the white tile and check its streak. Then try the steel nail, and weigh them. Both pieces are the same size!'},
        'explore': {'label': 'Part 4 · build your claim (Clue 4)', 'length': '15–20 s',
                    'script': 'Three samples, six tests. Drag a test onto a sample’s row and watch the table fill. Then build a claim with two pieces of evidence. One clue alone won’t do!'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · your own mystery', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '15–20 s'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 30.01 (physical changes).'},
    },
    'videoOff': [],
    'lensVoice': False,
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Kai’s claim tower, crashed (Warm-Up)',
        'The bolt’s fingerprint lined up on the shelf (The Lesson)',
        'The suspect board with one suspect left (The Lesson)',
        'Two streaks on the white tile (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['Kai’s treasure pouch', 'Two streaks on a white tile', 'A fingerprint barcode'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · draw and label your mysteries', 'required': True, 'minLabels': 4,
                           'prompts': ['Draw your 3 mystery things', 'Label each one with what it is', 'Add one property label to each', 'Circle the test that helped most']}]},
    'hlCoach': copy.deepcopy(Q['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '✨', 'name': 'A chip of Kai’s fool’s gold',
                 'line': 'You cracked Case 29, part 2, and a chip of Kai’s fool’s gold goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next lesson: changes that don’t make anything new!'},
    'notebookTitle': Q['notebookTitle'],
    'notebook': copy.deepcopy(Q['notebook']) + [{'lesson': '29.02', 'icon': '✨', 'name': 'A chip of Kai’s fool’s gold'}],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are sorted. Nice work, detective!',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to see what it means.']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '#tab-vocab .fs-game[data-mod="tower"]'},
         'label': 'Warm-Up: gold or not?', 'q': 'Warm-Up: what I notice about the two nuggets, and a test I would try.', 'title': 'My nugget notes', 'compact': True,
         'fields': [{'t': 'Same on both', 'icon': '🟰', 'ph': 'Both nuggets are ___.'},
                    {'t': 'Something different', 'icon': '🔍', 'ph': 'But Kai’s nugget ___.'},
                    {'t': 'A test I would try', 'icon': '🧪', 'ph': 'I would test ___ because ___.'}]},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Then identify each one with evidence.'},
         'label': 'Part C: your own mystery', 'q': 'Part C: my 3 mystery things, my test results, and what each one is.', 'title': 'My mystery table',
         'fields': [{'t': 'Mystery A', 'icon': '🔍', 'ph': 'Color ___ · magnet? ___ · floats? ___ · hard? ___ → it’s ___'},
                    {'t': 'Mystery B', 'icon': '🔍', 'ph': 'Color ___ · magnet? ___ · floats? ___ · hard? ___ → it’s ___'},
                    {'t': 'Mystery C', 'icon': '🔍', 'ph': 'Color ___ · magnet? ___ · floats? ___ · hard? ___ → it’s ___'},
                    {'t': 'My evidence sentence', 'icon': '🔍', 'ph': 'I identify Mystery ___ as ___ because ___ and ___.', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Is every gray, hard material iron?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-1': 'Part B · Question 5', 'ans-3': 'Part B · Question 7', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'One property can fool you, so scientists match three or four properties to a property guide.',
    'key': ['property', 'fool', 'three', 'four', 'guide'],
    'small': ['can', 'so', 'to', 'a', 'or'],
    'model': 'A scientist might highlight “one property can fool you” and “three or four properties”. Those words hold the big idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: which properties helped identify the material, and which ones could fool you?']
D['cues'] = {
    'warmup': [{'at': '^nuggets', 'sel': '.fs-twr-pics', 'fx': 'pop', 'scroll': True},
               {'at': '^block', 'sel': '.fs-twr-pile .fs-twr-blk', 'i': 0, 'fx': 'point'},
               {'at': '^sign', 'sel': '.fs-twr-sign', 'fx': 'wiggle'},
               {'at': '^locked', 'sel': '.fs-twr-blk.locked', 'all': True, 'fx': 'glow'}],
    'part1': [{'at': '^fingerprint', 'sel': '.fs-bcd-mine', 'fx': 'pop', 'scroll': True},
              {'at': '^test', 'sel': '.fs-bcd-test', 'i': 0, 'fx': 'point'},
              {'at': '^switch', 'sel': '.fs-bcd-sw', 'i': 0, 'fx': 'glow'},
              {'at': '^shelf', 'sel': '[data-mod="barcode"] .fs-todo li', 'i': 2, 'fx': 'trace'}],
    'part3': [{'at': '^tile', 'sel': '.fs-skp-plate', 'fx': 'pop', 'scroll': True},
              {'at': '^streak', 'sel': '[data-mod="streak"] .fs-todo li', 'i': 0, 'fx': 'trace'},
              {'at': '^nail', 'sel': '.fs-skp-st', 'i': 1, 'fx': 'glow'},
              {'at': '^weigh', 'sel': '.fs-skp-st', 'i': 2, 'fx': 'glow'}],
    'explore': [{'at': '^tests', 'sel': '.fs-clt-tools', 'fx': 'pop', 'scroll': True},
                {'at': '^row', 'sel': '.fs-clt-row', 'i': 0, 'fx': 'point'},
                {'at': '^table', 'sel': '.fs-clt-tab table', 'fx': 'glow'},
                {'at': '^claim', 'sel': '[data-mod="claimtiles"] .fs-todo li', 'i': 2, 'fx': 'trace'}],
}
D['cueWords'] = json.load(open('cuewords.json', encoding='utf-8')) if os.path.exists('cuewords.json') else {}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
# budget counter (oao-audio-budget): G4 science = 1,400 credits per lesson; scripts are written to 95% (1,330). Nothing is generated from week 25 on.
clips = {k: v['script'] for k, v in D['slots'].items() if v.get('script')}
tot = sum(len(t) for t in clips.values())
for k, t in clips.items(): print(f'  {k:10} {len(t):4}')
print(f'this page: {tot} / 1400 credits ({tot/1400:.0%}), scripts only, 0 generated')
assert tot <= 1330
json.dump(clips, open('clip-scripts.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
