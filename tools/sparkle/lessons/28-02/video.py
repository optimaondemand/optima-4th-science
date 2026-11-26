#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 28.02 · Proof for the Steel Bin (Case 28 part 2, Dr. Priya Nair).
Scripts only era (week 25 on): no crew clips generated yet, so no script says "Press Listen"."""
import json
pics = {
    'scrap': {'src': 'images/28-02-scrap-magnet.jpg', 'cap': 'A lifting magnet at a steel mill scrapyard (Alfred T. Palmer, Library of Congress, public domain)'},
    'table': {'src': 'images/28-02-magnet-data-table.png', 'cap': 'Predict. Test. Record. Sort.'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE, C_GOLD = '#7A5BB5', '#2F7A55', '#5A3B92', '#C8553D', '#2D7AA6', '#B8860B'
S = {}
S['welcome'] = {'label': 'Welcome · Proof for the Steel Bin', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '♻️ The steel bin', 'tag': 'CASE 28 · PART 2', 'title': 'The haul is at the recycling center', 'col': C_GREEN, 'body': 'Eight things from the pond cleanup.'},
    {'label': '📞 Dana’s voicemail', 'tag': 'LISTEN', 'title': 'She wants proof', 'col': C_GOLD, 'body': 'Not “it looks like steel.” Real proof.'},
    {'label': '🔍 The question', 'tag': 'THE QUESTION', 'title': 'Which go in the steel bin?', 'col': C_CASE, 'body': 'And what proof do we send?'}],
    'script': '(Hold up a spoon and a fork.) Both look like steel. Will a magnet grab both? Hmm. You can’t tell by looking.\n\n[ON SCREEN: The steel bin]\nOur pond haul is at the recycling center, and only magnetic steel goes in the steel bin.\n\n[ON SCREEN: Dana’s voicemail]\nDana won’t fill the bin on a guess. She wants proof.\n\n[ON SCREEN: The question]\nWhich things go in, and what proof do we send? Play Dana’s voicemail just below me.'}
S['warmup'] = {'label': 'Warm-Up · spot the differences (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🔍 Two pages', 'tag': 'WARM-UP GAME', 'title': 'Same bottle cap, opposite results', 'col': C_BLUE, 'rows': [['🟨', 'Kai: it jumped!'], ['🟦', 'Mo: nothing.']]},
    {'label': '⚖️ Fair?', 'tag': 'THE QUESTION', 'title': 'Whose result do we trust?', 'col': C_CASE, 'body': 'Find every place they tested differently.'}],
    'script': '(Hold a fridge magnet very close to a paperclip, then very far away.) Close… it jumps. Far… nothing. Same paperclip!\n\n[ON SCREEN: Two pages]\nKai and Mo tested the same bottle cap and got opposite results. Tap every place where they tested differently.\n\n[ON SCREEN: Fair?]\nThen decide whose result to trust. Answer the question, and Clue one is yours.'}
S['part1'] = {'label': 'Part 1 · the how-sure dial (Clue 2)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🎯 Predict', 'tag': 'PART 1 GAME', 'title': 'Predict, then how sure?', 'col': C_GOLD, 'rows': [['1', 'Will it stick?'], ['2', 'Turn the dial'], ['3', 'Test it']]},
    {'label': '⭐ Gold star', 'tag': 'WRONG IS GOOD', 'title': 'Sure and wrong = big learning', 'col': C_RED, 'body': 'A surprise is how scientists learn.'}],
    'script': '(Hold up a can of beans.) We call this a tin can. Will a magnet stick to tin? Make a prediction… how sure are you?\n\n[ON SCREEN: Predict]\nPredict, turn the dial to show how sure you are, then press Test it.\n\n[ON SCREEN: Gold star]\nIf you were sure and wrong, you earn a gold star. Wrong predictions are where scientists learn the most!'}
S['part2'] = {'label': 'Part 2 · messy notes to a data table (Clue 3)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '📝 Sticky notes', 'tag': 'PART 2 GAME', 'title': 'Mo’s messy notes', 'col': C_PURP, 'body': 'Which thing is each note about?'},
    {'kind': 'photo', 'pic': 'table', 'label': '📋 A data table'}],
    'script': '(Wave a handful of sticky notes, or scraps of paper, and drop them.) Oops. Which one was which?\n\n[ON SCREEN: Sticky notes]\nMo wrote every result on a sticky note. Read each one and drag it onto the right row of the data table.\n\n[ON SCREEN: A data table]\nRows and columns keep every result in its place. Watch the spoon row. There’s a surprise hiding there!'}
S['part3'] = {'label': 'Part 3 · make it a fair test', 'length': '20–30 s', 'want': False, 'parts': [
    {'label': '⚖️ Fair test', 'tag': 'PART 3', 'title': 'Change only ONE thing', 'col': C_GREEN, 'rows': [['🧲', 'Same magnet'], ['📏', 'Same distance'], ['🔄', 'Only the material changes']]}],
    'script': '(Hold up one finger.) One. A fair test changes only ONE thing.\n\n[ON SCREEN: Fair test]\nSame magnet, same distance, same way of moving it. Only the material changes. Then the results really mean something.'}
S['explore'] = {'label': 'Part 4 · slide to the jump (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🔒 Lock it', 'tag': 'PART 4 GAME', 'title': 'Lock the fair-test settings', 'col': C_GREEN, 'rows': [['🧲', 'The same magnet'], ['📏', 'Start at 10 cm']]},
    {'label': '📏 Slide', 'tag': 'WATCH FOR THE JUMP', 'title': 'At how many centimeters?', 'col': C_BLUE, 'body': 'No jump means not magnetic.'}],
    'script': '(Slowly slide a paperclip toward a magnet on your desk until it jumps.) There! It jumped!\n\n[ON SCREEN: Lock it]\nIn Part 4, lock the fair-test settings first: the same magnet, and every item starts at 10 centimeters.\n\n[ON SCREEN: Slide]\nThen slide each item toward the magnet. Does it jump? Where? Your data table fills in. That’s Clue four.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'What goes in the steel bin?', 'col': C_CASE, 'body': 'Use all four clues. And remember Dana wants proof.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO DO', 'title': 'Three places to work', 'col': C_GOLD, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Run your own magnet test'], ['CER', 'Claim, evidence, reasoning']]}],
    'script': '[ON SCREEN: Crack the case]\nUse all four clues to fill Dana’s steel bin, and choose the proof to send. Then look for a real giant magnet!\n\n[ON SCREEN: Your case report]\nNext, two short answers. For Part C, test six things at home the fair way, then sketch and label your two sorting circles. Last comes your CER.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“You don’t need to write down test results. Just remember them.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '(Tap your head.) I’ll just remember it all… what was row six again?\n\n[ON SCREEN: The claim]\nA classmate says you don’t need to write results down. Think about Kai and Mo, Mo’s sticky notes, and Dana.\n\n[ON SCREEN: The planner]\nTap your side and two facts. Then explain how they prove your claim. Try starting with “This shows that…”'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🧾 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'Dana’s steel-bin receipt', 'col': C_GOLD, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'kind': 'photo', 'pic': 'scrap', 'label': '🏗️ A giant magnet'},
    {'label': '➡ Next week', 'tag': 'WEEK 29', 'title': 'Mystery materials', 'col': C_BLUE, 'body': 'And what happens when matter changes.'}],
    'script': '(Pretend to stamp a receipt.) Received! The steel bin is full.\n\n[ON SCREEN: Your specimen]\nFinish your checklist, and Dana’s receipt goes into your Field Notebook.\n\n[ON SCREEN: A giant magnet]\nDid you see the steel mill’s giant lifting magnet? It sorts steel just like you did.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Next week]\nNext week: mystery materials!'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
