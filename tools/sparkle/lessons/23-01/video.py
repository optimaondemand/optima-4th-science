#!/usr/bin/env python3
"""Writes video.json (Video Studio plan) for 23.01 · The Canal Hum."""
import json
pics = {
    'bell': {'src': 'images/23-01-bell.jpg', 'cap': 'A ship’s bell (Naval History and Heritage Command, CC BY 2.0)'},
    'drum': {'src': 'images/23-01-black-drum.jpg', 'cap': 'A young black drum (Smithsonian Environmental Research Center, CC BY 2.0)'},
    'hydro': {'src': 'images/23-01-hydrophone.jpg', 'cap': 'A hydrophone on the sea floor (NOAA, public domain)'},
}
C_CASE, C_GREEN, C_PURP, C_RED, C_BLUE, C_GOLD = '#1F7F86', '#2F7A55', '#7A5BB5', '#C8553D', '#2D7AA6', '#B8860B'
S = {}
S['welcome'] = {'label': 'Welcome · the canal hum', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '📰 The front page', 'tag': 'CASE FILE 23', 'title': 'Mystery hum on Pelican Canal', 'col': C_BLUE, 'rows': [['🌙', 'Starts after dark'], ['〰️', 'A LOW hum'], ['🏠', 'Walls buzz inside']]},
    {'label': '🔊 Today', 'tag': 'TODAY', 'title': 'What is sound, really?', 'col': C_GREEN, 'body': 'Vibrations, waves, and high and low pitch.'}],
    'script': '(Put your fingers on your throat and hum.) Mmmmm. Feel that buzz?\n\n[ON SCREEN: The front page]\nNow imagine a hum like that coming through your bedroom walls every night, and nobody knows where it comes from.\n\n[ON SCREEN: Today]\nToday you’ll find out what sound really is. Read the front page in the case file just below me.'}
S['warmup'] = {'label': 'Warm-Up · hold it to stop it (Clue 1)', 'length': '40–50 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'bell', 'label': '🔔 Make it ring'},
    {'label': '✋ Hold it to stop it', 'tag': 'WARM-UP GAME', 'title': 'Ring it, then hold it', 'col': C_PURP, 'rows': [['🔔', 'Make it ring'], ['✋', 'Press and HOLD'], ['🔇', 'What happens?']]}],
    'script': '(Tap a glass with a spoon, then touch it.) Ding… and gone. My finger stopped something.\n\n[ON SCREEN: Make it ring]\nWhat was the glass doing while it rang?\n\n[ON SCREEN: Hold it to stop it]\nMake each one ring, then press and hold the picture to stop it. Press Listen on Sam’s walkie-talkie, right below me.'}
S['part1'] = {'label': 'Part 1 · be the vibration (Clue 2)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '〰️ Be the vibration', 'tag': 'PART 1 GAME', 'title': 'Wiggle the fork', 'col': C_GOLD, 'rows': [['⟷', 'Drag left and right'], ['🔴', 'Watch the red dot'], ['🧱', 'Try water and a wall']]}],
    'script': '(Stand in a line with stuffed animals, and bump the first one.) Bump, bump, bump. The push moved down the line. Did any of them walk to the end?\n\n[ON SCREEN: Be the vibration]\nThat’s how sound travels. Wiggle the tuning fork and keep your eye on the red dot. Press Listen.'}
S['part2'] = {'label': 'Part 2 · match the note (Clue 3)', 'length': '30–40 s', 'want': False, 'parts': [
    {'label': '🎸 Match the note', 'tag': 'PART 2 GAME', 'title': 'Tune it by ear', 'col': C_RED, 'rows': [['📏', 'Shorter or longer'], ['🔩', 'Looser or tighter'], ['💪', 'Then pluck it HARD']]}],
    'script': '(Stretch a rubber band and pluck it, then pull it tighter and pluck again.) Hear the difference?\n\n[ON SCREEN: Match the note]\nTune the band by ear to match three notes. Then pluck it hard. Does it get higher, or just louder?'}
S['explore'] = {'label': 'Part 3 · the ruler test (Clue 4)', 'length': '40–50 s', 'want': True, 'parts': [
    {'label': '📏 The ruler test', 'tag': 'PART 3 GAME', 'title': '2, 6 and 10 inches', 'col': C_BLUE, 'rows': [['📏', 'Pick a length'], ['👇', 'Pull and let go'], ['📋', 'Fill the table']]}],
    'script': '(Hold a ruler on the edge of a table and twang it.) Bwoing!\n\n[ON SCREEN: The ruler test]\nYour turn. Change only ONE thing: how much ruler hangs off. Listen to each length, and the table fills in. If you have a ruler, try it for real, too! Press Listen.'}
S['assignment'] = {'label': 'Assignment · crack the case', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '🔓 Crack the case', 'tag': 'TOP OF THE ASSIGNMENT', 'title': 'What is making the hum?', 'col': C_CASE, 'body': 'Pick the answer that fits all four clues.'},
    {'kind': 'photo', 'pic': 'drum', 'label': '🐟 The hum-maker'},
    {'label': '✍️ Your case report', 'tag': 'WHAT TO WRITE', 'title': 'Three places to write', 'col': C_RED, 'rows': [['Part B', 'Two short answers'], ['Part C', 'Your sound model + sketch'], ['CER', 'Claim, evidence, reasoning']]}],
    'script': '[ON SCREEN: Crack the case]\nFour clues: crack the case at the top of this tab.\n\n[ON SCREEN: The hum-maker]\nThen meet the real hum-maker, and write back to the newspaper.\n\n[ON SCREEN: Your case report]\nLast, two short answers, your sound model with a labeled sketch, and your CER.'}
S['evidence'] = {'label': 'Use your evidence · CER', 'length': '35–45 s', 'want': True, 'parts': [
    {'label': '💬 The claim', 'tag': 'USE YOUR EVIDENCE', 'title': 'A classmate says…', 'col': C_RED, 'body': '“Sound is something invisible that flies through the air, like a tiny ball.”'},
    {'label': '🧩 The planner', 'tag': 'PLAN BEFORE YOU WRITE', 'title': 'Claim · Evidence · Reasoning', 'col': C_PURP, 'rows': [['1', 'Tap I agree or I disagree.'], ['2', 'Tap two pieces of evidence.'], ['3', 'You write the reasoning.']]}],
    'script': '[ON SCREEN: The claim]\nA tiny ball? Hmm. Think about that red dot. Where did it go?\n\nThere’s no wrong side, as long as you prove it.\n\n[ON SCREEN: The planner]\nTap your side and two facts, then explain how they prove your claim. Try starting with “This shows that…” Press Listen.'}
S['closing'] = {'label': 'Case closed', 'length': '30–40 s', 'want': True, 'parts': [
    {'kind': 'photo', 'pic': 'hydro', 'label': '🎧 Bonus: the hydrophone'},
    {'label': '🎧 Your specimen', 'tag': 'FIELD NOTEBOOK', 'title': 'The canal hum recording', 'col': C_CASE, 'body': 'Finish the checklist to stamp CASE CLOSED.'},
    {'label': '➡ Next time', 'tag': 'LESSON 23.02', 'title': 'Moving air and water', 'col': C_BLUE, 'body': 'Can wind and water do work?'}],
    'script': '(Cup a hand behind your ear.) Shhh. Hear that? Fish, drumming in a canal!\n\n[ON SCREEN: Bonus: the hydrophone]\nWant to listen underwater? Try the hydrophone at the very end.\n\n[ON SCREEN: Your specimen]\nFinish your checklist, and the canal hum recording goes into your Field Notebook.\n\n[ON SCREEN: Confetti]\n\n[ON SCREEN: Next time]\nNext time: can moving air and water do work? Bring a pinwheel if you have one!'}
S['quiz'] = {'label': 'Self-Check', 'length': '15–20 s', 'want': False, 'parts': [],
    'script': 'Quick check: three questions, one at a time. It’s not graded. If you miss one, read the hint and try again.'}
V = {'slots': S, 'pics': pics, 'other': ['vocab', 'lesson', 'partb', 'partc']}
json.dump(V, open('video.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('video.json written')
