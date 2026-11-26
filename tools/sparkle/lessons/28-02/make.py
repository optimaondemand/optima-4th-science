#!/usr/bin/env python3
"""Writes data.json and fixes.json for 28.02 (run from this folder). Case 28 part 2 "Proof for the Steel Bin" (Dr. Priya Nair, Unit 6, Palmetto Springs):
the cleanup haul goes to the recycling center. Dana's steel bin only takes items that passed a fair test, with the data table as proof.
New (Bethany's brainstorm, 26 Nov 2026): case.intake (the intake slip), spotdiff (Warm-Up: two volunteers' notes), suredial (Part 1: predict + how sure; a sure
wrong guess earns a gold star), notes2table (Part 2: messy sticky notes into a data table; the stainless spoon wow), ruler (Part 4 = the old Explore: lock the fair
test, slide each item along a ruler until it jumps), bulletin reused as Dana's voicemail (skin phone; browser voice until a clip exists), photos after the solve
(the 1940s scrapyard lifting magnet), SIMS.fieldviewer reused with a NEW plate option (steel vs aluminum plate). SCRIPTS ONLY: nothing generated."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
O = json.load(open('../27-01/data.json', encoding='utf-8'))
Q = json.load(open('../28-01/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

# ---------------------------------------------------------------- labels (standing approval + ticked)
fx('fix', 'unit label (ticked): “Ecosystems & Energy” is a leftover; Module 28 is in Unit 6 “Matter, Magnets, and Changes”', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Matter, Magnets &amp; Changes</div>')
fx('fix', 'science label (ticked): magnets are physical science, not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standards label: the plan’s CPALMS codes; TEKS is a Texas code that isn’t in the plan', '<div class="info-value">SC.4.N.1.1, SC.4.P.8.4 · TEKS 4.7(C), 4.2(A)</div>', '<div class="info-value">SC.4.N.1.1, SC.4.P.8.4</div>')
fx('fix', 'quarter label in the footer (ticked): 28.02 is due Apr 22, Q4 (the header already says Q4)', 'Science &middot; Quarter 3 &middot; Student Lesson Page', 'Science &middot; Quarter 4 &middot; Student Lesson Page')
fx('fix', '6 vs 8 materials (ticked): the test has 8 materials; no dashes', r"<p>Hold this question in your head as you work\. By the end of the lesson.*?</p>",
   "<p>Keep this question in mind. By the end, you’ll have run a fair test on 8 materials, recorded the data in a table and used it as evidence.</p>", True)

# ---------------------------------------------------------------- ticked: energy-lesson leftovers
fx('fix', '22.01 leftover: the Warm-Up title named the toaster lesson', '<div class="act-title">🌅 Warm-Up: What Goes In, What Comes Out?</div>\n        <div class="act-subtitle">A familiar device, a hidden change</div>',
   '<div class="act-title">🌅 Warm-Up: Two Volunteers, Two Answers</div>\n        <div class="act-subtitle">Same bottle cap, opposite results</div>')
fx('fix', '22.01 leftover: the toaster warm-up → two volunteers’ test notes',
   '<p>Think about a toaster. You drop in cold bread. A minute later, you pull out hot toast.</p>',
   '<p>Two cleanup volunteers, Kai and Mo, tested the same bottle cap from the pond haul. They wrote down opposite results!</p>')
fx('fix', '22.01 leftover: the toaster sketch → spot the differences (played and answered on the page)',
   "<p>In your notebook, draw a quick sketch of a toaster. On one side, label what goes IN. On the other, label what comes OUT. (Hint: bread on both sides — but something invisible is also going in. What is it?)</p>",
   '<p>Find what they did differently. Then decide whose result to trust.</p>')
fx('fix', '22.01 leftover: Notice & Wonder about the toaster',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Notice &amp; Wonder</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover: “energy can CONVERT … toasters” callout',
   r'<div class="callout callout-tip">\s*<span class="callout-icon">💡</span>\s*<p>Today you\'ll learn that energy can CONVERT.*?</p>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover (ticked): “Device” meant converting energy',
   'A tool or machine designed to do a job. Most devices convert energy from one form to another — a flashlight, a toaster, a fan are all devices.',
   'A tool or machine made to do a job, like a magnet or a recycling sorter.')
fx('fix', '22.01 leftover (ticked): the Stop & Reason asked about “the three devices above … INPUT and OUTPUT”',
   r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', '9.01 leftover (ticked): Part C was a food chain; the checklist already describes a 6-item magnet test', '🎨 Part C &mdash; Build Your Own Food Chain', '🎨 Part C &mdash; Run Your Own Magnet Test')
fx('fix', '9.01 leftover (ticked): Part C task → the checklist’s 6-item magnet test (planned on the page, sorted in a required sketch)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Pick 6 small things at home (ask first!). Predict each one, test it with a magnet the same fair way, and write what happened. Then sort them into two circles and finish the sentence about your pattern.</p>', True)
fx('fix', '9.01 leftover (ticked): Reflect asked about a hawk; the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'supply list: what Part C needs', r'<span class="need-chip"><span>✏️</span>Colored pencils</span>',
   '<span class="need-chip"><span>🧲</span>A fridge magnet</span><span class="need-chip"><span>📏</span>Optional: a ruler</span>', True)

# ---------------------------------------------------------------- Part 1 and Part 2 (plain; games carry the misconception and the old diagram)
fx('plain', 'Part 1: no dashes', 'Based on what you already know — magnets attract iron, nickel, and steel — you can usually guess',
   'Based on what you already know (magnets attract iron, nickel and steel), you can usually guess')
fx('plain', 'Part 1: shorter; a lead-in for the how-sure dial',
   "<p>Predicting before testing has two big benefits: (1) it shows what you ALREADY know; (2) when your prediction is WRONG, that's where you learn the most. A wrong prediction is a clue that there's something interesting about the material you didn't know.</p>",
   "<p>Predicting first shows what you ALREADY know. And when a prediction is WRONG, that’s where you learn the most. Try it: predict, say how sure you are, then test.</p>")
fx('cut', 'lean: the Stop & Think (penny) is played by the how-sure dial and Part B question 6',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('plain', 'Part 2: a lead-in for the notes game; no dash', 'Then look for patterns: what do all the magnetic items have in common?</p>',
   'Then look for patterns: what do all the magnetic items have in common?</p>\n      <p>Mo didn’t use a table. Mo used sticky notes. Help turn them into a real data table.</p>')
fx('cut', 'lean: the misconception (“a wrong prediction = failure”) is played by the how-sure dial’s gold stars',
   r'\s*<p><strong>Common misconception:</strong> Some people think the prediction has to be CORRECT.*?</p>', '', True)
fx('plain', 'figure caption: no dash', 'Group the magnetic items together — and look for what they have in common.', 'Group the magnetic items together, and look for what they have in common.')
fx('plain', 'figure: drop the image-suggestion fallback (the image exists)', r'\s*onerror="this\.style\.display=\'none\';[^"]*"\s*/>\s*<div class="image-suggestion".*?</div>\s*</div>', ' />', True)
fx('cut', 'lean: Key Concept (Part 3 says it)',
   r'<div style="background:#FFF6E5;border:2\.5px solid #F0C97A;[^>]*>\s*<div[^>]*>⭐ Key Concept</div>.*?</p>\s*</div>\s*', '', True)
fx('cut', 'lean: the Four Test Results tap diagram is played by the how-sure dial; with it go Observe & Reason, the sea-turtle Amazing Fact, the lighthouse-compass Florida connection and the controls Go Deeper. Part 3 (fair tests) is added in their place so the parts run 1–4',
   r'<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">Four Test Results</h3>.*?(?=<div class="tab-next-wrap">)',
   H3 + 'Part 3 · Make It a Fair Test</h3>\n      <p>A fair test changes only ONE thing. Everything else stays the same: the same magnet, the same distance, the same way of moving it. Then, if the results are different, you know why: it was the material.</p>\n\n      ', True)

# ---------------------------------------------------------------- Word Wall: no dashes (same meanings)
fx('plain', 'Word Wall: no dash', 'A reasonable guess about what will happen — made BEFORE the test, based on what you already know.', 'A reasonable guess about what will happen, made BEFORE the test and based on what you already know.')
fx('plain', 'cut filler; no dash', r"<p>These six words show up all through the lesson\. <strong>Tap a card to flip it</strong>.*?</p>",
   "<p><strong>Tap a card to flip it</strong> and read what the word means.</p>", True)

# ---------------------------------------------------------------- Part 4 = the old Explore
fx('cut', 'Part 4 = the old Explore (the 8-material test → slide to the jump, a fair test with a data table); the next button goes to Self-Check',
   '''<div class="tab-next-wrap">
        <button class="tab-next-btn" onclick="switchTab('explore')">Continue to 🔬 Explore →</button>''',
   H3 + 'Part 4 · The 8-Material Fair Test</h3>\n      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">Now run a real fair test. Lock the settings first. Then slide each item toward the magnet along a ruler, and record where it jumps.</p>\n  <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>')
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its predict-test-sort steps live on as the ruler test and Part C; the scrapyard Amazing Fact becomes the real photo after the solve; the stainless knife Think like a scientist is the spoon wow; the repeated-trials Go Deeper goes)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)

# ---------------------------------------------------------------- Assignment
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('plain', 'Part B question 5 no longer points at the cut diagram', '<span class="pq-text">Pick ONE test result from the diagram.', '<span class="pq-text">Pick ONE thing you tested today.')
fx('plain', 'Part B question 5: it is the student who tested', 'and what the scientist LEARNED.', 'and what you LEARNED.')
fx('plain', 'Part B question 5 label (Gathered Answers)', 'data-label="Pick ONE test result from the diagram. Name the pr..."', 'data-label="One test: prediction, result, what I learned"')
fx('plain', 'Part B question 6 label (Gathered Answers)', 'data-label="You predict a copper penny will be magnetic. Your ..."', 'data-label="The penny: what the data tells me"')
fx('cut', 'lean: Part B question 7 removed (Bethany kept 5 and 6; the CER argues the same “write it down” idea)', r'<div class="pq">\s*<span class="pq-num"[^>]*>7</span>.*?</textarea>\s*', '', True)
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'no dash', '<em>"You don\'t need to write down test results — just remember them."</em>', '<em>"You don\'t need to write down test results. Just remember them."</em>')
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C checklist ends with the required sketch', 'A real 6-item magnet investigation with predictions, results, notes, and a one-sentence sort with the pattern.',
   'My 6 items, predictions, results and my pattern sentence. Plus your labeled sketch of the two circles.')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether scientists need data tables, supported with two pieces of evidence.',
   '<strong>Use Your Evidence:</strong> My claim about whether scientists need to write results down, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a 9.01 leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Download your field journal (it has your answers and your sketch) and upload it to the Canvas assignment. Or copy your Gathered Answers (above) into Canvas.', True)
fx('plain', 'closing: no dashes; names next week', "You've now done what real investigators do — made a", "You’ve now done what real investigators do. You made a")
fx('plain', 'closing: next week', 'Next module brings physical and chemical changes — what happens when matter transforms.', 'Next week: mystery materials, and what happens when matter changes.')

# ---------------------------------------------------------------- the story
PRIYA = O['crew']['priya']
HAUL = [('caps', '🍾', 'Bottle caps (a bag of 12)'), ('beans', '🥫', 'Bean can (a “tin” can)'), ('soda', '🥤', 'Soda can'), ('wrench', '🔧', 'Wrench'),
        ('spoon', '🥄', 'Spoon stamped “stainless steel”'), ('fork', '🍴', 'Picnic fork'), ('wire', '➰', 'Copper wire'), ('tag', '🏷️', 'Race number tag')]
D = {
    'lesson': '28.02', 'week': 28, 'day': 2, 'guide': 'priya', 'prefix': 'g4sci-28-2', 'manifestKey': '28-02',
    'paths': P['paths'], 'crew': {'priya': PRIYA},
    'expedition': {'num': 28, 'title': 'Proof for the Steel Bin'},
    'ambient': {'icon': '♻️', 'label': 'The recycling center'},
    'case': {
        'num': 28, 'title': 'Proof for the Steel Bin', 'style': 'order',
        'hook': 'Dr. Priya Nair here. The pond is clean, and the haul is at the recycling center! But Dana won’t fill the steel bin until we prove which things are magnetic steel. Listen to her voicemail below.',
        'intake': {'head': 'PALMETTO SPRINGS RECYCLING CENTER', 'title': 'Intake slip · pond cleanup haul', 'cols': ['Item from the haul', 'Steel bin?'],
                   'rows': [[r[1], r[2]] for r in HAUL], 'blank': '?', 'proofLine': 'Proof attached (fair test + data table)', 'sign': 'Dana, intake desk'},
        'stills': [],
        'question': 'Which haul items go in the steel bin, and what proof should we send Dana?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'spotdiff', 'icon': '🔍', 'where': 'Warm-Up: two volunteers, two answers', 't': 'A fair test keeps the magnet, the distance and the wait the same. Kai and Mo changed three things, so their results disagreed.'},
            {'id': 'suredial', 'icon': '🎯', 'where': 'The Lesson, Part 1: the how-sure dial', 't': 'Names can fool you. A “tin” can is really steel, and it stuck. Test it; don’t guess.'},
            {'id': 'notes2table', 'icon': '📋', 'where': 'The Lesson, Part 2: messy notes to a data table', 't': 'The data table proved it: the steel fork stuck, but the stainless steel spoon did not.'},
            {'id': 'ruler', 'icon': '📏', 'where': 'The Lesson, Part 4: the fair test', 't': 'In the fair test, only iron and steel things jumped to the magnet. No jump means not magnetic.'},
        ],
        'solve': {
            'title': 'What goes in the steel bin?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Everything with “steel” or “tin” in its name: the caps, the bean can, the wrench, the fork and the stainless spoon. Send a photo of the bin.', 'why': 'Check Clue 3. The stainless steel spoon didn’t stick. And a photo isn’t a fair test or a data table.'},
                {'t': 'Only the shiny things: the caps, the soda can, the spoon and the tag. Shiny is proof enough.', 'why': 'Check Clue 2. Looks and names can fool you. The soda can and the tag are aluminum.'},
                {'t': 'The caps, the bean can, the wrench and the fork, because they stuck in a fair test. Send the data table as proof.', 'right': True,
                 'why': 'Case cracked! Four items passed the fair test, and the data table is the proof Dana asked for.'},
                {'t': 'Whatever Kai remembers sticking. No need to write anything down.', 'why': 'Check Clue 1. Kai and Mo remembered opposite results for the same bottle cap.'},
            ]},
    },
    'bulletin': {
        'afterSel': '.fs-casecard', 'kicker': 'New voicemail', 'title': 'Dana from the recycling center', 'skin': 'phone', 'tone': 'ring',
        'todo': ['Press Play and listen. You can read along.', 'Tap the 3 things Dana needs from us.'],
        'device': 'Voicemail', 'deviceSub': 'Dana · 0:18', 'station': '1 new message from Dana', 'playBtn': 'Play the voicemail', 'againBtn': 'Play it again',
        'audio': 'voicemail', 'paperHead': 'VOICEMAIL · DANA, RECYCLING CENTER',
        'lines': ['Hi, this is Dana at the Palmetto Springs Recycling Center. Thanks for the cleanup haul!',
                  'But I can’t put anything in the steel bin [[x:That’s why she called. Now listen for what she NEEDS from you.|just because it looks like steel]].',
                  'Please [[fair|run a fair test: the same magnet and the same distance, every time]].',
                  '[[table|Write every result in a data table]].',
                  'Then [[proof|send me the table as your proof]], and I’ll fill the bin. Bye!'],
        'foundLabel': 'What Dana needs', 'dangerWord': 'Need', 'countIcon': '📎', 'countWord': 'needs found',
        'dangers': [{'id': 'fair', 'icon': '⚖️', 't': 'A fair test', 'does': 'same magnet, same distance'}, {'id': 'table', 'icon': '📋', 't': 'A data table', 'does': 'every result written down'},
                    {'id': 'proof', 'icon': '📎', 't': 'Send the proof', 'does': 'the table goes to Dana'}],
        'win': 'A fair test, a data table, and the proof. Now find out which items pass!'},
    'spotdiff': {
        'afterText': 'Then decide whose result to trust.', 'kicker': 'Warm-Up game', 'title': 'Spot the differences',
        'why': {'icon': '🔍', 'q': 'Why compare their notes?', 't': 'When two tests of the same thing disagree, something about HOW they tested was different. Find it.'},
        'todo': ['Read Kai’s page and Mo’s page.', 'Tap each place where they tested differently.', 'Then decide whose result to trust.'],
        'pages': [
            {'who': 'Kai’s test notes', 'lines': ['[[x:Both pages tested the same bottle cap. Look for HOW they tested.|Bottle cap from the pond.]]', 'Used [[magnet|the big horseshoe magnet]].',
                                                  'Held it [[dist|1 cm away]].', '[[time|Counted to 3]] while I waited.', 'RESULT: it jumped! Magnetic.']},
            {'who': 'Mo’s test notes', 'lines': ['[[x:Both pages tested the same bottle cap. Look for HOW they tested.|Bottle cap from the pond.]]', 'Used [[magnet|my old, flat fridge magnet]].',
                                                 'Held it [[dist|8 cm away]].', '[[time|Waited 1 second]].', 'RESULT: nothing. Not magnetic.']}],
        'diffs': [{'id': 'magnet', 'icon': '🧲', 't': 'Different magnets'}, {'id': 'dist', 'icon': '📏', 't': 'Different distances'}, {'id': 'time', 'icon': '⏱️', 't': 'Different wait times'}],
        'foundLabel': 'Differences you found', 'countWord': 'differences found',
        'q': 'Kai and Mo got opposite results. Whose result should Ranger Bell trust?',
        'opts': [{'t': 'Neither yet. Test again with the same magnet, the same distance and the same wait.', 'ok': True},
                 {'t': 'Kai’s, because it stuck.', 'miss': 'Maybe! But Kai and Mo changed three things. Until the test is fair, you can’t be sure.'},
                 {'t': 'Mo’s, because nothing happened.', 'miss': '8 cm is far, and a weak magnet might not reach. That test isn’t fair either.'}],
        'win': 'Change only ONE thing, or results can’t be compared. Clue 1!', 'clue': 'spotdiff'},
    'suredial': {
        'afterText': 'Try it: predict, say how sure you are, then test.', 'kicker': 'Part 1 game', 'title': 'The how-sure dial',
        'why': {'icon': '🎯', 'q': 'Why say how sure you are?', 't': 'Scientists love the surprises. A prediction you were SURE about that turns out wrong teaches you the most.'},
        'todo': ['Pick a thing. Predict: will it stick?', 'Turn the dial: how sure are you?', 'Press Test it. A sure prediction that was wrong earns a gold star!'],
        'items': [
            {'id': 'can', 'icon': '🥫', 't': 'A “tin” can of beans', 'mag': True, 'line': 'It stuck! A “tin” can is really steel with a very thin coat of tin.'},
            {'id': 'staple', 'icon': '📌', 't': 'A staple', 'mag': True, 'line': 'Staples are thin steel wire. Snap!'},
            {'id': 'foil', 'icon': '🥧', 't': 'A foil pie tray', 'mag': False, 'line': 'No pull. The tray is aluminum.'},
            {'id': 'cap', 'icon': '🧴', 't': 'A plastic bottle cap', 'mag': False, 'line': 'No pull. Plastic isn’t magnetic.'}],
        'predQ': 'Your prediction:', 'yes': '🧲 It will stick', 'no': '💨 It won’t stick', 'sureQ': 'How sure are you?', 'sure': ['A little sure', 'Pretty sure', 'Super sure'],
        'testBtn': '🧲 Test it', 'rightLine': 'You called it!', 'goldLine': 'Big learning! You were sure, and you were wrong. Now you know something new.', 'wrongLine': 'Surprise! That’s new learning.',
        'yesShort': 'I said: sticks', 'noShort': 'I said: no', 'okShort': 'right', 'goldShort': 'Big learning!', 'newShort': 'something new', 'countWord': 'tested', 'starsWord': 'gold stars',
        'q': 'Lots of scientists predict the “tin” can won’t stick, and they’re wrong. What does a wrong prediction mean?',
        'opts': [{'t': 'You found something new to learn. That’s how science works.', 'ok': True},
                 {'t': 'You failed the test.', 'miss': 'Look at the gold stars. A wrong prediction isn’t a failure. It’s a discovery.'},
                 {'t': 'The magnet must be broken.', 'miss': 'The same magnet worked on the staple. Test results don’t lie.'}],
        'win': 'Wrong predictions are gold. Names can fool you, so test! Clue 2!', 'clue': 'suredial'},
    'notes2table': {
        'afterText': 'Help turn them into a real data table.', 'kicker': 'Part 2 game', 'title': 'Messy notes to a data table',
        'why': {'icon': '📋', 'q': 'What’s wrong with sticky notes?', 't': 'They get lost, and they don’t say which thing they mean. A data table puts every result in its own row.'},
        'todo': ['Read a sticky note. Which thing is it about?', 'Drag it onto that row (or tap the note, then the row).', 'Fill all 8 rows. Watch the spoon!'],
        'notesLabel': 'Mo’s sticky notes', 'tableLabel': 'Mo’s data table', 'cols': ['Material', 'Result', 'Notes'],
        'rows': [
            {'id': 'fork', 'icon': '🍴', 't': 'Picnic fork', 'note': 'From the picnic basket. Has 4 points. SNAP! It stuck.', 'short': 'steel; stuck fast', 'mag': True, 'miss': 'Which thing has 4 points?'},
            {'id': 'spoon', 'icon': '🥄', 't': 'Spoon', 'note': 'Also from the picnic basket. Shiny. “STAINLESS STEEL” stamped on it. Nothing?!', 'short': 'stainless steel; NO pull!', 'mag': False, 'wow': True, 'miss': 'Which picnic thing is stamped “stainless steel”?'},
            {'id': 'beans', 'icon': '🥫', 't': 'Bean can', 'note': 'Label says beans. Everybody calls it a tin can. It stuck!', 'short': '“tin” can is steel', 'mag': True, 'miss': 'Which thing has a beans label?'},
            {'id': 'wrench', 'icon': '🔧', 't': 'Wrench', 'note': 'From the tackle box. Heavy tool. Stuck hard.', 'short': 'steel tool', 'mag': True, 'miss': 'Which heavy tool came from the tackle box?'},
            {'id': 'wire', 'icon': '➰', 't': 'Copper wire', 'note': 'Orange-brown and bendy. Nothing.', 'short': 'copper', 'mag': False, 'miss': 'Which thing is orange-brown and bendy?'},
            {'id': 'tag', 'icon': '🏷️', 't': 'Race number tag', 'note': 'Number 14 from the duck race. Light and silver. Nothing.', 'short': 'aluminum', 'mag': False, 'miss': 'Which thing has a race number on it?'},
            {'id': 'caps', 'icon': '🍾', 't': 'Bottle cap', 'note': 'Off a root beer bottle. Crimped edges. Stuck!', 'short': 'thin steel', 'mag': True, 'miss': 'Which thing came off a root beer bottle?'},
            {'id': 'duck', 'icon': '🦆', 't': 'Rubber duck', 'note': 'Yellow. Squeaks. Floats. Nothing.', 'short': 'rubber', 'mag': False, 'miss': 'Which thing squeaks and floats?'}],
        'stuck': '🧲 Stuck', 'nope': '💨 Nothing', 'countWord': 'notes in the table', 'emptyLine': 'Every note is in the table.',
        'wowCard': {'icon': '🤯', 't': 'Wow! The spoon is stainless STEEL, and it didn’t stick. Some stainless steel has so much nickel and chromium mixed in that a magnet hardly pulls it. Only a test can tell you, and only a table keeps the proof.'},
        'q': 'Dana says, “It’s steel, so it goes in the steel bin.” Which row of the table proves her wrong?',
        'opts': [{'t': 'The spoon row: stainless steel, and no pull.', 'ok': True},
                 {'t': 'The fork row.', 'miss': 'The fork stuck. That row agrees with Dana. Which steel thing did NOT stick?'},
                 {'t': 'The rubber duck row.', 'miss': 'Nobody thinks the duck is steel. Look for a “steel” thing that didn’t stick.'}],
        'win': 'The table caught it: not every steel sticks. Clue 3!', 'clue': 'notes2table'},
    'ruler': {
        'afterText': 'and record where it jumps.', 'kicker': 'Part 4 game', 'title': 'Slide to the jump',
        'why': {'icon': '📏', 'q': 'What is a jump distance?', 't': 'Slide something toward a strong magnet. If it’s magnetic, at some point it leaps across the gap. How far away that happens is its jump distance.'},
        'todo': ['Lock the two fair-test settings.', 'Pick an item. Hold the slide button, or drag the item along the ruler toward the magnet.', 'Watch for a jump. Test all 8.'],
        'model': 'A model test with one strong magnet.',
        'settings': [
            {'id': 'mag', 'q': 'Which magnet?', 'opts': [{'t': 'The same magnet for every item', 'ok': True}, {'t': 'Whichever magnet is closest', 'why': 'A strong magnet and a weak one give different results. Then you can’t compare the materials.'}]},
            {'id': 'start', 'q': 'Where does each item start?', 'opts': [{'t': 'At the 10 cm mark, every time', 'ok': True}, {'t': 'Anywhere I like', 'why': 'Start closer, and it jumps sooner. Same start, every time.'}]}],
        'lockLine': 'First, lock the fair-test settings:', 'lockedLine': 'Fair test locked: the same magnet, and every item starts at the 10 cm mark.',
        'items': [
            {'id': 'clip', 'icon': '📎', 't': 'Paperclip', 'jump': 3, 'line': 'Steel. It leaped across a 3 cm gap.'},
            {'id': 'button', 'icon': '🔘', 't': 'Plastic button', 'jump': 0, 'line': 'Plastic. It touched the magnet and just sat there.'},
            {'id': 'nail', 'icon': '🔩', 't': 'Iron nail', 'jump': 4, 'line': 'Iron. It jumped from 4 cm away.'},
            {'id': 'foil', 'icon': '✨', 't': 'Foil ball', 'jump': 0, 'line': 'Aluminum. No pull, even touching.'},
            {'id': 'pin', 'icon': '🧷', 't': 'Safety pin', 'jump': 2, 'line': 'Steel. It jumped at 2 cm.'},
            {'id': 'spoon', 'icon': '🥄', 't': 'Stainless spoon', 'jump': 0, 'line': 'The stainless spoon again: no jump. The table agrees with Mo’s note.'},
            {'id': 'washer', 'icon': '⚙️', 't': 'Steel washer', 'jump': 2.5, 'line': 'Steel. It jumped at 2.5 cm.'},
            {'id': 'penny', 'icon': '🪙', 't': 'Penny', 'jump': 0, 'line': 'Zinc and copper. No jump.'}],
        'startCm': 10, 'slideBtn': '◀ Hold to slide it closer', 'dragTip': 'Or drag the item along the ruler toward the magnet.',
        'jumpWord': 'It jumped at {x} cm!', 'noneWord': 'It touched the magnet. No pull at all.',
        'tableLabel': 'My data table', 'cols': ['Material', 'Jumped at', 'Magnetic?'], 'yes': 'Yes', 'no': 'No', 'noJump': 'no jump', 'countWord': 'tested',
        'q': 'Why did every item use the same magnet and start at the 10 cm mark?',
        'opts': [{'t': 'So the only thing that changed was the material. That’s a fair test.', 'ok': True},
                 {'t': 'To make the test go faster.', 'miss': 'Speed isn’t the reason. Think about Kai and Mo: what went wrong when they changed things?'},
                 {'t': 'Magnets only work at 10 cm.', 'miss': 'The nail jumped at 4 cm and the pin at 2 cm. Magnets work at many distances.'}],
        'win': 'Same magnet, same start: only the material changed. Iron and steel jumped. Clue 4!', 'clue': 'ruler'},
    'exploreMod': 'ruler',
    'photos': [
        {'id': 'scrap', 'afterSolve': True, 'lockLine': 'Crack the case first.', 'kicker': 'Case closed · one more wow', 'short': 'A real lifting magnet',
         'title': 'A magnet as big as a table', 'todo': ['Tap each number on the photo.', 'Then match each job to its number.'],
         'why': {'icon': '🏗️', 'q': 'What are we looking at?', 't': 'A real photo from about 80 years ago, at a steel mill in Pennsylvania. A giant magnet on a crane lifts scrap steel so it can be melted into new steel.'},
         'img': 'images/28-02-scrap-magnet.jpg', 'alt': 'A huge round magnet hangs from a chain under an overhead crane, above big piles of scrap metal in a steel mill yard. Blue sky and clouds behind.',
         'credit': 'Alfred T. Palmer, Office of War Information, Library of Congress (fsac.1a35061)', 'license': 'public domain, via Wikimedia Commons',
         'hotspots': [
             {'n': 1, 'x': 48, 'y': 57, 'label': 'The lifting magnet', 't': 'A giant electromagnet: a magnet that works only when electricity flows. Switch it on to grab steel, switch it off to drop it.'},
             {'n': 2, 'x': 26, 'y': 22, 'label': 'The overhead crane', 't': 'The crane rolls along its rails to carry the magnet over the piles.'},
             {'n': 3, 'x': 73, 'y': 36, 'label': 'The operator’s cab', 't': 'A worker sits in this little room and drives the crane and the magnet.'},
             {'n': 4, 'x': 60, 'y': 64, 'label': 'Scrap steel', 't': 'Old steel waiting to be melted. The magnet picks up only the magnetic metal.'}],
         'task': {'q': 'Match it: which number does each job?',
                  'items': [
                      {'icon': '🧲', 'step': 'Grabs steel when the power is on', 'ans': 1, 'evid': 'The electromagnet grabs steel when electricity flows.', 'miss': 'Look for the round thing on the chain.'},
                      {'icon': '👷', 'step': 'Where a worker drives the crane', 'ans': 3, 'evid': 'The operator works from the cab.', 'miss': 'Look for the little room up high on the right.'},
                      {'icon': '♻️', 'step': 'Old steel waiting to become new steel', 'ans': 4, 'evid': 'Scrap steel gets melted and used again.', 'miss': 'Look for the big piles.'}],
                  'win': 'A recycling center sorts steel the same way you did: with a magnet. Just a much bigger one!'}}],
    'tool': copy.deepcopy(Q['tool']),
    'quizKicker': '',
    'quizMiss': {
        'q1': {'B': 'Looking smart isn’t the goal. Remember the gold stars for wrong predictions?', 'C': 'A prediction is about THIS test: compare what you expected with what happened.'},
        'q2': {'A': 'The magnet lifted a tiny staple AND a heavy wrench. Size isn’t it.', 'B': 'The penny isn’t broken. What is it made of?'},
        'q3': {'A': 'A table can’t change the magnet. Did Mo’s table change any results?', 'C': 'A good table KEEPS the wrong predictions. They’re where the learning is!'}},
    'flags': {
        'ans-1': [
            {'label': 'the thing you tested', 're': 'can|staple|tray|foil|cap|fork|spoon|wrench|wire|tag|duck|clip|button|nail|pin|washer|penny'},
            {'label': 'your prediction', 're': 'predict|guess|thought|think|said|expect'},
            {'label': 'the result', 're': 'stuck|stick|jump|pull|attract|nothing|no pull|didn.?t|did not|result'},
            {'label': 'what you learned', 're': 'learn|now i know|found out|shows|means|because|so |realiz|surpris'}],
        'ans-2': [
            {'label': 'not magnetic', 're': 'not magnetic|nonmagnetic|non-magnetic|isn.?t magnetic|not attract|doesn.?t|no attraction|ignore'},
            {'label': 'the new understanding', 're': 'not all metal|some metal|copper|zinc|kind of metal|only iron|iron|steel|nickel|wrong|learn'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|wrong|right|true|not true|false|need to write|should write'},
            {'label': 'two pieces of evidence', 'any': ['kai', 'mo', 'opposite', 'remember', 'forgot', 'sticky', 'note', 'table', 'spoon', 'stainless', 'proof', 'dana', 'row', 'jump', 'data', 'fork', 'tin can', 'bean'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-1': 15, 'ans-2': 12, 'cer-4': 30},
    'hints': {
        'ans-1': ['Pick one thing you tested today: the tin can, the spoon, a thing on the ruler…', 'What did you predict? What really happened?', 'Try: I predicted the ___ would ___. It ___. I learned that ___.'],
        'ans-2': ['The penny is metal, but did it stick?', 'What is a penny made of? Is that one of the magnetic metals?', 'Try: The data shows the penny is ___. Now I understand that ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'Kai and Mo remembered opposite results for the same bottle cap.',
                'Mo’s sticky notes were a mess until we put them in a data table.',
                'Only the data table could prove to Dana that the stainless spoon didn’t stick.',
                'Writing takes a long time.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · Proof for the Steel Bin', 'length': '40–50 s'},
        'warmup': {'label': 'Warm-Up · spot the differences (Clue 1)', 'length': '15–20 s',
                   'script': 'Dr. Nair here. Kai and Mo tested the same bottle cap and got opposite results! Read both notes. Tap every place where they tested differently. Then decide: whose result should we trust?'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · the how-sure dial (Clue 2)', 'length': '15–20 s',
                  'script': 'Predict first. Will it stick? Then turn the dial: how sure are you? Press Test it. If you were sure and wrong, you earn a gold star. That is big learning!'},
        'part2': {'label': 'Part 2 · messy notes to a data table (Clue 3)', 'length': '15–20 s',
                  'script': 'Mo used sticky notes, and they are a mess! Read each note, then drag it onto the right row of the data table. Watch the spoon row. A surprise is hiding there.'},
        'part3': {'label': 'Part 3 · make it a fair test', 'length': '20–30 s'},
        'explore': {'label': 'Part 4 · slide to the jump (Clue 4)', 'length': '15–20 s',
                    'script': 'First, lock the fair test settings. Then pick an item and slide it toward the magnet along the ruler. Does it jump? At how many centimeters? Your data table fills in as you go.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · run your own magnet test', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '15–20 s'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease week 29 (mystery materials).'},
    },
    'videoOff': [],
    'lensVoice': False,
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'All three differences found (Warm-Up)',
        'A gold star on the how-sure dial (The Lesson)',
        'Mo’s finished data table (The Lesson)',
        'Your ruler data table with all 8 items (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['Kai and Mo’s two tests', 'The stainless spoon and the steel fork', 'Something jumping to a magnet'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · draw and label your two circles', 'required': True, 'minLabels': 4,
                           'prompts': ['Draw two big circles', 'Label them MAGNETIC and NONMAGNETIC', 'Draw your 6 items in the right circles', 'Label each item']}]},
    'hlCoach': copy.deepcopy(O['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🧾', 'name': 'Dana’s steel-bin receipt',
                 'line': 'You cracked Case 28, part 2, and Dana’s steel-bin receipt goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next week: mystery materials!'},
    'notebookTitle': O['notebookTitle'],
    'notebook': copy.deepcopy(Q['notebook']) + [{'lesson': '28.02', 'icon': '🧾', 'name': 'Dana’s steel-bin receipt'}],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are sorted. Nice testing!',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to see what it means.']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '#tab-vocab p', 'text': 'Then decide whose result to trust.'},
         'label': 'Warm-Up: two volunteers, two answers', 'q': 'Warm-Up: what Kai and Mo did differently, whose result I trust, and how I would test fairly.', 'title': 'My fair-test fix', 'compact': True,
         'fields': [{'t': 'What they did differently', 'icon': '🔍', 'ph': 'Kai ___, but Mo ___.'},
                    {'t': 'Whose result I trust', 'icon': '🤔', 'ph': 'I trust ___ because ___.'},
                    {'t': 'How I’d test it fairly', 'icon': '⚖️', 'ph': 'Use the same ___ and the same ___.'}]},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'finish the sentence about your pattern'},
         'label': 'Part C: run your own magnet test', 'q': 'Part C: my 6 items, predictions, results and pattern.', 'title': 'My magnet test',
         'fields': [{'t': 'My 6 items', 'icon': '🧺', 'ph': '1. ___ 2. ___ 3. ___ 4. ___ 5. ___ 6. ___'},
                    {'t': 'My predictions', 'icon': '🎯', 'ph': 'Stick: ___. Won’t stick: ___.'},
                    {'t': 'My results', 'icon': '🧲', 'ph': 'Stuck: ___. Didn’t stick: ___.'},
                    {'t': 'My pattern', 'icon': '📋', 'ph': 'I claim ___ are magnetic. My evidence is ___.', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Do scientists need to write their results down?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-1': 'Part B · Question 5', 'ans-2': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
T = D['tool']
T['teaser'] = 'Put a steel plate, then an aluminum plate, in front of a magnet. Which one blocks the field?'
T['done'] = 'Tool of the Week: you found which plate blocks a magnetic field.'
T['fieldviewer'] = {
    'title': 'Block the field?', 'todo': ['Pick a setup.', 'Press Sprinkle and watch the filings.', 'Try all three, then answer the question.'],
    'model': 'A model: each little line is a filing, turned the way the magnetic field points.', 'sprinkleBtn': '🧂 Sprinkle the iron filings',
    'setups': [
        {'k': 'none', 'icon': '1️⃣', 't': 'No plate', 'mags': [[150, False]], 'note': 'The field spreads out on both sides of the magnet.'},
        {'k': 'steel', 'icon': '🔩', 't': 'Steel plate', 'mags': [[150, False]], 'plate': {'x': 270, 'kind': 'steel', 'label': 'steel'}, 'note': 'The steel plate soaks up the field. Behind it, the filings hardly line up at all.'},
        {'k': 'alu', 'icon': '✨', 't': 'Aluminum plate', 'mags': [[150, False]], 'plate': {'x': 270, 'kind': 'alu', 'label': 'aluminum'}, 'note': 'The aluminum plate changes nothing. The field goes right through it.'}],
    'q': {'q': 'Which plate blocked the magnet’s field?',
          'opts': [{'t': 'The steel plate', 'ok': True, 'why': 'Steel is magnetic, so it pulls the field into itself. Aluminum isn’t magnetic, so the field passes right through.'},
                   {'t': 'The aluminum plate', 'why': 'Look again: behind the aluminum plate, the filings still line up.'},
                   {'t': 'Both of them', 'why': 'Compare the two setups. Only one of them changed the filings.'}]}}
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'A fair test changes only one thing, and a data table keeps every result as evidence.',
    'key': ['fair', 'one', 'data', 'table', 'evidence'],
    'small': ['a', 'and', 'only', 'keeps'],
    'model': 'A scientist might highlight “fair test”, “one thing” and “data table”. Those words hold the big idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this tell how to test fairly, or what counts as evidence?']

D['cues'] = {
    'warmup': [{'at': '^opposite', 'sel': '.fs-sdf-two', 'fx': 'glow', 'scroll': True},
               {'at': '^notes', 'sel': '.fs-sdf-page', 'i': 0, 'fx': 'pop'},
               {'at': '^tap', 'sel': '.fs-sdf-w[data-id]', 'i': 0, 'fx': 'point'},
               {'at': '^trust', 'sel': '[data-mod="spotdiff"] .fs-todo li', 'i': 2, 'fx': 'trace'}],
    'part1': [{'at': '^predict', 'sel': '.fs-srd-card .fs-sv-q', 'i': 0, 'fx': 'pop', 'scroll': True},
              {'at': '^dial', 'sel': '.fs-srd-dial', 'fx': 'point'},
              {'at': '^test', 'sel': '.fs-srd-go', 'fx': 'point'},
              {'at': '^gold', 'sel': '[data-mod="suredial"] .fs-count', 'fx': 'pop'}],
    'part2': [{'at': '^sticky', 'sel': '.fs-n2t-board', 'fx': 'glow', 'scroll': True},
              {'at': '^drag', 'sel': '.fs-n2t-note', 'i': 0, 'fx': 'point'},
              {'at': '^table', 'sel': '.fs-n2t-table', 'fx': 'glow'},
              {'at': '^spoon', 'sel': '.fs-n2t-row[data-id="spoon"]', 'fx': 'wiggle'}],
    'explore': [{'at': '^lock', 'sel': '.fs-jmp-set', 'fx': 'pop', 'scroll': True},
                {'at': '^slide', 'sel': '[data-mod="ruler"] .fs-todo li', 'i': 1, 'fx': 'trace'},
                {'at': '^ruler', 'sel': '.fs-jmp-stage', 'fx': 'glow'},
                {'at': '^table', 'sel': '[data-mod="ruler"] .fs-count', 'fx': 'pop'}],
}
D['cueWords'] = json.load(open('cuewords.json', encoding='utf-8')) if os.path.exists('cuewords.json') else {}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
# budget counter (oao-audio-budget): G4 science = 1,400 credits per lesson; scripts are written to 95% (1,330). Nothing is generated from week 25 on.
clips = {k: v['script'] for k, v in D['slots'].items() if v.get('script')}
tot = sum(len(t) for t in clips.values())
for k, t in clips.items(): print(f'  {k:10} {len(t):4}')
print(f'this page: {tot} / 1400 credits ({tot/1400:.0%}), scripts only, 0 generated')
assert tot <= 1330
json.dump(clips, open('clip-scripts.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
