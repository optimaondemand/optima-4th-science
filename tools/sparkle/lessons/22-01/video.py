#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 22.01 · The Beacon Went Dark."""
import json
pics = {
    'uscg': {'src': 'images/22-01-coast-guard-light.jpg', 'cap': 'A real solar harbor light (U.S. Coast Guard, public domain)'},
    'toaster': {'src': 'images/22-01-toaster.jpg', 'cap': 'A running toaster (Kansattica, CC BY 4.0)'},
    'solar': {'src': 'images/22-01-solar-light.jpg', 'cap': 'A solar garden light (Leon Brooks, public domain)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE, C_GOLD = '#1F7F86', '#2F7A55', '#7A5BB5', '#C8553D', '#2D7AA6', '#B8860B'
S = {}
S['welcome'] = {'label': 'Welcome · the jetty light', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '📄 Notice to Mariners', 'tag': 'CASE FILE 22', 'title': 'Jetty light out', 'col': C_BLUE, 'rows': [['🟢', 'The jetty light is dark'], ['🚤', 'Boats use it to find the harbor'], ['🔌', 'Nobody plugs it in!']]},
    {'kind': 'photo', 'pic': 'uscg', 'label': '🔲 A real solar harbor light'}],
    'script': '(Turn a lamp on, then unplug it.) Click. No energy in, no light out.\n\n[ON SCREEN: Notice to Mariners]\nBut the light at the end of the Palmetto Beach jetty has no plug at all. And three nights ago, it went dark.\n\n[ON SCREEN: A real solar harbor light]\nHere’s a real one. See the little square on top? Keep your eye on that. Open the case file just below me and read the keeper’s ticket.'}
S['warmup'] = {'label': 'Warm-Up · the black box (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '📦 The black box', 'tag': 'WARM-UP GAME', 'title': 'What’s inside?', 'col': C_PURP, 'rows': [['📥', 'Read what goes IN'], ['📤', 'Read what comes OUT'], ['🃏', 'Drag the device onto the box']]},
    {'kind': 'photo', 'pic': 'toaster', 'label': '🍞 Box A, opened'}],
    'script': '(Hold up a closed box and shake it.) I can’t see inside. But I can see what goes in, and what comes out.\n\n[ON SCREEN: The black box]\nThat’s a black box. Read each box’s IN and OUT, then drag the device that fits onto it.\n\n[ON SCREEN: Box A, opened]\nHere’s one opened up. Look at those glowing wires! Press Listen on Sam’s walkie-talkie, right below me.'}
S['part1'] = {'label': 'Part 1 · flip the arrow tag (Clue 2)', 'length': '35–45 s', 'want': False, 'parts': [
    {'label': '🏷️ Moves or changes?', 'tag': 'PART 1 GAME', 'title': 'Flip the arrow tag', 'col': C_BLUE, 'rows': [['➡️', 'MOVES: same form, it travels'], ['🔄', 'CHANGES: a new form']]}],
    'script': '(Roll a ball to the camera, then rub your hands fast.) The ball passed its motion along. My hands turned motion into heat.\n\n[ON SCREEN: Moves or changes?]\nOne MOVES, one CHANGES. Tag every arrow, then press Check my tags. Watch the colors!'}
S['part2'] = {'label': 'Part 2 · the energy pipes (Clue 3)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🚰 The energy pipes', 'tag': 'PART 2 GAME', 'title': '10 units in', 'col': C_RED, 'rows': [['🎚️', 'Guess the useful split'], ['▶', 'Pour in 10 units'], ['🔢', 'Count both pipes']]},
    {'label': '💡 Old bulb vs. LED', 'tag': 'TRY THESE TWO', 'title': 'Same light?', 'col': C_GOLD, 'body': 'Which one sends more energy out as heat?'}],
    'script': 'Here’s a riddle. Can a device use up energy? Can it make new energy?\n\n[ON SCREEN: The energy pipes]\nGuess first: how many of the 10 units will come out useful? Then pour, and count both pipes.\n\n[ON SCREEN: Old bulb vs. LED]\nTry the old bulb, then the LED. One of them gets really hot. Press Listen.'}
S['explore'] = {'label': 'Part 3 · back to the Sun (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '☀️ Follow it back', 'tag': 'PART 3 GAME', 'title': 'Where did the energy come from?', 'col': C_GOLD, 'rows': [['🍞', 'Start with hot toast'], ['⬅️', 'Take one step back at a time'], ['🔁', 'Then follow one more device']]},
    {'kind': 'photo', 'pic': 'solar', 'label': '🏮 Sun to panel to light'}],
    'script': '(Hold up a piece of toast.) This toast is warm. Where did that heat come from? The toaster. And before that?\n\n[ON SCREEN: Follow it back]\nFollow the energy backward, one step at a time, until you can’t go back any further.\n\n[ON SCREEN: Sun to panel to light]\nThen try another device. Look at where every trail starts. Press Listen.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'Why did the light go dark?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues.'},
    {'label': '🧾 The repair ticket', 'tag': 'AFTER THE CASE', 'title': 'Find the broken link', 'col': C_GREEN, 'body': 'Tap the broken link, pick the fix, stamp it FIXED.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Three places to write', 'col': C_RED, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Your device energy map + sketch'], ['CER', 'Claim, evidence, reasoning']]}],
    'script': '[ON SCREEN: Crack the case]\nYou have four clues. Crack the case at the top of this tab.\n\n[ON SCREEN: The repair ticket]\nThen be the engineer: find the broken link in the light’s chain and stamp the ticket FIXED.\n\n[ON SCREEN: Your case report]\nLast, two short answers, your device energy map with a labeled sketch, and your CER.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“A toaster CREATES heat energy. The heat wasn’t there before.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '[ON SCREEN: The claim]\nCreates heat? Out of nothing? Hmm. Unplug a toaster and see how much toast you make.\n\nThere’s no wrong side, as long as you prove it.\n\n[ON SCREEN: The planner]\nTap your side and two facts, then explain how they prove your claim. Try starting with “This shows that…” Press Listen.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🪶 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'A pelican feather', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '⚓ Light the harbor', 'tag': 'BONUS GAME', 'title': 'Can you get 9 stars?', 'col': C_GREEN, 'body': 'Pick the best device for three night jobs.'},
    {'label': '➡ Next time', 'tag': 'LESSON 22.02', 'title': 'You design a device', 'col': C_BLUE, 'body': 'Light with no battery and no plug. How would you build it?'}],
    'script': '(Pretend to shine a flashlight.) The jetty light shines again, and the pelican has its own perch!\n\n[ON SCREEN: Your specimen]\nFinish your checklist, and a pelican feather goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Light the harbor]\nThen try the bonus game. Go for nine stars.\n\n[ON SCREEN: Next time]\nNext time, YOU are the engineer. Start thinking: how could you make light with no plug and no battery?'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
