#!/usr/bin/env python3
"""Writes data.json and fixes.json for 27.02 (run from this folder). Case 27 part 2 "Next Year's Trophy" (Dr. Priya Nair, Unit 6, Palmetto Springs):
the real trophy is found; now Mr. Ortiz orders a NEW trophy with three needs (survives rain, won't break if dropped, under 500 g). The engraver sends four designs.
New: case.order (order form + four design cards with part masses), takeapart (Warm-Up: the toy robot on two scales, SC.4.P.8.3), stickers (Part 1: one material,
many property stickers), rigs (Part 2: four job test rigs), tally (the wow: the real trophy's parts add up to 412 g), driplab (Part 4 = the old Explore: drip and
bend five swatches into a classification table), sunnote (after the solve: the July-sun twist, swap the handles and re-add), photos[].afterSolve (the NASA heat-tile
photo, opens after the solve). No tool (27.01 has the pan balance). SCRIPTS ONLY: clip scripts written and budgeted, nothing generated."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
O = json.load(open('../27-01/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)
def I(n, ext='jpg'): return 'images/27-02-' + n + '.' + ext

# ---------------------------------------------------------------- labels (standing approval)
fx('fix', 'unit label: “Ecosystems & Energy” is a leftover; the plan puts Module 27 in Unit 6 “Matter, Magnets, and Changes”', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Matter, Magnets &amp; Changes</div>')
fx('fix', 'materials and properties are physical science, not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standards label: the plan’s CPALMS codes; TEKS is a Texas code that isn’t in the plan', '<div class="info-value">SC.4.N.1.1, SC.4.P.8.1, SC.4.P.8.3 · TEKS 4.6(A), 4.6(B), 4.6(C)</div>', '<div class="info-value">SC.4.N.1.1, SC.4.P.8.1, SC.4.P.8.3</div>')
fx('fix', 'standards detail: density, mixtures and solutions are Grade 5 (SC.5.P.8); the plan row is sorting materials + mass of whole = sum of parts', '<div class="info-detail">Properties, Density, Mixtures & Solutions</div>', '<div class="info-detail">Sorting materials &amp; mass of parts</div>')
fx('fix', 'quarter label in the footer: week 27 is Q4 in the Canvas plan (the header already says Q4)', 'Science &middot; Quarter 3 &middot; Student Lesson Page', 'Science &middot; Quarter 4 &middot; Student Lesson Page')

# ---------------------------------------------------------------- ticked fixes (Bethany, 26 Nov 2026)
fx('fix', '22.01 leftover: the Warm-Up title named the toaster lesson', '<div class="act-title">🌅 Warm-Up: What Goes In, What Comes Out?</div>\n        <div class="act-subtitle">A familiar device, a hidden change</div>',
   '<div class="act-title">🌅 Warm-Up: Take It Apart</div>\n        <div class="act-subtitle">Does anything get lost?</div>')
fx('fix', '22.01 leftover: the toaster warm-up → take it apart (SC.4.P.8.3, the plan’s required coverage)',
   '<p>Think about a toaster. You drop in cold bread. A minute later, you pull out hot toast.</p>',
   '<p>A toy robot built from snap-together blocks sits on a kitchen scale: 60 grams. Now pull it apart into a pile of pieces. Will the pile weigh more, less or the same?</p>')
fx('fix', '22.01 leftover: the toaster sketch → the take-apart test (played and answered on the page)',
   "<p>In your notebook, draw a quick sketch of a toaster. On one side, label what goes IN. On the other, label what comes OUT. (Hint: bread on both sides — but something invisible is also going in. What is it?)</p>",
   '<p>Lock in your prediction. Then test it right here.</p>')
fx('fix', '22.01 leftover: Notice & Wonder about the toaster',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Notice &amp; Wonder</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover: “energy can CONVERT … toasters” callout',
   r'<div class="callout callout-tip">\s*<span class="callout-icon">💡</span>\s*<p>Today you\'ll learn that energy can CONVERT.*?</p>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover: “Device” meant converting energy; this lesson’s devices are jobs that need the right materials',
   'A tool or machine designed to do a job. Most devices convert energy from one form to another — a flashlight, a toaster, a fan are all devices.',
   'A tool or machine made to do a job. An umbrella, a sponge and a frying pan are devices: each one needs materials with the right properties.')
fx('fix', '22.01 leftover: the Stop & Reason asked about “the three devices above” (no devices on this page)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', '9.01 leftover: Part C was a food chain; the checklist already describes a material-choice project', '🎨 Part C &mdash; Build Your Own Food Chain', '🎨 Part C &mdash; Choose a Material for a Job')
fx('fix', '9.01 leftover: Part C task → the checklist’s material-choice project (typed and sketched on the page)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Pick a real job at home: a raincoat, a phone stand, a kitchen towel or a dog bowl. Name 3 properties the material needs. Pick 2 materials that could work. Then choose the winner and prove it in one sentence.</p>', True)
fx('fix', '9.01 leftover: Reflect asked about a hawk; the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'supply list: what the Warm-Up and the drip and bend lab can use at home', r'<span class="need-chip"><span>✏️</span>Colored pencils</span>',
   '<span class="need-chip"><span>🧱</span>Optional: snap-together blocks and a kitchen scale</span><span class="need-chip"><span>💧</span>Optional: a spoon of water, foil, a paper towel, a scrap of cloth</span>', True)
fx('fix', 'Grade 5 box (ticked): “Mixtures, Solutions & Relative Density” is not in the plan row (SC.5.P.8.3 and density are 5th grade). Part 3 now teaches the plan’s required SC.4.P.8.3 (mass of the whole = sum of the parts), from the page’s own Science Connection, + the cropped job picture moved here, after the rigs game',
   r'<div style="background:#EAF8FD;border:2px solid #B8E0F8;[^>]*>\s*<p[^>]*>🧪 Mixtures, Solutions &amp; Relative Density</p>.*?</div>\s*', True and
   ('<div class="lesson-figure scroll-reveal">\n        <div class="lesson-figure-label">🎯 Job → Material</div>\n        <img src="images/27-02-job-to-material.png" alt="Three jobs matched to a material. An umbrella needs flexible and waterproof: plastic. A sponge needs absorbent and flexible: foam. A bridge needs rigid and strong: steel." />\n'
    '        <div class="lesson-figure-caption"><strong>The job decides.</strong> A material that is right for one job can be wrong for another.</div>\n      </div>\n\n      '
    + H3 + 'Part 3 · Mass and Volume Are Properties, Too</h3>\n      <p>Mass is how much matter an object has. Volume is how much space it takes up. Engineers check both: a trophy for a little kid needs a small mass.</p>\n'
    '      <p>Here is a surprising fact: take something apart, and the mass of the whole equals the sum of the masses of its parts. Nothing is lost. You saw it with the toy robot. Now try it with the real trophy:</p>\n\n      '), True)
F[-1]['old'] = r'<div style="background:#EAF8FD;border:2px solid #B8E0F8;[^>]*>\s*<p[^>]*>🧪 Mixtures, Solutions & Relative Density</p>.*?</div>\s*'
fx('fix', 'picture (ticked): the infographic’s left half puts each material in ONE group, which contradicts Part 1 (one material, many groups). The right half (job → material) is kept as a cropped copy and moved after the rigs game, so it doesn’t give the rigs’ answers away. (The original file stays in images/.)',
   r'<div class="lesson-figure scroll-reveal">\s*<div class="lesson-figure-label">🗂️ Sort, Then Choose</div>.*?<div class="lesson-figure-caption"><strong>Sort first\. Choose second\.</strong>.*?</div>\s*</div>\s*', '', True)
fx('fix', 'tap diagram (ticked): the Four Material-Job Matches tap diagram is replaced by the job test rigs; with it go Observe & Reason (Part B question 5 asks the same), the spacesuit Amazing Fact, the hurricane Florida connection (the “shingle clips” line is shaky: hurricane clips hold roof trusses), the Smart materials Go Deeper and the Science Connection (its mass idea is now Part 3)',
   r'<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">Four Material-Job Matches</h3>.*?(?=<div class="tab-next-wrap">)', '', True)
fx('fix', 'shaky fact (ticked): swimsuit fabric does soak up some water (“not absorb water” is wrong). Cut for length rather than reworded: the three jobs above it match the rigs',
   r'\s*<li><strong>Florida swimsuit:</strong> needs to dry quickly AND not absorb water.*?</li>', '', True)

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; no dashes', r"<p>Hold this question in your head as you work\. By the end of the lesson.*?</p>",
   "<p>Keep this question in mind. By the end, you’ll sort materials by their properties and pick the best one for a job.</p>", True)
fx('plain', 'cut filler; no dash', r"<p>These six words show up all through the lesson\. <strong>Tap a card to flip it</strong>.*?</p>",
   "<p><strong>Tap a card to flip it</strong> and read what the word means.</p>", True)
fx('plain', 'Word Wall: no dash', 'To sort items into groups based on a shared property — like sorting all metals together or all flexible things together.', 'To sort items into groups by a shared property, like putting all the bendy things together.')
fx('plain', 'Word Wall: no dash, plain words', 'A trait of a material — color, hardness, flexibility, magnetism, waterproof, conducts heat.', 'A trait of a material: its color, how hard it is, whether it bends, whether it keeps water out.')
fx('plain', 'Word Wall: no dash', 'A specific kind of matter — wood, metal, plastic, rubber, paper, cloth. Each has its own set of properties.', 'A kind of matter, like wood, metal, plastic, rubber, paper or cloth. Each has its own set of properties.')
fx('plain', 'define magnetism where it first shows up', 'You can sort by color, hardness, magnetism, or whether', 'You can sort by color, hardness, magnetism (sticking to a magnet), or whether')
fx('plain', 'Part 1: one example; the stickers game lets students find the rest instead of reading the answers',
   r'<p>For example, rubber is flexible AND waterproof\. Wood is rigid AND absorbent\..*?</p>',
   '<p>Rubber, for example, is flexible AND waterproof. So which groups does each material belong to? Test it with stickers.</p>', True)
fx('cut', 'lean: the Stop & Think (flexible vs rigid) is played by the stickers game',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: the misconception paragraph (“one best material”) is played by the rigs game, where steel wins one job and fails three',
   r'\s*<p><strong>Common misconception:</strong> Some people think there\'s ONE "best material".*?</p>', '', True)
fx('cut', 'lean: Key Concept (the rigs game and Part 2 teach it)',
   r'\s*<div style="background:#FFF6E5;border:2\.5px solid #F0C97A;[^>]*>\s*<div[^>]*>⭐ Key Concept</div>.*?</p>\s*</div>', '', True)
fx('plain', 'Part B question 5 now points at the rigs (the tap diagram is gone)', 'Pick ONE job from the diagram (umbrella, sponge, bridge, frying pan handle).', 'Pick ONE job from the test rigs (umbrella, sponge, bridge, frying pan handle).')
fx('plain', 'Part B question 5 label (Gathered Answers)', 'data-label="Pick ONE job from the diagram (umbrella, sponge, b..."', 'data-label="One job: two properties and the best material"')
fx('plain', 'Part B question 6 label (Gathered Answers)', 'data-label="A friend wants to build a boat out of paper. Will ..."', 'data-label="A paper boat: will it work?"')
fx('plain', 'no dash', '<em>"There\'s one best material for everything — steel."</em>', '<em>"There\'s one best material for everything: steel."</em>')
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'closing: no dashes', 'Engineers everywhere — from architects to spacesuit designers — do exactly this. Next module, we move to MAGNETS — another set of properties that opens up its own world of design.',
   'Engineers everywhere, from builders to spacesuit designers, do exactly this. Next week: MAGNETS, a whole new set of properties to explore.')

# ---------------------------------------------------------------- lean cuts
fx('cut', 'Part 4 = the old Explore (Classify and Choose → the drip and bend lab, a classification table); the next button goes to Self-Check',
   '''<div class="tab-next-wrap">
        <button class="tab-next-btn" onclick="switchTab('explore')">Continue to 🔬 Explore →</button>''',
   H3 + 'Part 4 · The Drip and Bend Lab</h3>\n      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">Time for an investigation (a test you run to answer a question): five materials, two tests. Drip water on each one, then bend it. Your results go into a classification table (a chart that sorts evidence into rows and columns).</p>\n  <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>')
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its sort-and-test steps live on as the drip and bend lab; its choose-a-job step is Part C; the Hubble fact, the phone-stand Think like a scientist and the recycling Go Deeper go with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 7 removed (Bethany kept 5 and 6; the CER argues the same idea)', r'<div class="pq">\s*<span class="pq-num"[^>]*>7</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C checklist ends with the required sketch', 'A material-choice project with job, 3 properties, 2 candidate materials, and a claim+evidence sentence picking the winner.',
   'A job, 3 properties it needs, 2 materials that could work, and one sentence that picks the winner with evidence. Plus your labeled sketch.')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether one material is best for everything, supported with two pieces of evidence.',
   '<strong>Use Your Evidence:</strong> My claim about whether one material is best for everything, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a 9.01 leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Download your field journal (it has your answers and your sketch) and upload it to the Canvas assignment. Or copy your Gathered Answers (above) into Canvas.', True)

# ---------------------------------------------------------------- the story
PRIYA = O['crew']['priya']
DESIGNS = [
    {'tag': 'DESIGN A', 'icon': '🥇', 't': 'All brass', 'parts': [['Cup', 'brass', 300], ['2 handles', 'brass', 90], ['Base', 'brass', 210], ['Screws', 'steel', 6]]},
    {'tag': 'DESIGN B', 'icon': '💎', 't': 'Glass and wood', 'parts': [['Cup', 'glass', 220], ['2 handles', 'glass', 40], ['Base', 'wood', 150]]},
    {'tag': 'DESIGN C', 'icon': '🥈', 't': 'Aluminum and plastic', 'parts': [['Cup', 'aluminum', 100], ['2 handles', 'aluminum', 28], ['Base', 'hard plastic', 120], ['Screws', 'steel', 6]]},
    {'tag': 'DESIGN D', 'icon': '📦', 't': 'Cardboard', 'parts': [['Cup', 'cardboard', 40], ['2 handles', 'cardboard', 10], ['Base', 'cardboard', 60]]},
]
TOT = {d['tag']: sum(p[2] for p in d['parts']) for d in DESIGNS}
assert TOT == {'DESIGN A': 606, 'DESIGN B': 410, 'DESIGN C': 254, 'DESIGN D': 110}, TOT
ROBOT = [{'id': 'head', 'icon': '🟥', 't': 'Head', 'g': 8, 'c': '#E8636B'}, {'id': 'body', 'icon': '🟦', 't': 'Body', 'g': 20, 'c': '#2D7AA6'},
         {'id': 'armL', 'icon': '🟨', 't': 'Left arm', 'g': 6, 'c': '#F5C842'}, {'id': 'armR', 'icon': '🟨', 't': 'Right arm', 'g': 6, 'c': '#F5C842'},
         {'id': 'legL', 'icon': '🟩', 't': 'Left leg', 'g': 10, 'c': '#2F7A55'}, {'id': 'legR', 'icon': '🟩', 't': 'Right leg', 'g': 10, 'c': '#2F7A55'}]
assert sum(p['g'] for p in ROBOT) == 60
TROPHY = [{'id': 'cup', 'icon': '🏆', 't': 'Brass cup', 'g': 254}, {'id': 'hl', 'icon': '🪝', 't': 'Left handle', 'g': 41}, {'id': 'hr', 'icon': '🪝', 't': 'Right handle', 'g': 41},
          {'id': 'stem', 'icon': '🟨', 't': 'Stem', 'g': 18}, {'id': 'base', 'icon': '⬛', 't': 'Base', 'g': 52}, {'id': 'screws', 'icon': '🔩', 't': 'Screws', 'g': 6}]
assert sum(p['g'] for p in TROPHY) == 412
D = {
    'lesson': '27.02', 'week': 27, 'day': 2, 'guide': 'priya', 'prefix': 'g4sci-27-2', 'manifestKey': '27-02',
    'paths': P['paths'], 'crew': {'priya': PRIYA},
    'expedition': {'num': 27, 'title': 'Next Year’s Trophy'},
    'ambient': {'icon': '🔧', 'label': 'The engraver’s workshop'},
    'case': {
        'num': 27, 'title': 'Next Year’s Trophy', 'style': 'order',
        'hook': 'Dr. Priya Nair here. You found the real trophy! Now Mr. Ortiz wants a NEW one for next year. The engraver, R. Vega, sent four designs. Only one fits every need.',
        'order': {'head': 'PALMETTO SPRINGS DUCK DERBY', 'title': 'Trophy order form · for next year',
                  'rows': [['Job', 'A trophy for the winning duck’s owner'], ['Need 1', 'It sits outside by the pond, so it must survive rain'],
                           ['Need 2', 'It must not break if a little kid drops it'], ['Need 3', 'A 5-year-old must lift it: under 500 grams in all']],
                  'sign': 'Mr. Ortiz, Derby organizer', 'designsLabel': 'R. Vega’s four designs (add up each one!)', 'totalWord': 'Total', 'designs': DESIGNS},
        'stills': [],
        'question': 'Which design should R. Vega build for next year’s trophy?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'takeapart', 'icon': '🧱', 'where': 'Warm-Up: take it apart', 't': 'Taking something apart does not change its mass. The robot’s parts added up to 60 g, the same as the whole. So add up a design’s parts to find its total.'},
            {'id': 'stickers', 'icon': '🏷️', 'where': 'The Lesson, Part 1: sticker every property', 't': 'One material can belong to many groups. Foil bends AND keeps water out. Look for the material with every property the job needs.'},
            {'id': 'rigs', 'icon': '🧪', 'where': 'The Lesson, Part 2: the job test rigs', 't': 'The job decides. Steel held up the bridge but failed the umbrella, the sponge and the pan handle. Heavy and strong is not always best.'},
            {'id': 'driplab', 'icon': '💧', 'where': 'The Lesson, Part 4: the drip and bend lab', 't': 'A classification table shows which materials pass EVERY test at once. Only plastic wrap and foil kept water out AND bent.'},
        ],
        'solve': {
            'title': 'Which design fits every need?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Design A, all brass. Heavy and strong must be best.', 'why': 'Check Clues 1 and 3. Add up Design A: 606 grams. That is over the 500-gram limit, and heavy is not the same as best.'},
                {'t': 'Design B, glass and wood. The shiniest, at 410 grams.', 'why': 'Check Clue 3. The order says it must not break if a little kid drops it. Glass shatters.'},
                {'t': 'Design C, aluminum and plastic. Rain can’t soak in, it won’t shatter, and it adds up to 254 grams.', 'right': True,
                 'why': 'Case cracked! Design C passes all three needs at once, just like a winner in your classification table.'},
                {'t': 'Design D, cardboard. The lightest: only 110 grams.', 'why': 'Check Clues 2 and 4. Cardboard soaks up water. One rainy derby and the trophy turns to mush.'},
            ]},
    },
    'takeapart': {
        'afterText': 'Then test it right here.', 'kicker': 'Warm-Up game', 'title': 'Take it apart',
        'why': {'icon': '🧱', 'q': 'Why take a toy apart?', 't': 'A pile of pieces LOOKS smaller. Does it really have less mass?'},
        'todo': ['Lock in your prediction.', 'Drag each part onto Scale 2, or tap the part and then the scales.', 'Watch the scales and the adding tape.'],
        'alt': 'Two model kitchen scales. A toy robot made of colored blocks stands on Scale 1. Scale 2 is empty.',
        'model': 'A model test. Try it at home with snap-together blocks and a kitchen scale.',
        'predictQ': 'The whole robot weighs 60 grams. The pile of parts will weigh…',
        'predictOpts': [{'k': 'more', 't': 'More than 60 g'}, {'k': 'less', 't': 'Less than 60 g'}, {'k': 'same', 't': 'The same: 60 g'}],
        'predictFirst': 'Lock in your prediction first!', 'lockedWord': 'My prediction',
        'parts': ROBOT, 's1': 'Scale 1 · the robot', 's2': 'Scale 2 · the pile',
        'tapLine': '',
        'tapeLabel': 'The adding tape', 'sumWord': 'On Scale 2 so far',
        'results': {'same': 'You called it! The pile weighs exactly 60 g, the same as the whole robot.',
                    'more': 'Surprise! The pile weighs exactly 60 g, the same as the whole robot. Spreading out added nothing.',
                    'less': 'Surprise! The pile weighs exactly 60 g, the same as the whole robot. Nothing got lost.'},
        'q': 'Why does the pile weigh the same as the whole robot?',
        'opts': [{'t': 'Taking it apart did not add or remove any matter. The whole equals the sum of its parts.', 'ok': True},
                 {'t': 'The scale must be broken.', 'miss': 'Check the tape: 8 + 20 + 6 + 6 + 10 + 10. Add it up yourself.'},
                 {'t': 'Spread-out pieces always weigh more.', 'miss': 'Look at Scale 2. Spread out, the pieces still added up to 60 g.'}],
        'win': 'The whole equals the sum of its parts. Nothing was lost! Clue 1!', 'clue': 'takeapart'},
    'stickers': {
        'afterText': 'Test it with stickers.', 'kicker': 'Part 1 game', 'title': 'Sticker every true property',
        'why': {'icon': '🏷️', 'q': 'Why stickers?', 't': 'Each sticker is a group. A material can wear many stickers.'},
        'todo': ['Drag a sticker onto a material, or tap the sticker and then the material.', 'Each card shows how many stickers fit it. Fill every spot.', 'A wrong sticker bounces off. Read why.'],
        'sheetLabel': 'Your sticker sheet (stickers never run out)',
        'stickers': [{'k': 'bends', 'icon': '🤸', 't': 'Bends'}, {'k': 'stiff', 'icon': '🧱', 't': 'Stays stiff'}, {'k': 'water', 'icon': '☔', 't': 'Waterproof'},
                     {'k': 'soak', 'icon': '🧽', 't': 'Soaks up water'}, {'k': 'magnet', 'icon': '🧲', 't': 'Sticks to a magnet'}],
        'mats': [
            {'id': 'rubber', 'icon': '➰', 'name': 'Rubber band', 'has': ['bends', 'water'], 'miss': {'stiff': 'Stretch a rubber band. It bends and stretches easily.', 'soak': 'Water rolls right off rubber. It can’t soak in.', 'magnet': 'Rubber has no iron in it. A magnet won’t grab it.'}},
            {'id': 'foil', 'icon': '✨', 'name': 'Aluminum foil', 'has': ['bends', 'water'], 'miss': {'stiff': 'Crumple foil in your hand. It bends easily.', 'soak': 'Water beads up on foil. It can’t soak in.', 'magnet': 'Foil is a metal, but aluminum does NOT stick to a magnet. Try it on your fridge!'}},
            {'id': 'wood', 'icon': '🪵', 'name': 'Wood block', 'has': ['stiff', 'soak'], 'miss': {'bends': 'Try to bend a block of wood. It stays stiff.', 'water': 'Bare wood soaks up water slowly. That’s why decks get painted.', 'magnet': 'Wood has no iron in it. A magnet slides right off.'}},
            {'id': 'glass', 'icon': '🫙', 'name': 'Glass jar', 'has': ['stiff', 'water'], 'miss': {'bends': 'Glass can’t bend. It breaks first!', 'soak': 'Water can’t soak into glass. That’s why we drink from it.', 'magnet': 'Glass has no iron in it. A magnet won’t stick.'}},
            {'id': 'paper', 'icon': '📄', 'name': 'Paper', 'has': ['bends', 'soak'], 'miss': {'stiff': 'Hold up a sheet of paper. It flops over: it bends.', 'water': 'Spill on paper and it gets soggy. Water soaks in.', 'magnet': 'Paper has no iron in it. A magnet won’t grab it.'}},
            {'id': 'wrap', 'icon': '🫧', 'name': 'Plastic wrap', 'has': ['bends', 'water'], 'miss': {'stiff': 'Plastic wrap is floppy. It bends.', 'soak': 'Water slides off plastic wrap. That’s why it keeps food fresh.', 'magnet': 'Plastic has no iron in it. A magnet won’t stick.'}},
            {'id': 'nail', 'icon': '🔩', 'name': 'Iron nail', 'has': ['stiff', 'water', 'magnet'], 'miss': {'bends': 'Try to bend a nail with your fingers. It stays stiff.', 'soak': 'Water can’t soak into iron. (It can rust on the outside, though!)'}},
            {'id': 'cloth', 'icon': '🧣', 'name': 'Cotton cloth', 'has': ['bends', 'soak'], 'miss': {'stiff': 'A cotton shirt folds and drapes. It bends.', 'water': 'Spill on a cotton shirt and it gets wet through. It soaks water up.', 'magnet': 'Cotton has no iron in it. A magnet won’t grab it.'}},
        ],
        'againMiss': '{m} already wears that sticker.', 'countWord': 'materials wearing every sticker that fits',
        'mostLine': '{names} wore the most stickers: {n}. Every material wore at least two. One material, many groups!',
        'q': 'The rubber band wore BOTH Bends and Waterproof. What does that tell you?',
        'opts': [{'t': 'One material can belong to more than one group. Which group matters depends on the job.', 'ok': True},
                 {'t': 'Rubber should only be in one group.', 'miss': 'Look at the rubber band card. Both stickers stuck, because both are true.'},
                 {'t': 'Waterproof things can’t bend.', 'miss': 'Look at the plastic wrap and the foil. Both bend AND keep water out.'}],
        'win': 'One material, many groups. Sort by the property the job needs. Clue 2!', 'clue': 'stickers'},
    'rigs': {
        'afterText': 'it works in any weather', 'kicker': 'Part 2 game', 'title': 'The job test rigs',
        'why': {'icon': '🧪', 'q': 'What is a test rig?', 't': 'A setup that makes a material do the job: rain on an umbrella, a truck on a bridge.'},
        'todo': ['Pick a job tab. Read what it needs.', 'Drag a material into the rig (or tap it, then the rig). Press Run the test.', 'If it fails, swap. Pass all four jobs, then try steel in every rig.'],
        'trayLabel': 'Materials',
        'mats': [{'k': 'paper', 'icon': '📄', 't': 'Paper', 'c': '#F3EBD8'}, {'k': 'plastic', 'icon': '🛍️', 't': 'Plastic', 'c': '#4FA3D9'}, {'k': 'foam', 'icon': '🧽', 't': 'Foam', 'c': '#F4D35E'},
                 {'k': 'steel', 'icon': '🔩', 't': 'Steel', 'c': '#8C959B'}, {'k': 'wood', 'icon': '🪵', 't': 'Wood', 'c': '#B5835A'}],
        'jobs': [
            {'id': 'umbrella', 'icon': '☂️', 't': 'Umbrella', 'needs': 'bends to fold up + waterproof', 'ok': ['plastic'], 'leak': ['paper', 'foam', 'wood'],
             'fx': {'paper': '💧 soaked through!', 'foam': '💧 soaked through!', 'steel': '🏋️ too heavy, won’t fold', 'wood': '🪵 won’t fold'}, 'okFx': '☺ dry',
             'lines': {'plastic': 'Plastic bends to fold up, and the rain rolls right off.', 'paper': 'Rain soaked right through the paper, and it sagged and tore.',
                       'foam': 'Foam soaks up rain like a sponge. Soggy and heavy!', 'steel': 'Waterproof, yes. But steel is too stiff to fold and too heavy to hold up. Heavier is not better.',
                       'wood': 'Wood can’t fold up, and bare wood soaks up rain.'}},
            {'id': 'sponge', 'icon': '🧽', 't': 'Sponge', 'needs': 'soaks up water + squishes into corners', 'ok': ['foam'],
             'fx': {'paper': '🌊 falls apart', 'plastic': '🌊 still wet', 'steel': '🌊 still wet', 'wood': '🌊 still wet'}, 'okFx': '✨ soaked up',
             'lines': {'foam': 'Foam is full of tiny holes that soak up the spill, and it squishes back into shape.', 'paper': 'Paper soaks up a little, then falls apart when you scrub.',
                       'plastic': 'Water slides right off plastic. The spill stays put.', 'steel': 'Steel can’t soak up a single drop. The spill stays.', 'wood': 'Wood is too stiff to squish into corners, and it soaks up water very slowly.'}},
            {'id': 'bridge', 'icon': '🌉', 't': 'Bridge beam', 'needs': 'stays stiff + strong enough for a truck', 'ok': ['steel', 'wood'],
             'fx': {'paper': '⚠️ it folded!', 'foam': '⚠️ it sagged!', 'plastic': '⚠️ it sagged!'}, 'okFx': '✓ made it across',
             'lines': {'steel': 'Steel stays stiff and strong under the heavy truck.', 'wood': 'A thick wooden beam is stiff and strong too. Lots of small bridges are made of wood.',
                       'foam': 'Foam squished and sagged as soon as the truck rolled on.', 'paper': 'Paper folded right under the truck.', 'plastic': 'This thin plastic bent and sagged under the load.'}},
            {'id': 'handle', 'icon': '🍳', 't': 'Frying pan handle', 'needs': 'stays cool enough to hold + stiff', 'ok': ['wood', 'plastic'], 'hot': ['steel'],
             'fx': {'steel': '🔥 too hot to hold!', 'foam': '❌ melts and flops', 'paper': '❌ floppy, could burn'}, 'okFx': '✋ cool enough',
             'lines': {'wood': 'Wood carries heat slowly, so the handle stays cool enough to hold.', 'plastic': 'Heat-proof plastic carries heat slowly too, so the handle stays cool enough to hold.',
                       'steel': 'Steel carries heat fast. The handle got too hot to hold. Strong is not the same as right!', 'foam': 'Foam is soft and floppy, and it melts near a hot stove.',
                       'paper': 'Paper is floppy, and it could catch fire next to a stove.'}},
        ],
        'mustTry': 'steel', 'mustLine': 'All four jobs passed! One more test: put {m} in every rig. Can the strongest material win them all? Still to try: {jobs}.',
        'runBtn': '▶ Run the test', 'dropLine': 'Put a material in the rig', 'passWord': 'passes!', 'failWord': 'fails.', 'needWord': 'The job needs', 'inRigWord': 'In the rig',
        'countWord': 'jobs passed', 'logLabel': 'Test results', 'cols': ['Job', 'It needs', 'Passed'],
        'q': 'Steel held up the bridge, but it failed the other three jobs. What does that prove?',
        'opts': [{'t': 'There is no one best material. The job decides which properties matter.', 'ok': True},
                 {'t': 'Steel is still the best material.', 'miss': 'Check your tests. Steel failed the umbrella, the sponge and the pan handle.'},
                 {'t': 'The heaviest material always wins.', 'miss': 'Steel is the heaviest material here, and it lost three jobs. Heavy is not the same as right.'}],
        'win': 'Four jobs, four winners. The JOB decides the material. Clue 3!', 'clue': 'rigs'},
    'tally': {
        'afterText': 'Now try it with the real trophy:', 'kicker': 'Wow!', 'title': 'The 412-gram puzzle',
        'why': {'icon': '🔧', 'q': 'Why is the trophy in pieces?', 't': 'R. Vega took the real trophy apart to engrave it. Mr. Ortiz is worried: the pile LOOKS smaller. Is brass missing?'},
        'todo': ['Tap each part on the bench.', 'Compare the total with the whole trophy: 412 grams.'],
        'benchLabel': 'R. Vega’s bench', 'parts': TROPHY, 'tapeHead': 'The adding tape', 'totalWord': 'Total', 'emptyLine': 'Tap a part to print it.',
        'matchLine': 'The parts add up to {x} g: exactly what the whole trophy weighed. Nothing went missing!',
        'q': 'Mr. Ortiz thought some brass was missing because the pile looked smaller. What do you tell him?',
        'opts': [{'t': 'Nothing is missing. The parts add up to 412 g, the mass of the whole trophy.', 'ok': True},
                 {'t': 'Some brass got lost when it came apart.', 'miss': 'Check the tape. Every gram is there: 412.'},
                 {'t': 'A pile always weighs less than the whole.', 'miss': 'The robot pile in the Warm-Up weighed the same as the whole robot. So does this one.'}],
        'done': 'Wow! The whole equals the sum of its parts, for a toy robot AND a real brass trophy.'},
    'driplab': {
        'afterText': 'sorts evidence into rows and columns).', 'kicker': 'Part 4 game', 'title': 'The drip and bend lab',
        'why': {'icon': '📋', 'q': 'What is a classification table?', 't': 'A chart with a row for each material and a column for each test.'},
        'todo': ['Press Drip water, watch, and tap what you saw. Then Bend it.', 'Test all five. Then read your table.'],
        'model': 'A model lab table. Try it at home with a spoon of water.',
        'mats': [{'id': 'foil', 'icon': '✨', 't': 'Foil', 'c': '#C9D1D6', 'water': 'beads', 'bend': 'bends'},
                 {'id': 'towel', 'icon': '🧻', 't': 'Paper towel', 'c': '#FFFFFF', 'water': 'soaks', 'bend': 'bends'},
                 {'id': 'wrap', 'icon': '🫧', 't': 'Plastic wrap', 'c': '#DDEFF8', 'water': 'beads', 'bend': 'bends'},
                 {'id': 'cloth', 'icon': '🧣', 't': 'Cotton cloth', 'c': '#E8A0A8', 'water': 'soaks', 'bend': 'bends'},
                 {'id': 'card', 'icon': '📦', 't': 'Cardboard', 'c': '#C99B66', 'water': 'soaks', 'bend': 'stiff'}],
        'tests': {'water': {'btn': '💧 Drip water', 'q': 'What did the water do on the {m}?', 'opts': [{'k': 'beads', 't': 'It beaded up and sat on top', 'cell': 'Waterproof'}, {'k': 'soaks', 't': 'It soaked in and spread', 'cell': 'Soaks up water'}]},
                  'bend': {'btn': '🤲 Bend it', 'q': 'What did the {m} do when you bent it?', 'opts': [{'k': 'bends', 't': 'It bent easily', 'cell': 'Bends'}, {'k': 'stiff', 't': 'It stayed stiff and creased', 'cell': 'Stays stiff'}]}},
        'wrongSaw': 'Look again at the swatch. What did it really do?',
        'tableLabel': 'My classification table', 'cols': ['Material', 'Water test', 'Bend test'], 'doneLine': 'Your table is full. Read it like a scientist.',
        'q': 'Read your table. Which two materials kept water out AND bent?',
        'opts': [{'t': 'Paper towel and cotton cloth', 'miss': 'Check the Water test column. Those two soaked the water up.'},
                 {'t': 'Plastic wrap and foil', 'ok': True},
                 {'t': 'Cardboard and foil', 'miss': 'Check the Bend test column for cardboard.'}],
        'win': 'Your table sorted the evidence: only two materials pass BOTH tests. That’s how you pick a raincoat. Clue 4!', 'clue': 'driplab'},
    'exploreMod': 'driplab',
    'sunnote': {
        'after': '.fs-solve', 'kicker': 'Case closed · a twist', 'title': 'The late note', 'lockLine': 'Crack the case first.',
        'todo': ['Read Mr. Ortiz’s late note.', 'Pick new handles.', 'Add up the parts again.'],
        'note': {'t': 'One more thing! The awards are at noon in July, out in the sun, and the winner holds the trophy up by its handles. Is Design C still okay?', 'sign': 'Mr. Ortiz'},
        'pickQ': 'A new need: the handles must stay cool enough to hold in the hot sun. Which handles now?',
        'base': [{'t': 'Aluminum cup', 'g': 100}, {'t': 'Hard plastic base', 'g': 120}, {'t': 'Steel screws', 'g': 6}],
        'oldTotal': 254,
        'handles': [{'k': 'alu', 'icon': '🥈', 't': 'Keep aluminum', 'g': 14, 'ok': False, 'why': 'In the July noon sun, metal handles soak up heat and carry it straight to your fingers. Ouch!'},
                    {'k': 'wood', 'icon': '🪵', 't': 'Painted wood', 'g': 12, 'ok': True, 'why': 'Wood carries heat slowly, so it stays cool enough to hold. The paint keeps rain out.'},
                    {'k': 'plastic', 'icon': '🛍️', 't': 'Hard plastic', 'g': 10, 'ok': True, 'why': 'Hard plastic carries heat slowly too, and rain can’t soak in.'},
                    {'k': 'glass', 'icon': '💎', 't': 'Glass', 'g': 20, 'ok': False, 'why': 'Glass handles would snap off if a little kid dropped the trophy. Need 2!'}],
        'partsLabel': 'The new design’s parts', 'totalWord': 'Total',
        'totalQ': 'Add up the parts. What is the new total?',
        'win': 'New total: {x} g. Still under 500 g, cool to hold, and it survives rain and drops. A new need changed the pick!'},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Classifying doesn’t change the materials. What did the stickers do?', 'C': 'Paint changes how a thing looks. Classifying puts things into groups.'},
        'q2': {'B': 'Absorbent means it soaks up water. What happened to the paper umbrella in the rain rig?', 'C': 'Heavy and stiff can’t fold up. Remember the steel umbrella?'},
        'q3': {'A': 'Check the rigs: steel failed three jobs.', 'B': 'Plastic failed the sponge rig. No ONE material wins every job.'}},
    'flags': {
        'ans-1': [
            {'label': 'your job', 're': 'umbrel|unbrel|sponge|spong|bridg|brige|\\bpan|handle|handel|frying|fryin'},
            {'label': 'two properties it needs', 're': 'water ?pro+f|water ?pruf|flexib|flexab|bend|bendy|fold|absorb|soak|rigid|stiff|strong|cool|heat|hot|insulat|squish|light|hard'},
            {'label': 'the best material', 're': 'plastic|foam|steel|wood|nylon|metal|concrete|rubber'}],
        'ans-2': [
            {'label': 'your answer', 're': 'no|not|won.?t|will not|wouldn.?t|sink|fail|bad idea|doesn.?t work'},
            {'label': 'a property of paper', 're': 'absorb|soak|soggy|wet|waterproof|water ?proof|mush|tear|rip|weak|floppy|fall apart'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|wrong|right|true|not true|false|depends|no one best|not the best'},
            {'label': 'two pieces of evidence', 'any': ['steel', 'umbrella', 'sponge', 'handle', 'hot', 'bridge', 'heavy', 'fold', 'soak', 'brass', '606', '500', 'glass', 'aluminum', 'plastic', 'foam', 'wood', 'rig', 'test', 'trophy', 'design'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since|depends'}]},
    'minWords': {'ans-1': 12, 'ans-2': 12, 'cer-4': 30},
    'hints': {
        'ans-1': ['Pick one job from the test rigs. What did it need?', 'Each job tab listed two needs. Which material passed?', 'Try: For the ___, the material needs to be ___ and ___. The best material is ___.'],
        'ans-2': ['Think about the paper in the umbrella rig. What did the rain do to it?', 'A boat sits in water all day. Does paper keep water out, or soak it up?', 'Try: A paper boat will / won’t work because paper is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'Steel held up the bridge but failed the umbrella, the sponge and the pan handle.',
                'The steel pan handle got too hot to hold, but wood and plastic stayed cool.',
                'The all-brass trophy design weighed 606 grams, over the 500-gram limit.',
                'Steel is shiny and looks strong.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'photos': [
        {'id': 'heattile', 'afterSolve': True, 'lockLine': 'Crack the case first.', 'kicker': 'Case closed · one more wow', 'short': 'The NASA heat tile',
         'title': 'Picked for the hottest job', 'todo': ['Tap each number on the photo.', 'Then match each material to its job.'],
         'why': {'icon': '🚀', 'q': 'What are we looking at?', 't': 'A real photo from NASA’s Kennedy Space Center in Florida: a worker lifts a space shuttle heat tile out of a 2,200-degree oven.'},
         'img': I('heat-tile-oven'), 'alt': 'A worker in a shiny silver suit, thick gloves and a gold face shield holds a white holder with a glowing red-hot heat tile on it.',
         'credit': 'NASA/Jim Grossmann, KSC-08pd1969', 'license': 'public domain, via NASA Image Library',
         'hotspots': [
             {'n': 1, 'x': 38, 'y': 52, 'label': 'The glowing tile', 't': 'A shuttle heat tile, fresh from a 2,200-degree oven. It glows red-hot, but it is full of tiny air pockets, so heat crawls through it very slowly. Tiles like it covered the space shuttle to block the heat of coming home from space.'},
             {'n': 2, 'x': 58, 'y': 57, 'label': 'Thick gloves', 't': 'Thick, puffy gloves carry heat slowly, so the worker’s hands stay safe. Same idea as a wooden pan handle!'},
             {'n': 3, 'x': 78, 'y': 63, 'label': 'The silver suit', 't': 'The suit is coated with shiny metal. It reflects (bounces back) the heat glowing off the oven and the tile.'},
             {'n': 4, 'x': 63, 'y': 12, 'label': 'The gold face shield', 't': 'A thin gold-colored coating reflects heat and bright glare, but the worker can still see through it.'}],
         'task': {'q': 'Match it: which label shows the material picked for each job?',
                  'items': [
                      {'icon': '🔥', 'step': 'Survive a 2,200-degree oven', 'ans': 1, 'evid': 'A shuttle heat tile survives a 2,200-degree oven. It was picked for one job: blocking heat.', 'miss': 'Look for the thing that is glowing.'},
                      {'icon': '✋', 'step': 'Keep hands safe by carrying heat slowly', 'ans': 2, 'evid': 'Thick gloves carry heat slowly, like a wooden pan handle.', 'miss': 'What is the worker holding things with?'},
                      {'icon': '🪞', 'step': 'Bounce heat away from the body', 'ans': 3, 'evid': 'A shiny metal-coated suit reflects heat away from the worker’s body.', 'miss': 'Look for the big shiny thing the worker is wearing.'},
                      {'icon': '👀', 'step': 'Block glare but still let you see', 'ans': 4, 'evid': 'A gold-coated face shield blocks heat and glare, but you can see through it.', 'miss': 'Look at the worker’s face.'}],
                  'win': 'Four materials, four jobs, one very hot room. Every one was picked for its properties, just like your trophy.'}}],
    'slots': {
        'welcome': {'label': 'Welcome · Next Year’s Trophy', 'length': '40–50 s'},
        'warmup': {'label': 'Warm-Up · take it apart (Clue 1)', 'length': '15–20 s',
                   'script': 'Dr. Nair here. Before we build a new trophy, take a toy apart. Lock in your prediction first. Then drag each part onto Scale 2. Watch both scales and the adding tape. Does anything go missing?'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · sticker every property (Clue 2)', 'length': '15–20 s',
                  'script': 'Each sticker is a group. Drag Bends onto the rubber band. Does Waterproof fit too? Every card shows how many stickers it needs. A wrong sticker bounces off, so read why. The iron nail might surprise you.'},
        'part2': {'label': 'Part 2 · the job test rigs (Clue 3)', 'length': '15–20 s',
                  'script': 'Engineers test before they build. Pick a job tab and read what it needs. Drag a material into the rig, then press Run the test. If it fails, swap and run again. Can steel win every job?'},
        'part3': {'label': 'Part 3 · the 412-gram puzzle (wow)', 'length': '20–30 s'},
        'explore': {'label': 'Part 4 · the drip and bend lab (Clue 4)', 'length': '15–20 s',
                    'script': 'Five swatches, two tests. Press Drip water and watch: does it bead up, or soak in? Then press Bend it. Tap what you saw. Your classification table fills in row by row. Read it at the end.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · choose a material for a job', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '15–20 s'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease week 28 (magnets).'},
    },
    'videoOff': [],
    'lensVoice': False,
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Both scales reading 60 g in all (Warm-Up)',
        'The iron nail wearing 3 stickers (The Lesson)',
        'A rig that passed its test (The Lesson)',
        'Your finished classification table (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['The toy robot in pieces', 'A test rig that failed', 'Your favorite trophy design'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · draw and label your object', 'required': True, 'minLabels': 4,
                           'prompts': ['Draw the object that does your job', 'Label the material you chose', 'Label the 3 properties it needs', 'Circle the property that beat the other material']}]},
    'hlCoach': copy.deepcopy(O['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🏅', 'name': 'The new trophy design',
                 'line': 'You cracked Case 27, part 2, and the new trophy design goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next week: magnets!'},
    'notebookTitle': O['notebookTitle'],
    'notebook': copy.deepcopy(O['notebook']) + [{'lesson': '27.02', 'icon': '🏅', 'name': 'The new trophy design'}],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are sorted. Nice classifying!',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to see what it means.']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '#tab-vocab p', 'text': 'Then test it right here.'},
         'label': 'Warm-Up: take it apart', 'q': 'Warm-Up: my prediction, what the scales showed, and what I learned.', 'title': 'My take-apart test', 'compact': True,
         'fields': [{'t': 'My prediction', 'icon': '🔒', 'ph': 'I predicted the pile would weigh ___.'},
                    {'t': 'What the scales showed', 'icon': '⚖️', 'ph': 'The pile weighed ___ grams.'},
                    {'t': 'What I learned', 'icon': '💡', 'ph': 'The mass of the whole ___.'}]},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Then choose the winner and prove it in one sentence.'},
         'label': 'Part C: choose a material for a job', 'q': 'Part C: my job, the properties it needs, two materials, and my pick with evidence.', 'title': 'My material choice',
         'fields': [{'t': 'The job', 'icon': '🎯', 'ph': 'My object is a ___. Its job is to ___.'},
                    {'t': '3 properties it needs', 'icon': '🏷️', 'ph': 'It needs to be ___, ___ and ___.'},
                    {'t': '2 materials that could work', 'icon': '🧪', 'ph': '___ or ___.'},
                    {'t': 'My pick, with evidence', 'icon': '🏆', 'ph': 'I chose ___ for the ___ because ___.', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Is steel the best material for everything?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-1': 'Part B · Question 5', 'ans-2': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'Engineers choose the material whose properties match the job, so no one material is best for everything.',
    'key': ['material', 'properties', 'job', 'best'],
    'small': ['the', 'whose', 'so', 'no', 'for'],
    'model': 'A scientist might highlight “properties”, “job” and “material”. Those words hold the big idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this tell how to sort materials, or how to pick one for a job?']

EV = '#tab-assignment .act-body > div:has(> .fs-plan)'
D['cues'] = {
    'warmup': [{'at': '^prediction', 'sel': '[data-mod="takeapart"] .fs-sv-q, .fs-tka-pred', 'fx': 'pop', 'scroll': True},
               {'at': '^drag', 'sel': '.fs-tka-tray .fs-dragc', 'i': 0, 'fx': 'point'},
               {'at': '^scales', 'sel': '.fs-tka-stage', 'fx': 'glow'},
               {'at': '^tape', 'sel': '[data-mod="takeapart"] .fs-todo li', 'i': 2, 'fx': 'trace'}],
    'part1': [{'at': '^sticker', 'sel': '.fs-pst-sheet', 'fx': 'glow', 'scroll': True},
              {'at': '^bends', 'sel': '.fs-pst-st', 'i': 0, 'fx': 'point'},
              {'at': '^rubber', 'sel': '.fs-pst-card', 'i': 0, 'fx': 'pop'},
              {'at': '^card', 'sel': '[data-mod="stickers"] .fs-todo li', 'i': 1, 'fx': 'trace'},
              {'at': '^nail', 'sel': '.fs-pst-card[data-id="nail"]', 'fx': 'wiggle'}],
    'part2': [{'at': '^tab', 'sel': '.fs-rig-tabs', 'fx': 'pop', 'scroll': True},
              {'at': '^needs', 'sel': '.fs-rig-need', 'fx': 'trace'},
              {'at': '^rig', 'sel': '.fs-rig', 'fx': 'glow'},
              {'at': '^run', 'sel': '.fs-rig-go', 'fx': 'point'},
              {'at': '^steel', 'sel': '[data-mod="rigs"] .fs-dragc[data-k="steel"]', 'fx': 'wiggle'}],
    'explore': [{'at': '^swatches', 'sel': '[data-mod="driplab"] .fs-twn-tools', 'fx': 'pop', 'scroll': True},
                {'at': '^drip', 'sel': '[data-mod="driplab"] .fs-mug-go .fs-btn', 'i': 0, 'fx': 'point'},
                {'at': '^bend', 'sel': '[data-mod="driplab"] .fs-mug-go .fs-btn', 'i': 1, 'fx': 'point'},
                {'at': '^table', 'sel': '.fs-dbl-table', 'fx': 'glow', 'scroll': True}],
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
