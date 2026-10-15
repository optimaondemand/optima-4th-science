#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 11.01."""
import json
pics = {
    'beak': {'src': 'images/11-01-case-beak.jpg', 'cap': 'pg. 3 · the beak · flat and wide at the tip'},
    'sweep': {'src': 'images/11-01-case-sweep.jpg', 'cap': 'pg. 4 · beak in the water'},
    'legs': {'src': 'images/11-01-case-legs.jpg', 'cap': 'pg. 5 · the legs'},
    'lagoon': {'src': 'images/11-01-case-flock.jpg', 'cap': 'pg. 6 · where I found it'},
    'gator': {'src': 'images/11-01-gator-hiding.jpg', 'cap': 'An American alligator hiding (CC BY-SA 3.0)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE = '#B9822A', '#2F7A55', '#7A5BB5', '#C8553D', '#2B7BB9'
S = {}
S['welcome'] = {'label': 'Welcome · the washed-out notebook', 'length': '50–60 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'beak', 'label': '📷 The beak'},
    {'kind': 'photo', 'pic': 'sweep', 'label': '📷 Beak in the water'},
    {'kind': 'photo', 'pic': 'legs', 'label': '📷 The legs'},
    {'kind': 'photo', 'pic': 'lagoon', 'label': '📷 Where I found it'},
    {'label': '🗂 The case question', 'tag': 'CASE FILE 11', 'title': 'The Washed-Out Notebook', 'col': C_CASE, 'body': 'How does this bird find food it can’t even see?'},
    {'label': '🧭 Your clue bar', 'tag': 'HOW TO SOLVE IT', 'title': 'Find 4 clues', 'col': C_GREEN, 'rows': [['🗂 My clues', 'The bar under the tabs. Tap it to see your clues.'], ['? ? ? ?', 'Each game you finish fills in a clue.'], ['🔒', 'Crack the case at the top of the Assignment.']]}],
    'script': 'Hi, scientists! Today’s case starts with a soggy notebook.\n\n(Hold up a notebook.) Dr. Reyes found one like this on a boardwalk, soaked by the rain. Only four photos survived.\n\n[ON SCREEN: The beak · Beak in the water]\nLook at that beak. It’s flat, like a spoon!\n\n[ON SCREEN: The legs · Where I found it]\nLong pink legs, standing in shallow water.\n\n[ON SCREEN: The case question]\nThe last line is washed out. This bird finds food it can’t even see… how?\n\n[ON SCREEN: Your clue bar]\nEvery game you finish adds a clue. Press Listen on Dr. Reyes’s walkie-talkie, right below me.'}
S['warmup'] = {'label': 'Warm-Up · beak or tool (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🔧 Four tools', 'tag': 'WARM-UP GAME', 'title': 'Beak or tool?', 'col': C_GREEN, 'rows': [['🥄', 'Spoon'], ['🥤', 'Straw'], ['🗜️', 'Nutcracker'], ['🍢', 'Skewer (a sharp stick)']]},
    {'label': '👆 How to match', 'tag': 'HOW TO PLAY', 'title': 'Drag or tap', 'col': C_GREEN, 'rows': [['1', 'Look at the shape of each beak.'], ['2', 'Drag a tool onto it, or tap the tool, then the beak.'], ['3', 'Match all four, then write your best guess.']]}],
    'script': '(Hold up a spoon and a straw.) Which one would you use to scoop soup? Which one to sip a drink? The shape tells you the job!\n\n[ON SCREEN: Four tools]\nBird beaks work the same way. Here are four tools.\n\n[ON SCREEN: How to match]\nLook at each beak’s shape. Drag the tool with the same shape onto it, or tap the tool and then the beak. Then write your best guess: why is a flat beak good for sweeping?\n\nPress Listen. Dr. Reyes has a tip for you.'}
S['part2'] = {'label': 'Part 2 · inside or outside (Clue 2)', 'length': '30–40 s', 'want': False, 'parts': [
    {'label': '🫀 Two sides', 'tag': 'PART 2 GAME', 'title': 'Inside or outside?', 'col': C_PURP, 'rows': [['👀', 'External: you can see it from outside.'], ['🫀', 'Internal: hidden inside the body.']]}],
    'script': '(Point to your skin, then to your heart.) My skin is external. I can see it. My heart is internal. It’s hidden inside.\n\n[ON SCREEN: Two sides]\nSort each card. Ask: could I see this part from the outside? Watch the last card. It’s a clue! Press Listen on the walkie-talkie.'}
S['part3'] = {'label': 'Part 3 · how deep can you go (Clue 3)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '💧 Four depths', 'tag': 'PART 3 GAME', 'title': 'How deep can you go?', 'col': C_BLUE, 'rows': [['💧', '1 inch'], ['💧', '6 inches'], ['💧', '1 foot'], ['💧', '3 feet']]},
    {'label': '🦵 Three birds', 'tag': 'WHO CAN STAND?', 'title': 'Watch all three', 'col': C_GREEN, 'rows': [['Sanderling', 'Short legs'], ['Roseate spoonbill', 'Long legs'], ['Mottled duck', 'Short legs, webbed feet']]}],
    'script': '(Hold a ruler up to your leg.) If I stood in water this deep, my knees would stay dry. Up to here? I’d be swimming!\n\n[ON SCREEN: Four depths]\nTap a water depth and watch the water rise.\n\n[ON SCREEN: Three birds]\nThree birds, three kinds of legs. Who can still stand and feed? Try every depth, then answer the question.\n\nPress Listen on Dr. Reyes’s walkie-talkie first.'}
S['explore'] = {'label': 'Part 4 · build a hiding head (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'gator', 'label': '📷 A gator hiding'},
    {'label': '🧪 Build and test', 'tag': 'PART 4 GAME', 'title': 'Build a hiding head', 'col': C_GREEN, 'rows': [['1', 'Pick where the eyes and nostrils go.'], ['2', 'Press Sink it to hide.'], ['3', 'Read the three tests. Try another design.']]}],
    'script': '(Cover your mouth and nose with your hand.) Can you breathe? Not easily!\n\n[ON SCREEN: A gator hiding]\nNow look at this alligator. Its whole body is hiding underwater. What’s still sticking out?\n\n[ON SCREEN: Build and test]\nBuild a model head. Put the eyes and nostrils where you want, then sink it. Can it watch? Can it breathe? Test at least two designs. That’s your last clue!\n\nPress Listen on the walkie-talkie.'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '45–55 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'How does it find food?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Four places to write', 'col': C_GREEN, 'rows': [['Part B', 'Two short answers'], ['Part C', 'A Florida plant or animal and three structures'], ['CER', 'Claim, evidence, reasoning'], ['📋', 'Copy your Gathered Answers into Canvas']]},
    {'label': '🛟 Help buttons', 'tag': 'STUCK?', 'title': 'Help under every box', 'col': C_PURP, 'rows': [['Your answer needs', 'Chips light up as you write.'], ['Hint', 'Three hints, one at a time.']]}],
    'script': '[ON SCREEN: Crack the case]\nYou found all four clues! At the top of this tab, crack the case: how does the mystery bird find food it can’t see?\n\n[ON SCREEN: Your case report]\nThen write your case report: two short answers, a Florida plant or animal with three of its structures, and a CER.\n\n[ON SCREEN: Help buttons]\nWatch the chips light up as you write. Stuck? Press Hint. Your answers save as you type.\n\nPress Listen on the walkie-talkie.'}
S['partc'] = {'label': 'Part C · label a Florida organism', 'length': '25–35 s', 'want': False, 'parts': [
    {'label': '🐾 Your pick', 'tag': 'PART C', 'title': 'Pick a Florida plant or animal', 'col': C_GREEN, 'rows': [['🐢', 'A gopher tortoise'], ['🦭', 'A manatee'], ['🌴', 'A cabbage palm'], ['🐸', 'A tree frog']]}],
    'script': '[ON SCREEN: Your pick]\nNow it’s your turn. Pick a Florida plant or animal, but not the spoonbill. Name three of its structures, the job of each one, and whether it’s internal or external. Want to draw it? The sketch pad is a bonus.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The quote', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“Plants don’t really have structures — they’re just leaves and stems. Only animals have body parts that matter.”'},
    {'label': '⚖ CER', 'tag': 'REMEMBER CER?', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['C', 'Claim: what you think is true.'], ['E', 'Evidence: facts from the lesson that prove it.'], ['R', 'Reasoning: how the facts prove your claim.']]},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Tap to plan', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'They drop into your C and E boxes. You write the R.']]}],
    'script': '[ON SCREEN: The quote]\nA classmate says plants don’t really have structures. Only animals have body parts that matter. Hmm!\n\n(Hold up a leaf or a plant.) What does this leaf do? What about the roots underneath?\n\n[ON SCREEN: CER]\nRemember CER? Claim, evidence, reasoning.\n\n[ON SCREEN: The planner]\nTap your side, tap two pieces of evidence, then write your reasoning in your own words.\n\nPress Listen for Dr. Reyes.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🪶 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'Roseate spoonbill feather', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '➡ Next time', 'tag': 'LESSON 11.02', 'title': 'Build a model', 'col': C_GREEN, 'body': 'A drawing that explains how a body part does its job.'}],
    'script': 'Case closed! The spoonbill finds food by feeling, not seeing. Every part fits its job.\n\n[ON SCREEN: Your specimen]\nFinish your checklist and a pink spoonbill feather goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Next time]\nNext time, you’ll build a model, a drawing that explains how a body part does its job. Bring your clues!\n\nPress Listen for Dr. Reyes’s last word.'}
json.dump({'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'part1', 'partb']}, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote video.json', len(S), 'slots')
