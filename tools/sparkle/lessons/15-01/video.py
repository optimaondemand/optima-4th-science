#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 15.01."""
import json
pics = {
    's1985': {'src': 'images/15-01-sat-1985.jpg', 'cap': '1985 · from space (USGS, public domain)'},
    's2023': {'src': 'images/15-01-sat-2023.jpg', 'cap': '2023 · from space (USGS, public domain)'},
    'dragline': {'src': 'images/15-01-dragline.jpg', 'cap': 'A dragline near Parrish, Florida (USGS, public domain)'},
    'solar': {'src': 'images/15-01-solar-farm.jpg', 'cap': 'A solar farm at Kennedy Space Center (NASA, public domain)'},
    'gyp': {'src': 'images/15-01-gypstack.jpg', 'cap': 'A fertilizer waste pile in Florida (USGS, public domain)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE = '#B9822A', '#2F7A55', '#7A5BB5', '#C8553D', '#2D7AA6'
S = {}
S['welcome'] = {'label': 'Welcome · the lakes that weren’t there', 'length': '50–60 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 's1985', 'label': '🛰 1985'}, {'kind': 'photo', 'pic': 's2023', 'label': '🛰 2023'},
    {'label': '🗂 The case question', 'tag': 'CASE FILE 15', 'title': 'The Lakes That Weren’t There', 'col': C_CASE, 'body': 'What is making the square lakes, and will the thing being taken ever come back?'}],
    'script': 'Welcome, scientists! New week, new case, and this time we’re looking at Florida from space.\n\n[ON SCREEN: 1985]\nThis is a satellite photo of central Florida from 1985. Mostly green fields and wetlands, with some dark spots.\n\n[ON SCREEN: 2023]\nSame place, 2023. Look! Dark square lakes and bare tan patches in new places. Hmm. Lakes don’t usually come in squares.\n\n[ON SCREEN: The case question]\nWhat is making them? And is something being taken that won’t come back? Find four clues. Press Listen on Dr. Reyes’s walkie-talkie, right below me.'}
S['warmup'] = {'label': 'Warm-Up · take it apart (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '✏️ Take it apart', 'tag': 'WARM-UP GAME', 'title': 'Where did it start?', 'col': C_GREEN, 'rows': [['🌳', 'It grew'], ['☀️', 'Sun, rain or wind'], ['⛏️', 'Dug from the ground'], ['🛢️', 'Pumped from deep underground']]}],
    'script': '(Hold up a pencil.) This pencil used to be part of the Earth. Really!\n\nThe wood grew on a tree. The gray part inside isn’t lead at all. It’s a rock, dug out of the ground.\n\n[ON SCREEN: Take it apart]\nIn the game, take apart a pencil, a juice box and a Florida orange. Drag each part to where it started. Then take apart something near you and write about it.\n\nSave the orange for last. It has a surprise. Press Listen for Dr. Reyes’s hint.'}
S['part2'] = {'label': 'Part 2 · refill race (Clue 2)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '⏳ Refill race', 'tag': 'PART 2 GAME', 'title': 'Does it come back?', 'col': C_BLUE, 'rows': [['1', 'Use them all up.'], ['2', 'Drag time forward to 1 million years.'], ['3', 'Try the water slow and fast.'], ['4', 'Stamp each one.']]},
    {'kind': 'photo', 'pic': 'dragline', 'label': '🏗️ The dragline'}],
    'script': '(Snap your fingers.) If you use something up, does it come back?\n\nRenewable means it comes back fast enough to keep using, like sunlight. Nonrenewable means it takes millions of years to form.\n\n[ON SCREEN: Refill race]\nIn the Refill race, use up five resources, then drag time forward. Watch which bars fill back up. Try the water at both pumping speeds.\n\n[ON SCREEN: The dragline]\nRight after, meet the giant machine that digs up phosphate rock. Tap every number. Press Listen.'}
S['explore'] = {'label': 'Part 4 · two sources (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '📑 Two sources', 'tag': 'PART 4 GAME', 'title': 'Source A and Source B', 'col': C_PURP, 'rows': [['A', 'A mining company’s flyer'], ['B', 'A report by government scientists']]},
    {'kind': 'photo', 'pic': 'gyp', 'label': '⛰️ The waste pile'}],
    'script': '(Hold up two different books.) If I only read one of these, I might miss something.\n\n[ON SCREEN: Two sources]\nDr. Reyes found two sources about the mines. Source A is a mining company’s flyer. Source B is a report by government scientists.\n\n[ON SCREEN: The waste pile]\nThis giant pile is in Source B. Do you think the flyer mentions it?\n\nSort every fact: benefit or cost. Then build a claim that’s fair to both sources. That’s your last clue. Press Listen.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'Square lakes?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Three places to write', 'col': C_GREEN, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Compare two Florida resources'], ['CER', 'Claim, evidence, reasoning'], ['📋', 'Copy your Gathered Answers into Canvas']]}],
    'script': '[ON SCREEN: Crack the case]\nYou have four clues. Crack the case at the top of this tab: what is making those square lakes?\n\n[ON SCREEN: Your case report]\nThen write your case report. Two short answers, a comparison of two Florida resources in Part C, and a CER. Want to draw your chart? That’s a bonus. Stuck? Press Hint under any box. Your answers save as you type. Press Listen.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“All renewable resources are good for the environment and all nonrenewable resources are bad.”'},
    {'kind': 'photo', 'pic': 'solar', 'label': '☀️ The solar farm'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '[ON SCREEN: The claim]\nA classmate says all renewables are good and all nonrenewables are bad. Do you agree?\n\n[ON SCREEN: The solar farm]\nThink about this solar farm. Renewable, yes. But what happened to the land?\n\n[ON SCREEN: The planner]\nRemember CER. Tap your side and two facts from today. Then explain how your facts prove your claim. Try starting with “This shows that…” Press Listen.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🪨 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'Phosphate pebble', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '➡ Next time', 'tag': 'LESSON 15.02', 'title': 'Florida’s resource map', 'col': C_GREEN, 'body': 'Why are some Florida resources found in one place and not another?'}],
    'script': 'Case closed! The square lakes are old phosphate mine pits, and that rock won’t come back.\n\n[ON SCREEN: Your specimen]\nFinish your checklist and a phosphate pebble goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Next time]\nNext time, we’ll read a map of Florida. Why is phosphate only in one part of the state? Press Listen for Dr. Reyes’s last word.'}
S['part3'] = {'label': 'Part 3 · impact check (Clue 3)', 'length': '30–40 s', 'want': False, 'parts': [],
    'script': 'Every resource has an impact, even renewable ones. Open each photo, stamp it renewable or nonrenewable, then pick what using it changes. Look closely at the last photo. Have you seen it before? Press Listen.'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
S['vr'] = {'label': 'VR activity · The island field camp (separate page)', 'length': '45–55 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'solar', 'label': '📷 Power from the sun'},
    {'label': '📋 The supply order', 'tag': 'CASE 15 FOLLOW-UP', 'title': 'Only order what refills!', 'col': C_CASE, 'body': 'Our island camp has to run for 20 years. Diesel, propane and gravel? Or sun, rain and trees?'},
    {'label': '🧭 Two ways', 'tag': 'PICK AT THE TOP', 'title': 'Two ways to do it', 'col': C_BLUE, 'rows': [['🥽', 'VR Field Mission: build the camp in Island Town and say why each piece won’t run out.'], ['🗂', 'No headset? Run the camp for 20 years and see what runs out first.']]},
    {'label': '🥇 The badge', 'tag': 'VR ONLY', 'title': 'Golden Sun badge', 'col': C_PURP, 'body': 'Save your capture in VR to earn it.'}],
    'script': '[ON SCREEN: Power from the sun]\nHi, scientists! Dr. Reyes is opening a Field Station camp on a little island, and it has to keep running for twenty years.\n\n[ON SCREEN: The supply order]\nA volunteer filled out the supply order. Some of it would run out and never come back! Only order what refills.\n\n[ON SCREEN: Two ways]\nPick your way at the top. With a headset, build the camp in Island Town and tell why each piece won’t run out. No headset? Run the camp for twenty years and watch the piles.\n\n[ON SCREEN: The badge]\nFinish in VR to earn the Golden Sun badge!\n\nPress Listen on Dr. Reyes’s walkie-talkie, right below me.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'part1', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
