#!/usr/bin/env python3
"""Writes data.json and fixes.json for 21.02 (run from this folder). Case 21 part 2 "The Speed Limit Sign" (Sam Park, Palmetto Beach pier).
New: case.style 'cork' + case.envelopes (sealed predictions pinned to a corkboard; they open when the case is cracked), ghosts (Warm-Up: drag ghost
marbles to where you predict the real ones stop, then Play), iknewit (Part 1: sticky notes onto a BEFORE / AFTER timeline, then stamp a wrong
prediction USEFUL), flaglane (Part 2: plant a prediction flag, roll, a tape shows the gap; 6 trials, one variable, a bumpy trial, a gap meter, then
Gus's one-try test), cradle (Part 3: a Newton's cradle, pull 1/2/3, predict, 3 trials each, real photo), cradlefree (bonus after the case, folded),
signmaker (after the case: pick the speed limit the pattern supports and stamp the sign). No Tool of the Week (day 2)."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../18-01/data.json', encoding='utf-8'))
O = json.load(open('../21-01/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
PS = '<p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)
def I(n): return 'images/21-02-' + n + '.jpg'

# ---------------------------------------------------------------- ticked fixes (Bethany, 5 Nov 2026)
# labels
fx('fix', 'unit label: “Ecosystems & Energy” is a leftover; weeks 18–24 are Unit 5', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Energy, Motion &amp; Collisions</div>')
fx('fix', 'collisions are physical science, not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standard: 4-PS3-3 is about energy in collisions (4-ESS3-1 is about energy resources)', '<div class="info-value">4-ESS3-1 · TEKS 4.7(B)</div>', '<div class="info-value">4-PS3-3 · TEKS 4.7(B)</div>')
fx('fix', 'standard detail: the lesson is about predicting collisions, not friction', '<div class="info-detail">Friction in Collisions</div>', '<div class="info-detail">Predicting Collisions</div>')
# 9.01 leftovers
fx('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist already asks for a trial table', '🎨 Part C &mdash; Build Your Own Food Chain', '📋 Part C &mdash; My Trial Table')
fx('fix', 'copy-paste leftover: Part C task from 9.01 (now a 3-trial table typed on the page)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Pick one collision test: the flag lane, the cradle, or your own test at home with two balls. For 3 trials, write your prediction and the outcome. Then write the pattern in one sentence.</p>', True)
fx('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'supply list: two balls for the optional home test (the old Explore asked for them)', '<span class="need-chip"><span>✏️</span>Colored pencils</span>', '<span class="need-chip"><span>✏️</span>Colored pencils</span>\n  <span class="need-chip"><span>⚪</span>Two balls or marbles (optional)</span>')
# shaky facts
fx('fix', 'shaky: “five trials lock it in” overstates it; more trials make you surer, never certain. No dash',
   "<p>One trial alone is rarely enough. Three trials usually start showing a pattern. Five or more lock it in. Real scientific studies sometimes run THOUSANDS of trials to spot tiny patterns.</p>",
   "<p>One trial alone can fool you. Three trials can start to show a pattern, and more trials make you surer. Some real studies run THOUSANDS of trials.</p>")
fx('fix', 'the AI table picture (never made), Stop & Reason, the tap diagram (its angle card said “angle in predicts angle out”, which is how light bounces, not marbles: a side hit sends the target off at an angle, along the line where the balls touch), Observe & Reason, the “collision drift tables” fact (could not be verified), the Florida traffic-model callout and Go Deeper are gone (lean); the flag lane replaces the picture and the diagram, and the Newton’s cradle is Part 3. Next button goes to Self-Check',
   r'<div class="lesson-figure scroll-reveal">\s*<div class="lesson-figure-label">🎯 Predictions vs\. Real Results</div>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 3 · Pull, Predict, Let Go</h3>\n      ' + PS + 'Remember the Newton’s cradle from the Warm-Up? Now test it. Pull back 1, 2, then 3 balls. Predict first, then run 3 trials of each.</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
# questions that pointed at cut parts
fx('fix', 'Part B question 5 pointed at the removed diagram; now it plans a new test on today’s games',
   'Pick ONE investigation idea from the diagram. Write a 2-sentence prediction about what you think the pattern will be. Then write what variable you would change.',
   'Plan a new test on the flag lane or the cradle. What ONE variable would you change? Write a 2-sentence prediction about the pattern you think you will see.')
fx('fix', 'Part B question 5 label (Gathered Answers)', 'data-label="Pick ONE investigation idea from the diagram. Writ..."', 'data-label="Plan a new test: one variable + a prediction"')
fx('fix', 'Part B question 7 said “predicts X… shows Y”; now a real example from the lesson (a small marble hitting a big one bounces back)',
   'A scientist predicts X. The trials show Y instead. Did the investigation fail? Explain using the word <em>pattern</em>.',
   'Ava predicted the small marble would roll forward after it hit the big marble. In 5 trials, it bounced back every time. Did her investigation fail? Explain using the word <em>pattern</em>.')
fx('fix', 'Part B question 7 label (Gathered Answers)', 'data-label="A scientist predicts X. The trials show Y instead...."', 'data-label="Did Ava’s investigation fail?"')

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; plain words',
   "Hold this question in your head as you work. By the end of the lesson, you'll have planned a collision test, made predictions, run multiple trials, recorded outcomes, and spotted a real pattern in your data.",
   "Keep this question in mind. By the end, you’ll predict, test, run lots of trials and spot a real pattern.")
fx('plain', 'the warm-up opens with a real Newton’s cradle photo; the prediction is typed on the page',
   "<p>Imagine you roll a heavy marble at a smaller marble sitting still. In your notebook, sketch what you think the AFTER picture will look like. Which marble moves? How fast? Which direction?</p>",
   "<p>Look at this toy. It’s called a Newton’s cradle: five steel balls hanging in a row. If you pull back TWO balls and let go, how many will fly out the other side? Write your prediction before you find out.</p>")
fx('plain', 'the marble sketches are now the ghost marbles game',
   "<p>Now imagine swapping it: roll the SMALLER marble at the HEAVIER one. Sketch that AFTER too. Same question.</p>",
   "<p>Now a warm-up with marbles. A big marble rolls into a small one that is sitting still. Then the small one rolls into the big one. Where will each marble stop? Use ghost marbles to predict.</p>")
fx('plain', 'subtitle', 'What do you THINK will happen?', 'Predict before you look!')
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', 'no dash; shorter',
   "is your best guess about what will happen — written down BEFORE you run a test. That timing matters. Scientists write predictions first because it forces them to think clearly about what they already know.</p>",
   "is your best guess about what will happen, written down BEFORE you run a test. That timing matters: a prediction you write first can be checked. Saying “I knew it!” afterward can’t.</p>")
fx('plain', 'no dash; the misconception lives here now (wrong ≠ failed)',
   "tells you whether your prediction was right, partly right, or wrong. ALL THREE are useful! A \"wrong\" prediction often teaches you the most — it tells you something you didn't know yet.</p>",
   "tells you whether your prediction was right, partly right, or wrong. ALL THREE are useful! A “wrong” prediction does not mean the test failed. It often teaches you the most, because it shows you something you didn’t know yet.</p>")
fx('plain', 'plain; drops the “Florida engineers” and “for centuries” claims',
   "<p>The three-step cycle has been used for centuries because it works. It's how Florida engineers test bridges, how doctors test medicines, and how 4th-grade scientists figure out marble collisions:</p>",
   "<p>Scientists use three steps over and over. Engineers use them to test bridges, doctors use them to test medicines, and you can use them to test marble crashes:</p>")
fx('plain', 'no dash', '<li><strong>PREDICT</strong> — Write down', '<li><strong>PREDICT:</strong> Write down')
fx('plain', 'no dash', '<li><strong>TEST</strong> — Run multiple', '<li><strong>TEST:</strong> Run several')
fx('plain', 'no dash', '<li><strong>COMPARE</strong> — Look at', '<li><strong>COMPARE:</strong> Look at')
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'shorter closing; no dash; points to 22.01',
   r'<p><strong>Nicely done\.</strong> You can now plan a.*?</p>',
   '<p><strong>Nicely done.</strong> You wrote predictions first, ran trials, changed one thing at a time and found a pattern you can trust. Next lesson, energy changes from one form to another.</p>', True)

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: Notice & Wonder (the ghost marbles are the warm-up’s thinking stop)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Notice &amp; Wonder</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: Stop & Think (the I-knew-it trap is the thinking stop for Part 1)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: the misconception paragraph repeats Part 1 (moved there)', r'<p><strong>Common misconception:</strong> Some people think a "wrong" prediction.*?</p>\s*', '', True)
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its two-ball test is now the Newton’s cradle in Part 3 and the optional home test in Part C; its “strike in a blink” fact was wrong: pins take about 2 seconds to fall)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 6 removed (Bethany kept 5 and 7)', r'<div class="pq">\s*<span class="pq-num"[^>]*>6</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: renumber Part B (7 → 6)', '<span class="pq-num" style="background:#D4772C;">7</span>', '<span class="pq-num" style="background:#D4772C;">6</span>')
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C typed on the page', 'A collision-investigation data table with at least 3 trials, a prediction column, an outcome column, and a one-sentence pattern claim.',
   'My trial table: the one thing I changed, 3 trials (prediction and outcome) and the pattern in one sentence.')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether one trial is enough, and supported it with two pieces of evidence from the lesson or my own trials.',
   '<strong>Use Your Evidence:</strong> My claim about whether one trial is enough, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', True)

# ---------------------------------------------------------------- the story
SAM = Q['crew']['sam']
D = {
    'lesson': '21.02', 'week': 21, 'day': 2, 'guide': 'sam', 'prefix': 'g4sci-21-2', 'manifestKey': '21-02',
    'paths': P['paths'], 'crew': {'sam': SAM},
    'expedition': {'num': 21, 'title': 'The Speed Limit Sign'},
    'ambient': {'icon': '🌊', 'label': 'Ocean sounds'},
    'case': {
        'num': 21, 'title': 'The Speed Limit Sign', 'style': 'cork',
        'hook': 'After the fender bender, the pier manager wants a speed limit for golf carts. Gus says speed doesn’t matter, and he says he already tested it. Gus, Rosa and I each sealed a prediction in an envelope. Before anyone opens them, we test.',
        'notice': {'head': 'PALMETTO BEACH PIER · NOTICE', 'title': 'Coming soon: a cart speed limit',
                   'rows': [['From', 'Ms. Okafor, pier manager'], ['Why', 'Last Tuesday, a golf cart bumped Rosa’s ice cream cart.'], ['The rule', 'If a cart bumps something, the thing it hits must not roll more than 2 feet.']],
                   'line': 'Three sealed predictions are pinned below.'},
        'memo': {'t': 'I already tested it! I rolled a BIG marble down the low ramp, and a SMALL marble down the high ramp. Both pushed the block about the same. One try each. So speed doesn’t matter. Any speed limit is fine!', 'sign': '— Gus, pier security'},
        'envelopes': [
            {'who': 'Gus', 'icon': '🛺', 'front': 'Open after the trials', 'inside': 'Speed doesn’t matter. A bump is a bump.', 'verdict': '✗ Not supported. His test changed two things and ran only one try.'},
            {'who': 'Rosa', 'icon': '🍦', 'front': 'Open after the trials', 'inside': 'A faster cart will push my cart farther. At 5 mph it rolled 3 feet!', 'verdict': '✓ Supported by the trials.'},
            {'who': 'Sam', 'icon': '🔧', 'front': 'Open after the trials', 'inside': 'Faster means farther. I’ll trust it after many fair trials.', 'verdict': '✓ Supported, and now tested.'}],
        'envLine': 'No peeking! They open when you crack the case.',
        'envOpen': 'The envelopes are open! Whose prediction did the trials support?',
        'stills': [],
        'question': 'Gus says speed doesn’t matter in a bump. Rosa and Sam say a faster cart pushes farther. Whose prediction do the trials support, and how do you know?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'ghosts', 'icon': '👻', 'where': 'Warm-Up: ghost marbles', 't': 'Your ghost marbles were predictions placed BEFORE the roll. Comparing them to where the real marbles stopped showed what you got right and what surprised you.'},
            {'id': 'iknewit', 'icon': '📝', 'where': 'The Lesson, Part 1: the I-knew-it trap', 't': 'Only notes written BEFORE the test can be checked. A wrong prediction is still useful: it shows what you didn’t know yet.'},
            {'id': 'flaglane', 'icon': '🚩', 'where': 'The Lesson, Part 2: the flag lane', 't': 'Change ONE thing (the ramp height) and run several trials: the high ramp pushed the block farther every time, except one bumpy trial. One try alone can fool you.'},
            {'id': 'cradle', 'icon': '⚪', 'where': 'The Lesson, Part 3: the Newton’s cradle', 't': 'Pull back 1, 2 or 3 balls: the same number flew out, trial after trial. When a pattern repeats, you can trust it and use it to predict.'},
        ],
        'solve': {
            'title': 'Whose prediction do the trials support?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Gus’s. His test proved that speed doesn’t matter.', 'why': 'Check Clue 3. How many things did Gus change at once? How many tries did he run?'},
                {'t': 'Rosa’s and Sam’s. In fair trials that changed only the ramp, the faster marble pushed the block farther, again and again.', 'right': True,
                 'why': 'Case cracked! Many fair trials showed the same pattern: faster pushes farther. The envelopes are open, and the sign is ready to make just below.'},
                {'t': 'Nobody’s. Predictions can be wrong, so we can’t know.', 'why': 'Check Clue 2. A wrong prediction still teaches you something, and trials give you evidence.'},
                {'t': 'Just do one more bump. One try will settle it.', 'why': 'Check Clue 3. Remember the bumpy trial? One try alone can fool you.'},
            ]},
    },
    'ghosts': {
        'afterText': 'Use ghost marbles to predict', 'kicker': 'Warm-Up game', 'title': 'Ghost marbles',
        'hook': {'beforeText': 'It’s called a Newton’s cradle', 'img': I('cradle'), 'alt': 'A real Newton’s cradle: five shiny steel balls hang from thin strings on a metal frame. The two end balls are swinging out.',
                 'cap': 'A real Newton’s cradle. Pull back two balls and let go. How many fly out the other side?', 'credit': ''},
        'todo': ['Drag each see-through ghost marble down onto the board, where you think that marble will stop. (Or tap a ghost, then tap the board.)', 'Press Play. The real marbles roll, and your ghosts stay put.', 'How close were you? Do both rounds.'],
        'why': {'icon': '👻', 'q': 'Why ghosts?', 't': 'A ghost marble is your prediction. You place it BEFORE the test, so afterward you can check it.'},
        'model': 'a model', 'trayWord': 'Ghost marbles: drag each one down onto the board', 'scale': 4, 'e': 0.9, 'k': 140,
        'rounds': [
            {'k': 'big', 't': 'Round 1:', 'sub': 'the BIG marble rolls into the small one.', 'alt': 'A model: a big blue marble rolls along a board toward a small orange marble that is sitting still.',
             'a': {'t': 'Big marble', 'tag': 'BIG', 'r': 22, 'm': 4, 'c': '#2D7AA6'}, 'b': {'t': 'Small marble', 'tag': 'small', 'r': 12, 'm': 1, 'c': '#F2994A'},
             'line': 'The big marble kept rolling, slower. The small marble shot far away.'},
            {'k': 'small', 't': 'Round 2:', 'sub': 'the SMALL marble rolls into the big one.', 'alt': 'A model: a small orange marble rolls along a board toward a big blue marble that is sitting still.',
             'a': {'t': 'Small marble', 'tag': 'small', 'r': 12, 'm': 1, 'c': '#F2994A'}, 'b': {'t': 'Big marble', 'tag': 'BIG', 'r': 22, 'm': 4, 'c': '#2D7AA6'},
             'line': 'Surprise for many people: the small marble BOUNCED BACK, and the big one only rolled a little.'}],
        'playBtn': 'Play', 'placeMiss': 'Drag both ghost marbles down onto the board first. They are your prediction!', 'nextBtn': 'Round 2', 'againBtn': 'Try this round again',
        'offWord': 'cm off', 'close': 8, 'closeLine': 'Great prediction! ', 'tableLabel': 'How close were my ghosts?', 'roundWord': 'Round', 'gapWord': 'How far off my ghosts were',
        'q': 'Why did you place the ghosts BEFORE pressing Play?',
        'opts': [{'t': 'So I could check my prediction against what really happened.', 'ok': True},
                 {'t': 'So the marbles would roll where my ghosts were.', 'miss': 'Did the real marbles follow your ghosts, or did they go their own way?'},
                 {'t': 'It doesn’t matter. I could place them after.', 'miss': 'If you place them after you watch, is that still a prediction?'}],
        'win': 'Ghosts first, then the test. That’s how you check a prediction. Clue 1!'},
    'iknewit': {
        'afterText': 'often teaches you the most', 'kicker': 'Part 1 game', 'title': 'The “I knew it!” trap',
        'todo': ['Sam tested a small marble rolling into a big one at 8:15 PM. Read each pier kid’s sticky note and its time.', 'Drag each note to BEFORE or AFTER the test (or tap a note, then a side).', 'Then the result comes in. Stamp the wrong prediction.'],
        'why': {'icon': '📝', 'q': 'What’s a sticky note doing here?', 't': 'Pier kids watched Sam’s test and wrote notes. The time on each note shows when they wrote it.'},
        'test': {'icon': '💥', 't': 'Sam’s marble test', 'time': '8:15 PM'},
        'zones': {'before': 'BEFORE the test', 'after': 'AFTER the test'},
        'timeMiss': 'Look at the time on the note. The test was at 8:15 PM.', 'checkWord': 'Can be checked', 'nocheckWord': 'Too late to check',
        'notes': [
            {'id': 'mia', 'who': 'Mia', 'icon': '🧢', 'time': '8:02 PM', 't': 'I predict the small marble will bounce back, because the big one is heavier.', 'side': 'before', 'miss': 'Mia wrote at 8:02. Is that before or after 8:15?'},
            {'id': 'leo', 'who': 'Leo', 'icon': '🛹', 'time': '8:16 PM', 't': 'I KNEW the small one would bounce back!', 'side': 'after', 'miss': 'Leo wrote at 8:16, one minute after the test.'},
            {'id': 'ava', 'who': 'Ava', 'icon': '🎀', 'time': '8:05 PM', 't': 'I predict the small marble will push the big one far away.', 'side': 'before', 'miss': 'Ava wrote at 8:05. The test was at 8:15.'},
            {'id': 'jay', 'who': 'Jay', 'icon': '🏄', 'time': '8:20 PM', 't': 'Obviously the big one would barely move. I could have told you.', 'side': 'after', 'miss': 'Jay wrote at 8:20. The test was over by then.'}],
        'q1': {'q': 'Leo says he knew it. Why doesn’t his note count as a prediction?',
               'opts': [{'t': 'He wrote it AFTER the test, so nobody can check it.', 'ok': True},
                        {'t': 'Because he was right.', 'miss': 'Mia was right too, and her note counts. Look at the times.'},
                        {'t': 'Sticky notes never count.', 'miss': 'Mia’s and Ava’s sticky notes count. What’s different about Leo’s?'}]},
        'result': {'icon': '📋', 'head': 'The result: the small marble bounced back, and the big one rolled a little.', 't': ' Mia’s prediction was right. Ava’s was wrong.'},
        'wrong': {'id': 'ava', 'q': 'Ava’s prediction was wrong. Stamp it:', 'mark': 'USEFUL',
                  'stamps': [{'k': 'useful', 't': 'USEFUL', 'ok': True}, {'k': 'failed', 't': 'FAILED', 'miss': 'Did Ava learn something from her wrong prediction? A wrong prediction is not a failed test.'}]},
        'q': 'What did Ava’s wrong prediction teach her?',
        'opts': [{'t': 'A small marble can’t push a heavy one far. It bounces back instead.', 'ok': True},
                 {'t': 'That she should stop making predictions.', 'miss': 'Then she’d never learn anything new! What did the test show her?'},
                 {'t': 'Nothing, because she was wrong.', 'miss': 'Wrong predictions often teach the most. What surprised her?'}],
        'win': 'Write it BEFORE, check it AFTER, and learn from the wrong ones. Clue 2!'},
    'flaglane': {
        'afterText': 'more trials make you surer', 'kicker': 'Part 2 game', 'title': 'The flag lane',
        'todo': ['Drag the yellow flag to where you think the red block will stop (or tap the board).', 'Press Roll the marble. The yellow tape shows your gap.', 'Do 3 trials on the low ramp, then 3 on the high ramp. Watch your gap meter.'],
        'why': {'icon': '🚩', 'q': 'What’s the flag for?', 't': 'Your flag is your prediction. The gap between the flag and the block shows how close you were.'},
        'model': 'a model', 'alt': 'A model: a ramp on the left, a marble at the top, a red wooden block at the bottom, and a ruler in centimeters along the board.',
        'unit': 'cm', 'max': 60, 'keep': 'Kept the same: the marble, the block and the board.',
        'ramps': {'low': {'t': 'Low ramp', 'h': 34}, 'high': {'t': 'High ramp', 'h': 92}},
        'trials': [{'ramp': 'low', 'd': 13, 'note': 'Now you know about where a low-ramp marble pushes the block.'},
                   {'ramp': 'low', 'd': 15, 'note': 'Close to the first trial, but not exactly the same.'},
                   {'ramp': 'low', 'd': 14, 'note': 'Three trials, all close together: a pattern!'},
                   {'ramp': 'high', 'd': 33, 'note': 'The higher ramp made a faster marble, and the block went much farther.'},
                   {'ramp': 'high', 'd': 12, 'bump': True, 'note': 'Way off! The block caught on a gap between the boards. If this were your ONLY trial, you’d think the high ramp didn’t matter.'},
                   {'ramp': 'high', 'd': 35, 'note': 'Back to the pattern. Trial 5 was a fluke (a weird one-time result).'}],
        'flagWord': 'Drag the flag to where you think the block will stop', 'myFlag': 'my flag',
        'flagMiss': 'Plant your flag first: drag it to where you think the block will stop.', 'rollBtn': 'Roll the marble', 'nextBtn': 'Next trial', 'trialWord': 'Trial',
        'switchLine': 'Now change ONE thing: the ramp height. The marble, the block and the board stay the same.',
        'realWord': 'The block stopped at', 'gapWord': 'Gap', 'tableLabel': 'My trials', 'cols': ['Trial', 'Ramp', 'My flag', 'Real stop', 'Gap'],
        'meterLabel': 'Gap meter: how far off was each flag?', 'closerLine': 'Your flag got closer as you learned the pattern!', 'useLine': 'Use the pattern in your table to place the next flag.', 'allDone': 'All 6 trials done',
        'gus': {'icon': '🛺', 'who': 'Remember Gus’s test?', 't': 'I rolled a BIG marble down the low ramp, and a SMALL marble down the high ramp. Both pushed the block about the same. One try each. So speed doesn’t matter!',
                'q': 'Tap the 2 problems with Gus’s test.', 'need': 2,
                'opts': [{'t': 'He changed two things at once: the ramp AND the marble.', 'ok': True, 'yes': 'Two changes at once: we can’t tell which one made the difference.'},
                         {'t': 'He wrote down a prediction first.', 'miss': 'Writing a prediction first is a GOOD thing. Look for something he did wrong.'},
                         {'t': 'He ran only one try of each.', 'ok': True, 'yes': 'One try can be a fluke, like our bumpy trial 5.'},
                         {'t': 'He used a block.', 'miss': 'We used a block too. That part is fine.'}]},
        'win': 'One thing changed, many trials, and a clear pattern: faster pushes farther. Clue 3!'},
    'cradle': {
        'afterText': 'run 3 trials of each', 'kicker': 'Part 3 game', 'title': 'Pull, predict, let go',
        'todo': ['Pick how many balls to pull back: 1, 2 or 3.', 'Predict how many will fly out the other side.', 'Drag the end ball back and let go (or press Let go). Run 3 trials of each.'],
        'why': {'icon': '⚪', 'q': 'What is a Newton’s cradle?', 't': 'A row of same-size steel balls hanging from strings. It’s named after Isaac Newton, a scientist who studied how things move.'},
        'alt': 'A model of a Newton’s cradle: five steel balls hanging in a row from strings on a frame.', 'balls': 5, 'pulls': [1, 2, 3], 'trials': 3, 'predMax': 4,
        'pullQ': '1. How many balls will you pull back?', 'ballWord': 'ball', 'ballsWord': 'balls', 'predQ': '2. Predict: how many balls will fly out the other side?', 'lockedWord': '(locked in)',
        'dragLine': '3. Drag the end ball back and let go, or press Let go.', 'letBtn': 'Let go',
        'pullMiss': 'First pick how many balls to pull back.', 'predMiss': 'Predict first: how many will fly out?', 'doneMiss': 'You did all 3 trials for this one. Pick another number.',
        'trialWord': 'Trial', 'outWord': 'flew out', 'rightPre': 'Your prediction was right! ', 'wrongPre': 'Surprise! A wrong prediction still teaches you something. ',
        'againLine': 'Run it again. Does the same thing happen?', 'doneLine': 'Same every time: that’s a pattern. Try another number.',
        'warmFrom': 'fs-warm', 'warmLabel': 'Your Warm-Up prediction (2 balls):',
        'tableLabel': 'My cradle trials', 'cols': ['Pulled back', 'My prediction', 'Trial 1', 'Trial 2', 'Trial 3'],
        'photo': {'head': 'The real thing', 'img': I('cradle'), 'alt': 'A real Newton’s cradle: five shiny steel balls on strings. The two end balls are swinging out, one on each side, and the middle three hang still.',
                  'cap': 'A real Newton’s cradle. Here someone let go of BOTH end balls at once, so one ball bounces out on each side and the middle three stay still. The balls are all the same size, so each click passes the motion along the row.', 'credit': ''},
        'slowLine': 'Why does it slowly stop? Every CLICK turns a little of the energy into sound and heat (and the balls push through air). So each swing is a little smaller.',
        'q': 'You pulled back 1, 2 and 3 balls, 3 trials each. What pattern did you find?',
        'opts': [{'t': 'The same number of balls flew out as I pulled back, every time.', 'ok': True},
                 {'t': 'Always just one ball flew out.', 'miss': 'Look at your table. What happened when you pulled back 3?'},
                 {'t': 'It was different every trial.', 'miss': 'Look across each row of your table. Did the trials match?'}],
        'win': 'Pull 1, 1 flies out. Pull 2, 2 fly out. Every trial! A pattern you can predict with. Clue 4!'},
    'exploreMod': 'cradle',
    'cradlefree': {
        'after': '.fs-solve', 'kicker': 'Bonus game · unlocked after the case', 'title': 'Cradle free play',
        'todo': ['Pick 5 or 7 balls, and how many to pull back.', 'Predict how many fly out, then let go.', 'How long can your prediction streak get?'],
        'lockLine': 'Crack the case first. Then free play opens.', 'alt': 'A model of a Newton’s cradle with steel balls hanging in a row.',
        'sizes': [5, 7], 'sizeWord': 'How many balls on the cradle?', 'pullQ': 'Pull back:', 'predQ': 'Predict: how many fly out?', 'letBtn': 'Let go',
        'predMiss': 'Predict first: how many will fly out?', 'outWord': 'flew out', 'streakWord': 'Prediction streak', 'bestWord': 'Best',
        'rightLine': 'You predicted it! The pattern works.', 'wrongLine': 'Not this time. What does the pattern say?'},
    'signmaker': {
        'after': '.fs-solve', 'kicker': 'Case closed · make the sign', 'title': 'Make the speed limit sign',
        'todo': ['Read Ms. Okafor’s rule and Sam’s test results.', 'Pick the speed limit the pattern supports.', 'Tell how you knew, then stamp the sign.'],
        'why': {'icon': '🪧', 'q': 'Nobody tested every speed. Can you still choose?', 't': 'Yes! A pattern from your trials lets you predict speeds you didn’t test. That’s what patterns are for.'},
        'lockLine': 'Crack the case first. Then make the sign.',
        'rule': 'Ms. Okafor’s rule: if a cart bumps something, the thing it hits must not roll more than 2 feet.',
        'data': {'head': 'Sam’s night test: a cart bumps a parked cart (3 trials each, averaged)', 'cols': ['Cart speed', 'Parked cart rolled'],
                 'rows': [['2 mph', 'about ½ foot'], ['4 mph', 'about 2 feet'], ['6 mph', 'about 4½ feet']],
                 'note': 'And Gus’s real bump: at 5 mph, Rosa’s cart rolled about 3 feet.'},
        'pickQ': 'Which speed limit keeps a bumped cart under 2 feet?',
        'opts': [{'mph': 3, 'ok': True, 'line': '3 mph is between 2 and 4 mph on the table, so a bumped cart would roll about 1 foot. Under 2 feet!'},
                 {'mph': 5, 'line': 'Gus’s real bump was at 5 mph, and Rosa’s cart rolled about 3 feet. Too far!'},
                 {'mph': 8, 'line': 'Faster than anything Sam tested. The pattern says much more than 4½ feet. Way too far!'},
                 {'mph': 12, 'line': 'The pattern says faster pushes MUCH farther. Way too far!'}],
        'signHead': 'SPEED LIMIT', 'unitWord': 'mph',
        'q': 'Nobody tested 3 mph. How did you know it would work?',
        'qopts': [{'t': 'The pattern: faster pushes farther, so 3 mph lands between 2 and 4 mph.', 'ok': True},
                  {'t': 'I guessed.', 'miss': 'It was more than a guess! What did the table show as the speed went up?'},
                  {'t': 'Gus said so.', 'miss': 'Gus said speed doesn’t matter. What did the trials say?'}],
        'stampBtn': 'Stamp the sign', 'stamp': 'APPROVED', 'sign': 'Approved by Ms. Okafor, pier manager',
        'win': 'APPROVED! The pier’s new sign says 3 mph, about walking speed. Your trials and your pattern made a real rule.'},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Think about the ghost marbles: your ghost and the real marble were in different places.', 'B': 'Predictions can be wrong, like Ava’s. Which one comes BEFORE the test?'},
        'q2': {'B': 'Remember the flag lane? What did the extra trials show that one trial couldn’t?', 'C': 'Your first flag lane trial wasn’t wrong. Why run more?'},
        'q3': {'A': 'Ava didn’t ignore her result. What did she learn?', 'C': 'A test with a surprise result is still a good test. What should you do with new evidence?'}},
    'flags': {
        'ans-1': [
            {'label': 'one variable', 're': 'change|variable|switch|only one|one thing|instead|swap|use a'},
            {'label': 'a prediction', 're': 'predict|think|will|bet|guess|expect|probably'},
            {'label': 'a pattern', 're': 'pattern|every time|farther|further|more|less|same|faster|slower|bigger|heavier|lighter|higher'}],
        'ans-3': [
            {'label': 'did it fail?', 're': 'no|not|didn|did not|wasn|was not|success|learn|taught'},
            {'label': 'pattern', 're': 'pattern|paturn|patern'},
            {'label': 'the evidence', 're': 'trial|every time|5|five|bounce|back|repeat|same|each time|all'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|doesn|does not|need|more than one|not enough'},
            {'label': 'two pieces of evidence', 'any': ['bump', 'gap', 'board', 'flag', 'fluke', 'trial', 'cradle', 'ball', 'pattern', 'gus', 'ramp', 'block', 'same', 'repeat', 'fool', 'ghost', 'marble', 'meter'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-1': 15, 'ans-3': 15, 'cer-4': 30},
    'hints': {
        'ans-1': ['Pick the flag lane or the cradle.', 'What could you change? A heavier marble? A bigger block? More balls?', 'Try: I would change only the ___. I predict that ___ will ___ because ___.'],
        'ans-3': ['Remember Ava’s sticky note. Was her wrong prediction useful?', 'What happened in all 5 trials? Did it repeat?', 'Try: No, it didn’t fail, because the trials showed a pattern: ___.'],
        'cer-4': ['First decide: is one trial enough?', 'Think about the bumpy trial on the flag lane, and the cradle trials.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'Trial 5 on the flag lane hit a gap in the boards and stopped way short. One trial alone would have fooled me.',
                'In the normal trials, the high ramp pushed the block farther every time. The pattern repeated.',
                'The cradle sent out the same number of balls, trial after trial.',
                'Gus ran one try and changed two things, so his answer was wrong.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · the speed limit sign', 'length': '20–30 s',
                    'script': 'Hi, it’s Sam! The pier manager wants a speed limit for golf carts. Read her notice. Gus says speed doesn’t matter, and he tested it once. Read his note. Gus, Rosa and I each sealed a prediction in an envelope. We open them when the case is cracked.'},
        'warmup': {'label': 'Warm-Up · ghost marbles (Clue 1)', 'length': '20–30 s',
                   'script': 'Look at the photo of the Newton’s cradle. If you pull back two balls, how many fly out? Write your prediction in the box. Then drag each ghost marble down to where you think the real marble will stop, and press Play.'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Hold up a sticky note for “prediction”; roll a ball twice for “trial”.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · the I-knew-it trap (Clue 2)', 'length': '20–30 s',
                  'script': 'Some pier kids wrote sticky notes about my marble test. Look at the time on each note. Drag it before the test or after the test. Which notes can we really check? Then a wrong prediction comes in. Is it useless?'},
        'part2': {'label': 'Part 2 · the flag lane (Clue 3)', 'length': '20–30 s',
                  'script': 'Drag the yellow flag to where you think the block will stop. Then roll the marble. The tape shows your gap. Do three trials on the low ramp, then change one thing: the ramp. Watch your gap meter.'},
        'explore': {'label': 'Part 3 · the Newton’s cradle (Clue 4)', 'length': '25–35 s',
                    'script': 'Here’s the Newton’s cradle. Pick how many balls to pull back. Predict how many will fly out. Then drag the end ball back and let go. Run three trials of each. Does the same thing happen every time?'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s',
                       'script': 'Got all four clues? Crack the case at the top of this tab, and the envelopes open. Then make the speed limit sign. After that, answer two questions, fill in your trial table, and finish your C-E-R.'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · my trial table', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says one trial is enough. Is that true? Think about the bumpy trial on the flag lane, and the cradle. Pick your side, tap two pieces of evidence, then explain how they prove your claim.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 22.01 (energy conversion).',
                    'script': 'Case closed! The trials showed it: faster carts push farther, so the pier got a real speed limit. Your opened envelope goes in your Field Notebook. Next time: energy that changes from one form to another.'},
    },
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Your ghost marbles next to the real ones (Warm-Up)',
        'A USEFUL stamp (The Lesson)',
        'Your gap meter (The Lesson)',
        'Balls flying out of the cradle (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['The flag lane after a trial', 'The Newton’s cradle', 'Your own two-ball test'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 3,
                           'prompts': ['Draw your test setup', 'Mark your prediction', 'Label what you changed']}]},
    'hlCoach': copy.deepcopy(Q['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '✉️', 'name': 'An opened prediction envelope',
                 'line': 'You cracked Case 21 part 2, and Rosa’s opened envelope goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next time: energy that changes form.'},
    'notebookTitle': 'Unit 5 · Energy, Motion & Collisions',
    'notebook': copy.deepcopy(O['notebook']),
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. Time to predict, test and compare!',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '#tab-vocab p', 'text': 'It’s called a Newton’s cradle'},
         'label': 'Warm-Up: my Newton’s cradle prediction', 'q': 'Warm-Up: Pull back 2 balls on a Newton’s cradle. How many fly out? Why?', 'title': 'My prediction (write it BEFORE you find out!)', 'compact': True,
         'fields': [{'t': 'How many balls will fly out?', 'icon': '🎯', 'ph': 'I predict ___ balls will fly out.'},
                    {'t': 'Why do you think so?', 'icon': '💭', 'ph': 'Because…'}]},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'For 3 trials, write your prediction'},
         'label': 'Part C: My trial table', 'q': 'Part C: My trial table (the one thing I changed, 3 trials, the pattern)', 'title': 'My trial table',
         'fields': [{'t': 'My test, and the ONE thing I changed', 'icon': '🎛️', 'ph': 'On the ___, I changed only the ___.'},
                    {'t': 'Trial 1: my prediction → the outcome', 'icon': '1️⃣', 'ph': 'I predicted ___ → it ___'},
                    {'t': 'Trial 2: my prediction → the outcome', 'icon': '2️⃣', 'ph': 'I predicted ___ → it ___'},
                    {'t': 'Trial 3: my prediction → the outcome', 'icon': '3️⃣', 'ph': 'I predicted ___ → it ___'},
                    {'t': 'The pattern (one sentence)', 'icon': '🔁', 'ph': 'Every time, ___', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Is ONE trial enough?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-1': 'Part B · Question 5', 'ans-3': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] == '21.02': n.update({'icon': '✉️', 'name': 'An opened prediction envelope'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'A prediction is written before the test, and many trials show a pattern you can trust.',
    'key': ['prediction', 'before', 'test', 'trials', 'pattern', 'trust'],
    'small': ['A', 'is', 'the', 'and', 'you', 'can'],
    'model': 'A scientist might highlight “prediction”, “before the test”, “many trials” and “pattern”. Those words hold the big idea. Small words like “a” and “the” don’t carry the idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me explain how trials and predictions find a pattern?']

# ---------------------------------------------------------------- Spotlight: what lights up as Sam talks
EV = '#tab-assignment .act-body > div:has(> .fs-plan)'
D['cues'] = {
    'welcome': [{'at': '^notice', 'sel': '.fs-casecard .fs-notice', 'fx': 'glow'},
                {'at': '^tested', 'sel': '.fs-casecard .fs-memo', 'fx': 'pop'},
                {'at': '^note', 'sel': '.fs-casecard .fs-memo p', 'fx': 'trace'},
                {'at': '^envelope', 'sel': '.fs-casecard .fs-env-board', 'fx': 'pop'},
                {'at': '^cracked', 'sel': '.fs-casecard .fs-case-ask', 'fx': 'glow'}],
    'warmup': [{'at': '^photo', 'sel': '.fs-gh-hook', 'fx': 'pop', 'scroll': True},
               {'at': '^box', 'sel': '#tab-vocab .fs-in-frame', 'fx': 'glow'},
               {'at': '^ghost', 'sel': '.fs-gh-stage', 'fx': 'glow', 'tag': 'Ghost marbles', 'scroll': True},
               {'at': '^Play', 'sel': '.fs-gh-play', 'fx': 'point'}],
    'part1': [{'at': '^sticky', 'sel': '.fs-ikn-deck', 'fx': 'pop', 'scroll': True},
              {'at': '^time$', 'sel': '.fs-ikn-who em', 'fx': 'glow', 'all': True},
              {'at': '^before', 'sel': '.fs-ikn-zone[data-k="before"]', 'fx': 'glow'},
              {'at': '^after', 'sel': '.fs-ikn-zone[data-k="after"]', 'fx': 'glow'},
              {'at': '^wrong', 'sel': '.fs-ikn-test', 'fx': 'wiggle'}],
    'part2': [{'at': '^flag', 'sel': '.fs-flg-stage', 'fx': 'pop', 'tag': 'Your flag', 'scroll': True},
              {'at': '^roll', 'sel': '.fs-flg-roll', 'fx': 'point'},
              {'at': '^tape', 'sel': '.fs-flg-stage', 'fx': 'glow'},
              {'at': '^ramp', 'sel': '.fs-flg-rp', 'fx': 'pop'},
              {'at': '^meter', 'sel': '.fs-flg-meter', 'fx': 'glow'}],
    'explore': [{'at': '^cradle', 'sel': '.fs-nc-stage', 'fx': 'glow', 'scroll': True},
                {'at': '^Pick', 'sel': '.fs-nc-pick', 'fx': 'pop'},
                {'at': '^Predict', 'sel': '.fs-nc-pred', 'fx': 'pop'},
                {'at': '^drag', 'sel': '.fs-nc-let', 'fx': 'point'},
                {'at': '^trials', 'sel': '.fs-nc-table', 'fx': 'glow'}],
    'assignment': [{'at': '^clues', 'sel': '.fs-board', 'fx': 'glow'},
                   {'at': '^Crack', 'sel': '.fs-solve', 'fx': 'pop', 'scroll': True},
                   {'at': '^sign', 'sel': '.fs-game[data-mod="signmaker"]', 'fx': 'glow'},
                   {'at': '^two$', 'sel': '#tab-assignment .pq', 'fx': 'glow', 'all': True, 'scroll': True},
                   {'at': '^table', 'sel': '#tab-assignment .fs-in-frame', 'fx': 'pop', 'scroll': True},
                   {'at': '^C-E-R$', 'sel': '#tab-assignment .fs-cer', 'fx': 'glow', 'scroll': True}],
    'evidence': [{'at': '^classmate', 'sel': EV + ' > p', 'i': 0, 'fx': 'trace'},
                 {'at': '^bumpy', 'sel': '.fs-plan .fs-opt', 'i': 2, 'fx': 'glow'},
                 {'at': '^cradle', 'sel': '.fs-plan .fs-opt', 'i': 4, 'fx': 'glow'},
                 {'at': '^side', 'sel': '.fs-plan .fs-plan-row', 'i': 0, 'fx': 'pop'},
                 {'at': '^explain', 'sel': '.fs-cer .fs-cer-row', 'i': 2, 'fx': 'glow', 'scroll': True}],
    'closing': [{'at': '^closed', 'sel': '.fs-specimen', 'fx': 'pop', 'scroll': True},
                {'at': '^limit', 'sel': '.fs-game[data-mod="signmaker"]', 'fx': 'glow'},
                {'at': '^envelope', 'sel': '.fs-specimen', 'fx': 'glow'},
                {'at': '^Next', 'sel': '#tab-assignment .callout-tip', 'fx': 'glow'}],
}
D['fold'] = {'cradlefree': {'icon': '⚪', 'tease': 'A cradle with 5 or 7 balls. Predict, let go, and build a prediction streak.', 'open': 'Play'}}
CRED = json.load(open('credits.json', encoding='utf-8')) if os.path.exists('credits.json') else {}
if CRED.get('cradle'):
    D['ghosts']['hook']['credit'] = CRED['cradle']; D['cradle']['photo']['credit'] = CRED['cradle']
D['cueWords'] = json.load(open('cuewords.json', encoding='utf-8')) if os.path.exists('cuewords.json') else {}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
