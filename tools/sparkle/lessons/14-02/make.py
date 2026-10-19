#!/usr/bin/env python3
"""Writes data.json and fixes.json for 14.02 (run from this folder)."""
import json, copy
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../14-01/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

# ---------------------------------------------------------------- ticked fixes (Bethany, 19 Oct 2026)
fx('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist asks for a two-region seasonal model',
   '🎨 Part C &mdash; Build Your Own Food Chain', '🗺️ Part C &mdash; A Two-Region Seasonal Model')
fx('fix', 'copy-paste leftover: Part C task from 9.01 (typed on the page now; the sketch is a bonus)',
   r'<p style="font-size:15px;color:#9A8E82;margin-bottom:14px;">In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   '<p style="font-size:15px;color:#9A8E82;margin-bottom:14px;">Pick a season and one region besides Florida (like Maine or Colorado). Describe both places in that season, one food-energy connection in each, and how the regions are connected.</p>', True)
fx('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'quarter label in the footer: week 14 is Quarter 2', 'Science &middot; Quarter 3 &middot;', 'Science &middot; Quarter 2 &middot;')
fx('fix', 'wrong fact: seasons come from Earth’s tilt, not the water cycle (the water-cycle paragraph is cut; the weather/climate idea stays, shorter)',
   r'<p style="font-size:15px;color:#5A4D3E;line-height:1.65;margin:0 0 10px;"><strong>Weather</strong> is what.*?</p>\s*<p style="font-size:15px;color:#5A4D3E;line-height:1.65;margin:0;"><strong>The water cycle connects it all\.</strong>.*?</p>',
   '<p style="font-size:15px;color:#5A4D3E;line-height:1.65;margin:0;"><strong>Weather</strong> is what\'s happening outside <em>right now</em>. <strong>Climate</strong> is the usual weather in a place over many years. Seasons happen because Earth is tilted as it travels around the Sun, so each place gets more sunlight in summer and less in winter.</p>', True)
fx('fix', 'the old figure looked AI-made (a two-way food-energy arrow on the chickadee); two real photos replace it',
   r'<div class="lesson-figure-label">🍂 January in Florida vs\. January in Maine</div>\s*<img src="images/14-02-seasons-comparison\.png"\s*alt="[^"]*"',
   '<div class="lesson-figure-label">🍂 Winter in Florida vs. winter up north</div>\n        <img src="images/14-02-seasons-real.jpg"\n             alt="Two photos side by side. Left: dozens of manatees crowded in the clear water of a Florida spring in winter. Right: a pond frozen solid and covered with snow, with bare trees behind it."', True)
fx('fix', 'caption matches the real photos', r'<div class="lesson-figure-caption"><strong>Same month, two regions\.</strong>.*?</div>',
   '<div class="lesson-figure-caption"><strong>Same season, two regions.</strong> Florida\'s water stays open; up north, ponds freeze. Photos: USFWS (CC BY 2.0); Dinohoax1 (CC BY 3.0).</div>', True)
fx('fix', 'Q5 pointed to “the diagram”; the four stories are now rows in Turn the calendar',
   'Pick one of the four examples from the diagram (migrating ducks, manatee winter, citrus harvest, or sea turtle nesting).',
   'Pick one of these seasonal stories from Turn the calendar: migrating ducks, manatees in winter, the orange harvest, or sea turtle nesting.')

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; dashes removed',
   "Hold this question in your head as you work. By the end of the lesson, you'll build a model that compares Florida's seasons to another region's — and shows how plants, animals, and food energy stay connected across the year.",
   "Keep this question in mind. By the end, you'll build a model that compares Florida's seasons to another region's, and shows how plants, animals and food energy stay connected.")
fx('plain', 'answers are made on the page now (the game below)',
   r"<p>It's January in Florida\. What's happening outside\?.*?</p>\s*<p>Now imagine the same month in Maine\..*?</p>",
   "<p>It's January. In Florida, what's happening outside? Now picture the same month in Maine. <strong>Where would you see each photo?</strong> Sort them in the game below.</p>", True)
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', 'shorter; dashes removed',
   "If you visited Maine in January, you'd see snow on the ground, bare trees, and very few animals out in the open. Florida in January looks completely different: green grass, palm trees with leaves, songbirds singing, lizards on fences. Same month — totally different scene.",
   "In January, Maine has snow on the ground, bare trees and very few animals out in the open. Florida in January has green grass, songbirds and lizards on fences. Same month, totally different scene.")
fx('plain', 'one idea per sentence',
   "is mild. Our winters stay warm. Our summers are hot and rainy. Other ",
   "is mild. Our winters are mild and our summers are hot and rainy. Other ")
fx('plain', 'dashes removed; shorter',
   "</span></span> — they all need each other. Plants need pollinators to make seeds. Birds need insects to feed their babies. Mammals need plants and animals for food. Every animal — including humans — gets its energy from food, which means the energy was stored in something else first.</p>",
   "</span></span>: they need each other. Plants need pollinators to make seeds. Birds need insects to feed their babies. Every animal, including you, gets its energy from food.</p>")
fx('plain', 'shorter bullets', "Most plants keep growing (slower). Many animals stay active. Florida becomes a winter home for birds that ",
   "Plants keep growing and many animals stay active. Birds ")
fx('plain', 'shorter bullets', "south to find food.</li>", "here from the north to find food.</li>")
fx('plain', 'shorter bullets', "Many trees drop their leaves to save energy. Some animals ", "Many trees drop their leaves. Some animals ")
fx('plain', 'shorter bullets', " (like bears and chipmunks). Other animals — like robins — fly south, sometimes all the way to Florida.</li>", ", like bears. Others, like robins, fly south.</li>")
fx('plain', 'shorter; dash removed', "the plant stored gets passed to them. So when winter comes and plants slow down or die back, every animal in that region has to find food a different way — or move to a place where food is still available.</p>",
   "the plant stored passes to them. When winter stops the plants, animals must find food another way, or move where food is still growing.</p>")
fx('plain', 'shorter labels', "<strong>Florida response to mild winters:</strong>", "<strong>Florida's mild winter:</strong>")
fx('plain', 'shorter labels', "<strong>Maine response to cold winters:</strong>", "<strong>Maine's cold winter:</strong>")
fx('plain', 'shorter', "When humans and animals eat plants, the ", "When animals eat plants, the ")
fx('cut', 'lean: Turn the calendar asks the same question; one calm stop per tab is enough', r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('plain', 'dash removed', "about the INTERDEPENDENCE — who depends on whom?", "about the INTERDEPENDENCE: who depends on whom?")
fx('plain', 'shorter; dashes removed', r"<p><strong>Nicely done\.</strong>.*?</p>",
   "<p><strong>Nicely done.</strong> You can now compare Florida to other <span class=\"vtip\">regions<span class=\"vtip-box\"><span class=\"vtip-word\">Region</span>A large area with its own climate.</span></span> across the seasons and explain how living things depend on each other for food energy. Next lesson: the rocks, water, sunlight and wind that people use as <em>resources</em>.</p>", True)
fx('plain', 'plain label; dashes removed; drops the “wet/dry seasons” claim about bird timing',
   r"<p><strong>Common misconception:</strong> Some people think Florida doesn't have seasons\..*?</p>",
   "<p><strong>Watch out:</strong> Some people think Florida doesn't have seasons. It does! They're just <em>milder</em>. Days are shorter in winter and longer in summer here too, and plants flower at different times of year.</p>", True)
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean + shaky fact: remove the Explore tab (its model moves to Part 4 and Part C; the “hurricane season is shifting” Go Deeper goes with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: the Key Concept box repeats Part 2', r'<div style="background:#FFF6E5;border:2.5px solid #F0C97A;[^"]*">\s*<div[^>]*>⭐ Key Concept</div>.*?</div>\s*', '', True)
fx('cut', 'lean: Stop & Reason pointed at arrows in the old figure (Stop & Think in Part 1 stays)', r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: the tap diagram becomes Part 3 (the four stories are rows in Turn the calendar)', 'margin-top:22px;">Four Seasonal Stories</h3>', 'margin-top:22px;">Part 3 · The Manatee Water Test</h3>')
fx('cut', 'lean: Part 3 intro for the water test', '<p><strong>Tap each card</strong> to see what one Florida species does (or who visits it) across the seasons.</p>',
   '<p>Every winter, Florida manatees face a test: cold water. Scientists test one thing at a time. Change only the river\'s temperature and see where the manatees go.</p>')
fx('cut', 'lean: the tap diagram is replaced by the water test (its four stories live in Turn the calendar)',
   r'<div class="diagram-wrap diagram-interactive".*?<div class="diagram-info-panel" id="diagramPanel">.*?</div>\s*</div>\s*', '', True)
fx('cut', 'lean + wrong fact: Observe & Reason, the “5 million ducks … more than half the people” fact, the manatee callout and Go Deeper; Part 4 = the old Explore; next button goes to Self-Check',
   r'<div class="socratic-q">\s*<span class="sq-icon">👀</span>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 4 · Build a Seasonal Model</h3>\n      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">Scientists build models to show connections. Build a model of January in two regions, Florida and Maine. Put a plant, an animal and the weather in each circle. Then show how food energy and migration connect them.</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 7 removed (Bethany kept 5 and 6)', r'<div class="pq">\s*<span class="pq-num"[^>]*>7</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C typed on the page; the sketch is a bonus',
   'A two-region model showing Florida + one other region in the same season, with food-energy arrows in each circle plus one arrow between them.',
   'Your two-region model: both places in one season, a food-energy connection in each, and how they are connected. (A sketch is a bonus.)')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether Florida has seasons, and supported it with two pieces of evidence from the lesson.',
   '<strong>Use Your Evidence:</strong> My claim about whether Florida has seasons, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', True)

# ---------------------------------------------------------------- photo credits
CR = {
    'frozen': 'Frozen pond in winter, Dinohoax1, via Wikimedia Commons (CC BY 3.0)',
    'bearden': 'A U.S. Fish and Wildlife Service biologist at a black bear’s winter den, USFWS, via Wikimedia Commons (public domain)',
    'bear': 'American black bear lying in snow, Warren Garst, via Wikimedia Commons (CC BY-SA 4.0)',
    'chick': 'Black-capped chickadee in the snow, U.S. Fish and Wildlife Service Midwest Region, via Wikimedia Commons (public domain)',
    'ducks': 'Ring-necked ducks at Lake Apopka, Florida, in January, lwolfartist, via Wikimedia Commons (CC BY 2.0)',
    'robin': 'American robin eating holly berries, Andy Reago & Chrissy McClarren, via Wikimedia Commons (CC BY 2.0)',
    'spring': 'Manatees crowded in a warm spring, Crystal River National Wildlife Refuge, U.S. Fish and Wildlife Service, via Wikimedia Commons (CC BY 2.0)',
    'manatee': 'Florida manatee, U.S. Fish and Wildlife Service, via Wikimedia Commons (public domain)',
    'orange': 'Florida orange grove, Mmacbeth, via Wikimedia Commons (CC0)',
    'anole': 'Green anole, Danny S., via Wikimedia Commons (public domain)',
    'spruce': 'Black spruce cones on snow, U.S. Fish and Wildlife Service Alaska Region, via Wikimedia Commons (public domain)',
    'seagrass': 'Manatee grass (a seagrass), James St. John, via Wikimedia Commons (CC BY 2.0)',
    'teggs': 'Loggerhead sea turtle eggs in a nest, U.S. Fish and Wildlife Service, via Wikimedia Commons (public domain)',
}
def cr(*keys): return '. '.join(CR[k] for k in keys) + '.'
I = lambda n: 'images/14-02-' + n + '.jpg'

def row(icon, name, fl, up):
    def cells(v): return [{'s': s, 't': t} for s, t in v]
    return {'icon': icon, 'name': name, 'cells': {'fl': cells(fl), 'up': cells(up)}}
NONE4 = lambda t: [('none', t)] * 4

D = {
    'lesson': '14.02', 'week': 14, 'day': 2, 'guide': 'lena', 'prefix': 'g4sci-14-2', 'manifestKey': '14-02',
    'paths': P['paths'], 'crew': P['crew'],
    'expedition': {'num': 14, 'title': 'Postcards from Maine'},
    'ambient': {'icon': '🦆', 'label': 'Winter pond sounds'},
    'case': {
        'num': '14 · part 2', 'title': 'Postcards from Maine', 'style': 'postcards',
        'hook': 'It’s January, and my pond is busier than ever: ducks on the water, robins in the holly, a manatee in the warm spring run. Then postcards came from my friend Bea, a ranger in Maine. Her pond is frozen and almost empty. She asks: “Florida doesn’t really have seasons, right?”',
        'question': 'Why did my pond get busier in January when Bea’s pond in Maine went quiet? And does Florida have seasons?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'stills': [],
        'logs': [
            {'head': 'Postcard 1 · Bea’s pond', 'img': I('frozen-pond'), 'alt': 'A pond frozen solid and covered with snow, with bare trees behind it.',
             'rows': [['Water', 'frozen solid'], ['Ducks', 'all gone'], ['Plants', 'brown, resting']], 'big': 'MAINE JAN 5'},
            {'head': 'Postcard 2 · the woods', 'img': I('bear-den'), 'alt': 'A biologist in winter clothes kneels in deep snow next to the dark opening of a bear den.',
             'rows': [['Found', 'a bear den in the snow'], ['Bear', 'asleep since November'], ['Eating?', 'not until spring']], 'big': 'MAINE JAN 12'},
            {'head': 'Postcard 3 · my feeder', 'img': I('chickadee'), 'alt': 'A small black, white and gray chickadee perched on a branch while snow falls.',
             'rows': [['Still here', 'chickadees'], ['Gone', 'robins and ducks'], ['P.S.', 'no seasons in Florida, right?']], 'big': 'MAINE JAN 19'},
            {'head': 'My pond log · Florida', 'img': I('ducks'), 'alt': 'A group of brown and gray ring-necked ducks swimming on open water.',
             'rows': [['Ducks', 'about 60, new since fall'], ['Robins', 'a flock in the holly'], ['Spring run', '1 manatee']], 'big': 'FLORIDA JAN 20'}],
        'sticky': '“Florida doesn’t really have seasons, right?” (Bea)',
        'stillsCredit': 'Postcard 1: ' + CR['frozen'] + '. Postcard 2: ' + CR['bearden'] + '. Postcard 3: ' + CR['chick'] + '. Pond log: ' + CR['ducks'] + '. Bea and her postcards are part of the story; the photos are real.',
        'clues': [
            {'id': 'twowinters', 'icon': '🌡', 'where': 'Warm-Up: two winters', 't': 'In January, ponds up north freeze and most plants stop growing. Florida’s water stays open and plants keep growing. Same season, different regions.'},
            {'id': 'calendar', 'icon': '📅', 'where': 'The Lesson, Part 1: turn the calendar', 't': 'Florida has seasons too, just milder ones. Ducks and robins leave the cold north in fall and spend the winter here. Maine’s bears hibernate; Florida’s stay awake.'},
            {'id': 'manatee', 'icon': '♨️', 'where': 'The Lesson, Part 3: the manatee water test', 't': 'When river water drops below 68°F, manatees crowd into warm springs that stay about 72°F all year. They depend on Florida’s warm water to survive winter.'},
            {'id': 'seasonmodel', 'icon': '🧩', 'where': 'The Lesson, Part 4: build the seasonal model', 't': 'Animals get food energy from plants. When winter freezes the food up north, some animals sleep and others migrate to Florida, where plants keep growing.'},
        ],
        'solve': {
            'title': 'Why is Dr. Reyes’s pond so busy?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'Florida has no seasons, so the animals here never change what they do.', 'why': 'Check Clues 2 and 3. Do manatees and ducks do the same thing in July as in January?'},
                {'t': 'Winter froze Bea’s pond and stopped the plants, so food energy got hard to find. Bears hibernate, and ducks and robins migrate to Florida, where the water stays open and plants keep growing. Florida does have seasons, just milder ones: in winter, manatees move into warm springs.', 'right': True,
                 'why': 'Case cracked! Same season, two regions, and living things that depend on each other and on the seasons. Now write your case report: it’s the questions below.'},
                {'t': 'The animals got lost on their way somewhere else, and Florida is just where they landed.', 'why': 'Check Clue 4. What do the animals find in Florida that they can’t find in frozen Maine?'},
            ]},
    },
    'twowinters': {
        'afterText': 'Where would you see each photo?', 'kicker': 'Warm-Up game', 'title': 'Two winters',
        'todo': ['Where would you see each photo in January: Florida or Maine?', 'Drag it there, or tap the photo and then the place.', 'Sort all eight, then answer the question.'],
        'why': {'icon': '🗺️', 'q': 'Two regions', 't': 'Florida and Maine are regions: large areas, each with its own climate.'},
        'sides': [{'k': 'fl', 'icon': '☀️', 't': 'January in Florida', 'sub': 'about 61°F'}, {'k': 'up', 'icon': '❄️', 't': 'January in Maine', 'sub': 'about 22°F'}],
        'cards': [
            {'id': 'man', 't': 'Manatees in a warm spring', 'img': I('manatee-spring'), 'alt': 'Dozens of manatees crowded in clear spring water.', 'z': 'fl', 'why': 'On cold days, Florida manatees gather in springs that stay warm all year.', 'miss': 'Manatees need warm water. Could they live in a frozen pond?'},
            {'id': 'duck', 't': 'Ducks on an open lake', 'img': I('ducks'), 'alt': 'Ring-necked ducks swimming on open water.', 'z': 'fl', 'why': 'Florida lakes don’t freeze, so ducks from the north find water and food here.', 'miss': 'Is this water frozen or open?'},
            {'id': 'orange', 't': 'Oranges ready to pick', 'img': I('orange-grove'), 'alt': 'Rows of green orange trees under a blue sky.', 'z': 'fl', 'why': 'Florida oranges ripen in fall and winter. January is picking time.', 'miss': 'Could an orange tree grow in snow?'},
            {'id': 'anole', 't': 'A lizard out in the sun', 'img': I('anole'), 'alt': 'A small brown-green anole lizard on a leaf.', 'z': 'fl', 'why': 'On sunny Florida winter days, lizards come out to bask (warm up in the sun).', 'miss': 'Lizards need warmth to move. Where is it warm in January?'},
            {'id': 'pond', 't': 'A frozen pond', 'img': I('frozen-pond'), 'alt': 'A pond frozen solid and covered with snow.', 'z': 'up', 'why': 'Up north, January is cold enough to freeze ponds solid.', 'miss': 'Do Florida ponds freeze solid in January?'},
            {'id': 'bear', 't': 'A black bear in the snow', 'img': I('bear-snow'), 'alt': 'A black bear lying in the snow.', 'z': 'up', 'why': 'Maine’s black bears spend most of the winter asleep in dens.', 'miss': 'Look at the ground. Where is there snow in January?'},
            {'id': 'chick', 't': 'A chickadee in the snow', 'img': I('chickadee'), 'alt': 'A chickadee on a branch in falling snow.', 'z': 'up', 'why': 'Chickadees stay up north all winter and eat seeds from trees.', 'miss': 'Look at the snowflakes. Where does it snow in January?'},
            {'id': 'cones', 't': 'Spruce cones on snow', 'img': I('spruce-cones'), 'alt': 'Two brown spruce cones lying on white snow.', 'z': 'up', 'why': 'Snow covers the ground, so most plants up north rest until spring.', 'miss': 'Look at what the cones are lying on.'}],
        'q': 'What is the biggest difference for a hungry duck in January?',
        'opts': [{'t': 'Florida’s water is open and has food. Maine’s is frozen.', 'ok': True},
                 {'t': 'Florida has more lizards.', 'miss': 'Would a duck care about lizards? Look at the ponds.'},
                 {'t': 'Maine has more snow to play in.', 'miss': 'Think about what a duck needs: water to swim in and food to eat.'}],
        'credit': cr('spring', 'ducks', 'orange', 'anole', 'frozen', 'bear', 'chick', 'spruce'),
        'win': 'Same month, two regions, two very different Januarys. Florida has seasons too, but its winter is mild. That’s a clue.',
        'clue': 'twowinters'},
    'calendar': {
        'afterText': 'bury the ground in snow', 'kicker': 'Part 1 game', 'title': 'Turn the calendar',
        'todo': ['Tap a calendar page to turn to that season.', 'Read across each row: what does it do in Florida, and in Maine?', 'Turn all four pages, then answer the question.'],
        'why': {'icon': '📅', 'q': 'One page, one season', 't': 'Same plants and animals, two regions. Watch what changes.'},
        'regions': [{'k': 'fl', 'icon': '☀️', 't': 'Florida'}, {'k': 'up', 'icon': '❄️', 't': 'Maine'}],
        'seasons': [
            {'k': 'jan', 'icon': '❄️', 't': 'January', 'temps': {'fl': 'about 61°F', 'up': 'about 22°F'}, 'notes': {'fl': 'water open, plants growing', 'up': 'ponds frozen, snow'}},
            {'k': 'apr', 'icon': '🌱', 't': 'April', 'temps': {'fl': 'about 72°F', 'up': 'about 44°F'}, 'notes': {'fl': 'warm and dry', 'up': 'ice melting'}},
            {'k': 'jul', 'icon': '☀️', 't': 'July', 'temps': {'fl': 'about 83°F', 'up': 'about 69°F'}, 'notes': {'fl': 'hot and rainy', 'up': 'warm and green'}},
            {'k': 'oct', 'icon': '🍂', 't': 'October', 'temps': {'fl': 'about 76°F', 'up': 'about 49°F'}, 'notes': {'fl': 'cooler and drier', 'up': 'leaves falling'}}],
        'rows': [
            row('🦆', 'Ducks', [('here', 'here for the winter'), ('gone', 'flying north'), ('gone', 'up north nesting'), ('here', 'starting to arrive')],
                              [('gone', 'flew south'), ('here', 'back to nest'), ('here', 'raising ducklings'), ('gone', 'heading south')]),
            row('🐦', 'Robins', [('here', 'big flocks eating berries'), ('gone', 'most fly north'), ('gone', 'most are up north'), ('gone', 'not here yet')],
                               [('gone', 'most flew south'), ('here', 'back, pulling worms'), ('here', 'raising chicks'), ('busy', 'eating berries to get ready')]),
            row('🦋', 'Monarchs', [('here', 'some stay all winter'), ('here', 'laying eggs'), ('here', 'laying eggs'), ('here', 'many fly through')],
                                 [('gone', 'flew to Mexico'), ('none', 'not back yet'), ('here', 'laying eggs on milkweed'), ('gone', 'flying south')]),
            row('🐉', 'Dragonflies', [('rest', 'fewer flying; nymphs in the pond'), ('here', 'flying'), ('here', 'lots flying'), ('here', 'flying')],
                                    [('rest', 'nymphs wait under the ice'), ('rest', 'nymphs under water'), ('here', 'flying'), ('rest', 'adults gone; nymphs under water')]),
            row('🐻', 'Black bears', [('here', 'awake, finding food'), ('here', 'awake'), ('here', 'awake'), ('busy', 'eating acorns')],
                                    [('sleep', 'hibernating in a den'), ('here', 'waking up hungry'), ('here', 'eating berries'), ('busy', 'eating to store fat')]),
            row('🌊', 'Manatees', [('warm', 'crowd into warm springs'), ('here', 'spread out to eat seagrass'), ('here', 'in rivers and bays'), ('here', 'eating seagrass')], NONE4('too cold for manatees')),
            row('🍊', 'Orange trees', [('here', 'oranges ripe: harvest time'), ('here', 'flowering; bees visit'), ('here', 'green fruit growing'), ('here', 'fruit ripening')], NONE4('too cold to grow')),
            row('🐢', 'Sea turtle nests', [('none', 'no nests'), ('none', 'nesting starts soon'), ('here', 'nests on the beaches'), ('here', 'the last hatchlings')], NONE4('no nests here'))],
        'key': '✅ here · ✈️ migrated away · 😴 hibernating · ♨️ in warm water · 🍽 eating to get ready · 💤 resting',
        'q': 'In January, which two animals from the calendar have flown to Florida from the cold north?',
        'opts': [{'t': 'Ducks and robins', 'ok': True},
                 {'t': 'Manatees and sea turtles', 'miss': 'Look at the Maine column. Do manatees and sea turtle nests ever show up there?'},
                 {'t': 'Black bears and monarchs', 'miss': 'Turn to January. Where are Maine’s bears? And where did Maine’s monarchs fly?'}],
        'credit': 'Temperatures are rounded averages for central Florida (Orlando) and Portland, Maine. Each row shows what most of that animal or plant does; some always stay behind.',
        'win': 'Florida has seasons: milder ones. When the north freezes, ducks and robins migrate here, Maine’s bears hibernate, and Florida’s manatees head for warm water. That’s a clue.',
        'clue': 'calendar'},
    'manatee': {
        'afterText': 'Change only the river', 'kicker': 'Part 3 test', 'title': 'The manatee water test',
        'todo': ['Drag the thermometer to set the river’s temperature.', 'Press Run the morning. Where do the manatees go?', 'Test a cold and a warm morning, then answer the question.'],
        'why': {'icon': '♨️', 'q': 'Why a spring?', 't': 'Water from deep underground bubbles up in Florida springs. It stays about 72°F, winter and summer.'},
        'min': 50, 'max': 85, 'start': 76, 'cold': 68, 'springT': 72, 'token': I('manatee-token'),
        'river': {'img': I('seagrass'), 'alt': 'Long, thin green seagrass growing on a sandy bottom.', 't': 'The river (seagrass to eat)'},
        'spring': {'img': I('manatee-spring'), 'alt': 'Dozens of manatees crowded together in a clear spring.', 't': 'Warm spring'},
        'coldResult': 'Into the warm spring (the river is too cold)', 'warmResult': 'Out in the river, eating seagrass',
        'q': 'On a January morning the river is 58°F. Where will Dr. Reyes find the manatees?',
        'opts': [{'t': 'Crowded in the warm spring', 'ok': True},
                 {'t': 'Out in the river, eating seagrass', 'miss': 'Check your test log. What happened below 68°F?'},
                 {'t': 'Asleep in a den, like a bear', 'miss': 'Manatees don’t hibernate. Where did they go on your cold morning?'}],
        'credit': cr('manatee', 'spring', 'seagrass') + ' The 68°F line is the temperature Florida wildlife scientists use: below it, manatees can get sick from the cold.',
        'win': 'Below 68°F, manatees can get sick from the cold, so they crowd into springs that stay about 72°F. On warm days they swim out to eat seagrass. That’s a clue.',
        'clue': 'manatee'},
    'seasonmodel': {
        'afterText': 'show how food energy and migration connect them', 'kicker': 'Part 4 game', 'title': 'Build the seasonal model',
        'todo': ['Drag each card into a circle, or tap the card and then the circle. Each circle needs a plant, an animal and the weather.', 'In each circle, tap a plant, then the animal that eats it.', 'Add the migration arrow, then answer the question.'],
        'why': {'icon': '🧩', 'q': 'What is a model?', 't': 'A simple picture that shows how parts connect. Scientists use models to explain.'},
        'regions': [{'k': 'fl', 'icon': '☀️', 't': 'Florida in January'}, {'k': 'up', 'icon': '❄️', 't': 'Maine in January'}],
        'roles': [{'k': 'plant', 't': 'a plant'}, {'k': 'animal', 't': 'an animal'}, {'k': 'weather', 't': 'the weather'}],
        'steps': ['Fill both circles', 'Draw the food-energy arrows', 'Add the migration arrow'],
        'doneLine': 'Two regions, two food-energy arrows and a migration arrow: a model a scientist could use.',
        'cards': [
            {'id': 'grass', 't': 'Seagrass', 'img': I('seagrass'), 'alt': 'Long, thin green seagrass on a sandy bottom.', 'z': 'fl', 'role': 'plant', 'why': 'Seagrass keeps growing in Florida’s open water all winter.', 'miss': 'Could seagrass grow under Maine’s ice?'},
            {'id': 'man', 't': 'Manatee', 'img': I('manatee-swim'), 'alt': 'A manatee swimming.', 'z': 'fl', 'role': 'animal', 'why': 'Manatees spend Florida’s winter near warm springs.', 'eatWhy': 'Manatees get their food energy from seagrass and other water plants.', 'miss': 'Manatees need warm water. Which circle has it?'},
            {'id': 'flw', 't': 'Mild, about 61°F; water stays open', 'icon': '☀️', 'alt': '', 'z': 'fl', 'role': 'weather', 'why': 'A mild winter: cool mornings, sunny days, no ice.', 'miss': 'Which place stays mild in January?'},
            {'id': 'cones', 't': 'Spruce cones (seeds inside)', 'img': I('spruce-cones'), 'alt': 'Two spruce cones on snow.', 'z': 'up', 'role': 'plant', 'why': 'Spruce trees keep their seeds in cones, even in winter.', 'miss': 'Look at what the cones are lying on.'},
            {'id': 'chick', 't': 'Chickadee', 'img': I('chickadee'), 'alt': 'A chickadee in falling snow.', 'z': 'up', 'role': 'animal', 'why': 'Chickadees stay in Maine all winter.', 'eatWhy': 'Chickadees pick seeds out of cones and stay in Maine all winter.', 'miss': 'Look at the snowflakes around the chickadee.'},
            {'id': 'bear', 't': 'Black bear, hibernating', 'img': I('bear-snow'), 'alt': 'A black bear lying in snow.', 'z': 'up', 'role': 'animal', 'why': 'In January, Maine’s bears are asleep in dens.', 'arrowMiss': 'A hibernating bear isn’t eating. It lives on fat it stored by eating in the fall.', 'miss': 'Where do bears hibernate in January?'},
            {'id': 'upw', 't': 'Snow and ice, about 22°F', 'icon': '❄️', 'alt': '', 'z': 'up', 'role': 'weather', 'why': 'Cold enough to freeze ponds solid.', 'miss': 'Where is it below freezing in January?'},
            {'id': 'turtle', 't': 'Sea turtle laying eggs', 'img': 'images/14-01-turtle-eggs.jpg', 'alt': 'Sea turtle eggs in a sandy nest.', 'z': 'no', 'role': 'animal', 'miss': 'Sea turtles nest in the warm months (May to October). This model is January.'},
            {'id': 'robin', 't': 'Robin pulling up worms in Maine', 'img': I('robin'), 'alt': 'An American robin eating red holly berries.', 'z': 'no', 'role': 'animal', 'miss': 'In January, Maine’s ground is frozen and most of its robins have flown south.'}],
        'arrows': {'fl': [['grass', 'man']], 'up': [['cones', 'chick']]},
        'arrowMiss': 'Food energy goes from a plant to an animal that eats it, inside the same circle. Which animal here eats that plant?',
        'migrant': {'id': 'duck', 't': 'Ring-necked duck', 'img': I('ducks'), 'alt': 'Ring-necked ducks on open water.', 'done': 'Ducks: Maine ➜ Florida',
                    'ask': 'Ring-necked ducks nest in the north in summer. In January, which way does their migration arrow point?',
                    'q': 'In January, which way does the migration arrow point for ring-necked ducks?',
                    'opts': [{'t': 'From Maine to Florida', 'ok': True},
                             {'t': 'From Florida to Maine', 'miss': 'In January, Maine’s ponds are frozen. Which way would a hungry duck fly?'}]},
        'q': 'Your model explains why ducks come to Florida in winter. Which part of it explains that?',
        'opts': [{'t': 'Florida’s water stays open and plants keep growing, so there’s food energy.', 'ok': True},
                 {'t': 'Florida has more beaches.', 'miss': 'Look at your food-energy arrows. What does a duck need?'},
                 {'t': 'Ducks hibernate in Florida.', 'miss': 'Ducks don’t hibernate. Look at the migration arrow.'}],
        'credit': cr('seagrass', 'manatee', 'spruce', 'chick', 'bear', 'teggs', 'robin', 'ducks'),
        'win': 'Your model is complete! Plants pass food energy to animals. When winter freezes the food in Maine, some animals sleep and others migrate to Florida, where plants keep growing. That’s your last clue.',
        'clue': 'seasonmodel'},
    'exploreMod': 'seasonmodel',
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Roads don’t help a duck. What does a duck need to survive?', 'B': 'Ducks don’t travel for fun. Think about frozen water and food.'},
        'q2': {'A': 'Both are American black bears. What is different about their winters?', 'C': 'Size doesn’t explain it. What does winter take away from a Maine bear?'},
        'q3': {'B': 'Where did the worm get its energy? Keep going back.', 'C': 'Can an animal make energy without eating? Think about where it all starts.'}},
    'flags': {
        'ans-1': [
            {'label': 'one seasonal story', 're': 'duck|manatee|orange|citrus|turtle|nest'},
            {'label': 'the season', 're': 'winter|summer|spring|fall|autumn|season|cold|warm|hot|month|january|may|october'},
            {'label': 'who depends on whom', 're': 'depend|need|eat|food|feed|warm|spring|sand|bee|pollinat|water|shelter'}],
        'ans-2': [
            {'label': 'seasonal change', 're': 'seasonal change|seasons? chang|season'},
            {'label': 'region', 're': 'region'},
            {'label': 'two differences', 'any': ['cold|freez|frozen|snow|ice', 'warm|mild', 'migrat|fly south|flew|leave', 'hibernat|sleep', 'plant|grow|green', 'food'], 'min': 2}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|wrong|right|true|not|does have|do have'},
            {'label': 'two pieces of evidence', 'any': ['day|daylight|shorter|longer', 'manatee|spring', 'duck|robin|bird|migrat', 'turtle|nest', 'orange|citrus|harvest', 'winter|summer|cold|temperature', 'flower|bloom|fruit', 'bear|hibernat'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves'}]},
    'minWords': {'ans-1': 15, 'ans-2': 20, 'cer-4': 30},
    'hints': {
        'ans-1': ['Pick the row you remember best from Turn the calendar.', 'One sentence: which season? One sentence: who needs what?', 'Try: In ___, ___. The ___ depends on ___ for ___.'],
        'ans-2': ['Think of the two winters from the Warm-Up.', 'What happens to the water, the plants and the animals in each place?', 'Try: Florida’s winter is ___, but in the colder region ___. This seasonal change means…'],
        'cer-4': ['First decide: does Florida have seasons or not?', 'Think of the manatee test and Turn the calendar.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'Florida’s days get shorter in winter and longer in summer.',
                'In winter, manatees crowd into warm springs. In summer, they spread out into rivers and bays.',
                'Ducks and robins come to Florida every winter and leave in spring.',
                'Sea turtles nest on Florida beaches only in the warm months.',
                'Florida oranges ripen in fall and winter.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · postcards from Maine', 'length': '30–40 s',
                    'script': 'Hi, it’s Dr. Reyes. It’s January, and my pond is busier than ever: ducks, robins, even a manatee in the spring run. But my friend Bea in Maine says her pond is frozen and quiet. Read her postcards. She thinks Florida doesn’t have seasons. Is she right? Let’s find out.'},
        'warmup': {'label': 'Warm-Up · two winters (Clue 1)', 'length': '20–30 s',
                   'script': 'Same month, two places. Look at each photo and ask yourself: would I see this in Florida in January, or in Maine? Here’s a hint: check whether the water is frozen or open.'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Say each word. Act out migration (flap and fly across the screen) and hibernation (curl up and snore).'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · turn the calendar (Clue 2)', 'length': '20–30 s',
                  'script': 'Let’s turn the calendar. Tap each season and see what my plants and animals do, here and in Maine. Who stays? Who leaves? Who sleeps? Keep an eye on the ducks and the robins.'},
        'part2': {'label': 'Part 2 · depending on each other', 'length': '25–35 s'},
        'figure': {'label': 'Figure · winter in Florida vs. up north', 'length': '15–20 s'},
        'part3': {'label': 'Part 3 · the manatee water test (Clue 3)', 'length': '20–30 s',
                  'script': 'Time for a real test. Change just one thing: the river temperature. Then run the morning and watch where the manatees go. Try a cold morning and a warm one, and read your test log.'},
        'explore': {'label': 'Part 4 · build the seasonal model (Clue 4)', 'length': '25–35 s',
                    'script': 'Now put it all together. Build a model of January in Florida and in Maine. Each circle needs a plant, an animal and the weather. Then draw the food-energy arrows, and don’t forget the migration arrow in between.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s',
                       'script': 'Do you have all four clues? Crack the case at the top of this tab. Why is my pond so busy when Bea’s is quiet? Then answer two questions, build your two-region model, and write your CER. Your answers save as you type.'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · a two-region seasonal model', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says Florida doesn’t really have seasons. It’s just summer all year. Hmm. Think about the manatees, the ducks and the sea turtles. Pick your side, tap two pieces of evidence in the planner, then explain how they prove your claim.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 15.01 (resources).',
                    'script': 'Case closed! Florida does have seasons, just milder ones. That’s why ducks and robins fly here for the winter. I’m mailing Bea a postcard right now. Next time, we look at the resources we all use, like water, sunlight and wind.'},
    },
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Both winters with all eight photos sorted (Warm-Up)',
        'January on the calendar (The Lesson)',
        'Your manatee test log (The Lesson)',
        'Your finished seasonal model (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['January in Florida and in Maine', 'A manatee in a warm spring', 'My two-region model'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 3,
                           'prompts': ['Draw two circles: Florida and your other region', 'Add a food-energy arrow in each', 'Add one arrow between them and label everything']}]},
    'hlCoach': copy.deepcopy(P['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '📮', 'name': 'Postcard from Maine',
                 'line': 'You cracked Case 14, part 2, and Bea’s postcard from Maine goes in your Field Notebook. (A specimen is something a scientist collects to study.) Next lesson: the resources we all use.'},
    'notebookTitle': P['notebookTitle'],
    'notebook': [dict(x) for x in Q['notebook']],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You’ll use every one of them today.',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'list', 'find': {'sel': '.fs-game[data-mod="twowinters"]'},
         'label': 'Warm-Up: how January in Florida is different from January in Maine', 'q': 'Warm-Up: Three ways January in Florida is different from January in Maine',
         'title': 'Your turn: list three ways January in Florida is different from January in Maine.', 'min': 3, 'unit': 'differences', 'addLabel': '+ Add a difference', 'ph': ['In Florida… but in Maine…', 'Another difference…', 'One more…']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'hide-nw', 'type': 'hide', 'find': {'sel': '.act-warmup .socratic-q', 'text': 'Notice'}},
        {'id': 'hide-tip', 'type': 'hide', 'find': {'sel': '.act-warmup .callout', 'text': 'Today'}},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Pick a season and one region besides Florida'},
         'label': 'Part C: A two-region seasonal model', 'q': 'Part C: Florida and one other region in the same season, with food energy and migration',
         'title': 'My two-region seasonal model',
         'fields': [{'t': 'My season and my other region', 'icon': '🗺️', 'ph': 'Winter in Florida and…'},
                    {'t': 'Florida: a plant, an animal and the weather', 'icon': '☀️', 'ph': 'In Florida there is…', 'long': True},
                    {'t': 'My other region: a plant, an animal and the weather', 'icon': '❄️', 'ph': 'In ___ there is…', 'long': True},
                    {'t': 'A food-energy arrow in each region', 'icon': '⚡', 'ph': '___ ➜ ___ in Florida, and ___ ➜ ___ in…', 'long': True},
                    {'t': 'How the two regions are connected', 'icon': '✈️', 'ph': 'The ___ migrates from ___ to ___ because…', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Does Florida have seasons?', 'ph': 'I disagree. Florida does have…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-1': 'Part B · Question 5', 'ans-2': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] in ('13.02', '14.01'): n['have'] = True
    if n['lesson'] == '14.02': n.update({'icon': '📮', 'name': 'Postcard from Maine'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'In winter, ducks fly south to Florida, where the water stays open.',
    'key': ['winter', 'ducks', 'fly', 'south', 'Florida', 'open'],
    'small': ['In', 'to', 'where', 'the'],
    'model': 'A scientist might highlight “winter”, “ducks”, “fly south” and “open”. Those words tell who, when and why. Small words like “the” and “to” don’t carry the idea.'}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
