#!/usr/bin/env python3
"""Writes data.json and fixes.json for 13.02 (run from this folder)."""
import json, copy
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../13-01/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

OLDBQ = '"How are the life cycles of Florida plants and animals alike — and how are they different?"'
BQ = '"How do Florida’s flowering plants make seeds, and how do those seeds become new plants?"'
# ---------------------------------------------------------------- ticked fixes (Bethany, 17 Oct 2026)
fx('fix', 'copy-paste leftover: the Big Question was about life cycles (shared with 13.01–14.01)',
   'Think about this…</div>\n          <div class="question">' + OLDBQ, 'Think about this…</div>\n          <div class="question">' + BQ)
fx('fix', 'copy-paste leftover: Circle Back repeats the life-cycle Big Question',
   'Now You Know!</div>\n          <div class="question">' + OLDBQ, 'Now You Know!</div>\n          <div class="question">' + BQ)
fx('fix', 'copy-paste leftover: “predict what stages it goes through” is about life cycles',
   "Hold this question in your head as you work. By the end of the lesson, you'll be able to look at a Florida plant or animal and predict what stages it goes through from birth to making the next generation.",
   "Keep this question in mind. By the end, you'll be able to follow a Florida flower all the way from pollen to a brand-new plant.")
fx('fix', 'copy-paste leftover: “Complete vs. Incomplete” is about metamorphosis', '<div class="info-detail">Complete vs. Incomplete</div>', '<div class="info-detail">Pollination to germination</div>')
fx('fix', 'the definition left out self-pollination, which the lesson describes later',
   ' — when pollen moves from the male part of one flower to the female part of another.', ': pollen moves from the male part to the female part of a flower, usually a different flower.')
fx('fix', 'quarter label in the footer: week 13 is Quarter 2', 'Science &middot; Quarter 3 &middot;', 'Science &middot; Quarter 2 &middot;')
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', '“module” → “week”', "Next module, you'll see how cycles like this play out across the seasons in Florida ecosystems.",
   "Next week, you'll follow Florida plants and animals through their whole lives, and through the seasons.")

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter', "Picture a bee landing on a flower in a Florida garden. It crawls inside, gets dusty with yellow powder, then flies off to the next flower. A week later, that first flower has turned into a tiny seed pod. Months later, a new plant is sprouting from a seed that fell to the ground.",
   "Picture a bee landing on a flower in a Florida garden. It crawls around, gets dusty with yellow powder, then flies to the next flower. Weeks later, that flower is full of seeds.")
fx('cut', 'the notebook sketch becomes the Pollen pass game and an on-page answer',
   "In your notebook, sketch the bee on the flower. Add an arrow showing where the bee will go next. Underneath, write ONE sentence guessing what the yellow powder might be.",
   "<strong>Pollen pass:</strong> be the bee! Fly from flower to flower and watch what the yellow powder does.")
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', 'dash removed', "is more than a pretty thing on a stem — it's the part of a plant that MAKES the next generation.", "is more than a pretty thing on a stem. It's the part of a plant that MAKES the next generation.")
fx('plain', 'dashes removed', "happens — the egg can now grow into a seed.", "happens, and the egg can now grow into a seed.")
fx('plain', 'dash removed; “gravity” explained', "seeds travel — by wind, water, animals, or gravity — away from the parent.", "seeds travel away from the parent by wind, water, animals or gravity (falling).")
fx('plain', '“misconception” → plain words', '<p><strong>Common misconception:</strong> Some people think', '<p><strong>Watch out:</strong> Some people think')
fx('plain', 'dash removed', "The new plant inherits its traits from BOTH parent flowers — that's why orange tree seeds grow into orange trees, not apple trees. Each step in the cycle keeps the inherited traits moving forward.",
   "The new plant inherits its traits from its parent flowers. That's why orange seeds grow into orange trees, not apple trees.")
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (sequencing becomes the Cycle relay; the flower drawing becomes Part C; Seed travelers is Part 4)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: the Key Concept box repeats Part 2', r'<div style="background:#FFF6E5;border:2.5px solid #F0C97A;[^"]*">\s*<div[^>]*>⭐ Key Concept</div>.*?</div>\s*', '', True)
fx('cut', 'lean: one thinking stop per tab (Stop & Think in Part 1 stays)', r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: the diagram heading becomes Part 3', 'margin-top:22px;">Four Florida Pollinators &amp; Plants</h3>', 'margin-top:22px;">Part 3 · Four Florida Pollinators &amp; Plants</h3>')
fx('cut', 'lean: Observe & Reason, the oak pollen fact, the bee callout (its count was shaky) and Go Deeper; Part 4 = Seed travelers; next button goes to Self-Check',
   r'<div class="socratic-q">\s*<span class="sq-icon">👀</span>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 4 · Seed Travelers</h3>\n      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">A seed that lands right under its parent has to share sun and water. So seeds travel. Florida seeds travel in five ways.</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 5 removed (Bethany kept 6 and 7)', r'<div class="pq">\s*<span class="pq-num"[^>]*>5</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: Part B question 6 is now number 5', '<span class="pq-num" style="background:#D4772C;">6</span>', '<span class="pq-num" style="background:#D4772C;">5</span>')
fx('cut', 'lean: Part B question 7 is now number 6', '<span class="pq-num" style="background:#D4772C;">7</span>', '<span class="pq-num" style="background:#D4772C;">6</span>')
fx('cut', 'lean: Part C typed on the page (the drawing is a bonus)',
   r'In your notebook, draw the FIVE steps of flowering plant reproduction as a cycle \(a big circle with arrows between each step\)\.</p>\s*<p[^>]*>For EACH step, draw a small picture.*?</p>',
   "Follow ONE Florida flower through all five steps. Write one sentence for each step, in your own words.</p>", True)
fx('cut', 'lean: no Reflect', r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C typed on the page; the sketch is a bonus',
   'A 5-step flowering plant reproduction cycle, drawn as a circle with arrows, with a picture and sentence for each step.',
   'One sentence for each of the five steps. (A sketch of the cycle is a bonus.)')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether flowers really matter, and supported it with two pieces of evidence from the lesson.',
   '<strong>Use Your Evidence:</strong> My claim about whether flowers matter to the plant, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', True)

# ---------------------------------------------------------------- data
CR = {
    'bee': 'Bee on a sunny flower, Bob Peterson, via Wikimedia Commons (CC BY-SA 2.0)',
    'bs1': 'Dune sunflower, Sanibel Island, Fredlyfish4, via Wikimedia Commons (CC BY-SA 4.0)',
    'bs2': 'Dune sunflower, Sanibel Island, James St. John, via Wikimedia Commons (CC BY 2.0)',
    'bs3': 'Beach sunflower, Bob Peterson, via Wikimedia Commons (CC BY-SA 2.0)',
    'gail': 'Blanket flower (Marineland), Ebyabe, via Wikimedia Commons (CC BY 2.5)',
    'tick': 'Leavenworth’s tickseed, Bob Peterson, via Wikimedia Commons (CC BY-SA 2.0)',
}
FLOWERS = [
    {'id': 'a', 'name': 'Beach sunflower 1', 'img': 'images/13-02-bs-1.jpg', 'alt': 'A beach sunflower: yellow petals around a dark brown center.', 'kind': 'bs'},
    {'id': 'g', 'name': 'Blanket flower', 'img': 'images/13-02-blanket.jpg', 'alt': 'A blanket flower: red petals with yellow tips around a dark center.', 'kind': 'gail',
     'miss': 'A blanket flower is a different kind of plant. Sunflower pollen can’t make blanket flower seeds.', 't': 'The bee sips nectar here, but the sunflower pollen does nothing for this flower.'},
    {'id': 'b', 'name': 'Beach sunflower 2', 'img': 'images/13-02-bs-2.jpg', 'alt': 'A beach sunflower with a dark center, among green leaves.', 'kind': 'bs'},
    {'id': 't', 'name': 'Tickseed', 'img': 'images/13-02-tickseed.jpg', 'alt': 'Tickseed: small yellow flowers with notched petals.', 'kind': 'tick',
     'miss': 'Tickseed looks a lot like a beach sunflower, but it’s a different kind of plant. Sunflower pollen can’t make tickseed seeds.', 't': 'Tickseed is Florida’s state wildflower. Look-alikes can fool you!'},
    {'id': 'c', 'name': 'Beach sunflower 3', 'img': 'images/13-02-bs-3.jpg', 'alt': 'Beach sunflowers on tall thin stems.', 'kind': 'bs'},
    {'id': 'd', 'name': 'Beach sunflower 4', 'img': 'images/13-01-case-parent.jpg', 'alt': 'A wild beach sunflower growing on a sand dune.', 'kind': 'bs'},
]
SEEDS = [
    {'t': 'Red maple: each seed has a thin wing that spins like a helicopter.', 'bin': 0, 'miss': 'A thin wing catches moving air. What carries it?'},
    {'t': 'Red mangrove: long, pencil-shaped seedlings drop into the water and float to new shores.', 'bin': 1, 'miss': 'It floats. What carries something that floats?'},
    {'t': 'Spanish needles: tiny seeds with hooked prongs that stick to fur and socks.', 'bin': 2, 'miss': 'Hooks grab onto things that walk by. Which way is that?'},
    {'t': 'Beautyberry: purple berries that birds eat. The seeds come out in their droppings far away.', 'bin': 3, 'miss': 'Something swallows these. Which way travels inside an animal?'},
    {'t': 'Live oak: heavy acorns fall under the tree. Squirrels bury some and forget them.', 'bin': 4, 'miss': 'These are too heavy to fly or float. They fall, and then an animal moves them.'},
]
D = {
    'lesson': '13.02', 'week': 13, 'day': 2, 'guide': 'lena', 'prefix': 'g4sci-13-2', 'manifestKey': '13-02',
    'paths': P['paths'], 'crew': P['crew'],
    'expedition': {'num': 13, 'title': 'The Empty Seed Heads'},
    'ambient': {'icon': '🐝', 'label': 'Garden sounds'},
    'case': {
        'num': '13 · part 2', 'title': 'The Empty Seed Heads', 'style': 'sheet',
        'hook': 'Same parent, two gardens. But there’s one more thing. When I opened the dry flower heads, Pot A’s were packed with seeds. Pot B’s, from the shady courtyard, were almost empty. I hardly ever see bees back there. So I set up a test, and I wrote everything on my data sheet.',
        'question': 'Why were Pot B’s flower heads almost empty of seeds?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'stills': [],
        'logs': [
            {'head': 'Pot A · sunny dune garden', 'img': 'images/13-01-case-seeds.jpg', 'alt': 'Dried beach sunflower heads full of seeds.',
             'rows': [['Bees seen', 'lots, every morning'], ['Seeds in each head', 'packed full']], 'big': 'FULL'},
            {'head': 'Pot B · shady courtyard', 'img': 'images/13-01-case-shade.jpg', 'alt': 'One thin beach sunflower in the shade.',
             'rows': [['Bees seen', 'almost none'], ['Seeds in each head', 'a few; the rest are hollow']], 'big': 'EMPTY?'}],
        'sticky': 'My test: tie mesh bags over some heads in the SUNNY garden, so bees can’t reach them. Same sun, same water. Only the bees change.',
        'stillsCredit': 'Photos: dune sunflower seed heads, Daniel Di Palma, via Wikimedia Commons (CC BY-SA 4.0); beach sunflower, sonnia hill, via Wikimedia Commons (CC BY 2.0). The data sheet is part of the story.',
        'clues': [
            {'id': 'pollen', 'icon': '🐝', 'where': 'Warm-Up: pollen pass', 't': 'A bee picks up pollen at one flower and rubs it off at the next. Only a flower of the same kind can use it.'},
            {'id': 'bagtest', 'icon': '🕸', 'where': 'The Lesson, Part 1: the bag test', 't': 'Same sun, same water: flower heads with bees made lots of seeds; bagged heads made almost none. The bees were the difference.'},
            {'id': 'relay', 'icon': '🔄', 'where': 'The Lesson, Part 2: the cycle', 't': 'Pollination comes first. No pollination means no fertilization, and no fertilization means no seeds.'},
            {'id': 'sort', 'icon': '🌬', 'where': 'The Lesson, Part 4: seed travelers', 't': 'Seeds travel away from the parent by wind, water, hitchhiking, animals eating them, or falling and being buried.'},
        ],
        'solve': {
            'title': 'What happened to Pot B?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'The seeds were there, but they blew away before Dr. Reyes looked.', 'why': 'Check Clue 2. In the bag test, the bagged heads never made full seeds at all, even with nothing blowing them away.'},
                {'t': 'Almost no bees reached Pot B. Without bees carrying pollen between flowers, most tiny flowers were never pollinated, so they couldn’t be fertilized or make seeds.', 'right': True,
                 'why': 'Case cracked! The bag test proved it: same sun, same water, no bees, no seeds. Pollination comes first. Now write your case report: it’s the questions below.'},
                {'t': 'Shady plants never make seeds, no matter what.', 'why': 'Check Clue 2: the bagged heads were in full SUN and still made almost no seeds. What did the bags keep out?'},
            ]},
    },
    'pollen': {
        'afterText': 'be the bee!', 'kicker': 'Warm-Up game', 'title': 'Pollen pass',
        'todo': ['The bee starts on Beach sunflower 1, dusty with pollen.', 'Drag the bee to another flower, or tap the bee and then a flower.', 'Pollinate all three other beach sunflowers. Watch out for look-alikes!'],
        'why': {'icon': '🐝', 'q': 'Why does a bee visit flowers?', 't': 'For food: sweet nectar and pollen. While it eats, pollen sticks to its fuzzy body.'},
        'hint': 'Drag the bee to a flower, or tap the bee and then a flower.',
        'bee': {'img': 'images/13-02-bee.jpg', 'alt': 'A fuzzy, striped bee on a yellow flower.'},
        'start': 'a', 'kind': 'bs', 'flowers': FLOWERS,
        'wrongKind': 'That’s a different kind of plant. Sunflower pollen only works on beach sunflowers.',
        'startLine': 'This is where the bee picked up its pollen. Fly to another beach sunflower!',
        'again': 'Already pollinated. Find a beach sunflower that still needs pollen.',
        'done': 'Pollen rubbed off on this flower. Now it can make seeds! 🌰',
        'countWord': 'beach sunflowers pollinated',
        'q': 'What did the bee and the flowers each get?',
        'opts': [{'t': 'The bee got food (nectar). The flowers got pollen moved, so they can make seeds.', 'ok': True},
                 {'t': 'The bee got seeds to eat.', 'miss': 'The seeds aren’t made yet! What was the bee drinking?'},
                 {'t': 'Only the bee got something.', 'miss': 'Look at the flowers with 🌰. What did the bee do for them?'}],
        'credit': CR['bee'] + '. ' + CR['bs1'] + '. ' + CR['bs2'] + '. ' + CR['bs3'] + '. ' + CR['gail'] + '. ' + CR['tick'] + '.',
        'win': 'Three sunflowers pollinated! The bee carried pollen from flower to flower of the SAME kind. Look-alikes can’t use it. That’s a clue.',
        'clue': 'pollen'},
    'bagtest': {
        'afterText': 'pollen has to reach the egg', 'kicker': 'Part 1 game', 'title': 'The bag test',
        'model': 'This is a model of Dr. Reyes’s test. All three heads grow in the same sunny garden with the same water.',
        'todo': ['For each flower head, pick: leave it open for bees, or tie on a mesh bag.', 'Bag at least one and leave at least one open. That makes it a fair test.', 'Press ▶ and count the full seeds. Then answer two questions.'],
        'why': {'icon': '🌻', 'q': 'One head, many flowers', 't': 'A sunflower head is really hundreds of tiny flowers packed together. Each tiny flower can make one seed.'},
        'img': 'images/13-02-head.jpg', 'alt': 'A beach sunflower head up close: yellow petals around a dark center packed with tiny flowers.',
        'credit': CR['bs1'] + '. The seed counts are a model.',
        'heads': [{'id': 'h1', 'name': 'Head 1'}, {'id': 'h2', 'name': 'Head 2'}, {'id': 'h3', 'name': 'Head 3'}],
        'open': {'label': 'Open', 'seeds': 34, 'note': 'Bees visited and carried pollen in from other plants.'},
        'bag': {'label': 'Mesh bag', 'seeds': 1, 'note': 'Air and sunlight got through the mesh, but bees couldn’t.'},
        'total': 40,
        'runBtn': '▶ Wait 3 weeks, then count the seeds',
        'needBoth': 'A fair test compares two things. Bag at least one head and leave at least one open.',
        'q1': 'What made the difference in the seed counts?',
        'opts1': [{'t': 'The sun', 'miss': 'All three heads were in the same sunny garden. What did the bags keep out?'},
                  {'t': 'The bees bringing pollen', 'ok': True},
                  {'t': 'The water', 'miss': 'Every head got the same water. What did the bags keep out?'}],
        'q2': 'Why did Dr. Reyes do the test in ONE sunny garden?',
        'opts2': [{'t': 'So only one thing changed: bees or no bees', 'ok': True},
                  {'t': 'Because it was closer to the lab', 'miss': 'Think about a fair test. What would happen if the sun ALSO changed?'},
                  {'t': 'So the bees would get more sun', 'miss': 'Think about a fair test. How many things should change at once?'}],
        'win': 'Same sun, same water: open heads were full of seeds, bagged heads were almost empty. Bees bring the pollen, and pollination comes first. That’s a clue.',
        'clue': 'bagtest'},
    'relay': {
        'afterText': 'The new plant inherits its traits', 'kicker': 'Part 2 game', 'title': 'Put the cycle in order',
        'todo': ['Drag each step onto a station, or tap a step and then a station.', 'Start with what has to happen FIRST before a seed can exist.', 'Fill all five stations and watch a new plant come around.'],
        'why': {'icon': '🔄', 'q': 'Why a cycle?', 't': 'The last step makes a new plant. When it flowers, the whole cycle starts again.'},
        'steps': [{'icon': '🐝', 't': 'Pollination'}, {'icon': '🥚', 't': 'Fertilization'}, {'icon': '🌰', 't': 'Seed made'}, {'icon': '🌬', 't': 'Seed travels'}, {'icon': '🌱', 't': 'Germination'}],
        'miss': {'0': 'Pollen has to move first. Nothing else can happen until it does.', '1': 'Pollen has to arrive before it can join the egg.',
                 '2': 'A seed can only form after the egg is fertilized.', '3': 'A seed has to exist before it can travel.', '4': 'Sprouting is the last step, after the seed lands somewhere new.'},
        'win': 'Around the cycle! Pollination → fertilization → seed → travel → germination. Then the new plant flowers, and it starts again. That’s a clue.',
        'clue': 'relay'},
    'sort': {
        'afterText': 'Florida seeds travel in five ways', 'kicker': 'Part 4 game', 'subject': 'Florida seeds', 'title': 'Seed travelers',
        'todo': ['Read each Florida seed card.', 'Drag it to the way it travels, or tap a card and then a way.', 'One seed for each way.'],
        'why': {'icon': '🌱', 'q': 'Why travel?', 't': 'A seed that lands far from its parent has its own sun, water and space to grow.'},
        'bins': [{'icon': '🌬', 't': 'Wind'}, {'icon': '🌊', 't': 'Water'}, {'icon': '🧦', 't': 'Hitchhiker'}, {'icon': '🐦', 't': 'Eaten by animals'}, {'icon': '🐿', 't': 'Falls, then buried'}],
        'cards': SEEDS,
        'win': 'Five seeds, five ways to travel! Wings, floating, hooks, berries and buried acorns all get seeds away from the parent. That’s your last clue.',
        'clue': 'sort'},
    'exploreMod': 'sort',
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Can a seed exist before pollen reaches the egg?', 'C': 'Germination needs a seed. Which step has to come first?'},
        'q2': {'A': 'That’s germination. Which step is about pollen?', 'B': 'That’s dispersal. Which step is about pollen?'},
        'q3': {'B': 'Flowers do look nice. But what do they MAKE?', 'C': 'Many flowers invite insects in. Why would a flower want visitors?'}},
    'flags': {
        'ans-2': [
            {'label': 'what pollination is', 're': 'pollen.{0,40}(move|carr|travel|go|land|reach|from|to )|(move|carr|bring).{0,30}pollen|bee|insect|wind'},
            {'label': 'what fertilization is', 're': 'egg|join|seed|fertiliz.{0,30}(egg|join|seed|mak|start)|combin|meet'},
            {'label': 'which comes first', 're': 'first|before|then|after|next|1st|comes'}],
        'ans-3': [
            {'label': 'why it didn’t grow', 're': 'dry|no water|water|drawer|dark|cold|need'},
            {'label': 'water', 're': 'water|wet|moist|rain'},
            {'label': 'warmth', 're': 'warm|heat|temperature|hot|sun'},
            {'label': 'time', 're': 'time|wait|days|weeks|long'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|wrong|right|true|not true|matter|important|need'},
            {'label': 'two pieces of evidence', 'any': ['pollen', 'pollinat', 'bee', 'bag', 'seed', 'egg', 'fertiliz', 'nectar', 'tiny flower', 'next generation|new plant', 'germinat', 'empty', 'reproduc'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|without|proves'}]},
    'minWords': {'ans-2': 20, 'ans-3': 15, 'cer-4': 30},
    'hints': {
        'ans-2': ['Pollination is about pollen moving. Fertilization is about pollen joining the egg.', 'Think about the cycle you put in order in Part 2. Which station came first?', 'Try: Pollination is when ___. Fertilization is when ___. ___ happens first.'],
        'ans-3': ['Read the paragraph about the dry drawer in Part 2.', 'A seed is waiting for the right environment. What was missing in a dry drawer?', 'Try: It didn’t grow because ___. A seed needs ___, ___ and ___ to germinate.'],
        'cer-4': ['First decide: do you agree or disagree with the classmate?', 'Think about the bag test. What happened to heads that bees couldn’t reach?', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'Bagged flower heads, which bees couldn’t reach, made almost no seeds.',
                'Pollen has to reach the egg before a seed can form.',
                'Each tiny flower in a sunflower head can make one seed.',
                'Flowers give bees nectar, and bees carry their pollen.',
                'Seeds from flowers grow into the next generation of plants.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · the empty seed heads', 'length': '30–40 s',
                    'script': 'It’s Dr. Reyes again. Remember my two pots? I opened the dry flower heads. Pot A’s were packed with seeds. Pot B’s, from the shady courtyard, were almost empty. And I almost never see bees back there. Is that a coincidence? I set up a test to find out. Look at my data sheet in the case file.'},
        'warmup': {'label': 'Warm-Up · pollen pass (Clue 1)', 'length': '20–30 s',
                   'script': 'Time to be the bee. You start out dusty with sunflower pollen. Fly to another beach sunflower and watch the pollen rub off. One warning from the field: some flowers look a lot like beach sunflowers, but they aren’t. Look closely before you land.'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Say each word. For pollination, pretend to fly a bee from flower to flower.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · the bag test (Clue 2)', 'length': '25–35 s',
                  'script': 'Here’s my test. Same sunny garden, same water. On some flower heads, I tie a mesh bag. Air and sunlight get through, but bees can’t. Others stay open. You decide which heads get bags. Then wait three weeks and count the seeds. Bag at least one and leave one open, so it’s a fair test.'},
        'part2': {'label': 'Part 2 · put the cycle in order (Clue 3)', 'length': '20–30 s',
                  'script': 'Five steps make a new plant. Your job is to put them in order. Ask yourself: what has to happen before a seed can even exist? Start there. When all five are in place, watch a new plant come all the way around.'},
        'figure': {'label': 'The cycle picture', 'length': '20–30 s'},
        'part3': {'label': 'Part 3 · four pollinator pairs', 'length': '20–30 s'},
        'explore': {'label': 'Part 4 · seed travelers (Clue 4)', 'length': '25–35 s',
                    'script': 'Seeds can’t walk, but they sure do travel. Some fly. Some float. Some hitch a ride on your socks. Read each Florida seed card and figure out how it gets away from its parent. Look for clues like wings, hooks or berries.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s',
                       'script': 'Do you have all four clues? Crack the case at the top of this tab: why were Pot B’s flower heads empty? Then answer two questions, follow one flower through all five steps, and write your CER. Your answers save as you type.'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · follow one flower', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says flowers are just for looking pretty. Hmm. Think about my bag test. What happened to the flower heads the bees couldn’t reach? Pick your side, tap two pieces of evidence in the planner, then explain how they prove your claim.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease week 14 (life cycles and seasons).',
                    'script': 'Case closed! My courtyard sunflower had plenty of flowers, but almost no bees, so almost no seeds. I’m planting more flowers back there to invite the bees in. Next week, we’ll follow Florida plants and animals through their whole lives, and through the seasons.'},
    },
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'The bee on its third pollinated sunflower (Warm-Up)',
        'Your bag test with the seed counts showing (The Lesson)',
        'All five seeds sorted (The Lesson)',
        'The answer that cracked the case (Assignment)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['The five-step cycle', 'A bee carrying pollen', 'A seed traveling'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 2,
                           'prompts': ['Draw the cycle as a circle with arrows', 'Label each of the five steps', 'Add the bee']}]},
    'hlCoach': copy.deepcopy(P['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🕸', 'name': 'Mesh pollinator bag',
                 'line': 'You cracked Case 13, part 2, and a mesh pollinator bag goes in your Field Notebook. (A specimen is something a scientist collects to study.) Next week: whole life cycles, through the seasons.'},
    'notebookTitle': P['notebookTitle'],
    'notebook': [dict(x) for x in Q['notebook']],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You’ll use every one of them today.',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'write', 'find': {'sel': '.fs-game[data-mod="pollen"]'},
         'label': 'Warm-Up: what the yellow powder does', 'q': 'Warm-Up: What is the yellow powder on the bee? Why did only some flowers make seeds?',
         'ph': 'The yellow powder is… Only some flowers made seeds because…', 'rows': 3},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'hide-nw', 'type': 'hide', 'find': {'sel': '.act-warmup .socratic-q', 'text': 'Notice'}},
        {'id': 'hide-tip', 'type': 'hide', 'find': {'sel': '.act-warmup .callout', 'text': 'Today'}},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Follow ONE Florida flower'},
         'label': 'Part C: One flower, five steps', 'q': 'Part C: Follow one Florida flower through the five steps of plant reproduction',
         'title': 'My flower: ___', 'compact': True,
         'fields': [{'t': '1 · Pollination', 'icon': '🐝', 'ph': 'A ___ carries pollen from…'},
                    {'t': '2 · Fertilization', 'icon': '🥚', 'ph': 'The pollen joins…'},
                    {'t': '3 · Seed made', 'icon': '🌰', 'ph': 'Seeds grow where…'},
                    {'t': '4 · Seed travels', 'icon': '🌬', 'ph': 'The seeds travel by…'},
                    {'t': '5 · Germination', 'icon': '🌱', 'ph': 'With water and warmth, the seed…'}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Do flowers matter to the plant, or are they just pretty?', 'ph': 'I disagree. Flowers matter because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-2': 'Part B · Question 5', 'ans-3': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] in ('12.01', '12.02', '13.01'): n['have'] = True
    if n['lesson'] == '13.02': n.update({'icon': '🕸', 'name': 'Mesh pollinator bag'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'A bee carries pollen from one flower to another, so the flower can make seeds.',
    'key': ['bee', 'carries', 'pollen', 'flower', 'seeds'],
    'small': ['A', 'from', 'one', 'to', 'so', 'the', 'can'],
    'model': 'A scientist might highlight “bee”, “carries pollen” and “seeds”. Those words carry the idea. Small words like “the” and “so” don’t.'}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
