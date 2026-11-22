#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 25.01 · The Lost Time Capsule (Case 25).
Week 25 on has no crew clips yet, so no script says "Press Listen": each one hands off to the page itself."""
import json
pics = {
    'ferris': {'src': 'images/25-01-ferris-wheel.jpg', 'cap': 'The Seattle Great Wheel in a long-exposure photo (Diego Delso, CC BY-SA 4.0)'},
    'compass': {'src': 'images/25-01-compass.jpg', 'cap': 'A real pocket compass (Evan-Amos, public domain)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE, C_GOLD = '#1F7F86', '#2F7A55', '#7A5BB5', '#C8553D', '#2D7AA6', '#B8860B'
S = {}
S['welcome'] = {'label': 'Welcome · the lost time capsule', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🗺 Teo’s map', 'tag': 'CASE 25', 'title': 'How to find it', 'col': C_RED, 'rows': [['1', 'Start at the rowboat.'], ['2', 'Walk 5 steps.'], ['3', 'Dig!']]},
    {'label': '🕳 Six holes', 'tag': 'THE PROBLEM', 'title': 'Nobody found it', 'col': C_GOLD, 'body': 'Six people followed the map. Six holes. No time capsule.'},
    {'label': '🔍 Today', 'tag': 'TODAY', 'title': 'Describe how things move', 'col': C_GREEN, 'body': 'Where it started, where it ended, and which way it went.'}],
    'script': '(Hold up a folded paper like a treasure map.) I have a treasure map. Want to see?\n\n[ON SCREEN: Teo’s map]\nTeo buried a time capsule on the beach. Start at the rowboat, walk five steps, dig. Easy, right?\n\n[ON SCREEN: Six holes]\nSix people tried it. Six holes. Nothing. Hmm.\n\n[ON SCREEN: Today]\nToday you’ll learn how to describe motion so clearly that nobody gets lost. Read Teo’s map, just below me, and see what you notice.'}
S['warmup'] = {'label': 'Warm-Up · which train moved? (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🚆 Which train moved?', 'tag': 'WARM-UP GAME', 'title': 'Watch, vote, check', 'col': C_BLUE, 'rows': [['▶', 'Watch out the left window'], ['🗳', 'Vote: who moved?'], ['👀', 'Look out the right window']]},
    {'label': '🪧 The station sign', 'tag': 'LOOK FOR THIS', 'title': 'Something that stays put', 'col': C_CASE, 'body': 'It never moves. So it can tell you who did.'}],
    'script': '(Sit very still. Slowly slide your hand past your face like a train going by.) Whoa. Am I moving, or is that train moving?\n\n[ON SCREEN: Which train moved?]\nPress Watch and look out the left window. Then vote. Did your train move, or the other one? It is okay to say you can’t tell yet.\n\n[ON SCREEN: The station sign]\nThen look out the right window and find the station sign. Take both trips. The second one might fool you!'}
S['part1'] = {'label': 'Part 1 · find it from the clue (Clue 2)', 'length': '35–45 s', 'want': False, 'parts': [
    {'label': '📍 Find it from the clue', 'tag': 'PART 1 GAME', 'title': 'Count from the reference point', 'col': C_GREEN, 'rows': [['📌', 'Find the reference point'], ['👣', 'Count the steps'], ['📍', 'Tap the square']]}],
    'script': '(Point to your desk, then count three hand-steps to the right.) My pencil is three hands to the right of my mug. Can you picture it?\n\n[ON SCREEN: Find it from the clue]\nRead each clue. Find the thing it starts from, count the steps and tap that square. North is up on this map. Watch out for the last clue. It was written yesterday.'}
S['part2'] = {'label': 'Part 2 · program the helper (Clue 3)', 'length': '45–55 s', 'want': True, 'parts': [
    {'label': '🤖 Meet Scoot', 'tag': 'PART 2 GAME', 'title': 'Scoot does exactly what you say', 'col': C_PURP, 'rows': [['⬆➡⬇⬅', 'Tap an arrow card'], ['− +', 'Set the steps'], ['▶', 'Press Go']]},
    {'label': '🧾 The order slip', 'tag': 'DELIVERY 1', 'title': '“Take the cocoa 4 steps.”', 'col': C_RED, 'body': 'Four steps… which way?'},
    {'kind': 'photo', 'pic': 'ferris', 'label': '🎡 The Ferris wheel'}],
    'script': '(Close your eyes. Take four small steps in a random direction, then open them and look surprised.) Four steps! Did I end up in the right place?\n\n[ON SCREEN: Meet Scoot]\nScoot is Sam’s delivery robot. Tap an arrow card, set the steps, and press Go.\n\n[ON SCREEN: The order slip]\nThe first slip only says four steps. What is missing? Fix it. After three deliveries, a surprise is waiting.\n\n[ON SCREEN: The Ferris wheel]\nIf you get off a Ferris wheel right where you got on, did you move? Vote, then ride.'}
S['explore'] = {'label': 'Part 3 · diagram the replay (Clue 4)', 'length': '45–55 s', 'want': True, 'parts': [
    {'label': '🗺 Diagram the replay', 'tag': 'PART 3 GAME', 'title': 'Four things on every diagram', 'col': C_GREEN, 'rows': [['🟢', 'Where it started'], ['🔴', 'Where it ended'], ['➡', 'An arrow for the direction'], ['📌', 'A reference point']]}],
    'script': '(Roll a pencil or a toy car across your desk. Stop it. Point to where it started, then where it ended.) It started here. It ended there. It went that way.\n\n[ON SCREEN: Diagram the replay]\nA motion diagram is a picture of that: a start, an end, an arrow and a reference point. Your turn. Watch a crab and a seagull. Plant the Start flag and the End flag, name the direction and the path, then tap something that stays put. Your description writes itself.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'What is wrong with Teo’s directions?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO DO', 'title': 'Three places to work', 'col': C_GOLD, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Draw and label your own motion diagram'], ['CER', 'Claim, evidence, reasoning']]}],
    'script': '[ON SCREEN: Crack the case]\nYou have four clues. So what is wrong with Teo’s directions, and what would fix them? Pick the answer that fits every clue. Then help Scoot dig up the capsule.\n\n[ON SCREEN: Your case report]\nAfter that: two short answers. Then watch something move at home, like a toy car or your pet, and draw its motion diagram. Label the start, the end, the direction and your reference point. Last comes your CER.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“You can describe motion without a reference point. Just say how far it moved.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '(Hold up five fingers.) It moved five steps. There. Do you know where it is now?\n\n[ON SCREEN: The claim]\nA classmate says how far is all you need. Think about the train window, and Scoot’s slip that only said four steps.\n\n[ON SCREEN: The planner]\nTap your side and two facts. Then explain how they prove your claim. Try starting with “This shows that…”'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🗺 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'Teo’s treasure map', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'kind': 'photo', 'pic': 'compass', 'label': '🧭 Bonus: the compass'},
    {'label': '➡ Next lesson', 'tag': 'LESSON 25.02', 'title': 'How fast did it move?', 'col': C_BLUE, 'body': 'Distance and time tell us speed.'}],
    'script': '(Hold up the folded map again.) Start at the lamp post. Five steps east. Three steps south. Dig! Now THAT is a map.\n\n[ON SCREEN: Your specimen]\nFinish your checklist, and Teo’s map goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Bonus: the compass]\nWant more? Try the compass at the very end, and the Night Delivery game.\n\n[ON SCREEN: Next lesson]\nNext time: we know which way it went. But how fast?'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
