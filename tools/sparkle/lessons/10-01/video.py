#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 10.01."""
import json
pics = {
    'oak': {'src': 'images/10-01-before-oak.jpg', 'cap': 'BEFORE · the big live oak · June'},
    'owl': {'src': 'images/10-01-before-owl.jpg', 'cap': 'BEFORE · barred owl up in the limbs · June'},
    'fallen': {'src': 'images/10-01-after-oak.jpg', 'cap': 'AFTER · the oak knocked over · August'},
    'fungus': {'src': 'images/10-01-after-fungus.jpg', 'cap': 'AFTER · mushrooms on the trunk · October'},
    'sketch': {'src': 'images/10-01-vr-sketch.jpg', 'cap': 'Dr. Reyes’s notebook sketch · June'},
    'liveoak': {'src': 'images/10-01-live-oak.jpg', 'cap': 'Southern live oak with resurrection ferns (CC0)'},
}
C_CASE, C_GREEN, C_PURP, C_RED = '#B9822A', '#2F7A55', '#7A5BB5', '#C8553D'
S = {}
S['welcome'] = {'label': 'Welcome · open the case', 'length': '50–60 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'oak', 'label': '📷 Before the oak'},
    {'kind': 'photo', 'pic': 'owl', 'label': '📷 Before the owl'},
    {'kind': 'photo', 'pic': 'fallen', 'label': '📷 After the fallen oak'},
    {'kind': 'photo', 'pic': 'fungus', 'label': '📷 After the mushrooms'},
    {'label': '🗂 The case question', 'tag': 'CASE FILE 10', 'title': 'The Day the Big Oak Fell', 'col': C_CASE, 'body': 'Why did so much change when only one tree fell?'},
    {'label': '🧭 Your clue bar', 'tag': 'HOW TO SOLVE IT', 'title': 'Find 4 clues', 'col': C_GREEN, 'rows': [['🗂 My clues', 'The bar under the tabs. Tap it to see your clues.'], ['? ? ? ?', 'Each game you finish fills in a clue.'], ['🔒', 'Crack the case at the top of the Assignment.']]}],
    'script': 'Hi, scientists! Welcome back to the Field Station. Today’s case starts with a tree.\n\n[ON SCREEN: Before the oak · Before the owl]\nThis giant live oak stood in a Florida hammock, a shady patch of forest. A barred owl lived up in its limbs.\n\n[ON SCREEN: After the fallen oak · After the mushrooms]\nThen a storm knocked it over. Look what showed up on the trunk. Hmm. Only ONE tree fell, but the owl left, the squirrels left, and mushrooms moved in.\n\n[ON SCREEN: The case question]\nThat’s our case: why did so much change?\n\n[ON SCREEN: Your clue bar]\nEvery game you finish adds a clue to “My clues.” Press Listen on Dr. Reyes’s walkie-talkie, right below me.'}
S['warmup'] = {'label': 'Warm-Up · tie the threads (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🧵 The five threads', 'tag': 'WARM-UP GAME', 'title': 'Five kinds of threads', 'col': C_GREEN, 'rows': [['🍽️', 'Food'], ['🌼', 'Pollination'], ['🏠', 'Shelter'], ['♻️', 'Nutrients'], ['🤲', 'Human care']]},
    {'label': '👆 How to tie', 'tag': 'HOW TO PLAY', 'title': 'Drag or tap', 'col': C_GREEN, 'rows': [['1', 'Tap a visitor to read what it does.'], ['2', 'Drag a thread onto it, or tap the thread, then the visitor.'], ['3', 'Tie all five, then list what you found.']]}],
    'script': 'Let’s meet the oak’s neighbors.\n\n(Hold up a piece of string.) Scientists draw a line, or a thread, for every connection between living things.\n\n[ON SCREEN: The five threads]\nHere are five kinds of threads. Only one is about eating!\n\n[ON SCREEN: How to tie]\nTap a visitor to read what it does with the oak. Then drag the thread that fits, or tap the thread and then the visitor. One visitor isn’t even alive. Can you spot it?\n\nWhen all five are tied, list what you found in the boxes. Press Listen. Dr. Reyes has a tip for you.'}
S['part3'] = {'label': 'Part 3 · pull a thread (Clue 3)', 'length': '45–55 s', 'want': True, 'parts': [
    {'label': '🕸️ The web', 'tag': 'THE WEB AROUND THE OAK', 'title': 'Each line is one connection', 'col': C_GREEN, 'rows': [['🌳', 'Live oak in the middle'], ['🐿️ 🦉 🐝', 'Tied to the oak'], ['🌴 🐻', 'Two threads away']]},
    {'label': '🔮 Predict first', 'tag': 'HOW TO PLAY', 'title': 'Guess, then pull', 'col': C_PURP, 'rows': [['1', 'Pick a thread to pull.'], ['2', 'Tap the living things you think will change.'], ['3', 'Press Pull the thread and check your guess.']]}],
    'script': '(Hold a string web or a cat’s cradle, then tug one string.) Watch. I pull one string, and look how many others move!\n\n[ON SCREEN: The web]\nThis is the web around Dr. Reyes’s oak. Each colored line is one connection.\n\n[ON SCREEN: Predict first]\nPick a thread to pull. Before you pull, predict: tap every living thing you think will change. Then press Pull the thread and see how close you were. Try all three.\n\nPress Listen on the walkie-talkie. One of these pulls surprised Dr. Reyes!'}
S['explore'] = {'label': 'Part 4 · the saw palmetto (Clue 4)', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🌴 Saw palmetto', 'tag': 'PART 4', 'title': 'A short palm with fan-shaped fronds', 'col': C_GREEN, 'body': 'It grows all over Florida, often right under big oaks.'},
    {'label': '🗃 Five boxes', 'tag': 'THE SORT', 'title': 'One card in each box', 'col': C_GREEN, 'rows': [['🍽️', 'Food'], ['🌼', 'Pollination'], ['🏠', 'Shelter'], ['♻️', 'Nutrients'], ['🤲', 'Human care']]}],
    'script': '[ON SCREEN: Saw palmetto]\nHave you seen this plant? Saw palmetto grows all over Florida. Its stems have tiny teeth, like a saw. Ouch!\n\nIt’s short, but it has a web of its own.\n\n[ON SCREEN: Five boxes]\nRead about it, then drag each card into its kind of connection. One card goes in each box. That’s your last clue!\n\nPress Listen on Dr. Reyes’s walkie-talkie first.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '45–55 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'Why did so much change?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Four places to write', 'col': C_GREEN, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Your own ecosystem web'], ['CER', 'Claim, evidence, reasoning'], ['📋', 'Copy your Gathered Answers into Canvas']]},
    {'label': '🛟 Help buttons', 'tag': 'STUCK?', 'title': 'Help under every box', 'col': C_PURP, 'rows': [['Your answer needs', 'Chips light up as you write.'], ['Hint', 'Three hints, one at a time.'], ['📎 My evidence', 'Your highlights and photo evidence.']]}],
    'script': '[ON SCREEN: Crack the case]\nYou found all four clues! At the top of this tab, crack the case: why did so much change when only one tree fell?\n\n[ON SCREEN: Your case report]\nThen write your case report: two short answers, your own ecosystem web, and a CER.\n\n[ON SCREEN: Help buttons]\nWatch the chips light up as you write. Stuck? Press Hint. Your answers save as you type.\n\nPress Listen on the walkie-talkie.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The quote', 'tag': 'USE YOUR EVIDENCE', 'title': 'Some people say…', 'col': C_RED, 'body': '“As long as we have plants and animals, we don’t need to worry about the small stuff like bees, fungi, and bacteria.”'},
    {'label': '⚖ CER', 'tag': 'REMEMBER CER?', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['C', 'Claim: what you think is true.'], ['E', 'Evidence: facts from the lesson that prove it.'], ['R', 'Reasoning: how the facts prove your claim.']]},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Tap to plan', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'They drop into your C and E boxes. You write the R.']]}],
    'script': '[ON SCREEN: The quote]\nSome people say, “As long as we have plants and animals, the small stuff doesn’t matter.” Bees. Mushrooms. Bacteria. Hmm. Think about the threads you pulled.\n\n[ON SCREEN: CER]\nRemember CER: your claim, your evidence from today, and your reasoning.\n\n[ON SCREEN: The planner]\nTap your side, then two pieces of evidence. They drop right into your boxes. The reasoning is all you. Try starting with “This shows that…”\n\nPress Listen. Dr. Reyes wants to hear your side.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🌰 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'Live oak acorn', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '➡ Next time', 'tag': 'LESSON 10.02', 'title': 'Healthy or out of balance?', 'col': C_GREEN, 'body': 'Real Florida numbers.'}],
    'script': 'Case closed! One tree was the center of a whole web.\n\n[ON SCREEN: Your specimen]\nFinish your checklist and a live oak acorn goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Next time]\nNext time, we’ll look at real numbers from Florida. How can you tell if a place is healthy, or out of balance?\n\nPress Listen for Dr. Reyes’s last word.'}
# optional slots
S['part1'] = {'label': 'Part 1 · the real live oak (Clue 2)', 'length': '30–40 s', 'want': False, 'parts': [
    {'kind': 'photo', 'pic': 'liveoak', 'label': '📸 The live oak photo'}],
    'script': '[ON SCREEN: The live oak photo]\nThis is a real live oak, the same kind as Dr. Reyes’s tree. See those little ferns on the limbs? Open every number, then match each kind of connection to a number. That’s Clue 2! Press Listen on the walkie-talkie.'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
             'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
S['partc'] = {'label': 'Part C · your own ecosystem web', 'length': '25–35 s', 'want': False, 'parts': [
    {'label': '🗺️ Your place', 'tag': 'PART C', 'title': 'Pick a Florida place', 'col': C_GREEN, 'rows': [['🏖️', 'A beach'], ['🏡', 'A backyard'], ['🐸', 'A pond'], ['🌲', 'A pine forest']]}],
    'script': '[ON SCREEN: Your place]\nNow it’s your web. Pick a Florida place you know. Name five living things there, then three connections, each a different kind. Want to draw it? The sketch pad is a bonus.'}
# VR activity page (vr-10-01.html) uses the same prefix: g4sci-10-1-vr.mp4
S['vr'] = {'label': 'VR activity · Rebuild the web (separate page)', 'length': '45–55 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'sketch', 'label': '📷 The sketch'},
    {'label': '🧭 Two ways', 'tag': 'PICK AT THE TOP', 'title': 'Two ways to do it', 'col': '#2B7BB9', 'rows': [['🥽', 'VR Field Mission: build 4 connections around one big tree in Tranquil Forest.'], ['🗂', 'No headset? Place 5 photo cards around the oak on your computer.']]},
    {'label': '🥇 The badge', 'tag': 'VR ONLY', 'title': 'Golden Acorn badge', 'col': '#B9822A', 'body': 'Save your capture in VR to earn it.'}],
    'script': 'Hi, scientists! You cracked the case of the fallen oak. (Hold up an acorn, or make goggles with your hands.) Now let’s build it back.\n\n[ON SCREEN: The sketch]\nThis is Dr. Reyes’s last sketch of the oak, from June. See the blank tags? Each one was a neighbor that needed the tree.\n\n[ON SCREEN: Two ways]\nPick your way at the top. With a headset, go into the Tranquil Forest, pick the biggest tree, and add food, pollination, shelter and nutrient cycling around it. No headset? Place the photo cards around the oak.\n\n[ON SCREEN: The badge]\nFinish in VR and you earn the Golden Acorn badge!\n\nPress Listen on Dr. Reyes’s walkie-talkie, right below me.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'part2', 'partb']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
