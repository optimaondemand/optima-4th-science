#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 29.02 · Kai's Treasure Pouch (Case 29 part 2, Dr. Priya Nair).
Scripts only era (week 25 on): no crew clips generated yet, so no script says "Press Listen"."""
import json
pics = {
    'pyrite': {'src': 'images/29-02-pyrite.jpg', 'cap': 'Kai’s nugget: pyrite from Peru (James St. John, CC BY 2.0)'},
    'gold': {'src': 'images/29-02-gold-nugget.jpg', 'cap': 'A real gold nugget from Australia (James St. John, CC BY 2.0)'},
    'pstreak': {'src': 'images/29-02-pyrite-streak.jpg', 'cap': 'Pyrite’s dark streak on a white tile (Ra’ike, CC BY-SA 3.0)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE, C_GOLD = '#7A5BB5', '#2F7A55', '#5A3B92', '#C8553D', '#2D7AA6', '#B8860B'
S = {}
S['welcome'] = {'label': 'Welcome · Kai’s treasure pouch', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '👝 The pouch', 'tag': 'CASE 29 · PART 2', 'title': 'Kai’s Treasure Pouch', 'col': C_RED, 'rows': [['🟡', 'GOLD!'], ['🔩', 'SILVER bolt'], ['💎', 'DIAMOND'], ['🪙', 'old COIN']]},
    {'label': '❓ The question', 'tag': 'THE QUESTION', 'title': 'What are they really made of?', 'col': C_CASE, 'body': 'Kai only LOOKED at them.'}],
    'script': '(Hold up something shiny, like a spoon or a foil ball, and squint at it.) Is this silver? How would you KNOW?\n\n[ON SCREEN: The pouch]\nThe morning after Campfire Night, Kai panned the creek and came back with a pouch of treasure. Gold, silver, a diamond and an old coin. At least, that’s what his tags say.\n\n[ON SCREEN: The question]\nBut Kai only looked at them. Today you’ll test each find like a detective and prove what it really is. Find four clues, then crack the case.'}
S['warmup'] = {'label': 'Warm-Up · the claim tower (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'pyrite', 'label': '🟡 Kai’s nugget'},
    {'kind': 'photo', 'pic': 'gold', 'label': '🏛️ Museum gold'},
    {'label': '🏗️ The tower', 'tag': 'WARM-UP GAME', 'title': 'Can looks hold up a claim?', 'col': C_GOLD, 'rows': [['🟡', 'Gold-colored'], ['✨', 'Shiny'], ['😤', 'Kai is SURE'], ['🔒', 'Tests: later!']]}],
    'script': '(Hold up two things that look alike, like two pens.) Same color, same shape. Are they the same?\n\n[ON SCREEN: Kai’s nugget]\nHere’s Kai’s nugget from the creek.\n\n[ON SCREEN: Museum gold]\nAnd here’s real gold from a museum. They look almost the same!\n\n[ON SCREEN: The tower]\nKai says his is gold. Stack evidence blocks under his sign and see if the tower holds. Then write what you notice, and Clue one is yours.'}
S['part1'] = {'label': 'Part 1 · fingerprint barcode (Clue 2)', 'length': '30–40 s', 'want': False, 'parts': [
    {'label': '🧬 Fingerprint', 'tag': 'PART 1 GAME', 'title': 'Print the bolt’s fingerprint', 'col': C_BLUE, 'rows': [['🎨', 'Color'], ['💪', 'Hard?'], ['🧲', 'Magnetic?'], ['💧', 'Floats?']]}],
    'script': '(Press your thumb on the table, then look at it.) Your fingerprint is yours alone. Materials have one too!\n\n[ON SCREEN: Fingerprint]\nRun four tests on Kai’s silver bolt. Each one prints a stripe. Then slide your strip along the shelf until every stripe lines up. Which stripe proves it isn’t silver?'}
S['part3'] = {'label': 'Part 3 · fool’s gold! (the wow)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '✏️ Streak test', 'tag': 'PART 3 · THE WOW', 'title': 'Three tests looks can’t do', 'col': C_GOLD, 'rows': [['✏️', 'Streak on a white tile'], ['🔩', 'Scratch with a steel nail'], ['⚖️', 'Weigh the same size']]},
    {'kind': 'photo', 'pic': 'pstreak', 'label': '🖤 A real streak'}],
    'script': '(Scribble with a pencil, then hold up the mark.) The mark is the color of the powder. Scientists call that a streak.\n\n[ON SCREEN: Streak test]\nIn Part 3, rub each nugget on a white tile. Then try a steel nail on each one, and weigh them.\n\n[ON SCREEN: A real streak]\nHere’s a real streak test. Gold leaves a gold-yellow streak. So what do you think a dark streak means?'}
S['explore'] = {'label': 'Part 4 · build your claim (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🧾 Your claim', 'tag': 'PART 4 GAME', 'title': 'I identify ___ as ___ because ___ and ___.', 'col': C_PURP, 'rows': [['🧪', 'Run 3 tests on each sample'], ['📒', 'Check the property guide'], ['🧩', 'Snap in two pieces of evidence']]}],
    'script': '(Count on two fingers.) One piece of evidence? Not enough. Two? Now we’re talking.\n\n[ON SCREEN: Your claim]\nIn Part 4, run tests on three samples and watch the table fill. Then build a claim for each one with two pieces of evidence. If your claim only has one, it bounces right back!'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'What did Kai really find?', 'col': C_CASE, 'body': 'Use all four clues. Then two surprises.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO DO', 'title': 'Three places to work', 'col': C_GOLD, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Your own mystery at home'], ['CER', 'Claim, evidence, reasoning']]}],
    'script': '[ON SCREEN: Crack the case]\nUse all four clues to name what Kai really found. Then test one more “silver” find, and write a museum label.\n\n[ON SCREEN: Your case report]\nNext, two short answers. For Part C, ask someone at home to pick three mystery things. Test them, fill your table, then sketch and label them. Last comes your CER.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“If a material is gray and hard, it must be iron.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '(Hold up a gray spoon or a key.) Gray. Hard. So it must be iron… right?\n\n[ON SCREEN: The claim]\nA classmate says anything gray and hard must be iron. Think about Kai’s coin and the suspect board.\n\n[ON SCREEN: The planner]\nTap your side and two facts. Then explain how they prove your claim. Try starting with: This shows that.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '✨ Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'A chip of Kai’s fool’s gold', 'col': C_GOLD, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'kind': 'photo', 'pic': 'pyrite', 'label': '🟡 Fool’s gold'},
    {'label': '➡ Next lesson', 'tag': '30.01', 'title': 'Physical changes', 'col': C_BLUE, 'body': 'Changes that don’t make anything new.'}],
    'script': '(Pretend to hand a nugget back.) Sorry, Kai. Not rich today!\n\n[ON SCREEN: Your specimen]\nFinish your checklist, and a chip of fool’s gold goes into your Field Notebook.\n\n[ON SCREEN: Fool’s gold]\nRemember: looks can fool you. Tests can’t.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Next lesson]\nNext lesson: changes that don’t make anything new!'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'part2', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
