#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 28.01 · Magnet Fishing Day (Case 28, Dr. Priya Nair).
Scripts only era (week 25 on): no crew clips generated yet, so no script says "Press Listen"."""
import json
pics = {
    'filings': {'src': 'images/28-01-iron-filings.jpg', 'cap': 'Iron filings around a bar magnet (Black & Davis, Practical Physics, 1913, public domain)'},
    'poles': {'src': 'images/28-01-magnet-poles.png', 'cap': 'Opposite poles attract. Same poles repel.'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE, C_GOLD = '#7A5BB5', '#2F7A55', '#5A3B92', '#C8553D', '#2D7AA6', '#B8860B'
S = {}
S['welcome'] = {'label': 'Welcome · Magnet Fishing Day', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🎣 Magnet fishing', 'tag': 'CASE 28', 'title': 'Cleanup day at the pond', 'col': C_BLUE, 'body': 'Five things fell off the dock after the Duck Derby.'},
    {'label': '📋 The lost-item log', 'tag': 'MAGNET OR NET?', 'title': 'Five lost things', 'col': C_GOLD, 'rows': [['🔑', 'Key on a key ring'], ['🏷️', 'Race number tag'], ['💍', 'Gold ring'], ['🔧', 'Wrench'], ['🪙', 'Penny']]},
    {'label': '🧲 The magnet kit', 'tag': 'A SECOND PROBLEM', 'title': 'The magnets push apart!', 'col': C_RED, 'body': 'How should the team stack them?'}],
    'script': '(Hold a fridge magnet up to a metal spoon or a paperclip.) Click! Now watch. (Hold it to a soda can.) Nothing. Hmm.\n\n[ON SCREEN: Magnet fishing]\nThe Duck Derby is over, and the pond needs a cleanup. Dr. Nair’s team has a magnet on a rope and a long net.\n\n[ON SCREEN: The lost-item log]\nFive things fell off the dock. Some come up on the magnet. Some need the net.\n\n[ON SCREEN: The magnet kit]\nAnd their two magnets keep pushing each other away! Read the case file just below me.'}
S['warmup'] = {'label': 'Warm-Up · cast and reel (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🎣 Cast and reel', 'tag': 'WARM-UP GAME', 'title': 'Six muddy shapes', 'col': C_BLUE, 'rows': [['👉', 'Drag the magnet onto a shape'], ['🤔', 'Guess: Clank, or Nothing?'], ['🎣', 'Reel it up']]},
    {'label': '📝 The haul', 'tag': 'LOOK FOR THE PATTERN', 'title': 'What clanked on?', 'col': C_GOLD, 'body': 'What do the things that came up have in common?'}],
    'script': '(Pretend to drop a rope over the side of your desk, then pull it up slowly.) Got something… I think!\n\n[ON SCREEN: Cast and reel]\nDrag the magnet onto a muddy shape on the pond bottom. Make your guess, Clank or Nothing, then reel it up. Six casts.\n\n[ON SCREEN: The haul]\nWatch your haul list. Some metal things come up, and some metal things stay in the mud. Why? Answer the question, and Clue one is yours.'}
S['part1'] = {'label': 'Part 1 · the worn-label magnet (Clue 2)', 'length': '40–50 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'poles', 'label': '🧲 The rule'},
    {'label': '🖌️ The worn-label magnet', 'tag': 'PART 1 GAME', 'title': 'Which end is N?', 'col': C_RED, 'rows': [['🔄', 'Flip the test magnet'], ['👉', 'Bring it to an end'], ['🖌️', 'Paint the letter']]},
    {'label': '💥 Snap it', 'tag': 'THE WOW', 'title': 'One N piece and one S piece?', 'col': C_GOLD, 'body': 'Test the two new ends and see.'}],
    'script': '(Hold two fridge magnets back to back, then flip one so they snap together.) Push… flip… snap!\n\n[ON SCREEN: The rule]\nOpposite poles pull together. Same poles push apart.\n\n[ON SCREEN: The worn-label magnet]\nThis magnet’s letters wore off. Use the test magnet to find out which end is N and which is S. Then paint them.\n\n[ON SCREEN: Snap it]\nThen snap it in half. Do you get an N piece and an S piece? Test the new ends and find out.'}
S['part2'] = {'label': 'Part 2 · the magnet sweeper (Clue 3)', 'length': '30–40 s', 'want': False, 'parts': [
    {'label': '🪄 The sweeper', 'tag': 'PART 2 GAME', 'title': 'Eight metal things', 'col': C_GREEN, 'rows': [['📎', 'Paperclip'], ['✨', 'Foil ball'], ['🔩', 'Iron nail'], ['🪙', 'Penny'], ['💍', 'Gold ring'], ['🍾', 'Bottle cap'], ['🗝️', 'Brass key'], ['➰', 'Copper wire']]}],
    'script': '(Hold up a key and a paperclip.) Both metal. Will a magnet grab both?\n\n[ON SCREEN: The sweeper]\nDrag the magnet wand slowly over the tray. Watch what jumps up and what stays put. Read every made-of tag.'}
S['part3'] = {'label': 'Part 2 · the iron filings photo', 'length': '30–40 s', 'want': False, 'parts': [
    {'kind': 'photo', 'pic': 'filings', 'label': '🔬 The filings'}],
    'script': '(Wave your hand slowly around an imaginary magnet.) A magnet’s pull is invisible. But we can see it.\n\n[ON SCREEN: The filings]\nThis real photo is more than 100 years old. Tiny bits of iron lined up around a magnet. Tap each number to find where the pull is strongest, and where it is weakest.'}
S['explore'] = {'label': 'Part 4 · the prediction chart (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '📋 The chart', 'tag': 'PART 4 GAME', 'title': 'Predict EVERY row first', 'col': C_PURP, 'rows': [['1', 'Yes or No for all eight'], ['2', 'Lock your chart'], ['3', 'Test every row']]},
    {'label': '⭕ Circled', 'tag': 'WRONG IS GOOD', 'title': 'Circled = something new', 'col': C_RED, 'body': 'A wrong prediction shows you what you didn’t know yet.'}],
    'script': '(Hold up a coin.) This is a nickel. Is a nickel magnetic? Don’t answer yet!\n\n[ON SCREEN: The chart]\nIn Part 4, predict every row first, Yes or No, for all eight things. Lock your chart. Then drag the magnet onto each row.\n\n[ON SCREEN: Circled]\nWrong guesses get circled. Good! That’s where the learning is. Then finish the rule. That’s Clue four.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'Magnet or net?', 'col': C_CASE, 'body': 'Check each lost item’s made-of line. And fix the magnet kit.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO DO', 'title': 'Three places to work', 'col': C_GOLD, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Draw two magnets'], ['CER', 'Claim, evidence, reasoning']]}],
    'script': '[ON SCREEN: Crack the case]\nUse all four clues. Which lost things come up on the magnet, which need the net, and how do you stack the magnets? Then stamp the ranger’s report and open the tackle box!\n\n[ON SCREEN: Your case report]\nNext, two short answers. For Part C, plan two magnets near each other, then sketch and label every pole. Last comes your CER.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“Magnets stick to all metal.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '(Pretend to stick a magnet on everything around you: the desk leg, a window, a can.) It sticks to everything metal… right?\n\n[ON SCREEN: The claim]\nA classmate says magnets stick to all metal. You tested lots of metals today.\n\n[ON SCREEN: The planner]\nTap your side and two facts. Then explain how they prove your claim. Try starting with “This shows that…”'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🎣 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'The rusty bolt from the pond', 'col': C_GOLD, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '🧭 The compass', 'tag': 'THE TWIST', 'title': 'A compass is a magnet too', 'col': C_BLUE, 'body': 'Earth is a giant magnet.'},
    {'label': '➡ Next lesson', 'tag': '28.02', 'title': 'A real fair test', 'col': C_GREEN, 'body': 'Test magnets like a scientist, with a data table.'}],
    'script': '(Hold up an imaginary rusty bolt like a trophy.) The pond is clean!\n\n[ON SCREEN: Your specimen]\nFinish your checklist, and the rusty bolt goes into your Field Notebook.\n\n[ON SCREEN: The compass]\nDid you catch the twist? A compass needle is a tiny magnet, and Earth is a giant one.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Next lesson]\nNext lesson: a real fair test of magnets, with a data table.'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
