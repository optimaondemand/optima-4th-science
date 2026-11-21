#!/usr/bin/env python3
"""Writes data.json and fixes.json for 23.01 (run from this folder). Case 23 "The Canal Hum" (Sam Park, Palmetto Beach; based on the real
Cape Coral / Punta Gorda canal hum, traced to black drum fish by USF and Mote scientist James Locascio with hydrophones).
New: case.paper (a newspaper front page + letters), holdstop (Warm-Up: make a real thing ring, press and hold it to stop the sound),
wiggle (Part 1: wiggle a tuning fork, the push passes dot to dot to an eardrum through air, water or a wall), tuner (Part 2: tune a rubber
band by ear to 3 notes, then louder is not higher), rulerlab (Part 3 = the old Explore: 2 / 6 / 10 inch ruler, pull and let go, table),
drumfish (after the case: a real black drum photo + the swim-bladder model + a chorus model), column (Ask the Engineer + SOLVED stamp),
concert (bonus, folded), SIMS.hydrophone (Tool of the Week)."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../18-01/data.json', encoding='utf-8'))
O = json.load(open('../22-02/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
PS = '<p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)
def I(n): return 'images/23-01-' + n + '.jpg'

# ---------------------------------------------------------------- labels (standing approval)
fx('fix', 'unit label: “Ecosystems & Energy” is a leftover; weeks 18–24 are Unit 5', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Energy, Motion &amp; Collisions</div>')
fx('fix', 'sound is physical science, not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standards label: Florida benchmark first; TEKS is a Texas code that isn’t in the plan', '<div class="info-value">SC.4.P.10.3 · TEKS 4.8(A)</div>', '<div class="info-value">SC.4.P.10.3</div>')
# ---------------------------------------------------------------- ticked fixes (Bethany, 21 Nov 2026)
# 22.01 leftovers in the Warm-Up
fx('fix', '22.01 leftover: the toaster warm-up → the case + the hold-it-to-stop-it game',
   '<p>Think about a toaster. You drop in cold bread. A minute later, you pull out hot toast.</p>',
   '<p>Every sound you have ever heard started the same way. Make each thing below ring, then stop it with your hand.</p>')
fx('fix', '22.01 leftover: the toaster sketch → a list of sounds at home (on the page)',
   "<p>In your notebook, draw a quick sketch of a toaster. On one side, label what goes IN. On the other, label what comes OUT. (Hint: bread on both sides — but something invisible is also going in. What is it?)</p>",
   '<p>Now listen around you. What is vibrating to make each sound?</p>')
fx('fix', '22.01 leftover: Notice & Wonder about the toaster',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Notice &amp; Wonder</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover: “energy can CONVERT … toasters” callout',
   r'<div class="callout callout-tip">\s*<span class="callout-icon">💡</span>\s*<p>Today you\'ll learn that energy can CONVERT.*?</p>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover: Stop & Reason about “the three devices above”',
   r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
# 9.01 leftovers
fx('fix', '9.01 leftover: Part C was a food chain; the checklist already asks for a sound model', '🎨 Part C &mdash; Build Your Own Food Chain', '🎨 Part C &mdash; My Sound Model')
fx('fix', '9.01 leftover: Part C task (now a sound model typed on the page + a required labeled sketch)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Show how a sound gets from a vibrating thing to an ear. Fill in your model below, then sketch it.</p>', True)
fx('fix', '9.01 leftover: Reflect asked about a hawk; the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'supply list: a ruler for the ruler test', r'<span class="need-chip"><span>✏️</span>Colored pencils</span>', '<span class="need-chip"><span>📏</span>A ruler (to try it for real)</span>', True)

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; plain words; no dash',
   r"<p>Hold this question in your head as you work\. By the end of the lesson.*?</p>",
   "<p>Keep this question in mind. By the end, you’ll explain what sound is and why fast vibrations sound high.</p>", True)
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', 'no dash; two examples (Part 1)',
   'Pluck a rubber band. Tap a desk. Strum a guitar string. Stand near a speaker and feel the air buzz. Every one of those sounds happens because something is moving back and forth very fast — a ',
   'Pluck a rubber band. Strum a guitar string. Each sound happens because something is moving back and forth very fast. That is a ')
SND = '<span class="vtip">sound<span class="vtip-box"><span class="vtip-word">Sound</span>Wave energy from a vibration.</span></span>'
fx('plain', 'no dash; the misconception moves here, next to the wave idea, and leads into the game (Part 1)',
   'When the wave reaches your ear, it shakes your eardrum — and your brain turns that shaking into ' + SND + '.</p>',
   'When the wave reaches your ear, it shakes your eardrum, and your brain hears it as ' + SND + '.</p>\n      <p><strong>Watch out:</strong> sound is NOT a tiny thing flying through the air. The air just shakes in place and passes the push along. Be the vibration and watch.</p>')
fx('fix', '22.01 leftover: the Warm-Up title and subtitle named the toaster lesson', '<div class="act-title">🌅 Warm-Up: What Goes In, What Comes Out?</div>\n        <div class="act-subtitle">A familiar device, a hidden change</div>',
   '<div class="act-title">🌅 Warm-Up: Every Sound Starts Somewhere</div>\n        <div class="act-subtitle">Make it ring, then stop it</div>')
fx('plain', 'no dash (Part 2)', 'Pitch depends on how FAST the source is vibrating — its ', 'Pitch depends on how FAST the source is vibrating: its ')
fx('plain', 'no dash; leads into the game (Part 2)',
   "<p>You've probably noticed: a short rubber band stretched tight makes a HIGH twang. A long, loose one makes a LOW twang. The tighter and shorter the band, the faster it vibrates — and the higher the pitch you hear.</p>",
   "<p>A short, tight rubber band makes a HIGH twang. A long, loose one makes a LOW twang. Shorter and tighter means faster vibrations and a higher pitch. Try to tune one by ear.</p>")
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'shorter closing; no dash; points to 23.02',
   r'Next lesson, we\'ll leave sound waves behind and look at moving AIR and WATER — and how they can do work for us\.',
   'Next lesson: moving air and moving water, and the work they can do.', True)
fx('plain', 'Part B question 6 label (Gathered Answers)', 'data-label="Explain how a guitar makes a higher pitch when you..."', 'data-label="Shorter guitar string, higher pitch"')
fx('plain', 'Part B question 7 label (Gathered Answers)', 'data-label="Why is it possible to FEEL sound on a speaker but ..."', 'data-label="Feel it but not see it"')

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: Stop & Think (the wiggle game is Part 1’s thinking stop)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'the misconception paragraph moved to Part 1 (next to the wave idea)',
   r'\s*<p><strong>Common misconception:</strong> Some people think sound is something invisible flying.*?</p>', '', True)
fx('cut', 'lean: Key Concept box (the games and the diagram carry it)',
   r'<div style="background:#FFF6E5;border:2\.5px solid #F0C97A;[^"]*">\s*<div[^>]*>⭐ Key Concept</div>.*?</div>\s*', '', True)
fx('cut', 'removed: the Four Florida Sounds tap diagram (its thunder line was wrong: you feel and hear thunder at the same time; its tree frog line said the vocal sac vibrates, but the vocal cords do and the sac makes it louder), Observe & Reason, the dolphin fact, the Florida connection and Go Deeper (lean). Part 3 = the old Explore (the ruler test); the next button goes to Self-Check',
   r'<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">Four Florida Sounds</h3>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 3 · Pluck, Tap, Listen</h3>\n      ' + PS + 'Test it like a scientist. A ruler hanging off a desk vibrates just like a guitar string. Change ONE thing, how much hangs off the edge, and listen.</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its ruler steps are now Part 3; its manatee fact was wrong: manatee chirps are high squeaks, not low rumbles; the thunder puzzle and Go Deeper go with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 5 removed (Bethany kept 6 and 7; Q5 named the removed diagram)', r'<div class="pq">\s*<span class="pq-num"[^>]*>5</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 6 and 7 answered')
fx('cut', 'lean: Part C typed on the page, plus the required sketch', 'A sound model labeled with vibrating source, wave, and ear — plus two mini-waves for high vs. low pitch.',
   'My sound model: the vibrating source, the wave, the ear, and what makes high and low pitch. Plus your labeled sketch.')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', r'<strong>Evidence Response:</strong> I made a claim about whether sound is a "flying object" or a "wave," and supported it with two pieces of evidence\.',
   '<strong>Use Your Evidence:</strong> My claim about whether sound is a tiny flying ball, with two pieces of evidence.', True)
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Download your field journal (it has your answers and your sketch) and upload it to the Canvas assignment. Or copy your Gathered Answers (above) into Canvas.', True)

# ---------------------------------------------------------------- the story
SAM = Q['crew']['sam']
GAZ_SVG = ('<svg viewBox="0 0 300 150" role="img" aria-label="A drawing of houses along a canal at night, with a moon."><rect width="300" height="150" fill="#3A3F4A"/>'
           '<circle cx="246" cy="30" r="14" fill="#EDE6CF"/><path d="M20 92 V60 l30 -18 l30 18 V92z M110 92 V56 l34 -20 l34 20 V92z M200 92 V64 l26 -16 l26 16 V92z" fill="#20242B"/>'
           '<rect x="44" y="66" width="12" height="10" fill="#E8D9A8"/><rect x="138" y="62" width="12" height="10" fill="#E8D9A8"/><rect x="220" y="70" width="12" height="10" fill="#555"/>'
           '<rect y="92" width="300" height="58" fill="#2A3038"/><path d="M0 104 h300 M0 118 h300 M0 132 h300" stroke="#4A515C" stroke-width="2" stroke-dasharray="20 14"/></svg>')
D = {
    'lesson': '23.01', 'week': 23, 'day': 1, 'guide': 'sam', 'prefix': 'g4sci-23-1', 'manifestKey': '23-01',
    'paths': P['paths'], 'crew': {'sam': SAM},
    'expedition': {'num': 23, 'title': 'The Canal Hum'},
    'ambient': {'icon': '🌙', 'label': 'Night sounds'},
    'case': {
        'num': 23, 'title': 'The Canal Hum', 'style': 'gazette',
        'hook': 'The Gazette asked me to find a mystery hum. Rule number one of sound: something has to be vibrating. Let’s find out what, and how the sound gets inside those houses.',
        'paper': {'name': 'The Palmetto Beach Gazette', 'date': 'Tuesday, January 13', 'price': '50¢',
                  'headline': 'Mystery hum keeps canal neighbors awake', 'deck': 'A low sound starts after dark. Nobody can find where it comes from.',
                  'photo': {'svg': GAZ_SVG, 'cap': 'Pelican Canal at night (drawing).'},
                  'body': ['Every night this winter, families along Pelican Canal hear a low hum. It starts after sunset and keeps going past midnight.',
                           '“It sounds like a big truck waiting outside,” said one neighbor. “But nothing is there.”',
                           'Some neighbors say they can FEEL it buzzing in their walls and floors. The Gazette asked engineer Sam Park to find the source.'],
                  'lettersHead': 'Letters to the Editor',
                  'letters': [{'t': 'It must be a ship’s engine way out in the bay.', 'sign': 'R. Ortiz'},
                              {'t': 'My cousin says it’s a generator. Or ghosts!', 'sign': 'Pat, age 9'},
                              {'t': 'In my yard it is quiet. Inside my house by the water, the walls hum.', 'sign': 'D. Lee'}]},
        'stills': [],
        'question': 'What is making the canal hum, and how does it get into the houses?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'holdstop', 'icon': '✋', 'where': 'Warm-Up: hold it to stop it', 't': 'Every sound comes from something vibrating. Stop the vibration, and the sound stops. So something near the canal is vibrating.'},
            {'id': 'wiggle', 'icon': '〰️', 'where': 'The Lesson, Part 1: be the vibration', 't': 'Sound is a vibration passed along as a wave. Air, water and even walls just shake in place and pass the push along.'},
            {'id': 'tuner', 'icon': '🎸', 'where': 'The Lesson, Part 2: match the note', 't': 'Slow vibrations make a LOW pitch. Fast vibrations make a HIGH pitch. The hum is low, so its source vibrates slowly.'},
            {'id': 'rulerlab', 'icon': '📏', 'where': 'The Lesson, Part 3: the ruler test', 't': 'The longer the ruler, the slower it vibrated and the lower it sounded. A low hum comes from a slow vibration.'},
        ],
        'solve': {
            'title': 'What is making the canal hum?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'A ship’s engine far out in the bay, sending tiny sound balls through the air.', 'why': 'Check Clue 2. Sound isn’t tiny balls flying. And the hum is loudest by the canal, inside the houses.'},
                {'t': 'Something in the canal water vibrating slowly. Its low waves travel through the water, the ground and the walls into the houses.', 'right': True,
                 'why': 'Case cracked! Something in the water vibrates slowly (a low pitch), and the waves travel through water, ground and walls. Meet the hum-maker just below!'},
                {'t': 'A very LOUD sound, because loud sounds are always low.', 'why': 'Check Clue 3. Loudness is how BIG a vibration is. Pitch is how FAST. A whistle can be loud AND high.'},
                {'t': 'Nothing is vibrating. Some sounds just happen by themselves.', 'why': 'Check Clue 1. Every sound starts with something vibrating.'},
            ]},
    },
    'holdstop': {
        'afterText': 'Make each thing below ring, then stop it with your hand', 'kicker': 'Warm-Up game', 'title': 'Hold it to stop it',
        'todo': ['Press “Make it ring” on a picture.', 'Then press and HOLD the picture to stop it. Listen!', 'Stop all 4.'],
        'why': {'icon': '✋', 'q': 'What does your hand do?', 't': 'When you hold something that is ringing, your hand stops it from shaking back and forth.'},
        'ringBtn': '🔔 Make it ring', 'holdLine': 'Now press and HOLD the picture.', 'firstLine': 'Make it ring first. Then press and hold it.', 'countWord': 'stopped', 'holdMs': 700,
        'items': [
            {'id': 'bell', 'img': I('bell'), 'alt': 'A big brass ship’s bell.', 't': 'Ship’s bell', 'freq': 523, 'type': 'sine', 'wob': 2.76, 'decay': 7, 'what': 'The bell’s metal was shaking. Your hand stopped it, and the ringing stopped.'},
            {'id': 'guitar', 'img': I('guitar'), 'alt': 'Hands playing the strings of an acoustic guitar.', 't': 'Guitar string', 'freq': 196, 'type': 'triangle', 'wob': 2.0, 'decay': 5, 'what': 'The string was shaking. Hold it still, and the sound stops.'},
            {'id': 'fork', 'img': I('tuning-fork'), 'alt': 'A metal tuning fork lying on a wooden table.', 't': 'Tuning fork', 'freq': 288, 'type': 'sine', 'wob': 6.25, 'decay': 8, 'what': 'Its two metal prongs were shaking. Squeeze them, and it goes quiet.'},
            {'id': 'chimes', 'img': I('chimes'), 'alt': 'Metal wind chimes hanging outside.', 't': 'Wind chimes', 'freq': 1046, 'type': 'sine', 'wob': 2.4, 'decay': 5, 'what': 'The metal tubes were shaking. Grab them, and the sound stops.'}],
        'credits': 'Ship’s bell, USS Vestal (1908): Naval History and Heritage Command, CC BY 2.0. Close up of an acoustic guitar being played: Nataev, CC BY-SA 4.0. Tuning Fork 288 Hz: K. Venkataramana, CC0 (turned sideways). Wind chimes: Kim Dae Jeung, CC0. All via Wikimedia Commons.',
        'q': 'What did your hand really stop?',
        'opts': [{'t': 'The vibration. No vibration, no sound.', 'ok': True},
                 {'t': 'The sound flying out of it.', 'miss': 'Did anything fly out? What did your hand feel, and stop?'},
                 {'t': 'The light shining on it.', 'miss': 'Light doesn’t make sound. What was the thing doing before you held it?'}],
        'win': 'No vibration, no sound. Something by the canal must be vibrating. Clue 1!'},
    'wiggle': {
        'afterText': 'Be the vibration and watch', 'kicker': 'Part 1 game', 'title': 'Be the vibration',
        'todo': ['Drag left and right, again and again, in the orange strip (or press a wiggle button).', 'Watch the dots pass the push to the ear. Keep your eye on the red dot.', 'Send the sound through air, canal water and a house wall.'],
        'why': {'icon': '〰️', 'q': 'What are the dots?', 't': 'A model of the tiny bits that air, water and walls are made of. They’re much too small to see.'},
        'model': 'a slowed-down model', 'meWord': 'watch me', 'redLine': 'The red dot is one bit of air. Does it reach the ear?', 'dragLine': 'Drag here: left, right, left, right!',
        'slowBtn': '🐢 Wiggle it slowly', 'fastBtn': '🐇 Wiggle it fast', 'pathLabel': 'What is the sound moving through?',
        'slowWord': 'Slow vibration → LOW pitch', 'fastWord': 'Fast vibration → HIGH pitch', 'idleWord': 'Wiggle the fork!',
        'heardWord': 'The eardrum is shaking: you hear it!', 'lateWord': 'in this slowed model',
        'paths': [{'k': 'air', 'icon': '💨', 't': 'Air', 'secs': 1.2, 'note': 'In air, the bits are far apart. The push moves slowest here.'},
                  {'k': 'water', 'icon': '🌊', 't': 'Canal water', 'secs': 0.3, 'note': 'In water, the bits are packed closer. The push moves about 4 times faster than in air.'},
                  {'k': 'wall', 'icon': '🧱', 't': 'A house wall', 'secs': 0.12, 'note': 'In solid wood or concrete, the push moves even faster. A hum from outside can make a wall buzz.'}],
        'taskLabel': 'Try all of these',
        'tasks': {'ear': 'Make the eardrum shake', 'slow': 'Wiggle slowly: a LOW pitch', 'fast': 'Wiggle fast: a HIGH pitch', 'paths': 'Send it through air, water and a wall'},
        'q': 'Look at the red dot. Did it travel to the ear?',
        'opts': [{'t': 'No. It only rocked back and forth and passed the push along.', 'ok': True},
                 {'t': 'Yes. It flew all the way to the ear.', 'miss': 'Watch the red dot again. Does it ever get to the ear?'},
                 {'t': 'It disappeared.', 'miss': 'Look again. The red dot is still there. What is it doing?'}],
        'win': 'Sound is a vibration passed along, not a flying thing. And it moves through water and walls, too. Clue 2!'},
    'tuner': {
        'afterText': 'Try to tune one by ear', 'kicker': 'Part 2 game', 'title': 'Match the note',
        'todo': ['Press “Play the target note” and listen.', 'Make the band shorter or longer, looser or tighter. Then pluck it.', 'Match all 3 notes by ear. The counter shows how fast it vibrates.'],
        'why': {'icon': '🎸', 'q': 'Why a rubber band?', 't': 'A rubber band works like a guitar string. It’s an easy way to see what changes the pitch.'},
        'model': 'a model', 'base': 100, 'lens': [12, 9, 6, 4, 3], 'tights': [1, 2, 3, 4], 'unit': 'inches long',
        'targets': [{'id': 'mid', 't': 'Middle note', 'f': 200}, {'id': 'low', 't': 'Low note', 'f': 100}, {'id': 'high', 't': 'High note', 'f': 400}],
        'lenLabel': 'Length', 'shortBtn': 'Shorter', 'longBtn': 'Longer', 'tightLabel': 'Tightness (turn the peg)', 'looseBtn': 'Looser', 'tightBtn': 'Tighter',
        'playBtn': '🎯 Play the target note', 'pluckBtn': '🎸 Pluck it', 'perSec': 'vibrations each second', 'perSecShort': 'each second',
        'lowLine': 'Too LOW: it vibrates too slowly. Make it vibrate faster.', 'highLine': 'Too HIGH: it vibrates too fast. Make it vibrate slower.', 'matchLine': 'A match! {n} vibrations each second.',
        'r2Label': 'Round 2: louder or higher?', 'r2Line': 'Pluck it gently, then hard. Watch the counter.', 'softBtn': '🤏 Pluck gently', 'hardBtn': '💪 Pluck HARD',
        'softWord': 'Gentle pluck', 'hardWord': 'Hard pluck', 'loudWord': 'How big the swing is (amplitude)',
        'loudQ': {'q': 'Plucking HARD made the sound…', 'opts': [
            {'t': 'Louder, but the same pitch.', 'ok': True},
            {'t': 'Higher.', 'miss': 'Look at the counter. Did the vibrations each second change?'},
            {'t': 'Lower.', 'miss': 'Look at the counter. Did the vibrations each second change?'}]},
        'q': 'How do you make a HIGHER pitch?',
        'opts': [{'t': 'Make it vibrate faster: shorter or tighter.', 'ok': True},
                 {'t': 'Pluck it harder.', 'miss': 'Harder made it louder. Did the counter go up?'},
                 {'t': 'Make it longer and looser.', 'miss': 'Try it! Did the pitch go up or down?'}],
        'win': 'Fast = high. Slow = low. A big swing = loud. The canal hum is low, so its source vibrates slowly. Clue 3!'},
    'rulerlab': {
        'afterText': 'how much hangs off the edge, and listen', 'kicker': 'Part 3 game', 'title': 'The ruler test',
        'todo': ['Pick how much ruler hangs over the edge: 2, 6 or 10 inches.', 'Drag the red tip down and let go (or press Pluck it). Listen.', 'Pick the pitch you heard. Fill all 3 rows of the table.'],
        'why': {'icon': '📏', 'q': 'Why change only ONE thing?', 't': 'If you change only the length, you know the length is what changed the pitch. That makes it a fair test.'},
        'model': 'a slowed-down model', 'unit': 'inches', 'lenLabel': 'How much hangs over the edge?',
        'lens': [{'L': 2, 'f': 375}, {'L': 6, 'f': 42}, {'L': 10, 'f': 15}],
        'pitches': [{'k': 'high', 't': 'High'}, {'k': 'mid', 't': 'Medium'}, {'k': 'low', 't': 'Low'}],
        'pitchKey': {'2': 'high', '6': 'mid', '10': 'low'},
        'missPitch': {'high': 'Listen again. A short ruler twangs very fast. Was it a high buzz or a low thwap?',
                      'mid': 'Listen again. Compare it with the other lengths. Is it in the middle?',
                      'low': 'Listen again. A long ruler flaps slowly: thwap, thwap. High or low?'},
        'pitchQ': 'What pitch did you hear at {L} inches?', 'pluckBtn': '👇 Pluck it', 'pullLine': 'Drag the red tip down and let go, or press Pluck it.',
        'countLine': 'About {n} vibrations each second', 'slowLine': '(The picture is slowed way down so you can see it.)',
        'tableHead': ['Ruler over the edge', 'Pitch I heard', 'Vibrations each second'],
        'q': 'What changed the ruler’s pitch?',
        'opts': [{'t': 'The length hanging off. Shorter → faster vibrations → higher pitch.', 'ok': True},
                 {'t': 'How hard I plucked it.', 'miss': 'Plucking harder makes it louder. Look at your table: what did you change?'},
                 {'t': 'The color of the ruler.', 'miss': 'The ruler never changed color! What did you change?'}],
        'win': 'Shorter = faster = higher. Longer = slower = lower. A deep hum means a slow vibration. Clue 4!'},
    'exploreMod': 'rulerlab',
    'drumfish': {
        'after': '.fs-solve', 'kicker': 'Case closed · the real hum-maker', 'title': 'Meet the black drum',
        'todo': ['Look at the real fish.', 'Press Play to hear a model of their night chorus.'],
        'lockLine': 'Crack the case first. Then meet the hum-maker.',
        'img': I('black-drum'), 'alt': 'A young black drum fish with dark stripes and small whiskers under its chin.',
        'cap': 'A young black drum. Its stripes fade as it grows. See the little whiskers (barbels) under its chin? They help it feel for food.',
        'credit': 'Black drum (Pogonias cromis): Smithsonian Environmental Research Center, CC BY 2.0, via Wikimedia Commons.',
        'modelLabel': 'a model', 'key': [{'c': '#C8553D', 't': 'drumming muscle'}, {'c': '#7FA6C2', 't': 'swim bladder (an air-filled bag)'}],
        'facts': [{'icon': '🐟', 't': 'Black drum are big fish that live in Florida’s bays, rivers and canals. Big ones can weigh more than 50 pounds.'},
                  {'icon': '🥁', 't': 'To drum, a special muscle squeezes the fish’s swim bladder (an air-filled bag inside it) again and again, very fast. The bladder vibrates like a drum.'},
                  {'icon': '🌙', 't': 'They drum at night in winter and early spring, when they gather to lay eggs. The sound is LOW and very strong.'},
                  {'icon': '🏠', 't': 'This really happened in Florida! In canals in Cape Coral and Punta Gorda, people heard black drum inside their homes. Scientists found them with hydrophones (underwater microphones).'}],
        'playBtn': '▶ Play a model of the night chorus', 'stopBtn': '■ Stop', 'chorusLine': 'Made with computer sounds. It’s a model, not a real recording.',
        'win': 'Mystery solved: the hum was fish! A vibrating muscle, a low pitch, and waves through water, ground and walls.'},
    'column': {
        'after': '.fs-solve', 'kicker': 'Case closed · write back', 'title': 'Ask the Engineer',
        'todo': ['Pick what is making the hum.', 'Pick two pieces of evidence.', 'Print Sam’s answer in the paper.'],
        'lockLine': 'Crack the case first. Then answer the letter.',
        'paper': 'The Palmetto Beach Gazette', 'head': 'Ask the Engineer',
        'letter': 'Dear Engineer: What is that hum, and how does it get into my house? ~ Sleepless on Pelican Canal',
        'causeQ': 'What is making the hum?',
        'causes': [{'t': 'Black drum fish drumming in the canal', 'ok': True, 'say': 'The hum comes from black drum fish in the canal. A muscle squeezes each fish’s swim bladder, and the bladder vibrates.'},
                   {'t': 'A ship’s engine far away', 'miss': 'Then the hum would be loudest out in the bay. Where is it loudest?'},
                   {'t': 'Ghosts', 'miss': 'Fun idea! But what does every sound need?'}],
        'evQ': 'Pick two pieces of evidence:',
        'evidence': [{'t': 'The hum is LOW, so its source vibrates slowly.', 'ok': True},
                     {'t': 'Sound waves travel through water, ground and walls, so walls can buzz.', 'ok': True},
                     {'t': 'It starts after dark, when black drum gather to lay eggs.', 'ok': True},
                     {'t': 'Sound is made of tiny balls.', 'miss': 'Check Clue 2. Is sound a flying thing?'}],
        'evLead': 'Here is how I know:', 'lead': 'Dear Sleepless,', 'printBtn': '🖨 Print my answer', 'stamp': 'SOLVED', 'sign': '~ Sam Park, engineer',
        'win': 'Printed! Pelican Canal knows the truth: the neighbors are fish.'},
    'concert': {
        'after': '.fs-solve', 'kicker': 'Bonus game', 'title': 'Canal concert',
        'todo': ['Pick a song.', 'Tap the rubber bands in the order of the numbers (or press keys 1 to 5).', 'No mistakes = 3 stars.'],
        'why': {'icon': '🎵', 'q': 'Why do the bands sound different?', 't': 'Each band is a different length. Shorter bands vibrate faster and sound higher.'},
        'pickLine': 'Pick a song. Then tap the bands in the order of the numbers.',
        'bands': [{'n': 1, 'f': 262, 'len': 100}, {'n': 2, 'f': 294, 'len': 89}, {'n': 3, 'f': 330, 'len': 79}, {'n': 4, 'f': 392, 'len': 67}, {'n': 5, 'f': 440, 'len': 60}],
        'songs': [{'id': 'buns', 't': 'Hot Cross Buns', 'notes': [3, 2, 1, 3, 2, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 2, 1]},
                  {'id': 'mary', 't': 'Mary Had a Little Lamb', 'notes': [3, 2, 1, 2, 3, 3, 3, 2, 2, 2, 3, 5, 5]}],
        'win': 'Two songs, all from vibrating bands. Bravo!'},
    'fold': {'concert': {'icon': '🎵', 'tease': 'Play two songs on five rubber bands. Shorter bands sound higher!', 'open': 'Play'}},
    'tool': {
        'name': 'Hydrophone', 'icon': '🎧', 'tab': 'assignment', 'after': '#tab-assignment .activity-card', 'key': '23-tool', 'sim': 'hydrophone',
        'kicker': 'Bonus · Tool of the Week', 'teaser': 'Drop an underwater microphone into the bay and the canal. When and where is the hum?',
        'done': 'You listened at every spot. A hydrophone sticker is in your Field Notebook.',
        'why': {'icon': '🎧', 'q': 'What is a hydrophone?', 't': 'A microphone that works underwater. Sound travels well in water, so scientists use hydrophones to listen to fish, whales and ships.'},
        'hydrophone': {
            'title': 'When and where is the hum?', 'model': 'a model',
            'todo': ['Tap a spot to drop the hydrophone in.', 'Watch the wave and listen.', 'Try all 3 spots.'],
            'img': I('hydrophone'), 'alt': 'A diver on the sandy sea floor writes notes next to a hydrophone on a stand, with fish swimming past.',
            'cap': 'A diver checks a hydrophone on the sea floor at Gray’s Reef National Marine Sanctuary, Georgia.',
            'credit': 'Photo: NOAA National Marine Sanctuaries (public domain), via Wikimedia Commons.',
            'screenLabel': 'HYDROPHONE · live wave',
            'spots': [{'k': 'bay', 'icon': '🌊', 't': 'Open bay', 'sub': 'noon', 'kind': 'crackle', 'amp': 0.6, 'f': 0,
                       'read': 'Crackle, crackle: HIGH clicks, fairly quiet.', 'note': 'That’s snapping shrimp, tiny shrimp that snap their claws shut. Lots of short, high sounds.'},
                      {'k': 'noon', 'icon': '☀️', 't': 'Pelican Canal', 'sub': 'noon', 'kind': 'tone', 'amp': 0.15, 'f': 3, 'f2': 60,
                       'read': 'Almost quiet: a faint, low hum of a boat far away.', 'note': 'Small, slow waves on the screen. No mystery hum during the day.'},
                      {'k': 'night', 'icon': '🌙', 't': 'Pelican Canal', 'sub': '9 PM', 'kind': 'knock', 'amp': 1, 'f': 6,
                       'read': 'BOOM-boom-boom: LOW and LOUD. Tall, slow waves.', 'note': 'Lots of low knocks at once, like a crowd of drums. That’s the hum!'}],
            'q': {'q': 'Where and when is the hum?', 'opts': [
                {'t': 'In the canal, at night.', 'ok': True, 'why': 'Yes! Real scientists in Cape Coral and Punta Gorda used hydrophones the same way to find the black drum chorus.'},
                {'t': 'In the open bay, at noon.', 'miss': 'Those were high crackles. Is the hum high or low?'},
                {'t': 'Everywhere, all the time.', 'miss': 'Compare the canal at noon and at 9 PM. Was it the same?'}]}}},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Think about the bell in the Warm-Up. Did light make it ring?', 'C': 'Think about the bell in the Warm-Up. What stopped the sound?'},
        'q2': {'A': 'Think about the ruler test. Did the longer ruler sound higher or lower?', 'B': 'In Match the Note, did the length change the counter?'},
        'q3': {'B': 'Faster changed the pitch. What did a HARD pluck change?', 'C': 'Think about Round 2 of Match the Note. What made it louder?'}},
    'flags': {
        'ans-2': [
            {'label': 'vibration', 're': 'vibrat|vibrait|vibrt|shak|back and forth|wiggl'},
            {'label': 'frequency', 're': 'frequen|frequn|frequancy|freqency|per second|each second|how fast|faster|quick'},
            {'label': 'higher pitch', 're': 'high|higher|squeak|pitch'}],
        'ans-3': [
            {'label': 'a wave', 're': 'wave|waive|vibrat|push'},
            {'label': 'why you can’t see it', 're': 'air|invisible|can.?t see|cannot see|too small|tiny|see through|clear'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|isn|is not|not a ball|no '},
            {'label': 'two pieces of evidence', 'any': ['dot', 'red', 'bell', 'hold', 'held', 'stop', 'wave', 'vibrat', 'push', 'rock', 'place', 'water', 'wall', 'fork', 'string', 'guitar', 'ruler'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-2': 15, 'ans-3': 15, 'cer-4': 30},
    'hints': {
        'ans-2': ['Think about Match the Note: what did shorter do to the counter?', 'Use VIBRATION and FREQUENCY (vibrations each second).', 'Try: A shorter string vibrates ___, so its frequency is ___, so the pitch is ___.'],
        'ans-3': ['Think about Be the Vibration: what were the dots doing?', 'Can you see air? Can you feel a push?', 'Try: You can feel it because ___. You can’t see it because the wave moves through ___.'],
        'cer-4': ['First decide: is sound a tiny ball that flies?', 'Think about the red dot and the bell you stopped.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'In Be the Vibration, the red air dot only rocked back and forth. It never flew to the ear.',
                'When I held the ringing bell still, the sound stopped. Sound needs a vibration.',
                'The canal hum traveled through water and walls, not just air.',
                'Sound is invisible, so it must be very tiny.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · the canal hum', 'length': '20–30 s'},
        'warmup': {'label': 'Warm-Up · hold it to stop it (Clue 1)', 'length': '20–30 s',
                   'script': 'Sam here. The Gazette asked me to find a mystery hum. Read the front page and the letters. Then, rule number one: every sound starts with something vibrating. Make each one ring, then press and hold the picture. What happens to the sound?'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Hum with fingers on your throat for “vibration”.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · be the vibration (Clue 2)', 'length': '20–30 s',
                  'script': 'This is a model of sound. Drag back and forth to wiggle the tuning fork. Watch the dots pass the push to the ear. Keep your eye on the red dot. Does it fly to the ear? Then send the sound through water and a wall.'},
        'part2': {'label': 'Part 2 · match the note (Clue 3)', 'length': '20–30 s'},
        'explore': {'label': 'Part 3 · the ruler test (Clue 4)', 'length': '25–35 s',
                    'script': 'Time for a real test. Pick how much ruler hangs off the desk, then drag the red tip down and let go. Listen, and pick the pitch you heard. Try all three lengths and watch the table fill in.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · my sound model', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says sound is a tiny ball that flies through the air. Is it? Think about the red dot, and the bell you stopped. Pick your side, tap two pieces of evidence, then explain. That’s your C-E-R.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 23.02 (moving air and water).'},
    },
    'videoOff': [],
    'lensVoice': False,
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'The Gazette’s front page (Warm-Up)',
        'The red air dot passing the push (The Lesson)',
        'Your matched high note (The Lesson)',
        'Your ruler table with all 3 rows (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['The canal hum', 'A ringing bell', 'A ruler twang'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch and label your sound model', 'required': True, 'minLabels': 3,
                           'prompts': ['Draw the vibrating thing', 'Draw the wave moving', 'Draw and label the ear']}]},
    'hlCoach': copy.deepcopy(Q['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🎧', 'name': 'The canal hum recording',
                 'line': 'You cracked Case 23, and the hydrophone recording of the black drum chorus goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next time: moving air and water.'},
    'notebookTitle': 'Unit 5 · Energy, Motion & Collisions',
    'notebook': copy.deepcopy(O['notebook']),
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. Time to listen!',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to see what it means.']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '#tab-vocab p', 'text': 'What is vibrating to make each sound?'},
         'label': 'Warm-Up: sounds around me', 'q': 'Warm-Up: Three sounds around you, and what is vibrating to make each one.', 'title': 'Three sounds around me', 'compact': True,
         'fields': [{'t': 'Sound 1 and what vibrates', 'icon': '🔊', 'ph': 'The ___ makes a sound because the ___ vibrates.'},
                    {'t': 'Sound 2 and what vibrates', 'icon': '🔊', 'ph': 'The ___ makes a sound because the ___ vibrates.'},
                    {'t': 'Sound 3 and what vibrates', 'icon': '🔊', 'ph': 'The ___ makes a sound because the ___ vibrates.'}]},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Fill in your model below'},
         'label': 'Part C: My sound model', 'q': 'Part C: My sound model (source, wave, ear, high and low pitch)', 'title': 'My sound model',
         'fields': [{'t': 'The vibrating source', 'icon': '🔔', 'ph': 'The ___ vibrates.'},
                    {'t': 'The wave: what it travels through', 'icon': '〰️', 'ph': 'The wave moves through ___.'},
                    {'t': 'The ear', 'icon': '👂', 'ph': 'The wave shakes the ___, and the brain ___.'},
                    {'t': 'High pitch', 'icon': '🐇', 'ph': 'A high pitch comes from a ___ vibration.'},
                    {'t': 'Low pitch', 'icon': '🐢', 'ph': 'A low pitch comes from a ___ vibration.', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Is sound a tiny ball that flies through the air?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-2': 'Part B · Question 6', 'ans-3': 'Part B · Question 7', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] == '23.01': n.update({'icon': '🎧', 'name': 'The canal hum recording'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'Every sound starts with a vibration, and faster vibrations make a higher pitch.',
    'key': ['sound', 'vibration', 'faster', 'vibrations', 'higher', 'pitch'],
    'small': ['every', 'with', 'a', 'and', 'make'],
    'model': 'A scientist might highlight “sound”, “vibration”, “faster” and “higher pitch”. Those words hold the big idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me explain what sound is, or why high notes sound different?']

EV = '#tab-assignment .act-body > div:has(> .fs-plan)'
D['cues'] = {
    'warmup': [{'at': '^front', 'sel': '.fs-gaz', 'fx': 'glow', 'scroll': True},
               {'at': '^letters', 'sel': '.fs-gaz-letters', 'fx': 'pop'},
               {'at': '^vibrating', 'sel': '.fs-hld-grid', 'fx': 'glow', 'scroll': True},
               {'at': '^ring', 'sel': '.fs-hld-go', 'i': 0, 'fx': 'point'},
               {'at': '^hold', 'sel': '.fs-hld-pic', 'i': 0, 'fx': 'pop'}],
    'part1': [{'at': '^model', 'sel': '.fs-wig-box', 'fx': 'glow', 'scroll': True},
              {'at': '^wiggle', 'sel': '.fs-wig-zone', 'fx': 'point'},
              {'at': '^dots', 'sel': '.fs-wig-svg', 'fx': 'pop', 'tag': 'bits of air'},
              {'at': '^red', 'sel': '.fs-wig-legend', 'fx': 'pop'},
              {'at': '^water', 'sel': '.fs-wig-paths', 'fx': 'glow'}],
    'explore': [{'at': '^ruler', 'sel': '.fs-rul-lens', 'fx': 'pop', 'scroll': True},
                {'at': '^tip', 'sel': '.fs-rul-go', 'fx': 'point'},
                {'at': '^pitch', 'sel': '.fs-rul-svg', 'fx': 'glow'},
                {'at': '^table', 'sel': '.fs-rul-t', 'fx': 'pop'}],
    'evidence': [{'at': '^classmate', 'sel': EV + ' > p', 'i': 0, 'fx': 'trace', 'scroll': True},
                 {'at': '^dot', 'sel': '.fs-plan .fs-opt', 'i': 2, 'fx': 'glow'},
                 {'at': '^bell', 'sel': '.fs-plan .fs-opt', 'i': 3, 'fx': 'glow'},
                 {'at': '^side', 'sel': '.fs-plan .fs-plan-row', 'i': 0, 'fx': 'pop'},
                 {'at': '^explain', 'sel': '.fs-cer .fs-cer-row', 'i': 2, 'fx': 'glow', 'scroll': True}],
}
D['cueWords'] = json.load(open('cuewords.json', encoding='utf-8')) if os.path.exists('cuewords.json') else {}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
