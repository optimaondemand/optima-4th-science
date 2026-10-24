#!/usr/bin/env python3
"""Writes data.json and fixes.json for 19.02 (run from this folder). Case 19 part 2 "The Rematch" (Sam Park, Dune Hill).
New modules: stopwatch (time the derby car 3 times), lockdown (padlock every variable but one), dotplot (trials drop as dots, drag the
middle marker), detective (Coach Dee's 9-trial notebook, the fluke = a sock on the track), bullseye (bonus game after the case),
case.thread (a phone text thread), bulletin skin:'phone' + tone:'ring' (Coach Dee's voicemail, folded). No tool (19.01 has the radar gun)."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../18-01/data.json', encoding='utf-8'))
O = json.load(open('../19-01/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
PS = '<p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

# ---------------------------------------------------------------- ticked fixes (Bethany, 24 Oct 2026)
fx('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist already asks for a 9-trial data table',
   '🎨 Part C &mdash; Build Your Own Food Chain', '📏 Part C &mdash; My 9-Trial Table')
fx('fix', 'copy-paste leftover: Part C task from 9.01 (now the 9-trial table, typed on the page)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Run 3 trials from each start with a ramp at home, or use Coach Dee’s fixed numbers. Fill in your table, find each average, and write a claim with numbers.</p>', True)
fx('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'unit label: “Ecosystems & Energy” is a leftover; weeks 18–24 are Unit 5', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Energy, Motion &amp; Collisions</div>')
fx('fix', 'speed and energy is physical science, not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standard: 4-PS3-1 is the speed-and-energy standard (4-ESS3-1 is about energy resources)', '<div class="info-value">4-ESS3-1 · TEKS 4.8(A)</div>', '<div class="info-value">4-PS3-1 · TEKS 4.8(A)</div>')
fx('fix', 'the warm-up’s imagined trials (7, 9, 8, 8, 10) become the student’s own stopwatch times, so the page and the game match',
   r"<p>Imagine you roll a marble down a ramp ONE time.*?</p>\s*<p>Now imagine you roll the marble FIVE times\..*?</p>",
   "<p>Can you time a race perfectly? The derby car rolls between two flags. Time it three times with the stopwatch. Will your times match?</p>", True)
fx('fix', 'the AI table picture (its arrow measures the gap between the ramp and the block, not how far the block moved; cm ramp heights mixed with inch distances) and the boxes that lean on it are gone; Dot plot drop replaces them and the tap diagram. Also lean: Key Concept (repeats Part 1), Stop & Reason, Observe & Reason, the Amazing Fact, the Florida connection (an FSU sports-lab claim we could not verify) and Go Deeper. Part 4 = Data detective (the old Explore was a copy of 19.01’s); next button goes to Self-Check',
   r'<div class="lesson-figure scroll-reveal">\s*<div class="lesson-figure-label">📊 A Real Investigation Data Table</div>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 4 · Data Detective</h3>\n      ' + PS + 'Coach Dee ran 9 trials after all! But one number in her notebook looks strange. Can you find it?</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; plain words; no dash',
   "Hold this question in your head as you work. By the end of the lesson, you'll run a small controlled investigation, collect data across multiple trials, and write a claim backed by numbers — not just observations.",
   "Keep this question in mind. By the end, you’ll run a fair test with many trials and back up your claim with numbers.")
fx('plain', 'warm-up title matches the new warm-up', '🌅 Warm-Up: Two Tests Are Better Than One', '🌅 Warm-Up: The Stopwatch Race')
fx('plain', 'warm-up subtitle', 'Why scientists never trust just one try', 'Can you time the same race three times?')
fx('plain', 'no dashes; shorter',
   "Real scientists run their tests many times — those are called TRIALS — so they don't accidentally trust a lucky or unlucky result. Today you'll plan an investigation, run trials, and let the DATA do the talking.",
   "Real scientists run a test many times. Each run is called a TRIAL. That way, one lucky or unlucky try can’t fool them.")
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', 'no dash', 'Real proof needs a fair test — what scientists call a <span class="vtip">controlled', 'Real proof needs a fair test, which scientists call a <span class="vtip">controlled')
fx('plain', 'no dash', '"the energy was bigger because of the speed!" — you can\'t be sure.', '“the energy was bigger because of the speed!” You can’t be sure.')
fx('plain', 'no dash', '</span></span> — usually at least 3, but more if you can.', '</span></span>, usually at least 3, and more if you can.')
fx('plain', 'no dash', 'measured with a ruler — how far did the target move?', 'measured with a ruler. How far did the target move?')
fx('plain', 'no dash', 'measured with a stopwatch — how long did the ball take to reach the bottom of the ramp?', 'measured with a stopwatch. How long did the ball take to reach the bottom of the ramp?')
fx('plain', 'misconception kept, plain, no dash',
   r'<p><strong>Common misconception:</strong> Some people think one trial is enough if it "looks right\."[^<]*</p>',
   '<p><strong>Watch out:</strong> Some people think one trial is enough if it “looks right.” Real scientists run many trials, so their answer comes from a pattern, not one lucky moment.</p>', True)
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'shorter closing; points to week 20',
   r'<p><strong>Nicely done\.</strong> You can now design a.*?</p>',
   '<p><strong>Nicely done.</strong> You ran a fair test, used many trials and caught a fluke. Next week, Sam follows the energy: how does it MOVE from one place to another?</p>', True)

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: Stop & Think (Lock it down is the thinking stop for Part 1)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (a copy of 19.01’s; Part 4 is Data detective now)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 5 removed (Bethany kept 6 and 7; it pointed at the removed diagram)', r'<div class="pq">\s*<span class="pq-num"[^>]*>5</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: renumber Part B (6 → 5)', '<span class="pq-num" style="background:#D4772C;">6</span>', '<span class="pq-num" style="background:#D4772C;">5</span>')
fx('cut', 'lean: renumber Part B (7 → 6)', '<span class="pq-num" style="background:#D4772C;">7</span>', '<span class="pq-num" style="background:#D4772C;">6</span>')
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C typed on the page',
   'A data table with at least 9 trials (3 trials at each of 3 speeds), full measurements, and an evidence-based claim.',
   'My 9-trial table (3 trials from each start), the averages and a claim with numbers. (A sketch is a bonus.)')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether one trial is enough for a real investigation, and supported it with two pieces of evidence from the lesson.',
   '<strong>Use Your Evidence:</strong> My claim about whether one trial is enough, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', True)

# ---------------------------------------------------------------- the story
SAM = Q['crew']['sam']
D = {
    'lesson': '19.02', 'week': 19, 'day': 2, 'guide': 'sam', 'prefix': 'g4sci-19-2', 'manifestKey': '19-02',
    'paths': P['paths'], 'crew': {'sam': SAM},
    'expedition': {'num': 19, 'title': 'The Rematch'},
    'ambient': {'icon': '🌊', 'label': 'Ocean sounds'},
    'case': {
        'num': 19, 'title': 'The Rematch', 'style': 'derby',
        'hook': 'Uh oh. Coach Dee runs the Dune Hill derby team, and she just texted me about my hay bale plan.',
        'threadHead': 'Coach Dee 🏁', 'threadSub': 'Saturday, 7:42 AM',
        'thread': [
            {'who': 'Coach Dee', 't': 'Sam! Your hay plan is WRONG. I tested it myself this morning. 😤'},
            {'who': 'Coach Dee', 't': 'Light car from the HIGH ramp: 15 inches. Heavy car from the LOW ramp: 16 inches. Same push! Height doesn’t matter.'},
            {'who': 'Sam', 'me': True, 't': 'Hmm. Was it the same car both times?'},
            {'who': 'Coach Dee', 't': 'No, the heavy one has the new wheels. Oh, and it got windy.'},
            {'who': 'Coach Dee', 't': 'One try each. That’s proof, right? 🏁'},
            {'who': 'Sam', 'me': True, 't': 'Let’s run a FAIR test. I’ll send you the results.', 'time': 'Read 7:45 AM'}],
        'stills': [],
        'question': 'Does the start height really matter? How can Sam prove it to Coach Dee?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'stopwatch', 'icon': '⏱️', 'where': 'Warm-Up: the stopwatch race', 't': 'You timed the same car 3 times and got 3 different times. Small differences are normal, so one try can fool you.'},
            {'id': 'lockdown', 'icon': '🔒', 'where': 'The Lesson, Part 1: lock it down', 't': 'Coach Dee changed 4 things at once. When ONLY the start height changed, the High start pushed 25 inches and the Low start only 8.'},
            {'id': 'dotplot', 'icon': '📊', 'where': 'The Lesson, Part 2: dot plot drop', 't': 'Many trials pile up around a typical number. The middle of the pile is easier to trust than any one try.'},
            {'id': 'detective', 'icon': '🧦', 'where': 'The Lesson, Part 4: data detective', 't': 'One odd trial was caused by a sock on the track. Checking and redoing it kept the test honest: Low 8, Middle 16, High 25 inches.'},
        ],
        'solve': {
            'title': 'How can Sam prove it?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Coach Dee is right. Her test proves start height doesn’t matter.', 'why': 'Check Clue 2. How many things changed in her test?'},
                {'t': 'One more try from each ramp will settle it.', 'why': 'Check Clues 1 and 3. Can one try be trusted?'},
                {'t': 'Run a fair test: same car, same wheels, same weather, and change ONLY the start height. Do several trials. The High start pushes farthest, so the hay plan stays.', 'right': True,
                 'why': 'Case cracked! A fair test with many trials shows the High start really does push the hay the farthest. Coach Dee agrees, and she wants a rematch. Bullseye Derby is open, just below!'},
                {'t': 'Throw out any numbers that don’t match the plan.', 'why': 'Check Clue 4. What should you do with an odd number?'},
            ]},
    },
    'stopwatch': {
        'afterText': 'Will your times match', 'kicker': 'Warm-Up game', 'title': 'The stopwatch race',
        'todo': ['Press Roll the car.', 'Press Start when the car passes the green flag. Press Stop at the red flag.', 'Do it 3 times. Do your times match?'],
        'why': {'icon': '⏱️', 'q': 'Why time it?', 't': 'Distance ÷ time = speed. To know how fast the car goes, you need a good time.'},
        'alt': 'A model: a derby car rolls along a flat track past a green START flag and a red STOP flag.', 'model': 'a model',
        'real': 2.5, 'tries': 3, 'goBtn': 'Roll the car', 'tapBtn': 'Start', 'stopBtn': 'Stop', 'flagA': 'START', 'flagB': 'STOP',
        'logLabel': 'Your times', 'tryWord': 'Try', 'realWord': 'Laser timer', 'everyWord': 'every time',
        'realLine': 'The car takes exactly the same time every run. Your times are a little different because people press a little early or a little late.',
        'missLine': 'The car got away! Roll it again. Press Start at the green flag and Stop at the red flag.',
        'early': 'That was early! The car hadn’t reached the green flag. It still counts. Real scientists make small timing mistakes too.',
        'q': 'Why didn’t your 3 times match?',
        'opts': [{'t': 'People press a little early or late, so every try is a little different.', 'ok': True},
                 {'t': 'The car changed speed every time.', 'miss': 'Read the laser timer. Was the car’s real time the same every run?'},
                 {'t': 'I did something wrong, so I should throw those times out.', 'miss': 'Small differences are normal in every test. That’s why scientists do several trials, not why they throw them out.'}],
        'win': 'Same car, same flags, three different times. That’s why scientists never trust just one try. Clue 1!'},
    'lockdown': {
        'afterText': 'controlling variables matters', 'kicker': 'Part 1 game', 'title': 'Lock it down',
        'todo': ['Run Coach Dee’s test first.', 'Red rows changed between her two runs. Click 🔓 to keep a row the same.', 'Lock everything except the ONE thing we test. Then run the fair test.'],
        'why': {'icon': '🔒', 'q': 'What is a variable?', 't': 'Anything that could change in a test. A fair test changes only ONE variable and keeps all the others the same.'},
        'runA': 'Run A', 'runB': 'Run B', 'testK': 'start', 'testTag': 'the one thing we test',
        'rows': [{'k': 'car', 'icon': '🏎️', 't': 'Car', 'a': 'Light car', 'b': 'Heavy car'},
                 {'k': 'wheels', 'icon': '⚙️', 't': 'Wheels', 'a': 'Old sticky wheels', 'b': 'New smooth wheels'},
                 {'k': 'wind', 'icon': '🌬️', 't': 'Wind', 'a': 'Blowing against it', 'b': 'Blowing behind it'},
                 {'k': 'start', 'icon': '⛰️', 't': 'Start', 'a': 'High ramp', 'b': 'Low ramp'},
                 {'k': 'bale', 'icon': '🌾', 't': 'Hay bale', 'a': 'Same bale', 'b': 'Same bale'}],
        'testMiss': 'If both cars start at the same height, what would you be testing? Keep the start ramps different. Lock the OTHER rows.',
        'stampFair': 'FAIR TEST', 'stampUnfair': 'UNFAIR TEST', 'unit': 'in',
        'deeBtn': 'Run Coach Dee’s test', 'fairBtn': 'Run the fair test',
        'deeResult': {'a': 15, 'b': 16, 't': 'About the same push. But the car, the wheels and the wind changed too. Which one made the difference? Nobody can tell!'},
        'fairResult': {'a': 25, 'b': 8, 't': 'Now ONLY the start height changed. The High start pushed 25 inches. The Low start pushed 8. The height made the difference.'},
        'q': 'Why couldn’t Coach Dee trust her test?',
        'opts': [{'t': 'She changed lots of things at once, so she can’t tell which one caused the result.', 'ok': True},
                 {'t': 'She used a hay bale.', 'miss': 'The hay bale stayed the same in both runs. Look at the red rows.'},
                 {'t': 'Her cars were too slow.', 'miss': 'Speed isn’t the problem. How many rows were different between her two runs?'}],
        'win': 'Change ONE thing, keep the rest the same. That’s a fair test! Clue 2!'},
    'dotplot': {
        'afterText': 'not one lucky moment', 'kicker': 'Part 2 game', 'title': 'Dot plot drop',
        'todo': ['Press Run a trial. Each trial drops a dot (Middle start, how far the bale slid).', 'Run at least 5 trials.', 'Drag the gold marker to the middle of the dots (or tap the number line).'],
        'why': {'icon': '📊', 'q': 'What is a dot plot?', 't': 'A number line with one dot for each result. Where the dots pile up shows the typical result.'},
        'alt': 'A number line from 0 to 30 inches with a dot for each trial and a gold marker.',
        'min': 0, 'max': 30, 'step': 1, 'unit': 'inches the hay bale slid', 'trials': [16, 15, 17, 16, 14, 16, 17], 'need': 5, 'tol': 1,
        'runBtn': 'Run a trial', 'markerLabel': 'middle', 'trialWord': 'trial', 'trialsWord': 'trials',
        'startLine': 'Run the first trial. One dot can’t tell you much yet.',
        'trust': [{'n': 1, 'icon': '🤔', 'head': '1 trial', 't': 'Just one dot. Was it a normal run or a lucky one? You can’t tell yet.'},
                  {'n': 3, 'icon': '🙂', 'head': '3 trials', 't': 'A pile is starting to form. Keep going.'},
                  {'n': 5, 'icon': '💪', 'head': '5 trials', 't': 'Now there’s a clear pile. Drag the gold marker to its middle.'},
                  {'n': 7, 'icon': '🏆', 'head': '7 trials', 't': 'More trials, same pile. Now you can really trust the middle.'}],
        'moreLine': 'Run at least {n} trials first. One or two dots can fool you.',
        'lowLine': 'More dots are to the right of your marker. Slide it toward the middle of the pile.',
        'highLine': 'More dots are to the left of your marker. Slide it toward the middle of the pile.',
        'q': 'Why are 5 trials better than 1?',
        'opts': [{'t': 'The dots pile up around a typical number, so one odd try can’t fool you.', 'ok': True},
                 {'t': 'More trials make the car go faster.', 'miss': 'The car is the same every trial. What does the pile of dots show you?'},
                 {'t': 'Five is the rule for every test.', 'miss': 'There’s no magic number. What happens to the pile as you add dots?'}],
        'win': 'The middle of the pile is about 16 inches. Many trials show the pattern. Clue 3!'},
    'bulletin': {
        'afterText': 'not one lucky moment', 'kicker': 'Bonus · New voicemail', 'title': 'Coach Dee’s voicemail', 'skin': 'phone', 'tone': 'ring',
        'todo': ['Press Play and listen. You can read along.', 'Tap the 3 things that made her test UNFAIR.'],
        'device': 'Voicemail', 'deviceSub': 'Coach Dee · 0:20', 'station': '1 new message from Coach Dee',
        'playBtn': 'Play the voicemail', 'againBtn': 'Play it again', 'audio': 'voicemail', 'paperHead': 'VOICEMAIL · COACH DEE',
        'lines': [
            'Sam, it’s Coach Dee. I tested your hay plan myself!',
            'I sent the [[cars|light car down the High ramp and the heavy car]] down [[x:The start ramp is the ONE thing she is testing. Changing it is OK! Look for something else that changed.|the Low ramp]].',
            'Oh, and it got [[wind|really windy]] right after the first run.',
            'They pushed the bale about the same, so height doesn’t matter. I only needed [[once|one try each]]. Call me back!'],
        'foundLabel': 'What made her test unfair', 'dangerWord': 'Problem', 'countIcon': '🔒', 'countWord': 'problems found',
        'dangers': [{'id': 'cars', 'icon': '🏎️', 't': 'Different cars', 'does': 'a light car and a heavy car with new wheels'},
                    {'id': 'wind', 'icon': '🌬️', 't': 'The wind changed', 'does': 'windy for only one of the runs'},
                    {'id': 'once', 'icon': '1️⃣', 't': 'One try each', 'does': 'one try can be a fluke'}],
        'win': 'Three problems in one test! No wonder the results were confusing.'},
    'detective': {
        'afterText': 'looks strange', 'kicker': 'Part 4 game', 'title': 'Data detective',
        'todo': ['Read Coach Dee’s notebook. Tap the number that doesn’t fit.', 'Decide what to do with it.'],
        'why': {'icon': '🔎', 'q': 'What is a fluke?', 't': 'A result that is way off because of an accident, not because of the thing you are testing.'},
        'head': 'Coach Dee’s Fair Test · Dune Hill', 'sub': 'Same car, same wheels, calm air. Only the start changes. How far the hay bale slid:',
        'note': 'Trial 3 from the Middle was weird. I was busy hanging my lucky socks on the fence to dry… (Dee)',
        'unit': 'in', 'colStart': 'Start', 'trialWord': 'Trial',
        'rows': [{'k': 'low', 't': 'Low', 'trials': [8, 7, 8]}, {'k': 'mid', 't': 'Middle', 'trials': [16, 15, 3]}, {'k': 'high', 't': 'High', 'trials': [25, 24, 26]}],
        'fluke': {'row': 'mid', 'i': 2, 'redo': 16},
        'fitLine': 'That number fits with the others in its row. Look for one that is way off.',
        'choiceQ': 'You found it! What should a scientist do with this odd number?',
        'choices': [{'t': 'Keep it. Every number counts.', 'miss': 'If something went wrong in that run, it isn’t telling you about the start height. Find out first.'},
                    {'t': 'Throw it out. It doesn’t match.', 'miss': 'Throwing out a number just because you don’t like it isn’t fair. First find out WHY it’s odd.'},
                    {'t': 'Check what happened, then redo that trial.', 'ok': True}],
        'replay': {'head': 'Replay of the odd trial', 'rec': 'REPLAY · MIDDLE START, TRIAL 3',
                   'alt': 'A replay: the derby car rolls down the hill and stops short when it hits a sock lying on the track.',
                   'cap': 'A sock blew off the fence onto the track! The car hit it and stopped early. The odd number came from an accident, not from the start height.'},
        'redoBtn': 'Redo trial 3 (sock removed)', 'avgLabel': 'Averages: the typical push from each start (inches)',
        'q': 'What do the averages show?',
        'opts': [{'t': 'The higher the start, the farther the push: about 8, 16 and 25 inches.', 'ok': True},
                 {'t': 'Start height doesn’t matter.', 'miss': 'Compare the three bars. Are they the same height?'},
                 {'t': 'The Middle start was weird, so the test failed.', 'miss': 'The weird number had a cause, and you redid it. Read the bars now.'}],
        'win': 'Caught the fluke, checked it and redid it. Now the pattern is clear. Clue 4!'},
    'exploreMod': 'detective',
    'bullseye': {
        'after': '.fs-solve', 'kicker': 'Bonus game · unlocked after the case', 'title': 'Bullseye Derby',
        'todo': ['Pick a start height with the slider.', 'Press Let it roll. Try to stop right on the bullseye!', 'Beat all 3 levels. Can you get 9 stars?'],
        'why': {'icon': '🎯', 'q': 'How does it work?', 't': 'A higher start means more speed and more energy, so the car rolls farther before rubbing stops it.'},
        'alt': 'A model: a hill on the left, a flat track with distance marks and a red and white bullseye target.', 'model': 'a model',
        'hMin': 1, 'hMax': 12, 'hStep': 1, 'unit': 'ft',
        'levels': [{'name': 'Smooth pavement', 'surface': 'pavement', 'k': 5, 'target': 30, 'tip0': 'Level 1: smooth pavement. Pick a height and let it roll!', 'tip': 'Higher start, more energy, longer roll.'},
                   {'name': 'Smooth pavement, far target', 'surface': 'pavement', 'k': 5, 'target': 45, 'tip0': 'Level 2: the bullseye moved farther away. More height, or less?', 'tip': 'More energy carried it farther.'},
                   {'name': 'Bumpy sand', 'surface': 'sand', 'k': 3, 'target': 24, 'tip0': 'Level 3: SAND! Sand rubs the wheels more, so the car stops sooner. Adjust your height!', 'tip': 'Sand takes the energy away faster.'}],
        'goBtn': 'Let it roll', 'nextBtn': 'Next level', 'lockLine': 'Crack the case first. Then Bullseye Derby opens.',
        'lines': {'level': 'Level', 'target': 'Target', 'best': 'best', 'height': 'Start height', 'stopped': 'It stopped at',
                  's3': 'BULLSEYE! Three stars!', 's2': 'So close! Two stars.', 's1': 'On the target! One star.',
                  'short': 'Too slow! Not enough energy to reach the target. Start higher.', 'long': 'Too fast! Too much energy, and it blasted past the target. Start lower.',
                  'done': 'You beat every level, derby champion!', 'again': 'Play again for more stars'}},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Not that kind of trial! In science, what is one run of a test called?', 'C': 'A measurement is a number you get. What do we call one run of the test?'},
        'q2': {'B': 'Where it happens doesn’t make it fair. Think about Lock it down.', 'C': 'Scientists don’t control the result. What did you lock in Lock it down?'},
        'q3': {'A': 'Changing the marble changes two things! Which change controls speed?', 'B': 'The target should stay the same. Which change controls the marble’s speed?'}},
    'flags': {
        'ans-2': [
            {'label': 'more than one trial', 're': 'trial|tries|try|times|again|more than one|many'},
            {'label': 'the word pattern', 're': 'pattern'},
            {'label': 'why', 're': 'fluke|luck|lucky|mistake|wrong|odd|weird|different|trust|sure|accident|sock|early|late'}],
        'ans-3': [
            {'label': 'two things changed', 're': 'two|both|2|more than one|changed|change'},
            {'label': 'can’t tell which one', 're': 'which|know|sure|tell|cause|caused|because|why'},
            {'label': 'a lesson word', 're': 'controlled|control|fair|variable|trial|test|measure'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|not enough|enough'},
            {'label': 'two pieces of evidence', 'any': ['trial', 'stopwatch', 'times', 'dot', 'middle', 'pattern', 'average', 'coach', 'dee', 'unfair', 'fair', 'wind', 'wheel', 'sock', 'fluke', 'nine', '9', 'three', '3', 'pile'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-2': 15, 'ans-3': 15, 'cer-4': 30},
    'hints': {
        'ans-2': ['Think about your 3 stopwatch times. Did they match?', 'Think about the dot plot. What did the pile of dots show?', 'Try: Scientists run more than one trial because ___. Many trials show a pattern, like ___.'],
        'ans-3': ['Think about Coach Dee’s test in Lock it down.', 'If two things changed, could you tell which one caused the result?', 'Try: They can’t trust it because ___. A controlled test ___.'],
        'cer-4': ['First decide: is one roll enough?', 'Think about your stopwatch times and Coach Dee’s sock.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'My 3 stopwatch times were all different, even for the same car.',
                'In the dot plot, the trials piled up around 16 inches. One try alone could be off.',
                'One of Coach Dee’s trials was only 3 inches because a sock was on the track.',
                'Coach Dee’s one-try test changed lots of things and gave a confusing answer.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · the rematch', 'length': '30–40 s',
                    'script': 'Uh oh. Coach Dee texted me. She tested my hay plan once, and she says start height doesn’t matter! Read our text messages. Is her test fair? Let’s find out, the scientist way.'},
        'warmup': {'label': 'Warm-Up · the stopwatch race (Clue 1)', 'length': '20–30 s',
                   'script': 'Can you time a race perfectly? Press Roll the car. Press Start at the green flag and Stop at the red flag. Do it three times. Do your three times match?'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Use a real stopwatch or phone timer for “time”; a ruler for “distance” and “measurement”.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · lock it down (Clue 2)', 'length': '20–30 s',
                  'script': 'Here’s Coach Dee’s test on my control panel. The red rows changed between her two runs. Click the padlocks to keep them the same. Lock everything except the start height. Then run both tests.'},
        'part2': {'label': 'Part 2 · dot plot drop (Clue 3)', 'length': '20–30 s',
                  'script': 'Time for lots of trials! Press Run a trial, again and again. Watch the dots pile up. Then drag the gold marker to the middle of the pile.'},
        'explore': {'label': 'Part 4 · data detective (Clue 4)', 'length': '25–35 s',
                    'script': 'Coach Dee ran nine trials after all! Look at her notebook. One number looks really strange. Tap it. Then decide: keep it, throw it out, or check and redo?'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s',
                       'script': 'Do you have all four clues? Crack the case at the top of this tab. Then answer two questions, fill in your nine trial table, and finish your C-E-R. And after the case, a bonus game opens!'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · my 9-trial table', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says one roll down a ramp is a whole investigation. Hmm. Think about your stopwatch times and Coach Dee’s sock. Pick your side, tap two pieces of evidence, then explain how they prove your claim.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease week 20 (how energy moves).',
                    'script': 'Case closed! Coach Dee says the hay plan stays, and she challenged you to Bullseye Derby! Next week, we follow the energy. How does it move from one place to another?'},
    },
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Your 3 stopwatch times (Warm-Up)',
        'The FAIR TEST stamp (The Lesson)',
        'Your dot plot with the gold marker (The Lesson)',
        'The sock in the replay (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['My fair test setup', 'A dot plot of my trials', 'The sock that caused the fluke'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 3,
                           'prompts': ['Draw your ramp and target', 'Label the ONE thing you change', 'Label two things you keep the same']}]},
    'hlCoach': copy.deepcopy(Q['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🧦', 'name': 'The fluke sock',
                 'line': 'You cracked Case 19 part 2, and Coach Dee’s fluke sock goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next week: how energy moves.'},
    'notebookTitle': 'Unit 5 · Energy, Motion & Collisions',
    'notebook': copy.deepcopy(O['notebook']),
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You’re ready to run a fair test.',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'list', 'find': {'sel': '.fs-game[data-mod="stopwatch"]'},
         'label': 'Warm-Up: three things that could make two tries different', 'q': 'Warm-Up: Three things that could make two tries of the same test come out different',
         'title': 'Your turn: name three things that could make two tries of the same test come out a little different.', 'min': 3, 'unit': 'things', 'addLabel': '+ Add another',
         'ph': ['Pressing the stopwatch late', 'A gust of wind', 'Something else…']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'hide-nw', 'type': 'hide', 'find': {'sel': '.act-warmup .socratic-q', 'text': 'Notice'}},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Run 3 trials from each start'},
         'label': 'Part C: My 9-trial table', 'q': 'Part C: My 9-trial table, the averages and my claim',
         'title': 'My 9-trial table (how far the target moved)',
         'fields': [{'t': 'LOW start: trial 1, 2, 3 and the average', 'icon': '🐢', 'ph': 'Trials: ___, ___, ___. Average: ___'},
                    {'t': 'MIDDLE start: trial 1, 2, 3 and the average', 'icon': '🚲', 'ph': 'Trials: ___, ___, ___. Average: ___'},
                    {'t': 'HIGH start: trial 1, 2, 3 and the average', 'icon': '🚀', 'ph': 'Trials: ___, ___, ___. Average: ___'},
                    {'t': 'My claim with numbers', 'icon': '📊', 'ph': 'Faster objects carry more energy. My evidence is that…', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Is one roll a whole investigation?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-2': 'Part B · Question 5', 'ans-3': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] == '19.02': n.update({'icon': '🧦', 'name': 'The fluke sock'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'A fair test changes only one thing and keeps everything else the same.',
    'key': ['fair', 'test', 'only', 'one', 'same'],
    'small': ['A', 'and', 'the'],
    'model': 'A scientist might highlight “fair test”, “only one thing” and “the same”. Those words hold the big idea. Small words like “a” and “and” don’t carry the idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me explain what makes evidence trustworthy?']

# ---------------------------------------------------------------- Spotlight: what lights up as Sam talks
EV = '#tab-assignment .act-body > div:has(> .fs-plan)'
D['cues'] = {
    'welcome': [{'at': '^Dee', 'sel': '.fs-casecard .fs-th3-top', 'fx': 'glow'},
                {'at': '^once', 'sel': '.fs-casecard .fs-th3-m', 'i': 4, 'fx': 'pop'},
                {'at': '^matter', 'sel': '.fs-casecard .fs-th3-m', 'i': 1, 'fx': 'trace'},
                {'at': '^text', 'sel': '.fs-casecard .fs-th3-m', 'all': True, 'fx': 'wiggle'},
                {'at': '^fair', 'sel': '.fs-casecard .fs-th3-m.me', 'i': 1, 'fx': 'pop'}],
    'warmup': [{'at': '^race', 'sel': '.fs-game[data-mod="stopwatch"] .fs-why', 'fx': 'glow', 'scroll': True},
               {'at': '^Roll', 'sel': '.fs-sw-go', 'fx': 'point'},
               {'at': '^green', 'sel': '.fs-sw-svg', 'fx': 'pop', 'tag': 'green flag = Start'},
               {'at': '^Stop', 'sel': '.fs-sw-watch', 'fx': 'pop'},
               {'at': '^match', 'sel': '.fs-sw-log', 'fx': 'glow'}],
    'part1': [{'at': '^panel', 'sel': '.fs-ld-panel', 'fx': 'glow', 'scroll': True},
              {'at': '^red', 'sel': '.fs-ld-row.diff', 'all': True, 'fx': 'wiggle'},
              {'at': '^padlocks', 'sel': '.fs-ld-lk', 'all': True, 'fx': 'pop'},
              {'at': '^start', 'sel': '.fs-ld-row.test', 'fx': 'glow', 'tag': 'Leave this one'},
              {'at': '^run', 'sel': '.fs-ld-btns', 'fx': 'point'}],
    'part2': [{'at': '^trials', 'sel': '.fs-game[data-mod="dotplot"] .fs-why', 'fx': 'glow', 'scroll': True},
              {'at': '^Run', 'sel': '.fs-dpl-run', 'fx': 'point'},
              {'at': '^dots', 'sel': '.fs-dpl-svg', 'fx': 'pop'},
              {'at': '^gold', 'sel': '.fs-dpl-box', 'fx': 'glow', 'tag': 'Drag the gold marker'}],
    'explore': [{'at': '^nine', 'sel': '.fs-dt-book', 'fx': 'glow', 'scroll': True},
                {'at': '^notebook', 'sel': '.fs-dt-book table', 'fx': 'pop'},
                {'at': '^strange', 'sel': '.fs-dt-note', 'fx': 'trace'},
                {'at': '^decide', 'sel': '.fs-game[data-mod="detective"] .fs-todo li', 'i': 1, 'fx': 'trace'}],
    'assignment': [{'at': '^clues', 'sel': '.fs-board', 'fx': 'glow'},
                   {'at': '^Crack', 'sel': '.fs-solve', 'fx': 'pop', 'scroll': True},
                   {'at': '^two$', 'sel': '#tab-assignment .pq', 'fx': 'glow', 'all': True, 'scroll': True},
                   {'at': '^table', 'sel': '#tab-assignment .fs-in-frame', 'fx': 'pop', 'scroll': True},
                   {'at': '^C-E-R$', 'sel': '#tab-assignment .fs-cer', 'fx': 'glow', 'scroll': True},
                   {'at': '^bonus', 'sel': '.fs-game[data-mod="bullseye"]', 'fx': 'wiggle', 'scroll': True}],
    'evidence': [{'at': '^classmate', 'sel': EV + ' > p', 'i': 0, 'fx': 'trace'},
                 {'at': '^stopwatch', 'sel': '.fs-plan .fs-opt', 'i': 2, 'fx': 'glow'},
                 {'at': '^sock', 'sel': '.fs-plan .fs-opt', 'i': 4, 'fx': 'glow'},
                 {'at': '^side', 'sel': '.fs-plan .fs-plan-row', 'i': 0, 'fx': 'pop'},
                 {'at': '^explain', 'sel': '.fs-cer .fs-cer-row', 'i': 2, 'fx': 'glow', 'scroll': True}],
    'closing': [{'at': '^closed', 'sel': '.fs-specimen', 'fx': 'pop', 'scroll': True},
                {'at': '^Bullseye', 'sel': '.fs-game[data-mod="bullseye"]', 'fx': 'glow', 'scroll': True},
                {'at': '^Next', 'sel': '#tab-assignment .callout-tip', 'fx': 'glow'}],
}
D['fold'] = {'bulletin': {'icon': '📱', 'tease': 'Coach Dee left Sam a grumpy voicemail. Can you catch what’s wrong with her test?', 'open': 'Listen'},
             'bullseye': {'icon': '🎯', 'tease': 'Roll your derby car onto the bullseye. 3 levels, 9 stars. Can you beat Coach Dee?', 'open': 'Play'}}
D['cueWords'] = json.load(open('cuewords.json', encoding='utf-8')) if os.path.exists('cuewords.json') else {}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
