#!/usr/bin/env python3
"""Writes data.json and fixes.json for 25.02 (run from this folder). Case 25 part 2 "Zippy vs Scoot" (Sam Park, Palmetto Beach, the same morning as
25.01): the hot-dog stand's robot Zippy has a sandwich board, "FASTEST ON THE BEACH! 90 steps!", and Rosa wonders if she should trade Scoot.
New: case.board (a sandwich-board sign + two delivery tickets + Rosa's sticky), fixsign (Warm-Up: word magnets on the sign), scratch (Part 1:
scratch-off tickets), slicer (Part 2: cut each run into 10-second pieces), photofinish (the wow: a model slit camera + a real photo finish),
rematch (Part 3 = the old Explore: one finish flag, race clocks, a typed data table, the claim builds), hireform + headstart (after the case).
No Tool of the Week (25.01 has the compass). SCRIPTS ONLY (week 25 on): clip scripts written and budgeted, nothing generated."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../18-01/data.json', encoding='utf-8'))
O = json.load(open('../25-01/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
PS = '<p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)
def I(n): return 'images/25-02-' + n + '.jpg'

# ---------------------------------------------------------------- labels (standing approval)
fx('fix', 'unit label: “Ecosystems & Energy” is a leftover; the plan puts Module 25 in “Energy, Motion, and Waves”', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Energy, Motion &amp; Waves</div>')
fx('fix', 'speed is physical science, not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standards label: the plan’s CPALMS codes, CPALMS first; TEKS is a Texas code that isn’t in the plan', '<div class="info-value">SC.4.N.1.1, SC.4.P.12.2 · TEKS 4.2(A)</div>', '<div class="info-value">SC.4.P.12.2, SC.4.N.1.1</div>')
fx('fix', 'NGSS line: the plan lists 4-PS3-1 as support', '<div class="info-detail">NGSS 4-PS3-1 · Measuring & Recording Data</div>', '<div class="info-detail">NGSS 4-PS3-1 (support)</div>')
fx('fix', 'quarter label (Bethany, 22 Nov 2026): weeks 24 on are Q4 in the Canvas plan', '<div class="info-value">Q3 &middot; Week 25</div>', '<div class="info-value">Q4 &middot; Week 25</div>')
fx('fix', 'quarter label in the footer', 'Science &middot; Quarter 3 &middot; Student Lesson Page', 'Science &middot; Quarter 4 &middot; Student Lesson Page')

# ---------------------------------------------------------------- ticked fixes (Bethany, 24 Nov 2026)
# 22.01 leftovers in the Warm-Up
fx('fix', '22.01 leftover: the Warm-Up title and subtitle named the toaster lesson', '<div class="act-title">🌅 Warm-Up: What Goes In, What Comes Out?</div>\n        <div class="act-subtitle">A familiar device, a hidden change</div>',
   '<div class="act-title">🌅 Warm-Up: Fastest on the Beach?</div>\n        <div class="act-subtitle">Does the number prove it?</div>')
fx('fix', '22.01 leftover: the toaster warm-up → Zippy’s sign',
   '<p>Think about a toaster. You drop in cold bread. A minute later, you pull out hot toast.</p>',
   '<p>Zippy’s sign says it is the fastest robot on the beach. Does the number on the sign prove that?</p>')
fx('fix', '22.01 leftover: the toaster sketch → races you have seen (answered on the page)',
   "<p>In your notebook, draw a quick sketch of a toaster. On one side, label what goes IN. On the other, label what comes OUT. (Hint: bread on both sides — but something invisible is also going in. What is it?)</p>",
   '<p>Now think about races you’ve seen. How could you tell who was faster?</p>')
fx('fix', '22.01 leftover: Notice & Wonder about the toaster',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Notice &amp; Wonder</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover: “energy can CONVERT … toasters” callout',
   r'<div class="callout callout-tip">\s*<span class="callout-icon">💡</span>\s*<p>Today you\'ll learn that energy can CONVERT.*?</p>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover (ticked): “Device” is in the plan row, but its meaning was about converting energy. Same word, a meaning for this lesson',
   'A tool or machine designed to do a job. Most devices convert energy from one form to another — a flashlight, a toaster, a fan are all devices.',
   'A tool or machine made to do a job, like a stopwatch or a tape measure.')
# 9.01 leftovers
fx('fix', '9.01 leftover: Part C was a food chain; the checklist already asks for a speed data table', '🎨 Part C &mdash; Build Your Own Food Chain', '🎨 Part C &mdash; My Speed Data Table')
fx('fix', '9.01 leftover: Part C task (now the lesson’s own data table: a home race or the rematch numbers, drawn on the sketch pad, + claim and evidence)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Race two things that roll (toy cars, balls or marbles) down a book ramp at home, from the same start to the same finish line. Or use your numbers from the Fair Rematch. Draw your data table and write your claim.</p>', True)
fx('fix', '9.01 leftover: Reflect asked about a hawk; the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'supply list: what Part C can use', r'<span class="need-chip"><span>✏️</span>Colored pencils</span>', '<span class="need-chip"><span>🚗</span>Optional: two things that roll, a book for a ramp and a timer</span>', True)

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; plain words', r"<p>Hold this question in your head as you work\. By the end of the lesson.*?</p>",
   "<p>Keep this question in mind. By the end, you’ll measure how far and how long, run a fair race, and use your data to prove who was faster.</p>", True)
fx('plain', 'cut filler; no dash', r"<p>These six words show up all through the lesson\. <strong>Tap a card to flip it</strong>.*?</p>",
   "<p><strong>Tap a card to flip it</strong> and read what the word means.</p>", True)
fx('plain', 'Word Wall: no dash; steps added (the lesson measures in steps)', 'How far an object traveled — measured in feet, meters, miles, etc.', 'How far something traveled. We measure it in feet, meters, miles or steps.')
fx('plain', 'Word Wall: no dash', 'How long an event took — measured in seconds, minutes, hours, etc.', 'How long something took. We measure it in seconds, minutes or hours.')
fx('plain', 'Word Wall: no dash', 'Information you collect during an investigation — usually numbers like measurements, times, or counts.', 'Information you collect in an investigation, usually numbers like measurements, times or counts.')
fx('plain', 'Part 1: no dashes; same idea',
   '<p>"Maya ran 30 feet in 5 seconds" tells you her speed in a useful way. "Maya ran 30 feet" alone doesn\'t — she could have been racing or strolling. "Maya ran for 5 seconds" alone doesn\'t — she could have walked or sprinted. You need BOTH numbers.</p>',
   '<p>"Maya ran 30 feet in 5 seconds" tells you her speed. "Maya ran 30 feet" alone doesn\'t: she could have raced or strolled. "Maya ran for 5 seconds" alone doesn\'t either. You need BOTH numbers.</p>\n\n'
   '      <p>Speeds can be huge. A peregrine falcon (a hunting bird) can dive at over 240 miles per hour, faster than a car on the highway.</p>\n\n'
   '      <p>Try it with race tickets. Some numbers hide under silver scratch panels. Call each race before you scratch.</p>')
fx('plain', 'Part 2: no dash', ' — everything stays the same except the thing you\'re testing.', ': everything stays the same except the thing you\'re testing.')
fx('plain', 'Part 2: “distance ÷ time” in words a 4th grader can use (same meaning, same example); this is what the Slice game does',
   '<li><strong>Different both</strong> → compare distance ÷ time. A car going 60 miles in 1 hour is faster than one going 90 miles in 2 hours.</li>',
   '<li><strong>Both different</strong> → find how far each one goes in the SAME amount of time. A car that goes 60 miles in 1 hour is faster than one that goes 90 miles in 2 hours (only 45 miles each hour).</li>')
fx('cut', 'Part 2: the data table paragraph repeats the list line above it (Part 3 and Part C build the table)',
   '<p>A good data table has the OBJECT in column 1, the DISTANCE in column 2, the TIME in column 3, and (if you want) a NOTES column. Then comparing speeds is just looking at the numbers side by side.</p>',
   '')
fx('plain', 'plain words: “misconception” is a hard word; no dash; adds the wrong idea Bethany ticked (more seconds = faster); leads into the Slice game',
   '<p><strong>Common misconception:</strong> Some people think the object that goes the longest distance must be the fastest. Not always — you have to check the TIME too. A turtle that walks 10 feet in an hour went farther than a sprinter who runs 5 feet in a second, but the sprinter was MUCH faster.</p>',
   '<p><strong>Watch out:</strong> the one that went farther is not always faster. A turtle that walks 10 feet in an hour goes farther than a sprinter who runs 5 feet in one second, but the sprinter is MUCH faster. And more seconds does not mean more speed. Taking LONGER to go the same distance means you were slower.</p>\n\n'
   '      <p>Now back to Zippy and Scoot. Both of their numbers are different! Slice each run into 10-second pieces and compare the pieces.</p>')
fx('plain', 'Part B question 6 label (Gathered Answers)', 'data-label="A red car covers 20 feet in 4 seconds. A blue car ..."', 'data-label="The red car or the blue car: which is faster?"')
fx('plain', 'Part B question 7 label (Gathered Answers)', 'data-label="Why is a FAIR TEST important when measuring speed?..."', 'data-label="Why a fair test matters, and an unfair test"')
fx('plain', 'no dash in the classmate’s claim (same claim)', 'You can tell which car is fastest just by watching them — you don\'t need to time it.', 'You can tell which car is fastest just by watching them. You don\'t need to time it.')
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'closing: no dashes; plain words (same meaning; the teaser for 26.01 Waves is right)',
   ' to back up your claim. Next module, we leave motion for WAVES — slinkies, water, and sound — to see how energy moves without anything actually traveling far.</p>',
   ' to back up your claim. Next lesson: WAVES. Slinkies, water and sound carry energy from place to place, while the water or air itself only wiggles back and forth.</p>')

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: Stop & Think (the scratch-off tickets play the same Maya and Jordan race)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'hidden (ticked): the sample table picture’s FINISH arrow points near the 3½-foot mark while its bracket says 6 feet; the Slice game teaches the same idea. The file stays in images/',
   r'\s*<div class="lesson-figure scroll-reveal">.*?<div class="lesson-figure-caption">.*?</div>\s*</div>', '', True)
fx('cut', 'removed: Key Concept, the Stop & Reason about “the three devices above” (a 22.01 leftover), the Four Speed Comparisons tap diagram (its turtle and hare card was muddled; Part B question 5 that used it is cut), Observe & Reason, the falcon fact box (kept as one sentence in Part 1, ticked), the Daytona callout (true, cut for length) and Go Deeper. Part 3 = the old Explore (Toy Car Speed Test → the Fair Rematch); the next button goes to Self-Check.',
   r'\s*<div style="background:#FFF6E5;border:2\.5px solid #F0C97A;[^>]*>\s*<div[^>]*>⭐ Key Concept</div>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   '\n\n      ' + H3 + 'Part 3 · The Fair Rematch</h3>\n      ' + PS + 'Rosa wants proof she can trust: a fair rematch. Same start line, same finish line, same boardwalk. Only the robot is different. Set the finish, run the race and record your data.</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its toy car test is now Part 3’s Fair Rematch and Part C’s home race; its NASCAR fact (true: 200 mph is about 293 feet per second), Think like a scientist and Go Deeper go with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 5 removed (Bethany kept 6 and 7; 5 asked about the removed tap diagram)', r'<div class="pq">\s*<span class="pq-num"[^>]*>5</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 6 and 7 answered')
fx('cut', 'lean: Part C drawn and typed on the page', 'A 4-column speed data table for two objects, plus a claim and evidence about which was faster.',
   'What I raced, my claim and my evidence. Plus your labeled sketch: your 4-column data table.')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether you can tell speed just by watching, supported with two pieces of evidence.',
   '<strong>Use Your Evidence:</strong> My claim about whether you can tell speed just by watching, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a 9.01 leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Download your field journal (it has your answers and your data table sketch) and upload it to the Canvas assignment. Or copy your Gathered Answers (above) into Canvas.', True)

# ---------------------------------------------------------------- the story
SAM = Q['crew']['sam']
SC, ZP = '#2D7AA6', '#E8792E'
D = {
    'lesson': '25.02', 'week': 25, 'day': 2, 'guide': 'sam', 'prefix': 'g4sci-25-2', 'manifestKey': '25-02',
    'paths': P['paths'], 'crew': {'sam': SAM},
    'expedition': {'num': 25, 'title': 'Zippy vs Scoot'},
    'ambient': {'icon': '🌊', 'label': 'Beach morning'},
    'case': {
        'num': 25, 'title': 'Zippy vs Scoot', 'style': 'board', 'stills': [],
        'hook': 'The time capsule is found! Now Rosa needs a second delivery robot for the busy boardwalk. The hot-dog stand next door wants to trade her its robot, Zippy, for Sam’s robot, Scoot. Zippy’s sign makes a big promise. Rosa also has two delivery tickets from this morning.',
        'board': {
            'sign': {'top': 'ZIPPY DELIVERS!', 'big': 'FASTEST ON THE BEACH!', 'sub': '90 steps!', 'foot': 'Trade your old robot today. Ask at the hot-dog stand.'},
            'tickets': [
                {'n': '41', 'icon': '🌭', 'who': 'Zippy', 'to': 'One hot dog to the end of the pier', 'rows': [['Distance', '90 steps'], ['Time', 'on the back']], 'stamp': 'DELIVERED'},
                {'n': '15', 'icon': '🤖', 'who': 'Scoot', 'to': 'One cocoa to the lifeguard tower', 'rows': [['Distance', '60 steps'], ['Time', 'on the back']], 'stamp': 'DELIVERED'}],
            'sticky': 'Zippy went farther. Does that mean Zippy is faster? Should I trade Scoot?', 'stickySign': 'Rosa'},
        'question': 'Which robot is really faster, Zippy or Scoot, and how can we prove it?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'fixsign', 'icon': '🪧', 'where': 'Warm-Up: fix the sign', 't': '“90 steps” tells how FAR Zippy went, not how FAST. A distance alone can’t prove speed.'},
            {'id': 'scratch', 'icon': '🎟️', 'where': 'The Lesson, Part 1: scratch-off tickets', 't': 'To call a race, you need BOTH numbers: how far it went and how long it took.'},
            {'id': 'slicer', 'icon': '✂️', 'where': 'The Lesson, Part 2: slice it into seconds', 't': 'In every 10 seconds, Scoot covers 20 steps and Zippy covers 10. More seconds means slower, not faster.'},
            {'id': 'rematch', 'icon': '🏁', 'where': 'The Lesson, Part 3: the fair rematch', 't': 'In a fair rematch (same start, same finish, same boardwalk), Scoot took half as long as Zippy.'},
        ],
        'solve': {
            'title': 'Which robot is really faster?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Zippy. It went 90 steps, more than Scoot’s 60.', 'why': 'Check Clue 1. Steps tell how far, not how fast.'},
                {'t': 'Zippy. Its trip lasted 90 seconds, so it ran the longest.', 'why': 'Check Clue 3. Taking longer means slower, not faster.'},
                {'t': 'Scoot. Zippy went farther, but it took much longer. In a fair rematch over the same distance, Scoot finished in half the time.', 'right': True,
                 'why': 'Case cracked! Speed needs distance AND time, measured in a fair test. Rosa should keep Scoot.'},
                {'t': 'Nobody can tell. They both look fast when you watch them.', 'why': 'Check Clue 4. You don’t have to guess: measure the distance and the time.'},
            ]},
    },
    'fixsign': {
        'afterText': 'Does the number on the sign prove that?', 'kicker': 'Warm-Up game', 'title': 'Fix the sign',
        'todo': ['Read Zippy’s sign. Then read each sentence under it.', 'Drag a word magnet (a word you can stick on the sign) onto each blank. Or tap a magnet, then tap the blank.', 'A word that claims too much slides right off.'],
        'board': {'top': 'ZIPPY DELIVERS!', 'big': 'FASTEST ON THE BEACH!', 'sub': '90 steps!'},
        'fixed': {'top': 'ZIPPY DELIVERS!', 'big': 'WENT FARTHER TODAY!', 'sub': '90 steps (Scoot: 60)'},
        'lines': [
            {'pre': '“90 steps” tells us how', 'post': 'Zippy went.', 'ok': 'far', 'missAny': 'Steps are a distance. They tell how far something went.',
             'miss': {'fast': 'Steps are a distance. They tell how FAR, not how fast. Fast needs the time, too.'}},
            {'pre': 'Zippy went', 'post': 'than Scoot (60 steps).', 'ok': 'farther', 'missAny': 'Compare 90 steps and 60 steps. Which word fits?',
             'miss': {'faster': 'Zippy did go more steps. More steps means FARTHER. Faster needs the time, too.'}},
            {'pre': 'Is Zippy faster? We', 'post': '', 'ok': 'cant', 'missAny': 'Does the sign say how long the trip took?',
             'miss': {'yes': 'Not so fast! The sign never says how long the trip took.', 'no': 'Maybe, maybe not! The sign never says how long the trip took.'}}],
        'tiles': [{'k': 'fast', 't': 'FAST'}, {'k': 'far', 't': 'FAR'}, {'k': 'faster', 't': 'FASTER'}, {'k': 'farther', 't': 'FARTHER'}, {'k': 'yes', 't': 'YES, IT IS'}, {'k': 'cant', 't': 'CAN’T TELL YET'}],
        'trayLabel': 'Word magnets', 'dropHere': 'drop a word here', 'countWord': 'blanks fixed', 'pickFirst': 'Pick a word magnet first, then tap the blank.',
        'q': 'What does Zippy’s sign need before it can say FASTEST?',
        'opts': [{'t': 'How long the trip took: the time.', 'ok': True},
                 {'t': 'A bigger number of steps.', 'miss': 'More steps only means farther. What number is missing?'},
                 {'t': 'Bigger, brighter letters.', 'miss': 'Fancy letters don’t prove anything! What number is missing?'}],
        'win': 'A distance alone can’t prove speed. You need the time, too. Clue 1!'},
    'scratch': {
        'afterText': 'Call each race before you scratch.', 'kicker': 'Part 1 game', 'title': 'Scratch-off tickets',
        'todo': ['Read both tickets. Some numbers hide under silver.', 'Call it first: who is faster?', 'Scratch off the silver (rub it, or press the button). Then call it again.'],
        'roundWord': 'Race', 'scratchBtn': '🪙 Scratch the silver panels', 'rubWord': 'SCRATCH', 'rubTip': 'Rub the silver with your mouse or finger, or press the button.',
        'nextBtn': 'Next race ▸', 'doneBtn': 'Finish ▸', 'countWord': 'races called',
        'rounds': [
            {'id': 'dash', 't': 'The beach dash: Maya vs Jordan',
             'a': {'icon': '🏃', 'who': 'Maya', 'rows': [['Distance', '30 feet'], ['Time', '5 seconds', True]]},
             'b': {'icon': '🏃', 'who': 'Jordan', 'rows': [['Distance', '30 feet'], ['Time', '10 seconds', True]]},
             'q1': 'Who is faster?', 'opts1': [{'t': 'Maya', 'miss': 'Maybe! But you can’t see either time yet. Can you be sure?'}, {'t': 'Jordan', 'miss': 'Maybe! But you can’t see either time yet. Can you be sure?'}, {'t': 'I can’t tell yet', 'ok': True}],
             'line1': 'Smart! Same distance, but you can’t see either time. Scratch both panels.',
             'q2': 'Now who is faster?',
             'opts2': [{'t': 'Maya: same distance, fewer seconds.', 'ok': True},
                       {'t': 'Jordan: 10 seconds is more running, so he’s faster.', 'miss': 'More seconds means Jordan took LONGER to go the same 30 feet. Taking longer means slower.'},
                       {'t': 'I still can’t tell.', 'miss': 'You have both numbers now. Same distance: who took less time?'}],
             'line2': 'Same distance, less time = faster. Maya wins.'},
            {'id': 'scoot', 't': 'Scooter race: Ana vs Ben, 10 seconds each',
             'a': {'icon': '🛴', 'who': 'Ana', 'rows': [['Time', '10 seconds'], ['Distance', '80 feet', True]]},
             'b': {'icon': '🛴', 'who': 'Ben', 'rows': [['Time', '10 seconds'], ['Distance', '50 feet', True]]},
             'q1': 'Who is faster?', 'opts1': [{'t': 'Ana', 'miss': 'Maybe! But you can’t see how far either one went. Can you be sure?'}, {'t': 'Ben', 'miss': 'Maybe! But you can’t see how far either one went. Can you be sure?'}, {'t': 'I can’t tell yet', 'ok': True}],
             'line1': 'Right: same time, but how far did each one go? Scratch to find out.',
             'q2': 'Now who is faster?',
             'opts2': [{'t': 'Ana: same time, more feet.', 'ok': True},
                       {'t': 'Ben.', 'miss': 'Both rode for 10 seconds. Who went more feet in that time?'},
                       {'t': 'They tied, because the times match.', 'miss': 'The times match, but the distances don’t. Who went farther in the same time?'}],
             'line2': 'Same time, longer distance = faster. Ana wins.'},
            {'id': 'robots', 't': 'Zippy vs Scoot: the times were on the back of the tickets!',
             'a': {'icon': '🌭', 'who': 'Zippy', 'rows': [['Distance', '90 steps'], ['Time', '90 seconds', True]]},
             'b': {'icon': '🤖', 'who': 'Scoot', 'rows': [['Distance', '60 steps'], ['Time', '30 seconds', True]]},
             'q1': 'Who is faster?', 'opts1': [{'t': 'Zippy, 90 steps!', 'miss': 'That’s the sign’s trick! Steps tell how far, not how fast.'}, {'t': 'Scoot', 'miss': 'Maybe! But you can’t see the times yet. Can you be sure?'}, {'t': 'I can’t tell yet', 'ok': True}],
             'line1': 'Right. Scratch off the times.',
             'q2': 'Both numbers are different now. What do you know for sure?',
             'opts2': [{'t': 'Zippy went farther, but it also took much longer. I need a fair way to compare.', 'ok': True},
                       {'t': 'Zippy is faster. It went more steps.', 'miss': 'More steps means farther. Zippy also took 90 seconds. Is farther the same as faster?'},
                       {'t': 'Zippy is faster. It ran for more seconds.', 'miss': 'More seconds means it took LONGER. Is that faster?'}],
             'line2': 'Hold that thought. In Part 2, you’ll slice both runs into pieces to compare them fairly.'}],
        'win': 'Speed needs both numbers: how far it went and how long it took. Clue 2!'},
    'slicer': {
        'afterText': 'Slice each run into 10-second pieces', 'kicker': 'Part 2 game', 'title': 'Slice it into seconds',
        'todo': ['Press Run for each robot. Each footprint is one step.', 'Every 10 seconds the robot stops. Press ✂ Cut (or tap the strip).', 'Then compare one piece from each robot.'],
        'why': {'icon': '✂️', 'q': 'Why cut it up?', 't': 'Zippy and Scoot went different distances in different times. Cutting both runs into pieces of the SAME time lets you compare them fairly.'},
        'every': 10, 'msPerSec': 60,
        'racers': [{'id': 'zippy', 'name': 'Zippy', 'icon': '🌭', 'steps': 90, 'secs': 90, 'c': ZP},
                   {'id': 'scoot', 'name': 'Scoot', 'icon': '🤖', 'steps': 60, 'secs': 30, 'c': SC}],
        'runBtn': '▶ Run {name}', 'cutBtn': '✂ Cut', 'autoBtn': '✂✂ Cut the rest for me', 'beepLine': '{s} seconds! Cut the strip here.',
        'stepsWord': 'steps', 'secWord': 'seconds', 'pieceTpl': '{n} steps', 'piecesLabel': 'Pieces: one for every {s} seconds',
        'needBoth': 'Now run the other robot.', 'compareLabel': 'One piece from each robot, side by side', 'compareTpl': '{n} steps in {s} seconds',
        'q1': 'Look at one piece from each robot. Who goes farther in every 10 seconds?',
        'opts1': [{'t': 'Scoot: 20 steps every 10 seconds.', 'ok': True},
                  {'t': 'Zippy: 10 steps every 10 seconds.', 'miss': 'Look at the two bars. Which piece is longer?'},
                  {'t': 'They go the same.', 'miss': 'Look at the two bars. Are they the same length?'}],
        'q': 'So who is faster?',
        'opts': [{'t': 'Scoot. In the same time, Scoot goes twice as far.', 'ok': True},
                 {'t': 'Zippy. It ran for 90 seconds, so it did more running.', 'miss': 'More seconds means it took LONGER. In the same 10 seconds, who went farther?'},
                 {'t': 'Zippy. It went 90 steps.', 'miss': 'Farther isn’t faster. Zippy needed 90 seconds for those 90 steps.'}],
        'win': 'Cut both runs into the same amount of time: Scoot covers 20 steps every 10 seconds, Zippy only 10. More seconds means slower. Clue 3!'},
    'photofinish': {
        'after': 'slicer', 'kicker': 'Wow!', 'title': 'The photo-finish camera',
        'todo': ['Press Run the race.', 'Watch the photo-finish picture build, one thin slice at a time.', 'Tap each robot’s nose in that picture to read its time.'],
        'why': {'icon': '📷', 'q': 'What is a photo finish?', 't': 'In a close race, a special camera looks only at the finish line. It takes thousands of thin slices every second and lines them up. The picture shows WHEN each racer crossed.'},
        'model': 'a model', 'runBtn': '▶ Run the race', 'againBtn': '↺ Run it again', 'sceneLabel': 'The race, seen from above', 'stripLabel': 'What the photo-finish camera makes',
        'sceneAlt': 'A model race seen from above: a blue robot and an orange robot drive toward a red finish line.',
        'stripAlt': 'The photo-finish picture the model camera builds. Left to right is time, in seconds.',
        'lanes': [{'id': 'scoot', 'name': 'Scoot', 'c': SC, 'speed': 60}, {'id': 'zippy', 'name': 'Zippy', 'c': ZP, 'speed': 30}],
        'start': 180, 'line': 300, 'len': 44, 'secs': 6, 'tol': 0.45,
        'preLine': 'The camera looks through a slit as thin as a hair, right on the red finish line.',
        'tapLine': 'Now tap each robot’s nose in the photo-finish picture: the first moment it touched the line.',
        'readTpl': '{t} seconds', 'missTap': 'Find where {name}’s shape STARTS (its left edge). That is when its nose first touched the line.',
        'slowLine': 'Zippy looks stretched out! It took twice as long to cross the line, because it was slower. Scoot looks squished because it crossed fast. In a photo finish, left to right is TIME, not distance.',
        'photoBtn': '📷 See a real photo finish',
        'photo': {'img': I('photo-finish'), 'alt': 'A real photo-finish picture of a rowing boat crossing the finish line. The water looks like long stripes and the oars look bent.',
                  'cap': 'A real photo finish from a rowing race in Germany in 2005. The camera saw only the finish line and lined up thousands of thin slices. That is why the water looks like stripes and the oars look bent: they kept moving while the camera scanned. Photo: staff of the 2005 World Rowing Junior Championships, CC BY-SA 2.5, via Wikimedia Commons.'},
        'done': 'Wow! A photo finish measures TIME with a camera. Race officials use it when a race is too close to call by watching.'},
    'rematch': {
        'afterText': 'Set the finish, run the race and record your data.', 'kicker': 'Part 3 game', 'title': 'The fair rematch',
        'todo': ['Drag the 🏁 finish flag onto the tape, or tap a mark.', 'Press Start the race. Watch both race clocks.', 'Type each robot’s distance and time into the data table.', 'Press Check. Your claim builds itself.'],
        'why': {'icon': '🎯', 'q': 'What makes it fair?', 't': 'One start line and one finish line for both robots, on the same boardwalk. The only thing that is different is the robot.'},
        'max': 40, 'marks': [20, 30, 40], 'unit': 'steps', 'model': 'a model', 'msPerSec': 90,
        'alt': 'A model race course on the boardwalk: two lanes, one start line and a tape measure marked in steps.',
        'flagLabel': '🏁 Finish flag: drag me onto the tape, or tap a mark below', 'markTpl': 'Finish at {n} steps', 'needFlag': 'Put the finish flag on the tape first.',
        'startWord': 'START', 'finishWord': 'FINISH', 'runBtn': '▶ Start the race', 'againBtn': '↺ Race again',
        'lanes': [{'id': 'scoot', 'name': 'Scoot', 'icon': '🤖', 'rate': 2, 'c': SC}, {'id': 'zippy', 'name': 'Zippy', 'icon': '🌭', 'rate': 1, 'c': ZP}],
        'tableLabel': 'My data table', 'cols': ['Object', 'Distance (steps)', 'Time (seconds)', 'Notes'], 'notesPh': 'optional',
        'checkBtn': '✓ Check my table', 'blankMiss': 'Fill in every number box.',
        'distMiss': 'Check {name}’s distance: where is the finish flag on the tape?', 'timeMiss': 'Check {name}’s time: read its race clock.',
        'claimLabel': 'Your claim, built from your table',
        'claimTpl': 'I claim that {a} is faster. My data shows {a} went {d} steps in {ta} seconds. {b} took {tb} seconds to go the same {d} steps.',
        'q': 'What made this rematch a fair test?',
        'opts': [{'t': 'Same start, same finish line, same boardwalk. Only the robot was different.', 'ok': True},
                 {'t': 'Both robots tried their best.', 'miss': 'Robots don’t try! What stayed the SAME for both of them?'},
                 {'t': 'We watched closely.', 'miss': 'Watching can fool you. What did we keep the same, and what did we measure?'}],
        'win': 'Same start, same finish, same boardwalk: only the robot changed. Scoot took half the time. Clue 4!'},
    'exploreMod': 'rematch',
    'hireform': {
        'after': '.fs-solve', 'kicker': 'Case closed · Rosa’s report', 'title': 'Rosa’s robot report',
        'todo': ['Your rematch numbers are already on the report.', 'Pick the faster robot and the best evidence.', 'Stamp it for Rosa.'], 'lockLine': 'Crack the case first.',
        'head': 'Rosa’s Robot Report', 'sub': 'Palmetto Beach boardwalk · delivery robots', 'idA': 'scoot', 'idB': 'zippy', 'defD': 40,
        'rowsTpl': [['Test', 'A fair rematch on the boardwalk'], ['Distance', '{d} steps for both robots'], ['Scoot’s time', '{ta} seconds'], ['Zippy’s time', '{tb} seconds']],
        'fasterLabel': 'Faster robot', 'evLabel': 'Best evidence',
        'fasterQ': '1. Which robot is faster?',
        'fasterOpts': [{'t': 'Scoot', 'ok': True, 'fill': 'Scoot 🤖'}, {'t': 'Zippy', 'miss': 'Read the two times. Who took less time to go the same distance?'}],
        'evQ': '2. What is the BEST evidence to show Rosa?',
        'evOpts': [{'t': 'My rematch data: same distance, and Scoot took half the time.', 'ok': True, 'fill': 'Measured data from a fair rematch'},
                   {'t': 'Zippy’s sign says FASTEST.', 'miss': 'Anyone can paint a sign. Which evidence was measured?'},
                   {'t': 'Zippy looks speedy.', 'miss': 'Looks can fool you. Which evidence was measured?'}],
        'stampBtn': '🖋️ Stamp Rosa’s report', 'stamp': 'KEEP SCOOT', 'sign': 'Rosa',
        'win': 'Rosa keeps Scoot, and she has the data to prove it.'},
    'headstart': {
        'after': '.fs-solve', 'kicker': 'Twist!', 'title': 'Zippy’s owner has a video',
        'todo': ['Press Play. Zippy’s owner says this race proves Zippy is faster.', 'Tap the part of the replay that isn’t fair.', 'Then run a fair redo.'], 'lockLine': 'Crack the case first.',
        'max': 30, 'finish': 30, 'msPerSec': 120, 'alt': 'A model replay of a two-lane robot race with a red finish line.',
        'lanes': [{'id': 'scoot', 'name': 'Scoot', 'icon': '🤖', 'rate': 2, 'start': 0}, {'id': 'zippy', 'name': 'Zippy', 'icon': '🌭', 'rate': 1, 'start': 20}],
        'recWord': 'REPLAY', 'caption': '🌭 ZIPPY WINS! (says Zippy’s owner)', 'playBtn': '▶ Play the replay',
        'spotQ': 'Something about this race isn’t fair. Tap it in the replay.',
        'spots': [{'k': 'start', 'x': 40, 'w': 570, 'y': 20, 'h': 130, 'ok': True},
                  {'k': 'finish', 'x': 812, 'w': 56, 'y': 20, 'h': 130, 'miss': 'Both robots had the same finish line. Look at where each robot STARTED.'}],
        'spotLine': 'Zippy started 20 steps closer to the finish! Scoot had to go 30 steps. Zippy only went 10.',
        'q': 'Does Zippy’s win count?',
        'opts': [{'t': 'No. They didn’t start at the same line, so it wasn’t a fair test.', 'ok': True},
                 {'t': 'Yes. Zippy crossed the finish line first.', 'miss': 'Crossing first isn’t the same as being faster. Did they both go the same distance?'}],
        'fairBtn': '▶ Run a fair redo', 'fairCap': 'FAIR REDO', 'fairCapEnd': '🤖 Scoot: 15 seconds · 🌭 Zippy: 30 seconds',
        'fairLine': 'Same start line this time: Scoot crosses in 15 seconds. Zippy needs 30. A head start can make a slower robot look faster.',
        'win': 'Twist solved! Only a fair test counts.'},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Think about the scratch-off tickets. Which two numbers did you need to call a race?', 'B': 'Think about the scratch-off tickets. Which two numbers did you need to call a race?'},
        'q2': {'B': 'Same 20 feet. Taking more seconds means taking LONGER. Is that faster?', 'C': 'You have both numbers. Same distance: who took less time?'},
        'q3': {'A': 'Think about the fair rematch. What stayed the same for both robots?', 'C': 'In the fair rematch you still measured. What stayed the same for both robots?'}},
    'flags': {
        'ans-2': [
            {'label': 'the faster car', 're': 'blue'},
            {'label': 'how you decided', 're': 'each second|every second|per second|a second|one second|1 second|divid|÷|/|five|six|5 feet|6 feet|5 ft|6 ft|same time|in 1|in one'}],
        'ans-3': [
            {'label': 'why fair matters', 're': 'same|only one|only the|honest|equal|fair|change one|one thing'},
            {'label': 'an unfair test', 're': 'head ?start|closer|different (start|ramp|surface|floor|finish|distance|line|place|spot)|push|carpet|tile|grass|shorter|longer|steeper|not the same|unfair'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|need|can.?t|cannot|isn|is not'},
            {'label': 'two pieces of evidence', 'any': ['zippy', 'scoot', 'sign', 'ticket', 'seconds', 'second', 'steps', 'clock', 'table', 'data', 'rematch', 'slice', 'piece', 'head start', 'photo finish', 'camera', 'maya', 'jordan', 'measure', 'time'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-2': 12, 'ans-3': 15, 'cer-4': 30},
    'hints': {
        'ans-2': ['Find how far each car goes in ONE second.', 'The red car: 20 feet in 4 seconds is 5 feet each second. Now do the blue car.', 'Try: The ___ car is faster because it goes ___ feet each second and the other goes ___.'],
        'ans-3': ['A fair test keeps everything the same except one thing. Which thing?', 'Think about Zippy’s owner’s video, or a race where one car starts on carpet and one on tile.', 'Try: A fair test matters because ___. An unfair test would be ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'Zippy’s sign only gave steps. Nobody could tell who was faster until we knew the seconds, too.',
                'In the fair rematch, the race clocks showed Scoot took half as long as Zippy.',
                'Cut into 10-second pieces, Scoot covered 20 steps each time and Zippy covered 10.',
                'Zippy’s owner says Zippy is the fastest.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · Zippy vs Scoot', 'length': '20–30 s'},
        'warmup': {'label': 'Warm-Up · fix the sign (Clue 1)', 'length': '15–20 s',
                   'script': 'Sam here. Zippy’s sign says fastest on the beach, ninety steps! Hmm. Drag a word magnet onto each blank, so the sign only says what the number proves. Wrong words slide right off.'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · scratch-off tickets (Clue 2)', 'length': '20–30 s'},
        'part2': {'label': 'Part 2 · slice it into seconds (Clue 3)', 'length': '15–20 s',
                  'script': 'Different distance, different time. Here’s a fair trick. Press Run. Every ten seconds the robot stops, and you press Cut. Then compare one piece from each robot, side by side.'},
        'explore': {'label': 'Part 3 · the fair rematch (Clue 4)', 'length': '15–20 s',
                    'script': 'Time for a fair rematch. Drag the finish flag onto the tape, or tap a mark. Press Start the race and watch both race clocks. Then type your numbers into the data table.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · my speed data table', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '15–20 s',
                     'script': 'A classmate says you can tell who’s fastest just by watching. True? Think about Zippy’s sign, and the race clocks. Pick your side, tap two facts, then explain. That’s your C-E-R.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 26.01 (waves).'},
    },
    'videoOff': [],
    'lensVoice': False,
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Zippy’s fixed sign (Warm-Up)',
        'A scratched-off ticket (The Lesson)',
        'One piece from each robot, side by side (The Lesson)',
        'Your rematch data table (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['Two toy cars on a ramp', 'A ball and a marble', 'Zippy and Scoot'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · draw and label your data table', 'required': True, 'minLabels': 4,
                           'prompts': ['Draw a table with 4 columns', 'Label them OBJECT, DISTANCE, TIME and NOTES', 'Fill in one row for each thing you raced', 'Circle the fastest one']}]},
    'hlCoach': copy.deepcopy(O['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🪧', 'name': 'Zippy’s sign',
                 'line': 'You cracked Case 25, part 2, and Zippy’s fixed sign goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next time: waves!'},
    'notebookTitle': O['notebookTitle'],
    'notebook': copy.deepcopy(O['notebook']) + [{'lesson': '25.02', 'icon': '🪧', 'name': 'Zippy’s sign'}],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You’re up to speed!',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to see what it means.']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '#tab-vocab p', 'text': 'How could you tell who was faster?'},
         'label': 'Warm-Up: races I have seen', 'q': 'Warm-Up: Something fast, something slow, and how I could tell which is faster.', 'title': 'Races I have seen', 'compact': True,
         'fields': [{'t': 'Something fast I have seen', 'icon': '🐆', 'ph': 'A ___ is fast.'},
                    {'t': 'Something slow I have seen', 'icon': '🐢', 'ph': 'A ___ is slow.'},
                    {'t': 'How I could tell which is faster', 'icon': '⏱️', 'ph': 'I could measure ___ and ___.'}]},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Draw your data table and write your claim.'},
         'label': 'Part C: My speed data table', 'q': 'Part C: My speed data table (what I raced, my claim and my evidence)', 'title': 'My speed data table',
         'fields': [{'t': 'What I raced', 'icon': '🚗', 'ph': 'I raced a ___ and a ___.'},
                    {'t': 'My claim', 'icon': '🏁', 'ph': 'I claim that ___ was the fastest.'},
                    {'t': 'My evidence (numbers from my table)', 'icon': '📋', 'ph': 'My data shows ___ went ___ in ___ seconds. ___ took ___ seconds.', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Can you tell who is fastest just by watching?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-2': 'Part B · Question 6', 'ans-3': 'Part B · Question 7', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'Speed needs two numbers: how far something went and how long it took.',
    'key': ['speed', 'two', 'far', 'long'],
    'small': ['needs', 'something', 'went', 'and', 'it'],
    'model': 'A scientist might highlight “speed”, “far” and “long”. Those words hold the big idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me tell how far, how long or who was faster?']

EV = '#tab-assignment .act-body > div:has(> .fs-plan)'
D['cues'] = {
    'warmup': [{'at': '^sign', 'sel': '.fs-sbd-sign', 'fx': 'glow', 'scroll': True},
               {'at': '^magnet', 'sel': '.fs-fxs-tray', 'fx': 'pop', 'scroll': True},
               {'at': '^blank', 'sel': '.fs-fxs-slot', 'all': True, 'fx': 'glow'},
               {'at': '^proves', 'sel': '.fs-fxs-head', 'fx': 'pop'},
               {'at': '^slide', 'sel': '[data-mod="fixsign"] .fs-todo li', 'i': 2, 'fx': 'trace'}],
    'part2': [{'at': '^trick', 'sel': '[data-mod="slicer"] .fs-why', 'fx': 'glow', 'scroll': True},
              {'at': '^run', 'sel': '.fs-slc-run', 'fx': 'point'},
              {'at': '^cut', 'sel': '[data-mod="slicer"] .fs-todo li', 'i': 1, 'fx': 'trace'},
              {'at': '^compare', 'sel': '[data-mod="slicer"] .fs-todo li', 'i': 2, 'fx': 'trace'}],
    'explore': [{'at': '^flag', 'sel': '.fs-rm-flag', 'fx': 'point', 'scroll': True},
                {'at': '^mark', 'sel': '.fs-rm-mk', 'all': True, 'fx': 'pop'},
                {'at': '^start', 'sel': '.fs-rm-run', 'fx': 'point'},
                {'at': '^clocks', 'sel': '.fs-rm-clk', 'all': True, 'fx': 'glow'},
                {'at': '^table', 'sel': '[data-mod="rematch"] .fs-todo li', 'i': 2, 'fx': 'trace'}],
    'evidence': [{'at': '^classmate', 'sel': EV + ' > p', 'i': 0, 'fx': 'trace', 'scroll': True},
                 {'at': '^sign', 'sel': '.fs-plan .fs-opt', 'i': 2, 'fx': 'glow'},
                 {'at': '^clocks', 'sel': '.fs-plan .fs-opt', 'i': 3, 'fx': 'glow'},
                 {'at': '^side', 'sel': '.fs-plan .fs-plan-row', 'i': 0, 'fx': 'pop'},
                 {'at': '^explain', 'sel': '.fs-cer .fs-cer-row', 'i': 2, 'fx': 'glow', 'scroll': True}],
}
D['cueWords'] = json.load(open('cuewords.json', encoding='utf-8')) if os.path.exists('cuewords.json') else {}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
# budget counter (oao-audio-budget): G4 science = 1,400 credits per lesson; scripts are written to 95% (1,330). Nothing is generated in week 25.
clips = {k: v['script'] for k, v in D['slots'].items() if v.get('script')}
tot = sum(len(t) for t in clips.values())
for k, t in clips.items(): print(f'  {k:10} {len(t):4}')
print(f'this page: {tot} / 1400 credits ({tot/1400:.0%}), scripts only, 0 generated')
assert tot <= 1330
json.dump(clips, open('clip-scripts.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
