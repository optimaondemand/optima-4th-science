#!/usr/bin/env python3
"""Unit 4 Review · Day 2 Lab — "Test the Shoreline" (June Calloway). The Main Street case continues on Bay Street.
Run from the repo root:  python3 tools/sparkle/lessons/r4-2/make.py   → original.html (+ the page the first time), data.json, video.json
Then:                    python3 tools/sparkle/build_lesson.py r4-2"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(os.path.dirname(HERE)))
import review_page

KEY, FILE = 'r4-2', 'review-unit-4-day-2.html'
CR = {
    'wall': 'Wave power (sea defences at Brackenbury Dip, England), Bob Jones, via Wikimedia Commons / geograph.org.uk (CC BY-SA 2.0)',
    'mang': 'Mangrove shoreline, Biscayne National Park, National Park Service (public domain)',
    'oys': 'Oyster reef living shoreline after about 3 years, Bo Lusk / The Nature Conservancy, via U.S. Fish and Wildlife Service (public domain)',
    'dune': 'Sea oats on a sand dune, John U. Lloyd Beach State Park, Florida, Georgialh, via Wikimedia Commons (CC BY-SA 4.0)',
    'storm': 'Hurricane Idalia storm surge on Bayshore Boulevard, Tampa, 2023, Andrew Heneen, via Wikimedia Commons (CC BY 4.0)',
}

PAGE = {
    'key': KEY, 'file': FILE, 'donor': '17-02', 'icon': '🌊',
    'title': 'Unit 4 Review Lab: Test the Shoreline', 'headerTitle': 'Review Lab: Test the Shoreline', 'badge': 'UNIT 4 REVIEW · DAY 2 LAB',
    'gatherTitle': 'Unit 4 Review · Day 2 Lab · Test the Shoreline', 'footer': 'Unit 4 Review · Day 2 Lab · Test the Shoreline',
    'info': {'when': 'Q3 · Unit 4 Review', 'whenDetail': 'Natural Forces & Safety', 'quarter': 'Quarter 3', 'day': 'Day 2 · Lab', 'dayDetail': 'Lessons 16.01–17.02',
             'focus': 'Engineering Design', 'focusDetail': 'Criteria, constraints, revise', 'std': '4-ESS3-2 · 3-5-ETS1', 'stdDetail': 'Engineering Design · TEKS 4.4(A)'},
    'bigQ': 'How do engineers choose the best way to protect a town from a natural hazard?',
    'bigQnote': 'Today you’re the town’s engineer. You’ll set the goals and limits, test three plans in a model, score them, and make the winner even better.',
    'ican': ['list criteria (goals) and constraints (limits) for a town’s problem.',
             'compare two solutions using test data.',
             'choose the better solution and revise it to make it stronger.'],
    'warm': {'title': '🌅 Warm-Up: The Town’s Wish List', 'subtitle': 'Goals and limits come first',
             'paras': ['The same hurricane pushed seawater into the homes on Bay Street. The town council wants a plan before the next storm season, and they made a wish list. Some lines are goals (criteria). Some are limits (constraints). Sort them so we know what a good plan must do.']},
    'words': [
        {'emoji': '✅', 'w': 'Criteria', 'def': 'The goals a good solution must meet, like “keep homes dry.”'},
        {'emoji': '🚧', 'w': 'Constraint', 'def': 'A limit on what you can do, like how much money or time you have.'},
        {'emoji': '🌊', 'w': 'Storm surge', 'def': 'Ocean water that a hurricane’s winds push up onto land.'},
        {'emoji': '🛡️', 'w': 'Mitigation', 'def': 'Steps people take to make a hazard’s harm smaller.'},
        {'emoji': '🦪', 'w': 'Living shoreline', 'def': 'Plants and oyster reefs along the water that calm waves and protect the shore.'},
        {'emoji': '🔁', 'w': 'Revise', 'def': 'To change a design to make it better, then test it again.'},
    ],
    'lesson': {'title': '📘 Lab: Test, Score, Improve', 'subtitle': 'Be the town’s engineer', 'parts': [
        {'h': 'Part 1 · Run the test tank', 'paras': [
            'Engineers can’t wait for a real hurricane to test a plan, so they use a <strong>model</strong> (a small version of the real thing). Our test tank is a model of Bay Street: the ocean on one side, a plan in the middle, and the homes on the other.',
            'Try each plan in the big storm. Watch how much water reaches the homes.']},
        {'h': 'Part 2 · Score the plans', 'paras': [
            'A plan doesn’t win just because it keeps out the most water. It has to meet the goals AND stay inside the limits. A constraint is a must: a plan that breaks one can’t be picked, even if it scores well.',
            'Use your test results to score the sea wall and the living shoreline.'],
         'stop': 'Why might a town choose a plan that keeps out a little LESS water?'},
        {'h': 'Part 3 · Make it better', 'paras': [
            'Even the best plan has a weak spot. Engineers <strong>revise</strong>: they change the design to fix the weak spot, then test it again.',
            'Find the living shoreline’s weak spot. Then pick a fix and re-run the big storm.']},
    ]},
    'quiz': [
        {'q': '“The plan must cost $2 million or less.” What is this?', 'opts': ['A criterion (a goal)', 'A constraint (a limit)', 'An effect'], 'ans': 'B',
         'right': '🚧 Right! A money limit is a constraint. A plan must stay inside it.', 'wrong': 'Is this something the plan should DO, or a LIMIT the plan has to stay inside?'},
        {'q': 'Mangroves and oyster reefs that calm waves are what kind of mitigation?', 'opts': ['Natural', 'Built', 'Planning'], 'ans': 'A',
         'right': '🦪 Right! They are living things, so this is natural mitigation.', 'wrong': 'Mangroves and oysters aren’t made of concrete, and they aren’t a plan on paper. What are they?'},
        {'q': 'Engineers tested a plan, found a weak spot, and added a sand dune. What did they do?', 'opts': ['They revised the design.', 'They made a constraint.', 'They caused a hazard.'], 'ans': 'A',
         'right': '🔁 Right! Fixing a weak spot and testing again is revising.', 'wrong': 'They changed the plan to make it better. What is that called?'},
    ],
    'assign': {'title': '✍️ Assignment: Crack the Case', 'subtitle': 'Make your recommendation to the town',
        'partB': ['Name one thing the sea wall did BETTER and one thing the living shoreline did BETTER. Use numbers from your test tank.',
                  'Why can’t the town pick a plan that breaks a constraint, even if it keeps out the most water?'],
        'partC': {'title': 'Engineering Brief', 'intro': 'Write the town a short brief (a report that helps people decide). Fill in the four boxes.'},
        'cer': {'prompt': 'The town council asks: <em>“What makes a GOOD engineering solution for a natural hazard?”</em>',
                'ask': 'Answer with a claim, <strong>two pieces of evidence</strong> from your tests, and your reasoning.'},
        'checklist': ['<strong>Crack the case:</strong> I picked the answer that fits all four clues.', '<strong>Part B:</strong> Questions 1 and 2 answered in complete sentences.',
                      '<strong>Part C:</strong> All four Engineering Brief boxes filled in.', '<strong>Use Your Evidence:</strong> my claim, two pieces of evidence, and my reasoning.'],
        'submit': 'Your answers save as you type. Copy your Gathered Answers and paste them into the Canvas assignment, or download them and upload the file.'},
    'circleTip': 'You set goals and limits, tested three plans, scored them, and made the winner better. That’s what engineers do, and it’s the same thinking the Unit 4 test asks for. You’re ready!',
}

crew = {'june': {'name': 'June Calloway', 'role': 'geologist (a scientist who studies rocks and the land)', 'initials': 'JC', 'color': '#9A5B2E', 'lens': 'handlens', 'voiceId': '8WaMCGQzWsKvf7sGPqjE'}}
PLANS = [
    {'k': 'none', 'icon': '🚫', 'name': 'No plan', 'img': 'images/r4-1-case-storm.jpg', 'alt': 'Storm surge floods a road next to a bridge.', 'cost': '$0', 'wild': 'No change', 'ready': '—',
     'res': {'small': {'ft': 1, 't': 'Even a small storm sends a little water into the yards.'}, 'med': {'ft': 3, 't': 'Water is up to the front doors.'}, 'big': {'ft': 6, 't': 'Six feet of water: the homes flood badly.'}}},
    {'k': 'wall', 'icon': '🧱', 'name': 'Sea wall', 'img': 'images/r4-2-seawall.jpg', 'alt': 'Waves crash against a concrete sea wall with steps.', 'cost': '$4 million', 'wild': 'Hurts the beach', 'ready': 'Right away',
     'res': {'small': {'ft': 0, 't': 'The wall stops every wave. Dry homes.'}, 'med': {'ft': 0, 't': 'Still dry. The wall bounces the waves back.'}, 'big': {'ft': 1, 't': 'A little water splashes over the top: 1 foot. Mostly dry.'}}},
    {'k': 'ls', 'icon': '🦪', 'name': 'Living shoreline', 'img': 'images/r4-2-mangroves.jpg', 'alt': 'Mangrove trees with tangled roots grow along calm water.', 'cost': '$1 million', 'wild': 'Helps a lot', 'ready': 'In 3–5 years',
     'res': {'small': {'ft': 0, 't': 'Mangroves and oysters calm the waves. Dry homes.'}, 'med': {'ft': 1, 't': 'The waves lose most of their energy in the roots: 1 foot of water.'}, 'big': {'ft': 2, 't': 'The big surge pushes 2 feet of water to the homes.'}}},
    {'k': 'dune', 'icon': '🏖️', 'name': 'Sand dune', 'img': 'images/r4-2-dune.jpg', 'alt': 'Sea oats grow on a sandy dune.', 'cost': '$0.5 million', 'wild': 'Helps', 'ready': 'In 1 year',
     'res': {'small': {'ft': 0, 't': 'The dune blocks the water. Dry homes.'}, 'med': {'ft': 1, 't': 'The dune holds back most of the water: 1 foot.'}, 'big': {'ft': 4, 't': 'The big surge washes much of the dune away: 4 feet of water.'}}},
]
D = {
    'lesson': '17.R2', 'label': 'Unit 4 Review · Day 2 Lab', 'weekLabel': 'Unit 4 Review', 'week': 17, 'day': 2, 'guide': 'june', 'prefix': 'g4sci-r4-2', 'manifestKey': KEY,
    'paths': {'audio': 'assets/audio/guide/', 'video': 'assets/video/teacher/', 'manifest': 'https://raw.githubusercontent.com/optimaondemand/optima-4th-science/main/video-manifest.json',
              'h2c': 'assets/sparkle/vendor/html2canvas.min.js', 'crew': 'assets/crew/', 'ornaments': 'assets/ornaments/'},
    'crew': crew, 'expedition': {'num': 'U4', 'title': 'The Flood on Bay Street'}, 'ambient': {'icon': '🦗', 'label': 'Field sounds'},
    'case': {
        'num': 'U4 · part 2', 'title': 'The Flood on Bay Street', 'style': 'sheet',
        'hook': 'Main Street is fixed. But the same hurricane pushed seawater into every home on Bay Street. The town council gave me three plans and one budget. They want to know which plan to build before the next storm season. I set up a test tank in the lab. Help me run the tests.',
        'question': 'Which plan should the town build, and how can they make it even better?',
        'how': 'Find 4 clues as you work through the lab. Then crack the case (solve it) at the top of the Assignment tab.',
        'stills': [],
        'logs': [
            {'head': 'Plan A · Sea wall', 'img': 'images/r4-2-seawall.jpg', 'alt': 'Waves crash against a concrete sea wall with steps.', 'rows': [['How it works', 'A tall concrete wall blocks the waves'], ['Cost', '$4 million'], ['Upkeep', 'Low: lasts 30+ years']]},
            {'head': 'Plan B · Living shoreline', 'img': 'images/r4-2-mangroves.jpg', 'alt': 'Mangrove trees with tangled roots grow along calm water.', 'rows': [['How it works', 'Mangroves + oyster reefs calm the waves'], ['Cost', '$1 million'], ['Upkeep', 'Replant after big storms']]},
            {'head': 'Plan C · Sand dune', 'img': 'images/r4-2-dune.jpg', 'alt': 'Sea oats grow on a sandy dune.', 'rows': [['How it works', 'A wall of sand held by sea oats'], ['Cost', '$0.5 million'], ['Upkeep', 'Add new sand after storms']]}],
        'sticky': 'From the council: we have $2 million in all. Bay Street must be ready before the next hurricane season.',
        'stillsCredit': 'Sea wall: ' + CR['wall'] + '. Living shoreline: ' + CR['mang'] + '. Sand dune: ' + CR['dune'] + '. The photos are real; Bay Street and the plans are part of the story.',
        'clues': [
            {'id': 'judge', 'icon': '🚧', 'where': 'Warm-Up: the town’s wish list', 't': 'The town’s biggest limit (constraint): the plan must cost $2 million or less.'},
            {'id': 'tank', 'icon': '🌊', 'where': 'The Lesson, Part 1: the test tank', 't': 'In the big storm: sea wall 1 ft of water, living shoreline 2 ft, sand dune 4 ft, no plan 6 ft.'},
            {'id': 'score', 'icon': '📋', 'where': 'The Lesson, Part 2: score the plans', 't': 'The sea wall and the living shoreline each got 2 ✓, but the sea wall costs $4 million: it breaks the limit.'},
            {'id': 'revise', 'icon': '🔁', 'where': 'The Lesson, Part 3: make it better', 't': 'A sand dune behind the living shoreline cut the water to 1 ft, for $1.5 million in all.'}],
        'solve': {'title': 'Which plan should Bay Street build?', 'q': 'Which answer fits all four clues?', 'options': [
            {'t': 'The sea wall. It kept out the most water in every storm, so it is the best plan for Bay Street.', 'why': 'Check Clues 1 and 3. The sea wall costs $4 million, and the town has $2 million. A plan that breaks a constraint can’t be picked.'},
            {'t': 'The living shoreline with a sand dune behind it. It fits the budget, helps wildlife, and keeps homes mostly dry.', 'right': True,
             'why': 'Case cracked! You met the goals, stayed inside the limit, and revised the winner. Now write your case report: it’s the questions below.'},
            {'t': 'The sand dune alone. It is the cheapest plan, so the town should build it and save the rest of the money.', 'why': 'Check Clue 2. In the big storm, the dune alone let 4 feet of water reach the homes.'}]}},
    'judge': {'afterText': 'Sort them so we know what a good plan must do', 'kicker': 'Warm-Up game · Clue 1', 'title': 'Goal or limit?',
        'todo': ['Read the line from the wish list.', 'Drag it to a side, or tap a side.', 'Sort all 8.'], 'hint': 'Read the line, then drag it to a side, or tap a side.',
        'why': {'icon': '📋', 'q': 'Why sort the wish list?', 't': 'Engineers write down the goals and the limits before they build anything. Then they test every plan against them.'},
        'sides': [{'k': 'goal', 'icon': '✅', 't': 'Goal (criteria)'}, {'k': 'limit', 'icon': '🚧', 't': 'Limit (constraint)'}],
        'cards': [
            {'t': 'Keep seawater out of the homes on Bay Street.', 'side': 'goal', 'why': 'That’s what the plan should DO: a goal.', 'miss': 'Is this something the plan should do, or a limit on it?'},
            {'t': 'Cost $2 million or less.', 'side': 'limit', 'why': 'Money is a limit: a constraint.', 'miss': 'Money is something the town only has so much of.'},
            {'t': 'Give fish and birds a place to live.', 'side': 'goal', 'why': 'A good plan could also help wildlife: a goal.', 'miss': 'Is helping wildlife a thing the plan should do?'},
            {'t': 'Be finished before the next hurricane season.', 'side': 'limit', 'why': 'Time is a limit: a constraint.', 'miss': 'Time is something the town only has so much of.'},
            {'t': 'Don’t block the town’s boat ramp.', 'side': 'limit', 'why': 'A rule the plan must follow: a constraint.', 'miss': 'This is a “must not”. Is that a goal or a limit?'},
            {'t': 'Last for at least 20 years.', 'side': 'goal', 'why': 'How long it lasts is part of how good the plan is: a goal.', 'miss': 'Lasting a long time is something a good plan should do.'},
            {'t': 'Fit in the 50 feet of land between the water and the homes.', 'side': 'limit', 'why': 'Space is a limit: a constraint.', 'miss': 'There is only so much land. Is that a goal or a limit?'},
            {'t': 'Keep the beach open for families.', 'side': 'goal', 'why': 'That’s something the town wants the plan to do: a goal.', 'miss': 'Is this something the town wants, or a limit?'}],
        'win': 'Clue 1: the town’s biggest limit is money. The plan must cost $2 million or less.', 'clue': 'judge'},
    'tank': {'afterText': 'Watch how much water reaches the homes', 'kicker': 'Part 1 lab · Clue 2', 'title': 'Shoreline test tank',
        'model': 'This is a model. The numbers are made up, but they follow what scientists have measured: walls block water, and roots and reefs take energy out of waves.',
        'todo': ['Pick a plan and a storm.', 'Press Run the storm and read how much water reaches the homes.', 'Test the sea wall, the living shoreline, and the sand dune in the big storm.'],
        'why': {'icon': '🧪', 'q': 'What is a test tank?', 't': 'A long tank of water where engineers make small waves to test a model of a shore. It lets them try many plans without waiting for a real storm.'},
        'plans': PLANS,
        'storms': [{'k': 'small', 'icon': '🌧️', 't': 'Tropical storm', 'surge': 3}, {'k': 'med', 'icon': '🌀', 't': 'Category 1', 'surge': 6}, {'k': 'big', 'icon': '🌪️', 't': 'Category 3', 'surge': 12}],
        'need': [['wall', 'big'], ['ls', 'big'], ['dune', 'big']], 'needLine': 'Keep testing: run the sea wall, the living shoreline, and the sand dune in the big storm (Category 3).',
        'runBtn': '▶ Run the storm',
        'q': 'In the big storm, what did your tests show?',
        'opts': [{'t': 'The sea wall let in the least water, but it costs the most.', 'ok': True},
                 {'t': 'All three plans kept the homes completely dry.', 'miss': 'Look at the big-storm column in your table.'},
                 {'t': 'The sand dune worked best in every storm.', 'miss': 'How much water got past the dune in the big storm?'}],
        'credit': 'No plan: ' + CR['storm'] + '. Sea wall: ' + CR['wall'] + '. Living shoreline: ' + CR['mang'] + '. Sand dune: ' + CR['dune'] + '.',
        'win': 'Clue 2: in the big storm, the sea wall let in 1 ft of water, the living shoreline 2 ft, and the dune 4 ft.', 'clue': 'tank'},
    'score': {'afterText': 'Use your test results to score', 'kicker': 'Part 2 lab · Clue 3', 'title': 'Score the plans',
        'todo': ['Read a row.', 'Tap ✓ if the plan meets it, or ✗ if it doesn’t.', 'Score both plans on every row.'],
        'why': {'icon': '📋', 'q': 'What is a scorecard?', 't': 'Engineers line up the plans side by side and check each one against the same goals and limits. It keeps the choice fair.'},
        'plans': [{'k': 'wall', 'icon': '🧱', 'name': 'Sea wall'}, {'k': 'ls', 'icon': '🦪', 'name': 'Living shoreline'}],
        'rows': [
            {'t': 'Keeps homes mostly dry (1 ft or less) in a big storm', 'kind': 'goal', 'ans': {'wall': True, 'ls': False}, 'miss': 'Check your test tank table: how much water reached the homes in the big storm?'},
            {'t': 'Helps wildlife', 'kind': 'goal', 'ans': {'wall': False, 'ls': True}, 'miss': 'Look at the Wildlife column in your table.'},
            {'t': 'Protects the town right away', 'kind': 'goal', 'ans': {'wall': True, 'ls': False}, 'miss': 'Look at the Ready column. Mangroves need time to grow.'},
            {'t': 'Costs $2 million or less', 'kind': 'limit', 'ans': {'wall': False, 'ls': True}, 'miss': 'Check the cost of each plan in the case file.'}],
        'q': 'Both plans got 2 ✓. Which one can the town choose?',
        'opts': [{'t': 'The living shoreline. The sea wall breaks the $2 million limit, and a plan that breaks a constraint can’t be picked.', 'ok': True},
                 {'t': 'The sea wall, because it keeps out the most water.', 'miss': 'Look at the limit row. Can the town pay $4 million?'},
                 {'t': 'Neither one. It’s a tie, so they should build nothing.', 'miss': 'A tie on goals? Check which plan stays inside the limit.'}],
        'win': 'Clue 3: both plans got 2 ✓, but the sea wall breaks the $2 million limit. The living shoreline wins.', 'clue': 'score'},
    'revise': {'afterText': 'Then pick a fix and re-run the big storm', 'kicker': 'Part 3 lab · Clue 4', 'title': 'Make it better',
        'todo': ['Pick the living shoreline’s weak spot.', 'Pick a fix.', 'Press Re-run the big storm. Keep trying until the plan meets the goal AND the limit.'],
        'why': {'icon': '🔁', 'q': 'Why test again?', 't': 'A fix is just a guess until you test it. Engineers test, fix, and test again.'},
        'weakQ': 'The town picked the living shoreline. What is its weak spot?',
        'weak': [{'t': 'In a big storm, 2 feet of water still reaches the homes.', 'ok': True},
                 {'t': 'It costs too much.', 'miss': 'It costs $1 million. The town has $2 million.'},
                 {'t': 'It hurts wildlife.', 'miss': 'Mangroves and oysters give fish and birds a home.'}],
        'fixQ': 'Pick a fix. The town has $2 million in all.', 'budget': 2,
        'fixes': [
            {'k': 'dune', 'icon': '🏖️', 't': 'Add a sand dune with sea oats behind the mangroves', 'costT': '+ $0.5 million', 'cost': 1.5, 'totalT': '$1.5 million', 'ft': 1, 'ok': True,
             'why': 'Two layers of protection: the mangroves and oysters calm the waves, then the dune stops most of the water. Homes stay mostly dry, it fits the budget, and turtles get a nesting beach.'},
            {'k': 'wall', 'icon': '🧱', 't': 'Add a sea wall too', 'costT': '+ $4 million', 'cost': 5, 'totalT': '$5 million', 'ft': 0, 'ok': False,
             'why': 'The homes stay dry, but $5 million breaks the $2 million limit. The town can’t pick it.'},
            {'k': 'more', 'icon': '🌱', 't': 'Plant more mangroves', 'costT': '+ $0.3 million', 'cost': 1.3, 'totalT': '$1.3 million', 'ft': 2, 'ok': False,
             'why': 'A good idea for later! But young mangroves take years to grow, so in the next big storm, 2 feet of water still reaches the homes.'},
            {'k': 'raise', 'icon': '🏠', 't': 'Raise every house on Bay Street', 'costT': '+ $6 million', 'cost': 7, 'totalT': '$7 million', 'ft': 0, 'ok': False,
             'why': 'Raised homes stay dry, but $7 million is way over the $2 million limit.'}],
        'runBtn': '▶ Re-run the big storm',
        'win': 'Clue 4: a sand dune behind the living shoreline cut the water to 1 foot, for $1.5 million in all.', 'clue': 'revise'},
    'quizKicker': '', 'quizMiss': {'q1': {'A': 'A goal is what the plan should DO. Is a money limit a goal?', 'C': 'An effect is a change caused by something. Is this a change?'},
        'q2': {'B': 'Built mitigation is made by people, like concrete walls. Are mangroves built?', 'C': 'Planning mitigation is rules and plans on paper. Are oysters a plan?'},
        'q3': {'B': 'A constraint is a limit. Did adding a dune set a limit?', 'C': 'A hazard is a natural event. Did the engineers make a storm?'}},
    'flags': {
        'ans-1': [{'label': 'something the sea wall did better', 're': 'wall'}, {'label': 'something the living shoreline did better', 're': 'living|shoreline|mangrove|oyster'},
                  {'label': 'a number from your tests', 're': '[0-9]|one|two|four|six|million'}],
        'ans-2': [{'label': 'what a constraint is', 're': 'limit|constraint|must|money|budget|cost|afford'},
                  {'label': 'why it matters', 're': 'can.?t|cannot|not allowed|break|over|too much|no money|pay'},
                  {'label': 'a because or so', 're': 'because|so |which|that means|this means|if'}],
        'cer-4': [{'label': 'your claim', 're': 'good|best|solution|goal|limit|criteria|constraint|meet'},
                  {'label': 'two pieces of evidence', 'any': ['wall', 'living|shoreline|mangrove|oyster', 'dune', '[0-9]', 'million|cost|money|budget', 'wildlife|fish|bird|turtle', 'ft|feet|foot|water'], 'min': 2},
                  {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves'}]},
    'minWords': {'ans-1': 20, 'ans-2': 15, 'cer-4': 30},
    'hints': {
        'ans-1': ['Look at your test tank table and the Wildlife and Cost columns.', 'One thing the wall did better is about water. One thing the shoreline did better is about wildlife or money.', 'Try: The sea wall did better at ___ (only ___ ft). The living shoreline did better at ___.'],
        'ans-2': ['Remember: a constraint is a limit, a MUST.', 'What happens if a town spends money it doesn’t have?', 'Try: The town can’t pick it because a constraint is ___. If a plan breaks it, ___.'],
        'cer-4': ['A good solution meets the goals AND stays inside the limits. Do you agree?', 'Use your tests: the sea wall’s cost, the dune that fixed the weak spot.', 'Try: A good solution ___. One piece of evidence is ___. Another is ___. This shows ___.']},
    'scholar': {},
    'planner': {'before': 'cer-4', 'title': 'Your claim and two pieces of evidence', 'rows': [
        {'label': '1. Pick your claim', 'options': ['A good solution meets the goals and stays inside every limit.', 'A good solution is the biggest, strongest one.'], 'pick': 1},
        {'label': '2. Pick two pieces of evidence from your tests', 'pick': 2, 'options': [
            'The sea wall let in the least water, but it costs $4 million: over the limit.', 'The living shoreline cost $1 million and helped wildlife.',
            'With a dune added, the living shoreline kept homes mostly dry for $1.5 million.', 'The sand dune alone let in 4 feet of water in the big storm.',
            'Both plans got 2 ✓, so the limit decided the winner.']}],
        'note': 'Tap your claim and two facts. Then write your reasoning in your own words.'},
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': ['The wish list, all sorted (Warm-Up)', 'Your test tank table (The Lesson)', 'Your finished scorecard (The Lesson)', 'The answer that cracked the case (Assignment)']},
    'sketch': {'tip': 'Draw with the pen. Then use 🏷️ Label: drag from a part of your sketch to an empty spot, and type its name.',
        'prompts': ['My revised plan', 'The test tank', 'Goals and limits'],
        'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 2,
                    'prompts': ['Draw your plan from the ocean to the homes', 'Show what calms the waves and what stops the water', 'Label 2 parts']}]},
    'hlCoach': {'title': 'Highlight like a scientist', 'tips': [
        ['🔑', 'Highlight key words, not whole paragraphs.', 'If everything is yellow, nothing stands out. Aim for a few words in each paragraph.'],
        ['📖', 'Look for words that are explained.', 'Bold words, and words followed by a meaning in ( ), are often worth saving.'],
        ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me explain how engineers choose a plan?'],
        ['🔗', 'Watch for clue words.', '“But”, “AND” and “no matter” show how ideas connect.'],
        ['🎨', 'Use the colors on purpose.', 'Yellow = important. Green = evidence I might use in my answer. Pink = something I wonder about.']],
        'practice': {'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.', 'text': 'A plan has to meet the goals and stay inside the limits.',
                     'key': ['plan', 'meet', 'goals', 'inside', 'limits'], 'small': ['A', 'has', 'to', 'the', 'and'],
                     'model': 'A scientist might highlight “meet”, “goals”, “inside” and “limits”. Those words carry the idea.'},
        'outside': 'This works in every subject. When you read anything, save the words that answer your question, and skip the rest.'},
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🦪', 'name': 'Oyster shell from the living shoreline',
                 'line': 'You cracked the Bay Street case, and an oyster shell from the new living shoreline goes in your Field Notebook. Unit 4 is complete. You’re ready for the test!'},
    'notebookTitle': 'Unit 4 · Natural Forces & Safety',
    'notebook': [{'lesson': '16.01'}, {'lesson': '16.02'}, {'lesson': '17.01'}, {'lesson': '17.02'}, {'lesson': '17.R1', 'icon': '🪨', 'name': 'Limestone sample'}, {'lesson': '17.R2', 'icon': '🦪', 'name': 'Oyster shell'}],
    'rankLine': 'Your Field Station ID just updated. Keep going, engineer.', 'lensWin': 'All six words are in focus. You’ll use every one of them today.',
    'exploreMod': 'revise',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'list', 'find': {'sel': '.fs-game[data-mod="judge"]'}, 'label': 'Warm-Up: one more goal and one more limit',
         'q': 'Warm-Up: Add one more goal and one more limit the town might have.', 'title': 'Your turn: add one more goal and one more limit for Bay Street.',
         'min': 2, 'unit': 'lines', 'addLabel': '+ Add a line', 'ph': ['Goal: the plan should…', 'Limit: the plan must…']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'}, 'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Write the town a short brief'}, 'label': 'Part C: Engineering Brief',
         'q': 'Part C: Engineering Brief: the hazard, two goals and one limit, my pick with evidence, and how I would make it better', 'title': 'My Engineering Brief',
         'fields': [{'t': 'The hazard and the town', 'icon': '🌀', 'ph': 'The hazard is ___. It hurts Bay Street by…', 'long': True}, {'t': 'Two goals and one limit', 'icon': '📋', 'ph': 'Goals: 1. ___ 2. ___ Limit: ___', 'long': True},
                    {'t': 'My pick and my evidence', 'icon': '🏆', 'ph': 'I pick ___ because my tests showed…', 'long': True}, {'t': 'How I’d make it better', 'icon': '🔁', 'ph': 'I would add ___ so that…', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'}, 'reminder': 'Claim = what you think is true. Evidence = facts from your tests that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'What makes a good engineering solution?', 'ph': 'A good engineering solution…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from your tests. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-1': 'Part B · Question 1', 'ans-2': 'Part B · Question 2', 'cer-4': 'Use Your Evidence (CER)'}},
    ],
}

S = {
    'welcome': ('Welcome · the flood on Bay Street', '30–40 s', 'June here! Main Street is safe now, but Bay Street had a rough storm. Seawater pushed right into people’s homes. The town council handed me three plans and a budget, and they want an answer before the next hurricane season. Today you’re my engineer. Let’s test those plans.'),
    'warmup': ('Warm-Up · goal or limit? (Clue 1)', '20–30 s', 'Here’s the council’s wish list. Before we test anything, we sort it. A goal is something the plan should do. A limit is something the plan has to stay inside, like money, time, or space. Read each line carefully. Some are tricky.'),
    'vocab': ('Word Wall', '30–45 s', None), 'lesson': ('The Lesson', '25–35 s', None),
    'part1': ('Part 1 · the test tank (Clue 2)', '25–35 s', 'Welcome to my test tank! Ocean on the left, the town on the right, and your plan in the middle. Pick a plan, pick a storm, and run it. Watch the water at the homes. Make sure you try every plan in the big storm. That’s the one that matters most.'),
    'part2': ('Part 2 · score the plans (Clue 3)', '20–30 s', 'Now we score the two strongest plans, side by side. Use your test results for each row. Here’s my tip: count the check marks, then look very carefully at the row that says limit.'),
    'part3': ('Part 3 · make it better (Clue 4)', '20–30 s', 'Every plan has a weak spot. First, find the living shoreline’s weak spot. Then try a fix and re-run the big storm. If your fix breaks the budget, try another one. Engineers never get it perfect the first time.'),
    'quiz': ('Self-Check', '15–20 s', None),
    'assignment': ('Assignment · crack the case', '20–30 s', 'All four clues? Then crack the case at the top of this tab: which plan should Bay Street build? After that, answer two questions, write the town an engineering brief, and finish with your CER.'),
    'partb': ('Part B', '30 s', None), 'partc': ('Part C · engineering brief', '30 s', None),
    'evidence': ('Use your evidence · CER', '25–35 s', 'The council wants to know what makes a good engineering solution. That’s a big question! Think about the sea wall’s price, the living shoreline, and the dune that fixed the weak spot. Pick your claim, tap two pieces of evidence, and explain your thinking.'),
    'closing': ('Case closed', '20–30 s', 'Case closed! Bay Street gets a living shoreline with a dune behind it. It fits the budget, it helps wildlife, and the homes stay mostly dry. You did real engineering today. Good luck on the Unit 4 test. You’ve got this.'),
}
D['slots'] = {k: ({'label': v[0], 'length': v[1], 'script': v[2]} if v[2] else {'label': v[0], 'length': v[1]}) for k, v in S.items()}

V = {'slots': {
    'welcome': {'label': 'Welcome · the flood on Bay Street', 'length': '50–60 s', 'want': True, 'parts': [
        {'kind': 'photo', 'pic': 'r42storm', 'label': '🌊 Storm surge'},
        {'label': '🗂 Three plans', 'tag': 'CASE FILE U4 · PART 2', 'title': 'The Flood on Bay Street', 'col': '#1F6F78', 'body': 'Sea wall $4 million · Living shoreline $1 million · Sand dune $0.5 million. Budget: $2 million.'}],
        'script': 'Welcome to lab day, engineers!\n\n[ON SCREEN: Storm surge]\nRemember storm surge? The hurricane’s wind pushes ocean water onto land. That’s what flooded Bay Street.\n\n[ON SCREEN: Three plans]\nThe town has three plans and only two million dollars. Hmm. Which one would you pick? Today we’ll test them, just like real engineers. Press Listen on June’s walkie-talkie, right below me.'},
    'warmup': {'label': 'Warm-Up · goal or limit?', 'length': '40–50 s', 'want': True, 'parts': [
        {'label': '✅ Goal or limit', 'tag': 'WARM-UP', 'title': 'Criteria and constraints', 'col': '#1F6F78', 'body': 'Goal (criteria) = what the plan should DO. Limit (constraint) = what it must stay inside.'}],
        'script': 'Before engineers build anything, they write down two lists.\n\n[ON SCREEN: Goal or limit]\nGoals, also called criteria, are what the plan should do. Limits, also called constraints, are what the plan has to stay inside, like money or time. (Hold your hands up like a box.) Sort the town’s wish list. Press Listen on June’s walkie-talkie, right below me.'},
    'part1': {'label': 'Part 1 · the test tank', 'length': '40–50 s', 'want': True, 'parts': [
        {'kind': 'photo', 'pic': 'r42mang', 'label': '🦪 Living shoreline'},
        {'label': '🧪 Test tank', 'tag': 'PART 1', 'title': 'A model of Bay Street', 'col': '#D4772C', 'body': 'Pick a plan · pick a storm · run it · read the water at the homes.'}],
        'script': 'Time to test!\n\n[ON SCREEN: Test tank]\nOur test tank is a model, a small version of Bay Street. Pick a plan, pick a storm, and run it.\n\n[ON SCREEN: Living shoreline]\nThis is a living shoreline. Mangrove roots and oyster reefs take energy out of the waves. Test all three plans in the big storm and look at your table. Press Listen on June’s walkie-talkie, right below me.'},
    'part2': {'label': 'Part 2 · score the plans', 'length': '40–50 s', 'want': True, 'parts': [
        {'label': '📋 Scorecard', 'tag': 'PART 2', 'title': 'Same rows for every plan', 'col': '#D4772C', 'body': 'Tap ✓ or ✗ for each plan on each row. Watch the limit row!'}],
        'script': 'Now we make it fair.\n\n[ON SCREEN: Scorecard]\nWe score both plans on the same rows, using your test results. Here’s a secret engineers know: a limit is a must. If a plan breaks a limit, it can’t win, even with lots of check marks. Press Listen on June’s walkie-talkie, right below me.'},
    'part3': {'label': 'Part 3 · make it better', 'length': '40–50 s', 'want': True, 'parts': [
        {'kind': 'photo', 'pic': 'r42dune', 'label': '🏖️ Sand dune'},
        {'label': '🔁 Revise', 'tag': 'PART 3', 'title': 'Test, fix, test again', 'col': '#B5543A', 'body': 'Find the weak spot. Pick a fix. Re-run the big storm.'}],
        'script': 'The winner still has a weak spot.\n\n[ON SCREEN: Revise]\nEngineers revise. They fix the weak spot and test again. Try a fix and re-run the big storm. If it breaks the budget, try another one.\n\n[ON SCREEN: Sand dune]\nHmm, I wonder if two kinds of protection together could work. Press Listen on June’s walkie-talkie, right below me.'},
    'assignment': {'label': 'Assignment · crack the case', 'length': '40–50 s', 'want': True, 'parts': [
        {'label': '🗂 Crack the case', 'tag': 'ASSIGNMENT', 'title': 'Your recommendation', 'col': '#34B76F', 'body': 'Pick the plan that fits all four clues. Then Part B, your engineering brief, and your CER.'}],
        'script': 'You’re ready to make your recommendation!\n\n[ON SCREEN: Crack the case]\nUse all four clues to pick the plan Bay Street should build. Then answer two questions and write the town an engineering brief. That’s a short report that helps people decide. Copy your gathered answers into Canvas when you finish. Press Listen on June’s walkie-talkie, right below me.'},
    'evidence': {'label': 'Use your evidence · CER', 'length': '40–50 s', 'want': True, 'parts': [
        {'label': '✏️ CER', 'tag': 'CER', 'title': 'What makes a good solution?', 'col': '#8B6FC0', 'body': 'Claim: what you think. Evidence: two facts from your tests. Reasoning: how they prove it.'}],
        'script': 'Last one, and it’s a big one.\n\n[ON SCREEN: CER]\nWhat makes a good engineering solution? Your claim answers the question. Your evidence comes from your tests, like the sea wall’s price or the dune fix. Your reasoning ties them together. The Unit 4 test asks this exact kind of question, so this is perfect practice. Press Listen on June’s walkie-talkie, right below me.'},
}, 'pics': {
    'r42storm': {'src': 'images/r4-1-case-storm.jpg', 'cap': 'Storm surge, Tampa, 2023 (Andrew Heneen, CC BY 4.0)'},
    'r42mang': {'src': 'images/r4-2-mangroves.jpg', 'cap': 'Mangrove shoreline, Biscayne National Park (NPS, public domain)'},
    'r42dune': {'src': 'images/r4-2-dune.jpg', 'cap': 'Sea oats on a Florida dune (Georgialh, CC BY-SA 4.0)'}},
    'other': ['vocab', 'lesson', 'quiz', 'partb', 'partc', 'closing']}

if __name__ == '__main__':
    review_page.write(PAGE, HERE)
    json.dump(D, open(os.path.join(HERE, 'data.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump(V, open(os.path.join(HERE, 'video.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('wrote data.json + video.json')
