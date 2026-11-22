#!/usr/bin/env python3
"""Writes data.json and fixes.json for 24.02 (run from this folder). Case 24 part 2 "Teo's Napkin Plan" (Sam Park, Palmetto Beach, the
December lighted boat parade): the boardwalk outlets are all taken by the parade stage, so Rosa's cousin Teo sketches a pedal bike that will
run her string lights, menu sign and cocoa warmer. "FREE energy, no plug!" Rosa: "Free? Prove it."
New: case.napkin (a napkin sketch + Rosa's sticky reply), glowstick (Warm-Up: bend, crack, shake, observe), reels (Part 1: the energy slot
machine; replaces the "card sort" AI picture and the tap diagram), bingo (Part 2: evidence bingo during a live parade scene), binder (Part 3 =
the old Explore: trading-card binder = the data table), pedal (the wow after the binder: one rider vs the cocoa warmer), glowwake (bonus after
the case, folded: comb jellies flash in a boat's wake). No Tool of the Week (24.01 has the infrared thermometer)."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../18-01/data.json', encoding='utf-8'))
O = json.load(open('../24-01/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
PS = '<p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)
def I(n): return 'images/24-02-' + n + '.jpg'

# ---------------------------------------------------------------- labels (standing approval)
fx('fix', 'unit label: “Ecosystems & Energy” is a leftover; weeks 18–24 are Unit 5', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Energy, Motion &amp; Collisions</div>')
fx('fix', 'energy changes are physical science, not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standards label: the plan’s CPALMS codes; TEKS 4.2(A) is a Texas code that isn’t in the plan', '<div class="info-value">SC.4.P.10.1, SC.4.P.10.2 · TEKS 4.2(A)</div>', '<div class="info-value">SC.4.P.10.1, SC.4.P.10.2</div>')

# ---------------------------------------------------------------- ticked fixes (Bethany, 21 Nov 2026)
# 22.01 leftovers in the Warm-Up
fx('fix', '22.01 leftover: the Warm-Up title and subtitle named the toaster lesson', '<div class="act-title">🌅 Warm-Up: What Goes In, What Comes Out?</div>\n        <div class="act-subtitle">A familiar device, a hidden change</div>',
   '<div class="act-title">🌅 Warm-Up: Crack a Glow Stick</div>\n        <div class="act-subtitle">Where does the light come from?</div>')
fx('fix', '22.01 leftover: the toaster warm-up → the glow stick',
   '<p>Think about a toaster. You drop in cold bread. A minute later, you pull out hot toast.</p>',
   '<p>Kids at the boat parade wave glow sticks. A glow stick has no plug and no battery. So where does its light come from? Crack one and look for clues.</p>')
fx('fix', '22.01 leftover: the toaster sketch → a list on the page',
   "<p>In your notebook, draw a quick sketch of a toaster. On one side, label what goes IN. On the other, label what comes OUT. (Hint: bread on both sides — but something invisible is also going in. What is it?)</p>",
   '<p>Now look around your home. What glows, buzzes, spins or warms up?</p>')
fx('fix', '22.01 leftover: Notice & Wonder about the toaster',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Notice &amp; Wonder</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover: “energy can CONVERT … toasters” callout',
   r'<div class="callout callout-tip">\s*<span class="callout-icon">💡</span>\s*<p>Today you\'ll learn that energy can CONVERT.*?</p>\s*</div>\s*', '', True)
# 9.01 leftovers
fx('fix', '9.01 leftover: Part C was a food chain; the checklist already asks for 4 energy change cards from home', '🎨 Part C &mdash; Build Your Own Food Chain', '🎨 Part C &mdash; My 4 Energy Change Cards')
fx('fix', '9.01 leftover: Part C task (now 4 cards typed on the page + a required labeled sketch)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Find 4 devices or systems at home that are NOT in today’s lesson. For each one, write its starting energy, its resulting energy and one piece of evidence. Then sketch and label one.</p>', True)
fx('fix', '9.01 leftover: Reflect asked about a hawk; the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'supply list: something to try it for real', r'<span class="need-chip"><span>✏️</span>Colored pencils</span>', '<span class="need-chip"><span>🪄</span>A glow stick, if you have one (to try it for real)</span>', True)
# wrong facts
fx('fix', 'wrong fact: a windmill (like the one in 23.02) pumps water; a wind TURBINE turns motion into electrical energy. No dashes.',
   'Almost everything around you has a starting and resulting energy. A toaster takes electrical → heat. A windmill takes motion → electrical.',
   'Almost everything around you has a starting and resulting energy. A toaster takes electrical → heat. A wind turbine takes motion → electrical.')
fx('fix', 'kept (Bethany ticked it): the Florida connection is true, as one line in Part 1',
   'Once you spot the pattern, you start seeing it everywhere.</p>',
   'Once you spot the pattern, you start seeing it everywhere.</p>\n      <p><strong>In Florida:</strong> sunshine starts lots of energy changes. Solar panels turn light into electrical energy, leaves turn it into food (chemical energy), and dark roads turn it into heat you can feel through your shoes.</p>')
fx('fix', 'wrong teaser: next week (25.01) is about how objects move, not food chains',
   'Next module, you\'ll look at how plants and animals interact in Florida ecosystems — and how energy moves between them in food chains.</p>',
   'Next week, you’ll describe how objects move: where they start, where they end up and which way they go.</p>')

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; plain words', r"<p>Hold this question in your head as you work\. By the end of the lesson.*?</p>",
   "<p>Keep this question in mind. By the end, you’ll name where the energy starts and what it becomes, and prove it with evidence.</p>", True)
fx('plain', 'cut filler', r"<p>These six words show up all through the lesson\. <strong>Tap a card to flip it</strong>.*?</p>",
   "<p><strong>Tap a card to flip it</strong> and read what the word means.</p>", True)
fx('plain', 'no dash (Part 2)', "It doesn't — it changes FORM.", "It doesn't. It changes FORM.")
fx('plain', 'Part B question 5 named the removed diagram; the same four cards are in the slot machine (same question, same answer)',
   'Pick ONE card from the diagram (lamp, pedaling a bike, speaker, or solar panel).', 'Pick ONE card from the slot machine (lamp, pedaling a bike, speaker or solar panel).')
fx('plain', 'Part B question 5 label (Gathered Answers)', 'data-label="Pick ONE card from the diagram (lamp, pedaling a b..."', 'data-label="One card from the slot machine"')
fx('plain', 'Part B question 7 label (Gathered Answers)', 'data-label="Why is EVIDENCE important when describing an energ..."', 'data-label="Why evidence matters"')
fx('plain', 'plain words: “misconception” is a hard word; same idea', '<p><strong>Common misconception:</strong> Some people think', '<p><strong>Watch out:</strong> some people think')
fx('plain', 'plain words: “circuit” is not taught until later; same meaning', 'when I push the button (closing the battery circuit), light comes out the front.', 'when I push the button, the battery’s electricity flows and light comes out the front.')
fx('plain', 'no dash in the classmate’s claim (same claim)', 'when you click the button — there\'s no starting energy.', 'when you click the button. There\'s no starting energy.')
fx('plain', 'no dash in the Lesson subtitle', '<div class="act-subtitle">Every system tells a story — find the proof</div>', '<div class="act-subtitle">Every system tells a story. Find the proof.</div>')
fx('plain', 'plain words: “converted” → “changes”', 'it just gets converted into the resulting energy.', 'it just changes into the resulting energy.')
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: Stop & Think (the slot machine is Part 1’s thinking stop)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'removed: the AI card-sort picture (its “windmill: motion → electrical” card shows a water-pumping farm windmill; the slot machine replaces it), Key Concept, the Stop & Reason about “the three devices above” (a 22.01 leftover), the Four Energy Change Cards tap diagram (its four cards live in the slot machine), Observe & Reason, the leaf “Amazing Florida Fact” (the leaf is now a binder card), the Florida callout (kept as a line in Part 1) and Go Deeper. Part 3 = the old Explore (Sort the Cards); the next button goes to Self-Check',
   r'\s*<div class="lesson-figure scroll-reveal">.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   '\n\n      ' + H3 + 'Part 3 · Sort the Cards</h3>\n      ' + PS + 'Here are five everyday systems. For each one, find the starting energy, the resulting energy and one piece of evidence. Every card you finish goes into your binder.</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its five systems are now the binder in Part 3; its notebook table, solar-toy “Amazing Florida Fact”, Think like a scientist and Go Deeper go with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 6 removed (Bethany kept 5 and 7; Q6 overlaps Part C’s home cards)', r'<div class="pq">\s*<span class="pq-num"[^>]*>6</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 7 answered')
fx('cut', 'lean: Part C typed on the page, plus the required sketch', 'Four hand-drawn energy change cards from systems in your home, each with system / starting → resulting / evidence.',
   'My 4 energy change cards from home, each with its starting → resulting energy and one piece of evidence. Plus your labeled sketch.')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether energy "appears" or whether there\'s always a starting energy, supported with two pieces of evidence.',
   '<strong>Use Your Evidence:</strong> My claim about whether energy just appears in a flashlight, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a 9.01 leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Download your field journal (it has your answers and your sketch) and upload it to the Canvas assignment. Or copy your Gathered Answers (above) into Canvas.', True)

# ---------------------------------------------------------------- the napkin sketch (hand-drawn look)
INK = 'stroke="#2D5BA6" stroke-width="3" fill="none" stroke-linecap="round" stroke-linejoin="round"'
NAPKIN = ('<svg viewBox="0 0 560 210" role="img" aria-label="Teo’s pen sketch: a bike on a stand turns a small generator; a wire runs to string lights, a menu sign and a cocoa warmer, with the words FREE energy!">'
  '<g ' + INK + '>'
  '<circle cx="62" cy="150" r="34"/><circle cx="158" cy="150" r="34"/><path d="M62 150 L104 104 L158 150 M104 104 L94 82 M80 80 h28 M104 104 L148 92 M148 92 l8 -14"/>'
  '<path d="M44 186 L80 186 M140 186 L176 186 M62 184 v-34 M158 184 v-34" stroke-dasharray="2 6"/>'
  '<rect x="186" y="132" width="34" height="30" rx="5"/><path d="M196 147 l6 -8 l4 12 l6 -8"/>'
  '<path d="M220 146 C 260 146, 262 60, 300 60 L540 60"/>'
  '<path d="M300 60 q20 16 40 0 q20 16 40 0 q20 16 40 0 q20 16 40 0 q20 16 40 0 q20 16 40 0"/>'
  + ''.join('<circle cx="%d" cy="70" r="6"/>' % x for x in (320, 360, 400, 440, 480, 520)) +
  '<path d="M330 60 v56 M436 60 v50 M500 60 v60"/>'
  '<rect x="300" y="116" width="62" height="34" rx="4"/><path d="M310 128 h40 M310 138 h28"/>'
  '<rect x="410" y="110" width="52" height="40" rx="6"/><path d="M420 104 q-4 -8 0 -14 M436 104 q-4 -8 0 -14"/>'
  '<path d="M488 120 h30 l-4 34 h-22z"/><path d="M518 128 q12 0 12 10 t-12 10"/>'
  '</g>'
  '<g font-family="Comic Sans MS, Chalkboard SE, Nunito, sans-serif" fill="#2D5BA6" font-size="15" font-weight="700">'
  '<text x="70" y="30">PEDAL HERE!</text><path d="M110 36 l-4 40" stroke="#2D5BA6" stroke-width="2" fill="none"/>'
  '<text x="176" y="124">GEN</text>'
  '<text x="372" y="34">string lights</text>'
  '<text x="300" y="172">menu sign</text><text x="406" y="172">cocoa</text><text x="406" y="188">warmer</text><text x="486" y="178">mug</text>'
  '<text x="232" y="206" font-size="20" fill="#C8553D">FREE energy! No plug!</text>'
  '</g></svg>')

# ---------------------------------------------------------------- the story
SAM = Q['crew']['sam']
EN = [{'id': 'electrical', 'icon': '⚡', 't': 'Electrical'}, {'id': 'chemical', 'icon': '🍎', 't': 'Chemical (food or fuel)'},
      {'id': 'light', 'icon': '💡', 't': 'Light'}, {'id': 'motion', 'icon': '🌀', 't': 'Motion'},
      {'id': 'sound', 'icon': '🔊', 't': 'Sound'}, {'id': 'heat', 'icon': '🔥', 't': 'Heat'}]
D = {
    'lesson': '24.02', 'week': 24, 'day': 2, 'guide': 'sam', 'prefix': 'g4sci-24-2', 'manifestKey': '24-02',
    'paths': P['paths'], 'crew': {'sam': SAM},
    'expedition': {'num': 24, 'title': 'Teo’s Napkin Plan'},
    'ambient': {'icon': '🎆', 'label': 'Parade night'},
    'case': {
        'num': 24, 'title': 'Teo’s Napkin Plan', 'style': 'napkin',
        'hook': 'The boat parade is tonight, and Rosa’s cocoa cart is back on the boardwalk. But this year every outlet is taken by the parade stage. Rosa’s cousin Teo sketched a plan on a napkin: a bike on a stand that will run everything. Rosa wants proof.',
        'napkin': {'head': 'Teo’s plan for the cart', 'svg': NAPKIN,
                   'notes': ['Someone pedals the bike.', 'The bike spins a little generator (GEN).', 'It runs the lights, the menu sign AND the cocoa warmer.', 'FREE energy! It comes from nowhere!'],
                   'sign': 'Teo',
                   'reply': {'t': 'Free? Energy doesn’t come from nowhere. Where does it START, and how do we PROVE it?', 'sign': 'Rosa'}},
        'stills': [{'cam': 'REAL PHOTO', 'time': 'A real bike generator', 'tag': '📷 PHOTO', 'img': I('bike-generator'), 'kind': 'print',
                    'alt': 'A woman pedals a bike that stands on a trainer. It powers the speakers for a music stage on a town square.'}],
        'stillsCredit': 'Bike-powered music stage (Cycloton), Fête de la Musique, Geneva: MHM55, CC BY-SA 4.0, via Wikimedia Commons.',
        'question': 'Where does the energy for Teo’s pedal-powered cart really start, and what evidence proves it?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'glowstick', 'icon': '🪄', 'where': 'Warm-Up: crack a glow stick', 't': 'A glow stick has no plug and no battery. Its light started as chemical energy stored inside. Energy doesn’t come from nowhere.'},
            {'id': 'reels', 'icon': '🎰', 'where': 'The Lesson, Part 1: the energy slot machine', 't': 'Every device has a starting and a resulting energy. A bike generator turns motion into electrical energy. A lamp turns electrical energy into light.'},
            {'id': 'bingo', 'icon': '🔲', 'where': 'The Lesson, Part 2: evidence bingo', 't': 'Evidence is something you can see, hear, feel or measure. “Teo says it works” is not evidence.'},
            {'id': 'binder', 'icon': '🃏', 'where': 'The Lesson, Part 3: the card binder', 't': 'When you walk, chemical energy from your food becomes motion. Your body is an energy changer, too.'},
        ],
        'solve': {
            'title': 'Where does Teo’s “free” energy come from?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'It comes from nowhere. The generator makes new energy all by itself.', 'why': 'Check Clue 1. Energy doesn’t come from nowhere. Even a glow stick has a starting energy.'},
                {'t': 'It starts as chemical energy in the rider’s food. Pedaling turns it into motion, the generator turns motion into electrical energy, and the lights turn that into light. The proof: the lights glow only while someone pedals.', 'right': True,
                 'why': 'Case cracked! Food → motion → electrical → light, and you can SEE the proof: stop pedaling and the lights go dark.'},
                {'t': 'The string lights make their own light. The bike just keeps them company.', 'why': 'Check Clue 2. A lamp needs a starting energy: electrical. Where does that come from here?'},
                {'t': 'Teo says it works, so that’s the proof.', 'why': 'Check Clue 3. Saying so is not evidence. Evidence is something you can see, hear, feel or measure.'},
            ]},
    },
    'glowstick': {
        'afterText': 'Crack one and look for clues.', 'kicker': 'Warm-Up game', 'title': 'Crack a glow stick',
        'todo': ['Bend it until it cracks: press Bend, or drag the ✋ up.', 'Shake it to mix.', 'Tap the two things you really observe.'],
        'why': {'icon': '🧪', 'q': 'What is inside a glow stick?', 't': 'Two liquids. One is sealed in a thin glass tube that floats inside the plastic tube. When the glass cracks, the liquids mix.'},
        'model': 'a model', 'bendBtn': '↷ Bend it', 'shakeBtn': '〰 Shake it', 'dragHint': 'Or drag the ✋ up to bend it.',
        'crackLine': 'CRACK! The glass tube inside broke. Now the two liquids can mix.', 'shakeMore': 'Keep shaking to mix: {n} more.', 'shakeLine': 'It glows!',
        'needBend': 'Bend it first, so the glass inside cracks.',
        'obsQ': 'What do you observe? Tap the TWO that really happen.', 'needObs': 2, 'obsWord': 'real observations found',
        'obs': [{'icon': '👀', 't': 'I see a glow.', 'ok': True},
                {'icon': '🌈', 't': 'I see a bright green color.', 'ok': True},
                {'icon': '🔥', 't': 'I feel it get hot.', 'miss': 'Touch a real one: it stays about as cool as the room. A glow stick makes light, not much heat.'},
                {'icon': '🔊', 't': 'I hear it hum.', 'miss': 'Listen: after the crack, it makes no sound at all.'}],
        'photo': {'img': I('glow-sticks'), 'alt': 'Two real glow sticks, one green and one blue, glowing in the dark.', 'cap': 'Real glow sticks glowing in the dark. Photo: David Muelheims, public domain, via Wikimedia Commons.'},
        'q': 'No plug and no battery. Where did the light’s starting energy come from?',
        'opts': [{'t': 'Chemical energy stored in the two liquids.', 'ok': True},
                 {'t': 'Nowhere. The light just appeared when I bent it.', 'miss': 'Bending only broke the glass so the liquids could mix. Did the light start before or after they mixed?'},
                 {'t': 'Heat from my hands.', 'miss': 'Did it feel hot? A glow stick glows even sitting on a table.'}],
        'win': 'The glow stick’s light started as chemical energy. Nothing came from nowhere. Clue 1!'},
    'reels': {
        'afterText': 'dark roads turn it into heat you can feel', 'kicker': 'Part 1 game', 'title': 'The energy slot machine',
        'todo': ['Pull the lever to get a device.', 'Stop the STARTING reel and the RESULTING reel on the right energy (or use ▲ ▼).', 'Press Check. A true line wins a card. Win all 5.'],
        'why': {'icon': '🎰', 'q': 'How does this machine work?', 't': 'The first reel shows a device. You line up the energy it starts with and the energy it ends with. Only true lines pay out.'},
        'machineName': 'ENERGY SLOTS', 'energies': EN, 'reelLabels': ['Device', 'Starting energy', 'Resulting energy'], 'stopBtn': 'STOP', 'leverBtn': 'Pull!',
        'checkBtn': '🎰 Check my line', 'spinMs': 750, 'startLine': 'Pull the lever',
        'needLever': 'Pull the lever first to get a device.', 'needStop': 'Stop both spinning reels first.',
        'winLine': 'A true line!', 'allLine': 'All 5 paid out!', 'cardsLabel': 'My winning cards', 'countWord': 'true lines',
        'devices': [
            {'id': 'lamp', 'icon': '💡', 't': 'Lamp', 's': 'electrical', 'r': 'light', 'why': 'Flip the switch and the bulb glows.',
             'missS': 'Where does a lamp get its energy? Follow the cord to the wall.', 'missR': 'What is a lamp’s job?',
             'also': {'heat': 'True, a lamp gets a little warm. But what is its main job? Stop the reel on that.'}},
            {'id': 'bike', 'icon': '🚴', 't': 'Pedaling a bike', 's': 'chemical', 'r': 'motion', 'why': 'Your food powers your legs, and the wheels spin.',
             'missS': 'What gives YOUR legs energy? Think about breakfast.', 'missR': 'What do the pedals and wheels do?'},
            {'id': 'speaker', 'icon': '📢', 't': 'Speaker', 's': 'electrical', 'r': 'sound', 'why': 'Plug it in and you hear music.',
             'missS': 'A speaker needs a cord or a battery. What kind of energy comes through it?', 'missR': 'What do you notice with your ears?'},
            {'id': 'solar', 'icon': '☀️', 't': 'Solar panel', 's': 'light', 'r': 'electrical', 'why': 'Sunlight in, electricity out.',
             'missS': 'What hits a solar panel on a sunny day?', 'missR': 'A solar panel can charge a battery. What kind of energy is that?'},
            {'id': 'gen', 'icon': '⚙️', 't': 'Bike generator', 's': 'motion', 'r': 'electrical', 'why': 'Spin it, and it sends electricity down the wire.',
             'missS': 'A generator only works when something spins it. What kind of energy is spinning?', 'missR': 'Teo’s generator sends energy down a wire to the lights. What kind?'}],
        'q': 'What does every winning line have?',
        'opts': [{'t': 'A starting energy that changes into a different resulting energy.', 'ok': True},
                 {'t': 'The same energy at both ends.', 'miss': 'Look at your cards. Was any starting energy the same as its result?'},
                 {'t': 'Energy that appears out of nowhere.', 'miss': 'Every card had a starting energy. Look again.'}],
        'win': 'Every device starts with one energy and changes it into another. Clue 2!'},
    'bingo': {
        'afterText': 'light comes out the front', 'kicker': 'Part 2 game', 'title': 'Evidence bingo',
        'todo': ['Press Play and watch Rosa’s cart.', 'The moment you see, hear, feel or measure something on your card, tap that square.', 'Get three in a row. One square never counts.'],
        'why': {'icon': '🔲', 'q': 'How do I play?', 't': 'Each square is a piece of evidence. Tap it only WHILE it is happening in the scene. The scene loops, so you get more chances.'},
        'model': 'a model', 'loopSec': 42, 'meterW': 40, 'cardTitle': 'EVIDENCE BINGO', 'freeWord': 'FREE',
        'teoSays': 'Trust me, it runs EVERYTHING!',
        'events': [
            {'id': 'lights', 'at': 2, 'dur': 6, 'fx': 'lights', 'icon': '💡', 'sense': 'I SAW', 't': 'The string lights glow'},
            {'id': 'horn', 'at': 7.5, 'dur': 5, 'fx': 'horn', 'icon': '🛥️', 'sense': 'I HEARD', 't': 'A boat horn honks'},
            {'id': 'wheel', 'at': 12, 'dur': 6, 'fx': 'wheel', 'icon': '🚴', 'sense': 'I SAW', 't': 'The bike wheel spins'},
            {'id': 'meter', 'at': 17, 'dur': 6, 'fx': 'meter', 'icon': '📟', 'sense': 'I MEASURED', 't': 'The meter reads 40 watts'},
            {'id': 'music', 'at': 22, 'dur': 6, 'fx': 'music', 'icon': '🎵', 'sense': 'I HEARD', 't': 'Music plays'},
            {'id': 'mug', 'at': 27, 'dur': 6, 'fx': 'mug', 'icon': '☕', 'sense': 'I FELT', 't': 'A warm mug in my hands'},
            {'id': 'thermo', 'at': 32, 'dur': 6, 'fx': 'thermo', 'icon': '🌡️', 'sense': 'I MEASURED', 't': 'The cocoa reads 160°F'},
            {'id': 'teo', 'at': 37, 'dur': 4.5, 'fx': 'teo', 'icon': '💬', 'sense': '', 't': ''}],
        'decoy': {'id': 'says', 'icon': '💬', 'sense': 'SOMEONE SAID', 't': 'Teo says it runs everything', 'miss': 'Saying so is not evidence. You can’t see, hear, feel or measure it.'},
        'grid': ['lights', 'horn', 'says', 'wheel', 'free', 'music', 'meter', 'mug', 'thermo'],
        'playBtn': '▶ Play the scene', 'pauseBtn': '⏸ Pause', 'nextBtn': 'Next moment ▶', 'liveWord': 'LIVE',
        'notNow': 'Not right now! Tap it WHILE it is happening.', 'needPlay': 'Press Play first, then watch the scene.', 'countWord': 'squares marked',
        'bingoLine': 'Every square you marked was something you could see, hear, feel or measure.',
        'q': 'What makes something evidence?',
        'opts': [{'t': 'You can see, hear, feel or measure it.', 'ok': True},
                 {'t': 'Someone tells you it’s true.', 'miss': 'Could you ever mark the “Teo says” square?'},
                 {'t': 'You really, really believe it.', 'miss': 'Believing isn’t observing. What did every marked square have in common?'}],
        'win': 'Evidence is what you can see, hear, feel or measure. Clue 3!'},
    'binder': {
        'afterText': 'Every card you finish goes into your binder.', 'kicker': 'Part 3 game', 'title': 'Fill the card binder',
        'todo': ['Tap a blank card.', 'Pick its starting energy and its resulting energy.', 'Pick the best evidence. A finished card shines and goes in your binder.'],
        'why': {'icon': '🃏', 'q': 'What makes the BEST evidence?', 't': 'It shows that the energy CHANGED. “The lamp is tall” is true, but it doesn’t prove anything about energy.'},
        'energies': EN, 'labels': {'s': 'Starting energy', 'r': 'Resulting energy', 'e': 'Best evidence'}, 'pickLine': '1. Tap a blank card',
        'binderLabel': 'My binder', 'emptyLine': 'empty sleeve', 'tableLabel': 'My data table', 'cols': ['System', 'Starting', 'Resulting', 'Evidence'], 'countWord': 'cards in the binder',
        'cards': [
            {'id': 'lamp', 't': 'A lamp', 'img': I('lamp'), 'alt': 'A desk lamp glowing at night over a desk with a pencil cup.', 's': 'electrical', 'r': 'light',
             'missS': 'What comes through the cord from the wall?', 'missR': 'What do you see when it’s on?',
             'ev': [{'t': 'The bulb glows when I flip the switch.', 'ok': True}, {'t': 'The lamp is tall and bendy.', 'miss': 'True, but does it show an energy change?'}, {'t': 'My friend says lamps make light.', 'miss': 'Saying so isn’t evidence. What can you observe?'}]},
            {'id': 'micro', 't': 'A microwave', 'img': I('microwave'), 'alt': 'A silver microwave oven with a number pad.', 's': 'electrical', 'r': 'heat',
             'missS': 'A microwave has a plug. What comes through it?', 'missR': 'What happens to cold soup inside?',
             'ev': [{'t': 'Cold soup comes out steaming, and a thermometer reads hotter.', 'ok': True}, {'t': 'It has a door and buttons.', 'miss': 'True, but does that show an energy change?'}, {'t': 'It’s the newest one at the store.', 'miss': 'That’s not something that shows energy changing.'}]},
            {'id': 'walk', 't': 'You walking', 'img': I('walking'), 'alt': 'Two people walking on a wooden boardwalk through a green Florida forest.', 's': 'chemical', 'r': 'motion',
             'missS': 'What gives your body energy? Think about lunch.', 'missR': 'What do your legs do?',
             'ev': [{'t': 'My legs move, and I get farther down the boardwalk.', 'ok': True}, {'t': 'My shoes are blue.', 'miss': 'True maybe, but does it show an energy change?'}, {'t': 'Walking is my favorite.', 'miss': 'That’s an opinion, not an observation.'}]},
            {'id': 'leaf', 't': 'The Sun on a leaf', 'img': I('leaf'), 'alt': 'Sunlight shining through a huge green taro leaf, showing its veins.', 's': 'light', 'r': 'chemical',
             'missS': 'What shines on the leaf?', 'missR': 'A leaf turns sunlight into stored food. What kind of energy is food?',
             'ev': [{'t': 'The plant grows new leaves when it gets sunlight.', 'ok': True}, {'t': 'Leaves are green.', 'miss': 'True, but does green show an energy change?'}, {'t': 'Plants are nice.', 'miss': 'That’s an opinion, not evidence.'}]},
            {'id': 'turbine', 't': 'A wind turbine', 'img': I('wind-turbine'), 'alt': 'Tall white wind turbines with three blades on a hillside under a blue sky.', 's': 'motion', 'r': 'electrical',
             'missS': 'What pushes the blades around?', 'missR': 'Wires carry its energy to homes. What kind?',
             'ev': [{'t': 'When the blades spin, a meter shows electricity flowing to homes.', 'ok': True}, {'t': 'Turbines are very tall.', 'miss': 'True, but does that show energy changing?'}, {'t': 'The sign says it’s a wind farm.', 'miss': 'A sign is someone saying so. What can you observe changing?'}]}],
        'credits': 'Photos via Wikimedia Commons: lamp, M. H. Mathias, CC BY 2.0 · microwave, Wrightmt, public domain · boardwalk, Everglades National Park, public domain · taro leaf, Avenue, CC BY-SA 3.0 · wind turbines, Joshua Winchell, U.S. Fish and Wildlife Service, public domain.',
        'q': 'Look at your “you walking” card. What is the starting energy for YOUR motion?',
        'opts': [{'t': 'Chemical energy from the food I ate.', 'ok': True},
                 {'t': 'Motion energy that was always in my legs.', 'miss': 'Where did your legs get their energy? Check the card.'},
                 {'t': 'Electrical energy from a wall outlet.', 'miss': 'You don’t plug yourself in! Check the card.'}],
        'win': 'Your food’s chemical energy becomes your motion. Your body is an energy changer. Clue 4!'},
    'exploreMod': 'binder',
    'pedal': {
        'after': 'binder', 'kicker': 'Wow!', 'title': 'Pedal Teo’s bike',
        'todo': ['Switch on the string lights, the menu sign and the radio.', 'Pedal: tap Left, Right, Left, Right (or the ← → keys). Then stop and watch.', 'Last, switch on the cocoa warmer.'],
        'why': {'icon': '🚴', 'q': 'What is a watt?', 't': 'A watt measures how fast energy is used. A strong grown-up rider can keep up about 100 watts for a while.'},
        'model': 'a model', 'riderW': 100, 'perStroke': 30, 'loadsLine': '1. Switch things on (tap)',
        'loads': [{'id': 'str', 'svg': 'str', 'icon': '💡', 't': 'String lights', 'w': 7},
                  {'id': 'sign', 'svg': 'sign', 'icon': '🪧', 't': 'Menu sign', 'w': 15},
                  {'id': 'radio', 'svg': 'radio', 'icon': '📻', 't': 'Radio', 'w': 8},
                  {'id': 'warm', 'svg': 'warm', 'icon': '☕', 't': 'Cocoa warmer', 'w': 1500, 'big': True}],
        'leftBtn': '◀ Left pedal', 'rightBtn': 'Right pedal ▶', 'keysLine': 'Tap them one after the other, or press the ← and → keys after you tap the picture.',
        'makeWord': 'You make', 'needWord': 'Switched on needs', 'okLine': 'It works! Your pedaling powers everything that’s switched on.', 'lowLine': 'Not enough. Pedal faster, or switch something off.',
        'stopLine': 'You stopped, and everything went dark. That’s evidence: the energy came from your pedaling.',
        'ridersLine': 'The cocoa warmer needs about 1,500 watts. That’s about {n} strong riders pedaling hard at the same time!',
        'bigLine': ' One rider can light the whole cart, but heating cocoa takes much more energy. Rosa will heat her cocoa at home and bring it in insulated jugs.',
        'done': 'One rider lights the cart. The warmer needs a plug. And no pedaling means no light!'},
    'glowwake': {
        'after': '.fs-solve', 'kicker': 'Bonus · wild card', 'title': 'The glowing wake',
        'todo': ['Drag the boat across the dark water (or press Go).', 'Watch the water where the boat goes.', 'Then answer one question.'],
        'lockLine': 'Crack the case first.', 'model': 'a model',
        'why': {'icon': '🌊', 'q': 'Is this real?', 't': 'Yes! In Florida’s Indian River Lagoon, tiny comb jellies flash blue-green when a boat or a paddle stirs the water on winter nights. A comb jelly is not a jellyfish, and it can’t sting.'},
        'goBtn': '⛵ Go', 'dragHint': 'Or drag the boat across the water.', 'needFlashes': 15, 'flashWord': 'flashes',
        'photo': {'img': I('comb-jelly'), 'alt': 'A see-through comb jelly with glowing rainbow-colored rows, swimming in dark water.', 'cap': 'A real comb jelly (a sea walnut). The rainbow shine in this photo is aquarium light bouncing off its moving combs. Its own flash is blue-green, and you only see it in the dark. Photo: Steven G. Johnson, CC BY-SA 3.0, via Wikimedia Commons.'},
        'q': 'The boat bumps the comb jellies, and they flash. What is the starting energy of the LIGHT?',
        'opts': [{'t': 'Chemical energy inside the comb jellies.', 'ok': True, 'why': 'Right! Like a glow stick, the jellies mix chemicals inside their bodies to make light. The bump only tells them when to flash.'},
                 {'t': 'The boat’s motion turns straight into light.', 'why': 'The bump is just the signal. Think about the glow stick: where did ITS light start?'},
                 {'t': 'The Moon’s light bouncing off the water.', 'why': 'The flashes happen only where the boat stirs the water. Moonlight is everywhere.'}],
        'win': 'Living glow sticks! Chemical energy → light.'},
    'fold': {'glowwake': {'icon': '🌊', 'tease': 'A boat’s wake glows in the dark, with no lights at all. How?', 'open': 'Play'}},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Think about the slot machine. Where does a plug-in device get its energy?', 'C': 'Bread can’t heat itself. What comes through the toaster’s cord?'},
        'q2': {'B': 'Think about evidence bingo. Does weight show an energy change?', 'C': 'Think about the binder. “It’s made of plastic” is true, but does it show a change?'},
        'q3': {'A': 'Start with the rider. What did you eat to get energy?', 'B': 'Think about Teo’s bike. What does the rider’s food become first?'}},
    'flags': {
        'ans-1': [
            {'label': 'the STARTING energy', 're': 'start|electric|chemical|food|light|sun'},
            {'label': 'the RESULTING energy', 're': 'result|light|motion|sound|electric|move|spin'},
            {'label': 'one piece of EVIDENCE', 're': 'evidence|see|saw|hear|heard|feel|felt|glow|spin|music|measure|meter|because'}],
        'ans-3': [
            {'label': 'uses EVIDENCE', 're': 'evidence|evedence|evidance|proof|prove'},
            {'label': 'what you can observe', 're': 'see|hear|feel|measure|observ|notice'},
            {'label': 'what happens with no evidence', 're': 'not believe|wouldn|won|nobody|no one|can.?t|cannot|might be wrong|could be wrong|not true|lie|guess|just say'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|start|doesn|does not|didn'},
            {'label': 'two pieces of evidence', 'any': ['glow', 'stick', 'chemical', 'battery', 'electric', 'pedal', 'bike', 'light', 'dark', 'stop', 'slot', 'lamp', 'generator', 'food', 'card', 'binder', 'evidence', 'bingo', 'switch'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-1': 15, 'ans-3': 15, 'cer-4': 30},
    'hints': {
        'ans-1': ['Pick one card: lamp, bike, speaker or solar panel.', 'Where does its energy start? What does it become?', 'Try: A ___ starts with ___ energy and makes ___ energy. My evidence is that I can see/hear ___.'],
        'ans-3': ['Think about the “Teo says” square in bingo.', 'What can a scientist see, hear, feel or measure?', 'Try: Evidence is important because ___. Without evidence, ___.'],
        'cer-4': ['First decide: does energy really just appear?', 'Think about the glow stick and Teo’s bike.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'A glow stick has no battery, but its light still started as chemical energy inside it.',
                'Teo’s lights glowed only while someone pedaled. When the pedaling stopped, they went dark.',
                'In the slot machine, every device had a starting energy that changed into a different one.',
                'The light was so bright it must have come from nowhere.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · Teo’s napkin plan', 'length': '20–30 s'},
        'warmup': {'label': 'Warm-Up · crack a glow stick (Clue 1)', 'length': '15–20 s',
                   'script': 'Sam here, back at the parade. First, read Teo’s napkin and Rosa’s note. Then, the glow stick! Bend it till it cracks, shake it, and tap the two things you really observe.'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · the energy slot machine (Clue 2)', 'length': '15–20 s',
                  'script': 'Welcome to the energy slot machine! Pull the lever to get a device. Then stop the starting reel and the resulting reel on the right energy, and press Check.'},
        'part2': {'label': 'Part 2 · evidence bingo (Clue 3)', 'length': '15–20 s',
                  'script': 'Evidence bingo! Press Play and watch Rosa’s cart. Tap a square the moment you see, hear, feel or measure it. Careful: one square never counts.'},
        'explore': {'label': 'Part 3 · the card binder + pedal power (Clue 4)', 'length': '20–30 s'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · my 4 energy change cards', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '15–20 s',
                     'script': 'A classmate says energy just appears in a flashlight. True? Think about the glow stick, and Teo’s bike when you stopped pedaling. Pick your side, tap two facts, then explain. That’s your C-E-R.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 25.01 (how objects move).'},
    },
    'videoOff': [],
    'lensVoice': False,
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Teo’s napkin plan (Warm-Up)',
        'Your glowing glow stick (Warm-Up)',
        'A winning line on the slot machine (The Lesson)',
        'Your full card binder (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['A flashlight', 'A fan', 'A bike with a light'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch and label one of your cards', 'required': True, 'minLabels': 3,
                           'prompts': ['Draw one device or system from your cards', 'Label where the energy STARTS and what it BECOMES', 'Label your evidence (what you can see, hear, feel or measure)']}]},
    'hlCoach': copy.deepcopy(O['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🧻', 'name': 'Teo’s napkin plan',
                 'line': 'You cracked Case 24, part 2, and Teo’s napkin goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next week: how objects move.'},
    'notebookTitle': 'Unit 5 · Energy, Motion & Collisions',
    'notebook': copy.deepcopy(O['notebook']),
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. Energy changed, and you proved it!',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to see what it means.']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '#tab-vocab p', 'text': 'What glows, buzzes, spins or warms up?'},
         'label': 'Warm-Up: things at home that glow, buzz, spin or warm up', 'q': 'Warm-Up: Three things at home that glow, buzz, spin or warm up.', 'title': 'Things that glow, buzz, spin or warm up', 'compact': True,
         'fields': [{'t': 'Thing 1', 'icon': '💡', 'ph': 'The ___ glows / buzzes / spins / warms up.'},
                    {'t': 'Thing 2', 'icon': '🔊', 'ph': 'The ___ glows / buzzes / spins / warms up.'},
                    {'t': 'Thing 3', 'icon': '🌀', 'ph': 'The ___ glows / buzzes / spins / warms up.'}]},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Then sketch and label one.'},
         'label': 'Part C: My 4 energy change cards', 'q': 'Part C: My 4 energy change cards (starting → resulting + one piece of evidence each)', 'title': 'My 4 energy change cards',
         'fields': [{'t': 'Card 1', 'icon': '🃏', 'ph': 'A ___: ___ energy → ___ energy. Evidence: I can see/hear/feel ___.'},
                    {'t': 'Card 2', 'icon': '🃏', 'ph': 'A ___: ___ energy → ___ energy. Evidence: ___.'},
                    {'t': 'Card 3', 'icon': '🃏', 'ph': 'A ___: ___ energy → ___ energy. Evidence: ___.'},
                    {'t': 'Card 4', 'icon': '🃏', 'ph': 'A ___: ___ energy → ___ energy. Evidence: ___.', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Does energy just appear in a flashlight?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-1': 'Part B · Question 5', 'ans-3': 'Part B · Question 7', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] == '24.02': n.update({'icon': '🧻', 'name': 'Teo’s napkin plan'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'A great claim names the energy change and points to evidence you can see, hear, feel or measure.',
    'key': ['claim', 'energy', 'change', 'evidence', 'measure'],
    'small': ['a', 'the', 'and', 'to', 'you', 'can', 'or'],
    'model': 'A scientist might highlight “claim”, “energy change” and “evidence”. Those words hold the big idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me say where the energy started, what it became, and how I know?']

EV = '#tab-assignment .act-body > div:has(> .fs-plan)'
D['cues'] = {
    'warmup': [{'at': '^napkin', 'sel': '.fs-npk-paper', 'fx': 'glow', 'scroll': True},
               {'at': '^note', 'sel': '.fs-npk-reply', 'fx': 'pop'},
               {'at': '^glow', 'sel': '.fs-gls-svg', 'fx': 'glow', 'scroll': True},
               {'at': '^bend', 'sel': '.fs-gls-bend', 'fx': 'point'},
               {'at': '^shake', 'sel': '.fs-gls-shake', 'fx': 'point'},
               {'at': '^observe', 'sel': '[data-mod="glowstick"] .fs-todo li', 'i': 2, 'fx': 'trace'}],
    'part1': [{'at': '^slot', 'sel': '.fs-reel-mach', 'fx': 'glow', 'scroll': True},
              {'at': '^lever', 'sel': '.fs-reel-pull', 'fx': 'point'},
              {'at': '^starting', 'sel': '.fs-reel-win[data-k="1"]', 'fx': 'pop', 'tag': 'START'},
              {'at': '^resulting', 'sel': '.fs-reel-win[data-k="2"]', 'fx': 'pop', 'tag': 'RESULT'},
              {'at': '^check', 'sel': '.fs-reel-check', 'fx': 'point'}],
    'part2': [{'at': '^play', 'sel': '.fs-bgo-play', 'fx': 'point', 'scroll': True},
              {'at': '^cart', 'sel': '.fs-bgo-svg', 'fx': 'glow'},
              {'at': '^square', 'sel': '.fs-bgo-grid', 'fx': 'pop'},
              {'at': '^never', 'sel': '.fs-bgo-sq[data-id="says"]', 'fx': 'wiggle'}],
    'evidence': [{'at': '^classmate', 'sel': EV + ' > p', 'i': 0, 'fx': 'trace', 'scroll': True},
                 {'at': '^glow', 'sel': '.fs-plan .fs-opt', 'i': 2, 'fx': 'glow'},
                 {'at': '^pedaling', 'sel': '.fs-plan .fs-opt', 'i': 3, 'fx': 'glow'},
                 {'at': '^side', 'sel': '.fs-plan .fs-plan-row', 'i': 0, 'fx': 'pop'},
                 {'at': '^explain', 'sel': '.fs-cer .fs-cer-row', 'i': 2, 'fx': 'glow', 'scroll': True}],
}
D['cueWords'] = json.load(open('cuewords.json', encoding='utf-8')) if os.path.exists('cuewords.json') else {}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
clips = {k: v['script'] for k, v in D['slots'].items() if v.get('script')}
tot = sum(len(t) for t in clips.values())
for k, t in clips.items(): print(f'  {k:10} {len(t):4}')
print(f'this page: {tot} / 1400 credits ({tot/1400:.0%})')
assert tot <= 1330
