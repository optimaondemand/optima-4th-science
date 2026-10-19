#!/usr/bin/env python3
"""Unit 4 Review · Day 1 — "The Hole on Main Street" (June Calloway).
Run from the repo root:  python3 tools/sparkle/lessons/r4-1/make.py   → original.html (+ the page the first time), data.json, video.json
Then:                    python3 tools/sparkle/build_lesson.py r4-1"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))
import review_page

KEY, FILE = 'r4-1', 'review-unit-4-day-1.html'
CR = {
    'hole': 'Sinkhole near Dover, Florida, after the January 2010 freeze, U.S. Geological Survey (public domain)',
    'storm': 'Hurricane Idalia storm surge on Bayshore Boulevard, Tampa, 2023, Andrew Heneen, via Wikimedia Commons (CC BY 4.0)',
    'rain': 'A 4-inch plastic rain gauge, Famartin, via Wikimedia Commons (CC BY-SA 3.0)',
    'rock': 'Ocala Limestone on the Suwannee River, Lafayette County, Florida, Charlie A. Smith, via Wikimedia Commons (CC BY-SA 3.0)',
    'gpr': 'Ground-penetrating radar in use, The Charles Machine Works, via Wikimedia Commons (CC BY-SA 2.0)',
}

# ---------------------------------------------------------------- the plain page
PAGE = {
    'key': KEY, 'file': FILE, 'donor': '17-02', 'icon': '🪨',
    'title': 'Unit 4 Review: The Hole on Main Street', 'headerTitle': 'Review: The Hole on Main Street', 'badge': 'UNIT 4 REVIEW · DAY 1',
    'gatherTitle': 'Unit 4 Review · Day 1 · The Hole on Main Street', 'footer': 'Unit 4 Review · Day 1 · The Hole on Main Street',
    'info': {'when': 'Q3 · Unit 4 Review', 'whenDetail': 'Natural Forces & Safety', 'quarter': 'Quarter 3', 'day': 'Day 1 · Review', 'dayDetail': 'Lessons 16.01–17.02',
             'focus': 'Hazards & Tradeoffs', 'focusDetail': 'Land, living things, people', 'std': '4-ESS3-1 · 4-ESS3-2', 'stdDetail': 'Earth & Human Activity · TEKS 4.10(B)'},
    'bigQ': 'How do natural events change Florida, and how do we choose the best way to protect it?',
    'bigQnote': 'Today you’ll pull together all of Unit 4: hazards, their effects, and the tradeoffs in every choice. Tomorrow, in the lab, you’ll test real ways to protect a town.',
    'ican': ['trace how one natural event changes the land, living things, and people.',
             'explain how a sinkhole forms in Florida.',
             'name what we gain and what we give up when we make a choice (a tradeoff).'],
    'warm': {'title': '🌅 Warm-Up: The Storm Scattered the Words', 'subtitle': 'Put Unit 4’s big words back together',
             'paras': ['Last night’s storm blew through June’s field office. Her Unit 4 word cards are all over the floor! Before we open her new case, help her put each word back with its meaning.']},
    'words': [
        {'emoji': '⚠️', 'w': 'Hazard', 'def': 'A natural event that can hurt people, living things, or property, like a hurricane, flood, wildfire, or sinkhole.'},
        {'emoji': '💥', 'w': 'Effect', 'def': 'A change caused by something. Heavy rain (the cause) can bring a flood (the effect).'},
        {'emoji': '🌿', 'w': 'Ecosystem', 'def': 'All the living and nonliving things in one place, working together, like a wetland or a beach.'},
        {'emoji': '🪨', 'w': 'Limestone', 'def': 'A rock under most of Florida. Water can slowly dissolve it (wear it away, like sugar in water).'},
        {'emoji': '🕳️', 'w': 'Sinkhole', 'def': 'A hole that opens when the ground falls into an empty space underground.'},
        {'emoji': '⚖️', 'w': 'Tradeoff', 'def': 'When you gain one thing but give up another.'},
    ],
    'lesson': {'title': '📘 Review: How Nature Changes Florida', 'subtitle': 'Effects, sinkholes, and tradeoffs', 'parts': [
        {'h': 'Part 1 · One storm, three layers', 'paras': [
            'A hurricane is a natural event. When it causes harm, it is a <strong>hazard</strong>.',
            'Scientists trace a hazard’s effects in three layers: the land, the living things (the ecosystem), and the people. One effect often ripples into the next. Fallen trees (land) take away bird nests (living things) and block roads (people).'],
         'stop': 'Think of one way a storm changes the land. What living thing does that change next?'},
        {'h': 'Part 2 · What’s under Florida?', 'paras': [
            'Under most of Florida is <strong>limestone</strong>, a rock made long ago from shells and sea animals. Rainwater is a tiny bit acidic (a little like very weak lemon juice). As it soaks down, it slowly dissolves the limestone.',
            'Over many years, this leaves hollows (empty spaces) in the rock. Sand and clay sit on top like a lid. If the lid gets too heavy or too wet, or the water underground drains away, the lid falls in. That’s a <strong>sinkhole</strong>.',
            'In 1981, a giant sinkhole opened in Winter Park, Florida, on a dry spring evening. There was no storm at all. Look closely at what it swallowed.']},
        {'h': 'Part 3 · Every choice is a tradeoff', 'paras': [
            'In January 2010, a hard freeze hit the strawberry farms near Plant City and Dover. To save their plants, farmers sprayed water on them all night. A thin coat of ice kept the berries from freezing solid.',
            'They pumped so much <strong>groundwater</strong> (water stored underground, in the limestone) that the water level underground dropped about 60 feet. About 140 sinkholes opened, and more than 750 neighbors’ wells went dry for a while. The farmers saved their crop, but the land and their neighbors paid a cost. That’s a <strong>tradeoff</strong>.',
            'Every choice has two sides. Sort each fact below: is it something people gain, or something given up?']},
    ]},
    'quiz': [
        {'q': 'Heavy rain makes a river flood. What is the heavy rain?', 'opts': ['The effect', 'The cause', 'A constraint'], 'ans': 'B',
         'right': '🌧️ Right! The rain makes the flood happen, so it is the cause. The flood is the effect.', 'wrong': 'A cause makes something happen. Did the rain make the flood happen, or did the flood make the rain?'},
        {'q': 'How do most Florida sinkholes form?', 'opts': ['Earthquakes crack the ground open.', 'Water slowly dissolves limestone and leaves a hollow. Then the ground above falls in.', 'Hurricane winds blow the sand away.'], 'ans': 'B',
         'right': '🕳️ Right! The hollow forms slowly, over years. The ground on top falls in later.', 'wrong': 'Think about the rock under Florida and what water does to it over many years.'},
        {'q': 'A town builds a sea wall. It keeps waves away from homes, but the beach in front washes away and sea turtles lose their nesting spot. This is…', 'opts': ['a tradeoff', 'a criterion', 'a natural event'], 'ans': 'A',
         'right': '⚖️ Right! The town gains safer homes and gives up its beach. That’s a tradeoff.', 'wrong': 'The town gained something and gave something up. What do we call that?'},
    ],
    'assign': {'title': '✍️ Assignment: Crack the Case', 'subtitle': 'Show what you remember from Unit 4',
        'partB': ['Pick ONE effect a hurricane has on the land. Explain how that change also affects living things OR people.',
                  'Explain how a sinkhole forms in Florida. Use the words limestone and groundwater.'],
        'partC': {'title': 'Tradeoff Check', 'intro': 'Pick one choice from today: spraying water to save strawberries, building a sea wall, or mining limestone for roads. Fill in the four boxes.'},
        'cer': {'prompt': 'A neighbor says, <em>“The hurricane made the hole on Main Street. Nothing else had anything to do with it.”</em>',
                'ask': 'Do you agree or disagree? Use <strong>two pieces of evidence</strong> from today.'},
        'checklist': ['<strong>Crack the case:</strong> I picked the answer that fits all four clues.', '<strong>Part B:</strong> Questions 1 and 2 answered in complete sentences.',
                      '<strong>Part C:</strong> All four Tradeoff Check boxes filled in.', '<strong>Use Your Evidence:</strong> my claim, two pieces of evidence, and my reasoning.'],
        'submit': 'Your answers save as you type. Copy your Gathered Answers and paste them into the Canvas assignment, or download them and upload the file.'},
    'circleTip': 'You traced a storm’s effects, found the real cause of a sinkhole, and weighed tradeoffs. Tomorrow you’ll be the engineer: you’ll test three ways to protect a town’s shoreline.',
}

# ---------------------------------------------------------------- the sparkle data
crew = {'june': {'name': 'June Calloway', 'role': 'geologist (a scientist who studies rocks and the land)', 'initials': 'JC', 'color': '#9A5B2E', 'lens': 'handlens', 'voiceId': '8WaMCGQzWsKvf7sGPqjE'}}
D = {
    'lesson': '17.R1', 'label': 'Unit 4 Review · Day 1', 'weekLabel': 'Unit 4 Review', 'week': 17, 'day': 1, 'guide': 'june', 'prefix': 'g4sci-r4-1', 'manifestKey': KEY,
    'paths': {'audio': 'assets/audio/guide/', 'video': 'assets/video/teacher/', 'manifest': 'https://raw.githubusercontent.com/optimaondemand/optima-4th-science/main/video-manifest.json',
              'h2c': 'assets/sparkle/vendor/html2canvas.min.js', 'crew': 'assets/crew/', 'ornaments': 'assets/ornaments/'},
    'crew': crew, 'expedition': {'num': 'U4', 'title': 'The Hole on Main Street'}, 'ambient': {'icon': '🦗', 'label': 'Field sounds'},
    'case': {
        'num': 'U4', 'title': 'The Hole on Main Street', 'style': 'tags',
        'hook': 'Last week a hurricane dumped 20 inches of rain on our town, Palmetto Springs. Two days later, a hole opened on Main Street and swallowed a sidewalk. Everyone says, “The hurricane did it!” But I pulled a rock sample from under the street. Look at all those holes. I don’t think the storm did it alone.',
        'question': 'What really made the hole on Main Street?',
        'how': 'Find 4 clues as you work through the review. Then crack the case (solve it) at the top of the Assignment tab.',
        'stills': [
            {'cam': 'Tag 1 · Main Street', 'time': 'two days after the storm', 'tag': 'THE HOLE', 'kind': 'print', 'img': 'images/r4-1-case-hole.jpg', 'alt': 'A sinkhole has swallowed part of a yard and the road in front of a house. Plastic sheets and orange barriers surround it.'},
            {'cam': 'Tag 2 · the storm', 'time': 'last week', 'tag': 'STORM', 'kind': 'print', 'img': 'images/r4-1-case-storm.jpg', 'alt': 'Hurricane seawater floods a road and pours over a railing next to a bridge.'},
            {'cam': 'Tag 3 · rain gauge', 'time': 'after the storm', 'tag': '20 IN.', 'kind': 'print', 'img': 'images/r4-1-case-rain.jpg', 'alt': 'A clear plastic rain gauge: a tube with marks that shows how much rain fell.'},
            {'cam': 'Tag 4 · rock sample', 'time': 'from under Main Street', 'tag': 'LIMESTONE', 'kind': 'print', 'img': 'images/r4-1-case-rock.jpg', 'alt': 'Pale limestone rock full of holes and hollows.'}],
        'stillsCredit': 'Tag 1: ' + CR['hole'] + '. Tag 2: ' + CR['storm'] + '. Tag 3: ' + CR['rain'] + '. Tag 4: ' + CR['rock'] + '. The photos are real; Palmetto Springs and the case are part of the story.',
        'clues': [
            {'id': 'words', 'icon': '🧩', 'where': 'Warm-Up: Word Rescue', 't': 'A cause makes something happen; an effect is the change. One effect, like a hole, can have more than one cause.'},
            {'id': 'layers', 'icon': '🌀', 'where': 'The Lesson, Part 1: three layers', 't': 'A hurricane’s heavy rain can open sinkholes, and one effect on the land ripples into living things and people.'},
            {'id': 'photos', 'icon': '🕳️', 'where': 'The Lesson, Part 2: the Winter Park sinkhole', 't': 'Sinkholes form where water slowly dissolved the limestone, leaving a hollow. Winter Park’s opened on a dry day, with no storm.'},
            {'id': 'judge', 'icon': '⚖️', 'where': 'The Lesson, Part 3: gain or give up?', 't': 'Pumping lots of groundwater near Dover opened about 140 sinkholes. People’s choices can make sinkholes more likely.'}],
        'solve': {'title': 'What made the hole on Main Street?', 'q': 'Which answer fits all four clues?', 'options': [
            {'t': 'The storm did it alone. Before the hurricane, the rock under Main Street was solid, with no holes in it at all.', 'why': 'Check Clue 3. Hollows in limestone take years to form, and Winter Park’s sinkhole opened on a dry day. Look at June’s rock sample, too.'},
            {'t': 'Water dissolved the limestone under Main Street for years and left a hidden hollow. The storm’s heavy rain was the last push, and the ground on top fell in.', 'right': True,
             'why': 'Case cracked! The storm was the last push, not the only cause. Now write your case report: it’s the questions below.'},
            {'t': 'Sinkholes only happen during hurricanes, so building a tall sea wall along the beach would stop the next one.', 'why': 'Check Clues 3 and 4. Sinkholes can open on dry days, or when people pump too much groundwater. A sea wall stops waves, not holes.'}]}},
    'words': {'afterText': 'Before we open her new case', 'kicker': 'Warm-Up game · Clue 1', 'title': 'Word Rescue',
        'todo': ['Read a meaning.', 'Drag the word onto it. Or tap the word, then tap the meaning.', 'Rescue all 8 words.'],
        'why': {'icon': '🧩', 'q': 'Why start with words?', 't': 'Every Unit 4 question uses these 8 words. If you know them, the rest is easier.'},
        'words': [
            {'id': 'hazard', 'icon': '⚠️', 't': 'Hazard', 'miss': 'A hazard is an EVENT in nature. Find the meaning about harm.'},
            {'id': 'cause', 'icon': '👉', 't': 'Cause', 'miss': 'A cause comes FIRST. It makes something happen.'},
            {'id': 'effect', 'icon': '💥', 't': 'Effect', 'miss': 'An effect comes AFTER. It is the change.'},
            {'id': 'tradeoff', 'icon': '⚖️', 't': 'Tradeoff', 'miss': 'A tradeoff has two sides: one you get, one you lose.'},
            {'id': 'envcost', 'icon': '🌫️', 't': 'Environmental cost', 'miss': 'Environmental means nature. What does nature lose?'},
            {'id': 'criteria', 'icon': '✅', 't': 'Criteria', 'miss': 'Criteria are the goals: what a good plan must DO.'},
            {'id': 'constraint', 'icon': '🚧', 't': 'Constraint', 'miss': 'A constraint is a limit, like money or time.'},
            {'id': 'mitigation', 'icon': '🛡️', 't': 'Mitigation', 'miss': 'Mitigation is what people DO to make harm smaller.'}],
        'meanings': [
            {'id': 'hazard', 't': 'A natural event that can cause harm.'}, {'id': 'cause', 't': 'What makes something happen.'},
            {'id': 'effect', 't': 'A change that happens because of something.'}, {'id': 'tradeoff', 't': 'You gain one thing, but you give up another.'},
            {'id': 'envcost', 't': 'What nature loses when people use a resource.'}, {'id': 'criteria', 't': 'The goals a good solution must meet.'},
            {'id': 'constraint', 't': 'A limit, like money, time, or space.'}, {'id': 'mitigation', 't': 'Steps that make a hazard’s harm smaller.'}],
        'win': 'All 8 words rescued! Clue 1: a cause makes something happen, and one effect can have more than one cause.', 'clue': 'words'},
    'layers': {'afterText': 'Scientists trace a hazard’s effects in three layers', 'kicker': 'Part 1 game · Clue 2', 'title': 'One event, three layers',
        'todo': ['Read an effect card.', 'Drag it to Land, Living things, or People. Or tap the card, then tap a box.', 'Sort the hurricane, then the wildfire.'],
        'bins': [{'k': 'land', 'icon': '🏝️', 't': 'Land'}, {'k': 'life', 'icon': '🦩', 't': 'Living things'}, {'k': 'people', 'icon': '👨‍👩‍👧', 't': 'People'}],
        'events': [
            {'id': 'hurricane', 'icon': '🌀', 'name': 'Hurricane', 'cards': [
                {'t': 'Beach sand washes away.', 'bin': 'land', 'miss': 'Sand is part of the ground. Which layer is that?'},
                {'t': 'Heavy rain helps a sinkhole open on a street.', 'bin': 'land', 'miss': 'A hole in the ground changes which layer first?'},
                {'t': 'Salt water floods a freshwater pond, and the fish die.', 'bin': 'life', 'miss': 'Who lived in the pond?'},
                {'t': 'Birds lose the trees they nest in.', 'bin': 'life', 'miss': 'Birds are living things in the ecosystem.'},
                {'t': 'The power goes out for five days.', 'bin': 'people', 'miss': 'Who uses the power?'},
                {'t': 'Families leave their homes to stay safe.', 'bin': 'people', 'miss': 'Families are people.'}]},
            {'id': 'wildfire', 'icon': '🔥', 'name': 'Wildfire', 'cards': [
                {'t': 'Bare, burned ground washes away in the next rain.', 'bin': 'land', 'miss': 'What washes away? The ground.'},
                {'t': 'Fire clears the brush, so young longleaf pines get sunlight to grow.', 'bin': 'life', 'miss': 'Pines are plants. Effects aren’t always bad!'},
                {'t': 'Smoke closes a highway.', 'bin': 'people', 'miss': 'Who drives on the highway?'}]}],
        'q': 'A hurricane knocked down trees. Birds lost their nests, and a road was blocked. What does that show?',
        'opts': [{'t': 'One effect can ripple into all three layers.', 'ok': True}, {'t': 'Hurricanes only change the land.', 'miss': 'Did the birds and the drivers notice the fallen trees?'},
                 {'t': 'Trees are not part of an ecosystem.', 'miss': 'Trees are living things. They are part of the ecosystem.'}],
        'win': 'Clue 2: a hurricane’s rain can open sinkholes, and one effect ripples into all three layers.', 'clue': 'layers'},
    'photos': [{'id': 'winterpark', 'afterText': 'Look closely at what it swallowed', 'clue': 'photos', 'kicker': 'Part 2 · real photo · Clue 3', 'short': 'Winter Park sinkhole',
        'title': 'The Winter Park sinkhole, May 1981', 'todo': ['Tap each number on the photo to read what it shows.', 'Then match three of them below.'],
        'why': {'icon': '📷', 'q': 'What is this?', 't': 'A real U.S. Geological Survey photo, taken the morning after. The hole was about 300 feet across (as long as a football field) and about 80 feet deep.'},
        'img': 'images/r4-1-winterpark.jpg', 'alt': 'A huge round sinkhole with steep sandy walls. People stand at the edge of a road high above. Broken pipes hang down the wall, and wood and other pieces lie at the bottom.',
        'credit': 'Winter Park sinkhole, May 9, 1981, Anthony S. Navoy, U.S. Geological Survey', 'license': 'Public domain',
        'hotspots': [
            {'n': 1, 'x': 40, 'y': 12, 'label': 'The street edge', 't': 'People stand where the road just ends. The ground under it fell away.'},
            {'n': 2, 'x': 30, 'y': 32, 'label': 'Sand and clay walls', 't': 'This was the “lid” on top of the limestone. It slid down into the hollow below.'},
            {'n': 3, 'x': 42, 'y': 52, 'label': 'Broken pipes', 't': 'Water pipes snapped when the ground fell. That is an effect on people.'},
            {'n': 4, 'x': 26, 'y': 71, 'label': 'What fell in', 't': 'A house, part of a swimming pool, and several cars ended up down here.'},
            {'n': 5, 'x': 47, 'y': 78, 'label': 'Water at the bottom', 't': 'Groundwater: water stored in the limestone deep underground. The hole reached all the way down to it.'}],
        'task': {'q': 'Which number shows each one?', 'items': [
            {'icon': '🟫', 'step': 'The ground that fell into the hollow', 'ans': 2, 'evid': 'The sand and clay on top fell into a hollow in the limestone below.', 'miss': 'Look for the walls that slid down.'},
            {'icon': '👨‍👩‍👧', 'step': 'An effect on people', 'ans': [1, 3, 4], 'evid': 'The sinkhole broke pipes, ended a road, and swallowed a house and cars.', 'miss': 'Look for something people built or use.'},
            {'icon': '💧', 'step': 'Water stored underground', 'ans': 5, 'evid': 'Groundwater sits in the limestone deep under the ground.', 'miss': 'Look at the very bottom.'}],
            'win': 'Clue 3! This sinkhole opened on a dry evening, with no storm at all. The hollow had been growing for years.'}}],
    'judge': {'afterText': 'Sort each fact below', 'kicker': 'Part 3 game · Clue 4', 'title': 'Gain or give up?',
        'todo': ['Read the card.', 'Drag it to a side, or tap a side.', 'Sort all 8.'], 'hint': 'Read the card, then drag it to a side, or tap a side.',
        'sides': [{'k': 'gain', 'icon': '🎁', 't': 'We gain'}, {'k': 'give', 'icon': '⚖️', 't': 'We give up'}],
        'cards': [
            {'t': 'Spraying water on strawberries kept them from freezing.', 'side': 'gain', 'why': 'The farmers saved their crop. That’s what they gained.', 'miss': 'Was saving the crop good for the farmers?'},
            {'t': 'So much water was pumped that about 140 sinkholes opened.', 'side': 'give', 'why': 'The land and the neighbors paid the price. That’s what was given up.', 'miss': 'Is a sinkhole something anyone wanted?'},
            {'t': 'Limestone from a mine becomes rock for roads and buildings.', 'side': 'gain', 'why': 'People gain building material. That’s a benefit.', 'miss': 'Roads and buildings help people.'},
            {'t': 'The mine leaves a big pit where a forest used to be.', 'side': 'give', 'why': 'The forest is lost. That’s an environmental cost.', 'miss': 'What happened to the forest?'},
            {'t': 'A sea wall blocks storm waves from homes.', 'side': 'gain', 'why': 'Safer homes: that’s the gain.', 'miss': 'Are safer homes a good thing?'},
            {'t': 'The beach in front of the sea wall washes away, and turtles lose nesting space.', 'side': 'give', 'why': 'The beach and the turtles pay the price.', 'miss': 'What did the beach and the turtles lose?'},
            {'t': 'Mangroves calm waves and give fish a home.', 'side': 'gain', 'why': 'Two gains at once: protection and habitat.', 'miss': 'Calmer waves and a home for fish: good or bad?'},
            {'t': 'Mangroves take years to grow before they protect the shore.', 'side': 'give', 'why': 'The town gives up protection right away.', 'miss': 'What does the town have to wait for?'}],
        'win': 'Clue 4: every choice has two sides. Pumping groundwater to save crops opened about 140 sinkholes near Dover.', 'clue': 'judge'},
    'quizKicker': '', 'quizMiss': {'q1': {'A': 'The flood comes after the rain. Which one came first?', 'C': 'A constraint is a limit on a plan. Is rain a limit?'},
        'q2': {'A': 'Florida has almost no earthquakes. What does water do to limestone?', 'C': 'Wind moves sand on the surface. Sinkholes start deep underground.'},
        'q3': {'B': 'A criterion is a goal for a plan. What did the town gain AND lose?', 'C': 'Building a wall is a choice people make, not something nature does.'}},
    'flags': {
        'ans-1': [{'label': 'an effect on the land', 're': 'sand|beach|soil|ground|sinkhole|tree|erod|wash|flood|land|road|mud|dirt'},
                  {'label': 'how it affects living things or people', 're': 'bird|fish|animal|turtle|plant|nest|home|people|famil|road|power|house|kid|school|live'},
                  {'label': 'a because or so', 're': 'because|so |which|that means|this means|then|when'}],
        'ans-2': [{'label': 'limestone', 're': 'lime ?stone|limstone|limestone'}, {'label': 'groundwater', 're': 'ground ?water|groundwater|water underground|underground water'},
                  {'label': 'a hollow or empty space', 're': 'hollow|empty|space|cave|hole|gap|cavit'}, {'label': 'the ground falls in', 're': 'fall|fell|collaps|cave in|caves in|sink|drop'}],
        'cer-4': [{'label': 'your claim', 're': 'agree|disagree|wrong|right|not true|true|not'},
                  {'label': 'two pieces of evidence', 'any': ['limestone', 'dissolv', 'hollow', 'winter park|dry day|no storm', 'dover|strawberr|pump', 'sample|rock', 'year', 'rain', 'groundwater'], 'min': 2},
                  {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves'}]},
    'minWords': {'ans-1': 20, 'ans-2': 20, 'cer-4': 30},
    'hints': {
        'ans-1': ['Pick one card from the three-layers game, like “Beach sand washes away.”', 'Then ask: who lives there, or who uses it?', 'Try: A hurricane can ___. This also affects ___ because ___.'],
        'ans-2': ['Start deep underground. What is the rock, and what does water do to it?', 'Then: what is left behind, and what sits on top of it?', 'Try: Groundwater slowly dissolves the limestone and leaves ___. Then the ___ on top ___.'],
        'cer-4': ['First decide: was the storm the only cause?', 'Think of the Winter Park photo, June’s rock sample, or the Dover farms.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {'before': 'cer-4', 'title': 'Your claim and two pieces of evidence', 'rows': [
        {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
        {'label': '2. Pick two pieces of evidence from today', 'pick': 2, 'options': [
            'Rainwater slowly dissolves limestone and leaves hollows over many years.', 'The Winter Park sinkhole opened on a dry day, with no storm.',
            'June’s rock sample from under Main Street is full of holes.', 'Pumping lots of groundwater near Dover opened about 140 sinkholes.',
            'Heavy rain can be the last push that makes the ground fall in.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': ['All 8 words rescued (Warm-Up)', 'Your three layers, all sorted (The Lesson)', 'The Winter Park sinkhole with a label open (The Lesson)', 'The answer that cracked the case (Assignment)']},
    'sketch': {'tip': 'Draw with the pen. Then use 🏷️ Label: drag from a part of your sketch to an empty spot, and type its name.',
        'prompts': ['What’s under Main Street', 'One storm, three layers', 'A tradeoff scale'],
        'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 2,
                    'prompts': ['Draw what’s under Main Street: sand and clay on top, limestone below', 'Draw the hollow in the limestone', 'Label 2 layers']}]},
    'hlCoach': {'title': 'Highlight like a scientist', 'tips': [
        ['🔑', 'Highlight key words, not whole paragraphs.', 'If everything is yellow, nothing stands out. Aim for a few words in each paragraph.'],
        ['📖', 'Look for words that are explained.', 'Bold words, and words followed by a meaning in ( ), are often worth saving.'],
        ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me explain how nature changes Florida?'],
        ['🔗', 'Watch for clue words.', '“Because”, “so” and “over many years” show how ideas connect.'],
        ['🎨', 'Use the colors on purpose.', 'Yellow = important. Green = evidence I might use in my answer. Pink = something I wonder about.']],
        'practice': {'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.', 'text': 'Over many years, water slowly dissolves the limestone and leaves hollows under the ground.',
                     'key': ['water', 'dissolves', 'limestone', 'hollows', 'years'], 'small': ['Over', 'many', 'the', 'and', 'under'],
                     'model': 'A scientist might highlight “water”, “dissolves”, “limestone” and “hollows”. Those words carry the idea.'},
        'outside': 'This works in every subject. When you read anything, save the words that answer your question, and skip the rest.'},
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🪨', 'name': 'Limestone sample with hollows',
                 'line': 'You cracked the Main Street case, and June’s limestone sample goes in your Field Notebook. (A specimen is something a scientist collects to study.) Next: the same storm flooded Bay Street. Time to test some fixes!'},
    'notebookTitle': 'Unit 4 · Natural Forces & Safety',
    'notebook': [{'lesson': '16.01'}, {'lesson': '16.02'}, {'lesson': '17.01'}, {'lesson': '17.02'}, {'lesson': '17.R1', 'icon': '🪨', 'name': 'Limestone sample'}, {'lesson': '17.R2'}],
    'rankLine': 'Your Field Station ID just updated. Keep going, scientist.', 'lensWin': 'All six words are in focus. You’ll use every one of them today.',
    'tool': {'name': 'Ground-penetrating radar', 'icon': '📡', 'tab': 'assignment', 'after': '#tab-assignment .activity-card', 'key': 'r4-tool', 'sim': 'gpr',
        'kicker': 'Bonus · Tool of the Week', 'teaser': 'Roll a radar cart down Main Street and find the hidden hollows before the road falls in.',
        'done': 'You found both hidden hollows. A radar sticker is in your Field Notebook.',
        'why': {'icon': '📡', 'q': 'What is ground-penetrating radar?', 't': 'A tool that sends radio waves into the ground. The waves bounce back off layers of rock and off empty spaces, and a computer turns the echoes into a picture. Road crews use it to find hollows before a road falls in.'},
        'gpr': {'title': 'Scan Main Street', 'img': 'images/r4-1-gpr.jpg', 'alt': 'A worker pushes a ground-penetrating radar cart, a small cart with wheels and a screen, across a grassy field.',
            'todo': ['Tap spot 1. The cart rolls there and the radar picture appears below.', 'Scan all 10 spots.', 'A bright upside-down U means the waves bounced off a hollow. Tap those spots again to flag them 🚩.'],
            'road': 'MAIN STREET · east of the hole', 'key': 'The dark picture shows what is under each spot. Gray wavy lines = layers of sand, clay, and rock. A bright yellow upside-down U = a hollow.',
            'spots': [{}, {}, {}, {'hollow': True, 'depth': 1}, {}, {}, {'hollow': True, 'depth': 2}, {}, {}, {}],
            'q': {'q': 'Main Street has two more hidden hollows. What should the town do first?', 'opts': [
                {'t': 'Fill the hollows and make the road stronger before they fall in.', 'ok': True, 'why': 'Yes! Finding hollows early is mitigation: a step that makes a hazard’s harm smaller.'},
                {'t': 'Nothing. Hollows never fall in.', 'why': 'Look at Tag 1 in the case file. This one did!'},
                {'t': 'Build a sea wall.', 'why': 'A sea wall stops waves, not holes in the ground.'}]},
            'credit': 'Photo: ' + CR['gpr'] + '. The radar picture is a model.'}},
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'list', 'find': {'sel': '.fs-game[data-mod="words"]'}, 'label': 'Warm-Up: two words in my own sentences',
         'q': 'Warm-Up: Pick two Unit 4 words. Use each one in a sentence about Florida.', 'title': 'Your turn: pick two words. Use each one in a sentence about Florida.',
         'min': 2, 'unit': 'sentences', 'addLabel': '+ Add a sentence', 'ph': ['A hazard in Florida is…', 'A tradeoff is when…']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'}, 'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Pick one choice from today'}, 'label': 'Part C: Tradeoff Check',
         'q': 'Part C: Tradeoff Check: one choice, what people gain, what is given up, and one way to lower the cost', 'title': 'My Tradeoff Check',
         'fields': [{'t': 'The choice', 'icon': '🤔', 'ph': 'I picked: ___'}, {'t': 'What people gain', 'icon': '🎁', 'ph': 'People gain…', 'long': True},
                    {'t': 'What is given up', 'icon': '⚖️', 'ph': 'Nature or people give up…', 'long': True}, {'t': 'One way to lower the cost', 'icon': '🛡️', 'ph': 'They could…', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'}, 'reminder': 'Claim = what you think is true. Evidence = facts from today that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Was the hurricane the only cause of the hole?', 'ph': 'I disagree. The hurricane was not the only cause because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from today. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-1': 'Part B · Question 1', 'ans-2': 'Part B · Question 2', 'cer-4': 'Use Your Evidence (CER)'}},
    ],
}

# ---------------------------------------------------------------- media slots (June's walkie-talkie lines)
S = {
    'welcome': ('Welcome · the hole on Main Street', '30–40 s', 'June here, geologist. That means I study rocks and the land. Something strange happened in our town. After last week’s hurricane, a hole opened right on Main Street. Everybody blames the storm. But I pulled up a rock from under the street, and it’s full of holes. Help me figure out what really happened.'),
    'warmup': ('Warm-Up · Word Rescue (Clue 1)', '20–30 s', 'Oh, my office is a mess! The wind scattered my word cards everywhere. These eight words come up in every Unit 4 question, so let’s get them back where they belong. Read each meaning first, then find the word that fits it.'),
    'vocab': ('Word Wall', '30–45 s', None),
    'lesson': ('The Lesson', '25–35 s', None),
    'part1': ('Part 1 · three layers (Clue 2)', '20–30 s', 'When I check a town after a storm, I look at three things. What happened to the land? What happened to the living things? What happened to the people? Sort each effect card. Some might surprise you. Not every effect of a wildfire is bad.'),
    'part2': ('Part 2 · the Winter Park sinkhole (Clue 3)', '25–35 s', 'This is one of the most famous holes in Florida. It opened in Winter Park in 1981. Here’s the strange part: it wasn’t raining. Tap each number on the photo. Look at the walls, the bottom, and the edge where people are standing.'),
    'part3': ('Part 3 · gain or give up? (Clue 4)', '20–30 s', 'Every choice people make has two sides. Something we gain, and something we give up. Read each card and decide which side it goes on. Watch the strawberry farmers. Their story is a big clue.'),
    'quiz': ('Self-Check', '15–20 s', None),
    'assignment': ('Assignment · crack the case', '20–30 s', 'Do you have all four clues? Then crack the case at the top of this tab: what really made the hole on Main Street? After that, answer two questions, do a tradeoff check, and write your CER. Your answers save as you type.'),
    'partb': ('Part B', '30 s', None), 'partc': ('Part C · tradeoff check', '30 s', None),
    'evidence': ('Use your evidence · CER', '25–35 s', 'My neighbor is sure the hurricane made the hole, all by itself. Do you agree? Think about my rock sample, the Winter Park sinkhole, and the farms near Dover. Pick your side, tap two pieces of evidence, then explain how they prove your claim.'),
    'closing': ('Case closed', '20–30 s', 'Case closed! The storm was the last push, but the hollow had been growing for years. Tomorrow, a new problem. The same storm pushed seawater into Bay Street. The town needs a plan, and you’re the engineer.'),
}
D['slots'] = {k: ({'label': v[0], 'length': v[1], 'script': v[2]} if v[2] else {'label': v[0], 'length': v[1]}) for k, v in S.items()}

# ---------------------------------------------------------------- teacher video plan
V = {'slots': {
    'welcome': {'label': 'Welcome · the hole on Main Street', 'length': '50–60 s', 'want': True, 'parts': [
        {'kind': 'photo', 'pic': 'r41hole', 'label': '🕳️ The hole'}, {'kind': 'photo', 'pic': 'r41rock', 'label': '🪨 The rock sample'},
        {'label': '🗂 The case question', 'tag': 'CASE FILE U4', 'title': 'The Hole on Main Street', 'col': '#9A5B2E', 'body': 'What really made the hole on Main Street?'}],
        'script': 'Welcome back, scientists! Today we’re reviewing all of Unit 4, and June has a case for us.\n\n[ON SCREEN: The hole]\nAfter a hurricane, this hole opened on Main Street. Everybody says the storm did it.\n\n[ON SCREEN: The rock sample]\nBut June pulled up this rock from under the street. Look at all those holes! Hmm. I wonder if the storm really did it alone.\n\n[ON SCREEN: The case question]\nThat’s our case. Find four clues today. Press Listen on June’s walkie-talkie, right below me.'},
    'warmup': {'label': 'Warm-Up · Word Rescue', 'length': '40–50 s', 'want': True, 'parts': [
        {'label': '🧩 Word Rescue', 'tag': 'WARM-UP', 'title': '8 Unit 4 words', 'col': '#1F6F78', 'body': 'Read the meaning first. Then drag the word onto it, or tap the word, then tap the meaning.'}],
        'script': 'Quick warm-up! June’s word cards blew all over her office.\n\n[ON SCREEN: Word Rescue]\nHere’s my tip: read the meaning first, then hunt for the word. If one bounces back, read the hint. It tells you where to look. Every one of these words is on the Unit 4 test, so this is great practice. Press Listen on June’s walkie-talkie, right below me.'},
    'part1': {'label': 'Part 1 · three layers', 'length': '40–50 s', 'want': True, 'parts': [
        {'label': '🏝️ Three layers', 'tag': 'PART 1', 'title': 'Three layers', 'col': '#D4772C', 'body': 'Every hazard changes the land, the living things, and the people.'}],
        'script': 'Remember our three layers from lesson 17.01?\n\n[ON SCREEN: Three layers]\nWhen a hurricane hits, scientists ask three questions. What happened to the land? To the living things? To the people? (Point to each one.) One effect usually leads to the next. Sort the hurricane cards, then the wildfire cards. Press Listen on June’s walkie-talkie, right below me.'},
    'part2': {'label': 'Part 2 · the Winter Park sinkhole', 'length': '45–60 s', 'want': True, 'parts': [
        {'kind': 'photo', 'pic': 'r41wp', 'label': '🕳️ Winter Park, 1981'},
        {'label': '🪨 How a sinkhole forms', 'tag': 'PART 2', 'title': 'Slowly, then all at once', 'col': '#9A5B2E', 'body': '1. Water dissolves limestone. 2. A hollow grows for years. 3. The sand and clay on top fall in.'}],
        'script': 'Okay, this one is amazing.\n\n[ON SCREEN: Winter Park, 1981]\nThis sinkhole opened in Winter Park, Florida. It swallowed a house and several cars! And it was a dry evening. No storm.\n\n[ON SCREEN: How a sinkhole forms]\nWater slowly dissolves the limestone under Florida. A hollow grows for years. Then one day, the ground on top falls in. Tap every number on the photo. Press Listen on June’s walkie-talkie, right below me.'},
    'part3': {'label': 'Part 3 · gain or give up?', 'length': '40–50 s', 'want': True, 'parts': [
        {'label': '⚖️ Tradeoff', 'tag': 'PART 3', 'title': 'Gain or give up?', 'col': '#B5543A', 'body': 'Every choice has two sides: what we gain and what we give up.'}],
        'script': 'Let’s talk tradeoffs. (Hold up two hands like a scale.)\n\n[ON SCREEN: Tradeoff]\nWhen we make a choice, we gain something on this side, and we give something up on this side. The strawberry farmers saved their berries. But look what they gave up. Sort all eight cards. Press Listen on June’s walkie-talkie, right below me.'},
    'assignment': {'label': 'Assignment · crack the case', 'length': '40–50 s', 'want': True, 'parts': [
        {'label': '🗂 Crack the case', 'tag': 'ASSIGNMENT', 'title': 'Four clues, one answer', 'col': '#34B76F', 'body': 'Pick the answer that fits all four clues. Then Part B, Part C, and your CER.'}],
        'script': 'You made it to the assignment!\n\n[ON SCREEN: Crack the case]\nFirst, use your four clues to crack the case. Pick the answer that fits every clue, not just one. Then answer two questions, do your tradeoff check, and write your CER. Copy your gathered answers into Canvas when you’re done. Press Listen on June’s walkie-talkie, right below me.'},
    'evidence': {'label': 'Use your evidence · CER', 'length': '40–50 s', 'want': True, 'parts': [
        {'label': '✏️ CER', 'tag': 'CER', 'title': 'Was it only the storm?', 'col': '#8B6FC0', 'body': 'Claim: what you think. Evidence: two facts. Reasoning: how they prove it.'}],
        'script': 'June’s neighbor thinks the hurricane made the hole, all by itself.\n\n[ON SCREEN: CER]\nDo you agree? Your claim is your answer. Then pick two facts from today, like the Winter Park photo or the Dover farms. Your reasoning explains how those facts prove you’re right. The real Unit 4 test has a CER too, so this is perfect practice. Press Listen on June’s walkie-talkie, right below me.'},
}, 'pics': {
    'r41hole': {'src': 'images/r4-1-case-hole.jpg', 'cap': 'Tag 1 · the hole (USGS, public domain)'},
    'r41rock': {'src': 'images/r4-1-case-rock.jpg', 'cap': 'Tag 4 · limestone (Charlie A. Smith, CC BY-SA 3.0)'},
    'r41wp': {'src': 'images/r4-1-winterpark.jpg', 'cap': 'Winter Park sinkhole, 1981 (USGS, public domain)'}},
    'other': ['vocab', 'lesson', 'quiz', 'partb', 'partc', 'closing']}

if __name__ == '__main__':
    review_page.write(PAGE, HERE)
    json.dump(D, open(os.path.join(HERE, 'data.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(V, open(os.path.join(HERE, 'video.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('wrote data.json + video.json')
