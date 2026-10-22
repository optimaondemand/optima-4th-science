#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 17.02 · The House That Stood."""
import json
pics = {
    'raised': {'src': 'images/17-02-raised-houses.jpg', 'cap': 'Mexico Beach, four days after Hurricane Michael (VOA, public domain)'},
    'flyafter': {'src': 'images/17-01-mexico-after.jpg', 'cap': 'Mexico Beach the day after Hurricane Michael (NOAA, public domain)'},
    'shutters': {'src': 'images/17-02-mit-shutters.jpg', 'cap': 'Storm shutters, Vero Beach (FEMA, public domain)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE = '#B9822A', '#2F7A55', '#7A5BB5', '#C8553D', '#2D7AA6'
S = {}
S['welcome'] = {'label': 'Welcome · the house that stood', 'length': '50–60 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'flyafter', 'label': '🛩️ Some houses stood'},
    {'label': '🗂 The case question', 'tag': 'CASE FILE 17 · PART 2', 'title': 'The House That Stood', 'col': C_CASE, 'body': 'How should the Riveras rebuild so their house stands up to the next storm?'}],
    'script': '[ON SCREEN: Some houses stood]\nRemember this photo from Storm Night? Most houses in Mexico Beach were gone. But look closely: a few were still standing. Why?\n\n[ON SCREEN: The case question]\nToday the Rivera family in Palmetto Springs has to rebuild their house on Bay Street. They want it to stand up to the next storm. You’re going to help them design it and test it. Press Listen to hear from June, right below me.'}
S['warmup'] = {'label': 'Warm-Up · what helped, what failed? (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'raised', 'label': '📷 A real street'}],
    'script': '(Hold up a piece of cardboard over a window, or over your face like a shield.) Before a storm, Florida families cover their windows. Why do you think they do that?\n\n[ON SCREEN: A real street]\nThis is a real street in Mexico Beach, four days after the storm. Tap each number and read what happened there. Then match the clues. Look closely: where did the storm hit hardest? Press Listen for June’s tip.'}
S['part2'] = {'label': 'Part 2 · build it, then storm it (Clue 3)', 'length': '45–55 s', 'want': True, 'parts': [
    {'label': '🏗️ Build it, then storm it', 'tag': 'PART 2 GAME', 'title': 'Three choices, one budget', 'col': C_BLUE, 'rows': [['🏗️', 'Foundation'], ['🪟', 'Windows'], ['🔩', 'Roof'], ['💰', '7 coins']]},
    {'label': '🔁 Revise', 'tag': 'IF A TEST FAILS', 'title': 'Change one part, run it again', 'col': C_GREEN, 'body': 'Every engineer’s first design fails something. That’s how designs get better.'}],
    'script': '(Pretend to blow hard on a paper house or a tissue.) Wind pushes. Water pushes. A house has to push back.\n\n[ON SCREEN: Build it, then storm it]\nPick a foundation, windows and a roof for the Riveras. But you only have seven coins. Then press Run the storm.\n\n[ON SCREEN: Revise]\nIf a test fails, that’s okay! Change one part and run it again. That’s called revising. Press Listen.'}
S['explore'] = {'label': 'Part 4 · fix the whole town (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🗺️ Fix the whole town', 'tag': 'PART 4 GAME', 'title': 'One fix for each problem', 'col': C_PURP, 'rows': [['🧱', 'Built'], ['🌿', 'Natural'], ['📋', 'Planning']]}],
    'script': 'The Riveras have their plan. But a lot more broke on Storm Night. Remember the branch on Pine Avenue? The flooded street?\n\n[ON SCREEN: Fix the whole town]\nTap each problem on the map. Pick the fix that would help most. Then stamp it: built, natural or planning. When you finish, think about this: could one fix ever solve every problem? Press Listen.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'How should the Riveras rebuild?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Three places to write', 'col': C_GREEN, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Design a mitigation plan'], ['CER', 'Claim, evidence, reasoning'], ['📋', 'Copy your Gathered Answers into Canvas']]}],
    'script': '[ON SCREEN: Crack the case]\nYou have four clues. Crack the case at the top of this tab: how should the Riveras rebuild?\n\n[ON SCREEN: Your case report]\nThen write your case report: two short answers, a mitigation plan for any Florida hazard in Part C, and a CER. Want to sketch your decision matrix? That’s a bonus. Stuck? Press Hint under any box. Press Listen.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“The only way to protect a town from a hurricane is to build the tallest, strongest wall you can.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '[ON SCREEN: The claim]\nA classmate says the tallest, strongest wall is the only way to protect a town. Hmm. Would a wall stop a branch from falling on Pine Avenue?\n\nThere’s no wrong side, as long as you prove it.\n\n[ON SCREEN: The planner]\nRemember CER. Tap your side and two facts from today. Then explain how your facts prove your claim. Try starting with “This shows that…” Press Listen.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🔩 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'Hurricane strap', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '➡ Next time', 'tag': 'REVIEW DAY 17.R1', 'title': 'The Hole on Main Street', 'col': C_GREEN, 'body': 'A hole opens on Main Street after the storm. Did the hurricane do it?'}],
    'script': 'Case closed! You helped the Riveras build a house that passed every storm test, and you made a plan for the whole town.\n\n[ON SCREEN: Your specimen]\nFinish your checklist, and a hurricane strap goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Next time]\nNext time is review day, and there’s a new mystery: a hole opens up on Main Street. Did the storm do it? Press Listen for June’s last word.'}
S['part1'] = {'label': 'Part 1 · three kinds of mitigation (Clue 2)', 'length': '30–40 s', 'want': False, 'parts': [
    {'kind': 'photo', 'pic': 'shutters', 'label': '🧱 Built'}],
    'script': '[ON SCREEN: Built]\nShutters like these are built mitigation. People make them and hang them. Now drag each photo onto its shelf: built, natural or planning. Press Listen.'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'part3', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
