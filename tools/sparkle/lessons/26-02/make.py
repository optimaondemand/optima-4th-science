#!/usr/bin/env python3
"""Writes data.json and fixes.json for 26.02 (run from this folder). Case 26, part 2 "Around the Bend" (Dr. Priya Nair, Palmetto Springs):
the Duck Derby moved to Palmetto Creek (26.01's fix). The ducks float the long way around a bend; the two judges' docks are 300 feet apart across an open marsh.
At the practice run the walkie-talkies cut out and the waterfall drowned out shouting: "WAIT, our net isn't ready!" was heard as "...ready!".
New: case.creek (a hand-drawn creek map + a walkie practice log + Mr. Ortiz's note), knock (Warm-Up: the secret knock), morsekey (Part 1: tap/hold a flashlight key),
lighthouse (the wow: three real Florida lighthouse flash patterns, then the real Cape Canaveral photo), crossbend (Part 2: switch on each limit, signals drop out, check goals),
codetest (Part 3 = the old Explore: the judges' first code fails a partner test; change ONE thing, retest until 4/4), fogtwist (after the solve: race night mist),
myname (bonus, folded: your name in Morse). No Tool of the Week (26.01 has the tuning fork). SCRIPTS ONLY: clip scripts written and budgeted, nothing generated."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
O = json.load(open('../26-01/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
PS = '<p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

# ---------------------------------------------------------------- labels (standing approval)
fx('fix', 'unit label: “Ecosystems & Energy” is a leftover; the plan puts Module 26 in “Energy, Motion, and Waves”', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Energy, Motion &amp; Waves</div>')
fx('fix', 'coded messages with light and sound waves are physical science (engineering), not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standards label: the plan’s CPALMS code; TEKS is a Texas code that isn’t in the plan', '<div class="info-value">SC.4.N.1.8 · TEKS 4.4(A)</div>', '<div class="info-value">SC.4.N.1.8</div>')
fx('fix', 'quarter label: weeks 24 on are Q4 in the Canvas plan', '<div class="info-value">Q3 &middot; Week 26</div>', '<div class="info-value">Q4 &middot; Week 26</div>')
fx('fix', 'quarter label in the footer', 'Science &middot; Quarter 3 &middot; Student Lesson Page', 'Science &middot; Quarter 4 &middot; Student Lesson Page')

# ---------------------------------------------------------------- ticked fixes (Bethany, 25 Nov 2026)
fx('fix', '22.01 leftover: the Warm-Up title and subtitle named the toaster lesson', '<div class="act-title">🌅 Warm-Up: What Goes In, What Comes Out?</div>\n        <div class="act-subtitle">A familiar device, a hidden change</div>',
   '<div class="act-title">🌅 Warm-Up: The Secret Knock</div>\n        <div class="act-subtitle">When does a pattern become a message?</div>')
fx('fix', '22.01 leftover: the toaster warm-up → the secret knock', '<p>Think about a toaster. You drop in cold bread. A minute later, you pull out hot toast.</p>',
   '<p>Knock, knock! Someone is at the clubhouse door. Listen to the knock, then knock it back.</p>')
fx('fix', '22.01 leftover: the toaster sketch → codes you already know (answered on the page)',
   "<p>In your notebook, draw a quick sketch of a toaster. On one side, label what goes IN. On the other, label what comes OUT. (Hint: bread on both sides — but something invisible is also going in. What is it?)</p>",
   '<p>Now think of a code you already know, like a doorbell, a school bell or a car horn. What pattern does it use, and what does it mean?</p>')
fx('fix', '22.01 leftover: Notice & Wonder about the toaster',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Notice &amp; Wonder</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover: “energy can CONVERT … toasters” callout',
   r'<div class="callout callout-tip">\s*<span class="callout-icon">💡</span>\s*<p>Today you\'ll learn that energy can CONVERT.*?</p>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover: “Device” is in the plan row, but its meaning was about converting energy. Same word, a meaning for this lesson',
   'A tool or machine designed to do a job. Most devices convert energy from one form to another — a flashlight, a toaster, a fan are all devices.',
   'A tool or machine made to do a job, like a flashlight or a whistle.')
fx('fix', '22.01 leftover: the Stop & Reason asked about “the three devices above” (no devices on this page); removed with the lean cut below', 'Look at the three devices above.', 'Look at the three devices above.')
fx('fix', 'Morse history (ticked): Morse code in the 1800s went over telegraph wires (railroads used the telegraph to run trains safely); ships sent it by radio from about 1900 and by signal lamps',
   'In the 1800s, sailors and trains used Morse code to send urgent messages across long distances. It used short and long pulses (dots and dashes) — basically the same idea you\'ll design today.',
   'In the 1800s, telegraph operators tapped Morse code over wires, and railroads used it to run trains safely. Later, ships sent it by radio and flashed it with lamps.')
fx('fix', 'shaky facts (ticked): no evidence that Florida lighthouse keepers signaled ships in Morse; the true part (every lighthouse has its own flash pattern; Cape Canaveral: 2 flashes every 20 s) is now the lighthouse wow. Removed with the lean cut below.',
   "Florida's lighthouse keepers used Morse code with flashing lights", "Florida's lighthouse keepers used Morse code with flashing lights")
fx('fix', '9.01 leftover: Part C was a food chain; the checklist already asks for a code design', '🎨 Part C &mdash; Build Your Own Food Chain', '🎨 Part C &mdash; My Code Design')
fx('fix', '9.01 leftover: Part C task → design a code for your own life (key drawn on the sketch pad; goals, limit, test plan and predicted redesign typed)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Invent a code for your own life, like a family signal or a game with a friend. Draw its key with 4 messages. Then write your goals, a limit, a test plan and one redesign you predict.</p>', True)
fx('fix', '9.01 leftover: Reflect asked about a hawk; the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'supply list: what Part C can use', r'<span class="need-chip"><span>✏️</span>Colored pencils</span>', '<span class="need-chip"><span>🔦</span>Optional: a flashlight</span>', True)
fx('fix', 'wrong closing teaser (ticked): the next lesson is 27.01 What Is Matter?, not rocks and fossils',
   " Next module starts something new — Earth's past and the rocks and fossils that tell its story.</p>", ' Next lesson starts something new: matter, the stuff everything is made of.</p>')

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; plain words', r"<p>Hold this question in your head as you work\. By the end of the lesson.*?</p>",
   "<p>Keep this question in mind. By the end, you’ll design a code, test it with a partner and make it better.</p>", True)
fx('plain', 'cut filler; no dash', r"<p>These six words show up all through the lesson\. <strong>Tap a card to flip it</strong>.*?</p>",
   "<p><strong>Tap a card to flip it</strong> and read what the word means.</p>", True)
fx('plain', 'Word Wall: no dash', 'A repeating arrangement that has meaning — like dot-dash-dot or three slow claps. Patterns are how we turn waves into messages.', 'A repeating arrangement that has meaning, like dot-dash-dot or three slow claps. Patterns are how we turn waves into messages.')
fx('plain', 'Word Wall: no dash', 'To improve a design based on what testing taught you. Every test that fails teaches you something — and you redesign to fix it.', 'To improve a design based on what testing taught you. Every test that fails teaches you something, and you redesign to fix it.')
fx('plain', 'Part 1: shorter, no dashes (same meaning)', ' is something repeating in a way you can recognize. Three slow knocks. Two short flashes followed by a long flash. A red light then a green light. When a pattern means something — like "open the door" or "stop, then go" — it becomes a ',
   ' is something that repeats in a way you can recognize, like three slow knocks or two short flashes. When a pattern means something, like “open the door,” it becomes a ')
fx('plain', 'Part 1: shorter, no dash (Morse code is explained in the game just below and in Part 2)', ' messages using waves. Morse code uses dots and dashes (short and long signals) to spell out letters. Phone signals use patterns of radio waves. Even traffic lights are a basic code — red, yellow, green mean specific things.',
   ' messages with waves of light, sound or radio. Phone signals use patterns of radio waves. Even traffic lights are a simple code: red, yellow and green each mean something.')
fx('cut', 'lean: the Stop & Think (four knocks) is played in the Warm-Up knock game; a one-line lead-in to the Part 1 game instead',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*',
   '<p>Try it! Send a message with a flashlight key, the way Morse code does.</p>\n\n      ', True)
fx('cut', 'lean: the Test line in the example list (Part 3 is the test)', r'\s*<li><strong>Test:</strong> have your partner read your message and tell you what they got\.</li>', '', True)
fx('plain', 'misconception paragraph: plain words, no dash, shorter (same idea)', r'<p><strong>Common misconception:</strong> Some people think a code needs to be complicated to be useful\. Simple codes are often the best.*?</p>',
   '<p><strong>Watch out:</strong> some people think a code has to be complicated to work. Simple codes are often best: fewer parts to remember, fewer ways to misread.</p>', True)
CAP = '<div class="lesson-figure-caption"><strong>A good code sheet has four parts:</strong> the patterns, the criteria, the constraints, and a redesign plan.</div>\n      </div>'
fx('plain', 'leads into the Part 2 game (the creek’s goals and limits)', CAP, CAP + '\n\n      <p>Now be the engineer for the Duck Derby. Which signal can cross the bend?</p>')
fx('plain', 'Science Connection: define “creativity” where first seen (same meaning; this box teaches SC.4.N.1.8, so it stays)',
   '<p><strong>Science Connection:</strong> Scientists and engineers use creativity. Inventing a code means imagining a new pattern, testing whether others can read it, and improving it.</p>',
   '<p><strong>Science Connection:</strong> Scientists and engineers use creativity (coming up with new ideas). Inventing a code means imagining a new pattern, testing whether others can read it, and improving it.</p>')
fx('plain', 'Part B question 6 label (Gathered Answers)', 'data-label="Explain why testing with a partner is important in..."', 'data-label="Why test with a partner?"')
fx('plain', 'Part B question 7 label (Gathered Answers)', 'data-label="Why is REDESIGN such an important step? Give an ex..."', 'data-label="Why redesign matters, and my redesign"')
fx('plain', 'CER label (Gathered Answers)', 'id="cer-4" data-label="Response"', 'id="cer-4" data-label="Use Your Evidence: do engineers get it right the first time?"')
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'closing: no dash', "You've now done what real engineers do — defined", "You did what real engineers do: you defined")

# ---------------------------------------------------------------- lean cuts
fx('cut', 'removed: Key Concept, the Stop & Reason (22.01 leftover), the Four Coded Systems tap diagram (Part B question 5 that used it is cut; the knock, the flashlight key and the lighthouses cover the same systems), Observe & Reason, the World War II fact (shaky: “faster than most people type”), the Florida connection (Morse-signaling keepers: no evidence; the true flash-pattern part is the lighthouse wow) and Go Deeper (true, beyond this lesson)',
   r'\s*<div style="background:#FFF6E5;border:2\.5px solid #F0C97A;[^>]*>\s*<div[^>]*>⭐ Key Concept</div>.*?(?=<div class="callout callout-think scroll-reveal">)', '\n\n      ', True)
fx('cut', 'Part 3 = the old Explore (Engineering Challenge: Design Your Code → Test It Across the Creek); the next button goes to Self-Check',
   '''<div class="tab-next-wrap">
        <button class="tab-next-btn" onclick="switchTab('explore')">Continue to 🔬 Explore →</button>''',
   H3 + 'Part 3 · Test It Across the Creek</h3>\n      ' + PS + 'The judges made their first code: a pattern of flashes for each race message. Test it with a partner at the finish dock. Find what fails, change one thing and test again.</p>\n  <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>')
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its design-test-redesign steps are now the Part 3 game and Part C; its Big Cypress “radio code patterns” fact (no source, likely made up), Think like a scientist and Go Deeper (binary: true, beyond this lesson) go with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 5 removed (Bethany kept 6 and 7; 5 asked about the removed tap diagram)', r'<div class="pq">\s*<span class="pq-num"[^>]*>5</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 6 and 7 answered')
fx('cut', 'lean: Part C drawn and typed on the page', 'A full code design — key with 4 messages, 2 criteria, 1 constraint, a test plan, and one predicted redesign.',
   'My goals, my limit, my test plan and one redesign I predict. Plus your labeled sketch: your code key with 4 messages and their patterns.')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether testing is essential to good engineering, supported with two pieces of evidence.',
   '<strong>Use Your Evidence:</strong> My claim about whether real engineers get it right the first time, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a 9.01 leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Download your field journal (it has your answers and your code key sketch) and upload it to the Canvas assignment. Or copy your Gathered Answers (above) into Canvas.', True)
# two placeholder fixes above (Stop & Reason, Florida callout) only record WHY; their text goes with the Key Concept cut. Drop them from the file (old == new).
F[:] = [f for f in F if f['old'] != f['new']]

# ---------------------------------------------------------------- the story
PRIYA = O['crew']['priya']
MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--',
         'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}
MAP = {'start': '🚩 START dock', 'finish': '🏁 FINISH dock', 'fall': '💦 little waterfall (LOUD!)', 'hill': '🌾 open marsh', 'feet': '300 feet across the marsh', 'duckWord': '🦆 the ducks float the long way',
       'alt': 'Mr. Ortiz’s hand-drawn map. Palmetto Creek bends the long way around an open marsh, past a little waterfall. The start dock and the finish dock are 300 feet apart across the marsh.'}
LIGHT = {'img': 'images/26-02-cape-canaveral-light.jpg', 'alt': 'The real Cape Canaveral Lighthouse: a tall tower with wide black and white stripes, a lantern room on top, a palm tree and a small brick building at its base, under a blue sky.',
         'cap': 'The real Cape Canaveral Lighthouse in Florida. Every night it still flashes twice every 20 seconds, and sailors can see it about 24 nautical miles (28 miles) out at sea. Photo: NASA/Jim Grossmann, public domain, via Wikimedia Commons.'}
D = {
    'lesson': '26.02', 'week': 26, 'day': 2, 'guide': 'priya', 'prefix': 'g4sci-26-2', 'manifestKey': '26-02',
    'paths': P['paths'], 'crew': {'priya': PRIYA},
    'expedition': {'num': 26, 'title': 'Around the Bend'},
    'ambient': {'icon': '🦗', 'label': 'Creek at dusk'},
    'case': {
        'num': 26, 'title': 'Around the Bend', 'style': 'flyer',
        'hook': 'Good news! Mr. Ortiz took our advice. This year’s Duck Derby will float down Palmetto Creek, where the water flows. But the creek bends the long way around a marsh, and the practice run went wrong.',
        'creek': {
            'map': MAP, 'mapCap': 'Mr. Ortiz’s map. The judges can see each other across the marsh, 300 feet apart.',
            'log': {'head': 'WALKIE-TALKIE PRACTICE RUN', 'sub': 'Saturday, 6:55 p.m. · Start dock and finish dock', 'cols': ['Who', 'What they said', 'What the other dock heard'],
                    'rows': [['Finish judge', 'WAIT! Our net isn’t ready!', '“…ready!” (crackle)', 1],
                             ['Start dock', 'Ready? Then GO!', '(nothing, just the waterfall)', 1],
                             ['Finish judge', 'The ducks are here, and there’s no net!', '(nothing)', 1]]},
            'note': {'to': 'Dear Dr. Nair,', 'body': ['Our walkie-talkies cut out at the bend, and the waterfall drowns out shouting.',
                                                       'Race night starts at 6:30 p.m., just before sunset. The judges need a code they can flash across the marsh: READY, WAIT, GO and WINNER IN. Can you help us make one that won’t get mixed up?'],
                     'sign': 'Mr. Ortiz, race organizer'}},
        'stills': [],
        'question': 'What code should the judges use on race night, and how will they know it works?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'knock', 'icon': '🚪', 'where': 'Warm-Up: the secret knock', 't': 'The knock meant nothing until the code key came out. A pattern is a code only when the sender and the receiver share the same rules.'},
            {'id': 'morsekey', 'icon': '🔦', 'where': 'The Lesson, Part 1: the flashlight key', 't': 'A good code uses patterns that are easy to tell apart, like clearly short and clearly long flashes. A flash in between got a “?”.'},
            {'id': 'crossbend', 'icon': '🚧', 'where': 'The Lesson, Part 2: which signal crosses the bend?', 't': 'No signal, a loud waterfall, sunset and no ropes across the water: only a flashlight met every goal inside every limit.'},
            {'id': 'codetest', 'icon': '📝', 'where': 'The Lesson, Part 3: test it across the creek', 't': 'The judges’ first code failed the partner test: short flashes in a row got mixed up. After a redesign and a new test, the partner read 4 out of 4.'},
        ],
        'solve': {
            'title': 'Which code should the judges use?', 'q': 'Which plan fits all four clues?',
            'options': [
                {'t': 'Talk on the walkie-talkies, but louder.', 'why': 'Check Clue 3. There’s no signal at the bend, and the waterfall drowns out voices.'},
                {'t': 'Full Morse code for every letter. More patterns make a better code.', 'why': 'Check Clue 2 and Clue 4. More patterns mean more chances to mix them up. Simple codes are often best.'},
                {'t': 'A simple flashlight code where every message looks very different, tested by a partner at the creek and redesigned until the partner reads 4 out of 4.', 'right': True,
                 'why': 'Case cracked! A code works when both judges share the key, the patterns are easy to tell apart, and a partner test proves it.'},
                {'t': 'Mr. Ortiz’s first code. He can read it, so it works.', 'why': 'Check Clue 1 and Clue 4. The finish judge has to read it too, and the partner test mixed it up.'},
            ]},
    },
    'knock': {
        'afterText': 'Listen to the knock, then knock it back.', 'kicker': 'Warm-Up game', 'title': 'The secret knock',
        'why': {'icon': '🚪', 'q': 'What is a secret knock?', 't': 'A knock pattern that friends agree on, so they know who is at the door without opening it or talking.'},
        'todo': ['Press Listen to the knock.', 'Tap the door to knock the same rhythm back. Knocks close together make a group. A pause starts a new one.', 'Then find the code key.'],
        'sign': 'CLUB', 'alt': 'A wooden clubhouse door with a CLUB sign and a red welcome mat.',
        'listenBtn': '👂 Listen to the knock', 'againBtn': '🔁 Listen again', 'doorBtn': '👊 Tap the door to knock', 'heardLabel': 'The door knocked', 'youLabel': 'You knocked',
        'listenFirst': 'Listen to the knock first.', 'gap': 550, 'endGap': 1400,
        'rounds': [{'id': 'r1', 'ask': 'Listen first. Then knock it back.', 'play': [2, 1], 'done': 'You knocked it back exactly: knock-knock … knock!'},
                   {'id': 'r2', 'ask': 'Now answer with the club code. Tell your friend “Come in!”', 'want': 'in', 'hint': 'three quick knocks (●●●)', 'done': 'Your friend heard “Come in!” and opened the door.'}],
        'wrongLine': 'You knocked {got}. Try again: {want}.',
        'q0': 'You copied the knock. But what does it MEAN?', 'keyBtn': '🧺 Look under the mat', 'keyHead': 'Club knock code',
        'key': [{'id': 'friend', 'g': [2, 1], 't': 'It’s me, a club friend!'}, {'id': 'in', 'g': [3], 't': 'Come in!'}, {'id': 'wait', 'g': [1, 2], 't': 'Wait a minute.'}],
        'q1': 'The code key is out! What did the first knock mean?', 'q1Miss': 'Find the row with the same dots as the knock you copied.',
        'doneLine': 'Message sent and read!',
        'q': 'Why could you read the knock only after you found the key?',
        'opts': [{'t': 'A pattern becomes a code when both people know the rules', 'ok': True},
                 {'t': 'The knocks got louder', 'miss': 'The knocks were the same. What did the key give you?'},
                 {'t': 'Knocks are always secret', 'miss': 'Anyone with the key can read it. What is written on the key?'}],
        'win': 'A pattern means something only when the sender and the receiver share the same rules. That’s a code! Clue 1!'},
    'morsekey': {
        'afterText': 'the way Morse code does.', 'kicker': 'Part 1 game', 'title': 'The flashlight key',
        'why': {'icon': '🔦', 'q': 'What is Morse code?', 't': 'A code where each letter is a pattern of short and long signals: clicks, beeps or flashes of light.'},
        'todo': ['Tap the red key quickly for a short flash (a dot). Hold it down for a long flash (a dash).', 'Stop for a moment after each letter.', 'Send SOS. Then send GO.'],
        'keyBtn': 'Tap or hold', 'dotMax': 280, 'dashMin': 430, 'letterGap': 1000, 'letters': MORSE, 'cheatLabel': 'Code key', 'sendLabel': 'Send this:',
        'rounds': [{'word': 'SOS', 'ask': 'SOS means “help!” Send it: three short, three long, three short.', 'done': 'You sent SOS! Ships have used this pattern to call for help.'},
                   {'word': 'GO', 'ask': 'Now send GO, the start signal for the race.', 'done': 'You sent GO!'}],
        'showBtn': '▶ Show me', 'clearBtn': '↺ Clear', 'emptyLine': 'Your flashes show up here.',
        'wobbly': 'That flash was too long for a dot and too short for a dash. Your partner can’t tell which one you meant! Tap quickly for a dot, or hold longer for a dash.',
        'wrongLetter': 'The letter {want} is {code}. Start the word again.',
        'q': 'Why does Morse code use just two kinds of flashes, short and long?',
        'opts': [{'t': 'They are easy to tell apart, so the receiver doesn’t mix them up', 'ok': True},
                 {'t': 'Long flashes are brighter', 'miss': 'A long flash isn’t brighter. It just lasts longer. Why is that easy to read?'},
                 {'t': 'So nobody can read it', 'miss': 'Anyone with the code key can read it. Think about the orange “?” on your strip.'}],
        'win': 'A code works when its patterns are easy to tell apart. A flash that wasn’t clearly short or long got a “?”. Clue 2!'},
    'lighthouse': {
        'after': 'morsekey', 'kicker': 'Wow!', 'title': 'Every lighthouse has a fingerprint',
        'why': {'icon': '🗼', 'q': 'Why do lighthouses blink?', 't': 'At night a sailor can’t see the tower, only its light. Each lighthouse flashes its own pattern, so sailors know which one they are looking at.'},
        'todo': ['Count each light’s flashes before it goes dark.', 'Drag each name onto its lighthouse, or tap a name and then a lighthouse.'],
        'speed': 5, 'model': 'a model, sped up {n} times', 'listHead': 'The light list (what sailors read)',
        'alt': 'A model of a dark Florida coast at night with three lighthouses, A, B and C. Each one blinks its own pattern.',
        'lights': [{'id': 'ponce', 'name': 'Ponce de Leon Inlet', 'short': '6 flashes, then dark, every 30 seconds', 'flashes': 6, 'apart': 2.5, 'period': 30},
                   {'id': 'staug', 'name': 'St. Augustine', 'short': '1 flash every 30 seconds', 'flashes': 1, 'apart': 0, 'period': 30},
                   {'id': 'canaveral', 'name': 'Cape Canaveral', 'short': '2 flashes every 20 seconds', 'flashes': 2, 'apart': 5, 'period': 20}],
        'miss': 'Count that light’s flashes before it goes dark. {name}: {short}.',
        'photo': LIGHT,
        'done': 'Sailors read the pattern, not the tower. Two flashes every 20 seconds means Cape Canaveral: a code made of light!'},
    'crossbend': {
        'afterText': 'Which signal can cross the bend?', 'kicker': 'Part 2 game', 'title': 'Which signal crosses the bend?',
        'todo': ['Tap each limit to switch it on.', 'Watch which ways to send a message get crossed out.', 'Then check the last one against each goal.'],
        'map': dict(MAP, duckWord='', feet=''),
        'limitsLabel': 'The limits at the bend (constraints): tap each one to switch it on', 'toolsLabel': 'Ways to send a message', 'onWord': 'switched on', 'offWord': 'tap to switch on',
        'tools': [{'id': 'phone', 'icon': '📱', 't': 'Text message'}, {'id': 'shout', 'icon': '📢', 't': 'Shouting'}, {'id': 'walkie', 'icon': '📻', 't': 'Walkie-talkie'},
                  {'id': 'flags', 'icon': '🚩', 't': 'Waving flags'}, {'id': 'bell', 'icon': '🔔', 't': 'A bell on a rope across the creek'}, {'id': 'light', 'icon': '🔦', 't': 'Flashlight'}],
        'limits': [{'id': 'signal', 'icon': '📵', 't': 'No signal at the bend: phones and walkie-talkies cut out', 'kills': ['phone', 'walkie'], 'why': 'No signal at the bend.'},
                   {'id': 'fall', 'icon': '💦', 't': 'The waterfall is too loud to hear voices', 'kills': ['shout'], 'why': 'The waterfall drowns out voices.'},
                   {'id': 'dusk', 'icon': '🌇', 't': 'The race ends at sunset, when it gets dark', 'kills': ['flags'], 'why': 'Too dark to see flags at sunset.'},
                   {'id': 'rope', 'icon': '🦆', 't': 'Nothing can stretch across the water: the ducks float through', 'kills': ['bell'], 'why': 'A rope would catch the ducks.'}],
        'leftLine': 'Only one is left: {t}. Does it meet every goal?', 'goalsLabel': 'The goals (criteria): tap each one to check',
        'goals': [{'id': 'reach', 'icon': '📏', 't': 'Reaches the finish dock, 300 feet away', 'ok': 'At dusk, a bright flashlight can be seen much farther than 300 feet.'},
                  {'id': 'four', 'icon': '✉️', 't': 'Can send 4 different messages', 'ok': 'Short and long flashes can make lots of different patterns.'},
                  {'id': 'fast', 'icon': '⏱️', 't': 'The finish judge can read it in a few seconds', 'ok': 'A short pattern of flashes takes just a second or two.'}],
        'keep': 'light',
        'q': 'Which one of these is a CONSTRAINT (a limit)?',
        'opts': [{'t': 'The waterfall is too loud to hear voices', 'ok': True},
                 {'t': 'Can send 4 different messages', 'miss': 'That’s a goal: something the design must DO. A constraint is a limit.'},
                 {'t': 'Reaches the finish dock', 'miss': 'That’s a goal too. Which one limits what you can use?'}],
        'win': 'Criteria are the goals. Constraints are the limits. At the bend, only the flashlight met every goal inside every limit. Clue 3!'},
    'codetest': {
        'afterText': 'change one thing and test again.', 'kicker': 'Part 3 game', 'title': 'Test it across the creek',
        'why': {'icon': '🧪', 'q': 'What is a partner test?', 't': 'Your partner writes down what they see. Here a model partner reads your flashes from the finish dock, 300 feet away.'},
        'todo': ['Press Test across the creek to test the judges’ first code.', 'Read the test sheet. Which messages got mixed up?', 'Change ONE thing: a pattern tile on one message, or the gap. Then test again.',
                 'Keep going until your partner reads 4 out of 4. There’s more than one way to fix it, so be creative!'],
        'msgs': [{'id': 'ready', 'icon': '🟢', 't': 'READY'}, {'id': 'wait', 'icon': '✋', 't': 'WAIT'}, {'id': 'go', 'icon': '🦆', 't': 'GO'}, {'id': 'winner', 'icon': '🏆', 't': 'WINNER IN'}],
        'tiles': [{'id': 't1', 'p': '.'}, {'id': 't2', 'p': '..'}, {'id': 't3', 'p': '...'}, {'id': 't4', 'p': '-'}, {'id': 't5', 'p': '--'}, {'id': 't6', 'p': '-.'}, {'id': 't7', 'p': '.-'}, {'id': 't8', 'p': '---'}],
        'start': {'ready': 't1', 'wait': 't2', 'go': 't3', 'winner': 't4'}, 'startGap': 'short',
        'boardLabel': 'The judges’ race code', 'gapLabel': 'Gap between flashes:', 'gaps': [{'k': 'short', 't': '⚡ Short (quick flashes)'}, {'k': 'long', 't': '🐢 Long (slow, clear pauses)'}],
        'tilesLabel': 'Pattern tiles: drag one onto a message, or tap a tile and then a message',
        'testBtn': '🔦 Test across the creek', 'againBtn': '🔦 Test again', 'sheetHead': 'Partner test #{n}', 'cols': ['Sent', 'Pattern', 'Partner got', ''], 'scoreTpl': '{n} out of 4',
        'firstLine': 'Test the judges’ first code before you change anything. Press Test across the creek.',
        'oneLine': 'You already changed one thing. Test it first! Engineers change ONE thing at a time, so they know what fixed it.',
        'sameLine': 'Nothing changed, so the test would come out the same. Change ONE thing first: a tile or the gap.',
        'changedLine': 'Changes since the last test: {n} of 1',
        'failLine': 'Some messages got mixed up. Those are your failure points. Change ONE thing and test again.',
        'passLine': 'Your partner read every message!',
        'q': 'The judges’ first code failed its test. What does that tell an engineer?',
        'opts': [{'t': 'What to fix next: a failed test shows where to redesign', 'ok': True},
                 {'t': 'The code is no good, so give up', 'miss': 'Engineers don’t give up. What did the test sheet show you to change?'},
                 {'t': 'Real engineers never fail a test', 'miss': 'Real engineers test early so they can find failures. How many tests did you run?'}],
        'win': 'Test, find the failure points, change one thing, test again. That’s redesign, and it got the code to 4 out of 4. Clue 4!'},
    'exploreMod': 'codetest',
    'fogtwist': {
        'after': '.fs-solve', 'kicker': 'Twist!', 'title': 'Race night: mist on the creek', 'lockLine': 'Crack the case first.',
        'todo': ['Test your code once more, in the real place, on race night.', 'Read the mist test sheet.', 'If it fails, pick a fix and test again.'],
        'map': MAP, 'intro': 'Race night, 7 p.m. As the sun sets, a thin mist rises off Palmetto Creek. In mist, a light looks fuzzy and spread out, so quick flashes can blur into one long glow.',
        'testBtn': '🔦 Test my code in the mist', 'againBtn': '🔦 Test again with long gaps', 'sheetHead': 'Mist test #{n}', 'longWord': 'Long gaps', 'shortWord': 'Short gaps',
        'defCode': {'ready': 't1', 'wait': 't6', 'go': 't5', 'winner': 't4'}, 'defGap': 'short',
        'fixQ': 'Your code got mixed up in the mist. What ONE change would help most?',
        'fixes': [{'t': 'Make the gaps between flashes longer', 'ok': True},
                  {'t': 'Shout the messages instead', 'miss': 'Remember the waterfall! Shouting can’t cross the marsh.'},
                  {'t': 'Give up: the code doesn’t work', 'miss': 'A failed test isn’t the end. It shows you what to change.'},
                  {'t': 'Add more messages', 'miss': 'More messages means more patterns to mix up. What would make the flashes easier to count?'}],
        'readyLine': 'Your long gaps were ready for the mist: 4 out of 4! Engineers still test in the real place, in real weather, to be sure.',
        'passLine': 'Long gaps: 4 out of 4 in the mist! One more redesign, and the code is ready for race night.',
        'win': 'Test, redesign, test again, even on race night. Engineers don’t expect to get it right the first time. They test until it works.'},
    'myname': {
        'after': '.fs-solve', 'kicker': 'Bonus', 'title': 'Send your name in Morse code',
        'todo': ['Type your first name.', 'Press Send it and watch the light blink each letter.', 'Compare the time with a one-flash race signal.'],
        'ph': 'Your first name', 'sendBtn': '🔦 Send it', 'unit': 0.2, 'letters': MORSE, 'onlyLetters': 'Type your first name with letters A to Z.',
        'timeTpl': '{name} took {s} seconds to send.', 'compare': 'A one-flash race signal takes less than 1 second. Simple codes are fast!',
        'done': 'Now you can sign your name in light!'},
    'fold': {'myname': {'icon': '🔦', 'tease': 'Type your name and watch it blink in Morse code.', 'open': 'Open'}},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'A computer program can use a code, but think about the knock at the clubhouse door. What turned those knocks into a message?', 'C': 'Anyone with the club’s code key could read the knock. A code is the set of rules.'},
        'q2': {'B': 'Think about the partner test. After it failed, what did one change do?', 'C': 'Swapping to another confusing code won’t help. What made the judges’ code work?'},
        'q3': {'A': '“No talking” is a LIMIT on how you send. Which choice says what the code must DO?', 'B': '“Only one hand” is a limit too. Which choice is a goal?'}},
    'flags': {
        'ans-2': [
            {'label': 'why a partner', 're': 'partner|someone else|another person|other person|friend|classmate|receiv|reader|they (can|could|might|will)|other people'},
            {'label': 'what goes wrong alone', 're': 'mix|confus|wrong|mistake|misread|can.?t (read|tell|understand)|cannot|doesn.?t (know|understand)|don.?t (know|understand)|only you|yourself|by myself|already know|fail|not work|won.?t work'}],
        'ans-3': [
            {'label': 'why redesign matters', 're': 'fix|better|improv|learn|work|fail|mistake|problem|wrong|mix'},
            {'label': 'a redesign idea', 're': 'long|gap|pause|space|slow|different|fewer|less|dash|bright|change|swap|new pattern'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|isn|is not|don.?t|do not|never|always'},
            {'label': 'two pieces of evidence', 'any': ['test', 'fail', 'partner', 'mix', 'redesign', 'first code', '4 out of 4', 'four out of four', 'fog', 'mist', 'knock', 'key', 'morse', 'dash', 'gap', 'judge', 'creek', 'bend', 'flash', 'change', 'tile', 'race'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-2': 15, 'ans-3': 15, 'cer-4': 30},
    'hints': {
        'ans-2': ['Who has to read your code: you, or someone else?', 'Think about the judges’ first code. Who found the mix-up?', 'Try: Testing with a partner matters because ___. If I only test by myself, ___.'],
        'ans-3': ['What did the test sheet show after the first test?', 'Think of one change: longer gaps, a long flash, fewer flashes.', 'Try: Redesign matters because ___. If my flashes were easy to confuse, I would ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'The judges’ first code failed the partner test: short flashes in a row got mixed up.',
                'After one change and a new test, the partner read 4 out of 4.',
                'On race night, the code was tested again in the mist, in the real place.',
                'The Cape Canaveral Lighthouse flashes twice every 20 seconds.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · Around the Bend', 'length': '20–30 s'},
        'warmup': {'label': 'Warm-Up · the secret knock (Clue 1)', 'length': '15–20 s',
                   'script': 'Knock, knock! Someone’s at the clubhouse door. Press Listen to the knock. Then tap the door to knock the same rhythm back. Knocks close together make a group. Then find the code key. What did the knock mean?'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · the flashlight key (Clue 2)', 'length': '15–20 s',
                  'script': 'This red key works a flashlight. Tap it quickly for a short flash, a dot. Hold it down for a long flash, a dash. Send SOS first. Watch your strip below. A flash that’s in between gets a question mark!'},
        'part2': {'label': 'Part 2 · which signal crosses the bend? (Clue 3)', 'length': '20–30 s'},
        'explore': {'label': 'Part 3 · test it across the creek (Clue 4)', 'length': '15–20 s',
                    'script': 'Here’s the judges’ first race code. Press Test across the creek, then read the test sheet. Which messages got mixed up? Change just one thing, a tile or the gap, and test again. Keep going until your partner reads four out of four!'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · my code design', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '15–20 s',
                     'script': 'A classmate says real engineers get it right the first time. Do you agree? Think about the judges’ first test, and race night in the mist. Pick your side, tap two facts in the planner, then explain. That’s your C-E-R.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 27.01 (What Is Matter?).'},
    },
    'videoOff': [],
    'lensVoice': False,
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'The club’s code key (Warm-Up)',
        'Your SOS on the flashlight strip (The Lesson)',
        'The three lighthouses at night (The Lesson)',
        'Your 4 out of 4 test sheet (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['A flashlight code key', 'A knock code', 'A whistle code'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · draw your code key', 'required': True, 'minLabels': 4,
                           'prompts': ['Write your 4 messages', 'Draw each pattern: dots and dashes, knocks or beeps', 'Label the kind of signal: light or sound', 'Make every pattern easy to tell apart']}]},
    'hlCoach': copy.deepcopy(O['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🔦', 'name': 'A judge’s signal flashlight',
                 'line': 'You cracked Case 26, part 2, and a judge’s signal flashlight goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next time: what is everything made of?'},
    'notebookTitle': O['notebookTitle'],
    'notebook': copy.deepcopy(O['notebook']) + [{'lesson': '26.02', 'icon': '🔦', 'name': 'A judge’s signal flashlight'}],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are decoded. Message received!',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to see what it means.']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '#tab-vocab p', 'text': 'What pattern does it use, and what does it mean?'},
         'label': 'Warm-Up: a code I know', 'q': 'Warm-Up: A code I know, its pattern and what it means.', 'title': 'A code I know', 'compact': True,
         'fields': [{'t': 'A code I know', 'icon': '🔔', 'ph': 'The ___'},
                    {'t': 'Its pattern', 'icon': '🔁', 'ph': 'It ___ (rings, beeps, flashes) ___ times.'},
                    {'t': 'What it means', 'icon': '💬', 'ph': 'It means ___.'}]},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'a test plan and one redesign you predict.'},
         'label': 'Part C: My code design', 'q': 'Part C: My code design (goals, limit, test plan, a redesign I predict)', 'title': 'My code design',
         'fields': [{'t': 'My 2 goals (criteria)', 'icon': '🎯', 'ph': 'My code must ___ and ___.'},
                    {'t': 'My limit (constraint)', 'icon': '🚧', 'ph': 'It can only use ___.'},
                    {'t': 'How I would test it', 'icon': '🧪', 'ph': 'My partner would stand ___ and ___.'},
                    {'t': 'One redesign I predict', 'icon': '🔧', 'ph': 'If ___ gets mixed up, I will ___.', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Do real engineers get it right the first time?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-2': 'Part B · Question 6', 'ans-3': 'Part B · Question 7', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'A code works only when the receiver knows the rules and can tell the patterns apart.',
    'key': ['code', 'receiver', 'rules', 'patterns', 'apart'],
    'small': ['a', 'only', 'when', 'the', 'and', 'can'],
    'model': 'A scientist might highlight “code”, “rules” and “patterns”. Those words hold the big idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this tell how a pattern becomes a code, or how to test and fix one?']

EV = '#tab-assignment .act-body > div:has(> .fs-plan)'
D['cues'] = {
    'warmup': [{'at': '^door', 'sel': '.fs-knk-door', 'fx': 'pop', 'scroll': True},
               {'at': '^listen', 'sel': '.fs-knk-listen', 'fx': 'point'},
               {'at': '^rhythm', 'sel': '.fs-knk-strips', 'fx': 'glow'},
               {'at': '^group', 'sel': '[data-mod="knock"] .fs-todo li', 'i': 1, 'fx': 'trace'},
               {'at': '^key', 'sel': '[data-mod="knock"] .fs-todo li', 'i': 2, 'fx': 'trace'}],
    'part1': [{'at': '^key', 'sel': '.fs-mky-key', 'fx': 'point', 'scroll': True},
              {'at': '^flashlight', 'sel': '.fs-mky-light', 'fx': 'glow'},
              {'at': '^dash', 'sel': '.fs-mky-cheat', 'fx': 'pop'},
              {'at': '^strip', 'sel': '.fs-mky-strip', 'fx': 'glow'}],
    'explore': [{'at': '^code', 'sel': '.fs-cdt-board', 'fx': 'glow', 'scroll': True},
                {'at': '^test', 'sel': '.fs-cdt-test', 'fx': 'point'},
                {'at': '^sheet', 'sel': '[data-mod="codetest"] .fs-todo li', 'i': 1, 'fx': 'trace'},
                {'at': '^tile', 'sel': '.fs-cdt-tiles', 'fx': 'pop'},
                {'at': '^gap', 'sel': '.fs-cdt-gap', 'fx': 'pop'}],
    'evidence': [{'at': '^classmate', 'sel': EV + ' > p', 'i': 0, 'fx': 'trace', 'scroll': True},
                 {'at': '^test', 'sel': '.fs-plan .fs-opt', 'i': 2, 'fx': 'glow'},
                 {'at': '^mist', 'sel': '.fs-plan .fs-opt', 'i': 4, 'fx': 'glow'},
                 {'at': '^side', 'sel': '.fs-plan .fs-plan-row', 'i': 0, 'fx': 'pop'},
                 {'at': '^explain', 'sel': '.fs-cer .fs-cer-row', 'i': 2, 'fx': 'glow', 'scroll': True}],
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
