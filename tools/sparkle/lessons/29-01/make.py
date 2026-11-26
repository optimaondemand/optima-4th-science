#!/usr/bin/env python3
"""Writes data.json and fixes.json for 29.01 (run from this folder). Case 29 "Campfire Night" (Dr. Priya Nair, Unit 7 in Canvas, Palmetto Springs):
the end-of-year campout. Ranger Bell's Changes Bingo card lists 8 things that happen tonight; which made a NEW substance?
New (Bethany's brainstorm, 26 Nov 2026): case.bingo, lens (Warm-Up: the s'more split), toolkit (Part 1: safe tools only), timelapse (Part 3: rust, rot, cooking and
Lady Liberty's patina = the wow, with real photos), conveyor (Part 4 = the old Explore: the property sort on a belt), glowtwist (after the solve), SIMS.cabbage (Tool).
SCRIPTS ONLY: nothing generated."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
O = json.load(open('../27-01/data.json', encoding='utf-8'))
Q = json.load(open('../28-02/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)
def VT(word, head, tip): return '<span class="vtip">' + word + '<span class="vtip-box"><span class="vtip-word">' + head + '</span>' + tip + '</span></span>'

# ---------------------------------------------------------------- labels
fx('fix', 'unit label (ticked): “Ecosystems & Energy” is a leftover; the plan puts Module 29 under “Matter, Magnets, and Changes”', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Matter, Magnets &amp; Changes</div>')
fx('fix', 'science label (ticked): properties and changes of matter are physical science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standards label: the plan’s CPALMS codes; TEKS is a Texas code that isn’t in the plan', '<div class="info-value">SC.4.P.8.1, SC.4.P.9.1 · TEKS 4.6(A)</div>', '<div class="info-value">SC.4.P.8.1, SC.4.P.9.1</div>')
fx('fix', 'quarter label in the footer (ticked): week 29 is Q4 (the header already says Q4)', 'Science &middot; Quarter 3 &middot; Student Lesson Page', 'Science &middot; Quarter 4 &middot; Student Lesson Page')
fx('plain', 'shorter; no dashes', r"<p>Hold this question in your head as you work\. Near the end of the year.*?</p>",
   "<p>Keep this question in mind. Today you’ll learn the big difference scientists make: physical properties (what a material IS) and clues that a NEW substance has formed.</p>", True)

# ---------------------------------------------------------------- ticked: energy-lesson leftovers
fx('fix', '22.01 leftover: the Warm-Up title named the toaster lesson', '<div class="act-title">🌅 Warm-Up: What Goes In, What Comes Out?</div>\n        <div class="act-subtitle">A familiar device, a hidden change</div>',
   '<div class="act-title">🌅 Warm-Up: One S’more, Two Changes</div>\n        <div class="act-subtitle">Same stuff, or new stuff?</div>')
fx('fix', '22.01 leftover: the toaster warm-up → the s’more split',
   '<p>Think about a toaster. You drop in cold bread. A minute later, you pull out hot toast.</p>',
   '<p>It’s Campfire Night at Palmetto Springs! Dr. Nair toasted a s’more: a graham cracker, a square of chocolate and a marshmallow, all warmed by the fire.</p>')
fx('fix', '22.01 leftover: the toaster sketch → the lens game (played and answered on the page)',
   "<p>In your notebook, draw a quick sketch of a toaster. On one side, label what goes IN. On the other, label what comes OUT. (Hint: bread on both sides — but something invisible is also going in. What is it?)</p>",
   '<p>Pull it apart and look closely at each layer. Which part became something new?</p>')
fx('fix', '22.01 leftover: Notice & Wonder about the toaster',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Notice &amp; Wonder</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover: “energy can CONVERT … toasters” callout',
   r'<div class="callout callout-tip">\s*<span class="callout-icon">💡</span>\s*<p>Today you\'ll learn that energy can CONVERT.*?</p>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover (ticked): “Device” meant converting energy',
   'A tool or machine designed to do a job. Most devices convert energy from one form to another — a flashlight, a toaster, a fan are all devices.',
   'A tool or machine made to do a job, like a toaster or a grill.')
fx('fix', '22.01 leftover (ticked): the Stop & Reason asked about “the three devices above … INPUT and OUTPUT”',
   r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', '9.01 leftover (ticked): Part C was a food chain; the checklist already describes a property/chemical-change sort', '🎨 Part C &mdash; Build Your Own Food Chain', '🎨 Part C &mdash; Sort 4 Things From Home')
fx('fix', '9.01 leftover (ticked): Part C task → the checklist’s 2-column sort (typed on the page, sketched in a required drawing)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Find 4 things at home: 2 with a physical property you can see or measure, and 2 that show a clue of a chemical change (rust, a browned piece of toast, an old banana…). Sort them, and back up one with evidence.</p>', True)
fx('fix', '9.01 leftover (ticked): Reflect asked about a hawk; the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'supply list: Part C needs nothing special', r'<span class="need-chip"><span>✏️</span>Colored pencils</span>', '<span class="need-chip"><span>🏠</span>4 things from around your home</span>', True)

# ---------------------------------------------------------------- Part 1, Part 2, Part 3
fx('plain', 'Part 1: no dash', 'Color, hardness, mass, shape, magnetism, whether it floats — all of these are physical properties.', 'Color, hardness, mass, shape, magnetism and whether it floats are all physical properties.')
fx('plain', 'Part 1: no dash; a lead-in for the tool kit', "You've been describing matter this way all year — properties tell you what something IS.</p>",
   "Properties tell you what something IS.</p>\n      <p>Try it: describe a wooden block without changing it.</p>")
fx('cut', 'lean: the Stop & Think (describe a block) is played by the tool kit',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('plain', 'Part 2: no dash', 'iron + water + air slowly form reddish rust — a brand-new substance.', 'iron + water + air slowly form reddish rust, a brand-new substance.')
fx('fix', 'standards gap (ticked): SC.4.P.9.1 names decay and cooking; the page never did. One line, backed by the time-lapse banana and pancake; no dash',
   "isn't just changing shape — it's changing INTO something else.</p>",
   "isn’t just changing shape. It’s changing INTO something else.</p>\n      <p>Rotting food and cooking food make new substances too. When a banana rots, tiny living things called mold and bacteria break it down. When pancake batter cooks, it can never go back to runny batter.</p>\n\n"
   "      " + H3 + "Part 3 · Watch Changes Happen</h3>\n      <p>Some changes take seconds. Some take years. Watch four of them, and catch every clue.</p>")
fx('cut', 'lean: the misconception (any change is chemical) is played by the conveyor sort',
   r'\s*<p><strong>Common misconception:</strong> Some people think any change to a material is a chemical change\..*?</p>', '', True)
fx('plain', 'figure: drop the image-suggestion fallback (the image exists)', r'\s*onerror="this\.style\.display=\'none\';[^"]*"\s*/>\s*<div class="image-suggestion".*?</div>\s*</div>', ' />', True)
fx('cut', 'lean: Key Concept (the games teach it)',
   r'<div style="background:#FFF6E5;border:2\.5px solid #F0C97A;[^>]*>\s*<div[^>]*>⭐ Key Concept</div>.*?</p>\s*</div>\s*', '', True)
fx('cut', 'lean: the Four Examples tap diagram is played by the conveyor; with it go Observe & Reason, the Statue of Liberty Amazing Fact (now the time-lapse wow, with real photos), the salty-air Florida connection and the “clues can fool you” Go Deeper (food coloring is a conveyor card; soda fizz is quiz Q3)',
   r'<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">Four Examples to Classify</h3>.*?(?=<div class="tab-next-wrap">)', '', True)

# ---------------------------------------------------------------- Word Wall: no dashes
fx('plain', 'Word Wall: no dash', 'A property you only see when a material CHANGES into something new — like rusting or burning.', 'A property you only see when a material CHANGES into something new, like rusting or burning.')
fx('plain', 'cut filler; no dash', r"<p>These six words show up all through the lesson\. <strong>Tap a card to flip it</strong>.*?</p>",
   "<p><strong>Tap a card to flip it</strong> and read what the word means.</p>", True)

# ---------------------------------------------------------------- Part 4 = the old Explore
fx('cut', 'Part 4 = the old Explore (Property Sort → the conveyor sort, the plan’s product); the next button goes to Self-Check',
   '''<div class="tab-next-wrap">
        <button class="tab-next-btn" onclick="switchTab('explore')">Continue to 🔬 Explore →</button>''',
   H3 + 'Part 4 · The Property Sort</h3>\n      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">Is it a property, a physical change or a clue that something new formed? Sort each card before it rides off the belt.</p>\n  <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>')
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (the home sort lives on as Part C; the apple Amazing Fact, the rusty-bike Think like a scientist and the both-kinds Go Deeper go with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)

# ---------------------------------------------------------------- Assignment
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('plain', 'Part B question 5 no longer points at the cut diagram', 'Pick ONE example from the diagram (blue block, wood burning, rock mass, iron rusting).', 'Pick ONE example: a blue block, wood burning, the mass of a rock or iron rusting.')
fx('plain', 'Part B question 5 label (Gathered Answers)', 'data-label="Pick ONE example from the diagram (blue block, woo..."', 'data-label="One example: property or chemical clue, with evidence"')
fx('plain', 'Part B question 6 label (Gathered Answers)', 'data-label="Explain the difference between a PHYSICAL property..."', 'data-label="Physical property vs chemical-change clue"')
fx('cut', 'lean: Part B question 7 removed (Bethany kept 5 and 6; quiz Q3 asks about bubbles)', r'<div class="pq">\s*<span class="pq-num"[^>]*>7</span>.*?</textarea>\s*', '', True)
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C checklist ends with the required sketch', 'A 2-column property/chemical-change sort with at least 4 examples and one evidence sentence.',
   'My 4 things sorted into property or chemical-change clue, with one evidence sentence. Plus your labeled sketch.')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether ALL color changes are chemical changes, supported with two pieces of evidence.',
   '<strong>Use Your Evidence:</strong> My claim about whether every color change is a chemical change, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a 9.01 leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Download your field journal (it has your answers and your sketch) and upload it to the Canvas assignment. Or copy your Gathered Answers (above) into Canvas.', True)
fx('plain', 'closing: no dash', "We're heading into the final stretch of the year — next lesson, you'll use property evidence to IDENTIFY mystery materials like a real detective.",
   "Next lesson, you’ll use property evidence to IDENTIFY mystery materials like a real detective.")

# ---------------------------------------------------------------- the story
PRIYA = O['crew']['priya']
SQ = [('🍫', 'Chocolate melting on a s’more'), ('🍡', 'Marshmallow toasting brown'), ('🪵', 'Logs burning to ash'), ('🧊', 'Ice melting in the cooler'),
      ('🔩', 'The old grill rusting'), ('🍌', 'A banana peel rotting in the compost'), ('🥞', 'Pancakes cooking for breakfast'), ('♨️', 'Water boiling for cocoa')]
D = {
    'lesson': '29.01', 'week': 29, 'day': 1, 'guide': 'priya', 'prefix': 'g4sci-29-1', 'manifestKey': '29-01',
    'paths': P['paths'], 'crew': {'priya': PRIYA},
    'expedition': {'num': 29, 'title': 'Campfire Night'},
    'ambient': {'icon': '🔥', 'label': 'The campfire at the springs'},
    'case': {
        'num': 29, 'title': 'Campfire Night', 'style': 'order',
        'hook': 'Dr. Priya Nair here. It’s the end-of-year campout at Palmetto Springs! Ranger Bell made a Changes Bingo card. To win, you have to find every square where a NEW substance formed. Things changed all night long. Which ones made something new?',
        'bingo': {'head': 'PALMETTO SPRINGS CAMPOUT', 'title': 'Ranger Bell’s Changes Bingo', 'free': {'icon': '🏕️', 't': 'Campfire Night (free!)'},
                  'squares': [{'icon': s[0], 't': s[1]} for s in SQ], 'sign': 'Ranger Bell'},
        'stills': [],
        'question': 'Which bingo squares made a NEW substance?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'lens', 'icon': '🔍', 'where': 'Warm-Up: one s’more, two changes', 't': 'Melted chocolate is still chocolate. The toasted marshmallow grew a crispy brown shell and a new smell: something NEW.'},
            {'id': 'toolkit', 'icon': '🪪', 'where': 'The Lesson, Part 1: safe tools only', 't': 'Physical properties, like color, size, mass and floating, can be checked without changing the material. Burning or rotting would change it.'},
            {'id': 'timelapse', 'icon': '⏱️', 'where': 'The Lesson, Part 3: watch changes happen', 't': 'Rust, rot and cooking all make new substances. Clues: a color change, bubbles, a new smell, a new coating.'},
            {'id': 'conveyor', 'icon': '📦', 'where': 'The Lesson, Part 4: the property sort', 't': 'Melting, boiling, folding and stirring in food coloring are physical changes. It’s still the same stuff.'},
        ],
        'solve': {
            'title': 'Which squares made something new?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'All 8, because everything changed.', 'why': 'Check Clue 4. Melting chocolate, melting ice and boiling water are physical changes. Same stuff!'},
                {'t': 'The toasting marshmallow, the burning logs, the rusting grill, the rotting peel and the cooking pancakes. The melting chocolate, the melting ice and the boiling water are still the same stuff.', 'right': True,
                 'why': 'Bingo! Five squares made new substances. The other three only changed form.'},
                {'t': 'Only the burning logs, because only fire makes new stuff.', 'why': 'Check Clue 3. Rust, rot and cooking make new substances too, and rust and rot need no fire.'},
                {'t': 'Everything that got hot: the chocolate, the marshmallow, the logs, the pancakes and the water.', 'why': 'Check Clues 1 and 4. Heat melted the chocolate and boiled the water, but they’re still chocolate and water. And the grill and the peel changed with no heat at all.'},
            ]},
    },
    'lens': {
        'afterText': 'Which part became something new?', 'kicker': 'Warm-Up game', 'title': 'Lens on the layers',
        'why': {'icon': '🔍', 'q': 'Why use a lens?', 't': 'Scientists look closely for clues. A magnifying lens helps you see what changed in each layer.'},
        'todo': ['Press Pull it apart.', 'Drag the 🔍 lens over each layer to find its clues (or tap the layer).', 'Mark each layer SAME STUFF or NEW STUFF.'],
        'model': 'A model s’more. Try it at a real campfire with an adult.', 'pullBtn': '✋ Pull it apart', 'lensTip': 'Drag the 🔍 lens over each layer, or tap a layer’s hidden spots.',
        'layers': [
            {'id': 'mallow', 't': 'Marshmallow', 'kind': 'mallow', 'new': True,
             'spots': [{'x': 60, 'y': 14, 't': 'A brown, crispy shell'}, {'x': 120, 'y': 22, 't': 'Tiny bubbles inside the goo'}, {'x': 180, 'y': 14, 't': 'Smells like caramel, not like a plain marshmallow'}],
             'why': 'Heat turned some of the sugar into new, brown, toasty substances.', 'miss': 'Look at its clues: a crispy brown shell and a brand-new smell. Is that the same stuff?'},
            {'id': 'choc', 't': 'Chocolate', 'kind': 'choc', 'new': False,
             'spots': [{'x': 60, 'y': 10, 't': 'Soft, shiny and drippy'}, {'x': 170, 'y': 8, 't': 'Still tastes like chocolate'}],
             'why': 'Melting only changed its shape. Cool it and it gets hard again: still chocolate.', 'miss': 'It melted, but is it still chocolate? Cool it down and see.'},
            {'id': 'cracker', 't': 'Graham cracker', 'kind': 'cracker', 'new': False,
             'spots': [{'x': 40, 'y': 13, 't': 'Warm, still crunchy'}, {'x': 190, 'y': 13, 't': 'Same holes, same crumbs'}],
             'why': 'It just got warm. Still a graham cracker.', 'miss': 'Look at its clues. Did anything new show up?'}],
        'sameWord': '🟰 SAME STUFF', 'newWord': '✨ NEW STUFF', 'notYet': 'Lens it to find clues…',
        'q': 'Which layer became something NEW?',
        'opts': [{'t': 'The toasted marshmallow: a crispy brown shell and a new smell.', 'ok': True},
                 {'t': 'The chocolate, because it melted.', 'miss': 'Melted chocolate is still chocolate. Let it cool and it’s hard again.'},
                 {'t': 'All three, because they all got hot.', 'miss': 'Getting hot isn’t enough. The cracker and the chocolate are the same stuff.'}],
        'win': 'Melting = same stuff. Toasting = new stuff. Clue 1!', 'clue': 'lens'},
    'toolkit': {
        'afterText': 'Try it: describe a wooden block without changing it.', 'kicker': 'Part 1 game', 'title': 'Safe tools only',
        'why': {'icon': '🪪', 'q': 'What is an ID card for a material?', 't': 'A list of its physical properties: what you can see or measure while it stays the same material.'},
        'todo': ['Drag a tool onto the wooden block (or tap the tool, then the block).', 'Each safe tool adds a property to the ID card.', 'Some tools would change the wood. They won’t work!'],
        'thing': {'icon': '🪵', 't': 'Wooden block'}, 'kitLabel': 'The tool kit', 'dropLine': 'Drop a tool here', 'cardHead': 'ID card: wooden block',
        'tools': [
            {'k': 'eyes', 'icon': '👀', 't': 'Look closely', 'ok': True, 'prop': 'Color', 'val': 'light brown with stripes', 'why': 'The stripes are the wood’s grain.'},
            {'k': 'fire', 'icon': '🔥', 't': 'A match', 'ok': False, 'why': 'Burning would turn the wood into ash and smoke: brand-new substances! Then you’d be describing ash, not wood.'},
            {'k': 'ruler', 'icon': '📏', 't': 'Ruler', 'ok': True, 'prop': 'Length', 'val': '5 cm', 'why': 'Measuring doesn’t change it.'},
            {'k': 'scale', 'icon': '⚖️', 't': 'Scale', 'ok': True, 'prop': 'Mass', 'val': '30 g', 'why': 'Still the same block after weighing.'},
            {'k': 'rain', 'icon': '🌧️', 't': 'A year out in the rain', 'ok': False, 'why': 'A year in the rain and the wood starts to rot: tiny living things break it into new substances. That changes it!'},
            {'k': 'tub', 'icon': '🛁', 't': 'Water tub', 'ok': True, 'prop': 'Floats?', 'val': 'Yes, it floats', 'why': 'A quick dunk. Pull it out and it’s still wood.'},
            {'k': 'magnet', 'icon': '🧲', 't': 'Magnet', 'ok': True, 'prop': 'Magnetic?', 'val': 'No', 'why': 'Wood has no iron in it.'},
            {'k': 'touch', 'icon': '✋', 't': 'Touch', 'ok': True, 'prop': 'Hardness', 'val': 'hard, a little rough', 'why': 'Feeling it doesn’t change it.'}],
        'need': 6, 'countWord': 'properties on the ID card', 'emptyLine': 'No properties yet.',
        'q': 'After all those tests, what is the block made of?',
        'opts': [{'t': 'Still wood. Physical properties describe it without changing it.', 'ok': True},
                 {'t': 'Something new, because we measured it.', 'miss': 'Measuring doesn’t change it. Look: it’s still a wooden block.'},
                 {'t': 'Ash, because we tested it.', 'miss': 'The match was refused! Nothing burned.'}],
        'win': 'Six properties, and the block is still wood. Clue 2!', 'clue': 'toolkit'},
    'timelapse': {
        'afterText': 'Watch four of them, and catch every clue.', 'kicker': 'Part 3 game', 'title': 'The time-lapse',
        'why': {'icon': '⏱️', 'q': 'What is a time-lapse?', 't': 'A way to watch a slow change fast, like days or years squeezed into seconds.'},
        'todo': ['Pick a change. Drag the time slider forward.', 'When a clue pops up, tap it and stamp what kind of clue it is.', 'Do all four. Save Lady Liberty for last!'],
        'slideLabel': 'Drag time forward', 'tapTip': 'Tap a clue that popped up to stamp it.', 'stampQ': 'What kind of clue is “{b}”?', 'countWord': 'clues stamped',
        'types': [{'k': 'color', 'icon': '🎨', 't': 'Color change'}, {'k': 'gas', 'icon': '🫧', 't': 'Bubbles (a gas)'}, {'k': 'smell', 'icon': '👃', 't': 'A new smell'}, {'k': 'coat', 'icon': '🧱', 't': 'A new coating or texture'}],
        'changes': [
            {'id': 'nail', 'icon': '🔩', 't': 'A nail in wet grass', 'unit': 'day', 'unitWord': 'days', 'from': 0, 'to': 60, 'kind': 'nail', 'alt': 'A model iron nail lying in wet grass.', 'model': 'A model. Real rust takes weeks.',
             'badges': [{'at': 20, 't': 'Orange-brown spots', 'type': 'color', 'miss': 'What happened to its color?'}, {'at': 70, 't': 'A flaky coat that rubs off', 'type': 'coat', 'miss': 'Something new is covering the nail. What kind of clue is that?'}],
             'endLine': 'Rust! Iron, water and air made a brand-new substance.'},
            {'id': 'banana', 'icon': '🍌', 't': 'A banana on the counter', 'unit': 'day', 'unitWord': 'days', 'from': 0, 'to': 12, 'kind': 'banana', 'alt': 'A model banana getting spotted, brown and soft.', 'model': 'A model. Real bananas take about two weeks.',
             'badges': [{'at': 30, 't': 'Brown, then black spots', 'type': 'color', 'miss': 'Look at the peel. What changed?'}, {'at': 70, 't': 'A strong, sour smell', 'type': 'smell', 'miss': 'This clue is one you’d notice with your nose.'}],
             'endLine': 'Rotting (decay) is a chemical change. Tiny living things, like mold and bacteria, break the banana down into new substances.'},
            {'id': 'pancake', 'icon': '🥞', 't': 'Pancake batter on a hot pan', 'unit': 'second', 'unitWord': 'seconds', 'from': 0, 'to': 120, 'kind': 'pancake', 'alt': 'A model pancake cooking in a pan.', 'model': 'A model pancake.',
             'badges': [{'at': 35, 't': 'Bubbles pop on top', 'type': 'gas', 'miss': 'Little holes are popping open. What makes them?'}, {'at': 75, 't': 'A golden-brown underside', 'type': 'color', 'miss': 'Peek underneath. What changed?'}],
             'endLine': 'Cooking is a chemical change. The pancake can never go back to being runny batter.'},
            {'id': 'liberty', 'icon': '🗽', 't': 'Lady Liberty’s copper', 'unit': 'year', 'from': 1886, 'to': 1920, 'kind': 'photo', 'wow': True,
             'photo': 'images/29-01-liberty-copper-face.jpg', 'photo2': 'images/29-01-liberty-green.jpg',
             'alt': 'A full-size copper copy of the Statue of Liberty’s face, shiny reddish brown.', 'alt2': 'The Statue of Liberty today, green all over.',
             'cap': '1886: new copper is shiny reddish brown, like this full-size copy of her face in the museum.', 'cap2': 'Today: green all over. Nobody painted her!',
             'credit': 'Copper face copy: Renata3, public domain · The statue in 2024: AskALotl, CC0 · both via Wikimedia Commons',
             'badges': [{'at': 25, 't': 'The copper turns dark brown', 'type': 'color', 'miss': 'Compare the start with now. What changed?'}, {'at': 80, 't': 'A green coat called patina', 'type': 'coat', 'miss': 'A new layer formed on top of the copper. What kind of clue is that?'}],
             'endLine': 'Wow! Nobody painted her. Copper, air and rain slowly made a brand-new green substance called patina. It even protects the copper underneath!'}],
        'q': 'What do rust, a rotting banana, a cooked pancake and Lady Liberty’s green coat have in common?',
        'opts': [{'t': 'Each one made a NEW substance.', 'ok': True},
                 {'t': 'They all melted.', 'miss': 'Nothing melted. Look at your clues: color, smell, bubbles, a new coat.'},
                 {'t': 'They all happened fast.', 'miss': 'The rust took weeks, and Lady Liberty took about 30 years!'}],
        'win': 'Rust, rot, cooking and patina: four new substances. Clue 3!', 'clue': 'timelapse'},
    'conveyor': {
        'afterText': 'Sort each card before it rides off the belt.', 'kicker': 'Part 4 game', 'title': 'The property sort',
        'why': {'icon': '📦', 'q': 'Three bins?', 't': 'A property tells what something IS. A physical change keeps the same stuff. A chemical clue means something new may have formed.'},
        'todo': ['Press Start the belt.', 'Read each card. Tap the right bin before it reaches the end (or drag the card in).', 'Too fast? Tap the turtle to slow it down.'],
        'bins': [{'k': 'prop', 'icon': '🎨', 't': 'Property (what it IS)'}, {'k': 'phys', 'icon': '🔄', 't': 'Physical change (same stuff)'}, {'k': 'chem', 'icon': '✨', 't': 'Chemical clue (new stuff)'}],
        'cards': [
            {'id': 'rock', 'icon': '🪨', 't': 'A rock is hard', 'bin': 'prop', 'why': 'Hardness describes what the rock IS.', 'miss': 'Did anything change, or is this just describing the rock?'},
            {'id': 'ice', 'icon': '🧊', 't': 'Ice melting in the cooler', 'bin': 'phys', 'why': 'Melted ice is still water. Freeze it again and it’s ice.', 'miss': 'Melted ice is still water. Is that new stuff?'},
            {'id': 'toast', 'icon': '🍞', 't': 'Bread toasting brown', 'bin': 'chem', 'why': 'The brown crust is a new substance. You can’t un-toast it.', 'miss': 'Can you turn toast back into bread? What does that tell you?'},
            {'id': 'plane', 'icon': '✈️', 't': 'Folding a paper airplane', 'bin': 'phys', 'why': 'New shape, same paper.', 'miss': 'Unfold it. Is it still paper?'},
            {'id': 'wood', 'icon': '🪵', 't': 'Wood is light brown', 'bin': 'prop', 'why': 'Color describes what the wood IS.', 'miss': 'Did anything change, or is this describing the wood?'},
            {'id': 'dye', 'icon': '💧', 't': 'Food coloring stirred into water', 'bin': 'phys', 'why': 'It looks different, but it’s still water with dye in it. No new substance.', 'miss': 'Careful: a color change can fool you. Is it still water with dye in it?'},
            {'id': 'log', 'icon': '🍄', 't': 'A log rotting on the bank', 'bin': 'chem', 'why': 'Decay: tiny living things break the wood into new substances.', 'miss': 'Rotting is like the banana in Part 3. Same stuff, or new stuff?'},
            {'id': 'boil', 'icon': '♨️', 't': 'Water boiling for cocoa', 'bin': 'phys', 'why': 'The steam is still water, just as a gas.', 'miss': 'Steam is water too. Is that new stuff?'},
            {'id': 'magnet', 'icon': '🧲', 't': 'A magnet sticks to the grill', 'bin': 'prop', 'why': 'Being magnetic is a property of the steel grill.', 'miss': 'Did the grill change, or is this describing it?'},
            {'id': 'match', 'icon': '🔥', 't': 'A match burning', 'bin': 'chem', 'why': 'Smoke, light and ash: new substances.', 'miss': 'Look for the clues: smoke, light and ash. Same stuff?'}],
        'secs': 9, 'startBtn': '▶ Start the belt', 'slowBtn': '🐢 Slow the belt', 'fastBtn': '🐇 Normal speed', 'missedLine': 'Missed one! “{c}” will come back around.', 'countWord': 'cards sorted',
        'q': 'Which pair is BOTH a physical change?',
        'opts': [{'t': 'Ice melting and water boiling', 'ok': True},
                 {'t': 'Bread toasting and a log rotting', 'miss': 'Those both made new substances. Check your Chemical clue bin.'},
                 {'t': 'A rock is hard and wood is brown', 'miss': 'Those are properties, not changes.'}],
        'win': 'Melting, boiling, folding and dye in water: same stuff, new look. Clue 4!', 'clue': 'conveyor'},
    'exploreMod': 'conveyor',
    'glowtwist': {
        'after': '.fs-solve', 'kicker': 'Case closed · a twist', 'title': 'Lights out!', 'lockLine': 'Crack the case first.',
        'why': {'icon': '🌙', 'q': 'What happened?', 't': 'The campfire is out. Ranger Bell hands you a glow stick for the walk back to the tents.'},
        'todo': ['Bend the glow stick until it cracks.', 'Watch. Then decide: did something new form?'],
        'model': 'A model glow stick.', 'crackBtn': '💥 Bend it until it cracks',
        'q': 'No flame and no heat, but light. Did a new substance form?',
        'opts': [{'t': 'Yes. Light can be a clue that chemicals mixed and made something new.', 'ok': True},
                 {'t': 'No, because nothing got hot.', 'miss': 'Heat isn’t the only clue. Light, color, bubbles and smell count too.'},
                 {'t': 'No, it’s just a tiny flashlight.', 'miss': 'There’s no battery inside! Read the card above.'}],
        'fact': {'q': 'What’s inside a glow stick?', 't': 'A thin glass tube floating in a liquid. Bending it breaks the tube, the two liquids mix, and they react to make light. You can’t un-mix them, and the glow fades when the chemicals are used up.'},
        'win': 'Light with no fire: a chemical change you can carry. Good night, campers!'},
    'tool': {
        'name': 'Red cabbage indicator', 'icon': '🥬', 'tab': 'assignment', 'after': '#tab-assignment .activity-card', 'key': '29-tool', 'sim': 'cabbage',
        'kicker': 'Bonus · Tool of the Week', 'teaser': 'A real chemist’s trick: purple cabbage juice changes color in acids and bases.',
        'done': 'Tool of the Week: you used a real color-change indicator.',
        'why': {'icon': '🧪', 'q': 'What is an indicator?', 't': 'A liquid that changes color to show whether something is an acid (like lemon juice) or a base (like baking soda). Chemists use them every day.'},
        'cabbage': {
            'title': 'Drip and see', 'todo': ['Drag the dropper into a cup (or tap the cup).', 'Watch the color. Test all four cups.', 'Then figure out the mystery cup.'],
            'dropWord': 'Cabbage juice dropper', 'model': 'A model. Try it at home with an adult: boil chopped red cabbage, cool the purple water, and drip it in.',
            'cups': [{'k': 'vinegar', 't': 'Vinegar', 'col': '#E0457B', 'colName': 'pink', 'line': 'Pink! Vinegar is an acid. The juice changes color to show it.'},
                     {'k': 'water', 't': 'Plain water', 'col': '#7B4BA8', 'colName': 'purple', 'line': 'Still purple. Plain water is neither an acid nor a base.'},
                     {'k': 'soda', 't': 'Baking-soda water', 'col': '#2FA38A', 'colName': 'blue-green', 'line': 'Blue-green! Baking-soda water is a base.'},
                     {'k': 'mystery', 't': 'Mystery cup', 'col': '#E8558A', 'colName': 'pink', 'line': 'Pink! The mystery cup acts like the vinegar. (It’s lemon juice.)'}],
            'q': {'q': 'The mystery cup turned pink. Which cup is it most like?',
                  'opts': [{'t': 'The vinegar', 'ok': True, 'why': 'Both turned pink, so both are acids. The mystery cup was lemon juice.'},
                           {'t': 'The plain water', 'why': 'Water stayed purple. The mystery cup turned pink.'},
                           {'t': 'The baking-soda water', 'why': 'Baking-soda water turned blue-green. The mystery cup turned pink.'}]}}},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'A browned crust is a NEW substance, like the toasted marshmallow.', 'C': 'Rust is a new substance, like the nail in the time-lapse.'},
        'q2': {'A': 'Cut paper is still paper.', 'B': 'Melted ice is still water. Remember the cooler card?'},
        'q3': {'B': 'Soda fizz is gas that was already there. No new substance.', 'C': 'The pancake bubbles WERE a clue of a chemical change.'}},
    'flags': {
        'ans-1': [
            {'label': 'your example', 're': 'block|blue|wood|burn|rock|mass|iron|rust|nail'},
            {'label': 'property or chemical clue', 're': 'physical|chemical|property|clue|new substance|same stuff'},
            {'label': 'evidence', 're': 'because|smoke|ash|rust|color|colour|brown|red|orange|heavy|mass|measure|new|flak|light'}],
        'ans-2': [
            {'label': 'a physical property', 're': 'physical|color|colour|hard|mass|shape|size|float|magnet'},
            {'label': 'a chemical-change clue', 're': 'chemical|rust|burn|bubbl|smell|smoke|rot|cook|toast|new substance'},
            {'label': 'an example from home', 're': 'kitchen|home|house|my |toast|stove|fridge|bike|apple|banana|pan|cook|bread|egg|counter|yard'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|wrong|right|true|not true|false|not always|not every|sometimes'},
            {'label': 'two pieces of evidence', 'any': ['food coloring', 'dye', 'water', 'liberty', 'statue', 'patina', 'green', 'copper', 'chocolate', 'melt', 'rust', 'banana', 'toast', 'marshmallow', 'pancake', 'brown'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-1': 12, 'ans-2': 18, 'cer-4': 30},
    'hints': {
        'ans-1': ['Pick one: a blue block, wood burning, the mass of a rock or iron rusting.', 'Did the material stay the same, or did something new form?', 'Try: ___ is a (physical property / chemical-change clue) because ___.'],
        'ans-2': ['A physical property describes what something IS. A chemical-change clue means something new formed.', 'Look around your kitchen: what color is the fridge? What happens to bread in a toaster?', 'Try: A physical property is ___, like ___. A chemical-change clue is ___, like ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'Food coloring turned the water a new color, but it was still water with dye in it.',
                'Melted chocolate looked shiny and new, but it was still chocolate.',
                'Lady Liberty turned green because a new substance, patina, formed.',
                'Colors are pretty.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · Campfire Night', 'length': '40–50 s'},
        'warmup': {'label': 'Warm-Up · lens on the layers (Clue 1)', 'length': '15–20 s',
                   'script': 'Dr. Nair here, by the campfire! Press Pull it apart. Then drag the lens over each layer and find its clues. Is the chocolate still chocolate? And what happened to the marshmallow?'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · safe tools only (Clue 2)', 'length': '15–20 s',
                  'script': 'Describe this wooden block without changing it. Drag a tool from the kit onto the block, and watch the ID card fill up. Some tools would change the wood. Which ones?'},
        'part2': {'label': 'Part 2 · signs of a chemical change', 'length': '20–30 s'},
        'part3': {'label': 'Part 3 · the time-lapse (Clue 3)', 'length': '15–20 s',
                  'script': 'Drag the time slider forward. Watch for clues to pop up. Tap each one, then stamp what kind of clue it is. And save Lady Liberty for last!'},
        'explore': {'label': 'Part 4 · the property sort (Clue 4)', 'length': '15–20 s',
                    'script': 'Press Start the belt. Read each card as it rides along. Then tap the right bin before it reaches the end. Too fast? Tap the turtle to slow it down.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · sort 4 things from home', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '15–20 s'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 29.02 (mystery materials).'},
    },
    'videoOff': [],
    'lensVoice': False,
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'The s’more with all three layers marked (Warm-Up)',
        'The wooden block’s full ID card (The Lesson)',
        'Lady Liberty, green, with both clues stamped (The Lesson)',
        'Your three sorted bins (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['A toasted s’more, layer by layer', 'Lady Liberty, then and now', 'A rusty nail'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · draw and label your sort', 'required': True, 'minLabels': 4,
                           'prompts': ['Draw two columns', 'Label them PROPERTY and CHEMICAL CLUE', 'Draw your 4 things in the right columns', 'Label each thing']}]},
    'hlCoach': copy.deepcopy(O['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🍡', 'name': 'A toasted marshmallow',
                 'line': 'You cracked Case 29, and a toasted marshmallow goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next lesson: mystery materials!'},
    'notebookTitle': O['notebookTitle'],
    'notebook': copy.deepcopy(Q['notebook']) + [{'lesson': '29.01', 'icon': '🍡', 'name': 'A toasted marshmallow'}],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are sorted. Nice work, chemist!',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to see what it means.']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '#tab-vocab p', 'text': 'Which part became something new?'},
         'label': 'Warm-Up: one s’more, two changes', 'q': 'Warm-Up: which layer stayed the same stuff, which became new stuff, and my evidence.', 'title': 'My s’more clues', 'compact': True,
         'fields': [{'t': 'Same stuff', 'icon': '🟰', 'ph': 'The ___ stayed the same stuff.'},
                    {'t': 'New stuff', 'icon': '✨', 'ph': 'The ___ became something new.'},
                    {'t': 'My evidence', 'icon': '🔍', 'ph': 'I know because ___.'}]},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'back up one with evidence'},
         'label': 'Part C: sort 4 things from home', 'q': 'Part C: my 4 things, sorted, and one evidence sentence.', 'title': 'My home sort',
         'fields': [{'t': 'Thing 1', 'icon': '1️⃣', 'ph': '___ : property or chemical clue?'},
                    {'t': 'Thing 2', 'icon': '2️⃣', 'ph': '___ : property or chemical clue?'},
                    {'t': 'Thing 3', 'icon': '3️⃣', 'ph': '___ : property or chemical clue?'},
                    {'t': 'Thing 4', 'icon': '4️⃣', 'ph': '___ : property or chemical clue?'},
                    {'t': 'My evidence sentence', 'icon': '🔍', 'ph': 'I classified ___ as ___ because ___.', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Does every color change mean a chemical change?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-1': 'Part B · Question 5', 'ans-2': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'Physical properties describe what a material is, but clues like rust, smoke and bubbles mean a new substance may have formed.',
    'key': ['physical', 'properties', 'clues', 'new', 'substance'],
    'small': ['what', 'but', 'like', 'may', 'have'],
    'model': 'A scientist might highlight “physical properties”, “clues” and “new substance”. Those words hold the big idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this describe what a material IS, or a clue that it changed into something new?']
D['cues'] = {
    'warmup': [{'at': '^pull', 'sel': '[data-mod="lens"] .fs-mug-go .fs-btn, [data-mod="lens"] .fs-todo li', 'fx': 'point', 'scroll': True},
               {'at': '^lens', 'sel': '.fs-lns-stage', 'fx': 'glow'},
               {'at': '^layer', 'sel': '[data-mod="lens"] .fs-todo li', 'i': 1, 'fx': 'trace'},
               {'at': '^marshmallow', 'sel': '[data-mod="lens"] .fs-todo li', 'i': 2, 'fx': 'trace'}],
    'part1': [{'at': '^block', 'sel': '.fs-tlk-thing', 'fx': 'pop', 'scroll': True},
              {'at': '^drag', 'sel': '.fs-tlk-kit .fs-dragc', 'i': 0, 'fx': 'point'},
              {'at': '^card', 'sel': '.fs-tlk-card', 'fx': 'glow'},
              {'at': '^change', 'sel': '[data-mod="toolkit"] .fs-todo li', 'i': 2, 'fx': 'trace'}],
    'part3': [{'at': '^slider', 'sel': '.fs-tlp-r', 'fx': 'point', 'scroll': True},
              {'at': '^clues', 'sel': '[data-mod="timelapse"] .fs-todo li', 'i': 1, 'fx': 'trace'},
              {'at': '^stamp', 'sel': '[data-mod="timelapse"] .fs-count', 'fx': 'pop'},
              {'at': '^liberty', 'sel': '[data-mod="timelapse"] .fs-twn-tools .fs-in-chip', 'i': 3, 'fx': 'wiggle'}],
    'explore': [{'at': '^start', 'sel': '[data-mod="conveyor"] .fs-mug-go .fs-btn', 'fx': 'point', 'scroll': True},
                {'at': '^card', 'sel': '.fs-cnv-belt', 'fx': 'glow'},
                {'at': '^bin', 'sel': '.fs-cnv-bins', 'fx': 'pop'},
                {'at': '^turtle', 'sel': '[data-mod="conveyor"] .fs-todo li', 'i': 2, 'fx': 'trace'}],
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
