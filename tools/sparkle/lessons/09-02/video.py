#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 9.02."""
import json
pics = {
    'vrrabbit': {'src': 'images/09-02-vr-rabbit.jpg', 'cap': 'Photo walk post 3: a marsh rabbit (Everglades NPS, public domain)'},
    'hawk': {'src': 'images/9-01-case-hawk.jpg', 'cap': 'TAG 1 · the hawk at post 7'},
    'frog': {'src': 'images/9-01-frog.jpg', 'cap': 'TAG 2 · green tree frog (missing)'},
    'hopper': {'src': 'images/9-01-grasshopper.jpg', 'cap': 'TAG 3 · grasshoppers'},
    'sawgrass': {'src': 'images/9-01-case-sawgrass.jpg', 'cap': 'TAG 4 · the marsh, silent at night'},
    'snake': {'src': 'images/9-02-hawk-snake.jpg', 'cap': 'Red-shouldered hawk with a snake, Everglades (public domain)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_SUN = '#B9822A', '#2F7A55', '#7A5BB5', '#C8553D', '#D9A21B'
S = {}
S['welcome'] = {'label': 'Welcome · open the case', 'length': '50–60 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'hawk', 'label': '📷 The hawk'},
    {'kind': 'photo', 'pic': 'frog', 'label': '📷 The missing frogs'},
    {'label': '📝 The volunteer’s note', 'tag': 'PINNED TO THE CASE FILE', 'title': '“No frogs? Then…”', 'col': C_RED, 'body': '“The hawk will starve, and nothing else in the marsh will change.”'},
    {'label': '🗂 The case question', 'tag': 'CASE FILE 9 · PART 2', 'title': 'Silent Night at Post 7', 'col': C_CASE, 'body': 'The frogs are gone. What really happens to the hawk and the rest of the marsh?'}],
    'script': 'Welcome back to the Field Station, scientists!\n\n[ON SCREEN: The hawk]\nRemember our hawk at post 7?\n\n[ON SCREEN: The missing frogs]\nAfter a long dry spell, the green tree frogs left the marsh. At night, it went silent. (Cup your hand to your ear.) Not one frog calling.\n\n[ON SCREEN: The volunteer’s note]\nA volunteer left this note: “The hawk will starve, and nothing else will change.” Hmm. Is she right?\n\n[ON SCREEN: The case question]\nThat’s our case. Find four clues, then crack it. Press Listen on Dr. Reyes’s walkie-talkie.'}
S['warmup'] = {'label': 'Warm-Up · more or fewer? (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🔗 A food chain', 'tag': 'WARM-UP GAME', 'title': 'One link disappears', 'col': C_GREEN, 'rows': [['🌱', 'Grass'], ['🐇', 'Rabbits'], ['🦊', 'Foxes']]},
    {'label': '⬆️⬇️ Sort the cards', 'tag': 'HOW TO PLAY', 'title': 'More or fewer?', 'col': C_GREEN, 'rows': [['1', 'Read which link disappears.'], ['2', 'Drag the card to More or Fewer.'], ['3', 'Sort all six.']]}],
    'script': '(Stack three books or blocks in a tower.) Watch. What happens if I pull out the middle one?\n\n[ON SCREEN: A food chain]\nA food chain is a little like this tower. Grass, rabbits, foxes. Now the rabbits disappear. Does the grass get more, or fewer? And the foxes?\n\n[ON SCREEN: Sort the cards]\nSort all six cards. Then write your reasons. Press Listen. Dr. Reyes has a tip.'}
S['part2'] = {'label': 'Part 2 · the hawk photo (Clue 2)', 'length': '35–45 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'snake', 'label': '📸 The hawk photo'},
    {'label': '🕸️ A food web', 'tag': 'PART 2', 'title': 'Many chains, connected', 'col': C_PURP, 'rows': [['🦅', 'eats frogs, snakes, lizards, mice'], ['🐸', 'eats grasshoppers, moths, beetles']]}],
    'script': '(Hold up a plate.) If your only food were pizza, and the pizza ran out, you’d be in trouble! But you eat lots of foods.\n\n[ON SCREEN: The hawk photo]\nLook what this real hawk caught in the Everglades. That’s not a frog! Tap every number on the photo.\n\n[ON SCREEN: A food web]\nWhen animals eat many things, their food chains connect into a food web.\n\nPress Listen on the walkie-talkie.'}
S['part3'] = {'label': 'Part 3 · the missing-link test (Clue 3)', 'length': '45–55 s', 'want': True, 'parts': [
    {'label': '📊 The model', 'tag': 'PART 3 GAME', 'title': 'Remove one link', 'col': C_SUN, 'rows': [['🦅 🐸 🦗 🌾', 'Hawks, frogs, grasshoppers, sawgrass'], ['✂️', 'Pick one to remove.'], ['⬆️ ⬇️ ➖', 'Predict for the others.'], ['▶', 'Run four seasons.']]},
    {'kind': 'photo', 'pic': 'hopper', 'label': '📷 Grasshoppers'},
    {'label': '🔓 To unlock', 'tag': 'TEST BOTH', 'title': 'Frogs AND hawks', 'col': C_GREEN, 'body': 'Run the frog test and the hawk test. Then answer the question.'}],
    'script': '[ON SCREEN: The model]\nScientists can’t take every frog out of a real marsh just to see what happens. So we use a model.\n\nPick one living thing to remove. Predict: will the others have more, fewer, or about the same? Then press Run and watch four seasons go by.\n\n[ON SCREEN: Grasshoppers]\nKeep an eye on the grasshoppers.\n\n[ON SCREEN: To unlock]\nTest the frogs AND the hawks. Some bars might surprise you! Press Listen first.'}
S['explore'] = {'label': 'Part 4 · test the volunteer’s note (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '📝 Three predictions', 'tag': 'PART 4 GAME', 'title': 'The volunteer’s note', 'col': C_RED, 'rows': [['1', '“The hawk will starve.”'], ['2', '“There will be more grasshoppers.”'], ['3', '“Nothing else will change.”']]},
    {'label': '✅❌ Stamp it', 'tag': 'HOW TO PLAY', 'title': 'Supported or not?', 'col': C_PURP, 'rows': [['✅', 'Supported: the evidence agrees.'], ['❌', 'Not supported: the evidence disagrees.'], ['🔎', 'Pick the line that proves it.']]},
    {'kind': 'photo', 'pic': 'sawgrass', 'label': '📷 The marsh'}],
    'script': '[ON SCREEN: Three predictions]\nTime to check the volunteer’s note. She made three predictions.\n\n[ON SCREEN: Stamp it]\n(Pretend to stamp a paper on your desk.) Stamp each one. Supported means the evidence agrees. Not supported means it doesn’t. Then pick the line that proves it.\n\n[ON SCREEN: The marsh]\nUse your hawk photo and your missing-link test. Press Listen on Dr. Reyes’s walkie-talkie.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '45–55 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'What happens when the frogs leave?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Four places to write', 'col': C_GREEN, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Your own missing link'], ['CER', 'Does the prey grow forever?'], ['📋', 'Copy your Gathered Answers into Canvas']]},
    {'label': '🛟 Help buttons', 'tag': 'STUCK?', 'title': 'Help under every box', 'col': C_PURP, 'rows': [['Your answer needs', 'Chips light up as you write.'], ['Hint', 'Three hints, one at a time.'], ['📎 My evidence', 'Your photo evidence and test results.']]}],
    'script': '[ON SCREEN: Crack the case]\nFour clues! At the top of this tab, crack the case: what really happens when the frogs leave?\n\n[ON SCREEN: Your case report]\nThen write your case report: two short answers, your own Florida food chain with one link missing, and a CER. Remember the frogs in the hawk test? Did they grow forever?\n\n[ON SCREEN: Help buttons]\nStuck? Press Hint. Your answers save as you type. Press Listen on the walkie-talkie.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🐛 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'Caterpillar', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '➡ Coming up', 'tag': 'NEXT TIME', 'title': 'A giant oak falls', 'col': C_GREEN, 'body': 'A storm knocks down one big tree. What changes in the forest?'}],
    'script': 'Case closed! The hawk switched to snakes and mice. But the marsh still changed: more grasshoppers, less sawgrass. One missing link ripples both ways!\n\n[ON SCREEN: Your specimen]\nFinish your checklist to add a caterpillar to your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Coming up]\nComing up: a giant oak falls in a storm. What happens to the forest around it?\n\nPress Listen for Dr. Reyes’s last word.'}
# optional slots
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '30–40 s', 'want': False, 'parts': [
    {'label': '💬 The quote', 'tag': 'USE YOUR EVIDENCE', 'title': 'Some people say…', 'col': C_RED, 'body': '“If a top predator like a hawk disappears, the prey will just keep growing forever, and the ecosystem will be fine.”'}],
    'script': '[ON SCREEN: The quote]\nSome people say that if the hawk disappears, the prey grows forever. Hmm. Look back at your hawk test. Tap your side in the planner, pick two pieces of evidence, then write your reasoning. Try starting with “This shows that…”'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
             'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
# VR activity page (vr-9-02.html) uses the same prefix: g4sci-9-2-vr.mp4
S['vr'] = {'label': 'VR activity · The hawk’s backup menu (separate page)', 'length': '45–55 s', 'want': True, 'parts': [{'label': '📌 The note', 'tag': 'CASE 9', 'title': '“No frogs? Then the hawk will starve.”', 'col': '#C2552E', 'body': 'Is the volunteer right?'}, {'label': '🧭 Two ways', 'tag': 'PICK AT THE TOP', 'title': 'Two ways to survey', 'col': '#2B7BB9', 'rows': [['🥽', 'VR Field Survey: walk the Everglades and look.'], ['📷', 'No headset? Take the boardwalk photo walk.']]}, {'kind': 'photo', 'pic': 'vrrabbit', 'label': '📷 Field notes'}, {'label': '🪶 The badge', 'tag': 'VR ONLY', 'title': 'Red-Shoulder Feather badge', 'col': '#C2552E', 'body': 'Finish your VR survey to earn it.'}], 'script': 'Hi, scientists! Remember the volunteer’s note? (Hold up a sticky note.) “No frogs? Then the hawk will starve.”\n\n[ON SCREEN: The note]\nToday you’ll find out if she’s right. You won’t build anything. You’ll do a field survey: a careful look at every living thing in one place.\n\n[ON SCREEN: Two ways]\nPick your way at the top. With a headset, walk the Everglades in VR. No headset? Take the boardwalk photo walk.\n\n[ON SCREEN: Field notes]\nEither way, write down at least five living things in your field notes, and ask: could a hawk eat this one?\n\n[ON SCREEN: The badge]\nFinish in VR and you earn the Red-Shoulder Feather badge!\n\nPress Listen on Dr. Reyes’s walkie-talkie, right below me.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'part1', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
