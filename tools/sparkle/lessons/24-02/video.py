#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 24.02 · Teo's Napkin Plan (Case 24, part 2)."""
import json
pics = {
    'bikegen': {'src': 'images/24-02-bike-generator.jpg', 'cap': 'A real bike-powered music stage in Geneva (MHM55, CC BY-SA 4.0)'},
    'glow': {'src': 'images/24-02-glow-sticks.jpg', 'cap': 'Real glow sticks (David Muelheims, public domain)'},
    'jelly': {'src': 'images/24-02-comb-jelly.jpg', 'cap': 'A real comb jelly (Steven G. Johnson, CC BY-SA 3.0)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE, C_GOLD = '#1F7F86', '#2F7A55', '#7A5BB5', '#C8553D', '#2D7AA6', '#B8860B'
S = {}
S['welcome'] = {'label': 'Welcome · Teo’s napkin plan', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🧻 The napkin', 'tag': 'CASE 24, PART 2', 'title': 'Teo’s plan', 'col': C_RED, 'rows': [['🚴', 'Pedal a bike'], ['⚙️', 'Spin a generator'], ['💡', 'Run the whole cart']]},
    {'kind': 'photo', 'pic': 'bikegen', 'label': '📷 A real bike generator'},
    {'label': '🔍 Today', 'tag': 'TODAY', 'title': 'Prove an energy change', 'col': C_GREEN, 'body': 'Where does the energy start, what does it become, and how do we know?'}],
    'script': '(Hold up a paper napkin with a quick pen sketch on it.) Big ideas sometimes start on a napkin.\n\n[ON SCREEN: The napkin]\nRosa’s cousin Teo says a bike can run her whole cocoa cart. FREE energy, he says. No plug!\n\n[ON SCREEN: A real bike generator]\nBike generators are real. This one powers a music stage.\n\n[ON SCREEN: Today]\nBut free energy? Rosa wants proof, and so do I. Read Teo’s napkin just below me.'}
S['warmup'] = {'label': 'Warm-Up · crack a glow stick (Clue 1)', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🪄 Crack a glow stick', 'tag': 'WARM-UP GAME', 'title': 'Where does the light come from?', 'col': C_PURP, 'rows': [['↷', 'Bend it till it cracks'], ['〰', 'Shake it'], ['👀', 'Tap what you observe']]},
    {'kind': 'photo', 'pic': 'glow', 'label': '✨ Real glow sticks'}],
    'script': '(Hold up a glow stick, or pretend to.) No plug. No battery. Watch. (Bend it, then shake it.)\n\n[ON SCREEN: Crack a glow stick]\nBend it until the glass inside cracks. Shake it, then tap only the things you really observe.\n\n[ON SCREEN: Real glow sticks]\nSo where did that light start? Press Listen on Sam’s walkie-talkie, right below me.'}
S['part1'] = {'label': 'Part 1 · the energy slot machine (Clue 2)', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🎰 Energy slots', 'tag': 'PART 1 GAME', 'title': 'Line up a true card', 'col': C_RED, 'rows': [['🎰', 'Pull the lever'], ['⏹', 'Stop START and RESULT'], ['✅', 'Check your line']]}],
    'script': '(Pretend to pull a lever.) Ka-chunk! A flashlight. Electrical in, light out. That’s a true line!\n\n[ON SCREEN: Energy slots]\nPull the lever to get a device. Stop the starting reel and the resulting reel on the right energy, then check. Win all five cards. Press Listen.'}
S['part2'] = {'label': 'Part 2 · evidence bingo (Clue 3)', 'length': '30–40 s', 'want': False, 'parts': [
    {'label': '🔲 Evidence bingo', 'tag': 'PART 2 GAME', 'title': 'See it, hear it, feel it, measure it', 'col': C_BLUE, 'rows': [['👀', 'Saw'], ['👂', 'Heard'], ['✋', 'Felt'], ['📏', 'Measured']]}],
    'script': '(Cup your hand to your ear.) Did you hear that? That’s evidence.\n\n[ON SCREEN: Evidence bingo]\nPress Play and watch Rosa’s cart. Tap a square the moment it happens. One square never counts. Can you find it?'}
S['explore'] = {'label': 'Part 3 · the card binder + pedal power (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🃏 The binder', 'tag': 'PART 3 GAME', 'title': 'Five cards, five changes', 'col': C_PURP, 'rows': [['🟢', 'Starting energy'], ['🔴', 'Resulting energy'], ['🔍', 'Best evidence']]},
    {'label': '🚴 Pedal Teo’s bike', 'tag': 'WOW', 'title': 'What can one rider run?', 'col': C_GOLD, 'body': 'Lights, sign, radio… and the cocoa warmer?'}],
    'script': '(Point to your own legs.) Here’s a device you use every day: you!\n\n[ON SCREEN: The binder]\nFill each card: where the energy starts, what it becomes, and the best evidence. Finished cards shine and go in your binder.\n\n[ON SCREEN: Pedal Teo’s bike]\nThen pedal Teo’s bike yourself. Tap left, right, left, right. Can one rider run the cocoa warmer?'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'Where does Teo’s energy start?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Three places to write', 'col': C_GOLD, 'rows': [['Part B', 'Two short answers'], ['Part C', '4 energy cards + a labeled sketch'], ['CER', 'Claim, evidence, reasoning']]}],
    'script': '[ON SCREEN: Crack the case]\nFour clues. Where does Teo’s “free” energy really start, and what proves it?\n\n[ON SCREEN: Your case report]\nThen two short answers, four energy change cards from your own home with a labeled sketch, and your CER.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“Energy just appears in a flashlight when you click the button.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '(Click a flashlight on and off, or pretend to.) Click. Light! Did that energy just appear?\n\n[ON SCREEN: The claim]\nThink about the glow stick, and what happened when you stopped pedaling.\n\n[ON SCREEN: The planner]\nTap your side and two facts, then explain how they prove your claim. Try starting with “This shows that…” Press Listen.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🧻 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'Teo’s napkin plan', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'kind': 'photo', 'pic': 'jelly', 'label': '🌊 Bonus: the glowing wake'},
    {'label': '➡ Next week', 'tag': 'LESSON 25.01', 'title': 'How objects move', 'col': C_BLUE, 'body': 'Where it starts, where it ends up, and which way it goes.'}],
    'script': '(Hold up the napkin again.) Free energy? Nope. It started as food!\n\n[ON SCREEN: Your specimen]\nFinish your checklist, and Teo’s napkin goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Bonus: the glowing wake]\nWant a surprise? Drag a boat across a dark Florida lagoon and watch the water.\n\n[ON SCREEN: Next week]\nNext week: how things move!'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
