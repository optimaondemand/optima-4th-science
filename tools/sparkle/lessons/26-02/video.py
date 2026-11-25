#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 26.02 · Around the Bend (Case 26 part 2, Dr. Priya Nair).
Week 25 on has no crew clips yet, so no script says "Press Listen": each one hands off to the page itself."""
import json
pics = {
    'lighthouse': {'src': 'images/26-02-cape-canaveral-light.jpg', 'cap': 'The real Cape Canaveral Lighthouse (NASA/Jim Grossmann, public domain)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE, C_GOLD = '#7A5BB5', '#2F7A55', '#5A3B92', '#C8553D', '#2D7AA6', '#B8860B'
S = {}
S['welcome'] = {'label': 'Welcome · Around the Bend', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🦆 The Duck Derby, part 2', 'tag': 'CASE 26', 'title': 'Now on Palmetto Creek', 'col': C_GOLD, 'body': 'The flowing creek will carry the ducks this time.'},
    {'label': '📻 The practice run', 'tag': 'WHAT WENT WRONG', 'title': '“WAIT!” was heard as “…ready!”', 'col': C_RED, 'body': 'The walkies cut out. The waterfall drowned out shouting.'},
    {'label': '❓ The question', 'tag': 'THE PROBLEM', 'title': 'What code should the judges use?', 'col': C_CASE, 'body': 'And how will they know it works?'}],
    'script': '(Cup your hands around your mouth like you’re yelling across a field.) Can you hear me over there? No? Hmm.\n\n[ON SCREEN: The Duck Derby, part 2]\nThe Duck Derby moved to Palmetto Creek, where the water flows. Great idea!\n\n[ON SCREEN: The practice run]\nBut at the practice run, the walkie-talkies cut out, and “Wait!” was heard as “ready!” The ducks floated right past an empty finish.\n\n[ON SCREEN: The question]\nToday you’ll help the judges design a code that can’t get mixed up. Dr. Nair’s case file is just below me.'}
S['warmup'] = {'label': 'Warm-Up · the secret knock (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🚪 The secret knock', 'tag': 'WARM-UP GAME', 'title': 'Knock it back', 'col': C_BLUE, 'rows': [['👂', 'Listen to the knock'], ['👊', 'Tap the door: same rhythm'], ['🗝️', 'Find the code key']]},
    {'label': '🤔 Think about it', 'tag': 'WONDER', 'title': 'What did it mean?', 'col': C_CASE, 'body': 'Can you tell without the key?'}],
    'script': '(Knock on your desk: knock-knock, pause, knock.) Did I just say something? What was it?\n\n[ON SCREEN: The secret knock]\nSomeone is knocking on the clubhouse door. Listen, then tap the door to knock the same rhythm back.\n\n[ON SCREEN: Think about it]\nYou copied it. But what does it mean? Look for the code key. Then write about a code you already know, like a doorbell or a school bell.'}
S['part1'] = {'label': 'Part 1 · the flashlight key + lighthouses (Clue 2)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🔦 The flashlight key', 'tag': 'PART 1 GAME', 'title': 'Tap or hold', 'col': C_GOLD, 'rows': [['•', 'Tap: a short flash (dot)'], ['—', 'Hold: a long flash (dash)'], ['🆘', 'Send SOS, then GO']]},
    {'kind': 'photo', 'pic': 'lighthouse', 'label': '🗼 A real lighthouse'}],
    'script': '(Turn a flashlight, or a phone light, on and off: short, short, short.) Short flashes. (Now hold it on longer.) A long flash.\n\n[ON SCREEN: The flashlight key]\nTap the red key quickly for a dot. Hold it for a dash. Send SOS, the call for help. If a flash is in between, your partner can’t tell what you meant!\n\n[ON SCREEN: A real lighthouse]\nThen meet three lighthouses that each flash their own pattern. Can you tell them apart?'}
S['part2'] = {'label': 'Part 2 · which signal crosses the bend? (Clue 3)', 'length': '35–45 s', 'want': False, 'parts': [
    {'label': '🚧 Goals and limits', 'tag': 'PART 2 GAME', 'title': 'Which signal crosses the bend?', 'col': C_PURP, 'rows': [['🎯', 'Criteria: the goals'], ['🚧', 'Constraints: the limits']]}],
    'script': '(Hold up two fingers, then fold one down.) Goals are what a design must do. Limits are what it has to work around.\n\n[ON SCREEN: Goals and limits]\nSwitch on each limit at the creek and watch the ways to send a message drop out. Then check the last one against every goal.'}
S['explore'] = {'label': 'Part 3 · test it across the creek (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '📝 Test it across the creek', 'tag': 'PART 3 GAME', 'title': 'Test, change one thing, test again', 'col': C_GREEN, 'rows': [['🔦', 'Test the judges’ first code'], ['❌', 'Find the mix-ups'], ['🔧', 'Change ONE thing'], ['✅', 'Aim for 4 out of 4']]}],
    'script': '(Hold up one finger.) One. Engineers change ONE thing at a time. Why do you think that is?\n\n[ON SCREEN: Test it across the creek]\nPress Test across the creek and read the test sheet. Which messages did the partner mix up? Those are your failure points. Change just one thing, a pattern tile or the gap, and test again. Keep going until your partner reads all four. There’s more than one way to fix it!'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'Which code should the judges use?', 'col': C_CASE, 'body': 'Pick the plan that fits all four clues.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO DO', 'title': 'Three places to work', 'col': C_GOLD, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Invent your own code, then sketch its key'], ['CER', 'Claim, evidence, reasoning']]}],
    'script': '[ON SCREEN: Crack the case]\nYou have four clues. Which code should the judges use on race night? Pick the plan that fits every clue. Then watch for a twist on race night.\n\n[ON SCREEN: Your case report]\nNext: two short answers. For Part C, invent a code for your own life, like a family signal or a game with a friend. Sketch its key and label it. Last comes your CER.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“Real engineers design things right the first time. Testing is just for amateurs.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '(Pretend to crumple a paper and toss it.) First try, perfect? Hmm.\n\n[ON SCREEN: The claim]\nA classmate says real engineers get it right the first time. Think about the judges’ first test, and race night in the mist.\n\n[ON SCREEN: The planner]\nTap your side and two facts. Then explain how they prove your claim. Try starting with “This shows that…”'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🔦 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'A judge’s signal flashlight', 'col': C_GOLD, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '➡ Next lesson', 'tag': 'LESSON 27.01', 'title': 'What is matter?', 'col': C_BLUE, 'body': 'The stuff everything is made of.'}],
    'script': '(Flash a light twice.) Two flashes: case closed!\n\n[ON SCREEN: Your specimen]\nFinish your checklist, and a judge’s signal flashlight goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Next lesson]\nNext time we start something new: matter, the stuff everything is made of. See you then!'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
