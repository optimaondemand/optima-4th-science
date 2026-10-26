#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 14.02."""
import json
pics = {
    'frozen': {'src': 'images/14-02-frozen-pond.jpg', 'cap': 'Postcard 1 · a frozen pond (CC BY 3.0)'},
    'den': {'src': 'images/14-02-bear-den.jpg', 'cap': 'Postcard 2 · a black bear’s winter den (USFWS, public domain)'},
    'ducks': {'src': 'images/14-02-ducks.jpg', 'cap': 'Ring-necked ducks in Florida in January (CC BY 2.0)'},
    'spring': {'src': 'images/14-02-manatee-spring.jpg', 'cap': 'Manatees in a warm spring (USFWS, CC BY 2.0)'},
    'bear': {'src': 'images/14-02-bear-snow.jpg', 'cap': 'A black bear in the snow (CC BY-SA 4.0)'},
    'robin': {'src': 'images/14-02-robin.jpg', 'cap': 'A robin eating holly berries (CC BY 2.0)'},
    'vrrobin': {'src': 'images/14-02-vr-robin.jpg', 'cap': 'An American robin on a snowy branch (USFWS, public domain)'},
    'grass': {'src': 'images/14-02-seagrass.jpg', 'cap': 'Seagrass, manatee food (CC BY 2.0)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE = '#B9822A', '#2F7A55', '#7A5BB5', '#C8553D', '#2D7AA6'
S = {}
S['welcome'] = {'label': 'Welcome · postcards from Maine', 'length': '50–60 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'ducks', 'label': '🦆 Dr. Reyes’s pond'}, {'kind': 'photo', 'pic': 'frozen', 'label': '📮 Postcard 1'}, {'kind': 'photo', 'pic': 'den', 'label': '📮 Postcard 2'},
    {'label': '🗂 The case question', 'tag': 'CASE FILE 14 · PART 2', 'title': 'Postcards from Maine', 'col': C_CASE, 'body': 'Why is Dr. Reyes’s pond busy in January when Bea’s pond in Maine is quiet? Does Florida have seasons?'}],
    'script': '(Hold up a postcard.) Welcome back, scientists! Remember Dr. Reyes’s pond? It’s January now.\n\n[ON SCREEN: Dr. Reyes’s pond]\nHer pond is busier than ever. Ducks! Robins! Even a manatee.\n\n[ON SCREEN: Postcard 1]\nBut her friend Bea in Maine sent this. Her pond is frozen solid.\n\n[ON SCREEN: Postcard 2]\nAnd the bears? Asleep under the snow.\n\n[ON SCREEN: The case question]\nBea thinks Florida doesn’t have seasons. Is she right? Find four clues. Press Listen on Dr. Reyes’s walkie-talkie, right below me.'}
S['warmup'] = {'label': 'Warm-Up · two winters (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'spring', 'label': '♨️ Manatees'}, {'kind': 'photo', 'pic': 'bear', 'label': '🐻 Bear'},
    {'label': '👆 How to play', 'tag': 'WARM-UP GAME', 'title': 'Two winters', 'col': C_GREEN, 'rows': [['1', 'Look at a photo card.'], ['2', 'Drag it to Florida or Maine, or tap it, then tap the place.'], ['3', 'Sort all eight.']]}],
    'script': '(Shiver and rub your arms.) Brrr! Close your eyes and picture January. What do you see outside?\n\n[ON SCREEN: Manatees]\nHere’s one January in Florida.\n\n[ON SCREEN: Bear]\nAnd here’s one in Maine. Same month! Hmm, how can that be?\n\n[ON SCREEN: How to play]\nSort each photo into Florida or Maine. Then list three ways the two Januarys are different. Press Listen for Dr. Reyes’s hint.'}
S['part1'] = {'label': 'Part 1 · turn the calendar (Clue 2)', 'length': '40–50 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'robin', 'label': '🐦 Robin'},
    {'label': '📅 The calendar', 'tag': 'PART 1 GAME', 'title': 'Turn the calendar', 'col': C_RED, 'rows': [['📄', 'Tap a page: January, April, July, October.'], ['➡', 'Read across: Florida, then Maine.'], ['✅ ✈️ 😴', 'Here, migrated, or hibernating?']]}],
    'script': '(Flip an imaginary calendar page.) Let’s travel through a whole year in one minute!\n\n[ON SCREEN: Robin]\nThis robin might eat berries in Florida in January, and pull up worms in Maine in July. Where is it in between?\n\n[ON SCREEN: The calendar]\nTap each calendar page. Read across each row to see what happens in Florida and in Maine. Who stays? Who leaves? Who sleeps? Press Listen.'}
S['part3'] = {'label': 'Part 3 · the manatee water test (Clue 3)', 'length': '40–50 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'grass', 'label': '🌿 The river'}, {'kind': 'photo', 'pic': 'spring', 'label': '♨️ The spring'},
    {'label': '🧪 The test', 'tag': 'PART 3 TEST', 'title': 'Change one thing', 'col': C_BLUE, 'rows': [['🌡', 'Set the river temperature.'], ['▶', 'Run the morning.'], ['📋', 'Read your test log.']]}],
    'script': '(Dip a finger in a cup of water and shiver.) Some animals feel cold water more than we do.\n\n[ON SCREEN: The river]\nManatees eat seagrass in Florida’s rivers.\n\n[ON SCREEN: The spring]\nBut this spring stays about 72 degrees all year. Hmm. Why would they crowd in here?\n\n[ON SCREEN: The test]\nScientists change only one thing at a time. Change the river temperature, run the morning, and watch. Try cold and warm. Press Listen.'}
S['explore'] = {'label': 'Part 4 · build the seasonal model (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'ducks', 'label': '🦆 Ducks'},
    {'label': '🧩 Three steps', 'tag': 'PART 4 GAME', 'title': 'Build the seasonal model', 'col': C_GREEN, 'rows': [['1', 'Fill both circles: a plant, an animal, the weather.'], ['2', 'Tap a plant, then the animal that eats it.'], ['3', 'Add the migration arrow.']]}],
    'script': '(Draw two circles in the air.) Scientists use models to show how things connect.\n\n[ON SCREEN: Ducks]\nThese ducks nest up north. So why are they in Florida in January? A model can show us.\n\n[ON SCREEN: Three steps]\nFill a Florida circle and a Maine circle. Add the food-energy arrows. Then point the migration arrow the right way. That’s your last clue. Press Listen.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'Postcards from Maine', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Four places to write', 'col': C_GREEN, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Your two-region model'], ['CER', 'Claim, evidence, reasoning'], ['📋', 'Copy your Gathered Answers into Canvas']]}],
    'script': '[ON SCREEN: Crack the case]\nYou have four clues. Crack the case at the top of this tab: why is Dr. Reyes’s pond so busy in January?\n\n[ON SCREEN: Your case report]\nThen write your case report: two short answers, your own two-region model in Part C, and a CER. Want to sketch your model? That’s a bonus. Stuck? Press Hint under any box. Press Listen.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“Florida doesn’t really have seasons. It’s just summer all year.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '[ON SCREEN: The claim]\nA classmate says Florida doesn’t really have seasons. It’s just summer all year. Sounds like Bea! Do you agree?\n\n[ON SCREEN: The planner]\nRemember CER. Tap your side and two facts from today. Think about the manatees and the ducks. Then explain how your facts prove your claim. Try starting with “This shows that…” Press Listen.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '📮 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'Postcard from Maine', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '➡ Next time', 'tag': 'LESSON 15.01', 'title': 'Resources', 'col': C_GREEN, 'body': 'The water, sunlight and wind people use, and which ones can run out.'}],
    'script': 'Case closed! Florida does have seasons, just milder ones. That’s why the ducks and robins come here for the winter.\n\n[ON SCREEN: Your specimen]\nFinish your checklist, and Bea’s postcard goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Next time]\nNext time: the resources we all use, like water, sunlight and wind. Press Listen for Dr. Reyes’s last word.'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
S['vr'] = {'label': 'VR activity · The season wheel (separate page)', 'length': '45–55 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'vrrobin', 'label': '📷 The banded robin'},
    {'label': '📋 The band report', 'tag': 'CASE 14 FOLLOW-UP', 'title': 'Where did the robin go?', 'col': C_CASE, 'body': 'Banded in Maine in July. Found in Tallahassee, Florida in January. Why?'},
    {'label': '🧭 Two ways', 'tag': 'PICK AT THE TOP', 'title': 'Two ways to do it', 'col': C_BLUE, 'rows': [['🥽', 'VR Field Mission: build a season wheel around a clock, with winter, spring, summer and fall.'], ['🗂', 'No headset? Follow four banded birds on a map. One never left home!']]},
    {'label': '🥇 The badge', 'tag': 'VR ONLY', 'title': 'Silver Snowflake badge', 'col': C_PURP, 'body': 'Save your capture in VR to earn it.'}],
    'script': '[ON SCREEN: The banded robin]\nHi, scientists! See this robin? Last summer, Dr. Reyes put a tiny band on its leg in Maine.\n\n[ON SCREEN: The band report]\nThis January, it turned up in Florida! Hmm. Why would a robin fly all that way?\n\n[ON SCREEN: Two ways]\nPick your way at the top. With a headset, build a season wheel around a clock and show who needs what in each season. No headset? Follow four banded birds on a map.\n\n[ON SCREEN: The badge]\nFinish in VR to earn the Silver Snowflake badge!\n\nPress Listen on Dr. Reyes’s walkie-talkie, right below me.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'part2', 'figure', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
