#!/usr/bin/env python3
"""Writes data.json and fixes.json for 20.02 (run from this folder). Case 20 part 2 "Prove It to the Council" (Sam Park, Palmetto Beach).
New modules: doubter (convince Councilor Ruiz: her face reacts to each piece of evidence), stationkit (build 4 stations on lab mats:
source / receiver / evidence tool, NOT READY without a tool), proofmeter (the three-bowls trick, then upgrade a weak claim until PROVEN),
stationrun (run 4 virtual stations and read each real tool by tapping its number), council (after the solve: answer her objections with
measurements, stamp the lightning rod work order APPROVED, real photo), speedround (bonus: WEAK or STRONG against the clock), printcard
(a printable blank station report), case.memo (a handwritten note), bulletin skin:'mic' + tone:'gavel'. No tool (20.01 has the circuit tester)."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../18-01/data.json', encoding='utf-8'))
O = json.load(open('../20-01/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
PS = '<p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)
def I(n): return 'images/20-02-' + n + '.jpg'

# ---------------------------------------------------------------- ticked fixes (Bethany, 25 Oct 2026)
fx('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist already asks for two station reports',
   '🎨 Part C &mdash; Build Your Own Food Chain', '🧪 Part C &mdash; Two Station Reports')
fx('fix', 'copy-paste leftover: Part C task from 9.01 (now two station reports, typed on the page)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Pick two stations from today. For each one, write the source, the receiver, what you observed, what you measured and your claim.</p>', True)
fx('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'unit label: “Ecosystems & Energy” is a leftover; weeks 18–24 are Unit 5', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Energy, Motion &amp; Collisions</div>')
fx('fix', 'energy transfer is physical science, not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standard: 4-PS3-2 is “energy can be transferred by sound, light, heat and electric currents” (4-ESS3-1 is about energy resources)',
   '<div class="info-value">4-ESS3-1 · TEKS 4.8(B)</div>', '<div class="info-value">4-PS3-2 · TEKS 4.8(B)</div>')
fx('fix', 'the AI station picture (smoke rising off the battery reads as a short or a hazard; an 85°F cup steaming hard) and the Key Concept, Stop & Reason, tap diagram (its electrical “time how long the bulb stays bright” would take hours), Observe & Reason, the weather-station fact, the Solar Energy Center callout and Go Deeper are gone (lean); Build-a-station kit replaces the picture and the diagram, and the stations (with safety lines: warm tap water, one AA battery, never a wall outlet) run in Part 4. Next button goes to Self-Check',
   r'<div class="lesson-figure scroll-reveal">\s*<div class="lesson-figure-label">🧪 Four Classroom Energy Stations</div>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 4 · Run the Stations</h3>\n      ' + PS + 'Now run all four stations yourself. Do something to each source, then read the tool. Every number you read goes into your station log.</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('fix', 'Part B question 5 pointed at the removed diagram', 'Pick ONE station from the diagram (heat, light, sound, or electrical).', 'Pick ONE station from today (heat, light, sound, or electrical).')

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; plain words; no dash',
   "Hold this question in your head as you work. By the end of the lesson, you'll have done your own investigation — running four small \"stations\" — and recorded evidence for each form of energy transfer.",
   "Keep this question in mind. By the end, you’ll run four small stations and collect evidence that energy moved at each one.")
fx('plain', 'the warm-up now asks how to PROVE it (typed on the page)',
   'In one minute, write down what you can tell about each of these without going closer:',
   'Look at these three from where you sit. What can you tell about each one, and how could you PROVE it to a doubter?')
fx('plain', 'no dash', "Today you'll be the investigator. You'll set up four small stations, each one showing a different form of energy moving — and collect evidence with your senses and simple tools.",
   "Today you're the investigator. You'll set up four small stations, each showing a different way energy moves, and collect evidence with your senses and simple tools.")
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', 'no dash', "Today, you'll do the same — four stations, one for each form of energy.", "Today you'll do the same: four stations, one for each way energy moves.")
fx('plain', 'no dash', 'your senses (you can SEE light, HEAR sound, FEEL heat) — and sometimes a tool', 'your senses (you can SEE light, HEAR sound, FEEL heat), and sometimes a tool')
fx('plain', 'no dash', 'Scientists do better than that — they collect EVIDENCE other people can check.', 'Scientists do better than that. They collect EVIDENCE other people can check.')
fx('plain', 'misconception kept, plain, no dash',
   r'<p><strong>Common misconception:</strong> Some people think you have to have fancy tools to do real science\..*?</p>',
   '<p><strong>Watch out:</strong> Some people think real science needs fancy tools. It doesn’t. A thermometer, a ruler, a stopwatch and your own senses are enough for this lesson and for thousands of real investigations.</p>', True)
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'shorter closing; points to 21.01',
   r'<p><strong>Nicely done\.</strong> You can now set up an investigation.*?</p>',
   '<p><strong>Nicely done.</strong> You set up stations, collected observations AND measurements, and convinced a doubter. Next week, things start crashing: what happens to energy when objects collide?</p>', True)

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: Stop & Think (Build-a-station kit is the thinking stop for Part 1)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (a copy of 20.01’s: the same home hunt, whale fact, hummingbird question and conductor Go Deeper)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 7 removed (Bethany kept 5 and 6)', r'<div class="pq">\s*<span class="pq-num"[^>]*>7</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C typed on the page',
   'Two station reports — each with source, receiver, evidence (observation + measurement), and an evidence-based claim.',
   'Two station reports, each with the source, the receiver, what I observed, what I measured and my claim. (A sketch is a bonus.)')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether we can prove energy moved, and supported it with two pieces of evidence from my stations.',
   '<strong>Use Your Evidence:</strong> My claim about whether we can prove energy moved, with two pieces of evidence from my stations.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', True)

# ---------------------------------------------------------------- the story
SAM = Q['crew']['sam']
D = {
    'lesson': '20.02', 'week': 20, 'day': 2, 'guide': 'sam', 'prefix': 'g4sci-20-2', 'manifestKey': '20-02',
    'paths': P['paths'], 'crew': {'sam': SAM},
    'expedition': {'num': 20, 'title': 'Prove It to the Council'},
    'ambient': {'icon': '🌊', 'label': 'Ocean sounds'},
    'case': {
        'num': 20, 'title': 'Prove It to the Council', 'style': 'council',
        'hook': 'Good news: the town might pay for a lightning rod on the pier. Bad news: one councilor doesn’t believe my 9:41 PM readings. (A councilor helps make decisions for a town.)',
        'notice': {'head': 'PALMETTO BEACH TOWN COUNCIL', 'title': 'Monday Meeting · Agenda',
                   'rows': [['Item 1', 'Beach cleanup schedule'], ['Item 2', 'A lightning rod for the pier lamp (Sam Park)'], ['To vote yes', 'Evidence that energy really moves'], ['When', '6:00 PM, Town Hall']],
                   'line': 'Bring your evidence.'},
        'memo': {'t': 'Sam, I think your pier sensors just glitched. Energy doesn’t really travel from place to place. No money for a lightning rod unless you PROVE it, with evidence I can check myself.', 'sign': '— Councilor Ruiz'},
        'stills': [],
        'question': 'What evidence will convince Councilor Ruiz that energy really moves?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'doubter', 'icon': '🤨', 'where': 'Warm-Up: convince the doubter', 't': 'Councilor Ruiz shrugged at “I just know” and smiled at a number from a tool, because she could check it herself.'},
            {'id': 'stationkit', 'icon': '🧪', 'where': 'The Lesson, Part 1: build-a-station kit', 't': 'Every station needs a source, a receiver and a way to collect evidence. Without a tool, a station is NOT READY.'},
            {'id': 'proofmeter', 'icon': '🌡️', 'where': 'The Lesson, Part 2: hands lie', 't': 'Your hands can be fooled: the same water felt warm AND cool. A measurement, checked by someone else, made the evidence PROVEN.'},
            {'id': 'stationrun', 'icon': '📋', 'where': 'The Lesson, Part 4: run the stations', 't': 'At every station the receiver changed, and a tool measured it: 104°F to 92°F, a 6 cm to 12 cm light spot, rice jumping 1 cm and 4 cm, 250 lux to 0.'},
        ],
        'solve': {
            'title': 'What will convince Councilor Ruiz?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Tell her Sam is an engineer, so she should trust him.', 'why': 'Check Clue 1. Being an expert isn’t evidence she can check.'},
                {'t': 'Describe how each station looked and felt.', 'why': 'Check Clue 3. Hands can be fooled. What makes evidence strong?'},
                {'t': 'Run four stations, each with a source, a receiver and a tool, and bring her observations AND measurements she can check.', 'right': True,
                 'why': 'Case cracked! Now present your evidence to the town council, just below.'},
                {'t': 'Wait for another lightning storm and hope she sees it.', 'why': 'Check Clue 4. You can collect evidence right now with stations.'},
            ]},
    },
    'doubter': {
        'afterText': 'PROVE it to a doubter', 'kicker': 'Warm-Up game', 'title': 'Convince the doubter',
        'todo': ['Pick a claim.', 'Tap the evidence you think would convince Councilor Ruiz.', 'Watch her face. Convince her about all 3.'],
        'why': {'icon': '🤨', 'q': 'What is a doubter?', 't': 'Someone who won’t believe a claim until they see evidence. Good scientists are doubters too!'},
        'name': 'Councilor Ruiz', 'hello': 'Prove it!', 'faces': ['🤨', '🙂', '😃'], 'claimWord': 'The claim', 'pickQ': 'Which evidence would convince her?',
        'halfLine': 'That’s real evidence! But she wants something she can check herself. Try another card.', 'zeroLine': 'She doesn’t buy it. Pick evidence she could check.',
        'countWord': 'claims proven', 'doneSay': 'Numbers I can check. Okay, I believe you!',
        'claims': [
            {'id': 'cocoa', 'icon': '☕', 'short': 'Warm cocoa', 't': 'This cup of cocoa is warm.',
             'opts': [{'t': 'I can see steam coming off it.', 'lvl': 1, 'react': 'Steam is a clue… but HOW warm?'},
                      {'t': 'A thermometer in it reads 130°F.', 'lvl': 2, 'react': 'A number! I can check that myself.'},
                      {'t': 'I just know it is.', 'lvl': 0, 'react': 'You just KNOW? That’s not evidence.'}]},
            {'id': 'lamp', 'icon': '💡', 'short': 'The lamp', 't': 'That lamp across the room is sending out light.',
             'opts': [{'t': 'Lamps always do that.', 'lvl': 0, 'react': 'Always? Says who?'},
                      {'t': 'The wall next to it looks brighter.', 'lvl': 1, 'react': 'Brighter to YOU. How much brighter?'},
                      {'t': 'A light meter by the wall reads 300 with the lamp on and 20 with it off.', 'lvl': 2, 'react': 'On, off, two numbers. Now I see it!'}]},
            {'id': 'pencil', 'icon': '✏️', 'short': 'The tapping pencil', 't': 'The tapping pencil is making sound.',
             'opts': [{'t': 'A sound meter reads 60 while it taps and 35 when it stops.', 'lvl': 2, 'react': 'Louder while it taps. I can test that!'},
                      {'t': 'Everybody knows pencils are noisy.', 'lvl': 0, 'react': 'Everybody? That’s not proof.'},
                      {'t': 'I can hear tap, tap, tap.', 'lvl': 1, 'react': 'You heard it. Can you show me a number?'}]}],
        'q': 'What convinced Councilor Ruiz the most?',
        'opts': [{'t': 'A number from a tool, because she could check it herself.', 'ok': True},
                 {'t': 'Saying “I just know.”', 'miss': 'Look at her face when you picked that one!'},
                 {'t': 'Whatever sounded the most sure.', 'miss': 'Sounding sure isn’t evidence. What could she check?'}],
        'win': 'Numbers she could check won every time. Clue 1!'},
    'bulletin': {
        'afterSel': '.act-warmup .callout-tip', 'kicker': 'Bonus · Voice memo', 'title': 'Councilor Ruiz speaks', 'skin': 'mic', 'tone': 'gavel',
        'todo': ['Press Play and listen. You can read along.', 'Tap the 3 weak spots in her argument.'],
        'device': 'TOWN HALL', 'deviceSub': 'Councilor Ruiz', 'station': 'A voice memo for Sam · 0:15',
        'playBtn': 'Play the voice memo', 'againBtn': 'Play it again', 'audio': 'memo', 'paperHead': 'VOICE MEMO · COUNCILOR RUIZ',
        'lines': [
            'This is Councilor Ruiz. I read Sam Park’s report about the pier.',
            'Honestly, his chart [[feel|just feels wrong to me]].',
            'Everybody knows [[wire|energy can’t move without wires]].',
            'And I [[look|didn’t even need to look at his numbers]]. [[x:That part is fair! Good scientists DO ask for evidence. Look for the weak spots.|Prove it to me with evidence I can check]].'],
        'foundLabel': 'Weak spots in her argument', 'dangerWord': 'Weak spot', 'countIcon': '🔎', 'countWord': 'weak spots found',
        'dangers': [{'id': 'feel', 'icon': '🤷', 't': 'A feeling', 'does': 'a feeling isn’t evidence'},
                    {'id': 'wire', 'icon': '⚡', 't': 'A wrong idea', 'does': 'light and sound cross the air'},
                    {'id': 'look', 'icon': '🙈', 't': 'Skipped the data', 'does': 'she didn’t look at the numbers'}],
        'win': 'Three weak spots! A feeling, a wrong idea and skipped data. Sam has work to do.'},
    'stationkit': {
        'afterText': 'Every station has the same three parts', 'kicker': 'Part 1 game', 'title': 'Build-a-station kit',
        'todo': ['Drag each part onto its station mat (or tap a part, then a slot).', 'Every mat needs a source, a receiver and an evidence tool.', 'Watch out: two parts don’t belong anywhere.'],
        'why': {'icon': '🧪', 'q': 'What is an evidence tool?', 't': 'A tool that measures something and gives you a number, like a thermometer, a ruler or a light meter.'},
        'roles': [{'k': 'src', 'icon': '📤', 't': 'Source'}, {'k': 'rec', 'icon': '📥', 't': 'Receiver'}, {'k': 'tool', 'icon': '📏', 't': 'Evidence tool'}],
        'stations': [{'id': 'heat', 'icon': '☕', 't': 'Heat station'}, {'id': 'light', 'icon': '🔦', 't': 'Light station'}, {'id': 'sound', 'icon': '🥁', 't': 'Sound station'}, {'id': 'elec', 'icon': '🔋', 't': 'Electrical station'}],
        'parts': [
            {'id': 'flash', 'icon': '🔦', 't': 'Flashlight', 'st': 'light', 'role': 'src'},
            {'id': 'therm', 'icon': '🌡️', 't': 'Thermometer', 'st': 'heat', 'role': 'tool'},
            {'id': 'rice', 'icon': '🍚', 't': 'Rice grains on the drum', 'st': 'sound', 'role': 'rec'},
            {'id': 'outlet', 'icon': '🔌', 't': 'Wall outlet', 'st': 'x', 'role': 'src', 'miss': 'Never a wall outlet! It’s far too strong to play with. A small battery is safe.'},
            {'id': 'bulb', 'icon': '💡', 't': 'Small bulb', 'st': 'elec', 'role': 'rec'},
            {'id': 'cup', 'icon': '☕', 't': 'Cup of warm tap water', 'st': 'heat', 'role': 'src'},
            {'id': 'meter', 'icon': '📟', 't': 'Light meter', 'st': 'elec', 'role': 'tool'},
            {'id': 'paper', 'icon': '📄', 't': 'White paper', 'st': 'light', 'role': 'rec'},
            {'id': 'hand', 'icon': '✋', 't': 'Your hand tapping the drum', 'st': 'sound', 'role': 'src'},
            {'id': 'know', 'icon': '🤞', 't': '“I just know”', 'st': 'x', 'role': 'tool', 'miss': 'That’s not a tool! A station needs a way to collect evidence someone else can check.'},
            {'id': 'ruler1', 'icon': '📏', 't': 'Ruler on the paper', 'st': 'light', 'role': 'tool'},
            {'id': 'air', 'icon': '🌬️', 't': 'The cooler air around the cup', 'st': 'heat', 'role': 'rec'},
            {'id': 'batt', 'icon': '🔋', 't': 'One AA battery', 'st': 'elec', 'role': 'src'},
            {'id': 'ruler2', 'icon': '📐', 't': 'Ruler standing by the drum', 'st': 'sound', 'role': 'tool'}],
        'trayLabel': 'Parts (drag one onto a mat, or tap it and then a slot)', 'ready': 'READY ✓', 'notReady': 'NOT READY: no way to measure', 'countWord': 'stations ready',
        'roleMiss': 'Right station! But this is the {is}, not the {slot}.',
        'q': 'Why does every station need an evidence tool?',
        'opts': [{'t': 'So we can collect a measurement someone else can check.', 'ok': True},
                 {'t': 'Tools make the station look cool.', 'miss': 'They do look cool! But what does a tool GIVE you?'},
                 {'t': 'Without a tool, the energy can’t move.', 'miss': 'Energy moves either way. The tool lets us measure it.'}],
        'win': 'Four stations, each with a source, a receiver and a tool. Clue 2!'},
    'proofmeter': {
        'afterText': 'The strongest investigation reports use BOTH', 'kicker': 'Part 2 game', 'title': 'Hands lie, numbers don’t',
        'todo': ['Try the three bowls with the buttons. (You can try it at home with an adult: warm tap water only.)', 'Then drag (or tap) evidence onto the claim until the meter says PROVEN.'],
        'why': {'icon': '✋', 'q': 'Why can hands be fooled?', 't': 'Your skin feels warmer or cooler than what it touched just before. It can’t tell you an exact temperature.'},
        'part1Head': '1. Can your hands be fooled?', 'part2Head': '2. Upgrade the evidence',
        'bowls': {'hot': {'t': 'Warm tap water', 'temp': 104}, 'room': {'t': 'Room-temperature water', 'temp': 72}, 'cold': {'t': 'Ice water', 'temp': 40}},
        'leftWord': 'left hand', 'rightWord': 'right hand',
        'steps': ['Put your left hand in the warm bowl and your right hand in the ice water', 'Wait 30 seconds', 'Waiting…', 'Move both hands into the middle bowl', 'Check with a thermometer'],
        'left': 'Left: “It feels COOL!”', 'right': 'Right: “It feels WARM!”', 'sameBowl': 'Same water. Two different answers!', 'trickAsk': 'Which hand is right?',
        'thermo': 'The middle bowl is 72°F. One number.',
        'trickWhy': 'Your hands only feel warmer or cooler than before. A thermometer gives a number anyone can check.',
        'claimWord': 'Claim', 'claim': 'The cup of cocoa cooled down.', 'dropHere': 'Drop evidence here',
        'levels': ['Hmm, not yet', 'Maybe', 'Pretty good', 'Strong', 'PROVEN!'],
        'pieces': [
            {'id': 'hand', 'icon': '✋', 't': 'My hand said the mug felt less warm.', 'pts': 0, 'why': 'Remember the bowls? Hands can be fooled.'},
            {'id': 't1', 'icon': '🌡️', 't': 'Thermometer at 3:00 PM: 130°F', 'pts': 1, 'why': 'A number! But one reading can’t show a change.'},
            {'id': 'steam', 'icon': '💨', 't': 'The steam slowly stopped.', 'pts': 1, 'why': 'An observation anyone could see. A good start!'},
            {'id': 'sure', 'icon': '🙂', 't': 'I’m really, really sure.', 'pts': 0, 'why': 'Being sure isn’t evidence. What could someone check?'},
            {'id': 't2', 'icon': '🌡️', 't': 'Thermometer at 3:20 PM: 110°F', 'pts': 2, 'why': 'Before and after: the number dropped 20°F.'},
            {'id': 'check', 'icon': '👥', 't': 'My partner read it too: 110°F.', 'pts': 1, 'why': 'Someone else checked and got the same number.'}],
        'q': 'What makes evidence the strongest?',
        'opts': [{'t': 'An observation AND a measurement someone else can check.', 'ok': True},
                 {'t': 'Whatever your hand feels.', 'miss': 'Remember the bowls! The same water felt warm and cool.'},
                 {'t': 'Saying it very loudly.', 'miss': 'Loud isn’t proof. What can someone check?'}],
        'win': 'Hands can be fooled, but numbers can be checked. Clue 3!'},
    'stationrun': {
        'afterText': 'Now run all four stations yourself', 'kicker': 'Part 4 game', 'title': 'Run the stations',
        'todo': ['Pick a station.', 'Press a button to run it.', 'Read the tool: tap the number it shows. Do both buttons at every station.'],
        'why': {'icon': '📋', 'q': 'What is a station log?', 't': 'A table where scientists write what they observed and what they measured, so anyone can check it later.'},
        'model': 'a model', 'condQ': 'Run it:', 'readQ': 'Read the tool. Tap the number it shows ({unit}).', 'pickLine': 'Press a button above to run the station.',
        'lowLine': 'A little low. Look again where the tool points.', 'highLine': 'A little high. Look again where the tool points.',
        'logLabel': 'My station log', 'colSt': 'Station', 'colObs': 'What I observed', 'colMeas': 'What I measured',
        'stations': [
            {'id': 'heat', 'icon': '☕', 't': 'Heat', 'kind': 'therm', 'unit': '°F', 'min': 60, 'max': 110, 'step': 2, 'tol': 2,
             'src': 'Source: warm water', 'rec': 'Receiver: the cooler air', 'obs': 'The steam slowly stopped.', 'safety': 'Warm tap water only. Never boiling water.',
             'conds': [{'k': 'a', 'btn': 'Start', 'val': 104, 'note': 'A cup of warm tap water just went on the table. The air in the room is 75°F.'},
                       {'k': 'b', 'btn': 'After 10 minutes', 'val': 92, 'note': 'Ten minutes later. Heat has been moving from the warm water into the cooler air.'}]},
            {'id': 'light', 'icon': '🔦', 't': 'Light', 'kind': 'ruler', 'unit': 'cm wide', 'min': 0, 'max': 13, 'step': 1, 'tol': 0,
             'src': 'Source: flashlight', 'rec': 'Receiver: white paper', 'obs': 'A bright spot on the paper. Farther away, it got bigger and dimmer.', 'safety': 'Never shine a flashlight into anyone’s eyes.',
             'conds': [{'k': 'a', 'btn': 'Flashlight 20 cm away', 'val': 6, 'note': 'The light makes a bright spot. How wide is it?'},
                       {'k': 'b', 'btn': 'Flashlight 40 cm away', 'val': 12, 'note': 'Twice as far away. The spot spreads out and looks dimmer.'}]},
            {'id': 'sound', 'icon': '🥁', 't': 'Sound', 'kind': 'vruler', 'unit': 'cm high', 'min': 0, 'max': 6, 'step': 0.5, 'tol': 0.5,
             'src': 'Source: your tapping hand', 'rec': 'Receiver: rice grains (and your ears)', 'obs': 'The rice grains jumped. Harder taps made them jump higher.', 'safety': 'Tap with your hand, not a hard object.',
             'conds': [{'k': 'a', 'btn': 'Soft tap', 'val': 1, 'note': 'A soft tap makes the drum shake a little. How high did the rice jump?'},
                       {'k': 'b', 'btn': 'Hard tap', 'val': 4, 'note': 'A hard tap sends more energy into the drum.'}]},
            {'id': 'elec', 'icon': '🔋', 't': 'Electrical', 'kind': 'meter', 'unit': 'lux', 'min': 0, 'max': 400, 'step': 50, 'major': 100, 'tol': 0,
             'src': 'Source: one AA battery', 'rec': 'Receiver: a small bulb', 'obs': 'The bulb glowed. With a wire unhooked, it went dark.', 'safety': 'One AA battery and a small bulb. Never a wall outlet.',
             'conds': [{'k': 'a', 'btn': 'Wires hooked up', 'val': 250, 'note': 'A light meter measures how much light reaches it, in units called lux.'},
                       {'k': 'b', 'btn': 'One wire unhooked', 'val': 0, 'note': 'The path is broken. What does the light meter say now?'}]}],
        'q': 'At every station, what showed that energy moved?',
        'opts': [{'t': 'The receiver changed, and a tool measured the change.', 'ok': True},
                 {'t': 'Nothing really moved. It was a trick.', 'miss': 'Look at your log. Did the numbers change?'},
                 {'t': 'Only the heat station worked.', 'miss': 'Check your log. Did every station get a number?'}],
        'win': 'Four stations, eight measurements. Your log is ready for the council. Clue 4!'},
    'exploreMod': 'stationrun',
    'council': {
        'after': '.fs-solve', 'kicker': 'After the case', 'title': 'Present to the council',
        'todo': ['Councilor Ruiz has one question for each station.', 'Answer with the evidence that will convince her.'],
        'lockLine': 'Crack the case first. Then the council meets.', 'name': 'Councilor Ruiz', 'icon': '🏛️',
        'meter': ['Not convinced', 'Hmm…', 'Getting there', 'Almost', 'I believe it!'],
        'answerQ': 'Answer her with evidence from your station log:', 'obsWord': 'What I observed', 'measWord': 'What I measured',
        'objections': [
            {'id': 'heat', 'icon': '☕', 't': 'Maybe that water was never warm in the first place.', 'obs': 'The steam slowly stopped.', 'meas': 'The thermometer read 104°F, then 92°F ten minutes later.', 'weak': 'Steam is nice, but how warm was it? She wants a number.', 'strong': 'Heat: 104°F → 92°F. Heat moved into the air.'},
            {'id': 'light', 'icon': '🔦', 't': 'Light doesn’t really GO anywhere. It just sits in the flashlight.', 'obs': 'I saw a bright spot on the paper.', 'meas': 'The spot was 6 cm wide at 20 cm and 12 cm wide at 40 cm.', 'weak': 'You saw it, but could she check it? Give her a measurement.', 'strong': 'Light: the spot grew from 6 cm to 12 cm as it traveled farther.'},
            {'id': 'sound', 'icon': '🥁', 't': 'Tapping a drum can’t move anything else.', 'obs': 'The rice wiggled.', 'meas': 'The rice jumped 1 cm on a soft tap and 4 cm on a hard tap.', 'weak': '“Wiggled” could mean anything. How high?', 'strong': 'Sound: the rice jumped 1 cm, then 4 cm.'},
            {'id': 'elec', 'icon': '🔋', 't': 'That bulb could be a fake. Maybe it glows by itself.', 'obs': 'The bulb looked bright.', 'meas': 'The light meter read 250 lux hooked up and 0 lux unhooked.', 'weak': 'Looked bright to YOU. She needs something she can check.', 'strong': 'Electrical: 250 lux hooked up, 0 unhooked.'}],
        'order': {'head': 'WORK ORDER 20-B · PALMETTO BEACH PIER',
                  'rows': [['Job', 'A lightning rod on the pier lamp post'], ['Material', 'A copper rod and a cable down to a rod in the ground'], ['Evidence', '4 stations: observations + measurements'], ['Asked for by', 'Sam Park, engineer']],
                  'stampBtn': 'Stamp it APPROVED', 'stamp': 'APPROVED', 'sign': 'Councilor Ruiz',
                  'img': I('lightning-rod'), 'alt': 'A thin metal lightning rod sticks up from a rusty metal roof under a blue sky.',
                  'cap': 'A real lightning rod on a house roof in LaPlace, Louisiana. A cable carries a strike safely down into the ground.',
                  'credit': '“Lightning rod, Woodland Plantation House, LaPlace, Louisiana” by Infrogmation of New Orleans, CC BY-SA 4.0, via Wikimedia Commons.'},
        'win': 'APPROVED! Your evidence convinced the council. The pier gets its lightning rod, and Evidence Detective is open below.'},
    'speedround': {
        'after': '.fs-game[data-mod="council"]', 'kicker': 'Bonus game · unlocked after the case', 'title': 'Evidence Detective',
        'todo': ['Press Start.', 'Tap WEAK or STRONG for each piece of evidence before time runs out.', 'Can you get 3 stars?'],
        'why': {'icon': '🕵️', 'q': 'What makes evidence STRONG?', 't': 'A number from a tool, or something anyone could check. “I just know” is weak.'},
        'lockLine': 'Crack the case first. Then Evidence Detective opens.', 'secs': 40, 'three': 9, 'two': 7, 'one': 5,
        'startBtn': 'Start', 'againBtn': 'Play again', 'weakBtn': 'WEAK', 'strongBtn': 'STRONG', 'ready': 'Press Start. Then tap WEAK or STRONG for each piece of evidence.',
        'lines': {'best': 'Best', 'three': 'Evidence Detective, first class!', 'some': 'Nice work! Play again for more stars.', 'none': 'Try again: look for numbers someone else could check.'},
        'items': [
            {'t': 'The thermometer went from 70°F to 85°F.', 'k': 's', 'why': 'Two numbers from a tool. That’s strong!'},
            {'t': 'I just know it got warmer.', 'k': 'w', 'why': '“I just know” can’t be checked.'},
            {'t': 'The rice jumped 3 cm when I tapped the drum.', 'k': 's', 'why': 'A measurement anyone could repeat.'},
            {'t': 'My friend said the bulb was on.', 'k': 'w', 'why': 'One person’s word, with no number to check.'},
            {'t': 'The light meter read 300 lux next to the lamp.', 'k': 's', 'why': 'A number from a tool.'},
            {'t': 'It felt kind of warm to me.', 'k': 'w', 'why': 'Remember the bowls? Hands can be fooled.'},
            {'t': 'Two of us measured the light spot: 8 cm and 8 cm.', 'k': 's', 'why': 'Measured twice, by two people. Very strong!'},
            {'t': 'Trust me, I’m a scientist.', 'k': 'w', 'why': 'Even scientists need evidence.'},
            {'t': 'I took the temperature 3 times: 92, 92 and 91°F.', 'k': 's', 'why': 'Several readings that agree.'},
            {'t': 'The drum probably made the rice move.', 'k': 'w', 'why': '“Probably” is a guess, not a measurement.'},
            {'t': 'The stopwatch read 4.2 seconds.', 'k': 's', 'why': 'A number anyone could check with a stopwatch.'}]},
    'printcard': {'after': '#tab-assignment .fs-in-frame', 'btn': 'Print a blank station report', 'note': 'Optional: run a real station at home with an adult.',
                  'head': 'My Station Report', 'sub': 'Field Station · Lesson 20.02',
                  'rows': ['Station (heat, light, sound or electrical):', 'Source (where the energy comes from):', 'Receiver (where the energy goes):', 'What I observed:', 'What I measured (the tool and the numbers):', 'My claim (did energy move? how do I know?):']},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Batteries and bulbs are only at the electrical station. What did EVERY mat in the station kit have?', 'C': 'Tools are one part. What else did every mat need?'},
        'q2': {'A': 'Warmth isn’t what you saw. What did the rice DO?', 'B': 'Color doesn’t change when energy arrives. What did the rice do?'},
        'q3': {'B': 'Measurements can be a little off. So why are they still strong?', 'C': 'Fancy words don’t make evidence strong. What can another scientist do with a number?'}},
    'flags': {
        'ans-1': [
            {'label': 'the station', 're': 'heat|light|sound|electric|cup|water|flashlight|drum|rice|battery|bulb'},
            {'label': 'source and receiver', 're': 'source|receiver|goes to|comes from'},
            {'label': 'evidence', 're': 'evidence|measure|thermometer|ruler|meter|number|degree|°|cm|lux|observ|saw|see|jump|glow|light up|lit'}],
        'ans-2': [
            {'label': 'observation', 're': 'observ|see|saw|hear|heard|feel|felt|notice|look|senses'},
            {'label': 'measurement', 're': 'measur|number|tool|thermometer|ruler|meter|degree|°|cm|lux|stopwatch'},
            {'label': 'a station example', 're': 'heat|light|sound|electric|cup|water|flashlight|drum|rice|battery|bulb|cocoa|lamp'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|can prove|you can'},
            {'label': 'two pieces of evidence', 'any': ['thermometer', 'degree', '°', '104', '92', 'rice', 'cm', 'jump', 'ruler', 'light meter', 'lux', '250', 'spot', 'bulb', 'battery', 'bowl', 'hand', 'measure', 'number', 'station'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-1': 15, 'ans-2': 15, 'cer-4': 30},
    'hints': {
        'ans-1': ['Think about the Build-a-station kit. What were the three parts?', 'Name the source, the receiver and the tool you would use.', 'Try: At the ___ station, the source is ___, the receiver is ___, and I would measure ___ with a ___.'],
        'ans-2': ['Think about the three bowls. What did your hands say? What did the thermometer say?', 'An observation uses your senses. A measurement uses a tool and gives a number.', 'Try: An observation is ___, like ___. A measurement is ___, like ___.'],
        'cer-4': ['First decide: can you prove energy moved?', 'Think about your station log: the thermometer, the rice and the light meter.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'The thermometer read 104°F, then 92°F ten minutes later.',
                'The rice jumped 1 cm on a soft tap and 4 cm on a hard tap.',
                'The light meter read 250 lux with the wires hooked up and 0 unhooked.',
                'My hands said the same water was warm AND cool, but the thermometer said 72°F.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · prove it to the council', 'length': '30–40 s',
                    'script': 'Good news and bad news. The town might pay for a lightning rod on the pier, but Councilor Ruiz doesn’t believe my readings. Read her note. She wants evidence she can check herself. Let’s give her some!'},
        'warmup': {'label': 'Warm-Up · convince the doubter (Clue 1)', 'length': '20–30 s',
                   'script': 'Councilor Ruiz is a tough doubter. For each claim, pick the evidence that would convince her. Watch her face. Does she raise an eyebrow, or does she smile?'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Hold up a thermometer for “measurement”; point at a lamp for “receiver”.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · build-a-station kit (Clue 2)', 'length': '20–30 s',
                  'script': 'Every station needs three parts. Drag a source, a receiver, and an evidence tool onto each mat. Watch out for parts that don’t belong. A station without a tool says not ready.'},
        'part2': {'label': 'Part 2 · hands lie, numbers don’t (Clue 3)', 'length': '20–30 s',
                  'script': 'Try the three bowls. One hand goes in warm water, one in ice water. Then both go into the middle bowl. Your hands disagree! Next, add evidence to the claim until the meter says proven.'},
        'explore': {'label': 'Part 4 · run the stations (Clue 4)', 'length': '25–35 s',
                    'script': 'Time to run all four stations. Pick a station, press a button to run it, then read the tool. Tap the number it shows. Every reading goes into your station log.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s',
                       'script': 'Do you have all four clues? Crack the case at the top of this tab, then present your evidence to the council. After that, answer two questions, write two station reports, and finish your C-E-R.'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · two station reports', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says you can’t really prove that energy moved. Hmm. Think about your thermometer and your rice ruler. Pick your side, tap two pieces of evidence, then explain how they prove your claim.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 21.01 (collisions).',
                    'script': 'Case closed! Councilor Ruiz approved the lightning rod, all because of your evidence. Next week, things start crashing. What happens to energy when objects collide?'},
    },
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Councilor Ruiz smiling (Warm-Up)',
        'A READY station mat (The Lesson)',
        'The PROVEN meter (The Lesson)',
        'Your station log (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['My favorite station', 'The three bowls', 'The pier with its new lightning rod'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 3,
                           'prompts': ['Draw one of your stations', 'Label the source and the receiver', 'Label the tool you used to measure']}]},
    'hlCoach': copy.deepcopy(Q['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '📋', 'name': 'The approved work order',
                 'line': 'You cracked Case 20 part 2, and the approved work order goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next week: collisions.'},
    'notebookTitle': 'Unit 5 · Energy, Motion & Collisions',
    'notebook': copy.deepcopy(O['notebook']),
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You’re ready to run your stations.',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '.fs-game[data-mod="doubter"]'},
         'label': 'Warm-Up: what I can tell, and how I could prove it', 'q': 'Warm-Up: What I can tell about each one, and how I could prove it to a doubter',
         'title': 'Your turn: what can you tell about each one, and how could you prove it?',
         'fields': [{'t': 'A lamp glowing across the room', 'icon': '💡', 'ph': 'I can tell… I could prove it with…'},
                    {'t': 'A friend tapping a pencil on a desk', 'icon': '✏️', 'ph': 'I can tell… I could prove it with…'},
                    {'t': 'A warm cup of cocoa on a table', 'icon': '☕', 'ph': 'I can tell… I could prove it with…'}]},
        {'id': 'hide-list', 'type': 'hide', 'find': {'sel': '.act-warmup ul', 'text': 'A lamp glowing'}},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'hide-nw', 'type': 'hide', 'find': {'sel': '.act-warmup .socratic-q', 'text': 'Notice'}},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Pick two stations from today'},
         'label': 'Part C: Two station reports', 'q': 'Part C: Two station reports (source, receiver, observation, measurement, claim)',
         'title': 'My two station reports',
         'fields': [{'t': 'STATION 1: which station, the source and the receiver', 'icon': '1️⃣', 'ph': 'Station: ___. Source: ___. Receiver: ___.'},
                    {'t': 'STATION 1: what I observed, what I measured and my claim', 'icon': '📏', 'ph': 'I observed… I measured… So energy…', 'long': True},
                    {'t': 'STATION 2: which station, the source and the receiver', 'icon': '2️⃣', 'ph': 'Station: ___. Source: ___. Receiver: ___.'},
                    {'t': 'STATION 2: what I observed, what I measured and my claim', 'icon': '📏', 'ph': 'I observed… I measured… So energy…', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Can you prove that energy moved?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-1': 'Part B · Question 5', 'ans-2': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] == '20.02': n.update({'icon': '📋', 'name': 'The approved work order'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'A measurement is a number from a tool that someone else can check.',
    'key': ['measurement', 'number', 'tool', 'check'],
    'small': ['A', 'a', 'that'],
    'model': 'A scientist might highlight “measurement”, “number from a tool” and “someone else can check”. Those words hold the big idea. Small words like “a” and “that” don’t carry the idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me explain what evidence shows that energy moved?']

# ---------------------------------------------------------------- Spotlight: what lights up as Sam talks
EV = '#tab-assignment .act-body > div:has(> .fs-plan)'
D['cues'] = {
    'welcome': [{'at': '^lightning', 'sel': '.fs-casecard .fs-notice', 'fx': 'glow'},
                {'at': '^Ruiz', 'sel': '.fs-casecard .fs-memo', 'fx': 'pop'},
                {'at': '^note', 'sel': '.fs-casecard .fs-memo p', 'fx': 'trace'},
                {'at': '^check', 'sel': '.fs-casecard .fs-case-ask', 'fx': 'glow'}],
    'warmup': [{'at': '^doubter', 'sel': '.fs-dbt-who', 'fx': 'glow', 'scroll': True},
               {'at': '^claim', 'sel': '.fs-dbt-tabs', 'fx': 'pop'},
               {'at': '^evidence', 'sel': '.fs-dbt-opts', 'fx': 'glow'},
               {'at': '^face', 'sel': '.fs-dbt-face', 'fx': 'wiggle', 'tag': 'Watch her face'},
               {'at': '^smile', 'sel': '.fs-dbt-say', 'fx': 'pop'}],
    'part1': [{'at': '^three', 'sel': '.fs-kit-mat .fs-kit-slots', 'all': True, 'fx': 'glow', 'scroll': True},
              {'at': '^Drag', 'sel': '.fs-kit-tray', 'fx': 'point'},
              {'at': '^mat', 'sel': '.fs-kit-mat', 'all': True, 'fx': 'pop'},
              {'at': '^belong', 'sel': '.fs-kit-part[data-id="outlet"]', 'fx': 'wiggle'},
              {'at': '^ready', 'sel': '.fs-kit-tag', 'all': True, 'fx': 'glow'}],
    'part2': [{'at': '^bowls', 'sel': '.fs-prf-bowls', 'fx': 'glow', 'scroll': True},
              {'at': '^warm$', 'sel': '.fs-prf-bowl.b-hot', 'fx': 'pop'},
              {'at': '^ice', 'sel': '.fs-prf-bowl.b-cold', 'fx': 'pop'},
              {'at': '^middle', 'sel': '.fs-prf-bowl.b-room', 'fx': 'point'},
              {'at': '^claim', 'sel': '.fs-game[data-mod="proofmeter"] .fs-todo li', 'i': 1, 'fx': 'trace'}],
    'explore': [{'at': '^four', 'sel': '.fs-srn-tabs', 'fx': 'glow', 'scroll': True},
                {'at': '^button', 'sel': '.fs-srn-conds', 'fx': 'point'},
                {'at': '^tool', 'sel': '.fs-srn-vis', 'fx': 'pop'},
                {'at': '^number', 'sel': '.fs-srn-panel', 'fx': 'glow'},
                {'at': '^log', 'sel': '.fs-srn-log', 'fx': 'glow'}],
    'assignment': [{'at': '^clues', 'sel': '.fs-board', 'fx': 'glow'},
                   {'at': '^Crack', 'sel': '.fs-solve', 'fx': 'pop', 'scroll': True},
                   {'at': '^council', 'sel': '.fs-game[data-mod="council"]', 'fx': 'glow', 'scroll': True},
                   {'at': '^two$', 'sel': '#tab-assignment .pq', 'fx': 'glow', 'all': True, 'scroll': True},
                   {'at': '^reports', 'sel': '#tab-assignment .fs-in-frame', 'fx': 'pop', 'scroll': True},
                   {'at': '^C-E-R$', 'sel': '#tab-assignment .fs-cer', 'fx': 'glow', 'scroll': True}],
    'evidence': [{'at': '^classmate', 'sel': EV + ' > p', 'i': 0, 'fx': 'trace'},
                 {'at': '^thermometer', 'sel': '.fs-plan .fs-opt', 'i': 2, 'fx': 'glow'},
                 {'at': '^rice', 'sel': '.fs-plan .fs-opt', 'i': 3, 'fx': 'glow'},
                 {'at': '^side', 'sel': '.fs-plan .fs-plan-row', 'i': 0, 'fx': 'pop'},
                 {'at': '^explain', 'sel': '.fs-cer .fs-cer-row', 'i': 2, 'fx': 'glow', 'scroll': True}],
    'closing': [{'at': '^closed', 'sel': '.fs-specimen', 'fx': 'pop', 'scroll': True},
                {'at': '^approved', 'sel': '.fs-game[data-mod="council"]', 'fx': 'glow'},
                {'at': '^Next', 'sel': '#tab-assignment .callout-tip', 'fx': 'glow'}],
}
D['fold'] = {'bulletin': {'icon': '🎙️', 'tease': 'Councilor Ruiz left Sam a voice memo. Can you spot the weak parts of her argument?', 'open': 'Listen'},
             'speedround': {'icon': '🕵️', 'tease': 'WEAK or STRONG? Sort 11 pieces of evidence before the clock runs out. Can you get 3 stars?', 'open': 'Play'}}
D['cueWords'] = json.load(open('cuewords.json', encoding='utf-8')) if os.path.exists('cuewords.json') else {}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
