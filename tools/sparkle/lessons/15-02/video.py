#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 15.02."""
import json
pics = {
    'spring': {'src': 'images/15-02-manatee-spring.jpg', 'cap': 'Manatee Springs, Florida (CC BY 2.5)'},
    's2023': {'src': 'images/15-01-sat-2023.jpg', 'cap': 'The square lakes from Case 15 (USGS, public domain)'},
    'dragline': {'src': 'images/15-01-dragline.jpg', 'cap': 'A dragline at a phosphate mine (USGS, public domain)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE = '#B9822A', '#2F7A55', '#7A5BB5', '#C8553D', '#2D7AA6'
S = {}
S['welcome'] = {'label': 'Welcome · dig here?', 'length': '50–60 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 's2023', 'label': '🛰 The square lakes'},
    {'label': '✉️ Marco’s letter', 'tag': 'CASE FILE 15 · PART 2', 'title': 'Dig Here?', 'col': C_CASE, 'rows': [['1', 'Near my cousin’s house in Miami'], ['2', 'The beach at Pensacola'], ['3', 'A pasture near Mulberry'], ['4', 'The woods near White Springs']]},
    {'label': '🗂 The case question', 'tag': 'CASE FILE 15', 'title': 'Which pins could have phosphate?', 'col': C_CASE, 'body': 'And why is phosphate found only in some places?'}],
    'script': 'Welcome back, scientists!\n\n[ON SCREEN: The square lakes]\nLast time we cracked the square lakes: they were phosphate mines.\n\n[ON SCREEN: Marco’s letter]\nNow our volunteer Marco wants to dig his own phosphate. He put four pins on a map: Miami, a Pensacola beach, a pasture near Mulberry, and the woods near White Springs. He thinks phosphate is everywhere in Florida.\n\n[ON SCREEN: The case question]\nIs he right? Let’s test his pins with a real map. Press Listen on Dr. Reyes’s walkie-talkie, right below me.'}
S['warmup'] = {'label': 'Warm-Up · guess first (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '⭐ Guess first', 'tag': 'WARM-UP GAME', 'title': 'Four stars, one blank map', 'col': C_GREEN, 'rows': [['🍊', 'Citrus groves'], ['🏖️', 'Beaches'], ['💎', 'Phosphate mines'], ['💧', 'Springs']]}],
    'script': '(Close your eyes and point at an imaginary map.) Where do you think Florida’s orange groves are? Guess!\n\n[ON SCREEN: Guess first]\nIn the game, pick a resource and tap the blank map where you think it’s found. Place all four stars, then press the button to see the real map. How many miles off were you?\n\nScientists guess first so they notice what surprises them. Then write about your closest and farthest guess. Press Listen.'}
S['part1'] = {'label': 'Part 1 · map layers (Clue 2)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🔑 The map key', 'tag': 'PART 1 GAME', 'title': 'Map layers', 'col': C_BLUE, 'rows': [['☑', 'Turn on one layer at a time.'], ['🔘', 'Clustered in one or two areas'], ['➖', 'A wide band'], ['🌊', 'Along the coast']]}],
    'script': '(Hold up a map or a phone map.) What’s the first thing you read on a map? The map key! It tells what every symbol means.\n\n[ON SCREEN: The map key]\nIn Map layers, turn on one layer at a time so the map doesn’t get too busy. For each one, pick the pattern: clustered, a wide band, or along the coast. Keep an eye on the phosphate layer. Does it look like it’s everywhere? Press Listen.'}
S['explore'] = {'label': 'Part 4 · test the pins (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '📍 Test the pins', 'tag': 'PART 4 GAME', 'title': 'Could Marco dig here?', 'col': C_RED, 'rows': [['1', 'Tap a pin. The map zooms in.'], ['2', 'Phosphate could be here, or not?'], ['3', 'Pick what the map shows.']]},
    {'kind': 'photo', 'pic': 'dragline', 'label': '🏗️ A real mine'}],
    'script': 'Here’s how scientists test an idea: they check it against data.\n\n[ON SCREEN: Test the pins]\nTap one of Marco’s pins and the map zooms in. Could he find phosphate there? Decide, then pick what the map shows. That’s your evidence.\n\n[ON SCREEN: A real mine]\nReal phosphate mines look like this. Will Marco need one of these machines? Test all four pins. There’s a surprise up north! Press Listen.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'Dig here?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Three places to write', 'col': C_GREEN, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Map one Florida resource'], ['CER', 'Claim, evidence, reasoning'], ['📋', 'Copy your Gathered Answers into Canvas']]}],
    'script': '[ON SCREEN: Crack the case]\nYou have four clues. Crack the case at the top of this tab: which of Marco’s pins could have phosphate?\n\n[ON SCREEN: Your case report]\nThen write your case report. Two short answers, one resource in Part C with an evidence statement, and a CER. Want to sketch your map? That’s a bonus. Stuck? Press Hint under any box. Your answers save as you type. Press Listen.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“Maps are just pictures. They don’t really count as scientific evidence.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '[ON SCREEN: The claim]\nA classmate says maps are just pictures and don’t count as scientific evidence. Do you agree?\n\n[ON SCREEN: The planner]\nThink about how you tested Marco’s pins. Did the map help you decide? Remember CER. Tap your side and two facts from today, then explain how your facts prove your claim. Try starting with “This shows that…” Press Listen.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🗺️ Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'Marco’s pinned map', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '➡ Next time', 'tag': 'LESSON 16.01', 'title': 'What we gain, what we lose', 'col': C_GREEN, 'body': 'When we use a resource, how do we balance the benefits and the costs?'}],
    'script': 'Case closed! Phosphate is found in only a few places, and the map proved it. Sorry, Marco!\n\n[ON SCREEN: Your specimen]\nFinish your checklist and Marco’s pinned map goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Next time]\nNext week, a hard question: when we use a resource, how do we weigh what we gain against what we lose? Press Listen for Dr. Reyes’s last word.'}
S['part3'] = {'label': 'Part 3 · why here? (Clue 3)', 'length': '30–40 s', 'want': False, 'parts': [{'kind': 'photo', 'pic': 'spring', 'label': '💧 A real spring'}],
    'script': 'Every pattern on a map has a reason: the rock underground, the weather, or the ocean. Drag a reason onto each little map. One is a trick!\n\n[ON SCREEN: A real spring]\nThen visit a real spring and find where the water comes up. Press Listen.'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'part2', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
