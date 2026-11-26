#!/usr/bin/env python3
"""Writes data.json and fixes.json for 28.01 (run from this folder). Case 28 "Magnet Fishing Day" (Dr. Priya Nair, Unit 6, Palmetto Springs):
after the Duck Derby the pond gets a cleanup. Five things fell off the dock; the ranger's log says what each is made of. The team's two magnets keep pushing
apart when they try to stack them. Which items can the magnet bring up, which need the net, and how do you stack the magnets?
New (Bethany's brainstorm, 26 Nov 2026): case.lostlog, fishing (Warm-Up: cast and reel), poles (Part 1: the worn-label magnet + the wow, snap it in half),
sweeper (Part 2: the magnet sweeper), predchart (Part 4 = the old Explore: the full prediction chart, then test), cleanup + compasstwist (after the solve),
SIMS.fieldviewer (Tool of the Week), photos (the 1913 iron-filings photo, not a clue). SCRIPTS ONLY: clip scripts written and budgeted, nothing generated."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
O = json.load(open('../27-01/data.json', encoding='utf-8'))
Q = json.load(open('../27-02/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)
def VT(word, head, tip): return '<span class="vtip">' + word + '<span class="vtip-box"><span class="vtip-word">' + head + '</span>' + tip + '</span></span>'

# ---------------------------------------------------------------- labels (standing approval + ticked)
fx('fix', 'unit label (ticked): “Ecosystems & Energy” is a leftover; the plan puts Module 28 in Unit 6 “Matter, Magnets, and Changes”', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Matter, Magnets &amp; Changes</div>')
fx('fix', 'science label (ticked): magnets are physical science, not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standards label: the plan’s CPALMS code; TEKS is a Texas code that isn’t in the plan', '<div class="info-value">SC.4.P.8.4 · TEKS 4.7(C)</div>', '<div class="info-value">SC.4.P.8.4</div>')
fx('fix', 'quarter label in the footer (ticked): 28.01 is due Apr 20, Q4 in the Canvas plan (the header already says Q4)', 'Science &middot; Quarter 3 &middot; Student Lesson Page', 'Science &middot; Quarter 4 &middot; Student Lesson Page')

# ---------------------------------------------------------------- ticked fixes (Bethany, 26 Nov 2026): energy-lesson leftovers
fx('fix', '22.01 leftover: the Warm-Up title named the toaster lesson', '<div class="act-title">🌅 Warm-Up: What Goes In, What Comes Out?</div>\n        <div class="act-subtitle">A familiar device, a hidden change</div>',
   '<div class="act-title">🌅 Warm-Up: Magnet Fishing Day</div>\n        <div class="act-subtitle">What will the magnet pull up?</div>')
fx('fix', '22.01 leftover: the toaster warm-up → magnet fishing off the dock',
   '<p>Think about a toaster. You drop in cold bread. A minute later, you pull out hot toast.</p>',
   '<p>Magnet fishing means tying a strong magnet to a rope, dropping it into the water and pulling up lost things. Dr. Nair’s team is trying it off the Palmetto Springs dock.</p>')
fx('fix', '22.01 leftover: the toaster sketch → the magnet-fishing game (played and answered on the page)',
   "<p>In your notebook, draw a quick sketch of a toaster. On one side, label what goes IN. On the other, label what comes OUT. (Hint: bread on both sides — but something invisible is also going in. What is it?)</p>",
   '<p>Before every cast, make your guess. Then reel it up and see.</p>')
fx('fix', '22.01 leftover: Notice & Wonder about the toaster',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Notice &amp; Wonder</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover: “energy can CONVERT … toasters” callout',
   r'<div class="callout callout-tip">\s*<span class="callout-icon">💡</span>\s*<p>Today you\'ll learn that energy can CONVERT.*?</p>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover (ticked): “Device” meant converting energy; this lesson’s devices are a compass and a magnet sweeper',
   'A tool or machine designed to do a job. Most devices convert energy from one form to another — a flashlight, a toaster, a fan are all devices.',
   'A tool or machine made to do a job. A compass and a magnet sweeper are devices.')
fx('fix', '22.01 leftover (ticked): the Stop & Reason asked about “the three devices above … INPUT and OUTPUT” (no devices on this page)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', '9.01 leftover (ticked): Part C was a food chain; the checklist already asks for a two-magnet diagram', '🎨 Part C &mdash; Build Your Own Food Chain', '🎨 Part C &mdash; Draw Two Magnets')
fx('fix', '9.01 leftover (ticked): Part C task → the checklist’s two-magnet diagram (planned and sketched on the page)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Draw two bar magnets near each other. Label every pole N or S. Add arrows to show whether they attract or repel. Then flip one magnet in your head: what happens now?</p>', True)
fx('fix', '9.01 leftover (ticked): Reflect asked about a hawk; the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'supply list: what the games can use at home', r'<span class="need-chip"><span>✏️</span>Colored pencils</span>',
   '<span class="need-chip"><span>🧲</span>Optional: a fridge magnet</span><span class="need-chip"><span>📎</span>Optional: a paperclip, foil, a coin, a key</span>', True)

# ---------------------------------------------------------------- Part 1: poles (figure moved here; the wow is played, not told)
FIG = ('<div class="lesson-figure scroll-reveal">\n        <div class="lesson-figure-label">🧲 Two Magnets, Two Outcomes</div>\n        <img src="images/28-01-magnet-poles.png" alt="Two side-by-side diagrams. Left: two bar magnets with opposite poles facing (N to S) pull together. Right: two bar magnets with the same poles facing (N to N) push apart." />\n'
       '        <div class="lesson-figure-caption"><strong>The rule never changes:</strong> N + S = pull together. N + N or S + S = push apart.</div>\n      </div>\n\n      ')
fx('plain', 'Part 1: the snap-in-half fact is now the wow, so the page asks instead of telling; no dash; the poles picture moves up to the poles paragraph',
   ' — a NORTH pole and a SOUTH pole. These poles are ALWAYS in opposite ends of the magnet. If you break a magnet in half, each piece becomes a smaller magnet with its own north AND south pole.</p>',
   ': a NORTH pole and a SOUTH pole, always at opposite ends. So what happens if you snap a magnet in half? You’ll find out below.</p>\n      ' + FIG)
fx('plain', 'Part 1: a lead-in for the worn-label game', '(N + N = push apart; S + S = push apart).</p>',
   '(N + N = push apart; S + S = push apart).</p>\n      <p>Scientists use this rule to find a pole they can’t see. Try it on a magnet whose letters wore off.</p>')
fx('cut', 'lean: the Stop & Think (flip one magnet) is played by the worn-label game',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)

# ---------------------------------------------------------------- Part 2: magnetic or not (the sweeper plays the list; the compass line keeps quiz Q3 taught)
fx('plain', 'Part 2: the answer list becomes the sweeper game; the magnetic field line stays, with the compass (ticked compass wording) so quiz Q3 is taught on the page; the fridge line is kept short; the misconception is played by the sweeper; the poles picture moved to Part 1',
   r'<ul style="font-size:16px;color:#2B1D12;line-height:1\.7;margin:10px 0 12px 24px;">\s*<li><strong>Magnetic \(a magnet pulls\):</strong>.*?</div>\s*</div>\s*(?=<div style="background:#FFF6E5)',
   '<p>So is every metal magnetic? Sweep the tray and see.</p>\n\n      <p>That’s why a magnet sticks to your fridge door (steel) but not to a soda can (aluminum).</p>\n\n'
   '      ' + H3 + 'Part 3 · The Invisible Pull Zone</h3>\n      <p>The invisible pull zone around a magnet is its ' + VT('magnetic field', 'Magnetic field', 'Invisible area of pull or push.') + '. Earth itself is a giant magnet! A compass needle is a tiny magnet, so Earth’s magnetic field turns it to point toward Earth’s magnetic north, near the North Pole.</p>\n\n      ', True)
fx('plain', 'Part 2: no dash', '</span></span> — mainly iron, nickel, and most kinds of steel.</p>', '</span></span>: mainly iron, nickel and most kinds of steel.</p>')
fx('cut', 'lean: Key Concept (the games teach it)',
   r'<div style="background:#FFF6E5;border:2\.5px solid #F0C97A;[^>]*>\s*<div[^>]*>⭐ Key Concept</div>.*?</p>\s*</div>\s*', '', True)
fx('cut', 'lean: the Four Magnet Tests tap diagram is replaced by the sweeper; with it go Observe & Reason (Part B question 5 asks the same), the compass Amazing Fact (its idea is now a sentence in Part 2), the sea-turtle Florida connection and the Where does magnetism come from Go Deeper',
   r'<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">Four Magnet Tests</h3>.*?(?=<div class="tab-next-wrap">)', '', True)

# ---------------------------------------------------------------- Word Wall: no dashes (same meanings)
fx('plain', 'Word Wall: no dash', 'An object that can pull (attract) certain metals — and that has two ends that push or pull on other magnets.', 'An object that can pull (attract) certain metals. Its two ends push or pull on other magnets.')
fx('plain', 'Word Wall: no dash', 'Two of the same poles (N+N or S+S) repel each other — they push away.', 'Two of the same poles (N+N or S+S) repel each other. They push away.')
fx('plain', 'shorter; no dashes', r"<p>Hold this question in your head as you work\. By the end of the lesson.*?</p>",
   "<p>Keep this question in mind. By the end, you’ll predict whether a magnet will attract, repel or do nothing, and explain why.</p>", True)
fx('plain', 'cut filler; no dash', r"<p>These six words show up all through the lesson\. <strong>Tap a card to flip it</strong>.*?</p>",
   "<p><strong>Tap a card to flip it</strong> and read what the word means.</p>", True)

# ---------------------------------------------------------------- Part 4 = the old Explore
fx('cut', 'Part 4 = the old Explore (Magnet Treasure Hunt → the full prediction chart, the plan’s product); the next button goes to Self-Check',
   '''<div class="tab-next-wrap">
        <button class="tab-next-btn" onclick="switchTab('explore')">Continue to 🔬 Explore →</button>''',
   H3 + 'Part 4 · The Magnet Treasure Hunt</h3>\n      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">Scientists predict BEFORE they test. Fill in the whole prediction chart first: will a magnet stick to each thing? Lock it in. Then test every row.</p>\n  <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>')
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its predict-test-sort steps live on as the prediction chart; the MRI Amazing Fact, the Think like a scientist and the Electromagnets Go Deeper go with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)

# ---------------------------------------------------------------- Assignment
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('plain', 'Part B question 5 no longer points at the cut diagram', 'Pick ONE object from the diagram (paperclip, soda can, another magnet, wooden block).', 'Pick ONE object: a paperclip, a soda can, another magnet or a wooden block.')
fx('plain', 'Part B question 5 label (Gathered Answers)', 'data-label="Pick ONE object from the diagram (paperclip, soda ..."', 'data-label="One object: attract, repel or ignore, and why"')
fx('plain', 'Part B question 6 label (Gathered Answers)', 'data-label="Two bar magnets snap together. Then someone flips ..."', 'data-label="One magnet flipped: what changed about the poles?"')
fx('cut', 'lean: Part B question 7 removed (Bethany kept 5 and 6; the CER asks the same “all metal” question)', r'<div class="pq">\s*<span class="pq-num"[^>]*>7</span>.*?</textarea>\s*', '', True)
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C checklist ends with the required sketch', 'A two-magnet diagram with poles labeled and an arrow showing whether they attract or repel.',
   'My plan: which poles face, what they do, why, and what a flip changes. Plus your labeled sketch.')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether magnets stick to all metal, supported with two pieces of evidence.',
   '<strong>Use Your Evidence:</strong> My claim about whether magnets stick to all metal, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a 9.01 leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Download your field journal (it has your answers and your sketch) and upload it to the Canvas assignment. Or copy your Gathered Answers (above) into Canvas.', True)
fx('plain', 'closing: shorter; tells what next lesson does', 'Next lesson, you\'ll run a real systematic test on a bunch of materials and back up your findings with data.',
   'Next lesson: a real fair test, with a data table to prove which materials are magnetic.')

# ---------------------------------------------------------------- the story
PRIYA = O['crew']['priya']
LOST = [  # (id, icon, item, made of, where, how, why, miss)
    ('keys', '🔑', 'Boathouse key on a key ring', 'brass key, steel ring', 'off the end of the dock', 'magnet',
     'The key is brass, but the ring is steel. The magnet grabs the ring and the key comes along.', 'Look at the ring, not just the key. What is the ring made of?'),
    ('tag', '🏷️', 'Duck race number tag', 'aluminum', 'by the boat ramp', 'net',
     'Aluminum is a metal, but it isn’t magnetic. The net scoops it up.', 'Aluminum is metal, but remember the soda can in the Warm-Up. Did it stick?'),
    ('ring', '💍', 'A gold ring', 'gold', 'near the snack stand', 'net',
     'Gold isn’t magnetic. Only the net can bring it up.', 'Gold stayed on the sweeper tray. A magnet ignores it.'),
    ('wrench', '🔧', 'Wrench from the tackle box', 'steel', 'under the dock', 'magnet',
     'Steel is magnetic. CLANK! It rides right up on the magnet.', 'Steel is one of the magnetic metals. Which tool will it stick to?'),
    ('penny', '🪙', 'A penny', 'zinc coated with copper', 'off the end of the dock', 'net',
     'Pennies are zinc and copper. Neither one is magnetic, so the net it is.', 'The penny stayed on the sweeper tray. Will a magnet grab it now?'),
]
D = {
    'lesson': '28.01', 'week': 28, 'day': 1, 'guide': 'priya', 'prefix': 'g4sci-28-1', 'manifestKey': '28-01',
    'paths': P['paths'], 'crew': {'priya': PRIYA},
    'expedition': {'num': 28, 'title': 'Magnet Fishing Day'},
    'ambient': {'icon': '🦆', 'label': 'The pond at Palmetto Springs'},
    'case': {
        'num': 28, 'title': 'Magnet Fishing Day', 'style': 'order',
        'hook': 'Dr. Priya Nair here. The Duck Derby is over, and the pond needs a cleanup! Five things fell off the dock. My team has a magnet on a rope and a long net. But our two magnets keep pushing each other away. Can you help?',
        'lostlog': {'head': 'PALMETTO SPRINGS PARK', 'title': 'Ranger’s lost-item log · after the Duck Derby', 'cols': ['Lost item', 'Made of', 'Where it fell'],
                    'rows': [[r[1] + ' ' + r[2], r[3], r[4]] for r in LOST], 'sign': 'Ranger Bell',
                    'kit': {'label': '🧰 The magnet kit', 't': 'We tried to stack our two magnets to make one stronger magnet. They keep pushing apart!'}},
        'stills': [],
        'question': 'Which lost items can the magnet bring up, which need the net, and how should the team stack its two magnets?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'fishing', 'icon': '🎣', 'where': 'Warm-Up: magnet fishing', 't': 'Only things with iron or steel in them clanked onto the magnet, even under water. The soda can and the fishing weight are metal, and they stayed in the mud.'},
            {'id': 'poles', 'icon': '🧲', 'where': 'The Lesson, Part 1: the worn-label magnet', 't': 'Same poles push apart. Opposite poles pull together. Flip one magnet and a push becomes a pull.'},
            {'id': 'sweeper', 'icon': '🪄', 'where': 'The Lesson, Part 2: the magnet sweeper', 't': 'Not all metal is magnetic. Foil, a penny, a gold ring, a brass key and copper wire all stayed on the tray.'},
            {'id': 'predchart', 'icon': '📋', 'where': 'The Lesson, Part 4: the prediction chart', 't': 'Magnets attract things made of iron, nickel or steel. If one part is steel, like a steel key ring, the whole thing can come up.'},
        ],
        'solve': {
            'title': 'Magnet or net?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Everything on the list is metal, so the magnet brings it all up. Stack the magnets any way.', 'why': 'Check Clues 1 and 3. Aluminum, gold, copper and zinc are metals, but a magnet ignores them. And check Clue 2 about stacking.'},
                {'t': 'Only the wrench comes up, because the key is brass. Push the magnets together harder.', 'why': 'Check Clue 4: the key hangs on a STEEL ring. And Clue 2: pushing harder won’t beat two same poles.'},
                {'t': 'The magnet brings up the key ring and the wrench. The tag, the gold ring and the penny need the net. Flip one magnet so N faces S.', 'right': True,
                 'why': 'Case cracked! Steel comes up on the magnet, the other metals go in the net, and opposite poles snap the two magnets together.'},
                {'t': 'Nothing comes up. Water blocks a magnet’s pull, so use the net for everything.', 'why': 'Check Clue 1. The bottle cap, the hook and the bolt clanked on right through the water.'},
            ]},
    },
    'fishing': {
        'afterText': 'Then reel it up and see.', 'kicker': 'Warm-Up game', 'title': 'Cast and reel',
        'why': {'icon': '🎣', 'q': 'What is magnet fishing?', 't': 'People drop a strong magnet on a rope to clean lost metal out of ponds and canals. Real magnet fishing needs an adult: sharp or rusty things can come up.'},
        'todo': ['Drag the magnet onto a muddy shape, or tap the shape.', 'Tap your guess: Clank! or Nothing.', 'Reel it up. Six casts in all.'],
        'alt': 'A model of the dock over the pond. Six muddy shapes lie on the bottom.',
        'model': 'A model pond. Real magnet fishing needs an adult.',
        'magWord': 'The magnet on its rope',
        'items': [
            {'id': 'cap', 'icon': '🍾', 't': 'Bottle cap', 'made': 'steel', 'mag': True, 'line': 'CLANK! Bottle caps are made of thin steel, and steel is magnetic.'},
            {'id': 'can', 'icon': '🥫', 't': 'Soda can', 'made': 'aluminum', 'mag': False, 'line': 'Nothing. A soda can is metal, but aluminum isn’t magnetic. It stayed in the mud.'},
            {'id': 'hook', 'icon': '🪝', 't': 'Fishing hook', 'made': 'steel', 'mag': True, 'line': 'CLANK! A steel fishing hook. (Careful: it’s sharp!)'},
            {'id': 'duck', 'icon': '🦆', 't': 'Rubber derby duck', 'made': 'rubber', 'mag': False, 'line': 'Nothing. Rubber has no iron in it. A lost derby duck needs the net.'},
            {'id': 'weight', 'icon': '⚓', 't': 'Fishing weight', 'made': 'lead', 'mag': False, 'line': 'Nothing! It’s heavy metal, but lead isn’t magnetic. Heavy doesn’t mean magnetic.'},
            {'id': 'bolt', 'icon': '🔩', 't': 'Rusty bolt', 'made': 'iron', 'mag': True, 'line': 'CLANK! Rust and all, iron is magnetic. The pull worked right through the water.'},
        ],
        'guessQ': 'Your guess: will something clank onto the magnet?', 'yesWord': '🧲 Clank! It sticks', 'noWord': '💨 Nothing sticks', 'reelBtn': '🎣 Reel it up',
        'haulLabel': 'The haul', 'cols': ['Found', 'Made of', 'Came up?'], 'upWord': 'Stuck to the magnet', 'downWord': 'Stayed in the mud', 'rightWord': 'you called it', 'wrongWord': 'surprise!',
        'countWord': 'casts',
        'q': 'Look at your haul. What did everything that clanked onto the magnet have in common?',
        'opts': [{'t': 'It was all made of iron or steel.', 'ok': True},
                 {'t': 'It was all metal.', 'miss': 'Check the soda can and the fishing weight. Both are metal, and both stayed in the mud.'},
                 {'t': 'It was the heaviest stuff.', 'miss': 'The lead weight was heavy, and it stayed down. The bottle cap is light, and it came up.'}],
        'win': 'Iron and steel came up, even through the water. Other metals stayed down. Clue 1!', 'clue': 'fishing'},
    'poles': {
        'afterText': 'Try it on a magnet whose letters wore off.', 'kicker': 'Part 1 game', 'title': 'The worn-label magnet',
        'why': {'icon': '🖌️', 'q': 'Why are the letters gone?', 't': 'The team’s third magnet lived in a wet tackle box, and the N and S paint wore off. A test magnet with clear letters can find them.'},
        'todo': ['Pick which pole of the test magnet faces down (Flip it).', 'Drag the test magnet to an end, or tap the end. Watch: pull or push?', 'Paint the right letter on each end. Then snap it in half!'],
        'model': 'A model test. Try it with two fridge magnets.',
        'ends': {'a': 'N', 'd': 'S'}, 'newEnds': {'b': 'S', 'c': 'N'},
        'endNames': {'a': 'Left end', 'b': 'Middle-left end', 'c': 'Middle-right end', 'd': 'Right end'},
        'tmWord': 'Test magnet', 'flipBtn': '🔄 Flip the test magnet (facing down now: {f})',
        'testLabel': 'Bring the test magnet to an end (drag it there, or tap the end):',
        'pullWord': 'SNAP! It pulls together', 'pushWord': 'It scoots away!', 'pullShort': 'pulled together', 'pushShort': 'pushed apart',
        'logLabel': 'My test log', 'colEnd': 'End', 'colFace': 'I brought my…', 'colWhat': 'What happened',
        'paintQ': 'Paint the {e}: which pole is it?',
        'paintMiss': {'pull': 'Your {f} pole PULLED. Opposite poles pull together. So this end is the opposite of {f}.', 'push': 'Your {f} pole PUSHED it away. Same poles push apart. So this end is…'},
        'nextLine': 'Now test the other end.',
        'snapAsk': 'Now the wow. Snap this magnet in half. Will you get one N piece and one S piece?', 'snapBtn': '💥 Snap it in half',
        'snapLine': 'Two NEW ends appeared in the middle. Test each one, then paint it.',
        'doneLine': 'Each half got its own N AND its own S. Snap a magnet and you get two smaller magnets!',
        'q': 'You snapped a magnet in half. What did you get?',
        'opts': [{'t': 'Two smaller magnets, each with its own N and S.', 'ok': True},
                 {'t': 'One N piece and one S piece.', 'miss': 'Check your painted ends. The left half has an N AND an S.'},
                 {'t': 'Two pieces that aren’t magnets anymore.', 'miss': 'Look at your test log. The new ends still pushed and pulled.'}],
        'win': 'Same poles push, opposite poles pull, and every magnet has both. Clue 2!', 'clue': 'poles'},
    'sweeper': {
        'afterText': 'Sweep the tray and see.', 'kicker': 'Part 2 game', 'title': 'The magnet sweeper',
        'why': {'icon': '🪄', 'q': 'What is a magnet sweeper?', 't': 'A magnet on a stick. Workers sweep it over floors and parking lots to pick up lost nails and screws.'},
        'todo': ['Drag the magnet wand slowly over the tray. (Or tap a thing to sweep it.)', 'Watch what jumps up and clings.', 'Sweep all 8. Read the made-of tags.'],
        'model': 'A model tray. Try it at home with a fridge magnet.',
        'items': [
            {'id': 'clip', 'icon': '📎', 't': 'Paperclip', 'made': 'steel', 'mag': True, 'line': 'Paperclips are steel wire. Steel is magnetic.'},
            {'id': 'foil', 'icon': '✨', 't': 'Foil ball', 'made': 'aluminum', 'mag': False, 'line': 'Shiny and metal, but aluminum isn’t magnetic.'},
            {'id': 'nail', 'icon': '🔩', 't': 'Iron nail', 'made': 'iron', 'mag': True, 'line': 'Iron is THE magnetic metal.'},
            {'id': 'penny', 'icon': '🪙', 't': 'Penny', 'made': 'zinc + copper', 'mag': False, 'line': 'A penny is zinc coated with copper. Neither is magnetic.'},
            {'id': 'gold', 'icon': '💍', 't': 'Gold ring', 'made': 'gold', 'mag': False, 'line': 'Gold is a metal, and a magnet ignores it completely.'},
            {'id': 'cap', 'icon': '🍾', 't': 'Bottle cap', 'made': 'steel', 'mag': True, 'line': 'Thin steel. Up it goes!'},
            {'id': 'key', 'icon': '🗝️', 't': 'Brass key', 'made': 'brass', 'mag': False, 'line': 'Brass is copper mixed with zinc. Not magnetic.'},
            {'id': 'wire', 'icon': '➰', 't': 'Copper wire', 'made': 'copper', 'mag': False, 'line': 'Copper carries electricity well, but it isn’t magnetic.'},
        ],
        'cling': 'jumped up and clung on!', 'stay': 'stayed put.', 'countWord': 'things swept',
        'jarLine': 'The wand held {n} things. The other five are metal too, and they stayed on the tray.',
        'q': 'Foil, a penny, a gold ring, a brass key and copper wire are all metal. They all stayed put. So…',
        'opts': [{'t': 'Only some metals are magnetic: iron, nickel and steel.', 'ok': True},
                 {'t': 'The magnet was too weak.', 'miss': 'The same magnet picked up the nail, the paperclip and the cap. It’s strong enough.'},
                 {'t': 'Shiny things are never magnetic.', 'miss': 'The steel bottle cap is shiny, and it clung to the wand.'}],
        'win': 'Not all metal is magnetic. Clue 3!', 'clue': 'sweeper'},
    'predchart': {
        'afterText': 'Then test every row.', 'kicker': 'Part 4 game', 'title': 'The full prediction chart',
        'why': {'icon': '📋', 'q': 'Why predict the whole chart first?', 't': 'If you test first, you can’t change your mind and pretend you knew. A locked chart shows what you really thought.'},
        'todo': ['Tap Yes or No for all 8 things.', 'Lock your chart.', 'Drag the magnet onto each row (or press Test it). Then finish the rule.'],
        'chartLabel': 'My prediction chart',
        'items': [
            {'id': 'binder', 'icon': '🗂️', 't': 'Binder clip', 'mag': True, 'line': 'Binder clips are steel. It snapped right on.'},
            {'id': 'pencil', 'icon': '✏️', 't': 'Wooden pencil', 'mag': False, 'line': 'Wood and pencil lead have no iron in them.'},
            {'id': 'keyring', 'icon': '🔑', 't': 'Brass key on a steel ring', 'mag': True, 'line': 'The key is brass, but the RING is steel. The magnet grabbed the ring, and the key came along.'},
            {'id': 'band', 'icon': '➰', 't': 'Rubber band', 'mag': False, 'line': 'Rubber isn’t magnetic.'},
            {'id': 'nickel', 'icon': '🪙', 't': 'A nickel (5-cent coin)', 'mag': False, 'line': 'Surprise! A U.S. nickel is mostly copper, so a magnet ignores it.'},
            {'id': 'pin', 'icon': '🧷', 't': 'Safety pin', 'mag': True, 'line': 'A steel safety pin. It jumped to the magnet.'},
            {'id': 'pan', 'icon': '🥧', 't': 'Aluminum pie pan', 'mag': False, 'line': 'Metal, but aluminum. The magnet slid right off.'},
            {'id': 'marble', 'icon': '🔮', 't': 'Glass marble', 'mag': False, 'line': 'Glass isn’t magnetic.'},
        ],
        'cols': ['Thing', 'My prediction', 'Result', ''], 'yes': 'Yes, it sticks', 'no': 'No', 'lockBtn': '🔒 Lock my chart', 'lockNeed': '{n} predictions to go',
        'testBtn': '🧲 Test it', 'magWord': 'Drag me onto a row', 'yesRes': 'it sticks!', 'noRes': 'it doesn’t stick.', 'yesShort': 'Sticks', 'noShort': 'Doesn’t stick',
        'scoreLine': '{r} of {n} predictions were right. The circled ones are where you learned something new!',
        'ruleQ': 'Finish the rule: Magnets attract things made of…',
        'ruleOpts': [{'t': 'iron, nickel or steel', 'ok': True, 'fill': 'Magnets attract things made of iron, nickel or steel.'},
                     {'t': 'any metal', 'miss': 'Check the pie pan and the nickel coin. Both are metal. Did they stick?'},
                     {'t': 'shiny things', 'miss': 'The marble and the pie pan are shiny. Did they stick?'}],
        'q': 'The key ring stuck, but the key is brass. Why did the key come along?',
        'opts': [{'t': 'The ring is steel. The magnet pulled the ring, and the key hung on.', 'ok': True},
                 {'t': 'Brass is magnetic after all.', 'miss': 'The brass key on the sweeper tray stayed put.'},
                 {'t': 'Keys are always magnetic.', 'miss': 'Look at the made-of line: the key is brass. What is the ring made of?'}],
        'win': 'Iron, nickel and steel. And one steel part can bring a whole thing up. Clue 4!', 'clue': 'predchart'},
    'exploreMod': 'predchart',
    'cleanup': {
        'after': '.fs-solve', 'kicker': 'Case closed', 'title': 'Stamp the cleanup report', 'lockLine': 'Crack the case first.',
        'todo': ['Stamp MAGNET or NET on each lost item.', 'Then stamp the report CLOSED.'],
        'head': 'Palmetto Springs Park · cleanup report', 'sub': 'Bring each lost item up with the right tool.',
        'rows': [{'id': r[0], 'icon': r[1], 't': r[2] + ' (' + r[3] + ')', 'how': r[5], 'why': r[6], 'miss': r[7]} for r in LOST] +
                [{'id': 'stack', 'icon': '🧲', 't': 'Stacking the two magnets: flip one so N faces S', 'how': 'magnet', 'why': 'Opposite poles pull together, so the stack holds. One stronger magnet!', 'miss': 'This one is about the magnets themselves. Flipping one makes them pull together.'}],
        'magWord': '🧲 MAGNET', 'netWord': '🥅 NET', 'stampBtn': '🖋️ Stamp it CLOSED', 'stamp': 'CLOSED', 'sign': 'Ranger Bell',
        'win': 'Report closed. Every lost item has the right tool. Now open the tackle box…'},
    'compasstwist': {
        'after': '.fs-solve', 'kicker': 'Case closed · a twist', 'title': 'The compass in the tackle box', 'lockLine': 'Crack the case first.',
        'why': {'icon': '🧭', 'q': 'What happened?', 't': 'Ranger Bell opened the tackle box to put the magnets away. The compass inside started spinning!'},
        'todo': ['Slide the magnet close to the compass. Watch the red end of the needle.', 'Flip the magnet and slide it close again.', 'Slide it away. Where does the needle point now?'],
        'model': 'A model compass. The red end of the needle is its north end.',
        'slideLabel': 'Slide the magnet closer', 'flipBtn': '🔄 Flip the magnet (its {f} end faces the compass now)',
        'nearLine': {'N': 'The magnet’s N end pushed the needle’s red north end AWAY. Same poles push!', 'S': 'Flipped: the S end pulled the red north end straight toward it. Opposite poles pull!'},
        'farLine': 'Magnet gone: the needle swings back and points north again.',
        'q': 'Why did the compass needle swing?',
        'opts': [{'t': 'The needle is a tiny magnet. The big magnet’s poles pushed and pulled it.', 'ok': True},
                 {'t': 'The compass broke.', 'miss': 'Slide the magnet away. Does the needle go back to north? Then it isn’t broken.'},
                 {'t': 'A compass always points at the closest metal.', 'miss': 'It pointed north before the magnet came close. And remember: not all metal is magnetic.'}],
        'fact': {'q': 'So why does a compass point north?', 't': 'Earth itself is a giant magnet. With no magnet nearby, Earth’s magnetic field turns the needle to point toward Earth’s magnetic north, near the North Pole. That’s why Ranger Bell keeps the compass away from the magnets!'},
        'win': 'A compass is a magnet too. Keep it away from the magnet kit!'},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Snapping together is for OPPOSITE poles. What did your N pole do to an N end?', 'B': 'Same poles push hard. Remember the end that scooted away?'},
        'q2': {'A': 'Plastic has no iron in it. Like the rubber duck, it stays put.', 'C': 'Aluminum is metal, but the soda can stayed in the mud.'},
        'q3': {'B': 'Both ends weigh the same. Reread the compass sentence in Part 2.', 'C': 'The Sun doesn’t pull on a compass. Reread the compass sentence in Part 2.'}},
    'flags': {
        'ans-1': [
            {'label': 'your object', 're': 'paper ?clip|clip|soda|can|magnet|wood|block'},
            {'label': 'attract, repel or ignore', 're': 'attract|stick|pull|repel|push|ignore|nothing|won.?t|doesn.?t|not'},
            {'label': 'why', 're': 'because|steel|iron|aluminum|alumin|wood|pole|magnetic|not magnetic|metal|same|opposite|since'}],
        'ans-2': [
            {'label': 'the poles', 're': 'pole|north|south|\\bn\\b|\\bs\\b|end'},
            {'label': 'same or opposite', 're': 'same|opposite|match|alike|differ|switch|flip|turn'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|wrong|right|true|not true|false|not all|only some'},
            {'label': 'two pieces of evidence', 'any': ['foil', 'aluminum', 'penny', 'gold', 'brass', 'copper', 'can', 'nickel', 'pie pan', 'weight', 'lead', 'sweeper', 'tray', 'steel', 'iron', 'paperclip', 'cap', 'nail', 'hook', 'chart', 'stayed'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-1': 12, 'ans-2': 10, 'cer-4': 30},
    'hints': {
        'ans-1': ['Pick one: a paperclip, a soda can, another magnet or a wooden block.', 'What is it made of? Is that one of the magnetic metals? For another magnet, which poles face?', 'Try: A magnet will ___ the ___ because it is made of ___.'],
        'ans-2': ['Think about the worn-label magnet. What did flipping the test magnet do?', 'Before the flip, which poles faced each other? After the flip?', 'Try: At first, opposite poles faced, so they ___. After the flip, ___ poles faced, so they ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'Foil, a penny, a gold ring, a brass key and copper wire are metal, but they stayed on the sweeper tray.',
                'The aluminum soda can and the lead fishing weight stayed in the mud. The steel bottle cap came up.',
                'A nickel coin is metal, but it did not stick in the prediction chart.',
                'Magnets are really strong.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'photos': [
        {'id': 'filings', 'afterText': 'near the North Pole.', 'kicker': 'Part 3 · a real photo', 'short': 'Iron filings show the field',
         'title': 'See the invisible field', 'todo': ['Tap each number on the photo.', 'Then match each fact to its number.'],
         'why': {'icon': '🔬', 'q': 'What are we looking at?', 't': 'A real photo from a 1913 science book. Paper sits on top of a bar magnet, and tiny iron bits called filings were sprinkled on it. Each filing turned to line up with the magnetic field.'},
         'img': 'images/28-01-iron-filings.jpg', 'alt': 'Black iron filings on white paper form curving lines that loop from one end of a hidden bar magnet, marked N, to the other end, marked S.',
         'credit': 'Newton Henry Black and Harvey N. Davis, Practical Physics (1913), fig. 200', 'license': 'public domain, via Wikimedia Commons',
         'hotspots': [
             {'n': 1, 'x': 22, 'y': 38, 'label': 'The N pole', 't': 'The north pole. The filings crowd in here and stick out like spikes: the pull is strongest at the ends.'},
             {'n': 2, 'x': 76, 'y': 38, 'label': 'The S pole', 't': 'The south pole. Just as crowded as the N end. Both poles pull iron equally hard.'},
             {'n': 3, 'x': 50, 'y': 14, 'label': 'Curving lines', 't': 'The filings make lines that curve out from one pole and loop around to the other. Scientists call these field lines.'},
             {'n': 4, 'x': 46, 'y': 49, 'label': 'The quiet middle', 't': 'Along the middle of the magnet, the filings lie flat and calm. The pull is weakest here.'}],
         'task': {'q': 'Match it: which number shows each fact?',
                  'items': [
                      {'icon': '💪', 'step': 'The north end, where the pull is strongest', 'ans': 1, 'evid': 'Filings crowd and stand up at the poles, where the pull is strongest.', 'miss': 'Find the end marked N. The filings crowd together there.'},
                      {'icon': '🌀', 'step': 'The field loops from one pole to the other', 'ans': 3, 'evid': 'Field lines curve from pole to pole.', 'miss': 'Find the long curving lines above the magnet.'},
                      {'icon': '😴', 'step': 'The pull is weakest here', 'ans': 4, 'evid': 'The middle of a bar magnet pulls the least.', 'miss': 'Look between the two poles.'}],
                  'win': 'You just saw a magnetic field: invisible, but iron filings can draw it.'}}],
    'tool': {
        'name': 'Magnetic field viewer', 'icon': '🧲', 'tab': 'assignment', 'after': '#tab-assignment .activity-card', 'key': '28-tool', 'sim': 'fieldviewer',
        'kicker': 'Bonus · Tool of the Week', 'teaser': 'Sprinkle iron filings over one magnet, a pulling pair and a pushing pair.',
        'done': 'Tool of the Week: you saw three magnetic fields.',
        'why': {'icon': '🧲', 'q': 'What is a field viewer?', 't': 'Scientists sprinkle iron filings, or use a special green film, to see a magnetic field that is invisible to our eyes.'},
        'fieldviewer': {
            'title': 'Sprinkle and see', 'todo': ['Pick a setup.', 'Press Sprinkle and watch the filings line up.', 'Try all three, then answer the question.'],
            'model': 'A model: each little line is a filing, turned the way the magnetic field points.',
            'sprinkleBtn': '🧂 Sprinkle the iron filings',
            'setups': [
                {'k': 'one', 'icon': '1️⃣', 't': 'One magnet', 'mags': [[240, False]], 'note': 'Lines loop from the N end around to the S end, like the 1913 photo.'},
                {'k': 'pull', 'icon': '🤝', 't': 'N faces S', 'mags': [[150, False], [330, False]], 'note': 'Opposite poles: the lines run straight across the gap, from one magnet into the other. That’s a pull.'},
                {'k': 'push', 'icon': '↔️', 't': 'N faces N', 'mags': [[150, False], [330, True]], 'note': 'Same poles: the lines bend AWAY from each other and leave an empty spot in the gap. That’s a push.'}],
            'q': {'q': 'In which setup do the lines bend away and leave an empty spot between the magnets?',
                  'opts': [{'t': 'N faces N', 'ok': True, 'why': 'Same poles push apart, and you can see it: the field lines turn away from each other.'},
                           {'t': 'N faces S', 'why': 'Look again: here the lines run straight across the gap.'},
                           {'t': 'One magnet', 'why': 'With one magnet there is no gap. Try the N faces N setup.'}]}}},
    'slots': {
        'welcome': {'label': 'Welcome · Magnet Fishing Day', 'length': '40–50 s'},
        'warmup': {'label': 'Warm-Up · cast and reel (Clue 1)', 'length': '15–20 s',
                   'script': 'Dr. Nair here, on the dock! Drag the magnet onto a muddy shape. Tap your guess: Clank, or Nothing. Then reel it up. Six casts. Watch the haul list. What do the clanks have in common?'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · the worn-label magnet (Clue 2)', 'length': '15–20 s',
                  'script': 'Our third magnet lost its letters. Flip the test magnet, then drag it to an end. Does it snap in, or scoot away? Check your test log, then paint the letter. Then, snap it in half!'},
        'part2': {'label': 'Part 2 · the magnet sweeper (Clue 3)', 'length': '15–20 s',
                  'script': 'Every thing on this tray is metal. Drag the magnet wand slowly across the tray. Some things jump up and cling. Some stay put. Read each made-of tag. Is every metal magnetic?'},
        'part3': {'label': 'Part 3 · the iron filings photo', 'length': '20–30 s'},
        'explore': {'label': 'Part 4 · the prediction chart (Clue 4)', 'length': '15–20 s',
                    'script': 'Predict every row first. Tap Yes or No for all eight. Then lock your chart. Now drag the magnet onto each row. Wrong guesses get circled. That is where the learning is. Then finish the rule.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · draw two magnets', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '15–20 s'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 28.02 (a fair test with a data table).'},
    },
    'videoOff': [],
    'lensVoice': False,
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Your haul list with all 6 casts (Warm-Up)',
        'The snapped magnet with all 4 ends painted (The Lesson)',
        'The magnet wand holding its catch (The Lesson)',
        'Your locked prediction chart, all tested (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['Your best catch from the pond', 'The snapped magnet with its four ends', 'A compass near a magnet'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · draw and label your two magnets', 'required': True, 'minLabels': 4,
                           'prompts': ['Draw two bar magnets', 'Label every pole N or S', 'Add arrows: pull together or push apart', 'Write “attract” or “repel”']}]},
    'hlCoach': copy.deepcopy(O['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🎣', 'name': 'The rusty bolt from the pond',
                 'line': 'You cracked Case 28, and the rusty bolt from the pond goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next lesson: a real fair test of magnets!'},
    'notebookTitle': O['notebookTitle'],
    'notebook': copy.deepcopy(Q['notebook']) + [{'lesson': '28.01', 'icon': '🎣', 'name': 'The rusty bolt from the pond'}],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are sorted. Nice magnet work!',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to see what it means.']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '#tab-vocab p', 'text': 'Then reel it up and see.'},
         'label': 'Warm-Up: magnet fishing', 'q': 'Warm-Up: what came up, what stayed down, and my idea why.', 'title': 'My haul', 'compact': True,
         'fields': [{'t': 'What came up', 'icon': '🧲', 'ph': 'The magnet pulled up ___.'},
                    {'t': 'What stayed down', 'icon': '💨', 'ph': '___ stayed in the mud.'},
                    {'t': 'My idea why', 'icon': '💡', 'ph': 'I think the magnet only pulls ___.'}]},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Then flip one magnet in your head'},
         'label': 'Part C: draw two magnets', 'q': 'Part C: which poles face, what they do, why, and what a flip changes.', 'title': 'My two-magnet plan',
         'fields': [{'t': 'The poles that face each other', 'icon': '🧲', 'ph': 'The ___ pole faces the ___ pole.'},
                    {'t': 'What they do', 'icon': '↔️', 'ph': 'They attract / repel.'},
                    {'t': 'Why (use the rule)', 'icon': '📏', 'ph': 'They ___ because ___ poles ___.'},
                    {'t': 'If I flip one magnet', 'icon': '🔄', 'ph': 'Then the ___ pole faces the ___ pole, so they ___.', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Do magnets stick to all metal?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-1': 'Part B · Question 5', 'ans-2': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'Opposite poles pull together, same poles push apart, and magnets only attract iron, nickel and steel.',
    'key': ['opposite', 'same', 'iron', 'nickel', 'steel'],
    'small': ['and', 'only', 'pull', 'push'],
    'model': 'A scientist might highlight “opposite”, “same” and “iron, nickel and steel”. Those words hold the big idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this tell when a magnet pulls, when it pushes, or what it ignores?']

D['cues'] = {
    'warmup': [{'at': '^drag', 'sel': '.fs-fsh-mag', 'fx': 'point', 'scroll': True},
               {'at': '^muddy', 'sel': '.fs-fsh-stage', 'fx': 'glow'},
               {'at': '^guess', 'sel': '[data-mod="fishing"] .fs-todo li', 'i': 1, 'fx': 'trace'},
               {'at': '^reel', 'sel': '[data-mod="fishing"] .fs-todo li', 'i': 2, 'fx': 'trace'},
               {'at': '^haul', 'sel': '[data-mod="fishing"] .fs-count', 'fx': 'pop'}],
    'part1': [{'at': '^letters', 'sel': '.fs-pol-stage', 'fx': 'glow', 'scroll': True},
              {'at': '^flip', 'sel': '.fs-pol-flip', 'fx': 'point'},
              {'at': '^drag', 'sel': '.fs-pol-tm', 'fx': 'wiggle'},
              {'at': '^log', 'sel': '[data-mod="poles"] .fs-todo li', 'i': 2, 'fx': 'trace'},
              {'at': '^snap', 'sel': '[data-mod="poles"] .fs-game-t', 'fx': 'pop', 'i': 0}],
    'part2': [{'at': '^tray', 'sel': '.fs-swp-tray', 'fx': 'glow', 'scroll': True},
              {'at': '^wand', 'sel': '.fs-swp-wand', 'fx': 'point'},
              {'at': '^cling', 'sel': '[data-mod="sweeper"] .fs-todo li', 'i': 1, 'fx': 'trace'},
              {'at': '^tag', 'sel': '[data-mod="sweeper"] .fs-todo li', 'i': 2, 'fx': 'trace'}],
    'explore': [{'at': '^predict', 'sel': '.fs-pch', 'fx': 'glow', 'scroll': True},
                {'at': '^lock', 'sel': '.fs-pch-lock', 'fx': 'point'},
                {'at': '^drag', 'sel': '[data-mod="predchart"] .fs-todo li', 'i': 2, 'fx': 'trace'},
                {'at': '^circled', 'sel': '.fs-pch-mk', 'fx': 'pop', 'i': 0},
                {'at': '^rule', 'sel': '[data-mod="predchart"] .fs-game-t', 'fx': 'pop'}],
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
