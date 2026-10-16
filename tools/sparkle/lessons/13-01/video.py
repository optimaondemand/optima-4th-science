#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 13.01."""
import json
pics = {
    'parent': {'src': 'images/13-01-case-parent.jpg', 'cap': 'Tag P · the wild parent plant on the dunes'},
    'sun': {'src': 'images/13-01-case-sun.jpg', 'cap': 'Pot A · sunny dune garden'},
    'shade': {'src': 'images/13-01-case-shade.jpg', 'cap': 'Pot B · shady courtyard'},
    'kitten': {'src': 'images/13-01-kitten.jpg', 'cap': 'Florida panther kitten (USACE, public domain)'},
    'panther': {'src': 'images/13-01-panther.jpg', 'cap': 'Adult Florida panther (USFWS, public domain)'},
    'mom': {'src': 'images/13-01-pan-mom.jpg', 'cap': 'Panther mother on a trail camera (USFWS, public domain)'},
    'kits': {'src': 'images/13-01-pan-kits.jpg', 'cap': 'Panther kittens in their den (USFWS, public domain)'},
}
C_CASE, C_GREEN, C_PURP, C_RED = '#B9822A', '#2F7A55', '#7A5BB5', '#C8553D'
S = {}
S['welcome'] = {'label': 'Welcome · one parent, two gardens', 'length': '50–60 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'parent', 'label': '🌻 The parent'}, {'kind': 'photo', 'pic': 'sun', 'label': '☀️ Pot A'}, {'kind': 'photo', 'pic': 'shade', 'label': '🌳 Pot B'},
    {'label': '🗂 The case question', 'tag': 'CASE FILE 13', 'title': 'One Parent, Two Gardens', 'col': C_CASE, 'body': 'Did the seeds get mixed up, or can one parent plant have offspring this different?'}],
    'script': 'Welcome, scientists! New week, new case.\n\n[ON SCREEN: The parent]\nThis is a wild beach sunflower on a Florida dune. Dr. Reyes collected its seeds.\n\n[ON SCREEN: Pot A · Pot B]\nShe planted some in the sun and some in the shade. Look how different they are! One is bushy with tons of flowers. One is tall and skinny. Hmm. I wonder… did the seeds get mixed up?\n\n[ON SCREEN: The case question]\nThat’s our case. Find four clues today. Press Listen on Dr. Reyes’s walkie-talkie, right below me.'}
S['warmup'] = {'label': 'Warm-Up · find the family (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'kitten', 'label': '🐾 Baby'}, {'kind': 'photo', 'pic': 'panther', 'label': '🐆 Parent'},
    {'label': '🔎 Look for', 'tag': 'WARM-UP GAME', 'title': 'Find the family', 'col': C_GREEN, 'rows': [['👀', 'Body shape first'], ['🎨', 'Colors can fool you'], ['✍️', 'Then list the inherited traits']]}],
    'script': '[ON SCREEN: Baby]\nLook at this baby. Spots! Blue eyes!\n\n[ON SCREEN: Parent]\nNow look at its mom: plain tan, no spots. Same face, same round ears, though. This kitten is a Florida panther, and its spots fade as it grows.\n\n[ON SCREEN: Look for]\nIn the warm-up game, match four Florida babies to their parents. Look at body shape first, because colors can fool you. Then list the traits the baby inherited.\n\nPress Listen for Dr. Reyes first.'}
S['vocab'] = {'label': 'Word Wall', 'length': '30–45 s', 'want': False, 'parts': [],
    'script': '[ON SCREEN: Inherited]\nInherited means passed down from your parents. (Point from yourself back over your shoulder.)\n\n[ON SCREEN: Environment]\nEnvironment is where you live and grow. (Spread your arms wide.)\n\nTap each word below me to hear it.'}
S['part2'] = {'label': 'Part 2 · grow the twins (Clue 2)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🌱 Two pots', 'tag': 'PART 2 GAME', 'title': 'Grow the twins', 'col': C_GREEN, 'rows': [['Pot A', 'one seed from the parent'], ['Pot B', 'one seed from the SAME parent'], ['You pick', 'sun or shade, lots of water or a little']]},
    {'label': '🔎 Watch for', 'tag': 'YOUR JOB', 'title': 'What changes? What never changes?', 'col': C_PURP, 'body': 'Height · spread · flowers · flower color · leaf shape'}],
    'script': '(Hold up two fingers.) Two seeds. Same parent.\n\n[ON SCREEN: Two pots]\nIn Grow the twins, you pick the garden for each pot: sun or shade, lots of water or a little. Then press Grow.\n\n[ON SCREEN: Watch for]\nYour job is to notice. Which traits change when the garden changes? And which ones never change, no matter what? Make sure one pot grows in the shade.\n\nPress Listen on the walkie-talkie.'}
S['part3'] = {'label': 'Part 3 · stamp the case (Clue 3)', 'length': '30–40 s', 'want': False, 'parts': [
    {'label': '🗂 Three stamps', 'tag': 'PART 3 GAME', 'title': 'Stamp the case', 'col': C_CASE, 'rows': [['👪', 'INHERITED: from the parents'], ['🌍', 'ENVIRONMENT: from where it lives'], ['⚖️', 'BOTH: a little of each']]}],
    'script': '[ON SCREEN: Three stamps]\nFour Florida cases, three stamps. Read the facts, stamp each one, then pick the fact that proves it. Watch out: two of them need the BOTH stamp.'}
S['explore'] = {'label': 'Part 4 · pass it on? (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'mom', 'label': '🐆 The mother'},
    {'label': '🤔 Guess', 'tag': 'PART 4 GAME', 'title': 'Will the kittens get it?', 'col': C_RED, 'rows': [['〰️', 'A kinked tail'], ['🩹', 'A scar on her nose'], ['👂', 'Round ears'], ['🦌', 'Thin after a hard year']]},
    {'kind': 'photo', 'pic': 'kits', 'label': '🐾 Next generation'}],
    'script': '[ON SCREEN: The mother]\nThis panther mom was caught on a trail camera, carrying her kitten. She just had a litter.\n\n[ON SCREEN: Guess]\nShe has a kinked tail. A scar on her nose. Round ears. And she’s thin after a hard year. (Tap your chin.) Which of those will her kittens get?\n\n[ON SCREEN: Next generation]\nGuess for each trait, then press Next generation. A wrong guess is fine. That’s how scientists learn.\n\nPress Listen on the walkie-talkie.'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '45–55 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'What happened in the two gardens?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Three parts', 'col': C_GREEN, 'rows': [['Part B', 'Two short answers'], ['Part C', 'A parent and its offspring: 3 inherited + 2 environment traits'], ['CER', 'Claim, evidence, reasoning']]}],
    'script': '[ON SCREEN: Crack the case]\nYou made it! First, crack the case at the top. Still locked? Tap “Show me where the clues are.” Pick the answer that fits every clue.\n\n[ON SCREEN: Your case report]\nThen three parts. Part B: two short answers. Part C: pick a real parent and its offspring, maybe your pet or a backyard plant. Name three inherited traits and two from the environment. A sketch is a bonus. Last, your CER.\n\nPress Listen on the walkie-talkie.'}
S['partc'] = {'label': 'Part C · parent and offspring', 'length': '25–35 s', 'want': False, 'parts': [
    {'label': '👪 Your pair', 'tag': 'PART C', 'title': 'A parent and its offspring', 'col': C_GREEN, 'rows': [['🧬', 'Three inherited traits'], ['🌍', 'Two traits from the environment'], ['🔎', 'How you can tell']]}],
    'script': '[ON SCREEN: Your pair]\nPick a real parent and offspring. A dog and her puppy? A mango tree and its seedling? Name three inherited traits and two from the environment, then tell how you can tell the difference.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The quote', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“Offspring are basically clones of their parents. Everything they look like comes from inheritance.”'},
    {'label': '⚖ CER', 'tag': 'REMEMBER CER?', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['C', 'Claim: what you think is true.'], ['E', 'Evidence: facts from the lesson that prove it.'], ['R', 'Reasoning: how the facts prove your claim.']]}],
    'script': '[ON SCREEN: The quote]\nA classmate says babies are clones of their parents. A clone is an exact copy. Hmm.\n\nThink back. Were the two sunflower pots exact copies? Did the kittens look exactly like their mom?\n\n[ON SCREEN: CER]\nPick your side in the planner, tap two pieces of evidence, then write your reasoning in your own words. Try starting with “This shows that…”\n\nPress Listen for Dr. Reyes.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🌻 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'Beach sunflower seed packet', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '➡ Next lesson', 'tag': 'LESSON 13.02', 'title': 'Where do seeds come from?', 'col': C_GREEN, 'body': 'How did one beach sunflower make all those seeds?'}],
    'script': '[ON SCREEN: Confetti]\nCase closed! Same parent, different gardens. The flower color and the leaves came from the parent. The sun did the rest.\n\n[ON SCREEN: Your specimen]\nCheck every box in What to Turn In, and a seed packet goes into your Field Notebook.\n\n[ON SCREEN: Next lesson]\nNext time: how did one flower make all those seeds?\n\nPress Listen for Dr. Reyes’s last word.'}
json.dump({'slots': S, 'pics': pics, 'other': ['lesson', 'part1', 'partb', 'figure']}, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote video.json', len(S), 'slots')
