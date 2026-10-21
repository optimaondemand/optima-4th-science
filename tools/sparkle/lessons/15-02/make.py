#!/usr/bin/env python3
"""Writes data.json and fixes.json for 15.02 (run from this folder). The Florida map comes from flmap.json (made by flmap-gen.mjs from us-atlas, U.S. Census shapes)."""
import json, copy
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../15-01/data.json', encoding='utf-8'))
FL = json.load(open('flmap.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

# ---------------------------------------------------------------- ticked fixes (Bethany, 21 Oct 2026)
fx('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist asks for a map, a key and an evidence statement',
   '🎨 Part C &mdash; Build Your Own Food Chain', '🗺️ Part C &mdash; Map One Florida Resource')
fx('fix', 'copy-paste leftover: Part C task from 9.01 (typed on the page; the map sketch is a bonus)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   "Pick one Florida resource from today’s map. Tell where it is found, describe its pattern, and write an evidence statement about why it’s there.</p>", True)
fx('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'quarter label in the footer: week 15 is Quarter 2', 'Science &middot; Quarter 3 &middot;', 'Science &middot; Quarter 2 &middot;')
fx('fix', 'this is an Earth science lesson (4-ESS3-1), not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Earth Science</div>')
fx('fix', 'the AI map drew Florida’s shape wrong, put limestone in one band (it lies under the whole state), wind turbines down the Atlantic coast (Florida has none) and phosphate too far north; the real-data map games replace it',
   r'<div class="lesson-figure scroll-reveal">.*?<div class="lesson-figure-caption">.*?</div>\s*</div>\s*', '', True)
fx('fix', 'shaky fact: Florida mines most of the country’s phosphate, not nearly all (North Carolina, Idaho and Utah mine it too); plain label',
   "<p><strong>Common misconception:</strong> Some people think a resource is \"everywhere\" just because it's common. Most resources have specific locations — Florida produces nearly all of the country's phosphate but very little iron. Maps make those patterns visible.</p>",
   "<p><strong>Watch out:</strong> A resource can be common and still be found in only a few places. Florida mines most of the phosphate in the United States, but almost all of it comes from two small areas. Maps make those patterns easy to see.</p>")
fx('fix', 'matches the real data: Florida’s groves are now mostly in central and south-central Florida (after big freezes in the 1980s, many moved south), including counties next to the Everglades',
   "\"The map shows citrus groves in a band across <strong>central Florida</strong>, away from the coldest northern areas and the wettest southern Everglades. The pattern is evidence that citrus trees need a specific mix of warmth and well-drained soil.\"",
   "\"The map shows citrus groves in a band across <strong>central and south-central Florida</strong>, away from the colder north. The pattern is evidence that orange trees need warm winters with few freezes.\"")

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; dash removed',
   "Hold this question in your head as you work. By the end of the lesson, you'll be able to read a Florida resource map, describe where things are concentrated, and explain why — using evidence from the map.",
   "Keep this question in mind. By the end, you’ll be able to read a Florida resource map, describe where things are found, and use the map as evidence to explain why.")
fx('plain', 'answers are made on the page now (the game below)',
   r"<p>Imagine you have a blank outline of Florida in your notebook\..*?</p>\s*<ul[^>]*>.*?</ul>",
   "<p>Where in Florida do you think orange groves, beaches, phosphate mines and springs are found? <strong>Guess first</strong> on the blank map below. No looking anything up!</p>", True)
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', 'dash removed; plain words', "</span></span> — the little box that explains what every symbol means.</p>", "</span></span>: the little box that tells what every symbol means.</p>")
fx('plain', 'plain words; shorter', "When you look at the whole map, you're really asking one question: where are things concentrated, and where are they sparse? That's the",
   "When you look at the whole map, ask one question: where are things crowded together, and where are there few or none? That’s the")
fx('plain', 'dash removed; Part 3 starts here (Why here?)',
   r"<p>Every resource's <span class=\"vtip\">location(<span class=\"vtip-box\">.*?</span>)</span> has a reason — usually related to geology, climate, or access to transportation\. The <span class=\"vtip\">availability<span class=\"vtip-box\">.*?</span></span> of a resource determines who can use it and how\.</p>",
   "<p>Every resource’s location has a reason, usually the rock underground (geology), the weather (climate), or the ocean nearby. How much of a resource a place has is its <span class=\"vtip\">availability<span class=\"vtip-box\"><span class=\"vtip-word\">Availability</span>How much is there and how easy it is to get to.</span></span>.</p>", True)
fx('plain', 'pretend map, said plainly (Bethany kept this question)',
   "A new resource map shows wind turbines mostly on Florida's coasts.", "Pretend a new resource map shows wind turbines mostly on Florida's coasts.")
fx('plain', 'the four resources are now on the map, not a diagram', "Pick one of the four resources from the diagram (citrus, phosphate, springs, or beaches).",
   "Pick one of the four resources from today’s map (citrus, phosphate, springs, or beaches).")
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'plain words; dash removed', "Next module, we'll dig into the tough questions: when we use resources, what tradeoffs do we make — and how do we choose well?",
   "Next week, we’ll dig into a tough question: when we use a resource, how do we weigh what we gain against what we lose?")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')

# ---------------------------------------------------------------- lean cuts (the fact boxes go with them: “75% of U.S. phosphate”, “10 million people”, the map-projection Go Deeper)
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (Map Detective moves to Part 4 and Part C; the “10 million people” fact goes with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: the Key Concept box repeats Part 2', r'<div style="background:#FFF6E5;border:2.5px solid #F0C97A;[^"]*">\s*<div[^>]*>⭐ Key Concept</div>\s*<p[^>]*>.*?</p>\s*</div>\s*', '', True)
fx('cut', 'lean: Stop & Reason pointed at the removed map (Stop & Think in Part 1 stays)', r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: the diagram heading becomes Part 3 (Why here? replaces the tap diagram)', 'margin-top:22px;">Four Florida Resource Patterns</h3>', 'margin-top:22px;">Part 3 · Why Here?</h3>')
fx('cut', 'lean + facts: Observe & Reason, the “75%” fact, the springs callout and Go Deeper at the end of the Lesson; Part 4 = the old Explore; next button goes to Self-Check',
   r'<div class="socratic-q">\s*<span class="sq-icon">👀</span>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 4 · Test the Pins</h3>\n      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">Now use the map like a scientist. Marco put four pins on his map. Check each pin against the map: could he find phosphate there? Your evidence is what the map shows.</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 6 removed (Bethany kept 5 and 7; Map layers teaches the key)', r'<div class="pq">\s*<span class="pq-num"[^>]*>6</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: renumber Part B (7 → 6)', '<span class="pq-num" style="background:#D4772C;">7</span>', '<span class="pq-num" style="background:#D4772C;">6</span>')
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C typed on the page; the map sketch is a bonus',
   "A sketched Florida map with at least 3 resource symbols, a map key, and a one-sentence evidence statement underneath.",
   "One Florida resource: where it is, its pattern, and an evidence statement. (A map sketch with a key is a bonus.)")
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether maps count as scientific evidence, and supported it with two pieces of evidence from the lesson.',
   '<strong>Use Your Evidence:</strong> My claim about whether maps count as scientific evidence, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', True)

# ---------------------------------------------------------------- the map
FL['layers'] = {
    'citrus': {'t': 'Citrus groves', 'c': '#F6B44B'},
    'beaches': {'t': 'Beaches', 'c': '#E9C46A'},
    'phosphate': {'t': 'Phosphate mines', 'c': '#7A5230'},
    'springs': {'t': 'Freshwater springs', 'c': '#1F7FB5'}}
MAPCREDIT = ('Map: Florida shapes from U.S. Census Bureau boundary files (public domain, via us-atlas). Springs: Florida’s first-magnitude springs. '
             'Phosphate mines: Bone Valley and Hamilton County mining areas (U.S. Geological Survey). Citrus: the leading citrus counties (USDA). Beaches: Florida’s sandy coast. Symbols are placed by hand and are approximate.')
PINS = [{'n': 1, 'id': 'miami', 'name': 'Near my cousin’s house in Miami'}, {'n': 2, 'id': 'pensacola', 'name': 'The beach at Pensacola'},
        {'n': 3, 'id': 'mulberry', 'name': 'A cow pasture near Mulberry'}, {'n': 4, 'id': 'white', 'name': 'The woods near White Springs'}]
I = lambda n: 'images/15-02-' + n + '.jpg'

D = {
    'lesson': '15.02', 'week': 15, 'day': 2, 'guide': 'lena', 'prefix': 'g4sci-15-2', 'manifestKey': '15-02',
    'paths': P['paths'], 'crew': P['crew'],
    'expedition': {'num': 15, 'title': 'Dig Here?'},
    'ambient': {'icon': '🌲', 'label': 'Pine forest sounds'},
    'flmap': FL,
    'case': {
        'num': 15, 'title': 'Dig Here?',
        'hook': 'After we solved the square lakes, a volunteer named Marco wrote me a letter with a big idea. He wants to dig our own phosphate to make fertilizer (plant food) for the Field Station garden. Before anyone grabs a shovel, let’s check his four pins against a real resource map.',
        'letter': {'to': 'Dear Dr. Reyes,', 'sign': '— Marco, Field Station volunteer',
                   'body': ['Phosphate makes fertilizer, right? So let’s dig our own! I put four pins on my map.',
                            'Phosphate is probably everywhere in Florida, so any pin should work. Which one should we dig first?'],
                   'pins': PINS},
        'stills': [],
        'question': 'Which of Marco’s pins could have phosphate, and why is phosphate found only in some places?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'stillsCredit': MAPCREDIT,
        'clues': [
            {'id': 'guessmap', 'icon': '⭐', 'where': 'Warm-Up: guess first', 't': 'Phosphate isn’t everywhere. On the real map, the mines sit in just two small areas: central Florida east of Tampa, and one spot in north Florida.'},
            {'id': 'maplayers', 'icon': '🔑', 'where': 'The Lesson, Part 1: map layers', 't': 'The map key tells what each symbol means. Phosphate mines are clustered. Beaches follow the coast, and citrus makes a band across the middle.'},
            {'id': 'whyhere', 'icon': '🐚', 'where': 'The Lesson, Part 3: why here?', 't': 'Phosphate rock formed only where shallow seas once covered parts of Florida. Mines go where the rock is, so the clusters on the map are evidence of what’s underground.'},
            {'id': 'pins', 'icon': '📍', 'where': 'The Lesson, Part 4: test the pins', 't': 'Pins 3 (Mulberry) and 4 (White Springs) are inside phosphate clusters. Pins 1 (Miami) and 2 (Pensacola) have no phosphate anywhere near.'},
        ],
        'solve': {
            'title': 'Where could Marco find phosphate?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Anywhere. Phosphate is spread all over Florida, so every pin works.', 'why': 'Check Clue 1. Are phosphate mines spread all over the map?'},
                {'t': 'Only at pins 3 and 4, near Mulberry and White Springs. Phosphate rock formed only where ancient seas left it, and the clusters on the map are the evidence.', 'right': True,
                 'why': 'Case cracked! Phosphate is found only in certain places, and the map pattern shows where. Now write your case report: it’s the questions below.'},
                {'t': 'Only at pins 1 and 2, because Miami and Pensacola are big, busy places.', 'why': 'Check Clue 4. Does the map show phosphate near Miami or Pensacola?'},
            ]},
    },
    'guessmap': {
        'afterText': 'on the blank map below', 'kicker': 'Warm-Up game', 'title': 'Guess first',
        'todo': ['Pick a resource, then tap the map where you think it is found most.', 'Place all four stars.', 'Press “Show me the real map” and see how close you were.'],
        'why': {'icon': '🗺️', 'q': 'Why guess first?', 't': 'Scientists write down what they expect before they look at data. Then they can tell what surprised them.'},
        'tokens': ['citrus', 'beaches', 'phosphate', 'springs'], 'near': 25, 'far': 90,
        'q': 'Look at the real map. Which resource is found in the fewest places?',
        'opts': [{'t': 'Beaches', 'miss': 'Beaches go all the way around the coast. Which symbol shows up in only a couple of small spots?'},
                 {'t': 'Phosphate mines', 'ok': True},
                 {'t': 'Springs', 'miss': 'There are lots of spring dots across north-central Florida. Which symbol shows up in only a couple of small spots?'}],
        'win': 'Phosphate is found in just two small areas of Florida. Marco thought it was everywhere. That’s a clue.',
        'clue': 'guessmap'},
    'maplayers': {
        'afterText': "tell you something about why it's there", 'kicker': 'Part 1 game', 'title': 'Map layers',
        'todo': ['Turn on one layer at a time in the map key.', 'For each layer, pick the pattern you see.', 'Read all four, then answer the question.'],
        'why': {'icon': '🔑', 'q': 'What is a map layer?', 't': 'One set of symbols for one thing. Turning layers on one at a time keeps a busy map easy to read.'},
        'layers': ['citrus', 'beaches', 'phosphate', 'springs'],
        'patterns': [{'k': 'cluster', 'icon': '🔘', 't': 'Clustered in one or two areas'}, {'k': 'band', 'icon': '➖', 't': 'A wide band'}, {'k': 'coast', 'icon': '🌊', 't': 'Along the coast'}],
        'answer': {'citrus': 'band', 'beaches': 'coast', 'phosphate': 'cluster', 'springs': 'cluster'},
        'note': {'citrus': 'Groves stretch in a band across central and south-central Florida.',
                 'beaches': 'Beaches follow the coast all the way around the state.',
                 'phosphate': 'Two small clusters: a big one east of Tampa and a small one in north Florida.',
                 'springs': 'Springs cluster in north-central Florida, with a few in the Panhandle.'},
        'miss': {'citrus': 'Look at the orange shading. Is it in one spot, or does it stretch across the state?',
                 'beaches': 'Where are the beach symbols? Follow the edge of the state.',
                 'phosphate': 'How many places have diamond symbols? Are they spread out or bunched up?',
                 'springs': 'Are the blue dots all over the state, or mostly in one part?'},
        'q': 'Marco says phosphate is probably everywhere. What does the phosphate layer show?',
        'opts': [{'t': 'It’s spread across the whole state.', 'miss': 'Turn the phosphate layer on again. Where are the diamonds?'},
                 {'t': 'It’s clustered in just two small areas.', 'ok': True},
                 {'t': 'It’s along the coast, like the beaches.', 'miss': 'Look again. Are the diamonds on the coast?'}],
        'win': 'You read every layer with the map key. Phosphate is clustered, not everywhere. That’s a clue.',
        'clue': 'maplayers'},
    'whyhere': {
        'replace': '#tab-lesson .diagram-wrap', 'kicker': 'Part 3 game', 'title': 'Why here?',
        'todo': ['Look at each small map.', 'Drag the reason that explains the pattern onto it, or tap the reason and then the map.', 'One reason is a trick. Then answer the question.'],
        'causes': [{'id': 'sea', 'icon': '🐚', 't': 'Rock left by ancient seas'},
                   {'id': 'lime', 'icon': '🪨', 't': 'Water-filled limestone close to the surface'},
                   {'id': 'warm', 'icon': '☀️', 't': 'Warm winters with few freezes'},
                   {'id': 'edge', 'icon': '🌊', 't': 'Where land meets the ocean'},
                   {'id': 'people', 'icon': '🏙️', 't': 'Where the most people live', 'miss': 'Trick card! Lots of people live in Miami and Jacksonville. Do these symbols follow the big cities?'}],
        'items': [
            {'k': 'phosphate', 'cause': 'sea', 'why': 'Millions of years ago, shallow seas covered these parts of Florida. Phosphate formed in the sea-floor mud and in old bones and teeth.', 'miss': 'Phosphate is a rock. What made the rock form only in these spots?'},
            {'k': 'springs', 'cause': 'lime', 'why': 'Here the limestone that holds Florida’s underground water is close to the surface, so water pushes up through openings.', 'miss': 'Springs are water coming out of the ground. Where is that water stored?'},
            {'k': 'citrus', 'cause': 'warm', 'why': 'A hard freeze can kill orange trees. Freezes are rarer here than in north Florida.', 'miss': 'Orange trees can die in a freeze. What kind of weather do they need?'},
            {'k': 'beaches', 'cause': 'edge', 'why': 'Waves pile up sand along the shore, so beaches only form on the coast.', 'miss': 'Where do waves pile up sand?'}],
        'q': 'So why are phosphate mines found in only a few places?',
        'opts': [{'t': 'The rock formed only in those places, so the mines go where the rock is.', 'ok': True},
                 {'t': 'Miners like to live near the beach.', 'miss': 'Look at the phosphate map. Are the mines on the beach?'},
                 {'t': 'Phosphate is everywhere, but people only dig in two places.', 'miss': 'Think about Why here. Did the rock form everywhere?'}],
        'credit': MAPCREDIT,
        'win': 'Every pattern has a reason. The phosphate clusters are evidence of where the rock formed. That’s a clue.',
        'clue': 'whyhere'},
    'photos': [{
        'id': 'spring', 'after': 'whyhere', 'kicker': 'Look closer · a real Florida spring', 'short': 'spring photo',
        'title': 'Where does spring water come from?',
        'todo': ['Tap each number on the photo to read what it is.', 'Then match the clues to the labels below.'],
        'why': {'icon': '📸', 'q': 'Where is this?', 't': 'Manatee Springs, one of the blue dots on the springs layer, in north-central Florida.'},
        'img': I('manatee-spring'), 'alt': 'A clear, blue-green spring pool surrounded by cypress trees, with a deep blue spot in the middle, swimmers on the left and cypress knees on the bank.',
        'credit': 'Manatee Springs, Manatee Springs State Park, Florida, Ebyabe, via Wikimedia Commons', 'license': 'CC BY 2.5',
        'hotspots': [
            {'n': 1, 'x': 42, 'y': 54, 'label': 'The deep blue spot', 't': 'This is the vent, the spring’s opening. Water from the underground limestone pours up out of it, every day of the year.'},
            {'n': 2, 'x': 12, 'y': 78, 'label': 'Pale rock under the water', 't': 'Limestone. The water traveled through cracks and holes in rock like this before it came up here.'},
            {'n': 3, 'x': 19, 'y': 40, 'label': 'Swimmers', 't': 'They show how big the spring is. The water stays about 72°F all year, even in winter.'},
            {'n': 4, 'x': 62, 'y': 84, 'label': 'Cypress knees', 't': 'Bumps that grow up from the roots of cypress trees. Cypress trees grow where the ground stays wet.'}],
        'task': {'q': 'Match each clue to a label on the photo.', 'win': 'You found it: spring water comes up from the limestone underground. That’s why springs cluster where that rock is close to the surface.',
                 'items': [{'icon': '⬆️', 'step': 'Where water comes up from underground', 'ans': 1, 'evid': 'Water pours up out of the spring’s vent.'},
                           {'icon': '🪨', 'step': 'The kind of rock the water flows through', 'ans': 2, 'evid': 'The water flows through limestone underground.'},
                           {'icon': '📏', 'step': 'Shows how big the spring is', 'ans': 3, 'evid': 'Swimmers show the spring pool is big.'},
                           {'icon': '🌳', 'step': 'A tree that grows in wet ground', 'ans': 4, 'evid': 'Cypress trees grow around the wet spring.'}]}}],
    'pins': {
        'afterText': 'Marco put four pins on his map', 'kicker': 'Part 4 game', 'title': 'Test the pins',
        'todo': ['Tap a numbered pin. The map zooms in.', 'Decide if Marco could find phosphate there, then pick the evidence.', 'Test all four pins.'],
        'why': {'icon': '📍', 'q': 'Why test with a map?', 't': 'A map is a record of real data. Checking an idea against data is how scientists test it.'},
        'hint': 'Tap a numbered pin on the map.',
        'layers': ['citrus', 'beaches', 'phosphate', 'springs'],
        'verdicts': [{'k': 'yes', 'icon': '✅', 't': 'Phosphate could be here'}, {'k': 'no', 'icon': '❌', 't': 'No phosphate here'}],
        'pins': [
            dict(PINS[0], note='My cousin has a big backyard!', verdict='no', vmiss='Look closely. Are there any diamond symbols near Pin 1?',
                 q='What does the map show near Pin 1?',
                 opts=[{'t': 'No phosphate symbols anywhere near it, just the beach.', 'ok': True},
                       {'t': 'A cluster of phosphate mines.', 'miss': 'Zoom in again. Is there a diamond near Miami?'},
                       {'t': 'Orange groves all around it.', 'miss': 'Look at the colors near Miami. Is it orange?'}],
                 why='No phosphate near Miami. The rock under Miami is limestone. People dig it for roads and cement, not fertilizer.'),
            dict(PINS[1], note='Sand is easy to dig!', verdict='no', vmiss='Is there a diamond symbol anywhere near Pin 2?',
                 q='What does the map show at Pin 2?',
                 opts=[{'t': 'A beach on the coast, with no phosphate nearby.', 'ok': True},
                       {'t': 'The biggest phosphate cluster in Florida.', 'miss': 'Zoom in again. Where is Pensacola compared to the diamonds?'},
                       {'t': 'A cluster of springs.', 'miss': 'Look at the symbols at Pin 2. Are they blue dots?'}],
                 why='Beach sand isn’t phosphate rock. The closest phosphate is hundreds of miles away.'),
            dict(PINS[2], note='Lots of open space here.', verdict='yes', vmiss='Look right around Pin 3. What symbols do you see?',
                 q='What does the map show at Pin 3?',
                 opts=[{'t': 'It’s right inside the big cluster of phosphate mines.', 'ok': True},
                       {'t': 'Only beaches.', 'miss': 'Is Mulberry on the coast? Look at the symbols around it.'},
                       {'t': 'Only springs.', 'miss': 'Look at the symbols around Pin 3. Are they blue dots or brown diamonds?'}],
                 why='Mulberry is in Bone Valley, Florida’s biggest phosphate area. That’s where the square lakes from Case 15 came from.'),
            dict(PINS[3], note='Nobody lives in these woods.', verdict='yes', vmiss='Look again. Is there a diamond symbol near Pin 4 too?',
                 q='What does the map show at Pin 4?',
                 opts=[{'t': 'A small cluster of phosphate mines right there.', 'ok': True},
                       {'t': 'Only springs, so no phosphate.', 'miss': 'There are springs nearby, but look again. Are there diamonds too?'},
                       {'t': 'Orange groves.', 'miss': 'Look at the colors near Pin 4. Is it orange?'}],
                 why='Surprise! A second, smaller phosphate area is in north Florida, near White Springs. Phosphate is found in certain places, not everywhere.')],
        'q': 'Which of Marco’s pins could have phosphate?',
        'opts': [{'t': 'All four pins.', 'miss': 'Look at your test results. Did every pin pass?'},
                 {'t': 'Pins 3 and 4, inside the phosphate clusters.', 'ok': True},
                 {'t': 'Only Pin 1.', 'miss': 'What did the map show near Miami?'}],
        'win': 'You tested every pin with real map data. Two pins pass and two fail. That’s your last clue.',
        'clue': 'pins'},
    'exploreMod': 'pins',
    'quizKicker': '',
    'quizMiss': {
        'q1': {'B': 'The title tells the topic. Which part tells what each symbol means?', 'C': 'Big symbols can trick you. Which part tells what each symbol means?'},
        'q2': {'A': 'Weather doesn’t make rock. What is under the ground there?', 'B': 'The mines aren’t on the coast. Think about Why here.'},
        'q3': {'A': 'People built hotels, but where does beach sand come from?', 'C': 'Look at the beaches layer. Are there beaches inland?'}},
    'flags': {
        'ans-1': [
            {'label': 'one resource', 're': 'citrus|orange|grove|phosph|spring|beach'},
            {'label': 'where it is', 're': 'north|south|central|middle|coast|edge|east|west|panhandle|tampa|miami|gainesville|bone valley|mulberry|cluster|band'},
            {'label': 'why it’s there', 're': 'because|since|so |rock|sea|ocean|limestone|water|warm|freez|weather|climate|sand|soil|underground'}],
        'ans-3': [
            {'label': 'where the wind is', 're': 'coast|shore|ocean|beach|sea|edge|water'},
            {'label': 'what the pattern tells', 're': 'strong|windy|wind|blow|more wind|most wind'},
            {'label': 'map evidence', 're': 'map|pattern|turbine|shows|evidence|because'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|do count|does count|are evidence|is evidence'},
            {'label': 'two pieces of evidence', 'any': ['key', 'symbol', 'pattern', 'cluster', 'phosph', 'spring', 'limestone', 'citrus', 'orange', 'beach', 'coast', 'pin', 'data', 'real', 'measure', 'mine', 'rock', 'test'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-1': 15, 'ans-3': 15, 'cer-4': 30},
    'hints': {
        'ans-1': ['Pick the one you remember best from Map layers.', 'Use place words: north, central, south, coast.', 'Try: ___ is found in ___. It’s there because ___.'],
        'ans-3': ['Where are the turbines on this pretend map?', 'People build wind turbines where the wind blows hardest.', 'Try: The pattern shows the wind is strongest ___, because ___.'],
        'cer-4': ['First decide: are maps only pictures, or are they evidence?', 'Think about how you tested Marco’s pins.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'The map key tells exactly what each symbol stands for.',
                'Each symbol on a resource map marks a real place where something was found or measured.',
                'The phosphate clusters on the map are where phosphate rock formed underground.',
                'Springs on the map cluster where water-filled limestone is close to the surface.',
                'We used the map to test Marco’s pins and ruled two of them out.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · dig here?', 'length': '30–40 s',
                    'script': 'Hi, it’s Dr. Reyes. Remember those square lakes? They were phosphate mines. Now Marco, one of our volunteers, wants to dig his own phosphate! He put four pins on a map, and he thinks phosphate is everywhere in Florida. Is he right? Let’s test his pins with a real resource map.'},
        'warmup': {'label': 'Warm-Up · guess first (Clue 1)', 'length': '20–30 s',
                   'script': 'Before we look at any data, let’s guess. Pick a resource, then tap the blank map where you think it’s found. Do all four. Then press the button and see the real map. Don’t worry about being right. Scientists guess first so they can notice what surprises them.'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Say each word. Point to a real map key, then sweep a hand along a coast for “pattern”.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · map layers (Clue 2)', 'length': '25–35 s',
                  'script': 'Busy maps can be confusing, so let’s turn on one layer at a time. Check a box in the map key, look at the symbols, and pick the pattern. Are they clustered together? Do they make a wide band? Or do they follow the coast? Watch the phosphate layer closely.'},
        'part2': {'label': 'Part 2 · patterns become evidence', 'length': '20–30 s'},
        'part3': {'label': 'Part 3 · why here? (Clue 3)', 'length': '25–35 s',
                  'script': 'Every pattern on a map has a reason. Look at each little map, then drag the reason that explains it. Is it the rock underground? The weather? The ocean? Be careful: one reason is a trick. After that, visit a real spring with me.'},
        'explore': {'label': 'Part 4 · test the pins (Clue 4)', 'length': '25–35 s',
                    'script': 'Time to test Marco’s idea. Tap a pin and the map zooms in. Could he find phosphate there? Decide, then pick what the map shows as your evidence. Test all four pins. You might find a surprise up north.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s',
                       'script': 'Do you have all four clues? Crack the case at the top of this tab: which of Marco’s pins could have phosphate, and why only there? Then answer two questions, map one resource in Part C, and write your CER. Your answers save as you type.'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · map one resource', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says maps are just pictures, and they don’t count as scientific evidence. Hmm. Think about how you tested Marco’s pins. Pick your side, tap two pieces of evidence in the planner, then explain how they prove your claim.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 16.01 (tradeoffs: benefits and costs of using resources).',
                    'script': 'Case closed! Phosphate is only in a few places, and the map proved it. Sorry, Marco, no digging in the garden. Next time, a new week and a hard question: when we use a resource, how do we weigh what we gain against what we lose?'},
    },
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Your four guesses next to the real map (Warm-Up)',
        'The phosphate layer turned on (The Lesson)',
        'A pin you tested, zoomed in (The Lesson)',
        'The answer that cracked the case (Assignment)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['My Florida resource map', 'A spring and the limestone under it', 'Marco’s four pins'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 3,
                           'prompts': ['Draw Florida and your resource’s symbols', 'Add a map key', 'Label two places']}]},
    'hlCoach': copy.deepcopy(Q['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🗺️', 'name': 'Marco’s pinned map',
                 'line': 'You cracked Case 15, part 2, and Marco’s pinned map goes in your Field Notebook. (A specimen is something a scientist collects to study.) Next week: weighing what we gain and what we lose when we use resources.'},
    'notebookTitle': P['notebookTitle'],
    'notebook': [dict(x) for x in Q['notebook']],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You’ll use every one of them today.',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '.fs-game[data-mod="guessmap"]'},
         'label': 'Warm-Up: my guesses compared to the real map', 'q': 'Warm-Up: My closest guess, my farthest guess, and what surprised me on the real map',
         'title': 'Your turn: how did your guesses compare?',
         'fields': [{'t': 'My closest guess', 'icon': '🎯', 'ph': 'My ___ star was closest. It was about ___ miles off.'},
                    {'t': 'My farthest guess, and where it really is', 'icon': '🧭', 'ph': 'I put ___ in ___, but it’s really in…', 'long': True},
                    {'t': 'What surprised me', 'icon': '😮', 'ph': 'I was surprised that…', 'long': True}]},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'hide-nw', 'type': 'hide', 'find': {'sel': '.act-warmup .socratic-q', 'text': 'Notice'}},
        {'id': 'hide-tip', 'type': 'hide', 'find': {'sel': '.act-warmup .callout', 'text': 'Today'}},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Pick one Florida resource from today'},
         'label': 'Part C: Map one Florida resource', 'q': 'Part C: One Florida resource: where it is found, its pattern, and an evidence statement',
         'title': 'My resource map report',
         'fields': [{'t': 'My resource', 'icon': '🗺️', 'ph': 'I picked…'},
                    {'t': 'Where it is found', 'icon': '📍', 'ph': 'It is found in ___ Florida (north, central, south, along the coast…)', 'long': True},
                    {'t': 'Its pattern', 'icon': '🔘', 'ph': 'It is clustered / in a band / along the coast…', 'long': True},
                    {'t': 'My evidence statement', 'icon': '🔎', 'ph': 'The map shows that ___ is found in ___. The pattern is evidence that ___.', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Do maps count as scientific evidence?', 'ph': 'I disagree. Maps are…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-1': 'Part B · Question 5', 'ans-3': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] == '15.01': n.update({'have': True, 'icon': '🪨', 'name': 'Phosphate pebble'})
    if n['lesson'] == '15.02': n.update({'icon': '🗺️', 'name': 'Marco’s pinned map'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'The map shows phosphate mines clustered in central Florida, where the rock formed.',
    'key': ['map', 'phosphate', 'clustered', 'central', 'rock'],
    'small': ['The', 'shows', 'in', 'where', 'the'],
    'model': 'A scientist might highlight “phosphate mines”, “clustered” and “central Florida”. Those words tell what, what pattern, and where. Small words like “the” and “in” don’t carry the idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me explain why a resource is found in one place and not another?']
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
