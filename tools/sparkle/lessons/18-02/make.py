#!/usr/bin/env python3
"""Writes data.json and fixes.json for 18.02 (run from this folder). Showcase lesson: Case 18 part 2 "The Star Party Wish List".
Sam Park (Unit 5). New modules: racelight, openwide, skyhunt, tv (Hubble launch on TV, news voice), deepfield, permit
(+ a real NASA Florida-at-night map and a satellite P.S.), case.wishes (kids' crayon wish cards). No Tool of the Week (18.01 has the hand lens)."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../18-01/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

# ---------------------------------------------------------------- ticked fixes (Bethany, 22 Oct 2026)
fx('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist already asks for a three-view sky sketch',
   '🎨 Part C &mdash; Build Your Own Food Chain', '🔭 Part C &mdash; Three Views of One Far-Away Thing')
fx('fix', 'copy-paste leftover: Part C task from 9.01 (typed on the page now; a sketch is a bonus)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   "Pick one far-away thing in the sky: the Moon, a planet, a star or a galaxy. Tell what you’d see with your eyes, with binoculars and with a backyard telescope. Then pick the best tool for it.</p>", True)
fx('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'unit label: “Ecosystems & Energy” is a leftover; weeks 18–24 are Unit 5', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Energy, Motion &amp; Collisions</div>')
fx('fix', 'a tools lesson is Nature of Science, not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Nature of Science</div>')
fx('fix', 'the misconception box said “the bigger part is just the side effect of zooming in”, which is muddled: a telescope gathers light AND magnifies',
   r'<p><strong>Common misconception:</strong> Some people think a telescope makes things look bigger like a microscope does\..*?</p>',
   '<p><strong>Watch out:</strong> Some people think a telescope just makes things look bigger. It does two jobs. It gathers much more light than your eye, so dim things show up. And it magnifies them (makes them look bigger).</p>', True)
fx('fix', 'space telescopes can be turned to point anywhere; “can’t be moved” is wrong',
   "Space telescopes cost billions of dollars and can't be moved.", "Space telescopes cost billions of dollars and are very hard to fix once they’re up there.")
fx('fix', 'the misleading AI picture (Saturn, the Moon and a bright spiral galaxy in one 200x view) and the boxes that lean on it are gone; Find it in the sky replaces them and the tap diagram',
   r'<div class="lesson-figure scroll-reveal">\s*<div class="lesson-figure-label">🔭 Same Night Sky, Three Views</div>.*?<h3[^>]*>Pick the Right Telescope</h3>\s*<p>.*?</p>',
   H3 + 'Find It in the Sky</h3>\n      <p>Sam set up two tools on the beach: binoculars and a backyard telescope. Which one shows each kid’s wish best?</p>', True)
fx('fix', 'Part B question 5 pointed at “the diagram”, which Find it in the sky replaced (same question, same objects)',
   'Pick ONE of the four objects from the diagram (Moon, Saturn, far stars, or galaxies).', 'Pick ONE of these from the lesson: the Moon, Saturn, far stars or galaxies.')
fx('fix', 'Part B question 5 label (Gathered Answers) matches the question', 'data-label="Pick ONE of the four objects from the diagram (Moo..."', 'data-label="Pick ONE of these from the lesson: the Moon, Satu..."')

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; plain words; no dash',
   "Hold this question in your head as you work. By the end of the lesson, you'll be able to name which tool a scientist would use to see different far-away things — and explain how telescopes collect light to reveal what your eyes alone can't.",
   "Keep this question in mind. By the end, you’ll know which tool to use for things far away, and how a telescope helps your eyes.")
fx('plain', 'the warm-up is Race the light now (Bethany’s hook: “the starlight you see tonight is older than you”); answers are made on the page',
   r"<p>The next clear Florida night, look up at the sky.*?</p>\s*<p>Now think: what big things in space.*?</p>",
   "<p>Here’s a surprising claim: the starlight you see tonight is older than you are. True or false? Let’s race the light and find out.</p>", True)
fx('plain', 'warm-up subtitle matches the new warm-up', 'What can you see in the night sky?', 'How old is the light you see?')
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', 'no dash; shorter', "The more light it collects, the more detail you can see — even if the thing itself is thousands of miles, or millions of light-years, away.",
   "The more light it collects, the more you can see, even if the thing is millions of miles away.")
fx('plain', 'plain words', 'Instead of making things look bigger from a few inches away, a telescope COLLECTS light from far away and focuses it.',
   'A telescope COLLECTS light from far away and focuses it.')
fx('plain', 'plain words', 'Portable and easy to hold.', 'Easy to carry.')
fx('plain', 'define atmosphere in place', "Sits in space ABOVE Earth's atmosphere so air can't blur the view.", "Sits in space, ABOVE Earth’s atmosphere (the air around Earth), so air can’t blur the view.")
fx('plain', 'shorter', 'Scientists pick tools based on <em>how far away</em> the object is and how much detail they want:', 'Scientists pick a tool by <em>how far away</em> something is and how much detail they need:')
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'shorter closing; points to week 19',
   r'<p><strong>Nicely done\.</strong> You can now pick the right tool.*?</p>',
   '<p><strong>Nicely done.</strong> You picked the right tool for every wish, from the Moon to the farthest galaxies. Next week, Sam’s tools get a new job: how does energy make things move?</p>', True)

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: Stop & Think (Open wider is the thinking stop for Part 1)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its three-view page becomes Part C; its “one object, three tools” idea becomes Part 4)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: Observe & Reason, the Amazing Fact (Sirius’s 8.6 years is in Race the light), the Florida connection (wrong about Webb, which launched from French Guiana; Hubble’s Florida launch is the TV report) and Go Deeper; Part 3 = the TV report, Part 4 = Stare at nothing; next button goes to Self-Check',
   r'<div class="socratic-q">\s*<span class="sq-icon">👀</span>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 3 · A Telescope Above the Air</h3>\n      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">Sam found an old TV news report from Florida. It shows how one famous telescope got above the air.</p>\n' +
   '      ' + H3 + 'Part 4 · Stare at Nothing</h3>\n      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">Jordan wants the farthest thing anyone has ever seen. Scientists found it by aiming a giant telescope at a tiny patch of sky that looked empty.</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 6 removed (Bethany kept 5 and 7)', r'<div class="pq">\s*<span class="pq-num"[^>]*>6</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: renumber Part B (7 → 6)', '<span class="pq-num" style="background:#D4772C;">7</span>', '<span class="pq-num" style="background:#D4772C;">6</span>')
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C typed on the page; the sketch is a bonus',
   'A three-tool sky sketch (eye, binoculars, backyard telescope) of one distant object, with labeled details in each circle plus a tool-choice sentence.',
   'Three views of one far-away thing (eyes, binoculars, backyard telescope), plus the best tool for it. (A sketch is a bonus.)')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether we still need space telescopes, and supported it with two pieces of evidence from the lesson.',
   '<strong>Use Your Evidence:</strong> My claim about whether we still need space telescopes, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', True)

# ---------------------------------------------------------------- the story
I = lambda n: 'images/18-02-' + n + '.jpg'
SAM = Q['crew']['sam']
C = {
    'moon': 'Full Moon: NASA Goddard / Lunar Reconnaissance Orbiter (public domain)',
    'sun': 'The Sun: NASA Solar Dynamics Observatory (public domain)',
    'sirius': 'Sirius (the bright star) and its tiny partner star: NASA, ESA, H. Bond and M. Barstow, Hubble Space Telescope (public domain)',
    'andromeda': 'The Andromeda Galaxy: Andy Weeks (CC0, no rights reserved)',
    'pleiades': 'The Seven Sisters star cluster (Pleiades): NASA, ESA, AURA/Caltech, Palomar Observatory (public domain)',
    'saturn': 'Saturn: NASA / Hubble Space Telescope, 2018 (public domain)',
    'jupiter': 'Jupiter: NASA, ESA and the Hubble Heritage Team (public domain)',
    'owl': 'Barred owl: Mara Koenig / U.S. Fish and Wildlife Service (public domain)',
    'scope': 'Backyard (Dobsonian) telescope: James Stewart (public domain)',
    'deep': 'Webb’s First Deep Field: NASA, ESA, CSA and STScI (public domain)',
    'launch': 'Discovery lifts off with Hubble, April 24, 1990: NASA (public domain)',
    'liftoff': 'STS-31 liftoff: NASA (public domain)',
    'hubble': 'Hubble in orbit, 2009: NASA, STS-125 crew (public domain)',
    'flnight': 'Florida at night from the International Space Station, Oct. 13, 2014: NASA Johnson Space Center (public domain)',
    'modis': 'Florida’s coast from NASA’s Terra satellite (MODIS), Feb. 14, 2023: NASA (public domain)',
}
ALL = ' All via Wikimedia Commons. Palmetto Beach, the kids and the star party are made up for this lesson.'
def cr(*ks): return '. '.join(C[k] for k in ks) + '.' + ALL

D = {
    'lesson': '18.02', 'week': 18, 'day': 2, 'guide': 'sam', 'prefix': 'g4sci-18-2', 'manifestKey': '18-02',
    'paths': P['paths'], 'crew': {'sam': SAM},
    'expedition': {'num': 18, 'title': 'The Star Party Wish List'},
    'ambient': {'icon': '🌊', 'label': 'Ocean sounds'},
    'case': {
        'num': 18, 'title': 'The Star Party Wish List', 'style': 'party',
        'hook': 'Great news: the red tide is gone! To celebrate, Palmetto Beach is having a star party (a night of looking at the sky together). Four kids sent me wishes, but the town can rent just ONE tool.',
        'notice': {'head': 'Palmetto Beach · Star Party Night', 'title': 'Saturday, 8 PM, on the beach',
                   'rows': [['Budget', 'The town can rent ONE tool.'], ['Sam’s job', 'Pick what to bring so every kid gets their wish.']],
                   'line': ''},
        'wishes': [
            {'icon': '🌕', 't': 'I want to see the craters on the Moon!', 'who': 'MAYA, age 9'},
            {'icon': '🪐', 't': 'Saturn’s rings, PLEASE!!', 'who': 'LEO, age 10'},
            {'icon': '✨', 't': 'The Seven Sisters stars my grandma told me about.', 'who': 'AVA, age 9'},
            {'icon': '🚀', 't': 'The FARTHEST thing anybody has ever seen.', 'who': 'JORDAN, age 10'}],
        'stills': [],
        'question': 'What should Sam bring so every wish comes true?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'racelight', 'icon': '✨', 'where': 'Warm-Up: race the light', 't': 'Things in space are so far away that their light is old. Andromeda’s light left it 2.5 million years ago.'},
            {'id': 'openwide', 'icon': '⭕', 'where': 'The Lesson, Part 1: open wider', 't': 'Far things look dim. A bigger opening gathers more light. Zooming in alone doesn’t help.'},
            {'id': 'skyhunt', 'icon': '🔭', 'where': 'The Lesson, Part 2: find it in the sky', 't': 'A backyard telescope shows Moon craters and Saturn’s rings. Binoculars fit the wide Seven Sisters.'},
            {'id': 'deepfield', 'icon': '🌌', 'where': 'The Lesson, Part 4: stare at nothing', 't': 'The farthest things need a space telescope. Webb stared at one “empty” speck for 12.5 hours and found thousands of galaxies.'},
        ],
        'solve': {
            'title': 'What should Sam bring?', 'q': 'Which plan fits all four clues?',
            'options': [
                {'t': 'Rent a space telescope for the beach, so every wish comes true.', 'why': 'Check Clue 4. Where do space telescopes work? Could anyone bring one to a beach?'},
                {'t': 'Just bring binoculars. They are easy to carry and show everything.', 'why': 'Check Clue 3. Can binoculars show Saturn’s rings?'},
                {'t': 'Rent a backyard telescope for the Moon and Saturn. Bring binoculars for the Seven Sisters. Show Webb’s picture for the farthest thing.', 'right': True,
                 'why': 'Case cracked! The right tool for each wish. Now fill in Sam’s star party permit, just below.'},
            ]},
    },
    'racelight': {
        'afterText': 'Let’s race the light and find out', 'kicker': 'Warm-Up game', 'title': 'Race the light',
        'todo': ['Guess first: drag each picture onto when you think its light left (or tap a card, then a spot).', 'Press Send the light. Watch each light race to you.'],
        'why': {'icon': '💡', 'q': 'Why can light be “old”?', 't': 'Light is the fastest thing there is, but space is huge. Light from far away has traveled a long time.'},
        'trayLabel': 'Drag each one onto your guess:',
        'marks': [{'k': 's', 't': 'about 1 second ago'}, {'k': 'm', 't': 'about 8 minutes ago'}, {'k': 'y', 't': 'about 9 years ago'}, {'k': 'my', 't': '2.5 MILLION years ago'}],
        'objs': [
            {'id': 'moon', 'name': 'The Moon', 'img': I('moon'), 'alt': 'The full Moon, gray with dark patches', 'mark': 's', 'left': 'Left about 1 second ago', 'dist': 'about 240,000 miles away'},
            {'id': 'sun', 'name': 'The Sun', 'img': I('sun'), 'alt': 'The Sun, glowing orange', 'mark': 'm', 'left': 'Left about 8 minutes ago', 'dist': 'about 93 million miles away'},
            {'id': 'sirius', 'name': 'Sirius, a bright star', 'img': I('sirius'), 'alt': 'The bright star Sirius, a white glow with light spikes', 'mark': 'y', 'left': 'Left about 9 years ago', 'dist': 'about 8.6 light-years away'},
            {'id': 'andromeda', 'name': 'The Andromeda Galaxy', 'img': I('andromeda'), 'alt': 'The Andromeda Galaxy, a huge glowing oval of stars', 'mark': 'my', 'left': 'Left 2.5 million years ago', 'dist': 'about 2.5 million light-years away'}],
        'sendBtn': 'Send the light', 'earth': '🌎 Your eyes',
        'q': 'Which light has been traveling the longest to reach you?',
        'opts': [{'t': 'The Sun’s light', 'miss': 'Look at your stamps. 8 minutes is not very long. Which one says millions?'},
                 {'t': 'The Moon’s light', 'miss': 'The Moon is the closest. Its light takes about 1 second.'},
                 {'t': 'Andromeda’s light', 'ok': True}],
        'credit': cr('moon', 'sun', 'sirius', 'andromeda'),
        'win': 'True! Starlight is old. The farther away something is, the longer its light travels, and the dimmer it looks. That’s a clue.',
        'clue': 'racelight'},
    'openwide': {
        'afterText': 'COLLECTS light from far away and focuses it', 'kicker': 'Part 1 game', 'title': 'Open wider',
        'todo': ['This is a model of the sky over Palmetto Beach. Drag the gold dot outward to open the light opening wider (or press Open wider).', 'Watch the star count. Then press Zoom only and compare.'],
        'why': {'icon': '⭕', 'q': 'Why does the opening matter?', 't': 'Light gets into your eye through the pupil (the dark circle). A bigger opening catches more light, like a bigger bucket catches more rain.'},
        'stops': [
            {'k': 'eye', 'icon': '👁️', 'name': 'Your eye', 'size': 'opening: about 7 mm (in the dark)', 'r': 0, 'limit': 0.3, 'gain': 'Your eye', 'note': 'In the dark, your pupil opens to about 7 mm. Only the brightest stars send enough light.'},
            {'k': 'owl', 'icon': '🦉', 'name': 'A barred owl', 'img': I('owl'), 'alt': 'A barred owl with big, dark eyes', 'size': 'big eyes, wide-open pupils', 'r': 22, 'limit': 0.4, 'gain': 'An owl gathers more light', 'note': 'Owls have huge eyes that let in more light, so they can hunt at night.'},
            {'k': 'bino', 'icon': '🔭', 'name': 'Binoculars', 'size': 'opening: 50 mm', 'r': 55, 'limit': 0.62, 'gain': 'About 50 times more light than your eye', 'note': 'Each lens is about 50 mm wide. Many more stars pop out.'},
            {'k': 'scope', 'icon': '🪞', 'name': 'Backyard telescope', 'img': I('telescope'), 'alt': 'A white backyard telescope on the grass, pointed at the sky', 'size': 'mirror: about 200 mm (8 inches)', 'r': 100, 'limit': 1.0, 'gain': 'About 800 times more light than your eye', 'note': 'Its mirror gathers about 800 times more light than your eye. Even a faint galaxy shows up.'}],
        'galaxyAt': 3, 'needZoom': True, 'zoomBtn': 'Zoom only',
        'zoomNote': 'Zoom made the stars bigger and dimmer, but no NEW stars appeared. Only a bigger opening gathers more light.',
        'tryZoom': 'Now press Zoom only. Does zooming in show you any NEW stars?',
        'q': 'What makes a telescope show MORE stars than your eye?',
        'opts': [{'t': 'Its big mirror gathers much more light.', 'ok': True},
                 {'t': 'It makes the stars bigger.', 'miss': 'Try Zoom only again. Bigger didn’t show any new stars, did it?'},
                 {'t': 'It brings the stars closer to Earth.', 'miss': 'The stars don’t move at all. What changed when you opened wider?'}],
        'credit': cr('owl', 'scope') + ' The sky is a model drawn for this lesson, not a photo.',
        'win': 'Far things look dim because only a little of their light reaches you. A bigger opening gathers more of it. That’s a clue.',
        'clue': 'openwide'},
    'skyhunt': {
        'afterText': 'Sam set up two tools on the beach', 'replace': '#tab-lesson .diagram-wrap', 'kicker': 'Part 2 game', 'title': 'Find it in the sky',
        'todo': ['Pick a tool. Then drag the circle across the sky (or tap a spot) to aim it.', 'Look at each one with BOTH tools. Then pick the best tool for it.'],
        'why': {'icon': '🔭', 'q': 'Why is the telescope circle so small?', 't': 'A telescope zooms in a lot, so it sees a tiny piece of sky. Binoculars see a much wider piece.'},
        'tools': [{'k': 'bino', 'icon': '🔭', 't': 'Binoculars', 'power': '10x · wide view', 'r': 120, 'hit': 46},
                  {'k': 'scope', 'icon': '🪞', 't': 'Backyard telescope', 'power': '150x · tiny view', 'r': 34, 'hit': 28}],
        'emptyLine': 'Just dark sky. Move the circle onto something.',
        'listLabel': 'Your sky list',
        'targets': [
            {'id': 'moon', 'name': 'The Moon', 'icon': '🌕', 'x': 170, 'y': 170, 'draw': 'moon',
             'views': {'bino': {'img': I('moon'), 'size': '74%', 'pos': 'center', 'note': 'The whole Moon fits. You can see dark patches and some big craters.'},
                       'scope': {'img': I('moon'), 'size': '380%', 'pos': '32% 70%', 'note': 'Craters inside craters! The Moon is too big to fit all at once.'}},
             'q': 'Maya wants the Moon’s craters. Best tool?', 'opts': [{'t': 'Binoculars', 'miss': 'Binoculars show some craters. Which tool showed craters inside craters?'}, {'t': 'Backyard telescope', 'ok': True}]},
            {'id': 'pleiades', 'name': 'Seven Sisters', 'icon': '✨', 'x': 430, 'y': 110, 'draw': 'cluster',
             'views': {'bino': {'img': I('pleiades'), 'size': '120%', 'pos': 'center', 'note': 'The whole cluster fits. Your eyes see about 6 or 7 stars; binoculars show dozens.'},
                       'scope': {'img': I('pleiades'), 'size': '900%', 'pos': '55% 45%', 'note': 'Too close! Only one or two stars fit in the tiny view.'}},
             'q': 'Ava wants the Seven Sisters. Best tool?', 'opts': [{'t': 'Binoculars', 'ok': True}, {'t': 'Backyard telescope', 'miss': 'How many of the sisters fit in the telescope’s tiny view?'}]},
            {'id': 'jupiter', 'name': 'Jupiter', 'icon': '🟠', 'x': 650, 'y': 330, 'draw': 'bright',
             'views': {'bino': {'html': '<i class="fs-sh-dot" style="width:9px;height:9px;left:46%;top:47%"></i><i class="fs-sh-dot" style="width:3px;height:3px;left:36%;top:49%"></i><i class="fs-sh-dot" style="width:3px;height:3px;left:41%;top:48%"></i><i class="fs-sh-dot" style="width:3px;height:3px;left:57%;top:50%"></i><i class="fs-sh-dot" style="width:3px;height:3px;left:63%;top:49%"></i>', 'note': 'A tiny dot with up to four tiny moons in a line. (A drawing.)'},
                       'scope': {'img': I('jupiter'), 'size': '42%', 'pos': 'center', 'note': 'A round world with cloud stripes. (Real Hubble photo; a backyard view is smaller.)'}},
             'q': 'To see Jupiter’s cloud stripes, which tool?', 'opts': [{'t': 'Binoculars', 'miss': 'Binoculars showed a dot. Where did you see stripes?'}, {'t': 'Backyard telescope', 'ok': True}]},
            {'id': 'saturn', 'name': 'Saturn', 'icon': '🪐', 'x': 860, 'y': 220, 'draw': 'dot',
             'views': {'bino': {'html': '<i class="fs-sh-dot" style="width:9px;height:6px;left:47%;top:48%;background:#F3D9A0;box-shadow:0 0 5px #F3D9A0"></i>', 'note': 'A tiny yellow dot. No rings yet. (A drawing.)'},
                       'scope': {'img': I('saturn'), 'size': '56%', 'pos': 'center', 'note': 'RINGS! At 100x or more they’re easy to see. (Real Hubble photo; a backyard view is smaller.)'}},
             'q': 'Leo wants Saturn’s rings. Best tool?', 'opts': [{'t': 'Binoculars', 'miss': 'Look again with binoculars. Can you see any rings?'}, {'t': 'Backyard telescope', 'ok': True}]}],
        'credit': cr('moon', 'pleiades', 'jupiter', 'saturn') + ' The sky, the dots and the binocular views of Jupiter and Saturn are drawings.',
        'win': 'Binoculars show wide things, like a star cluster. A backyard telescope shows small, far details, like Saturn’s rings. That’s a clue.',
        'clue': 'skyhunt'},
    'tv': {
        'afterText': 'Sam found an old TV news report', 'kicker': 'Breaking news · 1990', 'title': 'A telescope leaves Florida',
        'todo': ['Press Watch the report. Turn on your sound.', 'Then answer one question.'],
        'channel': 'NEWS 1990', 'live': 'LIVE', 'headline': 'HUBBLE SPACE TELESCOPE LAUNCHES', 'place': 'Kennedy Space Center, Florida', 'date': 'April 24, 1990',
        'slides': [{'img': I('launch'), 'alt': 'A space shuttle rises on a column of fire and smoke beside launch towers by the water.', 'cap': 'Discovery lifts off from Kennedy Space Center, Florida, with Hubble inside. Another shuttle, Columbia, waits on the next pad.'},
                   {'img': I('liftoff'), 'alt': 'A space shuttle climbing into a blue sky on a bright flame.', 'cap': 'Liftoff, April 24, 1990.'},
                   {'img': I('hubble'), 'alt': 'The Hubble Space Telescope, a silver tube with wing-like solar panels, floating above Earth.', 'cap': 'Hubble in space, high above the air. (Photo from 2009.)'}],
        'lineSlides': [0, 1, 1, 2, 2],
        'audio': 'tv',
        'lines': ['This is a special report from Kennedy Space Center, Florida.',
                  'Moments ago, the space shuttle Discovery blasted off, carrying the Hubble Space Telescope.',
                  'Tomorrow, astronauts will set Hubble free, more than three hundred miles above Earth.',
                  'Up there, it will be above the blurry, wobbly air that makes stars twinkle.',
                  'Scientists say its giant mirror will see farther and sharper than any telescope on the ground.'],
        'ticker': 'HUBBLE SPACE TELESCOPE · LAUNCHED APRIL 24, 1990 · KENNEDY SPACE CENTER, FLORIDA · MIRROR: ABOUT 8 FEET WIDE · ORBIT: MORE THAN 300 MILES UP · ',
        'playBtn': 'Watch the report', 'againBtn': 'Watch it again',
        'q': 'Why did scientists put Hubble in space?',
        'opts': [{'t': 'To get above the blurry air', 'ok': True},
                 {'t': 'To get closer to the stars', 'miss': 'Hubble is about 300 miles up. The stars are trillions of miles away. What did the report say about the air?'},
                 {'t': 'Because it was too big for Florida', 'miss': 'Listen again. What does the air do to starlight?'}],
        'credit': cr('launch', 'liftoff', 'hubble') + ' The report is read by a voice actor for this lesson.',
        'win': 'Right! Earth’s air blurs starlight and makes stars twinkle. Above the air, Hubble’s pictures are sharp.'},
    'deepfield': {
        'afterText': 'Jordan wants the farthest thing anyone has ever seen', 'kicker': 'Part 4 game', 'title': 'Stare at nothing',
        'todo': ['Look at the tiny square of “empty” sky with each tool, in order.', 'With Webb, press and HOLD the shutter button until 12.5 hours have passed.', 'Then tap three galaxy shapes.'],
        'why': {'icon': '🌌', 'q': 'How tiny is this speck?', 't': 'Hold a grain of sand at arm’s length. That’s how much sky this is, and it looks empty.'},
        'tools': [
            {'k': 'eye', 'icon': '👁️', 't': 'Your eyes', 'view': 'empty', 'note': 'Nothing. Just dark sky and a few stars around the speck.'},
            {'k': 'bino', 'icon': '🔭', 't': 'Binoculars', 'view': 'empty', 'note': 'Still nothing in the speck. It looks empty.'},
            {'k': 'scope', 'icon': '🪞', 't': 'Backyard telescope', 'view': 'smudge', 'note': 'Two very faint, fuzzy smudges. Something is there, but it’s too dim to see.'},
            {'k': 'webb', 'icon': '🛰️', 't': 'Webb space telescope', 'view': 'webb', 'note': 'Webb is a space telescope with a mirror about 21 feet wide. Press and hold to open its shutter.'}],
        'hold': {'btn': 'Press and HOLD to open Webb’s shutter', 'hours': 12.5, 'ms': 6500, 'label': 'Shutter open',
                 'letGo': 'You let go, so the shutter closed. Press and hold again to keep collecting light.'},
        'doneNote': 'After 12.5 hours, almost every speck is a galaxy with billions of stars. Some of this light traveled over 13 billion years.',
        'img': I('deepfield'), 'alt': 'Webb’s First Deep Field: thousands of glowing galaxies on black, some round, some spiral, some stretched into curved arcs, and a few stars with long spikes.',
        'findLabel': 'Tap three galaxy shapes:',
        'shapes': [
            {'k': 'round', 't': 'A big round glow', 'x': 52, 'y': 51.5, 'r': 6, 'found': 'A big round galaxy! It’s part of a giant group of galaxies.'},
            {'k': 'spiral', 't': 'A spiral (pinwheel)', 'x': 85.5, 'y': 38.5, 'r': 5, 'found': 'A spiral galaxy, shaped like a pinwheel, like our own Milky Way.'},
            {'k': 'arc', 't': 'A stretched curve', 'x': 60.5, 'y': 26.5, 'r': 5, 'found': 'A stretched, bent galaxy! Its light was bent on the way here by the giant group of galaxies in front of it.'}],
        'star': {'x': 42.5, 'y': 38, 'r': 4, 't': 'That one is a star in our own galaxy, much closer. The long spikes give it away. Find a galaxy shape instead.'},
        'hint': 'Look for a big round glow in the middle, a pinwheel on the right, and a curved streak near the top.',
        'lockLine': 'Look through the tool before this one first.',
        'q': 'Why could Webb see these galaxies when the backyard telescope couldn’t?',
        'opts': [{'t': 'Its huge mirror gathered light for hours, out in space.', 'ok': True},
                 {'t': 'It flew close to the galaxies.', 'miss': 'Webb is about a million miles from Earth. These galaxies are billions of light-years away. What did it do for 12.5 hours?'},
                 {'t': 'It zoomed in more.', 'miss': 'Remember Open wider: zoom alone doesn’t show new things. What does Webb’s mirror gather?'}],
        'credit': cr('deep') + ' The views through your eyes, binoculars and the backyard telescope are drawings.',
        'win': 'The farthest things need the biggest light-gatherer, out in space, looking for a long time. That’s your last clue.',
        'clue': 'deepfield'},
    'exploreMod': 'deepfield',
    'permit': {
        'kicker': 'Case closed · Sam’s permit', 'title': 'The star party permit',
        'todo': ['Tap the darkest place on this real photo of Florida at night. Then pick why.'],
        'head': 'TOWN OF PALMETTO BEACH · EVENT PERMIT', 'sub': 'Star Party Night · Saturday, 8 PM',
        'rows': [['Tools', 'Backyard telescope (rented), binoculars, Webb’s deep field picture'], ['Host', 'Sam Park, engineer']],
        'placeLabel': 'Place', 'whyLabel': 'Why there',
        'mapQ': 'Where are the stars easiest to see? Tap the darkest spot.',
        'img': I('florida-night'), 'alt': 'Florida at night from space: bright city lights along the coasts and around Orlando, and a big dark area in the south.',
        'spots': [
            {'k': 'miami', 't': 'Miami', 'x': 77, 'y': 72, 'side': 'r', 'miss': 'Miami is one of the brightest places in the photo. City lights hide faint stars.'},
            {'k': 'tampa', 't': 'Tampa Bay', 'x': 35, 'y': 60, 'side': 'l', 'miss': 'Look at all those lights around Tampa Bay. Find a darker spot.'},
            {'k': 'orlando', 't': 'Orlando', 'x': 43, 'y': 47, 'miss': 'Orlando glows at night. Look south for a dark place.'},
            {'k': 'cypress', 't': 'Big Cypress', 'x': 66, 'y': 79, 'side': 'l', 'ok': True, 'why': 'Big Cypress National Preserve is so dark that it is an official Dark Sky Park. Sam will take the star party bus there!'}],
        'whyQ': 'Why does a dark place help?',
        'whyOpts': [{'t': 'City lights wash out faint stars.', 'ok': True, 'fill': 'Big Cypress is dark. City lights wash out faint stars.'},
                    {'t': 'The stars are closer there.', 'miss': 'The stars are just as far away everywhere in Florida. What is different about the ground there?'},
                    {'t': 'It’s warmer there.', 'miss': 'Warm or cool, what makes stars hard to see? Look at the photo again.'}],
        'stamp': 'APPROVED', 'sign': 'Approved for Sam Park · Town of Palmetto Beach',
        'lockLine': 'Crack the case first. Then Sam’s permit opens.',
        'ps': {'head': 'P.S. from Sam: telescopes look down, too!', 'img': I('florida-satellite'), 'alt': 'Florida from space in daytime: green land, white clouds, and bright blue-green water swirling along the Gulf coast.',
               't': 'A real NASA satellite photo of Florida from more than 400 miles up. Scientists watch the water’s color from space to spot blooms like red tide. On this day, most of the blue-green swirls were mud stirred up by a storm. That’s why scientists still take water samples, like we did!', 'tease': 'See Florida from more than 400 miles up.',
               'credit': C['modis'] + '. Via Wikimedia Commons.'},
        'credit': C['flnight'] + '. Via Wikimedia Commons. Big Cypress National Preserve became an International Dark Sky Park in 2016.'},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'B': 'Bacteria are tiny and close. That’s a microscope’s job. What does a telescope collect?', 'C': 'Close-up insects need a hand lens or microscope. What does a telescope do with far-away light?'},
        'q2': {'A': 'Saturn looks like a bright dot to your eyes. Which tool showed the rings in Find it in the sky?', 'C': 'A hand lens is for close things. Saturn is about 900 million miles away!'},
        'q3': {'A': 'Space telescopes cost billions of dollars! What did the TV report say about the air?', 'B': 'Telescopes collect light, not sound. What blurs the view from the ground?'}},
    'flags': {
        'ans-1': [
            {'label': 'one far-away thing', 're': 'moon|saturn|star|galax|jupiter|andromeda|seven sisters|pleiades|planet'},
            {'label': 'the best tool', 're': 'telescope|binocular|hubble|webb|space'},
            {'label': 'why', 're': 'because|so |since|it can|it shows|to see|ring|crater|light|far|dim|wide|tiny|detail'}],
        'ans-3': [
            {'label': 'the word image', 're': 'image'},
            {'label': 'above the air', 're': 'air|atmosph|blur|twinkl|wobbl|space|above|sharp|clear'},
            {'label': 'a detail or example', 're': 'hubble|webb|galax|deep field|12|hours|mirror|far|faint|dim|light'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|we do need|still need|need space'},
            {'label': 'two pieces of evidence', 'any': ['air', 'atmosph', 'blur', 'twinkl', 'wobbl', 'hubble', 'webb', 'mirror', 'light', 'galax', 'deep field', 'hours', '12', 'zoom', 'bigger', 'dim', 'faint', 'mountain', 'space'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-1': 15, 'ans-3': 15, 'cer-4': 30},
    'hints': {
        'ans-1': ['Pick one: the Moon, Saturn, far stars or galaxies.', 'Think about Find it in the sky and Stare at nothing. Which tool showed it best?', 'Try: The best tool for ___ is ___ because ___.'],
        'ans-3': ['Think about the TV report. What does Earth’s air do to starlight?', 'Then think about Webb’s deep field. What did its image show?', 'Try: Space telescopes are better because ___. For example, Webb’s image ___.'],
        'cer-4': ['First decide: can a taller telescope on Earth do what a space telescope does?', 'Think about the blurry air in the TV report, and Zoom only in Open wider.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'Earth’s air blurs starlight. Hubble sits above the air, so its pictures are sharp.',
                'Zooming in only made stars bigger and dimmer. It didn’t show any new stars.',
                'Webb gathered light for 12.5 hours from space and found thousands of galaxies in an “empty” speck.',
                'Even a tall telescope on Earth still looks up through the air.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · the star party', 'length': '30–40 s',
                    'script': 'Great news! The red tide is gone, and Palmetto Beach is open again. So the town is throwing a star party, a night when everyone looks at the sky together. Four kids sent me their wish cards. Read them! The town can rent just one tool. Can we make every wish come true?'},
        'warmup': {'label': 'Warm-Up · race the light (Clue 1)', 'length': '20–30 s',
                   'script': 'Here’s a wild claim: the starlight you see tonight is older than you. Let’s test it. Drag each picture onto your guess. How long ago did its light leave? Then press Send the light and watch it race to Earth.'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Hold a paper towel tube to your eye for “telescope”; walk to the far side of the room for “distant”.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · open wider (Clue 2)', 'length': '20–30 s',
                  'script': 'Your eye is a light catcher. Drag the gold dot to open the opening wider. First an owl’s eye, then binoculars, then a telescope mirror. Watch the star count climb! Then try Zoom only. Do you see any new stars?'},
        'part2': {'label': 'Part 2 · find it in the sky (Clue 3)', 'length': '20–30 s',
                  'script': 'I set up two tools on the beach. Pick the binoculars or the telescope, then drag the circle across the sky. Look at every wish with both tools. The telescope sees more detail, but its view is tiny!'},
        'part3': {'label': 'Part 3 · the TV report', 'length': '20–30 s', 'notes': 'Optional video. The TV report itself is voiced by the news voice.'},
        'explore': {'label': 'Part 4 · stare at nothing (Clue 4)', 'length': '25–35 s',
                    'script': 'Jordan wants the farthest thing ever. Look at this tiny square of sky with each tool. Your eyes, binoculars, then the telescope. Then use Webb! Press and hold the shutter button. Keep holding until twelve and a half hours pass. Then tap three galaxy shapes.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s',
                       'script': 'Do you have all four clues? Crack the case at the top of this tab. Then fill in my star party permit and find the darkest place on the map. After that, answer two questions, write three views for Part C, and finish your C-E-R.'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · three views', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says we don’t need space telescopes. Just build them taller on Earth! Hmm. Think about the blurry air from the TV report. Think about Zoom only. Pick your side, tap two pieces of evidence in the planner, then explain how they prove your claim.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease week 19 (motion and energy).',
                    'script': 'Case closed! Every kid gets their wish, because you picked the right tool for each one. Binoculars, a backyard telescope, and a space telescope. Next week my tools get a new job. How does energy make things move?'},
    },
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Your four stamped light cards (Warm-Up)',
        'The sky with the most stars (The Lesson)',
        'Saturn through the telescope (The Lesson)',
        'Webb’s deep field after 12.5 hours (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['Three views of one far-away thing', 'Saturn through a telescope', 'The star party'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 3,
                           'prompts': ['Draw three circles in a row: eyes, binoculars, telescope', 'Draw what you’d see in each circle', 'Label one detail in each circle']}]},
    'hlCoach': copy.deepcopy(Q['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🎟️', 'name': 'Star party ticket',
                 'line': 'You cracked Case 18 part 2, and your star party ticket goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next week: energy and motion.'},
    'notebookTitle': 'Unit 5 · Energy, Motion & Collisions',
    'notebook': [{'lesson': w + '.0' + d} for w in ['18', '19', '20', '21', '22', '23', '24'] for d in ['1', '2']],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You’ll use every one of them at the star party.',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'list', 'find': {'sel': '.fs-game[data-mod="racelight"]'},
         'label': 'Warm-Up: three things I can see in the night sky', 'q': 'Warm-Up: Three things I can see in the night sky with just my eyes',
         'title': 'Your turn: name three things you can see in the night sky with just your eyes.', 'min': 3, 'unit': 'things', 'addLabel': '+ Add another',
         'ph': ['The Moon', 'Bright stars', 'Something else…']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'hide-nw', 'type': 'hide', 'find': {'sel': '.act-warmup .socratic-q', 'text': 'Notice'}},
        {'id': 'hide-tip', 'type': 'hide', 'find': {'sel': '.act-warmup .callout', 'text': 'Microscopes magnify tiny things'}},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Pick one far-away thing in the sky'},
         'label': 'Part C: Three views of one far-away thing', 'q': 'Part C: One far-away thing seen three ways, and the best tool for it',
         'title': 'Three views of my far-away thing',
         'fields': [{'t': 'My far-away thing', 'icon': '🌌', 'ph': 'I picked…'},
                    {'t': 'With my EYES, I see…', 'icon': '👁️', 'ph': 'With my eyes, I see…', 'long': True},
                    {'t': 'With BINOCULARS, I’d see…', 'icon': '🔭', 'ph': 'With binoculars, I’d see…', 'long': True},
                    {'t': 'With a BACKYARD TELESCOPE, I’d see…', 'icon': '🪞', 'ph': 'With a backyard telescope, I’d see…', 'long': True},
                    {'t': 'The best tool for it, and why', 'icon': '🎯', 'ph': 'The best tool is ___ because…', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Do we still need telescopes in space?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-1': 'Part B · Question 5', 'ans-3': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] == '18.01': n.update({'icon': '🧫', 'name': 'Red tide sample slide', 'have': False})
    if n['lesson'] == '18.02': n.update({'icon': '🎟️', 'name': 'Star party ticket'})
for n in D['notebook']:
    n.pop('have', None)
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'A telescope’s big mirror gathers much more light than your eye.',
    'key': ['telescope’s', 'big', 'mirror', 'gathers', 'more', 'light'],
    'small': ['A', 'than', 'your'],
    'model': 'A scientist might highlight “big mirror”, “gathers” and “more light”. Those words tell how a telescope works. Small words like “a” and “than” don’t carry the idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me explain how tools help us see things too far away?']

# ---------------------------------------------------------------- Spotlight: what lights up as Sam talks
EV = '#tab-assignment .act-body > div:has(> .fs-plan)'
D['cues'] = {
    'welcome': [{'at': '^gone', 'sel': '.fs-casecard .fs-case-k', 'fx': 'glow'},
                {'at': '^star$', 'sel': '.fs-casecard .fs-notice', 'fx': 'pop', 'tag': 'Saturday, 8 PM'},
                {'at': '^wish', 'sel': '.fs-casecard .fs-wishes', 'fx': 'reveal'},
                {'at': '^Read', 'sel': '.fs-casecard .fs-wish', 'all': True, 'fx': 'wiggle'},
                {'at': '^one$', 'sel': '.fs-casecard .fs-notice dl', 'fx': 'trace'},
                {'at': '^every', 'sel': '.fs-casecard .fs-case-ask', 'fx': 'pop'}],
    'warmup': [{'at': '^older', 'sel': '.fs-game[data-mod="racelight"] .fs-why', 'fx': 'glow', 'scroll': True},
               {'at': '^Drag', 'sel': '.fs-rl-tray', 'fx': 'glow'},
               {'at': '^guess', 'sel': '.fs-rl-rib', 'fx': 'pop'},
               {'at': '^Send', 'sel': '.fs-rl-send', 'fx': 'point'},
               {'at': '^race', 'sel': '.fs-rl-track', 'fx': 'glow', 'tag': '✨ Light speed!'}],
    'part1': [{'at': '^catcher', 'sel': '.fs-ow-ap', 'fx': 'glow', 'scroll': True},
              {'at': '^gold', 'sel': '.fs-ow-apsvg', 'fx': 'pop', 'tag': 'Drag the gold dot'},
              {'at': '^owl', 'sel': '.fs-ow-who', 'fx': 'wiggle', 'tag': '🦉'},
              {'at': '^star$', 'sel': '.fs-ow-n', 'fx': 'pop'},
              {'at': '^Zoom', 'sel': '.fs-ow-zoom', 'fx': 'point'}],
    'part2': [{'at': '^two$', 'sel': '.fs-sh-tools', 'fx': 'glow', 'scroll': True},
              {'at': '^binoculars', 'sel': '.fs-sh-tool[data-k="bino"]', 'fx': 'pop'},
              {'at': '^telescope', 'sel': '.fs-sh-tool[data-k="scope"]', 'i': 0, 'fx': 'pop'},
              {'at': '^drag', 'sel': '.fs-sh-sky', 'fx': 'glow'},
              {'at': '^wish', 'sel': '.fs-sh-list', 'fx': 'reveal'},
              {'at': '^tiny', 'sel': '.fs-sh-eye', 'fx': 'wiggle', 'tag': 'Tiny view!'}],
    'explore': [{'at': '^farthest', 'sel': '.fs-game[data-mod="deepfield"] .fs-why', 'fx': 'glow', 'scroll': True},
                {'at': '^square', 'sel': '.fs-df-view', 'fx': 'pop'},
                {'at': '^eyes', 'sel': '.fs-df-tools', 'fx': 'glow'},
                {'at': '^Webb', 'sel': '.fs-df-tool[data-i="3"]', 'fx': 'wiggle', 'tag': '🛰️'},
                {'at': '^hold', 'sel': '.fs-df-hold', 'fx': 'point'},
                {'at': '^galaxy', 'sel': '.fs-df-view', 'fx': 'glow'}],
    'assignment': [{'at': '^clues', 'sel': '.fs-board', 'fx': 'glow'},
                   {'at': '^Crack', 'sel': '.fs-solve', 'fx': 'pop', 'scroll': True},
                   {'at': '^permit', 'sel': '.fs-pm-form', 'fx': 'pop', 'scroll': True},
                   {'at': '^darkest', 'sel': '.fs-pm-photo', 'fx': 'glow'},
                   {'at': '^two$', 'sel': '#tab-assignment .pq', 'fx': 'glow', 'all': True, 'scroll': True},
                   {'at': '^CER$|^C$', 'sel': '#tab-assignment .fs-cer', 'fx': 'glow', 'scroll': True}],
    'evidence': [{'at': '^classmate', 'sel': EV + ' > p', 'i': 0, 'fx': 'trace'},
                 {'at': '^blurry', 'sel': '.fs-plan .fs-opt', 'i': 2, 'fx': 'glow'},
                 {'at': '^Zoom', 'sel': '.fs-plan .fs-opt', 'i': 3, 'fx': 'glow'},
                 {'at': '^side', 'sel': '.fs-plan .fs-plan-row', 'i': 0, 'fx': 'pop'},
                 {'at': '^evidence', 'sel': '.fs-plan .fs-plan-row', 'i': 1, 'fx': 'glow'},
                 {'at': '^explain', 'sel': '.fs-cer .fs-cer-row', 'i': 2, 'fx': 'glow', 'scroll': True}],
    'closing': [{'at': '^closed', 'sel': '.fs-specimen', 'fx': 'pop', 'scroll': True},
                {'at': '^Next', 'sel': '#tab-assignment .callout-tip', 'fx': 'glow'}],
}

# ---------------------------------------------------------------- stars everywhere (Bethany, 22 Oct 2026: "make it beautiful and awe inspiring")
D['nightsky'] = {'stars': 260}
# Telescopium ("the telescope"), a real constellation; one star per clue (eps, alpha, zeta, iota Tel), simplified shape from their RA/Dec, east on the left
D['constellation'] = {'name': 'TELESCOPIUM', 'meaning': 'means “the telescope.” It’s a real constellation!',
    'note': 'A French astronomer named it in the 1750s. He also named Microscopium, the microscope!',
    'hint': 'Each clue you find lights a star. Find all four and see what they draw.',
    'stars': [{'x': 108, 'y': 8.5}, {'x': 89.7, 'y': 8.7}, {'x': 87.7, 'y': 29.5}, {'x': 12, 'y': 23}],
    'lines': [[0, 1], [1, 2], [2, 3]]}
CH = json.load(open('chart.json', encoding='utf-8'))
D['starchart'] = {'after': '.fs-game[data-mod="permit"]', 'kicker': 'Bonus · for a real night out', 'title': 'My star party sky chart',
    'why': {'icon': '🗺️', 'q': 'Is this the real sky?', 't': 'Yes! A computer worked out where the stars and Saturn are over Florida in mid-January at 8 PM. The lines show Orion, the hunter.'},
    'teaser': '',
    'when': 'Mid-January, about 8 PM', 'where': 'anywhere in Florida',
    'alt': 'A round chart of the night sky over Florida in mid-January at 8 PM, with Orion, Sirius, the Seven Sisters, Saturn and the North Star marked.',
    'how': 'Hold the chart up over your head. Turn it until NORTH on the chart points north. When you look up, east really is on your left!',
    'pts': CH['pts'], 'lines': CH['lines'],
    'dirs': {'N': 'NORTH', 'S': 'SOUTH', 'E': 'EAST', 'W': 'WEST'},
    'checkLabel': 'Can you find…',
    'checks': ['Orion’s belt: three stars in a row', 'Sirius, the brightest star (its light left about 9 years ago!)', 'The Seven Sisters, almost straight up', 'Saturn: golden and steady, in the southwest', 'The North Star, low in the north', 'Bonus, from a dark place: the Andromeda Galaxy, a faint fuzzy smudge'],
    'note': 'The Moon moves every night, so it isn’t on the chart. Bright Jupiter rises in the east around 8 PM. Go out with a grown-up!',
    'btn': 'Print my star chart', 'printTitle': 'My star party sky',
    'credit': 'Star and Saturn positions worked out for Orlando, Florida, on January 14, 2027, at 8 PM, with the PyEphem astronomy program. The chart is close for any night in mid-January and anywhere in Florida.'}
D['cues']['closing'].insert(1, {'at': '^Binoculars', 'sel': '.fs-game[data-mod="starchart"]', 'fx': 'glow', 'scroll': True})
D['fold'] = {'tv': {'icon': '📺', 'tease': 'Watch a real 1990 news report: a famous telescope leaves Florida for space.', 'open': 'Watch'},
             'starchart': {'icon': '🗺️', 'tease': 'Print a real map of the January night sky over Florida, with your name on it.', 'open': 'Open'}}
D['cueWords'] = json.load(open('cuewords.json', encoding='utf-8')) if os.path.exists('cuewords.json') else {}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
