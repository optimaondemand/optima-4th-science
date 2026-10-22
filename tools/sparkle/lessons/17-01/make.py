#!/usr/bin/env python3
"""Writes data.json and fixes.json for 17.01 (run from this folder). Showcase lesson: Case 17 "Storm Night" in Palmetto Springs.
June Calloway (Unit 4). New modules: bulletin, stormclock, flyover, stormchain; rain gauge tool (SIMS.raingauge); case.map + D.townmap."""
import json, copy
from townmap import MAP
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../16-02/data.json', encoding='utf-8'))
R = json.load(open('../r4-1/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

# ---------------------------------------------------------------- ticked fixes (Bethany, 22 Oct 2026)
fx('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist already asks for a cause-and-effect chain',
   '🎨 Part C &mdash; Build Your Own Food Chain', '🔗 Part C &mdash; Trace a Cause-and-Effect Chain')
fx('fix', 'copy-paste leftover: Part C task from 9.01 (typed on the page now; a sketch is a bonus)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   "Pick one Florida natural event (a hurricane, wildfire, flood or sinkhole). Trace it like a scientist: its cause, then one effect on the land, the ecosystem and the people.</p>", True)
fx('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'quarter label in the header: week 17 is Quarter 2', '<div class="info-value">Q3 &middot; Week 17</div>', '<div class="info-value">Q2 &middot; Week 17</div>')
fx('fix', 'quarter label in the footer: week 17 is Quarter 2', 'Science &middot; Quarter 3 &middot;', 'Science &middot; Quarter 2 &middot;')
fx('fix', 'this is an Earth science lesson (4-ESS3), not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Earth Science</div>')
fx('fix', 'the hurricane diagram image was never made (images/17-01-hazard-cause-effect.png doesn’t exist, so the AI prompt showed); the storm clock and the flyover replace it',
   r'<div class="lesson-figure scroll-reveal">.*?<div class="lesson-figure-caption">.*?</div>\s*</div>\s*', '', True)
fx('fix', 'Stop & Reason pointed at the image that was never made', r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'gravity and friction: same two ideas in about 60 plain words (was about 150)',
   r'<p style="font-size:16px;color:#0E1C42;font-weight:800;margin:0 0 8px;">🧲 Two Hidden Forces Behind Every Natural Event</p>.*?every natural event you\'ll study\.</p>',
   '<p style="font-size:16px;color:#0E1C42;font-weight:800;margin:0 0 8px;">🧲 Two Hidden Forces in Every Natural Event</p>\n'
   '        <p style="font-size:15px;color:#5A4D3E;line-height:1.65;margin:0 0 10px;"><strong>Gravity</strong> is the pull that brings everything down toward Earth. It makes rain fall and floodwater rush downhill into low streets.</p>\n'
   '        <p style="font-size:15px;color:#5A4D3E;line-height:1.65;margin:0;"><strong>Friction</strong> is a force that holds things back when two surfaces rub. Tree roots grip the soil with friction. When heavy rain soaks the ground, that grip gets weaker, so wind and gravity can pull trees over.</p>', True)

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; plain words',
   "Hold this question in your head as you work. By the end of the lesson, you'll be able to take one Florida natural event and trace its effects on three things: the land, the ecosystem, and the people.",
   "Keep this question in mind. By the end, you’ll be able to take one Florida natural event and trace its effects on the land, the ecosystem and the people.")
fx('plain', 'the warm-up is the weather radio now; answers are made on the page',
   r"<p>Picture a hurricane making landfall in Florida.*?</p>",
   "<p>Tonight a hurricane is heading for Palmetto Springs. A <strong>weather radio</strong> is a special radio that sounds an alarm when dangerous weather is coming. June’s just went off.</p>", True)
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', 'dashes removed; shorter',
   "</span></span> — hurricanes, floods, wildfires, sinkholes, freezes. When one happens, scientists trace its effects using a simple idea:",
   "</span></span>: hurricanes, floods, wildfires, sinkholes and freezes. When one happens, scientists trace its effects with a simple idea:")
fx('plain', 'two sentences instead of a semicolon', ". The event is the cause; everything that changes because of it is an effect.</p>", ". The event is the cause. Everything that changes because of it is an effect.</p>")
fx('plain', 'plain words; “landfall” and “property” explained by what they mean',
   "A summer thunderstorm? Normal Florida weather. A Category 4 hurricane making landfall? A hazard. The difference is whether the event causes harm to people, animals, or property.",
   "A summer thunderstorm is normal Florida weather. A strong hurricane coming on shore is a hazard. The difference is whether the event can harm people, animals or the things people own.")
fx('plain', 'dash removed; “underbrush” explained',
   "Fires clear underbrush — sometimes that's actually good for some plants. The web of life shifts.",
   "Fires clear out low bushes, and some plants need that. The web of life shifts.")
fx('plain', 'shorter', 'they look at effects in three layers. Each layer adds detail to the picture:', 'they look at effects in three layers:')
fx('plain', 'the diagram is Part 3 now', 'margin-top:22px;">Four Florida Natural Events</h3>', 'margin-top:22px;">Part 3 · Four Florida Natural Events</h3>')
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'shorter closing; points to 17.02',
   r'<p><strong>Nicely done\.</strong> You can now name Florida.*?</p>',
   '<p><strong>Nicely done.</strong> You can now trace a Florida natural event from its cause to its effects on the land, the ecosystem and the people, and explain why not every effect is bad. Next time, you’ll think like an engineer and design ways to keep a Florida town safer.</p>', True)

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: Stop & Think (the storm clock is the thinking stop for Part 1)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: the Watch out box (Part 4’s last reading and the CER cover the “not always bad” idea)',
   r'<p><strong>Common misconception:</strong> Some people think hazards only matter.*?</p>\s*', '', True)
fx('cut', 'lean: the Key Concept box repeats Part 2', r'<div style="background:#FFF6E5;border:2.5px solid #F0C97A;[^"]*">\s*<div[^>]*>⭐ Key Concept</div>\s*<p[^>]*>.*?</p>\s*</div>\s*', '', True)
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its chain becomes Part 4’s game and Part C; the Andrew fact and Go Deeper go with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: Observe & Reason, the Amazing Fact, the Florida connection and Go Deeper at the end of the Lesson; Part 4 = the old Explore; next button goes to Self-Check',
   r'<div class="socratic-q">\s*<span class="sq-icon">👀</span>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 4 · Morning in Palmetto Springs</h3>\n      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">The storm is gone. June spreads the night’s evidence on her table. Can you link it into one chain, from the cause all the way to the people?</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 5 removed (Bethany kept 6 and 7; Part C asks nearly the same as 5)', r'<div class="pq">\s*<span class="pq-num"[^>]*>5</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: renumber Part B (6 → 5)', '<span class="pq-num" style="background:#D4772C;">6</span>', '<span class="pq-num" style="background:#D4772C;">5</span>')
fx('cut', 'lean: renumber Part B (7 → 6)', '<span class="pq-num" style="background:#D4772C;">7</span>', '<span class="pq-num" style="background:#D4772C;">6</span>')
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C typed on the page; the sketch is a bonus',
   "A cause-and-effect diagram with a CAUSE box, three EFFECT boxes (LAND, ECOSYSTEM, PEOPLE), each with at least 2 effects, plus one connecting arrow between layers.",
   "One Florida natural event traced from its cause to an effect on the land, the ecosystem and the people. (A sketch is a bonus.)")
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether all natural events are disasters, and supported it with two pieces of evidence from the lesson.',
   '<strong>Use Your Evidence:</strong> My claim about whether all natural events are disasters, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', True)

# ---------------------------------------------------------------- the story
I = lambda n: 'images/17-01-' + n + '.jpg'
CREDIT = 'Mexico Beach, Florida, in April 2017 and on October 11, 2018, the day after Hurricane Michael: NOAA aerial photos, shared by the USGS Coastal Change Hazards team, via Wikimedia Commons'

D = {
    'lesson': '17.01', 'week': 17, 'day': 1, 'guide': 'june', 'prefix': 'g4sci-17-1', 'manifestKey': '17-01',
    'paths': P['paths'], 'crew': R['crew'],
    'expedition': {'num': 17, 'title': 'Storm Night'},
    'ambient': {'icon': '🌧️', 'label': 'Storm sounds'},
    'townmap': MAP,
    'case': {
        'num': 17, 'title': 'Storm Night', 'style': 'storm', 'map': True,
        'mapCap': 'Palmetto Springs (a made-up town). The red dashed zone must evacuate (leave to stay safe).',
        'hook': 'It’s June Calloway again. A hurricane is coming to Palmetto Springs tonight. I’ll be at the town’s storm center all night, reading the gauges and taking calls. Stay with me. In the morning, we’ll figure out what the storm changed.',
        'stills': [],
        'question': 'What did the storm change in Palmetto Springs, and was all of it bad?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'bulletin', 'icon': '📻', 'where': 'Warm-Up: the weather radio', 't': 'A hurricane brings three dangers: strong wind, heavy rain and storm surge (ocean water pushed onto land).'},
            {'id': 'stormclock', 'icon': '🕛', 'where': 'The Lesson, Part 1: the storm clock', 't': 'Each danger had its own effects: wind knocked down a branch and a power line, rain flooded Elm Street, and storm surge pushed seawater onto Bay Street and into Cypress Slough.'},
            {'id': 'flyover', 'icon': '🛩️', 'where': 'The Lesson, Part 2: the morning flyover', 't': 'One real storm changed all three layers: the land (dunes washed away, sand on the road), the ecosystem (woods snapped and bare) and the people (homes and a campground swept away).'},
            {'id': 'stormchain', 'icon': '💧', 'where': 'The Lesson, Part 4: trace the chain', 't': 'Not every effect was bad: the storm’s rain ended a dry spell and refilled the spring and the water underground. In 2008, Tropical Storm Fay raised Lake Okeechobee more than 2 feet in one week.'},
        ],
        'solve': {
            'title': 'What did the storm change?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'It only knocked down some trees. Nothing else changed.', 'why': 'Check Clues 2 and 3. Did the storm change more than trees?'},
                {'t': 'It changed the land, the ecosystem and the people, and every one of those changes was bad.', 'why': 'Check Clue 4. What happened to the spring after the storm?'},
                {'t': 'Its wind, rain and storm surge changed the land, the ecosystem and the people. Most changes were harmful, but its rain also refilled the spring.', 'right': True,
                 'why': 'Case cracked! You traced every danger through all three layers, and you found the good side, too. Now write your case report: it’s the questions below.'},
            ]},
    },
    'bulletin': {
        'afterText': 'June’s just went off', 'kicker': 'Warm-Up game', 'title': 'The weather radio',
        'todo': ['Press Play and listen. You can read along on the paper.', 'Tap the three DANGERS the storm is bringing. A place or a time is not a danger.'],
        'device': 'WEATHER RADIO', 'station': 'Alert for Palmetto Springs · 4 PM', 'playBtn': 'Play the warning', 'againBtn': 'Play it again', 'audio': 'bulletin',
        'paperHead': 'HURRICANE WARNING · PALMETTO SPRINGS',
        'lines': ['This is a hurricane warning for Palmetto Springs. A strong hurricane will reach the coast tonight.',
                  '[[wind|Winds of 100 miles per hour]] can knock down trees and power lines.',
                  '[[rain|Heavy rain]], up to 20 inches, can flood streets.',
                  '[[surge|Storm surge]], ocean water pushed onto land by the storm, can rise 8 feet near the bay.',
                  'Everyone on [[x:Bay Street is a place, not a danger. What could hurt people there?|Bay Street]] must evacuate by [[x:6 PM is a time, not a danger. Look for something the storm brings.|6 PM]]. Go to a safe place inland (away from the coast) now.'],
        'foundLabel': 'The dangers you found',
        'dangers': [{'id': 'wind', 'icon': '💨', 't': 'Strong wind', 'does': 'knocks down trees and power lines'},
                    {'id': 'rain', 'icon': '🌧️', 't': 'Heavy rain', 'does': 'floods streets'},
                    {'id': 'surge', 'icon': '🌊', 't': 'Storm surge', 'does': 'pushes ocean water onto land near the bay'}],
        'win': 'Three dangers: wind, rain and storm surge. Each one causes different effects. That’s a clue.',
        'clue': 'bulletin'},
    'stormclock': {
        'afterText': 'The difference is whether the event can harm', 'kicker': 'Part 1 game', 'title': 'The storm clock',
        'todo': ['Press the button to move through the night. Watch the wind, the rain and the tide gauge.',
                 'When a call comes in, drag the danger that caused it onto the call (or tap a danger, then the call).'],
        'why': {'icon': '🌊', 'q': 'What is a tide gauge?', 't': 'A tall ruler on the dock that shows how high the bay water is.'},
        'boardTitle': 'Storm-call board', 'nextBtn': 'Next', 'endBtn': 'Morning: the storm has passed', 'dropHere': 'Drop the cause here',
        'startLine': 'It’s 6 PM. Bay Street is empty: those families evacuated. Press the button to move to 8 PM.',
        'waitLine': 'A new call came in! Drag the cause onto it (or tap a cause, then the call).',
        'normalLabel': 'normal high tide', 'tideMax': 9, 'tideNormal': 2,
        'hours': [
            {'t': '6 PM', 'wind': 45, 'rain': 0, 'tide': 2.5, 'note': 'The first rain bands arrive.'},
            {'t': '8 PM', 'wind': 65, 'rain': 1, 'tide': 3.5, 'note': 'The wind is getting louder.'},
            {'t': '10 PM', 'wind': 85, 'rain': 2.5, 'tide': 5, 'note': 'Rain is pounding the roofs.'},
            {'t': '12 AM', 'wind': 100, 'rain': 4.5, 'tide': 8, 'note': 'The strongest part of the storm hits.'},
            {'t': '2 AM', 'wind': 90, 'rain': 7, 'tide': 7, 'note': 'Still strong. The bay is still high.'},
            {'t': '4 AM', 'wind': 65, 'rain': 9.5, 'tide': 4.5, 'note': 'The worst has passed.', 'quiet': 'No new calls. The wind is dropping, and the bay is going back down.'},
            {'t': '6 AM', 'wind': 35, 'rain': 11, 'tide': 3, 'note': 'Sunrise. The storm is moving away.', 'quiet': 'Good morning! The storm is moving away. Answer the question below.'}],
        'causes': [{'k': 'wind', 'icon': '💨', 't': 'Strong wind'}, {'k': 'rain', 'icon': '🌧️', 't': 'Heavy rain'}, {'k': 'surge', 'icon': '🌊', 't': 'Storm surge'}],
        'notice': {'head': 'Evacuation order · 4 PM', 't': 'Everyone in the red zone along Bay Street must leave by 6 PM. The bay could rise up to 8 feet.'},
        'calls': [
            {'id': 'pine', 'at': 1, 'icon': '🌳', 'place': 'Pine Ave', 'x': 300, 'y': 118, 'cause': 'wind', 't': 'A big oak branch snapped and fell across the road.',
             'miss': {'rain': 'Rain soaks the ground, but what pushes on a branch so hard that it snaps?', 'surge': 'Pine Ave is far from the bay. Look at the map. Can seawater reach it?'},
             'why': 'Strong wind pushes hard on branches until they snap.'},
            {'id': 'oak', 'at': 2, 'icon': '💡', 'place': 'Oak Street', 'x': 470, 'y': 140, 'cause': 'wind', 't': 'The power is out on the whole street. A power line is down.',
             'miss': {'rain': 'Rain alone doesn’t pull down a power line. What could?', 'surge': 'Oak Street is far from the bay. Look at the map.'},
             'why': 'The wind blew a tree onto the power line and knocked the power out.'},
            {'id': 'bay', 'at': 3, 'icon': '🏠', 'place': 'Bay Street', 'x': 380, 'y': 278, 'cause': 'surge', 't': 'Salty water is coming up the street and into the houses!',
             'miss': {'wind': 'Wind pushes, but where did all that SALTY water come from? Check the tide gauge.', 'rain': 'Rain is fresh water. This water is salty and came from the bay. Check the tide gauge.'},
             'why': 'The tide gauge hit 8 feet. Storm surge pushed the bay onto land. That’s why Bay Street evacuated before the storm.'},
            {'id': 'elm', 'at': 3, 'icon': '🌧️', 'place': 'Elm Street', 'x': 430, 'y': 80, 'cause': 'rain', 't': 'The street is flooded. The storm drains are overflowing.',
             'miss': {'surge': 'Elm Street is far from the bay. Look at the map. What else is falling from the sky?', 'wind': 'Wind doesn’t fill a street with water. What is falling from the sky?'},
             'why': 'Rain fell faster than the storm drains could carry it away.'},
            {'id': 'slough', 'at': 4, 'icon': '🌾', 'place': 'Cypress Slough', 'x': 120, 'y': 250, 'cause': 'surge', 't': 'Salty bay water is pouring into the wetland.',
             'miss': {'rain': 'Rain is fresh water. Which danger brings SALTY water?', 'wind': 'Wind pushes the water, but which danger IS the water? Check the tide gauge.'},
             'why': 'Storm surge pushed salty bay water into a freshwater wetland. Salt can hurt plants and animals that need fresh water.'}],
        'q': 'Why did the town tell Bay Street to evacuate, but not Elm Street?',
        'opts': [{'t': 'Bay Street is next to the bay, where storm surge pushes seawater onto land.', 'ok': True},
                 {'t': 'The wind blew only on Bay Street.', 'miss': 'Look at the calls. Did the wind hit only Bay Street?'},
                 {'t': 'Elm Street got no rain.', 'miss': 'Look at Elm Street’s call. What flooded it?'}],
        'win': 'Each danger caused different effects in different places. That’s a clue.',
        'clue': 'stormclock'},
    'flyover': {
        'afterText': 'Each layer affects the others', 'kicker': 'Part 2 game', 'title': 'The morning flyover',
        'todo': ['Drag the slider to compare BEFORE and AFTER.', 'Tap each number on the photo. Then stamp it: Land, Ecosystem or People.'],
        'why': {'icon': '🛩️', 'q': 'Where is this?', 't': 'Mexico Beach, a real Florida town. Hurricane Michael hit it in October 2018. The next day, a plane took the “after” photo of the same spot.'},
        'before': {'img': I('mexico-before'), 'label': 'BEFORE · April 2017', 'short': 'Before',
                   'alt': 'From the air: a beach town with a campground full of RVs, houses among green woods, a pond and creek, and a road beside a wide white beach.'},
        'after': {'img': I('mexico-after'), 'label': 'AFTER · Oct. 11, 2018', 'short': 'After',
                  'alt': 'The same town the day after Hurricane Michael: the campground is bare sand, many houses are gone, the trees are brown and broken, and sand covers the road by the beach.'},
        'credit': CREDIT, 'license': 'Public domain',
        'startLine': 'Tap a number on the photo.', 'askLine': 'Which layer is this? Stamp it below.',
        'stamps': [{'k': 'land', 'icon': '🏖️', 't': 'Land'}, {'k': 'eco', 'icon': '🌿', 't': 'Ecosystem'}, {'k': 'people', 'icon': '🏠', 't': 'People'}],
        'spots': [
            {'n': 1, 'x': 60, 'y': 19, 'label': 'The woods', 'k': 'eco', 't': 'Before: thick green woods where birds and other animals lived. After: the trees are snapped and bare, so those animals lost their homes and food.',
             'miss': {'land': 'Fallen trees change the land, too. But think about the animals that lived here. Which layer is about living things?', 'people': 'No one lives in these woods. Who lost a home here?'}},
            {'n': 2, 'x': 25, 'y': 31, 'label': 'The campground', 'k': 'people', 't': 'Before: a campground full of RVs and cabins where families stayed. After: almost all of it was swept away. Only bare sand is left.',
             'miss': {'land': 'The sand is land, but what did PEOPLE lose here?', 'eco': 'RVs and cabins belong to people. Which layer is that?'}},
            {'n': 3, 'x': 42, 'y': 46, 'label': 'The pond and creek', 'k': 'eco', 't': 'Before: green woods grew all around the water. After: the edges are torn up and full of mud, sand and broken trees. Fish, turtles and birds live in places like this.',
             'miss': {'land': 'Look at what lives in and around the water. Which layer is that?', 'people': 'Is this about people’s homes, or about the plants and animals?'}},
            {'n': 4, 'x': 22, 'y': 52, 'label': 'The beach road', 'k': 'land', 't': 'Before: a road beside a wide white beach with sand dunes. After: waves and storm surge washed the dunes away and spread beach sand across the road.',
             'miss': {'eco': 'Sand and dunes aren’t alive. Which layer is about the ground itself?', 'people': 'The road is for people, but what changed here: the sand and the dunes. Which layer is that?'}},
            {'n': 5, 'x': 78, 'y': 87, 'label': 'Homes by the beach', 'k': 'people', 't': 'Many homes are gone. A few right next to them are still standing. Why? You’ll find out next lesson.',
             'miss': {'land': 'Homes belong to people. Which layer is that?', 'eco': 'Homes belong to people. Which layer is that?'}}],
        'q': 'What did the flyover show?',
        'opts': [{'t': 'The storm changed only the people layer.', 'miss': 'Look at your stamps. Did you use only 🏠?'},
                 {'t': 'One storm changed the land, the ecosystem AND the people.', 'ok': True},
                 {'t': 'The storm changed only the beach.', 'miss': 'Look at your stamps. What happened to the woods and the homes?'}],
        'win': 'One storm changed all three layers. That’s a clue.',
        'clue': 'flyover'},
    'stormchain': {
        'afterText': 'June spreads the night’s evidence', 'kicker': 'Part 4 game', 'title': 'Trace the chain',
        'todo': ['This chain follows the storm surge. Drag each card into its box (or tap a card, then a box).', 'Two cards don’t fit: they came from a different danger.'],
        'why': {'icon': '🔗', 'q': 'What is a cause-and-effect chain?', 't': 'One cause leads to an effect, and that effect leads to the next one, like falling dominoes.'},
        'slots': [{'k': 'cause', 'icon': '🌀', 't': 'Cause'}, {'k': 'land', 'icon': '🏖️', 't': 'Land'}, {'k': 'eco', 'icon': '🌿', 't': 'Ecosystem'}, {'k': 'people', 'icon': '🏠', 't': 'People'}],
        'links': ['pushed the bay onto land', 'with the dunes gone, seawater rushed in', 'and flooded the street by the bay'],
        'dropHere': 'drop a card here', 'trayLabel': 'The night’s evidence',
        'cards': [
            {'id': 'surge', 'icon': '🌊', 'art': 'Tide gauge · 12 AM', 't': 'Storm surge: the bay rose to 8 feet', 'k': 'cause',
             'missSlot': {'land': 'This is what STARTED it all. Which box comes first?', 'eco': 'This is what STARTED it all. Which box comes first?', 'people': 'This is what STARTED it all. Which box comes first?'}},
            {'id': 'dunes', 'icon': '🏖️', 'art': 'June’s morning photo', 't': 'Waves washed sand off the beach and over the dunes', 'k': 'land',
             'miss': 'Sand and dunes aren’t alive, and they aren’t people. Which box is about the ground?'},
            {'id': 'slough', 'icon': '🌾', 'art': 'Storm call · 2 AM', 't': 'Salty bay water poured into Cypress Slough, a freshwater wetland', 'k': 'eco',
             'miss': 'A wetland is full of plants and animals. Which box is that?'},
            {'id': 'bay', 'icon': '🏠', 'art': 'Evacuation order', 't': 'Bay Street homes flooded, but the families had evacuated and were safe', 'k': 'people',
             'miss': 'Homes and families are people. Which box is that?'},
            {'id': 'power', 'icon': '💡', 'art': 'Storm call · 10 PM', 't': 'The power went out on Oak Street', 'k': 'x',
             'miss': 'That effect came from the WIND, not the storm surge. Follow the seawater.'},
            {'id': 'elm', 'icon': '🌧️', 'art': 'Storm call · 12 AM', 't': 'Elm Street flooded', 'k': 'x',
             'miss': 'That came from the RAIN, far from the bay. This chain follows the storm surge.'}],
        'doneLine': 'The chain is complete: one cause, three layers.',
        'twist': {'btn': '🌅 One week later: June’s last reading', 'icon': '💧', 'head': 'Palmetto Spring · one week after the storm',
                  'rows': [['Before the storm', 'Two months with almost no rain. The spring was low, and the town asked everyone to save water.'],
                           ['After the storm', 'The water in the town well is 3 feet higher. The spring is flowing strong again.']],
                  't': 'The storm’s 20 inches of rain soaked into the ground and refilled the water stored in the rock underground.'},
        'q': 'Was every effect of the storm bad?',
        'opts': [{'t': 'Yes. Every effect of a hurricane is bad.', 'miss': 'Look at June’s last reading. What happened to the spring?'},
                 {'t': 'No. Its rain ended a dry spell and refilled the water underground.', 'ok': True},
                 {'t': 'No. The storm surge helped the wetland.', 'miss': 'Salty water hurts a freshwater wetland. Look at the spring instead.'}],
        'fact': 'This happens in real life, too. In August 2008, Tropical Storm Fay dropped heavy rain on Florida after one of its driest times on record. Lake Okeechobee rose more than 2 feet in one week.',
        'win': 'A natural event can harm AND help. That’s your last clue.',
        'clue': 'stormchain'},
    'exploreMod': 'stormchain',
    'tool': {
        'name': 'Rain gauge', 'icon': '🌧️', 'tab': 'assignment', 'after': '#tab-assignment .activity-card', 'key': '17-tool', 'sim': 'raingauge',
        'kicker': 'Bonus · Tool of the Week',
        'teaser': 'Read the rain gauge after each part of the storm and add up all the rain.',
        'done': 'You read the rain gauge like a weather watcher. A rain gauge sticker is in your Field Notebook.',
        'why': {'icon': '🌧️', 'q': 'What is a rain gauge?', 't': 'A clear tube with inch marks that catches rain, so you can measure exactly how much fell. Volunteers all over Florida read one every morning and share the numbers with weather scientists.'},
        'raingauge': {
            'title': 'How much rain did the storm drop?',
            'todo': ['Tap each part of the gauge to learn it.', 'Check the gauge after each part of the storm, and read how many inches fell.', 'Then add it all up.'],
            'max': 8, 'readQ': 'Read the gauge. How many inches of rain?', 'totalLabel': 'Rain logged so far', 'emptyLine': 'You wrote it down and emptied the gauge.',
            'parts': [{'label': 'The funnel', 't': 'It catches the rain and pours it into the tube, so none splashes out.'},
                      {'label': 'The tube', 't': 'Its marks are inches, like a ruler standing up. The top of the water shows how much rain fell.'},
                      {'label': 'Where it goes', 't': 'On a post in an open spot, away from trees and roofs, so nothing blocks the rain or drips extra water in.'}],
            'periods': [
                {'k': 'eve', 't': '6 PM to midnight', 'inches': 4.5, 'opts': [4, 4.5, 5], 'note': 'The rain got heavier as the storm came closer.'},
                {'k': 'night', 't': 'Midnight to 6 AM', 'inches': 6.5, 'opts': [6, 6.5, 7], 'note': 'The heaviest rain fell while the storm was right over town.'},
                {'k': 'morn', 't': '6 AM to noon', 'inches': 5, 'opts': [4.5, 5, 5.5], 'note': 'The storm was moving away, but its rain bands kept coming.'},
                {'k': 'aft', 't': 'Noon to 6 PM', 'inches': 4, 'opts': [3.5, 4, 4.5], 'note': 'The last rain bands passed. The sun came out at sunset.'}],
            'q': {'q': 'How much rain fell in the whole storm?', 'opts': [
                {'t': '6.5 inches', 'why': 'That’s the most in one part. Add all four parts together.'},
                {'t': '20 inches', 'ok': True, 'why': 'Right! 4.5 + 6.5 + 5 + 4 = 20 inches. Florida gets about 54 inches of rain in a whole year, so this one storm dropped more than a third of a year’s rain in one day.'},
                {'t': '4 inches', 'why': 'That’s just the last part. Add all four parts together.'}]}}},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'If they were the same, we wouldn’t need two words. Which one makes something happen?', 'C': 'Nature can be a cause, and people can feel effects, but that isn’t what the words mean. Which answer says what each word does?'},
        'q2': {'B': 'Closed roads change people’s day. Which layer is that?', 'C': 'A house belongs to people. Which answer is about animals and plants?'},
        'q3': {'A': 'Hurricanes form over warm ocean water, not under the ground. Which event starts with rock dissolving?', 'B': 'Wildfires need dry plants and a spark. Which event starts with rock dissolving?'}},
    'flags': {
        'ans-2': [
            {'label': 'why fire can help', 're': 'seed|cone|clear|underbrush|bush|new|grow|space|sun|light|healthy|need|open|room'},
            {'label': 'the word ecosystem', 're': 'eco.?sys'},
            {'label': 'why it can harm people', 're': 'home|house|smoke|people|danger|burn|evacuat|harm|hurt|property|town'}],
        'ans-3': [
            {'label': 'more than one layer', 'any': ['land', 'ecosystem', 'people', 'animal', 'plant', 'home', 'house', 'tree', 'beach', 'wetland'], 'min': 2},
            {'label': 'an example', 're': 'hurricane|storm|surge|flood|fire|wildfire|sinkhole|tree|wetland|slough|bay|power|beach|dune|for example|like'},
            {'label': 'why it matters', 're': 'because|so |connect|link|affect|lead|ripple|chain|whole|miss|cause'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|not all|aren|are not'},
            {'label': 'two pieces of evidence', 'any': ['rain', 'spring', 'refill', 'water', 'aquifer', 'fire', 'wildfire', 'pine', 'seed', 'thunderstorm', 'surge', 'flood', 'power', 'home', 'wetland', 'slough', 'fay', 'okeechobee', 'lake', 'dry'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-2': 15, 'ans-3': 20, 'cer-4': 30},
    'hints': {
        'ans-2': ['What does a fire clear away in a pine forest?', 'Some pine cones and plants need fire. Now, why could the same fire be dangerous for people?', 'Try: A wildfire can help the ecosystem because ___. But it can harm people because ___.'],
        'ans-3': ['Think about the flyover photos. Did the storm change only one layer?', 'Pick one storm effect and follow it into another layer, like the dunes and the wetland.', 'Try: It is important to trace all three layers because ___. For example, ___.'],
        'cer-4': ['First decide: is EVERY natural event a disaster?', 'Think about June’s last reading at the spring, and about wildfires in pine forests.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'The storm’s surge flooded Bay Street homes and pushed salty water into Cypress Slough.',
                'The storm’s rain ended a dry spell and refilled the spring and the water underground.',
                'Some Florida pine forests need fire to clear out low bushes and release their seeds.',
                'A summer thunderstorm is a natural event, but it is normal weather, not a hazard.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · storm night', 'length': '30–40 s',
                    'script': 'Hi, it’s June. Tonight a hurricane is heading straight for Palmetto Springs. I’m at the town’s storm center, and I’ll stay up all night reading the gauges and answering calls. Look at the map in the case file. See the red zone by the bay? Those families have to leave by six o’clock. Stay with me tonight. In the morning, we’ll figure out what the storm changed.'},
        'warmup': {'label': 'Warm-Up · the weather radio (Clue 1)', 'length': '20–30 s',
                   'script': 'My weather radio just went off. Press Play and listen closely. Then tap the three dangers the storm is bringing. Careful: a place or a time is not a danger. After that, write three things you think this storm might change in our town.'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Act out “evacuate” by grabbing a bag and walking off screen; point “cause” and “effect” with two hands like a domino push.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · the storm clock (Clue 2)', 'length': '25–35 s',
                  'script': 'Here’s the storm clock. Press the button to move through the night, two hours at a time. Watch the wind, the rain and the tide gauge on the dock. When a call comes in, drag the danger that caused it onto the call. Then you can move to the next hour.'},
        'part2': {'label': 'Part 2 · the morning flyover (Clue 3)', 'length': '20–30 s',
                  'script': 'Palmetto Springs is made up, but these photos are real. They show Mexico Beach, Florida, before and after Hurricane Michael. Drag the slider to compare. Then tap each number and stamp it: land, ecosystem or people.'},
        'explore': {'label': 'Part 4 · trace the chain (Clue 4)', 'length': '25–35 s',
                    'script': 'Good morning! The storm is gone, and the night’s evidence is on my table. Let’s follow the storm surge, one link at a time: the cause, the land, the ecosystem, then the people. Two cards came from a different danger, so leave them out. When you finish, I have one more reading to show you.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s',
                       'script': 'Do you have all four clues? Crack the case at the top of this tab: what did the storm change, and was all of it bad? Then answer two questions, trace a chain for any Florida natural event in Part C, and write your CER. Your answers save as you type.'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · trace a chain', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says all natural events are disasters, and the fewer the better. Hmm. Think about last night’s storm. Then think about my last reading at the spring. Pick your side, tap two pieces of evidence in the planner, then explain how they prove your claim.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 17.02 (design ways to keep a town safer, like an engineer).',
                    'script': 'Case closed! You followed a hurricane through a whole night, and you traced its effects on the land, the ecosystem and the people. You even found the good side. Next time, we’ll think like engineers and design ways to keep a town like ours safer before the next storm.'},
    },
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'The three dangers you found (Warm-Up)',
        'The storm clock at 12 AM (The Lesson)',
        'A spot you stamped on the flyover photo (The Lesson)',
        'Your finished chain (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['My cause-and-effect chain', 'Palmetto Springs during the storm', 'The tide gauge at midnight'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 3,
                           'prompts': ['Draw four boxes in a row', 'Write the cause in the first box and one effect in each of the others', 'Draw arrows from each box to the next']}]},
    'hlCoach': copy.deepcopy(Q['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '📈', 'name': 'Storm-night tide gauge chart',
                 'line': 'You cracked Case 17, and the tide gauge chart from Storm Night goes in your Field Notebook. (A specimen is something a scientist collects to study.) Next time: designing ways to keep a town safer.'},
    'notebookTitle': R['notebookTitle'],
    'notebook': [dict(x) for x in Q['notebook']],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You’ll hear every one of them on Storm Night.',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'list', 'find': {'sel': '.fs-game[data-mod="bulletin"]'},
         'label': 'Warm-Up: three things the hurricane might change', 'q': 'Warm-Up: Three things the hurricane might change in Palmetto Springs (think beyond buildings!)',
         'title': 'Your turn: three things this storm might change in town. Think beyond buildings!', 'min': 3, 'unit': 'changes', 'addLabel': '+ Add a change',
         'ph': ['The wind might…', 'The rain might…', 'The storm surge might…']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'hide-nw', 'type': 'hide', 'find': {'sel': '.act-warmup .socratic-q', 'text': 'Notice'}},
        {'id': 'hide-tip', 'type': 'hide', 'find': {'sel': '.act-warmup .callout', 'text': 'Today'}},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Trace it like a scientist'},
         'label': 'Part C: Trace a cause-and-effect chain', 'q': 'Part C: One Florida natural event: its cause, and one effect on the land, the ecosystem and the people',
         'title': 'My cause-and-effect chain',
         'fields': [{'t': 'The natural event I picked, and its cause', 'icon': '🌀', 'ph': 'I picked ___. It is caused by…', 'long': True},
                    {'t': 'One effect on the LAND', 'icon': '🏖️', 'ph': 'On the land, …'},
                    {'t': 'One effect on the ECOSYSTEM', 'icon': '🌿', 'ph': 'In the ecosystem, …'},
                    {'t': 'One effect on the PEOPLE, and how one effect led to the next', 'icon': '🏠', 'ph': 'For people, … This happened because…', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Are ALL natural events disasters?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-2': 'Part B · Question 5', 'ans-3': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] == '17.01': n.update({'icon': '📈', 'name': 'Storm-night tide gauge chart'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'Storm surge pushed salty bay water onto Bay Street and into the wetland.',
    'key': ['Storm', 'surge', 'salty', 'Bay', 'Street', 'wetland'],
    'small': ['pushed', 'onto', 'and', 'into', 'the'],
    'model': 'A scientist might highlight “storm surge”, “Bay Street” and “wetland”. Those words tell the cause and where its effects landed. Small words like “and” and “the” don’t carry the idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me explain how a natural event changes the land, the ecosystem and the people?']
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
