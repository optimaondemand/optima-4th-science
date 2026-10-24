#!/usr/bin/env python3
"""Writes data.json and fixes.json for 20.01 (run from this folder). Case 20 "9:41 PM" (Sam Park, the Palmetto Beach pier).
New modules: rateit (feel it, rate it: rub hands / hum / look at a light, slider + where did it go), blockpath (tap the gap, drag a
blocker into it), heatflow (iced lemonade on a hot porch: pick the arrow, wait an hour, then name the way for 4 Florida scenes),
stormwatch (real Kennedy Space Center lightning: tap at the flash, tap at the boom, seconds into miles), case.strip (a data-logger
strip chart), bulletin skin:'radio' + tone:'squelch' (the night guard's radio call, folded), SIMS.circuittester (Tool of the Week)."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../18-01/data.json', encoding='utf-8'))
O = json.load(open('../19-02/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
PS = '<p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)
def I(n): return 'images/20-01-' + n + '.jpg'

# ---------------------------------------------------------------- ticked fixes (Bethany, 24 Oct 2026)
fx('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist already asks for a four-row energy chart',
   '🎨 Part C &mdash; Build Your Own Food Chain', '🔎 Part C &mdash; My Energy Hunt')
fx('fix', 'copy-paste leftover: Part C task from 9.01 (now the four-row energy hunt, typed on the page)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Find one example of each way energy moves at home or at school. For each one, name the source, the receiver and your evidence that energy moved.</p>', True)
fx('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'unit label: “Ecosystems & Energy” is a leftover; weeks 18–24 are Unit 5', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Energy, Motion &amp; Collisions</div>')
fx('fix', 'energy transfer is physical science, not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standard: 4-PS3-2 is “energy can be transferred by sound, light, heat and electric currents” (4-ESS3-1 is about energy resources)',
   '<div class="info-value">4-ESS3-1 · TEKS 4.8(B), 4.8(C)</div>', '<div class="info-value">4-PS3-2 · TEKS 4.8(B), 4.8(C)</div>')
fx('fix', 'contradiction: the box said electricity “can’t jump through the air”, then the page featured lightning. Plain, true version; the box is trimmed (lean)',
   r'<p style="font-size:15px;color:#5A4D3E;line-height:1.65;margin:0 0 10px;">Electrical energy needs a path to travel.*?</p>\s*<p[^>]*>Not every material.*?</p>\s*<p[^>]*>Think about the lamp.*?</p>',
   '<p style="font-size:15px;color:#5A4D3E;line-height:1.65;margin:0 0 10px;">Electrical energy needs a path of metal, like a wire. That path is called a <strong>circuit</strong>. If the path is broken, no energy flows.</p>\n'
   '        <p style="font-size:15px;color:#5A4D3E;line-height:1.65;margin:0 0 10px;">Materials that let electricity flow easily, like copper, aluminum and steel, are called <strong>conductors</strong>. That’s why wires are made of metal! Materials that block it, like rubber, plastic and glass, are called <strong>insulators</strong>. The plastic coating on a power cord keeps the electricity safely inside the wire.</p>\n'
   '        <p style="font-size:15px;color:#5A4D3E;line-height:1.65;margin:0;">Air usually blocks electricity, too. Lightning is the giant exception: its push is so strong that it forces a path right through the air.</p>', True)
fx('fix', 'the four-panel AI picture and the Key Concept that leans on it are gone; Which way does heat go? replaces them and the tap diagram',
   r'<div class="lesson-figure scroll-reveal">\s*<div class="lesson-figure-label">🔥 Four Ways Energy Moves Around You</div>.*?(?=<div style="background:#EAF8FD;)', '', True)
fx('fix', 'the tap diagram (its 4 Florida scenes are now the cards in Which way does heat go?), Stop & Reason, Observe & Reason, the muddy Sun-and-heat fact, the Florida lightning callout (the checked number now lives in Storm watch) and Go Deeper are gone (lean). Part 4 = Storm watch (the old Explore); next button goes to Self-Check',
   r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 4 · Storm Watch</h3>\n      ' + PS + 'A summer storm is rolling toward Palmetto Beach. When you see a flash, start counting. When you hear the boom, stop. What does the gap tell you?</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; plain words; no dash',
   "Hold this question in your head as you work. By the end of the lesson, you'll be able to name four ways energy moves between places — and spot the source and the receiver in any everyday example.",
   "Keep this question in mind. By the end, you’ll name four ways energy moves and find the source and the receiver every time.")
fx('plain', 'the warm-up now starts with the student as the source; the list stays (typed on the page)',
   r'<p>Sit still for a moment\. Look around the room\..*?</p>',
   '<p>Today YOU are the energy source. Try each move in the game below for real. Then list three places where energy is moving around you <em>right now</em>.</p>', True)
fx('plain', 'no dash', 'Heat, light, sound, electrical — each with a source and a receiver', 'Heat, light, sound and electrical, each with a source and a receiver')
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', 'no dash', "Energy doesn't just exist — it MOVES.", "Energy doesn't just sit there. It MOVES.")
fx('plain', 'receiver gets its own meaning in context',
   '(where the energy came from) and a receiver (where the energy went).', '(where the energy comes from) and a <strong>receiver</strong> (where the energy goes).')
fx('plain', 'plain, no dash', "There are four big forms you'll see every day — even in a regular Florida classroom:", "There are four big ways you'll see every day, even in a Florida classroom:")
fx('plain', 'no dash; shorter',
   "A warmed cup, a lit-up room, a vibrating eardrum, a glowing bulb — all are evidence that energy traveled from a source to a receiver.",
   "A warmed cup, a lit-up room, a shaking eardrum, a glowing bulb: each one is evidence that energy traveled from a source to a receiver.")
fx('plain', 'misconception kept, plain, no dash',
   r'<p><strong>Common misconception:</strong> Some people think these are four different KINDS of energy.*?</p>',
   '<p><strong>Watch out:</strong> Some people think these are four different KINDS of energy, like four flavors. They are really four different WAYS energy can travel.</p>', True)
fx('plain', 'no dash, no “&”', '⚡ Conductors, Insulators & Simple Circuits', '⚡ Paths for Electricity')
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'no dash', '"Energy can\'t actually move through the air — you have to TOUCH things to transfer energy."',
   '“Energy can’t really move through the air. You have to TOUCH things to transfer energy.”')
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'shorter closing; points to 20.02',
   r'<p><strong>Nicely done\.</strong> You can now spot four ways.*?</p>',
   '<p><strong>Nicely done.</strong> You found four ways energy moves and proved it moved, even through the air. Next time, you set up energy stations and collect your own evidence.</p>', True)

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: Stop & Think (Block the path is the thinking stop for Part 1)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (the home hunt moves to Part C; Part 4 is Storm watch; its whale fact, hummingbird question and conductor Go Deeper go too)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 5 removed (Bethany kept 6 and 7; it pointed at the removed diagram)', r'<div class="pq">\s*<span class="pq-num"[^>]*>5</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: renumber Part B (6 → 5)', '<span class="pq-num" style="background:#D4772C;">6</span>', '<span class="pq-num" style="background:#D4772C;">5</span>')
fx('cut', 'lean: renumber Part B (7 → 6)', '<span class="pq-num" style="background:#D4772C;">7</span>', '<span class="pq-num" style="background:#D4772C;">6</span>')
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C typed on the page',
   'A four-row chart showing one Florida example for each form (heat / light / sound / electrical) with source, receiver, and evidence.',
   'One example each of heat, light, sound and electrical energy, with the source, the receiver and my evidence. (A sketch is a bonus.)')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether touch is required for energy transfer, and supported it with two pieces of evidence.',
   '<strong>Use Your Evidence:</strong> My claim about whether energy needs touch to move, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', True)

# ---------------------------------------------------------------- the story
SAM = Q['crew']['sam']
FORMS = {'heat': ('🔥', 'Heat', '#E8636B'), 'light': ('💡', 'Light', '#D99A00'), 'sound': ('🔊', 'Sound', '#3D5A99'), 'elec': ('⚡', 'Electrical', '#7A4FC0')}
D = {
    'lesson': '20.01', 'week': 20, 'day': 1, 'guide': 'sam', 'prefix': 'g4sci-20-1', 'manifestKey': '20-01',
    'paths': P['paths'], 'crew': {'sam': SAM},
    'expedition': {'num': 20, 'title': '9:41 PM'},
    'ambient': {'icon': '🌧️', 'label': 'Rain sounds'},
    'case': {
        'num': 20, 'title': '9:41 PM', 'style': 'strip',
        'hook': 'I put four sensors on the Palmetto Beach pier to watch a summer storm. (A sensor is a tool that measures something and records it.) At 9:41 PM, all four jumped at the same moment, and the pier lamp went dark.',
        'strip': {'head': 'PIER DATA LOGGER · STATION 3', 'sub': 'Friday night · one reading per minute', 'markLabel': '9:41 PM', 'mark': 6, 'every': 2,
                  'alt': 'A strip chart with four lines from 9:35 to 9:47 PM. At 9:41 the light, sound and heat lines all spike, and the power line to the pier lamp drops to zero.',
                  'times': ['9:35', '9:36', '9:37', '9:38', '9:39', '9:40', '9:41', '9:42', '9:43', '9:44', '9:45', '9:46', '9:47'],
                  'traces': [
                      {'icon': '💡', 't': 'Light', 'sub': 'how bright it is', 'c': '#D99A00', 'vals': [.3, .32, .3, .31, .3, .32, 1, .05, .06, .05, .05, .06, .05]},
                      {'icon': '🔊', 't': 'Sound', 'sub': 'how loud it is', 'c': '#3D5A99', 'vals': [.25, .3, .22, .28, .26, .3, 1, .3, .24, .28, .22, .26, .24]},
                      {'icon': '🌡️', 't': 'Heat', 'sub': 'sensor on the lamp post', 'c': '#E8636B', 'vals': [.2, .2, .2, .2, .2, .2, .95, .7, .5, .38, .3, .25, .22]},
                      {'icon': '🔌', 't': 'Power', 'sub': 'to the pier lamp', 'c': '#7A4FC0', 'vals': [.75, .75, .75, .75, .75, .75, .9, 0, 0, 0, 0, 0, 0]}],
                  'note': 'Nobody was on the pier. Nobody touched the lamp post. So how did energy reach all four sensors at once? (Sam)'},
        'stills': [],
        'question': 'What happened on the pier at 9:41 PM, when nobody was there?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'rateit', 'icon': '🙌', 'where': 'Warm-Up: feel it, rate it', 't': 'You were the source three times. Each time, you knew energy moved because the receiver CHANGED: it warmed up, buzzed or squinted. A spike on a sensor is a receiver changing too.'},
            {'id': 'blockpath', 'icon': '🚧', 'where': 'The Lesson, Part 1: block the path', 't': 'Heat, light and sound crossed empty air with nothing touching. Electricity needed a path, and plastic in the wire stopped it.'},
            {'id': 'heatflow', 'icon': '🌡️', 'where': 'The Lesson, Part 2: which way does heat go?', 't': 'Heat always moves from warmer to cooler. And lightning is a giant electric current that rushes from a cloud into whatever it hits.'},
            {'id': 'stormwatch', 'icon': '⚡', 'where': 'The Lesson, Part 4: storm watch', 't': 'Light arrives first and sound comes later. The shorter the gap, the closer the strike. At 9:41 the boom came only a split second after the flash.'},
        ],
        'solve': {
            'title': 'What happened at 9:41 PM?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Someone sneaked onto the pier and switched off the lamp.', 'why': 'Check the note and Clue 2. Nobody was there, and energy can cross the air without anyone touching anything.'},
                {'t': 'Cold storm air moved into the lamp post and froze the lamp.', 'why': 'Check Clue 3. Cold doesn’t travel, heat does. And the heat line went UP.'},
                {'t': 'Lightning struck the metal lamp post, right at the pier. Its electrical energy rushed down the post and burned out the lamp, and the bolt sent light, sound and heat through the air to every sensor.', 'right': True,
                 'why': 'Case cracked! The flash, the boom a split second later, the hot post and the dead lamp all point to a lightning strike right at the pier. Sam is putting up a lightning rod (a metal rod that gives lightning a safe path into the ground).'},
                {'t': 'A big wave crashed over the sensors.', 'why': 'Check Clues 1 and 4. Can a wave make a bright flash and a heat spike?'},
            ]},
    },
    'rateit': {
        'afterText': 'Today YOU are the energy source', 'kicker': 'Warm-Up game', 'title': 'Feel it, rate it',
        'todo': ['Pick a move and really do it.', 'Slide the meter: how much did the receiver change?', 'Then pick where the energy went. Do all 3 moves.'],
        'why': {'icon': '🙌', 'q': 'What is a receiver?', 't': 'The place the energy goes. You can’t see energy fly by, but you can feel or see the receiver change.'},
        'doneBtn': 'I did it!', 'zeroLine': 'Nothing yet? Try it again a little longer, then slide the meter.',
        'scale': ['😐 Nothing', '🙂 A little', '😮 Some', '🤩 A lot'], 'tallyLabel': 'Energy you sent',
        'moves': [
            {'id': 'rub', 'icon': '🙌', 't': 'Rub your hands', 'do': 'Rub your palms together fast for 10 seconds. Then press them gently on your cheeks.',
             'rate': 'How much did your cheeks warm up?', 'recQ': 'Where did the heat go?',
             'recs': [{'t': 'Into my cheeks', 'ok': True}, {'t': 'Into the ceiling', 'miss': 'What did you FEEL warm up?'},
                      {'t': 'Nowhere. It disappeared.', 'miss': 'Energy doesn’t disappear. Something got warmer. What was it?'}],
             'form': 'Heat', 'formIcon': '🔥', 'path': 'palms → cheeks', 'why': 'Rubbing made your palms warm. Then heat moved from your warm palms into your cooler cheeks.'},
            {'id': 'hum', 'icon': '🎵', 't': 'Hum', 'do': 'Put your fingertips gently on the front of your throat. Hum one long note.',
             'rate': 'How much buzz did your fingertips feel?', 'recQ': 'Where did the sound energy go?',
             'recs': [{'t': 'Into my fingertips and my ears', 'ok': True}, {'t': 'It stayed inside my throat', 'miss': 'Did your fingertips feel it? Could you hear it?'},
                      {'t': 'Into the lights', 'miss': 'Sound is shaking. What shook, besides your throat?'}],
             'form': 'Sound', 'formIcon': '🔊', 'path': 'voice → fingertips and ears', 'why': 'Your voice box shook (vibrated). The shaking traveled into your fingertips and through the air to your ears.'},
            {'id': 'look', 'icon': '👀', 't': 'Look at a light', 'do': 'Cover your eyes with your hands for 10 seconds. Then uncover them and look toward a window or a lamp. (Never look at the Sun.)',
             'rate': 'How bright did it seem when you uncovered your eyes?', 'recQ': 'Where did the light energy go?',
             'recs': [{'t': 'Into my eyes', 'ok': True}, {'t': 'Into my hands', 'miss': 'Your hands were in the way. What happened when you moved them?'},
                      {'t': 'It went nowhere', 'miss': 'It seemed bright! What part of you did the light reach?'}],
             'form': 'Light', 'formIcon': '💡', 'path': 'window or lamp → eyes', 'why': 'Light traveled across the room into your eyes. Your eyes changed: you squinted, and the dark centers of your eyes got smaller.'}],
        'q': 'How did you know energy moved each time?',
        'opts': [{'t': 'Something at the other end changed. It warmed up, buzzed or squinted.', 'ok': True},
                 {'t': 'I saw the energy flying through the air.', 'miss': 'You can’t see heat or sound flying by. What changed instead?'},
                 {'t': 'The page told me.', 'miss': 'You felt it yourself! What changed in your cheeks, fingertips and eyes?'}],
        'win': 'You were the source three times, and a receiver changed every time. Clue 1!'},
    'blockpath': {
        'afterText': 'In every transfer', 'kicker': 'Part 1 game', 'title': 'Block the path',
        'todo': ['Tap each gap. What is between the source and the receiver?', 'Drag a blocker into the gap (or tap a blocker, then the gap).', 'Watch the receiver. Did it stop changing?'],
        'why': {'icon': '🚧', 'q': 'Why block it?', 't': 'If blocking the gap stops the change, then energy really was traveling through that gap.'},
        'gapBtn': 'Tap the gap', 'tapFirst': 'First tap the gap. What is in there, between the source and the receiver?',
        'trayLabel': 'Blockers (drag one into a gap, or tap it and then a gap)',
        'blockers': [{'k': 'board', 'icon': '🪵', 't': 'Wooden board'}, {'k': 'umbrella', 'icon': '☂️', 't': 'Umbrella'},
                     {'k': 'earmuffs', 'icon': '🎧', 't': 'Earmuffs'}, {'k': 'plastic', 'icon': '🧩', 't': 'Plastic piece'}],
        'scenes': [
            {'id': 'fire', 'form': 'Heat', 'formIcon': '🔥', 'c': '#E8636B', 'fx': 'warm', 'src': {'icon': '🔥', 't': 'Campfire'}, 'rec': {'icon': '🙌', 't': 'Your hands'},
             'gap': 'Only air! The fire never touches your hands, but they still get warm.', 'on': 'Your hands are warming up.',
             'off': 'Your hands cool down. So the heat WAS crossing the air.', 'ok': ['board'],
             'miss': {'umbrella': 'Never hold an umbrella near a fire! Try something solid and thick.', 'earmuffs': 'Earmuffs block sound, not the heat from a fire.', 'plastic': 'That little plastic piece fits inside a wire. Try something big and solid.'}},
            {'id': 'sun', 'form': 'Light', 'formIcon': '💡', 'c': '#D99A00', 'fx': 'glow', 'src': {'icon': '☀️', 't': 'The Sun'}, 'rec': {'icon': '🌿', 't': 'A leaf'},
             'gap': 'Only air and empty space! The Sun is 93 million miles away, and its light still reaches the leaf.', 'on': 'The leaf is soaking up sunlight.',
             'off': 'Shade! The light is blocked. So the light WAS crossing the air.', 'ok': ['umbrella', 'board'],
             'miss': {'earmuffs': 'Earmuffs go on ears, not leaves!', 'plastic': 'That little plastic piece fits inside a wire. Try something big that makes shade.'}},
            {'id': 'drum', 'form': 'Sound', 'formIcon': '🔊', 'c': '#3D5A99', 'fx': 'buzz', 'src': {'icon': '🥁', 't': 'School band drum'}, 'rec': {'icon': '👂', 't': 'Your ear'},
             'gap': 'Only air! The drum is across the room, but the air carries its shaking to your ear.', 'on': 'Your eardrum is shaking with the beat.',
             'off': 'Much quieter! So the sound WAS traveling through the air.', 'ok': ['earmuffs'],
             'miss': {'board': 'A board helps a little, but sound bends around it. Try something right on your ears.', 'umbrella': 'Sound goes right around an umbrella. What covers your ears?', 'plastic': 'That little plastic piece fits inside a wire. What covers your ears?'}},
            {'id': 'wire', 'form': 'Electrical', 'formIcon': '⚡', 'c': '#7A4FC0', 'fx': 'lit', 'src': {'icon': '🔋', 't': 'Battery'}, 'rec': {'icon': '💡', 't': 'Bulb'},
             'gap': 'A wire! Here the energy needs a metal path. It can’t just cross the air.', 'on': 'The bulb is lit.',
             'off': 'Plastic doesn’t carry electricity, so the path is broken and the bulb goes dark.', 'ok': ['plastic'],
             'missAny': 'The energy here travels inside the wire. Put something that blocks electricity INTO the wire.'}],
        'q': 'What did blocking the paths prove?',
        'opts': [{'t': 'Energy really was traveling across each gap, even through air with nothing touching.', 'ok': True},
                 {'t': 'Energy only moves when things touch.', 'miss': 'Look at the gaps you tapped. Was anything touching the fire, the Sun or the drum?'},
                 {'t': 'The blockers made new energy.', 'miss': 'Blockers stop energy. They don’t make it.'}],
        'win': 'Heat, light and sound crossed the air. Electricity needed its wire. Clue 2!'},
    'heatflow': {
        'afterText': 'four different WAYS energy can travel', 'kicker': 'Part 2 game', 'title': 'Which way does heat go?',
        'todo': ['A glass of iced lemonade sits on a hot porch. Pick the arrow you think is true.', 'Press Wait one hour. Watch both thermometers.', 'Then drag the right way onto each Florida scene.'],
        'why': {'icon': '🌡️', 'q': 'What does a thermometer show?', 't': 'How warm something is. If its number goes up, energy moved in. If it goes down, energy moved out.'},
        'alt': 'A model: a glass of iced lemonade on a sunny porch, a thermometer in the porch air and a thermometer in the lemonade.', 'model': 'a model',
        'airT': 90, 'drinkT': 38, 'endT': 80, 'airLabel': 'Porch air', 'drinkLabel': 'Lemonade',
        'arrowQ': 'Which way does the energy go?',
        'arrows': [{'k': 'in', 't': '🔥 Heat moves from the warm air INTO the lemonade', 'ok': True}, {'k': 'out', 't': '❄️ Cold moves from the lemonade OUT into the air'}],
        'runBtn': 'Wait one hour', 'againBtn': 'Run it again', 'timeLabel': 'Minutes', 'rightHead': 'Heat moved IN.',
        'rightAfter': 'Heat always moves from warmer to cooler. The warm porch air sent heat into the cold drink, so the ice melted. The air hardly changed because there is so much of it.',
        'wrongHead': 'Look at the lemonade thermometer.',
        'wrongAfter': 'If cold were leaving the drink, the drink would get colder. But it got WARMER and the ice melted. Cold doesn’t travel. Pick the other arrow.',
        'cardsHead': 'Now name the way energy travels in each Florida scene', 'dropHere': 'Drop the way here',
        'forms': [{'k': k, 'icon': v[0], 't': v[1], 'c': v[2]} for k, v in FORMS.items()],
        'cards': [
            {'id': 'sidewalk', 'src': {'icon': '☀️', 't': 'The Sun'}, 'rec': {'icon': '🛣️', 't': 'Sidewalk'}, 'form': 'light',
             'why': 'Light traveled from the Sun. The sidewalk soaked it up and got hot enough to hurt bare feet.', 'miss': {'heat': 'The sidewalk does get hot in the end! But what traveled all the way from the Sun?'}},
            {'id': 'band', 'src': {'icon': '🎺', 't': 'School band'}, 'rec': {'icon': '👂', 't': 'Your ears'}, 'form': 'sound',
             'why': 'The instruments shake the air. The shaking travels to your ears.'},
            {'id': 'bolt', 'src': {'icon': '🌩️', 't': 'Storm cloud'}, 'rec': {'icon': '🌳', 't': 'A tree'}, 'form': 'elec',
             'why': 'A giant electric current crashed through the air into the tree. It made light, sound and heat, too!', 'miss': {'light': 'You SEE the flash, but what rushed from the cloud INTO the tree?', 'heat': 'The tree gets scorched, but what rushed from the cloud INTO the tree?'}},
            {'id': 'stove', 'src': {'icon': '♨️', 't': 'Hot burner'}, 'rec': {'icon': '🍳', 't': 'Pan and eggs'}, 'form': 'heat',
             'why': 'The burner is hotter than the pan, so heat moves into the pan and then into the eggs.', 'miss': {'elec': 'Electricity runs the burner. But between the hot burner and the pan, what moves from warmer to cooler?'}}],
        'q': 'Ice makes your drink cold. What is really happening?',
        'opts': [{'t': 'Heat moves from the warm drink into the colder ice.', 'ok': True},
                 {'t': 'Cold moves out of the ice into the drink.', 'miss': 'Remember the lemonade. Which way does energy travel: warmer to cooler, or cooler to warmer?'},
                 {'t': 'Nothing moves.', 'miss': 'The ice melts! Something moved into it.'}],
        'win': 'Heat moves from warmer to cooler, every time. And you named all four ways energy travels. Clue 3!'},
    'stormwatch': {
        'afterText': 'When you see a flash, start counting', 'kicker': 'Part 4 game', 'title': 'Storm watch',
        'todo': ['Press Start watching and keep your eyes on the sky.', 'Tap I SAW the flash as soon as it flashes.', 'Tap I HEARD the thunder when the boom comes. Turn your sound on!'],
        'why': {'icon': '⚡', 'q': 'What is thunder?', 't': 'Lightning heats the air so fast that the air bursts outward with a BOOM. The flash and the boom start at the same moment.'},
        'strikes': [
            {'img': I('storm-1'), 'alt': 'Lightning bolts branch across a stormy night sky over Kennedy Space Center, Florida.', 'gap': 10, 'far': 'about 2 miles away'},
            {'img': I('storm-2'), 'alt': 'Lightning bolts hit the ocean and a tall metal mast at Kennedy Space Center, Florida.', 'gap': 5, 'far': 'about 1 mile away'},
            {'img': I('storm-3'), 'alt': 'A lightning bolt hits the top of a tall metal mast at Kennedy Space Center, Florida.', 'gap': 2, 'far': 'less than half a mile away. Get inside!'}],
        'startBtn': 'Start watching', 'nextBtn': 'Next strike', 'seeBtn': 'I SAW the flash', 'hearBtn': 'I HEARD the thunder', 'strikeWord': 'Strike',
        'readyLine': 'Press Start watching, then keep your eyes on the sky.', 'waitLine': 'Watch the sky…', 'countLine': 'Counting… now listen for the boom!',
        'earlyLine': 'No flash yet! Wait until the sky lights up.', 'lateLine': 'Not yet! Listen. Tap when you HEAR the boom.',
        'mileLine': '{s} seconds ÷ 5 = {far}', 'logLabel': 'Your storm log (every 5 seconds = about 1 mile)', 'youWord': 'You:', 'realWord': 'Real:',
        'safetyHead': 'When thunder roars, go indoors!', 'safety': 'If you can hear thunder, lightning is close enough to strike you. Go inside a building or a hard-topped car, and wait 30 minutes after the last boom.',
        'credit': 'Lightning at Kennedy Space Center, Florida: “Lightning Above the STS-8 Launch Pad” (NASA, 1983), “Lightning Strikes at Pad 39B” (NASA, May 2011) and “Lightning Strikes at Pad 39B” (NASA, August 2019). All public domain, via Wikimedia Commons.',
        'q': 'Why did you SEE each flash before you HEARD the thunder?',
        'opts': [{'t': 'Light travels almost a million times faster than sound.', 'ok': True},
                 {'t': 'The thunder happened later.', 'miss': 'The flash and the boom happen at the same moment. Which one travels faster?'},
                 {'t': 'My ears are slower than my eyes.', 'miss': 'Your ears work fast! The sound itself was slow getting to you.'}],
        'win': 'Flash first, boom later. The shorter the gap, the closer the strike. Clue 4!'},
    'exploreMod': 'stormwatch',
    'bulletin': {
        'afterText': 'When you see a flash, start counting', 'kicker': 'Bonus · Radio call', 'title': 'The night guard’s call', 'skin': 'radio', 'tone': 'squelch',
        'todo': ['Press Play and listen. You can read along.', 'Tap the 4 signs that energy arrived.'],
        'device': 'CH 7', 'deviceSub': 'PIER GATE', 'station': 'Ray, the pier night guard · 9:41 PM',
        'playBtn': 'Play the radio call', 'againBtn': 'Play it again', 'audio': 'radio', 'paperHead': 'RADIO LOG · CHANNEL 7 · 9:41 PM',
        'lines': [
            'Base, this is Ray at the pier gate. It’s 9:41.',
            'I saw a [[light|huge white flash]] at the end of the pier, and right away a [[sound|BOOM so loud I felt it in my chest]].',
            'Now the [[power|pier lamp is dark]], and there’s a [[heat|burnt smell by the metal post]].',
            '[[x:Good to know for the case! But this isn’t a sign that energy arrived. Look for something that changed.|Nobody is out there]]. I’m staying inside the gate house. Over.'],
        'foundLabel': 'Signs that energy arrived', 'dangerWord': 'Sign', 'countIcon': '⚡', 'countWord': 'signs found',
        'dangers': [{'id': 'light', 'icon': '💡', 't': 'Light', 'does': 'a huge flash'},
                    {'id': 'sound', 'icon': '🔊', 't': 'Sound', 'does': 'a boom right away'},
                    {'id': 'power', 'icon': '⚡', 't': 'Electrical', 'does': 'the lamp burned out'},
                    {'id': 'heat', 'icon': '🔥', 't': 'Heat', 'does': 'a burnt smell'}],
        'win': 'Four ways energy arrived, all at 9:41. Ray stayed inside. Smart!'},
    'tool': {'name': 'Circuit tester', 'icon': '🔌', 'tab': 'assignment', 'after': '#tab-assignment .activity-card', 'key': '20-tool', 'sim': 'circuittester',
             'kicker': 'Bonus · Tool of the Week', 'teaser': 'Test a spoon, a key, a pencil and more. Which ones let electricity through?',
             'done': 'You tested every object. A circuit tester sticker is in your Field Notebook.',
             'why': {'icon': '🔌', 'q': 'What does a circuit tester do?', 't': 'It has a small battery and a bulb. Touch both tips to something. If electricity can flow through it, the path is complete and the bulb lights.'},
             'circuittester': {'title': 'Conductor or insulator?',
                               'todo': ['Drag a thing onto the tester (or tap it).', 'Predict: will the bulb light?', 'Test all 7. (A real tester uses a small battery. Never test a wall outlet.)'],
                               'model': 'a model', 'dropHere': 'Drop a thing on the tester',
                               'predictQ': 'Predict: will the bulb light?', 'yes': 'It will light', 'no': 'It won’t light',
                               'yesWord': 'CONDUCTOR. It lit up!', 'noWord': 'INSULATOR. No light.', 'rightPre': 'Your prediction was right. ', 'wrongPre': 'Surprise! ',
                               'logLabel': 'Your test log', 'colYes': 'Conductors (lit up)', 'colNo': 'Insulators (no light)',
                               'objects': [{'k': 'spoon', 'icon': '🥄', 't': 'Steel spoon', 'c': True, 'note': 'Steel is a metal. Metals let electricity flow.'},
                                           {'k': 'key', 'icon': '🔑', 't': 'House key', 'c': True, 'note': 'Keys are made of metal, like brass.'},
                                           {'k': 'coin', 'icon': '🪙', 't': 'Coin', 'c': True, 'note': 'Coins are made of metals like copper and nickel.'},
                                           {'k': 'pencil', 'icon': '✏️', 't': 'Pencil lead', 'c': True, 'note': 'Pencil “lead” is really graphite, a kind of carbon. It lets some electricity through, so the bulb glows.'},
                                           {'k': 'eraser', 'icon': '⬜', 't': 'Rubber eraser', 'c': False, 'note': 'Rubber blocks electricity. That’s why tool handles and boots for electricians use it.'},
                                           {'k': 'straw', 'icon': '🥤', 't': 'Plastic straw', 'c': False, 'note': 'Plastic blocks electricity, like the coating on a power cord.'},
                                           {'k': 'stick', 'icon': '🪵', 't': 'Wooden craft stick', 'c': False, 'note': 'Dry wood blocks electricity.'}],
                               'q': {'q': 'Sam is putting a lightning rod on the pier. What should it be made of?',
                                     'opts': [{'t': 'Metal, like copper. It’s a great conductor.', 'ok': True, 'why': 'Right! A copper or aluminum rod gives lightning an easy path down a cable into the ground, away from the lamp and the people.'},
                                              {'t': 'Plastic. It’s strong.', 'why': 'Plastic is an insulator. Lightning needs a path it can travel through.'},
                                              {'t': 'Wood. It’s natural.', 'why': 'Wood is an insulator, and it can catch fire. Which things lit your bulb?'}]}}},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Energy can’t be made from nothing. What did it do in Block the path?', 'B': 'Energy can’t be destroyed. Where did it go in the Warm-Up?'},
        'q2': {'B': 'A shout doesn’t warm your ear much. What did your fingertips feel when you hummed?', 'C': 'There’s no wire between you and your friend. What travels through the air as shaking?'},
        'q3': {'A': 'The bulb is where the energy ends up. That makes it the receiver.', 'C': 'The button opens and closes the path. Where does the energy come FROM?'}},
    'flags': {
        'ans-2': [
            {'label': 'source', 're': 'source|comes from|starts|start'},
            {'label': 'receiver', 're': 'receiver|goes to|ends|end up|gets it|recei'},
            {'label': 'a Florida example', 're': 'sun|beach|sand|sidewalk|lightning|storm|band|drum|stove|fire|campfire|lamp|light|ocean|pier|thunder|heat|hot|air condition|flashlight|battery|florida|leaf|plant'}],
        'ans-3': [
            {'label': 'two forms', 'any': ['light', 'sound', 'heat', 'electric', 'thunder', 'flash', 'boom', 'hot', 'bright', 'loud'], 'min': 2},
            {'label': 'evidence', 're': 'see|saw|hear|heard|feel|felt|burn|scorch|smell|bright|loud|boom|flash|evidence|because'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|don.?t have to|do not have to|can move|can travel'},
            {'label': 'two pieces of evidence', 'any': ['sun', 'light', 'fire', 'campfire', 'drum', 'sound', 'thunder', 'lightning', 'flash', 'boom', 'air', 'board', 'umbrella', 'earmuffs', 'block', 'gap', 'leaf', 'hands', 'ear', 'wire', 'lemonade', 'heat'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-2': 15, 'ans-3': 15, 'cer-4': 30},
    'hints': {
        'ans-2': ['Think about Block the path. Which end was the source? Which was the receiver?', 'A Florida example: the Sun and the sidewalk, or a storm cloud and a tree.', 'Try: The source is where ___. The receiver is where ___. For example, ___.'],
        'ans-3': ['Think about Storm watch. What did you see? What did you hear?', 'Evidence is something you notice: a flash, a boom, a burnt smell.', 'Try: One form is ___, and my evidence is ___. Another form is ___, and my evidence is ___.'],
        'cer-4': ['First decide: does energy need touch to move?', 'Think about the campfire, the Sun and the thunder.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'The campfire warmed my hands across the air. When the board blocked it, my hands cooled.',
                'Sunlight crossed 93 million miles of space to reach the leaf.',
                'The drum’s sound crossed the room through the air to my ear.',
                'I saw lightning flash and heard thunder from miles away. Nothing touched me.',
                'Electricity needed a wire. Plastic in the wire stopped it.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · 9:41 PM', 'length': '30–40 s',
                    'script': 'Hi, it’s Sam. Something strange happened on the Palmetto Beach pier last night. At 9:41, all four of my sensors jumped at once, and the pier lamp went dark. But nobody was there! Look at my strip chart. Find the red line. What could reach every sensor at the same moment?'},
        'warmup': {'label': 'Warm-Up · feel it, rate it (Clue 1)', 'length': '20–30 s',
                   'script': 'Today, you are the energy source! Read the first card and really do it. Rub your hands, hum, and look at a light. After each one, slide the meter to show how much changed. Then pick where the energy went.'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Rub your hands for “heat”; hum for “sound”; flick a flashlight for “light”.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · block the path (Clue 2)', 'length': '20–30 s',
                  'script': 'Here are four energy paths. Tap each gap first. What’s in there? Then drag a blocker into the gap, like the umbrella or the earmuffs. Watch the receiver. Did it stop changing?'},
        'part2': {'label': 'Part 2 · which way does heat go? (Clue 3)', 'length': '20–30 s',
                  'script': 'Iced lemonade on a hot porch! Pick an arrow. Does heat move in, or does cold move out? Press Wait one hour, and watch both thermometers. Then drag the right way onto each Florida scene.'},
        'explore': {'label': 'Part 4 · storm watch (Clue 4)', 'length': '25–35 s',
                    'script': 'A storm is rolling in. Turn your sound on and press Start watching. When the sky flashes, tap I saw the flash. When you hear the boom, tap I heard the thunder. Your storm log turns the seconds into miles.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s',
                       'script': 'Do you have all four clues? Crack the case at the top of this tab. Then answer two questions, fill in your energy hunt, and finish your C-E-R.'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · my energy hunt', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says energy only moves when things touch. Hmm. Think about the gaps you blocked and the thunder you counted. Pick your side, tap two pieces of evidence, then explain how they prove your claim.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 20.02 (energy stations).',
                    'script': 'Case closed! Lightning hit the pier lamp, and its energy reached every sensor through the air. Now I’m adding a lightning rod. Next time, you set up your own energy stations and collect evidence.'},
    },
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Your list of energy you sent, all 3 moves (Warm-Up)',
        'A blocked path (The Lesson)',
        'The two thermometers after one hour (The Lesson)',
        'Your storm log (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['The pier at 9:41 PM', 'Four energy paths in my house', 'Heat moving into my lemonade'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 3,
                           'prompts': ['Draw one of your energy paths', 'Label the source and the receiver', 'Draw an arrow the way the energy moves']}]},
    'hlCoach': copy.deepcopy(Q['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '💡', 'name': 'The burnt-out pier bulb',
                 'line': 'You cracked Case 20, and the burnt-out pier bulb goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next time: energy stations.'},
    'notebookTitle': 'Unit 5 · Energy, Motion & Collisions',
    'notebook': copy.deepcopy(O['notebook']),
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You’re ready to follow the energy.',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'list', 'find': {'sel': '.fs-game[data-mod="rateit"]'},
         'label': 'Warm-Up: three places energy is moving right now', 'q': 'Warm-Up: Three places where energy is moving from one place to another right now',
         'title': 'Your turn: list three places where energy is moving around you right now. Name the source and the receiver.', 'min': 3, 'unit': 'places', 'addLabel': '+ Add another',
         'ph': ['Light from the window to my desk', 'Sound from ___ to ___', 'Something else…']},
        {'id': 'hide-hints', 'type': 'hide', 'find': {'sel': '.act-warmup p', 'text': 'Hints: heat from a window'}},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'hide-nw', 'type': 'hide', 'find': {'sel': '.act-warmup .socratic-q', 'text': 'Notice'}},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Find one example of each way energy moves'},
         'label': 'Part C: My energy hunt', 'q': 'Part C: One example of each way energy moves, with its source, receiver and evidence',
         'title': 'My energy hunt (source → receiver, and my evidence)',
         'fields': [{'t': 'HEAT', 'icon': '🔥', 'ph': 'Source: ___ → Receiver: ___. My evidence: ___'},
                    {'t': 'LIGHT', 'icon': '💡', 'ph': 'Source: ___ → Receiver: ___. My evidence: ___'},
                    {'t': 'SOUND', 'icon': '🔊', 'ph': 'Source: ___ → Receiver: ___. My evidence: ___'},
                    {'t': 'ELECTRICAL', 'icon': '⚡', 'ph': 'Source: ___ → Receiver: ___. My evidence: ___'}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Do you have to touch things to transfer energy?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-2': 'Part B · Question 5', 'ans-3': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] == '19.02': n.update({'icon': '🧦', 'name': 'The fluke sock'})
    if n['lesson'] == '20.01': n.update({'icon': '💡', 'name': 'The burnt-out pier bulb'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'Energy moves from a source to a receiver, even through the air.',
    'key': ['energy', 'moves', 'source', 'receiver', 'air'],
    'small': ['a', 'to', 'the'],
    'model': 'A scientist might highlight “energy moves”, “source”, “receiver” and “through the air”. Those words hold the big idea. Small words like “a” and “the” don’t carry the idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me explain how energy moves, and how we know it moved?']

# ---------------------------------------------------------------- Spotlight: what lights up as Sam talks
EV = '#tab-assignment .act-body > div:has(> .fs-plan)'
D['cues'] = {
    'welcome': [{'at': '^pier$', 'sel': '.fs-casecard .fs-case-t', 'fx': 'glow'},
                {'at': '^sensors', 'sel': '.fs-casecard .fs-strip-svg', 'fx': 'pop'},
                {'at': '^dark', 'sel': '.fs-casecard .fs-strip-note', 'fx': 'trace'},
                {'at': '^chart', 'sel': '.fs-casecard .fs-strip', 'fx': 'glow'},
                {'at': '^red$', 'sel': '.fs-casecard .fs-strip-mk', 'fx': 'pop', 'tag': '9:41 PM'},
                {'at': '^moment', 'sel': '.fs-casecard .fs-case-ask', 'fx': 'trace'}],
    'warmup': [{'at': '^source', 'sel': '.fs-game[data-mod="rateit"] .fs-why', 'fx': 'glow', 'scroll': True},
               {'at': '^card', 'sel': '.fs-rt-card', 'fx': 'pop'},
               {'at': '^hum', 'sel': '.fs-rt-tab', 'all': True, 'fx': 'wiggle'},
               {'at': '^meter', 'sel': '.fs-rt-card', 'fx': 'point', 'tag': 'Slide the meter'},
               {'at': '^went', 'sel': '.fs-rt-tally', 'fx': 'glow'}],
    'part1': [{'at': '^paths', 'sel': '.fs-blk-grid', 'fx': 'glow', 'scroll': True},
              {'at': '^gap$', 'sel': '.fs-blk-gap', 'all': True, 'fx': 'pop'},
              {'at': '^blocker', 'sel': '.fs-blk-tray', 'fx': 'glow'},
              {'at': '^umbrella', 'sel': '.fs-blk-item', 'i': 1, 'fx': 'point'},
              {'at': '^earmuffs', 'sel': '.fs-blk-item', 'i': 2, 'fx': 'point'},
              {'at': '^receiver', 'sel': '.fs-blk-rec', 'all': True, 'fx': 'wiggle'}],
    'part2': [{'at': '^lemonade', 'sel': '.fs-hf-svg', 'fx': 'glow', 'scroll': True},
              {'at': '^arrow', 'sel': '.fs-hf-ask', 'fx': 'pop'},
              {'at': '^Wait', 'sel': '.fs-hf-run', 'fx': 'point'},
              {'at': '^thermometers', 'sel': '.fs-hf-th', 'all': True, 'fx': 'glow'},
              {'at': '^scene', 'sel': '.fs-game[data-mod="heatflow"] .fs-todo li', 'i': 2, 'fx': 'trace'}],
    'explore': [{'at': '^storm$', 'sel': '.fs-stw-view', 'fx': 'glow', 'scroll': True},
                {'at': '^Start', 'sel': '.fs-stw-start', 'fx': 'point'},
                {'at': '^saw', 'sel': '.fs-stw-see', 'fx': 'pop'},
                {'at': '^heard', 'sel': '.fs-stw-hear', 'fx': 'pop'},
                {'at': '^log', 'sel': '.fs-stw-log', 'fx': 'glow'},
                {'at': '^miles', 'sel': '.fs-game[data-mod="stormwatch"] .fs-in-k', 'fx': 'trace'}],
    'assignment': [{'at': '^clues', 'sel': '.fs-board', 'fx': 'glow'},
                   {'at': '^Crack', 'sel': '.fs-solve', 'fx': 'pop', 'scroll': True},
                   {'at': '^two$', 'sel': '#tab-assignment .pq', 'fx': 'glow', 'all': True, 'scroll': True},
                   {'at': '^hunt', 'sel': '#tab-assignment .fs-in-frame', 'fx': 'pop', 'scroll': True},
                   {'at': '^C-E-R$', 'sel': '#tab-assignment .fs-cer', 'fx': 'glow', 'scroll': True}],
    'evidence': [{'at': '^classmate', 'sel': EV + ' > p', 'i': 0, 'fx': 'trace'},
                 {'at': '^blocked', 'sel': '.fs-plan .fs-opt', 'i': 2, 'fx': 'glow'},
                 {'at': '^thunder', 'sel': '.fs-plan .fs-opt', 'i': 5, 'fx': 'glow'},
                 {'at': '^side', 'sel': '.fs-plan .fs-plan-row', 'i': 0, 'fx': 'pop'},
                 {'at': '^explain', 'sel': '.fs-cer .fs-cer-row', 'i': 2, 'fx': 'glow', 'scroll': True}],
    'closing': [{'at': '^closed', 'sel': '.fs-specimen', 'fx': 'pop', 'scroll': True},
                {'at': '^Lightning', 'sel': '.fs-solve', 'fx': 'glow'},
                {'at': '^rod', 'sel': '.fs-tool', 'fx': 'wiggle'},
                {'at': '^Next', 'sel': '#tab-assignment .callout-tip', 'fx': 'glow'}],
}
D['fold'] = {'bulletin': {'icon': '📻', 'tease': 'Ray, the pier night guard, radioed in at 9:41. Can you catch the 4 signs that energy arrived?', 'open': 'Listen'}}
D['cueWords'] = json.load(open('cuewords.json', encoding='utf-8')) if os.path.exists('cuewords.json') else {}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
