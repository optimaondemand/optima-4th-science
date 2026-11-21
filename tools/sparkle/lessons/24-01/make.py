#!/usr/bin/env python3
"""Writes data.json and fixes.json for 24.01 (run from this folder). Case 24 "The Cold Cocoa Cart" (Sam Park, Palmetto Beach, the December
lighted boat parade): Rosa switched to shiny metal mugs; the cocoa goes cold and the handles get hot. Why?
New: case.menu (a chalkboard menu + customer order slips), handlemap (Warm-Up: feel along three spoon handles in a hot mug), heatdots (Part 1:
drag heat dots warm -> cool; "send cold" never works), rodrace (Part 2: butter rod race, replaces the "heat stops here" AI picture and the tap
diagram), cuprace (Part 3 = the old Explore: live cooling graph), iceblocks (the wow after the Cup Race), mugdesign + snowcoat (after the case),
SIMS.irtherm (Tool of the Week: infrared thermometer on real photos)."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../18-01/data.json', encoding='utf-8'))
O = json.load(open('../23-02/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
PS = '<p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)
def I(n): return 'images/24-01-' + n + '.jpg'
VT = lambda w, word, d: '<span class="vtip">' + w + '<span class="vtip-box"><span class="vtip-word">' + word + '</span>' + d + '</span></span>'

# ---------------------------------------------------------------- labels (standing approval)
fx('fix', 'unit label: “Ecosystems & Energy” is a leftover; weeks 18–24 are Unit 5', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Energy, Motion &amp; Collisions</div>')
fx('fix', 'heat and materials is physical science, not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standards label: the plan’s CPALMS codes; TEKS is a Texas code that isn’t in the plan', '<div class="info-value">SC.4.P.10.2, SC.4.P.11.1, SC.4.P.11.2 · TEKS 4.8(B)</div>', '<div class="info-value">SC.4.P.10.2, SC.4.P.11.1, SC.4.P.11.2</div>')

# ---------------------------------------------------------------- ticked fixes (Bethany, 21 Nov 2026)
# 22.01 leftovers in the Warm-Up
fx('fix', '22.01 leftover: the Warm-Up title and subtitle named the toaster lesson', '<div class="act-title">🌅 Warm-Up: What Goes In, What Comes Out?</div>\n        <div class="act-subtitle">A familiar device, a hidden change</div>',
   '<div class="act-title">🌅 Warm-Up: Three Spoons in a Mug</div>\n        <div class="act-subtitle">Feel how far the heat climbs</div>')
fx('fix', '22.01 leftover: the toaster warm-up → the spoon test',
   '<p>Think about a toaster. You drop in cold bread. A minute later, you pull out hot toast.</p>',
   '<p>Sam stands three spoons in a mug of hot cocoa: one metal, one wood and one plastic. After one minute, which handle feels warm? Touch each one to find out.</p>')
fx('fix', '22.01 leftover: the toaster sketch → a list of hot and cold things (on the page)',
   "<p>In your notebook, draw a quick sketch of a toaster. On one side, label what goes IN. On the other, label what comes OUT. (Hint: bread on both sides — but something invisible is also going in. What is it?)</p>",
   '<p>Now think about your day. What hot and cold things did you touch?</p>')
fx('fix', '22.01 leftover: Notice & Wonder about the toaster',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Notice &amp; Wonder</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover: “energy can CONVERT … toasters” callout',
   r'<div class="callout callout-tip">\s*<span class="callout-icon">💡</span>\s*<p>Today you\'ll learn that energy can CONVERT.*?</p>\s*</div>\s*', '', True)
# 9.01 leftovers
fx('fix', '9.01 leftover: Part C was a food chain; the checklist already asks for a conductor and insulator chart', '🎨 Part C &mdash; Build Your Own Food Chain', '🎨 Part C &mdash; My Conductor and Insulator Chart')
fx('fix', '9.01 leftover: Part C task (now a chart typed on the page + a required labeled sketch)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Find 4 conductors and 4 insulators at home. Fill in your chart below, explain one from each side, then sketch one.</p>', True)
fx('fix', '9.01 leftover: Reflect asked about a hawk; the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'supply list: things to try it for real', r'<span class="need-chip"><span>✏️</span>Colored pencils</span>', '<span class="need-chip"><span>🥄</span>A metal spoon and a wooden spoon (to try it for real)</span>', True)
# wrong or shaky facts
fx('fix', 'shaky fact: insulators SLOW heat; they don’t block it (the page’s own pop-up says “Slows heat down”)',
   'Part 2 · Some Materials Carry Heat — Some Block It', 'Part 2 · Some Materials Carry Heat, Some Slow It Down')
fx('fix', 'shaky fact + no dashes: “block heat” → “slow heat down”',
   '</span></span> handle heat in totally different ways. Metals carry heat extremely well — they\'re heat ', '</span></span> handle heat in different ways. Metals carry heat very well, so they\'re heat ')
fx('fix', 'shaky fact: “Wood, plastic, foam, and fabric block heat” → slow it down',
   '</span></span>. Wood, plastic, foam, and fabric block heat — they\'re heat ', '</span></span>. Wood, plastic, foam, and fabric slow heat down, so they\'re heat ')
fx('fix', 'kept (Bethany ticked it): the Florida connection is true, as one line in the list',
   '<li><strong>Why it matters:</strong> we put metal where we WANT heat to flow (pot bottoms). We put insulators where we DON\'T want heat to flow (handles, oven mitts, jackets, walls).</li>',
   '<li><strong>Why it matters:</strong> we put metal where we WANT heat to flow (pot bottoms). We put insulators where we DON\'T want heat to flow (handles, oven mitts, jackets, walls).</li>\n        <li><strong>In Florida:</strong> builders put insulation and shiny barriers in the attic to keep the hot outside air’s heat from getting IN.</li>')
fx('fix', 'closing pop-up: an insulator slows heat, it doesn’t block it', '<span class="vtip-word">Insulator</span>Blocks heat.</span>', '<span class="vtip-word">Insulator</span>Slows heat down.</span>')

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; plain words; no dash', r"<p>Hold this question in your head as you work\. By the end of the lesson.*?</p>",
   "<p>Keep this question in mind. By the end, you’ll predict which materials carry heat well and which slow it down, and explain things like oven mitts and metal pots.</p>", True)
fx('plain', 'cut filler', r"<p>These six words show up all through the lesson\. <strong>Tap a card to flip it</strong>.*?</p>",
   "<p><strong>Tap a card to flip it</strong> and read what the word means.</p>", True)
fx('plain', 'no dash (Part 1)', "It feels cold. The handrail itself didn't change — but it gave its ", "It feels cold. The handrail itself didn't change, but it gave its ")
fx('plain', 'no dash; the misconception moves here and leads into the game (Part 1)',
   'It always travels in ONE direction — from the hotter object to the cooler one. This is called heat ',
   'It always travels in ONE direction: from the hotter object to the cooler one. This is called heat ')
fx('plain', 'the misconception now sits in Part 1, right before Be the Heat',
   'Energy moves between objects.</span></span>.</p>',
   'Energy moves between objects.</span></span>.</p>\n\n      <p><strong>Watch out:</strong> some people think “cold” is a kind of energy that flows. It’s not. Cold just means LESS heat. When ice makes your hand feel cold, YOUR heat is flowing INTO the ice. Try it: be the heat.</p>')
fx('plain', 'no dash; leads into the rod race (Part 2)',
   "The heat from the pan is real — but the mitt slows it down enough that you have time to set the pan down before your hand gets too hot.</p>",
   "The heat from the pan is real, but the mitt slows it down enough that you can set the pan down before your hand gets too hot. Now race some rods and see which materials carry heat fastest.</p>")
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'Part B question 6 label (Gathered Answers)', 'data-label="Explain why an oven mitt protects your hand from a..."', 'data-label="Why an oven mitt protects your hand"')
fx('plain', 'Part B question 7 label (Gathered Answers)', 'data-label="A spoon left in hot soup gets hot. Did the SOUP &quot;g..."', 'data-label="The spoon in hot soup"')

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: Stop & Think (Be the Heat is Part 1’s thinking stop, with the same ice cube)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'removed: the AI picture (it said insulators make heat “stop”, which is wrong; the rod race replaces it), Key Concept, the Stop & Reason about “the three devices above” (a 22.01 leftover), the Four Material Tests tap diagram, Observe & Reason, the trapped-air “Amazing Florida Fact” (not about Florida), the Florida callout (kept as a line in the list), and Go Deeper (it said a spoon gets hot “all the way up in a few seconds”). The misconception paragraph moved to Part 1. Part 3 = the old Explore (the Cup Race); the next button goes to Self-Check',
   r'\s*<p><strong>Common misconception:</strong> Some people think "cold" is a kind of energy\..*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   '\n\n      ' + H3 + 'Part 3 · The Cup Race</h3>\n      ' + PS + 'Which cup keeps warm water warm the longest? Pour the same warm water into a metal cup, a ceramic mug and a foam cup. Then watch the temperatures for 10 minutes.</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its Cup Race is now Part 3; its penguin “Amazing Florida Fact” (Antarctica, not Florida), Think like a scientist and Go Deeper go with it; the coat idea lives in the snow cone bonus)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 5 removed (Bethany kept 6 and 7; Q5 named the removed diagram)', r'<div class="pq">\s*<span class="pq-num"[^>]*>5</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 6 and 7 answered')
fx('cut', 'lean: Part C typed on the page, plus the required sketch', 'A two-column chart with at least 4 conductors and 4 insulators, plus a sentence explaining one item from each column.',
   'My chart: 4 conductors and 4 insulators, plus a sentence explaining one from each side. Plus your labeled sketch.')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether "cold flows" or whether heat moves into the ice, supported with two pieces of evidence.',
   '<strong>Use Your Evidence:</strong> My claim about whether cold flows out of ice, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a 9.01 leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Download your field journal (it has your answers and your sketch) and upload it to the Canvas assignment. Or copy your Gathered Answers (above) into Canvas.', True)

# ---------------------------------------------------------------- the story
SAM = Q['crew']['sam']
D = {
    'lesson': '24.01', 'week': 24, 'day': 1, 'guide': 'sam', 'prefix': 'g4sci-24-1', 'manifestKey': '24-01',
    'paths': P['paths'], 'crew': {'sam': SAM},
    'expedition': {'num': 24, 'title': 'The Cold Cocoa Cart'},
    'ambient': {'icon': '🎆', 'label': 'Parade night'},
    'case': {
        'num': 24, 'title': 'The Cold Cocoa Cart', 'style': 'menu',
        'hook': 'Remember Rosa’s ice cream cart on the boardwalk? In December it sells hot cocoa at the Palmetto Beach Lighted Boat Parade. This year Rosa switched to shiny new metal mugs. Now her order slips are full of complaints. What went wrong?',
        'menu': {'name': 'Rosa’s Cocoa Cart', 'sub': 'Lighted Boat Parade · Saturday, 6 to 9 PM',
                 'items': [{'t': 'Hot cocoa in our NEW shiny metal mug', 'p': '$3'}, {'t': 'Extra marshmallows', 'p': '50¢'}, {'t': 'Peppermint stick', 'p': '25¢'}],
                 'note': 'Tonight: 54°F by the water. Bring a jacket!',
                 'slipsHead': 'Order slips (with notes from customers)',
                 'slips': [{'n': 12, 'time': '7:05 PM', 't': 'My cocoa was cold before the first boat went by!', 'who': 'Mia, age 8'},
                           {'n': 15, 'time': '7:20 PM', 't': 'Ouch! The mug handle was too hot to hold.', 'who': 'Mr. Lopez'},
                           {'n': 21, 'time': '7:40 PM', 't': 'Last year your foam cups kept my cocoa hot all night. What happened?', 'who': 'Grandma Jo'}]},
        'stills': [{'cam': 'REAL PHOTO', 'time': 'A Florida boat parade', 'tag': '📷 PHOTO', 'img': I('boat-parade'), 'kind': 'print',
                    'alt': 'A fishing boat covered in colorful holiday lights, with a lit-up tree and candy canes, sails past at night.'}],
        'stillsCredit': 'Light Boat Parade at John’s Pass, Madeira Beach, Florida: Richard Mc Neil, CC BY 3.0, via Wikimedia Commons.',
        'question': 'Why does Rosa’s cocoa go cold so fast in the new metal mugs, and why do the handles get hot?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'handlemap', 'icon': '🥄', 'where': 'Warm-Up: three spoons in a mug', 't': 'Metal carried the cocoa’s heat all the way up the spoon handle. The wood and plastic handles stayed cool.'},
            {'id': 'heatdots', 'icon': '🔴', 'where': 'The Lesson, Part 1: be the heat', 't': 'Heat moves from the warmer thing to the cooler thing. Hot cocoa gives its heat to the cold night air. Cold never flows in.'},
            {'id': 'rodrace', 'icon': '🧈', 'where': 'The Lesson, Part 2: the butter rod race', 't': 'Metals are conductors: heat moves through them fast. Glass and wood are insulators: they slow heat down.'},
            {'id': 'cuprace', 'icon': '🥤', 'where': 'The Lesson, Part 3: the Cup Race', 't': 'The metal cup cooled the fastest. The foam cup kept its water warm the longest.'},
        ],
        'solve': {
            'title': 'What went wrong at the cocoa cart?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'The cold night air flows into the metal mugs and makes the cocoa cold.', 'why': 'Check Clue 2. Cold doesn’t flow. Heat flows OUT of the cocoa into the cooler air.'},
                {'t': 'Metal is a conductor. It carries the cocoa’s heat out into the cold air and up into the handle. A mug made of an insulator, with a lid, would keep the cocoa hot.', 'right': True,
                 'why': 'Case cracked! Metal moves heat fast, so the cocoa cooled and the handles got hot. Insulators slow heat down.'},
                {'t': 'Metal mugs are just colder than other mugs, even on the same cart.', 'why': 'Check Clue 3. Metal isn’t colder. It moves heat faster, so heat leaves the cocoa faster.'},
                {'t': 'Rosa didn’t make the cocoa hot enough.', 'why': 'Check Clue 4. In the Cup Race, every cup started with the same warm water. The metal one still cooled the fastest.'},
            ]},
    },
    'handlemap': {
        'afterText': 'Touch each one to find out.', 'kicker': 'Warm-Up game', 'title': 'Three spoons in a mug',
        'todo': ['Guess which handle will get warm.', 'Press “Wait 1 minute”.', 'Tap every numbered spot (or drag the 👆 onto it) to feel it.'],
        'model': 'a model', 'predictQ': 'Which handle will feel warm after one minute?',
        'waitBtn': '⏱ Wait 1 minute', 'waitLine': 'Now touch the handles.', 'finger': '👆 Drag me onto a spot, or tap a spot',
        'needPick': 'First, guess which handle will get warm.', 'needWait': 'Press “Wait 1 minute” first, so the heat has time to move.',
        'mapLabel': 'My heat map (spot 1 is near the cocoa, spot 4 is the tip)', 'spotWord': 'spots touched',
        'spoons': [
            {'id': 'metal', 't': 'Metal', 'c': 'metal', 'spots': [
                {'feel': 'hot', 'f': 130, 'icon': '🔥', 'word': 'Hot!', 'note': 'Right by the cocoa, the metal is hot.'},
                {'feel': 'warm', 'f': 108, 'icon': '♨️', 'word': 'Warm', 'note': 'The heat has climbed up the metal.'},
                {'feel': 'warm', 'f': 96, 'icon': '♨️', 'word': 'Warm', 'note': 'Still warm, way up here.'},
                {'feel': 'warm', 'f': 88, 'icon': '♨️', 'word': 'A little warm', 'note': 'Even the tip is a little warm. Metal carried the heat all the way up.'}]},
            {'id': 'wood', 't': 'Wood', 'c': '#B07A43', 'spots': [
                {'feel': 'warm', 'f': 92, 'icon': '♨️', 'word': 'A little warm', 'note': 'Only the part next to the cocoa is warm.'},
                {'feel': 'room', 'f': 76, 'icon': '🙂', 'word': 'Not warm', 'note': 'The heat hardly moved up the wood.'},
                {'feel': 'room', 'f': 73, 'icon': '🙂', 'word': 'Not warm', 'note': 'Cool, like the room.'},
                {'feel': 'room', 'f': 72, 'icon': '🙂', 'word': 'Not warm', 'note': 'Room temperature.'}]},
            {'id': 'plastic', 't': 'Plastic', 'c': '#E4573D', 'spots': [
                {'feel': 'warm', 'f': 90, 'icon': '♨️', 'word': 'A little warm', 'note': 'Only the part next to the cocoa is warm.'},
                {'feel': 'room', 'f': 75, 'icon': '🙂', 'word': 'Not warm', 'note': 'The heat hardly moved up the plastic.'},
                {'feel': 'room', 'f': 73, 'icon': '🙂', 'word': 'Not warm', 'note': 'Cool, like the room.'},
                {'feel': 'room', 'f': 72, 'icon': '🙂', 'word': 'Not warm', 'note': 'Room temperature.'}]}],
        'q': 'Which handle carried the heat the farthest?',
        'opts': [{'t': 'The metal one.', 'ok': True},
                 {'t': 'The wooden one.', 'miss': 'Look at your heat map. Was the wooden tip warm?'},
                 {'t': 'They were all the same.', 'miss': 'Compare spot 4 on each spoon in your heat map.'}],
        'win': 'Metal carried the heat all the way up. Wood and plastic didn’t. Clue 1!'},
    'heatdots': {
        'afterText': 'Try it: be the heat.', 'kicker': 'Part 1 game', 'title': 'Be the heat',
        'todo': ['Drag a 🔴 heat dot from the warmer thing to the cooler thing (or press Send).', 'Try “Send cold”, too.', 'Keep going until they are the same temperature. Then do round 2.'],
        'why': {'icon': '🔴', 'q': 'What are the dots?', 't': 'Each red dot stands for a little bit of heat. More dots means warmer. This is a model.'},
        'model': 'a model', 'sendBtn': 'Send a heat dot →', 'coldBtn': '← Send cold',
        'coldNo': 'Nothing moved. There is no such thing as a “cold dot”. Cold just means LESS heat.',
        'wrongWay': 'That dot bounced back. Heat only moves from the WARMER thing to the COOLER thing.',
        'sameLine': 'Same temperature! Heat stops moving.', 'roundWord': 'rounds done',
        'rounds': [
            {'id': 'ice', 't': '✋ Hand and ice cube', 'line': 'Your hand is warmer than the ice. Drag a heat dot from your hand to the ice, or press Send.',
             'a': {'icon': '✋', 't': 'Warm hand', 'dots': 8, 'base': 32, 'per': 8}, 'b': {'icon': '🧊', 't': 'Ice cube', 'dots': 0, 'base': 32, 'per': 8},
             'done': 'In this model, heat moved from your hand INTO the ice until they matched. That’s why your hand felt cold: it was losing heat. (In real life your body keeps making heat, and the ice melts.)'},
            {'id': 'cocoa', 't': '☕ Cocoa and night air', 'line': 'The cocoa is warmer than the night air. Send its heat dots out.',
             'a': {'icon': '☕', 't': 'Hot cocoa', 'dots': 8, 'base': 54, 'per': 13}, 'b': {'icon': '🌙', 't': 'Cold night air', 'dots': 0, 'base': 54, 'per': 0.25, 'big': 40, 'floor': 0, 'bigNote': 'The night air is HUGE, so the heat dots barely warm it.'},
             'done': 'The cocoa cooled down to the air’s temperature. The air hardly changed. Cold air never flowed IN. Heat flowed OUT.'}],
        'q': 'Which way does heat move?',
        'opts': [{'t': 'From the warmer thing to the cooler thing.', 'ok': True},
                 {'t': 'From the colder thing to the warmer thing.', 'miss': 'Did “Send cold” ever work?'},
                 {'t': 'Both ways at the same time.', 'miss': 'Could you drag a dot from the ice back to the hand?'}],
        'win': 'Heat only moves from warmer to cooler. Cold never flows. Clue 2!'},
    'rodrace': {
        'afterText': 'Now race some rods', 'kicker': 'Part 2 game', 'title': 'The butter rod race',
        'todo': ['Pick 3 rods.', 'Predict: drag each butter dot onto 1st, 2nd or 3rd (or tap it, then a place).', 'Press “Heat the ends” and watch.'],
        'why': {'icon': '🧈', 'q': 'Why butter?', 't': 'Butter melts when it gets warm. A dot of butter at the far end of a rod slides off when the heat reaches it.'},
        'model': 'a model: the real order, sped up', 'pickN': 3, 'maxMin': 10, 'minWord': 'min',
        'pickLine': '1. Pick 3 rods', 'predictLine': '2. Predict: which butter dot falls off first?', 'dropHere': 'drop a butter dot',
        'heatBtn': '🔥 Heat the ends', 'needPick': 'Pick {n} rods first.', 'needPredict': 'Put every butter dot on 1st, 2nd or 3rd first.',
        'tooMany': 'Pick only {n}. Tap one you picked to take it out.', 'never': 'never fell',
        'needMix': 'Race again with at least one metal rod AND one rod that is not metal.',
        'rightLine': 'Your prediction matched!', 'wrongLine': 'Surprise! Look at the order.',
        'stillLine': '{r}: the butter never fell off.',
        'logLabel': 'My races', 'raceWord': 'Race', 'orderWord': 'Butter fell off (in order)', 'predWord': 'My prediction',
        'rods': [{'id': 'copper', 't': 'Copper', 'c': '#C87533', 'kind': 'metal', 'min': 1.0, 'note': 'Copper carried the heat fastest.'},
                 {'id': 'aluminum', 't': 'Aluminum', 'c': '#C9CED3', 'kind': 'metal', 'min': 1.2, 'note': 'Aluminum was close behind.'},
                 {'id': 'steel', 't': 'Steel', 'c': '#8C949C', 'kind': 'metal', 'min': 7.0, 'note': 'Steel carried heat, too, but more slowly.'},
                 {'id': 'glass', 't': 'Glass', 'c': '#BFE3E8', 'kind': 'non', 'min': None, 'note': ''},
                 {'id': 'wood', 't': 'Wood', 'c': '#B07A43', 'kind': 'non', 'min': None, 'note': ''}],
        'q': 'Which rods carried the heat fastest?',
        'opts': [{'t': 'The metal rods. Metals are heat conductors.', 'ok': True},
                 {'t': 'The wood and glass rods.', 'miss': 'Whose butter fell off first?'},
                 {'t': 'They all carried heat the same.', 'miss': 'Look at your race table. Did all the butter fall at once?'}],
        'win': 'Metals carry heat fast (conductors). Glass and wood slow it down (insulators). Clue 3!'},
    'cuprace': {
        'afterText': 'for 10 minutes', 'kicker': 'Part 3 game', 'title': 'The Cup Race',
        'todo': ['Tap the cup you think stays warmest.', 'Press Start and watch the graph.', 'Then rank the cups.'],
        'why': {'icon': '📈', 'q': 'How do I read the graph?', 't': 'Each line is one cup. The higher the line, the warmer the water. A line that drops fast means the cup lost heat fast.'},
        'model': 'a model', 'start': 110, 'room': 72, 'mins': 10, 'xLabel': 'minutes',
        'cups': [{'id': 'metal', 't': 'Metal cup', 'icon': '🥫', 'c': '#5B6570', 'k': 0.045},
                 {'id': 'ceramic', 't': 'Ceramic mug', 'icon': '☕', 'c': '#C8553D', 'k': 0.035},
                 {'id': 'foam', 't': 'Foam cup', 'icon': '🥤', 'c': '#2D7AA6', 'k': 0.02}],
        'predictQ': 'Which cup will keep the water warm the longest? Tap one.', 'runBtn': '▶ Start the 10-minute race', 'againBtn': '↺ Run it again',
        'needPredict': 'Predict first: tap the cup you think stays warmest.', 'rightPre': 'You predicted it! ', 'wrongPre': 'Surprise! ', 'bestLine': '{c} stayed warmest.',
        'rankLine': 'Rank the cups: drag each one onto a place (or tap it, then a place).', 'ranks': ['🔥 Warmest', 'Middle', '❄️ Coolest'],
        'rankMiss': 'Look at the graph again. Where did the {c} line end?',
        'q': 'Which cup is the best insulator?',
        'opts': [{'t': 'The foam cup.', 'ok': True},
                 {'t': 'The metal cup.', 'miss': 'Look at the graph. Whose line dropped fastest?'},
                 {'t': 'The ceramic mug.', 'miss': 'Close! But whose line stayed highest?'}],
        'win': 'The foam cup slowed the heat the most. The metal cup let it out fastest. Clue 4!'},
    'exploreMod': 'cuprace',
    'iceblocks': {
        'after': 'cuprace', 'kicker': 'Wow!', 'title': 'Ice on two blocks',
        'todo': ['Touch both blocks.', 'Check them with a thermometer.', 'Predict, then drop the ice cubes.'],
        'model': 'a model', 'room': 72, 'mins': 10,
        'blocks': [{'id': 'al', 't': 'Aluminum block', 'c': '#C9CED3', 'feel': 'Brrr! It feels COLD.', 'cold': True, 'melt': 2.5},
                   {'id': 'pl', 't': 'Plastic block', 'c': '#E4573D', 'feel': 'It feels about normal.', 'melt': 25}],
        'touchBtn': '✋ Touch it', 'thermoBtn': '🌡 Check both with a thermometer',
        'sameLine': 'Both blocks are 72°F!', 'sameWhy': 'They sat in the same room, so they are the same temperature. The metal only FELT colder.',
        'predictQ': 'Put an ice cube on each block. Which ice cube melts first?', 'dropBtn': '🧊 Drop the ice cubes',
        'needPredict': 'Predict first: which ice cube melts first?', 'rightPre': 'You called it! ', 'wrongPre': 'Surprise! ', 'fastLine': 'The ice on the {b} melted first.',
        'whyLine': 'Metal is a conductor, so it carries the room’s heat into the ice fast. That’s also why it felt cold: it carried YOUR heat away from your hand fast. The plastic slowed the heat down, so its ice is still there.',
        'done': 'Wow! The block that feels coldest melts ice the fastest.'},
    'mugdesign': {
        'after': '.fs-solve', 'kicker': 'Case closed · Rosa’s new mug', 'title': 'Design Rosa’s new mug',
        'todo': ['Pick the mug, a lid and the handle.', 'Run the 30-minute parade test.', 'Keep changing things until it gets the APPROVED stamp.'],
        'lockLine': 'Crack the case first.',
        'why': {'icon': '☕', 'q': 'What makes a good parade mug?', 't': 'After 30 minutes in 54°F air, the cocoa should still be hot (120°F or more), and the handle must be safe to hold.'},
        'model': 'a model', 'start': 160, 'air': 54, 'mins': 30, 'need': 120,
        'walls': [{'id': 'steel', 't': 'Thin metal mug', 'icon': '🥫', 'k': 0.03, 'lidK': 0.02, 'metal': True},
                  {'id': 'ceramic', 't': 'Ceramic mug', 'icon': '☕', 'k': 0.022, 'lidK': 0.014},
                  {'id': 'double', 't': 'Two-wall mug (air between the walls)', 'icon': '🍵', 'k': 0.015, 'lidK': 0.008},
                  {'id': 'foam', 't': 'Foam cup', 'icon': '🥤', 'k': 0.015, 'lidK': 0.009}],
        'lids': [{'id': 'none', 't': 'No lid'}, {'id': 'lid', 't': 'A lid'}],
        'handles': [{'id': 'metal', 't': 'Metal handle', 'metal': True}, {'id': 'wood', 't': 'Wooden handle'}, {'id': 'plastic', 't': 'Plastic handle'}],
        'wallLabel': '1. The mug', 'lidLabel': '2. A lid?', 'handleLabel': '3. The handle',
        'runBtn': '🎆 Run the 30-minute parade test', 'needAll': 'Pick a mug, a lid choice and a handle first.', 'afterWord': 'After 30 minutes: ',
        'hotWord': 'Still hot!', 'coldLine': 'Too cool to enjoy.', 'burnLine': 'The metal handle on a metal mug got too hot to hold!',
        'passLine': 'APPROVED for the parade!', 'tryLine': 'Change one thing and test again.', 'stamp': 'APPROVED',
        'cols': ['Mug', 'Lid', 'Handle', 'Cocoa at 30 min', 'Result'], 'logLabel': 'My tests',
        'win': 'Rosa’s new mug keeps the cocoa hot AND is safe to hold. Insulators win!'},
    'snowcoat': {
        'after': '.fs-solve', 'kicker': 'Bonus · wild card', 'title': 'The coat on the snow cone',
        'todo': ['Guess which snow cone melts FIRST.', 'Put them in the sun.', 'Read why.'],
        'lockLine': 'Crack the case first.', 'model': 'a model: a hot afternoon at Palmetto Beach', 'mins': 60,
        'wraps': [{'id': 'none', 't': 'No wrap', 'icon': '☀️', 'melt': 12}, {'id': 'napkin', 't': 'Paper napkin', 'icon': '🧻', 'melt': 16},
                  {'id': 'scarf', 't': 'Wool scarf', 'icon': '🧣', 'melt': 35}, {'id': 'coat', 't': 'Puffy coat', 'icon': '🧥', 'melt': 60}],
        'guessQ': 'Four snow cones sit in the hot beach sun. Which one melts FIRST?', 'runBtn': '☀️ Into the sun!', 'needGuess': 'Guess first: which one melts FIRST?',
        'meltedWord': 'melted!', 'frozenWord': 'still frozen',
        'rightPre': 'You called it!', 'wrongPre': 'Surprise! The coat didn’t warm it up.',
        'whyLine': ' The puffy coat kept its snow cone frozen the LONGEST. A coat doesn’t make heat. Its trapped air slows heat down, so the beach’s heat gets IN slowly. In winter, a coat slows YOUR heat from getting OUT.',
        'win': 'Coats don’t make heat. They slow it down!'},
    'fold': {'snowcoat': {'icon': '🧥', 'tease': 'Wrap a snow cone in a puffy coat and set it in the sun. What happens?', 'open': 'Play'}},
    'tool': {
        'name': 'Infrared thermometer', 'icon': '🌡️', 'kicker': 'Bonus · Tool of the Week', 'teaser': 'Read a temperature without touching anything.',
        'key': '24-tool', 'sim': 'irtherm', 'after': '#tab-assignment .activity-card',
        'why': {'icon': '🔴', 'q': 'What is an infrared thermometer?', 't': 'Every warm thing gives off invisible light called infrared. This tool catches that light and shows the temperature, without touching. The red dot is just for aiming.'},
        'done': 'You measured without touching!',
        'irtherm': {
            'kicker': 'Try it: an infrared thermometer', 'title': 'Aim, pull, read',
            'todo': ['Drag the red dot onto something in the photo (or tap a dashed circle).', 'Pull the trigger and read the screen.', 'Try both photos. On the shiny mug, try the tape trick.'],
            'photo': {'img': I('ir-thermometer'), 'alt': 'A hand holding a real infrared thermometer. Its screen reads 28.5 degrees Celsius.', 'cap': 'A real infrared thermometer. Photo: Cjp24, CC BY-SA 3.0, via Wikimedia Commons.'},
            'trigger': '🔫 Pull the trigger', 'tapeBtn': '🩹 Stick tape on the shiny mug', 'radius': 10,
            'missLine': 'Aim the red dot right on something first.',
            'shinyLine': 'That can’t be right! The mug was just in hot water. Shiny metal acts like a mirror, so the thermometer reads mostly the light bouncing off it. Scientists stick tape on shiny metal. Press the tape button.',
            'tapeLine': 'Tape on! Aim at the tape and pull the trigger again.',
            'logLabel': 'My readings', 'whatWord': 'Aimed at', 'readWord': 'Reading', 'tapeWord': 'With tape',
            'scenes': [
                {'id': 'bench', 't': '🪑 A park bench on a sunny morning', 'img': I('bench'), 'alt': 'A park bench in the sun with a wooden seat and dark iron armrests and legs, on green grass.',
                 'credit': 'Bench: Acabashi, CC BY-SA 4.0, via Wikimedia Commons.',
                 'spots': [{'id': 'seat', 'x': 50, 'y': 44, 't': 'Wooden seat', 'f': 95, 'note': 'Warm from the sun.'},
                           {'id': 'arm', 'x': 80, 'y': 52, 't': 'Iron armrest', 'f': 98, 'note': 'Almost the same as the wood! But touch it, and the iron feels much hotter.'},
                           {'id': 'grass', 'x': 22, 'y': 86, 't': 'Grass', 'f': 80, 'note': 'Grass stays cooler than the bench.'}]},
                {'id': 'mug', 't': '🥫 A shiny metal mug, just washed in hot water', 'img': I('steel-mug'), 'alt': 'A shiny steel mug with a black plastic handle.',
                 'credit': 'Mug: Qurren, CC BY-SA 4.0, via Wikimedia Commons (logo blurred).',
                 'spots': [{'id': 'side', 'x': 35, 'y': 55, 't': 'Shiny metal side', 'f': 79, 'shiny': True, 'tapeF': 118, 'tapeNote': 'With tape on it: 118°F. That’s the real temperature of the hot mug.'},
                           {'id': 'handle', 'x': 89, 'y': 50, 't': 'Black plastic handle', 'f': 108, 'note': 'Dull, dark things are easy for this tool to read.'}]}],
            'q': {'q': 'The iron armrest and the wooden seat read almost the same. Why does the iron FEEL hotter?',
                  'opts': [{'t': 'Iron is a conductor, so it moves heat into your hand much faster.', 'ok': True, 'why': 'Right! A metal slide in the sun burns for the same reason: it pours heat into your skin fast.'},
                           {'t': 'The iron is much hotter than the wood.', 'why': 'Check your readings: 98°F and 95°F are close.'},
                           {'t': 'The thermometer is broken.', 'why': 'It read the shiny mug right once the tape was on.'}]}}},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'B': 'Think about Be the Heat. Which way did the heat dots move?', 'C': 'Think about Be the Heat. Could a dot go back from the ice to the hand?'},
        'q2': {'A': 'Think about the rod race. Did the wood rod’s butter ever fall off?', 'C': 'Think about the Cup Race. The foam cup kept heat IN.'},
        'q3': {'A': 'Think about the spoon test. The metal handle got hot.', 'B': 'Insulators only SLOW heat down. They don’t stop all of it.'}},
    'flags': {
        'ans-2': [
            {'label': 'uses HEAT', 're': 'heat|hot'},
            {'label': 'uses TRANSFER', 're': 'transf|tranf|trasf|tansf|transfur'},
            {'label': 'uses INSULATOR', 're': 'insul|insol|insal|insual|inslu'}],
        'ans-3': [
            {'label': 'the soup gave heat', 're': 'heat|warm|hot|energy'},
            {'label': 'uses TRANSFER', 're': 'transf|tranf|trasf|tansf|transfur'},
            {'label': 'from the soup to the spoon', 're': 'soup.{0,40}spoon|spoon.{0,40}soup|from the soup|into the spoon|to the spoon'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|cold does|cold doesn|isn|is not|heat'},
            {'label': 'two pieces of evidence', 'any': ['dot', 'send', 'hand', 'ice', 'melt', 'metal', 'block', 'aluminum', 'plastic', 'thermometer', 'same', 'spoon', 'rod', 'butter', 'cup', 'graph', 'flow', 'warmer', 'cooler'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-2': 15, 'ans-3': 15, 'cer-4': 30},
    'hints': {
        'ans-2': ['Which way does the heat move: from the pan to your hand, or from your hand to the pan?', 'What does an insulator do to heat?', 'Try: The heat from the pan wants to ___. The mitt is an INSULATOR, so it ___ the heat TRANSFER.'],
        'ans-3': ['Which was warmer at first, the soup or the spoon?', 'Think about the spoon test: what climbed up the metal handle?', 'Try: Yes, the soup gave ___ to the spoon. Heat TRANSFERS from ___ to ___.'],
        'cer-4': ['First decide: does cold really flow?', 'Think about Be the Heat and the ice on the metal block.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'In Be the Heat, heat dots only moved from the warm hand into the ice. “Send cold” never worked.',
                'The ice melted fastest on the metal block, because the metal carried heat into the ice.',
                'The metal block felt cold, but the thermometer showed it was the same temperature as the plastic.',
                'Ice is cold, so it must send cold into your hand.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · the cold cocoa cart', 'length': '20–30 s'},
        'warmup': {'label': 'Warm-Up · three spoons in a mug (Clue 1)', 'length': '15–20 s',
                   'script': 'Sam here, at Rosa’s cocoa cart. Read the menu and the order slips first. Then, the spoon test! Guess which handle gets warm, press Wait, then touch every spot.'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Rub your hands together for “heat”.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · be the heat (Clue 2)', 'length': '15–20 s',
                  'script': 'Does cold really flow? Let’s test it. Drag a heat dot from the warm hand to the ice cube. Now try Send cold. Keep going until both are the same temperature.'},
        'part2': {'label': 'Part 2 · the butter rod race (Clue 3)', 'length': '20–30 s'},
        'explore': {'label': 'Part 3 · the Cup Race (Clue 4)', 'length': '15–20 s',
                    'script': 'Cup Race time! First, tap the cup you think stays warmest. Press Start, and watch the lines on the graph. Then rank the cups, warmest to coolest.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · my conductor and insulator chart', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '15–20 s',
                     'script': 'A classmate says cold flows out of ice into your hand. True? Think about the heat dots, and the ice on the metal block. Pick your side, tap two facts, then explain. That’s your C-E-R.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 24.02 (energy changes).'},
    },
    'videoOff': [],
    'lensVoice': False,
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Rosa’s menu and the order slips (Warm-Up)',
        'Your spoon heat map (Warm-Up)',
        'A butter dot falling off a rod (The Lesson)',
        'The Cup Race graph (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['A pot on a stove', 'A mug of cocoa', 'An oven mitt'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch and label one thing from your chart', 'required': True, 'minLabels': 3,
                           'prompts': ['Draw a pot, a mug or a pan', 'Label the conductor part and the insulator part', 'Draw an arrow where the heat flows']}]},
    'hlCoach': copy.deepcopy(O['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🧾', 'name': 'Order slip #15',
                 'line': 'You cracked Case 24, and Mr. Lopez’s order slip goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next time: tracking energy as it changes.'},
    'notebookTitle': 'Unit 5 · Energy, Motion & Collisions',
    'notebook': copy.deepcopy(O['notebook']),
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. Nice and toasty!',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to see what it means.']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '#tab-vocab p', 'text': 'What hot and cold things did you touch?'},
         'label': 'Warm-Up: hot and cold things I touched', 'q': 'Warm-Up: Three hot or cold things I touched today, and what they felt like.', 'title': 'Hot and cold things I touched', 'compact': True,
         'fields': [{'t': 'Thing 1', 'icon': '🔥', 'ph': 'I touched ___. It felt ___.'},
                    {'t': 'Thing 2', 'icon': '❄️', 'ph': 'I touched ___. It felt ___.'},
                    {'t': 'Thing 3', 'icon': '🥄', 'ph': 'I touched ___. It felt ___.'}]},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Fill in your chart below'},
         'label': 'Part C: My conductor and insulator chart', 'q': 'Part C: My conductor and insulator chart (4 conductors, 4 insulators, one of each explained)', 'title': 'My conductor and insulator chart',
         'fields': [{'t': '4 conductors (heat moves through them fast)', 'icon': '🥄', 'ph': '1. ___ 2. ___ 3. ___ 4. ___'},
                    {'t': '4 insulators (they slow heat down)', 'icon': '🧤', 'ph': '1. ___ 2. ___ 3. ___ 4. ___'},
                    {'t': 'One conductor and why we use it', 'icon': '🍳', 'ph': 'A ___ is made of ___, so heat ___.'},
                    {'t': 'One insulator and why we use it', 'icon': '🧥', 'ph': 'A ___ is made of ___, so it slows heat ___.', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Does cold flow out of ice into your hand?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-2': 'Part B · Question 6', 'ans-3': 'Part B · Question 7', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] == '24.01': n.update({'icon': '🧾', 'name': 'Order slip #15'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'Heat always moves from a warmer object to a cooler one, and insulators slow it down.',
    'key': ['heat', 'warmer', 'cooler', 'insulators', 'slow'],
    'small': ['always', 'from', 'a', 'to', 'one', 'and', 'it', 'down'],
    'model': 'A scientist might highlight “heat”, “warmer”, “cooler” and “insulators slow”. Those words hold the big idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me explain which way heat moves, or why metal feels cold and wood doesn’t?']

EV = '#tab-assignment .act-body > div:has(> .fs-plan)'
D['cues'] = {
    'warmup': [{'at': '^menu', 'sel': '.fs-menu-board', 'fx': 'glow', 'scroll': True},
               {'at': '^slips', 'sel': '.fs-slip-row', 'fx': 'pop'},
               {'at': '^guess', 'sel': '.fs-hm-pq', 'fx': 'pop', 'scroll': True},
               {'at': '^wait', 'sel': '.fs-hm-wait', 'fx': 'point'},
               {'at': '^spot', 'sel': '.fs-hm-spot', 'all': True, 'fx': 'wiggle'}],
    'part1': [{'at': '^dot', 'sel': '.fs-hdt-dot', 'i': 0, 'fx': 'point', 'scroll': True},
              {'at': '^ice', 'sel': '.fs-hdt-box.s-b', 'fx': 'glow'},
              {'at': '^cold', 'sel': '.fs-hdt-cold', 'fx': 'point'},
              {'at': '^temperature', 'sel': '.fs-hdt-temp', 'all': True, 'fx': 'pop'}],
    'explore': [{'at': '^cup', 'sel': '.fs-cup-pq', 'fx': 'pop', 'scroll': True},
                {'at': '^start', 'sel': '.fs-cup-run', 'fx': 'point'},
                {'at': '^graph', 'sel': '.fs-cup-svg', 'fx': 'glow'},
                {'at': '^rank', 'sel': '.fs-cup-rank', 'fx': 'glow'}],
    'evidence': [{'at': '^classmate', 'sel': EV + ' > p', 'i': 0, 'fx': 'trace', 'scroll': True},
                 {'at': '^dots', 'sel': '.fs-plan .fs-opt', 'i': 2, 'fx': 'glow'},
                 {'at': '^block', 'sel': '.fs-plan .fs-opt', 'i': 3, 'fx': 'glow'},
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
