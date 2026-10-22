#!/usr/bin/env python3
"""Writes data.json and fixes.json for 18.01 (run from this folder). Showcase lesson: Case 18 "The Red Water Sample" at Palmetto Beach.
Sam Park (Unit 5) introduces himself. New modules: zoom, bench, scope (+ lab report); hand lens tool (SIMS.handlens).
Reused: bulletin (the beach alert, news voice) and mitsort (4 shelves, the size ladder)."""
import json, copy
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../16-02/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

# ---------------------------------------------------------------- ticked fixes (Bethany, 22 Oct 2026)
fx('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist already asks for a three-view sketch',
   '🎨 Part C &mdash; Build Your Own Food Chain', '🔬 Part C &mdash; Three Views of One Small Thing')
fx('fix', 'copy-paste leftover: Part C task from 9.01 (typed on the page now; a sketch is a bonus)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   "Pick one small Florida thing (a leaf, a shell, a grain of sand, an ant). Tell what you’d see with your eyes, with a hand lens and with a microscope. Then pick the best tool for one question about it.</p>", True)
fx('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'unit label under the week: “Ecosystems & Energy” is a leftover; week 18 starts Unit 5', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Energy, Motion &amp; Collisions</div>')
fx('fix', 'this is a Nature of Science lesson (tools, SC.4.N.1.1 / SC.4.E.6.5), not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Nature of Science</div>')
fx('fix', 'the electron microscope needs a dried, prepared sample; the lesson said “carefully prepared” only once, and the case turns on it',
   "Can show the bumps on a single virus. Most schools don't have one, but universities and research labs do.",
   "It can show the bumps on a single virus. But the sample must be dried and specially coated first, so nothing on it can be alive. Most schools don't have one.")

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; plain words',
   "Hold this question in your head as you work. By the end of the lesson, you'll know which tool to grab when something is too small for your eyes — and why scientists trust the evidence those tools give them.",
   "Keep this question in mind. By the end, you’ll know which tool to grab when something is too small for your eyes, and why.")
fx('plain', 'the warm-up is the beach alert and the zoom machine now; answers are made on the page',
   r"<p>Hold your hand out in front of you\..*?</p>\s*<p>In your notebook, draw what you can see\..*?</p>",
   "<p>Something strange is happening at Palmetto Beach. Listen to the alert. Then look closer with Sam’s zoom machine.</p>", True)
fx('plain', 'warm-up title matches the new warm-up', "🌅 Warm-Up: What's on the Tip of Your Finger?", '🌅 Warm-Up: Something in the Water')
fx('plain', 'warm-up subtitle; dash removed', 'Look — really look — at something tiny', 'Listen, then zoom in')
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', '“like seeing 10 inches in 1 inch” confuses more than it helps',
   'A 10x hand lens magnifies an object 10 times — like seeing 10 inches in 1 inch.', 'A 10x hand lens makes things look 10 times bigger.')
fx('plain', 'dash removed; shorter', 'Every tool has limitations — that\'s why scientists use more than one.', 'Every tool has limitations. That\'s why scientists use more than one.')
fx('plain', 'shorter', 'Scientists deal with this by using tools that', 'Scientists use tools that')
fx('plain', 'dash removed', '</span></span> — they make small things look bigger so you can', '</span></span>. These tools make small things look bigger, so you can')
fx('plain', 'shorter: the electron microscope’s limit is now in its list item', ' An electron microscope can see almost anything tiny — but only on things that have been carefully prepared.', '')
fx('plain', 'dash removed', 'Part 1 · Your Eyes Are Powerful — But Limited', 'Part 1 · Your Eyes Are Powerful, but Limited')
fx('plain', 'dash removed; plain words', 'Shows things invisible to the eye — plant cells, blood cells, the tiny moving life in a drop of pond water.', 'Shows things too small for your eyes: plant cells, blood cells and the tiny moving life in a drop of pond water.')
fx('plain', 'shorter', " You can't see the tiny scales on a moth's wing.", '')
fx('plain', 'dash removed', 'Same drop of pond water — three completely different pictures.', 'Same drop of pond water, three very different pictures.')
fx('plain', 'dash removed from the claim', 'the most powerful tool you can find — the more magnification, the better.', 'the most powerful tool you can find. The more magnification, the better.')
fx('plain', 'misconception kept (it is the CER) but plain, no dash',
   r'<p><strong>Common misconception:</strong> Some people think a more powerful tool is always better\..*?</p>',
   '<p><strong>Watch out:</strong> Some people think a more powerful tool is always better. But a hand lens is the right tool for a leaf. A 1,000x microscope would show only a tiny, confusing piece of it. The best tool is the one that fits the question.</p>', True)
fx('plain', 'the tool bench is Part 3 now', 'margin-top:22px;">Pick the Right Tool</h3>', 'margin-top:22px;">Part 3 · Pick the Right Tool</h3>')
fx('plain', 'the bench replaces the tap diagram', "<p><strong>Tap a tiny Florida thing</strong> to see which tool works best — and why.</p>",
   '<p>Sam’s lab got four requests this morning. Each one needs the right tool.</p>')
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'shorter closing; points to 18.02',
   r'<p><strong>Nicely done\.</strong> You can now pick the right tool.*?</p>',
   '<p><strong>Nicely done.</strong> You found what was hiding in Palmetto’s water, and you picked the right tool for each job. Next time, you’ll flip the question: how do tools help us see things that are very far away, like the Moon, stars and planets?</p>', True)

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: Stop & Think (the size ladder is the thinking stop for Part 1)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: the Key Concept box repeats Part 2', r'<div style="background:#FFF6E5;border:2.5px solid #F0C97A;[^"]*">\s*<div[^>]*>⭐ Key Concept</div>\s*<p[^>]*>.*?</p>\s*</div>\s*', '', True)
fx('cut', 'lean: Stop & Reason (the picture speaks; the bench is the next thinking stop)', r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its three-view notebook page becomes Part C)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: Observe & Reason, the Amazing Fact, the Florida red tide note (it becomes the case) and Go Deeper (the two lenses are in Part 4’s why card); Part 4 = Sam’s microscope; next button goes to Self-Check',
   r'<div class="socratic-q">\s*<span class="sq-icon">👀</span>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 4 · Count the Cells</h3>\n      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">Back to Sam’s sample. A light microscope can count living red tide cells. Florida scientists count them this way to warn people at the beach.</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 5 removed (Bethany kept 6 and 7; the bench already asks it)', r'<div class="pq">\s*<span class="pq-num"[^>]*>5</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: renumber Part B (6 → 5)', '<span class="pq-num" style="background:#D4772C;">6</span>', '<span class="pq-num" style="background:#D4772C;">5</span>')
fx('cut', 'lean: renumber Part B (7 → 6)', '<span class="pq-num" style="background:#D4772C;">7</span>', '<span class="pq-num" style="background:#D4772C;">6</span>')
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C typed on the page; the sketch is a bonus',
   'A three-view sketch (eye, hand lens, microscope) of one small Florida thing, with labeled details in each circle plus a tool-choice sentence.',
   'Three views of one small Florida thing (eyes, hand lens, microscope), plus the best tool for one question. (A sketch is a bonus.)')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether the most powerful tool is always best, and supported it with two pieces of evidence from the lesson.',
   '<strong>Use Your Evidence:</strong> My claim about whether the most powerful tool is always best, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', True)

# ---------------------------------------------------------------- the story
I = lambda n: 'images/18-01-' + n + '.jpg'
SAM = {'name': 'Sam Park', 'role': 'engineer (someone who designs and builds things to solve problems)', 'initials': 'SP', 'color': '#1F7F86', 'lens': 'blueprint', 'voiceId': 's3TPKV1kjDlVtZbl4Ksh'}
CDC = 'Red tide along the Florida coast, 2005: CDC / Lorraine Backer, PhD (CDC Public Health Image Library, public domain)'
FWC = 'One red tide cell (Karenia brevis) under an electron microscope: Florida Fish and Wildlife Conservation Commission (public domain)'
WING = 'Honey bee wing: USGS Bee Inventory and Monitoring Lab, Sam Droege (public domain)'
SAND = 'Sand grains up close (greensand): USGS Bee Inventory and Monitoring Lab (public domain)'
ELODEA = 'Water plant (Elodea) leaf cells at 450x, through a microscope eyepiece: Angryarmpit (public domain)'
DIATOM = 'Diatoms through a light microscope: Prof. Gordon T. Taylor, Stony Brook University (NOAA, public domain)'
POLLEN = 'Pollen under an electron microscope, colorized: Dartmouth Electron Microscope Facility (public domain)'
PRINT = 'Whorl fingerprint: NIST (public domain)'
ALL = ' All via Wikimedia Commons except the CDC photo. Palmetto Beach, the alert and Sam’s sample are made up for this lesson.'

D = {
    'lesson': '18.01', 'week': 18, 'day': 1, 'guide': 'sam', 'prefix': 'g4sci-18-1', 'manifestKey': '18-01',
    'paths': P['paths'], 'crew': {'sam': SAM},
    'expedition': {'num': 18, 'title': 'The Red Water Sample'},
    'ambient': {'icon': '🌊', 'label': 'Ocean sounds'},
    'case': {
        'num': 18, 'title': 'The Red Water Sample', 'style': 'lab',
        'hook': 'Hi! I’m Sam Park, an engineer. I design and build tools, and I’m your guide for the next few weeks. Today my tools have a real job. A lifeguard at Palmetto Beach brought me a jar of strange-looking water. Let’s find out what’s in it.',
        'notice': {'head': 'Water sample · Palmetto Field Lab', 'title': 'Sample 18-A: Palmetto Beach, Gulf side',
                   'rows': [['Collected', 'Monday, 7 AM, in knee-deep water'],
                            ['How it looks', 'Red-brown and a little cloudy'],
                            ['At the beach', 'Dead fish on the sand. Swimmers coughing, sneezing, eyes stinging.']],
                   'line': 'Sam’s job: find out what is in the water.'},
        'stills': [{'cam': 'A real Florida beach', 'time': 'during a red tide', 'tag': '📷 Real place', 'kind': 'print', 'img': I('redtide-coast'),
                    'alt': 'Looking down at a Florida beach from the air: waves roll in, and the water near the shore is a muddy red-brown.'}],
        'stillsCredit': CDC + '. Palmetto Beach, the lifeguard and the sample are made up for this lesson.',
        'question': 'What is hiding in the water at Palmetto Beach, and which tool can find it?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'zoom', 'icon': '🔍', 'where': 'Warm-Up: the zoom machine', 't': 'Your eyes see only red-brown water. The cause is a cell so small that two or three side by side are about as wide as one hair.'},
            {'id': 'mitsort', 'icon': '🪜', 'where': 'The Lesson, Part 1: how small can each tool go?', 't': 'A red tide cell is too small for your eyes or a hand lens. You need a microscope.'},
            {'id': 'bench', 'icon': '🧪', 'where': 'The Lesson, Part 3: pick the right tool', 't': 'To COUNT living red tide cells, use a light microscope. An electron microscope shows more detail, but only on dried samples, so nothing on them is alive.'},
            {'id': 'scope', 'icon': '🔬', 'where': 'The Lesson, Part 4: count the cells', 't': 'Sam counted 12 cells in the square: about 1,200,000 red tide cells in one liter. The FWC chart says that’s HIGH: fish die, people cough, and the water changes color.'},
        ],
        'solve': {
            'title': 'What is in the water?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Nothing is in the water. The fish died because the water got cold.', 'why': 'Check Clues 1 and 4. What did Sam find in the drop?'},
                {'t': 'Red tide cells, found with an electron microscope while they were swimming.', 'why': 'Check Clue 3. Can an electron microscope look at living, swimming cells?'},
                {'t': 'Red tide: tiny living cells, too small to see. A light microscope found and counted them, and the level is HIGH.', 'right': True,
                 'why': 'Case cracked! You picked the right tool and found the cause. Now write your case report: it’s the questions below.'},
            ]},
    },
    'bulletin': {
        'afterText': 'Something strange is happening at Palmetto Beach', 'kicker': 'Warm-Up', 'title': 'The beach alert',
        'todo': ['Press Play and listen. You can read along on the paper.', 'Tap the three things people NOTICED at the beach. A place or a time is not something they noticed.'],
        'device': 'BEACH ALERT', 'station': 'Palmetto Beach · Monday, 7 AM', 'playBtn': 'Play the alert', 'againBtn': 'Play it again', 'audio': 'bulletin',
        'paperHead': 'HEALTH ALERT · PALMETTO BEACH',
        'lines': ['This is a health alert for Palmetto Beach.',
                  'Lifeguards found [[fish|dead fish washing up on the sand]].',
                  'The [[water|water looks red-brown]] in long streaks near the shore.',
                  'Swimmers say [[cough|they are coughing and sneezing]], and their eyes sting.',
                  'Please stay out of the water at [[x:Palmetto Beach is a place. What did people see, hear or feel there?|Palmetto Beach]] until [[x:Wednesday is a time. What did people notice?|Wednesday]]. Scientists are testing the water now.'],
        'foundLabel': 'What people noticed', 'dangerWord': 'Clue', 'countIcon': '👀', 'countWord': 'things people noticed',
        'dangers': [{'id': 'fish', 'icon': '🐟', 't': 'Dead fish', 'does': 'washing up on the sand'},
                    {'id': 'water', 'icon': '🟤', 't': 'Red-brown water', 'does': 'in long streaks near the shore'},
                    {'id': 'cough', 'icon': '🤧', 't': 'Coughing and sneezing', 'does': 'and stinging eyes'}],
        'win': 'People noticed three things. But nobody could SEE what was causing them. Time to zoom in.'},
    'zoom': {
        'afterSel': '.fs-game[data-mod="bulletin"]', 'kicker': 'Warm-Up game', 'title': 'Sam’s zoom machine',
        'todo': ['Each stop on the dial is a stronger tool. Tap the new detail at each stop, then turn the dial.'],
        'stops': [
            {'k': 'eye', 'icon': '👁️', 'tool': 'Your eyes', 'power': '1x', 'img': I('redtide-coast'), 'alt': 'A Florida beach from the air during a red tide. The water near the shore is red-brown.',
             'ask': 'This is what your eyes see at a red tide beach. Tap the strange color.', 'hint': 'Look at the water near the shore. What color is it?',
             'spot': {'x': 32, 'y': 42, 'r': 34, 't': 'Red-brown streaks in the water'},
             'see': 'Your eyes can see the color. But they can’t see what is making it.'},
            {'k': 'lens', 'icon': '🔍', 'tool': 'Hand lens', 'power': '10x', 'img': I('sand'), 'alt': 'Sand grains up close: green, tan and clear grains of many shapes.',
             'ask': 'A hand lens on sand from a beach. Tap a grain that looks like glass.', 'hint': 'Look for a grain you can almost see through.',
             'spot': {'x': 62, 'y': 46, 'r': 14, 't': 'A clear, glassy grain'},
             'see': 'With a hand lens, each grain has its own shape and color. But red tide cells are still too small to see at 10x.'},
            {'k': 'light', 'icon': '🔬', 'tool': 'Light microscope', 'power': '450x', 'img': I('elodea'), 'alt': 'A circle of light through a microscope eyepiece: a green leaf made of rows of tiny box shapes.',
             'ask': 'A water plant’s leaf through a light microscope. Tap the tiny shapes that build the leaf.', 'hint': 'Look inside the bright circle. Do you see little boxes in rows?',
             'spot': {'x': 62, 'y': 62, 'r': 22, 't': 'Rows of tiny boxes: cells!'},
             'see': 'A light microscope shows cells, and they can stay alive. Red tide cells are about this size.'},
            {'k': 'em', 'icon': '⚡', 'tool': 'Electron microscope', 'power': 'over 1,000x', 'img': I('kbrevis-sem'), 'alt': 'A gray, bumpy, three-dimensional cell with a groove around its middle and a curly, whip-like tail.',
             'ask': 'This is ONE red tide cell. Tap the part that helps it swim.', 'hint': 'Look for something curly, like a tiny whip.',
             'spot': {'x': 36, 'y': 57, 'r': 16, 't': 'A tiny whip-like tail'},
             'see': 'The tail helps it swim. Two or three of these cells side by side are about as wide as one hair. This cell had to be dried first, so it was not alive.'}],
        'lockLine': 'Find the new detail at this stop first. Then turn the dial.',
        'q': 'Why couldn’t people at the beach see what turned the water red-brown?',
        'opts': [{'t': 'The cells are much too small to see with just your eyes.', 'ok': True},
                 {'t': 'The water was too dark to see into.', 'miss': 'Look at the last stop. How big is one red tide cell?'},
                 {'t': 'The cells only come out at night.', 'miss': 'Look at the last stop. How big is one red tide cell?'}],
        'credit': CDC + '. ' + SAND + '. ' + ELODEA + '. ' + FWC + '.' + ALL,
        'win': 'Your eyes saw only the color. The cause is a cell too small to see. That’s a clue.',
        'clue': 'zoom'},
    'mitsort': {
        'afterText': 'Scientists use tools that', 'kicker': 'Part 1 game', 'title': 'How small can each tool go?', 'cols': 4,
        'todo': ['Drag each card onto the weakest tool that shows it clearly (or tap a card, then a shelf).'],
        'why': {'icon': '🪜', 'q': 'Why the weakest tool?', 't': 'Scientists start simple. If your eyes can do the job, you don’t need a microscope.'},
        'shelves': [{'k': 'eye', 'icon': '👁️', 't': 'Your eyes', 'sub': 'no tool'},
                    {'k': 'lens', 'icon': '🔍', 't': 'Hand lens', 'sub': '2x to 10x'},
                    {'k': 'light', 'icon': '🔬', 't': 'Light microscope', 'sub': '40x to 1,000x'},
                    {'k': 'em', 'icon': '⚡', 't': 'Electron microscope', 'sub': 'up to 1,000,000x'}],
        'cards': [
            {'id': 'fish', 'icon': '🐟', 't': 'A dead fish on the sand', 'k': 'eye', 'why': 'A whole fish is big enough to see with just your eyes.', 'miss': 'A whole fish is big! Do you need a tool at all?'},
            {'id': 'water', 'img': I('redtide-coast'), 'alt': 'Red-brown water along a beach', 't': 'Red-brown streaks in the sea', 'k': 'eye', 'why': 'You can see the color from the beach, with no tool.', 'miss': 'You can see a color in the sea from the beach. Do you need a tool?'},
            {'id': 'wing', 'img': I('bee-wing'), 'alt': 'A honey bee wing up close', 't': 'The veins on a bee’s wing', 'k': 'lens', 'why': 'Wing veins are thin, but a hand lens shows them easily.', 'miss': 'Your eyes see the wing, but not the thin veins clearly. Do you need a whole microscope, or something smaller?'},
            {'id': 'print', 'img': I('fingerprint'), 'alt': 'A fingerprint with swirling ridges', 't': 'Every ridge in a fingerprint', 'k': 'lens', 'why': 'Your eyes see some lines. A hand lens shows every ridge and swirl.', 'miss': 'Your eyes see some lines, but not every ridge. Which small, quick tool fits?'},
            {'id': 'diatom', 'img': I('diatoms'), 'alt': 'Tiny glassy living things through a microscope', 't': 'Tiny living things in a drop of seawater', 'k': 'light', 'why': 'Much too small for a hand lens. A light microscope shows them alive.', 'miss': 'Too small for a hand lens. And you want to see them alive. Which microscope uses light?'},
            {'id': 'redcell', 'icon': '🟤', 't': 'Red tide cells swimming in a drop', 'k': 'light', 'why': 'Each cell is thinner than a hair. A light microscope shows them alive and swimming.', 'miss': 'Too small for a hand lens. And they are swimming, so they are alive. Which microscope can show living things?'},
            {'id': 'pollen', 'img': I('pollen-sem'), 'alt': 'Many grains of pollen with spikes and bumps, colored pink, green and yellow', 't': 'The spikes on one grain of pollen', 'k': 'em', 'why': 'The spikes are tiny, even on a tiny grain. An electron microscope shows them. (The pollen is dried first.)', 'miss': 'A light microscope shows the grains, but not the tiny spikes clearly. Which tool sees the smallest bumps?'},
            {'id': 'virus', 'icon': '🦠', 't': 'A virus (much smaller than a cell)', 'k': 'em', 'why': 'Most viruses are too small for a light microscope. An electron microscope shows them.', 'miss': 'A light microscope can’t see most viruses. Which tool goes even smaller?'}],
        'startLine': 'Drag a card onto a shelf (or tap a card, then a shelf).', 'doneLine': 'Every card is on a shelf.',
        'q': 'Which tools are too weak to show one red tide cell?',
        'opts': [{'t': 'Only your eyes', 'miss': 'Look at the hand lens shelf. Did the red tide cells go there?'},
                 {'t': 'Your eyes AND a hand lens', 'ok': True},
                 {'t': 'The light microscope', 'miss': 'Look at the light microscope shelf. What’s on it?'}],
        'credit': CDC + '. ' + WING + '. ' + PRINT + '. ' + DIATOM + '. ' + POLLEN + '.' + ALL,
        'win': 'A red tide cell is too small for your eyes or a hand lens. You need a microscope. That’s a clue.',
        'clue': 'mitsort'},
    'bench': {
        'afterText': 'Sam’s lab got four requests', 'replace': '#tab-lesson .diagram-wrap', 'kicker': 'Part 3 game', 'title': 'Pick the right tool',
        'todo': ['Read each lab request. Think: how small is it, and what does the question ask?', 'Drag a tool onto the request (or tap a tool, then the request).'],
        'why': {'icon': '⚡', 'q': 'Why can’t the electron microscope do every job?', 't': 'It shows the smallest details. But the sample has to be dried and coated first, so nothing on it can be alive.'},
        'toolsLabel': 'Sam’s tools', 'dropHere': 'Drop a tool here',
        'tools': [{'k': 'lens', 'icon': '🔍', 't': 'Hand lens', 'power': '2x to 10x'},
                  {'k': 'light', 'icon': '🔬', 't': 'Light microscope', 'power': '40x to 1,000x'},
                  {'k': 'em', 'icon': '⚡', 't': 'Electron microscope', 'power': 'up to 1,000,000x'}],
        'jobs': [
            {'id': 'wing', 'img': I('bee-wing'), 'alt': 'A honey bee wing up close', 't': 'At a beach picnic, look at the veins on a bee’s wing.', 'k': 'lens',
             'why': 'Quick, no batteries, and strong enough for wing veins.',
             'miss': {'light': 'A light microscope needs a thin slide and a lab. You’re at a picnic!', 'em': 'Way too much, and it needs a lab and a dried sample. Pick something you can carry.'}},
            {'id': 'count', 'img': I('redtide-coast'), 'alt': 'Red-brown water along a beach', 't': 'Count how many LIVING red tide cells are in one drop of this water.', 'k': 'light',
             'why': 'Strong enough to see each cell, and the cells stay alive in the drop.',
             'miss': {'lens': 'Too weak. At 10x, red tide cells are still too small to see.', 'em': 'It can’t look at living things. The sample must be dried first, so the cells would be dead.'}},
            {'id': 'leaf', 'img': I('elodea'), 'alt': 'A green leaf made of rows of tiny cells', 't': 'See the cells inside a water plant’s leaf.', 'k': 'light',
             'why': 'Cells are too small for a hand lens, but a light microscope shows them clearly.',
             'miss': {'lens': 'Cells are far too small for a hand lens.', 'em': 'Too much! A light microscope already shows the cells clearly.'}},
            {'id': 'groove', 'img': I('kbrevis-sem'), 'alt': 'One bumpy red tide cell with a groove and a whip-like tail', 't': 'See the tiny groove and the whip-like tail on the outside of ONE red tide cell.', 'k': 'em',
             'why': 'Only an electron microscope shows surface details this small. This real photo was taken with one.',
             'miss': {'lens': 'Way too weak for one cell’s outside.', 'light': 'A light microscope shows the cell, but not the tiny bumps and grooves on its outside.'}}],
        'q': 'What makes a tool the RIGHT tool?',
        'opts': [{'t': 'The most powerful one', 'miss': 'Look at request 2. The most powerful tool couldn’t count living cells.'},
                 {'t': 'The one that fits the question', 'ok': True},
                 {'t': 'The one that’s easiest to carry', 'miss': 'Look at request 4. A hand lens is easy to carry, but could it do that job?'}],
        'credit': WING + '. ' + CDC + '. ' + ELODEA + '. ' + FWC + '.' + ALL,
        'win': 'The best tool fits the question. To COUNT living red tide cells, Sam needs a light microscope. That’s a clue.',
        'clue': 'bench'},
    'scope': {
        'afterText': 'Back to Sam’s sample', 'kicker': 'Part 4 game', 'title': 'Count the cells',
        'todo': ['Follow the four steps. The view is a model of what Sam sees.', 'Then fill in Sam’s lab report.'],
        'why': {'icon': '🔬', 'q': 'Why does it say 400x?', 't': 'A microscope has two lenses. The eyepiece makes things look 10 times bigger. The objective lens makes them 40 times bigger. 10 × 40 = 400.'},
        'eyepiece': 10, 'objectives': [{'x': 4, 'focus': 22}, {'x': 10, 'focus': 47}, {'x': 40, 'focus': 71}], 'target': 12,
        'steps': ['Put the slide on', 'Turn to the 40x lens', 'Focus', 'Count the cells in the square'],
        'slideBtn': '🧫 Put the slide on the stage',
        'lines': {'low': 'At 40x in all, red tide cells are just specks. Too small to count.',
                  'mid': 'At 100x, you can see tiny golden dots. Still too small to count well. Try the strongest lens.',
                  'needLens': 'These cells are too small to count at this power. Turn to the 40x lens.',
                  'needFocus': 'It’s too blurry to count. Turn the focus knob first.',
                  'doneTitle': '12 cells!', 'doneT': 'Now fill in the lab report below.',
                  'fieldAlt': 'A model of the view through the microscope: a circle of light with small golden red tide cells, a few long striped diatoms, and a dashed counting square.'},
        'rule': {'head': 'Sam’s rule', 't': 'The count square holds only a tiny bit of one drop. Each cell you counted stands for 100,000 cells in one liter of seawater (about one big water bottle).'},
        'report': {
            'head': 'PALMETTO FIELD LAB · SAMPLE REPORT', 'sub': 'Sample 18-A · Palmetto Beach, Gulf side',
            'rows': [
                {'k': 'tool', 'label': 'Tool used', 'q': 'Which tool did Sam use?',
                 'opts': [{'t': 'Hand lens', 'miss': 'A hand lens was too weak to show the cells.'}, {'t': 'Light microscope', 'ok': True}, {'t': 'Electron microscope', 'miss': 'The electron microscope can’t count living cells.'}]},
                {'k': 'mag', 'label': 'Magnification', 'q': 'How much bigger did the cells look? (10x eyepiece × 40x lens)',
                 'opts': [{'t': '40x', 'miss': '40x is just the lens. Multiply by the 10x eyepiece.'}, {'t': '50x', 'miss': 'Multiply, don’t add: 10 × 40.'}, {'t': '400x', 'ok': True}]},
                {'k': 'n', 'label': 'Cells in the count square', 'fixed': '12'},
                {'k': 'perL', 'label': 'Cells in 1 liter of seawater', 'q': 'Use Sam’s rule: 12 cells × 100,000. How many in one liter?',
                 'opts': [{'t': '120,000', 'miss': 'Count the zeros. 100,000 has five zeros, so 12 × 100,000 = 12 with five zeros.'}, {'t': '1,200,000', 'ok': True, 'fill': '1,200,000 cells'}, {'t': '12,000,000', 'miss': 'One zero too many. 12 × 100,000 = 12 with five zeros.'}]}],
            'levelLabel': 'Red tide level (FWC chart)',
            'levelQ': 'Find 1,200,000 on the real red tide chart from Florida’s wildlife scientists (FWC). Tap its row.',
            'levels': [
                {'k': 'none', 't': 'NOT PRESENT', 'range': '1,000 or fewer', 'eff': 'No effects.', 'miss': '1,200,000 is way more than 1,000. Look lower in the chart.'},
                {'k': 'vlow', 't': 'VERY LOW', 'range': '1,000 to 10,000', 'eff': 'Some people may cough. Shellfish beds may close.', 'miss': '1,200,000 is way more than 10,000. Look lower in the chart.'},
                {'k': 'low', 't': 'LOW', 'range': '10,000 to 100,000', 'eff': 'Coughing. Shellfish beds close. Some fish may die.', 'miss': '1,200,000 is more than 100,000. Look lower in the chart.'},
                {'k': 'medium', 't': 'MEDIUM', 'range': '100,000 to 1,000,000', 'eff': 'Coughing. Shellfish beds close. Fish will probably die.', 'miss': 'Is 1,200,000 more or less than 1,000,000?'},
                {'k': 'high', 't': 'HIGH', 'range': 'more than 1,000,000', 'eff': 'All of that, and the water can change color.'}],
            'level': 'high', 'stamp': 'HIGH', 'sign': 'Checked by Sam Park, Palmetto Field Lab',
            'chartSrc': 'Chart: Florida Fish and Wildlife Conservation Commission (FWC) red tide levels, in cells per liter. Effects in plain words.'},
        'photo': {'img': I('kbrevis-sem'), 'alt': 'One red tide cell under an electron microscope: gray, bumpy, with a groove and a curly tail.',
                  'cap': 'This is ONE red tide cell. Its name is Karenia brevis. Florida scientists took this photo with an electron microscope. The cell had to be dried first, so it was no longer alive.'},
        'credit': FWC + '. Red tide levels: FWC. The microscope view is a model drawn for this lesson, not a photo.',
        'win': 'Sam’s sample: about 1,200,000 red tide cells in one liter. That’s HIGH: enough to kill fish, make people cough and turn the water red-brown. That’s your last clue.',
        'clue': 'scope'},
    'exploreMod': 'scope',
    'tool': {
        'name': 'Hand lens', 'icon': '🔍', 'tab': 'assignment', 'after': '#tab-assignment .activity-card', 'key': '18-tool', 'sim': 'handlens',
        'kicker': 'Bonus · Tool of the Week',
        'teaser': 'Find where a 2x, a 5x and a 10x lens get sharp, then hunt for hidden details.',
        'done': 'You focused a hand lens like a scientist. A hand lens sticker is in your Field Notebook.',
        'why': {'icon': '🔍', 'q': 'What is a hand lens?', 't': 'A curved piece of glass in a frame. The curve bends light, so things look bigger. Scientists carry one outdoors because it needs no batteries.'},
        'handlens': {
            'title': 'Where does each lens get sharp?',
            'todo': ['Drag the lens over the photo. Pick 2x, 5x or 10x.', 'Slide the lens closer or farther until the view is sharp.', 'Find two hidden details on each thing. Put the lens on one and tap Log what I see.'],
            'powers': [{'x': 2, 'f': 12}, {'x': 5, 'f': 5}, {'x': 10, 'f': 2.5}],
            'objects': [
                {'k': 'w', 't': '🐝 Bee wing', 'img': I('bee-wing'), 'w': 30, 'alt': 'A honey bee wing on a table',
                 'details': [{'x': 0.39, 'y': 0.46, 't': 'Veins that make little window shapes', 'power': 5}, {'x': 0.79, 'y': 0.86, 't': 'Fuzzy hairs where the wing meets the body', 'power': 5}]},
                {'k': 's', 't': '🏖️ Sand', 'img': I('sand'), 'w': 34, 'alt': 'A pinch of sand on a table',
                 'details': [{'x': 0.58, 'y': 0.46, 't': 'A clear grain, like a tiny piece of glass', 'power': 10}, {'x': 0.36, 'y': 0.79, 'r': 1, 't': 'A tan grain with a rough, bumpy edge', 'power': 10}]}],
            'q': {'q': 'The stronger the lens, the ___ you hold it to the thing you’re looking at.', 'opts': [
                {'t': 'closer', 'ok': True, 'why': 'Right! The 10x lens got sharp about 2.5 cm away, and the 2x lens about 12 cm away. A stronger lens has more curved glass, so it focuses closer.'},
                {'t': 'farther', 'why': 'Look at your list. Where did 10x get sharp? Where did 2x?'},
                {'t': 'It doesn’t matter', 'why': 'Look at your list. Did every lens get sharp at the same distance?'}]},
            'credit': WING + '. ' + SAND + '.'}},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'A brighter light can help, but that isn’t what magnify means. Which answer is about size?', 'B': 'Cutting something open doesn’t make it look bigger. Which answer is about size?'},
        'q2': {'A': 'An electron microscope is way too much for a whole wing, and it needs a dried sample. What simple tool fits?', 'C': 'Your eyes see the wing, but not the thin veins clearly. What simple tool helps?'},
        'q3': {'B': 'A hand lens is just glass. Does it need batteries?', 'C': 'Hand lenses fit in a pocket. What can’t a hand lens do?'}},
    'flags': {
        'ans-2': [
            {'label': 'the word detail', 're': 'detail'},
            {'label': 'what the hand lens does', 're': 'hand ?lens|magnifying'},
            {'label': 'what the microscope does', 're': 'microscope'}],
        'ans-3': [
            {'label': 'why limits matter', 're': 'can.?t|cannot|not |limit|miss|wrong|only|too '},
            {'label': 'an example', 're': 'hand ?lens|microscope|electron|red tide|cell|bee|sand|leaf|virus|for example|like'},
            {'label': 'a way around it', 're': 'another|different|second|switch|both|instead|stronger|more than one|use a|dried|prepare'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|not always|isn|is not'},
            {'label': 'two pieces of evidence', 'any': ['lens', 'microscope', 'electron', 'light', 'cell', 'count', 'alive', 'living', 'dried', 'dead', 'bee', 'wing', 'leaf', 'sand', 'red tide', '400', 'detail', 'picnic', 'carry'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-2': 15, 'ans-3': 20, 'cer-4': 30},
    'hints': {
        'ans-2': ['Think about Sam’s zoom machine. What did the hand lens show? What did the microscope show?', 'A hand lens shows the whole thing. A microscope shows tiny parts. Why would you want both?', 'Try: A scientist might use a hand lens first to ___. Then a microscope shows more detail, like ___.'],
        'ans-3': ['Think about the electron microscope and Sam’s red tide cells.', 'What couldn’t it do? Which tool did Sam use instead?', 'Try: Limitations matter because ___. For example, ___. A scientist can work around it by ___.'],
        'cer-4': ['First decide: is the most powerful tool ALWAYS the best?', 'Think about the bee wing at the picnic, and about counting living red tide cells.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'The electron microscope can’t look at living cells, so it couldn’t count Sam’s red tide cells.',
                'A light microscope at 400x showed the red tide cells, and they stayed alive.',
                'A hand lens is the right tool for a bee’s wing at a picnic. A microscope would be too much.',
                'An electron microscope showed the tiny groove and tail on one red tide cell.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · meet Sam', 'length': '30–40 s',
                    'script': 'Hi! I’m Sam Park. I’m an engineer, which means I design and build tools to solve problems. I’ll be your guide for the next few weeks. And today, my tools have a real job. Something is wrong at Palmetto Beach. There are dead fish on the sand, and swimmers are coughing. A lifeguard brought me a jar of that water. Let’s find out what’s hiding in it.'},
        'warmup': {'label': 'Warm-Up · the beach alert and the zoom machine (Clue 1)', 'length': '20–30 s',
                   'script': 'First, play the beach alert and tap the three things people noticed. Then try my zoom machine! Each stop on the dial is a stronger tool. Find the new detail at each stop, and keep turning. The last stop is a big surprise.'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Hold up a magnifying glass (or a clear glass of water) for “magnify”; cover one eye with your hand for “limitation”.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · how small can each tool go? (Clue 2)', 'length': '20–30 s',
                  'script': 'Here’s an engineer’s rule: start with the simplest tool that works. Drag each card onto the weakest tool that shows it clearly. Your eyes, a hand lens, a light microscope or an electron microscope. Where do you think a red tide cell goes?'},
        'part2': {'label': 'Part 2 · three tools', 'length': '20–30 s'},
        'part3': {'label': 'Part 3 · pick the right tool (Clue 3)', 'length': '20–30 s',
                  'script': 'My lab got four requests this morning. Read each one carefully. How small is the thing, and what does the question ask you to do? Then drag the right tool onto it. Careful: the most powerful tool can’t do every job.'},
        'explore': {'label': 'Part 4 · count the cells (Clue 4)', 'length': '25–35 s',
                    'script': 'Okay, back to the sample! Put the slide on my microscope, turn to the strongest lens, and focus slowly until the cells look sharp. Then count every cell inside the square. When you’re done, we’ll fill in my lab report and check it against the real chart Florida scientists use.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s',
                       'script': 'Do you have all four clues? Crack the case at the top of this tab: what was hiding in the water, and which tool found it? Then answer two questions, describe three views of one small thing in Part C, and write your CER. Your answers save as you type.'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · three views', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says you should always use the most powerful tool you can find. Hmm. Think about the bee wing at the picnic. Then think about counting living red tide cells. Pick your side, tap two pieces of evidence in the planner, then explain how they prove your claim.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 18.02 (telescopes: tools for things very far away).',
                    'script': 'Case closed! You found red tide hiding in the water, and you picked the right tool for every job. That’s real engineering thinking: the best tool is the one that fits the question. Next time, we flip it around. How do we see things that are really far away, like the Moon and the planets?'},
    },
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'The zoom machine at the last stop (Warm-Up)',
        'Your four tool shelves (The Lesson)',
        'Your four stamped lab requests (The Lesson)',
        'Your lab report with its stamp (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['Three views of one small thing', 'What I saw at 400x', 'Sam’s lab'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 3,
                           'prompts': ['Draw three circles in a row: eyes, hand lens, microscope', 'Draw what you’d see in each circle', 'Label one detail in each circle']}]},
    'hlCoach': copy.deepcopy(Q['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🧫', 'name': 'Red tide sample slide',
                 'line': 'You cracked Case 18, and Sam’s red tide slide goes in your Field Notebook. (A specimen is something a scientist collects to study.) Next time: tools for things very far away.'},
    'notebookTitle': 'Unit 5 · Energy, Motion & Collisions',
    'notebook': [{'lesson': w + '.0' + d} for w in ['18', '19', '20', '21', '22', '23', '24'] for d in ['1', '2']],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You’ll use every one of them in Sam’s lab.',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '.fs-game[data-mod="zoom"]'},
         'label': 'Warm-Up: what your eyes could and couldn’t tell', 'q': 'Warm-Up: What my eyes could tell me about the water, what they could not, and the tool I’d use',
         'title': 'Your turn: what could your eyes tell you about the water?',
         'fields': [{'t': 'One thing my eyes COULD tell me', 'icon': '👁️', 'ph': 'My eyes could see…'},
                    {'t': 'One thing my eyes could NOT tell me', 'icon': '❓', 'ph': 'My eyes could not tell…', 'long': True},
                    {'t': 'The tool I’d use to find out, and why', 'icon': '🔬', 'ph': 'I would use a ___ because…', 'long': True}]},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'hide-nw', 'type': 'hide', 'find': {'sel': '.act-warmup .socratic-q', 'text': 'Notice'}},
        {'id': 'hide-tip', 'type': 'hide', 'find': {'sel': '.act-warmup .callout', 'text': 'Your eyes are amazing'}},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Pick one small Florida thing'},
         'label': 'Part C: Three views of one small thing', 'q': 'Part C: One small Florida thing seen three ways, and the best tool for one question',
         'title': 'Three views of my small thing',
         'fields': [{'t': 'My small Florida thing', 'icon': '🐚', 'ph': 'I picked…'},
                    {'t': 'With my EYES, I see…', 'icon': '👁️', 'ph': 'With my eyes, I see…', 'long': True},
                    {'t': 'With a HAND LENS, I’d see…', 'icon': '🔍', 'ph': 'With a hand lens, I’d see…', 'long': True},
                    {'t': 'With a MICROSCOPE, I’d see…', 'icon': '🔬', 'ph': 'With a microscope, I’d see…', 'long': True},
                    {'t': 'One question about it, and the best tool to answer it', 'icon': '🎯', 'ph': 'My question: … The best tool is ___ because…', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Is the most powerful tool ALWAYS the best?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-2': 'Part B · Question 5', 'ans-3': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] == '18.01': n.update({'icon': '🧫', 'name': 'Red tide sample slide'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'A light microscope can count living red tide cells in a drop of seawater.',
    'key': ['light', 'microscope', 'count', 'living', 'red', 'tide', 'cells'],
    'small': ['A', 'can', 'in', 'a', 'of'],
    'model': 'A scientist might highlight “light microscope”, “living” and “red tide cells”. Those words tell which tool fits the job. Small words like “a” and “of” don’t carry the idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me explain how tools help us see things too small for our eyes?']

# ---------------------------------------------------------------- Spotlight: what lights up as Sam talks
EV = '#tab-assignment .act-body > div:has(> .fs-plan)'
D['cues'] = {
    'welcome': [{'at': '^Sam$', 'sel': '.fs-casecard .fs-case-k', 'fx': 'glow'},
                {'at': '^Palmetto', 'sel': '.fs-casecard .fs-still', 'fx': 'pop', 'tag': '📷 A real red tide'},
                {'at': '^dead', 'sel': '.fs-casecard .fs-notice dl', 'fx': 'glow'},
                {'at': '^jar', 'sel': '.fs-casecard .fs-notice', 'fx': 'wiggle', 'tag': 'Sample 18-A'},
                {'at': '^hiding', 'sel': '.fs-casecard .fs-case-ask', 'fx': 'pop'}],
    'warmup': [{'at': '^beach', 'sel': '.fs-game[data-mod="bulletin"] .fs-bn-play', 'fx': 'point'},
               {'at': '^three', 'sel': '.fs-game[data-mod="bulletin"] .fs-bn-found', 'fx': 'glow'},
               {'at': '^zoom', 'sel': '.fs-game[data-mod="zoom"] .fs-zm-lens', 'fx': 'pop', 'scroll': True},
               {'at': '^dial', 'sel': '.fs-zm-dial', 'fx': 'glow'},
               {'at': '^last', 'sel': '.fs-zm-dial .fs-zm-stop:last-of-type', 'fx': 'wiggle', 'tag': '⚡ Surprise!'}],
    'part1': [{'at': '^simplest', 'sel': '.fs-game[data-mod="mitsort"] .fs-why', 'fx': 'glow'},
              {'at': '^Drag', 'sel': '.fs-mk-deck', 'fx': 'glow'},
              {'at': '^eyes', 'sel': '.fs-mk-shelf[data-k="eye"]', 'fx': 'pop', 'scroll': True},
              {'at': '^hand', 'sel': '.fs-mk-shelf[data-k="lens"]', 'fx': 'pop'},
              {'at': '^light', 'sel': '.fs-mk-shelf[data-k="light"]', 'fx': 'pop'},
              {'at': '^electron', 'sel': '.fs-mk-shelf[data-k="em"]', 'fx': 'pop'},
              {'at': '^red', 'sel': '.fs-mk-card[data-id="redcell"]', 'fx': 'wiggle', 'tag': 'Where does it go?'}],
    'part3': [{'at': '^four', 'sel': '.fs-tp-jobs', 'fx': 'glow', 'scroll': True},
              {'at': '^small', 'sel': '.fs-tp-job[data-id="wing"]', 'fx': 'pop'},
              {'at': '^question', 'sel': '.fs-tp-job[data-id="count"] p', 'fx': 'trace'},
              {'at': '^drag', 'sel': '.fs-tp-tools', 'fx': 'glow'},
              {'at': '^powerful', 'sel': '.fs-tp-tool[data-k="em"]', 'fx': 'wiggle', 'tag': 'Not every job!'}],
    'explore': [{'at': '^slide', 'sel': '.fs-vm-place', 'fx': 'point'},
                {'at': '^strongest', 'sel': '.fs-vm-ob .fs-in-chip:last-child', 'fx': 'pop', 'tag': '40x'},
                {'at': '^focus', 'sel': '.fs-vm-fk', 'fx': 'glow'},
                {'at': '^count', 'sel': '.fs-vm-eye', 'fx': 'pop'},
                {'at': '^report', 'sel': '.fs-vm-steps', 'fx': 'glow'}],
    'assignment': [{'at': '^clues', 'sel': '.fs-board', 'fx': 'glow'},
                   {'at': '^Crack', 'sel': '.fs-solve', 'fx': 'pop'},
                   {'at': '^two', 'sel': '#tab-assignment .pq', 'fx': 'glow', 'all': True, 'scroll': True},
                   {'at': '^three', 'sel': '#tab-assignment .fs-in-frame', 'fx': 'glow', 'scroll': True},
                   {'at': '^CER', 'sel': '#tab-assignment .fs-cer', 'fx': 'glow', 'scroll': True}],
    'evidence': [{'at': '^classmate', 'sel': EV + ' > p', 'i': 0, 'fx': 'trace'},
                 {'at': '^bee', 'sel': '.fs-plan .fs-opt', 'i': 4, 'fx': 'glow'},
                 {'at': '^counting', 'sel': '.fs-plan .fs-opt', 'i': 2, 'fx': 'glow'},
                 {'at': '^side', 'sel': '.fs-plan .fs-plan-row', 'i': 0, 'fx': 'pop'},
                 {'at': '^evidence', 'sel': '.fs-plan .fs-plan-row', 'i': 1, 'fx': 'glow'},
                 {'at': '^explain', 'sel': '.fs-cer .fs-cer-row', 'i': 2, 'fx': 'glow', 'scroll': True}],
    'closing': [{'at': '^closed', 'sel': '.fs-specimen', 'fx': 'pop', 'scroll': True},
                {'at': '^Next', 'sel': '#tab-assignment .callout-tip', 'fx': 'glow'}],
}
D['cueWords'] = json.load(open('cuewords.json', encoding='utf-8'))  # word times from ElevenLabs Scribe transcripts of the clips
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
