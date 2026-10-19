#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 9.01."""
import json
pics = {
    'hawk': {'src': 'images/9-01-case-hawk.jpg', 'cap': 'TAG 1 · the hawk at post 7'},
    'pellet': {'src': 'images/9-01-case-pellet.jpg', 'cap': 'TAG 2 · the pellet under the branch'},
    'bones': {'src': 'images/9-01-case-bones.jpg', 'cap': 'TAG 3 · inside the pellet'},
    'sawgrass': {'src': 'images/9-01-case-sawgrass.jpg', 'cap': 'TAG 4 · the sawgrass marsh'},
    'sun': {'src': 'images/9-01-grow-sun.jpg', 'cap': 'Tray in a sunny window'},
    'dark': {'src': 'images/9-01-grow-dark.jpg', 'cap': 'Tray in a dark closet'},
    'frog': {'src': 'images/9-01-frog.jpg', 'cap': 'Green tree frog (CC0)'},
    'hopper': {'src': 'images/9-01-grasshopper.jpg', 'cap': 'A Florida grasshopper'},
    'marsh': {'src': 'images/9-01-marsh.jpg', 'cap': 'A real sawgrass marsh, Everglades (public domain)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_SUN = '#B9822A', '#2F7A55', '#7A5BB5', '#C8553D', '#D9A21B'
S = {}
S['welcome'] = {'label': 'Welcome · open the case', 'length': '50–60 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'hawk', 'label': '📷 The hawk'},
    {'kind': 'photo', 'pic': 'pellet', 'label': '📷 The pellet'},
    {'kind': 'photo', 'pic': 'bones', 'label': '📷 Inside the pellet'},
    {'label': '🗂 The case question', 'tag': 'CASE FILE 9', 'title': 'The Pellet Under Post 7', 'col': C_CASE, 'body': 'The hawk never eats plants. So where did its energy really start?'},
    {'label': '🧭 Your clue bar', 'tag': 'HOW TO SOLVE IT', 'title': 'Find 4 clues', 'col': C_GREEN, 'rows': [['🗂 My clues', 'The bar under the tabs. Tap it to see your clues.'], ['? ? ? ?', 'Each game you finish fills in a clue.'], ['🔒', 'Crack the case at the top of the Assignment.']]}],
    'script': 'Hi, scientists! Welcome to the Field Station, deep in the Florida Everglades.\n\n[ON SCREEN: The hawk]\nMeet our hawk. Every morning it sits by boardwalk post 7.\n\n[ON SCREEN: The pellet · Inside the pellet]\nUnder its branch, Dr. Reyes found this: a pellet. That’s a lump of fur and tiny bones the hawk coughed up. Ew! But it tells us what the hawk ate: mice, frogs, bugs. Never a plant.\n\n[ON SCREEN: The case question]\nSo here’s our case: where did the hawk’s energy really start?\n\n[ON SCREEN: Your clue bar]\nEvery game you finish adds a clue. Press Listen on Dr. Reyes’s walkie-talkie, right below me.'}
S['warmup'] = {'label': 'Warm-Up · trace your lunch (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🍽️ Pick a food', 'tag': 'WARM-UP GAME', 'title': 'Trace your lunch', 'col': C_GREEN, 'rows': [['🍳', 'Scrambled eggs'], ['🍞', 'A slice of bread'], ['🍓', 'A strawberry'], ['🧀', 'Cheese']]},
    {'label': '👣 One step back', 'tag': 'HOW TO PLAY', 'title': 'Ask: where did this come from?', 'col': C_GREEN, 'rows': [['1', 'Pick a food.'], ['2', 'Answer each question to take one step back.'], ['3', 'Trace at least 2 foods, then list where they started.']]}],
    'script': '(Hold up a snack, like a cracker or an apple.) I’m about to eat this. But where did its energy come from?\n\n[ON SCREEN: Pick a food]\nPick one of these foods.\n\n[ON SCREEN: One step back]\nNow take it back one step at a time. Where did it come from? And what gave THAT its energy? Each right answer adds a step to your trail. Keep going until you can’t go back any further.\n\nTrace two foods, then list where each trail ended. Press Listen. Dr. Reyes has a field tip.'}
S['part2'] = {'label': 'Part 2 · the light test (Clue 2) + the marsh photo (Clue 3)', 'length': '50–60 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'sun', 'label': '📷 Sunny tray'},
    {'kind': 'photo', 'pic': 'dark', 'label': '📷 Dark tray'},
    {'label': '🧪 The light test', 'tag': 'PART 2 GAME', 'title': 'Change only the light', 'col': C_PURP, 'rows': [['☀️ 🌥 🌑', 'Pick the light for each tray.'], ['▶', 'Grow both trays.'], ['🍬', 'Check the Food made row.']]},
    {'kind': 'photo', 'pic': 'marsh', 'label': '📸 The marsh photo'}],
    'script': '(Cup your hands around a leaf or a plant.) Plants don’t eat. So how do they get food? They make it!\n\n[ON SCREEN: The light test]\nLet’s test it. Two trays, same seeds, same soil, same water. You change only the light.\n\n[ON SCREEN: Sunny tray · Dark tray]\nHere’s a peek: one grew in a sunny window, one in a dark closet. Hmm, look at that color! Grow both, and check how much food each one made.\n\n[ON SCREEN: The marsh photo]\nThen open every number on this real Everglades marsh.\n\nPress Listen on the walkie-talkie.'}
S['explore'] = {'label': 'Part 4 · build the hawk’s food chain (Clue 4)', 'length': '45–55 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'hopper', 'label': '📷 The grasshopper'},
    {'kind': 'photo', 'pic': 'frog', 'label': '📷 The frog'},
    {'label': '🔗 Five boxes', 'tag': 'PART 4 GAME', 'title': 'Build the chain', 'col': C_SUN, 'rows': [['⭐', 'Energy source'], ['🌿', 'Producer'], ['1️⃣ 2️⃣ 3️⃣', 'Three consumers']]},
    {'label': '➡ The arrows', 'tag': 'THEN', 'title': 'Explain every arrow', 'col': C_GREEN, 'body': 'Each arrow shows which way the energy moves. The meter fills as your model gets stronger.'}],
    'script': '[ON SCREEN: The grasshopper · The frog]\nMeet two more members of the marsh: a grasshopper and a green tree frog.\n\n(Line up three objects on your desk, then point from one to the next.) A food chain is like a line of passes in a game. The energy gets passed along.\n\n[ON SCREEN: Five boxes]\nDrag each card into its box. Start where the energy starts! Two cards don’t belong.\n\n[ON SCREEN: The arrows]\nThen explain every arrow and watch the meter fill.\n\nPress Listen on Dr. Reyes’s walkie-talkie first.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '45–55 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'Where did the hawk’s energy start?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Four places to write', 'col': C_GREEN, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Your own food chain'], ['CER', 'Claim, evidence, reasoning'], ['📋', 'Copy your Gathered Answers into Canvas']]},
    {'label': '🛟 Help buttons', 'tag': 'STUCK?', 'title': 'Help under every box', 'col': C_PURP, 'rows': [['Your answer needs', 'Chips light up as you write.'], ['Hint', 'Three hints, one at a time.'], ['📎 My evidence', 'Your highlights and photo evidence.']]}],
    'script': '[ON SCREEN: Crack the case]\nYou found all four clues! At the top of this tab, crack the case: where did the hawk’s energy really start?\n\n[ON SCREEN: Your case report]\nThen write your case report: two short answers, your own Florida food chain, and a CER.\n\n[ON SCREEN: Help buttons]\nWatch the chips light up as you write. Stuck? Press Hint. Your answers save as you type.\n\nPress Listen on the walkie-talkie.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The quote', 'tag': 'USE YOUR EVIDENCE', 'title': 'Some people say…', 'col': C_RED, 'body': '“Plants don’t really need sunlight. They get their food from the soil.”'},
    {'label': '⚖ CER', 'tag': 'REMEMBER CER?', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['C', 'Claim: what you think is true.'], ['E', 'Evidence: facts from the lesson that prove it.'], ['R', 'Reasoning: how the facts prove your claim.']]},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Tap to plan', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'They drop into your C and E boxes. You write the R.']]}],
    'script': '[ON SCREEN: The quote]\nSome people say, “Plants don’t need sunlight. They get their food from the soil.” Hmm. Remember the dark tray?\n\n[ON SCREEN: CER]\nRemember CER: your claim, your evidence from today, and your reasoning.\n\n[ON SCREEN: The planner]\nTap your side, then two pieces of evidence. They drop right into your boxes. The reasoning is all you. Try starting with “This shows that…”\n\nPress Listen. Dr. Reyes wants to hear your side.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🍃 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'Sunlit leaf', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '➡ Next time', 'tag': 'LESSON 9.02', 'title': 'What if a link goes missing?', 'col': C_GREEN, 'body': 'The same marsh, one piece gone.'}],
    'script': 'Case closed! The hawk never ate a plant, but it still runs on sunlight. And so do you!\n\n[ON SCREEN: Your specimen]\nFinish your checklist and a sunlit leaf goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Next time]\nNext time, we’ll ask: what happens to the hawk if something in the chain goes missing?\n\nPress Listen for Dr. Reyes’s last word.'}
# optional slots
S['part1'] = {'label': 'Part 1 · the Sun is the start', 'length': '20–30 s', 'want': False, 'parts': [],
              'script': '(Flip on a flashlight.) A flashlight needs a battery. Almost all life on Earth runs on one giant battery: the Sun. Read Part 1 to find out why animals can’t make their own food.'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
             'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
S['partc'] = {'label': 'Part C · your own food chain', 'length': '25–35 s', 'want': False, 'parts': [
    {'label': '🗺️ Your place', 'tag': 'PART C', 'title': 'Pick a Florida place', 'col': C_GREEN, 'rows': [['🏖️', 'A beach'], ['🏡', 'A backyard'], ['🐸', 'A pond'], ['🌲', 'A pine forest']]}],
    'script': '[ON SCREEN: Your place]\nNow it’s your turn. Pick a Florida place you know. Name one producer and two consumers, then show how the energy moves. Want to draw it? The sketch pad is a bonus.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'part3', 'figure', 'partb']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
