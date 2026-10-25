#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 13.02."""
import json
pics = {
    'full': {'src': 'images/13-01-case-seeds.jpg', 'cap': 'Pot A · seed heads packed full'},
    'shade': {'src': 'images/13-01-case-shade.jpg', 'cap': 'Pot B · shady courtyard'},
    'bee': {'src': 'images/13-02-bee.jpg', 'cap': 'A native bee on a beach sunflower (Bob Peterson, CC BY-SA 2.0)'},
    'head': {'src': 'images/13-02-head.jpg', 'cap': 'A beach sunflower head: hundreds of tiny flowers'},
    'vrwm': {'src': 'images/13-02-vr-wm-young.jpg', 'cap': 'A female watermelon flower with a baby watermelon behind it (Pollinator, CC BY-SA 3.0)'},
}
C_CASE, C_GREEN, C_PURP, C_RED = '#B9822A', '#2F7A55', '#7A5BB5', '#C8553D'
S = {}
S['welcome'] = {'label': 'Welcome · the empty seed heads', 'length': '50–60 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'full', 'label': '🌰 Pot A'}, {'kind': 'photo', 'pic': 'shade', 'label': '🌳 Pot B'},
    {'label': '🗂 The case question', 'tag': 'CASE FILE 13 · PART 2', 'title': 'The Empty Seed Heads', 'col': C_CASE, 'body': 'Why were Pot B’s flower heads almost empty of seeds?'}],
    'script': 'Welcome back! We solved part one: same parent, different gardens. But the case isn’t over.\n\n[ON SCREEN: Pot A · Pot B]\nDr. Reyes opened the dry flower heads. Pot A’s were packed with seeds. Pot B’s were almost empty. Hmm. And she says she hardly ever sees bees in that shady courtyard. I wonder if that matters.\n\n[ON SCREEN: The case question]\nThat’s our case. Find four clues today. Press Listen on Dr. Reyes’s walkie-talkie, right below me.'}
S['warmup'] = {'label': 'Warm-Up · pollen pass (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'bee', 'label': '🐝 The bee'},
    {'label': '💛 Pollen', 'tag': 'WARM-UP GAME', 'title': 'Pollen pass', 'col': C_GREEN, 'rows': [['1', 'The bee starts dusty with pollen'], ['2', 'Fly it to another beach sunflower'], ['⚠️', 'Watch out for look-alikes']]}],
    'script': '[ON SCREEN: The bee]\nLook at this little bee on a beach sunflower. See the yellow dust? (Rub your fingers together.) That’s pollen, and it sticks to the bee’s fuzzy body.\n\n[ON SCREEN: Pollen]\nIn Pollen pass, you are the bee. Fly to another beach sunflower and the pollen rubs off. But be careful: two flowers are look-alikes. Then answer: what is that yellow powder for?\n\nPress Listen for Dr. Reyes first.'}
S['vocab'] = {'label': 'Word Wall', 'length': '30–45 s', 'want': False, 'parts': [],
    'script': '[ON SCREEN: Pollination]\nPollination is pollen moving to a flower. (Fly a pretend bee with your hand.)\n\n[ON SCREEN: Germination]\nGermination is a seed starting to grow. (Pop your fist open like a sprout.)\n\nTap each word below me to hear it.'}
S['part1'] = {'label': 'Part 1 · the bag test (Clue 2)', 'length': '45–55 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'head', 'label': '🌻 One head'},
    {'label': '🕸 The test', 'tag': 'PART 1 GAME', 'title': 'A fair test', 'col': C_PURP, 'rows': [['Same', 'sunny garden'], ['Same', 'water'], ['Changes', 'bees or no bees (mesh bag)']]}],
    'script': '[ON SCREEN: One head]\nHere’s something surprising. This sunflower head isn’t one flower. It’s hundreds of tiny flowers packed together, and each one can make one seed.\n\n[ON SCREEN: The test]\nDr. Reyes tied mesh bags on some heads. Air and sun get in, but bees can’t. Everything else stays the same. That’s a fair test: only ONE thing changes.\n\nYou choose which heads get bags, then count the seeds. Press Listen on the walkie-talkie.'}
S['part2'] = {'label': 'Part 2 · put the cycle in order (Clue 3)', 'length': '25–35 s', 'want': False, 'parts': [
    {'label': '🔄 Five steps', 'tag': 'PART 2 GAME', 'title': 'The cycle', 'col': C_GREEN, 'rows': [['🐝', 'Pollination'], ['🥚', 'Fertilization'], ['🌰', 'Seed made'], ['🌬', 'Seed travels'], ['🌱', 'Germination']]}],
    'script': '[ON SCREEN: Five steps]\nFive steps make a new plant. Put them in order. Here’s a tip: what has to happen before a seed can even exist?'}
S['explore'] = {'label': 'Part 4 · seed travelers (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🌱 Five ways', 'tag': 'PART 4 GAME', 'title': 'Seed travelers', 'col': C_GREEN, 'rows': [['🌬', 'Wind'], ['🌊', 'Water'], ['🧦', 'Hitchhiker'], ['🐦', 'Eaten by animals'], ['🐿', 'Falls, then buried']]}],
    'script': '(Pretend to pull something off your sock.) Have you ever found sticky little seeds stuck to your socks after a walk? Those seeds were hitchhiking!\n\n[ON SCREEN: Five ways]\nSeeds can’t walk, but they travel five ways: wind, water, hitchhiking, inside an animal that eats them, or falling and getting buried. Read each Florida seed card and sort it. Look for clues like wings, hooks or berries.\n\nPress Listen on the walkie-talkie.'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '45–55 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'What happened to Pot B?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Three parts', 'col': C_GREEN, 'rows': [['Part B', 'Two short answers'], ['Part C', 'One flower, five steps'], ['CER', 'Claim, evidence, reasoning']]}],
    'script': '[ON SCREEN: Crack the case]\nYou made it! First, crack the case at the top. Still locked? Tap “Show me where the clues are.”\n\n[ON SCREEN: Your case report]\nThen three parts. Part B: two short answers. Part C: pick one Florida flower and write one sentence for each of the five steps. A sketch is a bonus. Last, your CER.\n\nPress Listen on the walkie-talkie.'}
S['partc'] = {'label': 'Part C · follow one flower', 'length': '25–35 s', 'want': False, 'parts': [
    {'label': '🌸 One flower', 'tag': 'PART C', 'title': 'Five sentences', 'col': C_GREEN, 'body': 'Pollination · fertilization · seed · travel · germination'}],
    'script': '[ON SCREEN: One flower]\nPick one Florida flower, maybe a beach sunflower or an orange blossom. Write one sentence for each step, from pollen all the way to a new sprout.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The quote', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“Flowers are just for looking pretty. They don’t really matter to the plant.”'},
    {'label': '⚖ CER', 'tag': 'REMEMBER CER?', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['C', 'Claim: what you think is true.'], ['E', 'Evidence: facts from the lesson that prove it.'], ['R', 'Reasoning: how the facts prove your claim.']]}],
    'script': '[ON SCREEN: The quote]\nA classmate says flowers are just for looking pretty. Hmm.\n\nThink back to the bag test. What happened to the heads the bees couldn’t reach? Could a plant make seeds without its flowers?\n\n[ON SCREEN: CER]\nPick your side in the planner, tap two pieces of evidence, then write your reasoning in your own words. Try starting with “This shows that…”\n\nPress Listen for Dr. Reyes.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🕸 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'Mesh pollinator bag', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '➡ Next week', 'tag': 'WEEK 14', 'title': 'Circle of life', 'col': C_GREEN, 'body': 'Follow Florida plants and animals through their whole lives, and through the seasons.'}],
    'script': '[ON SCREEN: Confetti]\nCase closed! No bees, no pollen moving, no seeds. Pollination comes first.\n\n[ON SCREEN: Your specimen]\nCheck every box in What to Turn In, and a mesh pollinator bag goes into your Field Notebook.\n\n[ON SCREEN: Next week]\nNext week, we’ll follow Florida plants and animals through their whole lives.\n\nPress Listen for Dr. Reyes’s last word.'}
S['vr'] = {'label': 'VR activity · Seed to seed (separate page)', 'length': '45–55 s', 'want': True, 'parts': [
    {'label': '✉️ The seed envelope', 'tag': 'CASE 13 FOLLOW-UP', 'title': 'Can you grow these into new seeds?', 'col': C_CASE, 'body': 'Dr. Reyes saved Pot A’s seeds. She wants proof you know the whole circle, from seed to seed.'},
    {'label': '🧭 Two ways', 'tag': 'PICK AT THE TOP', 'title': 'Two ways to do it', 'col': '#2B7BB9', 'rows': [['🥽', 'VR Field Mission: grow a sunflower circle and a pumpkin circle in Farm Town.'], ['🗂', 'No headset? Follow a watermelon, a pumpkin and a tomato from flower to seed.']]},
    {'kind': 'photo', 'pic': 'vrwm', 'label': '📷 A baby watermelon'},
    {'label': '🥇 The badge', 'tag': 'VR ONLY', 'title': 'Golden Seed badge', 'col': C_GREEN, 'body': 'Save your capture in VR to earn it.'}],
    'script': 'Hi, scientists! Dr. Reyes saved some of Pot A’s seeds, and she has a question.\n\n[ON SCREEN: The seed envelope]\nCan you grow these into NEW seeds? Show her the whole circle.\n\n[ON SCREEN: Two ways]\nPick your way at the top. With a headset, grow two full circles in Farm Town: seeds, four stages, and a bee to close the ring. Then tell each story out loud.\n\n[ON SCREEN: A baby watermelon]\nNo headset? Watch three flowers turn into fruit. See this tiny bump behind the flower? That’s a baby watermelon!\n\n[ON SCREEN: The badge]\nFinish in VR to earn the Golden Seed badge!\n\nPress Listen on Dr. Reyes’s walkie-talkie, right below me.'}
json.dump({'slots': S, 'pics': pics, 'other': ['lesson', 'part3', 'partb', 'figure']}, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote video.json', len(S), 'slots')
