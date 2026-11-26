#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 27.01 · The Trophy Twins (Case 27, Dr. Priya Nair).
Scripts only era (week 25 on): no crew clips generated yet, so no script says "Press Listen"."""
import json
pics = {
    'coquina': {'src': 'images/27-01-limestone-coquina.jpg', 'cap': 'Coquina limestone at the Castillo de San Marcos (Kiran891, CC BY-SA 4.0)'},
    'sphere': {'src': 'images/27-01-kg-sphere.jpg', 'cap': 'A nearly perfect silicon kilogram sphere (CSIRO, CC BY 3.0)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE, C_GOLD = '#7A5BB5', '#2F7A55', '#5A3B92', '#C8553D', '#2D7AA6', '#B8860B'
S = {}
S['welcome'] = {'label': 'Welcome · The Trophy Twins', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🏆 The missing trophy', 'tag': 'CASE 27', 'title': 'Two trophies, one real', 'col': C_GOLD, 'body': 'The Derby trophy vanished. Two look-alikes turned up at the lost-and-found.'},
    {'label': '❓ The question', 'tag': 'THE PROBLEM', 'title': 'Which one is real brass?', 'col': C_RED, 'body': 'No one is allowed to cut them open.'},
    {'label': '🧪 Dr. Nair’s plan', 'tag': 'THE SCIENCE', 'title': 'Describe, then MEASURE', 'col': C_CASE, 'body': 'Matter has mass and takes up space. Properties tell objects apart.'}],
    'script': '(Hold up two matching cups or two matching spoons.) Twins! Could you tell which one is which with just your eyes?\n\n[ON SCREEN: The missing trophy]\nThe Duck Derby trophy vanished, and TWO matching trophies turned up at the Palmetto Springs lost-and-found.\n\n[ON SCREEN: The question]\nOne is real brass. One is painted plastic. Nobody may cut them open.\n\n[ON SCREEN: Dr. Nair’s plan]\nDr. Nair says eyes can tie, but measurements don’t. Read her case file just below me.'}
S['warmup'] = {'label': 'Warm-Up · the bottle that fights back (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🧴 The squeeze test', 'tag': 'WARM-UP GAME', 'title': 'The bottle fights back', 'col': C_BLUE, 'rows': [['🔴', 'Cap ON: drag down and squeeze'], ['⚪', 'Cap OFF: squeeze again'], ['📋', 'Your squeeze log fills in']]},
    {'label': '🤔 Think about it', 'tag': 'THE MYSTERY', 'title': 'What pushed back?', 'col': C_CASE, 'body': 'The bottle looked empty…'}],
    'script': '(Hold up an empty plastic bottle, cap on tight, and try to crush it.) It fights back! (Uncap it and crush it flat.) Now it gives right up.\n\n[ON SCREEN: The squeeze test]\nTry it on the page. Cap on: drag down on the bottle. Cap off: squeeze again. Your squeeze log fills in.\n\n[ON SCREEN: Think about it]\nThe bottle looked empty. So what pushed back? Answer, and Clue one is yours.'}
S['part1'] = {'label': 'Part 1 · the matter gates (Clue 2)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🚪 The matter gates', 'tag': 'PART 1 GAME', 'title': 'Two tests, two gates', 'col': C_PURP, 'rows': [['1️⃣', 'Gate 1: does it have mass?'], ['2️⃣', 'Gate 2: does it take up space?'], ['✅', 'Pass both: MATTER'], ['⛔', 'Fail one: NOT MATTER']]},
    {'label': '🌑 The tricky ones', 'tag': 'WATCH OUT', 'title': 'A shadow and a bell’s ring', 'col': C_RED, 'body': 'Test them. Don’t guess.'}],
    'script': '(Point at your own shadow on the wall.) Is my shadow STUFF? Hmm. We don’t guess in the Field Station. We test.\n\n[ON SCREEN: The matter gates]\nSend a rock, water, air, a shadow and a bell’s ring through the machine. Gate one: does it have mass? Gate two: does it take up space? Pick the proof at each gate.\n\n[ON SCREEN: The tricky ones]\nThe shadow and the ring might surprise you. Then stay for a wow: we weigh AIR.'}
S['part2'] = {'label': 'Part 2 · tell the twins apart (Clue 3)', 'length': '35–45 s', 'want': False, 'parts': [
    {'label': '🫙 The twin jars', 'tag': 'PART 2 GAME', 'title': 'Four tools, one tie-breaker', 'col': C_GOLD, 'rows': [['👀', 'Look: tie'], ['✋', 'Feel: tie'], ['📏', 'Ruler: tie'], ['⚖️', 'Balance: …?']]}],
    'script': '(Hold up the two matching cups again, one in each hand, and move them up and down like a balance.) Eyes say they match. My hands aren’t sure…\n\n[ON SCREEN: The twin jars]\nDr. Nair keeps twin practice jars. Try all four tools on them. Looking, feeling, even the ruler can tie. Watch which tool finally breaks the tie, and which KIND of property it measures.'}
S['explore'] = {'label': 'Part 3 · the weigh and dunk test (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '⚖️ Weigh it', 'tag': 'PART 3 GAME', 'title': 'Read the balance', 'col': C_GREEN, 'rows': [['🏆', 'Put each trophy on the balance'], ['🔢', 'Read the screen']]},
    {'label': '💧 Dunk it', 'tag': 'THEN', 'title': 'Read the water line', 'col': C_BLUE, 'rows': [['👇', 'Hold it under with the rod'], ['📈', 'How far did the water climb?']]}],
    'script': '(Pretend to lower something gently into a fish tank.) When a thing goes under, the water has to move over. The water line climbs exactly as much space as the thing takes up!\n\n[ON SCREEN: Weigh it]\nPut each trophy on the balance and read its mass.\n\n[ON SCREEN: Dunk it]\nThen hold each one under the water and read the climb. Fill both property cards. Same space, different mass. That’s Clue four, the big one.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'Which trophy is real?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues. Then the engraver’s sealed note opens.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO DO', 'title': 'Three places to work', 'col': C_GOLD, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Property cards for two home objects'], ['CER', 'Claim, evidence, reasoning']]}],
    'script': '[ON SCREEN: Crack the case]\nFour clues, two trophies, one answer. Pick the one that fits every clue, and the engraver’s sealed note opens to check your work.\n\n[ON SCREEN: Your case report]\nThen two short answers. For Part C, pick two look-alike objects at home and make a property card for each. Then sketch and label it. Last comes your CER about air.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“Air doesn’t take up space because you can’t see it.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '(Hold up the capped bottle one more time and squeeze.) Remember what pushed back?\n\n[ON SCREEN: The claim]\nA classmate says air takes up no space because you can’t see it. You tested that twice today: the bottle, and the balloon on the scale.\n\n[ON SCREEN: The planner]\nTap your side and two facts. Then explain how they prove your claim. Try starting with “This shows that…”'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🏆 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'The derby trophy', 'col': C_GOLD, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '➡ Next lesson', 'tag': 'LESSON 27.02', 'title': 'Classify by properties', 'col': C_BLUE, 'body': 'Sort materials and pick the right one for a job.'}],
    'script': '(Hold an invisible trophy high, then set it down proudly.) The winner finally gets the REAL trophy, thanks to you.\n\n[ON SCREEN: Your specimen]\nFinish your checklist, and the derby trophy goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Next lesson]\nNext time: you’ll use properties to sort materials, and to pick the right one for a job.'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
