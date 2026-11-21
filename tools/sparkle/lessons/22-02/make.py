#!/usr/bin/env python3
"""Writes data.json and fixes.json for 22.02 (run from this folder). Case 22 part 2 "The Backup Light" (Sam Park, the Palmetto Beach jetty light).
New: stamps (Warm-Up: stamp the keeper's work order lines CRITERION or CONSTRAINT), crossout (Part 1: add limits one at a time, ideas get crossed
out), versions (Part 2: Sam's wind-spinner light v1 -> v4, pick the ONE change, retest; replaces the never-made picture + tap diagram), stormtest
(Part 3: pick an input + add-ons under budget, run 3 cloudy days + a storm night), patent (after the case: the student's passing design as a
patent drawing + APPROVED). Wright brothers photo card = photos module, folded. No Tool of the Week (day 2)."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../18-01/data.json', encoding='utf-8'))
O = json.load(open('../22-01/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
PS = '<p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)
def I(n): return 'images/22-02-' + n + '.jpg'

# ---------------------------------------------------------------- labels (standing approval) + ticked fixes (Bethany, 21 Nov 2026)
fx('fix', 'unit label: “Ecosystems & Energy” is a leftover; weeks 18–24 are Unit 5', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Energy, Motion &amp; Collisions</div>')
fx('fix', 'engineering a device is physical science, not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standard detail: the circuits box is cut (not in this lesson’s plan row)', '<div class="info-detail">NGSS 4-PS3-4 · Engineering Design & Electrical Circuits</div>', '<div class="info-detail">NGSS 4-PS3-4 · Engineering Design</div>')
# 9.01 leftovers
fx('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist already asks for a prototype plan', '🎨 Part C &mdash; Build Your Own Food Chain', '🛠️ Part C &mdash; My Device Design Plan')
fx('fix', 'copy-paste leftover: Part C task from 9.01 (now a design plan typed on the page + a required labeled sketch)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Design your OWN device that converts energy (the night-hike light, your storm-test light, or a new idea). Fill in the plan below, then sketch it.</p>', True)
fx('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
# wrong facts
fx('fix', 'wrong: the Saturn V was designed and tested in about six years (1961–1967), not over decades. No dash',
   "<p>The cycle keeps going. Each redesign makes the next prototype a little better. NASA spent decades redesigning the Saturn V rocket. Cars are redesigned every year. Even something as simple as a backpack zipper has been redesigned thousands of times.</p>",
   "<p>The cycle keeps going. Each redesign makes the next prototype a little better. Cars get redesigned every year, and even zippers keep getting better.</p>")

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; plain words; no dash',
   r"<p>Hold this question in your head as you work\. By the end of the lesson, you'll have designed.*?</p>",
   "<p>Keep this question in mind. By the end, you’ll design a device, test it in a storm and make it better.</p>", True)
fx('plain', 'the night hike stays as the warm-up story; no dash',
   "<p>Imagine you're hiking in a Florida state park at sunset, and your flashlight battery dies. The park doesn't have any outlets nearby — but you do have sunlight, wind, your hands, and the small stream running next to the trail.</p>",
   "<p>Before you design anything, an engineer asks: what must it DO, and what are the LIMITS? The harbor keeper just sent Sam a work order. Sort it out.</p>")
fx('fix', 'Warm-Up notebook sketch → the work-order stamps (the sketch is now the required Part C sketch)',
   "<p>In your notebook, sketch ONE simple idea for a device that could give you light — without using a regular battery. Don't worry about it being perfect.</p>",
   "<p>Tap a line, then stamp it.</p>")
fx('plain', 'no dash; points to the lesson',
   "<p>Today you'll think like an engineer. You'll define criteria, list constraints, sketch a prototype, and plan how to test and improve your design.</p>",
   "<p>Goals are called criteria. Limits are called constraints. Engineers write both down before they build anything.</p>")
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', 'no dash; shorter examples (Part 1)',
   "</span></span> — the goals. Things like: \"produce enough light to read a book,\" \"fit in a backpack,\" \"be safe for a 4th grader to use.\"</p>",
   "</span></span>: the goals, like “bright enough to read a book.”</p>")
fx('plain', 'no dash; shorter; points to the game (Part 1)',
   r"</span></span> — things like budget, materials available, weight limits, or safety rules\. A wind-powered flashlight has a constraint:.*?</p>",
   "</span></span>: limits like money, materials or safety rules. Limits help, too: they cross out ideas that won’t work, so you only test the good ones.</p>", True)
fx('plain', 'no dash (Part 2)', "</span></span> — a first version meant to be improved. Real engineering devices usually go through DOZENS of prototypes.</p>",
   "</span></span>: a first version, built to be tested and improved. Real devices often go through dozens of prototypes.</p>")
fx('plain', 'the misconception, plain; leads into the version timeline',
   r"<p><strong>Common misconception:</strong> Some people think real engineers come up with perfect designs on the first try\..*?</p>",
   "<p><strong>Watch out:</strong> Some people think real engineers get it perfect on the first try. They don’t. A failed test isn’t a disaster. It tells you exactly what to fix next. Watch Sam’s backup light change, version by version.</p>", True)
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'shorter closing; no dash; points to 23.01',
   r'<p><strong>Nicely done\.</strong> You can now think like an engineer.*?</p>',
   '<p><strong>Nicely done.</strong> You thought like an engineer: you set criteria and constraints, built a prototype, tested it in a storm and made it better. Next lesson, a new kind of energy: the sound that is vibrating around you right now.</p>', True)
fx('plain', 'Part B question 6 label (Gathered Answers)', 'data-label="Explain the difference between a CRITERION and a C..."', 'data-label="Criterion vs. constraint"')
fx('plain', 'Part B question 7 label (Gathered Answers)', 'data-label="Why is REDESIGN so important in engineering? Give ..."', 'data-label="Why redesign matters"')

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: Notice & Wonder (the stamps are the warm-up’s thinking stop)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Notice &amp; Wonder</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: Stop & Think (the limits game is the thinking stop for Part 1)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'the never-made AI design-cycle picture, Key Concept, the circuits box (Bethany: not in this plan row), Stop & Reason, the Four Design Challenges tap diagram, Observe & Reason, the Wright “200 wing prototypes” fact (wrong: they tested 200+ small model wings in a wind tunnel; the Wright card says it right), the Florida connection and Go Deeper are gone (lean); the version timeline replaces the picture and the diagram. The Science Connection box (energy causes change + creativity, SC.4.P.10.2 / SC.4.N.1.8) stays',
   r'<div class="lesson-figure scroll-reveal">\s*<div class="lesson-figure-label">🛠️ The Engineering Design Cycle</div>.*?(?=<div class="callout callout-think scroll-reveal">)', '', True)
fx('cut', 'Part 3 = the old Explore (design it, then storm it); next button goes to Self-Check',
   r'<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 3 · Design It, Then Storm It</h3>\n      ' + PS + 'Now you are the engineer. There is more than one good design, so use your creativity! Build a backup light inside the keeper’s limits, then test it in the storm.</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its design steps are now Part 3 and Part C; its Wright facts, “solar AC” scenario and Go Deeper go with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 5 removed (Bethany kept 6 and 7; Q5 also named the removed diagram)', r'<div class="pq">\s*<span class="pq-num"[^>]*>5</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 6 and 7 answered')
fx('cut', 'lean: Part C typed on the page, plus the required sketch', r'A prototype sketch labeled with INPUT, OUTPUT, and conversion point — plus 2 criteria, 1 constraint, a test plan, and a redesign idea\.',
   'My design plan: the problem, 2 criteria, 1 constraint, IN and OUT, a test and a redesign. Plus your labeled sketch.', True)
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', r'<strong>Evidence Response:</strong> I made a claim about whether real engineers get it right on the first try, and supported it with two pieces of evidence\.',
   '<strong>Use Your Evidence:</strong> My claim about whether engineers get it right on the first try, with two pieces of evidence.', True)
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Download your field journal (it has your answers and your sketch) and upload it to the Canvas assignment. Or copy your Gathered Answers (above) into Canvas.', True)

# ---------------------------------------------------------------- the story
SAM = Q['crew']['sam']
D = {
    'lesson': '22.02', 'week': 22, 'day': 2, 'guide': 'sam', 'prefix': 'g4sci-22-2', 'manifestKey': '22-02',
    'paths': P['paths'], 'crew': {'sam': SAM},
    'expedition': {'num': 22, 'title': 'The Backup Light'},
    'ambient': {'icon': '🌊', 'label': 'Ocean sounds'},
    'case': {
        'num': 22, 'title': 'The Backup Light', 'style': 'mariners',
        'hook': 'The jetty light is fixed. But a big storm is coming, and clouds will hide the Sun for days. Its solar panel can’t charge with no sunshine, so the keeper wants a backup light. My first try failed. Good! Now I know what to fix.',
        'notice': {'head': 'NOTICE TO MARINERS · STORM WATCH', 'title': 'CLOUDS AND STORM AHEAD',
                   'rows': [['Mon–Wed', '☁️ Thick clouds all day. Very little sunshine.'], ['Thu night', '⛈️ Storm: strong wind, rain and salt spray.'], ['Boats', 'The jetty light must shine every night.']],
                   'line': 'A forecast tells what the weather will probably do.'},
        'memo': {'t': 'Sam, the solar light can’t charge with no sunshine. Can you build a backup light that keeps shining through all of this? Work order attached.', 'sign': '~ the harbor keeper'},
        'stills': [],
        'question': 'What will make Sam’s backup light ready for the storm?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'stamps', 'icon': '📋', 'where': 'Warm-Up: stamp the work order', 't': 'Criteria are the goals a design must meet. Constraints are the limits it must stay inside. Write both down first.'},
            {'id': 'crossout', 'icon': '✂️', 'where': 'The Lesson, Part 1: limits cross out ideas', 't': 'The limits crossed out 4 of 6 ideas. Only ideas that fit the limits are worth building and testing.'},
            {'id': 'versions', 'icon': '🔁', 'where': 'The Lesson, Part 2: the version timeline', 't': 'Every failed test showed what to fix. Changing ONE thing at a time, Sam’s light got better: v1, v2, v3, v4.'},
            {'id': 'stormtest', 'icon': '⛈️', 'where': 'The Lesson, Part 3: design it, then storm it', 't': 'A design isn’t ready until it passes a test in the real conditions: three cloudy days and a storm night.'},
        ],
        'solve': {
            'title': 'What will make the backup light ready for the storm?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Sam’s first design. Good engineers get it right on the first try.', 'why': 'Check Clue 3. Sam’s first try was too dim! It took four versions.'},
                {'t': 'The brightest, biggest light, no matter what it costs.', 'why': 'Check Clue 1. The light has to stay inside the limits, like the budget.'},
                {'t': 'A design that meets the goals, stays inside the limits, and passed a real storm test after redesigns.', 'right': True,
                 'why': 'Case cracked! Goals, limits, a test, and redesign until it passes: that’s engineering. Make your patent drawing just below.'},
                {'t': 'Any design works if you build it carefully. You don’t need to test it.', 'why': 'Check Clue 4. Only a test in real conditions shows if it works.'},
            ]},
    },
    'stamps': {
        'afterText': 'Tap a line, then stamp it.', 'kicker': 'Warm-Up game', 'title': 'Stamp the work order',
        'todo': ['Tap a line on the work order.', 'Stamp it CRITERION (a goal) or CONSTRAINT (a limit). Or drag a stamp onto the line.'],
        'why': {'icon': '📋', 'q': 'What’s a work order?', 't': 'A note that tells a builder what job to do. This one is from the harbor keeper to Sam.'},
        'order': {'head': 'WORK ORDER · Palmetto Beach Harbor', 'num': 'No. 22-B', 'title': 'Build a backup jetty light', 'to': 'To: Sam Park, engineer'},
        'kinds': {'crit': {'t': 'CRITERION', 'icon': '🎯', 'sub': 'a goal: what it should DO'}, 'cons': {'t': 'CONSTRAINT', 'icon': '🚧', 'sub': 'a limit: what it CAN’T do'}},
        'lines': [
            {'id': 'bright', 't': 'Boats must see it from 1 mile away.', 'k': 'crit', 'why': 'A goal: how well it must work.', 'miss': 'Is this something the light should DO well, or a limit?'},
            {'id': 'cost', 't': 'Spend no more than $50.', 'k': 'cons', 'why': 'A limit: the budget.', 'miss': 'Is money something the light DOES, or a limit Sam must stay inside?'},
            {'id': 'night', 't': 'Shine all night, every night.', 'k': 'crit', 'why': 'A goal: what the light must do.', 'miss': 'Is shining all night a goal or a limit?'},
            {'id': 'wires', 't': 'No wires out to the jetty.', 'k': 'cons', 'why': 'A limit: something Sam can’t use.', 'miss': 'Is “no wires” a goal, or a rule that limits Sam?'},
            {'id': 'nobody', 't': 'Must work with nobody there at night.', 'k': 'cons', 'why': 'A limit: no one can help it.', 'miss': 'Does this tell what the light should do, or what Sam can’t count on?'},
            {'id': 'storm', 't': 'Keep shining through the storm.', 'k': 'crit', 'why': 'A goal: it must survive and work.', 'miss': 'Is this a goal for the light, or a limit?'}],
        'pickLine': 'Tap a line, then press a stamp. (Or drag a stamp onto a line.)', 'countWord': 'lines stamped',
        'q': 'What’s the difference between a criterion and a constraint?',
        'opts': [{'t': 'A criterion is a goal. A constraint is a limit.', 'ok': True},
                 {'t': 'They mean the same thing.', 'miss': 'Look at your stamps. Are “seen from 1 mile” and “$50” the same kind of line?'},
                 {'t': 'A constraint is a goal. A criterion is a limit.', 'miss': 'Flip it! Which stamp did “Spend no more than $50” get?'}],
        'win': 'Goals and limits, sorted. That’s step one for every engineer. Clue 1!'},
    'crossout': {
        'afterText': 'so you only test the good ones', 'kicker': 'Part 1 game', 'title': 'Limits cross out ideas',
        'todo': ['Read the 6 backup-light ideas.', 'Add the keeper’s limits one at a time (press the button, or drag the next limit onto the ideas).', 'Watch which ideas get crossed out, and why.'],
        'why': {'icon': '✂️', 'q': 'Why add limits?', 't': 'Limits save time. Crossing out ideas that can’t work means you only build and test the good ones.'},
        'ideas': [
            {'id': 'cord', 'icon': '🔌', 't': 'A long extension cord from shore', 'breaks': {'wires': 'No wires to the jetty.'}},
            {'id': 'candle', 'icon': '🕯️', 't': 'A candle lantern', 'breaks': {'nobody': 'Someone has to light it every night.'}},
            {'id': 'crank', 'icon': '🔄', 't': 'A hand-crank light', 'breaks': {'nobody': 'Nobody is there to turn the crank.'}},
            {'id': 'gen', 'icon': '⛽', 't': 'A gas generator', 'sub': 'costs about $400', 'breaks': {'nobody': 'Someone has to add gas.', 'cost': 'Costs way more than $50.'}},
            {'id': 'solar', 'icon': '🔲', 't': 'A solar light with a bigger battery'},
            {'id': 'wind', 'icon': '🌀', 't': 'A small wind-spinner light'}],
        'limits': [{'id': 'wires', 'icon': '🔌', 't': 'No wires out to the jetty.'}, {'id': 'nobody', 'icon': '🌙', 't': 'Must work with nobody there.'}, {'id': 'cost', 'icon': '💲', 't': 'No more than $50.'}],
        'limitsLabel': 'The keeper’s limits', 'addBtn': 'Add limit {n}', 'dragLine': 'Or drag the next limit onto the ideas.',
        'leftLine': 'Two ideas are left. Now they need testing!',
        'q': 'What did the limits do?',
        'opts': [{'t': 'They crossed out ideas that couldn’t work, so only the good ones are left to test.', 'ok': True},
                 {'t': 'They picked the perfect design.', 'miss': 'Two ideas are still left. Do we know yet which one works?'},
                 {'t': 'They made the job impossible.', 'miss': 'Look again. Are any ideas still standing?'}],
        'win': '6 ideas, 3 limits, 2 left to test. Limits help! Clue 2!'},
    'versions': {
        'afterText': 'Watch Sam’s backup light change, version by version', 'kicker': 'Part 2 game', 'title': 'The version timeline',
        'todo': ['Read the test results for each version of Sam’s wind-spinner light.', 'Pick the ONE change that fixes what failed.', 'Build and test the next version.'],
        'why': {'icon': '🔁', 'q': 'What’s a version?', 't': 'Each new try of a prototype. Engineers number them: v1, v2, v3… so they can compare.'},
        'model': 'a model', 'partsLabel': 'Built with', 'oneQ': 'What ONE change should Sam make for the next version?', 'buildBtn': 'Build and test {v}',
        'goalWord': 'Goal', 'testWord': 'Test result', 'passWord': 'Pass', 'failWord': 'Fail', 'naWord': 'Not tested yet',
        'crit': [{'id': 'bright', 'icon': '💡', 't': 'Seen from 1 mile away'}, {'id': 'night', 'icon': '🌙', 't': 'Shines all night'}, {'id': 'salt', 'icon': '🌊', 't': 'Survives a week of salt spray'}],
        'vers': [
            {'v': 'v1', 'name': 'first try', 'icon': '🌀', 'parts': ['a small wind spinner', 'a small battery', 'a tiny LED'], 'tests': {'bright': False, 'night': None, 'salt': None},
             'note': 'Too dim! From the boats, nobody could see it. Sam stopped testing here: no point testing the rest until it’s bright enough.',
             'opts': [{'t': 'Use a brighter LED.', 'ok': True},
                      {'t': 'Change everything: new spinner, new battery, new LED, new case.', 'miss': 'If v2 works, how would Sam know WHICH change fixed it? Change ONE thing.'},
                      {'t': 'Give up. Wind lights don’t work.', 'miss': 'One failed test is information, not the end. What did the test tell Sam to fix?'}]},
            {'v': 'v2', 'name': 'brighter LED', 'icon': '🌀', 'parts': ['a small wind spinner', 'a small battery', 'a BRIGHTER LED'], 'fixed': 'Changed: the LED', 'tests': {'bright': True, 'night': False, 'salt': None},
             'note': 'Bright enough now! But at 2 AM the light went out. The brighter LED uses energy faster, and the small battery ran empty. Fixing one thing caused a new problem.',
             'opts': [{'t': 'Add a bigger battery.', 'ok': True},
                      {'t': 'Go back to the tiny LED.', 'miss': 'Then it fails the brightness test again!'},
                      {'t': 'Give up.', 'miss': 'Sam is close! Which goal failed this time?'}]},
            {'v': 'v3', 'name': 'bigger battery', 'icon': '🌀', 'parts': ['a small wind spinner', 'a BIGGER battery', 'a brighter LED'], 'fixed': 'Changed: the battery', 'tests': {'bright': True, 'night': True, 'salt': False},
             'note': 'Bright, and it shines all night! But after 3 days of salt spray, the spinner’s motor rusted stuck. No spinning, no charging.',
             'opts': [{'t': 'Put the spinner’s motor in a salt-proof case.', 'ok': True},
                      {'t': 'Add an even bigger battery.', 'miss': 'The battery was fine this time. Which goal failed?'},
                      {'t': 'Paint the light a brighter color.', 'miss': 'Paint won’t stop rust inside the motor. What failed?'}]},
            {'v': 'v4', 'name': 'salt-proof case', 'icon': '🌀', 'parts': ['a small wind spinner in a salt-proof case', 'a bigger battery', 'a brighter LED'], 'fixed': 'Changed: added a salt-proof case', 'tests': {'bright': True, 'night': True, 'salt': True},
             'note': 'All three goals pass! Four versions, one change at a time. Every failed test showed Sam what to fix next.'}],
        'q': 'Sam’s light failed three times. Was Sam a bad engineer?',
        'opts': [{'t': 'No. Each failed test showed what to fix, and the light got better every time.', 'ok': True},
                 {'t': 'Yes. Good engineers get it right the first time.', 'miss': 'Look at the timeline. Did the failed tests help or hurt?'},
                 {'t': 'Yes, Sam should have changed everything at once.', 'miss': 'Then Sam wouldn’t know which change fixed what. One change at a time!'}],
        'win': 'Fail, learn, fix one thing, test again. That’s the design cycle! Clue 3!'},
    'stormtest': {
        'afterText': 'Build a backup light inside the keeper’s limits, then test it in the storm', 'kicker': 'Part 3 game', 'title': 'Design it, then storm it',
        'todo': ['Pick ONE energy input and up to 2 add-ons. Stay under $50.', 'Press Run the storm test: 3 cloudy days, then a storm night.', 'If the light goes dark, read why, change your design and test again.'],
        'why': {'icon': '⛈️', 'q': 'Why test in a storm?', 't': 'A light that works on a sunny day might fail when it matters most. Engineers test in the real conditions.'},
        'model': 'a model', 'budget': 50, 'maxAdd': 2, 'cap': 8, 'bigCap': 24, 'need': 6, 'brightNeed': 9, 'saltFrom': 1,
        'inQ': '1. Pick ONE energy input', 'addQ': '2. Add up to {n} add-ons', 'budgetWord': 'Budget',
        'inputs': [
            {'id': 'solar', 'icon': '🔲', 't': 'Solar panel', 'cost': 20, 'note': 'Light → electrical. No moving parts.', 'charge': {'cloudy': 2, 'storm': 0}},
            {'id': 'wind', 'icon': '🌀', 't': 'Wind spinner', 'cost': 25, 'note': 'Moving air → motion → electrical.', 'moving': True, 'charge': {'cloudy': 6, 'storm': 12}},
            {'id': 'crank', 'icon': '🔄', 't': 'Hand crank', 'cost': 10, 'note': 'Your arm’s motion → electrical.', 'person': True, 'charge': {'cloudy': 8, 'storm': 8}},
            {'id': 'tide', 'icon': '🌊', 't': 'Tide water wheel', 'cost': 45, 'note': 'Moving water → motion → electrical.', 'moving': True, 'charge': {'cloudy': 8, 'storm': 8}}],
        'addons': [
            {'id': 'big', 'icon': '🔋', 't': 'Bigger battery', 'cost': 15, 'note': 'Stores 3 times more energy.', 'big': True},
            {'id': 'salt', 'icon': '🛡️', 't': 'Salt-proof case', 'cost': 10, 'note': 'Keeps salt spray off moving parts.', 'salt': True},
            {'id': 'bright', 'icon': '🔆', 't': 'Extra-bright LED', 'cost': 10, 'note': 'Brighter than needed. Uses more energy.', 'bright': True},
            {'id': 'panel2', 'icon': '➕', 't': 'Second solar panel', 'cost': 15, 'note': 'Catches a little more light on cloudy days.', 'extra': 2}],
        'days': [{'k': 'cloudy', 'icon': '☁️', 't': 'Day 1'}, {'k': 'cloudy', 'icon': '☁️', 't': 'Day 2'}, {'k': 'cloudy', 'icon': '🌥️', 't': 'Day 3'}, {'k': 'storm', 'icon': '⛈️', 't': 'Storm night'}],
        'runBtn': '⛈ Run the storm test', 'pickLine': 'Pick an energy input first.', 'overLine': 'Over budget! The keeper’s limit is $50. Take something off.',
        'maxLine': 'Only 2 add-ons fit. Tap one to take it off first.', 'rustWord': 'rusted', 'logLabel': 'My tests',
        'lines': {'dark': 'The battery ran empty and the light went dark.', 'rust': 'Salt spray rusted the moving parts, so it stopped charging.', 'person': 'Nobody was there at night to turn the crank.', 'ok': 'The light shone every night, even in the storm!'},
        'retryLine': ' Redesign: change ONE thing and test again.',
        'wow': ' The boats can see the jetty light all through the storm. Your design passed a real test.',
        'q': 'Why didn’t Sam trust the backup light until it passed the storm test?',
        'opts': [{'t': 'Only a test in the real conditions shows whether a design really works.', 'ok': True},
                 {'t': 'Because tests are fun.', 'miss': 'They are fun! But what does a storm test SHOW?'},
                 {'t': 'He didn’t need to. It looked good on paper.', 'miss': 'Did every design that looked good on paper pass the storm?'}],
        'win': 'Tested in clouds and a storm, and it kept shining. Clue 4!'},
    'exploreMod': 'stormtest',
    'patent': {
        'after': '.fs-solve', 'kicker': 'Case closed · your patent drawing', 'title': 'Patent your backup light',
        'todo': ['Your design from the storm test is drawn below.', 'Give your invention a name.', 'Stamp it APPROVED.'],
        'lockLine': 'Crack the case first. Then patent your design.',
        'noDesign': 'Pass the storm test in Part 3 first. Your winning design becomes the drawing.',
        'head': 'PATENT DRAWING · Palmetto Beach Harbor',
        'chains': {
            'solar': [{'icon': '☀️', 't': 'Sunlight', 'sub': 'light IN'}, {'icon': '🔲', 't': 'Solar panel', 'sub': 'light → electrical'}, {'icon': '🔋', 't': 'Battery', 'sub': 'stores it'}, {'icon': '💡', 't': 'LED', 'sub': 'electrical → light OUT'}],
            'wind': [{'icon': '🌬️', 't': 'Wind', 'sub': 'motion IN'}, {'icon': '🌀', 't': 'Spinner', 'sub': 'motion → electrical'}, {'icon': '🔋', 't': 'Battery', 'sub': 'stores it'}, {'icon': '💡', 't': 'LED', 'sub': 'electrical → light OUT'}],
            'tide': [{'icon': '🌊', 't': 'Moving water', 'sub': 'motion IN'}, {'icon': '⚙️', 't': 'Water wheel', 'sub': 'motion → electrical'}, {'icon': '🔋', 't': 'Battery', 'sub': 'stores it'}, {'icon': '💡', 't': 'LED', 'sub': 'electrical → light OUT'}],
            'crank': [{'icon': '💪', 't': 'Your arm', 'sub': 'motion IN'}, {'icon': '🔄', 't': 'Crank', 'sub': 'motion → electrical'}, {'icon': '🔋', 't': 'Battery', 'sub': 'stores it'}, {'icon': '💡', 't': 'LED', 'sub': 'electrical → light OUT'}]},
        'addLabels': {'big': '🔋 bigger battery', 'salt': '🛡️ salt-proof case', 'bright': '🔆 extra-bright LED', 'panel2': '➕ second solar panel'}, 'addWord': 'Add-ons:',
        'nameQ': 'Name your invention:', 'ph': 'The Storm Beacon 3000', 'stampBtn': 'Stamp it APPROVED', 'stamp': 'APPROVED', 'sign': 'Approved by the harbor keeper',
        'win': 'APPROVED! Your backup light goes up on the jetty tonight.'},
    'photos': [{
        'id': 'wright', 'after': 'versions', 'kicker': 'Even the Wright brothers', 'short': 'Wright glider photo', 'title': 'They failed first, too',
        'fold': {'icon': '✈️', 'tease': 'A real 1901 photo: the famous airplane builders had a glider that disappointed them. What did they do next?', 'open': 'Look'},
        'todo': ['Tap each number on the photo.', 'Then match the clues.'],
        'why': {'icon': '✈️', 'q': 'Who were the Wright brothers?', 't': 'Wilbur and Orville Wright, two bike makers from Ohio. In 1903 they flew the first powered airplane.'},
        'img': I('glider-1901'), 'alt': 'An old black-and-white photo: a big two-winged glider made of cloth and wood floats above the sand, held by ropes. Two men stand on the beach holding the ropes.',
        'credit': '1901 Wright glider flown as a kite at Kitty Hawk, North Carolina: photo by Wilbur or Orville Wright, Library of Congress (public domain, via Wikimedia Commons)', 'license': 'Public domain',
        'hotspots': [{'n': 1, 'x': 46, 'y': 34, 'label': 'The wings', 't': 'In 1901 these wings lifted much less than the Wrights’ numbers said they should. A disappointing test!'},
                     {'n': 2, 'x': 9, 'y': 62, 'label': 'The ropes', 't': 'They flew it like a kite first, with nobody on it. A safe way to test a prototype.'},
                     {'n': 3, 'x': 50, 'y': 84, 'label': 'The sand', 't': 'Kitty Hawk has steady wind and soft sand for landings. A good place to test.'}],
        'task': {'q': 'Match each clue to a number on the photo.', 'win': 'After this test, the Wrights built a small wind tunnel and tested more than 200 model wings. Their redesigned 1902 glider made hundreds of good glides. Failing first helped them succeed.',
                 'items': [{'icon': '🪁', 'step': 'A safe way to test with nobody on board', 'ans': 2, 'evid': 'The ropes.'},
                           {'icon': '📉', 'step': 'The part that failed the test', 'ans': 1, 'evid': 'The wings lifted less than expected.'},
                           {'icon': '🏖️', 'step': 'Why Kitty Hawk was a good test spot', 'ans': 3, 'evid': 'Steady wind and soft sand.'}]}}],
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Think about Sam’s v1. Was it the final version?', 'C': 'Sam actually built and tested every version.'},
        'q2': {'A': 'Sam’s light failed three times. Did Sam throw it away?', 'B': 'A failed test tells you what to fix. What should the engineer do next?'},
        'q3': {'B': 'Bright light is a goal. Which answer is a LIMIT?', 'C': 'A nice-to-have isn’t a limit. Which one limits what you can spend?'}},
    'flags': {
        'ans-2': [
            {'label': 'a criterion', 're': 'criteri|criter|goal|should|must do|need to|want|success|job'},
            {'label': 'a constraint', 're': 'constrain|limit|can.?t|cannot|budget|cost|\\$|money|only|rule|not allowed'},
            {'label': 'an example', 're': 'light|bright|mile|night|battery|wire|50|dollar|storm|salt|spinner|solar|flashlight|crank|tide|device'}],
        'ans-3': [
            {'label': 'why redesign', 're': 'redesign|fix|improve|better|problem|fail|test|learn|mistake|change'},
            {'label': 'a flashlight example', 're': 'flashlight|bright|battery|light|led|bulb|longer|waterproof|water|case|crank|solar'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|doesn|does not|don|first try|perfect'},
            {'label': 'two pieces of evidence', 'any': ['version', 'v1', 'v2', 'v3', 'v4', 'sam', 'wright', 'glider', 'wing', 'storm', 'test', 'fail', 'redesign', 'dim', 'rust', 'battery'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-2': 15, 'ans-3': 15, 'cer-4': 30},
    'hints': {
        'ans-2': ['Think about your stamps on the work order.', 'A criterion is a ___. A constraint is a ___.', 'Try: A criterion is a goal, like ___. A constraint is a limit, like ___.'],
        'ans-3': ['Think about Sam’s version timeline.', 'What could go wrong with a flashlight? Too dim? Dies fast? Gets wet?', 'Try: Redesign matters because ___. A flashlight could be improved by ___.'],
        'cer-4': ['First decide: do engineers get it perfect the first time?', 'Think about Sam’s 4 versions, the Wright brothers, and your storm test.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'Sam’s backup light took four versions. Each failed test showed what to fix.',
                'The Wright brothers’ 1901 glider disappointed them, so they tested more than 200 model wings and redesigned it.',
                'In my storm test, I changed my design and tested again until it passed.',
                'Engineers are very smart people.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · the backup light', 'length': '20–30 s'},
        'warmup': {'label': 'Warm-Up · stamp the work order (Clue 1)', 'length': '20–30 s',
                   'script': 'Sam here. A big storm is coming, and clouds will hide the Sun for days. Read the forecast and the keeper’s work order. Tap a line, then stamp it. Is it a goal the light should meet, or a limit it has to stay inside?'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Hold up a paper airplane for “prototype”; fold a second, better one for “redesign”.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · limits cross out ideas (Clue 2)', 'length': '20–30 s'},
        'part2': {'label': 'Part 2 · the version timeline (Clue 3)', 'length': '20–30 s',
                  'script': 'Here’s my backup light, version one. Read the test results. Which goal failed? Pick the ONE change that fixes it, then build and test the next version. Watch out: fixing one thing can break another!'},
        'explore': {'label': 'Part 3 · design it, then storm it (Clue 4)', 'length': '25–35 s',
                    'script': 'Your turn to be the engineer. Pick one energy input and up to two add-ons, and stay inside the budget. Then press run the storm test. If the beam goes dark, read why, change one thing, and test again.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · my device design plan', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says real engineers get it perfect on the first try. Do they? Think about my four versions, and the Wright brothers. Pick your side, tap two pieces of evidence, then explain. That’s your C-E-R.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 23.01 (sound).'},
    },
    'videoOff': [],
    'lensVoice': False,
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Your stamped work order (Warm-Up)',
        'The two ideas left after the limits (The Lesson)',
        'Sam’s v4 passing every test (The Lesson)',
        'Your light shining in the storm (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['Your backup light', 'Sam’s v4', 'A night-hike light'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch and label your device', 'required': True, 'minLabels': 3,
                           'prompts': ['Draw your device', 'Label the energy IN', 'Label where it changes and the energy OUT']}]},
    'hlCoach': copy.deepcopy(Q['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '📐', 'name': 'Your approved patent drawing',
                 'line': 'You cracked Case 22 part 2, and your patent drawing goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next time: sound.'},
    'notebookTitle': 'Unit 5 · Energy, Motion & Collisions',
    'notebook': copy.deepcopy(O['notebook']),
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. Time to engineer!',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to see what it means.']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '#tab-vocab p', 'text': 'Engineers write both down before they build'},
         'label': 'Warm-Up: my night-hike light', 'q': 'Warm-Up: Your flashlight dies on a night hike. No battery. Pick an energy source and one goal and one limit.', 'title': 'Night hike, dead flashlight: your idea', 'compact': True,
         'fields': [{'t': 'Energy source (sunlight, wind, your hands or a stream)', 'icon': '⚡', 'ph': 'I would use ___.'},
                    {'t': 'One criterion (a goal)', 'icon': '🎯', 'ph': 'It must ___.'},
                    {'t': 'One constraint (a limit)', 'icon': '🚧', 'ph': 'It can’t ___.'}]},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Fill in the plan below'},
         'label': 'Part C: My device design plan', 'q': 'Part C: My device design plan (problem, criteria, constraint, IN and OUT, test, redesign)', 'title': 'My device design plan',
         'fields': [{'t': 'The problem it solves', 'icon': '❓', 'ph': 'I want a device that ___.'},
                    {'t': 'Two criteria (goals)', 'icon': '🎯', 'ph': '1. ___  2. ___'},
                    {'t': 'One constraint (a limit)', 'icon': '🚧', 'ph': 'It can’t ___.'},
                    {'t': 'Energy IN → energy OUT', 'icon': '🔄', 'ph': '___ energy in, ___ energy out.'},
                    {'t': 'How I would test it', 'icon': '🧪', 'ph': 'I would test it by ___.'},
                    {'t': 'One redesign if it fails', 'icon': '🔧', 'ph': 'If it ___, I would change ___.', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Do real engineers get it perfect on the first try?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-2': 'Part B · Question 6', 'ans-3': 'Part B · Question 7', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] == '22.02': n.update({'icon': '📐', 'name': 'Your approved patent drawing'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'Engineers set goals and limits, test a prototype, and redesign it when a test fails.',
    'key': ['goals', 'limits', 'test', 'prototype', 'redesign', 'fails'],
    'small': ['and', 'a', 'it', 'when'],
    'model': 'A scientist might highlight “goals and limits”, “test a prototype” and “redesign”. Those words hold the big idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me explain how to design a device that converts energy?']

EV = '#tab-assignment .act-body > div:has(> .fs-plan)'
D['cues'] = {
    'warmup': [{'at': '^forecast', 'sel': '.fs-casecard .fs-notice', 'fx': 'glow'},
               {'at': '^order', 'sel': '.fs-stp-paper', 'fx': 'pop', 'scroll': True},
               {'at': '^line', 'sel': '.fs-stp-line', 'i': 0, 'fx': 'point'},
               {'at': '^goal', 'sel': '.fs-stp-stamp.k-crit', 'fx': 'pop'},
               {'at': '^limit', 'sel': '.fs-stp-stamp.k-cons', 'fx': 'pop'}],
    'part2': [{'at': '^version', 'sel': '.fs-ver-line', 'fx': 'glow', 'scroll': True},
              {'at': '^results', 'sel': '.fs-ver-tests', 'fx': 'pop'},
              {'at': '^failed', 'sel': '.fs-ver-tests tr.bad', 'fx': 'wiggle'},
              {'at': '^ONE$', 'sel': '.fs-ver-q', 'fx': 'glow'},
              {'at': '^break', 'sel': '.fs-ver-card', 'fx': 'glow'}],
    'explore': [{'at': '^input', 'sel': '.fs-stm-opts', 'i': 0, 'fx': 'pop', 'scroll': True},
                {'at': '^add', 'sel': '.fs-stm-opts', 'i': 1, 'fx': 'pop'},
                {'at': '^budget', 'sel': '.fs-stm-budget', 'fx': 'glow'},
                {'at': '^storm', 'sel': '.fs-stm-run', 'fx': 'point'},
                {'at': '^again', 'sel': '.fs-stm-go', 'fx': 'glow'}],
    'evidence': [{'at': '^classmate', 'sel': EV + ' > p', 'i': 0, 'fx': 'trace', 'scroll': True},
                 {'at': '^versions', 'sel': '.fs-plan .fs-opt', 'i': 2, 'fx': 'glow'},
                 {'at': '^Wright', 'sel': '.fs-plan .fs-opt', 'i': 3, 'fx': 'glow'},
                 {'at': '^side', 'sel': '.fs-plan .fs-plan-row', 'i': 0, 'fx': 'pop'},
                 {'at': '^explain', 'sel': '.fs-cer .fs-cer-row', 'i': 2, 'fx': 'glow', 'scroll': True}],
}
D['cueWords'] = json.load(open('cuewords.json', encoding='utf-8')) if os.path.exists('cuewords.json') else {}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
