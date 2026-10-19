#!/usr/bin/env python3
"""Writes data.json and fixes.json for 14.01 (run from this folder)."""
import json, copy
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../13-02/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

# ---------------------------------------------------------------- ticked fixes (Bethany, 18 Oct 2026)
fx('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist asks for a life-cycle drawing',
   '🎨 Part C &mdash; Build Your Own Food Chain', '🔄 Part C &mdash; A Florida Life Cycle')
fx('fix', 'copy-paste leftover: Part C task from 9.01 (typed on the page; the circle sketch is a bonus)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   "Pick one Florida plant or animal (not the monarch). List every stage of its life cycle in order, and tell what kind of life cycle it has.</p>", True)
fx('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'quarter label in the footer: week 14 is Quarter 2', 'Science &middot; Quarter 3 &middot;', 'Science &middot; Quarter 2 &middot;')
fx('fix', 'the generated figure’s grasshopper “nymph” has full wings and looks like the adult; the real photos in Side by side replace it',
   r'<div class="lesson-figure scroll-reveal">.*?<div class="lesson-figure-caption">.*?</div>\s*</div>\s*', '', True)
fx('fix', 'Q5 pointed to “the diagram”; the four organisms are now the Part 3 game',
   'Pick one of the four organisms from the diagram (monarch, grasshopper, sea turtle, or sunflower).',
   'Pick one of the four organisms from Part 3 (monarch, grasshopper, sea turtle, or sunflower).')

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; dash removed',
   "Hold this question in your head as you work. By the end of the lesson, you'll be able to look at a Florida plant or animal and predict what stages it goes through from birth to making the next generation.",
   "Keep this question in mind. By the end, you'll be able to look at a Florida plant or animal and tell what stages it goes through, from its start to making the next generation.")
fx('plain', 'answers are made on the page now (the game below); the stage list moves into the game',
   "A monarch butterfly goes through four very different stages between hatching and laying eggs of its own. In your notebook, write these four stages in the order you think they happen:</p>",
   "A monarch butterfly goes through four very different stages in its life. <strong>What comes next?</strong> Put its life back in order in the game below.</p>")
fx('cut', 'the four stage words now live in the game', r'\s*<ul style="font-size:16px;color:#2B1D12;line-height:1.7;margin:6px 0 10px 24px;">\s*<li><strong>caterpillar</strong></li>.*?</ul>', '', True)
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', 'shorter; dashes removed',
   "You've studied how plants and animals are built and how they sense the world. Today we step back and look at the whole picture: every organism goes through a ",
   "Today we look at the whole picture: every living thing goes through a ")
fx('plain', 'dashes removed', "It starts with the beginning — an egg, a seed, or a tiny baby — and ends with the same organism making ",
   "It starts with an egg, a seed or a tiny baby, and ends with that living thing making ")
fx('plain', 'one idea per sentence',
   "A sunflower seed grows into a stem, then a leafy plant, then a flowering plant, then makes new seeds. A monarch butterfly hatches from an egg, eats, changes its body, becomes a butterfly, and lays new eggs.",
   "A sunflower seed grows into a seedling, then a flowering plant that makes new seeds. A monarch hatches from an egg, eats, changes its body, and becomes a butterfly that lays new eggs.")
fx('plain', 'dash removed', "</span></span> — a Greek word that means \"change of shape.\"</p>", "</span></span>. It comes from a Greek word that means \"change of shape.\"</p>")
fx('plain', 'dash removed; defines pupa', "metamorphosis</strong> — four <span class=\"vtip\">stages", "metamorphosis</strong> has four <span class=\"vtip\">stages")
fx('plain', 'defines pupa', "<em>egg &rarr; larva &rarr; pupa &rarr; adult</em>.", "<em>egg &rarr; larva &rarr; pupa (a resting stage, like a chrysalis) &rarr; adult</em>.")
fx('plain', 'dash removed', "metamorphosis</strong> — three stages:", "metamorphosis</strong> has three stages:")
fx('plain', 'dash removed', "from the start — a Florida bear cub looks like a tiny bear", "from the start. A Florida bear cub looks like a tiny bear")
fx('plain', 'plain label; dashes removed',
   "<strong>Common misconception:</strong> Some people think \"metamorphosis\" means any kind of growing up. It really means a <em>big shape change</em> — like a caterpillar turning into a butterfly.",
   "<strong>Watch out:</strong> Some people think \"metamorphosis\" means any kind of growing up. It really means a <em>big change in body shape</em>, like a caterpillar turning into a butterfly.")
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')

# ---------------------------------------------------------------- lean cuts (the wrong-fact boxes go with them: the “liquid” chrysalis fact, the monarch-route callout, the 17-year cicada)
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean + wrong fact: remove the whole Explore tab (the comparison chart moves to Part 4 and Part C; the 17-year Florida cicada fact goes with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: the Key Concept box repeats Part 2', r'<div style="background:#FFF6E5;border:2.5px solid #F0C97A;[^"]*">\s*<div[^>]*>⭐ Key Concept</div>.*?</div>\s*', '', True)
fx('cut', 'lean: Stop & Reason pointed at the removed figure (Stop & Think in Part 1 stays)', r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: the diagram heading becomes Part 3 (Close the circle replaces the tap diagram)', 'margin-top:22px;">Four Florida Life Cycles</h3>', 'margin-top:22px;">Part 3 · Four Florida Life Cycles</h3>')
fx('cut', 'lean + wrong facts: Observe & Reason, the “turns into liquid” fact, the monarch-route callout and Go Deeper at the end of the Lesson; Part 4 = the old Explore; next button goes to Self-Check',
   r'<div class="socratic-q">\s*<span class="sq-icon">👀</span>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 4 · Alike and Different</h3>\n      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">Remember the empty shells on Dr. Reyes’s cattails? Scientists compare life cycles side by side. Pick two Florida living things and sort facts about their lives: which facts fit both, and which fit only one?</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 7 removed (Bethany kept 5 and 6)', r'<div class="pq">\s*<span class="pq-num"[^>]*>7</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C typed on the page; the circle sketch is a bonus',
   "A drawing of one Florida organism's life cycle, in a circle with arrows, every stage labeled, plus the metamorphosis type explained.",
   "One Florida organism's life cycle: every stage in order, plus its kind of life cycle explained. (A circle sketch is a bonus.)")
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether a caterpillar and butterfly are the same animal, and supported it with two pieces of evidence from the lesson.',
   '<strong>Use Your Evidence:</strong> My claim about whether a caterpillar and a butterfly are the same animal, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', True)

# ---------------------------------------------------------------- photo credits
CR = {
    'exuvia': 'Dragonfly exuvia (empty nymph skin) on a grass stem, gailhampshire, via Wikimedia Commons (CC BY 2.0)',
    'emerged': 'Eastern pondhawk just out of its nymph skin, ImagePerson, via Wikimedia Commons (CC BY 4.0)',
    'nymph': 'Emperor dragonfly nymph, George Elbogen, via Wikimedia Commons (CC BY 4.0)',
    'nymphW': 'Dragonfly nymph underwater, Totti, via Wikimedia Commons (CC BY-SA 4.0)',
    'dragonfly': 'Eastern pondhawk (male), Florida, D. Gordon E. Robertson, via Wikimedia Commons (CC BY-SA 3.0)',
    'megg': 'Monarch egg on a milkweed leaf, Lorie Shaull, via Wikimedia Commons (CC BY-SA 2.0)',
    'mcat': 'Monarch caterpillar, U.S. Fish and Wildlife Service, via Wikimedia Commons (public domain)',
    'mchrys': 'Monarch chrysalis, Shenandoah National Park (NPS), via Wikimedia Commons (public domain)',
    'mchrys2': 'Monarch chrysalis the day before the butterfly comes out, U.S. Fish and Wildlife Service, via Wikimedia Commons (public domain)',
    'madult': 'Monarch butterfly on milkweed, U.S. Fish and Wildlife Service, via Wikimedia Commons (public domain)',
    'lhatch': 'Just-hatched eastern lubber grasshopper nymphs, Everglades National Park, Judy Gallagher, via Wikimedia Commons (CC BY 2.0)',
    'lnymph': 'Eastern lubber grasshopper nymph, Lower Suwannee National Wildlife Refuge, Judy Gallagher, via Wikimedia Commons (CC BY 2.0)',
    'ladult': 'Adult eastern lubber grasshopper, Ryan Wood, via Wikimedia Commons (public domain)',
    'geggs': 'A grasshopper laying eggs in the soil, Kyu3a, via Wikimedia Commons (CC BY-SA 4.0)',
    'teggs': 'Loggerhead sea turtle eggs in a nest, U.S. Fish and Wildlife Service, via Wikimedia Commons (public domain)',
    'thatch': 'Loggerhead sea turtle hatchling, U.S. Fish and Wildlife Service, via Wikimedia Commons (public domain)',
    'tjuv': 'Young loggerhead sea turtle, NOAA, via Wikimedia Commons (public domain)',
    'tadult': 'Adult loggerhead sea turtle, NOAA National Marine Sanctuaries, via Wikimedia Commons (public domain)',
    'sseeds': 'Sunflower seeds, Kaldari, via Wikimedia Commons (public domain)',
    'sseedling': 'Sunflower seedling, Hildabast, via Wikimedia Commons (CC0)',
    'sflower': 'Sunflower in bloom, Wilfredor, via Wikimedia Commons (CC0)',
    'shead': 'Ripe sunflower head full of seeds, Alan Levine (cogdogblog), via Wikimedia Commons (CC BY 2.0)',
    'mayfly': 'Mayfly nymph, Ian Alexander, via Wikimedia Commons (CC BY-SA 4.0)',
    'tadpole': 'Tadpoles, Wing-Chi Poon, via Wikimedia Commons (CC BY-SA 3.0)',
    'snail': 'Marsh ramshorn snail (Planorbella trivolvis), via Wikimedia Commons (public domain)',
}
def cr(*keys): return '. '.join(CR[k] for k in keys) + '.'
I = lambda n: 'images/14-01-' + n + '.jpg'
MON = [{'id': 'egg', 't': 'Egg', 'img': I('monarch-egg'), 'alt': 'A tiny pale, ribbed monarch egg on a fuzzy milkweed leaf.'},
       {'id': 'cat', 't': 'Caterpillar (larva)', 'img': I('monarch-caterpillar'), 'alt': 'A monarch caterpillar with yellow, black and white stripes on a milkweed leaf.'},
       {'id': 'chr', 't': 'Chrysalis (pupa)', 'img': I('monarch-chrysalis'), 'alt': 'A smooth green monarch chrysalis with gold dots, hanging from a stem.'},
       {'id': 'adu', 't': 'Adult butterfly', 'img': I('monarch-adult'), 'alt': 'An orange and black monarch butterfly hanging from a milkweed leaf.'}]

D = {
    'lesson': '14.01', 'week': 14, 'day': 1, 'guide': 'lena', 'prefix': 'g4sci-14-1', 'manifestKey': '14-01',
    'paths': P['paths'], 'crew': P['crew'],
    'expedition': {'num': 14, 'title': 'Shells on the Cattails'},
    'ambient': {'icon': '🐸', 'label': 'Pond sounds'},
    'case': {
        'num': 14, 'title': 'Shells on the Cattails', 'style': 'jars',
        'hook': 'This week at the Field Station pond, I found dozens of little brown bug shapes hanging on the cattail stems. They don’t move at all. In the mud, my net caught something shaped a lot like them, but alive. And by the gate, a green case hangs under a milkweed leaf. A volunteer wrote on my jar: “Dead bugs?”',
        'question': 'Are the shells on the cattails dead bugs, and what is the green case on the milkweed?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'stills': [],
        'logs': [
            {'head': 'Jar 1 · cattail stems', 'img': I('exuvia'), 'alt': 'A brown, bug-shaped shell clinging to a green stem. It has six legs and a split down its back.',
             'rows': [['Found', 'on stems above the water'], ['Moving?', 'no'], ['Inside', 'empty! split down the back']], 'big': '23 shells'},
            {'head': 'Jar 2 · pond mud', 'img': I('nymph-water'), 'alt': 'A brown, bug-shaped animal with six legs crawling on the bottom of a pond.',
             'rows': [['Found', 'in the mud, underwater'], ['Moving?', 'yes, fast'], ['Wings?', 'none']], 'big': '4 alive'},
            {'head': 'Photo · milkweed by the gate', 'img': I('monarch-chrysalis'), 'alt': 'A smooth green case with gold dots hanging from a stem.',
             'rows': [['Found', 'hanging under a leaf'], ['Moving?', 'no'], ['Looks like', 'green with gold dots']], 'big': '1 case'}],
        'sticky': '“Dead bugs?” (a volunteer)',
        'stillsCredit': 'Jar 1: ' + CR['exuvia'] + '. Jar 2: ' + CR['nymphW'] + '. Milkweed: ' + CR['mchrys'] + '. The jars and the pond are part of the story.',
        'clues': [
            {'id': 'nextup', 'icon': '🦋', 'where': 'Warm-Up: what comes next?', 't': 'A chrysalis isn’t a dead caterpillar. It’s the pupa stage: inside, the caterpillar’s body is being rebuilt into a butterfly.'},
            {'id': 'morph', 'icon': '📅', 'where': 'The Lesson, Part 2: side by side', 't': 'A grasshopper nymph already looks like a small adult and grows by shedding its skin. A caterpillar looks nothing like its parent until after the chrysalis.'},
            {'id': 'wheel', 'icon': '🔄', 'where': 'The Lesson, Part 3: close the circle', 't': 'Monarchs have 4 stages (complete metamorphosis). Grasshoppers have 3 (incomplete). Sea turtles and sunflowers have no metamorphosis.'},
            {'id': 'venn', 'icon': '🧩', 'where': 'The Lesson, Part 4: alike and different', 't': 'A dragonfly nymph lives underwater. Then it climbs a stem and sheds its skin one last time. The empty skin stays behind, and there’s no pupa.'},
        ],
        'solve': {
            'title': 'What did Dr. Reyes find?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'They’re all dead bugs. Something killed the insects at the pond.', 'why': 'Check Clue 4. The shells were empty, split down the back. Where did the insects go?'},
                {'t': 'The shells are empty skins. Dragonfly nymphs climbed out of the water and shed their skin one last time to become adult dragonflies (incomplete: egg, nymph, adult). The green case is a monarch chrysalis (the pupa stage of complete metamorphosis), and a butterfly will come out.', 'right': True,
                 'why': 'Case cracked! Nothing died. Two insects, two kinds of metamorphosis. Now write your case report: it’s the questions below.'},
                {'t': 'The shells and the green case come from the same kind of insect at the same stage.', 'why': 'Check Clues 2 and 3. Does a dragonfly have a chrysalis stage like the monarch?'},
            ]},
    },
    'nextup': {
        'afterText': 'What comes next?', 'kicker': 'Warm-Up game', 'title': 'What comes next?',
        'todo': ['Look at the stage in the “Now” box.', 'Drag the stage that comes next into the empty box, or tap it.', 'Go all the way around, then answer the question.'],
        'why': {'icon': '🦋', 'q': 'What is a stage?', 't': 'A stage is one step in a life cycle. A monarch looks very different at each stage.'},
        'stages': MON,
        'whys': ['After about 4 days, a tiny caterpillar hatches. It eats its eggshell, then milkweed leaves.',
                 'After about two weeks of eating and growing, the caterpillar hangs upside down. Its skin splits and a green chrysalis is underneath.',
                 'About 10 days later, the chrysalis turns clear. An adult butterfly climbs out.',
                 'The adult lays eggs on milkweed, and the life cycle starts over.'],
        'q': 'Dr. Reyes’s chrysalis on the milkweed isn’t moving. What is happening inside?',
        'opts': [{'t': 'The caterpillar died inside.', 'miss': 'Look at your strip. What comes after the chrysalis?'},
                 {'t': 'It’s the pupa stage. The caterpillar is changing into a butterfly.', 'ok': True},
                 {'t': 'It’s a seed that will grow into milkweed.', 'miss': 'Look at the strip. Which animal made the chrysalis?'}],
        'credit': cr('megg', 'mcat', 'mchrys', 'madult'),
        'win': 'The circle is complete! Egg → caterpillar → chrysalis → butterfly → eggs again. A still chrysalis is alive and changing. That’s a clue.',
        'clue': 'nextup'},
    'morph': {
        'afterText': 'is just growth', 'kicker': 'Part 2 game', 'title': 'Side by side',
        'todo': ['Drag the slider to make the days go by.', 'Watch both young animals grow. Does each one look like its parent?', 'Stop at each day listed under the slider, then answer the question.'],
        'why': {'icon': '🦗', 'q': 'Meet the eastern lubber', 't': 'A big, slow Florida grasshopper. Its young are black with a yellow stripe. The adults are yellow and orange, with wings.'},
        'start': 'Hatching day', 'max': 60, 'checks': [10, 20, 58],
        'lanes': [
            {'name': '🦋 Monarch butterfly', 'parent': 'butterfly', 'frames': [
                {'d': 0, 'img': I('monarch-caterpillar'), 'alt': 'A monarch caterpillar on a milkweed leaf.', 'stage': 'Caterpillar (larva)', 'like': False, 'note': 'It eats milkweed and sheds its skin as it grows. It looks nothing like a butterfly.'},
                {'d': 14, 'img': I('monarch-chrysalis'), 'alt': 'A green monarch chrysalis.', 'stage': 'Chrysalis (pupa)', 'like': False, 'note': 'No eating, no walking. Inside, the body is being rebuilt.'},
                {'d': 24, 'img': I('monarch-adult'), 'alt': 'An adult monarch butterfly.', 'stage': 'Adult', 'like': True, 'note': 'A butterfly climbs out. Now it looks like its parents.'}]},
            {'name': '🦗 Eastern lubber grasshopper', 'parent': 'grasshopper', 'frames': [
                {'d': 0, 'img': I('lubber-hatchlings'), 'alt': 'Dozens of tiny black grasshopper nymphs on green leaves.', 'stage': 'Nymph (just hatched)', 'like': True, 'note': 'Tiny, black and no wings yet, but already shaped like a grasshopper.'},
                {'d': 20, 'img': I('lubber-nymph'), 'alt': 'A black lubber grasshopper nymph with a yellow stripe on a leaf.', 'stage': 'Nymph', 'like': True, 'note': 'Bigger now. It has shed its skin a few times to grow.'},
                {'d': 55, 'img': I('lubber-adult'), 'alt': 'A big yellow and orange adult lubber grasshopper.', 'stage': 'Adult', 'like': True, 'note': 'One last shed, and now it has wings. Same body shape, just bigger.'}]}],
        'q': 'On day 20, which young animal looks like a small version of its parent?',
        'opts': [{'t': 'The grasshopper nymph', 'ok': True},
                 {'t': 'The monarch chrysalis', 'miss': 'A green case with no legs or wings? Slide back to day 20 and look again.'},
                 {'t': 'Both of them', 'miss': 'Look at the check marks on day 20. Do both say “looks like a small adult”?'}],
        'credit': cr('mcat', 'mchrys', 'madult', 'lhatch', 'lnymph', 'ladult') + ' The days are rounded for this model.',
        'win': 'A nymph looks like a small adult and just grows (incomplete metamorphosis). A caterpillar changes completely inside a chrysalis (complete metamorphosis). That’s a clue.',
        'clue': 'morph'},
    'wheel': {
        'replace': '#tab-lesson .diagram-wrap', 'kicker': 'Part 3 game', 'title': 'Close the circle',
        'todo': ['Pick a living thing. Its first stage is already on the circle.', 'Drag the next stage onto the glowing spot, or tap the card and then the spot.', 'When the circle closes, pick what kind of life cycle it is. Do all four.'],
        'why': {'icon': '🔄', 'q': 'Why a circle?', 't': 'A life cycle has no end. The adult makes offspring, and the offspring start the cycle over.'},
        'kinds': [{'k': 'complete', 'icon': '🦋', 't': 'Complete metamorphosis (4 stages)'}, {'k': 'incomplete', 'icon': '🦗', 't': 'Incomplete metamorphosis (3 stages)'},
                  {'k': 'none', 'icon': '🐢', 't': 'No metamorphosis'}, {'k': 'plant', 'icon': '🌱', 't': 'A plant life cycle'}],
        'orgs': [
            {'id': 'monarch', 'name': 'Monarch butterfly', 'icon': '🦋', 'stages': [{'t': s['t'], 'img': s['img'], 'alt': s['alt']} for s in MON], 'kind': 'complete',
             'kindMiss': 'Count the stages. Is there a resting stage where the body changes completely?', 'why': 'Four very different stages, with a pupa (the chrysalis). The young looks nothing like the adult.'},
            {'id': 'grass', 'name': 'Grasshopper', 'icon': '🦗', 'stages': [
                {'t': 'Eggs in the soil', 'img': I('grasshopper-eggs'), 'alt': 'A grasshopper pushing the end of its body into the soil to lay eggs.'},
                {'t': 'Nymph', 'img': I('lubber-nymph'), 'alt': 'A black lubber grasshopper nymph with no wings.'},
                {'t': 'Adult', 'img': I('lubber-adult'), 'alt': 'An adult lubber grasshopper with wings.'}], 'kind': 'incomplete',
             'kindMiss': 'Count the stages. Does the nymph already look like a small adult?', 'why': 'Three stages and no pupa. The nymph looks like a small adult without wings.'},
            {'id': 'turtle', 'name': 'Loggerhead sea turtle', 'icon': '🐢', 'stages': [
                {'t': 'Eggs in the sand', 'img': I('turtle-eggs'), 'alt': 'Round white sea turtle eggs in a sandy nest.'},
                {'t': 'Hatchling', 'img': I('turtle-hatchling'), 'alt': 'A tiny dark loggerhead hatchling held in a gloved hand.'},
                {'t': 'Young turtle', 'img': I('turtle-juvenile'), 'alt': 'A young loggerhead sea turtle swimming.'},
                {'t': 'Adult', 'img': I('turtle-adult'), 'alt': 'A large adult loggerhead sea turtle swimming over a reef.'}], 'kind': 'none',
             'kindMiss': 'Does the hatchling change its body shape, or just grow bigger? And is a turtle an insect?', 'why': 'No metamorphosis. The hatchling is shaped like the adult and just grows. A loggerhead takes many years, often more than 20, to be ready to lay eggs.'},
            {'id': 'sunflower', 'name': 'Sunflower', 'icon': '🌻', 'stages': [
                {'t': 'Seed', 'img': I('sunflower-seeds'), 'alt': 'Two sunflower seeds, one striped and one pale.'},
                {'t': 'Seedling', 'img': I('sunflower-seedling'), 'alt': 'A small sunflower seedling with two round leaves in the soil.'},
                {'t': 'Flowering plant', 'img': I('sunflower-flower'), 'alt': 'A big yellow sunflower in bloom.'},
                {'t': 'Seed head', 'img': I('sunflower-head'), 'alt': 'A dried sunflower head full of seeds, held in a hand.'}], 'kind': 'plant',
             'kindMiss': 'Is a sunflower an animal?', 'why': 'Plants don’t have metamorphosis, but they have stages too. The flower makes seeds, and the seeds start the cycle again.'}],
        'credit': cr('megg', 'mcat', 'mchrys', 'madult', 'geggs', 'lnymph', 'ladult', 'teggs', 'thatch', 'tjuv', 'tadult', 'sseeds', 'sseedling', 'sflower', 'shead'),
        'win': 'Four circles closed! Every life cycle starts over when adults make offspring. Some animals change shape (metamorphosis). Others just grow. That’s a clue.',
        'clue': 'wheel'},
    'venn': {
        'afterText': 'which facts fit both, and which fit only one', 'kicker': 'Part 4 game', 'title': 'Alike and different',
        'todo': ['Pick a pair to compare.', 'Drag each fact to “Only …”, “Both” or the other “Only …”, or tap the fact and then the box.', 'Sort every fact, then answer the question.'],
        'why': {'icon': '🧩', 'q': 'Why compare?', 't': 'Putting two life cycles side by side shows what all life cycles share, and what makes each one different.'},
        'pairs': [
            {'id': 'md', 'a': {'name': 'Monarch', 'img': I('monarch-adult'), 'alt': 'A monarch butterfly.'}, 'b': {'name': 'Dragonfly', 'img': I('dragonfly'), 'alt': 'A blue eastern pondhawk dragonfly.'},
             'cards': [{'t': 'Starts life as a tiny egg', 'z': 'both', 'miss': 'Do both insects start as eggs?'},
                       {'t': 'Grows by shedding its skin (molting)', 'z': 'both', 'miss': 'Caterpillars shed their skin too. Is this true for both?'},
                       {'t': 'Has a pupa stage (the chrysalis)', 'z': 'a', 'miss': 'Which one makes a chrysalis?'},
                       {'t': 'Its young (caterpillars) eat milkweed leaves', 'z': 'a', 'miss': 'Which insect’s young are called caterpillars?'},
                       {'t': 'Its young (nymphs) live underwater', 'z': 'b', 'miss': 'Think of Jar 2 from the pond mud.'},
                       {'t': 'Leaves an empty skin on a stem when it becomes an adult', 'z': 'b', 'miss': 'Think of Jar 1 from the cattail stems.'}],
             'q': 'Which fact explains the shells on Dr. Reyes’s cattails?',
             'opts': [{'t': 'Leaves an empty skin on a stem when it becomes an adult', 'ok': True},
                      {'t': 'Has a pupa stage (the chrysalis)', 'miss': 'That’s the monarch. Which insect climbs out of the water?'},
                      {'t': 'Starts life as a tiny egg', 'miss': 'True for both, but does it explain empty shells?'}],
             'done': 'Dragonflies go egg → nymph → adult (incomplete metamorphosis). Monarchs go egg → caterpillar → chrysalis → adult (complete).'},
            {'id': 'dt', 'a': {'name': 'Dragonfly', 'img': I('dragonfly-emerged'), 'alt': 'A green dragonfly that just climbed out of its brown nymph skin.'}, 'b': {'name': 'Sea turtle', 'img': I('turtle-hatchling'), 'alt': 'A loggerhead hatchling.'},
             'cards': [{'t': 'Starts life as an egg', 'z': 'both', 'miss': 'Do both of them hatch from eggs?'},
                       {'t': 'Adults make offspring, so the cycle starts over', 'z': 'both', 'miss': 'Is this true for every life cycle?'},
                       {'t': 'Changes body shape as it grows up (metamorphosis)', 'z': 'a', 'miss': 'Which one gets wings at the end?'},
                       {'t': 'Gets wings as an adult', 'z': 'a', 'miss': 'Which one can fly?'},
                       {'t': 'Its hatchlings are shaped like small adults', 'z': 'b', 'miss': 'Which baby already has a shell and flippers?'},
                       {'t': 'Lays its eggs in the sand on a beach', 'z': 'b', 'miss': 'Which one digs a nest on the beach?'}],
             'q': 'Which one goes through metamorphosis?',
             'opts': [{'t': 'The dragonfly', 'ok': True},
                      {'t': 'The sea turtle', 'miss': 'Does a hatchling change its body shape, or just grow?'},
                      {'t': 'Both of them', 'miss': 'Look at the “Only” boxes. Which one changes shape?'}],
             'done': 'Dragonflies change shape (incomplete metamorphosis). Sea turtles just grow bigger (no metamorphosis).'}],
        'credit': cr('madult', 'dragonfly', 'emerged', 'thatch'),
        'win': 'You compared life cycles like a scientist! A dragonfly nymph climbs out of the water and leaves its last skin behind. That’s your last clue.',
        'clue': 'venn'},
    'exploreMod': 'venn',
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Does a caterpillar come before the egg?', 'C': 'Every life cycle starts with the new generation. What does a monarch start as?'},
        'q2': {'B': 'Count again: which kind has four stages?', 'C': 'Do grasshoppers start as eggs too?'},
        'q3': {'A': 'Both are native Florida animals. Think about body shape.', 'B': 'Age doesn’t explain it. Does a bear cub ever change its body shape?'}},
    'flags': {
        'ans-1': [
            {'label': 'one organism', 're': 'monarch|butterfl|grasshop|turtle|sunflower'},
            {'label': 'its stages in order', 'any': ['egg', 'larva|caterpill', 'pupa|chrysal', 'adult', 'nymph', 'hatchling|baby', 'juvenile|young', 'seed', 'seedling|sprout', 'flower|bloom'], 'min': 3},
            {'label': 'the kind of metamorphosis', 're': 'complete|incomplete|no metamorph|not.{0,20}metamorph|doesn.?t.{0,20}metamorph|no change|plant'}],
        'ans-2': [
            {'label': 'complete', 're': 'complete|4|four|pupa|chrysal|cocoon'},
            {'label': 'incomplete', 're': 'incomplete|3|three|nymph|no pupa'},
            {'label': 'a Florida example of each', 'any': ['monarch|butterfl', 'bee', 'beetle', 'grasshop|lubber', 'dragonfl', 'cockroach|roach', 'mosquito', 'moth', 'cricket'], 'min': 2}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|same|wrong|right|true|not'},
            {'label': 'two pieces of evidence', 'any': ['chrysal|pupa', 'egg', 'stage', 'metamorph', 'complete', 'caterpill|larva', 'change|shape', 'same animal|same insect', 'body', 'rebuil|transform', 'lays?\\b'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves'}]},
    'minWords': {'ans-1': 15, 'ans-2': 20, 'cer-4': 30},
    'hints': {
        'ans-1': ['Pick the one you remember best from Close the circle.', 'Write the stages in order with arrows, like: egg → … → adult.', 'Try: A ___ goes ___ → ___ → ___. It has ___ metamorphosis.'],
        'ans-2': ['Complete = 4 stages with a pupa. Incomplete = 3 stages, no pupa.', 'Think of the monarch and the grasshopper in Side by side.', 'Try: Complete metamorphosis has ___, like a ___. Incomplete has ___, like a ___.'],
        'cer-4': ['First decide: is a caterpillar the same animal as the butterfly?', 'Think of What comes next? and the chrysalis on the milkweed.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'A monarch’s egg hatches into a caterpillar, and the caterpillar becomes the butterfly.',
                'Inside the chrysalis, the caterpillar’s body is rebuilt into a butterfly.',
                'Complete metamorphosis means one animal changes its body shape through four stages.',
                'The butterfly lays eggs that hatch into caterpillars again.',
                'A grasshopper nymph looks like its parent, but a caterpillar doesn’t.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · shells on the cattails', 'length': '30–40 s',
                    'script': 'Hi, it’s Dr. Reyes, down at the Field Station pond. Look at the jars in the case file. Dozens of little brown shells on the cattails, and none of them move. In the mud, something shaped just like them, but alive. And a green case on the milkweed. A volunteer thinks they’re dead bugs. Are they? Let’s find out.'},
        'warmup': {'label': 'Warm-Up · what comes next? (Clue 1)', 'length': '20–30 s',
                   'script': 'Here’s my favorite insect to watch grow up: the monarch. Look at the stage in the Now box, then find the one that comes next. Keep going all the way around. Here’s a hint: the circle never really ends.'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Say each word. Act out metamorphosis: curl up small, then open your arms like wings.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · every living thing has a life cycle', 'length': '20–30 s'},
        'part2': {'label': 'Part 2 · side by side (Clue 2)', 'length': '25–35 s',
                  'script': 'Two babies hatched on the same day: a monarch caterpillar and a lubber grasshopper. Drag the slider and watch them grow up side by side. Stop at each day listed under the slider. Which baby already looks like its mom and dad? Which one looks like a totally different animal?'},
        'part3': {'label': 'Part 3 · close the circle (Clue 3)', 'length': '20–30 s',
                  'script': 'Every life cycle is a circle. I put the first stage on for you. Drag the next one onto the glowing spot, and keep going until the circle closes. Then decide what kind of life cycle it is. Count the stages. That’s a big hint.'},
        'explore': {'label': 'Part 4 · alike and different (Clue 4)', 'length': '25–35 s',
                    'script': 'Scientists compare. Pick a pair, then sort each fact: true for only one of them, or true for both? When you finish the monarch and the dragonfly, look closely at the dragonfly’s side. It might explain those shells on my cattails.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s',
                       'script': 'Do you have all four clues? Crack the case at the top of this tab: are my shells dead bugs, and what is that green case? Then answer two questions, write one Florida life cycle, and write your CER. Your answers save as you type.'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · a Florida life cycle', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says a caterpillar and a butterfly are completely different animals. They don’t even look alike! Hmm. Think about the chrysalis on my milkweed. Pick your side, tap two pieces of evidence in the planner, then explain how they prove your claim.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 14.02 (seasons and migration).',
                    'script': 'Case closed! My shells weren’t dead bugs. They were dragonfly skins, and the green case was a monarch chrysalis. Next time, winter is coming to the pond. Where do the dragonflies and the monarchs go? We’ll find out.'},
    },
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Your full monarch strip with the circle closed (Warm-Up)',
        'Day 20 in Side by side (The Lesson)',
        'A life-cycle circle you closed (The Lesson)',
        'The answer that cracked the case (Assignment)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['A monarch life cycle in a circle', 'A dragonfly coming out of its skin', 'My Florida life cycle'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 3,
                           'prompts': ['Draw your organism’s stages in a circle', 'Add arrows from stage to stage', 'Label every stage']}]},
    'hlCoach': copy.deepcopy(P['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🫙', 'name': 'Dragonfly shell in a jar',
                 'line': 'You cracked Case 14, and one of the empty dragonfly shells from the cattails goes in your Field Notebook. (A specimen is something a scientist collects to study.) Next lesson: winter comes to the pond.'},
    'notebookTitle': P['notebookTitle'],
    'notebook': [dict(x) for x in Q['notebook']],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You’ll use every one of them today.',
    'tool': {
        'name': 'Dip net', 'icon': '🥅', 'tab': 'assignment', 'after': '#tab-assignment .activity-card', 'key': '14-tool', 'sim': 'dipnet',
        'kicker': 'Bonus · Tool of the Week',
        'teaser': 'Sweep a Florida pond with a dip net, look at your catch, and meet the young animals that live underwater.',
        'done': 'You swept three spots, met every animal in your tray, and put them back in the pond. A dip net sticker is in your Field Notebook.',
        'why': {'icon': '🥅', 'q': 'What is a dip net?', 't': 'A net on a long pole that scientists sweep through ponds and streams to catch small water animals, look at them, and let them go.'},
        'dipnet': {
            'title': 'What lives in Dr. Reyes’s pond?',
            'todo': ['Tap each part of the dip net to learn it.', 'Pick a spot, then press Sweep the net. Try all three spots.', 'Tap every animal in the tray, then answer the question.'],
            'parts': [{'label': 'The D-shaped frame', 't': 'The flat side sits on the pond bottom, so animals can’t escape underneath.'},
                      {'label': 'The fine mesh bag', 't': 'Tiny holes let the water drain out but keep small animals in.'},
                      {'label': 'The long pole', 't': 'Lets you reach into the water from the bank without stepping in.'}],
            'spots': [{'k': 'reeds', 'name': 'Cattails and reeds', 'icon': '🌾', 'where': 'Sweeping along the cattail stems', 'catch': ['dnymph', 'tadpole']},
                      {'k': 'open', 'name': 'Open water', 'icon': '💧', 'where': 'Sweeping through the open water', 'catch': ['mayfly']},
                      {'k': 'mud', 'name': 'Muddy bottom', 'icon': '🟫', 'where': 'Scooping the muddy bottom', 'catch': ['dnymph', 'snail']}],
            'critters': {
                'dnymph': {'name': 'Dragonfly nymph', 'img': I('dragonfly-nymph'), 'alt': 'A brown dragonfly nymph with six legs and no wings.', 'stage': 'young (nymph)',
                           'note': 'It lives underwater and grabs food with a jaw that shoots out. One day it will climb a cattail, shed its skin one last time, and fly away as a dragonfly.'},
                'mayfly': {'name': 'Mayfly nymph', 'img': I('pond-mayfly'), 'alt': 'A thin mayfly nymph with feathery gills along its sides and three tails.', 'stage': 'young (nymph)',
                           'note': 'Feathery gills on its sides help it breathe underwater. Mayflies go through incomplete metamorphosis too.'},
                'tadpole': {'name': 'Tadpole', 'img': I('pond-tadpole'), 'alt': 'Two brown tadpoles with round bodies and long tails.', 'stage': 'young (tadpole)',
                            'note': 'A young frog. Frogs change shape too: the tadpole grows legs and loses its tail. But frogs aren’t insects.'},
                'snail': {'name': 'Ramshorn snail', 'img': I('pond-snail'), 'alt': 'Two ramshorn snails with flat, coiled shells on a plant stem.', 'stage': 'adult',
                          'note': 'Baby ramshorn snails hatch from eggs already shaped like tiny snails. No metamorphosis: they just grow.'}},
            'credit': cr('nymph', 'mayfly', 'tadpole', 'snail'),
            'q': {'q': 'Which animal from your tray will one day leave an empty shell on a cattail?', 'opts': [
                {'t': 'The dragonfly nymph', 'ok': True, 'why': 'Yes! It climbs out of the water, and the adult crawls out of its old skin. Now gently pour the tray back into the pond.'},
                {'t': 'The ramshorn snail', 'why': 'Snails don’t climb out and shed their skin. Which animal becomes a flying insect?'},
                {'t': 'The tadpole', 'why': 'A tadpole becomes a frog, not a shell on a cattail. Which one becomes a dragonfly?'}]}}},
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'list', 'find': {'sel': '.fs-game[data-mod="nextup"]'},
         'label': 'Warm-Up: what changes from caterpillar to butterfly', 'q': 'Warm-Up: Three things that change from caterpillar to butterfly',
         'title': 'Your turn: list three things that change from caterpillar to butterfly.', 'min': 3, 'unit': 'changes', 'addLabel': '+ Add a change', 'ph': ['The caterpillar has… but the butterfly has…', 'Another change…', 'One more…']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'hide-nw', 'type': 'hide', 'find': {'sel': '.act-warmup .socratic-q', 'text': 'Notice'}},
        {'id': 'hide-tip', 'type': 'hide', 'find': {'sel': '.act-warmup .callout', 'text': 'Today'}},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Pick one Florida plant or animal (not the monarch)'},
         'label': 'Part C: A Florida life cycle', 'q': 'Part C: One Florida organism’s life cycle: its stages in order and its kind of life cycle',
         'title': 'My Florida life cycle',
         'fields': [{'t': 'My Florida plant or animal', 'icon': '🌿', 'ph': 'I picked…'},
                    {'t': 'Its stages, in order', 'icon': '🔄', 'ph': '___ → ___ → ___ → back to ___', 'long': True},
                    {'t': 'What kind of life cycle it has', 'icon': '🦋', 'ph': 'complete, incomplete, no metamorphosis, or a plant life cycle', 'long': True},
                    {'t': 'How I can tell', 'icon': '🔎', 'ph': 'I can tell because the young…', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Are a caterpillar and a butterfly different animals?', 'ph': 'I disagree. A caterpillar and a butterfly are…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-1': 'Part B · Question 5', 'ans-2': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] in ('13.01', '13.02'): n['have'] = True
    if n['lesson'] == '14.01': n.update({'icon': '🫙', 'name': 'Dragonfly shell in a jar'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'A dragonfly nymph climbs out of the pond and sheds its skin one last time.',
    'key': ['dragonfly', 'nymph', 'climbs', 'sheds', 'skin'],
    'small': ['A', 'out', 'of', 'the', 'and', 'its', 'one'],
    'model': 'A scientist might highlight “dragonfly nymph”, “sheds” and “skin”. Those words tell who and what happens. Small words like “the” and “of” don’t carry the idea.'}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
