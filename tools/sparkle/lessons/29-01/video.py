#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 29.01 · Campfire Night (Case 29, Dr. Priya Nair).
Scripts only era (week 25 on): no crew clips generated yet, so no script says "Press Listen"."""
import json
pics = {
    'face': {'src': 'images/29-01-liberty-copper-face.jpg', 'cap': 'A full-size copper copy of Lady Liberty’s face (Renata3, public domain)'},
    'green': {'src': 'images/29-01-liberty-green.jpg', 'cap': 'The Statue of Liberty in 2024 (AskALotl, CC0)'},
    'sort': {'src': 'images/29-01-properties-sort.png', 'cap': 'Two kinds of property clues'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE, C_GOLD = '#7A5BB5', '#2F7A55', '#5A3B92', '#C8553D', '#2D7AA6', '#B8860B'
S = {}
S['welcome'] = {'label': 'Welcome · Campfire Night', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🏕️ Campfire Night', 'tag': 'CASE 29', 'title': 'The end-of-year campout', 'col': C_RED, 'body': 'Ranger Bell made a Changes Bingo card.'},
    {'label': '🎯 Bingo', 'tag': 'TO WIN', 'title': 'Find every NEW substance', 'col': C_GOLD, 'rows': [['🍫', 'Chocolate melting'], ['🪵', 'Logs burning'], ['🔩', 'A grill rusting'], ['♨️', 'Water boiling']]},
    {'label': '❓ The question', 'tag': 'THE QUESTION', 'title': 'Same stuff, or new stuff?', 'col': C_CASE, 'body': 'Which squares made something new?'}],
    'script': '(Hold up an ice cube, or pretend to.) If this melts, is it still water? What if I toasted a piece of bread? Is it still bread?\n\n[ON SCREEN: Campfire Night]\nIt’s the end-of-year campout at Palmetto Springs, and Ranger Bell made a Changes Bingo card.\n\n[ON SCREEN: Bingo]\nTo win, you have to find every square where a brand-new substance formed.\n\n[ON SCREEN: The question]\nThings change all night long. Which ones made something new? Read the case file just below me.'}
S['warmup'] = {'label': 'Warm-Up · lens on the layers (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🔍 The s’more', 'tag': 'WARM-UP GAME', 'title': 'One s’more, two changes', 'col': C_BLUE, 'rows': [['✋', 'Pull it apart'], ['🔍', 'Lens each layer'], ['✨', 'Same stuff or new stuff?']]}],
    'script': '(Pretend to toast a marshmallow on a stick, turning it slowly.) Mmm. Golden brown. Is this still a plain marshmallow?\n\n[ON SCREEN: The s’more]\nPull the s’more apart. Then drag the lens over each layer and find the clues. Is the melted chocolate still chocolate? What about that crispy brown marshmallow? Mark each layer, and Clue one is yours.'}
S['part1'] = {'label': 'Part 1 · safe tools only (Clue 2)', 'length': '30–40 s', 'want': False, 'parts': [
    {'label': '🪵 The block', 'tag': 'PART 1 GAME', 'title': 'Describe it without changing it', 'col': C_GREEN, 'rows': [['📏', 'Ruler'], ['⚖️', 'Scale'], ['🧲', 'Magnet'], ['🔥', 'A match?']]}],
    'script': '(Hold up a pencil. Look at it, measure it with your fingers, tap it.) Still a pencil. I didn’t change it one bit.\n\n[ON SCREEN: The block]\nDescribe the wooden block with tools from the kit. Watch the ID card fill up. But careful: some tools would change the wood into something new!'}
S['part3'] = {'label': 'Part 3 · the time-lapse (Clue 3)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '⏱️ Time-lapse', 'tag': 'PART 3 GAME', 'title': 'Watch slow changes fast', 'col': C_GOLD, 'rows': [['🔩', 'A nail rusting'], ['🍌', 'A banana rotting'], ['🥞', 'A pancake cooking'], ['🗽', 'Lady Liberty']]},
    {'kind': 'photo', 'pic': 'face', 'label': '🗽 Shiny copper'}],
    'script': '(Hold up a penny, or anything copper.) Copper is shiny and reddish brown, like this.\n\n[ON SCREEN: Time-lapse]\nIn Part 3, drag time forward and catch every clue: a nail rusting, a banana rotting, a pancake cooking.\n\n[ON SCREEN: Shiny copper]\nAnd Lady Liberty! She’s made of copper. So why is she green today? Save her for last.'}
S['explore'] = {'label': 'Part 4 · the property sort (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '📦 The belt', 'tag': 'PART 4 GAME', 'title': 'Three bins', 'col': C_PURP, 'rows': [['🎨', 'Property: what it IS'], ['🔄', 'Physical change: same stuff'], ['✨', 'Chemical clue: new stuff']]}],
    'script': '(Pretend to grab things off a moving belt, faster and faster.) Whoa, whoa, too fast!\n\n[ON SCREEN: The belt]\nIn Part 4, cards ride a conveyor belt. Tap the right bin before each card falls off the end. Is it a property, a physical change, or a clue that something new formed? Too fast? Tap the turtle.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'Which squares made something new?', 'col': C_CASE, 'body': 'Use all four clues. Then lights out!'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO DO', 'title': 'Three places to work', 'col': C_GOLD, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Sort 4 things from home'], ['CER', 'Claim, evidence, reasoning']]}],
    'script': '[ON SCREEN: Crack the case]\nUse all four clues to find every bingo square that made a new substance. Then the campfire goes out, and something surprising lights up!\n\n[ON SCREEN: Your case report]\nNext, two short answers. For Part C, find four things at home and sort them, then sketch and label your two columns. Last comes your CER.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“Any color change means a chemical change happened.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '(Hold up a glass of water and pretend to add a drop of food coloring.) Blue water! Did I make a brand-new substance?\n\n[ON SCREEN: The claim]\nA classmate says any color change means a chemical change. Think about the food coloring card, the chocolate and Lady Liberty.\n\n[ON SCREEN: The planner]\nTap your side and two facts. Then explain how they prove your claim. Try starting with “This shows that…”'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🍡 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'A toasted marshmallow', 'col': C_GOLD, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'kind': 'photo', 'pic': 'green', 'label': '🗽 Green Lady Liberty'},
    {'label': '➡ Next lesson', 'tag': '29.02', 'title': 'Mystery materials', 'col': C_BLUE, 'body': 'Use property evidence to identify them.'}],
    'script': '(Wave an imaginary glow stick.) Lights out, campers!\n\n[ON SCREEN: Your specimen]\nFinish your checklist, and a toasted marshmallow goes into your Field Notebook.\n\n[ON SCREEN: Green Lady Liberty]\nRemember: nobody painted her. Copper, air and rain made something new.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Next lesson]\nNext lesson: mystery materials!'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'part2', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
