#!/usr/bin/env python3
"""Writes data.json and fixes.json for 21.01 (run from this folder). Case 21 "The Boardwalk Fender Bender" (Sam Park, Palmetto Beach).
New modules: clapper (Warm-Up clap machine: gentle vs hard rounds, sound meter + warm palms), coinbank (Part 1: drag every energy coin to where it went,
a Disappeared bin refuses coins), bumpercars (Part 2: set speeds, predict, crash in 3 patterns, read both speedometers), crashlab (Part 4: steel / rubber /
clay balls + a heat camera, then the real heat-camera photo), strike (bonus bowling after the case, folded), SIMS.soundmeter (Tool of the Week),
case.style:'report' + case.diagram (an accident report with a drawn diagram). Rosa's voicemail = bulletin skin:'phone' (folded)."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../18-01/data.json', encoding='utf-8'))
O = json.load(open('../20-02/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
PS = '<p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)
def I(n): return 'images/21-01-' + n + '.jpg'

# ---------------------------------------------------------------- ticked fixes (Bethany, 26 Oct 2026)
# 9.01 leftovers
fx('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist already asks for a before/after of one collision',
   '🎨 Part C &mdash; Build Your Own Food Chain', '🔄 Part C &mdash; Before and After')
fx('fix', 'copy-paste leftover: Part C task from 9.01 (now a before/after of one collision, typed on the page)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Pick one collision from today, or one from your own life. Describe the BEFORE, the AFTER and where the energy went.</p>', True)
fx('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
# labels and standard
fx('fix', 'unit label: “Ecosystems & Energy” is a leftover; weeks 18–24 are Unit 5', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Energy, Motion &amp; Collisions</div>')
fx('fix', 'collisions are physical science, not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standard: 4-PS3-3 is “changes in energy when objects collide” (4-ESS3-1 is about energy resources)',
   '<div class="info-value">4-ESS3-1 · TEKS 4.7(A)</div>', '<div class="info-value">4-PS3-3 · TEKS 4.7(A)</div>')
fx('fix', 'standard detail: the lesson is about energy, not forces', '<div class="info-detail">Forces in Collisions</div>', '<div class="info-detail">Energy Changes in Collisions</div>')
# add sound and heat (4-PS3-3)
fx('fix', '4-PS3-3: some energy turns into sound and heat in a collision; the page never said so',
   '<div class="act-subtitle">Motion and energy switch places</div>', '<div class="act-subtitle">Energy moves, and some becomes sound and heat</div>')
fx('fix', '4-PS3-3: name where the rest of the energy goes (sound and heat), no dash',
   '<p>And every collision does the same basic thing: it <span class="vtip">transfers<span class="vtip-box"><span class="vtip-word">Transfer</span>When energy moves between objects.</span></span> energy and motion from one object to another. A moving ball stops or slows down; a still object starts moving. The total energy goes somewhere — it doesn\'t just disappear.</p>',
   '<p>Every collision does the same basic thing: it <span class="vtip">transfers<span class="vtip-box"><span class="vtip-word">Transfer</span>When energy moves between objects.</span></span> energy from one object to another. A moving ball stops or slows down; a still object starts moving. And some of the energy always turns into <strong>sound</strong> (the click or crash you hear) and <strong>heat</strong> (a tiny bit of warming where they hit). The energy goes somewhere. It never just disappears.</p>')
# shaky facts
fx('fix', 'the AI before/after marble picture (it shows no sound or heat), Key Concept, Stop & Reason, the tap diagram, Observe & Reason, the “Florida car bumpers crumple on purpose” fact (it is the car’s front frame, a crumple zone, and nothing Florida-only), the bowling callout and Go Deeper are gone (lean); the Energy coin bank and Bumper cars replace the picture and the diagram, and the Crash lab is Part 4. Next button goes to Self-Check',
   r'<div class="lesson-figure scroll-reveal">\s*<div class="lesson-figure-label">💥 Before vs\. After: A Marble Collision</div>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 4 · The Crash Lab</h3>\n      ' + PS + 'Now be the scientist. Pick two balls, predict the AFTER, crash them, then look with a heat camera. Where did the energy go?</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('fix', 'Part B question 7: it is the front of the car (a crumple zone) that is built to crush, not the bumper',
   'Why do car bumpers crumple in collisions? Use the words <em>energy</em> and <em>transfer</em> in your answer.',
   'Why is the front of a car built to crumple in a crash? Use the words <em>energy</em> and <em>transfer</em> in your answer.')
fx('fix', 'Part B question 7 label (Gathered Answers)', 'data-label="Why do car bumpers crumple in collisions? Use the ..."', 'data-label="Why is the front of a car built to crumple?"')
fx('fix', 'Self-Check Q1 feedback: objects DO stop by themselves when something like rubbing (friction) slows them',
   "Objects don't stop on their own (something has to push them), and sunlight hitting a leaf is a light transfer, not a collision.",
   "An object that stops by itself was slowed by rubbing (friction), and sunlight hitting a leaf is a light transfer, not a collision.")

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; plain words; no dash',
   "Hold this question in your head as you work. By the end of the lesson, you'll be able to describe how energy moves between objects when they collide — and use that idea to predict what will happen in everyday collisions.",
   "Keep this question in mind. By the end, you’ll know where the energy goes when things crash, and you’ll predict what happens next.")
fx('plain', 'warm-up title matches the clap machine', '🌅 Warm-Up: A Marble at Rest', '🌅 Warm-Up: The Clap Test')
fx('plain', 'warm-up subtitle', 'What needs to happen for it to move?', 'Your hands can collide too!')
fx('plain', 'the warm-up starts with a real clap; the marble list is typed on the page',
   'Imagine a marble sitting still on a table. In your notebook, list three different ways you could make it start moving.',
   'Clap your hands hard 10 times, then touch your cheek. Do your palms feel warm? Your hands just collided over and over! Next, imagine a marble sitting still on a table. What could make it start moving?')
fx('plain', 'no dash', "Hint: you don't have to touch it with your hand — what could touch it?", "Hint: you don't have to touch it with your hand. What else could bump into it?")
fx('plain', 'no dash', "Today you'll learn that when two objects collide, energy and motion can pass from one to the other. The ball you bump becomes the next thing in motion — and you can predict what happens.",
   "Today you'll learn that when two objects collide, energy passes from one to the other, and some turns into sound and heat. Then you can predict what happens.")
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', 'no dash', 'Both slow down — and sometimes change direction.', 'Both slow down, and sometimes change direction.')
fx('plain', 'no dash', 'If you know what BEFORE looks like — which objects were moving, and how fast — you can usually', 'If you know what BEFORE looks like (which objects were moving, and how fast), you can usually')
fx('plain', 'misconception kept, plain, no dash',
   r'<p><strong>Common misconception:</strong> Some people think the moving object always "wins" a collision.*?</p>',
   '<p><strong>Watch out:</strong> Some people think the moving object always “wins” a collision and the still one always “loses.” Not true! In most collisions, BOTH objects change how they move.</p>', True)
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'shorter closing; points to 21.02',
   r'<p><strong>Nicely done\.</strong> You can now describe what happens in a.*?</p>',
   '<p><strong>Nicely done.</strong> You found where the energy goes in a crash: into the other object’s motion, sound and heat. It never disappears. Next lesson, you’ll run your own trials to test collision predictions.</p>', True)

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: Notice & Wonder (the clap machine is the warm-up’s thinking stop)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Notice &amp; Wonder</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: Stop & Think (the energy coin bank is the thinking stop for Part 1)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its marble test is now the Crash lab in Part 4; its blink-fast strike fact was wrong: pins take about 2 seconds to fall)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 5 removed (Bethany kept 6 and 7; it pointed at the removed diagram)', r'<div class="pq">\s*<span class="pq-num"[^>]*>5</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: renumber Part B (6 → 5)', '<span class="pq-num" style="background:#D4772C;">6</span>', '<span class="pq-num" style="background:#D4772C;">5</span>')
fx('cut', 'lean: renumber Part B (7 → 6)', '<span class="pq-num" style="background:#D4772C;">7</span>', '<span class="pq-num" style="background:#D4772C;">6</span>')
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C typed on the page', 'A before/after sketch of one collision with motion arrows and a one-sentence energy statement.',
   'The BEFORE, the AFTER and where the energy went, for one collision. (A sketch is a bonus.)')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether energy disappears in a crash, and supported it with two pieces of evidence.',
   '<strong>Use Your Evidence:</strong> My claim about whether energy disappears in a crash, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', True)

# ---------------------------------------------------------------- the accident report diagram (top view, drawn)
DIAGRAM = ('<svg viewBox="0 0 560 200" role="img" aria-label="Diagram from the report, seen from above: the golf cart (A) drives right along the boardwalk and bumps the parked ice cream cart (B). B rolls about 3 feet to the right. A stops.">'
  '<rect width="560" height="200" fill="#F3E2C2"/>' + ''.join('<line x1="0" y1="%d" x2="560" y2="%d" stroke="#D9C29A" stroke-width="2"/>' % (y, y) for y in range(20, 200, 30)) +
  '<rect x="0" y="0" width="560" height="14" fill="#7DB7D9"/><text x="10" y="11" font-size="11" font-family="Nunito,sans-serif" font-weight="800" fill="#fff">THE GULF</text>'
  '<g transform="translate(110 100)"><rect x="-55" y="-30" width="110" height="60" rx="12" fill="#F4F4F0" stroke="#3A4A5A" stroke-width="3"/><text y="7" text-anchor="middle" font-size="22" font-family="Nunito,sans-serif" font-weight="900" fill="#3A4A5A">A</text></g>'
  '<text x="110" y="160" text-anchor="middle" font-size="15" font-family="Nunito,sans-serif" font-weight="800" fill="#3A2C1E">Golf cart (Gus)</text>'
  '<path d="M172 100 h62" stroke="#C8553D" stroke-width="4" marker-end="url(#rptArr)"/><text x="200" y="78" text-anchor="middle" font-size="14" font-family="Nunito,sans-serif" font-weight="800" fill="#C8553D">about 5 mph</text>'
  '<defs><marker id="rptArr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="#C8553D"/></marker></defs>'
  '<path d="M262 76 l6 14 l15 -3 l-9 11 l9 12 l-15 -3 l-6 14 l-6 -14 l-15 3 l9 -12 l-9 -11 l15 3 z" fill="#FFD84D" stroke="#E0A800" stroke-width="2"/>'
  '<g transform="translate(330 100)"><rect x="-40" y="-26" width="80" height="52" rx="8" fill="#F8C8DC" stroke="#B5577E" stroke-width="3"/><text y="7" text-anchor="middle" font-size="22" font-family="Nunito,sans-serif" font-weight="900" fill="#B5577E">B</text></g>'
  '<g transform="translate(440 100)" opacity=".5"><rect x="-40" y="-26" width="80" height="52" rx="8" fill="none" stroke="#B5577E" stroke-width="3" stroke-dasharray="6 5"/></g>'
  '<path d="M372 140 h66" stroke="#B5577E" stroke-width="3" stroke-dasharray="6 5" marker-end="url(#rptArr)"/><text x="405" y="160" text-anchor="middle" font-size="15" font-family="Nunito,sans-serif" font-weight="800" fill="#3A2C1E">Ice cream cart (Rosa)</text>'
  '<text x="440" y="56" text-anchor="middle" font-size="14" font-family="Nunito,sans-serif" font-weight="800" fill="#B5577E">rolled about 3 ft</text>'
  '<text x="110" y="56" text-anchor="middle" font-size="14" font-family="Nunito,sans-serif" font-weight="800" fill="#3A4A5A">stopped dead</text>'
  '</svg>')

# ---------------------------------------------------------------- the story
SAM = Q['crew']['sam']
D = {
    'lesson': '21.01', 'week': 21, 'day': 1, 'guide': 'sam', 'prefix': 'g4sci-21-1', 'manifestKey': '21-01',
    'paths': P['paths'], 'crew': {'sam': SAM},
    'expedition': {'num': 21, 'title': 'The Boardwalk Fender Bender'},
    'ambient': {'icon': '🌊', 'label': 'Ocean sounds'},
    'case': {
        'num': 21, 'title': 'The Boardwalk Fender Bender', 'style': 'report',
        'hook': 'CRUNCH! Last night on the Palmetto Beach boardwalk, Gus’s golf cart bumped Rosa’s ice cream cart. Nobody was hurt. Gus filled out an accident report, but one line in it puzzles me.',
        'notice': {'head': 'PALMETTO BEACH · ACCIDENT REPORT', 'title': 'Report 21-A · Boardwalk, Pier 2',
                   'rows': [['When', 'Tuesday, 8:15 PM'], ['Vehicle A', 'Pier security golf cart (driver: Gus)'], ['Vehicle B', 'Ice cream cart, parked (owner: Rosa)'], ['Speed', 'About 5 mph (walking speed is 3)'], ['Hurt?', 'No one. One scoop of mint chip was lost.']],
                   'line': 'Driver’s statement below.'},
        'diagram': {'svg': DIAGRAM, 'cap': 'The diagram from the report, seen from above.'},
        'memo': {'t': 'My cart was moving, then it stopped dead. So all of its energy just disappeared. Poof! Case closed, right?', 'sign': '— Gus, pier security'},
        'stills': [{'cam': 'A real crash test', 'time': 'the front is built to crumple', 'tag': 'PHOTO 1', 'img': I('crash-test'), 'kind': 'print',
                    'alt': 'A white pickup truck after a government crash test. Its front end is crushed and folded, and the hood is bent up, but the cab where people sit is not crushed.'}],
        'stillsCredit': '“Ford F-150 Crew Cab Frontal Crash Test” by Calspan Corporation for the National Highway Traffic Safety Administration (NHTSA), public domain, via Wikimedia Commons.',
        'question': 'Gus’s golf cart stopped dead. Did its energy really disappear? If not, where did it go?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'clapper', 'icon': '👏', 'where': 'Warm-Up: the clap machine', 't': 'Your clapping hands stopped, but their energy didn’t vanish. It became the CLAP (sound) and warm palms (heat). Hard claps made more of both.'},
            {'id': 'coinbank', 'icon': '🪙', 'where': 'The Lesson, Part 1: the energy coin bank', 't': 'In both crashes, every energy coin went somewhere: the other object’s motion, sound and heat. The Disappeared bin stayed empty.'},
            {'id': 'bumpercars', 'icon': '🚗', 'where': 'The Lesson, Part 2: bumper cars', 't': 'In every bumper-car crash, BOTH cars changed how they moved. A car that slows or stops passes its motion to the other car.'},
            {'id': 'crashlab', 'icon': '🔥', 'where': 'The Lesson, Part 4: the crash lab', 't': 'The heat camera showed warm spots where the balls hit. The squishier the crash, the more energy became heat and a dent.'},
        ],
        'solve': {
            'title': 'Where did the golf cart’s energy go?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'It disappeared, because the golf cart stopped.', 'why': 'Check Clue 2. Did any energy coin ever land in Disappeared?'},
                {'t': 'Into Rosa’s cart (it rolled), the CRUNCH (sound), and heat in the dented bumpers.', 'right': True,
                 'why': 'Case cracked! The energy moved into motion, sound and heat. None of it disappeared. Strike! is open just below.'},
                {'t': 'It all stayed inside the golf cart.', 'why': 'Check Clue 3. The golf cart stopped. A stopped cart doesn’t keep its motion.'},
                {'t': 'Only into the sound of the crash.', 'why': 'Check Clue 4. What did the heat camera show where things hit?'},
            ]},
    },
    'clapper': {
        'afterText': 'What else could bump into it', 'kicker': 'Warm-Up game', 'title': 'The clap machine',
        'todo': ['Pick a round: gentle claps or hard claps.', 'Clap as fast as you can for 5 seconds: press the 👏 button, tap the hands or press the space bar.', 'Do both rounds. Which made more sound and more heat?'],
        'why': {'icon': '👏', 'q': 'Is a clap a collision?', 't': 'Yes! Your two hands bump into each other. Every clap is a tiny collision.'},
        'alt': 'A model: two hands clapping, a sound meter that jumps with each clap, and a warm glow that grows on the palms.', 'model': 'a model',
        'secs': 5, 'pickLabel': '1. Pick a round', 'pickMiss': 'Pick a round first: gentle or hard.', 'clapBtn': 'Clap!', 'meterLabel': 'Sound meter', 'warmLabel': 'Palms',
        'rounds': [{'k': 'gentle', 'btn': '🤲 Round 1: gentle claps', 'label': 'Gentle claps', 'db': 55, 'warm': 0.05, 'vol': 0.25, 'line': 'Gentle claps! Your 5 seconds start with your first clap.'},
                   {'k': 'hard', 'btn': '👏 Round 2: hard claps', 'label': 'Hard claps', 'db': 78, 'warm': 0.14, 'vol': 0.9, 'line': 'HARD claps! Your 5 seconds start with your first clap.'}],
        'clapsWord': 'claps', 'aboutWord': 'about', 'palmsWord': 'palms', 'notYet': 'Not tried yet', 'startLine': 'Pick a round to start.', 'nextLine': 'Now try the other round.',
        'doneLine': 'Hard claps made more sound AND more heat. More energy went in, so more came out.',
        'q': 'Your hands stopped moving after each clap. Where did their motion energy go?',
        'opts': [{'t': 'Into sound (the clap) and heat (warm palms).', 'ok': True},
                 {'t': 'It just disappeared.', 'miss': 'Then why did your palms get warm, and what made the clap sound?'},
                 {'t': 'Back into your arms, ready for the next clap.', 'miss': 'Your arms make NEW motion for each clap. Where did the old motion go when the hands hit?'}],
        'win': 'The clap was sound and the warm palms were heat. Clue 1!'},
    'bulletin': {
        'afterSel': '.act-warmup .callout-tip', 'kicker': 'Bonus · New voicemail', 'title': 'Rosa’s voicemail', 'skin': 'phone', 'tone': 'ring',
        'todo': ['Press Play and listen. You can read along.', 'Tap the 3 clues that tell where the golf cart’s energy went.'],
        'device': 'Voicemail', 'deviceSub': 'Rosa · 0:18', 'station': '1 new message from Rosa',
        'playBtn': 'Play the voicemail', 'againBtn': 'Play it again', 'audio': 'voicemail', 'paperHead': 'VOICEMAIL · ROSA',
        'lines': ['Hi Sam, it’s Rosa from the ice cream cart on the boardwalk.',
                  'Gus’s golf cart bumped my cart, and I heard a [[crunch|loud CRUNCH]]!',
                  'My whole cart [[roll|rolled about three feet]], and a scoop of mint chip fell off a cone.',
                  'When I touched the dent, the bumper felt [[warm|a little warm]]. [[x:That tells how Rosa felt, not where the energy went. Listen for something she heard, saw or felt with her hand.|I was so surprised!]] Call me back!'],
        'foundLabel': 'Where the energy went', 'dangerWord': 'Clue', 'countIcon': '🔎', 'countWord': 'clues found',
        'dangers': [{'id': 'crunch', 'icon': '🔊', 't': 'A sound', 'does': 'some energy became the CRUNCH'},
                    {'id': 'roll', 'icon': '🍦', 't': 'Motion', 'does': 'Rosa’s cart started moving'},
                    {'id': 'warm', 'icon': '🌡️', 't': 'Heat', 'does': 'the dented bumper got warm'}],
        'win': 'Sound, motion and heat. Rosa just told Sam where the energy went!'},
    'coinbank': {
        'afterText': 'It never just disappears', 'kicker': 'Part 1 game', 'title': 'The energy coin bank',
        'todo': ['Press Play the crash and watch.', 'Read the clue under each bin.', 'Drag every energy coin out of the bank to where the energy went (or tap a coin, then a bin). Tap a coin in a bin to send it back.', 'Then press Check my bank.'],
        'why': {'icon': '🪙', 'q': 'What is an energy coin?', 't': 'A pretend coin that stands for a share of the energy, so we can count where it goes. Real energy isn’t coins, but it can be counted with tools.'},
        'coins': 10, 'model': 'a model', 'playBtn': 'Play the crash', 'playFirst': 'Play the crash first, so you can see where the energy went.',
        'bankLabel': 'BEFORE: the energy of the moving one (10 coins)', 'inWord': 'In', 'outWord': 'Out', 'leftWord': 'Coins still in the bank', 'balanced': 'Balanced! Every coin went somewhere.',
        'checkBtn': 'Check my bank', 'leftMiss': 'Some coins are still in the bank. Every bit of energy went somewhere!',
        'lost': {'icon': '🕳️', 't': 'Disappeared', 'miss': 'Energy never just disappears! Read the clues again. What did you hear? What got warm? What moved?'},
        'samLabel': 'Sam’s estimate', 'youWord': 'You', 'samWord': 'Sam', 'nextBtn': 'Next crash',
        'rounds': [
            {'k': 'bowl', 'icon': '🎳', 't': 'Bowling ball and pins', 'scene': 'bowl', 'sfx': 'CRASH!',
             'alt': 'A model: a bowling ball rolls into four pins. The pins fly up and away, and the ball keeps rolling slowly.',
             'bins': [{'k': 'pins', 'icon': '🎳', 't': 'Pins moving', 'need': 'most', 'ev': 'The pins flew across the lane.', 'sam': 6},
                      {'k': 'ball', 'icon': '⚫', 't': 'Ball still moving', 'need': 'some', 'ev': 'The ball kept rolling, but slower.', 'sam': 2},
                      {'k': 'sound', 'icon': '🔊', 't': 'Sound', 'need': 'some', 'ev': 'CRASH! You could hear it.', 'sam': 1},
                      {'k': 'heat', 'icon': '🌡️', 't': 'Heat', 'need': 'some', 'ev': 'The ball and pins got a tiny bit warmer where they hit.', 'sam': 1}],
             'someMiss': 'Look at the clue under “{bin}”: {ev} So some energy went there.', 'mostMiss': 'The pins flew the farthest. Give “{bin}” the most coins.',
             'done': 'Close enough is great: nobody can count energy exactly by eye. What matters: 10 coins in, 10 coins out.'},
            {'k': 'cart', 'icon': '🛺', 't': 'Golf cart and ice cream cart', 'scene': 'cart', 'sfx': 'CRUNCH!',
             'alt': 'A model: a golf cart rolls into a parked ice cream cart. The golf cart stops, and the ice cream cart rolls away.',
             'bins': [{'k': 'ice', 'icon': '🍦', 't': 'Ice cream cart moving', 'need': 'most', 'ev': 'Rosa’s cart rolled about 3 feet.', 'sam': 5},
                      {'k': 'golf', 'icon': '🛺', 't': 'Golf cart still moving', 'need': 'zero', 'ev': 'Gus’s golf cart stopped dead.', 'sam': 0},
                      {'k': 'sound', 'icon': '🔊', 't': 'Sound', 'need': 'some', 'ev': 'CRUNCH! The whole boardwalk heard it.', 'sam': 1},
                      {'k': 'dent', 'icon': '🌡️', 't': 'Heat and the dent', 'need': 'some', 'ev': 'Both bumpers dented and felt warm.', 'sam': 4}],
             'zeroMiss': 'Look at the clue: Gus’s golf cart stopped dead. Can “{bin}” keep any coins?',
             'someMiss': 'Look at the clue under “{bin}”: {ev} So some energy went there.', 'mostMiss': 'Which one moved the most after the crash? Give “{bin}” the most coins.',
             'done': 'The golf cart kept zero coins, but none disappeared. They went into Rosa’s cart, the CRUNCH and the warm dents.'}],
        'q': 'What did the coin bank show about energy in a collision?',
        'opts': [{'t': 'Every bit of energy went somewhere: into motion, sound and heat.', 'ok': True},
                 {'t': 'Some of the energy disappeared.', 'miss': 'Did the Disappeared bin ever keep a coin?'},
                 {'t': 'All of it went into sound.', 'miss': 'Look at your bins. Which got the most coins?'}],
        'win': '10 coins in, 10 coins out. Nothing disappeared. Clue 2!'},
    'bumpercars': {
        'afterText': 'BOTH objects change how they move', 'kicker': 'Part 2 game', 'title': 'Bumper cars',
        'todo': ['Set each car’s speed with − and +.', 'Predict who will change how it moves.', 'Press Crash! and read both speedometers. Do all 3 rounds.'],
        'why': {'icon': '🚗', 'q': 'What is a speedometer?', 't': 'A dial that shows how fast something is going, here in miles per hour (mph).'},
        'alt': 'A model: two bumper cars on a rink, a red one and a blue one.', 'model': 'a model', 'e': 0.5, 'unit': 'mph', 'max': 6, 'bonk': 'BONK!',
        'cars': {'a': {'t': 'Red car', 'c': '#E8636B'}, 'b': {'t': 'Blue car', 'c': '#2D7AA6'}},
        'speedWord': 'Set the speeds', 'stillWord': 'still', 'predictQ': 'Predict: after the crash, who will change how it moves?',
        'preds': [{'k': 'a', 't': 'Only the red car'}, {'k': 'b', 't': 'Only the blue car'}, {'k': 'both', 't': 'BOTH cars'}],
        'predMiss': 'Make a prediction first. Who will change how it moves?', 'runBtn': 'Crash!', 'nextBtn': 'Next round', 'againBtn': 'Try other speeds',
        'beforeWord': 'Before', 'afterWord': 'After', 'both': 'BOTH cars changed.',
        'words': {'slowed': 'slowed down', 'sped': 'sped up', 'stopped': 'stopped', 'turned': 'turned around', 'started': 'started moving', 'still': 'stayed still', 'same': 'kept the same speed'},
        'rightPre': 'Your prediction was right! ', 'wrongPre': 'Surprise! ',
        'rounds': [
            {'k': 'still', 'icon': '1️⃣', 't': 'One still', 'sub': 'Round 1: the blue car is parked. The red car bumps it.', 'a': 5, 'b': 0, 'aMin': 2, 'aMax': 6, 'bMin': 0, 'bMax': 0, 'bDir': 0,
             'line': 'The mover passed most of its motion to the parked car.'},
            {'k': 'same', 'icon': '2️⃣', 't': 'Same way', 'sub': 'Round 2: both cars go the same way. The fast red car catches the slow blue car.', 'a': 6, 'b': 2, 'aMin': 3, 'aMax': 6, 'bMin': 1, 'bMax': 5, 'bDir': 1,
             'limitMiss': 'Keep the red car faster than the blue car, so it can catch up.', 'line': 'The fast car slowed down and the slow car sped up.'},
            {'k': 'toward', 'icon': '3️⃣', 't': 'Head on', 'sub': 'Round 3: the cars drive toward each other.', 'a': 4, 'b': -3, 'aMin': 1, 'aMax': 6, 'bMin': 1, 'bMax': 6, 'bDir': -1,
             'line': 'Both slowed down, and at least one turned around.'}],
        'q': 'In every bumper-car crash, who changed how it moved?',
        'opts': [{'t': 'BOTH cars, every time.', 'ok': True},
                 {'t': 'Only the car that was hit.', 'miss': 'Look at the red car’s speedometer before and after. Did it change?'},
                 {'t': 'Only the faster car.', 'miss': 'Check the slower car’s speedometers too.'}],
        'win': 'The mover doesn’t always win. Both cars changed every time. Clue 3!'},
    'crashlab': {
        'afterText': 'Now be the scientist', 'kicker': 'Part 4 game', 'title': 'The crash lab',
        'todo': ['Pick two balls: steel, rubber or clay.', 'Predict the AFTER, then press Crash them.', 'Switch on the heat camera. Where did it get warm? Do all three pairs.'],
        'why': {'icon': '📷', 'q': 'What is a heat camera?', 't': 'A camera that sees warmth instead of light. Warm spots show up bright yellow and orange; cool things look dark blue.'},
        'alt': 'A model: one ball rolls along a table toward a ball that is sitting still.', 'model': 'a model',
        'predictQ': 'Predict the AFTER:', 'predMiss': 'Predict the AFTER first.', 'pickMiss': 'Pick a pair of balls first.', 'crashBtn': 'Crash them',
        'camBtn': 'Heat camera ON', 'camOff': 'Heat camera OFF', 'camFirst': 'Crash the balls first, then look with the heat camera.', 'camNudge': 'Now switch on the heat camera.',
        'rightPre': 'Your prediction was right! ', 'wrongPre': 'Surprise! ',
        'preds': [{'k': 'pass', 't': 'The moving ball stops, and the still ball rolls away'}, {'k': 'stick', 't': 'They stick together and roll slowly'}, {'k': 'back', 't': 'The moving ball bounces straight back'}],
        'pairs': [
            {'k': 'steel', 'icon': '⚪', 't': 'Steel balls', 'c': '#AAB4BE', 'e': 0.95, 'sound': 'CLICK! (loud)', 'heat': 'a tiny bit warmer', 'glow': 0.25, 'ok': 'pass',
             'after': 'Mover stopped; other rolled away fast',
             'line': 'Steel balls bounce apart cleanly: almost all the motion passed to the other ball. The loud click took a little energy, and the heat camera shows only a tiny warm spot.'},
            {'k': 'rubber', 'icon': '🔴', 't': 'Rubber balls', 'c': '#E8636B', 'e': 0.75, 'sound': 'thump', 'heat': 'warmer', 'glow': 0.55, 'ok': 'pass',
             'after': 'Mover almost stopped; other rolled a bit slower',
             'line': 'Rubber squishes a little when it hits. More of the motion turned into heat, so the other ball rolled away a bit slower.'},
            {'k': 'clay', 'icon': '🟤', 't': 'Clay balls', 'c': '#B98C5E', 'e': 0.0, 'sound': 'splat (quiet)', 'heat': 'warmest!', 'glow': 0.95, 'ok': 'stick',
             'after': 'Stuck together; rolled slowly',
             'line': 'Clay squished flat and stuck. Lots of the motion turned into heat and a dent, so they rolled away slowly, together.'}],
        'tableLabel': 'My crash lab table', 'cols': ['Ball pair', 'After', 'Sound', 'Heat camera'],
        'photo': {'head': 'The real thing: a heat camera at work',
                  'img': I('heat-rub'), 'alt': 'Two frames from a real heat-camera video. Left: a wooden stick rubs a wooden board, and the spot glows yellow and orange. Right: the stick is gone, but an orange warm mark stays on the board.',
                  'cap': 'A real heat-camera video. Left: someone rubs a wooden stick hard on a wooden board, and the spot glows warm (yellow and orange). Right: the stick is gone, but the warm mark stays for a while. Rubbing and bumping both turn motion into heat.',
                  'credit': 'Frames from “Heat by friction” by Laserlicht, CC BY-SA 4.0, via Wikimedia Commons.'},
        'q': 'The clay balls slowed down the most. Where did their “missing” motion energy go?',
        'opts': [{'t': 'Into heat and squishing the clay (and a little sound).', 'ok': True},
                 {'t': 'It disappeared.', 'miss': 'Look at the heat camera. What glowed the brightest?'},
                 {'t': 'Into the table.', 'miss': 'The table didn’t move. Where did the heat camera show a warm spot?'}],
        'win': 'The squishiest crash made the warmest spot. The “missing” energy became heat. Clue 4!'},
    'exploreMod': 'crashlab',
    'strike': {
        'after': '.fs-solve', 'kicker': 'Bonus game · unlocked after the case', 'title': 'Strike!',
        'todo': ['Drag the slider to aim. Pick a speed.', 'Roll! Every pin that falls passes energy to the pins behind it.', '3 lanes, up to 9 stars.'],
        'why': {'icon': '🎳', 'q': 'Why do falling pins knock down other pins?', 't': 'A falling pin is moving, so it carries energy. When it hits another pin, it passes some of that energy on: a chain of collisions.'},
        'lockLine': 'Crack the case first. Then Strike! opens.', 'alt': 'A model: a bowling lane seen from above, with the pins at the far end and the ball at the near end.', 'model': 'a model',
        'aimLabel': 'Aim (drag left or right)', 'rollBtn': 'Roll!', 'nextBtn': 'Next lane',
        'speeds': [{'k': 'slow', 't': 'Slow', 'coins': 4}, {'k': 'med', 't': 'Medium', 'coins': 7}, {'k': 'fast', 't': 'Fast', 'coins': 10}],
        'levels': [{'name': 'Warm-up lane', 'pins': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'need': 7, 'tip0': 'Knock down 7 or more pins for 2 stars. Every pin for 3!'},
                   {'name': 'Pick up the spare', 'pins': [3, 6, 9, 10], 'need': 3, 'tip0': 'Only 4 pins left, on the right. Aim carefully!'},
                   {'name': 'Go for the strike', 'pins': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 'need': 9, 'tip0': 'Can you knock down all 10? You’ll need lots of energy and a perfect aim.'}],
        'lines': {'lane': 'Lane', 'pinsWord': 'pins down', 'all': 'STRIKE! Every pin fell.', 'some': 'Nice roll!', 'none': 'Gutter! The ball missed the pins.',
                  'aimTip': 'Aim closer to the front pin, so the falling pins knock the others.', 'speedTip': 'Try a faster roll: more energy coins to pass along.',
                  'again': 'Reset the pins', 'done': 'You bowled every lane!'}},
    'tool': {
        'name': 'Sound level meter', 'icon': '🔊', 'tab': 'assignment', 'after': '#tab-assignment .activity-card', 'key': '21-tool', 'sim': 'soundmeter',
        'kicker': 'Bonus · Tool of the Week', 'teaser': 'Measure a whisper, a clap, a slammed door and more. Which collisions are loudest?',
        'done': 'You measured every sound. A sound level meter sticker is in your Field Notebook.',
        'why': {'icon': '🔊', 'q': 'What does a sound level meter do?', 't': 'It has a small microphone that measures how loud a sound is, in units called decibels (dB). A louder bang means more energy turned into sound.'},
        'soundmeter': {
            'title': 'How loud is that collision?', 'model': 'a model',
            'todo': ['Tap a sound to play it and measure it.', 'Watch the needle and read the decibels (dB).', 'Measure all 7. Your loudness ladder builds itself.'],
            'aboutWord': 'about', 'notCollWord': 'not a collision', 'ladderLabel': 'Your loudness ladder', 'quietWord': 'quietest', 'loudWord': 'loudest',
            'safeLine': 'Hearing experts say sounds of 85 dB or more can hurt your ears if you hear them for a long time.',
            'sounds': [
                {'k': 'whisper', 'icon': '🤫', 't': 'A whisper', 'db': 30, 'coll': False, 's': 'whisper', 'note': 'Very little energy. It’s here so you can compare.'},
                {'k': 'tap', 'icon': '✏️', 't': 'A pencil tap', 'db': 45, 'coll': True, 's': 'tap', 'note': 'A tiny, gentle collision: a tiny bit of sound.'},
                {'k': 'talk', 'icon': '🗣️', 't': 'Talking', 'db': 60, 'coll': False, 's': 'talk', 'note': 'Normal talking, so you can compare.'},
                {'k': 'bounce', 'icon': '🏀', 't': 'A basketball bounce', 'db': 70, 'coll': True, 's': 'bounce', 'note': 'Every bounce is a collision with the floor.'},
                {'k': 'clap', 'icon': '👏', 't': 'A hard clap', 'db': 75, 'coll': True, 's': 'clap', 'note': 'Your hands collide hard, and part of that energy becomes sound.'},
                {'k': 'book', 'icon': '📕', 't': 'A dropped textbook', 'db': 80, 'coll': True, 's': 'book', 'note': 'A heavy book hits the floor. Part of its energy becomes a BANG.'},
                {'k': 'slam', 'icon': '🚪', 't': 'A slammed door', 'db': 85, 'coll': True, 's': 'slam', 'note': 'A big, fast collision: lots of energy turns into sound.'}],
            'q': {'q': 'Which collisions turned the most energy into sound?',
                  'opts': [{'t': 'The biggest, hardest bumps: the slammed door and the dropped book.', 'ok': True, 'why': 'Right! Harder collisions send more energy into sound, so the meter reads more decibels.'},
                           {'t': 'The whisper.', 'why': 'A whisper isn’t a collision, and it was the quietest of all.'},
                           {'t': 'They all made the same amount of sound.', 'why': 'Look at your ladder. Are all the bars the same length?'}]}},
        'credit': ''},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'A collision needs TWO things. What happens when two objects meet?', 'C': 'Sunlight hitting a leaf moves light energy. A collision is two objects bumping.'},
        'q2': {'B': 'Remember the coin bank? Did any coin land in Disappeared?', 'C': 'Energy can’t double. The coin bank always had 10 in and 10 out.'},
        'q3': {'A': 'A guess isn’t a prediction. What could you look at first?', 'B': 'Waiting means it’s too late to predict! What can you see BEFORE the crash?'}},
    'flags': {
        'ans-2': [
            {'label': 'both players', 're': 'both|each|two|they|players'},
            {'label': 'how motion changes', 're': 'slow|stop|bounce|back|turn|direction|change|fall|knock|speed'},
            {'label': 'a sport example', 're': 'soccer|football|basketball|hockey|baseball|tackle|player|ball|game|sport|run'}],
        'ans-3': [
            {'label': 'energy', 're': 'energy'},
            {'label': 'transfer', 're': 'transfer|moves|goes|passes'},
            {'label': 'why it helps', 're': 'crumple|crush|bend|dent|squish|heat|safe|protect|people|inside|hurt|less'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|doesn|does not|never'},
            {'label': 'two pieces of evidence', 'any': ['clap', 'palm', 'warm', 'heat', 'sound', 'crunch', 'crash', 'coin', 'bank', 'bumper', 'car', 'speed', 'heat camera', 'clay', 'dent', 'rosa', 'cart', 'rolled', 'motion', 'pins'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-2': 15, 'ans-3': 15, 'cer-4': 30},
    'hints': {
        'ans-2': ['Think about Round 3 of Bumper cars: the cars drove toward each other.', 'What happened to EACH car? Did it slow, stop or turn around?', 'Try: When two players run into each other, the first one ___ and the second one ___.'],
        'ans-3': ['Look at the crash test photo in the case file. Which part got crushed?', 'Think about the clay balls. Squishing turned motion into heat and a dent.', 'Try: The front crumples so the energy is transferred into ___ instead of ___.'],
        'cer-4': ['First decide: does the energy really disappear?', 'Think about the clap machine, the coin bank and the heat camera.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'Hard claps made a louder sound AND warmer palms.',
                'In the coin bank, every coin went to motion, sound or heat. None disappeared.',
                'The heat camera showed warm spots where the balls crashed.',
                'Rosa heard a CRUNCH, her cart rolled, and the dented bumper felt warm.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · the fender bender', 'length': '20–30 s',
                    'script': 'Crunch! There was a crash on the boardwalk. Read the accident report and look at the drawing. Gus wrote that his cart’s energy just disappeared. Read his note. Can energy really vanish? Let’s find out where it went.'},
        'warmup': {'label': 'Warm-Up · the clap machine (Clue 1)', 'length': '20–30 s',
                   'script': 'Your hands can collide too! Pick a round, gentle or hard. Then clap as fast as you can. Watch the sound meter jump, and watch the palms glow warmer. Which round made more sound and more heat?'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Clap once for “collision”; roll a ball into another for “motion change”.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · the energy coin bank (Clue 2)', 'length': '20–30 s',
                  'script': 'Press Play the crash and watch the ball hit the pins. Then drag every energy coin out of the bank, to where the energy went. Read the clue under each bin. Can a coin go in Disappeared? Try it!'},
        'part2': {'label': 'Part 2 · bumper cars (Clue 3)', 'length': '20–30 s',
                  'script': 'Bumper cars! Set each car’s speed with the minus and plus buttons. Predict who will change, then press Crash. Read both speedometers. Does the moving car always win?'},
        'explore': {'label': 'Part 4 · the crash lab (Clue 4)', 'length': '25–35 s',
                    'script': 'Welcome to the crash lab. Pick two balls: steel, rubber or clay. Predict the after, then crash them. Now switch on the heat camera. Where did it get warm?'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s',
                       'script': 'Do you have all four clues? Crack the case at the top of this tab, and a bowling game opens. Then answer two questions, fill in your before and after, and finish your C-E-R.'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · before and after', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says all the energy disappears when two cars crash. Hmm. Think about your claps and the heat camera. Pick your side, tap two pieces of evidence, then explain how they prove your claim.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 21.02 (testing collision predictions).',
                    'script': 'Case closed! Gus’s energy never disappeared. It moved into Rosa’s cart, the crunch and the warm dent. Next time, you’ll run your own trials to test collision predictions.'},
    },
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Your glowing palms (Warm-Up)',
        'A balanced coin bank (The Lesson)',
        'Two speedometers after a crash (The Lesson)',
        'The heat camera’s warmest spot (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['The bumper-car crash', 'The clay balls before and after', 'Rosa’s cart rolling away'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 3,
                           'prompts': ['Draw the BEFORE and the AFTER', 'Add motion arrows', 'Label where the energy went']}]},
    'hlCoach': copy.deepcopy(Q['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🔩', 'name': 'A bolt from the dented bumper',
                 'line': 'You cracked Case 21, and a bolt from the dented bumper goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next time: test your own collision predictions.'},
    'notebookTitle': 'Unit 5 · Energy, Motion & Collisions',
    'notebook': copy.deepcopy(O['notebook']),
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You’re ready for some crashes.',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'list', 'find': {'sel': '.fs-game[data-mod="clapper"]'},
         'label': 'Warm-Up: three ways to make a still marble move', 'q': 'Warm-Up: Three ways I could make a still marble start moving',
         'title': 'Your turn: name three ways to make a still marble start moving.', 'min': 3, 'unit': 'ways', 'addLabel': '+ Add another',
         'ph': ['Flick it with a finger', 'Roll another marble into it', 'Something else…']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Describe the BEFORE, the AFTER'},
         'label': 'Part C: Before and after', 'q': 'Part C: The BEFORE, the AFTER and where the energy went', 'title': 'My before and after',
         'fields': [{'t': 'The collision', 'icon': '💥', 'ph': 'Two things that bumped: ___ and ___'},
                    {'t': 'BEFORE: what was moving, and how fast?', 'icon': '⏪', 'ph': 'Before the crash, ___ was moving ___ and ___ was ___.'},
                    {'t': 'AFTER: what is moving now?', 'icon': '⏩', 'ph': 'After the crash, ___'},
                    {'t': 'Where did the energy go? (motion, sound, heat)', 'icon': '⚡', 'ph': 'The energy went into ___, ___ and ___.', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Does all the energy disappear when two cars crash?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-2': 'Part B · Question 5', 'ans-3': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] == '21.01': n.update({'icon': '🔩', 'name': 'A bolt from the dented bumper'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'In a collision, energy moves into motion, sound and heat, and none of it disappears.',
    'key': ['collision', 'energy', 'motion', 'sound', 'heat', 'disappears'],
    'small': ['In', 'a', 'and', 'of', 'it'],
    'model': 'A scientist might highlight “collision”, “motion, sound and heat” and “none of it disappears”. Those words hold the big idea. Small words like “a” and “of” don’t carry the idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me explain what happens to energy when two objects bump?']

# ---------------------------------------------------------------- Spotlight: what lights up as Sam talks
EV = '#tab-assignment .act-body > div:has(> .fs-plan)'
D['cues'] = {
    'welcome': [{'at': '^report', 'sel': '.fs-casecard .fs-notice', 'fx': 'glow'},
                {'at': '^drawing', 'sel': '.fs-casecard .fs-rpt-dia', 'fx': 'pop'},
                {'at': '^Gus', 'sel': '.fs-casecard .fs-memo', 'fx': 'glow'},
                {'at': '^note', 'sel': '.fs-casecard .fs-memo p', 'fx': 'trace'},
                {'at': '^went', 'sel': '.fs-casecard .fs-case-ask', 'fx': 'glow'}],
    'warmup': [{'at': '^round', 'sel': '.fs-clp-pick', 'fx': 'pop', 'scroll': True},
               {'at': '^clap$', 'sel': '.fs-clp-btn', 'fx': 'point'},
               {'at': '^meter', 'sel': '.fs-clp-stage', 'fx': 'glow', 'tag': 'Sound meter'},
               {'at': '^palms', 'sel': '.fs-clp-stage', 'fx': 'pop', 'tag': 'Warm palms'},
               {'at': '^Which', 'sel': '.fs-clp-res', 'fx': 'glow'}],
    'part1': [{'at': '^Play', 'sel': '.fs-cbk-play', 'fx': 'point', 'scroll': True},
              {'at': '^coin', 'sel': '.fs-cbk-bank', 'fx': 'pop'},
              {'at': '^clue', 'sel': '.fs-cbk-bins', 'fx': 'glow'},
              {'at': '^Disappeared', 'sel': '.fs-cbk-bin.lost', 'fx': 'wiggle'}],
    'part2': [{'at': '^speed$', 'sel': '.fs-bmp-ctl', 'fx': 'glow', 'scroll': True},
              {'at': '^Predict', 'sel': '.fs-bmp-pred', 'fx': 'pop'},
              {'at': '^Crash', 'sel': '.fs-bmp-run', 'fx': 'point'},
              {'at': '^speedometers', 'sel': '.fs-bmp-gauges', 'fx': 'glow'}],
    'explore': [{'at': '^balls', 'sel': '.fs-cl-tabs', 'fx': 'pop', 'scroll': True},
                {'at': '^Predict', 'sel': '.fs-cl-pred', 'fx': 'glow'},
                {'at': '^crash', 'sel': '.fs-cl-go', 'fx': 'point'},
                {'at': '^heat', 'sel': '.fs-cl-cam', 'fx': 'point'},
                {'at': '^warm', 'sel': '.fs-cl-stage', 'fx': 'glow'}],
    'assignment': [{'at': '^clues', 'sel': '.fs-board', 'fx': 'glow'},
                   {'at': '^Crack', 'sel': '.fs-solve', 'fx': 'pop', 'scroll': True},
                   {'at': '^bowling', 'sel': '.fs-game[data-mod="strike"]', 'fx': 'glow'},
                   {'at': '^two$', 'sel': '#tab-assignment .pq', 'fx': 'glow', 'all': True, 'scroll': True},
                   {'at': '^before$', 'sel': '#tab-assignment .fs-in-frame', 'fx': 'pop', 'scroll': True},
                   {'at': '^C-E-R$', 'sel': '#tab-assignment .fs-cer', 'fx': 'glow', 'scroll': True}],
    'evidence': [{'at': '^classmate', 'sel': EV + ' > p', 'i': 0, 'fx': 'trace'},
                 {'at': '^claps', 'sel': '.fs-plan .fs-opt', 'i': 2, 'fx': 'glow'},
                 {'at': '^camera', 'sel': '.fs-plan .fs-opt', 'i': 4, 'fx': 'glow'},
                 {'at': '^side', 'sel': '.fs-plan .fs-plan-row', 'i': 0, 'fx': 'pop'},
                 {'at': '^explain', 'sel': '.fs-cer .fs-cer-row', 'i': 2, 'fx': 'glow', 'scroll': True}],
    'closing': [{'at': '^closed', 'sel': '.fs-specimen', 'fx': 'pop', 'scroll': True},
                {'at': '^cart', 'sel': '.fs-solve', 'fx': 'glow'},
                {'at': '^Next', 'sel': '#tab-assignment .callout-tip', 'fx': 'glow'}],
}
D['fold'] = {'bulletin': {'icon': '📱', 'tease': 'Rosa from the ice cream cart left Sam a voicemail. Can you hear where the energy went?', 'open': 'Listen'},
             'strike': {'icon': '🎳', 'tease': 'Bowl 3 lanes and watch falling pins pass energy down the line. Can you get 9 stars?', 'open': 'Play'}}
D['cueWords'] = json.load(open('cuewords.json', encoding='utf-8')) if os.path.exists('cuewords.json') else {}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
