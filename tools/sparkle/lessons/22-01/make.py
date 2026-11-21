#!/usr/bin/env python3
"""Writes data.json and fixes.json for 22.01 (run from this folder). Case 22 "The Beacon Went Dark" (Sam Park, Palmetto Beach jetty light).
New: case.style 'mariners' + case.ticket (a Notice to Mariners + the keeper's work ticket), blackbox (Warm-Up: three sealed boxes show only IN and
OUT; drag the device card onto the box; it opens to a real photo), arrowtags (Part 1: tag each arrow MOVES or CHANGES; the energy changes color
only on CHANGES), pipes (Part 2: guess the useful split, pour 10 energy units through a device, always 10 out; replaces the never-made picture
and the tap diagram), trace reused with new data for Part 3 (follow the toast's energy back to the Sun; new options countWord, anotherBtn,
twist, q/opts), repair (after the case: tap the broken link, pick the fix, stamp FIXED), harbor (bonus after the case, folded: best device for
3 night jobs, stars), tool SIMS.wattmeter (plug-in watt meter)."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../18-01/data.json', encoding='utf-8'))
O = json.load(open('../21-02/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
PS = '<p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)
def I(n): return 'images/22-01-' + n + '.jpg'

# ---------------------------------------------------------------- labels (standing approval) + ticked fixes (Bethany, 20 Nov 2026)
fx('fix', 'unit label: “Ecosystems & Energy” is a leftover; weeks 18–24 are Unit 5', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Energy, Motion &amp; Collisions</div>')
fx('fix', 'energy conversion is physical science, not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
# 9.01 leftovers
fx('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist already asks for a device energy map', '🎨 Part C &mdash; Build Your Own Food Chain', '🔌 Part C &mdash; My Device Energy Map')
fx('fix', 'copy-paste leftover: Part C task from 9.01 (now an energy map typed on the page + a required labeled sketch)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Pick ONE device you can see right now (a lamp, a fan, a phone charger). Map its energy below, then sketch it.</p>', True)
fx('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
# confusing lines
fx('fix', 'confusing: “the heat that escapes the kitchen” → the heat that warms the kitchen air instead of the bread (vocab card)',
   'Some output energy is also "wasted" — like the toaster\'s sound or the heat that escapes the kitchen.',
   'Some output energy is extra, like the toaster’s click or the heat that warms the kitchen air instead of the bread.')
# wrong facts: the Explore Go Deeper said LEDs are “over 90% efficient”; it goes with the Explore tab (cut below); the pipes use about 4 of 10 for an LED
# ("about a third to half of their electricity becomes light"; LEDs use at least 75% less energy than old bulbs, U.S. Department of Energy)

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; plain words',
   "Hold this question in your head as you work. By the end of the lesson, you'll be able to look at any device — a toaster, a flashlight, a fan — and explain what energy goes IN, what energy comes OUT, and how it changed in between.",
   "Keep this question in mind. By the end, you’ll look at any device and say what energy goes IN, what comes OUT, and how it changed.")
fx('plain', 'the warm-up opens with the toaster, then the black box game',
   '<p>Think about a toaster. You drop in cold bread. A minute later, you pull out hot toast.</p>',
   '<p>Think about a toaster. You drop in cold bread. A minute later, you pull out hot toast. Something you can’t see went into the toaster, too!</p>')
fx('fix', 'Warm-Up sketch → the black box game + a 3-row typed list (Bethany ticked it)',
   "<p>In your notebook, draw a quick sketch of a toaster. On one side, label what goes IN. On the other, label what comes OUT. (Hint: bread on both sides — but something invisible is also going in. What is it?)</p>",
   "<p>A device is a bit like a black box. You can see what goes IN and what comes OUT, even when you can’t see inside. Open three mystery boxes.</p>")
fx('plain', 'no dash; plain; points to the list',
   "<p>Today you'll learn that energy can CONVERT — change from one form into a completely different form. Toasters, flashlights, wind turbines, your own body — they're all energy converters.</p>",
   "<p>Every box changed energy from one form into a different form. That’s called converting energy. Now look around your home for three more devices.</p>")
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', 'no dash; shorter (Part 1)',
   "In the last few lessons, you saw energy TRANSFER between things — one marble passing motion to another, sound moving from a drum to your ear. Today's idea is different. In <span class=\"vtip\">transformation",
   "In the last few lessons, energy TRANSFERRED (moved) between things: one marble passed its motion to another, and sound traveled from a drum to your ear. Today’s idea is different. In <span class=\"vtip\">transformation")
fx('plain', 'no dash', "</span></span>, energy doesn't just move — it CHANGES into a different form.</p>", "</span></span>, energy doesn’t just move. It CHANGES into a different form.</p>")
fx('plain', 'shorter: two examples, no wind turbine (Part 1)',
   "A toaster doesn't just move electrical energy. It <span class=\"vtip\">converts<span class=\"vtip-box\"><span class=\"vtip-word\">Convert</span>Change energy from one form to another.</span></span> electrical energy INTO heat energy. A flashlight converts electrical energy INTO light energy. A wind turbine converts the motion of the wind INTO electrical energy.",
   "A toaster <span class=\"vtip\">converts<span class=\"vtip-box\"><span class=\"vtip-word\">Convert</span>Change energy from one form to another.</span></span> (changes) electrical energy INTO heat. A flashlight converts electrical energy INTO light.")
fx('plain', 'no dash; new words named (Part 2)', "is anything designed to convert energy. Every device has the same basic structure:</p>", "is a tool or machine built to do a job, and most devices convert energy. Every device has three parts to its energy story:</p>")
fx('plain', 'one example each', "what goes IN. (Battery for a flashlight. Wind for a turbine. The Sun's light for a solar panel.)", "what goes IN. (A battery for a flashlight.)")
fx('plain', 'no dash; one example', "what comes OUT — usually a NEW form. (Light from the flashlight. Electricity from the turbine. Electricity from the solar panel.)", "what comes OUT, usually in a NEW form. (Light from the flashlight.)")
fx('plain', 'shorter, one idea; no dash',
   r"<p>Sometimes the output includes BOTH the useful form AND some extras you didn't plan for\..*?No device is 100% efficient — some output always sneaks out as a form you didn't ask for\.</p>",
   "<p>The output you want is the <span class=\"vtip\">useful energy<span class=\"vtip-box\"><span class=\"vtip-word\">Useful energy</span>The output you wanted.</span></span>. But there are always extras. A flashlight makes light (useful) and also gets a little warm (extra heat). No device turns ALL its energy into the useful kind.</p>", True)
fx('plain', 'the misconception, plain; leads into the pipes',
   r"<p><strong>Common misconception:</strong> Some people think energy gets used up or created inside a device\..*?</p>",
   "<p><strong>Watch out:</strong> Some people think a device USES UP energy, or MAKES new energy. It doesn’t do either. It only changes the form. Put 10 units of energy in, and 10 units come out, in different forms. Test it with the energy pipes.</p>", True)
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'shorter closing; no dash; points to 22.02',
   r'<p><strong>Nicely done\.</strong> You can now map any.*?</p>',
   '<p><strong>Nicely done.</strong> You can map any device from input energy to output energy, find its useful energy, and trace its energy back to the Sun. Next lesson, you become the engineer: you design your OWN device that converts energy.</p>', True)
fx('plain', 'Part B question 5 named the removed diagram; now it names the pipes devices',
   'Pick ONE conversion from the diagram (solar panel, gas car, wind turbine, or toaster). Write the INPUT form and OUTPUT form. Identify one form of extra energy that\'s also produced.',
   'Pick ONE device from the energy pipes (toaster, old bulb, LED bulb, gas car or solar panel). Write its INPUT energy and its useful OUTPUT energy. Then name one kind of extra energy it also makes.')
fx('plain', 'Part B question 5 label (Gathered Answers)', 'data-label="Pick ONE conversion from the diagram (solar panel,..."', 'data-label="One device: input, useful output, extra"')
fx('plain', 'Part B question 6 label (Gathered Answers)', 'data-label="Explain the difference between TRANSFER (last less..."', 'data-label="Transfer vs. transformation"')

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: Notice & Wonder (the black box is the warm-up’s thinking stop; its “nothing moved between objects” was confusing, since electrical energy did move in)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Notice &amp; Wonder</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: Stop & Think (the arrow tags are the thinking stop for Part 1)',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'the never-made AI picture, Key Concept, Stop & Reason, the Four Florida Conversions tap diagram, Observe & Reason, the solar Amazing Fact, the “Florida connection” (about the body, not Florida) and Go Deeper are gone (lean); the energy pipes replace the picture and the diagram, and Part 3 follows the energy back to the Sun. Next button goes to Self-Check',
   r'<div class="lesson-figure scroll-reveal">\s*<div class="lesson-figure-label">🔌 Three Devices Converting Energy</div>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 3 · Follow It Back to the Sun</h3>\n      ' + PS + 'Where did the toaster’s energy come from before it reached your kitchen? Follow it backward, one step at a time. Then follow one more device.</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its trace-a-device task is now Part C; its two Amazing Facts and Go Deeper go with it, including the wrong “LED bulbs are over 90% efficient”)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 7 removed (Bethany kept 5 and 6)', r'<div class="pq">\s*<span class="pq-num"[^>]*>7</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C typed on the page, plus the required sketch', 'A device energy map with INPUT, OUTPUT, and one wasted-energy arrow, plus a one-sentence conversion statement.',
   'My device energy map: IN, useful OUT, extra OUT and one conversion sentence. Plus your labeled sketch.')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether a toaster CREATES heat, and supported it with two pieces of evidence.',
   '<strong>Use Your Evidence:</strong> My claim about whether a toaster creates heat, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Download your field journal (it has your answers and your sketch) and upload it to the Canvas assignment. Or copy your Gathered Answers (above) into Canvas.', True)

# ---------------------------------------------------------------- the story
SAM = Q['crew']['sam']
EL = {'t': 'electrical', 'c': '#E0A100', 'icon': '⚡'}
HEAT = {'t': 'heat', 'c': '#E8636B', 'icon': '🔥'}
LIGHT = {'t': 'light', 'c': '#F2C94C', 'icon': '💡'}
MOTION = {'t': 'motion', 'c': '#2D7AA6', 'icon': '🌀'}
CHEM = {'t': 'chemical (stored in fuel)', 'c': '#8E5BB5', 'icon': '⛽'}
SUN = {'t': 'light from the Sun', 'c': '#F2994A', 'icon': '☀️'}
D = {
    'lesson': '22.01', 'week': 22, 'day': 1, 'guide': 'sam', 'prefix': 'g4sci-22-1', 'manifestKey': '22-01',
    'paths': P['paths'], 'crew': {'sam': SAM},
    'expedition': {'num': 22, 'title': 'The Beacon Went Dark'},
    'ambient': {'icon': '🌊', 'label': 'Ocean sounds'},
    'case': {
        'num': 22, 'title': 'The Beacon Went Dark', 'style': 'mariners',
        'hook': 'The light at the end of the Palmetto Beach jetty (a rock wall that sticks out into the water) went dark. Boats use it to find the harbor at night. Nobody plugs it in. So where does its energy come from?',
        'notice': {'head': 'NOTICE TO MARINERS · PALMETTO BEACH', 'title': 'JETTY LIGHT OUT',
                   'rows': [['What', 'The green light at the end of the jetty is not working.'], ['Since', 'Three nights ago'], ['Boats', 'Use extra care entering the harbor at night.']],
                   'line': 'Mariners (people who drive boats) read notices like this one.'},
        'ticket': {'head': 'Keeper’s work ticket', 'num': 'No. 22-A', 'title': 'Jetty light: checked this morning',
                   'rows': [['💡', 'LED lamp', 'Works when I test it with a spare battery', 'ok'],
                            ['🔋', 'Battery', 'Empty', 'bad'],
                            ['🔌', 'Wires', 'No breaks', 'ok'],
                            ['🔲', 'Solar panel', 'Covered in a white crust. Our pelican loves to sit on it!', 'bad']],
                   'foot': 'Sam, can you figure out what went wrong? ~ the harbor keeper'},
        'stills': [{'cam': 'A real solar harbor light', 'time': 'U.S. Coast Guard, Lake Erie', 'tag': 'PHOTO', 'kind': 'print', 'img': I('coast-guard-light'),
                    'alt': 'A real photo: two Coast Guard crew members in hard hats install a small light with a solar panel on top onto a red marker in the water.'}],
        'stillsCredit': 'U.S. Coast Guard crew installing a solar-powered LED light on Lake Erie: photo by Petty Officer 3rd Class George Degener, U.S. Coast Guard (public domain, via Wikimedia Commons).',
        'question': 'The jetty light’s lamp still works. So why did the light go dark?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'blackbox', 'icon': '📦', 'where': 'Warm-Up: the black box', 't': 'Every device takes energy IN and sends energy OUT in a different form. A device can only change the energy it gets.'},
            {'id': 'arrowtags', 'icon': '🏷️', 'where': 'The Lesson, Part 1: flip the arrow tag', 't': 'The jetty light’s solar panel CHANGES light into electrical energy, and its lamp CHANGES electrical energy back into light.'},
            {'id': 'pipes', 'icon': '🚰', 'where': 'The Lesson, Part 2: the energy pipes', 't': 'A device never makes energy and never uses it up: 10 units in, 10 units out. With 0 units in, you get 0 out. A battery only stores energy that came in.'},
            {'id': 'trace', 'icon': '☀️', 'where': 'The Lesson, Part 3: back to the Sun', 't': 'Follow the energy back far enough and it almost always starts at the Sun. The jetty light’s chain starts with sunlight hitting its panel.'},
        ],
        'solve': {
            'title': 'Why did the jetty light go dark?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'The LED lamp used up all its light.', 'why': 'Check Clue 3. Energy doesn’t get used up, and the ticket says the lamp still works.'},
                {'t': 'The battery stopped making energy.', 'why': 'Check Clue 3. A battery never makes energy. It only stores energy that came IN.'},
                {'t': 'The crust on the panel blocked the sunlight. No light went in, so no electrical energy was made, the battery emptied, and the lamp had nothing to convert.', 'right': True,
                 'why': 'Case cracked! No energy in means no energy out. The chain broke at the very first step: sunlight couldn’t reach the panel. Fill in Sam’s repair ticket just below.'},
                {'t': 'Nights are too dark for a light to work.', 'why': 'Check Clue 4. The light works at night on energy the panel collected during the day.'},
            ]},
    },
    'blackbox': {
        'afterText': 'Open three mystery boxes', 'kicker': 'Warm-Up game', 'title': 'The black box',
        'todo': ['Read what goes IN and what comes OUT.', 'Drag the device that fits onto the box (or tap the card, then the box).'],
        'why': {'icon': '📦', 'q': 'What’s a black box?', 't': 'Something you can’t see inside. You only see what goes in and what comes out, and you can still figure out a lot!'},
        'inWord': 'Goes IN', 'outWord': 'Comes OUT', 'sealWord': 'SEALED', 'nextBtn': 'Next box →', 'countWord': 'boxes opened',
        'trayLabel': 'Which device is inside?',
        'boxes': [
            {'id': 'a', 'label': 'Box A', 'in': {'icon': '🔌', 't': 'Electricity from the wall'},
             'outs': [{'icon': '🔥', 't': 'Lots of heat', 'fx': 'heat'}, {'icon': '🟠', 't': 'An orange glow', 'fx': 'glow'}, {'icon': '🔔', 't': 'A click', 'fx': 'sound'}],
             'answer': 'toaster', 'reveal': {'img': I('toaster'), 'alt': 'A real photo looking down into a running toaster: a slice of bread sits over glowing orange wires.', 'cap': 'A toaster!',
                                              'line': ' Electrical energy IN. Heat OUT (useful: it toasts the bread), plus a little light and a click.'}},
            {'id': 'b', 'label': 'Box B', 'in': {'icon': '🔌', 't': 'Electricity from the wall'},
             'outs': [{'icon': '🌬️', 't': 'Moving air', 'fx': 'spin'}, {'icon': '🔊', 't': 'A soft hum', 'fx': 'sound'}, {'icon': '♨️', 't': 'A tiny bit of warmth', 'fx': 'heat'}],
             'answer': 'fan', 'reveal': {'img': I('fan'), 'alt': 'A real photo of an electric desk fan with dark blades behind a wire cage.', 'cap': 'A desk fan!',
                                          'line': ' Electrical energy IN. Motion OUT (useful: the spinning blades push air), plus a hum and a little heat.'}},
            {'id': 'c', 'label': 'Box C', 'in': {'icon': '☀️', 't': 'Sunlight, all day'},
             'outs': [{'icon': '💡', 't': 'Light, all night', 'fx': 'glow'}],
             'answer': 'solar', 'reveal': {'img': I('solar-light'), 'alt': 'A real photo of a solar garden light on a metal stake, with a small dark solar panel on its round top.', 'cap': 'A solar garden light!',
                                            'line': ' Light IN by day. Its little panel changes it into electrical energy, a battery stores it, and at night the lamp changes it back into light. The jetty light works the same way.'}}],
        'cards': [{'id': 'toaster', 'icon': '🍞', 't': 'Toaster'}, {'id': 'fan', 'icon': '🌀', 't': 'Desk fan'}, {'id': 'solar', 'icon': '🏮', 't': 'Solar garden light'}, {'id': 'flash', 'icon': '🔦', 't': 'Battery flashlight'}],
        'misses': {
            'a': {'fan': 'A fan makes moving air. Does Box A make wind?', 'solar': 'Box A’s input is a wall plug, not sunlight.', 'flash': 'A flashlight runs on batteries, and it makes light, not LOTS of heat.'},
            'b': {'toaster': 'A toaster makes lots of heat. Box B makes moving air.', 'solar': 'Box B’s input is a wall plug, not sunlight.', 'flash': 'A flashlight makes light. Box B makes moving air.'},
            'c': {'toaster': 'A toaster needs a wall plug. Box C’s input is sunlight.', 'fan': 'A fan needs a wall plug and makes moving air.', 'flash': 'Close! But a flashlight’s energy comes from batteries you put in. Box C’s comes from the Sun.'}},
        'credit': 'Toaster: “Bread sticking out of running toaster from above” by Kansattica, CC BY 4.0. Desk fan: “Electric Fan” by Rfc1394, public domain. Solar garden light: Leon Brooks, public domain. All via Wikimedia Commons.',
        'q': 'What did every box do to the energy that went in?',
        'opts': [{'t': 'It changed the energy into a different form.', 'ok': True},
                 {'t': 'It made brand-new energy.', 'miss': 'Could the fan run if you unplugged it? Where did its energy come from?'},
                 {'t': 'It kept the energy exactly the same.', 'miss': 'Electricity went into the toaster. Did electricity come out?'}],
        'win': 'Energy IN, a different form OUT. Every device is an energy changer. Clue 1!'},
    'arrowtags': {
        'afterText': 'A flashlight converts electrical energy INTO light', 'kicker': 'Part 1 game', 'title': 'Flip the arrow tag',
        'todo': ['Tag each arrow MOVES or CHANGES: drag a tag onto it, or tap the arrow to flip it.', 'Press Check my tags.'], 'trayLabel': 'Tags',
        'why': {'icon': '🏷️', 'q': 'Moves or changes?', 't': 'MOVES = transferred: same form, it just travels. CHANGES = transformed: a new form.'},
        'tags': {'moves': {'t': 'MOVES', 'icon': '➡️'}, 'changes': {'t': 'CHANGES', 'icon': '🔄'}},
        'forms': {'motion': MOTION, 'electrical': EL, 'heat': HEAT, 'light': LIGHT, 'sound': {'t': 'sound', 'c': '#3FA37C', 'icon': '🔊'}},
        'emptyTag': '? tap me', 'checkBtn': 'Check my tags', 'countWord': 'arrows tagged', 'noneLine': 'Tag at least one arrow first: MOVES or CHANGES.',
        'scenes': [
            {'id': 'marble', 'from': {'icon': '🔵', 't': 'A rolling marble'}, 'to': {'icon': '🟠', 't': 'A still marble', 'see': 'starts rolling'}, 'a': 'motion', 'b': 'motion', 'k': 'moves',
             'why': 'Motion in, motion out. The energy MOVED from one marble to the other.', 'miss': 'The first marble was rolling. What does the second marble do? Is that a new form?'},
            {'id': 'toaster', 'from': {'icon': '🔌', 't': 'The wall plug'}, 'to': {'icon': '🍞', 't': 'A toaster', 'see': 'gets hot'}, 'a': 'electrical', 'b': 'heat', 'k': 'changes',
             'why': 'Electrical in, heat out. The energy CHANGED form.', 'miss': 'Electricity went in. Does electricity come out, or something else?'},
            {'id': 'drum', 'from': {'icon': '🥁', 't': 'A drum'}, 'to': {'icon': '👂', 't': 'Your ear', 'see': 'hears a boom'}, 'a': 'sound', 'b': 'sound', 'k': 'moves',
             'why': 'Sound traveled through the air to your ear. Same form: it MOVED.', 'miss': 'The drum made sound. What reaches your ear? Is that a new form?'},
            {'id': 'fan', 'from': {'icon': '🔌', 't': 'The wall plug'}, 'to': {'icon': '🌀', 't': 'A fan', 'see': 'blades spin'}, 'a': 'electrical', 'b': 'motion', 'k': 'changes',
             'why': 'Electrical in, motion out. The energy CHANGED form.', 'miss': 'Electricity went in. Spinning blades are what kind of energy?'},
            {'id': 'panel', 'from': {'icon': '☀️', 't': 'Sunlight'}, 'to': {'icon': '🔲', 't': 'The jetty light’s solar panel', 'see': 'sends power to the battery'}, 'a': 'light', 'b': 'electrical', 'k': 'changes',
             'why': 'Light in, electrical out. The panel CHANGED the form. That’s the jetty light’s first step!', 'miss': 'Light hits the panel. What goes out of the panel on its wires?'},
            {'id': 'lamp', 'from': {'icon': '🔋', 't': 'The jetty light’s battery'}, 'to': {'icon': '💡', 't': 'Its LED lamp', 'see': 'shines green at night'}, 'a': 'electrical', 'b': 'light', 'k': 'changes',
             'why': 'Electrical in, light out. The lamp CHANGED it back into light.', 'miss': 'The battery sends electricity. What comes out of the lamp?'}],
        'q': 'Which arrow shows a TRANSFORMATION?',
        'opts': [{'t': 'The fan: electrical energy turns into motion.', 'ok': True},
                 {'t': 'The marbles: motion passes to another marble.', 'miss': 'Did the form change, or did motion just move to the other marble?'},
                 {'t': 'The drum: sound travels to your ear.', 'miss': 'Sound went in and sound arrived. Did the form change?'}],
        'win': 'MOVES keeps the form. CHANGES makes a new form. The jetty light changes energy twice! Clue 2!'},
    'pipes': {
        'afterText': 'Test it with the energy pipes', 'kicker': 'Part 2 game', 'title': 'The energy pipes',
        'todo': ['Pick a device and drag the slider to guess.', 'Press Pour and count both pipes. Try 3 devices, including both bulbs.'],
        'why': {'icon': '🚰', 'q': 'What’s an energy unit?', 't': 'A pretend scoop of energy, so we can count it. Sam’s numbers are about right for real devices.'},
        'model': 'a model (numbers are about right)', 'units': 10, 'inWord': 'IN', 'useWord': 'USEFUL', 'xtraWord': 'EXTRA',
        'guessQ': 'Guess first: of {n} units, how many come out USEFUL?', 'pourBtn': 'Pour in 10 units', 'nextBtn': 'Try another device →',
        'usefulWord': 'useful', 'extraWord': 'extra', 'outWord': 'units out', 'exactLine': 'Your guess was exactly right! ', 'closeLine': 'Close guess! ', 'farLine': 'A surprise! ',
        'devices': [
            {'id': 'toaster', 'icon': '🍞', 't': 'Toaster', 'inF': EL, 'use': {'t': 'heat in the bread', 'c': '#E8636B', 'icon': '🍞', 'n': 6}, 'xtra': {'t': 'heat in the air, glow, click', 'c': '#B98A7A', 'icon': '♨️', 'n': 4},
             'note': 'Most of it becomes heat, but not all of that heat goes into the bread. Some warms the kitchen air.'},
            {'id': 'oldbulb', 'icon': '💡', 't': 'Old bulb', 'inF': EL, 'use': {'t': 'light', 'c': '#F2C94C', 'icon': '💡', 'n': 1}, 'xtra': {'t': 'heat', 'c': '#E8636B', 'icon': '🔥', 'n': 9},
             'note': 'An old-style bulb turns only about 1 of every 10 units into light. The rest becomes heat. That’s why old bulbs get so hot!'},
            {'id': 'led', 'icon': '🔆', 't': 'LED bulb', 'inF': EL, 'use': {'t': 'light', 'c': '#F2C94C', 'icon': '💡', 'n': 4}, 'xtra': {'t': 'heat', 'c': '#E8636B', 'icon': '🔥', 'n': 6},
             'note': 'An LED turns much more of its energy into light, so it needs much less energy for the same brightness.'},
            {'id': 'car', 'icon': '🚗', 't': 'Gas car', 'inF': CHEM, 'use': {'t': 'motion', 'c': '#2D7AA6', 'icon': '🌀', 'n': 2}, 'xtra': {'t': 'heat, sound', 'c': '#E8636B', 'icon': '🔥', 'n': 8},
             'note': 'A gas car turns only about 2 of every 10 units into motion. Most becomes heat in the engine.'},
            {'id': 'solar', 'icon': '🔲', 't': 'Solar panel', 'inF': {'t': 'light', 'c': '#F2994A', 'icon': '☀️'}, 'use': {'t': 'electrical', 'c': '#E0A100', 'icon': '⚡', 'n': 2}, 'xtra': {'t': 'heat, bounced light', 'c': '#E8636B', 'icon': '🔥', 'n': 8},
             'note': 'A solar panel turns about 2 of every 10 units of sunlight into electrical energy. The rest warms the panel or bounces off.'}],
        'need': ['oldbulb', 'led'], 'needCount': 3, 'needLine': 'Try at least 3 devices, including the old bulb and the LED bulb.',
        'tableLabel': 'My pipe log', 'cols': ['Device', 'My guess', 'Useful', 'Extra', 'Total out'],
        'q': '10 units of energy went into the old bulb. How many units came out?',
        'opts': [{'t': '10: 1 as light and 9 as heat.', 'ok': True},
                 {'t': '1, because only the light counts.', 'miss': 'The heat came out too! Count every unit in both pipes.'},
                 {'t': '0, because the bulb used it all up.', 'miss': 'Look at your pipe log. Did the units disappear, or come out in a new form?'}],
        'win': 'Nothing used up, nothing made: 10 in, 10 out, every time. So 0 in means 0 out! Clue 3!'},
    'trace': {
        'afterText': 'Then follow one more device', 'kicker': 'Part 3 game', 'title': 'Follow it back to the Sun',
        'todo': ['Start with the hot toast. Each right answer takes one step backward.', 'Keep going until the trail can’t step back any more. Then follow 1 more device.'],
        'why': {'icon': '☀️', 'q': 'Why go backward?', 't': 'Every device gets its energy from somewhere. Going backward shows where it started.'},
        'pick': 'Pick a device:', 'need': 2, 'countWord': 'devices traced to the start', 'anotherBtn': 'Follow another device →',
        'empty': '👆 Pick a device to start your trail.', 'arrowNote': 'The arrows show which way the energy moved: from the start to your device.',
        'foods': [
            {'id': 'toast', 'icon': '🍞', 'name': 'Hot toast', 'steps': [
                {'q': 'The toast got its heat from the toaster. Where did the toaster get its energy?', 'opts': [
                    {'t': '🔌 Electrical energy through the wires', 'icon': '🔌', 'short': 'Wires', 'ok': True},
                    {'t': '🍞 From the bread', 'miss': 'The bread got hot, but bread doesn’t power the toaster. What does the toaster plug into?'},
                    {'t': '✨ It made the energy itself', 'miss': 'Devices can’t make energy (Clue 3!). What goes INTO a toaster?'}]},
                {'q': 'Where did the electricity in the wires come from?', 'opts': [
                    {'t': '🔋 A battery in the wall', 'miss': 'There’s no battery in your wall. The wires run a long way, to a big building.'},
                    {'t': '🏭 A power plant', 'icon': '🏭', 'short': 'Power plant', 'ok': True},
                    {'t': '🌩 Lightning', 'miss': 'Lightning is electrical, but nobody catches it to run toasters. Where do the power lines lead?'}]},
                {'q': 'Most of Florida’s electricity comes from power plants that burn natural gas. Where did natural gas come from?', 'opts': [
                    {'t': '🦠 Tiny sea living things, buried for millions of years', 'icon': '🦠', 'short': 'Ancient sea life', 'ok': True},
                    {'t': '🏭 A factory makes it', 'miss': 'People pump natural gas from deep underground. What turned into gas down there?'},
                    {'t': '🌬 Air', 'miss': 'Natural gas is pumped from deep underground, not from the air.'}]},
                {'q': 'Those tiny sea living things needed energy to grow. Where did it come from?', 'opts': [
                    {'t': '🌊 The waves', 'miss': 'Waves moved them around, but many of them made their own food, like plants do. What do plants use?'},
                    {'t': '☀️ Sunlight: they made food from it, like plants', 'icon': '☀️', 'short': 'Sun', 'ok': True},
                    {'t': '🪨 The sand', 'miss': 'Sand has no food energy. What do plant-like living things use to make food?'}]}],
             'end': 'Your toast’s heat started as sunlight, millions of years ago! It was stored in tiny sea living things, then natural gas, then turned into electricity, then heat.'},
            {'id': 'fan', 'icon': '🌀', 'name': 'A ceiling fan', 'steps': [
                {'q': 'Where does the fan get its energy?', 'opts': [
                    {'t': '🔌 Electrical energy through the wires', 'icon': '🔌', 'short': 'Wires', 'ok': True},
                    {'t': '🌬 The wind outside', 'miss': 'The fan MAKES moving air. What does it plug into?'},
                    {'t': '🧲 Magnets make the energy', 'miss': 'A fan’s motor has magnets, but they don’t make energy. What goes INTO the fan?'}]},
                {'q': 'This fan’s home has solar panels on the roof. Where did the panels get their energy?', 'opts': [
                    {'t': '☀️ Sunlight', 'icon': '☀️', 'short': 'Sun', 'ok': True},
                    {'t': '🌧 Rain', 'miss': 'Rain can make panels dirty! What do solar panels change into electricity?'},
                    {'t': '🌡 Hot air', 'miss': 'Heat actually makes panels work a little worse. What lands on a panel?'}]}],
             'end': 'Sunlight to panel to wires to fan: a short chain, and it still starts at the Sun.'},
            {'id': 'bike', 'icon': '🚲', 'name': 'You, riding a bike', 'steps': [
                {'q': 'Your legs push the pedals. Where do your muscles get their energy?', 'opts': [
                    {'t': '🥣 Food: your breakfast cereal', 'icon': '🥣', 'short': 'Cereal', 'ok': True},
                    {'t': '😴 Sleep', 'miss': 'Sleep helps you rest, but it doesn’t give your body energy to use. What do you eat?'},
                    {'t': '🚲 The bike', 'miss': 'The bike gets its motion from YOU. Where does your energy come from?'}]},
                {'q': 'Cereal is made from grain, like wheat or corn. Where did those plants get their energy?', 'opts': [
                    {'t': '🟫 The soil', 'miss': 'Plants take in water and minerals from soil, but their energy comes from somewhere else. Look up!'},
                    {'t': '☀️ They made food from sunlight', 'icon': '☀️', 'short': 'Sun', 'ok': True},
                    {'t': '💧 Water', 'miss': 'Plants need water, but water has no food energy. What else do plants need?'}]}],
             'end': 'Sunlight to wheat to cereal to your muscles to the bike. YOU are an energy changer, too!'},
            {'id': 'beacon', 'icon': '🟢', 'name': 'The jetty light', 'steps': [
                {'q': 'At night, where does the jetty light’s lamp get its energy?', 'opts': [
                    {'t': '🔋 Its battery', 'icon': '🔋', 'short': 'Battery', 'ok': True},
                    {'t': '🌙 The Moon', 'miss': 'Moonlight is much too dim to power a lamp. What is stored inside the light?'},
                    {'t': '🌊 The waves', 'miss': 'The waves splash the jetty, but nothing catches their energy here. Look at the keeper’s ticket.'}]},
                {'q': 'The battery only stores energy. Where did its energy come from?', 'opts': [
                    {'t': '🔲 The solar panel, during the day', 'icon': '🔲', 'short': 'Solar panel', 'ok': True},
                    {'t': '🔋 Batteries make their own energy', 'miss': 'A battery can’t make energy (Clue 3). What fills it up each day?'},
                    {'t': '💡 The lamp', 'miss': 'The lamp USES the battery’s energy. What fills the battery?'}]},
                {'q': 'And the solar panel got its energy from…', 'opts': [
                    {'t': '☀️ Sunlight', 'icon': '☀️', 'short': 'Sun', 'ok': True},
                    {'t': '🐦 The pelican', 'miss': 'The pelican only blocks the panel! What should be landing on it?'},
                    {'t': '🌊 Salt water', 'miss': 'Salt spray just makes the crust worse. What should reach the panel?'}]}],
             'end': 'Sun to panel to battery to lamp. If sunlight can’t reach the panel, the whole chain breaks!'}],
        'twist': {'icon': '🌞', 'head': 'Almost every chain starts at the Sun!', 't': ' Food, natural gas, oil, wind and solar power all trace back to sunlight. A few don’t: nuclear power plants (Florida has some) and the heat deep inside Earth start somewhere else.'},
        'q': 'What did every chain you followed have in common?',
        'opts': [{'t': 'It started with sunlight.', 'ok': True},
                 {'t': 'It started at a power plant.', 'miss': 'Look at the left end of your trails. Was there a power plant in the bike chain?'},
                 {'t': 'It started with a battery.', 'miss': 'Look at the left end of your trails. What is always there?'}],
        'win': 'From the Sun to your toast! The jetty light’s chain starts with sunlight on its panel, too. Clue 4!'},
    'exploreMod': 'trace',
    'repair': {
        'after': '.fs-solve', 'kicker': 'Case closed · fill in the repair ticket', 'title': 'Sam’s repair ticket',
        'todo': ['Tap the link in the jetty light’s chain that broke.', 'Pick the best fix.', 'Stamp the ticket FIXED.'],
        'lockLine': 'Crack the case first. Then fill in the repair ticket.',
        'chain': [{'id': 'sun', 'icon': '☀️', 't': 'Sunlight', 'sub': 'light'}, {'id': 'panel', 'icon': '🔲', 't': 'Solar panel', 'sub': 'light → electrical'},
                  {'id': 'battery', 'icon': '🔋', 't': 'Battery', 'sub': 'stores it'}, {'id': 'lamp', 'icon': '💡', 't': 'LED lamp', 'sub': 'electrical → light'}, {'id': 'boats', 'icon': '🚤', 't': 'Boats see it', 'sub': 'light'}],
        'broken': 'panel', 'brokenQ': '1. Tap the link where the chain broke.',
        'brokenMiss': {'sun': 'The Sun was shining every day. Something stopped the light from getting IN.', 'battery': 'The battery was empty, but why? Nothing was filling it.',
                       'lamp': 'The ticket says the lamp works with a spare battery.', 'boats': 'The boats are fine. They just can’t see a light!'},
        'brokenLine': 'The panel! Salt crust and pelican droppings blocked the sunlight, so the panel couldn’t change light into electrical energy.',
        'fixQ': '2. What is the best fix?',
        'fixes': [{'t': 'Clean the panel, and put a perch post next to it for the pelican.', 'ok': True},
                  {'t': 'Put in a brighter lamp.', 'miss': 'A brighter lamp still gets 0 units in. Fix the first link!'},
                  {'t': 'Add a second battery.', 'miss': 'Two empty batteries are still empty. What needs to fill them?'}],
        'ticket': {'head': 'Repair ticket', 'num': 'No. 22-A', 'rows': [['What broke', 'Light couldn’t get into the solar panel.'], ['The fix', '{fix}'], ['Test', 'Panel charged the battery all day. Lamp on all night.']]},
        'stampBtn': 'Stamp it FIXED', 'stamp': 'FIXED', 'sign': 'Signed: Sam Park, engineer',
        'win': 'FIXED! The jetty light shines green again, and the pelican has its own perch.'},
    'harbor': {
        'after': '.fs-solve', 'kicker': 'Bonus game · unlocked after the case', 'title': 'Light the harbor',
        'todo': ['Read each night job.', 'Pick the device you think fits best.', 'Can you get 3 stars on every job?'],
        'lockLine': 'Crack the case first. Then this game opens.', 'starsWord': 'stars',
        'jobs': [
            {'id': 'dock', 'icon': '🛶', 't': 'Light the dock path all night. There are no wires out there.', 'picks': [
                {'icon': '🏮', 't': 'Solar path lights', 'chain': 'light → electrical (stored) → light', 'stars': 3, 'line': 'Perfect: no wires, and they charge themselves every sunny day.'},
                {'icon': '🔦', 't': 'Battery flashlights', 'chain': 'chemical (battery) → light', 'stars': 2, 'line': 'They work, but someone has to change the batteries all the time.'},
                {'icon': '🍞', 't': 'A toaster', 'chain': 'electrical → heat', 'stars': 1, 'line': 'Mostly heat, a tiny glow, and it needs a wall plug. Not a light!'}]},
            {'id': 'fog', 'icon': '🌫️', 't': 'Warn boats on a foggy night, when lights are hard to see.', 'picks': [
                {'icon': '📯', 't': 'A foghorn', 'chain': 'electrical → sound', 'stars': 3, 'line': 'Sound travels through fog, so boats hear it even when they can’t see.'},
                {'icon': '💡', 't': 'A brighter light', 'chain': 'electrical → light', 'stars': 2, 'line': 'It helps a little, but thick fog blocks light.'},
                {'icon': '🌀', 't': 'A big fan', 'chain': 'electrical → motion', 'stars': 1, 'line': 'Moving air won’t warn a boat far away.'}]},
            {'id': 'storm', 'icon': '⛈️', 't': 'Keep the keeper’s radio working through a cloudy, stormy week.', 'picks': [
                {'icon': '🔄', 't': 'A hand-crank radio', 'chain': 'motion (your arm) → electrical → sound', 'stars': 3, 'line': 'Turn the crank: your own motion powers it, sun or no sun.'},
                {'icon': '🏮', 't': 'A solar radio', 'chain': 'light → electrical → sound', 'stars': 2, 'line': 'Great on sunny days, but a cloudy week gives it very little energy.'},
                {'icon': '🔥', 't': 'A campfire', 'chain': 'chemical (wood) → heat, light', 'stars': 1, 'line': 'Warm, but it can’t run a radio, and the rain puts it out.'}]}],
        'win': '9 stars! You matched each job to the right energy change. Next lesson, you design a device of your own.'},
    'fold': {'harbor': {'icon': '⚓', 'tease': 'Three night jobs at the harbor. Pick the best device for each, and earn 3 stars.', 'open': 'Play'}},
    'tool': {
        'name': 'Plug-in watt meter', 'icon': '🔌', 'tab': 'assignment', 'after': '#tab-assignment .activity-card', 'key': '22-tool', 'sim': 'wattmeter',
        'kicker': 'Bonus · Tool of the Week', 'teaser': 'Plug in a lamp, a fan, a toaster and more. How much energy goes IN?',
        'done': 'You measured every device. A watt meter sticker is in your Field Notebook.',
        'why': {'icon': '🔌', 'q': 'What does a watt meter do?', 't': 'You plug it into the wall, then plug a device into it. Its screen shows how fast the device takes in electrical energy, in units called watts (W).'},
        'wattmeter': {
            'title': 'How much energy goes IN?', 'model': 'a model', 'aboutWord': 'about', 'unitWord': 'watts',
            'todo': ['Tap a device to plug it into the meter.', 'Read the watts on the screen.', 'Plug in all 6. Your watt bars build themselves.'],
            'ladderLabel': 'Watts going IN (more watts = energy goes in faster)',
            'pairLine': 'The old bulb and the LED make about the SAME amount of light. The old bulb needs about 60 watts. The LED needs about 9!',
            'loads': [
                {'k': 'phone', 'icon': '📱', 't': 'Phone charger', 'w': 5, 'note': 'A small trickle: electrical energy IN, stored in the phone’s battery.'},
                {'k': 'led', 'icon': '🔆', 't': 'LED bulb', 'w': 9, 'same': True, 'note': 'Bright light for only a few watts, because less of its energy turns into heat.'},
                {'k': 'fan', 'icon': '🌀', 't': 'Desk fan', 'w': 30, 'note': 'Electrical IN, motion OUT (plus a hum and a little heat).'},
                {'k': 'oldbulb', 'icon': '💡', 't': 'Old bulb', 'w': 60, 'same': True, 'note': 'The same brightness as the LED, but much more energy goes in, and most of it comes out as heat.'},
                {'k': 'tv', 'icon': '📺', 't': 'TV', 'w': 100, 'note': 'Electrical IN, light and sound OUT (and some heat out the back).'},
                {'k': 'toaster', 'icon': '🍞', 't': 'Toaster', 'w': 900, 'note': 'Huge! Making heat fast takes lots of energy. Never touch a toaster’s wires.'}],
            'q': {'q': 'The old bulb and the LED make the same light. Why does the old bulb need so many more watts?',
                  'opts': [{'t': 'Most of its energy comes out as heat instead of light.', 'ok': True, 'why': 'Right! The LED wastes less as heat, so it needs much less energy for the same light.'},
                           {'t': 'It makes more light.', 'why': 'They make about the same light. Where does the rest of the old bulb’s energy go?'},
                           {'t': 'It uses up the energy faster.', 'why': 'Energy doesn’t get used up. It changes form. What form, besides light?'}]}}},
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Think about the energy pipes: 10 units in, 10 units out. Did anything get used up?', 'C': 'That’s energy moving (transfer). What’s different about conversion?'},
        'q2': {'A': 'The turbine’s blades turn a machine inside it. What kind of energy goes out on its wires?', 'B': 'A little heat comes out, but that’s extra. What’s the useful output?'},
        'q3': {'B': 'What did the toaster’s owner want: toast or a click?', 'C': 'The input is what goes IN. Is the click going in or coming out?'}},
    'flags': {
        'ans-1': [
            {'label': 'the input', 're': 'input|in |into|goes in|electric|chemical|gas|fuel|light|sun|plug'},
            {'label': 'the useful output', 're': 'output|out|light|heat|motion|electric|move|moving|useful'},
            {'label': 'extra energy', 're': 'extra|waste|also|heat|sound|warm|hot|click|bounce'}],
        'ans-2': [
            {'label': 'transfer', 're': 'transfer|move|moves|moved|travel|pass|same form|stays'},
            {'label': 'transformation', 're': 'transform|chang|convert|different form|new form|turns into|becomes'},
            {'label': 'an example', 're': 'marble|ball|drum|ear|sound|toaster|fan|bulb|flash|panel|solar|car|lamp|light'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|doesn|does not|didn|create|make|made'},
            {'label': 'two pieces of evidence', 'any': ['pipe', 'unit', '10', 'ten', 'electric', 'plug', 'wire', 'change', 'chang', 'convert', 'form', 'used up', 'box', 'sun', 'battery', 'jetty', 'heat', 'input', 'in '], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-1': 15, 'ans-2': 15, 'cer-4': 30},
    'hints': {
        'ans-1': ['Pick one: toaster, old bulb, LED bulb, gas car or solar panel.', 'What went IN? What came out USEFUL? What else came out?', 'Try: The ___ takes in ___ energy. Its useful output is ___. It also makes extra ___.'],
        'ans-2': ['Transfer = energy moves. Transformation = energy changes form.', 'Think about the arrow tags: the marbles and the fan.', 'Try: In a transfer, energy ___, like ___. In a transformation, energy ___, like ___.'],
        'cer-4': ['First decide: does a toaster MAKE heat out of nothing?', 'Think about what goes into a toaster, and about the energy pipes.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'The toaster only works when it’s plugged in. Electrical energy goes IN.',
                'In the energy pipes, 10 units went in and 10 came out, every time.',
                'Unplug it, and no heat comes out. 0 in means 0 out.',
                'Toast gets brown and crunchy.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · the jetty light', 'length': '20–30 s'},
        'warmup': {'label': 'Warm-Up · the black box (Clue 1)', 'length': '20–30 s',
                   'script': 'Hi, it’s Sam. The jetty light is out. Read the notice, then the keeper’s ticket. The lamp works, but the battery is empty. Nobody plugs this light in! To figure it out, open three black boxes. Read what goes in and what comes out, then drag the right device onto each box.'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Hold up a lamp plug for “input”, switch on a lamp for “output”.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · flip the arrow tag (Clue 2)', 'length': '20–30 s'},
        'part2': {'label': 'Part 2 · the energy pipes (Clue 3)', 'length': '20–30 s',
                  'script': 'Time to count energy. Pick a device, then drag the slider to guess how many units come out useful. Press pour, and count both pipes. Try the old bulb, then the LED. Where did the energy go? Did any disappear?'},
        'explore': {'label': 'Part 3 · back to the Sun (Clue 4)', 'length': '25–35 s',
                    'script': 'Let’s go backward. Start with the hot toast. Pick the answer for each step, and watch your trail grow. Wires, a power plant, then what? Keep going until you can’t go back any further. Then follow one more device. Look at the start of every trail.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · my device energy map', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says a toaster creates heat. Does it? Think about the energy pipes, and what goes into a toaster. Pick your side, tap two pieces of evidence, then explain how they prove your claim. That’s your C-E-R.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 22.02 (design your own device).'},
    },
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'A black box, opened (Warm-Up)',
        'An arrow that CHANGES color (The Lesson)',
        'Your pipe log (The Lesson)',
        'A trail that ends at the Sun (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['A device and its energy arrows', 'The jetty light’s energy chain', 'A toaster: IN and OUT'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch and label your device', 'required': True, 'minLabels': 3,
                           'prompts': ['Draw your device', 'Label the energy going IN', 'Label the useful and the extra energy coming OUT']}]},
    'hlCoach': copy.deepcopy(Q['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🪶', 'name': 'A pelican feather from the solar panel',
                 'line': 'You cracked Case 22, and a pelican feather from the jetty light’s panel goes in your Field Notebook. (A specimen is something a scientist collects to keep.) Next time: design your own device.'},
    'notebookTitle': 'Unit 5 · Energy, Motion & Collisions',
    'notebook': copy.deepcopy(O['notebook']),
    'rankLine': P['rankLine'],
    'lensVoice': False,
    'lensWin': 'All six words are in focus. Time to follow the energy!',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '#tab-vocab p', 'text': 'look around your home for three more devices'},
         'label': 'Warm-Up: three devices at home', 'q': 'Warm-Up: Three devices at home. What goes IN? What comes OUT?', 'title': 'Three devices at home', 'compact': True,
         'fields': [{'t': 'Device 1', 'icon': '1️⃣', 'ph': 'A ___: ___ energy IN, ___ energy OUT'},
                    {'t': 'Device 2', 'icon': '2️⃣', 'ph': 'A ___: ___ energy IN, ___ energy OUT'},
                    {'t': 'Device 3', 'icon': '3️⃣', 'ph': 'A ___: ___ energy IN, ___ energy OUT'}]},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to see what it means.']},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Map its energy below'},
         'label': 'Part C: My device energy map', 'q': 'Part C: My device energy map (IN, useful OUT, extra OUT, one conversion sentence)', 'title': 'My device energy map',
         'fields': [{'t': 'My device', 'icon': '⚙️', 'ph': 'My device is a ___.'},
                    {'t': 'Energy that goes IN', 'icon': '📥', 'ph': '___ energy goes in.'},
                    {'t': 'Useful energy that comes OUT', 'icon': '⭐', 'ph': 'The useful output is ___ energy.'},
                    {'t': 'Extra energy that comes OUT', 'icon': '♨️', 'ph': 'It also makes extra ___.'},
                    {'t': 'My conversion sentence', 'icon': '🔄', 'ph': 'My device converts ___ energy into ___ energy.', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Does a toaster CREATE heat energy?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-1': 'Part B · Question 5', 'ans-2': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] == '22.01': n.update({'icon': '🪶', 'name': 'A pelican feather from the solar panel'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'A device converts the energy that goes in into a different form, and the energy is never used up.',
    'key': ['device', 'converts', 'energy', 'different', 'form', 'never', 'used'],
    'small': ['A', 'the', 'that', 'into', 'and', 'is'],
    'model': 'A scientist might highlight “device converts”, “different form” and “never used up”. Those words hold the big idea. Small words like “a” and “the” don’t carry the idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me explain how energy changes from one form into another?']

# ---------------------------------------------------------------- Spotlight: what lights up as Sam talks (4 clips: warmup, part2, explore, evidence)
EV = '#tab-assignment .act-body > div:has(> .fs-plan)'
D['cues'] = {
    'warmup': [{'at': '^notice', 'sel': '.fs-casecard .fs-notice', 'fx': 'glow'},
               {'at': '^ticket', 'sel': '.fs-casecard .fs-wkt', 'fx': 'pop'},
               {'at': '^empty', 'sel': '.fs-casecard .fs-wkt li.bad', 'i': 0, 'fx': 'wiggle'},
               {'at': '^boxes', 'sel': '.fs-bbx-box', 'fx': 'glow', 'tag': 'Black box', 'scroll': True},
               {'at': '^drag', 'sel': '.fs-bbx-cards', 'fx': 'point'}],
    'part2': [{'at': '^device', 'sel': '.fs-pip-tabs', 'fx': 'pop', 'scroll': True},
              {'at': '^slider', 'sel': '.fs-pip-split', 'fx': 'glow'},
              {'at': '^pour', 'sel': '.fs-pip-pour', 'fx': 'point'},
              {'at': '^pipes', 'sel': '.fs-pip-svg', 'fx': 'glow'},
              {'at': '^LED', 'sel': '.fs-pip-tab', 'i': 2, 'fx': 'pop'}],
    'explore': [{'at': '^toast', 'sel': '.fs-tc-picks .fs-in-chip', 'i': 0, 'fx': 'pop', 'scroll': True},
                {'at': '^trail', 'sel': '.fs-tc-trail', 'fx': 'glow'},
                {'at': '^further', 'sel': '.fs-tc-stage', 'fx': 'glow'},
                {'at': '^device$', 'sel': '.fs-tc-picks', 'fx': 'pop'},
                {'at': '^start', 'sel': '.fs-tc-trail', 'fx': 'trace'}],
    'evidence': [{'at': '^classmate', 'sel': EV + ' > p', 'i': 0, 'fx': 'trace', 'scroll': True},
                 {'at': '^pipes', 'sel': '.fs-plan .fs-opt', 'i': 3, 'fx': 'glow'},
                 {'at': '^side', 'sel': '.fs-plan .fs-plan-row', 'i': 0, 'fx': 'pop'},
                 {'at': '^explain', 'sel': '.fs-cer .fs-cer-row', 'i': 2, 'fx': 'glow', 'scroll': True}],
}
D['cueWords'] = json.load(open('cuewords.json', encoding='utf-8')) if os.path.exists('cuewords.json') else {}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
