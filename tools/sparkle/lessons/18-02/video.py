#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 18.02 · The Star Party Wish List."""
import json
pics = {
    'saturn': {'src': 'images/18-02-saturn.jpg', 'cap': 'Saturn, Hubble Space Telescope, 2018 (NASA, public domain)'},
    'deep': {'src': 'images/18-02-deepfield.jpg', 'cap': 'Webb’s First Deep Field (NASA, ESA, CSA, STScI, public domain)'},
    'andromeda': {'src': 'images/18-02-andromeda.jpg', 'cap': 'The Andromeda Galaxy (Andy Weeks, CC0)'},
    'flnight': {'src': 'images/18-02-florida-night.jpg', 'cap': 'Florida at night from the International Space Station (NASA, public domain)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE = '#1F7F86', '#2F7A55', '#7A5BB5', '#C8553D', '#2D7AA6'
S = {}
S['welcome'] = {'label': 'Welcome · the star party', 'length': '45–55 s', 'want': True, 'parts': [
    {'label': '🌕 Four wishes', 'tag': 'CASE FILE 18, PART 2', 'title': 'The Star Party Wish List', 'col': C_CASE, 'rows': [['🌕', 'Maya: Moon craters'], ['🪐', 'Leo: Saturn’s rings'], ['✨', 'Ava: the Seven Sisters'], ['🚀', 'Jordan: the farthest thing ever']]},
    {'label': '🔎 The case question', 'tag': 'ONE TOOL TO RENT', 'title': 'What should Sam bring?', 'col': C_RED, 'body': 'The town can rent ONE tool. Can every wish come true?'}],
    'script': '(Look up, like you’re searching the night sky.) Have you ever made a wish on a star? Today four kids made wishes about the stars.\n\n[ON SCREEN: Four wishes]\nThe red tide is gone, and Palmetto Beach is throwing a star party. Read these four wish cards. Which one sounds hardest to you?\n\n[ON SCREEN: The case question]\nThe town can rent just one tool. Press Listen on Sam’s walkie-talkie, right below me.'}
S['warmup'] = {'label': 'Warm-Up · race the light (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'TRUE OR FALSE?', 'title': 'Starlight is older than you', 'col': C_PURP, 'body': 'The starlight you see tonight left its star before you were born.'},
    {'kind': 'photo', 'pic': 'andromeda', 'label': '🌌 The farthest one'}],
    'script': '[ON SCREEN: The claim]\nHere’s a claim: the starlight you see tonight is older than you. Thumbs up if you think that’s true. Thumbs down if it’s false.\n\n[ON SCREEN: The farthest one]\nThis is the Andromeda Galaxy. You can see it from a dark place in Florida as a faint fuzzy patch. How long ago do you think its light left? Make your guesses, then send the light. Press Listen.'}
S['part1'] = {'label': 'Part 1 · open wider (Clue 2)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '⭕ Your light catcher', 'tag': 'PART 1 GAME', 'title': 'Open wider', 'col': C_BLUE, 'rows': [['👁️', 'Your eye: about 7 mm'], ['🦉', 'An owl'], ['🔭', 'Binoculars: 50 mm'], ['🪞', 'Telescope: about 200 mm']]},
    {'label': '🔍 The trick button', 'tag': 'TRY THIS', 'title': 'Zoom only', 'col': C_RED, 'body': 'Does zooming in show any NEW stars?'}],
    'script': '(Make a tiny circle with your finger and thumb, then a big circle with both hands.) Which one would catch more rain? Light works the same way.\n\n[ON SCREEN: Your light catcher]\nDrag the gold dot to open the opening wider, and count the stars.\n\n[ON SCREEN: The trick button]\nThen try Zoom only. Watch closely. Did you get any new stars? Press Listen.'}
S['part2'] = {'label': 'Part 2 · find it in the sky (Clue 3)', 'length': '30–40 s', 'want': False, 'parts': [
    {'kind': 'photo', 'pic': 'saturn', 'label': '🪐 Leo’s wish'}],
    'script': '[ON SCREEN: Leo’s wish]\nThis is what Leo wants to see. Aim each tool at Saturn and the other wishes. Which tool shows the rings? Which one fits the whole star cluster? Press Listen.'}
S['explore'] = {'label': 'Part 4 · stare at nothing (Clue 4)', 'length': '45–55 s', 'want': True, 'parts': [
    {'label': '⬛ An empty speck', 'tag': 'PART 4 GAME', 'title': 'A grain of sand at arm’s length', 'col': C_GREEN, 'body': 'Hold a grain of sand out at arm’s length. That’s how much sky Webb stared at.'},
    {'kind': 'photo', 'pic': 'deep', 'label': '🌌 After 12.5 hours'}],
    'script': '(Pinch your fingers like you’re holding a grain of sand, and hold your arm out.) This tiny! That’s how much sky we’re about to look at.\n\n[ON SCREEN: An empty speck]\nTo your eyes it looks empty. Try binoculars and the telescope too.\n\n[ON SCREEN: After 12.5 hours]\nHere’s a sneak peek. Then press and hold Webb’s shutter until all 12 and a half hours pass. Press Listen.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'What should Sam bring?', 'col': C_CASE, 'body': 'Pick the plan that fits all four clues.'},
    {'kind': 'photo', 'pic': 'flnight', 'label': '🗺️ The permit map'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Three places to write', 'col': C_GREEN, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Three views of one far-away thing'], ['CER', 'Claim, evidence, reasoning']]}],
    'script': '[ON SCREEN: Crack the case]\nYou have four clues. Crack the case at the top of this tab.\n\n[ON SCREEN: The permit map]\nThen Sam’s permit opens. This is Florida at night, from space. Where would the stars be easiest to see?\n\n[ON SCREEN: Your case report]\nThen write your case report: two short answers, three views for Part C, and your CER. Press Listen.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“We don’t need telescopes in space. Just build them taller on Earth.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '[ON SCREEN: The claim]\nA classmate says we can skip space telescopes. Just build them taller! Hmm. Would a taller telescope get above the air? Did zooming in show new stars?\n\nThere’s no wrong side, as long as you prove it.\n\n[ON SCREEN: The planner]\nTap your side and two facts, then explain how they prove your claim. Try starting with “This shows that…” Press Listen.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🎟️ Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'Star party ticket', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '➡ Next week', 'tag': 'LESSON 19.01', 'title': 'Motion and energy', 'col': C_BLUE, 'body': 'How does energy make things move?'}],
    'script': 'Case closed! Every kid gets their wish, because you matched each wish to the right tool.\n\n[ON SCREEN: Your specimen]\nFinish your checklist, and your star party ticket goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Next week]\nNext week Sam’s tools get a new job: energy and motion. Press Listen for Sam’s last word.'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'part3', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
