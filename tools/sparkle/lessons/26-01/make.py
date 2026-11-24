#!/usr/bin/env python3
"""Writes data.json and fixes.json for 26.01 (run from this folder). Case 26 "The Duck Derby Flop" (Dr. Priya Nair's first lesson, Unit 6, Palmetto Springs pond):
a charity rubber-duck race rented a wave machine to push 200 ducks to the dock; they bobbed in place for an hour, and the organizer wants a BIGGER machine.
New: case.flyer (event flyer + rental receipt + letter), crowd (Warm-Up: be the crowd, track the red-cap fan), swapwave (Part 1: one wave, five mediums, tag a piece),
duckloop (the wow: the duck's small loop), brackets (Part 2: measure amplitude and wavelength with a bracket), shake (Part 3 = the old Explore: your hand makes the wave,
a cup tower), rivertwist + raceplan (after the case), SIMS.tuningfork (Tool of the Week: vibration and pitch, SC.4.P.10.3). SCRIPTS ONLY: clip scripts written and
budgeted, nothing generated."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
O = json.load(open('../25-02/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
PS = '<p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)
def I(n, ext='jpg'): return 'images/26-01-' + n + '.' + ext

# ---------------------------------------------------------------- labels (standing approval)
fx('fix', 'unit label: “Ecosystems & Energy” is a leftover; the plan puts Module 26 in “Energy, Motion, and Waves”', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Energy, Motion &amp; Waves</div>')
fx('fix', 'waves are physical science, not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standards label: the plan’s CPALMS code; TEKS is a Texas code that isn’t in the plan', '<div class="info-value">SC.4.P.10.3 · TEKS 4.8(B)</div>', '<div class="info-value">SC.4.P.10.3</div>')
fx('fix', 'quarter label: weeks 24 on are Q4 in the Canvas plan', '<div class="info-value">Q3 &middot; Week 26</div>', '<div class="info-value">Q4 &middot; Week 26</div>')
fx('fix', 'quarter label in the footer', 'Science &middot; Quarter 3 &middot; Student Lesson Page', 'Science &middot; Quarter 4 &middot; Student Lesson Page')

# ---------------------------------------------------------------- ticked fixes (Bethany, 24 Nov 2026)
fx('fix', '22.01 leftover: the Warm-Up title and subtitle named the toaster lesson', '<div class="act-title">🌅 Warm-Up: What Goes In, What Comes Out?</div>\n        <div class="act-subtitle">A familiar device, a hidden change</div>',
   '<div class="act-title">🌅 Warm-Up: Do the Wave!</div>\n        <div class="act-subtitle">What travels, and what stays?</div>')
fx('fix', '22.01 leftover: the toaster warm-up → the stadium wave',
   '<p>Think about a toaster. You drop in cold bread. A minute later, you pull out hot toast.</p>',
   '<p>Have you ever seen fans do “the wave” at a big game? A wave of people standing up races all the way around the stadium. Be the crowd, and keep your eye on the fan in the red cap.</p>')
fx('fix', '22.01 leftover: the toaster sketch → waves you have seen (answered on the page)',
   "<p>In your notebook, draw a quick sketch of a toaster. On one side, label what goes IN. On the other, label what comes OUT. (Hint: bread on both sides — but something invisible is also going in. What is it?)</p>",
   '<p>Now think about other waves you’ve seen. What wiggled, and what traveled?</p>')
fx('fix', '22.01 leftover: Notice & Wonder about the toaster',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Notice &amp; Wonder</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover: “energy can CONVERT … toasters” callout',
   r'<div class="callout callout-tip">\s*<span class="callout-icon">💡</span>\s*<p>Today you\'ll learn that energy can CONVERT.*?</p>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover (ticked): “Device” is in the plan row, but its meaning was about converting energy. Same word, a meaning for this lesson',
   'A tool or machine designed to do a job. Most devices convert energy from one form to another — a flashlight, a toaster, a fan are all devices.',
   'A tool or machine made to do a job, like a wave machine or a tuning fork.')
fx('fix', '22.01 leftover: the Stop & Reason asked about “the three devices above” (no devices on this page)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', '9.01 leftover: Part C was a food chain; the checklist already asks for a labeled wave diagram', '🎨 Part C &mdash; Build Your Own Food Chain', '🎨 Part C &mdash; My Wave Model')
fx('fix', '9.01 leftover: Part C task (now a wave the student made or saw, drawn and labeled on the sketch pad, + one amplitude and energy claim)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Make a wave at home with a jump rope, a string or a slinky. Or think of a wave you’ve seen in a pond, a pool or a bathtub. Draw it, label its parts and write one sentence about its amplitude and energy.</p>', True)
fx('fix', '9.01 leftover: Reflect asked about a hawk; the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'supply list: what Part C can use', r'<span class="need-chip"><span>✏️</span>Colored pencils</span>', '<span class="need-chip"><span>🪢</span>Optional: a jump rope, a string or a slinky</span>', True)
fx('fix', 'picture (ticked): the bottom panel’s “HIGH ENERGY” sample wave grows from small to tall inside one wave (mixed amplitudes). Show only the main labeled wave (cropped copy); the bracket game compares small and big amplitude. The original file stays.',
   'src="images/26-01-wave-anatomy.png"', 'src="images/26-01-wave-anatomy-main.png"')
fx('fix', 'picture alt text: matches the cropped picture (it shows the trough and the center line too)',
   'alt="A labeled wave diagram showing crest (peak), amplitude (peak height from center), and wavelength (peak-to-peak distance). An arrow shows the direction of energy travel through the medium."',
   'alt="A labeled wave on a center line: the crest (top), the trough (bottom), the amplitude (height from the center line to a crest) and the wavelength (crest to crest). A big arrow shows the energy traveling to the right."')
# (Part B question 5 wording, ticked, is moot: question 5 is cut; Bethany kept 6 and 7.)

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; plain words', r"<p>Hold this question in your head as you work\. By the end of the lesson.*?</p>",
   "<p>Keep this question in mind. By the end, you’ll measure a wave’s amplitude and wavelength and use models to show how a wave carries energy.</p>", True)
fx('plain', 'cut filler; no dash', r"<p>These six words show up all through the lesson\. <strong>Tap a card to flip it</strong>.*?</p>",
   "<p><strong>Tap a card to flip it</strong> and read what the word means.</p>", True)
fx('plain', 'Word Wall: no dash; “center line” and “crest” match the picture', 'How TALL the wave is — measured from the middle to a peak. Big amplitude = more energy.', 'How TALL a wave is, measured from the center line to a crest. Bigger amplitude means more energy.')
fx('plain', 'Word Wall: crest instead of peak (one word for one thing)', 'The distance from one peak of a wave to the next peak. Close peaks = short wavelength.', 'The distance from one crest (top) of a wave to the next crest. Close crests mean a short wavelength.')
fx('plain', 'Word Wall: no dash', 'The stuff a wave moves through — water, air, a rope, a slinky. The medium wiggles; the wave passes through.', 'The stuff a wave moves through, like water, air, a rope or a slinky. The medium wiggles; the wave passes through.')
fx('plain', 'Word Wall: no dash', 'The TOP of a wave — the highest point. The lowest point is called a trough.', 'The TOP of a wave, its highest point. The lowest point is called a trough.')
fx('plain', 'Part 1: no dash', 'The medium can be water, air, a rope, a slinky — anything that can wiggle.', 'The medium can be water, air, a rope or a slinky: anything that can wiggle.')
fx('plain', 'Part 1: no dashes (same idea)', 'The COILS don\'t travel — each one just wiggles in place — but the bump (the wave) moves the whole length.', 'The COILS don\'t travel. Each one just wiggles in place, but the bump (the wave) moves the whole length.')
fx('cut', 'lean: the Stop & Think (the pond leaf) is played in the duck wow and Self-Check Q1; a one-line lead-in to the Part 1 game instead',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*',
   '<p>Try it with five kinds of stuff. Tag one piece and send a wave.</p>\n\n      ', True)
fx('plain', 'Part 2: “peaks” → “crests” (the word the lesson teaches)', '<li><strong>Short wavelength</strong> → peaks are close together.</li>', '<li><strong>Short wavelength</strong> → crests are close together.</li>')
fx('plain', 'Part 2: “peaks” → “crests”', '<li><strong>Long wavelength</strong> → peaks are far apart.</li>', '<li><strong>Long wavelength</strong> → crests are far apart.</li>')
fx('cut', 'lean: the misconception paragraph repeats Part 1 (the five-mediums game and the duck’s loop let students meet it)',
   r"\s*<p><strong>Common misconception:</strong> Some people think waves CARRY the water.*?</p>", '', True)
fx('plain', 'caption matches the cropped picture; leads into the measuring game',
   '<div class="lesson-figure-caption"><strong>Every wave has the same parts.</strong> Amplitude is height (energy). Wavelength is peak-to-peak distance.</div>\n      </div>',
   '<div class="lesson-figure-caption"><strong>Every wave has the same parts.</strong> Amplitude is the height from the center line (energy). Wavelength is the distance from one crest to the next.</div>\n      </div>\n\n      <p>Now measure three waves on grid paper.</p>')
fx('plain', 'Science Connection: define “vibrates” and “pitch” where first seen (same meaning; this box teaches SC.4.P.10.3, so it stays)',
   '<p><strong>Science Connection:</strong> Sound is a wave made by vibrations. When an object vibrates fast, it makes a high pitch. When it vibrates slowly, it makes a low pitch.</p>',
   '<p><strong>Science Connection:</strong> Sound is a wave made by vibrations (fast back-and-forth shakes). When an object vibrates fast, it makes a high pitch (a high sound). When it vibrates slowly, it makes a low pitch.</p>')
fx('plain', 'Part B question 6 label (Gathered Answers)', 'data-label="An ocean storm wave is taller than a small ripple...."', 'data-label="Storm wave or ripple: which carries more energy?"')
fx('plain', 'Part B question 7 label (Gathered Answers)', 'data-label="Why is it accurate to say that &quot;the wave moves but..."', 'data-label="The wave moves but the water stays: why, and proof"')
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'closing: no dash; plain words (same meaning; the teaser for 26.02 Coded Messages is right)',
   ' Next lesson, we use what we know about waves to DESIGN — engineering coded message systems that send information using patterns.</p>',
   ' Next lesson: you’ll use patterns of light and sound to design your own code and send a secret message.</p>')

# ---------------------------------------------------------------- lean cuts
fx('cut', 'removed: Key Concept, the Four Kinds of Waves tap diagram (the five-mediums game replaces it; Part B question 5 that used it is cut), Observe & Reason, the Amazing Florida Fact (true, cut for length), the Florida connection callout (“rare tsunami warnings” is true but unclear; cut for length) and Go Deeper (radio waves cross empty space: true, beyond this lesson). The Stop & Reason was removed above (22.01 leftover).',
   r'\s*<div style="background:#FFF6E5;border:2\.5px solid #F0C97A;[^>]*>\s*<div[^>]*>⭐ Key Concept</div>.*?(?=<div class="callout callout-think scroll-reveal">)', '\n\n      ', True)
fx('cut', 'Part 3 = the old Explore (Slinky or Rope Wave → Shake It Yourself); the next button goes to Self-Check',
   '''<div class="tab-next-wrap">
        <button class="tab-next-btn" onclick="switchTab('explore')">Continue to 🔬 Explore →</button>''',
   H3 + 'Part 3 · Shake It Yourself</h3>\n      ' + PS + 'Picture a slinky stretched across the floor. A red ribbon is tied to one coil, and a tower of cups waits at the far end. Wiggle your end gently. Then wiggle it hard. Watch the ribbon and the cups.</p>\n  <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>')
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its slinky test is now Part 3 and Part C’s home wave; its tsunami fact (true: wavelengths can top 60 miles), Think like a scientist and Go Deeper (light is a wave) go with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 5 removed (Bethany kept 6 and 7; 5 asked about the removed tap diagram)', r'<div class="pq">\s*<span class="pq-num"[^>]*>5</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 6 and 7 answered')
fx('cut', 'lean: Part C drawn and typed on the page', 'A labeled wave diagram with crest, trough, amplitude, wavelength, and direction of energy — plus a one-sentence amplitude/energy claim.',
   'The wave I made or saw, what it moved through and my amplitude and energy claim. Plus your labeled sketch: crest, trough, amplitude, wavelength and an energy arrow.')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether water travels with a wave or stays in place, supported with two pieces of evidence.',
   '<strong>Use Your Evidence:</strong> My claim about whether water travels with a wave, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a 9.01 leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Download your field journal (it has your answers and your wave sketch) and upload it to the Canvas assignment. Or copy your Gathered Answers (above) into Canvas.', True)

# ---------------------------------------------------------------- the story
PRIYA = {'name': 'Dr. Priya Nair', 'role': 'materials scientist (someone who studies what things are made of and how they behave)', 'initials': 'PN', 'color': '#7A5BB5', 'lens': 'beaker', 'voiceId': 'uYXf8XasLslADfZ2MB4u'}
RACE = {'img': I('duck-race'), 'alt': 'Hundreds of yellow rubber ducks floating on a narrow river in a city, with a long yellow float stretched across the water.'}
D = {
    'lesson': '26.01', 'week': 26, 'day': 1, 'guide': 'priya', 'prefix': 'g4sci-26-1', 'manifestKey': '26-01',
    'paths': P['paths'], 'crew': {'priya': PRIYA},
    'expedition': {'num': 26, 'title': 'The Duck Derby Flop'},
    'ambient': {'icon': '🦆', 'label': 'Pond morning'},
    'case': {
        'num': 26, 'title': 'The Duck Derby Flop', 'style': 'flyer',
        'hook': 'Hi! I’m Dr. Priya Nair. I study what things are made of and how they behave, like how water, rope and air carry energy. My first case for you comes from the pond in Palmetto Springs. Last Saturday’s Duck Derby was a flop.',
        'flyer': {
            'flyer': {'top': 'PALMETTO SPRINGS', 'icon': '🦆🦆🦆', 'big': 'DUCK DERBY', 'sub': '200 rubber ducks. One pond. First duck to the dock wins!',
                      'rows': [['When', 'Saturday, 10 a.m.'], ['Where', 'The town pond'], ['Prize', 'Free ice cream for a year']], 'foot': 'Every dollar helps the town library.'},
            'receipt': {'head': 'WAVE-O-MATIC RENTALS', 'rows': [['Item', 'Wave machine'], ['Setting', 'GENTLE'], ['Time', '1 hour']], 'stamp': 'PAID'},
            'letter': {'to': 'Dear Dr. Nair,', 'body': ['The wave machine made lovely waves for a whole hour. The ducks bobbed up and down, but NOT ONE reached the dock!',
                                                     'Next year I’ll rent the giant Wave-O-Matic 5000. Bigger waves will push the ducks to the dock. Right?'], 'sign': 'Mr. Ortiz, race organizer'}},
        'stills': [dict(RACE, cam='A real duck race', time='Luxembourg, 2017', tag='📷 Real race', kind='print')],
        'question': 'Will a bigger wave machine get the ducks to the dock? Why or why not?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'crowd', 'icon': '🏟️', 'where': 'Warm-Up: be the crowd', 't': 'The wave went all the way around the stadium, but the fan in the red cap never left her seat. A wave is a pattern that travels. The stuff stays put.'},
            {'id': 'swapwave', 'icon': '🪀', 'where': 'The Lesson, Part 1: same wave, new stuff', 't': 'A wave can travel through a slinky, a rope, water, a line of kids or air. Every time, the tagged piece moved and came back to the same spot.'},
            {'id': 'brackets', 'icon': '📏', 'where': 'The Lesson, Part 2: measure the waves', 't': 'Amplitude is how tall a wave is, from the center line to a crest. The wave with the biggest amplitude carries the most energy.'},
            {'id': 'shake', 'icon': '🌊', 'where': 'The Lesson, Part 3: shake it yourself', 't': 'A hard wiggle made a taller wave with more energy. It knocked the cups down, but the red ribbon still only went up and down in its own spot.'},
        ],
        'solve': {
            'title': 'Will a bigger wave machine work?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Yes. Bigger waves push harder, so the ducks will float to the dock.', 'why': 'Check Clue 4. The taller wave had more energy, but the ribbon still stayed in its spot.'},
                {'t': 'Yes, if the waves are longer. Longer waves go farther.', 'why': 'Check Clue 2. Every wave went the whole way, and every tagged piece still came back to its spot.'},
                {'t': 'No. A bigger machine makes taller waves with more energy, so the ducks will bob higher. But waves carry energy, not ducks. The ducks will stay in place.', 'right': True,
                 'why': 'Case cracked! A wave carries energy through the water. The water, and the ducks floating on it, only move up and down as it passes.'},
                {'t': 'No. Rubber ducks are too light for waves to move.', 'why': 'Check Clue 2. Heavy or light, every tagged piece came back to its spot. It isn’t about the duck.'},
            ]},
    },
    'crowd': {
        'afterText': 'keep your eye on the fan in the red cap.', 'kicker': 'Warm-Up game', 'title': 'Be the crowd',
        'why': {'icon': '🏟️', 'q': 'What is “the wave”?', 't': 'At big games, fans stand up and sit down one section after another. A wave of standing people races around the stadium.'},
        'todo': ['Tap Section 1 (or press Stand up!). Then tap each glowing section, in order.', 'Keep going all the way around. Wait too long, and the wave fizzles!', 'Keep your eye on the fan in the red cap.'],
        'sections': 6, 'cols': 18, 'rows': 3, 'red': {'col': 4, 'row': 1}, 'gap': 2400, 'secWord': 'Section',
        'alt': 'A model of stadium stands: three rows of fans in six numbered sections. One fan wears a red cap.',
        'standBtn': '🙌 Stand up!', 'fizzle': 'The wave fizzled out! The next section waited too long. Start again at Section 1.', 'wrongSec': 'Not yet! The wave has to reach Section {n} first.',
        'tracker': {'wave': 'The wave', 'start': 'not started', 'red': 'Red cap', 'seatWord': 'seat'},
        'lapLine': 'The wave went all the way around the stadium!',
        'q1': 'Where is the fan in the red cap now?',
        'opts1': [{'t': 'In her same seat: Section 2, seat 5', 'ok': True},
                  {'t': 'On the other side of the stadium', 'miss': 'Look at the red cap tracker. Did her seat change?'},
                  {'t': 'She went around with the wave', 'miss': 'Watch her when the wave passes. Does she leave her seat, or just stand up and sit down?'}],
        'stats': [['The wave traveled', 'all the way around'], ['The red-cap fan traveled', '0 seats']],
        'fact': 'Scientists timed real stadium waves. A wave races about 20 seats every second, but each fan only stands up and sits down.',
        'q': 'So what traveled around the stadium?',
        'opts': [{'t': 'The pattern of standing up and sitting down: the wave', 'ok': True},
                 {'t': 'The fans', 'miss': 'The fans stayed in their seats. What moved from section to section?'},
                 {'t': 'The seats', 'miss': 'Seats are bolted down! What moved from section to section?'}],
        'win': 'A wave is a pattern that travels. The fans (the stuff) just move up and down in their own seats. Clue 1!'},
    'swapwave': {
        'afterText': 'Tag one piece and send a wave.', 'kicker': 'Part 1 game', 'title': 'Same wave, new stuff',
        'todo': ['Pick a kind of stuff.', 'Tap one piece to tag it red. Then press Send a wave.', 'Watch your tag. Your wave log fills in.', 'Try all five.'],
        'media': [
            {'id': 'slinky', 'icon': '🪀', 'name': 'Slinky', 'kind': 'slinky', 'n': 26, 'piece': 'coil', 'line': 'A slinky on the floor.', 'how': 'wiggled up and down, then stopped in the same spot'},
            {'id': 'rope', 'icon': '🪢', 'name': 'Rope', 'kind': 'rope', 'n': 22, 'piece': 'bead', 'line': 'A rope with beads on it.', 'how': 'wiggled up and down, then stopped in the same spot'},
            {'id': 'water', 'icon': '💧', 'name': 'Pond water', 'kind': 'water', 'n': 30, 'piece': 'bit of water', 'line': 'Pond water, seen from the side.', 'how': 'bobbed up and down, then stopped in the same spot'},
            {'id': 'kids', 'icon': '🧒', 'name': 'A line of kids', 'kind': 'kids', 'n': 12, 'piece': 'kid', 'line': 'A line of kids. Each one stands up when the kid beside them does.', 'how': 'stood up and sat down, then was in the same spot'},
            {'id': 'air', 'icon': '🔊', 'name': 'Air', 'kind': 'air', 'n': 22, 'piece': 'bit of air', 'line': 'Air between a drum and an ear. The drum skin vibrates (shakes back and forth fast) and pushes the air next to it.', 'how': 'moved back and forth a tiny bit, then stopped in the same spot'}],
        'sendBtn': '〰 Send a wave', 'tagFirst': 'Tap one {piece} to tie a red tag on it.', 'tagLine': 'Tagged! Now press Send a wave and watch your tagged {piece}.', 'nextLine': 'Now try it with: {name}.',
        'logLabel': 'My wave log', 'cols': ['Stuff (the medium)', 'The wave', 'My tagged piece'], 'waveCell': 'went the whole way',
        'q1': 'Where is your tagged piece now?',
        'opts1': [{'t': 'Right where it started', 'ok': True},
                  {'t': 'At the far end', 'miss': 'Watch the red tag. Did it ride all the way to the end, or come back?'},
                  {'t': 'It fell off', 'miss': 'The tag is still there! Look for the red piece. Where is it?'}],
        'q': 'Which kinds of stuff can carry a wave?',
        'opts': [{'t': 'All five: a slinky, a rope, water, a line of kids and air', 'ok': True},
                 {'t': 'Only water', 'miss': 'Look at your wave log. Did the wave go the whole way in the slinky and the air, too?'},
                 {'t': 'Only things you can see wiggle', 'miss': 'You can’t see air, but your log says the wave went through it. That’s how sound reaches your ear.'}],
        'win': 'A wave can travel through all kinds of stuff (mediums). Every time, the wave went the whole way and the tagged piece stayed in its spot. Clue 2!'},
    'duckloop': {
        'after': 'swapwave', 'kicker': 'Wow!', 'title': 'The duck’s secret loop',
        'todo': ['Press Send waves across the pond.', 'Watch the duck, not the waves.', 'Look at the red path the duck draws.'],
        'why': {'icon': '🔬', 'q': 'What does the water really do?', 't': 'Scientists who study water waves found that as a wave passes, each bit of water near the top moves in a small circle. A duck floating on top rides the same loop.'},
        'feet': 40, 'unit': 'feet', 'waveWord': 'The waves traveled', 'duckWord': 'The duck traveled', 'loopWord': 'a little loop, back to the start', 'frontWord': 'wave front', 'startWord': 'where the duck started',
        'runBtn': '▶ Send waves across the pond', 'againBtn': '↺ Send the waves again',
        'done': 'Wow! The waves rolled 40 feet across the pond, but the duck only drew a little loop and ended up (almost) right where it started.'},
    'brackets': {
        'afterText': 'Now measure three waves on grid paper.', 'kicker': 'Part 2 game', 'title': 'Measure the waves',
        'todo': ['Tap two dots to lay a bracket between them. Or drag from one dot to the other.', 'Measure the amplitude, then the wavelength.', 'Do all three waves, then answer the question.'],
        'waves': [{'id': 'ripple', 'name': 'Pebble ripple', 'icon': '🪨', 'amp': 1, 'wl': 4, 'c': '#55A7D8'},
                  {'id': 'swell', 'name': 'Ocean swell', 'icon': '🌊', 'amp': 2, 'wl': 9, 'c': '#2D7AA6'},
                  {'id': 'storm', 'name': 'Storm wave', 'icon': '⛈️', 'amp': 3, 'wl': 6, 'c': '#1E4F86'}],
        'tasks': {'amp': {'name': 'Amplitude', 'ask': 'Tap the dot on the center line under a crest. Then tap the crest above it.'},
                  'wl': {'name': 'Wavelength', 'ask': 'Tap one crest. Then tap the very next crest.'}},
        'readTpl': '{name}: {n}', 'unit': 'squares', 'unitOne': 'square', 'midWord': 'center line', 'sqWord': 'Each box on the grid is 1 square.', 'waveWord': 'Wave', 'waveCol': 'Wave', 'tableLabel': 'My wave measurements',
        'miss': {'ampTall': 'That bracket goes from the top all the way to the bottom: twice too tall. Amplitude starts at the center line.',
                 'ampSide': 'That bracket goes sideways. Amplitude goes straight up: from the center line to a crest.',
                 'amp': 'Start on the center line, right under a crest, and go straight up to the crest.',
                 'wlTwo': 'That is more than one wave. Go from one crest to the very NEXT crest.',
                 'wlHalf': 'That is only half a wave. Go from one crest to the NEXT crest.',
                 'wl': 'Wavelength goes sideways along the wave: from one crest to the next crest.',
                 'energyWl': 'The swell has the longest wavelength, but wavelength is spacing, not height. Energy goes with amplitude.',
                 'energy': 'Look at the amplitude column. Which wave is tallest?'},
        'q': 'Which wave carries the MOST energy?',
        'win': 'Amplitude is how tall a wave is, from the center line to a crest. The tallest wave carries the most energy. Clue 3!'},
    'shake': {
        'afterText': 'Watch the ribbon and the cups.', 'kicker': 'Part 3 game', 'title': 'Shake it yourself',
        'todo': ['Drag the hand up and down, or press Gentle wiggle.', 'Watch the red ribbon’s path and the cups.', 'Then make a hard wiggle and compare.'],
        'why': {'icon': '🪀', 'q': 'Why a slinky?', 't': 'Scientists use a slinky as a model of a wave. You can see every coil, so you can watch what moves and what stays.'},
        'gentleBtn': '〰 Gentle wiggle', 'hardBtn': '🌊 Hard wiggle', 'handLabel': 'drag me ↕', 'ribbonWord': 'ribbon path', 'hardAt': 60, 'topple': 52,
        'logLabel': 'My slinky log', 'cols': ['Wiggle', 'How tall (amplitude)', 'The red ribbon', 'The cups'],
        'rows': {'gentle': ['Gentle', 'Short (small amplitude)', 'Went up and down a little. Stayed in its spot.', 'Fell down', 'Stayed up'],
                 'hard': ['Hard', 'Tall (big amplitude)', 'Went up and down more. Stayed in its spot.', 'Fell down! 💥', 'Stayed up']},
        'needLine': 'Now try a {k} wiggle.',
        'q': 'What did the HARD wiggle change?',
        'opts': [{'t': 'It made a taller wave (bigger amplitude) with more energy. The ribbon still stayed in its spot.', 'ok': True},
                 {'t': 'The ribbon rode the wave down to the cups.', 'miss': 'Look at the ribbon’s red path. Did it move toward the cups, or only up and down?'},
                 {'t': 'Nothing. Both waves were the same.', 'miss': 'Look at your log. Which wiggle knocked the cups down?'}],
        'win': 'A taller wave (bigger amplitude) carries more energy: enough to knock the cups down. But the ribbon still only went up and down. Clue 4!'},
    'exploreMod': 'shake',
    'rivertwist': {
        'after': '.fs-solve', 'kicker': 'Twist!', 'title': 'What really moves the ducks?', 'lockLine': 'Crack the case first.',
        'todo': ['Press Race the ducks.', 'Compare the pond and the river.', 'Then answer the question.'],
        'pondLabel': 'The pond, with the wave machine', 'riverLabel': 'A river, where the water flows', 'finishWord': 'finish',
        'raceBtn': '▶ Race the ducks', 'againBtn': '↺ Race again',
        'photo': dict(RACE, cap='A real charity duck race on the Pétrusse river in Luxembourg, 2017. The river’s moving water carries the ducks to the finish. Photo: Bdx, CC BY-SA 4.0, via Wikimedia Commons.'),
        'q': 'What really carries the ducks to the finish in a real duck race?',
        'opts': [{'t': 'The moving river water (the current)', 'ok': True},
                 {'t': 'Bigger waves', 'miss': 'Look at the pond: big or small, waves only bob the ducks. What is different about the river?'},
                 {'t': 'The ducks swim', 'miss': 'Rubber ducks can’t swim! What is the river water doing?'}],
        'line': 'Most real duck races float on rivers or streams. The flowing water (the current) carries the ducks downstream. A wave only passes through the water.',
        'win': 'Twist solved! Waves carry energy. Moving water carries ducks.'},
    'raceplan': {
        'after': '.fs-solve', 'kicker': 'Case closed · the new plan', 'title': 'Mr. Ortiz’s new race plan', 'lockLine': 'Crack the case first.',
        'todo': ['Tap the right choice on each line to circle it.', 'A wrong choice gets crossed out.', 'Then stamp the plan.'],
        'head': 'Duck Derby · Plan for Next Year', 'sub': 'Palmetto Springs · Mr. Ortiz, with help from Dr. Nair',
        'lines': [
            {'label': 'Wave machine:', 'opts': [{'t': 'Rent the giant Wave-O-Matic 5000', 'miss': 'Bigger waves only make the ducks bob higher. Waves carry energy, not ducks.'}, {'t': 'No wave machine', 'ok': True}]},
            {'label': 'Where to race:', 'opts': [{'t': 'The still pond', 'miss': 'On still water, nothing carries the ducks along. Where does water flow?'}, {'t': 'Palmetto Creek, where the water flows', 'ok': True}]},
            {'label': 'Why:', 'opts': [{'t': 'A wave carries energy, not ducks. Flowing water carries ducks.', 'ok': True}, {'t': 'Bigger waves push harder.', 'miss': 'Remember the cups and the ribbon: a taller wave has more energy, but the ribbon stayed in its spot.'}]}],
        'stampBtn': '🖋️ Stamp the new plan', 'stamp': 'APPROVED', 'signLabel': 'Signed', 'sign': 'Mr. Ortiz',
        'win': 'Next year’s Duck Derby will really race. Thanks, scientist!'},
    'tool': {
        'name': 'Tuning fork', 'icon': '🎵', 'tab': 'assignment', 'after': '#tab-assignment .activity-card', 'key': '26-tool', 'sim': 'tuningfork',
        'kicker': 'Bonus · Tool of the Week', 'teaser': 'Strike two tuning forks, hear their notes and watch them vibrate in slow motion.',
        'done': 'You made sound from vibrations. A tuning fork sticker is in your Field Notebook.',
        'why': {'icon': '🎵', 'q': 'What is a tuning fork?', 't': 'A metal fork that rings one exact note when you tap it. Musicians use it to tune instruments, and scientists use it to study sound.'},
        'tuningfork': {
            'title': 'Fast or slow vibrations?', 'todo': ['Strike each fork and listen.', 'Watch the prongs wiggle in slow motion.', 'Answer the question. Then dip a ringing fork in water.'],
            'forks': [{'id': 'low', 'name': 'Low fork', 'hz': 256, 'tag': '256 a second', 'c': '#8C959B'}, {'id': 'high', 'name': 'High fork', 'hz': 512, 'tag': '512 a second', 'c': '#5E7A8C'}], 'slow': 128,
            'strikeBtn': '🔨 Strike it', 'wigTpl': 'In slow motion: {n} wiggles every second. For real: {hz} every second!',
            'needBoth': 'Now strike the other fork. Listen: is it higher or lower?',
            'model': 'A model: the prongs move in slow motion (128 times slower than real).',
            'q': {'q': 'The high fork makes a higher sound. How do its prongs move?',
                  'opts': [{'t': 'Faster: fast vibrations make a high pitch.', 'ok': True},
                           {'t': 'Slower', 'miss': 'Count the slow-motion wiggles for each fork. Which one wiggles more each second?'},
                           {'t': 'The same speed', 'miss': 'Look at the numbers under each fork. Are they the same?'}]},
            'dipBtn': '💧 Dip a ringing fork in water',
            'photo': {'img': I('fork-splash'), 'alt': 'A real ringing tuning fork touching water in a small glass. Tiny drops splash up where the prong touches the water.',
                      'cap': 'A real ringing tuning fork touching water. The prongs vibrate too fast to see, but the water feels it: tiny splashes jump up. Photo: a frame from a video by Lordgurke, CC BY-SA 4.0, via Wikimedia Commons.'}}},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Think about the duck on the pond. Did the water carry it anywhere?', 'B': 'Leaves can’t swim! Think about the duck: what moved across the pond?'},
        'q2': {'A': 'Think about the measuring game. Wavelength is the spacing. Which one is the HEIGHT?', 'C': 'Color isn’t part of a wave here. Which measurement tells how tall a wave is?'},
        'q3': {'B': 'Think about the red tag on the slinky. Did it slide to the end?', 'C': 'Something DID travel down the slinky. What reached the other end?'}},
    'flags': {
        'ans-2': [
            {'label': 'which carries more energy', 're': 'storm|taller|tall|bigger|big|larger|ocean'},
            {'label': 'uses amplitude', 're': 'ampl|amplit|ampitude|amplatude|amp[a-z]*tud'}],
        'ans-3': [
            {'label': 'why it’s true', 're': 'stay|in place|same (spot|place)|bob|up and down|wiggl|doesn.?t (move|go|travel)|does not (move|go|travel)|energy|loop|circle'},
            {'label': 'proof for a friend', 're': 'leaf|duck|cork|stick|ribbon|tag|slinky|rope|float|boat|toy|crowd|stadium|fan|test|watch|show|see|ball|bottle'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|doesn.?t|does not|stays|isn|is not'},
            {'label': 'two pieces of evidence', 'any': ['duck', 'loop', 'tag', 'ribbon', 'slinky', 'rope', 'cup', 'crowd', 'stadium', 'fan', 'red cap', 'seat', 'leaf', 'bob', 'pond', 'air', 'kids', 'amplitude', 'energy', 'circle', 'same spot', 'stayed'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-2': 12, 'ans-3': 15, 'cer-4': 30},
    'hints': {
        'ans-2': ['Which wave is taller?', 'Amplitude is how tall a wave is. Taller means more energy.', 'Try: The ___ carries more energy because its amplitude is ___.'],
        'ans-3': ['What happened to the red tag, the duck or the fan in the red cap?', 'Think of a test your friend could watch, like a floating leaf or a ribbon on a slinky.', 'Try: The wave moves but the water stays because ___. To prove it, I would ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'The waves rolled across the pond, but the duck only drew a little loop and ended up where it started.',
                'The red tag on the slinky, the rope and the water went up and down, then stopped in the same spot.',
                'A taller wave knocked the cups down, but the ribbon stayed in its spot.',
                'Mr. Ortiz thinks bigger waves will push the ducks.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · The Duck Derby Flop', 'length': '20–30 s'},
        'warmup': {'label': 'Warm-Up · be the crowd (Clue 1)', 'length': '15–20 s',
                   'script': 'Hi, I’m Dr. Priya Nair. Let’s do the wave! Tap Section one, then each glowing section, in order. Don’t wait too long, or it fizzles. And keep your eye on the fan in the red cap. Where does she end up?'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · same wave, new stuff (Clue 2)', 'length': '15–20 s',
                  'script': 'Same wave, new stuff. Pick the slinky, the rope, the pond water, the line of kids, or the air. Tap one piece to tag it red. Then press Send a wave and watch your tag. Your wave log fills in as you go.'},
        'part2': {'label': 'Part 2 · measure the waves (Clue 3)', 'length': '20–30 s'},
        'explore': {'label': 'Part 3 · shake it yourself (Clue 4)', 'length': '15–20 s',
                    'script': 'Now you make the wave. Drag the hand up and down, or press Gentle wiggle. Watch the red ribbon, and the cups at the far end. Then try a hard wiggle. What changed?'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · my wave model', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '15–20 s',
                     'script': 'A classmate says the water has to travel with the wave. True? Think about the duck’s loop, and the red tag. Pick your side, tap two facts in the planner, then explain. That’s your C-E-R.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 26.02 (coded messages).'},
    },
    'videoOff': [],
    'lensVoice': False,
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'The fan in the red cap, standing up (Warm-Up)',
        'Your wave log (The Lesson)',
        'The duck’s little loop (The Lesson)',
        'The cups falling down (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['A jump rope wave', 'Ripples in a pond', 'A slinky wave'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · draw and label your wave', 'required': True, 'minLabels': 5,
                           'prompts': ['Draw your wave with at least 2 crests', 'Label a CREST and a TROUGH', 'Show and label the AMPLITUDE and the WAVELENGTH', 'Add an arrow labeled ENERGY: the way it traveled']}]},
    'hlCoach': copy.deepcopy(O['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🦆', 'name': 'A derby duck',
                 'line': 'You cracked Case 26, and a derby duck goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next time: secret messages sent with waves!'},
    'notebookTitle': O['notebookTitle'],
    'notebook': copy.deepcopy(O['notebook']) + [{'lesson': '26.01', 'icon': '🦆', 'name': 'A derby duck'}],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You’re riding the wave!',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to see what it means.']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '#tab-vocab p', 'text': 'What wiggled, and what traveled?'},
         'label': 'Warm-Up: waves I have seen', 'q': 'Warm-Up: A wave I have seen, what wiggled and what traveled.', 'title': 'Waves I have seen', 'compact': True,
         'fields': [{'t': 'A wave I have seen', 'icon': '🌊', 'ph': 'I saw a wave in ___.'},
                    {'t': 'What wiggled', 'icon': '〰️', 'ph': 'The ___ wiggled.'},
                    {'t': 'What traveled', 'icon': '➡️', 'ph': 'The ___ traveled across.'}]},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'write one sentence about its amplitude and energy.'},
         'label': 'Part C: My wave model', 'q': 'Part C: My wave model (the wave, what it moved through, my amplitude and energy claim)', 'title': 'My wave model',
         'fields': [{'t': 'The wave I made or saw', 'icon': '🪢', 'ph': 'I made a wave with ___. / I saw a wave in ___.'},
                    {'t': 'What it moved through (the medium)', 'icon': '🌐', 'ph': 'It moved through ___.'},
                    {'t': 'My amplitude and energy claim', 'icon': '📈', 'ph': 'When the wave was taller, ___.', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Does the water have to travel with the wave?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-2': 'Part B · Question 6', 'ans-3': 'Part B · Question 7', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'A wave carries energy across the pond, but the water stays in place.',
    'key': ['wave', 'energy', 'water', 'stays'],
    'small': ['a', 'across', 'but', 'the', 'in'],
    'model': 'A scientist might highlight “wave”, “energy” and “stays”. Those words hold the big idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this tell what travels, what stays, or how much energy a wave has?']

EV = '#tab-assignment .act-body > div:has(> .fs-plan)'
D['cues'] = {
    'warmup': [{'at': '^section', 'sel': '.fs-crd-sec.next', 'fx': 'point', 'scroll': True},
               {'at': '^glowing', 'sel': '.fs-crd-go', 'fx': 'pop'},
               {'at': '^fizzles', 'sel': '[data-mod="crowd"] .fs-todo li', 'i': 1, 'fx': 'trace'},
               {'at': '^red', 'sel': '.fs-crd-r', 'fx': 'pop', 'tag': 'red cap'},
               {'at': '^end', 'sel': '.fs-crd-track', 'fx': 'glow'}],
    'part1': [{'at': '^slinky', 'sel': '.fs-swv-tab', 'i': 0, 'fx': 'pop', 'scroll': True},
              {'at': '^air', 'sel': '.fs-swv-tab', 'i': 4, 'fx': 'pop'},
              {'at': '^tag', 'sel': '.fs-swv-stage', 'fx': 'glow'},
              {'at': '^send', 'sel': '.fs-swv-send', 'fx': 'point'},
              {'at': '^log', 'sel': '[data-mod="swapwave"] .fs-todo li', 'i': 2, 'fx': 'trace'}],
    'explore': [{'at': '^hand', 'sel': '.fs-shk-stage', 'fx': 'glow', 'scroll': True},
                {'at': '^gentle', 'sel': '.fs-shk-g', 'fx': 'point'},
                {'at': '^ribbon', 'sel': '[data-mod="shake"] .fs-todo li', 'i': 1, 'fx': 'trace'},
                {'at': '^hard', 'sel': '.fs-shk-h', 'fx': 'point'}],
    'evidence': [{'at': '^classmate', 'sel': EV + ' > p', 'i': 0, 'fx': 'trace', 'scroll': True},
                 {'at': '^loop', 'sel': '.fs-plan .fs-opt', 'i': 2, 'fx': 'glow'},
                 {'at': '^tag', 'sel': '.fs-plan .fs-opt', 'i': 3, 'fx': 'glow'},
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
