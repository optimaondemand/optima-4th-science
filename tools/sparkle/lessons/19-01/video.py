#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 19.01 · The Downhill Derby."""
import json
pics = {
    'car': {'src': 'images/19-01-derby-car.jpg', 'cap': 'A soap box derby car (Bill Wrigley, public domain)'},
    'hill': {'src': 'images/19-01-derby-hill.jpg', 'cap': 'Derby Downs, the derby hill in Akron, Ohio (Troop330, CC BY-SA 3.0)'},
    'moon': {'src': 'images/18-02-moon.jpg', 'cap': 'The full Moon and its craters (NASA, public domain)'},
    'radar': {'src': 'images/19-01-radar-gun.jpg', 'cap': 'A radar gun in use (U.S. Navy, public domain)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE = '#1F7F86', '#2F7A55', '#7A5BB5', '#C8553D', '#2D7AA6'
S = {}
S['welcome'] = {'label': 'Welcome · the Downhill Derby', 'length': '45–55 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'car', 'label': '🏎️ A derby car'},
    {'label': '🏁 The race program', 'tag': 'CASE FILE 19', 'title': 'The Downhill Derby', 'col': C_CASE, 'rows': [['🐢', 'Low ramp'], ['🚲', 'Middle ramp'], ['🚀', 'High ramp (the top)']]},
    {'label': '🔎 The case question', 'tag': 'SAM’S JOB', 'title': 'Which ramp needs the most hay?', 'col': C_RED, 'body': 'Every car must stop safely in the hay bales at the finish line.'}],
    'script': '(Hold your hands up high, then swoop them down like a car racing downhill.) Whoosh!\n\n[ON SCREEN: A derby car]\nThis is a real derby car. It has no motor at all. So what makes it go?\n\n[ON SCREEN: The race program]\nPalmetto Beach is having a Downhill Derby, with three start ramps: Low, Middle and High.\n\n[ON SCREEN: The case question]\nSam has to plan the hay bales at the finish line. Press Listen on Sam’s walkie-talkie, right below me.'}
S['warmup'] = {'label': 'Warm-Up · the flour crater test (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🥣 Try it with me', 'tag': 'LIVE DEMO', 'title': 'A marble and a pan of flour', 'col': C_PURP, 'rows': [['🪶', 'Drop it gently'], ['💨', 'Throw it down fast'], ['🔍', 'Compare the craters']]},
    {'kind': 'photo', 'pic': 'moon', 'label': '🌕 Real craters'}],
    'script': '(Show a pan of flour and a marble.) Watch this. I’ll drop the marble gently. (Drop it.) Now I’ll throw it down fast. (Throw it.)\n\n[ON SCREEN: Try it with me]\nWhich crater is bigger? Same marble, same flour. What changed?\n\n[ON SCREEN: Real craters]\nThe Moon has craters, too. Space rocks hit it very fast. Now flick the marble on your screen. Press Listen.'}
S['part1'] = {'label': 'Part 1 · scrub the replay (Clue 2)', 'length': '30–40 s', 'want': False, 'parts': [
    {'label': '🎞️ The replay', 'tag': 'PART 1 GAME', 'title': 'Where is the energy?', 'col': C_BLUE, 'body': 'Step through 4 frames. Tap every place the energy is.'}],
    'script': '(Roll a pencil or a marble across your desk.) Does it have energy before it hits anything?\n\n[ON SCREEN: The replay]\nStep through the replay one frame at a time. At each frame, tap every place the energy is right now. Press Listen.'}
S['part2'] = {'label': 'Part 2 · pinball power (Clue 3)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🕹️ Pinball power', 'tag': 'PART 2 GAME', 'title': 'Pull, predict, let go', 'col': C_BLUE, 'rows': [['1', 'A little pull'], ['2', 'Halfway'], ['3', 'All the way']]},
    {'label': '🎳 Big and slow', 'tag': 'ROUND 2', 'title': 'Bowling ball vs. baseball', 'col': C_RED, 'body': 'A 16-pound bowling ball rolled gently, or a 5-ounce baseball thrown fast. Which one knocks the blocks over?'}],
    'script': '(Pull your arm back a little, then all the way, like a slingshot.) Which pull sends it farther?\n\n[ON SCREEN: Pinball power]\nPull the plunger, predict which light the ball will reach, then let go. Try all three pulls.\n\n[ON SCREEN: Big and slow]\nThen Round 2. Thumbs up for the bowling ball, thumbs down for the baseball. Press Listen.'}
S['explore'] = {'label': 'Part 4 · build Dune Hill (Clue 4)', 'length': '45–55 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'hill', 'label': '⛰️ A real derby hill'},
    {'label': '🏁 Build Dune Hill', 'tag': 'PART 4 GAME', 'title': 'Draw, play, measure', 'col': C_GREEN, 'rows': [['✏️', 'Draw a track from a flag'], ['▶', 'Press Play'], ['📏', 'Measure the hay bale push'], ['📊', 'Build your bar chart']]}],
    'script': '(Prop a book on a stack of books like a ramp.) The higher the ramp, the faster the ride.\n\n[ON SCREEN: A real derby hill]\nThis is a real derby hill. Now you get to draw your own.\n\n[ON SCREEN: Build Dune Hill]\nDraw a track from Low, Middle and High. Press Play, measure how far the hay bale slides, and build your bar chart. Press Listen.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'Which ramp needs the most hay?', 'col': C_CASE, 'body': 'Pick the plan that fits all four clues.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Three places to write', 'col': C_GREEN, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Your speed table'], ['CER', 'Claim, evidence, reasoning']]}],
    'script': '[ON SCREEN: Crack the case]\nYou have four clues. Crack the case at the top of this tab.\n\n[ON SCREEN: Your case report]\nThen write your case report: two short answers, your speed table for Part C, and your CER. Use the numbers from your bar chart! Press Listen.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“All moving objects have the same energy. Speed doesn’t really matter.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '[ON SCREEN: The claim]\nA classmate says speed doesn’t matter. Hmm. Think about your two craters. Think about the baseball and the bowling ball.\n\nThere’s no wrong side, as long as you prove it.\n\n[ON SCREEN: The planner]\nTap your side and two facts, then explain how they prove your claim. Try starting with “This shows that…” Press Listen.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🏁 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'Derby checkered flag', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'kind': 'photo', 'pic': 'radar', 'label': '📡 Bonus tool'},
    {'label': '➡ Next time', 'tag': 'LESSON 19.02', 'title': 'A fair test at Dune Hill', 'col': C_BLUE, 'body': 'One change at a time, and lots of tries.'}],
    'script': 'Case closed! The High ramp gets the most hay, because faster cars carry more energy.\n\n[ON SCREEN: Your specimen]\nFinish your checklist, and your checkered flag goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Bonus tool]\nWant more? Try the radar gun at the very end.\n\n[ON SCREEN: Next time]\nNext time, a fair test at Dune Hill. Press Listen for Sam’s last word.'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'part3', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
