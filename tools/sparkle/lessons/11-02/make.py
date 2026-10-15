#!/usr/bin/env python3
"""Writes data.json and fixes.json for 11.02 (run from this folder)."""
import json, copy
P = json.load(open('../11-01/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

# ticked fixes (Bethany, 15 Oct 2026)
fx('fix', 'quarter label: week 11 is Quarter 2', 'Q3 &middot; Week 11', 'Q2 &middot; Week 11')
fx('fix', 'quarter label in the footer', 'Science &middot; Quarter 3 &middot;', 'Science &middot; Quarter 2 &middot;')
fx('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist asks for an annotated model', '🎨 Part C &mdash; Build Your Own Food Chain', '🎨 Part C &mdash; Build an Annotated Model')
fx('fix', 'copy-paste leftover: Part C task from 9.01',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Pick one Florida organism and one of its structures (not the spoonbill). Build a model in words: name the structure, tell what it does (that\'s your arrow), and finish with a caption that ties it to a survival need.</p>', True)
fx('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'copy-paste leftover: supply list (every lesson lists a sunny window)', '<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '')
fx('fix', 'accuracy: NGSS does not name exactly four “model types”; plain words',
   r'A model can be a drawing on paper, a clay sculpture, a digital diagram, or even an explanation you say out loud\. NGSS calls these "<span class="vtip">model<span class="vtip-box">.*?</span></span> types": two-dimensional \(flat\), three-dimensional \(solid\), in-your-mind \(mental\), or computer model\. They\'re all useful for different jobs\.',
   'Scientists use many kinds of models: a drawing on paper, a clay build, a computer model, or even a clear explanation you say out loud. Each kind is good for a different job.', True)

# plain language
fx('plain', 'shorter; dashes removed',
   "Hold this question in your head as you work. By the end of the lesson, you'll build your own model — a drawing with labels and arrows — that <em>explains</em> how a Florida animal's structure helps it meet a survival need.",
   "Keep this question in mind. By the end, you'll build your own model, a drawing with labels and arrows that <em>explains</em> how a Florida animal's body part helps it meet a survival need.")
fx('plain', 'the notebook drawing becomes the on-page arrow game',
   r'<p>In your notebook, draw a Florida alligator quickly.*?</ul>',
   '<p>Here is an alligator, shown two ways. <strong>Drawing 1</strong> just has a label. <strong>Drawing 2</strong> is a tiny model: an arrow shows what the part does. Build Drawing 2 below.</p>', True)
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', '“relationship” → plain words',
   "A model goes one step further: it explains a <em>relationship</em>. It tells your reader why something matters.",
   "A model goes one step further: it explains <em>how the part helps</em>. It tells your reader why the part matters.")
fx('plain', '“misconception” → plain words; shorter',
   "<strong>Common misconception:</strong> A really pretty drawing is <em>not</em> the same as a strong model. A simple stick-figure drawing with good labels and arrows can be a stronger model than a beautiful artwork with no explanation. The model's job is to make the relationship clear, not to look fancy.",
   "<strong>A mix-up to watch for:</strong> A pretty drawing is <em>not</em> the same as a strong model. A stick figure with good labels and arrows can explain more than a beautiful painting with no words. A model's job is to explain, not to look fancy.")
fx('plain', 'dash removed', '<strong>This is a model — not just a label.</strong>', '<strong>This is a model, not just a label.</strong>')
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', '“module” → “week”; dash removed',
   " — not just label one. Next module, we'll move from structures to <em>behaviors</em>: how Florida animals use their senses, send information to the brain, and respond to the world around them.",
   ", not just label one. Next week, we'll move from body parts to <em>behaviors</em>: how Florida animals use their senses, send messages to the brain, and react to the world around them.")

# lean cuts
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (the model build moves to the Lesson as Part 4)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: the Key Concept box repeats Part 2', r'<div style="background:#FFF6E5;border:2.5px solid #F0C97A;[^"]*">\s*<div[^>]*>⭐ Key Concept</div>.*?</div>\s*', '', True)
fx('cut', 'lean: the diagram heading becomes Part 3 (the Chain it game replaces the tap diagram)',
   'margin-top:22px;">Four Models of Florida Adaptations</h3>', 'margin-top:22px;">Part 3 · Structure → Action → Survival Need</h3>')
fx('cut', 'lean: Observe & Reason, the pine fact, the panther callout and Go Deeper at the end of the Lesson (the pine-cone fact and the panther paws were shaky); Part 4 = the old Explore; next button goes to Self-Check',
   r'<div class="socratic-q">\s*<span class="sq-icon">👀</span>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 4 · Build Your Own Model</h3>\n      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">Now it\'s your turn. Pick a Florida organism, pick one of its structures, and turn it into a model: a label, an arrow that shows what the part does, and a caption about a survival need.</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 5 removed (Bethany kept 6 and 7)', r'<div class="pq">\s*<span class="pq-num"[^>]*>5</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: Part B question 6 is now number 5', '<span class="pq-num" style="background:#D4772C;">6</span>', '<span class="pq-num" style="background:#D4772C;">5</span>')
fx('cut', 'lean: Part B question 7 is now number 6', '<span class="pq-num" style="background:#D4772C;">7</span>', '<span class="pq-num" style="background:#D4772C;">6</span>')
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C is a model in words; the sketch is a bonus',
   'An annotated model of one Florida adaptation — including the organism, the structure, an arrow showing action, and a caption tying the structure to a survival need.',
   'A model of one Florida organism’s structure: the label, what it does (the arrow), and a caption about a survival need. (A sketch is a bonus.)')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether drawings count as science, and supported it with two pieces of evidence from the lesson.',
   '<strong>Use Your Evidence:</strong> My claim about whether drawings count as science, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', True)

# ---------------------------------------------------------------- data
NEEDS = ['food', 'water', 'air', 'shelter', 'safety']
def needs(ok, a, b):
    return [{'t': ok, 'ok': True}, {'t': a, 'miss': 'Ask: what does this part help the animal get or stay away from?'}, {'t': b, 'miss': 'Look at the arrow again. Which need does that action help with?'}]
D = {
    'lesson': '11.02', 'week': 11, 'day': 2, 'guide': 'lena', 'prefix': 'g4sci-11-2', 'manifestKey': '11-02',
    'paths': P['paths'], 'crew': P['crew'],
    'expedition': {'num': 11, 'title': 'The Refuge Sign'},
    'ambient': P['ambient'],
    'case': {
        'num': '11 · part 2', 'title': 'The Refuge Sign', 'style': 'notebook',
        'hook': 'Good news! The refuge read our case report on the spoonbill. Now they want a sign about it for the boardwalk where I found the soggy notebook. Three people sent drafts, and I taped them into my notebook. Only one can go on the sign.',
        'question': 'Which draft explains how the spoonbill survives, and what would make the other two better?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'stills': [
            {'cam': 'Draft A', 'time': 'a photo with labels', 'tag': 'A', 'img': 'images/11-02-draft-labels.jpg', 'alt': 'A photo of a spoonbill feeding, with three labels: beak, legs, feathers. There are no arrows and no sentences.'},
            {'cam': 'Draft B', 'time': 'a painting from 1836', 'tag': 'B', 'img': 'images/11-02-draft-painting.jpg', 'alt': 'A beautiful old painting of a pink spoonbill bending down to the water. There are no labels, arrows or words about the bird.'},
            {'cam': 'Draft C', 'time': 'a photo with arrows', 'tag': 'C', 'img': 'images/11-02-draft-model.jpg', 'alt': 'The spoonbill photo with labels, arrows from the beak and legs to what they do, and a caption about food.'},
            {'cam': 'Where the sign goes', 'time': 'the shallow lagoon', 'tag': '📍', 'img': 'images/11-01-case-flock.jpg', 'alt': 'Pink spoonbills standing in a shallow lagoon, with mangroves behind them.'},
        ],
        'stillsCredit': 'Drafts A and C are built on a real photo: roseate spoonbill feeding, Andy Morffew (CC BY 2.0). Draft B: Roseate Spoonbill, Robert Havell after John James Audubon, 1836, National Gallery of Art (CC0). Lagoon: James St. John (CC BY 2.0). All via Wikimedia Commons.',
        'clues': [
            {'id': 'arrow', 'icon': '➜', 'where': 'Warm-Up: point the arrow', 't': 'A label only names a part. An arrow from the part to what it acts on, with a few action words, turns a drawing into a model.'},
            {'id': 'upgrade', 'icon': '⬆️', 'where': 'The Lesson, Part 2: upgrade the drawing', 't': 'A strong model has three things: labels, arrows that show action, and a caption that ties the part to a survival need.'},
            {'id': 'chain', 'icon': '🔗', 'where': 'The Lesson, Part 3: chain it', 't': 'Every model follows the same chain: structure → action → survival need. A color or a name alone isn’t a link.'},
            {'id': 'kit', 'icon': '🧩', 'where': 'The Lesson, Part 4: the model kit', 't': 'You built a model on a real photo. Any picture, even a pretty one, becomes a model when you add labels, arrows and a caption.'},
        ],
        'solve': {
            'title': 'Which draft goes on the sign?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Draft B, the painting, because it’s the most beautiful.', 'why': 'Check Clue 4. A painting is lovely, but with no labels or arrows a visitor can’t tell what the beak does.'},
                {'t': 'Draft A, because it names every part.', 'why': 'Check Clue 1. Names alone don’t tell what the parts do.'},
                {'t': 'Draft C. It has labels, arrows that show what the beak and legs do, and a caption about food. Draft A needs arrows and a caption. Draft B needs labels, arrows and a caption.', 'right': True,
                 'why': 'Case closed for good! Draft C is a model: it explains, not just names. Now write your case report: it’s the questions below.'},
            ]},
    },
    'arrow': {
        'afterText': 'Build Drawing 2 below', 'kicker': 'Warm-Up game', 'title': 'Point the arrow',
        'todo': ['Drag the arrow to what the teeth act on, or tap that box.', 'Pick the action words for your arrow.', 'Compare Drawing 1 and Drawing 2.'],
        'why': {'icon': '➜', 'q': 'What does an arrow do in a model?', 't': 'In a model, an arrow points from a part to the thing it acts on. The words on the arrow tell what the part does.'},
        'img': 'images/11-02-gator-head.jpg', 'alt': 'A close-up of an American alligator’s head resting on the ground, with its teeth showing along its jaw.',
        'credit': 'American alligator head, Stephenx77, via Wikimedia Commons (public domain).',
        'label': {'t': 'teeth', 'x': 14, 'y': 74}, 'from': {'x': 34, 'y': 74}, 'at': {'x': 82, 'y': 86},
        'tokenLabel': 'Arrow',
        'q1': 'Step 1: Where should the arrow point?',
        'targets': [{'k': 'sun', 'icon': '☀️', 't': 'the sun', 'miss': 'Teeth don’t do anything to the sun. What do they grab?'},
                    {'k': 'fish', 'icon': '🐟', 't': 'a fish', 'ok': True},
                    {'k': 'rock', 'icon': '🪨', 't': 'a rock', 'miss': 'A gator doesn’t eat rocks. What does it catch with its teeth?'}],
        'q2': 'Step 2: What do the teeth do? Pick the words for your arrow.',
        'actions': [{'t': 'look scary', 'miss': 'That’s a feeling, not a job. What do the teeth do to the fish?'},
                    {'t': 'teeth', 'miss': 'That’s just the label again. What do the teeth DO?'},
                    {'t': 'grab and hold prey', 'ok': True}],
        'left': 'Drawing 1 · just a label', 'right': 'Drawing 2 · your tiny model',
        'win': 'That’s a tiny model! Drawing 2 tells a friend what the teeth do, not just what they’re called. That’s a clue.',
        'clue': 'arrow'},
    'upgrade': {
        'afterText': 'Each kind is good for a different job', 'kicker': 'Part 2 game', 'title': 'Upgrade the drawing',
        'todo': ['Answer each step to add one thing to the photo.', 'Watch the meter at the top.', 'Finish all three steps.'],
        'why': {'icon': '⬆️', 'q': 'Why upgrade?', 't': 'A labeled drawing names a part. Each thing you add tells the reader more about how the part helps the bird survive.'},
        'img': 'images/11-01-wade-spoonbill.jpg', 'alt': 'A pink roseate spoonbill bending down with its long beak in dark, shallow water.',
        'credit': 'Roseate spoonbill feeding, Andy Morffew, via Wikimedia Commons (CC BY 2.0).',
        'label': {'x': 28, 'y': 42}, 'from': {'x': 45, 'y': 63}, 'to': {'x': 24, 'y': 87},
        'meter': ['Just a photo', 'A labeled drawing', 'Almost a model', 'A model!'],
        'steps': [
            {'k': 'label', 'q': 'Add a label. Which part will this model explain?', 'opts': [
                {'t': 'PINK', 'miss': 'Pink is a color, not a part.'}, {'t': 'BEAK', 'ok': True}, {'t': 'SPOONBILL', 'miss': 'That’s the whole bird. A label names one part.'}]},
            {'k': 'arrow', 'q': 'Add an arrow. What does the beak do?', 'opts': [
                {'t': 'is long', 'miss': 'That describes its shape. What does it DO?'}, {'t': 'looks like a spoon', 'miss': 'That’s its shape again. What job does it do in the water?'}, {'t': 'sweeps + feels for shrimp', 'ok': True}]},
            {'k': 'caption', 'q': 'Add a caption that ties it to a survival need.', 'opts': [
                {'t': 'This beak helps the spoonbill meet its survival need for food.', 'ok': True},
                {'t': 'This is a roseate spoonbill.', 'miss': 'That’s just a name. Which survival need does the beak help with?'},
                {'t': 'Spoonbills are very pretty.', 'miss': 'Pretty isn’t a survival need. Food, water, air, shelter or safety?'}]}],
        'win': 'Label, arrow, caption: that’s a model! That’s a clue.',
        'clue': 'upgrade'},
    'chain': {
        'kicker': 'Part 3 game', 'title': 'Chain it',
        'todo': ['Pick an organism.', 'Drag each card into its link, or tap a card and then a link.', 'Build all four chains.'],
        'why': {'icon': '🔗', 'q': 'Why a chain?', 't': 'A model explains in order: first the part, then what it does, then which survival need it meets.'},
        'slots': [{'k': 's', 'icon': '🦴', 't': 'Structure'}, {'k': 'a', 'icon': '⚙️', 't': 'Action'}, {'k': 'n', 'icon': '🍎', 't': 'Survival need'}],
        'hint': 'Drag each card into its link, or tap a card and then a link. Two cards don’t belong in the chain.',
        'missX': 'That card is true, or it’s a name, but it isn’t a link. A link is a part, what the part does, or the need it meets.',
        'missSlot': {'s': 'That card is a part. Put it in the Structure link.', 'a': 'That card is an action, something a part does.', 'n': 'That card is a survival need: food, water, air, shelter or safety.'},
        'orgs': [
            {'id': 'frog', 'name': 'Green tree frog', 'icon': '🐸', 'cards': [{'t': 'Bright green skin', 'k': 's'}, {'t': 'Blends in with the leaves', 'k': 'a'}, {'t': 'Safety from snakes and birds', 'k': 'n'}, {'t': 'Green tree frog', 'k': 'x'}, {'t': 'Green is a nice color', 'k': 'x'}],
             'why': 'Green skin → blends in → safety. That’s camouflage, a color adaptation.'},
            {'id': 'tortoise', 'name': 'Gopher tortoise', 'icon': '🐢', 'cards': [{'t': 'Thick, shovel-shaped front legs', 'k': 's'}, {'t': 'Dig a long burrow in the sand', 'k': 'a'}, {'t': 'Shelter from heat and predators', 'k': 'n'}, {'t': 'Gopher tortoise', 'k': 'x'}, {'t': 'It moves slowly', 'k': 'x'}],
             'why': 'Shovel legs → dig a burrow → shelter. Hundreds of other Florida animals use those burrows too.'},
            {'id': 'anhinga', 'name': 'Anhinga', 'icon': '🐦', 'cards': [{'t': 'Long, pointed beak on an S-shaped neck', 'k': 's'}, {'t': 'Spears fish underwater', 'k': 'a'}, {'t': 'Food', 'k': 'n'}, {'t': 'Anhinga', 'k': 'x'}, {'t': 'It lives in Florida', 'k': 'x'}],
             'why': 'Pointed beak → spears fish → food. The anhinga model in Part 2 shows the same chain.'},
            {'id': 'pine', 'name': 'Longleaf pine', 'icon': '🌲', 'cards': [{'t': 'Thick, layered bark', 'k': 's'}, {'t': 'Keeps the heat of a fire away from the living wood', 'k': 'a'}, {'t': 'Safety from wildfire', 'k': 'n'}, {'t': 'Longleaf pine', 'k': 'x'}, {'t': 'It grows very tall', 'k': 'x'}],
             'why': 'Thick bark → blocks heat → safety from fire. Plants have structures that help them survive, too.'}],
        'win': 'Four chains built! Every strong model follows this chain. That’s a clue.',
        'clue': 'chain'},
    'kit': {
        'afterText': "Now it's your turn. Pick a Florida organism", 'kicker': 'Part 4 game', 'title': 'Model kit',
        'todo': ['Pick an organism, then tap a + on the photo.', 'Point the arrow, pick what the part does, then pick the survival need.', 'Read your caption. Then build one more.'],
        'why': {'icon': '🧩', 'q': 'Why a real photo?', 't': 'Scientists often draw arrows right on photos. The photo shows what the part looks like; the arrows and caption explain what it does.'},
        'qs': {'target': '1. Where does the arrow point?', 'action': '2. What does this part do?', 'need': '3. Which survival need does it meet?'},
        'capTpl': 'Caption: The {part} {action}, so the {org} meets its survival need for {need}.',
        'tmiss': 'Think about what this part touches, pushes or hides from.',
        'start': 'Tap a + on the photo to pick the part your model will explain.',
        'doneLine': 'That’s a real model! Tap another + or pick another organism to build one more.',
        'orgs': [
            {'id': 'frog', 'name': 'Green tree frog', 'icon': '🐸', 'img': 'images/11-02-kit-frog.jpg', 'alt': 'A bright green tree frog sitting on a big green leaf.',
             'credit': 'American green tree frog, Greg Schechter, via Wikimedia Commons (CC BY 2.0)',
             'targets': [{'k': 'leaf', 't': 'the green leaf', 'x': 72, 'y': 88}, {'k': 'sky', 't': 'the night sky', 'x': 84, 'y': 10}, {'k': 'snake', 't': 'a hungry snake', 'x': 14, 'y': 12}],
             'parts': [
                 {'k': 'skin', 'label': 'Green skin', 'x': 50, 'y': 42, 'target': 'leaf', 'tmiss': {'sky': 'Does green skin do anything to the sky? Look at what is the same color.', 'snake': 'Close! The skin helps it hide FROM the snake. But what does the skin match?'},
                  'actions': [{'t': 'blends in with the leaf', 'ok': True}, {'t': 'is bright and shiny', 'miss': 'That describes it. What does the color DO next to the leaf?'}, {'t': 'jumps on the leaf', 'miss': 'Skin doesn’t jump. What does green skin do on a green leaf?'}],
                  'needs': needs('safety', 'water', 'food')},
                 {'k': 'toes', 'label': 'Sticky toe pads', 'x': 31, 'y': 72, 'target': 'leaf',
                  'actions': [{'t': 'grip the smooth leaf', 'ok': True}, {'t': 'catch insects', 'miss': 'The frog catches insects with its tongue. What do the toe pads do?'}, {'t': 'dig in the mud', 'miss': 'Tree frogs climb. What do sticky toes do on a leaf?'}],
                  'needs': needs('safety', 'air', 'water')}]},
            {'id': 'tortoise', 'name': 'Gopher tortoise', 'icon': '🐢', 'img': 'images/11-02-kit-tortoise.jpg', 'alt': 'A gopher tortoise at the sandy entrance of its burrow, with its front legs on the sand.',
             'credit': 'Gopher tortoise at its burrow, Andrea Westmoreland, via Wikimedia Commons (CC BY-SA 2.0)',
             'targets': [{'k': 'sand', 't': 'the sand of its burrow', 'x': 64, 'y': 38}, {'k': 'bite', 't': 'a predator’s bite', 'x': 14, 'y': 14}, {'k': 'tree', 't': 'a tall tree', 'x': 86, 'y': 12}],
             'parts': [
                 {'k': 'legs', 'label': 'Shovel front legs', 'x': 25, 'y': 62, 'target': 'sand',
                  'actions': [{'t': 'dig into the sand', 'ok': True}, {'t': 'climb up trees', 'miss': 'Gopher tortoises don’t climb. Look at the hole behind it.'}, {'t': 'swim fast', 'miss': 'Gopher tortoises live on dry, sandy land. What do the legs do to the sand?'}],
                  'needs': needs('shelter', 'food', 'air')},
                 {'k': 'shell', 'label': 'Hard shell', 'x': 42, 'y': 42, 'target': 'bite',
                  'actions': [{'t': 'blocks bites and claws', 'ok': True}, {'t': 'keeps it warm', 'miss': 'Think about danger. What does a hard shell stop?'}, {'t': 'helps it dig', 'miss': 'That’s the legs’ job. What does the hard shell stop?'}],
                  'needs': needs('safety', 'food', 'water')}]},
            {'id': 'anhinga', 'name': 'Anhinga', 'icon': '🐦', 'img': 'images/11-02-kit-anhinga.jpg', 'alt': 'An anhinga swimming with its body under the water and only its long neck and pointed beak showing.',
             'credit': 'Anhinga swimming, Wknight94, via Wikimedia Commons (CC BY-SA 3.0)',
             'targets': [{'k': 'fish', 't': 'a fish under the water', 'x': 18, 'y': 84}, {'k': 'water', 't': 'the water', 'x': 78, 'y': 92}, {'k': 'sky', 't': 'the sky', 'x': 80, 'y': 10}],
             'parts': [
                 {'k': 'beak', 'label': 'Pointed beak', 'x': 26, 'y': 19, 'target': 'fish',
                  'actions': [{'t': 'spears the fish', 'ok': True}, {'t': 'sips nectar', 'miss': 'That’s a hummingbird’s job. What does a sharp, pointed beak do to a fish?'}, {'t': 'cracks seeds', 'miss': 'That’s a cardinal’s job. What does a spear-shaped beak do?'}],
                  'needs': needs('food', 'shelter', 'air')},
                 {'k': 'feathers', 'label': 'Feathers that soak up water', 'x': 40, 'y': 52, 'target': 'water',
                  'actions': [{'t': 'let it sink low and swim underwater', 'ok': True}, {'t': 'keep it dry', 'miss': 'Anhinga feathers soak up water. Look how low it sits.'}, {'t': 'help it fly faster', 'miss': 'Wet feathers are heavy. What do they help it do in the water?'}],
                  'needs': needs('food', 'water', 'shelter')}]},
            {'id': 'manatee', 'name': 'Florida manatee', 'capName': 'Florida manatee', 'icon': '🌊', 'img': 'images/11-02-kit-manatee.jpg', 'alt': 'A gray Florida manatee swimming in a clear blue spring, with its wide, flat tail behind it.',
             'credit': 'Florida manatee, Keith Ramos, U.S. Fish and Wildlife Service, via Wikimedia Commons (public domain)',
             'targets': [{'k': 'water', 't': 'the water', 'x': 88, 'y': 80}, {'k': 'air', 't': 'the air above the water', 'x': 22, 'y': 8}, {'k': 'rock', 't': 'a rock', 'x': 86, 'y': 92}],
             'parts': [
                 {'k': 'tail', 'label': 'Wide, flat tail', 'x': 74, 'y': 42, 'target': 'water',
                  'actions': [{'t': 'pushes the water to swim', 'ok': True}, {'t': 'grabs seagrass', 'miss': 'Manatees eat with their lips. What does a big flat tail push?'}, {'t': 'keeps it warm', 'miss': 'Think about moving. What does the tail push on?'}],
                  'needs': [{'t': 'food', 'ok': True}, {'t': 'air', 'miss': 'Look at the arrow: the tail moves it through the water, to its food.'}, {'t': 'shelter', 'miss': 'Look at the arrow: the tail moves it through the water, to its food.'}]},
                 {'k': 'nose', 'label': 'Nostrils on top of its snout', 'x': 28, 'y': 47, 'target': 'air',
                  'actions': [{'t': 'breathe at the surface', 'ok': True}, {'t': 'smell the water', 'miss': 'Manatees close their nostrils underwater. What do they do at the top?'}, {'t': 'push water', 'miss': 'That’s the tail. What do nostrils do at the surface?'}],
                  'needs': needs('air', 'food', 'shelter')}]}],
        'win': 'You built a real model! That’s your last clue.',
        'clue': 'kit'},
    'exploreMod': 'kit',
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Colors don’t explain anything. What shows how the parts work?', 'B': 'Size doesn’t make a model stronger. What do arrows and captions add?'},
        'q2': {'A': 'A survival need is something it must have, like food. Is green skin a need, or something that helps it?', 'C': 'Skin color is on the outside of the frog, not inside.'},
        'q3': {'B': 'Computer models count. But are they the only kind?', 'C': 'A fancy drawing isn’t needed. What makes any model count?'}},
    'flags': {
        'ans-2': [
            {'label': 'what a label does', 're': 'name|label|just says|tells what|says what'},
            {'label': 'what a model does', 're': 'explain|show|how|work|why|arrow|action|does|job'},
            {'label': 'the word annotate', 're': 'annotat'}],
        'ans-3': [
            {'label': 'the word function', 're': 'function'},
            {'label': 'why 3-D', 're': '3.?d|three.?d|solid|build|clay|shape|move|bend|turn|around|all sides|real'},
            {'label': 'what the fluke does', 're': 'swim|push|water|move|steer|tail|fluke|paddle'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|wrong|right|not true|true|is science|are science|count'},
            {'label': 'two pieces of evidence', 'any': ['arrow', 'label', 'caption', 'model', 'explain', 'anhinga', 'beak', 'scientist', 'drawing', '3.?d|three', 'computer', 'notebook'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|without|help'}]},
    'minWords': {'ans-2': 18, 'ans-3': 18, 'cer-4': 30},
    'hints': {
        'ans-2': ['Think about Drawing 1 and Drawing 2 in the Warm-Up.', 'A label names a part. What does a model add? Annotate means to add labels, arrows and short notes.', 'Try: A labeled drawing only ___. A model ___. When you annotate, you ___.'],
        'ans-3': ['A fluke is a manatee’s wide, flat tail. It pushes the water so the manatee can swim.', 'A flat drawing can’t bend or move. What could you see if you could turn a 3-D model in your hands?', 'Try: A 3-D model shows how the fluke ___. Its function is to ___.'],
        'cer-4': ['First decide: do you agree or disagree with the classmate?', 'Look for two facts from today about what models do or who uses them.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'A model uses labels and arrows to explain how a part works.',
                'The anhinga model shows how its beak, body and feathers help it catch fish.',
                'Scientists use many kinds of models: drawings, 3-D builds and computer models.',
                'A model explains how a part helps, not just its name.',
                'A pretty picture with no labels or arrows doesn’t explain anything.',
                'Dr. Reyes fills her field notebook with drawings that have arrows and notes.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · the refuge sign', 'length': '30–40 s',
                    'script': 'Good news from the refuge! They read our case report about the spoonbill, and now they want a sign for the boardwalk where I found that soggy notebook. Three people sent drafts. One is a photo with labels. One is a beautiful old painting. One is a photo with arrows. Only one can go on the sign. Help me decide which one really explains how the spoonbill survives.'},
        'warmup': {'label': 'Warm-Up · point the arrow (Clue 1)', 'length': '20–30 s',
                   'script': 'Here’s a trick I use in my field notebook. When I draw an animal, I don’t just write names next to the parts. I draw an arrow from the part to whatever it acts on. One arrow can turn a drawing into an explanation. Try it with this alligator’s teeth.'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Say each word; for annotate, add an arrow and a note to a quick sketch on a whiteboard.'},
        'lesson': {'label': 'The Lesson', 'length': '30–45 s'},
        'part1': {'label': 'Part 1 · a model explains', 'length': '20–30 s'},
        'part2': {'label': 'Part 2 · upgrade the drawing (Clue 2)', 'length': '20–30 s',
                  'script': 'Let’s upgrade a drawing, one step at a time. First a label, then an arrow, then a caption. Watch the meter at the top. It shows how close your drawing is to being a real model.'},
        'part3': {'label': 'Part 3 · chain it (Clue 3)', 'length': '20–30 s',
                  'script': 'Every model I make follows the same chain. First the part. Then what the part does. Then which survival need it meets. Build a chain for four Florida organisms. Watch out: two cards in each set don’t belong in the chain.'},
        'explore': {'label': 'Part 4 · the model kit (Clue 4)', 'length': '25–35 s',
                    'script': 'Now it’s your turn to be the scientist. Pick an organism, tap a part on the real photo, and point its arrow. Then choose what the part does and which need it meets. When you finish, you’ll have a real model, just like the ones in my notebook.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s',
                       'script': 'You’ve got all four clues. Crack the case at the top of this tab: which draft should go on the refuge sign? Then build your own model in Part C. Your answers save as you type.'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · build an annotated model', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'Someone once told me that drawings aren’t real science. I laughed, because my notebook is full of them! What do you think? Pick your side, choose two pieces of evidence in the planner, then explain how they prove your claim.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease week 12 (senses, brain and the four trail cameras).',
                    'script': 'Case closed for good! Draft C goes on the sign, and visitors will learn how the spoonbill finds its food. Next week, we’ll find out what happens inside an animal when it notices something: its senses, its brain, and what it does next.'},
    },
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Drawing 2 with its arrow (Warm-Up)',
        'The meter when your drawing becomes a model (The Lesson)',
        'A model you built in the model kit (The Lesson)',
        'The answer that cracked the case (Assignment)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['My annotated model', 'A Florida organism with one arrow', 'The refuge sign, my way'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 1,
                           'prompts': ['My organism with a label', 'An arrow that shows what the part does', 'A caption about a survival need']}]},
    'hlCoach': copy.deepcopy(P['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '📝', 'name': 'Annotated spoonbill sketch',
                 'line': 'You cracked Case 11, part 2, and Draft C’s annotated sketch goes in your Field Notebook. (A specimen is something a scientist collects to study.) Next week: four trail cameras, four Florida animals, and a mystery about senses.'},
    'notebookTitle': P['notebookTitle'],
    'notebook': [dict(x) for x in P['notebook']],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You’ll use every one of them today.',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'write', 'inside': True, 'find': {'sel': '.act-warmup .socratic-q', 'text': 'Notice'},
         'label': 'Warm-Up: which drawing tells more?', 'q': 'Warm-Up: Which drawing tells a friend more about how the alligator survives? Why?', 'ph': 'Drawing ___ tells more, because…', 'rows': 3},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'hide-tip', 'type': 'hide', 'find': {'sel': '.act-warmup .callout', 'text': 'A label says'}},
        {'id': 'hide-st', 'type': 'hide', 'find': {'sel': '.socratic-q', 'text': 'drawing of a turtle'}},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Pick one Florida organism and one of its structures'},
         'label': 'Part C: My annotated model', 'q': 'Part C: A model in words: a Florida organism, one structure, what it does, and a caption about a survival need',
         'title': 'My annotated model',
         'fields': [{'t': 'My Florida organism', 'icon': '🐾', 'ph': 'For example: a pelican, a cabbage palm, a bobcat…'},
                    {'t': 'Label: the structure', 'icon': '🏷️', 'ph': 'Which part will your model explain?'},
                    {'t': 'Arrow: what it does', 'icon': '➜', 'ph': 'The arrow points to… The part…', 'long': True},
                    {'t': 'Caption', 'icon': '💬', 'ph': 'This ___ helps the ___ meet its survival need for ___ by ___.', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Do you agree or disagree with the classmate?', 'ph': 'I disagree. Drawings can be science because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-2': 'Part B · Question 5', 'ans-3': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] == '11.01': n['have'] = True
    if n['lesson'] == '11.02': n.update({'icon': '📝', 'name': 'Annotated spoonbill sketch'})
D['hlCoach']['tips'][2][2] = 'Ask yourself: does this help me explain how a model shows what a part does?'
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'A model uses arrows and a caption to explain what a part does.',
    'key': ['model', 'arrows', 'caption', 'explain', 'part', 'does'],
    'small': ['A', 'and', 'a', 'to', 'what'],
    'model': 'A scientist might highlight “model”, “arrows”, “caption” and “explain”. Those words carry the idea. Small words like “a” and “to” don’t.'}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
