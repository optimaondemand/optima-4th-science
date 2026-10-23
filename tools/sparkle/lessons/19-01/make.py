#!/usr/bin/env python3
"""Writes data.json and fixes.json for 19.01 (run from this folder). Showcase lesson: Case 19 "The Downhill Derby".
Sam Park (Unit 5). New modules: flick (flour crater test), replay (scrub a marble-and-pencil replay), pinball (plunger + big-slow vs small-fast),
slowmo (a real NASA high-speed impact sequence as a flip book), drawpath (draw Dune Hill, measure the hay bale push, build the bars),
SIMS.radargun (Tool of the Week). The race-day announcer reuses bulletin (folded, news voice, tone:'start')."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../18-01/data.json', encoding='utf-8'))
R2 = json.load(open('../18-02/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
PS = '<p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

# ---------------------------------------------------------------- ticked fixes (Bethany, 22 Oct 2026)
fx('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist already asks for a slow/medium/fast data table',
   '🎨 Part C &mdash; Build Your Own Food Chain', '📏 Part C &mdash; My Speed and Energy Table')
fx('fix', 'copy-paste leftover: Part C task from 9.01 (now the data table from Part 4, typed on the page)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Fill in your table from Part 4: how far the hay bale slid from the Low, Middle and High starts. Then write what your numbers show.</p>', True)
fx('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'unit label: “Ecosystems & Energy” is a leftover; weeks 18–24 are Unit 5', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Energy, Motion &amp; Collisions</div>')
fx('fix', 'speed and energy is physical science, not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standard: 4-PS3-1 is the speed-and-energy standard (4-ESS3-1 is about energy resources)',
   '<div class="info-value">4-ESS3-1 · TEKS 4.8(A), 4.7(A)</div>', '<div class="info-value">4-PS3-1 · TEKS 4.8(A), 4.7(A)</div>')
fx('fix', 'standard detail matches 4-PS3-1', '<div class="info-detail">Energy Forms & Gravity Affects Motion</div>', '<div class="info-detail">Speed and Energy</div>')
fx('fix', 'the hailstone example was wrong (big hailstones fall faster, not slower); same idea with a true example, no dashes',
   r'<p><strong>Common misconception:</strong> Some people think energy is only about how big or heavy something is\..*?</p>',
   '<p><strong>Watch out:</strong> Some people think energy is only about how big or heavy something is. Size matters. But for two objects that are the same, the faster one ALWAYS has more energy. And speed counts a lot: a small baseball thrown fast can crack a window. A big beach ball rolling slowly just bumps it.</p>', True)
fx('fix', 'the misleading AI picture (the FAST car flies off a ramp that ends in mid-air; the arrows measure the gap, not how far the block slid) and the boxes that lean on it are gone; Pinball power replaces them and the tap diagram. Also lean: Key Concept (repeats Part 2), Stop & Reason, Observe & Reason, the Amazing Fact (hurricane wind is about 60 times walking speed, not 25), the Florida Highway Patrol note and Go Deeper. Part 3 = a real NASA slow-motion crash, Part 4 = the old Explore (Build Dune Hill); next button goes to Self-Check',
   r'<div class="lesson-figure scroll-reveal">\s*<div class="lesson-figure-label">⚡ Same Ball, Three Speeds, Three Effects</div>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 3 · A Crash in Slow Motion</h3>\n      ' + PS + 'NASA scientists study crashes, too. They fire a small ball at a target at up to 15,000 miles per hour, then film it with a super-fast camera.</p>\n' +
   '      ' + H3 + 'Part 4 · Build Dune Hill</h3>\n      ' + PS + 'Sam needs evidence for his hay bale plan. Draw a track from each start (Low, Middle and High), and measure how far the car pushes the bale.</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; plain words; no dash',
   "Hold this question in your head as you work. By the end of the lesson, you'll be able to use evidence — what you can see and measure — to explain why a fast-moving object carries more energy than a slow one.",
   "Keep this question in mind. By the end, you’ll use evidence (what you can see and measure) to explain why a fast object carries more energy than a slow one.")
fx('plain', 'the warm-up is the flour crater test now (Bethany’s hook); answers are made on the page',
   r"<p>Tap your finger gently on your desk\..*?</p>\s*<p>In your notebook, write down:.*?</p>",
   "<p>Here’s a test with a marble and a pan of flour. Drop the marble gently. Then throw it down fast. Which crater is bigger?</p>", True)
fx('plain', 'warm-up title matches the new warm-up', '🌅 Warm-Up: Soft Hit vs. Hard Hit', '🌅 Warm-Up: The Flour Crater Test')
fx('plain', 'warm-up subtitle; dash removed', 'Tap a finger on the desk — then tap harder', 'Drop it gently, then throw it fast')
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', 'no “go back to Lesson 9.01”; the meaning is given right here', 'Way back in Lesson 9.01, you learned that <span class="vtip">energy', '<span class="vtip">Energy')
fx('plain', 'no dash; lightning is mostly electrical energy, so a clearer example',
   'A walking person, a falling raindrop, a Florida lightning bolt — all of them have kinetic energy.', 'A walking person, a falling raindrop and a rolling marble all have kinetic energy.')
fx('plain', 'dashes removed', 'Same ball — different speed — different energy.', 'Same ball, different speed, different energy.')
fx('cut', 'lean: this paragraph repeats the rule (Pinball power is the next thinking stop)',
   r"\s*<p>Scientists call this the relationship between speed and energy\..*?</p>", '', True)
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'shorter closing; points to 19.02',
   r'<p><strong>Nicely done\.</strong> You can now describe how.*?</p>',
   '<p><strong>Nicely done.</strong> You showed that the faster something moves, the more energy it carries, and the bigger the change it can cause. Next time, Sam runs a fair test at Dune Hill: one change at a time, and lots of tries.</p>', True)

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: Stop & Think (Scrub the replay is the thinking stop for Part 1)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its ramp test becomes Part 4, Build Dune Hill; its chart becomes Part C)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 5 removed (Bethany kept 6 and 7; it pointed at the old tap diagram)', r'<div class="pq">\s*<span class="pq-num"[^>]*>5</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: renumber Part B (6 → 5)', '<span class="pq-num" style="background:#D4772C;">6</span>', '<span class="pq-num" style="background:#D4772C;">5</span>')
fx('cut', 'lean: renumber Part B (7 → 6)', '<span class="pq-num" style="background:#D4772C;">7</span>', '<span class="pq-num" style="background:#D4772C;">6</span>')
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C typed on the page',
   'A three-row data table showing slow/medium/fast trials with the target distance, sketches, and an evidence statement.',
   'My speed and energy table (Low, Middle and High starts) and what the numbers show. (A sketch is a bonus.)')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether speed matters for energy, and supported it with two pieces of evidence from the lesson or my test.',
   '<strong>Use Your Evidence:</strong> My claim about whether speed matters for energy, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', True)

# ---------------------------------------------------------------- the story
I = lambda n: 'images/19-01-' + n + '.jpg'
SAM = Q['crew']['sam']
C = {
    'car': 'Soap box derby racer (late 1960s design, a replica built by Bill Wrigley Jr.): Bill Wrigley (public domain)',
    'hill': 'Derby Downs, the derby hill in Akron, Ohio: Troop330 (CC BY-SA 3.0)',
    'finish': 'Soapbox race finish line in Differdange, Luxembourg: MMFE (CC BY-SA 4.0)',
    'impact': 'High-speed impact sequence: P. H. Schultz, Brown University, and the NASA Ames Vertical Gun Range (public domain)',
    'radar': 'A radar gun in use: U.S. Navy photo by Mass Communication Specialist 1st Class Hodges Pone (public domain)',
    'moon': 'Full Moon: NASA Goddard / Lunar Reconnaissance Orbiter (public domain)',
}
ALL = ' All via Wikimedia Commons. Palmetto Beach, Dune Hill and the derby are made up for this lesson.'
def cr(*ks): return '. '.join(C[k] for k in ks) + '.' + ALL

D = {
    'lesson': '19.01', 'week': 19, 'day': 1, 'guide': 'sam', 'prefix': 'g4sci-19-1', 'manifestKey': '19-01',
    'paths': P['paths'], 'crew': {'sam': SAM},
    'expedition': {'num': 19, 'title': 'The Downhill Derby'},
    'ambient': {'icon': '🌊', 'label': 'Ocean sounds'},
    'case': {
        'num': 19, 'title': 'The Downhill Derby', 'style': 'derby',
        'hook': 'Hi again! Palmetto Beach is holding its first Downhill Derby. Kids built cars with no motors, and gravity (the pull that brings things down) pulls them down Dune Hill. My job is the hay bales at the finish line, so every car stops safely.',
        'notice': {'head': 'PALMETTO BEACH DOWNHILL DERBY · RACE PROGRAM', 'title': 'Saturday, 10 AM, at Dune Hill',
                   'rows': [['Start ramps', 'Low, Middle and High (the top of the hill)'], ['Cars', 'Built by kids. No motors. Same size and weight rules.'],
                            ['Sam’s job', 'Plan the hay bales. How long a stopping zone does each ramp need?']],
                   'line': 'Safety first: every car must stop safely in the hay.'},
        'stills': [
            {'cam': 'A derby car', 'time': 'no motor, just gravity', 'tag': 'PHOTO 1', 'img': I('derby-car'), 'alt': 'A shiny red soap box derby car with four red wheels and an open seat.', 'kind': 'print'},
            {'cam': 'A real derby hill', 'time': 'Akron, Ohio', 'tag': 'PHOTO 2', 'img': I('derby-hill'), 'alt': 'A long, straight paved derby track running down a grassy hill between trees.', 'kind': 'print'},
            {'cam': 'A finish line', 'time': 'soft padding stops the cars', 'tag': 'PHOTO 3', 'img': I('derby-finish'), 'alt': 'A small derby car crossing a finish line on a street, with soft padded barriers along both sides and people watching.', 'kind': 'print'}],
        'stillsCredit': cr('car', 'hill', 'finish'),
        'question': 'Which start ramp needs the longest stopping zone (the most hay bales), and why?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'flick', 'icon': '🌕', 'where': 'Warm-Up: the flour crater test', 't': 'The faster marble made the bigger crater. Faster means more energy, and more energy makes a bigger change.'},
            {'id': 'replay', 'icon': '🎞️', 'where': 'The Lesson, Part 1: scrub the replay', 't': 'A moving object carries energy the whole time it moves. When it stops, the energy doesn’t vanish. It goes into what it hits, sound and a little warmth.'},
            {'id': 'pinball', 'icon': '🕹️', 'where': 'The Lesson, Part 2: pinball power', 't': 'A harder pull sent the ball faster and higher. And a small fast baseball beat a big slow bowling ball. Speed matters a lot.'},
            {'id': 'drawpath', 'icon': '🏁', 'where': 'The Lesson, Part 4: build Dune Hill', 't': 'Higher start, faster car. The car from the High start pushed the hay bale the farthest.'},
        ],
        'solve': {
            'title': 'Which ramp needs the most hay?', 'q': 'Which plan fits all four clues?',
            'options': [
                {'t': 'The Low ramp. Its cars are slowest, so they need the most help stopping.', 'why': 'Check Clue 4. Which start pushed the hay bale the farthest?'},
                {'t': 'Whichever ramp has the heaviest car. Weight is all that matters.', 'why': 'Check Clue 3. Did the big, slow bowling ball win?'},
                {'t': 'The High ramp. Its cars go fastest, so they carry the most energy and push the hay the farthest.', 'right': True,
                 'why': 'Case cracked! Faster cars carry more energy, so the High ramp gets the longest stopping zone. Now Sam can plan the hay bales.'},
                {'t': 'Every ramp the same. The energy disappears when a car stops anyway.', 'why': 'Check Clue 2. Where does the energy go when something stops?'},
            ]},
    },
    'flick': {
        'afterText': 'Which crater is bigger', 'kicker': 'Warm-Up game', 'title': 'The flour crater test',
        'todo': ['Press on the marble and flick it DOWN with your mouse. (Or tap the buttons.)', 'Make one slow drop and one fast drop. Then compare the two craters.'],
        'why': {'icon': '🌕', 'q': 'What is a crater?', 't': 'A bowl-shaped dent made when something hits a surface. Flour shows the dent clearly.'},
        'alt': 'A model: a marble held above a pan of flour, with a speed meter on the right.',
        'flickHint': 'Press on the marble and flick DOWN', 'model': 'a model', 'meterLabel': 'speed',
        'gentle': {'t': 'Gentle drop', 'v': 2}, 'hard': {'t': 'Hard throw', 'v': 9},
        'slowMax': 3, 'fastMin': 7, 'unit': 'cm',
        'startLine': 'No drops yet. Flick the marble!', 'midLine': 'That was a medium drop. Now try a very slow one or a very fast one.',
        'slowLabel': '🐢 Slow drop', 'fastLabel': '🚀 Fast drop',
        'q': 'Why was one crater bigger?',
        'opts': [{'t': 'The faster marble carried more energy, so it made a bigger change.', 'ok': True},
                 {'t': 'The marble got heavier when I threw it hard.', 'miss': 'It’s the same marble every time. What changed between your two drops?'},
                 {'t': 'The flour was softer the second time.', 'miss': 'The flour is smoothed the same way before every drop. What did YOU change?'}],
        'photo': {'img': 'images/18-02-moon.jpg', 'alt': 'The full Moon, covered with round craters.',
                  'cap': 'Real craters! Rocks from space hit the Moon very fast and blasted out these bowls.', 'credit': C['moon'] + '. Via Wikimedia Commons.'},
        'win': 'Same marble, same flour. Only the speed changed, and the fast drop made the bigger crater. That’s your first clue!'},
    'replay': {
        'afterText': 'that energy was there', 'kicker': 'Part 1 game', 'title': 'Scrub the replay',
        'todo': ['Drag the slider (or press ▶) to step through the replay.', 'At each frame, tap EVERY place the energy is right now. Then press Check.'],
        'why': {'icon': '🎞️', 'q': 'What is a replay?', 't': 'A video you can step through one frame (one still picture) at a time, like a sports replay on TV.'},
        'alt': 'A model: a marble rolling toward a pencil lying on a table.', 'model': 'a model',
        'ask': 'Where is the energy right now? Tap every place.', 'checkBtn': 'Check',
        'places': [{'k': 'marble', 'icon': '⚪', 't': 'In the moving marble'}, {'k': 'pencil', 'icon': '✏️', 't': 'In the moving pencil'},
                   {'k': 'sound', 'icon': '🔊', 't': 'In the CLICK sound'}, {'k': 'warm', 'icon': '♨️', 't': 'Spread out as a tiny bit of warmth'},
                   {'k': 'gone', 'icon': '🚫', 't': 'Nowhere. It’s gone.'}],
        'frames': [
            {'cap': 'The marble rolls toward the pencil.', 'm': 70, 'p': 380, 'mv': True, 'pv': False, 'ans': ['marble'],
             'hint': 'Is anything moving in this frame? A moving object carries energy, even before it hits anything.', 'gone': 'The marble is rolling! Anything that moves has energy.',
             'ok': 'Yes! The marble carries energy the whole time it rolls, not just when it hits.'},
            {'cap': 'CLICK! The marble hits the pencil.', 'm': 352, 'p': 380, 'mv': True, 'pv': True, 'sound': True, 'ans': ['marble', 'pencil', 'sound'],
             'hint': 'Three things happen at once: something is still moving, something starts to move, and something makes a noise.', 'gone': 'Look and listen! Things are moving and making a sound.',
             'ok': 'Right! The marble passes its energy to the pencil, and some becomes the CLICK sound.'},
            {'cap': 'The marble stops. The pencil slides and rubs on the table.', 'm': 356, 'p': 430, 'mv': False, 'pv': True, 'warm': True, 'ans': ['pencil', 'warm'],
             'hint': 'Which thing is still moving? And rub your hands together fast. What do you feel?', 'gone': 'The pencil is still sliding! Where is its energy?',
             'ok': 'Yes! The sliding pencil has the energy now, and rubbing on the table makes a tiny bit of warmth.'},
            {'cap': 'Everything has stopped.', 'm': 356, 'p': 452, 'mv': False, 'pv': False, 'warm': True, 'ans': ['warm'], 'allow': ['sound'],
             'hint': 'Nothing is moving now. But energy doesn’t vanish. Where did it spread out to?',
             'gone': 'Energy doesn’t vanish! The pencil rubbed the table and made a click. Where did that energy go?',
             'ok': 'Right! The energy didn’t disappear. It spread out as a tiny bit of warmth in the table and the air. It’s just too spread out to notice.'}],
        'q': 'When did the marble have energy?',
        'opts': [{'t': 'The whole time it was moving, even before the hit.', 'ok': True},
                 {'t': 'Only at the moment it hit the pencil.', 'miss': 'Look at frame 1. The marble hadn’t hit anything yet. Was it moving?'},
                 {'t': 'Only after it stopped.', 'miss': 'A stopped marble isn’t moving. Look at frame 4 again.'}],
        'win': 'A moving object carries energy the whole time it moves. When it stops, the energy goes somewhere else. Clue 2!'},
    'pinball': {
        'afterText': 'just bumps it', 'kicker': 'Part 2 game', 'title': 'Pinball power',
        'todo': ['Pull the plunger: drag the red knob down, or tap a pull.', 'Predict which light the ball will reach. Then press Let go.', 'Try all three pulls.'],
        'why': {'icon': '🕹️', 'q': 'How does a pinball plunger work?', 't': 'It’s a spring. Pull it back farther and it pushes the ball off faster. The table tilts uphill, so a faster ball climbs higher before it rolls back.'},
        'alt': 'A model pinball table tilted uphill, with a plunger lane on the right and three rows of lights.', 'model': 'a model',
        'pullLabel': '1. Pull the plunger', 'pullWord': 'Pull',
        'pulls': [{'k': 'little', 't': 'A little pull', 'f': 0.33}, {'k': 'half', 't': 'Halfway', 'f': 0.66}, {'k': 'full', 't': 'All the way', 'f': 1}],
        'rows': [{'k': 'r1', 't': 'Row 1', 'h': 0.1, 'pts': 100}, {'k': 'r2', 't': 'Row 2', 'h': 0.4, 'pts': 500}, {'k': 'r3', 't': 'Row 3', 'h': 0.9, 'pts': 1000}],
        'predictQ': '2. Predict: which light will the ball reach?', 'noneT': 'None', 'launchBtn': '3. Let go!',
        'startLine': 'Pull, predict, then let go!',
        'reachedLine': 'It reached {row}!', 'noneLine': 'It didn’t reach any lights.', 'rightLine': 'Your prediction was right.', 'wrongLine': 'Not what you predicted. That’s why scientists test!',
        'needPull': 'Pull the plunger back first.', 'needPred': 'Predict first: tap the light you think it will reach.',
        'holdLine': 'Good pull! Now predict which light it will reach, then press Let go.',
        'round2': {'kicker': 'Round 2', 'title': 'Big and slow vs. small and fast',
                   'todo': ['Each ball rolls at a row of three wooden blocks. Which one knocks them over?', 'Tap your prediction, then run the test.'],
                   'q1': 'Your prediction: tap a ball. Then run the test.', 'runBtn': 'Run the test',
                   'balls': [{'k': 'bowl', 'icon': '🎳', 'name': 'Bowling ball', 'sub': '16 pounds, rolled gently at 1 mile per hour', 'knock': False, 'line': 'Bump. The blocks scoot a little and stay up.'},
                             {'k': 'base', 'icon': '⚾', 'name': 'Baseball', 'sub': '5 ounces, thrown at 60 miles per hour', 'knock': True, 'line': 'SMACK! All three blocks go flying.'}],
                   'right': 'Your prediction was right!', 'wrong': 'Surprise! Look at what happened to each row of blocks.',
                   'needPick': 'Predict first: tap the ball you think will knock the blocks over.',
                   'why': 'The bowling ball is about 50 times heavier. But the baseball is 60 times faster, and speed counts extra. The fast baseball carries about 70 times more energy!'},
        'q': 'What does Pinball power show?',
        'opts': [{'t': 'Speed matters a lot. A small fast ball can carry more energy than a big slow one.', 'ok': True},
                 {'t': 'Heavier things always have more energy.', 'miss': 'Look at Round 2. Did the heavy bowling ball win?'},
                 {'t': 'Speed doesn’t change energy.', 'miss': 'Look at your three pulls. Which one climbed highest?'}],
        'win': 'Faster ball, more energy. Even a small ball can beat a big one when it’s fast. Clue 3!'},
    'slowmo': {
        'afterText': 'film it with a super-fast camera', 'kicker': 'The Lesson, Part 3', 'title': 'A crash in slow motion',
        'todo': ['Press Play in slow motion, or drag the slider one frame at a time.'],
        'why': {'icon': '🎥', 'q': 'What is a high-speed camera?', 't': 'A camera that takes thousands of pictures every second. A crash that is over in a blink can be seen step by step.'},
        'strip': I('impact-strip'), 'n': 25, 'rec': 'HIGH-SPEED CAMERA',
        'alt': 'A real NASA high-speed photo sequence in 25 frames: a very fast ball hits a target, a bright flash, then a spray of hot gas and broken bits flies out and a crater forms.',
        'caps': [{'from': 0, 't': 'Before: the target sits still.'}, {'from': 1, 't': 'The hit! The super-fast ball flashes as it strikes.'},
                 {'from': 2, 't': 'Hot gas and bits of the target spray out.'}, {'from': 7, 't': 'A cone-shaped curtain of debris (broken bits) grows wider and wider.'},
                 {'from': 16, 't': 'The debris falls back down.'}, {'from': 21, 't': 'A crater is left behind.'}],
        'q': 'Where did the ball’s energy go?',
        'opts': [{'t': 'Into the flash, the flying debris and blasting out the crater.', 'ok': True},
                 {'t': 'Nowhere. The ball just stopped.', 'miss': 'Look at frames 2 to 16. Something huge happened when it stopped!'},
                 {'t': 'Back into the launcher.', 'miss': 'Watch the target. What changed there?'}],
        'credit': C['impact'] + ', via Wikimedia Commons. The NASA Ames Vertical Gun Range in California can fire small balls at up to about 15,000 miles per hour.',
        'win': 'A small ball moving super fast carried enough energy to blast out a crater. Speed is powerful!'},
    'bulletin': {
        'afterText': 'film it with a super-fast camera', 'kicker': 'Bonus · Race day', 'title': 'The race-day announcer',
        'todo': ['Press Play and listen. You can read along on the paper.', 'Tap the three phrases that tell how FAST a car is going. A place is not a speed!'],
        'device': 'DUNE HILL P.A.', 'station': 'Palmetto Beach Downhill Derby · Heat 3', 'tone': 'start',
        'playBtn': 'Play the race call', 'againBtn': 'Play it again', 'audio': 'announcer', 'paperHead': 'RACE CALL · HEAT 3',
        'lines': [
            'And they’re off in Heat 3! Car 7 starts at [[x:That’s a place on the hill. Listen for words about how fast a car goes.|the top of Dune Hill]]. Car 12 starts at the Low ramp.',
            'Car 7 is [[fast|picking up speed]] all the way down!',
            'The radar gun says [[mph|twenty-two miles per hour]]!',
            'Car 12 rolls in [[slow|nice and slow]] and taps the hay bales.',
            'Car 7 hits the bales with a big WHUMP! They slid back almost two feet. That’s a lot of energy!'],
        'foundLabel': 'Speed words you found', 'dangerWord': 'Speed word', 'countIcon': '🏁', 'countWord': 'speed words found',
        'dangers': [{'id': 'fast', 'icon': '🚀', 't': 'Picking up speed', 'does': 'Car 7 goes faster and faster downhill'},
                    {'id': 'mph', 'icon': '📡', 't': '22 miles per hour', 'does': 'a speed measured with a radar gun'},
                    {'id': 'slow', 'icon': '🐢', 't': 'Nice and slow', 'does': 'Car 12 barely moves the bales'}],
        'win': 'Faster car, bigger push. You heard the case in action!'},
    'drawpath': {
        'afterText': 'measure how far the car pushes the bale', 'kicker': 'Part 4 game', 'title': 'Build Dune Hill',
        'todo': ['Press a flag on the tower (Low, Middle or High) and draw your hill down to the ground. Or tap the flag, then tap points.',
                 'Press Play. Then drag the red tape end to the bale (or tap the bale) to measure.',
                 'Do all three starts. Then drag each bar up to match your table.'],
        'why': {'icon': '🏁', 'q': 'How can a car go with no motor?', 't': 'Gravity pulls it downhill. The higher it starts, the faster it’s going at the bottom.'},
        'alt': 'A drawing area: a start tower on the left with Low, Middle and High flags, the ground, and a hay bale on the right.', 'model': 'a model',
        'starts': [{'k': 'low', 't': 'Low', 'h': 0.3}, {'k': 'mid', 't': 'Middle', 'h': 0.6}, {'k': 'high', 't': 'High', 'h': 0.9}],
        'unit': 'in', 'scale': 0.12, 'loss': 0.025, 'mph': 1.6, 'chartMax': 40,
        'playBtn': 'Play', 'eraseBtn': 'Erase my track',
        'lines': {'start': 'Start at a flag on the tower. Draw down to the ground.', 'hint': 'Start at a flag on the tower',
                  'tapMore': 'Now tap points down to the ground', 'notDown': 'Keep going: bring your track down to the ground', 'ready': 'Track ready. Press Play!',
                  'needStart': 'Start your track at one of the flags on the tower: Low, Middle or High.',
                  'measureFirst': 'Measure the push first: drag the red tape end to the bale.', 'speedWord': 'Speed',
                  'stallHead': 'Stuck!', 'stall': 'The car ran out of speed on a bump. A car can’t climb higher than where it started. Erase and try again.',
                  'measureHead': 'Measure the push', 'measure': 'Drag the red tape end to the front of the bale (or tap the bale).',
                  'measureMiss': 'Line the tape end up with the front edge of the bale.',
                  'recorded': 'Recorded! Press Erase my track and draw from another start.',
                  'colStart': 'Start', 'colPush': 'How far the bale slid', 'barMiss': 'Check each bar against your table. A bar turns green when it matches.'},
        'chartQ': 'Build your bar chart: drag each bar up (or tap in the column) to match your table.',
        'q': 'What does your bar chart show?',
        'opts': [{'t': 'The higher the start, the faster the car, and the farther it pushed the bale.', 'ok': True},
                 {'t': 'All three starts pushed the bale the same.', 'miss': 'Read your bars. Are they the same height?'},
                 {'t': 'The Low start pushed it the farthest.', 'miss': 'Which bar is the tallest?'}],
        'win': 'Higher start, faster car, more energy, bigger push. Clue 4!'},
    'exploreMod': 'drawpath',
    'tool': {'name': 'Radar speed gun', 'icon': '📡', 'tab': 'assignment', 'after': '#tab-assignment .activity-card', 'key': '19-tool', 'sim': 'radargun',
             'kicker': 'Bonus · Tool of the Week', 'teaser': 'Clock a soccer ball, a bike, a derby car and a fastball.',
             'done': 'You clocked four speeds like a pro. A radar gun sticker is in your Field Notebook.',
             'why': {'icon': '📡', 'q': 'How does a radar gun work?', 't': 'It sends out invisible radio waves. They bounce off a moving thing and come back changed. The faster the thing moves, the bigger the change, and the gun turns that into a speed.'},
             'radargun': {'title': 'Clock the speed', 'todo': ['Pick something to measure.', 'When it’s inside the yellow beam, pull the trigger (or tap the beam).'],
                          'img': I('radar-gun'), 'alt': 'A police officer aims a radar gun out of a patrol car window.', 'cap': 'A real radar gun at work.',
                          'trigger': 'Pull the trigger', 'logLabel': 'Speeds you measured',
                          'missLine': 'Nothing in the beam. Wait until it’s inside the yellow beam, then pull the trigger.',
                          'targets': [{'k': 'ball', 'icon': '⚽', 'name': 'Kicked soccer ball', 'mph': 30, 'pace': 0.05, 'note': 'A strong kick.'},
                                      {'k': 'bike', 'icon': '🚲', 'name': 'Bike', 'mph': 12, 'pace': 0.025, 'note': 'A steady ride.'},
                                      {'k': 'derby', 'icon': '🏎️', 'name': 'Derby car (High start)', 'mph': 22, 'pace': 0.04, 'note': 'Fast enough to need lots of hay!'},
                                      {'k': 'pitch', 'icon': '⚾', 'name': 'Fastball', 'mph': 90, 'pace': 0.09, 'note': 'A pro pitcher’s fastball.'}],
                          'q': {'q': 'Pretend the bike and the derby car weigh the same. Which one would push a hay bale farther?',
                                'opts': [{'t': 'The derby car. It’s going faster.', 'ok': True, 'why': 'Right! Same weight, more speed, more energy. That’s why the High ramp needs the most hay.'},
                                         {'t': 'The bike. It’s bigger.', 'why': 'We said they weigh the same. What’s different? Check your speeds.'},
                                         {'t': 'They’d push it the same.', 'why': 'Look at your speeds. Is one faster?'}]},
                          'credit': C['radar'] + '. Via Wikimedia Commons.'}},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Food energy is stored. Think about the word “kinetic.” What does it go with?', 'C': 'Sunlight is light energy. Which kind does every MOVING thing have?'},
        'q2': {'B': 'Think about your two flour craters. Did the slower drop make the bigger crater?', 'C': 'Same marbles, different speeds. Did the pinball ball climb the same height for every pull?'},
        'q3': {'A': 'Cups can’t think! What was different about the ball?', 'B': 'The ball stays the same weight. What changed between the rolls?'}},
    'flags': {
        'ans-2': [
            {'label': 'speed', 're': 'speed|fast|slow|quick'},
            {'label': 'the word evidence', 're': 'evidence'},
            {'label': 'energy or a change', 're': 'energ|crater|push|farther|further|higher|bigger|move|knock|change'}],
        'ans-3': [
            {'label': 'a moving thing at home', 're': 'ball|marble|car|door|toy|dog|cat|brother|sister|bike|fan|wind|water|rain|shoe|pillow|kick|throw|roll|drop|slam|bounc'},
            {'label': 'what it did', 're': 'knock|push|move|bang|sound|loud|noise|crash|fell|fall|broke|break|slid|dent|shook|shake|hit|bump'},
            {'label': 'details', 're': 'because|when|faster|fast|hard|slow|so |then'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|does matter|matters'},
            {'label': 'two pieces of evidence', 'any': ['crater', 'flour', 'marble', 'pinball', 'plunger', 'baseball', 'bowling', 'bale', 'hay', 'ramp', 'high', 'low', 'push', 'farther', 'higher', 'faster', 'bigger', 'chart', 'inches', 'nasa', 'pencil'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-2': 15, 'ans-3': 15, 'cer-4': 30},
    'hints': {
        'ans-2': ['Think about the flour craters and Pinball power. What happened when things went faster?', 'Use the word evidence: what did you SEE that proves it?', 'Try: Speed matters because ___. My evidence is ___.'],
        'ans-3': ['Think of something at home that moves: a ball, a door, a toy car.', 'What happens when it hits something fast? What do you see or hear?', 'Try: When I ___, it ___. That shows it had energy.'],
        'cer-4': ['First decide: does speed matter for energy?', 'Think about your craters, the pinball and your hay bale chart.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'The fast marble made a bigger flour crater than the slow one.',
                'Pulling the plunger all the way sent the pinball higher than a little pull.',
                'The small fast baseball knocked the blocks over. The big slow bowling ball didn’t.',
                'The car from the High start pushed the hay bale farther than the car from the Low start.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · the Downhill Derby', 'length': '30–40 s',
                    'script': 'Hi again! It’s Sam. Palmetto Beach is having its first Downhill Derby! Kids built cars with no motors, and they race down Dune Hill. My job is the hay bales at the finish line. Read the race program. Which start ramp needs the longest stopping zone? Let’s find out!'},
        'warmup': {'label': 'Warm-Up · the flour crater test (Clue 1)', 'length': '20–30 s',
                   'script': 'Let’s start with a crater test. Press on the marble and flick it down. Try a gentle drop first, then a really fast flick. Watch the crater grow. Then compare your two craters in the cards below.'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Walk slowly, then jog in place for “speed”; roll a ball for “motion”.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · scrub the replay (Clue 2)', 'length': '20–30 s',
                  'script': 'Here’s a replay of a marble rolling into a pencil. Drag the slider one frame at a time. At each frame, tap every place the energy is right now. Careful! The marble is moving before it hits anything.'},
        'part2': {'label': 'Part 2 · pinball power (Clue 3)', 'length': '20–30 s',
                  'script': 'Time for pinball! Pull the plunger back, then predict which light the ball will reach. Let go and watch it climb. Try a little pull, halfway, and all the way. Then comes Round 2: a big, slow bowling ball against a small, fast baseball.'},
        'part3': {'label': 'Part 3 · a crash in slow motion', 'length': '15–25 s',
                  'script': 'These are real photos from a NASA high-speed camera. Press Play, or drag the slider one frame at a time. Watch what a super fast ball does to the target.'},
        'explore': {'label': 'Part 4 · build Dune Hill (Clue 4)', 'length': '25–35 s',
                    'script': 'Now you design Dune Hill! Start at a flag on the tower and draw your track down to the ground. Press Play. Then drag the red tape to measure how far the hay bale slid. Do it from Low, Middle and High. Then build your bar chart.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s',
                       'script': 'Do you have all four clues? Crack the case at the top of this tab. Then answer two questions, fill in your speed table for Part C, and finish your C-E-R.'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · my speed table', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says speed doesn’t really matter. Hmm. Think about your craters, the pinball, and your hay bale numbers. Pick your side, tap two pieces of evidence in the planner, then explain how they prove your claim.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 19.02 (a fair test with trials).',
                    'script': 'Case closed! Cars from the High start go fastest and carry the most energy, so they get the longest stopping zone. Next time we test it for real at Dune Hill: one change at a time, and lots of tries!'},
    },
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Your two flour craters (Warm-Up)',
        'The pinball lighting Row 3 (The Lesson)',
        'The NASA crater in slow motion (The Lesson)',
        'Your Dune Hill bar chart (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['My fastest Dune Hill track', 'A fast crash and a slow bump', 'The derby finish line'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 3,
                           'prompts': ['Draw your Low, Middle and High tracks', 'Draw the hay bale after each run', 'Label the start heights']}]},
    'hlCoach': copy.deepcopy(Q['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🏁', 'name': 'Derby checkered flag',
                 'line': 'You cracked Case 19, and a derby checkered flag goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next time: a fair test at Dune Hill.'},
    'notebookTitle': 'Unit 5 · Energy, Motion & Collisions',
    'notebook': [{'lesson': w + '.0' + d} for w in ['18', '19', '20', '21', '22', '23', '24'] for d in ['1', '2']],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You’ll use every one of them at the derby.',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'list', 'find': {'sel': '.fs-game[data-mod="flick"]'},
         'label': 'Warm-Up: three things a moving object can do', 'q': 'Warm-Up: Three things a moving object can do that show it has energy',
         'title': 'Your turn: name three things a moving object can do that show it has energy.', 'min': 3, 'unit': 'things', 'addLabel': '+ Add another',
         'ph': ['Knock something over', 'Make a sound', 'Something else…']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'hide-nw', 'type': 'hide', 'find': {'sel': '.act-warmup .socratic-q', 'text': 'Notice'}},
        {'id': 'hide-tip', 'type': 'hide', 'find': {'sel': '.act-warmup .callout', 'text': 'microscope'}},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Fill in your table from Part 4'},
         'label': 'Part C: My speed and energy table', 'q': 'Part C: How far the hay bale slid from each start, and what the numbers show',
         'title': 'My speed and energy table',
         'fields': [{'t': 'LOW start: the bale slid…', 'icon': '🐢', 'ph': 'The bale slid ___ inches.'},
                    {'t': 'MIDDLE start: the bale slid…', 'icon': '🚲', 'ph': 'The bale slid ___ inches.'},
                    {'t': 'HIGH start: the bale slid…', 'icon': '🚀', 'ph': 'The bale slid ___ inches.'},
                    {'t': 'What my numbers show', 'icon': '📊', 'ph': 'Faster cars carry more energy because my evidence shows that…', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Does speed matter for energy?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-2': 'Part B · Question 5', 'ans-3': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] == '18.01': n.update({'icon': '🧫', 'name': 'Red tide sample slide'})
    if n['lesson'] == '18.02': n.update({'icon': '🎟️', 'name': 'Star party ticket'})
    if n['lesson'] == '19.01': n.update({'icon': '🏁', 'name': 'Derby checkered flag'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'The faster an object moves, the more energy it carries.',
    'key': ['faster', 'moves', 'more', 'energy', 'carries'],
    'small': ['The', 'an', 'it'],
    'model': 'A scientist might highlight “faster”, “more energy” and “carries”. Those words hold the big idea. Small words like “the” and “an” don’t carry the idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me explain how speed and energy are connected?']

# ---------------------------------------------------------------- Spotlight: what lights up as Sam talks
EV = '#tab-assignment .act-body > div:has(> .fs-plan)'
D['cues'] = {
    'welcome': [{'at': '^Derby', 'sel': '.fs-casecard .fs-case-t', 'fx': 'glow'},
                {'at': '^motors', 'sel': '.fs-casecard .fs-still', 'i': 0, 'fx': 'pop', 'tag': 'No motor!'},
                {'at': '^Hill', 'sel': '.fs-casecard .fs-still', 'i': 1, 'fx': 'pop'},
                {'at': '^finish', 'sel': '.fs-casecard .fs-still', 'i': 2, 'fx': 'wiggle'},
                {'at': '^program', 'sel': '.fs-casecard .fs-notice', 'fx': 'pop'},
                {'at': '^stopping', 'sel': '.fs-casecard .fs-notice dl', 'fx': 'trace'}],
    'warmup': [{'at': '^crater', 'sel': '.fs-game[data-mod="flick"] .fs-why', 'fx': 'glow', 'scroll': True},
               {'at': '^flick$', 'sel': '.fs-fk-stage', 'fx': 'point', 'tag': 'Flick DOWN'},
               {'at': '^gentle', 'sel': '.fs-fk-btns .fs-btn', 'i': 0, 'fx': 'pop'},
               {'at': '^fast', 'sel': '.fs-fk-btns .fs-btn', 'i': 1, 'fx': 'pop'},
               {'at': '^grow', 'sel': '.fs-fk-stage', 'fx': 'glow'},
               {'at': '^cards', 'sel': '.fs-fk-cards', 'fx': 'wiggle'}],
    'part1': [{'at': '^replay', 'sel': '.fs-rpl-scene', 'fx': 'glow', 'scroll': True},
              {'at': '^slider', 'sel': '.fs-rpl-range', 'fx': 'point'},
              {'at': '^frame', 'sel': '.fs-rpl-strip', 'fx': 'pop'},
              {'at': '^tap', 'sel': '.fs-rpl-ask .fs-in-chips', 'fx': 'reveal'},
              {'at': '^moving', 'sel': '.fs-rpl-cap', 'fx': 'trace'}],
    'part2': [{'at': '^pinball', 'sel': '.fs-pb-svg', 'fx': 'glow', 'scroll': True},
              {'at': '^plunger', 'sel': '.fs-pb-pulls', 'fx': 'pop', 'tag': 'Pull'},
              {'at': '^predict', 'sel': '.fs-pb-preds', 'fx': 'pop'},
              {'at': '^Let', 'sel': '.fs-pb-go', 'fx': 'point'},
              {'at': '^halfway', 'sel': '.fs-pb-log', 'fx': 'trace'},
              {'at': '^Round', 'sel': '.fs-game[data-mod="pinball"] .fs-todo', 'fx': 'glow'}],
    'part3': [{'at': '^NASA', 'sel': '.fs-smo-view', 'fx': 'glow', 'scroll': True},
              {'at': '^Play', 'sel': '.fs-smo-play', 'fx': 'point'},
              {'at': '^slider', 'sel': '.fs-smo-range', 'fx': 'pop'},
              {'at': '^target', 'sel': '.fs-smo-cap', 'fx': 'trace'}],
    'explore': [{'at': '^design', 'sel': '.fs-game[data-mod="drawpath"] .fs-why', 'fx': 'glow', 'scroll': True},
                {'at': '^flag', 'sel': '.fs-dp-box', 'fx': 'pop', 'tag': 'Start at a flag'},
                {'at': '^Play', 'sel': '.fs-dp-play', 'fx': 'point'},
                {'at': '^tape', 'sel': '.fs-dp-info', 'fx': 'pop'},
                {'at': '^Low', 'sel': '.fs-dp-table', 'fx': 'glow'},
                {'at': '^chart', 'sel': '.fs-game[data-mod="drawpath"] .fs-todo li', 'i': 2, 'fx': 'trace'}],
    'assignment': [{'at': '^clues', 'sel': '.fs-board', 'fx': 'glow'},
                   {'at': '^Crack', 'sel': '.fs-solve', 'fx': 'pop', 'scroll': True},
                   {'at': '^two$', 'sel': '#tab-assignment .pq', 'fx': 'glow', 'all': True, 'scroll': True},
                   {'at': '^table', 'sel': '#tab-assignment .fs-in-frame', 'fx': 'pop', 'scroll': True},
                   {'at': '^C$|^CER$', 'sel': '#tab-assignment .fs-cer', 'fx': 'glow', 'scroll': True}],
    'evidence': [{'at': '^classmate', 'sel': EV + ' > p', 'i': 0, 'fx': 'trace'},
                 {'at': '^craters', 'sel': '.fs-plan .fs-opt', 'i': 2, 'fx': 'glow'},
                 {'at': '^pinball', 'sel': '.fs-plan .fs-opt', 'i': 3, 'fx': 'glow'},
                 {'at': '^hay', 'sel': '.fs-plan .fs-opt', 'i': 5, 'fx': 'glow'},
                 {'at': '^side', 'sel': '.fs-plan .fs-plan-row', 'i': 0, 'fx': 'pop'},
                 {'at': '^explain', 'sel': '.fs-cer .fs-cer-row', 'i': 2, 'fx': 'glow', 'scroll': True}],
    'closing': [{'at': '^closed', 'sel': '.fs-specimen', 'fx': 'pop', 'scroll': True},
                {'at': '^High', 'sel': '.fs-solve', 'fx': 'glow'},
                {'at': '^Next', 'sel': '#tab-assignment .callout-tip', 'fx': 'glow'}],
}
D['fold'] = {'bulletin': {'icon': '📣', 'tease': 'Hear a race called live at Dune Hill. Can you catch the speed words?', 'open': 'Listen'}}
D['cueWords'] = json.load(open('cuewords.json', encoding='utf-8')) if os.path.exists('cuewords.json') else {}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
