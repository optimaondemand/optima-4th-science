#!/usr/bin/env python3
"""Writes data.json and fixes.json for 12.02 (run from this folder)."""
import json, copy
P = json.load(open('../12-01/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

# ---------------------------------------------------------------- ticked fixes (Bethany, 16 Oct 2026)
fx('fix', 'quarter label: week 12 is Quarter 2', 'Q3 &middot; Week 12', 'Q2 &middot; Week 12')
fx('fix', 'quarter label in the footer', 'Science &middot; Quarter 3 &middot;', 'Science &middot; Quarter 2 &middot;')
fx('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist asks for two pathway models', '🎨 Part C &mdash; Build Your Own Food Chain', '🎨 Part C &mdash; Build Two Pathway Models')
fx('fix', 'copy-paste leftover: Part C task from 9.01',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   'Pick two different Florida animals that use <strong>different senses</strong> (not the bat or the eagle). Build a pathway model for each one: stimulus → sense organ → brain → response. Then compare them.</p>', True)
fx('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'accuracy: a black bear’s smelling area is about 100 times bigger than a person’s (NPS); “hundreds of times more scent cells” isn’t supported',
   "the bear's nose, which has hundreds of times more scent cells than yours", "the bear's nose, whose smelling area is about 100 times bigger than yours")
fx('fix', 'accuracy: Florida’s sea turtles don’t hunt fish (green turtles eat plants; loggerheads eat crabs and jellyfish)',
   r'In your notebook, predict: imagine a bald eagle and a sea turtle each notice a fish\..*?</p>',
   '<strong>Predict:</strong> an eagle notices a fish, and a sea turtle notices a jellyfish. Which step will change the most between them?</p>', True)

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter; dashes removed',
   "Hold this question in your head as you work. By the end of the lesson, you'll build <strong>two</strong> response models for two different Florida animals — and compare them to see what the same four steps look like in two very different lives.",
   "Keep this question in mind. By the end, you'll build pathway models for different Florida animals and compare them: same four steps, very different lives.")
fx('plain', 'shorter', "Today the question is: <em>do all animals do them the same way?</em>", "Today's question: <em>do all animals do them the same way?</em>")
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', 'shorter; dash removed', "shows them in order, with arrows that explain what happens at each step. The strongest models include:",
   "shows them in order, with arrows between the steps. The strongest models have:")
fx('plain', 'dashes removed', '</strong> — showing what the animal noticed.', '</strong>: what the animal noticed.')
fx('plain', 'dashes removed', '</strong> — labeled "signal" to show information traveling.', '</strong>, labeled "signal": the message traveling inside the body.')
fx('plain', 'dashes removed', '</strong> — showing what the brain decided.', '</strong>: what the brain decided.')
fx('plain', 'shorter', 'The four steps stay the same, but the <em>details</em> change a lot between animals. Two Florida examples that look totally different — but follow the same pathway:',
   'The four steps stay the same, but the <em>details</em> change a lot. Here are two Florida hunters that look totally different but follow the same pathway:')
fx('plain', '“calculates” → plain words', "brain calculates where the moth is (process)", "brain works out where the moth is (process)")
fx('plain', '“universal” → plain words', "Totally different ways of doing it. That's why scientists like to build <em>multiple</em> models — comparing them shows what's universal and what's special to each animal.",
   "Totally different ways of doing it. Comparing models shows what is the same for every animal and what is special to each one.")
fx('cut', 'lean: the “misconception” paragraph (good enough models) is extra reading; the games carry the idea',
   r'\s*<p><strong>Common misconception:</strong>.*?</p>', '', True)
fx('cut', 'lean: Stop & Reason repeats Match the sense (Part 3)', r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('plain', 'dash removed', 'only shows <em>stimulus → response</em> — no middle steps.', 'only shows <em>stimulus → response</em>, with no middle steps.')
fx('plain', 'shorter caption', '<strong>Same four steps, two different animals.</strong> The labels match — but the stimulus, sense organ, and response look very different between the two pathways.',
   '<strong>Same four steps, two different animals.</strong> The step names match, but the stimulus, sense organ and response look very different.')
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'Part B question 5: the four animals now live in Part 3', 'Pick one of the four Florida animals from the diagram (bat, anhinga, bear, or crab).', 'Pick one of the four Florida animals from Part 3 (bat, anhinga, bear, or crab).')
fx('plain', '“module” → “week”; dash removed',
   " Next module, you'll switch gears from <em>behavior</em> to <em>family</em>: how Florida plants and animals pass traits to their offspring — and which traits the environment shapes along the way.",
   " Next week, you'll switch from <em>behavior</em> to <em>families</em>: how Florida plants and animals pass traits to their young, and which traits the world around them shapes.")

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (building and comparing two models moves to Part C; the fixing game is Part 4)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: the Key Concept box repeats Part 1', r'<div style="background:#FFF6E5;border:2.5px solid #F0C97A;[^"]*">\s*<div[^>]*>⭐ Key Concept</div>.*?</div>\s*', '', True)
fx('cut', 'lean: the diagram heading becomes Part 3 (Match the sense replaces the tap diagram)',
   'margin-top:22px;">Four Pathway Models to Study</h3>', 'margin-top:22px;">Part 3 · Four Florida Pathways</h3>')
fx('cut', 'lean: Observe & Reason, the bat fact (shaky), the Florida callout and Go Deeper at the end of the Lesson; Part 4 = fix the broken models; next button goes to Self-Check',
   r'<div class="socratic-q">\s*<span class="sq-icon">👀</span>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 4 · Fix the Broken Models</h3>\n      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">Last night, volunteers at the field station drew models of Florida animals. Some models are broken: a step is missing. Find what’s wrong, fix it, and run it.</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 6 removed (Bethany kept 5 and 7; the CER asks almost the same thing)', r'<div class="pq">\s*<span class="pq-num"[^>]*>6</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: Part B question 7 is now number 6', '<span class="pq-num" style="background:#D4772C;">7</span>', '<span class="pq-num" style="background:#D4772C;">6</span>')
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C typed on the page; the sketch is a bonus',
   'Two complete pathway models (four boxes each, all arrows present) plus two comparison sentences underneath.',
   'Two pathway models (all four steps each) and two sentences comparing them. (A sketch is a bonus.)')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether one pathway model is enough, and supported it with two pieces of evidence from the lesson.',
   '<strong>Use Your Evidence:</strong> My claim about whether one pathway model is enough, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', True)

# ---------------------------------------------------------------- data
SLOTS4 = [{'k': 'stim', 'icon': '⚡', 't': 'Stimulus'}, {'k': 'sense', 'icon': '👂', 't': 'Sense organ'},
          {'k': 'brain', 'icon': '🧠', 't': 'Brain'}, {'k': 'resp', 'icon': '🏃', 't': 'Response'}]
CR = {
    'bat': 'Florida bonneted bat, Shalana Gray, via Wikimedia Commons (CC BY-SA 4.0)',
    'moth': 'Moth by a porch light, Fir0002, via Wikimedia Commons (CC BY-SA 3.0)',
    'house': 'Bat house at Moccasin Lake Nature Park, Clearwater, Florida, MatthewHoobin, via Wikimedia Commons (CC0)',
    'eagle': 'Bald eagle at Kennedy Space Center, Florida, NASA/Gary Rothstein, via Wikimedia Commons (public domain)',
    'bear': 'Florida black bear on a remote camera, Florida Fish and Wildlife Conservation Commission, via Wikimedia Commons (public domain)',
    'crab': 'Blue crab, NOAA, via Wikimedia Commons (public domain)',
    'anhinga': 'Anhinga swimming, Wknight94, via Wikimedia Commons (CC BY-SA 3.0)',
}
ANIMALS = [
    {'id': 'bat', 'name': 'Florida bonneted bat', 'img': 'images/12-02-bat.jpg', 'alt': 'A Florida bonneted bat’s face, with very large, rounded ears.',
     'stim': 'Echoes of its own clicks bouncing off a moth', 'sense': '👂 Big ears', 'brain': 'Works out where the moth is', 'resp': 'Swoops and grabs the moth',
     'missAny': 'An echo is a sound. Which body part picks up sound?'},
    {'id': 'anhinga', 'name': 'Anhinga', 'img': 'images/11-02-kit-anhinga.jpg', 'alt': 'An anhinga swimming low in the water with its long neck and pointed beak showing.',
     'stim': 'A small fish moving underwater', 'sense': '👁 Sharp eyes', 'brain': 'Decides “a fish to eat!” and aims its head', 'resp': 'Spears the fish with its beak',
     'missAny': 'A fish moving is something you see. Which body part picks up light?'},
    {'id': 'bear', 'name': 'Florida black bear', 'img': 'images/12-02-bear.jpg', 'alt': 'A Florida black bear standing among saw palmettos in the woods.',
     'stim': 'The smell of ripe saw palmetto berries', 'sense': '👃 A powerful nose', 'brain': 'Decides “food!” and which way to go', 'resp': 'Follows the smell to the berries',
     'missAny': 'A smell drifts on the air. Which body part picks up smells?'},
    {'id': 'crab', 'name': 'Blue crab', 'img': 'images/12-02-crab.jpg', 'alt': 'A blue crab with bright blue claws on wet mud.',
     'stim': 'A tiny shake in the water from something coming close', 'sense': '〰️ Feelers (antennae)', 'brain': 'Decides “danger!”', 'resp': 'Raises its claws or scoots sideways to hide',
     'missAny': 'A shake in the water is felt, like a touch. Which body part feels it?'},
]
D = {
    'lesson': '12.02', 'week': 12, 'day': 2, 'guide': 'lena', 'prefix': 'g4sci-12-2', 'manifestKey': '12-02',
    'paths': P['paths'], 'crew': P['crew'],
    'expedition': {'num': 12, 'title': 'The Silent Camera'},
    'case': {
        'num': '12 · part 2', 'title': 'The Silent Camera',
        'hook': 'Last night I put one more camera, CAM 6, by the porch light at our pond. At 9:41 it filmed moths around the light. By 9:52 they were gone, and the camera saw nothing else move. But my bat detector (a microphone that records bat clicks) printed something at 9:52. And there’s a bat house across the pond.',
        'question': 'What caught the moths in the dark, and how did it find them?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'stills': [
            {'cam': 'CAM 6 · porch light', 'time': '9:41:27 PM', 'img': 'images/12-02-cam6-moth.jpg', 'alt': 'Night-vision camera picture: a moth flying beside a bright porch light.'},
            {'cam': 'CAM 6 · porch light', 'time': '9:52:14 PM', 'img': 'images/12-02-cam6-empty.jpg', 'alt': 'The same porch light 11 minutes later. There are no moths anywhere.'},
            {'cam': 'Bat detector', 'time': '9:52:10 PM', 'kind': 'print', 'tag': '🎙 SOUND', 'img': 'images/12-02-detector.png',
             'alt': 'A bat detector printout. Each green mark is one click, too high for people to hear. First there are slow clicks, then faster clicks, then a fast BUZZ of clicks, then it goes quiet.'},
            {'cam': 'Across the pond', 'time': 'the bat house', 'kind': 'print', 'tag': '📍', 'img': 'images/12-02-bat-house.jpg', 'alt': 'A tall wooden bat house on poles at the edge of a Florida park.'},
        ],
        'stillsCredit': 'CAM 6: ' + CR['moth'] + ', shown in night-vision green. Bat house: ' + CR['house'] + '. The detector printout was drawn for this lesson in the pattern real bat detectors record.',
        'clues': [
            {'id': 'echo', 'icon': '🔊', 'where': 'Warm-Up: the echo hunt', 't': 'A bat makes its own stimulus. It clicks, and the echo bouncing off a moth comes back to its ears. A quicker echo means a closer moth.'},
            {'id': 'build', 'icon': '🦇', 'where': 'The Lesson, Part 1: build a strong model', 't': 'A strong pathway model has all four steps in order, arrows between them, a “signal” arrow to the brain, and a caption about a survival need.'},
            {'id': 'compare', 'icon': '👂', 'where': 'The Lesson, Part 3: match the sense', 't': 'Every animal uses the same four steps. What changes is the stimulus and the sense organ that can pick it up: ears for echoes, a nose for smells.'},
            {'id': 'fix', 'icon': '🛠', 'where': 'The Lesson, Part 4: fix the broken models', 't': 'A model that skips a step can’t explain what the animal did. Something has to notice the stimulus, and the brain has to decide.'},
        ],
        'solve': {
            'title': 'What happened at the pond?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'A bird swooped in and spotted the moths by the porch light.', 'why': 'Check the printout and Clue 1. The detector heard clicks that sped up into a buzz. Birds don’t click like that. Bats do.'},
                {'t': 'A bat from the bat house clicked. The echoes off the moths reached its ears, its brain worked out where each moth was, and it swooped. Same four steps as an eagle, with a different stimulus and sense organ.', 'right': True,
                 'why': 'Case cracked! The camera missed the bat because it was small, fast and dark. The detector heard everything. Now write your case report: it’s the questions below.'},
                {'t': 'Nothing caught them. The moths just flew away.', 'why': 'Look at the printout again: slow clicks, faster clicks, then a BUZZ at the exact minute the moths disappeared. Something was hunting. Check Clue 1.'},
            ]},
    },
    'echo': {
        'afterText': 'You already know the four steps', 'kicker': 'Warm-Up game', 'title': 'Echo hunt in the dark',
        'todo': ['Press <b>Click!</b> The click bounces off a moth and comes back. That bounce is an <b>echo</b>.',
                 'Read the echo time (<b>ms</b> = thousandths of a second) and compare it with the test click.',
                 'Drag the 📍 pin to where the moth is, or tap that spot. Find the moth 3 times.'],
        'why': {'icon': '🎙', 'q': 'What is a bat detector?', 't': 'A microphone that records bat clicks. Most are too high for people to hear, so it prints a picture of each click.'},
        'img': 'images/12-02-bat.jpg', 'alt': 'A Florida bonneted bat’s face, with very large ears.', 'mothImg': 'images/12-02-moth.jpg',
        'credit': CR['bat'] + '. ' + CR['moth'] + '.',
        'marks': [1, 3, 6], 'rounds': [6, 1, 3],
        'wall': {'m': 3, 't': 'Test click: the echo off the pond railing, 3 m away, came back in 17 ms.'},
        'clickBtn': '🔊 Click!', 'pin': 'The moth is here',
        'ask': 'Click, read the echo time, then show where the moth is.',
        'needClick': 'Click first, then read how long the echo took.',
        'closer': 'Too far. This echo came back quicker, so the moth is closer than that.',
        'farther': 'Too close. This echo took longer, so the moth is farther away than that.',
        'foundLine': 'Found it! {ms} ms means {m} m away. You just did the bat’s brain step.',
        'win': 'Three moths found! A bat makes its own stimulus: it clicks, and the echo comes back to its ears. Its brain uses the echo time to work out where the moth is. That’s a clue.',
        'clue': 'echo'},
    'build': {
        'afterText': 'The strongest models have', 'kicker': 'Part 1 game', 'title': 'Build a strong model: the bat',
        'todo': ['Drag each card into its step, or tap a card and then a step. Two cards aren’t steps.', 'Answer the three arrow questions.', 'Add a caption and watch the meter fill up.'],
        'why': {'icon': '🦇', 'q': 'Meet the suspect', 't': 'The Florida bonneted bat is Florida’s biggest bat, and one of the rarest. It hunts flying insects at night.'},
        'img': 'images/12-02-bat.jpg', 'alt': 'A Florida bonneted bat’s face, with very large, rounded ears.', 'credit': CR['bat'],
        'name': 'Florida bonneted bat', 'sub': 'Hunting a moth in the dark',
        'slots': SLOTS4,
        'cards': [{'t': 'The echo bouncing back off a moth', 'k': 'stim'}, {'t': 'The bat’s big ears', 'k': 'sense'}, {'t': 'The brain works out where the moth is', 'k': 'brain'},
                  {'t': 'The bat swoops and grabs the moth', 'k': 'resp'}, {'t': 'The moth is brown', 'k': 'x'}, {'t': 'Bats sleep in the daytime', 'k': 'x'}],
        'hint': 'Drag each card into its step, or tap a card and then a step. Two cards aren’t steps.',
        'missX': 'That’s true, but it isn’t a step in the pathway. Each step is something that happens, in order.',
        'missSlot': {'stim': 'That card is what the bat noticed. It goes first, in Stimulus.', 'sense': 'That card is the body part that picks up the echo.',
                     'brain': 'That card is what the brain does with the signal.', 'resp': 'That card is what the bat does. It goes last.'},
        'arrows': [
            {'q': 'Arrow 1 (stimulus → sense organ): what does this arrow show?', 'opts': [
                {'t': 'The echo reaching the bat’s ears', 'tag': 'echo reaches the ears', 'ok': True},
                {'t': 'The bat flying home', 'miss': 'That’s not part of this hunt. What travels from the moth to the bat?'},
                {'t': 'The moth getting bigger', 'miss': 'The moth doesn’t change. What comes back from the moth to the bat?'}]},
            {'q': 'Arrow 2 (sense organ → brain): what travels on this arrow?', 'opts': [
                {'t': 'The moth', 'miss': 'The moth stays outside the bat! Inside the body, a message travels.'},
                {'t': 'A signal (a message inside the body)', 'tag': 'signal', 'ok': True},
                {'t': 'The sound itself', 'miss': 'The sound stops at the ear. What carries the news from the ear to the brain?'}]},
            {'q': 'Arrow 3 (brain → body): what does this arrow show?', 'opts': [
                {'t': 'The echo going back out', 'miss': 'Echoes are outside the bat. This arrow starts in the brain.'},
                {'t': 'The bat getting tired', 'miss': 'Think about the hunt. What did the brain tell the wings to do?'},
                {'t': 'What the brain decided: “swoop!”', 'tag': '“swoop!”', 'ok': True}]}],
        'caption': {'q': 'Last step: add a caption about a survival need.', 'opts': [
            {'t': 'This is a Florida bonneted bat.', 'miss': 'That’s just a name. Which survival need does this pathway help with?'},
            {'t': 'Echoes help the bat find food in the dark.', 'ok': True},
            {'t': 'Bats are really cool.', 'miss': 'True, but “cool” isn’t a survival need. Food, water, air, shelter or safety?'}]},
        'meter': ['Empty boxes', 'Four steps in order', '+ an arrow for what it noticed', '+ the signal arrow', '+ what the brain decided', 'A strong model!'],
        'win': 'That’s a strong pathway model: four steps in order, three arrows (one labeled signal) and a caption. That’s a clue.',
        'clue': 'build'},
    'compare': {
        'kicker': 'Part 3 game', 'title': 'Match the sense',
        'todo': ['Read what each animal notices.', 'Drag in the sense organ that can pick it up, or tap a sense organ and then a dashed box.', 'Look across all four models.'],
        'why': {'icon': '👂', 'q': 'Why match?', 't': 'Each sense organ picks up one kind of stimulus. Ears pick up sound, eyes pick up light, a nose picks up smells, and feelers pick up touch.'},
        'rows': [{'k': 'stim', 'icon': '⚡', 't': 'Stimulus'}, {'k': 'sense', 'icon': '👂', 't': 'Sense organ'}, {'k': 'brain', 'icon': '🧠', 't': 'Brain'}, {'k': 'resp', 'icon': '🏃', 't': 'Response'}],
        'dropHere': 'Drop the sense organ here',
        'animals': ANIMALS,
        'senses': [{'id': a['id'], 't': a['sense']} for a in ANIMALS],
        'q': 'Look across all four models. What stayed the SAME every time?',
        'opts': [{'t': 'The sense organ', 'miss': 'Ears, eyes, a nose, feelers: those all changed.'},
                 {'t': 'The four steps, in the same order', 'ok': True},
                 {'t': 'The stimulus', 'miss': 'An echo, a fish, a smell, a shake: those all changed.'}],
        'credit': CR['bat'] + '. ' + CR['anhinga'] + '. ' + CR['bear'] + '. ' + CR['crab'] + '.',
        'win': 'Four animals, four different senses, the same four steps every time. The stimulus and the sense organ change the most. That’s a clue.',
        'clue': 'compare'},
    'fix': {
        'afterText': 'Some models are broken: a step is missing', 'kicker': 'Part 4 game', 'title': 'Fix the broken models',
        'todo': ['Read the volunteer’s model and pick what’s wrong.', 'Drag the missing step into its box, or tap a card and then the box.', 'Press ▶ Run the model. Fix all three.'],
        'why': {'icon': '🛠', 'q': 'Why fix a model?', 't': 'Scientists check each other’s models. If a step is missing, the model can’t explain what happened.'},
        'slots': SLOTS4,
        'hint': 'Drag the missing step into its box, or tap a card and then the box. One card isn’t a step.',
        'missX': 'That’s true, but it isn’t a step. Look for what’s missing.',
        'missSlot': {'stim': 'That card is what the animal noticed. It goes in Stimulus.', 'sense': 'That card is the body part that picks it up.',
                     'brain': 'That card is what the brain decides.', 'resp': 'That card is what the animal does.'},
        'runBtn': '▶ Run the model', 'runOk': 'It runs!',
        'models': [
            {'id': 'bat', 'name': 'Bat', 'icon': '🦇', 'img': 'images/12-02-bat.jpg', 'alt': 'A Florida bonneted bat.', 'by': 'Volunteer 1 drew:',
             'drawn': ['An echo bounces off a moth', 'The bat grabs the moth'],
             'q': 'What’s wrong with this model?', 'opts': [
                 {'t': 'It needs more colors', 'miss': 'Colors don’t explain anything. Count the steps. A pathway has four.'},
                 {'t': 'It skips the sense organ and the brain', 'ok': True},
                 {'t': 'Nothing. It’s complete.', 'miss': 'Count the steps. A pathway has four.'}],
             'have': {'stim': 'An echo bounces off a moth', 'resp': 'The bat grabs the moth'},
             'pool': [{'t': 'Big ears pick up the echo', 'k': 'sense'}, {'t': 'The brain works out where the moth is', 'k': 'brain'}, {'t': 'The moth has wings', 'k': 'x'}],
             'why': 'Now it explains HOW the bat found the moth: its ears picked up the echo, and its brain decided where to swoop.'},
            {'id': 'eagle', 'name': 'Bald eagle', 'icon': '🦅', 'img': 'images/12-02-eagle.jpg', 'alt': 'A bald eagle flying with its wings spread wide.', 'by': 'Volunteer 2 drew:',
             'drawn': ['The eagle’s eyes', 'The brain decides “fish!”', 'The eagle dives'],
             'q': 'What’s missing?', 'opts': [
                 {'t': 'The response', 'miss': 'The eagle dives: that’s the response. What did it notice first?'},
                 {'t': 'The brain', 'miss': 'The brain is there. What starts the whole pathway?'},
                 {'t': 'The stimulus: what the eagle noticed', 'ok': True}],
             'have': {'sense': 'The eagle’s eyes', 'brain': 'The brain decides “fish!”', 'resp': 'The eagle dives'},
             'pool': [{'t': 'A fish flashes near the top of the water', 'k': 'stim'}, {'t': 'Eagles build big nests', 'k': 'x'}],
             'why': 'Every pathway starts with a stimulus. Without the flash of the fish, the eagle would have nothing to react to.'},
            {'id': 'bear', 'name': 'Black bear', 'icon': '🐻', 'img': 'images/12-02-bear.jpg', 'alt': 'A Florida black bear in the woods.', 'by': 'Volunteer 3 drew:',
             'drawn': ['The smell of berries', 'The bear’s nose', 'The bear walks to the berries'],
             'q': 'What’s missing?', 'opts': [
                 {'t': 'The brain: what the bear decided', 'ok': True},
                 {'t': 'The sense organ', 'miss': 'The nose is there. What has to happen between smelling and walking?'},
                 {'t': 'Nothing. It’s complete.', 'miss': 'Count the steps. Something has to decide what the smell means.'}],
             'have': {'stim': 'The smell of berries', 'sense': 'The bear’s nose', 'resp': 'The bear walks to the berries'},
             'pool': [{'t': 'The brain decides “food!” and which way to go', 'k': 'brain'}, {'t': 'Bears have black fur', 'k': 'x'}],
             'why': 'No camera can film the brain step, but without it the nose’s signal goes nowhere. The brain decides what to do.'}],
        'credit': CR['bat'] + '. ' + CR['eagle'] + '. ' + CR['bear'] + '.',
        'win': 'Three broken models fixed! A model that skips a step can’t explain what the animal did. Every step must be there, in order. That’s your last clue.',
        'clue': 'fix'},
    'exploreMod': 'fix',
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Colors look nice, but do they show the order of the steps?', 'C': 'A paragraph can explain, but what shows how the signal moves from step to step?'},
        'q2': {'A': 'Bats use ears; bears use noses. Did that stay the same?', 'B': 'An echo and a smell are different stimuli. What never changed?'},
        'q3': {'B': 'Count the steps in the friend’s model. Are there four?', 'C': 'Arrows help, but two whole steps are missing. Which ones?'}},
    'flags': {
        'ans-1': [
            {'label': 'a stimulus', 're': 'when|smell|echo|fish|vibrat|shak|sound|moth|berr|click|water|move'},
            {'label': 'a sense organ', 're': 'ear|eye|nose|antenn|feeler|whisker|sense'},
            {'label': 'what the brain does', 're': 'brain|decid|figur|work.{0,3}out|think|process|know'},
            {'label': 'the response', 're': 'swoop|grab|catch|spear|div|walk|follow|eat|hide|run|rais|claw|scoot|skitter|move|go|get|snap'}],
        'ans-3': [
            {'label': 'the sense organ', 're': 'sense|ear|eye|nose|organ'},
            {'label': 'the brain', 're': 'brain|decid|process|think'},
            {'label': 'why it matters', 're': 'because|without|can.?t|cannot|won.?t|wouldn.?t|no way|need|has to|have to|notice|know|matter|so '}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|wrong|right|true|not true|waste|need|one|two|both'},
            {'label': 'two pieces of evidence', 'any': ['bat', 'eagle', 'bear', 'crab', 'anhinga', 'ear', 'eye', 'nose', 'antenn|feeler', 'four steps|4 steps', 'stimul', 'sense', 'differ', 'same', 'compar', 'echo', 'smell'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|without|help'}]},
    'minWords': {'ans-1': 20, 'ans-3': 15, 'cer-4': 30},
    'hints': {
        'ans-1': ['Pick one animal from Part 3: bat, anhinga, bear or crab. They’re shown right above this question.', 'Use its four boxes. Each box fills one blank in the sentence.', 'Try: When the ___ happens, the ___ picks it up. The brain ___. The animal ___.'],
        'ans-3': ['Count the steps: stimulus, sense organ, brain, response. Which two are missing?', 'Think about the broken bat model you fixed in Part 4.', 'Try: They are missing the ___ and the ___. That matters because without them ___.'],
        'cer-4': ['First decide: do you agree or disagree with the classmate?', 'Think about Match the sense: what changed from animal to animal, and what stayed the same?', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'The bat hunts with its ears; the eagle hunts with its eyes.',
                'All four Florida models had the same four steps.',
                'The sense organ changed from animal to animal.',
                'A bat model can’t show how a bear smells its food.',
                'Comparing models shows what stays the same and what changes.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · the silent camera', 'length': '30–40 s',
                    'script': 'Last night, my new camera by the pond filmed moths around the porch light. Eleven minutes later they were gone, and the camera saw nothing. But my bat detector heard plenty. Look at the printout in the case file: slow clicks, faster clicks, then a buzz. Something was hunting in the dark. Help me figure out how it found those moths.'},
        'warmup': {'label': 'Warm-Up · echo hunt (Clue 1)', 'length': '20–30 s',
                   'script': 'Bats make their own stimulus. A bat clicks, and the sound bounces off a moth and comes back as an echo. The quicker the echo comes back, the closer the moth is. Try it yourself: click, read the echo time, and find the moth.'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Say each word. For pathway, trace the four steps with your finger in the air.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · build a strong model (Clue 2)', 'length': '20–30 s',
                  'script': 'Here’s what makes my models strong. Four steps in order. An arrow between each one, with the word signal on the arrow to the brain. And a caption about a survival need. Build one for the bonneted bat, and watch the meter fill up.'},
        'part2': {'label': 'Part 2 · two animals, two pathways', 'length': '20–30 s'},
        'figure': {'label': 'The eagle and bat picture', 'length': '20–30 s'},
        'part3': {'label': 'Part 3 · match the sense (Clue 3)', 'length': '25–35 s',
                  'script': 'Every animal uses the same four steps, but not the same senses. Look at what each animal notices. Then give it the sense organ that can pick that up. An echo needs ears. A smell needs a nose. When all four are done, look across the models. What stayed the same?'},
        'explore': {'label': 'Part 4 · fix the broken models (Clue 4)', 'length': '25–35 s',
                    'script': 'My volunteers drew models last night, and some of them are broken. A step is missing. A model that skips a step can’t explain what the animal did. Find what’s wrong, add the missing step, then press Run and watch the signal go all the way through.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s',
                       'script': 'Do you have all four clues? Crack the case at the top of this tab: what caught the moths, and how did it find them? Then answer two questions, build two pathway models of your own, and write your CER. Your answers save as you type.'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · two pathway models', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says one model is enough to understand every animal. Hmm. Think about the bat, the eagle, the bear and the crab. Could one model explain them all? Pick your side, tap two pieces of evidence in the planner, then explain how they prove your claim.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease week 13 (families and traits).',
                    'script': 'Case closed! A Florida bonneted bat clicked, listened for the echoes, and its brain did the rest. Same four steps as an eagle, just a different sense. Next week, we’ll look at families: how Florida plants and animals pass their traits to their young.'},
    },
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Your echo hunt with all three moths found (Warm-Up)',
        'Your bat model when the meter is full (The Lesson)',
        'All four animals in Match the sense (The Lesson)',
        'The answer that cracked the case (Assignment)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['My two pathway models', 'A bat hunting with echoes', 'The four steps, with arrows'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 2,
                           'prompts': ['Animal 1: four boxes and arrows', 'Animal 2: four boxes and arrows', 'Circle the step that changed the most']}]},
    'hlCoach': copy.deepcopy(P['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🦇', 'name': 'Bat detector printout',
                 'line': 'You cracked Case 12, part 2, and the bat detector printout goes in your Field Notebook. (A specimen is something a scientist collects to study.) Next week: families! How do Florida plants and animals pass their traits to their young?'},
    'notebookTitle': P['notebookTitle'],
    'notebook': [dict(x) for x in P['notebook']],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You’ll use every one of them today.',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'write', 'find': {'sel': '#tab-vocab p', 'text': 'sea turtle notices a jellyfish'},
         'label': 'Warm-Up: my prediction', 'q': 'Warm-Up: An eagle notices a fish and a sea turtle notices a jellyfish. Which step will change the most between them? Which will stay the same?',
         'ph': 'I think the ___ will change the most, because… The ___ will stay the same.', 'rows': 3},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'hide-pw', 'type': 'hide', 'find': {'sel': '.act-warmup .socratic-q', 'text': 'Same four steps, two very different'}},
        {'id': 'hide-tip', 'type': 'hide', 'find': {'sel': '.act-warmup .callout', 'text': 'Today'}},
        {'id': 'hide-st', 'type': 'hide', 'find': {'sel': '.socratic-q', 'text': 'labels the four parts'}},
        {'id': 'recap-b5', 'type': 'recap', 'find': {'sel': '.pq-text', 'text': 'Pick one of the four Florida animals'}, 'title': 'The four Florida pathways from Part 3',
         'items': [{'name': a['name'], 'img': a['img'], 't': a['stim'] + ' → ' + a['sense'].split(' ', 1)[1].lower() + ' → ' + a['brain'][0].lower() + a['brain'][1:] + ' → ' + a['resp'][0].lower() + a['resp'][1:] + '.'} for a in ANIMALS]},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Pick two different Florida animals'},
         'label': 'Part C: My two pathway models', 'q': 'Part C: Two pathway models for two Florida animals that use different senses, and how they compare',
         'title': 'My two pathway models',
         'fields': [{'t': 'Animal 1 and its four steps', 'icon': '1️⃣', 'ph': 'Animal: ___. Stimulus: ___ → sense organ: ___ → brain: ___ → response: ___', 'long': True},
                    {'t': 'Animal 2 and its four steps', 'icon': '2️⃣', 'ph': 'Animal: ___. Stimulus: ___ → sense organ: ___ → brain: ___ → response: ___', 'long': True},
                    {'t': 'These pathways are alike because…', 'icon': '🟰', 'ph': 'Both pathways…', 'long': True},
                    {'t': 'These pathways are different because…', 'icon': '↔️', 'ph': 'One animal uses its ___, but the other uses its ___…', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Do you agree or disagree with the classmate?', 'ph': 'I disagree. One model is not enough because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-1': 'Part B · Question 5', 'ans-3': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] == '12.01': n['have'] = True
    if n['lesson'] == '12.02': n.update({'icon': '🦇', 'name': 'Bat detector printout'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'A strong model shows the four steps in order, with arrows that show the signal.',
    'key': ['strong', 'model', 'four', 'steps', 'order', 'arrows', 'signal'],
    'small': ['A', 'the', 'in', 'with', 'that'],
    'model': 'A scientist might highlight “model”, “four steps”, “arrows” and “signal”. Those words carry the idea. Small words like “a” and “the” don’t.'}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
