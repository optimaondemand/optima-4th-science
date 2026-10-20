#!/usr/bin/env python3
"""Writes data.json and fixes.json for 15.01 (run from this folder)."""
import json, copy
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../14-02/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

# ---------------------------------------------------------------- ticked fixes (Bethany, 20 Oct 2026)
fx('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist asks for a renewable / nonrenewable comparison',
   '🎨 Part C &mdash; Build Your Own Food Chain', '⚖️ Part C &mdash; Compare Two Florida Resources')
fx('fix', 'copy-paste leftover: Part C task from 9.01 (typed on the page; the chart sketch is a bonus)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   "Pick one <strong>renewable</strong> and one <strong>nonrenewable</strong> Florida resource. For each one, tell one way people use it and one impact. Then tell which one changes the land, air or water less, and why.</p>", True)
fx('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'quarter label in the footer: week 15 is Quarter 2', 'Science &middot; Quarter 3 &middot;', 'Science &middot; Quarter 2 &middot;')
fx('fix', 'this is an Earth science lesson (4-ESS3-1), not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Earth Science</div>')
fx('fix', 'Florida makes almost no electricity from wind, so wind is not a Florida example; trees are named as the pine forests they are',
   r'<ul style="font-size:16px;color:#2B1D12;line-height:1.7;margin:10px 0 12px 24px;">\s*<li><strong>Renewable Florida examples:</strong>.*?</ul>',
   '<ul style="font-size:16px;color:#2B1D12;line-height:1.7;margin:10px 0 12px 24px;">\n        <li><strong>Renewable Florida examples:</strong> sunlight (for solar panels), fresh water from rain and springs, and pine forests that people replant. Wind is renewable too, but Florida makes almost no electricity from it.</li>\n        <li><strong>Nonrenewable Florida examples:</strong> phosphate rock (dug up to make fertilizer, which is plant food), oil and natural gas, and limestone (used for cement and roads).</li>\n      </ul>\n      <p>How fast is “fast”? Try it: use up five resources, then race time forward.</p>', True)
fx('fix', 'the AI-made chart named wind as a Florida resource and called coal “rare in FL” (Florida burns coal for some electricity but doesn’t mine it); the real-photo games replace it',
   r'<div class="lesson-figure scroll-reveal">.*?<div class="lesson-figure-caption">.*?</div>\s*</div>\s*', '', True)
fx('fix', 'shaky fact: Arizona, Nevada and other states get more sunny days than Florida (the tap diagram text is replaced by Impact check; fixed anyway)',
   'Florida gets more sunny days than almost any U.S. state.', 'Florida gets strong sunshine all year long.')

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; dash removed',
   "Hold this question in your head as you work. By the end of the lesson, you'll be able to tell the difference between resources we can use again and again — and resources that run out — using real Florida examples.",
   "Keep this question in mind. By the end, you’ll be able to tell resources that come back from resources that run out, using real Florida examples.")
fx('plain', 'answers are made on the page now (the game below, then three boxes)',
   r"<p>Look around the room\. Pick one thing.*?</p>\s*<p>Underneath, list at least three materials.*?</p>",
   "<p>Everything you use started somewhere on Earth. Some of it grew. Some came from the sky. Some was dug out of the ground. <strong>Take it apart</strong> in the game below: where did each part start?</p>", True)
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', 'dashes removed; shorter list',
   "is anything from Earth that people use to live and work. Water for drinking, sunlight for solar panels, wood for building, oil for fuel, sand for glass, copper for wires — all resources. Florida has a lot of them.</p>",
   "is anything from Earth that people use to live and work: water to drink, sunlight for solar panels, wood for houses, oil for gasoline. Florida has a lot of resources.</p>")
fx('plain', 'plain words', "resources take so long to form that once we use them, they're essentially gone.</p>",
   "resources take millions of years to form. Once we use them up, they’re gone for good.</p>")
fx('plain', 'dashes removed; Part 3 starts here; wind example dropped (not a Florida resource)',
   '<p>Every resource has an <span class="vtip">impact<span class="vtip-box"><span class="vtip-word">Impact</span>An effect, especially on the environment.</span></span> — a way it changes the environment when humans use it. Solar panels need land. Wind turbines can affect birds. Oil drilling can leak. Limestone mining changes the land. Even renewable resources have impacts — scientists work to keep them low.</p>',
   H3 + 'Part 3 · Every Resource Has an Impact</h3>\n      <p>Every resource has an <span class="vtip">impact<span class="vtip-box"><span class="vtip-word">Impact</span>An effect, especially on the environment.</span></span>: a way it changes the environment when people use it. Solar panels need land. Oil can spill. Mines dig up the land. Scientists work to keep impacts small.</p>')
fx('plain', 'plain label; shorter',
   "<p><strong>Common misconception:</strong> Some people think \"renewable\" means \"no impact.\" That's not quite right. Renewable resources come back, but using them still affects the environment. The real question is: <em>how big is the impact, and how can we reduce it?</em></p>",
   "<p><strong>Watch out:</strong> Renewable doesn’t mean “no impact.” A renewable resource comes back, but using it still changes things. The real question is: <em>how big is the impact, and how can we make it smaller?</em></p>")
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')

# ---------------------------------------------------------------- lean cuts (the shaky fact boxes go with them: the “1 million years per barrel” oil fact, the out-of-date “less than 5% solar” fact)
fx('cut', 'lean: the sources paragraph moves into Part 4 (Two sources, one claim)',
   r'\s*<p>Good scientists check at least <strong>two <span class="vtip">sources.*?</p>', '', True)
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean + shaky fact: remove the whole Explore tab (its comparison chart moves to Part 4 and Part C; the “less than 5% solar” fact goes with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: the Key Concept box repeats Part 2', r'<div style="background:#FFF6E5;border:2.5px solid #F0C97A;[^"]*">\s*<div[^>]*>⭐ Key Concept</div>\s*<p[^>]*>.*?</p>\s*</div>\s*', '', True)
fx('cut', 'lean: Stop & Reason pointed at the removed chart (Stop & Think in Part 1 stays)', r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: the old diagram heading and tap line go (Impact check replaces the tap diagram)',
   r'<h3[^>]*>Four Florida Resources</h3>\s*<p><strong>Tap a resource</strong>[^<]*</p>\s*', '', True)
fx('cut', 'lean + shaky facts: Observe & Reason, the “1 million years per barrel” oil fact, the Florida connection callout and Go Deeper at the end of the Lesson; Part 4 = the old Explore; next button goes to Self-Check',
   r'<div class="socratic-q">\s*<span class="sq-icon">👀</span>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 4 · Two Sources, One Claim</h3>\n      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">Scientists check at least two <span class="vtip">sources<span class="vtip-box"><span class="vtip-word">Source</span>Where information comes from.</span></span> before making a claim (saying what they think is true), because one source might leave something out. Dr. Reyes found two sources about the phosphate mines.</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 5 removed (Bethany kept 6 and 7; Part C covers one resource’s use and impact)', r'<div class="pq">\s*<span class="pq-num"[^>]*>5</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: renumber Part B (6 → 5)', '<span class="pq-num" style="background:#D4772C;">6</span>', '<span class="pq-num" style="background:#D4772C;">5</span>')
fx('cut', 'lean: renumber Part B (7 → 6)', '<span class="pq-num" style="background:#D4772C;">7</span>', '<span class="pq-num" style="background:#D4772C;">6</span>')
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C typed on the page; the chart sketch is a bonus',
   "A two-column comparison chart with one renewable and one nonrenewable Florida resource, including uses, environmental impact, and an open question for each.",
   "One renewable and one nonrenewable Florida resource: a use and an impact for each, and which one has the smaller impact. (A chart sketch is a bonus.)")
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether all renewables are good and all nonrenewables are bad, and supported it with two pieces of evidence.',
   '<strong>Use Your Evidence:</strong> My claim about whether all renewables are good and all nonrenewables are bad, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', True)

# ---------------------------------------------------------------- photo credits
CR = {
    'sat': 'Satellite photos (Landsat, 1985, 2004 and 2023) of the Bone Valley phosphate mining area southeast of Tampa Bay, from “Annual NLCD Assessment: Phosphate Mining and Land Cover Change”, U.S. Geological Survey EROS Center, 2024 (public domain)',
    'dragline': 'Surface strip mining with draglines near Parrish, Florida, U.S. Geological Survey EROS Center, about 2003 (public domain)',
    'gyp': 'A stack of phosphogypsum in Florida, U.S. Geological Survey EROS Center, about 2003 (public domain)',
    'solar': 'Discovery Solar Energy Center at NASA Kennedy Space Center, NASA, 2021, via Wikimedia Commons (public domain)',
    'pine': 'Longleaf pine forest, Osceola National Forest, Florida, Geoff Gallice, via Wikimedia Commons (CC BY 2.0)',
    'oil': 'Oil-stained beach in Pensacola, Florida, July 1, 2010, Geoff Livingston, via Wikimedia Commons (CC BY-SA 2.0)',
}
I = lambda n: 'images/15-01-' + n + '.jpg'

D = {
    'lesson': '15.01', 'week': 15, 'day': 1, 'guide': 'lena', 'prefix': 'g4sci-15-1', 'manifestKey': '15-01',
    'paths': P['paths'], 'crew': P['crew'],
    'expedition': {'num': 15, 'title': 'The Lakes That Weren’t There'},
    'ambient': {'icon': '🌲', 'label': 'Pine forest sounds'},
    'case': {
        'num': 15, 'title': 'The Lakes That Weren’t There', 'style': 'sat',
        'hook': 'A volunteer brought me three satellite photos of the same piece of central Florida, taken from space in 1985, 2004 and 2023. Dark, square lakes and bare tan patches keep showing up in new places. Lakes don’t usually come in squares! The volunteer wrote: “Lakes popping up out of nowhere?”',
        'question': 'What is making the square lakes and bare patches, and will the thing being taken ever come back?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'stills': [
            {'cam': '1985', 'time': '', 'tag': '🛰 LANDSAT', 'img': I('sat-1985'), 'alt': 'A satellite photo of green land with a cluster of small dark squares and tan patches near the middle.'},
            {'cam': '2004', 'time': '', 'tag': '🛰 LANDSAT', 'img': I('sat-2004'), 'alt': 'The same land in 2004. The dark squares and tan patches have spread out, mostly toward the south.'},
            {'cam': '2023', 'time': '', 'tag': '🛰 LANDSAT', 'img': I('sat-2023'), 'alt': 'The same land in 2023. New dark squares and tan patches are near the bottom and edges. Some old spots in the middle look greener.'}],
        'stillsCredit': CR['sat'] + '. Each photo is cropped from the USGS animation.',
        'clues': [
            {'id': 'unmake', 'icon': '🍊', 'where': 'Warm-Up: take it apart', 't': 'The fertilizer that helps Florida oranges grow starts as phosphate rock, dug out of the ground in central Florida.'},
            {'id': 'refill', 'icon': '⏳', 'where': 'The Lesson, Part 2: refill race', 't': 'Phosphate rock took millions of years to form. Once it’s dug up, it doesn’t come back, even in a million years. It’s nonrenewable.'},
            {'id': 'impact', 'icon': '⛏️', 'where': 'The Lesson, Part 3: impact check', 't': 'When a mine digs out phosphate, the deep pit fills with rain and groundwater and becomes a lake. The land can be replanted, but the rock is gone.'},
            {'id': 'twosources', 'icon': '📑', 'where': 'The Lesson, Part 4: two sources', 't': 'Both sources agree: phosphate becomes fertilizer for growing food. The government report adds what the flyer left out: mines clear wetlands and fields, and leave huge waste piles.'},
        ],
        'solve': {
            'title': 'What is making the square lakes?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Heavy rains flooded the fields. Rain comes back, so nothing is lost.', 'why': 'Check Clue 3. Rain fills the pits, but what dug the square holes in the first place?'},
                {'t': 'People are mining phosphate rock for fertilizer. The dug pits fill with water and become lakes. Phosphate takes millions of years to form, so it’s nonrenewable and won’t come back.', 'right': True,
                 'why': 'Case cracked! The square lakes are old phosphate mine pits. Now write your case report: it’s the questions below.'},
                {'t': 'People are building solar farms, and sunlight is renewable.', 'why': 'Check Clues 1 and 4. What do the sources say comes out of the ground there?'},
            ]},
    },
    'unmake': {
        'afterText': 'where did each part start?', 'kicker': 'Warm-Up game', 'title': 'Take it apart',
        'todo': ['Pick a thing: the pencil, the juice box or the orange.', 'Drag each of its parts to where it started on Earth, or tap the part and then the place.', 'Take apart all three things, then answer the question.'],
        'why': {'icon': '🌎', 'q': 'What is a resource?', 't': 'Anything from Earth that people use, like water, sunlight, wood or rock.'},
        'hint': 'Sort a part to learn more about it here.',
        'sources': [{'k': 'grew', 'icon': '🌳', 't': 'It grew', 'sub': 'plants and trees'},
                    {'k': 'sky', 'icon': '☀️', 't': 'Sun, rain or wind', 'sub': 'from the sky'},
                    {'k': 'dug', 'icon': '⛏️', 't': 'Dug from the ground', 'sub': 'rock and metal'},
                    {'k': 'oil', 'icon': '🛢️', 't': 'Pumped from deep underground', 'sub': 'oil and natural gas'}],
        'items': [
            {'id': 'pencil', 'icon': '✏️', 'name': 'Pencil', 'parts': [
                {'id': 'p-wood', 'icon': '🪵', 't': 'Wood', 'src': 'grew', 'why': 'Most pencils are made of cedar wood. Trees can be cut and replanted.', 'miss': 'Wood comes from something that grows. What is it?'},
                {'id': 'p-lead', 'icon': '✏️', 't': 'The “lead” inside', 'src': 'dug', 'why': 'It isn’t really lead! It’s graphite, a soft gray rock, mixed with clay. Both are dug out of the ground.', 'miss': 'Pencil “lead” is a soft gray rock. Where do rocks come from?'},
                {'id': 'p-band', 'icon': '🔩', 't': 'Metal band', 'src': 'dug', 'why': 'The band that holds the eraser is aluminum. It’s made from a rock that miners dig up.', 'miss': 'Metal starts as rock. Where do people get rock?'}]},
            {'id': 'juice', 'icon': '🧃', 'name': 'Juice box', 'parts': [
                {'id': 'j-box', 'icon': '📦', 't': 'Paper box', 'src': 'grew', 'why': 'Paper is made from wood fibers, from trees.', 'miss': 'Paper is made from wood. Where does wood come from?'},
                {'id': 'j-straw', 'icon': '🥤', 't': 'Plastic straw', 'src': 'oil', 'why': 'Most plastic is made from oil or natural gas, pumped from deep underground.', 'miss': 'Plastic is made from something pumped out of the ground. What is it?'},
                {'id': 'j-foil', 'icon': '🥫', 't': 'Thin metal lining', 'src': 'dug', 'why': 'A thin layer of aluminum keeps the juice fresh. Aluminum starts as a rock that is mined.', 'miss': 'Metal starts as rock. Where do people get rock?'},
                {'id': 'j-juice', 'icon': '🍊', 't': 'Orange juice', 'src': 'grew', 'why': 'The juice comes from oranges, which grow on trees.', 'miss': 'Juice comes from fruit. Where does fruit come from?'}]},
            {'id': 'orange', 'icon': '🍊', 'name': 'Florida orange', 'sub': 'What it took to grow it and get it to you:', 'parts': [
                {'id': 'o-fruit', 'icon': '🍊', 't': 'The orange itself', 'src': 'grew', 'why': 'It grew on a tree in a Florida grove.', 'miss': 'Where do oranges come from?'},
                {'id': 'o-rain', 'icon': '🌧️', 't': 'Rain that watered the tree', 'src': 'sky', 'why': 'Rain falls again and again. Florida gets about 50 inches a year.', 'miss': 'Where does rain come from?'},
                {'id': 'o-sun', 'icon': '☀️', 't': 'Sunlight the leaves used', 'src': 'sky', 'why': 'Leaves use sunlight to make food for the tree. The sun rises again every day.', 'miss': 'Look up! Where does sunlight come from?'},
                {'id': 'o-fert', 'icon': '🧪', 't': 'Fertilizer for the tree', 'src': 'dug', 'why': 'Fertilizer is plant food. Much of it is made from phosphate rock, dug out of the ground in central Florida.', 'miss': 'Fertilizer is made from a kind of rock. Where does rock come from?'},
                {'id': 'o-fuel', 'icon': '🚚', 't': 'Fuel for the truck to the store', 'src': 'oil', 'why': 'Diesel fuel is made from oil, pumped from deep underground.', 'miss': 'Truck fuel is made from oil. Where does oil come from?'}]}],
        'q': 'Which part of the orange came out of the ground, like the pencil’s “lead”?',
        'opts': [{'t': 'The fertilizer', 'ok': True},
                 {'t': 'The rain', 'miss': 'Rain falls from the sky. Which part was dug up?'},
                 {'t': 'The orange itself', 'miss': 'The orange grew on a tree. Which part was dug up?'}],
        'win': 'You took everything apart! Some parts grew, some came from the sky, and some were dug up or pumped out of the ground. That’s a clue.',
        'clue': 'unmake'},
    'refill': {
        'afterText': 'How fast is “fast”?', 'kicker': 'Part 2 game', 'title': 'Refill race',
        'todo': ['Press “Use them all up”, then drag time forward. Which bars fill back up?', 'Try the water at both pumping speeds.', 'Stamp each one renewable or nonrenewable.'],
        'useBtn': '⚡ Use them all up',
        'stops': ['1 day', '1 year', '25 years', '100 years', '1 million years'],
        'rows': [
            {'id': 'sun', 'icon': '☀️', 'name': 'Sunlight', 'levels': [100, 100, 100, 100, 100], 'kind': 're', 'why': 'The sun rises again every morning.', 'miss': 'Look at the sunlight bar after just 1 day. Did it come back?'},
            {'id': 'water', 'icon': '💧', 'name': 'Fresh water underground', 'levels': [40, 100, 100, 100, 100], 'fast': [30, 20, 10, 0, 0], 'kind': 're',
             'why': 'Rain refills it every year, as long as we don’t pump faster than the rain soaks back in.', 'miss': 'At the slow pumping speed, did the water come back?'},
            {'id': 'pine', 'icon': '🌲', 'name': 'Pine forest', 'levels': [0, 5, 100, 100, 100], 'kind': 're', 'why': 'New pines grow back in about 25 years, when people replant them.', 'miss': 'Look at the pine bar at 25 years. Did the forest come back?'},
            {'id': 'phos', 'icon': '🪨', 'name': 'Phosphate rock', 'levels': [0, 0, 0, 0, 0], 'kind': 'non', 'why': 'It took millions of years to form. Even after a million years, it isn’t back.', 'miss': 'Look at the phosphate bar at 1 million years. Did it come back?'},
            {'id': 'oil', 'icon': '🛢️', 'name': 'Oil', 'levels': [0, 0, 0, 0, 0], 'kind': 'non', 'why': 'Oil formed from tiny sea creatures buried for millions of years.', 'miss': 'Look at the oil bar at 1 million years. Did it come back?'}],
        'pump': {'id': 'water', 'label': 'Pumping:', 'slow': '🐢 Slow', 'fast': '🐇 Fast',
                 'note': {'slow': 'Pumping slower than the rain soaks back in: the water fills back up.', 'fast': 'Pumping faster than the rain soaks back in: the water keeps dropping, even though it’s renewable!'}},
        'stampQ': 'Stamp each one: renewable or nonrenewable?',
        'stamps': [{'k': 're', 'icon': '♻️', 't': 'Renewable'}, {'k': 'non', 'icon': '⛔', 't': 'Nonrenewable'}],
        'q': 'Dr. Reyes’s satellite photos show land being dug up for phosphate rock. Will the rock come back?',
        'opts': [{'t': 'Yes, in about a year, like rain.', 'miss': 'Look at the phosphate bar at 1 year. Is it full?'},
                 {'t': 'Yes, in about 25 years, like a pine forest.', 'miss': 'Look at the phosphate bar at 25 years. Is it full?'},
                 {'t': 'No. It takes millions of years to form, so it’s nonrenewable.', 'ok': True}],
        'win': 'Sunlight, water and pine forests came back. Phosphate rock and oil didn’t, not even in a million years. That’s a clue.',
        'clue': 'refill'},
    'photos': [{
        'id': 'dragline', 'after': 'refill', 'kicker': 'Look closer · a real Florida phosphate mine', 'short': 'dragline photo',
        'title': 'How does phosphate come out of the ground?',
        'todo': ['Tap each number on the photo to read what it is.', 'Then match the steps to the labels below.'],
        'why': {'icon': '📸', 'q': 'What is a dragline?', 't': 'A giant digging machine. Government scientists photographed this one at a Florida phosphate mine.'},
        'img': I('dragline'), 'alt': 'A giant white mining machine with a long steel arm stands behind a farm field. A bucket hangs from cables near a pale pile of sand.',
        'credit': CR['dragline'].replace(' (public domain)', ''), 'license': 'Public domain',
        'hotspots': [
            {'n': 1, 'x': 15, 'y': 47, 'label': 'The dragline', 't': 'The giant machine. Its operator sits inside, and big motors pull the cables. It moves slowly on huge feet.'},
            {'n': 2, 'x': 40, 'y': 31, 'label': 'The boom', 't': 'A long steel arm that holds the bucket far out from the machine. On the biggest draglines, it’s about as long as a football field.'},
            {'n': 3, 'x': 48, 'y': 54, 'label': 'The bucket', 't': 'It hangs from cables. The dragline drops it, drags it to scoop up the ground, then lifts it and dumps it.'},
            {'n': 4, 'x': 63, 'y': 57, 'label': 'A pile of dug-up sand', 't': 'First the dragline scrapes off the sand on top and piles it out of the way. The phosphate layer is under it.'},
            {'n': 5, 'x': 35, 'y': 70, 'label': 'Land not mined yet', 't': 'A farm field. One dragline can dig up about 15 acres in a month, about the size of 11 football fields.'}],
        'task': {'q': 'Match each step of mining to a label on the photo.', 'win': 'You matched every step. The phosphate comes out, and the hole it leaves becomes a pit.',
                 'items': [{'icon': '🌾', 'step': 'The land before digging', 'ans': 5, 'evid': 'Before mining, the land was fields and wetlands.'},
                           {'icon': '🏗️', 'step': 'Holds the bucket far out', 'ans': 2, 'evid': 'The dragline’s long boom holds the bucket far from the machine.'},
                           {'icon': '🪣', 'step': 'Scoops up the ground', 'ans': 3, 'evid': 'The bucket scoops up the ground to reach the phosphate.'},
                           {'icon': '⛰️', 'step': 'Sand moved out of the way', 'ans': 4, 'evid': 'Sand on top is piled to the side to reach the phosphate under it.'}]}}],
    'impact': {
        'replace': '#tab-lesson .diagram-wrap', 'kicker': 'Part 3 game', 'title': 'Impact check',
        'todo': ['Pick a photo and stamp it renewable or nonrenewable.', 'Pick what using it changes. Check all four photos.'],
        'kinds': [{'k': 're', 'icon': '♻️', 't': 'Renewable'}, {'k': 'non', 'icon': '⛔', 't': 'Nonrenewable'}],
        'cards': [
            {'id': 'solar', 'name': 'Solar farm', 'img': I('solar-farm'), 'alt': 'Rows and rows of dark solar panels covering a huge flat area of land, seen from the air.', 'kind': 're',
             'kindMiss': 'Solar panels use sunlight. Does sunlight come back?',
             'use': 'Solar panels turn sunlight into electricity. This one at Kennedy Space Center is bigger than 350 football fields.',
             'q': 'What does using it change?',
             'opts': [{'t': 'It covers a lot of land, so plants and animals that lived there have to move.', 'ok': True},
                      {'t': 'It makes smoke every day.', 'miss': 'Solar panels make electricity without smoke. Look at the photo: what covers the ground?'},
                      {'t': 'Nothing changes, because it’s renewable.', 'miss': 'Renewable means it comes back, not that nothing changes. Look at the land in the photo.'}],
             'fact': 'Solar panels make electricity with no smoke. But they need lots of land, and making them uses metals that are dug from the ground.'},
            {'id': 'pine', 'name': 'Pine forest', 'img': I('pine-forest'), 'alt': 'Tall, straight pine trees with short palm-like plants covering the ground under them.', 'kind': 're',
             'kindMiss': 'Can people plant new pine trees? Do they grow back?',
             'use': 'People cut pines for wood and paper, then plant new ones. New pines grow back in about 25 years.',
             'q': 'What does cutting the forest change?',
             'opts': [{'t': 'Animals lose their homes until the new trees grow.', 'ok': True},
                      {'t': 'The trees can never grow back.', 'miss': 'Pines can be replanted. How long did they take in the Refill race?'},
                      {'t': 'Nothing changes, because it’s renewable.', 'miss': 'Think about the animals that live in the forest. What happens to them?'}],
             'fact': 'Woodpeckers, gopher tortoises and other animals need pine forests. Foresters plant new trees and often leave some old trees standing for them.'},
            {'id': 'oil', 'name': 'Oil', 'img': I('oil-beach'), 'alt': 'A Florida beach with brown streaks of oil washed up on the white sand.', 'kind': 'non',
             'kindMiss': 'Oil took millions of years to form. Does it come back?',
             'use': 'Oil is made into gasoline and plastic. In 2010, oil from a broken well in the Gulf washed up on Pensacola Beach.',
             'q': 'What does using it change?',
             'opts': [{'t': 'Burning it pollutes the air, and spills hurt beaches and wildlife.', 'ok': True},
                      {'t': 'It grows back in a year.', 'miss': 'Look at the oil bar in the Refill race. Did it come back?'},
                      {'t': 'Nothing changes.', 'miss': 'Look at the sand in the photo. What is on it?'}],
             'fact': 'Oil formed from tiny sea creatures that were buried for millions of years. Burning it for gasoline puts smoke and gases into the air.'},
            {'id': 'mine', 'name': 'Phosphate mine', 'img': I('sat-2023'), 'alt': 'The 2023 satellite photo: green land with dark square lakes and bare tan patches.', 'kind': 'non',
             'kindMiss': 'Phosphate rock took millions of years to form. Does it come back?',
             'use': 'Draglines dig up phosphate rock to make fertilizer. This is the 2023 satellite photo from the case file.',
             'q': 'What does mining it change?',
             'opts': [{'t': 'The land is dug into deep pits, and the pits fill with water and become lakes.', 'ok': True},
                      {'t': 'It fills the air with smoke, like burning oil.', 'miss': 'Look at the photo. What do you see on the land?'},
                      {'t': 'Nothing changes.', 'miss': 'Look at the dark squares in the photo. What are they?'}],
             'fact': 'Rain and groundwater fill the empty pits, making square lakes. Since 1975, Florida law has said mined land must be fixed up afterward, with new plants and shaped lakes. But the phosphate rock is gone for good.'}],
        'q': 'A classmate says, “Renewable means no impact.” What did you find?',
        'opts': [{'t': 'All four changed something. Renewables still have impacts, but sunlight and trees come back.', 'ok': True},
                 {'t': 'Only the nonrenewable ones had an impact.', 'miss': 'Look back at the solar farm and the pine forest. Did they change anything?'},
                 {'t': 'None of them had an impact.', 'miss': 'Look at the oil on the beach and the pits in the land.'}],
        'credit': 'Solar farm: ' + CR['solar'] + '. Pine forest: ' + CR['pine'] + '. Oil: ' + CR['oil'] + '. Mine: ' + CR['sat'] + '.',
        'win': 'Every resource has an impact, even renewable ones. The square lakes in the case are mine pits filled with water. That’s a clue.',
        'clue': 'impact'},
    'twosources': {
        'afterText': 'Dr. Reyes found two sources about the phosphate mines', 'kicker': 'Part 4 game', 'title': 'Two sources, one claim',
        'todo': ['Drag each fact to Benefit or Cost, or tap the fact and then the box.', 'Answer three questions to build a fair claim.'],
        'sources': [
            {'k': 'a', 'tag': 'Source A', 't': 'Phosphate: Feeding the World!', 'by': 'A flyer from a mining company (a pretend company for this case)',
             'facts': [{'id': 'a1', 't': 'Florida phosphate helps make fertilizer that farmers use to grow food.', 'side': 'ben'},
                       {'id': 'a2', 't': 'Mining gives jobs to many people in central Florida.', 'side': 'ben'},
                       {'id': 'a3', 't': 'When we finish digging, we replant the land and shape lakes and fields.', 'side': 'ben', 'miss': 'Fixing up the land helps. Is that a benefit or a cost?'}]},
            {'k': 'b', 'tag': 'Source B', 't': 'Phosphate Mining and Land Cover Change', 'by': 'A report by the U.S. Geological Survey (USGS), a team of government scientists, 2024',
             'img': I('gypstack'), 'alt': 'A huge pale gray hill of waste with a bulldozer and a digger parked on top.',
             'facts': [{'id': 'b1', 't': 'Mines clear away wetlands, grassland and pasture to dig the phosphate.', 'side': 'cost'},
                       {'id': 'b2', 't': 'Making fertilizer leaves giant waste piles, like the one in the photo. Florida has about 1 billion tons of this waste.', 'side': 'cost'},
                       {'id': 'b3', 't': 'About 95 out of every 100 tons of U.S. phosphate rock is used for fertilizer and animal food.', 'side': 'ben', 'miss': 'Fertilizer grows food for people. Is that a benefit or a cost?'}]}],
        'bins': [{'k': 'ben', 'icon': '👍', 't': 'Benefit: it helps people'}, {'k': 'cost', 'icon': '👎', 't': 'Cost: it harms land, water or wildlife'}],
        'steps': [
            {'q': 'Which fact is ONLY in Source B?', 'opts': [
                {'t': 'Mines clear away wetlands, grassland and pasture.', 'ok': True},
                {'t': 'Phosphate is used to make fertilizer.', 'miss': 'Both sources say that one. Which fact did the flyer leave out?'},
                {'t': 'Mining gives jobs.', 'miss': 'That’s in the flyer, Source A.'}]},
            {'q': 'What do BOTH sources agree on?', 'opts': [
                {'t': 'Phosphate rock is used to make fertilizer that grows food.', 'ok': True},
                {'t': 'Mining doesn’t change the land.', 'miss': 'Does Source B say that? Look at its facts.'},
                {'t': 'Florida has giant waste piles.', 'miss': 'Only Source B says that.'}]},
            {'q': 'Which claim is fair to BOTH sources?', 'opts': [
                {'t': 'Phosphate mining is all good.', 'miss': 'That only uses Source A. What did Source B add?'},
                {'t': 'Phosphate mining helps grow food, but it clears land and leaves waste, and the rock won’t come back.', 'ok': True},
                {'t': 'Phosphate mining is all bad.', 'miss': 'That only uses Source B. What benefit do both sources agree on?'}]}],
        'credit': 'Source A is a pretend flyer made for this case. Source B facts: ' + CR['gyp'].split(',')[0] + ' and the USGS EROS Center report “Annual NLCD Assessment: Phosphate Mining and Land Cover Change” (2024). Photo: ' + CR['gyp'] + '.',
        'win': 'You used two sources to make a fair claim! One source alone would have told only half the story. That’s your last clue.',
        'clue': 'twosources'},
    'exploreMod': 'twosources',
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Oil took millions of years to form. Is it back by tomorrow?', 'C': 'Limestone formed slowly under ancient seas. What comes back every day?'},
        'q2': {'A': 'Being hard to find isn’t the reason. Think about the Refill race: how long did they take?', 'B': 'Price isn’t the reason. Think about time.'},
        'q3': {'A': 'Think about the solar farm in Impact check. Did it change the land?', 'C': 'Solar panels make no smoke. Which has the bigger impact: solar or oil?'}},
    'flags': {
        'ans-2': [
            {'label': 'renewable = comes back', 're': 'renew'},
            {'label': 'nonrenewable = takes millions of years / runs out', 're': 'non.?renew|million|run(s)? out|ran out|used up|gone|forever|take.{0,15}long|(can.?t|cannot|doesn.?t|does not|won.?t|will not|never) come back|not come back'},
            {'label': 'a Florida example of each', 'any': ['sun', 'solar', 'water', 'spring', 'rain', 'tree', 'pine', 'wood', 'forest', 'wind', 'phosph', 'oil', 'gas', 'limestone', 'lime stone', 'coal', 'rock'], 'min': 2}],
        'ans-3': [
            {'label': 'the word source', 're': 'source'},
            {'label': 'why two', 're': 'wrong|mistake|miss|left out|leave out|leaves out|forg[eo]t|only one|one side|check|compare|agree|whole|both|true|sure|different|same|all the|half'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|not all|not always'},
            {'label': 'two pieces of evidence', 'any': ['solar', 'sun', 'land', 'tree', 'pine', 'forest', 'animal', 'habitat', 'home', 'phosph', 'fertili', 'food', 'oil', 'spill', 'pollut', 'smoke', 'air', 'mine', 'mining', 'pit', 'lake', 'impact', 'water', 'beach'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-2': 20, 'ans-3': 15, 'cer-4': 30},
    'hints': {
        'ans-2': ['Think about the Refill race. Which bars came back?', 'Renewable comes back fast. Nonrenewable takes millions of years.', 'Try: A renewable resource ___. A nonrenewable resource ___. In Florida, ___ is renewable and ___ is not.'],
        'ans-3': ['Think about Source A and Source B in Part 4.', 'What did the flyer leave out?', 'Try: Scientists check two sources because one source might ___.'],
        'cer-4': ['First decide: are all renewables good and all nonrenewables bad?', 'Think of the solar farm, the pine forest and the phosphate mine.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'A solar farm is renewable, but it covers a lot of land where animals lived.',
                'Pine forests grow back, but animals lose their homes until new trees grow.',
                'Phosphate is nonrenewable, but it makes fertilizer that helps grow food.',
                'Oil spills hurt beaches and wildlife, and burning oil pollutes the air.',
                'Every resource in Impact check changed the land, air, water or wildlife.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · the lakes that weren’t there', 'length': '30–40 s',
                    'script': 'Hi, it’s Dr. Reyes. A volunteer brought me three photos taken from space: the same piece of central Florida in 1985, 2004 and 2023. See the dark square lakes and the bare tan patches? They keep showing up in new places. Lakes don’t usually come in squares. What is making them? And is something being taken that won’t come back? Let’s find four clues.'},
        'warmup': {'label': 'Warm-Up · take it apart (Clue 1)', 'length': '20–30 s',
                   'script': 'Everything you use started somewhere on Earth. Pick the pencil, the juice box or the orange, and take it apart. Drag each part to where it started. Did it grow? Did it come from the sky? Or did it come out of the ground? Save the orange for last. It has a surprise inside.'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Say each word. Hold up something renewable (a leaf) and something nonrenewable (a rock or a plastic bottle).'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · what counts as a resource', 'length': '20–30 s'},
        'part2': {'label': 'Part 2 · refill race (Clue 2)', 'length': '25–35 s',
                  'script': 'Time for a race! Press the button to use up all five resources. Then drag time forward: one day, one year, all the way to a million years. Watch the bars. Which ones fill back up? And try the water at both pumping speeds. Something sneaky happens when you pump fast.'},
        'part3': {'label': 'Part 3 · impact check (Clue 3)', 'length': '25–35 s',
                  'script': 'Even good choices change things. Open each photo. First, stamp it renewable or nonrenewable. Then pick what using it changes. Here’s my hint: none of them gets “nothing changes.” And look closely at the mine photo. Does it look familiar?'},
        'explore': {'label': 'Part 4 · two sources (Clue 4)', 'length': '25–35 s',
                    'script': 'Two sources, one claim. A mining company made Source A. Government scientists wrote Source B. Sort every fact: is it a benefit or a cost? Then find what one source left out. When you can make a claim that’s fair to both, you’ll have your last clue.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s',
                       'script': 'Do you have all four clues? Crack the case at the top of this tab: what is making those square lakes, and will it come back? Then answer two questions, compare two Florida resources in Part C, and write your CER. Your answers save as you type.'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · compare two resources', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says all renewable resources are good for the environment, and all nonrenewable ones are bad. Hmm. Think about the solar farm and the phosphate mine. Pick your side, tap two pieces of evidence in the planner, then explain how they prove your claim.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 15.02 (the Florida resource map).',
                    'script': 'Case closed! The square lakes are old phosphate mine pits. The rock became fertilizer, and it won’t come back. Next time, we’ll read a map of Florida. Why is phosphate found in just one part of the state? Bring your detective eyes.'},
    },
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'The Florida orange, taken apart (Warm-Up)',
        'Your Refill race at 1 million years (The Lesson)',
        'A resource you stamped in Impact check (The Lesson)',
        'The answer that cracked the case (Assignment)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['A satellite view of a mine with square lakes', 'A dragline digging', 'My two-column resource chart'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 3,
                           'prompts': ['Draw a two-column chart: renewable and nonrenewable', 'Draw one picture in each column', 'Label each with its use and its impact']}]},
    'hlCoach': copy.deepcopy(P['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🪨', 'name': 'Phosphate pebble',
                 'line': 'You cracked Case 15, and a phosphate pebble from the mine goes in your Field Notebook. (A specimen is something a scientist collects to study.) Next lesson: a map of Florida’s resources.'},
    'notebookTitle': P['notebookTitle'],
    'notebook': [dict(x) for x in Q['notebook']],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You’ll use every one of them today.',
    'tool': {
        'name': 'Core drill', 'icon': '🔩', 'tab': 'assignment', 'after': '#tab-assignment .activity-card', 'key': '15-tool', 'sim': 'coredrill',
        'kicker': 'Bonus · Tool of the Week',
        'teaser': 'Drill into the ground at three Florida spots, pull up the layers, and find where the phosphate is.',
        'done': 'You drilled three spots and read the layers like a geologist. A core drill sticker is in your Field Notebook.',
        'why': {'icon': '🔩', 'q': 'What is a core drill?', 't': 'A drill with a hollow bit. As it spins down into the ground, a long column of soil and rock slides up inside it. Scientists pull it out to see the layers.'},
        'coredrill': {
            'title': 'What’s under Florida?',
            'todo': ['Tap each part of the core drill to learn it.', 'Pick a spot, then press Drill. Drill all three spots.', 'Tap the layers in your cores to read them, then answer the question.'],
            'parts': [{'label': 'The hollow drill bit', 't': 'Its sharp teeth cut a round hole. The middle is empty, so a column of ground slides up inside.'},
                      {'label': 'The core tube', 't': 'The long tube that holds the sample as the drill goes deeper.'},
                      {'label': 'The core box', 't': 'Scientists lay each sample in a long box, top at the top, so they can read the layers in order.'}],
            'deepest': 80,
            'sites': [
                {'k': 'bone', 'name': 'Central Florida', 'icon': '🌾', 'where': 'A pasture near Bone Valley, east of Tampa',
                 'layers': [{'k': 'sand', 't': 'Sand and soil', 'from': 0, 'to': 20, 'col': '#E6D2A4', 'note': 'Loose sand on top. Miners call it the overburden (the layer over the good stuff) and pile it to the side first.'},
                            {'k': 'phos', 't': 'Phosphate pebbles', 'from': 20, 'to': 40, 'col': '#9C8A6B', 'note': 'Gray-brown pebbles mixed with sand and clay. They formed millions of years ago, when shallow seas covered this part of Florida. Fossil shark teeth are found in this layer!'},
                            {'k': 'lime', 't': 'Limestone', 'from': 40, 'to': 80, 'col': '#D9D3C2', 'note': 'Rock made from the shells and skeletons of ancient sea life. Florida’s underground fresh water fills its tiny holes.'}]},
                {'k': 'miami', 'name': 'South Florida', 'icon': '🏙️', 'where': 'Near Miami, at the edge of the Everglades',
                 'layers': [{'k': 'soil', 't': 'Thin soil', 'from': 0, 'to': 3, 'col': '#4A3A2A', 'note': 'Only a few inches to a few feet of soil here. Rock is right under your feet.'},
                            {'k': 'lime', 't': 'Limestone full of water', 'from': 3, 'to': 80, 'col': '#E2DCC8', 'note': 'This limestone is dug up to make cement and roads. Water seeps into the pits, so they turn into lakes. No phosphate layer here.'}]},
                {'k': 'spring', 'name': 'North Florida', 'icon': '💧', 'where': 'Near the springs north of Gainesville',
                 'layers': [{'k': 'sand', 't': 'Sand', 'from': 0, 'to': 30, 'col': '#EBDDB5', 'note': 'Rain soaks down through this sand.'},
                            {'k': 'lime', 't': 'Limestone full of water', 'from': 30, 'to': 80, 'col': '#BFD3D0', 'note': 'This is the Floridan Aquifer, an underground layer of rock that holds fresh water. Springs bubble out of it. Most Floridians get their drinking water from underground.'}]}],
            'need': {'site': 'bone', 'layer': 'phos'},
            'q': {'q': 'Where would a mining company drill to find phosphate?', 'opts': [
                {'t': 'Central Florida', 'ok': True, 'why': 'Yes! Only the central Florida core had a phosphate layer. Next lesson, a map of Florida will show you why.'},
                {'t': 'South Florida', 'why': 'Look at the South Florida core. Is there a phosphate layer?'},
                {'t': 'North Florida', 'why': 'Look at the North Florida core. Is there a phosphate layer?'}]}}},
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '.fs-game[data-mod="unmake"]'},
         'label': 'Warm-Up: one thing near me and where it came from', 'q': 'Warm-Up: One thing near me, three materials it’s made of, and where one of them started',
         'title': 'Your turn: take apart one thing near you.',
         'fields': [{'t': 'My thing', 'icon': '🎒', 'ph': 'I picked my…'},
                    {'t': 'Three materials it’s made of', 'icon': '🧩', 'ph': 'It’s made of ___, ___ and ___.', 'long': True},
                    {'t': 'Where one material started on Earth', 'icon': '🌎', 'ph': 'The ___ started as… It grew / came from the sky / was dug up / was pumped up.', 'long': True}]},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'hide-nw', 'type': 'hide', 'find': {'sel': '.act-warmup .socratic-q', 'text': 'Notice'}},
        {'id': 'hide-tip', 'type': 'hide', 'find': {'sel': '.act-warmup .callout', 'text': 'Today'}},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Pick one <strong>renewable</strong>'.replace('<strong>', '').replace('</strong>', '')},
         'label': 'Part C: Compare two Florida resources', 'q': 'Part C: One renewable and one nonrenewable Florida resource, a use and an impact for each, and which has the smaller impact',
         'title': 'My resource comparison',
         'fields': [{'t': 'My renewable resource: one use and one impact', 'icon': '♻️', 'ph': '___ is renewable. People use it to… Its impact is…', 'long': True},
                    {'t': 'My nonrenewable resource: one use and one impact', 'icon': '⛔', 'ph': '___ is nonrenewable. People use it to… Its impact is…', 'long': True},
                    {'t': 'Which one changes the land, air or water less, and why', 'icon': '⚖️', 'ph': '___ has a smaller impact because…', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Are all renewables good and all nonrenewables bad?', 'ph': 'I disagree. Not all…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-2': 'Part B · Question 5', 'ans-3': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] in ('14.01', '14.02'): n['have'] = True
    if n['lesson'] == '15.01': n.update({'icon': '🪨', 'name': 'Phosphate pebble'})
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me explain which resources come back and which run out?']
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'Phosphate rock takes millions of years to form, so it is nonrenewable.',
    'key': ['Phosphate', 'rock', 'millions', 'years', 'nonrenewable'],
    'small': ['takes', 'of', 'to', 'so', 'it', 'is'],
    'model': 'A scientist might highlight “phosphate rock”, “millions of years” and “nonrenewable”. Those words tell what it is and why. Small words like “of” and “so” don’t carry the idea.'}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
