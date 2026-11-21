#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 23.02 · The Still Canal (Case 23, part 2)."""
import json
pics = {
    'windmill': {'src': 'images/23-02-windmill.jpg', 'cap': 'A farm windmill and its water tank (USDA Forest Service, public domain)'},
    'dam': {'src': 'images/23-02-dam.jpg', 'cap': 'Jim Woodruff Dam on the Apalachicola River (U.S. Army Corps of Engineers, public domain)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE, C_GOLD = '#1F7F86', '#2F7A55', '#7A5BB5', '#C8553D', '#2D7AA6', '#B8860B'
S = {}
S['welcome'] = {'label': 'Welcome · the still canal', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '📰 The front page', 'tag': 'CASE 23 · PART 2', 'title': 'Pelican Canal goes still and green', 'col': C_BLUE, 'rows': [['🟢', 'Water hardly moves'], ['🐟', 'Fish need air'], ['💡', 'Readers send Bright Ideas']]},
    {'label': '🌬️ Today', 'tag': 'TODAY', 'title': 'Can moving air and water do work?', 'col': C_GREEN, 'body': 'Wind energy, water energy, and what makes a wheel spin faster.'}],
    'script': '(Blow on your hand.) Feel that? That’s moving air. Can something you can’t even see do real work?\n\n[ON SCREEN: The front page]\nPelican Canal is back in the news. The water has gone still and green, and readers sent in ideas to get it moving.\n\n[ON SCREEN: Today]\nToday you help Sam judge which idea really works. Read the front page and the three entries just below me.'}
S['warmup'] = {'label': 'Warm-Up · the mystery tower (Clue 1)', 'length': '35–45 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'windmill', 'label': '🧩 The mystery tower'},
    {'label': '⭐ Fewer tiles, more stars', 'tag': 'WARM-UP GAME', 'title': 'Lift, look, guess', 'col': C_PURP, 'rows': [['🧩', 'Lift one tile'], ['🤔', 'Guess what it does'], ['⭐', 'Fewer tiles = more stars']]}],
    'script': '(Peek through your fingers.) When I only see a little, I have to think like a detective.\n\n[ON SCREEN: The mystery tower]\nThis tower stands in a field with no wires at all. What could it be for?\n\n[ON SCREEN: Fewer tiles, more stars]\nLift one tile at a time and guess. Press Listen on Sam’s walkie-talkie, right below me.'}
S['part1'] = {'label': 'Part 1 · the drop race (Clue 2)', 'length': '30–40 s', 'want': False, 'parts': [
    {'label': '🪶 The drop race', 'tag': 'PART 1 GAME', 'title': 'Predict, then let go', 'col': C_GOLD, 'rows': [['🏁', 'Drag the flag'], ['✋', 'Let go!'], ['🌀', 'Then the fan']]}],
    'script': '(Hold up a flat sheet of paper and a crumpled one.) Same paper. Which lands first?\n\n[ON SCREEN: The drop race]\nPredict, then let go. If air is really nothing, they should tie. Press Listen.'}
S['part2'] = {'label': 'Part 2 · turn the valve (Clue 3)', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🚰 Turn the valve', 'tag': 'PART 2 GAME', 'title': 'More water, faster wheel?', 'col': C_RED, 'rows': [['↻', 'Drag the handle around'], ['💡', 'Watch the lamp'], ['⚡', 'Try “Spin by itself”']]}],
    'script': '(Turn on a faucet a little, then all the way.) Trickle… whoosh!\n\n[ON SCREEN: Turn the valve]\nDrag the red valve handle and watch the waterwheel, the stone and the lamp. Then close it all the way and press “Spin by itself.” Can a wheel make its own energy? Find out.'}
S['explore'] = {'label': 'Part 3 · count the red blade (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🌀 Count the red blade', 'tag': 'PART 3 GAME', 'title': 'A fair test', 'col': C_BLUE, 'rows': [['1️⃣', 'Test 1 as it is'], ['🔀', 'Change ONE thing'], ['👆', 'Tap at the top']]}],
    'script': '(Hold up a pinwheel, or one finger spinning in a circle.) One, two, three…\n\n[ON SCREEN: Count the red blade]\nScientists count carefully. Run Test 1. Then change just ONE thing, the wind or the way it faces, and tap every time the red blade passes the top. If you have a pinwheel, try it for real, too! Press Listen.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'Which Bright Idea wins?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues.'},
    {'kind': 'photo', 'pic': 'dam', 'label': '💧 Florida’s zero'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Three places to write', 'col': C_RED, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Your wind and water model + sketch'], ['CER', 'Claim, evidence, reasoning']]}],
    'script': '[ON SCREEN: Crack the case]\nFour clues: pick the Bright Idea that really works.\n\n[ON SCREEN: Florida’s zero]\nThen guess how many wind farms Florida has. The answer might surprise you!\n\n[ON SCREEN: Your case report]\nLast, two short answers, your wind and water model with a labeled sketch, and your CER.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“Wind isn’t real energy. It’s just air moving. It doesn’t do anything.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '[ON SCREEN: The claim]\nDoesn’t do anything? Hmm. Think about that flat paper, and the fan.\n\nThere’s no wrong side, as long as you prove it.\n\n[ON SCREEN: The planner]\nTap your side and two facts, then explain how they prove your claim. Try starting with “This shows that…” Press Listen.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🎀 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'The Bright Idea ribbon', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '⛵ Bonus', 'tag': 'BONUS GAME', 'title': 'Sail the canal', 'col': C_GOLD, 'body': 'Turn the sail to catch the wind.'},
    {'label': '➡ Next time', 'tag': 'LESSON 24.01', 'title': 'Heat on the move', 'col': C_BLUE, 'body': 'Why does a metal spoon feel cold?'}],
    'script': '(Blow on your hand again.) Now you know: that little breeze is real energy.\n\n[ON SCREEN: Your specimen]\nFinish your checklist, and the Bright Idea ribbon goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Bonus]\nWant more wind? Try sailing the canal.\n\n[ON SCREEN: Next time]\nNext time: heat! Why does a metal spoon feel colder than a wooden one?'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
