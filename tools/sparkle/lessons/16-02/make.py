#!/usr/bin/env python3
"""Writes data.json and fixes.json for 16.02 (run from this folder). Case 16 part 2 "The Last Pit": Palmetto Springs, June Calloway."""
import json, copy
P = json.load(open('../12-01/data.json', encoding='utf-8'))
Q = json.load(open('../16-01/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

# ---------------------------------------------------------------- ticked fixes (Bethany, 21 Oct 2026)
fx('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist already asks for a decision matrix',
   '🎨 Part C &mdash; Build Your Own Food Chain', '📊 Part C &mdash; Build a Decision Matrix')
fx('fix', 'copy-paste leftover: Part C task from 9.01 (typed on the page now)',
   r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
   "Pick one of the four Florida challenges from Part 3 (or one you make up). Compare two solutions like an engineer: name the goals and a limit, score each solution, choose one, and suggest a way to make it better.</p>", True)
fx('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', 'supply list: “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list: no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)
fx('fix', 'quarter label in the footer: this lesson closes out Quarter 2 (the page says so)', 'Science &middot; Quarter 3 &middot;', 'Science &middot; Quarter 2 &middot;')
fx('fix', 'this is an Earth science lesson (4-ESS3-1), not life science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Earth Science</div>')
fx('fix', 'Florida has no offshore wind turbines; a real Florida option instead', '(B) Build offshore wind turbines', '(B) Put solar panels on school and store rooftops')

# ---------------------------------------------------------------- plain language
fx('plain', 'shorter',
   "Hold this question in your head as you work. By the end of the lesson, you'll be able to compare at least two solutions for one Florida resource problem, choose one, and propose a way to improve it.",
   "Keep this question in mind. By the end, you’ll be able to compare two or more solutions to a Florida problem, choose one, and make it better.")
fx('plain', 'plain words', "Imagine the Florida city you live in needs more clean drinking water. Engineers and city leaders have to pick a way to get it. Three possible ideas are on the table:",
   "Imagine your Florida city needs more clean drinking water. Engineers and city leaders have to pick a way to get it. Here are three ideas:")
fx('plain', 'cut filler', "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
   "<strong>Tap a card to flip it</strong> and read what the word means.")
fx('plain', 'dash removed; plain words',
   "<p>Engineers don't just look for \"the best idea.\" They define what \"best\" even means — and what they can't change.",
   "<p>Engineers don’t just look for “the best idea.” First they decide what “best” means, and what they can’t change.")
fx('plain', 'shorter examples', '<li><strong>Criteria</strong> = the goals. (Examples: "Provide enough water for 10,000 people," "Cost less than $50 million," "Don\'t pollute the springs.")</li>',
   '<li><strong>Criteria</strong> = the goals. A goal can be met well, just OK, or poorly. (Example: “Provide enough water for 10,000 people.”)</li>')
fx('plain', 'shorter examples', '<li><strong>Constraints</strong> = the limits. (Examples: "Must finish in 3 years," "Can\'t use new land," "Must follow Florida water laws.")</li>',
   '<li><strong>Constraints</strong> = the limits. A limit is pass or fail. (Example: “Must cost less than $50 million.”)</li>')
fx('plain', 'dash removed', '</span></span> side by side. The tool they often use is called a <em>decision matrix</em> — a chart that scores each',
   '</span></span> side by side. They often use a <em>decision matrix</em>: a chart that scores each')
fx('plain', 'shorter', "Engineers don't stop at \"pick one.\" They look at the gaps and figure out how to make the chosen solution stronger. Maybe by combining ideas, adding a protection strategy, or trying a small test first.</p>",
   "Engineers look at the gaps and make the chosen solution stronger, maybe by combining ideas or testing a small model first.</p>")
fx('plain', 'the diagram is Part 3 now', 'margin-top:22px;">Four Engineering Challenges</h3>', 'margin-top:22px;">Part 3 · Four Florida Challenges</h3>')
fx('plain', 'the challenges are in Part 3 of the Lesson',
   "Pick one of the four engineering challenges from the diagram (city water, clean electricity, beach erosion, or plastic waste).",
   "Pick one of the four Florida challenges from Part 3 (city water, clean electricity, beach erosion, or plastic waste).")
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   "Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today's lesson.")
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('plain', 'shorter closing; dash removed', r'<p><strong>You\'ve closed out Quarter 2\.</strong> You can now define.*?</p>',
   '<p><strong>You’ve closed out Quarter 2.</strong> You can now set criteria and constraints, compare solutions, and revise the winner. That’s real engineering. Next week: what happens to Florida’s land when a big storm hits?</p>', True)

# ---------------------------------------------------------------- lean cuts
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its matrix becomes Part C; the facts and Go Deeper go with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)
fx('cut', 'lean: Stop & Think repeats the warm-up game', r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: the misconception box repeats the revise paragraph', r"<p><strong>Common misconception:</strong> Some people think real engineering is about coming up with one perfect idea\..*?</p>\s*", '', True)
fx('cut', 'lean: the Key Concept box repeats Part 2', r'<div style="background:#FFF6E5;border:2.5px solid #F0C97A;[^"]*">\s*<div[^>]*>⭐ Key Concept</div>\s*<p[^>]*>.*?</p>\s*</div>\s*', '', True)
fx('cut', 'lean: Stop & Reason asks what Make it better does', r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('cut', 'lean: Observe & Reason, the Amazing Fact, the Florida connection and Go Deeper at the end of the Lesson; Part 4 = the old Explore; next button goes to Self-Check',
   r'<div class="socratic-q">\s*<span class="sq-icon">👀</span>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
   H3 + 'Part 4 · Test It Small</h3>\n      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">Engineers rarely build the real thing first. They test a small model, because a problem is much cheaper to fix on a model. June built a model of the improved pit. Run each test, see what goes wrong, and revise it.</p>\n      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', True)
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('cut', 'lean: Part B question 6 removed (Bethany kept 5 and 7)', r'<div class="pq">\s*<span class="pq-num"[^>]*>6</span>.*?</textarea>\s*', '', True)
fx('cut', 'lean: renumber Part B (7 → 6)', '<span class="pq-num" style="background:#D4772C;">7</span>', '<span class="pq-num" style="background:#D4772C;">6</span>')
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fx('cut', 'lean: Part C typed on the page',
   "A decision matrix comparing 2 solutions against 2 criteria, with star ratings, a chosen winner, and a revision suggestion.",
   "Two solutions compared with 2 criteria and a limit, star scores, a winner, and a way to make it better.")
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist', '<strong>Evidence Response:</strong> I made a claim about whether the first idea is always the best, and supported it with two pieces of evidence from the lesson.',
   '<strong>Use Your Evidence:</strong> My claim about whether the first idea is always the best, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', True)

# ---------------------------------------------------------------- the three designs (blueprints)
def bp(body):
    return ('<svg viewBox="0 0 200 90" xmlns="http://www.w3.org/2000/svg" aria-hidden="true" fill="none" stroke="#FFFFFF" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">'
            '<path d="M6,24 H194" stroke-dasharray="3 3" opacity=".6"/>' + body + '</svg>')
LAKE = bp('<path d="M20,24 L60,44 L140,44 L180,24"/><path d="M34,31 L166,31" stroke="#9FD3F0" stroke-dasharray="5 4"/><path d="M38,30 l2,-8 l2,8 M50,36 l2,-8 l2,8 M150,36 l2,-8 l2,8 M162,30 l2,-8 l2,8"/><path d="M98,18 c4,-8 10,-8 12,0" /><text x="100" y="62" fill="#FFFFFF" stroke="none" font-size="9" text-anchor="middle" font-family="Nunito,sans-serif">shallow, planted edges</text>')
RES = bp('<path d="M30,24 L36,80 L164,80 L170,24"/><path d="M34,34 L166,34" stroke="#9FD3F0" stroke-dasharray="5 4"/><path d="M178,24 v-10 h10 v10"/><text x="100" y="58" fill="#FFFFFF" stroke="none" font-size="9" text-anchor="middle" font-family="Nunito,sans-serif">deep, steep sides</text><text x="183" y="10" fill="#FFFFFF" stroke="none" font-size="7" text-anchor="middle" font-family="Nunito,sans-serif">pump</text>')
SOL = bp('<path d="M30,24 L36,80 L164,80 L170,24"/><path d="M34,30 L166,30" stroke="#9FD3F0" stroke-dasharray="5 4"/><path d="M44,26 l16,-8 M66,26 l16,-8 M88,26 l16,-8 M110,26 l16,-8 M132,26 l16,-8"/><text x="100" y="58" fill="#FFFFFF" stroke="none" font-size="9" text-anchor="middle" font-family="Nunito,sans-serif">panels float on the water</text>')
I = lambda n: 'images/16-02-' + n + '.jpg'
FACTS = ('L-8 Reservoir: Florida Department of Environmental Protection (a former rock mine site in Palm Beach County; 53 feet deep; stores up to 15 billion gallons). '
         'Palmetto Springs, its designs and their costs are made up for this lesson.')

D = {
    'lesson': '16.02', 'week': 16, 'day': 2, 'guide': 'june', 'prefix': 'g4sci-16-2', 'manifestKey': '16-02',
    'paths': P['paths'], 'crew': Q['crew'],
    'expedition': {'num': 16, 'title': 'The Last Pit'},
    'ambient': {'icon': '🐦', 'label': 'Lake sounds'},
    'case': {
        'num': 16, 'title': 'The Last Pit', 'style': 'hall',
        'hook': 'Fast-forward 20 years. The Palmetto Springs quarry is digging its very last pit, and the town has to decide what it becomes. Three designs are pinned on my drafting table. Which one should we build, and can we make it even better?',
        'plans': [
            {'tag': 'Design A', 'icon': '🦢', 't': 'Bird lake park', 'svg': LAKE, 'rows': [['Idea', 'A lake with shallow, planted edges for birds, plus a trail'], ['Cost', '$2 million']]},
            {'tag': 'Design B', 'icon': '💧', 't': 'Water reservoir', 'svg': RES, 'rows': [['Idea', 'A deep pit that stores water for dry months'], ['Cost', '$3.5 million']]},
            {'tag': 'Design C', 'icon': '☀️', 't': 'Floating solar farm', 'svg': SOL, 'rows': [['Idea', 'Solar panels floating on the water make electricity'], ['Cost', '$6 million']]}],
        'stills': [],
        'stillsCredit': 'The town, the designs and the costs are made up. Design B is like a real Florida project: the L-8 Reservoir, an old rock mine that now stores water.',
        'question': 'Which design should Palmetto Springs build in the last pit, and how can they make it better?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'limits', 'icon': '🚧', 'where': 'Warm-Up: limit or goal?', 't': 'A limit is pass or fail, like the town’s $4 million budget. A goal gets scored: more stars is better.'},
            {'id': 'matrix', 'icon': '📊', 'where': 'The Lesson, Part 2: build the matrix', 't': 'The floating solar farm broke the budget limit, so it’s out. The bird lake and the reservoir tied at 6 stars.'},
            {'id': 'improve', 'icon': '🔧', 'where': 'The Lesson, Part 2: make it better', 't': 'Borrowing one feature from another design beat both first ideas, and it still fit the budget.'},
            {'id': 'pilot', 'icon': '🧪', 'where': 'The Lesson, Part 4: test it small', 't': 'Testing a model showed two problems no one saw on paper. A spillway and a sloped shelf fixed them.'},
        ],
        'solve': {
            'title': 'What should the last pit become?', 'q': 'Which answer fits all four clues?',
            'options': [
                {'t': 'The floating solar farm, because it got 3 stars for being useful.', 'why': 'Check Clue 2. Did the solar farm fit the budget?'},
                {'t': 'Whichever design was pinned up first. The first idea is usually the best one.', 'why': 'Check Clue 3. Did the first ideas score as well as the improved one?'},
                {'t': 'One of the tied designs, made better: borrow a feature from the other design, stay inside the budget, then test a model and revise it until it works.', 'right': True,
                 'why': 'Case cracked! You set limits and goals, compared, improved and tested, just like real engineers. Now write your case report: it’s the questions below.'},
            ]},
    },
    'limits': {
        'afterText': 'Here are three ideas', 'kicker': 'Warm-Up game', 'title': 'Limit or goal?',
        'todo': ['Read the card from the town’s plan for the last pit.', 'Drag it to LIMIT or GOAL (or tap the card, then a box).', 'Sort all 8, then answer the question.'],
        'why': {'icon': '🚧', 'q': 'What’s the difference?', 't': 'A limit is a gate: a design passes or fails. A goal is a score: a design can meet it well, just OK, or poorly.'},
        'zones': {'limit': {'icon': '🚧', 't': 'LIMIT (constraint)', 'sub': 'Pass or fail. Yes or no.'},
                  'goal': {'icon': '⭐', 't': 'GOAL (criterion)', 'sub': 'Score it. More is better.'}},
        'cards': [
            {'id': 'budget', 'icon': '💵', 't': 'Must cost $4 million or less', 'k': 'limit', 'why': 'A design costs $4 million or less, or it doesn’t. Pass or fail.', 'miss': 'Can a design be “a little bit” under budget and still get stars? Or is it yes or no?'},
            {'id': 'birds', 'icon': '🪶', 't': 'Helps birds and other wildlife', 'k': 'goal', 'why': 'A design can help wildlife a lot, a little or barely. That’s a score.', 'miss': 'Could one design help wildlife MORE than another? Then it’s scored.'},
            {'id': 'slopes', 'icon': '⛰️', 't': 'Edges must be gentle enough that no one can fall in', 'k': 'limit', 'why': 'Safe or not safe. There’s no “a little safe” for the town.', 'miss': 'Is safety something the town would accept “just OK” on? Or is it yes or no?'},
            {'id': 'store', 'icon': '💧', 't': 'Stores water for the dry months', 'k': 'goal', 'why': 'A design can store lots of water, some, or a little. That’s a score.', 'miss': 'Could one design store MORE water than another? Then it’s scored.'},
            {'id': 'time', 'icon': '📅', 't': 'Must be finished within 3 years', 'k': 'limit', 'why': 'It’s finished in 3 years, or it isn’t. Pass or fail.', 'miss': 'A deadline is met or missed. Is that a score, or yes or no?'},
            {'id': 'useful', 'icon': '🏙️', 't': 'Gives the town something useful, like power or a park', 'k': 'goal', 'why': 'Some designs give the town more than others. That’s a score.', 'miss': 'Could one design be MORE useful than another? Then it’s scored.'},
            {'id': 'wells', 'icon': '🚰', 't': 'Can’t take water the town wells need', 'k': 'limit', 'why': 'The wells keep their water, or they don’t. Pass or fail.', 'miss': 'Would the town accept a design that takes just a little of the wells’ water? Or is it yes or no?'},
            {'id': 'pretty', 'icon': '🌅', 't': 'Looks nice to the neighbors', 'k': 'goal', 'why': 'A design can look great, OK or not so nice. That’s a score.', 'miss': 'Could one design look nicer than another? Then it’s scored.'}],
        'q': 'Which one is a LIMIT, not a goal?',
        'opts': [{'t': 'Helps birds and other wildlife', 'miss': 'Can a design help birds a lot or a little? Then it’s a goal.'},
                 {'t': 'Must cost $4 million or less', 'ok': True},
                 {'t': 'Looks nice to the neighbors', 'miss': 'Can a design look nicer or less nice? Then it’s a goal.'}],
        'win': 'Limits are pass or fail. Goals get scored. That’s a clue.',
        'clue': 'limits'},
    'matrix': {
        'afterSel': '#tab-lesson .lesson-figure', 'kicker': 'Part 2 game', 'title': 'Build the matrix',
        'todo': ['Tap a ? box. Read the evidence for that design and goal.', 'Give it ⭐ (poor), ⭐⭐ (OK) or ⭐⭐⭐ (great).', 'Fill every box, then check the budget limit.'],
        'why': {'icon': '📊', 'q': 'What is this matrix?', 't': 'The same kind of chart as the one above, now for the last pit in Palmetto Springs.'},
        'designs': [{'id': 'lake', 'icon': '🦢', 't': 'Bird lake'}, {'id': 'res', 'icon': '💧', 't': 'Reservoir'}, {'id': 'solar', 'icon': '☀️', 't': 'Floating solar'}],
        'rows': [{'id': 'wild', 'icon': '🪶', 't': 'Helps wildlife'}, {'id': 'water', 'icon': '💧', 't': 'Stores water'}, {'id': 'useful', 'icon': '🏙️', 't': 'Useful to the town'}],
        'cells': {
            'lake': {'wild': {'stars': 3, 'fact': 'Shallow, planted edges give wading birds like herons and wood storks a place to feed and nest.'},
                     'water': {'stars': 1, 'fact': 'A park lake is kept at about the same level, so it can’t save much extra water for dry months.'},
                     'useful': {'stars': 2, 'fact': 'People could walk, fish and watch birds, but it makes no power and stores little water.'}},
            'res': {'wild': {'stars': 1, 'fact': 'The water goes way up and down, and the sides are steep and deep, so few plants grow and few birds can feed.'},
                    'water': {'stars': 3, 'fact': 'A deep rock pit can hold a huge amount of water. Florida’s L-8 Reservoir, an old rock mine, holds up to 15 billion gallons.'},
                    'useful': {'stars': 2, 'fact': 'In dry months, stored water can be sent to the wetland. But there’s no park and no power.'}},
            'solar': {'wild': {'stars': 1, 'fact': 'Panels would cover much of the water, leaving little open water or shoreline for birds.'},
                      'water': {'stars': 1, 'fact': 'The panels don’t make the pit store any extra water.'},
                      'useful': {'stars': 3, 'fact': 'The panels would make clean electricity for many homes in town.'}}},
        'limit': {'icon': '💵', 't': 'Budget: $4 million or less', 'check': 'Check the budget limit',
                  'values': {'lake': {'t': '$2 million', 'ok': True}, 'res': {'t': '$3.5 million', 'ok': True}, 'solar': {'t': '$6 million', 'ok': False}}},
        'q': 'The bird lake and the reservoir tied. What should the engineers do next?',
        'opts': [{'t': 'Pick the solar farm. It got 3 stars for being useful.', 'miss': 'Look at the budget row. Can the town afford it?'},
                 {'t': 'Flip a coin.', 'miss': 'Engineers don’t guess. What could make one of them even better?'},
                 {'t': 'Make one of them better by borrowing a feature from another design.', 'ok': True}],
        'credit': FACTS,
        'win': 'The solar farm broke the limit, and two designs tied. That’s a clue.',
        'clue': 'matrix'},
    'improve': {
        'after': 'matrix', 'kicker': 'Part 2 game', 'title': 'Make it better',
        'todo': ['Pick one of the tied designs.', 'Add features from the other designs. Watch the stars and the cost.', 'Get every goal to at least ⭐⭐ and stay inside the budget.'],
        'budget': 4, 'unit': '$# million', 'need': 2,
        'rows': [{'id': 'wild', 'icon': '🪶', 't': 'Helps wildlife'}, {'id': 'water', 'icon': '💧', 't': 'Stores water'}, {'id': 'useful', 'icon': '🏙️', 't': 'Useful to the town'}],
        'bases': [{'id': 'lake', 'icon': '🦢', 't': 'Bird lake', 'scores': {'wild': 3, 'water': 1, 'useful': 2}, 'cost': 2},
                  {'id': 'res', 'icon': '💧', 't': 'Reservoir', 'scores': {'wild': 1, 'water': 3, 'useful': 2}, 'cost': 3.5}],
        'adds': [
            {'id': 'edges', 'icon': '🌿', 't': 'Shallow planted edges for birds', 'from': 'lake', 'cost': 0.5, 'boosts': {'wild': 1}, 'why': 'A planted shelf gives birds a shallow place to feed, even beside deep water.'},
            {'id': 'deep', 'icon': '🕳️', 't': 'A deep middle to store extra water', 'from': 'res', 'cost': 1, 'boosts': {'water': 1}, 'why': 'Digging the middle deeper lets the lake hold extra water for dry months.'},
            {'id': 'panels', 'icon': '☀️', 't': 'Some floating solar panels', 'from': 'solar', 'cost': 2.5, 'boosts': {'useful': 1}, 'why': 'Panels on part of the water make electricity, but they cost a lot.'},
            {'id': 'trail', 'icon': '🥾', 't': 'A walking trail and fishing dock', 'from': 'lake', 'cost': 0.5, 'boosts': {'useful': 1}, 'why': 'A trail and dock let people enjoy the water.'}],
        'q': 'Why is your improved design better than either first idea?',
        'opts': [{'t': 'It costs the most, so it must be the best.', 'miss': 'Look at the cost bar. Is spending more money a goal?'},
                 {'t': 'It meets every goal at least OK and still fits the budget.', 'ok': True},
                 {'t': 'It was the first design on the table.', 'miss': 'Did you keep the first design exactly as it was?'}],
        'win': 'You borrowed a feature and beat both first ideas, inside the budget. That’s a clue.',
        'clue': 'improve'},
    'photos': [{
        'id': 'l8', 'after': 'improve', 'kicker': 'Look closer · a real rock-pit reservoir', 'short': 'reservoir photo',
        'title': 'An old rock mine that stores water',
        'todo': ['Tap each number on the photo to read what it is.', 'Then match the clues to the labels below.'],
        'why': {'icon': '🛰', 'q': 'Where is this?', 't': 'The L-8 Reservoir in Palm Beach County, seen from above. It was a rock mine. Now it stores water for the Everglades.'},
        'img': I('l8-reservoir'), 'alt': 'An aerial photo: a huge dark reservoir split by thin strips of land, a canal running along its right side, and pale bare ground on the left where rock is being dug.',
        'credit': 'L-8 Reservoir area, Palm Beach County: U.S. Geological Survey, The National Map orthoimagery', 'license': 'Public domain',
        'hotspots': [
            {'n': 1, 'x': 45, 'y': 25, 'label': 'The dark water', 't': 'Old rock pits, now full of water. The reservoir is about 53 feet deep and can hold up to 15 billion gallons.'},
            {'n': 2, 'x': 52, 'y': 39, 'label': 'The thin strips of land', 't': 'Walls of earth split the reservoir into parts, so engineers can move water from one part to another.'},
            {'n': 3, 'x': 71, 'y': 60, 'label': 'The long dark line', 't': 'A canal. It carries water into the reservoir during storms and out again in dry months.'},
            {'n': 4, 'x': 20, 'y': 45, 'label': 'The pale ground', 't': 'Bare rock and sand where digging is still going on. The reservoir looked like this before it filled with water.'}],
        'task': {'q': 'Match each clue to a label on the photo.', 'win': 'You read a real reservoir like an engineer. One old rock pit got a whole new job.',
                 'items': [{'icon': '💧', 'step': 'Where the water is stored', 'ans': 1, 'evid': 'The deep old pits store the water.'},
                           {'icon': '🧱', 'step': 'Walls that split it into parts', 'ans': 2, 'evid': 'Strips of earth split the reservoir into parts.'},
                           {'icon': '↔️', 'step': 'Moves water in and out', 'ans': 3, 'evid': 'A canal moves water in and out.'},
                           {'icon': '⛏️', 'step': 'What a pit looks like while digging', 'ans': 4, 'evid': 'The pale ground is where digging is still going on.'}]}}],
    'pilot': {
        'afterText': 'June built a model of the improved pit', 'kicker': 'Part 4 game', 'title': 'Test it small',
        'todo': ['Run the first test on the model and watch the water.', 'If something goes wrong, pick the revision that fixes it.', 'Run the test again. Then do the next test.'],
        'why': {'icon': '🧪', 'q': 'Why a model?', 't': 'Engineers test small models before they build big projects like dams and harbors. A problem is much cheaper to fix on a model.'},
        'start': 62,
        'tests': [
            {'id': 'rain', 'icon': '🌧️', 'name': 'A week of heavy rain', 'kind': 'rain', 'level': 42, 'fixLevel': 56, 'fixKey': 'fix1',
             'problem': 'The water rose way over the planted shelf. The plants are drowning, and wading birds can’t stand in water that deep.',
             'fixes': [{'t': 'Plant taller grass on the shelf', 'miss': 'Tall grass still drowns if the water stays deep for weeks. What could stop the water from rising so high?'},
                       {'t': 'Add a spillway pipe so extra water flows out to the canal', 'ok': True, 'why': 'A spillway lets extra water flow out, so the water can only rise so high.'},
                       {'t': 'Take the planted shelf out', 'miss': 'Then the birds lose their shallow spot. That undoes your improvement!'}],
             'pass': 'The extra water flowed out the spillway, and the shelf stayed shallow.'},
            {'id': 'dry', 'icon': '☀️', 'name': 'A long dry spell', 'kind': 'dry', 'level': 84, 'fixLevel': 84, 'fixKey': 'fix2',
             'problem': 'The water dropped below the flat shelf. The plants dried out, and the birds left.',
             'fixes': [{'t': 'Fill it with a hose every day', 'miss': 'That would use lots of drinking water. Is there a way to change the design instead?'},
                       {'t': 'Dig the whole pit deeper', 'miss': 'A deeper middle doesn’t keep the flat shelf wet. What shape would keep part of it wet?'},
                       {'t': 'Make the shelf a gentle slope, so part of it stays wet at any water level', 'ok': True, 'why': 'On a slope, some of the edge is always right at the water, whether it’s high or low.'}],
             'pass': 'Even with low water, the bottom of the slope stayed wet, and the plants kept growing.'}],
        'q': 'Why test a small model before building the real thing?',
        'opts': [{'t': 'Problems show up early, when they’re cheap and easy to fix.', 'ok': True},
                 {'t': 'Models are more fun than real pits.', 'miss': 'Maybe! But what did testing the model help you find?'},
                 {'t': 'So you never have to revise.', 'miss': 'You revised twice! What did the tests help you find?'}],
        'win': 'Testing found two problems no one saw on paper, and each revision fixed one. That’s your last clue.',
        'clue': 'pilot'},
    'exploreMod': 'pilot',
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'Think about Limit or goal? Were the two boxes the same?', 'C': 'Cost can be a limit. Which one is a goal and which is a limit?'},
        'q2': {'A': 'Defining the problem comes first. What is changing a design to make it better?', 'B': 'A constraint is a limit. What is changing a design to make it better?'},
        'q3': {'B': 'Spending more isn’t a goal. Think about the matrix: what did comparing show?', 'C': 'Comparing takes time. Think about the matrix: what did comparing show?'}},
    'flags': {
        'ans-1': [
            {'label': 'a challenge', 're': 'water|electric|power|energy|beach|erosion|sand|plastic|trash|waste'},
            {'label': 'a criterion (goal)', 're': 'criteri|goal|enough|clean|protect|help|safe|less pollution|wildlife|last'},
            {'label': 'a constraint (limit)', 're': 'constraint|limit|budget|cost|money|cheap|must|can.?t|cannot|time|years|law|rule'}],
        'ans-3': [
            {'label': 'why revision matters', 're': 'better|improve|fix|stronger|problem|gap|work'},
            {'label': 'an example', 're': 'water|well|rule|recycl|solar|dune|sand|grass|plastic|ban|campaign|combin|pit|lake|reservoir|edge|spillway|slope'},
            {'label': 'how it changes', 're': 'combin|add|change|mix|both|instead|because|so '}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|not true|wrong|right|true|false|always|not always'},
            {'label': 'two pieces of evidence', 'any': ['first', 'tie', 'tied', 'budget', 'limit', 'solar', 'compare', 'matrix', 'score', 'star', 'better', 'borrow', 'feature', 'test', 'model', 'revis', 'problem', 'spillway', 'slope'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-1': 15, 'ans-3': 20, 'cer-4': 30},
    'hints': {
        'ans-1': ['Pick the challenge you understand best from Part 3.', 'A criterion is a goal. A constraint is a limit, pass or fail.', 'Try: For ___, one criterion is ___. One constraint is ___.'],
        'ans-3': ['Think about Make it better and Test it small. What changed?', 'Pick one solution from Part 3 and combine it with another idea.', 'Try: Revision is important because ___. For example, ___ could be better if ___.'],
        'cer-4': ['First decide: is the first idea always the best?', 'Think about the tie, the budget, and the model tests.', 'Try: I ___ because ___. One piece of evidence is ___. Another is ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'The first two designs tied, and neither met every goal.',
                'The solar farm looked great on one goal but broke the budget limit.',
                'Borrowing a feature from another design beat both first ideas.',
                'Testing a model found two problems no one saw on paper.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · the last pit', 'length': '30–40 s',
                    'script': 'June here! Let’s jump twenty years into the future. The Palmetto Springs quarry is digging its very last pit, and the town has to decide what it becomes. A bird lake? A water reservoir? A floating solar farm? Today you’re my engineer. We’ll compare all three, pick one, and make it even better.'},
        'warmup': {'label': 'Warm-Up · limit or goal? (Clue 1)', 'length': '20–30 s',
                   'script': 'Engineers sort a plan into two kinds of rules. A limit is pass or fail, like a budget. A goal gets scored, like helping wildlife. Read each card from the town’s plan and drop it in the right box. Then tell me what you think about the city water ideas.'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s', 'notes': 'Act out “revise” by erasing and redrawing a quick sketch; hold up a ruler for “constraint”.'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · criteria and constraints', 'length': '20–30 s'},
        'part2': {'label': 'Part 2 · build the matrix (Clues 2 and 3)', 'length': '25–35 s',
                  'script': 'Time to build a decision matrix for our last pit. Tap each question box, read the evidence, and give it one, two or three stars. Then check the budget. Something surprising happens! After that, pick a design and make it better.'},
        'part3': {'label': 'Part 3 · four Florida challenges', 'length': '20–30 s',
                  'script': 'Engineers in Florida face lots of challenges like ours. Tap each one to see the possible solutions, and the revision an engineer might make. Notice how many of the best ideas combine two solutions.'},
        'explore': {'label': 'Part 4 · test it small (Clue 4)', 'length': '25–35 s',
                    'script': 'Before we build the real thing, let’s test a model. Run the first test and watch the water. If something goes wrong, pick the revision that fixes it, then test again. Real engineers do this over and over.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s',
                       'script': 'Do you have all four clues? Crack the case at the top of this tab: what should the last pit become, and how can the town make it better? Then answer two questions, build your own decision matrix in Part C, and write your CER. Your answers save as you type.'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · build a decision matrix', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '25–35 s',
                     'script': 'A classmate says that if we just pick the smartest scientist’s first idea, we’ll always get the best solution. Hmm. Think about the tie, the budget and the model tests. Pick your side, tap two pieces of evidence, then explain how they prove your claim.'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate the end of Quarter 2; tease 17.01 (natural hazards: what a storm changes).',
                    'script': 'Case closed, engineer! You compared, improved and tested, and the last pit got a great new job. That wraps up the quarter, too. Next week, a brand-new kind of problem: what happens to Florida’s land when a big storm hits?'},
    },
    'videoOff': [],
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'Your LIMIT and GOAL boxes (Warm-Up)',
        'The matrix after the budget check (The Lesson)',
        'Your improved design inside the budget (The Lesson)',
        'The answer that cracked the case (Assignment)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['My decision matrix', 'My improved design for the last pit', 'The model test that went wrong'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · sketch it (optional)', 'required': False, 'minLabels': 3,
                           'prompts': ['Draw your matrix as a table', 'Add stars in each box', 'Circle the winner and label your revision']}]},
    'hlCoach': copy.deepcopy(Q['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '📐', 'name': 'Blueprint of the last pit',
                 'line': 'You cracked Case 16, part 2, and the blueprint of the last pit goes in your Field Notebook. (A specimen is something a scientist collects to study.) Next week: what a big storm changes.'},
    'notebookTitle': Q['notebookTitle'],
    'notebook': [dict(x) for x in Q['notebook']],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are in focus. You’ll use every one of them today.',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '.fs-game[data-mod="limits"]'},
         'label': 'Warm-Up: the city water ideas', 'q': 'Warm-Up: The city water idea I like best, what I’d need to know, and what could go wrong',
         'title': 'Your turn: the three city water ideas',
         'fields': [{'t': 'The idea I like best', 'icon': '💧', 'ph': 'I like Idea ___ best because…'},
                    {'t': 'One thing I’d need to know before choosing', 'icon': '❓', 'ph': 'I’d need to know…', 'long': True},
                    {'t': 'One thing that could go wrong', 'icon': '⚠️', 'ph': 'Something that could go wrong is…', 'long': True}]},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to hear it and see what it means.']},
        {'id': 'hide-nw', 'type': 'hide', 'find': {'sel': '.act-warmup .socratic-q', 'text': 'Notice'}},
        {'id': 'hide-tip', 'type': 'hide', 'find': {'sel': '.act-warmup .callout', 'text': 'favorites'}},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'Compare two solutions like an engineer'},
         'label': 'Part C: Build a decision matrix', 'q': 'Part C: A decision matrix: the problem, goals and a limit, two solutions scored, the winner and a revision',
         'title': 'My decision matrix',
         'fields': [{'t': 'The problem', 'icon': '🧩', 'ph': 'The problem is…'},
                    {'t': 'Two goals (criteria) and one limit (constraint)', 'icon': '🎯', 'ph': 'Goal 1: … Goal 2: … Limit: …', 'long': True},
                    {'t': 'Two solutions and their stars', 'icon': '⭐', 'ph': 'Solution A: ⭐⭐ for goal 1, ⭐ for goal 2. Solution B: …', 'long': True},
                    {'t': 'The winner, and how I would make it better', 'icon': '🔧', 'ph': 'I choose ___ because ___. I would make it better by…', 'long': True}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Is the smartest scientist’s first idea always the best solution?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-1': 'Part B · Question 5', 'ans-3': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
for n in D['notebook']:
    if n['lesson'] == '16.01': n.update({'have': True, 'icon': '🗳️', 'name': 'Town hall comment card'})
    if n['lesson'] == '16.02': n.update({'icon': '📐', 'name': 'Blueprint of the last pit'})
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'The solar farm was useful, but it broke the budget limit.',
    'key': ['solar', 'useful', 'broke', 'budget', 'limit'],
    'small': ['The', 'was', 'but', 'it', 'the'],
    'model': 'A scientist might highlight “solar farm”, “broke” and “budget limit”. Those words tell what happened and why. Small words like “the” and “but” don’t carry the idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: does this help me explain how engineers compare solutions and make the best one better?']
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
