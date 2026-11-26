#!/usr/bin/env python3
"""Writes data.json and fixes.json for 27.01 (run from this folder). Case 27 "The Trophy Twins" (Dr. Priya Nair, Unit 6, the Palmetto Springs lost-and-found):
the Duck Derby's little brass trophy vanished, and TWO identical-looking trophies were turned in — one real brass, one painted plastic. Only measuring can tell them apart.
New: case.shelf (two drawn trophies with claim tags + the clerk's report + the engraver's sealed envelope), squeeze (Warm-Up: the bottle that fights back),
gates (Part 1: the matter gates), airscale (the wow: air on the scale, 2.0 -> 2.3 g), twins (Part 2: tell the twin jars apart with tools), dunklab (Part 3 = the old
Explore: weigh and dunk both trophies), kgsphere (after the solve: the real silicon-sphere photo), SIMS.panbalance (Tool of the Week: find the heavy box in two
weighings). SCRIPTS ONLY: clip scripts written and budgeted, nothing generated."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
O = json.load(open('../26-02/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)
def I(n, ext='jpg'): return 'images/27-01-' + n + '.' + ext

# ---------------------------------------------------------------- labels (standing approval)
fx('fix', 'unit label: “Ecosystems & Energy” is a leftover; the plan puts Module 27 in Unit 6 “Matter, Magnets, and Changes”', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Matter, Magnets &amp; Changes</div>')
fx('fix', 'matter and properties are physical science, not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standards label: the plan’s CPALMS code; TEKS is a Texas code that isn’t in the plan', '<div class="info-value">SC.4.P.8.1 · TEKS 4.6(A)</div>', '<div class="info-value">SC.4.P.8.1</div>')
fx('fix', 'quarter label in the footer: week 27 is Q4 in the Canvas plan (the header already says Q4)', 'Science &middot; Quarter 3 &middot; Student Lesson Page', 'Science &middot; Quarter 4 &middot; Student Lesson Page')

# ---------------------------------------------------------------- ticked fixes (Bethany, 25 Nov 2026)
fx('fix', '22.01 leftover: the Warm-Up title and subtitle named the toaster lesson', '<div class="act-title">🌅 Warm-Up: What Goes In, What Comes Out?</div>\n        <div class="act-subtitle">A familiar device, a hidden change</div>',
   '<div class="act-title">🌅 Warm-Up: The Bottle That Fights Back</div>\n        <div class="act-subtitle">Something invisible pushes back</div>')
fx('fix', '22.01 leftover: the toaster warm-up → the bottle squeeze',
   '<p>Think about a toaster. You drop in cold bread. A minute later, you pull out hot toast.</p>',
   '<p>Grab a clean, empty plastic bottle. Cap on tight: try to squash it. It fights back! Cap off: flat. So what was pushing back? The bottle looked empty.</p>')
fx('fix', '22.01 leftover: the toaster sketch → the squeeze test (played on the page, answered on the page)',
   "<p>In your notebook, draw a quick sketch of a toaster. On one side, label what goes IN. On the other, label what comes OUT. (Hint: bread on both sides — but something invisible is also going in. What is it?)</p>",
   '<p>Try the squeeze test right here. Then tell what pushed back.</p>')
fx('fix', '22.01 leftover: Notice & Wonder about the toaster',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Notice &amp; Wonder</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover: “energy can CONVERT … toasters” callout',
   r'<div class="callout callout-tip">\s*<span class="callout-icon">💡</span>\s*<p>Today you\'ll learn that energy can CONVERT.*?</p>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover (ticked): “Device” is in the plan row, but its meaning was about converting energy. This lesson’s devices measure',
   'A tool or machine designed to do a job. Most devices convert energy from one form to another — a flashlight, a toaster, a fan are all devices.',
   'A tool or machine made to do a job. A balance, a ruler and a measuring cup are measuring devices: they put a number on a property.')
fx('fix', '22.01 leftover: the Stop & Reason asked about “the three devices above” (no devices on this page)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', '9.01 leftover: Part C was a food chain; the checklist already asks for two property cards', '🎨 Part C &mdash; Build Your Own Food Chain', '🎨 Part C &mdash; Property Cards for Two Objects')
fx('fix', '9.01 leftover: Part C task (now two property cards for two look-alike home objects, typed and sketched on the page)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Pick TWO objects from your home that look a little alike: two mugs, two balls, two rocks. Give each a property card: its name, one observable property, one measurable property (a ruler or kitchen scale helps) and one behavior (does it float? does a magnet stick?). Then write one sentence comparing them.</p>', True)
fx('fix', '9.01 leftover: Reflect asked about a hawk; the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'supply list: what the Warm-Up and Part C can use', r'<span class="need-chip"><span>✏️</span>Colored pencils</span>', '<span class="need-chip"><span>🧴</span>A clean, empty plastic bottle with a cap</span><span class="need-chip"><span>⚖️</span>Optional: a kitchen scale, a ruler or a measuring cup</span>', True)
fx('fix', 'picture (ticked): the generated chart shows a 600 g / 500 mL water bottle marked “floats” (600 g in 500 mL sinks). The twins game now builds the same kind of property table live, so the picture comes out rather than teaching a wrong number. (The file stays in images/.)',
   r'<div class="lesson-figure scroll-reveal">.*?<div class="lesson-figure-caption"><strong>The more properties you list, the better you can describe any object\.</strong> Mass, volume, color, texture, and behavior all count\.</div>\s*</div>\s*', '', True)

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; plain words', r"<p>Hold this question in your head as you work\. By the end of the lesson.*?</p>",
   "<p>Keep this question in mind. By the end, you’ll describe objects by their properties and measure mass and volume yourself.</p>", True)
fx('plain', 'cut filler; no dash', r"<p>These six words show up all through the lesson\. <strong>Tap a card to flip it</strong>.*?</p>",
   "<p><strong>Tap a card to flip it</strong> and read what the word means.</p>", True)
fx('plain', 'Word Wall: no dash', 'Anything that has MASS and takes up SPACE. Air, water, your body, a rock — all matter.', 'Anything that has MASS and takes up SPACE. Air, water, your body and a rock are all matter.')
fx('plain', 'Part 1: senses first, no dashes',
   'Some are <span class="vtip">observable<span class="vtip-box"><span class="vtip-word">Observable</span>Notice with your senses.</span></span> — you notice them with your senses. Others are <span class="vtip">measurable<span class="vtip-box"><span class="vtip-word">Measurable</span>Has a number.</span></span> — you can put a NUMBER on them with a tool.',
   'Some are <span class="vtip">observable<span class="vtip-box"><span class="vtip-word">Observable</span>Notice with your senses.</span></span>: you notice them with your senses. Others are <span class="vtip">measurable<span class="vtip-box"><span class="vtip-word">Measurable</span>Has a number.</span></span>: you can put a NUMBER on them with a tool.')
fx('plain', 'safe tasting; shorter', '<li><strong>Observable:</strong> color, shape, texture, smell, taste (be careful!), how it sounds when tapped.</li>', '<li><strong>Observable:</strong> color, shape, texture, smell, taste (only food, with a grown-up).</li>')
fx('plain', 'shorter; the dunk lab teaches the measuring-cup idea itself', '<li><strong>Measurable:</strong> mass (grams, balance), volume (liters/cm³, ruler or graduated cylinder), length, hardness, temperature.</li>', '<li><strong>Measurable:</strong> mass (grams, on a balance), volume (how much space), length, temperature.</li>')
fx('plain', 'Part 1: the game tests these instead of the text giving the answers away',
   "<p>Air is matter too — it weighs a little (very little, but real) and it takes up space (try squeezing an inflated balloon). Water is matter. Even invisible water vapor in the air is matter. What ISN'T matter? Light, sound, shadows, ideas, and feelings. They don't have mass and don't take up space.</p>",
   '<p>Air is matter too: it weighs a little, and it takes up space. You felt that in the Warm-Up! But what about a shadow, or a sound? Don’t guess. Send them through the two tests.</p>')
fx('cut', 'lean: the Stop & Think (the shadow) is played inside the matter gates, where students test a shadow themselves',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: the misconception paragraph repeats the Warm-Up and the air-on-the-scale wow, which let students meet the wrong idea and watch it fail',
   r"\s*<p><strong>Common misconception:</strong> Some people think air \"isn't really there\".*?</p>", '', True)
fx('fix', 'Florida connection → the coquina photo lead-in (the photo activity Bethany picked); same limestone facts, told where students can see them',
   r'<div class="callout callout-info" style="margin-top:18px;">\s*<span class="callout-icon">🌴</span>\s*<p><strong>Florida connection:</strong> Florida\'s state rock is LIMESTONE.*?</p>\s*</div>',
   '<p>Florida’s state rock is LIMESTONE. It makes up most of Florida’s ground, and water slowly dissolves it, carving out springs and sinkholes. At an old fort in St. Augustine, the walls are a Florida limestone called coquina (co-KEE-nah), a rock packed with tiny shells. Look closely:</p>', True)
fx('plain', 'Part B question 5 label (Gathered Answers)', 'data-label="Pick ONE object from the diagram (limestone, water..."', 'data-label="One object: two observable and two measurable properties"')
fx('plain', 'Part B question 7 label (Gathered Answers)', 'data-label="Why do scientists list MANY properties when they d..."', 'data-label="Why scientists list MANY properties"')
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')

fx('plain', 'shorter: the two-rocks example carries the idea (and anchors the twins game)',
   '<p>The more properties you list, the more clearly you can describe an object. Two rocks might both be "gray and hard," but only one weighs 500 grams and only one is heavier than water.</p>',
   '<p>Two rocks might both be "gray and hard," but only one weighs 500 grams and only one is heavier than water.</p>')

# ---------------------------------------------------------------- lean cuts
fx('cut', 'removed: Key Concept (the body text and the games teach it), Observe & Reason (Part B question 5 asks the same thing), the Amazing Florida Fact (the helium balloon: true, cut for length) and Go Deeper (fire: true, beyond this lesson)',
   r'\s*<div style="background:#FFF6E5;border:2\.5px solid #F0C97A;[^>]*>\s*<div[^>]*>⭐ Key Concept</div>.*?(?=<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">Four Objects)', '\n\n      ', True)
fx('cut', 'lean: Observe & Reason under the diagram (Part B question 5 is the same ask) and the helium Amazing Florida Fact (true, cut for length)',
   r'<div class="socratic-q">\s*<span class="sq-icon">👀</span>\s*<div>\s*<div class="label">Observe &amp; Reason</div>.*?(?=<p>Florida’s state rock is LIMESTONE)', '', True)
fx('cut', 'lean: the fire Go Deeper (true, beyond this lesson)',
   r'<details style="margin-top:18px;border:2px solid #8B6FC0;[^>]*>\s*<summary[^>]*>🔭 Go Deeper · What about something like fire\?</summary>.*?</details>\s*', '', True)
fx('cut', 'Part 3 = the old Explore (Property Detective → the weigh and dunk test); the next button goes to Self-Check',
   '''<div class="tab-next-wrap">
        <button class="tab-next-btn" onclick="switchTab('explore')">Continue to 🔬 Explore →</button>''',
   H3 + 'Part 3 · The Weigh and Dunk Test</h3>\n      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">Back at the lost-and-found, the twin trophies are waiting. Time to measure: weigh each one, then hold it under the water and watch how far the water climbs.</p>\n  <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>')
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its Property Detective hunt lives on as Part C’s home property cards; its calcite fact, the balloon Think like a scientist — now the air-on-the-scale wow — and the mass-vs-weight Go Deeper go with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 6 removed (Bethany kept 5 and 7; the CER already argues about air)', r'<div class="pq">\s*<span class="pq-num"[^>]*>6</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 7 answered')
fx('cut', 'lean: Part C checklist ends with the required sketch', 'Two property cards (one per object) with name, observable, measurable, behavior, and a comparison sentence.',
   'Two property cards (one per object) with a name, an observable property, a measurable property, a behavior and a comparison sentence. Plus your labeled sketch.')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether air takes up space, supported with two pieces of evidence.',
   '<strong>Use Your Evidence:</strong> My claim about whether air takes up space, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a 9.01 leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Download your field journal (it has your answers and your sketch) and upload it to the Canvas assignment. Or copy your Gathered Answers (above) into Canvas.', True)

# ---------------------------------------------------------------- the story
PRIYA = {'name': 'Dr. Priya Nair', 'role': 'materials scientist (someone who studies what things are made of and how they behave)', 'initials': 'PN', 'color': '#7A5BB5', 'lens': 'beaker', 'voiceId': 'uYXf8XasLslADfZ2MB4u'}
D = {
    'lesson': '27.01', 'week': 27, 'day': 1, 'guide': 'priya', 'prefix': 'g4sci-27-1', 'manifestKey': '27-01',
    'paths': P['paths'], 'crew': {'priya': PRIYA},
    'expedition': {'num': 27, 'title': 'The Trophy Twins'},
    'ambient': {'icon': '🏷️', 'label': 'Lost and found'},
    'case': {
        'num': 27, 'title': 'The Trophy Twins', 'style': 'shelf',
        'hook': 'Dr. Priya Nair here. The Duck Derby’s little brass trophy never reached the winner: it vanished from the judges’ table. Now TWO matching trophies sit at the Palmetto Springs lost-and-found. One is real brass. One is a painted plastic copy from the party store.',
        'shelf': {
            'label': 'The lost-and-found shelf',
            'trophies': [
                {'tag': 'TROPHY A', 'line': 'Turned in Sunday, 4:10 p.m., by a jogger'},
                {'tag': 'TROPHY B', 'line': 'Turned in Monday, 9:05 a.m., in a paper bag'}],
            'note': 'The counter vote: almost everyone picked Trophy B. “It just looks newer and shinier.”'},
        'notice': {'head': 'PALMETTO SPRINGS LOST & FOUND', 'title': 'Lost property report',
                   'rows': [['Item', 'Small brass trophy cup, two handles'], ['Lost by', 'The Duck Derby judges'], ['Marks', 'None. The engraving was not done yet'], ['Problem', 'TWO matching trophies turned in']],
                   'line': 'Please send a scientist. We are not allowed to cut them open.'},
        'envelopes': [{'who': 'The engraver', 'icon': '✉️', 'front': 'Open when the real trophy is found', 'seal': 'SEALED',
                       'head': 'The engraver’s note',
                       'inside': 'I always weigh a trophy before I engrave it. The real brass cup is 412 grams exactly. — R. Vega, engraver',
                       'verdict': 'Trophy A weighed 412 grams on your balance. It matches!'}],
        'envLine': 'The engraver left a sealed note at the counter. Crack the case to open it.',
        'envOpen': 'The engraver’s note is open!',
        'stills': [],
        'question': 'Which trophy is the real brass one, and how can you prove it without cutting them open?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'squeeze', 'icon': '🧴', 'where': 'Warm-Up: the bottle that fights back', 't': 'Stuff can be real even when you can’t see it. The capped bottle would not squash, because the trapped air inside takes up space and pushes back.'},
            {'id': 'gates', 'icon': '🚪', 'where': 'The Lesson, Part 1: the matter gates', 't': 'Matter must pass BOTH tests: it has mass AND it takes up space. A rock, water and air all pass. A shadow and a sound fail.'},
            {'id': 'twins', 'icon': '🫙', 'where': 'The Lesson, Part 2: tell the twins apart', 't': 'Eyes can tie. The twin jars matched on every observable property. Only a measurement, mass, told them apart.'},
            {'id': 'dunklab', 'icon': '⚖️', 'where': 'The Lesson, Part 3: the weigh and dunk test', 't': 'Both trophies pushed the water up the SAME 150 milliliters, but Trophy A has 412 grams of mass and Trophy B only 165. Different stuff inside.'},
        ],
        'solve': {
            'title': 'Which trophy is the real brass one?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Trophy B. It looks newer and shinier, and most people at the counter picked it.', 'why': 'Check Clue 3. Eyes can tie! Every observable property matched. Looking newer is not proof.'},
                {'t': 'Trophy A. Both trophies take up the same space, but A has far more mass. Brass packs more stuff into the same space than painted plastic.', 'right': True,
                 'why': 'Case cracked! Same volume, very different mass: Trophy A must be made of heavier stuff. That is brass. And nobody had to cut anything open.'},
                {'t': 'Trophy A, because it is bigger than Trophy B.', 'why': 'Check Clue 4. The dunk test: both trophies pushed the water up the SAME amount. They are the same size.'},
                {'t': 'You can’t tell without cutting them open.', 'why': 'Check Clues 3 and 4. The balance and the tank told the twins apart from the outside.'},
            ]},
    },
    'squeeze': {
        'afterText': 'Then tell what pushed back.', 'kicker': 'Warm-Up game', 'title': 'The bottle that fights back',
        'why': {'icon': '🧴', 'q': 'Why squeeze a bottle?', 't': 'An “empty” bottle is really full of air. The trapped air shows it is there by pushing back.'},
        'todo': ['Put the cap on. Drag down on the bottle to squeeze it, or press Squeeze it.', 'Take the cap off and squeeze again.', 'Watch your squeeze log. Then answer the question.'],
        'model': 'A model bottle. Try it for real with a clean, empty plastic bottle.',
        'alt': 'A model plastic bottle on a table. A red cap can go on or off. Squeeze the bottle and watch what happens.',
        'capOnBtn': '🔴 Put the cap on', 'capOffBtn': '🔴 Take the cap off', 'squeezeBtn': '🤜 Squeeze it', 'resetBtn': '↺ A fresh bottle',
        'dragHint': 'Drag down on the bottle to squeeze it yourself, or press Squeeze it.',
        'needBoth': 'Now try it with the cap {k}.',
        'rows': {'on': ['Cap ON', 'It dented a little, then sprang right back.'], 'off': ['Cap OFF', 'It squashed flat. The air whooshed out the top.']},
        'logLabel': 'My squeeze log', 'cols': ['The bottle', 'What happened'],
        'q': 'The bottle looked empty. What pushed back when the cap was on?',
        'opts': [{'t': 'The air trapped inside. It takes up space, so there was no room to squash the bottle.', 'ok': True},
                 {'t': 'The plastic is just too stiff to squash.', 'miss': 'Look at your log. With the cap OFF, the same plastic squashed flat.'},
                 {'t': 'Nothing. The bottle was empty.', 'miss': 'Something stopped your squeeze when the cap was on. The only thing inside was air.'}],
        'win': 'Trapped air pushed back! Air is invisible, but it is really there: it takes up space. Clue 1!', 'clue': 'squeeze'},
    'gates': {
        'afterText': 'Send them through the two tests.', 'kicker': 'Part 1 game', 'title': 'The matter gates',
        'why': {'icon': '🚪', 'q': 'What are the gates?', 't': 'Two tests decide if something is matter: does it have mass, and does it take up space? Only things that pass BOTH gates come out as matter.'},
        'todo': ['Tap a thing to send it into the machine.', 'At each gate, pick the proof that answers the question.', 'Pass both gates: MATTER. Fail one: NOT MATTER. Test all five.'],
        'g1': {'t': 'Does it have mass?', 'sub': 'Would it press down on a scale?'},
        'g2': {'t': 'Does it take up space?', 'sub': 'Does it fill room that nothing else can use?'},
        'trayYes': 'MATTER', 'trayNo': 'NOT MATTER', 'pickLine': 'Tap the next thing to send it into the machine.',
        'passWord': 'matter!', 'failWord': 'not matter', 'countWord': 'things tested',
        'cands': [
            {'id': 'rock', 'icon': '🪨', 'name': 'A rock',
             'g1': {'pass': True, 'opts': [{'t': 'Yes. Put it on a scale and the number climbs.', 'ok': True}, {'t': 'Yes, because it is gray.', 'miss': 'Gray is a color your eyes notice. Which proof uses a SCALE?'}]},
             'g2': {'pass': True, 'opts': [{'t': 'Yes. Drop it in water and the water level climbs.', 'ok': True}, {'t': 'No. It is too small to take up space.', 'miss': 'Small still counts! What happens to the water when a rock goes in?'}]},
             'why': 'A rock has mass and takes up space. Matter.'},
            {'id': 'water', 'icon': '💧', 'name': 'A cup of water',
             'g1': {'pass': True, 'opts': [{'t': 'Yes. A full cup weighs more than an empty cup.', 'ok': True}, {'t': 'No. Water is too runny to weigh.', 'miss': 'Runny things still press on a scale. Compare a full cup and an empty cup.'}]},
             'g2': {'pass': True, 'opts': [{'t': 'Yes. It fills the cup. Nothing else can use that room.', 'ok': True}, {'t': 'No. You can put your finger in it.', 'miss': 'Your finger PUSHES the water out of the way. The water level climbs!'}]},
             'why': 'Water has mass and fills space. Matter.'},
            {'id': 'air', 'icon': '🎈', 'name': 'Air in a balloon',
             'g1': {'pass': True, 'opts': [{'t': 'Yes. A blown-up balloon weighs a tiny bit more than an empty one.', 'ok': True}, {'t': 'No. You can’t see air, so it can’t have mass.', 'miss': 'Seeing is not the test. The scale is. What did the Warm-Up bottle tell you?'}]},
             'g2': {'pass': True, 'opts': [{'t': 'Yes. The capped bottle would not squash. The air filled the room inside.', 'ok': True}, {'t': 'No. Air is invisible, so it takes up no room.', 'miss': 'Invisible is not the test. Remember what pushed back in the Warm-Up.'}]},
             'why': 'Air has a little mass and takes up space. Matter, even though you can’t see it.'},
            {'id': 'shadow', 'icon': '🌑', 'name': 'A shadow',
             'g1': {'pass': False, 'opts': [{'t': 'No. A shadow on a scale changes nothing.', 'ok': True}, {'t': 'Yes. Big shadows are heavy.', 'miss': 'Try it! Stand so your shadow falls on a scale. Does the number move?'}]},
             'g2': {'pass': False, 'opts': []},
             'why': 'A shadow is just a spot where light is blocked. No mass, no space. Not matter.'},
            {'id': 'sound', 'icon': '🔔', 'name': 'A bell’s ring',
             'g1': {'pass': False, 'opts': [{'t': 'No. A ringing room weighs the same as a quiet room.', 'ok': True}, {'t': 'Yes. Loud sounds are heavier than quiet ones.', 'miss': 'Can you pour a sound into a cup or set it on a scale? Loud is not heavy.'}]},
             'g2': {'pass': False, 'opts': []},
             'why': 'Sound is a wave traveling through matter (you learned that last week!), but the sound itself has no mass and fills no space. Not matter.'},
        ],
        'q': 'What must be true, BOTH at once, for something to be matter?',
        'opts': [{'t': 'It has mass AND it takes up space.', 'ok': True},
                 {'t': 'You can see it and touch it.', 'miss': 'Air passed both gates, and you can’t see air. Which two tests did the gates ask?'},
                 {'t': 'It is heavy and hard.', 'miss': 'A feather and water passed the same tests a rock did. The tests are about mass and space, not heavy and hard.'}],
        'win': 'Both tests, every time: mass AND space. That is what matter means. Clue 2!', 'clue': 'gates'},
    'airscale': {
        'after': 'gates', 'kicker': 'Wow!', 'title': 'Air on the scale',
        'todo': ['Weigh the empty balloon.', 'Pump it up.', 'Weigh it again and watch the number.'],
        'why': {'icon': '🎈', 'q': 'Can a scale see air?', 't': 'Pump extra air into a balloon and you squeeze more matter inside. A good scale can feel it.'},
        'model': 'A model of a real balloon test.', 'alt': 'A model digital kitchen scale and a red balloon.',
        'weighBtn': '⚖️ Put the balloon on the scale', 'weighBtn2': '⚖️ Weigh it again', 'pumpBtn': '💨 Pump it up', 'pumps': 3,
        'emptyG': 2.0, 'fullG': 2.3,
        'weigh1Line': 'Empty balloon: {x} g.', 'pumpLine': 'Pumped full! Now weigh it again.', 'weigh2Line': 'Blown-up balloon: {x} g. The number climbed!',
        'q': 'The scale climbed from 2.0 to 2.3 grams. What does the extra 0.3 grams prove?',
        'opts': [{'t': 'The air you pumped in has mass. Air is real matter.', 'ok': True},
                 {'t': 'The balloon got heavier because it stretched.', 'miss': 'Stretching does not add stuff. What did the pump push INTO the balloon?'},
                 {'t': 'The scale made a mistake.', 'miss': 'Scientists have done this test many times, very carefully. The number climbs every time.'}],
        'done': 'Wow! A scale can weigh air. Invisible does not mean nothing.'},
    'twins': {
        'afterText': 'but only one weighs 500 grams and only one is heavier than water.', 'kicker': 'Part 2 game', 'title': 'Tell the twins apart',
        'why': {'icon': '🫙', 'q': 'Why twin jars?', 't': 'Dr. Nair keeps twin practice jars, sealed just like the trophies. Which kind of property can split a tie your eyes can’t?'},
        'todo': ['Drag a tool onto the jars, or tap the tool and then the jars.', 'Each tool checks BOTH jars and adds a row to the table.', 'Try all four tools. Then answer the question.'],
        'alt': 'Two sealed jars that look exactly alike, labeled Jar A and Jar B.',
        'aName': 'Jar A', 'bName': 'Jar B', 'trayLabel': 'Dr. Nair’s tool tray',
        'dropHint': 'Each tool checks both jars at once.',
        'againMiss': 'You already used that tool. Try one with no check mark.',
        'tools': [
            {'k': 'look', 'icon': '👀', 't': 'Look', 'prop': 'Color and shape (observable)', 'a': 'Blue-gray, round', 'b': 'Blue-gray, round', 'same': True, 'note': 'Your eyes say: tie.'},
            {'k': 'feel', 'icon': '✋', 't': 'Feel', 'prop': 'Texture (observable)', 'a': 'Smooth, cool', 'b': 'Smooth, cool', 'same': True, 'note': 'Your fingers say: tie.'},
            {'k': 'ruler', 'icon': '📏', 't': 'Ruler', 'prop': 'Height (measurable)', 'a': '12 cm', 'b': '12 cm', 'same': True, 'note': 'A measurement can tie too. Keep going.'},
            {'k': 'balance', 'icon': '⚖️', 't': 'Balance', 'prop': 'Mass (measurable)', 'a': '310 g', 'b': '180 g', 'same': False, 'note': 'There it is! The balance broke the tie.'}],
        'logLabel': 'The twins’ property table', 'cols': ['Property', 'Jar A', 'Jar B', 'Verdict'],
        'sameWord': 'SAME', 'diffWord': 'DIFFERENT!', 'countWord': 'tools tried',
        'q': 'The jars looked, felt and measured the same height. What finally told them apart?',
        'opts': [{'t': 'A measurable property: their mass, in grams.', 'ok': True},
                 {'t': 'An observable property: one looked newer.', 'miss': 'Check the table. Every LOOK and FEEL row says SAME.'},
                 {'t': 'Nothing can tell twins apart.', 'miss': 'One row says DIFFERENT! Which tool made that row?'}],
        'win': 'When eyes tie, numbers decide. A measured property split the twins. Clue 3!', 'clue': 'twins'},
    'dunklab': {
        'afterText': 'weigh each one, then hold it under the water and watch how far the water climbs.',
        'kicker': 'Part 3 game', 'title': 'The weigh and dunk test',
        'why': {'icon': '🧪', 'q': 'Why dunk a trophy?', 't': 'When something goes all the way under, it shoves water aside, so the water line climbs exactly as much space as it takes up.'},
        'todo': ['Put each trophy on the balance and read the screen.', 'Hold each trophy under the water with the rod. Read how far the water climbs.', 'Fill both property cards. Then compare them.'],
        'model': 'A model lab bench. The rod holds the trophy under the water.',
        'alt': 'A model balance scale and a measuring tank with a push rod, used to measure each trophy.',
        'rodWord': 'push rod',
        'items': [
            {'id': 'a', 'name': 'Trophy A', 'massG': 412,
             'massOpts': [{'t': '395 g', 'miss': 'Look again at the number on the scale screen.'}, {'t': '412 g', 'ok': True}, {'t': '450 g', 'miss': 'Look again at the number on the scale screen.'}],
             'volOpts': [{'t': 'It climbed 100 mL', 'miss': 'Where did the water start, and where is the line now? Count the marks.'}, {'t': 'It climbed 150 mL', 'ok': True}, {'t': 'It climbed 200 mL', 'miss': 'Where did the water start, and where is the line now? Count the marks.'}]},
            {'id': 'b', 'name': 'Trophy B', 'massG': 165,
             'massOpts': [{'t': '125 g', 'miss': 'Look again at the number on the scale screen.'}, {'t': '165 g', 'ok': True}, {'t': '412 g', 'miss': 'That was Trophy A. Read this screen.'}],
             'volOpts': [{'t': 'It climbed 150 mL', 'ok': True}, {'t': 'It climbed 50 mL', 'miss': 'Count the marks. It climbed just as far as Trophy A did.'}, {'t': 'It climbed 300 mL', 'miss': 'Count the marks. It climbed just as far as Trophy A did.'}]},
        ],
        'tankStart': 600, 'tankRise': 150, 'unit': 'mL',
        'placeBtn': '⚖️ Put {name} on the balance', 'dunkBtn': '💧 Hold {name} under the water',
        'readScale': 'Read the screen. What is the mass?', 'readTank': 'How far did the water climb?',
        'cardWord': 'Property card', 'massWord': 'Mass', 'volWord': 'Volume (water climb)',
        'doneLine': 'Both cards are full. Read them side by side.',
        'q': 'Same volume, very different mass. What does that tell you about the trophies?',
        'opts': [{'t': 'They take up the same space but are made of different stuff. One packs much more matter into the same room.', 'ok': True},
                 {'t': 'Trophy A is bigger than Trophy B.', 'miss': 'Check the volume rows. The water climbed the SAME amount for both.'},
                 {'t': 'The balance must be broken.', 'miss': 'The balance read the twin jars just fine. Two true measurements can be different.'}],
        'win': 'You measured mass AND volume, and the numbers cracked it open: same space, different stuff. Clue 4!', 'clue': 'dunklab'},
    'exploreMod': 'dunklab',
    'kgsphere': {
        'after': '.fs-solve', 'kicker': 'Case closed · one more wow', 'title': 'The most careful measuring on Earth', 'lockLine': 'Crack the case first.',
        'todo': ['Look at the real photo.', 'Then answer the question.'],
        'img': I('kg-sphere'), 'alt': 'A scientist in a white coat and white gloves holds a dark, mirror-shiny silicon sphere about the size of a grapefruit.',
        'cap': 'A real, nearly perfect silicon sphere. Scientists polished it for years so its mass could help pin down exactly what one kilogram is. Photo: CSIRO, CC BY 3.0, via Wikimedia Commons.',
        'q': 'Why would scientists spend YEARS polishing one perfect ball?',
        'opts': [{'t': 'To pin down exactly how much matter one kilogram is, so every scale on Earth can agree.', 'ok': True},
                 {'t': 'Because shiny balls are worth a lot of money.', 'miss': 'It is not for selling. Think about what every scale in the world needs to agree on.'},
                 {'t': 'To use it as a mirror.', 'miss': 'It is shiny, but that is not the job. What property were they pinning down?'}],
        'fact': 'You used the same idea today: when looks can’t settle it, careful measuring can. Yours took one afternoon. Theirs took years.',
        'win': 'From a lost trophy to a perfect sphere: measuring matter settles arguments.'},
    'tool': {
        'name': 'Pan balance', 'icon': '⚖️', 'tab': 'assignment', 'after': '#tab-assignment .activity-card', 'key': '27-tool', 'sim': 'panbalance',
        'kicker': 'Bonus · Tool of the Week', 'teaser': 'Weigh pairs on a two-pan balance. Then find the heavy box in just two weighings.',
        'done': 'You balanced it! A pan balance sticker is in your Field Notebook.',
        'why': {'icon': '⚖️', 'q': 'What is a pan balance?', 't': 'One of the oldest measuring tools in the world. Put something on each pan: the heavier side sinks. When the pans sit level, both sides hold the same mass.'},
        'panbalance': {
            'title': 'Which side sinks?',
            'todo': ['Tap an object, then tap again to load the other pan. Press Weigh them.', 'Weigh two different pairs.', 'Then try the two-weighings puzzle.'],
            'model': 'A model balance. When the pans sit level, the two sides have the same mass.',
            'trayLabel': 'The tray (tap one object for the left pan, then one for the right)',
            'weighBtn': '⚖️ Weigh them', 'clearBtn': '↺ Clear the pans',
            'objs': [
                {'id': 'feather', 'icon': '🪶', 't': 'a feather', 'g': 1},
                {'id': 'sponge', 'icon': '🧽', 't': 'a big dry sponge', 'g': 12},
                {'id': 'golf', 'icon': '⛳', 't': 'a small golf ball', 'g': 46},
                {'id': 'spoon', 'icon': '🥄', 't': 'a metal spoon', 'g': 60}],
            'tipLine': 'The {a} side sank: more mass, even when it is not bigger.',
            'balLine': '{a} and {b} balance: the same mass.',
            'pairLine': 'Weigh one more pair. Can the BIGGER thing lose?',
            'puzzle': {
                'head': 'The two-weighings puzzle', 'sub': 'Three boxes look exactly alike. One is heavier inside. You may weigh only TWICE. Find it!',
                'boxes': ['Box 1', 'Box 2', 'Box 3'], 'heavy': 'Box 2',
                'weighsLeft': '{n} weighings left',
                'tipLine': 'The pan with {a} sank!', 'balLine': '{a} and {b} balance. Neither one is the heavy box.',
                'ask': 'Which box is the heavy one?',
                'opts': [{'t': 'Box 1', 'miss': 'Check your weighings. Did Box 1 ever sink a pan?'}, {'t': 'Box 2', 'ok': True}, {'t': 'Box 3', 'miss': 'Check your weighings. Did Box 3 ever sink a pan?'}],
                'done': 'Puzzle solved in two weighings or fewer!'},
            'q': {'q': 'The pans sit LEVEL. What does that tell you?',
                  'opts': [{'t': 'The two sides hold the same mass.', 'ok': True},
                           {'t': 'The two sides are the same size.', 'why': 'A balance feels mass, not size. A big sponge can balance a tiny stone.'},
                           {'t': 'The balance is stuck.', 'why': 'Level is an answer, not a jam: it means the two sides match.'}]}}},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'A shadow is just a dark spot where light is blocked. Run it through the two gates.', 'B': 'Can you pour a sound into a jar, or set it on a scale? Think about the gates.'},
        'q2': {'A': 'A ruler measures how long something is. Which tool did the trophies sit on?', 'C': 'A thermometer measures how hot. Which tool reads in grams?'},
        'q3': {'B': '“Brown” is something your eyes notice: observable. Which option has a NUMBER?', 'C': 'A smell has no number. Which option could you write in grams?'}},
    'flags': {
        'ans-1': [
            {'label': 'your object', 're': 'limestone|rock|stone|coquina|water|bottle|balloon|air|wood|block'},
            {'label': 'observable (your senses)', 're': 'gray|grey|white|clear|brown|tan|smooth|rough|hard|soft|round|bumpy|shape|color|colour|wet|cool|cold|shiny|holes|see|feel|looks'},
            {'label': 'measurable (a number and a tool)', 're': 'gram|mass|volume|liter|litre|\\bml\\b|millilit|\\bcm\\b|centimeter|inch|weigh|measur|length|tall|height|scale|balance|ruler|temperature'}],
        'ans-3': [
            {'label': 'why many properties help', 're': 'tell (them |things )?apart|sure|certain|exact|clear|better|more|mix|match|describe|know which|prove'},
            {'label': 'what could go wrong with one', 're': 'wrong|mix|confus|same|two|both|another|mistake|could be|might be|not enough'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|wrong|right|true|not true|false|does take|doesn.?t|does not|takes up'},
            {'label': 'two pieces of evidence', 'any': ['bottle', 'cap', 'squeeze', 'squash', 'crush', 'push', 'balloon', 'scale', '2.3', '0.3', 'pump', 'gate', 'trophy', 'water', 'climb', 'rose', '150', 'dunk', 'tank', 'balance', 'mass', 'space'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-1': 12, 'ans-3': 15, 'cer-4': 30},
    'hints': {
        'ans-1': ['Pick one object. What do your eyes and fingers notice? What could a tool put a number on?', 'Observable: color, shape, texture. Measurable: mass in grams, volume, length.', 'Try: The ___ is ___ and ___. Its mass is about ___ and its length is about ___.'],
        'ans-3': ['Remember the twin jars. How many properties matched before one split them?', 'One property can tie, or fit LOTS of objects. More properties pin down one exact thing.', 'Try: Scientists list many properties because ___. With only one, ___ could happen.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'The capped bottle would not squash: the trapped air inside pushed back.',
                'The balloon made the scale climb from 2.0 to 2.3 grams.',
                'Each trophy pushed the water line up 150 milliliters when it went under.',
                'Almost everyone at the counter picked the shinier trophy.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'photos': [
        {'id': 'coquina', 'afterText': 'a rock packed with tiny shells. Look closely:', 'kicker': 'Look closer', 'short': 'Florida limestone up close',
         'title': 'Florida limestone, up close', 'todo': ['Tap each number on the photo.', 'For each label, decide: observable, or would you need a tool?'],
         'why': {'icon': '🏰', 'q': 'What are we looking at?', 't': 'A wall of the Castillo de San Marcos, a 350-year-old fort in St. Augustine. Its blocks are coquina: tiny shells pressed into rock.'},
         'img': I('limestone-coquina'), 'alt': 'A very close view of a coquina limestone wall: thousands of tiny tan shell pieces pressed together, with a smoother pale patch and small holes.',
         'credit': 'Kiran891, Castillo de San Marcos National Monument', 'license': 'CC BY-SA 4.0, via Wikimedia Commons',
         'hotspots': [
             {'n': 1, 'x': 47, 'y': 66, 'label': 'Tiny shells', 't': 'Thousands of little shell pieces, pressed together into rock. You can SEE them: an observable property.'},
             {'n': 2, 'x': 82, 'y': 22, 'label': 'A smooth, pale patch', 't': 'Weather wore this spot smooth and lighter in color. Color and texture: observable properties.'},
             {'n': 3, 'x': 19, 'y': 52, 'label': 'A little hole', 't': 'Water slowly dissolves limestone and leaves holes. In Florida’s ground, holes like this grow into springs and sinkholes.'}],
         'task': {'q': 'Match it: which label shows each clue about this rock?',
                  'items': [
                      {'icon': '🐚', 'step': 'Tiny pieces pressed together into rock', 'ans': 1, 'evid': 'Coquina is made of tiny shells pressed together. You can SEE them: observable.', 'miss': 'Look for the spot crowded with little shell bits.'},
                      {'icon': '🎨', 'step': 'A patch with a different color and feel', 'ans': 2, 'evid': 'Weather wore one patch smooth and pale. Color and texture are observable properties.', 'miss': 'Look for the smoother, lighter spot.'},
                      {'icon': '💧', 'step': 'Proof that water slowly eats limestone', 'ans': 3, 'evid': 'Water dissolves limestone and leaves holes. Big holes become Florida’s springs and sinkholes.', 'miss': 'Look for the dark little opening in the wall.'}],
                  'win': 'Good eye! A photo shows observable properties. For mass or volume you would still need tools, like today’s balance and tank.'}}],
    'slots': {
        'welcome': {'label': 'Welcome · The Trophy Twins', 'length': '40–50 s'},
        'warmup': {'label': 'Warm-Up · the bottle that fights back (Clue 1)', 'length': '15–20 s',
                   'script': 'Dr. Nair here. Before we touch those trophies, squeeze a bottle. Put the cap on, then drag down on the bottle. Feel that push back? Now take the cap off and squeeze again. Watch your squeeze log fill in, and ask: what was pushing?'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · the matter gates (Clue 2)', 'length': '15–20 s',
                  'script': 'Time to test, not guess. Tap the rock to send it into the machine. Gate one asks: does it have mass? Gate two: does it take up space? Pick your proof at each gate. The shadow and the bell might surprise you. Fill both trays.'},
        'part2': {'label': 'Part 2 · tell the twins apart (Clue 3)', 'length': '20–30 s'},
        'explore': {'label': 'Part 3 · the weigh and dunk test (Clue 4)', 'length': '15–20 s',
                    'script': 'The real test. Put Trophy A on the balance and read the screen. Then hold it under the water with the rod, and read how far the water climbs. Do both trophies. When both property cards are full, compare them. Same space, different mass. What does that mean?'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · property cards', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '15–20 s',
                     'script': 'A classmate says air takes up no space because you can’t see it. You tested that today! Pick your side, tap two facts in the planner, then write your reasoning. Claim, evidence, reasoning. That’s your C-E-R.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 27.02 (classify by properties, pick the right material for a job).'},
    },
    'videoOff': [],
    'lensVoice': False,
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'The squashed bottle, cap off (Warm-Up)',
        'Your full MATTER tray (The Lesson)',
        'The scale reading 2.3 g (The Lesson)',
        'Both property cards, filled in (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['The bottle that fought back', 'The twin trophies on the shelf', 'The dunk tank, mid-climb'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · draw and label your two objects', 'required': True, 'minLabels': 4,
                           'prompts': ['Draw your two look-alike objects side by side', 'Label one OBSERVABLE property on each', 'Label one MEASURABLE property with its number', 'Circle the property that best tells them apart']}]},
    'hlCoach': copy.deepcopy(O['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🏆', 'name': 'The derby trophy',
                 'line': 'You cracked Case 27, and the derby trophy goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next time: use properties to pick the right material for a job!'},
    'notebookTitle': O['notebookTitle'],
    'notebook': copy.deepcopy(O['notebook']) + [{'lesson': '27.01', 'icon': '🏆', 'name': 'The derby trophy'}],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You measure up!',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to see what it means.']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '#tab-vocab p', 'text': 'Then tell what pushed back.'},
         'label': 'Warm-Up: the squeeze test', 'q': 'Warm-Up: what happened with the cap on and off, and what pushed back.', 'title': 'My squeeze test', 'compact': True,
         'fields': [{'t': 'With the cap ON', 'icon': '🔴', 'ph': 'The bottle ___.'},
                    {'t': 'With the cap OFF', 'icon': '⚪', 'ph': 'The bottle ___.'},
                    {'t': 'What pushed back', 'icon': '🌬️', 'ph': 'I think ___ pushed back, because ___.'}]},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Then write one sentence comparing them.'},
         'label': 'Part C: property cards for two objects', 'q': 'Part C: my two property cards and my comparison sentence.', 'title': 'My property cards',
         'fields': [{'t': 'Object 1: name, one observable, one measurable, one behavior', 'icon': '🗂️', 'ph': 'My ___ is ___ (observable). Its ___ is ___ (measurable). It ___ (behavior).', 'long': True},
                    {'t': 'Object 2: name, one observable, one measurable, one behavior', 'icon': '🗂️', 'ph': 'My ___ is ___ (observable). Its ___ is ___ (measurable). It ___ (behavior).', 'long': True},
                    {'t': 'My comparison sentence', 'icon': '⚖️', 'ph': 'They both ___, but only one ___.'}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Does air take up space?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-1': 'Part B · Question 5', 'ans-3': 'Part B · Question 7', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'Matter is anything that has mass and takes up space, even air you cannot see.',
    'key': ['matter', 'mass', 'space', 'air'],
    'small': ['is', 'that', 'and', 'even', 'you'],
    'model': 'A scientist might highlight “matter”, “mass” and “space”. Those words hold the big idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this tell what matter is, or how a property can be observed or measured?']

EV = '#tab-assignment .act-body > div:has(> .fs-plan)'
D['cues'] = {
    'warmup': [{'at': '^squeeze', 'sel': '.fs-sq-stage', 'fx': 'glow', 'scroll': True},
               {'at': '^cap', 'sel': '.fs-sq-cap', 'fx': 'point'},
               {'at': '^drag', 'sel': '.fs-sq-stage', 'fx': 'pop'},
               {'at': '^off', 'sel': '.fs-sq-cap', 'fx': 'point'},
               {'at': '^log', 'sel': '[data-mod="squeeze"] .fs-todo li', 'i': 2, 'fx': 'trace'}],
    'part1': [{'at': '^rock', 'sel': '.fs-mg-tray .fs-mg-cand', 'i': 0, 'fx': 'point', 'scroll': True},
              {'at': '^one', 'sel': '.fs-mg-gate[data-g="1"]', 'fx': 'pop'},
              {'at': '^two', 'sel': '.fs-mg-gate[data-g="2"]', 'fx': 'pop'},
              {'at': '^proof', 'sel': '[data-mod="gates"] .fs-todo li', 'i': 1, 'fx': 'trace'},
              {'at': '^trays', 'sel': '.fs-mg-out', 'fx': 'glow'}],
    'explore': [{'at': '^balance', 'sel': '.fs-dk-stage', 'fx': 'glow', 'scroll': True},
                {'at': '^rod', 'sel': '[data-mod="dunklab"] .fs-todo li', 'i': 1, 'fx': 'trace'},
                {'at': '^cards', 'sel': '.fs-dk-cards', 'fx': 'pop'},
                {'at': '^compare', 'sel': '[data-mod="dunklab"] .fs-todo li', 'i': 2, 'fx': 'trace'}],
    'evidence': [{'at': '^classmate', 'sel': EV + ' > p', 'i': 0, 'fx': 'trace', 'scroll': True},
                 {'at': '^side', 'sel': '.fs-plan .fs-plan-row', 'i': 0, 'fx': 'pop'},
                 {'at': '^facts', 'sel': '.fs-plan .fs-plan-row', 'i': 1, 'fx': 'glow'},
                 {'at': '^reasoning', 'sel': '.fs-cer .fs-cer-row', 'i': 2, 'fx': 'glow', 'scroll': True}],
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
