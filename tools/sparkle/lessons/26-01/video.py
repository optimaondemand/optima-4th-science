#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 26.01 · The Duck Derby Flop (Case 26, Dr. Priya Nair).
Week 25 on has no crew clips yet, so no script says "Press Listen": each one hands off to the page itself."""
import json
pics = {
    'duckrace': {'src': 'images/26-01-duck-race.jpg', 'cap': 'A real charity duck race, Luxembourg 2017 (Bdx, CC BY-SA 4.0)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE, C_GOLD = '#7A5BB5', '#2F7A55', '#5A3B92', '#C8553D', '#2D7AA6', '#B8860B'
S = {}
S['welcome'] = {'label': 'Welcome · The Duck Derby Flop', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🦆 The Duck Derby', 'tag': 'CASE 26', 'title': '200 ducks, one pond', 'col': C_GOLD, 'body': 'A wave machine was supposed to push them to the dock.'},
    {'kind': 'photo', 'pic': 'duckrace', 'label': '📷 A real duck race'},
    {'label': '❓ The question', 'tag': 'THE PROBLEM', 'title': 'Will BIGGER waves work?', 'col': C_RED, 'body': 'Mr. Ortiz wants a giant wave machine next year.'},
    {'label': '🧪 Meet Dr. Nair', 'tag': 'NEW CREW MEMBER', 'title': 'Dr. Priya Nair', 'col': C_CASE, 'body': 'A materials scientist: what things are made of and how they behave.'}],
    'script': '(Hold up a rubber duck, or any small floating toy.) If I make waves in the bathtub, will this duck surf to the other end?\n\n[ON SCREEN: The Duck Derby]\nThat is exactly what the town of Palmetto Springs tried: two hundred ducks and a wave machine.\n\n[ON SCREEN: A real duck race]\nThis is a real duck race. Look closely at where these ducks are floating.\n\n[ON SCREEN: The question]\nNot one duck reached the dock! Now the organizer wants bigger waves.\n\n[ON SCREEN: Meet Dr. Nair]\nOur new scientist, Dr. Priya Nair, needs your help. Read her case file just below me.'}
S['warmup'] = {'label': 'Warm-Up · be the crowd (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🏟️ Be the crowd', 'tag': 'WARM-UP GAME', 'title': 'Do the wave', 'col': C_BLUE, 'rows': [['👆', 'Tap Section 1, then each glowing section'], ['⏱', 'Too slow and it fizzles'], ['🧢', 'Watch the fan in the red cap']]},
    {'label': '🤔 Think about it', 'tag': 'WATCH CLOSELY', 'title': 'What went around?', 'col': C_CASE, 'body': 'The wave? Or the people?'}],
    'script': '(Stand up fast with your arms in the air, then sit back down.) That’s one fan doing the wave. Now picture a whole stadium!\n\n[ON SCREEN: Be the crowd]\nYou’re in charge of the crowd. Tap Section one, then each glowing section, in order. Don’t wait too long!\n\n[ON SCREEN: Think about it]\nKeep your eye on the fan in the red cap. When the wave goes all the way around, where is she? Then write about a wave you’ve seen.'}
S['part1'] = {'label': 'Part 1 · same wave, new stuff (Clue 2)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🪀 Same wave, new stuff', 'tag': 'PART 1 GAME', 'title': 'Five kinds of stuff', 'col': C_GOLD, 'rows': [['🪀', 'Slinky'], ['🪢', 'Rope'], ['💧', 'Pond water'], ['🧒', 'A line of kids'], ['🔊', 'Air']]},
    {'label': '🔴 Tag it', 'tag': 'HOW TO PLAY', 'title': 'Tag one piece red', 'col': C_RED, 'body': 'Send a wave. Where does your tag end up?'}],
    'script': '(Tie a ribbon, or a twist tie, onto a jump rope or a string, and flick one end.) Watch the ribbon. Does it travel to the other end?\n\n[ON SCREEN: Tag it]\nIn this game you tag one piece red, then send a wave, and watch your tag.\n\n[ON SCREEN: Same wave, new stuff]\nTry all five: a slinky, a rope, pond water, a line of kids and even air. Your wave log fills in. Then watch for a surprise about the duck.'}
S['part2'] = {'label': 'Part 2 · measure the waves (Clue 3)', 'length': '35–45 s', 'want': False, 'parts': [
    {'label': '📏 Measure the waves', 'tag': 'PART 2 GAME', 'title': 'Lay a bracket', 'col': C_PURP, 'rows': [['📈', 'Amplitude: center line up to a crest'], ['↔', 'Wavelength: crest to the next crest']]}],
    'script': '(Hold one hand flat for the center line and lift the other hand above it.) From the middle up to the top: that’s the amplitude.\n\n[ON SCREEN: Measure the waves]\nTap two dots to lay a bracket and read how many squares it is. Measure the amplitude, then the wavelength, for three waves. Which one carries the most energy?'}
S['explore'] = {'label': 'Part 3 · shake it yourself (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '🌊 Shake it yourself', 'tag': 'PART 3 GAME', 'title': 'Your hand makes the wave', 'col': C_GREEN, 'rows': [['✊', 'Drag the hand up and down'], ['〰', 'Gentle wiggle'], ['🌊', 'Hard wiggle'], ['🥤', 'Watch the cups and the red ribbon']]}],
    'script': '(Wiggle your hand gently, then hard, like shaking a rope.) Small wiggle. BIG wiggle. What do you think changes?\n\n[ON SCREEN: Shake it yourself]\nDrag the hand at the end of the slinky up and down, or press Gentle wiggle. Watch the red ribbon and the tower of cups at the far end. Then try a hard wiggle. Your log fills in, so compare the two.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'Will bigger waves work?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues.'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO DO', 'title': 'Three places to work', 'col': C_GOLD, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Make or find a wave, then draw and label it'], ['CER', 'Claim, evidence, reasoning']]}],
    'script': '[ON SCREEN: Crack the case]\nYou have four clues. Will a bigger wave machine get the ducks to the dock? Pick the answer that fits every clue. Then watch for a twist, and help Mr. Ortiz fix his plan.\n\n[ON SCREEN: Your case report]\nNext: two short answers. For Part C, make a wave with a jump rope or a string, or think of one you’ve seen. Then sketch and label it. Last comes your CER.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“When a wave moves through water, the water has to travel with it.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '(Make a wave with your arm and pretend to ride it.) Does the water ride along with the wave?\n\n[ON SCREEN: The claim]\nA classmate says the water has to travel with the wave. Think about the duck’s little loop and the red tag.\n\n[ON SCREEN: The planner]\nTap your side and two facts. Then explain how they prove your claim. Try starting with “This shows that…”'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'label': '🦆 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'A derby duck', 'col': C_GOLD, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '➡ Next lesson', 'tag': 'LESSON 26.02', 'title': 'Coded messages', 'col': C_BLUE, 'body': 'Send a secret message with light and sound.'}],
    'script': '(Set the duck down and give it a little bob.) Bob, bob. Still right here!\n\n[ON SCREEN: Your specimen]\nFinish your checklist, and a derby duck goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Next lesson]\nNext time: waves can carry messages, too. You’ll design your own secret code with light and sound.'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
