#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 21.02 · The Speed Limit Sign."""
import json
pics = {
    'cradle': {'src': 'images/21-02-cradle.jpg', 'cap': 'A real Newton’s cradle (Sheila Sund, CC BY 2.0)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE = '#1F7F86', '#2F7A55', '#7A5BB5', '#C8553D', '#2D7AA6'
S = {}
S['welcome'] = {'label': 'Welcome · the speed limit sign', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '📌 The pier notice', 'tag': 'CASE FILE 21 · PART 2', 'title': 'The Speed Limit Sign', 'col': C_RED, 'rows': [['🪧', 'The pier needs a cart speed limit'], ['📏', 'A bumped cart may roll 2 feet at most'], ['🛺', 'Gus: “Speed doesn’t matter!”']]},
    {'label': '✉️ Three sealed envelopes', 'tag': 'NO PEEKING', 'title': 'Gus · Rosa · Sam', 'col': C_PURP, 'body': 'Each one sealed a prediction. They open when the case is cracked.'}],
    'script': '(Hold up a sealed envelope.) Inside this envelope is a prediction. I wrote it BEFORE the test, and I can’t change it now.\n\n[ON SCREEN: The pier notice]\nThe pier manager wants a speed limit for golf carts. But Gus says speed doesn’t matter. He tried it once!\n\n[ON SCREEN: Three sealed envelopes]\nGus, Rosa and Sam each sealed a prediction. Whose will the trials support? Press Listen on Sam’s walkie-talkie, right below me.'}
S['warmup'] = {'label': 'Warm-Up · ghost marbles (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'cradle', 'label': '⚪ A Newton’s cradle'},
    {'label': '👻 Ghost marbles', 'tag': 'WARM-UP GAME', 'title': 'Predict, then play', 'col': C_PURP, 'rows': [['1', 'Drag the ghosts onto the board'], ['2', 'Press Play'], ['3', 'How far off were you?']]}],
    'script': '[ON SCREEN: A Newton’s cradle]\nThis toy is a Newton’s cradle. If I pull back TWO balls and let go, how many fly out the other side? Don’t tell me. Write it in the box first!\n\n[ON SCREEN: Ghost marbles]\nNow the ghost marbles. Your ghost is your prediction. Put it where you think the real marble will stop, then press Play. Press Listen.'}
S['part1'] = {'label': 'Part 1 · the I-knew-it trap (Clue 2)', 'length': '35–45 s', 'want': False, 'parts': [
    {'label': '📝 Before or after?', 'tag': 'PART 1 GAME', 'title': 'The “I knew it!” trap', 'col': C_BLUE, 'rows': [['🕗', 'Read the time on each note'], ['⏪', 'BEFORE the test: can be checked'], ['⏩', 'AFTER the test: too late']]}],
    'script': '(Snap your fingers, then say proudly:) I KNEW I was going to snap!\n\n[ON SCREEN: Before or after?]\nHmm. Does that count? Read each sticky note and look at its time. Which ones were written before the test? Press Listen.'}
S['part2'] = {'label': 'Part 2 · the flag lane (Clue 3)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🚩 The flag lane', 'tag': 'PART 2 GAME', 'title': 'Plant, roll, measure', 'col': C_RED, 'rows': [['🚩', 'Plant your flag'], ['▶', 'Roll the marble'], ['📏', 'Read the gap']]},
    {'label': '📊 The gap meter', 'tag': 'SIX TRIALS', 'title': 'One thing changes', 'col': C_GREEN, 'body': '3 trials on the low ramp, then 3 on the high ramp. Same marble, same block.'}],
    'script': '(Roll a ball across your desk, then roll it again.) Did it stop in the same place both times? Not exactly!\n\n[ON SCREEN: The flag lane]\nPlant your flag where you think the block will stop. Then roll. The tape shows your gap.\n\n[ON SCREEN: The gap meter]\nAfter three trials, change ONE thing: the ramp. Watch out for a surprise trial! Press Listen.'}
S['explore'] = {'label': 'Part 3 · the Newton’s cradle (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '⚪ Pull, predict, let go', 'tag': 'PART 3 GAME', 'title': '1, 2, then 3 balls', 'col': C_PURP, 'rows': [['1', 'Pick how many to pull back'], ['2', 'Predict how many fly out'], ['3', 'Let go, 3 trials each']]},
    {'kind': 'photo', 'pic': 'cradle', 'label': '✨ The real thing'}],
    'script': 'Remember your Warm-Up prediction? Now you find out.\n\n[ON SCREEN: Pull, predict, let go]\nPull back one ball, then two, then three. Predict first every time. Run three trials of each.\n\n[ON SCREEN: The real thing]\nListen for the clicks. Why do you think it slowly stops? Press Listen.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'Whose prediction?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues. The envelopes open!'},
    {'label': '🪧 Make the sign', 'tag': 'AFTER THE CASE', 'title': 'Pick the speed limit', 'col': C_RED, 'body': 'Use the pattern to choose a speed nobody tested.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Three places to write', 'col': C_GREEN, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Your trial table'], ['CER', 'Claim, evidence, reasoning']]}],
    'script': '[ON SCREEN: Crack the case]\nYou have four clues. Crack the case at the top of this tab, and the envelopes open!\n\n[ON SCREEN: Make the sign]\nThen make the speed limit sign. Nobody tested that speed. Can your pattern predict it?\n\n[ON SCREEN: Your case report]\nLast, two short answers, your trial table and your CER. Press Listen.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“You should only run ONE trial. Running more is a waste of time.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '[ON SCREEN: The claim]\nOne trial and done? Hmm. Think about trial five on the flag lane. Think about Gus’s test.\n\nThere’s no wrong side, as long as you prove it.\n\n[ON SCREEN: The planner]\nTap your side and two facts, then explain how they prove your claim. Try starting with “This shows that…” Press Listen.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '✉️ Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'An opened prediction envelope', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '⚪ Cradle free play', 'tag': 'BONUS GAME', 'title': 'How long is your streak?', 'col': C_GREEN, 'body': '5 or 7 balls. Predict, then let go.'},
    {'label': '➡ Next time', 'tag': 'LESSON 22.01', 'title': 'Energy changes form', 'col': C_BLUE, 'body': 'Energy that turns from one kind into another.'}],
    'script': '(Open the envelope you held up at the start and read it.) My prediction: faster pushes farther. Supported!\n\n[ON SCREEN: Your specimen]\nFinish your checklist, and the opened envelope goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Cradle free play]\nThen try cradle free play. Tell me your best streak.\n\n[ON SCREEN: Next time]\nNext time: energy that changes from one form to another. Press Listen for Sam’s last word.'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
