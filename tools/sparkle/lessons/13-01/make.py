#!/usr/bin/env python3
"""Writes data.json and fixes.json for 13.01 (run from this folder)."""
import json, copy
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../12-02/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

BQ = 'Which traits do Florida plants and animals get from their parents, and which come from where they live?'
# ---------------------------------------------------------------- ticked fixes (Bethany, 16 Oct 2026)
fx('fix', 'copy-paste leftover: the Big Question was about life cycles (shared with 13.02–14.01)',
   'Think about this…</div>\n          <div class="question">"How are the life cycles of Florida plants and animals alike — and how are they different?"', 'Think about this…</div>\n          <div class="question">"' + BQ + '"')
fx('fix', 'copy-paste leftover: Circle Back repeats the life-cycle Big Question',
   'Now You Know!</div>\n          <div class="question">"How are the life cycles of Florida plants and animals alike — and how are they different?"', 'Now You Know!</div>\n          <div class="question">"' + BQ + '"')
fx('fix', 'copy-paste leftover: “predict what stages it goes through” is about life cycles',
   "Hold this question in your head as you work. By the end of the lesson, you'll be able to look at a Florida plant or animal and predict what stages it goes through from birth to making the next generation.",
   "Keep this question in mind. By the end, you'll be able to look at a Florida plant or animal and tell which traits came from its parents and which came from its environment.")
fx('fix', 'copy-paste leftover: “Complete vs. Incomplete” is about metamorphosis', '<div class="info-detail">Complete vs. Incomplete</div>', '<div class="info-detail">Inherited vs. Environmental</div>')
fx('fix', 'the chart listed plant height as environmental only; Part 2 says size is BOTH',
   '<text x="50" y="-4" font-size="14" font-weight="800" fill="#0E1C42">Plant height</text>\n            <text x="50" y="14" font-size="12" fill="#3F3F3F">Bigger with sun + water</text>',
   '<text x="50" y="-4" font-size="14" font-weight="800" fill="#0E1C42">A broken branch</text>\n            <text x="50" y="14" font-size="12" fill="#3F3F3F">From a storm, not from parents</text>')
fx('fix', 'the chart listed body strength as environmental only; Part 2 says strength is BOTH',
   '<text x="50" y="-4" font-size="14" font-weight="800" fill="#0E1C42">Body strength</text>\n            <text x="50" y="14" font-size="12" fill="#3F3F3F">Built up by exercise</text>',
   '<text x="50" y="-4" font-size="14" font-weight="800" fill="#0E1C42">A dented shell</text>\n            <text x="50" y="14" font-size="12" fill="#3F3F3F">From a fall or a bite</text>')
fx('fix', 'chart icon: the dented shell row had the strength icon', '<text x="0" y="0" font-size="34">💪</text>', '<text x="0" y="0" font-size="34">🐚</text>')
fx('fix', 'the chart’s description still named plant size and dog weight as environmental',
   'Right: environmental traits like scars, plant size from sunlight, dog weight from food.', 'Right: environmental traits like a scar, a broken branch, a dented shell and a tan.')
fx('fix', 'accuracy: turning toward the sun is an inherited ability; which way it points depends on the sun (and grown sunflowers stop turning and face east)',
   'data-part="Sunflower facing sun · ENVIRONMENTAL"', 'data-part="Sunflower facing sun · BOTH"')
fx('fix', 'accuracy: sunflower case text',
   r'data-info="Young sunflowers turn to follow the sun across the sky during the day\..*?"/>',
   'data-info="Young sunflowers turn to follow the sun across the sky. The ABILITY to turn is inherited: every young sunflower can do it. Which way a flower points right now depends on the environment: where the sun is. (Grown sunflowers stop turning and face east.) INHERITED + ENVIRONMENTAL."/>', True)
fx('fix', 'quarter label in the footer: week 13 is Quarter 2', 'Science &middot; Quarter 3 &middot;', 'Science &middot; Quarter 2 &middot;')
fx('fix', 'supply list: no notebook or sunny window needed (answers are typed on the page)',
   r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'pelican chicks aren’t the same color as adults; the warm-up now asks about a family from the game',
   r"<p>In your notebook, draw a quick sketch of two pelicans.*?</p>",
   "<p><strong>Find the family:</strong> match four Florida babies to their parents. Look closely. Some traits passed straight down. Others change as the baby grows up.</p>", True)

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; dash removed',
   "Picture a family photo: a brown-eyed mom, a brown-eyed dad, and three kids. Two kids have brown eyes. One has green eyes (just like Grandma). Some traits passed straight down. Others skipped a generation. And nobody got mom's accent — that came from where she grew up.",
   "Picture a family photo: a brown-eyed mom, a brown-eyed dad and three kids. Two kids have brown eyes. One has green eyes, just like Grandma. Nobody got Mom's accent (the way she says words). That came from where she grew up.")
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', 'one idea per paragraph; dash removed',
   "A baby pelican looks like a smaller pelican. A puppy looks like a smaller dog. A sunflower seedling, given time, becomes a sunflower again. Why? Because parents pass down their",
   "A baby pelican grows into a pelican. A sunflower seed grows into a sunflower. Why? Because parents pass down their")
fx('plain', 'shorter list', "Examples of inherited traits: eye color, beak shape, leaf shape, fur color (mostly), height (mostly), how a plant's flowers look. Offspring",
   "Eye color, beak shape, leaf shape and flower color are inherited traits. Offspring")
fx('plain', 'dashes removed; “stays small” → what really happens in shade (matches Grow the twins)',
   " — where you live, what you eat, how much sun you get — can affect traits too. A plant that gets lots of sun and water grows BIG; the same kind of plant in dry shade stays small. A puppy that's well fed grows full size; one that doesn't eat enough stays smaller.</p>",
   " (where you live, what you eat, how much sun you get) can change traits too. A plant with lots of sun and water grows big and bushy. The same kind of plant in shade grows thin, with few flowers. A puppy that eats well grows full size. One that doesn't get enough food stays smaller.</p>")
fx('plain', 'shorter; dash removed', "So when you see a trait on an offspring, the scientist's question is: did this come from the parents, or from where it grew up? Offspring show",
   "So a scientist asks: did this trait come from the parents, or from where it grew up? Offspring show")
fx('plain', 'dash removed', "Small differences between offspring and parents.</span></span> — they're never EXACTLY their parents.</p>",
   "Small differences between offspring and parents.</span></span>. They're never EXACTLY like their parents.</p>")
fx('plain', '“potential” → plain words', 'SIZE (you inherit the potential, but food and care decide if you reach it)', 'SIZE (parents pass down how big you COULD grow; food and care decide if you get there)')
fx('plain', 'shorter caption', '<strong>Some traits come from parents. Some come from the world around you.</strong> Many traits — like SIZE — are a mix of both.',
   '<strong>Some traits come from parents. Some come from the world around you.</strong> Many traits, like size, are a mix of both.')
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'dash removed; tease the next lesson in plain words',
   "Next lesson, you'll see how flowering plants actually MAKE the next generation — pollination, seeds, and germination.",
   "Next lesson, you'll find out how a flower makes the seeds for the next generation.")

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (sorting a real organism’s traits moves to Part C; Pass it on? is Part 4)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: the misconception paragraph is what Pass it on? (Part 4) teaches', r'\s*<p><strong>Common misconception:</strong>.*?</p>', '', True)
fx('cut', 'lean: the Key Concept box repeats Part 2', r'<div style="background:#FFF6E5;border:2.5px solid #F0C97A;[^"]*">\s*<div[^>]*>⭐ Key Concept</div>.*?</div>\s*', '', True)
fx('cut', 'lean: one thinking stop per tab (Stop & Think in Part 1 stays)', r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: the diagram heading becomes Part 3 (Stamp the case replaces the tap diagram)', 'margin-top:22px;">Four Florida Trait Cases</h3>', 'margin-top:22px;">Part 3 · Four Florida Trait Cases</h3>')
fx('cut', 'lean: Observe & Reason, the panther fact, the mangrove callout and Go Deeper at the end of the Lesson; Part 4 = Pass it on?; next button goes to Self-Check',
   r'<div class="socratic-q">\s*<span class="sq-icon">👀</span>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 4 · Pass It On?</h3>\n      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">A Florida panther mother has three new kittens in her den. Some of her traits she was born with. Others came from her life in the swamp. Which ones will her kittens get?</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 5 removed (Bethany kept 6 and 7; Stamp the case covers the four cases)', r'<div class="pq">\s*<span class="pq-num"[^>]*>5</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: Part B question 6 is now number 5', '<span class="pq-num" style="background:#D4772C;">6</span>', '<span class="pq-num" style="background:#D4772C;">5</span>')
fx('cut', 'lean: Part B question 7 is now number 6', '<span class="pq-num" style="background:#D4772C;">7</span>', '<span class="pq-num" style="background:#D4772C;">6</span>')
fx('cut', 'lean: Part C typed on the page (the drawing is a bonus)',
   r"In your notebook, draw a parent animal or plant and one of its offspring side by side\. Could be real or invented — a pelican \+ chick, a dog \+ puppy, a flower \+ seedling\.</p>\s*<p[^>]*>Label THREE inherited traits.*?</p>",
   "Pick a real Florida parent and its offspring: a pet, a backyard plant, or an animal from today. Name THREE traits the offspring inherited and TWO it could get from its environment.</p>", True)
fx('cut', 'lean: no Reflect', r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C typed on the page; the sketch is a bonus',
   'A parent + offspring drawing with 3 inherited traits and 2 environmental traits labeled clearly.',
   'A parent and offspring with 3 inherited traits and 2 environmental traits. (A sketch is a bonus.)')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether offspring are basically clones, and supported it with two pieces of evidence from the lesson.',
   '<strong>Use Your Evidence:</strong> My claim about whether offspring are clones of their parents, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', True)

# ---------------------------------------------------------------- data
CR = {
    'parent': 'Dune sunflowers on the sand, Miami Beach, Daniel Di Palma, via Wikimedia Commons (CC BY-SA 4.0)',
    'seeds': 'Dune sunflower seed heads, Miami Beach, Daniel Di Palma, via Wikimedia Commons (CC BY-SA 4.0)',
    'sun': 'Dune sunflowers, Sanibel Island, James St. John, via Wikimedia Commons (CC BY 2.0)',
    'shade': 'Beach sunflower with one tall stem, sonnia hill, via Wikimedia Commons (CC BY 2.0)',
    'leaf': 'Dune sunflower leaves, Sanibel Island, James St. John, via Wikimedia Commons (CC BY 2.0)',
    'kitten': 'Florida panther kitten, U.S. Army Corps of Engineers / Erica Skolte, via Wikimedia Commons (public domain)',
    'panther': 'Florida panther, George Gentry / U.S. Fish and Wildlife Service, via Wikimedia Commons (public domain)',
    'colt': 'Sandhill crane colt, NASA / Bill White, via Wikimedia Commons (public domain)',
    'crane': 'Sandhill crane, NASA / Bill White, via Wikimedia Commons (public domain)',
    'tbaby': 'Baby gopher tortoise, U.S. Fish and Wildlife Service, via Wikimedia Commons (public domain)',
    'gbaby': 'Alligator hatchlings, Everglades National Park / R. Cammauf, via Wikimedia Commons (public domain)',
    'pelican': 'Young brown pelican, Sarasota, Stuart Woodfin, via Wikimedia Commons (CC BY 2.0)',
    'manatee': 'Florida manatee with propeller scars, Robert K. Bonde / U.S. Fish and Wildlife Service, via Wikimedia Commons (public domain)',
    'sunflowers': 'Young sunflowers in a field, Timothy Akolamazima, via Wikimedia Commons (CC BY-SA 4.0)',
    'pmom': 'Florida panther mother carrying her kitten, on a U.S. Fish and Wildlife Service trail camera, via Wikimedia Commons (public domain)',
    'pkits': 'Florida panther kittens in their den, U.S. Fish and Wildlife Service, via Wikimedia Commons (public domain)',
}
OLD = json.load(open('../11-02/data.json', encoding='utf-8'))
def oldcredit(path):
    import re
    s = json.dumps(OLD, ensure_ascii=False)
    return None
D = {
    'lesson': '13.01', 'week': 13, 'day': 1, 'guide': 'lena', 'prefix': 'g4sci-13-1', 'manifestKey': '13-01',
    'paths': P['paths'], 'crew': P['crew'],
    'expedition': {'num': 13, 'title': 'One Parent, Two Gardens'},
    'ambient': {'icon': '🌊', 'label': 'Dune sounds'},
    'case': {
        'num': 13, 'title': 'One Parent, Two Gardens', 'style': 'tags',
        'hook': 'Last spring I collected seeds from ONE wild beach sunflower on the dunes. I planted some in our sunny dune garden and some in the shady courtyard behind the lab. Now the plants look so different that a volunteer wrote on the tags: “Mixed up? Different parents?”',
        'question': 'Did the seeds get mixed up, or can one parent plant have offspring this different?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'stills': [
            {'cam': 'Tag P · the parent plant', 'time': 'wild, on the dunes', 'tag': 'PARENT', 'kind': 'print', 'img': 'images/13-01-case-parent.jpg', 'alt': 'A wild beach sunflower growing on a sand dune: one yellow flower with a dark center and rough green leaves.'},
            {'cam': 'Tag S · its seeds', 'time': 'collected in May', 'tag': 'SEEDS', 'kind': 'print', 'img': 'images/13-01-case-seeds.jpg', 'alt': 'Dried brown flower heads on the parent plant. Each one is full of seeds.'},
            {'cam': 'Pot A · sunny dune garden', 'time': 'planted in June', 'tag': 'POT A', 'kind': 'print', 'img': 'images/13-01-case-sun.jpg', 'alt': 'A low, bushy patch of beach sunflowers covered in yellow flowers.'},
            {'cam': 'Pot B · shady courtyard', 'time': 'planted in June', 'tag': 'POT B', 'kind': 'print', 'img': 'images/13-01-case-shade.jpg', 'alt': 'One tall, thin beach sunflower stem with only one yellow flower.'},
        ],
        'stillsCredit': 'Parent: ' + CR['parent'] + '. Seeds: ' + CR['seeds'] + '. Pot A: ' + CR['sun'] + '. Pot B: ' + CR['shade'] + '. The tags and the gardens are part of the story.',
        'clues': [
            {'id': 'lineup', 'icon': '👪', 'where': 'Warm-Up: find the family', 't': 'Babies resemble their parents in inherited traits like body shape, even when other things (spots, stripes, size) are different for now.'},
            {'id': 'grow', 'icon': '🌱', 'where': 'The Lesson, Part 2: grow the twins', 't': 'Two seeds from one parent: sun and water changed the height, the spread and the number of flowers, but never the flower color or the leaf shape.'},
            {'id': 'verdict', 'icon': '🗂', 'where': 'The Lesson, Part 3: stamp the case', 't': 'Some traits are inherited (a pelican’s beak), some come from the environment (a manatee’s scars), and many are both (how tall an oak grows).'},
            {'id': 'passiton', 'icon': '🐾', 'where': 'The Lesson, Part 4: pass it on?', 't': 'Only inherited traits pass to the next generation. A scar, or being thin after a hard year, stays with the parent.'},
        ],
        'solve': {
            'title': 'What happened in the two gardens?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Someone mixed up the seeds. Plants that look this different must have different parents.', 'why': 'Check Clue 2. In Grow the twins, seeds from ONE parent looked very different in sun and in shade. Different looks don’t prove different parents.'},
                {'t': 'Same parent. Both plants have the same yellow flowers with dark centers and the same leaf shape: those are inherited. The shady plant grew tall and thin with few flowers because it got less sun: that’s the environment.', 'right': True,
                 'why': 'Case cracked! The seeds weren’t mixed up. Inherited traits matched; the garden changed the rest. Now write your case report: it’s the questions below.'},
                {'t': 'The shady plant changed its traits on purpose to reach the sun, so its seeds will grow tall and thin too.', 'why': 'Check Clue 4. Traits from the environment stay with that plant. They don’t pass to its seeds. And plants don’t choose their traits.'},
            ]},
    },
    'lineup': {
        'afterText': 'Find the family:', 'kicker': 'Warm-Up game', 'title': 'Find the family',
        'todo': ['Look at each baby’s body shape, not its colors.', 'Drag each baby onto its parent, or tap a baby and then a parent.', 'Find all four families, then answer the question.'],
        'why': {'icon': '👪', 'q': 'Why match families?', 't': 'Offspring (babies) inherit traits from their parents. Some babies look different at first, but their inherited traits give them away.'},
        'hint': 'Drag a baby onto its parent, or tap a baby and then a parent.',
        'babies': [
            {'id': 'panther', 'name': 'Spotted kitten', 'img': 'images/13-01-kitten.jpg', 'alt': 'A Florida panther kitten with dark spots and blue eyes.', 'miss': 'Look at the face and the round ears. Which parent has the same face shape?'},
            {'id': 'crane', 'name': 'Fluffy brown chick', 'img': 'images/13-01-colt.jpg', 'alt': 'A fluffy, rusty-brown chick with long legs, walking in shallow water.', 'miss': 'Look at the long legs and long neck. Which parent has them too?'},
            {'id': 'tortoise', 'name': 'Tiny shelled baby', 'img': 'images/13-01-tortoise-baby.jpg', 'alt': 'A tiny tortoise with a yellow and orange patterned shell.', 'miss': 'A dome-shaped shell and thick front legs. Which parent has the same shape?'},
            {'id': 'gator', 'name': 'Striped babies', 'img': 'images/13-01-gator-baby.jpg', 'alt': 'A group of baby alligators with bright yellow stripes, resting in the grass.', 'miss': 'Ignore the stripes. Look at the snout and the eyes on top of the head.'},
        ],
        'parents': [
            {'id': 'panther', 'name': 'Florida panther', 'img': 'images/13-01-panther.jpg', 'alt': 'An adult Florida panther with a plain tan coat, sitting in the grass.',
             'same': 'the face shape, round ears and long tail.', 'diff': 'the spots and blue eyes. The spots fade as the kitten grows, and its eyes turn golden brown.'},
            {'id': 'crane', 'name': 'Sandhill crane', 'img': 'images/13-01-crane.jpg', 'alt': 'A tall gray sandhill crane with a red patch on its head, standing by a tree in the water.',
             'same': 'long legs, a long neck and a long, pointed beak.', 'diff': 'the fluffy brown feathers. The chick (called a colt) grows gray feathers and a red cap later.'},
            {'id': 'tortoise', 'name': 'Gopher tortoise', 'img': 'images/11-02-kit-tortoise.jpg', 'alt': 'An adult gopher tortoise with a domed brown shell and thick front legs.',
             'same': 'the domed shell and thick front legs made for digging.', 'diff': 'the bright yellow shell. It turns brown and gray as the tortoise gets older.'},
            {'id': 'gator', 'name': 'American alligator', 'img': 'images/11-02-gator-head.jpg', 'alt': 'An adult alligator’s head with eyes and nostrils on top.',
             'same': 'the wide snout, the sharp teeth, and eyes and nostrils on top of the head.', 'diff': 'the yellow stripes. They fade as the alligator grows.'},
        ],
        'q': 'Look at all four families. Which is true?',
        'opts': [{'t': 'Babies look exactly like their parents.', 'miss': 'The kitten has spots and the chick is brown. Do they look EXACTLY like their parents?'},
                 {'t': 'Babies inherit their parents’ body shape, but some things, like spots or colors, can be different for now.', 'ok': True},
                 {'t': 'Babies pick which traits to copy from their parents.', 'miss': 'Babies can’t choose their traits. Where do inherited traits come from?'}],
        'credit': CR['kitten'] + '. ' + CR['panther'] + '. ' + CR['colt'] + '. ' + CR['crane'] + '. ' + CR['tbaby'] + '. ' + CR['gbaby'] + '. Adult tortoise and alligator: see the 11.02 photo credits.',
        'win': 'Four families found! Each baby inherited its parents’ body shape. Spots, stripes and fluffy feathers are traits that change as the baby grows. That’s a clue.',
        'clue': 'lineup'},
    'grow': {
        'afterText': 'can change traits too', 'kicker': 'Part 2 game', 'title': 'Grow the twins',
        'model': 'This is a model of Dr. Reyes’s test pots. Each pot gets one seed from the SAME parent beach sunflower.',
        'todo': ['Pick the sun and water for Pot A and Pot B.', 'Press ▶ Grow both pots and compare the plants.', 'Try a sunny pot AND a shady pot. Then answer the question.'],
        'why': {'icon': '🌻', 'q': 'Meet the beach sunflower', 't': 'A wild Florida flower that grows on sand dunes by the beach. It spreads low across the sand.'},
        'seedLine': 'a seed from the same parent plant',
        'dials': [{'k': 'sun', 't': 'Sun', 'opts': [{'k': 'sun', 'icon': '☀️', 't': 'Full sun'}, {'k': 'shade', 'icon': '🌳', 't': 'Shade'}]},
                  {'k': 'water', 't': 'Water', 'opts': [{'k': 'wet', 'icon': '💧', 't': 'Plenty'}, {'k': 'dry', 'icon': '🏜', 't': 'A little'}]}],
        'results': {
            'sun-wet': {'label': '☀️💧', 'img': 'images/13-01-case-sun.jpg', 'alt': 'A bushy beach sunflower with many flowers.', 'h': 30, 'w': 92, 'spread': 90, 'flowers': 24, 'note': 'Low, bushy and covered in flowers.'},
            'sun-dry': {'label': '☀️🏜', 'img': 'images/13-01-case-sun.jpg', 'alt': 'A small beach sunflower with a few flowers.', 'h': 15, 'w': 48, 'spread': 35, 'flowers': 8, 'note': 'Smaller, with fewer flowers.'},
            'shade-wet': {'label': '🌳💧', 'img': 'images/13-01-case-shade.jpg', 'alt': 'A tall, thin beach sunflower with one flower.', 'h': 55, 'w': 46, 'spread': 20, 'flowers': 3, 'note': 'Tall and thin: it stretched toward the light.'},
            'shade-dry': {'label': '🌳🏜', 'img': 'images/13-01-case-shade.jpg', 'alt': 'A short, thin beach sunflower with one flower.', 'h': 25, 'w': 30, 'spread': 10, 'flowers': 1, 'note': 'Thin and weak, with one flower.'}},
        'measures': [{'k': 'h', 't': '📏 Height', 'unit': 'cm'}, {'k': 'spread', 't': '↔️ Spread', 'unit': 'cm'}, {'k': 'flowers', 't': '🌼 Flowers', 'unit': ''}],
        'fixed': [{'t': '🎨 Flower color', 'v': 'yellow, dark center'}, {'t': '🍃 Leaf shape', 'v': 'rough, with wavy edges'}],
        'need': {'sun': ['sun', 'shade']},
        'needLine': 'Now change the sun: grow a sunny pot AND a shady pot.',
        'growBtn': '▶ Grow both pots (8 weeks)',
        'q': 'Which traits NEVER changed, no matter what garden you picked?',
        'opts': [{'t': 'Height and number of flowers', 'miss': 'Look at your results. Did the height change between gardens?'},
                 {'t': 'Flower color and leaf shape', 'ok': True},
                 {'t': 'Nothing stayed the same', 'miss': 'Check the green rows in each pot’s results. Did they ever change?'}],
        'credit': CR['sun'] + '. ' + CR['shade'] + '.',
        'win': 'Same parent, different gardens. Sun and water changed the height, spread and flowers (environment). Flower color and leaf shape never changed (inherited). That’s a clue.',
        'clue': 'grow'},
    'verdict': {
        'replace': '#tab-lesson .diagram-wrap', 'kicker': 'Part 3 game', 'title': 'Stamp the case',
        'todo': ['Open a case and read the facts.', 'Stamp it INHERITED, ENVIRONMENT or BOTH.', 'Pick the fact that proves it. Stamp all four.'],
        'why': {'icon': '🗂', 'q': 'Three stamps', 't': 'INHERITED = from the parents. ENVIRONMENT = from where it lives and what happens to it. BOTH = the parents give the start, and the environment shapes the rest.'},
        'stamps': [{'k': 'inh', 'icon': '👪', 't': 'INHERITED'}, {'k': 'env', 'icon': '🌍', 't': 'ENVIRONMENT'}, {'k': 'both', 'icon': '⚖️', 't': 'BOTH'}],
        'stories': [
            {'id': 'pelican', 'name': 'Pelican beak shape', 'img': 'images/13-01-pelican.jpg', 'alt': 'A young brown pelican with a long, straight beak.',
             'data': ['Every brown pelican has a long beak with a stretchy pouch underneath.', 'Chicks hatch with a short beak of the same shape. It grows longer.', 'Pelicans that catch lots of fish and pelicans that catch few have the same beak shape.'],
             'answer': 'inh', 'stampMiss': 'Does the beak shape change with what a pelican eats or where it lives? Read the facts again.',
             'proof': [{'t': 'Every pelican has the same beak shape, no matter how much it eats.', 'ok': True}, {'t': 'Pelicans live near the ocean.', 'miss': 'True, but does that prove where the beak shape came from?'}, {'t': 'Some pelicans are bigger than others.', 'miss': 'That’s about size, not beak shape.'}],
             'why': 'The beak shape comes from the parents. It’s the same in every pelican, whatever its life is like.'},
            {'id': 'manatee', 'name': 'A manatee’s scars', 'img': 'images/13-01-manatee-scars.jpg', 'alt': 'A gray manatee underwater with two long white scars on its back.',
             'data': ['Many Florida manatees have long white scars on their backs.', 'The scars come from boat propellers (the spinning blades that push a boat).', 'Manatee calves are born with smooth skin and no scars.'],
             'answer': 'env', 'stampMiss': 'Were the calves born with these scars? Read the facts again.',
             'proof': [{'t': 'Calves are born with no scars. The scars come from boat injuries.', 'ok': True}, {'t': 'Manatees are gray.', 'miss': 'That’s about color, not the scars.'}, {'t': 'Manatees swim slowly.', 'miss': 'Swimming slowly is why boats hit them, but what proves the scars aren’t inherited?'}],
             'why': 'Scars come from the environment, not the parents. Scientists use each manatee’s scar pattern to tell it apart from others.'},
            {'id': 'oak', 'name': 'How tall a live oak grows', 'img': 'images/10-01-live-oak.jpg', 'alt': 'A huge live oak tree with wide, spreading branches.',
             'data': ['A live oak acorn always grows into a live oak, never a palm.', 'In an open, sunny field, a live oak can grow huge and wide.', 'The same kind of tree squeezed into a small, shady spot stays much smaller.'],
             'answer': 'both', 'stampMiss': 'One fact is about the parents and two are about the place it grows. What does that tell you?',
             'proof': [{'t': 'It’s a live oak because of its parents, but sun and space change how big it grows.', 'ok': True}, {'t': 'Live oaks grow in Florida.', 'miss': 'True, but which fact shows two causes?'}, {'t': 'Oak trees make acorns.', 'miss': 'True, but that doesn’t explain its height.'}],
             'why': 'Both! The parents give the tree the ability to grow tall. Sun, water, soil and space decide how tall it really gets.'},
            {'id': 'sunflower', 'name': 'A sunflower turning to the sun', 'img': 'images/13-01-sunflowers.jpg', 'alt': 'A field of young sunflowers, all facing the same direction.',
             'data': ['Young sunflowers turn to follow the sun across the sky.', 'Every young sunflower can do this. The ability comes from its parents.', 'Which way a flower points right now depends on where the sun is.'],
             'answer': 'both', 'stampMiss': 'One fact is about the parents and one is about the sun. What does that tell you?',
             'proof': [{'t': 'The ability to turn is inherited, but where it points depends on the sun.', 'ok': True}, {'t': 'Sunflowers are yellow.', 'miss': 'That’s about color, not turning.'}, {'t': 'Sunflowers are tall.', 'miss': 'That’s about height, not turning.'}],
             'why': 'Both! The ability to turn is inherited. Where the flower points depends on the sun. (Grown sunflowers stop turning and face east.)'},
        ],
        'credit': CR['pelican'] + '. ' + CR['manatee'] + '. Southern live oak with resurrection ferns, JamesDeMers, via Wikimedia Commons (CC0). ' + CR['sunflowers'] + '.',
        'win': 'Four cases stamped! Some traits are inherited, some come from the environment, and many are both. That’s a clue.',
        'clue': 'verdict'},
    'passiton': {
        'afterText': 'Which ones will her kittens get', 'kicker': 'Part 4 game', 'title': 'Pass it on?',
        'todo': ['Read each of the mother’s traits.', 'Guess: will it pass to her kittens, or stay with her?', 'Press ▶ Next generation to see what the kittens got.'],
        'why': {'icon': '🐾', 'q': 'What is a generation?', 't': 'A generation is one step in a family: parents are one generation, and their babies are the next.'},
        'parent': {'name': 'The mother panther', 'img': 'images/13-01-pan-mom.jpg', 'alt': 'A trail camera photo of a Florida panther mother carrying her kitten in her mouth.'},
        'kids': {'name': 'Her three kittens', 'img': 'images/13-01-pan-kits.jpg', 'alt': 'Three spotted Florida panther kittens with blue eyes in their den.'},
        'yes': 'Passed to the kittens', 'no': 'Stays with mom',
        'traits': [
            {'id': 'tail', 'icon': '〰️', 't': 'A kink (a sharp bend) at the tip of her tail. She was born with it.', 'short': 'The kinked tail', 'pass': True,
             'why': 'Inherited traits pass down. Kinked tails were once common in Florida panther families, passed from parents to kittens.'},
            {'id': 'scar', 'icon': '🩹', 't': 'A scar on her nose from an old fight.', 'short': 'The scar', 'pass': False,
             'why': 'A scar comes from something that happened to her (the environment). Her kittens are born without it.'},
            {'id': 'ears', 'icon': '👂', 't': 'Round ears and a long, thick tail, like every Florida panther.', 'short': 'Round ears and a long tail', 'pass': True,
             'why': 'All Florida panthers inherit these from their parents. Every kitten has them too.'},
            {'id': 'thin', 'icon': '🦌', 't': 'She is thin because deer were hard to find this year.', 'short': 'Being thin', 'pass': False,
             'why': 'Her body changed because of not enough food (the environment). Kittens that eat well will grow to full size.'},
        ],
        'nextBtn': '▶ Next generation',
        'q': 'Why didn’t the kittens get the scar?',
        'opts': [{'t': 'The scar came from the environment, so it can’t be passed down.', 'ok': True},
                 {'t': 'The kittens are too young to have a scar yet.', 'miss': 'Even when they grow up, they won’t get HER scar. Where did the scar come from?'},
                 {'t': 'Only fathers pass down traits.', 'miss': 'Both parents pass down inherited traits. Where did the scar come from?'}],
        'credit': CR['pmom'] + '. ' + CR['pkits'] + '. This panther family is part of the lesson’s story.',
        'win': 'Only inherited traits pass to the next generation. Things that happen to a parent, like a scar or a hungry year, stay with that parent. That’s your last clue.',
        'clue': 'passiton'},
    'exploreMod': 'passiton',
    'quizKicker': '',
    'quizMiss': {
        'q1': {'B': 'Can a puppy choose what it looks like?', 'C': 'Growing up in one place doesn’t give a puppy its mother’s ear shape. What does?'},
        'q2': {'A': 'Did the flower’s parents have that color too?', 'B': 'Is an alligator born with scaly skin?'},
        'q3': {'A': 'Read again: both seedlings came from the same parent plant.', 'C': 'If size were 100% inherited, would the two seedlings be different sizes?'}},
    'flags': {
        'ans-2': [
            {'label': 'what inherited means', 're': 'inherit|parent|born with|pass|mom|dad|mother|father|family'},
            {'label': 'what environment means', 're': 'environ|where|live|food|eat|sun|water|happen|injur|scar|grow up|place'},
            {'label': 'a Florida example of each', 'any': ['pelican', 'beak', 'manatee', 'scar', 'oak', 'tree', 'sunflower', 'flower', 'panther', 'kitten', 'spot', 'alligator|gator', 'stripe', 'tortoise', 'crane', 'turtle', 'shell', 'leaf|leaves', 'color', 'tail', 'tan', 'branch', 'height|tall', 'dent'], 'min': 2}],
        'ans-3': [
            {'label': 'inherited', 're': 'inherit|parent|same mom|same mother|born with|pass'},
            {'label': 'environment', 're': 'environ|food|eat|home|care|place|grew up|hungry'},
            {'label': 'which traits differ', 're': 'size|big|small|tall|short|weigh|strong|healthy|thin|fat|fur|shin'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|wrong|right|true|not true|clone|not'},
            {'label': 'two pieces of evidence', 'any': ['sunflower|pot', 'shade|sun', 'scar', 'manatee', 'kitten|panther', 'spot', 'stripe|gator|alligator', 'oak|tree', 'environ', 'variation|differ', 'puppy|puppies', 'tail', 'food|water'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves'}]},
    'minWords': {'ans-2': 20, 'ans-3': 15, 'cer-4': 30},
    'hints': {
        'ans-2': ['Inherited = from the parents. Environment = from where it lives and what happens to it.', 'Think of the cases you stamped in Part 3: the pelican’s beak and the manatee’s scars.', 'Try: An inherited trait ___. For example, ___. An environmental trait ___. For example, ___.'],
        'ans-3': ['The puppies have the same parents. What did they inherit?', 'Think of Grow the twins: same parent, different gardens.', 'Try: The puppies inherited ___ from their parents. But the environment ___, so ___.'],
        'cer-4': ['First decide: are offspring clones (exact copies) of their parents?', 'Think of the two gardens, the kittens’ spots, or the manatee’s scars.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'Seeds from one beach sunflower grew very differently in sun and in shade.',
                'Panther kittens have spots that their mother doesn’t have.',
                'A manatee’s scars come from boats, not from its parents.',
                'Siblings from the same parents still have small differences (variation).',
                'An oak’s height depends on its parents AND on sun and space.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · one parent, two gardens', 'length': '30–40 s',
                    'script': 'Hi, it’s Dr. Reyes. Last spring I collected seeds from one wild beach sunflower on the dunes. I planted some in the sunny dune garden and some in the shady courtyard. Look at the two pots in the case file. They look so different! A volunteer thinks the seeds got mixed up. Did they? Help me find out.'},
        'warmup': {'label': 'Warm-Up · find the family (Clue 1)', 'length': '20–30 s',
                   'script': 'Here’s a field trick. When you match a baby to its parents, don’t look at colors first. Look at the shape: the legs, the snout, the shell. Some babies wear spots or stripes that fade later. Their body shape gives them away.'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Say each word. For resemble, point to a family photo.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · traits are passed down', 'length': '20–30 s'},
        'part2': {'label': 'Part 2 · grow the twins (Clue 2)', 'length': '25–35 s',
                  'script': 'This is my favorite test. Two seeds, same parent. You pick the garden for each pot: sun or shade, plenty of water or a little. Then grow them. Watch which traits change, and which ones never change at all. Make sure you try one pot in the shade.'},
        'figure': {'label': 'The inherited or environmental chart', 'length': '20–30 s'},
        'part3': {'label': 'Part 3 · stamp the case (Clue 3)', 'length': '20–30 s',
                  'script': 'Four Florida cases, three stamps. Inherited means from the parents. Environment means from where it lives, or something that happened to it. Both means a little of each. Read the facts, stamp it, then pick the fact that proves it.'},
        'explore': {'label': 'Part 4 · pass it on? (Clue 4)', 'length': '25–35 s',
                    'script': 'A panther mother just had three kittens. She has a kinked tail, a scar on her nose, and she’s thin after a hard year. Which of those will her kittens get? Make your guess for each one, then press Next generation. Don’t worry if a guess is wrong. That’s how scientists learn.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s',
                       'script': 'Do you have all four clues? Crack the case at the top of this tab: did my seeds get mixed up? Then answer two questions, write about a parent and its offspring, and write your CER. Your answers save as you type.'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · parent and offspring', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says babies are basically clones of their parents. Clones are exact copies. Hmm. Think about my two sunflower pots, the spotted kittens, the manatee’s scars. Are babies exact copies? Pick your side, tap two pieces of evidence in the planner, then explain how they prove your claim.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 13.02 (how a flower makes seeds).',
                    'script': 'Case closed! My seeds weren’t mixed up. Same parent, different gardens. The flower color and leaves came from the parent, and the sun did the rest. Next time, a new question: how did that one beach sunflower make all those seeds in the first place?'},
    },
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'All four families matched (Warm-Up)',
        'Your sunny pot next to your shady pot (The Lesson)',
        'The kittens after Next generation (The Lesson)',
        'The answer that cracked the case (Assignment)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['A parent and its offspring', 'My sunny pot and my shady pot', 'A trait that passes down'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 2,
                           'prompts': ['The parent and its offspring side by side', 'Label 3 inherited traits', 'Label 2 traits from the environment']}]},
    'hlCoach': copy.deepcopy(P['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🌻', 'name': 'Beach sunflower seed packet',
                 'line': 'You cracked Case 13, and a packet of beach sunflower seeds goes in your Field Notebook. (A specimen is something a scientist collects to study.) Next lesson: how did one flower make all those seeds?'},
    'notebookTitle': P['notebookTitle'],
    'notebook': [dict(x) for x in Q['notebook']],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You’ll use every one of them today.',
    'tool': {
        'name': 'Digital calipers', 'icon': '📏', 'tab': 'assignment', 'after': '#tab-assignment .activity-card', 'key': '13-tool', 'sim': 'calipers',
        'kicker': 'Bonus · Tool of the Week',
        'teaser': 'Measure leaves from one parent plant, grown in sun and in shade. Does the garden change the leaves?',
        'done': 'You measured all six leaves and found the pattern. A calipers sticker is in your Field Notebook.',
        'why': {'icon': '📏', 'q': 'What are calipers?', 't': 'A tool that measures small things very exactly. You close the jaws on the object and read the length, in millimeters (mm), on the screen.'},
        'calipers': {
            'title': 'Sun leaves vs. shade leaves',
            'todo': ['Tap a leaf. The jaws close on it and the screen shows its length.', 'Measure all three leaves from each pot.', 'Look at the dots, then answer the question.'],
            'leafImg': 'images/13-01-leaf.jpg', 'maxMm': 100,
            'groups': [{'k': 'a', 'icon': '☀️', 't': 'Pot A · sunny garden', 'short': 'Pot A (sun)', 'leaves': [42, 55, 48]},
                       {'k': 'b', 'icon': '🌳', 't': 'Pot B · shady courtyard', 'short': 'Pot B (shade)', 'leaves': [71, 63, 78]}],
            'credit': 'Leaf photo: ' + CR['leaf'] + '. The leaf lengths are a model.',
            'q': {'q': 'What do your measurements show?', 'opts': [
                {'t': 'Every leaf is exactly the same length.', 'why': 'Look at the dots. Are any two leaves the same?'},
                {'t': 'The leaves vary, and the shade leaves are bigger on average.', 'ok': True,
                 'why': 'Yes! Leaves from one parent still vary a little (variation). And shade leaves grew bigger, to catch more of the dim light. That’s the environment at work.'},
                {'t': 'The shade plant must have a different parent.', 'why': 'Both pots grew from the same parent’s seeds. What else was different between the pots?'}]}}},
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'list', 'find': {'sel': '.fs-game[data-mod="lineup"]'},
         'label': 'Warm-Up: inherited traits I spotted', 'q': 'Warm-Up: Pick one family from the game. List traits the baby inherited from its parent.',
         'title': 'Your turn: pick one family. List two traits the baby inherited from its parent.', 'min': 2, 'unit': 'traits', 'addLabel': '+ Add a trait', 'ph': ['Family: ___. The baby inherited…', 'It also inherited…']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'hide-nw', 'type': 'hide', 'find': {'sel': '.act-warmup .socratic-q', 'text': 'Notice'}},
        {'id': 'hide-tip', 'type': 'hide', 'find': {'sel': '.act-warmup .callout', 'text': 'Today'}},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Pick a real Florida parent and its offspring'},
         'label': 'Part C: My parent and offspring', 'q': 'Part C: A Florida parent and its offspring: three inherited traits and two traits from the environment',
         'title': 'My parent and offspring',
         'fields': [{'t': 'The parent and its offspring', 'icon': '👪', 'ph': 'Parent: ___. Offspring: ___.'},
                    {'t': 'Three traits the offspring inherited', 'icon': '🧬', 'ph': '1. ___ 2. ___ 3. ___', 'long': True},
                    {'t': 'Two traits it could get from its environment', 'icon': '🌍', 'ph': '1. ___ 2. ___', 'long': True},
                    {'t': 'How I can tell the difference', 'icon': '🔎', 'ph': 'I can tell because…', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Are offspring clones (exact copies) of their parents?', 'ph': 'I disagree. Offspring are not clones because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-2': 'Part B · Question 5', 'ans-3': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
del D['lineup']['credit']
D['lineup']['credit'] = CR['kitten'] + '. ' + CR['panther'] + '. ' + CR['colt'] + '. ' + CR['crane'] + '. ' + CR['tbaby'] + '. ' + CR['gbaby'] + '. Adult gopher tortoise at its burrow, Andrea Westmoreland, via Wikimedia Commons (CC BY-SA 2.0). American alligator head, Stephenx77, via Wikimedia Commons (public domain).'
for n in D['notebook']:
    if n['lesson'] in ('12.01', '12.02'): n['have'] = True
    if n['lesson'] == '13.01': n.update({'icon': '🌻', 'name': 'Beach sunflower seed packet'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'Offspring inherit many traits from their parents, but the environment shapes other traits.',
    'key': ['Offspring', 'inherit', 'traits', 'parents', 'environment', 'shapes'],
    'small': ['many', 'from', 'their', 'but', 'the', 'other'],
    'model': 'A scientist might highlight “inherit”, “parents” and “environment”. Those words carry the idea. Small words like “the” and “but” don’t.'}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
