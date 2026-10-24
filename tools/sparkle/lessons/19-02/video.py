#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 19.02 · The Rematch."""
import json
pics = {
    'hill': {'src': 'images/19-01-derby-hill.jpg', 'cap': 'Derby Downs, the derby hill in Akron, Ohio (Troop330, CC BY-SA 3.0)'},
    'car': {'src': 'images/19-01-derby-car.jpg', 'cap': 'A soap box derby car (Bill Wrigley, public domain)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE = '#1F7F86', '#2F7A55', '#7A5BB5', '#C8553D', '#2D7AA6'
S = {}
S['welcome'] = {'label': 'Welcome · the rematch', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '📱 Coach Dee’s texts', 'tag': 'CASE FILE 19, PART 2', 'title': 'The Rematch', 'col': C_CASE, 'rows': [['🏎️', 'Light car from HIGH: 15 in'], ['🏎️', 'Heavy car from LOW: 16 in'], ['🌬️', '“Oh, and it got windy.”'], ['1️⃣', '“One try each. That’s proof!”']]},
    {'label': '🔎 The case question', 'tag': 'IS IT FAIR?', 'title': 'Does start height matter?', 'col': C_RED, 'body': 'How can Sam prove it to Coach Dee?'}],
    'script': '(Hold up your phone like you just got a text, and gasp.) Uh oh. Sam just got a text from Coach Dee.\n\n[ON SCREEN: Coach Dee’s texts]\nShe ran ONE test, and she says start height doesn’t matter. Read her texts. Do you trust her test?\n\n[ON SCREEN: The case question]\nToday we find out, the scientist way. Press Listen on Sam’s walkie-talkie, right below me.'}
S['warmup'] = {'label': 'Warm-Up · the stopwatch race (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '⏱️ Try it with me', 'tag': 'LIVE DEMO', 'title': 'Time it three times', 'col': C_PURP, 'rows': [['1', 'Start at the green flag'], ['2', 'Stop at the red flag'], ['3', 'Do it 3 times']]},
    {'kind': 'photo', 'pic': 'car', 'label': '🏎️ The derby car'}],
    'script': '(Hold up a stopwatch or a phone timer.) I’m going to time something three times. Watch my numbers.\n\n[ON SCREEN: Try it with me]\nWere my three times exactly the same? Almost never!\n\n[ON SCREEN: The derby car]\nNow it’s your turn. Time the derby car three times and compare. Press Listen.'}
S['part1'] = {'label': 'Part 1 · lock it down (Clue 2)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🔒 Lock it down', 'tag': 'PART 1 GAME', 'title': 'Change only ONE thing', 'col': C_BLUE, 'rows': [['🏎️', 'Car: lock it'], ['⚙️', 'Wheels: lock it'], ['🌬️', 'Wind: lock it'], ['⛰️', 'Start: the one thing we test']]}],
    'script': '(Hold up two different shoes.) If I race in two different shoes on two different days, which one made me faster? I can’t tell!\n\n[ON SCREEN: Lock it down]\nCoach Dee changed lots of things at once. Lock every row except the start height, then run the fair test. Press Listen.'}
S['part2'] = {'label': 'Part 2 · dot plot drop (Clue 3)', 'length': '30–40 s', 'want': False, 'parts': [
    {'label': '📊 Dot plot drop', 'tag': 'PART 2 GAME', 'title': 'Watch the dots pile up', 'col': C_GREEN, 'body': 'Run at least 5 trials. Then drag the gold marker to the middle of the pile.'}],
    'script': '[ON SCREEN: Dot plot drop]\nOne dot can fool you. Five dots make a pile. Run your trials, then find the middle of the pile. Press Listen.'}
S['explore'] = {'label': 'Part 4 · data detective (Clue 4)', 'length': '45–55 s', 'want': True, 'parts': [
    {'label': '🔎 Data detective', 'tag': 'PART 4 GAME', 'title': 'Find the odd number', 'col': C_RED, 'rows': [['Low', '8 · 7 · 8'], ['Middle', '16 · 15 · ???'], ['High', '25 · 24 · 26']]},
    {'label': '🧦 Keep it, toss it, or check it?', 'tag': 'YOU DECIDE', 'title': 'What would a scientist do?', 'col': C_PURP, 'body': 'Thumbs up: keep it. Thumbs down: throw it out. Magnifying glass: check and redo.'}],
    'script': '(Squint at a piece of paper like a detective.) Hmm. Something here doesn’t look right.\n\n[ON SCREEN: Data detective]\nCoach Dee ran nine trials. One number is way off. Can you find it?\n\n[ON SCREEN: Keep it, toss it, or check it?]\nShow me what you’d do with your hand. Then find out what really happened. Press Listen.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'How can Sam prove it?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Three places to write', 'col': C_GREEN, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Your 9-trial table'], ['CER', 'Claim, evidence, reasoning']]}],
    'script': '[ON SCREEN: Crack the case]\nYou have four clues. Crack the case at the top of this tab, and a bonus game opens!\n\n[ON SCREEN: Your case report]\nThen write your case report: two short answers, your nine-trial table and your CER. Press Listen.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“I rolled a marble down a ramp once and the block moved 8 inches. That’s my whole investigation.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '[ON SCREEN: The claim]\nOne roll, one number, done? Hmm. Think about your stopwatch times. Think about the sock.\n\nThere’s no wrong side, as long as you prove it.\n\n[ON SCREEN: The planner]\nTap your side and two facts, then explain how they prove your claim. Try starting with “This shows that…” Press Listen.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🧦 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'The fluke sock', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '🎯 Bullseye Derby', 'tag': 'BONUS GAME', 'title': 'Can you get 9 stars?', 'col': C_GREEN, 'body': 'Roll your car onto the bullseye in 3 levels.'},
    {'label': '➡ Next week', 'tag': 'LESSON 20.01', 'title': 'How does energy move?', 'col': C_BLUE, 'body': 'Heat, light, sound and electricity.'}],
    'script': 'Case closed! A fair test with lots of trials beat one lucky try.\n\n[ON SCREEN: Your specimen]\nFinish your checklist, and Coach Dee’s fluke sock goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Bullseye Derby]\nThen try Bullseye Derby. Tell me how many stars you got!\n\n[ON SCREEN: Next week]\nNext week, we follow the energy. Press Listen for Sam’s last word.'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
