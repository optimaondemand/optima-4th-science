#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 24.01 · The Cold Cocoa Cart (Case 24)."""
import json
pics = {
    'parade': {'src': 'images/24-01-boat-parade.jpg', 'cap': 'A lighted boat parade at John’s Pass, Madeira Beach, Florida (Richard Mc Neil, CC BY 3.0)'},
    'bench': {'src': 'images/24-01-bench.jpg', 'cap': 'A wood and iron bench (Acabashi, CC BY-SA 4.0)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE, C_GOLD = '#1F7F86', '#2F7A55', '#7A5BB5', '#C8553D', '#2D7AA6', '#B8860B'
S = {}
S['welcome'] = {'label': 'Welcome · the cold cocoa cart', 'length': '40–50 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'parade', 'label': '🎆 The boat parade'},
    {'label': '☕ The menu', 'tag': 'CASE 24', 'title': 'Rosa’s Cocoa Cart', 'col': C_RED, 'rows': [['🥫', 'New shiny metal mugs'], ['🥶', 'Cocoa goes cold'], ['🔥', 'Handles get hot']]},
    {'label': '🌡️ Today', 'tag': 'TODAY', 'title': 'How does heat move?', 'col': C_GREEN, 'body': 'Warm to cool, and which materials carry it fast or slow it down.'}],
    'script': '(Wrap both hands around a warm mug.) Mmm. Where is this warmth going?\n\n[ON SCREEN: The boat parade]\nIn Florida, December brings lighted boat parades. Rosa sells hot cocoa at the one in Palmetto Beach.\n\n[ON SCREEN: The menu]\nThis year she switched to shiny metal mugs. Now the cocoa goes cold, and the handles get hot!\n\n[ON SCREEN: Today]\nToday you help Sam find out why. Read the menu and the order slips just below me.'}
S['warmup'] = {'label': 'Warm-Up · three spoons in a mug (Clue 1)', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🥄 Three spoons', 'tag': 'WARM-UP GAME', 'title': 'Which handle gets warm?', 'col': C_PURP, 'rows': [['🤔', 'Guess first'], ['⏱', 'Wait 1 minute'], ['👆', 'Touch every spot']]}],
    'script': '(Hold up a metal spoon and a wooden spoon.) Two spoons. One cup of hot cocoa. Which handle would you rather hold?\n\n[ON SCREEN: Three spoons]\nGuess first. Then wait one minute and touch the spots up each handle. Watch your heat map fill in. If you have both spoons at home, try it for real with an adult and a warm drink. Press Listen on Sam’s walkie-talkie, right below me.'}
S['part1'] = {'label': 'Part 1 · be the heat (Clue 2)', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🔴 Be the heat', 'tag': 'PART 1 GAME', 'title': 'Which way does heat go?', 'col': C_RED, 'rows': [['✋', 'Warm hand'], ['🧊', 'Ice cube'], ['❄️', 'Try “Send cold”']]}],
    'script': '(Hold an ice cube, or pretend to.) Brrr! Is the ice putting cold INTO my hand? Or is my hand losing something?\n\n[ON SCREEN: Be the heat]\nYou be the heat. Drag the red dots and see which way they can go. Then try the Send cold button. Does it work? Press Listen.'}
S['part2'] = {'label': 'Part 2 · the butter rod race (Clue 3)', 'length': '30–40 s', 'want': False, 'parts': [
    {'label': '🧈 The rod race', 'tag': 'PART 2 GAME', 'title': 'Which rod carries heat fastest?', 'col': C_GOLD, 'rows': [['1️⃣', 'Pick 3 rods'], ['🥇', 'Predict the order'], ['🔥', 'Heat the ends']]}],
    'script': '(Hold up a pencil like a rod and point to one end.) Heat goes in here. How fast does it get to the other end?\n\n[ON SCREEN: The rod race]\nPick three rods, predict which butter dot falls off first, then heat the ends. Race a metal rod against one that isn’t metal.'}
S['explore'] = {'label': 'Part 3 · the Cup Race (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🥤 The Cup Race', 'tag': 'PART 3 GAME', 'title': 'Which cup keeps water warm?', 'col': C_BLUE, 'rows': [['🥫', 'Metal cup'], ['☕', 'Ceramic mug'], ['🥤', 'Foam cup']]},
    {'label': '🧊 Ice on two blocks', 'tag': 'WOW', 'title': 'Which ice melts first?', 'col': C_PURP, 'body': 'Touch, check with a thermometer, predict, then drop the ice.'}],
    'script': '(Hold up a foam cup and a metal cup.) Same warm water in both. Which one keeps it warm longer?\n\n[ON SCREEN: The Cup Race]\nPredict, then watch the graph. The higher the line, the warmer the water. Press Listen.\n\n[ON SCREEN: Ice on two blocks]\nThen don’t skip the ice blocks. The block that feels coldest might surprise you!'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'What went wrong at the cart?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues.'},
    {'label': '☕ Rosa’s new mug', 'tag': 'AFTER THE CASE', 'title': 'Design and test it', 'col': C_RED, 'body': 'Mug, lid, handle. Run the parade test.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Three places to write', 'col': C_GOLD, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Your chart + a labeled sketch'], ['CER', 'Claim, evidence, reasoning']]}],
    'script': '[ON SCREEN: Crack the case]\nFour clues: why did Rosa’s cocoa go cold, and why did the handles get hot?\n\n[ON SCREEN: Rosa’s new mug]\nThen design Rosa a better mug and run the parade test.\n\n[ON SCREEN: Your case report]\nLast, two short answers, your conductor and insulator chart with a labeled sketch, and your CER.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“Cold flows out of ice cubes into my hand.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '[ON SCREEN: The claim]\nCold flows out of ice? Hmm. Think about those red heat dots, and that “Send cold” button.\n\nThere’s no wrong side, as long as you prove it.\n\n[ON SCREEN: The planner]\nTap your side and two facts, then explain how they prove your claim. Try starting with “This shows that…” Press Listen.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🧾 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'Order slip #15', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '🧥 Bonus', 'tag': 'BONUS GAME', 'title': 'The coat on the snow cone', 'col': C_GOLD, 'body': 'Does a coat make heat?'},
    {'kind': 'photo', 'pic': 'bench', 'label': '🌡️ Tool of the Week'},
    {'label': '➡ Next time', 'tag': 'LESSON 24.02', 'title': 'Energy changes', 'col': C_BLUE, 'body': 'Sort the evidence: where did the energy start, and what did it become?'}],
    'script': '(Wrap your hands around the mug again.) Now you know where that warmth goes: from the mug into my hands.\n\n[ON SCREEN: Your specimen]\nFinish your checklist, and order slip number fifteen goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Bonus]\nWant a surprise? Put a coat on a snow cone.\n\n[ON SCREEN: Tool of the Week]\nAnd try the infrared thermometer on this bench.\n\n[ON SCREEN: Next time]\nNext time: tracking energy as it changes!'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
