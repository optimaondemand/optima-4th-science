#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 21.01 · The Boardwalk Fender Bender."""
import json
pics = {
    'crash': {'src': 'images/21-01-crash-test.jpg', 'cap': 'A real crash test: the front is built to crumple (NHTSA, public domain)'},
    'heat': {'src': 'images/21-01-heat-rub.jpg', 'cap': 'A real heat-camera video: rubbing makes a warm spot (Laserlicht, CC BY-SA 4.0)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE = '#1F7F86', '#2F7A55', '#7A5BB5', '#C8553D', '#2D7AA6'
S = {}
S['welcome'] = {'label': 'Welcome · the fender bender', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '📋 The accident report', 'tag': 'CASE FILE 21', 'title': 'The Boardwalk Fender Bender', 'col': C_RED, 'rows': [['🛺', 'Gus’s golf cart, about 5 mph'], ['🍦', 'Rosa’s ice cream cart, parked'], ['💥', 'CRUNCH!'], ['📝', '“The energy just disappeared.”']]},
    {'kind': 'photo', 'pic': 'crash', 'label': '🚗 A real crash test'},
    {'label': '🔎 The case question', 'tag': 'WHERE DID IT GO?', 'title': 'Can energy just disappear?', 'col': C_CASE, 'body': 'Gus’s golf cart stopped dead. Where did its energy go?'}],
    'script': '(Slap your hands together once, loudly.) Crunch! There was a crash on the Palmetto Beach boardwalk last night.\n\n[ON SCREEN: The accident report]\nGus’s golf cart bumped Rosa’s ice cream cart. Nobody was hurt. But Gus wrote that his cart’s energy just disappeared.\n\n[ON SCREEN: A real crash test]\nThis is a real crash test. Look at the front of the truck. Where do you think the energy went?\n\n[ON SCREEN: The case question]\nLet’s find out. Press Listen on Sam’s walkie-talkie, right below me.'}
S['warmup'] = {'label': 'Warm-Up · the clap machine (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '👏 Clap with me', 'tag': 'LIVE DEMO', 'title': 'Clap 10 times, hard', 'col': C_PURP, 'rows': [['1', 'Clap hard 10 times with me'], ['2', 'Touch your cheek'], ['3', 'Warm palms? That’s energy!']]},
    {'label': '🔊 The clap machine', 'tag': 'WARM-UP GAME', 'title': 'Gentle or hard?', 'col': C_GREEN, 'body': 'Clap for 5 seconds each round. Watch the sound meter and the warm glow.'}],
    'script': 'Clap with me! Hard, ten times. (Clap ten times.) Now touch your cheek with your palms. Warm?\n\n[ON SCREEN: Clap with me]\nYour hands just crashed into each other ten times. Where did that motion go? You heard some of it, and you felt some of it.\n\n[ON SCREEN: The clap machine]\nNow try the clap machine. Do a gentle round and a hard round. Which one makes more sound and more heat? Press Listen.'}
S['part1'] = {'label': 'Part 1 · the energy coin bank (Clue 2)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🪙 The energy coin bank', 'tag': 'PART 1 GAME', 'title': '10 coins in, 10 coins out', 'col': C_BLUE, 'rows': [['🎳', 'Pins moving'], ['🔊', 'Sound'], ['🌡️', 'Heat'], ['🕳️', 'Disappeared? Try it!']]}],
    'script': '(Hold up ten coins or ten paper clips in your hand.) Pretend these ten coins are the energy of a bowling ball.\n\n[ON SCREEN: The energy coin bank]\nWhen the ball hits the pins, where does each coin go? Some go into the pins. Some become sound. Some become heat. Can any coin just vanish? Try putting one in Disappeared and see what happens. Press Listen.'}
S['part2'] = {'label': 'Part 2 · bumper cars (Clue 3)', 'length': '30–40 s', 'want': False, 'parts': [
    {'label': '🚗 Bumper cars', 'tag': 'PART 2 GAME', 'title': 'Who changes?', 'col': C_RED, 'body': 'Set the speeds, predict, crash, then read both speedometers.'}],
    'script': '[ON SCREEN: Bumper cars]\nHave you ever ridden bumper cars? When you bump someone, do only THEY move? Or do you feel it too? Predict, crash, and read both speedometers. Press Listen.'}
S['explore'] = {'label': 'Part 4 · the crash lab (Clue 4)', 'length': '45–55 s', 'want': True, 'parts': [
    {'label': '🔥 The crash lab', 'tag': 'PART 4 GAME', 'title': 'Steel, rubber or clay?', 'col': C_PURP, 'rows': [['⚪', 'Steel: CLICK!'], ['🔴', 'Rubber: thump'], ['🟤', 'Clay: splat']]},
    {'kind': 'photo', 'pic': 'heat', 'label': '📷 A real heat camera'}],
    'script': '(Squish a ball of play dough or clay in your hand.) When clay hits something, it squishes. Does squishing take energy?\n\n[ON SCREEN: The crash lab]\nCrash steel balls, rubber balls and clay balls. Then switch on the heat camera.\n\n[ON SCREEN: A real heat camera]\nThis is a real heat camera. Bright yellow and orange mean warm. Find the warmest crash in the lab. Press Listen.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'Where did the energy go?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues. Then Strike! opens.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Three places to write', 'col': C_GREEN, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Your before and after'], ['CER', 'Claim, evidence, reasoning']]}],
    'script': '[ON SCREEN: Crack the case]\nYou have four clues. Crack the case at the top of this tab, and a bowling game opens!\n\n[ON SCREEN: Your case report]\nThen write your case report: two short answers, your before and after, and your CER. Press Listen.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“When two cars crash, all the energy just disappears.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '[ON SCREEN: The claim]\nAll the energy just disappears? Hmm. Think about your warm palms. Think about the heat camera.\n\nThere’s no wrong side, as long as you prove it.\n\n[ON SCREEN: The planner]\nTap your side and two facts, then explain how they prove your claim. Try starting with “This shows that…” Press Listen.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🔩 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'A bolt from the dented bumper', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '🎳 Strike!', 'tag': 'BONUS GAME', 'title': 'Can you get 9 stars?', 'col': C_GREEN, 'body': 'Watch falling pins pass energy down the line.'},
    {'label': '➡ Next time', 'tag': 'LESSON 21.02', 'title': 'Predict, then test', 'col': C_BLUE, 'body': 'Run your own collision trials.'}],
    'script': 'Case closed! The energy never disappeared. It moved into motion, sound and heat.\n\n[ON SCREEN: Your specimen]\nFinish your checklist, and a bolt from the dented bumper goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Strike!]\nThen try Strike! Tell me how many stars you got.\n\n[ON SCREEN: Next time]\nNext time, you’ll run your own collision trials. Press Listen for Sam’s last word.'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
