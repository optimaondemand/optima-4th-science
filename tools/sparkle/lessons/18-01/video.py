#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 18.01 · The Red Water Sample."""
import json
pics = {
    'coast': {'src': 'images/18-01-redtide-coast.jpg', 'cap': 'Red tide along the Florida coast, 2005 (CDC, public domain)'},
    'cell': {'src': 'images/18-01-kbrevis-sem.jpg', 'cap': 'One red tide cell under an electron microscope (FWC, public domain)'},
    'elodea': {'src': 'images/18-01-elodea.jpg', 'cap': 'Water plant cells through a microscope (public domain)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE = '#1F7F86', '#2F7A55', '#7A5BB5', '#C8553D', '#2D7AA6'
S = {}
S['welcome'] = {'label': 'Welcome · meet Sam', 'length': '50–60 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'coast', 'label': '🌊 Strange water'},
    {'label': '🗂 The case question', 'tag': 'CASE FILE 18', 'title': 'The Red Water Sample', 'col': C_CASE, 'body': 'What is hiding in the water at Palmetto Beach, and which tool can find it?'}],
    'script': '(Hold up a clear glass of water.) This looks clean, right? But is it empty? Today we find out.\n\n[ON SCREEN: Strange water]\nThis is a real Florida beach. Look at the color of the water near the shore. Something made it red-brown, and fish are washing up.\n\n[ON SCREEN: The case question]\nWe have a new crew member for this unit: Sam Park, an engineer who builds tools. Sam has a jar of this water. Press Listen to meet Sam, right below me.'}
S['warmup'] = {'label': 'Warm-Up · the beach alert and the zoom machine (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '📻 The beach alert', 'tag': 'WARM-UP', 'title': 'What did people notice?', 'col': C_RED, 'rows': [['🐟', 'Dead fish'], ['🟤', 'Red-brown water'], ['🤧', 'Coughing']]},
    {'kind': 'photo', 'pic': 'cell', 'label': '⚡ The last stop'}],
    'script': '[ON SCREEN: The beach alert]\nFirst, play the beach alert. People noticed three things with their eyes. But could anyone see what caused them?\n\n[ON SCREEN: The last stop]\nThen use Sam’s zoom machine. Each stop is a stronger tool. Here’s a sneak peek of the last stop. What do you think this is? Press Listen for Sam’s tip.'}
S['part1'] = {'label': 'Part 1 · how small can each tool go? (Clue 2)', 'length': '30–40 s', 'want': False, 'parts': [
    {'label': '🪜 Four tools', 'tag': 'PART 1 GAME', 'title': 'The weakest tool that works', 'col': C_BLUE, 'rows': [['👁️', 'Your eyes'], ['🔍', 'Hand lens'], ['🔬', 'Light microscope'], ['⚡', 'Electron microscope']]}],
    'script': '[ON SCREEN: Four tools]\nScientists start simple. If your eyes can do the job, you don’t need a microscope. Sort each card onto the weakest tool that shows it clearly. Press Listen.'}
S['part3'] = {'label': 'Part 3 · pick the right tool (Clue 3)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🧪 Four lab requests', 'tag': 'PART 3 GAME', 'title': 'Which tool fits the question?', 'col': C_PURP, 'body': 'Count living cells? See one cell’s surface? Look at a wing at a picnic?'},
    {'label': '⚡ The catch', 'tag': 'WHY IT MATTERS', 'title': 'The strongest tool can’t do every job', 'col': C_RED, 'body': 'An electron microscope needs a dried sample. Nothing on it can be alive.'}],
    'script': '(Hold up something big, like a backpack, and pretend to look at it through a tiny tube.) Is the strongest tool always the best? Hmm.\n\n[ON SCREEN: Four lab requests]\nSam’s lab got four requests. Read each one and think: what does the question ask you to DO?\n\n[ON SCREEN: The catch]\nHere’s the catch: the electron microscope sees the most, but it can’t look at anything alive. Press Listen.'}
S['explore'] = {'label': 'Part 4 · count the cells (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🔬 Sam’s microscope', 'tag': 'PART 4 GAME', 'title': 'Slide, lens, focus, count', 'col': C_GREEN, 'rows': [['1', 'Put the slide on'], ['2', 'Turn to the 40x lens'], ['3', 'Focus slowly'], ['4', 'Count the cells in the square']]},
    {'label': '📋 The lab report', 'tag': 'THEN', 'title': 'Match the real FWC chart', 'col': C_CASE, 'body': 'Florida scientists use this chart to warn people at the beach.'}],
    'script': '[ON SCREEN: Sam’s microscope]\nTime to use a real scientist’s routine. Slide on, strongest lens, then turn the focus knob slowly. Watch the cells get sharp. Count only the ones inside the square.\n\n[ON SCREEN: The lab report]\nThen fill in Sam’s lab report and find your number on the real chart. How bad is the red tide? Press Listen.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'What is in the water?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Three places to write', 'col': C_GREEN, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Three views of one small thing'], ['CER', 'Claim, evidence, reasoning'], ['📋', 'Copy your Gathered Answers into Canvas']]}],
    'script': '[ON SCREEN: Crack the case]\nYou have four clues. Crack the case at the top of this tab.\n\n[ON SCREEN: Your case report]\nThen write your case report: two short answers, three views of one small thing for Part C, and your CER. Pick something you can really find, like a leaf or a grain of sand. Stuck? Press Hint under any box. Press Listen.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“You should always use the most powerful tool you can find. The more magnification, the better.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '[ON SCREEN: The claim]\nA classmate says the most powerful tool is always best. Would you bring an electron microscope to a picnic to look at a bee? Could it count living red tide cells?\n\nThere’s no wrong side, as long as you prove it.\n\n[ON SCREEN: The planner]\nTap your side and two facts. Then explain how your facts prove your claim. Try starting with “This shows that…” Press Listen.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🧫 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'Red tide sample slide', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '➡ Next time', 'tag': 'LESSON 18.02', 'title': 'Tools for things far away', 'col': C_BLUE, 'body': 'Telescopes: how do we see the Moon and the planets up close?'}],
    'script': 'Case closed! You found red tide hiding in the water, and you picked the right tool for every job.\n\n[ON SCREEN: Your specimen]\nFinish your checklist, and Sam’s red tide slide goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Next time]\nNext time we flip it around: tools for things that are really far away. Press Listen for Sam’s last word.'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'part2', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
