#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 11.02."""
import json
pics = {
    'draftA': {'src': 'images/11-02-draft-labels.jpg', 'cap': 'Draft A · a photo with labels'},
    'draftB': {'src': 'images/11-02-draft-painting.jpg', 'cap': 'Draft B · a painting from 1836 (Audubon)'},
    'draftC': {'src': 'images/11-02-draft-model.jpg', 'cap': 'Draft C · a photo with arrows and a caption'},
    'gator': {'src': 'images/11-02-gator-head.jpg', 'cap': 'An alligator’s teeth'},
    'anhinga': {'src': 'images/11-02-adaptation-model.png', 'cap': 'The anhinga model'},
}
C_CASE, C_GREEN, C_PURP, C_RED = '#B9822A', '#2F7A55', '#7A5BB5', '#C8553D'
S = {}
S['welcome'] = {'label': 'Welcome · the refuge sign', 'length': '50–60 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'draftA', 'label': '📷 Draft A'}, {'kind': 'photo', 'pic': 'draftB', 'label': '📷 Draft B'}, {'kind': 'photo', 'pic': 'draftC', 'label': '📷 Draft C'},
    {'label': '🗂 The case question', 'tag': 'CASE FILE 11 · PART 2', 'title': 'The Refuge Sign', 'col': C_CASE, 'body': 'Which draft explains how the spoonbill survives, and what would make the other two better?'}],
    'script': 'Welcome back, scientists! Remember the soggy notebook? Our case report made it to the refuge, and now they want a sign about the spoonbill.\n\n[ON SCREEN: Draft A · Draft B · Draft C]\nThree people sent drafts. A photo with labels. A beautiful painting from 1836. And a photo with arrows.\n\n[ON SCREEN: The case question]\nOnly one can go on the sign. Which one really explains how the spoonbill survives?\n\nFind four clues today. Press Listen on Dr. Reyes’s walkie-talkie, right below me.'}
S['warmup'] = {'label': 'Warm-Up · point the arrow (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'gator', 'label': '📷 The teeth'},
    {'label': '➜ Two drawings', 'tag': 'WARM-UP GAME', 'title': 'Label or model?', 'col': C_GREEN, 'rows': [['Drawing 1', 'just the word “teeth”'], ['Drawing 2', 'an arrow + action words']]}],
    'script': '(Hold up a sticky note that says “teeth.”) If I stick this on an alligator drawing, what do you learn? Just a name.\n\n[ON SCREEN: The teeth]\nNow watch. (Draw an arrow in the air toward a pretend fish.) An arrow points from the part to what it acts on.\n\n[ON SCREEN: Two drawings]\nBuild Drawing 2: drag the arrow, then pick the action words. Then tell me which drawing teaches a friend more.\n\nPress Listen for Dr. Reyes’s field trick.'}
S['part2'] = {'label': 'Part 2 · upgrade the drawing (Clue 2)', 'length': '40–50 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'anhinga', 'label': '📷 The anhinga model'},
    {'label': '⬆️ Three steps', 'tag': 'PART 2 GAME', 'title': 'Upgrade the drawing', 'col': C_PURP, 'rows': [['1', 'A label'], ['2', 'An arrow that shows action'], ['3', 'A caption about a survival need']]}],
    'script': '[ON SCREEN: The anhinga model]\nLook at this anhinga. Every arrow goes from a part to what it does. The words at the bottom say why it matters.\n\n[ON SCREEN: Three steps]\nNow you upgrade a spoonbill photo, one step at a time: a label, an arrow, a caption. Watch the meter fill up as your drawing turns into a model.\n\nPress Listen on the walkie-talkie.'}
S['part3'] = {'label': 'Part 3 · chain it (Clue 3)', 'length': '30–40 s', 'want': False, 'parts': [
    {'label': '🔗 The chain', 'tag': 'PART 3 GAME', 'title': 'Structure → Action → Survival need', 'col': C_GREEN, 'rows': [['🦴', 'Structure: the part'], ['⚙️', 'Action: what it does'], ['🍎', 'Survival need: food, water, air, shelter or safety']]}],
    'script': '[ON SCREEN: The chain]\nEvery strong model follows a chain: the part, what it does, and the need it meets. Build four chains. Careful: two cards in each set are tricks. Press Listen first.'}
S['explore'] = {'label': 'Part 4 · the model kit (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🧩 Model kit', 'tag': 'PART 4 GAME', 'title': 'Build a model on a real photo', 'col': C_GREEN, 'rows': [['+', 'Tap a part'], ['➜', 'Point the arrow'], ['⚙️', 'Pick what it does'], ['🍎', 'Pick the survival need']]}],
    'script': '(Hold up a photo or a picture from a book.) Scientists don’t always draw from scratch. Sometimes they draw arrows right on a photo!\n\n[ON SCREEN: Model kit]\nPick a Florida organism: a tree frog, a gopher tortoise, an anhinga or a manatee. Tap a part, point the arrow, and pick what it does and which need it meets. Your caption writes itself. Build two if you can!\n\nPress Listen on the walkie-talkie.'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '45–55 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'Which draft goes on the sign?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Four places to write', 'col': C_GREEN, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Your own model in words'], ['CER', 'Claim, evidence, reasoning'], ['📋', 'Copy your Gathered Answers into Canvas']]}],
    'script': '[ON SCREEN: Crack the case]\nYou found all four clues! At the top of this tab, crack the case: which draft goes on the refuge sign, and what would fix the other two?\n\n[ON SCREEN: Your case report]\nThen write your case report. In Part C, you build your own model in words: a label, an arrow, a caption. Watch the chips light up. Stuck? Press Hint.\n\nPress Listen on the walkie-talkie.'}
S['partc'] = {'label': 'Part C · build an annotated model', 'length': '25–35 s', 'want': False, 'parts': [
    {'label': '🏷️ Your model', 'tag': 'PART C', 'title': 'Label · Arrow · Caption', 'col': C_GREEN, 'rows': [['🏷️', 'Name the part'], ['➜', 'Tell what it does'], ['💬', 'Tie it to a survival need']]}],
    'script': '[ON SCREEN: Your model]\nPick a Florida organism, not the spoonbill. Name one part, tell what it does, and finish with a caption about a survival need. Want to draw it too? The sketch pad is a bonus.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The quote', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“A drawing isn’t science — it’s art. Real scientists only use numbers and graphs.”'},
    {'label': '⚖ CER', 'tag': 'REMEMBER CER?', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['C', 'Claim: what you think is true.'], ['E', 'Evidence: facts from the lesson that prove it.'], ['R', 'Reasoning: how the facts prove your claim.']]}],
    'script': '[ON SCREEN: The quote]\nA classmate says drawings are just art, not science. Hmm!\n\n(Hold up a notebook page with a sketch and arrows.) Is this art, or is it explaining something?\n\n[ON SCREEN: CER]\nPick your side in the planner, tap two pieces of evidence, then write your reasoning in your own words.\n\nPress Listen for Dr. Reyes.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '📝 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'Annotated spoonbill sketch', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '➡ Next week', 'tag': 'LESSON 12.01', 'title': 'Senses to brain', 'col': C_GREEN, 'body': 'Four trail cameras, four Florida animals, one mystery.'}],
    'script': 'Case closed for good! Draft C goes on the sign, because it explains, not just names.\n\n[ON SCREEN: Your specimen]\nFinish your checklist and an annotated spoonbill sketch goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Next week]\nNext week: four trail cameras catch four Florida animals reacting at once. Why? Bring your detective eyes!\n\nPress Listen for Dr. Reyes’s last word.'}
json.dump({'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'part1', 'partb']}, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote video.json', len(S), 'slots')
