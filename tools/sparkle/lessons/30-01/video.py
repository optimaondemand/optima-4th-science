#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 30.01 · The Melted Box (Case 30, Dr. Priya Nair).
Scripts only era (week 25 on): no crew clips generated yet, so no script says "Press Listen"."""
import json
pics = {
    'chart': {'src': 'images/30-01-physical-changes.png', 'cap': 'Reversible and hard-to-undo physical changes'},
    'salt': {'src': 'images/30-01-salt-harvest.jpg', 'cap': 'Salt left behind when the seawater dried away'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE, C_GOLD = '#7A5BB5', '#2F7A55', '#5A3B92', '#C8553D', '#2D7AA6', '#B8860B'
S = {}
S['welcome'] = {'label': 'Welcome · the melted box', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '📦 The claim', 'tag': 'CASE 30', 'title': 'SUNSHINE FREIGHT · CLAIM DENIED', 'col': C_RED,
     'rows': [['Shipment', '300 crayons'], ['Left at', '1,200 g'], ['Arrived at', '1,200 g'], ['Inspector', '“A new material.”']]},
    {'label': '❓ The question', 'tag': 'THE QUESTION', 'title': 'Is the art show over?', 'col': C_CASE, 'body': 'One box. One melted slab. One claim to settle.'}],
    'script': '(Hold up a crayon and press it between your hands.) What if this ended up as a puddle? Would it still be a crayon? Would it still be wax?\n\n[ON SCREEN: The claim]\nThree hundred crayons were shipped here for the art show. The truck sat in the sun, and the box arrived as one solid rainbow slab. The freight company says the wax became a new material, so they owe the school nothing.\n\n[ON SCREEN: The question]\nAre they right? Find four clues today and you can settle this claim yourself.'}
S['warmup'] = {'label': 'Warm-Up · the sealed bag (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🧊 The bag', 'tag': 'WARM-UP GAME', 'title': 'One ice cube, zipped in', 'col': C_BLUE,
     'rows': [['⚖️', 'Read the scale'], ['⏱', 'Wait an hour'], ['🔢', 'Call it before you look']]},
    {'label': '🔒 Sealed', 'tag': 'WHY IT MATTERS', 'title': 'Nothing in, nothing out', 'col': C_GREEN, 'body': 'So anything that changes is still in there.'}],
    'script': '(Hold up a zip bag, seal it, and shake it.) Nothing gets in. Nothing gets out.\n\n[ON SCREEN: The bag]\nDrag the bag onto the scale and read the number. Then press Wait an hour. The ice melts into water.\n\n[ON SCREEN: Sealed]\nHere is the part I want you to do before you peek: call the number. Will the scale say less, more, or exactly the same? Pick first, then find out. That is Clue one.'}
S['part1'] = {'label': 'Part 1 · call the number first (Clue 2)', 'length': '30–40 s', 'want': False, 'parts': [
    {'label': '🔢 Three calls', 'tag': 'PART 1 GAME', 'title': 'Type your number before you weigh', 'col': C_GOLD,
     'rows': [['✂️', 'Cut the paper'], ['🫳', 'Flatten the clay'], ['🥄', 'Stir the sugar in']]}],
    'script': '(Write a number on your hand and cover it.) Scientists write down what they expect BEFORE they measure. That way they can’t fool themselves later.\n\n[ON SCREEN: Three calls]\nRead the starting number, make the change, then type your call and weigh it. Three changes. Watch what the number does every single time.'}
S['part2'] = {'label': 'Part 2 · the UNDO button (Clue 3)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '↩️ Six undo buttons', 'tag': 'PART 2 GAME', 'title': 'Which ones really come back?', 'col': C_PURP,
     'rows': [['🧊', 'Melted ice'], ['📄', 'Folded paper'], ['🗞️', 'Shredded paper'], ['🥛', 'Broken glass']]},
    {'kind': 'photo', 'pic': 'chart', 'label': '🔁 Same material'}],
    'script': '(Mime pressing an undo key, then shrug.) Some things undo. Some things really don’t.\n\n[ON SCREEN: Six undo buttons]\nPress UNDO on all six and watch what happens. Then stamp each card: came back, or stuck that way.\n\n[ON SCREEN: Same material]\nHere is the part most people get wrong. Look at the material line under every card. Shredded paper is still paper. Broken glass is still glass. Hard to undo does not mean a new material.'}
S['part3'] = {'label': 'Part 3 · where did the water go?', 'length': '30–40 s', 'want': False, 'parts': [
    {'kind': 'photo', 'pic': 'salt', 'label': '🧂 What the sun left'}],
    'script': '[ON SCREEN: What the sun left]\nThese were ponds of seawater. The sun turned the water into vapor and it floated off into the air. The salt could not float off, so it stayed, every grain of it. Drag the slider on the photo and watch it happen. Nothing disappeared.'}
S['explore'] = {'label': 'Part 4 · the state dial (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🌡️ The dial', 'tag': 'PART 4 GAME', 'title': 'Freezer to stovetop, and back', 'col': C_BLUE,
     'rows': [['🧊', 'Solid'], ['💧', 'Liquid'], ['☁️', 'Gas'], ['⚖️', 'Mass: 200 g the whole way']]},
    {'label': '🖍️ The wow', 'tag': 'LAST STOP', 'title': 'One giant crayon', 'col': C_RED, 'body': 'The slab the company called ruined.'}],
    'script': '(Shiver, then fan yourself.) Cold enough and water is a solid. Hot enough and it is a gas.\n\n[ON SCREEN: The dial]\nTake the dial all the way up to the stovetop, then all the way back down to the freezer. Watch two readouts the whole time: the mass, and the material.\n\n[ON SCREEN: The wow]\nThen stay for the last bit. Dr. Nair takes that melted slab to the art room, and what comes out of the mold is worth seeing.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'Was the claim fair?', 'col': C_CASE, 'body': 'Four clues, and the form’s own two weights.'},
    {'label': '✍️ Your work', 'tag': 'WHAT TO DO', 'title': 'Three places to work', 'col': C_GOLD,
     'rows': [['Part B', 'Two short answers'], ['Part C', 'Four changes from home'], ['CER', 'Claim, evidence, reasoning']]}],
    'script': '[ON SCREEN: Crack the case]\nUse your four clues to settle the claim. Then stamp the form yourself, with your own two pieces of evidence on it.\n\n[ON SCREEN: Your work]\nNext, two short answers. For Part C, find four physical changes at home, sort them into ones you can undo and ones you can’t, and name the material that stays the same in each. Then sketch and label two of them. Last comes your CER.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“Any change you can’t undo must be a chemical change.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP,
     'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '(Tear a piece of paper in half.) I can’t undo that. Does that make it a chemical change?\n\n[ON SCREEN: The claim]\nA classmate says any change you can’t undo must be chemical. Think about the shredded paper, and think about that rainbow slab.\n\n[ON SCREEN: The planner]\nTap your side and two facts. Then explain in your own words how they prove your claim. Try starting with: This shows that.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🖍️ Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'A sliver of the rainbow crayon', 'col': C_GOLD, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '➡ Next lesson', 'tag': '30.02', 'title': 'Chemical changes', 'col': C_GREEN, 'body': 'The last lesson of the year.'}],
    'script': '(Hold up a crayon and wave it.) The art show is on.\n\n[ON SCREEN: Your specimen]\nFinish your checklist and a sliver of that giant rainbow crayon goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Next lesson]\nOne lesson left in the whole year, and it is the big one. Tomorrow the material really does become something new.'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
