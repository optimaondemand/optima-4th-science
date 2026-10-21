#!/usr/bin/env python3
"""Writes data.json and fixes.json for 16.01 (run from this folder). First Unit 4 lesson: June Calloway, Case 16 "The Quarry Vote"."""
import json, copy
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../15-02/data.json', encoding='utf-8'))
R = json.load(open('../r4-1/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

# ---------------------------------------------------------------- ticked fixes (Bethany, 21 Oct 2026)
fx('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist already asks for a balance-scale tradeoff',
   '🎨 Part C &mdash; Build Your Own Food Chain', '⚖️ Part C &mdash; Weigh One Florida Tradeoff')
fx('fix', 'copy-paste leftover: Part C task from 9.01 (typed on the page now; the scale sketch is a bonus)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   "Pick one Florida resource use (a solar farm, a rock quarry, citrus farming, a beach rebuild, or water for a city). Weigh it like a scientist: two benefits, two environmental costs, and one protection strategy.</p>", True)
fx('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'quarter label in the footer: week 16 is Quarter 2', 'Science &middot; Quarter 3 &middot;', 'Science &middot; Quarter 2 &middot;')
fx('fix', 'this is an Earth science lesson (4-ESS3-1), not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Earth Science</div>')
fx('fix', 'the balance-scale image was never made (an AI prompt showed instead); the Load the scale game replaces it',
   r'<div class="lesson-figure scroll-reveal">.*?<div class="lesson-figure-caption">.*?</div>\s*</div>\s*', '', True)
fx('fix', 'shaky fact: “fertilizes farms in 50 states” can’t be checked; “phosphate dust” isn’t the main water risk (leaking mine waste is)',
   'BENEFIT: Florida phosphate fertilizes farms in 50 states, helping grow food for millions. Jobs and economic activity in central Florida. ENVIRONMENTAL COST: Mining permanently changes the land. Phosphate dust can pollute water. Mine sites need years to recover.',
   'BENEFIT: Florida phosphate helps make fertilizer for farms across the country, so they can grow more food. It also brings jobs to central Florida. ENVIRONMENTAL COST: Mining changes the land for good. Mining waste can pollute water if it leaks. Mine sites need years to recover.')
fx('fix', 'vague line (“sharing the grid”) cut',
   ' Use Florida\'s sunny days well by sharing the grid."', '"')

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; dash removed',
   "Hold this question in your head as you work. By the end of the lesson, you'll be able to break down a real Florida resource decision into its three parts: benefit, environmental cost, and protection strategy.",
   "Keep this question in mind. By the end, you’ll be able to break a real Florida resource choice into three parts: the benefit, the environmental cost, and a protection strategy.")
fx('plain', 'answers are made on the page now (the game below)',
   r"<p>Think about ONE thing you used this morning\..*?</p>\s*<p>Under it, draw two columns\..*?</p>",
   "<p>Think about something you did this morning. Every choice has two sides: something you <strong>GAINED</strong> and something you <strong>USED UP</strong>.</p>", True)
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', 'plain words; dash removed; the case is a real-world example',
   "<p>When a Florida city decides whether to build new homes, mine phosphate, or open a solar farm, it's making a <span class=\"vtip\">tradeoff<span class=\"vtip-box\"><span class=\"vtip-word\">Tradeoff</span>Gaining one thing while giving up another.</span></span> — gaining something and giving up something else. Scientists break tradeoffs into three parts that you can write down:</p>",
   "<p>When a Florida town decides whether to open a rock quarry, build new homes, or put in a solar farm, it’s making a <span class=\"vtip\">tradeoff<span class=\"vtip-box\"><span class=\"vtip-word\">Tradeoff</span>Gaining one thing while giving up another.</span></span>: it gains one thing and gives up another. Scientists break a tradeoff into three parts:</p>")
fx('plain', 'dash removed', 'What people GAIN — energy, food, jobs, building materials.', 'What people GAIN: energy, food, jobs, building materials.')
fx('plain', 'dash removed', 'What the environment LOSES — clean air, habitat, water, soil.', 'What the environment LOSES: clean air, habitat, water, soil.')
fx('plain', 'dash removed', 'What can be done to LOWER the environmental cost — laws, technology, careful planning.', 'What people can do to LOWER the environmental cost: laws, technology, careful planning.')
fx('plain', 'plain words', "Most resource decisions aren't \"do this or don't.\" They're \"how do we do this with the lowest cost?\" That's where",
   "Most resource choices aren’t just “yes” or “no.” People ask, “How can we do this with the smallest cost?” That’s where")
fx('plain', 'dashes removed', '<li><strong>Conservation</strong> — using less', '<li><strong>Conservation</strong>: using less')
fx('plain', 'dashes removed', '<li><strong>Restoration</strong> — fixing damage', '<li><strong>Restoration</strong>: fixing damage')
fx('plain', 'dashes removed', '<li><strong>Better technology</strong> — finding a smarter way.', '<li><strong>Better technology</strong>: finding a smarter way.')
fx('plain', 'dashes removed; “no-mine zones” said plainly', "<li><strong>Rules and laws</strong> — protecting things people can't protect alone. (Florida's water-use limits, no-mine zones, the Endangered Species Act.)</li>",
   "<li><strong>Rules and laws</strong>: rules everyone must follow to protect things people can’t protect alone.</li>")
fx('plain', 'shorter; dash removed',
   "None of these solutions makes the environmental cost ZERO. But the right protection strategy can shift the balance enough that the tradeoff becomes worth it. That's the job of communities, scientists, and engineers — together.",
   "None of these makes the environmental cost ZERO. But the right protection strategy can tip the balance enough that the tradeoff is worth it.")
fx('plain', 'the diagram is Part 3 now', 'margin-top:22px;">Four Florida Tradeoffs</h3>', 'margin-top:22px;">Part 3 · Four Florida Tradeoffs</h3>')
fx('plain', 'the four tradeoffs are on the diagram in the Lesson',
   "Pick one of the four Florida tradeoffs from the diagram (gas cars, solar farms, phosphate mining, or irrigation farms).",
   "Pick one of the four Florida tradeoffs from Part 3 (gas cars, solar farms, phosphate mining, or irrigation farms).")
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')

fx('cut', 'lean: the Watch out box (one idea per paragraph; Part 3 and the CER cover it)',
   "<p><strong>Common misconception:</strong> Some people think every environmental problem has ONE right answer. Real-world choices usually have several reasonable options, each with different costs and benefits. Comparing them is part of the science.</p>", '')
fx('plain', 'shorter: the examples are in the Strategy toolbox right below', ' of a resource so it lasts longer. (Shorter showers, energy-saving light bulbs.)</li>', ' so it lasts longer.</li>')
fx('plain', 'shorter: the examples are in the Strategy toolbox', ' after a resource is used. (Replanting trees after logging, restoring a wetland after mining.)</li>', ' after a resource is used.</li>')
fx('plain', 'shorter: the examples are in the Strategy toolbox', 'finding a smarter way. (Solar panels instead of coal plants. Drip irrigation instead of flooding fields.)</li>', 'finding a smarter way.</li>')
fx('plain', 'shorter closing', r'<p><strong>Nicely done\.</strong> You can now break down a Florida resource decision into its three parts:.*?</p>',
   '<p><strong>Nicely done.</strong> You can now break a Florida resource choice into three parts: the benefit, the environmental cost and a protection strategy. Next time, you’ll think like an engineer and make a solution even better.</p>', True)
# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its tradeoff analysis becomes Part C; the electric-car fact and the Go Deeper go with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: Stop & Think asks what Load the scale already does (one thinking stop per tab is enough)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: the Key Concept box repeats Part 1', r'<div style="background:#FFF6E5;border:2.5px solid #F0C97A;[^"]*">\s*<div[^>]*>⭐ Key Concept</div>\s*<p[^>]*>.*?</p>\s*</div>\s*', '', True)
fx('cut', 'lean: Stop & Reason pointed at the image that was never made', r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: Observe & Reason, the Amazing Fact, the Florida connection and Go Deeper at the end of the Lesson; Part 4 = the old Explore; next button goes to Self-Check',
   r'<div class="socratic-q">\s*<span class="sq-icon">👀</span>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 4 · The Town Hall</h3>\n      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">Tonight Palmetto Springs holds its town hall about the quarry. Six neighbors handed in comment cards. Read each one like a scientist: is it a benefit, an environmental cost, or a protection strategy?</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 6 removed (Bethany kept 5 and 7)', r'<div class="pq">\s*<span class="pq-num"[^>]*>6</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: renumber Part B (7 → 6)', '<span class="pq-num" style="background:#D4772C;">7</span>', '<span class="pq-num" style="background:#D4772C;">6</span>')
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C typed on the page; the scale sketch is a bonus',
   "A balance-scale tradeoff diagram for one Florida resource, with at least 2 benefits on the left, 2 environmental costs on the right, and 1 protection strategy below.",
   "One Florida resource use with 2 benefits, 2 environmental costs and 1 protection strategy. (A balance-scale sketch is a bonus.)")
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether Florida should always choose the option best for the environment, and supported it with two pieces of evidence.',
   '<strong>Use Your Evidence:</strong> My claim about whether Florida should always pick what’s best for the environment, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', True)

# ---------------------------------------------------------------- photos and credits
I = lambda n: 'images/16-01-' + n + '.jpg'
STILLS_CREDIT = ('Rock pits beside the Everglades, Miami-Dade County: U.S. Geological Survey, The National Map orthoimagery (public domain). '
                 'Limestone wall in the Brooksville quarry (Suwannee Limestone): RealGatba, CC BY-SA 4.0, via Wikimedia Commons. '
                 'Sawgrass on limestone, Everglades National Park: Moni3, public domain, via Wikimedia Commons. '
                 'Palmetto Springs is a made-up town; the photos show real places in Florida like it.')
FACTS = ('Lake Belt rock pits: South Florida Water Management District, Lake Belt Committee (they supply about half of the limestone used in Florida each year; '
         'a fee on every ton of rock pays to restore wetlands). Florida mine reclamation: Florida Department of Environmental Protection.')

D = {
    'lesson': '16.01', 'week': 16, 'day': 1, 'guide': 'june', 'prefix': 'g4sci-16-1', 'manifestKey': '16-01',
    'paths': P['paths'], 'crew': R['crew'],
    'expedition': {'num': 16, 'title': 'The Quarry Vote'},
    'ambient': {'icon': '🐸', 'label': 'Wetland sounds'},
    'case': {
        'num': 16, 'title': 'The Quarry Vote', 'style': 'hall',
        'hook': 'Hi, I’m June Calloway, a geologist (a scientist who studies rocks and the land). A company wants to dig a rock quarry (a big pit where rock is dug out) at the edge of my town, Palmetto Springs. The town votes Thursday. Will you help me weigh it?',
        'notice': {'head': 'Public notice · Palmetto Springs Town Council', 'title': 'Should we say yes to a rock quarry?',
                   'rows': [['The plan', 'Dig limestone for 20 years to make road rock and building stone.'],
                            ['Where', 'West of town, beside Cypress Slough (a wetland where herons and wood storks feed), about a mile from the town wells.']],
                   'line': ''},
        'stills': [
            {'cam': 'From the air', 'time': 'Rock pits beside the Everglades', 'tag': '📷 Real place', 'kind': 'print', 'img': I('lake-belt'),
             'alt': 'An aerial photo: flat brown-green sawgrass on the left, then big square lakes where rock was dug out, with white rock roads between them.'},
            {'cam': 'Inside a quarry', 'time': 'A wall of limestone', 'tag': '📷 Real place', 'kind': 'print', 'img': I('quarry-wall'),
             'alt': 'A tall pale yellow wall of limestone rock inside a Florida quarry, under a blue sky.'},
            {'cam': 'The wetland', 'time': 'Sawgrass growing on limestone', 'tag': '📷 Real place', 'kind': 'print', 'img': I('wetland'),
             'alt': 'Tall green sawgrass growing out of bumpy gray limestone rock in a wetland.'}],
        'stillsCredit': STILLS_CREDIT,
        'question': 'Should Palmetto Springs say yes to the quarry, and what would make it worth it?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'twocol', 'icon': '⚖️', 'where': 'Warm-Up: gained or used up?', 't': 'Every choice has two sides: something you gain and something you use up. The quarry is a choice, too.'},
            {'id': 'scale', 'icon': '🏗️', 'where': 'The Lesson, Part 1: load the scale', 't': 'The quarry’s benefits (road rock, jobs, building stone) and its costs (the wetland, the wells, noise and dust) both weigh a lot. Protection strategies made the costs smaller, but not zero.'},
            {'id': 'toolbox', 'icon': '🧰', 'where': 'The Lesson, Part 2: strategy toolbox', 't': 'There are four kinds of protection strategies: conservation, restoration, better technology, and rules. A quarry can use all four.'},
            {'id': 'townhall', 'icon': '🗳️', 'where': 'The Lesson, Part 4: the town hall', 't': 'Neighbors see different benefits and costs. Each big cost had a protection strategy to match: restore a wetland nearby, and keep the digging away from the wells.'},
        ],
        'solve': {
            'title': 'Should Palmetto Springs say yes?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Yes, no problem. A quarry has no environmental cost.', 'why': 'Check Clue 2. What went on the cost side of the scale?'},
                {'t': 'No. If a choice has any cost at all, the town should never make it.', 'why': 'Check Clue 1. Every choice has a cost. Is there a way to make this one smaller?'},
                {'t': 'Yes, but only with protection strategies. The town gains road rock and jobs, the wetland and wells pay a cost, and strategies like restoring a wetland and keeping away from the wells make that cost smaller.', 'right': True,
                 'why': 'Case cracked! You weighed the benefits against the costs and found ways to lower the costs. Now write your case report: it’s the questions below.'},
            ]},
    },
    'twocol': {
        'afterText': 'Every choice has two sides', 'kicker': 'Warm-Up game', 'title': 'Gained or used up?',
        'todo': ['Pick one, then drag each card to GAINED or USED UP (or tap a card, then a column).', 'Sort all three, then answer the question.'],
        'cols': [{'k': 'gain', 'icon': '👍', 't': 'GAINED'}, {'k': 'use', 'icon': '🔋', 't': 'USED UP'}],
        'items': [
            {'id': 'shower', 'icon': '🚿', 'name': 'A hot shower', 'chips': [
                {'id': 'clean', 't': 'A clean body', 'side': 'gain', 'miss': 'Being clean is something you get. Is that gained or used up?'},
                {'id': 'water', 't': 'Water', 'side': 'use', 'miss': 'Where does the water go after the shower? Down the drain. Is that gained or used up?'},
                {'id': 'heat', 't': 'Energy to heat the water', 'side': 'use', 'miss': 'A water heater burns gas or uses electricity. Is that gained or used up?'}]},
            {'id': 'toast', 'icon': '🍞', 'name': 'Toast for breakfast', 'chips': [
                {'id': 'food', 't': 'Energy from food for your body', 'side': 'gain', 'miss': 'Food gives your body energy. Do you get that or give it up?'},
                {'id': 'bread', 't': 'Bread made from wheat grown on a farm', 'side': 'use', 'miss': 'Once you eat the bread, it’s gone. Is that gained or used up?'},
                {'id': 'elec', 't': 'Electricity for the toaster', 'side': 'use', 'miss': 'The toaster runs on electricity from a power plant. Is that gained or used up?'}]},
            {'id': 'car', 'icon': '🚗', 'name': 'A car ride to school', 'chips': [
                {'id': 'fast', 't': 'Getting there fast', 'side': 'gain', 'miss': 'Getting there fast is a good thing you get. Gained or used up?'},
                {'id': 'gas', 't': 'Gasoline', 'side': 'use', 'miss': 'The engine burns gas, and then it’s gone. Gained or used up?'},
                {'id': 'air', 't': 'Some clean air (the car makes exhaust)', 'side': 'use', 'miss': 'Exhaust makes the air a little dirtier. Did the air gain or lose something?'}]}],
        'q': 'What did EVERY activity have?',
        'opts': [{'t': 'Only things we gained.', 'miss': 'Look at the USED UP column. Is it empty?'},
                 {'t': 'Something gained AND something used up.', 'ok': True},
                 {'t': 'Only things we used up.', 'miss': 'Look at the GAINED column. Is it empty?'}],
        'win': 'Every choice has two sides. The quarry is a choice too. That’s a clue.',
        'clue': 'twocol'},
    'scale': {
        'afterText': 'Scientists break a tradeoff into three parts', 'kicker': 'Part 1 game', 'title': 'Load the scale',
        'todo': ['Drag each card to a side of the scale (or tap a card, then a side). Heavy cards (●●●) count more.', 'Then add the protection strategies and watch the scale.'],
        'why': {'icon': '🏗️', 'q': 'What’s on the scale?', 't': 'The Palmetto Springs quarry. Real rock pits like it, beside the Everglades, supply about half of Florida’s limestone.'},
        'sides': {'benefit': {'icon': '👍', 't': 'Benefits'}, 'cost': {'icon': '🌫️', 't': 'Environmental costs'}},
        'weights': [
            {'id': 'roads', 'icon': '🛣️', 't': 'Rock to fix the town’s roads', 'side': 'benefit', 'w': 3, 'miss': 'Fixing roads is something the town GAINS. Which side is that?'},
            {'id': 'jobs', 'icon': '👷', 't': 'About 60 new jobs', 'side': 'benefit', 'w': 2, 'miss': 'Jobs are something people GAIN. Which side is that?'},
            {'id': 'stone', 'icon': '🏠', 't': 'Stone for building new homes', 'side': 'benefit', 'w': 2, 'miss': 'Building stone is something people GAIN. Which side is that?'},
            {'id': 'wetland', 'icon': '🪶', 't': 'Part of the wetland dug away for good', 'side': 'cost', 'w': 3, 'miss': 'The herons and wood storks LOSE their feeding place. Which side is that?'},
            {'id': 'wells', 'icon': '🚰', 't': 'A risk to the water in the town wells', 'side': 'cost', 'w': 3, 'miss': 'Dirty well water would be a LOSS for the town. Which side is that?'},
            {'id': 'dust', 'icon': '🚚', 't': 'Noise and dust from big trucks', 'side': 'cost', 'w': 1, 'miss': 'Noise and dust make the air worse. Which side is that?'}],
        'strategies': [
            {'id': 'restore', 'icon': '🌱', 't': 'The company pays to restore a wetland nearby', 'lowers': 'wetland', 'to': 1,
             'why': 'Restoration: a fee on every ton of rock pays to bring back wetland somewhere close. Real Florida rock pits pay a fee like this. The wetland here is still gone, so the cost is smaller, but not zero.'},
            {'id': 'wells', 'icon': '📏', 't': 'A rule: no digging near the town wells', 'lowers': 'wells', 'to': 1,
             'why': 'A rule and law: keeping the pit far from the wells lowers the risk to drinking water. It doesn’t remove every risk.'}],
        'q': 'The strategies tipped the scale. Is the environmental cost zero now?',
        'opts': [{'t': 'Yes. The wetland is fine now.', 'miss': 'Look at the cost side. Is it empty?'},
                 {'t': 'No. The costs are smaller, but some of the wetland is still gone.', 'ok': True},
                 {'t': 'The benefits got bigger instead.', 'miss': 'Look at which side changed when you added the strategies.'}],
        'credit': FACTS,
        'win': 'Benefits on one side, costs on the other. Protection strategies made the costs smaller, but not zero. That’s a clue.',
        'clue': 'scale'},
    'toolbox': {
        'afterText': 'That’s where', 'kicker': 'Part 2 game', 'title': 'Strategy toolbox',
        'todo': ['Drag each card into its drawer (or tap a card, then a drawer).', 'Round 2 is the quarry. Then answer the question.'],
        'kinds': [{'k': 'conserve', 'icon': '💧', 't': 'Conservation', 'sub': 'use less so it lasts'},
                  {'k': 'restore', 'icon': '🌱', 't': 'Restoration', 'sub': 'fix damage afterward'},
                  {'k': 'tech', 'icon': '⚙️', 't': 'Better technology', 'sub': 'a smarter way'},
                  {'k': 'rules', 'icon': '📜', 't': 'Rules and laws', 'sub': 'everyone must follow'}],
        'rounds': [
            {'title': 'Strategies people use in Florida', 'cards': [
                {'id': 'brush', 'icon': '🪥', 't': 'Turn off the faucet while you brush your teeth', 'k': 'conserve', 'why': 'You use less water, so more stays in the aquifer (the water stored in the rock underground).', 'miss': 'This uses less of something. Which drawer is about using less?'},
                {'id': 'park', 'icon': '🏞️', 't': 'Plant trees and wetland plants around an old mine pit', 'k': 'restore', 'why': 'Florida law says land mined for phosphate since 1975 must be fixed up afterward. Some old pits are parks now.', 'miss': 'This fixes the land after the digging is done. Which drawer is that?'},
                {'id': 'solar', 'icon': '☀️', 't': 'Use solar panels instead of a coal power plant', 'k': 'tech', 'why': 'Solar panels make electricity without smoke. It’s a smarter way to do the same job.', 'miss': 'This is a new, smarter machine for the same job. Which drawer is that?'},
                {'id': 'limit', 'icon': '🚿', 't': 'A law that limits which days people may water their lawns', 'k': 'rules', 'why': 'Many Florida towns let people water lawns only on certain days. Everyone has to follow it.', 'miss': 'Everyone has to follow this. Which drawer is that?'}]},
            {'title': 'Strategies for the Palmetto Springs quarry', 'cards': [
                {'id': 'recycle', 'icon': '♻️', 't': 'Crush old concrete into road rock, so less new rock is dug', 'k': 'conserve', 'why': 'Reusing old concrete means the quarry digs less new limestone, so it lasts longer.', 'miss': 'This means less new rock gets dug. Which drawer is about using less?'},
                {'id': 'lake', 'icon': '🦢', 't': 'Shape finished pits into lakes with plants for birds', 'k': 'restore', 'why': 'After digging stops, the pit is reshaped and planted so wildlife can come back.', 'miss': 'This happens after the digging is finished. Which drawer is that?'},
                {'id': 'spray', 'icon': '💦', 't': 'Trucks that spray water to keep dust down', 'k': 'tech', 'why': 'A spray system is a machine that makes the job cleaner.', 'miss': 'This is a machine that does the job better. Which drawer is that?'},
                {'id': 'mile', 'icon': '📏', 't': 'No digging within a mile of the town wells', 'k': 'rules', 'why': 'A rule protects drinking water that the whole town shares.', 'miss': 'The company has to follow this. Which drawer is that?'}]}],
        'q': 'Which kind of strategy fixes damage AFTER the resource is used?',
        'opts': [{'t': 'Conservation', 'miss': 'Conservation means using less. Which one fixes things afterward?'},
                 {'t': 'Restoration', 'ok': True},
                 {'t': 'Rules and laws', 'miss': 'Rules stop problems before they start. Which one fixes damage afterward?'}],
        'win': 'Four kinds of protection strategies, and the quarry can use all of them. That’s a clue.',
        'clue': 'toolbox'},
    'photos': [{
        'id': 'oldquarry', 'afterText': 'None of these makes the environmental cost ZERO', 'kicker': 'Look closer · an old Florida quarry', 'short': 'quarry photo',
        'title': 'What happens to a quarry after the digging?',
        'todo': ['Tap each number on the photo to read what it is.', 'Then match the clues to the labels below.'],
        'why': {'icon': '📸', 'q': 'Where is this?', 't': 'An old limestone quarry on Key Largo, in the Florida Keys. No one digs here now.'},
        'img': I('old-quarry'), 'alt': 'A dark pool of water in an old quarry. Behind it is a low wall of gray rock, with trees and bushes growing along the top under a blue sky.',
        'credit': 'Quarry, Key Largo, Florida, YourWorldExplorer, via Wikimedia Commons (from Panoramio)', 'license': 'CC BY 3.0',
        'hotspots': [
            {'n': 1, 'x': 45, 'y': 63, 'label': 'The gray rock wall', 't': 'Limestone made from an old coral reef. This is the rock that was cut out of the ground here.'},
            {'n': 2, 'x': 40, 'y': 86, 'label': 'The dark water', 't': 'Florida’s underground water is close to the surface. When a pit is dug deep enough, water seeps in from the rock and fills it.'},
            {'n': 3, 'x': 55, 'y': 40, 'label': 'The trees', 't': 'Trees and bushes grow right up to the edge. Plants can move back after the digging stops, but it takes many years.'},
            {'n': 4, 'x': 72, 'y': 53, 'label': 'The flat top of the wall', 't': 'This was the ground level before the digging. Everything below it, down past the water, was dug away.'}],
        'task': {'q': 'Match each clue to a label on the photo.', 'win': 'You read the quarry like a geologist. The rock is gone for good, but nature is slowly moving back in. That’s why the cost is never zero.',
                 'items': [{'icon': '🪨', 'step': 'The kind of rock that was dug out', 'ans': 1, 'evid': 'The rock wall is limestone that was cut out of the ground.'},
                           {'icon': '💧', 'step': 'What filled the pit from below', 'ans': 2, 'evid': 'Underground water seeped in and filled the pit.'},
                           {'icon': '🌳', 'step': 'Nature moving back in', 'ans': 3, 'evid': 'Trees and bushes are growing back around the pit.'},
                           {'icon': '📏', 'step': 'Where the ground used to be', 'ans': 4, 'evid': 'The top of the wall shows where the ground was before.'}]}}],
    'townhall': {
        'afterText': 'Six neighbors handed in comment cards', 'kicker': 'Part 4 game', 'title': 'The town hall',
        'todo': ['Stamp each comment card: Benefit, Cost or Strategy.', 'Then match each strategy to the cost it lowers, and answer the question.'],
        'why': {'icon': '🗳️', 'q': 'What is a town hall?', 't': 'A meeting where neighbors share ideas before leaders vote. Listening to everyone helps a town see the whole tradeoff.'},
        'tags': [{'k': 'benefit', 'icon': '👍', 't': 'Benefit'}, {'k': 'cost', 'icon': '🌫️', 't': 'Cost'}, {'k': 'strategy', 'icon': '🛡️', 't': 'Strategy'}],
        'comments': [
            {'id': 'diaz', 'who': 'Ms. Diaz, road crew', 'icon': '🛣️', 't': 'Our roads are full of potholes. Rock from close by means faster, cheaper repairs.', 'tag': 'benefit', 'miss': 'Fixing roads is something the town gains. Which stamp fits?'},
            {'id': 'okafor', 'who': 'Mr. Okafor, birdwatcher', 'icon': '🪶', 't': 'Wood storks and herons feed in Cypress Slough. Once it’s dug out, that part is gone.', 'tag': 'cost', 'miss': 'Losing the birds’ feeding place is a loss for the environment. Which stamp fits?'},
            {'id': 'lin', 'who': 'Ms. Lin, town water plant', 'icon': '🚰', 't': 'Our wells pull drinking water from the same limestone. A pit too close could let pollution in.', 'tag': 'cost', 'miss': 'Polluted drinking water would be a loss. Which stamp fits?'},
            {'id': 'jamal', 'who': 'Jamal, truck driver', 'icon': '🚚', 't': 'The quarry would hire about 60 people. I could get a job close to home!', 'tag': 'benefit', 'miss': 'A job is something people gain. Which stamp fits?'},
            {'id': 'june', 'who': 'June Calloway, geologist', 'icon': '🌱', 't': 'The company could pay to restore a wetland twice as big on land nearby.', 'short': 'Restore a bigger wetland nearby', 'tag': 'strategy', 'lowers': 'okafor',
             'miss': 'This idea lowers a cost. Which stamp fits?', 'matchMiss': 'A new wetland helps the birds. Whose card is about the birds?'},
            {'id': 'bell', 'who': 'Mayor Bell', 'icon': '📏', 't': 'We could make a rule: no digging within a mile of the town wells.', 'short': 'No digging near the wells', 'tag': 'strategy', 'lowers': 'lin',
             'miss': 'This rule lowers a cost. Which stamp fits?', 'matchMiss': 'This rule protects the wells. Whose card is about drinking water?'}],
        'matchQ': 'Now drag each strategy onto the cost it lowers (or tap it, then the cost).',
        'q': 'What did the town hall show?',
        'opts': [{'t': 'Everyone agrees, so there’s nothing to weigh.', 'miss': 'Look at the stamps. Did everyone talk about the same side?'},
                 {'t': 'Neighbors see different benefits and costs, and each big cost has a strategy that can lower it.', 'ok': True},
                 {'t': 'Only the benefits matter at a town hall.', 'miss': 'Look at the cost cards. Did the town hall ignore them?'}],
        'win': 'Every big cost has a protection strategy to match. That’s your last clue.',
        'clue': 'townhall'},
    'exploreMod': 'townhall',
    'tool': {
        'name': 'Water meter', 'icon': '🚰', 'tab': 'assignment', 'after': '#tab-assignment .activity-card', 'key': '16-tool', 'sim': 'watermeter',
        'kicker': 'Bonus · Tool of the Week',
        'teaser': 'Run a shower, a dripping faucet and a lawn sprinkler, and read how many gallons each one uses.',
        'done': 'You read the water meter like a pro. A water meter sticker is in your Field Notebook.',
        'why': {'icon': '🚰', 'q': 'What is a water meter?', 't': 'A counter on the pipe that brings water to a home. It adds up every gallon used, so families and towns can see where their water goes.'},
        'watermeter': {
            'title': 'Where does a home’s water go?',
            'todo': ['Tap each part of the meter to learn it.', 'Run all four ways of using water and watch the meter count.', 'Compare the bars, then answer the question.'],
            'perTurn': 10,
            'parts': [{'label': 'The counter', 't': 'The numbers add up every gallon that has gone through the pipe. They only go up.'},
                      {'label': 'The sweep hand', 'icon': '🔴', 't': 'The big red hand goes around once for every 10 gallons on many home meters, so you can see small amounts.'},
                      {'label': 'The leak triangle', 't': 'This little triangle spins whenever any water is flowing, even a tiny drip. If it spins when everything is off, there’s a leak.'}],
            'uses': [
                {'k': 'long', 'icon': '🚿', 'name': 'A 10-minute shower', 'gal': 25, 'note': 'A new shower head can use up to 2.5 gallons every minute, so 10 minutes is about 25 gallons.'},
                {'k': 'short', 'icon': '⏱️', 'name': 'A 5-minute shower', 'gal': 13, 'note': 'Half the time, about half the water (about 12 or 13 gallons). That’s conservation.'},
                {'k': 'drip', 'icon': '💧', 'name': 'A dripping faucet for a whole day', 'gal': 8, 'note': 'One drip every second adds up to about 8 gallons a day, and more than 3,000 gallons a year. Watch the leak triangle spin.'},
                {'k': 'lawn', 'icon': '🌱', 'name': 'Watering the lawn once', 'gal': 1000, 'note': 'A typical Florida yard uses about 1,000 gallons or more each time the sprinklers run.'}],
            'q': {'q': 'Which change would save the MOST water in one week?', 'opts': [
                {'t': 'Taking 5-minute showers instead of 10-minute ones', 'why': 'That saves about 12 gallons a shower, or about 85 gallons in a week. Good, but look at the longest bar.'},
                {'t': 'Fixing the dripping faucet', 'why': 'That saves about 8 gallons a day, or about 56 in a week. Good, but look at the longest bar.'},
                {'t': 'Watering the lawn one less time each week', 'ok': True, 'why': 'Right! Skipping one watering saves about 1,000 gallons, more than all the others together. That’s why Florida towns limit which days people may water lawns.'}]}}},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Those words are from last week. Which three parts did the scale have?', 'B': 'Those are map words from 15.02. Which three parts did the scale have?'},
        'q2': {'B': 'Drip irrigation saves water. Does that lower a cost or add one?', 'C': 'A benefit is what we gain. What is drip irrigation doing to the cost?'},
        'q3': {'A': 'Coal makes smoke. Solar farms cover land. Are those the same cost?', 'C': 'Think about Load the scale. Was any cost ever zero?'}},
    'flags': {
        'ans-1': [
            {'label': 'the benefit', 're': 'benefit|gain|job|energy|electric|food|fast|travel|money|fertiliz|grow'},
            {'label': 'the environmental cost', 're': 'cost|pollut|lose|habitat|land|air|water|dirty|smoke|exhaust|oil|spill|aquifer|runoff'},
            {'label': 'a protection strategy', 're': 'strateg|protect|restor|conserv|rule|law|limit|drip|electric car|rooftop|recycl|replant|less|bik|bus|transit|buffer'}],
        'ans-3': [
            {'label': 'why they matter', 're': 'lower|less|smaller|reduce|protect|help|save|keep|shift|balance|tip'},
            {'label': 'a Florida example', 're': 'restor|reclaim|park|pit|wetland|drip|water.use|water use|limit|law|rule|solar|recycl|lawn|well|mine|quarry|conserv'},
            {'label': 'how it lowers the cost', 're': 'because|so |which|that way|this means|by '}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|should|shouldn'},
            {'label': 'two pieces of evidence', 'any': ['benefit', 'cost', 'road', 'job', 'wetland', 'well', 'water', 'strateg', 'restor', 'rule', 'law', 'scale', 'balance', 'quarry', 'rock', 'zero', 'tradeoff', 'trade'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-1': 20, 'ans-3': 15, 'cer-4': 30},
    'hints': {
        'ans-1': ['Pick the one you understand best: gas cars, solar farms, phosphate mining or irrigation farms.', 'Write three sentences: what people gain, what the environment loses, what lowers the cost.', 'Try: The benefit of ___ is ___. The environmental cost is ___. One protection strategy is ___.'],
        'ans-3': ['What happened to the cost side of the scale when you added a strategy?', 'Think of a Florida example from the toolbox.', 'Try: Protection strategies matter because ___. For example, ___ lowers the cost by ___.'],
        'cer-4': ['First decide: should Florida ALWAYS pick what’s best for the environment, no matter what?', 'Think about the roads and the wetland in Palmetto Springs.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'Every choice has two sides: something gained and something used up.',
                'The quarry gives the town road rock and jobs, but it costs part of the wetland.',
                'Protection strategies made the costs smaller, but never zero.',
                'Restoring a wetland nearby and keeping away from the wells lowered the biggest costs.',
]}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · the quarry vote', 'length': '30–40 s',
                    'script': 'Hi! I’m June Calloway, and I’m a geologist. That means I study rocks and the land. I work in Palmetto Springs, a little Florida town. A company wants to dig a rock quarry right next to our wetland. The quarry would bring road rock and jobs. But what would we lose? The town votes on Thursday. Help me weigh it.'},
        'warmup': {'label': 'Warm-Up · gained or used up? (Clue 1)', 'length': '20–30 s',
                   'script': 'Let’s start small. Pick something you might do in the morning, like a shower or a car ride. Then sort each card. Is it something you gained, or something you used up? Sort all three. Then write about something you really did today.'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Act out “tradeoff” by trading a pencil for an eraser; hold out two hands like a scale for “benefit” and “environmental cost”.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · load the scale (Clue 2)', 'length': '25–35 s',
                  'script': 'Here’s our quarry on a balance scale. Drag each card to the benefit side or the cost side. Heavy cards count more, so watch the scale tip. When every card is on, add the protection strategies. What happens to the cost side? Does it ever reach zero?'},
        'part2': {'label': 'Part 2 · strategy toolbox (Clue 3)', 'length': '20–30 s',
                  'script': 'A good town needs a whole toolbox of strategies. Drop each card into its drawer: using less, fixing damage afterward, a smarter machine, or a rule everyone follows. Round two is our quarry. After that, I’ll show you a real old quarry in the Florida Keys.'},
        'explore': {'label': 'Part 4 · the town hall (Clue 4)', 'length': '25–35 s',
                    'script': 'Welcome to the town hall! Six neighbors brought comment cards. Read each one and stamp it: a benefit, a cost, or a protection strategy. Then match each strategy to the cost it lowers. Listen to everyone. That’s how a town sees the whole tradeoff.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s',
                       'script': 'Do you have all four clues? Crack the case at the top of this tab: should Palmetto Springs say yes to the quarry, and what would make it worth it? Then answer two questions, weigh one Florida tradeoff in Part C, and write your CER. Your answers save as you type.'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · weigh one tradeoff', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says Florida should always pick what’s best for the environment, no matter what. Hmm. Think about the roads and the wetland in Palmetto Springs. Pick your side, tap two pieces of evidence in the planner, then explain how they prove your claim.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 16.02 (compare several solutions and improve one, like an engineer).',
                    'script': 'Case closed! You weighed the benefits and the costs, and you found strategies to make the costs smaller. That’s exactly what a good town does. Next time, we’ll think like engineers: compare a few different solutions, pick the best one, and make it even better.'},
    },
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Your GAINED and USED UP columns (Warm-Up)',
        'The scale after you added the strategies (The Lesson)',
        'The full toolbox (The Lesson)',
        'The answer that cracked the case (Assignment)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['My balance scale for one Florida tradeoff', 'The quarry beside the wetland', 'A strategy that lowers a cost'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 3,
                           'prompts': ['Draw a balance scale', 'Put 2 benefits on one side and 2 costs on the other', 'Label one protection strategy']}]},
    'hlCoach': copy.deepcopy(Q['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🗳️', 'name': 'Town hall comment card',
                 'line': 'You cracked Case 16, and a Palmetto Springs comment card goes in your Field Notebook. (A specimen is something a scientist collects to study.) Next time: comparing solutions like an engineer.'},
    'notebookTitle': R['notebookTitle'],
    'notebook': [dict(x) for x in R['notebook']],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You’ll use every one of them today.',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '.fs-game[data-mod="twocol"]'},
         'label': 'Warm-Up: one thing I did today, what I gained and what I used up', 'q': 'Warm-Up: Something I did this morning, what I gained, and what I used up',
         'title': 'Your turn: something you really did today',
         'fields': [{'t': 'What I did', 'icon': '☀️', 'ph': 'This morning I…'},
                    {'t': 'What I GAINED', 'icon': '👍', 'ph': 'I gained…', 'long': True},
                    {'t': 'What I USED UP', 'icon': '🔋', 'ph': 'I used up… (water, energy, food, gas, time)', 'long': True}]},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'hide-nw', 'type': 'hide', 'find': {'sel': '.act-warmup .socratic-q', 'text': 'Notice'}},
        {'id': 'hide-tip', 'type': 'hide', 'find': {'sel': '.act-warmup .callout', 'text': 'Today'}},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Weigh it like a scientist'},
         'label': 'Part C: Weigh one Florida tradeoff', 'q': 'Part C: One Florida resource use: two benefits, two environmental costs, and one protection strategy',
         'title': 'My tradeoff scale',
         'fields': [{'t': 'The resource use I picked', 'icon': '⚖️', 'ph': 'I picked…'},
                    {'t': 'Two benefits (what people gain)', 'icon': '👍', 'ph': 'One benefit is… Another is…', 'long': True},
                    {'t': 'Two environmental costs (what the environment loses)', 'icon': '🌫️', 'ph': 'One cost is… Another is…', 'long': True},
                    {'t': 'One protection strategy, and why it works', 'icon': '🛡️', 'ph': 'One protection strategy is ___. This strategy works because…', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Should Florida always pick what’s best for the environment, no matter what?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-1': 'Part B · Question 5', 'ans-3': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] == '16.01': n.update({'icon': '🗳️', 'name': 'Town hall comment card'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'The quarry gives the town road rock, but it costs part of the wetland.',
    'key': ['quarry', 'road', 'rock', 'costs', 'wetland'],
    'small': ['The', 'gives', 'the', 'but', 'it'],
    'model': 'A scientist might highlight “road rock”, “costs” and “wetland”. Those words tell the benefit and the cost. Small words like “the” and “but” don’t carry the idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me explain what we gain and what we lose when we use a resource?']
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
