#!/usr/bin/env python3
"""Writes data.json and fixes.json for 30.01 (run from this folder). Case 30 "The Melted Box" (Dr. Priya Nair, Unit 7, Palmetto Springs):
crayons shipped for the end-of-year art show cooked in a hot truck and arrived as one rainbow slab. Sunshine Freight stamped the damage claim
DENIED: "the wax became a new material." It didn't, and the claim form's own two weights prove it.
New (Bethany's brainstorm, 27 Nov 2026): case.claim, sealbag (Warm-Up: the sealed bag on the scale), callit (Part 1: call the number first),
undoer (Part 2: the UNDO button, replaces the four-pop-up tap diagram), wipe (Part 3: the salt photos, not a clue), statedial (Part 4 = the old
Explore), remelt (the wow: the slab becomes one giant crayon), claimstamp (after the solve), SIMS.evapdish (Tool: evaporating dish).
SCRIPTS ONLY: nothing generated."""
import json, copy, os
P = json.load(open('../12-01/data.json', encoding='utf-8'))
O = json.load(open('../27-01/data.json', encoding='utf-8'))
Q = json.load(open('../29-02/data.json', encoding='utf-8'))
H3 = '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">'
F = []
def fx(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

# ---------------------------------------------------------------- labels (standing approval + ticked)
fx('fix', 'unit label: “Ecosystems & Energy” is a leftover; Module 30 sits under Matter, Magnets & Changes', '<div class="info-detail">Ecosystems &amp; Energy</div>', '<div class="info-detail">Matter, Magnets &amp; Changes</div>')
fx('fix', 'science label: changes of shape, size and state are physical science', '<div class="info-detail">Life Science</div>', '<div class="info-detail">Physical Science</div>')
fx('fix', 'standards label: content benchmark first; content benchmark first; TEKS is a Texas code that isn’t in the plan (the lesson also teaches conservation of mass, SC.4.P.8.3, but the plan row doesn’t list it)',
   '<div class="info-value">SC.4.P.8.2, SC.4.P.9.1 · TEKS 4.6(D)</div>', '<div class="info-value">SC.4.P.9.1, SC.4.P.8.2</div>')
fx('fix', 'footer standards in the same order as the header', '&middot; CPALMS SC.4.P.8.2, SC.4.P.9.1</div>', '&middot; CPALMS SC.4.P.9.1, SC.4.P.8.2</div>')
fx('fix', 'the header comment carries the same standards line', 'NGSS enrichment  ·  CPALMS SC.4.P.8.2, SC.4.P.9.1', 'NGSS enrichment  ·  CPALMS SC.4.P.9.1, SC.4.P.8.2')
fx('fix', 'quarter label in the footer: week 30 is Q4 (the header already says Q4)', 'Science &middot; Quarter 3 &middot; Student Lesson Page', 'Science &middot; Quarter 4 &middot; Student Lesson Page')
fx('plain', 'shorter; no dashes', r"<p>Hold this question in your head as you work\. We're nearly at the end of the year.*?</p>",
   '<p>Keep this question in mind. Today you’ll weigh things before and after they change, and find out that a change can look huge and still leave the same material behind.</p>', True)

# ---------------------------------------------------------------- ticked: energy-lesson leftovers (22.01)
fx('fix', '22.01 leftover (ticked): the Warm-Up title named the toaster lesson',
   '<div class="act-title">🌅 Warm-Up: What Goes In, What Comes Out?</div>\n        <div class="act-subtitle">A familiar device, a hidden change</div>',
   '<div class="act-title">🌅 Warm-Up: The Sealed Bag</div>\n        <div class="act-subtitle">One number, before and after</div>')
fx('fix', '22.01 leftover (ticked): the toaster → the sealed bag on the scale',
   '<p>Think about a toaster. You drop in cold bread. A minute later, you pull out hot toast.</p>',
   '<p>Dr. Priya Nair zipped one ice cube into a sandwich bag and set the bag on a kitchen scale. The scale showed a number. Then she left it on the counter.</p>')
fx('fix', '22.01 leftover (ticked): the toaster sketch → the game (played and answered on the page)',
   "<p>In your notebook, draw a quick sketch of a toaster. On one side, label what goes IN. On the other, label what comes OUT. (Hint: bread on both sides — but something invisible is also going in. What is it?)</p>",
   '<p>An hour later the ice was gone and the bag held water. Read the number before you touch anything.</p>')
fx('fix', '22.01 leftover (ticked): Notice & Wonder about the toaster',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Notice &amp; Wonder</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover (ticked): the “energy can CONVERT … toasters” callout',
   r'<div class="callout callout-tip">\s*<span class="callout-icon">💡</span>\s*<p>Today you\'ll learn that energy can CONVERT.*?</p>\s*</div>\s*', '', True)
fx('fix', '22.01 leftover (ticked): the Stop & Reason asked about “the three devices above … INPUT and OUTPUT”',
   r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>\s*<div>\s*<div class="label">Stop &amp; Reason</div>.*?</div>\s*</div>\s*</div>\s*', '', True)

# ---------------------------------------------------------------- ticked: Word Wall (Device and Magnetic are leftovers)
fx('fix', 'Word Wall (ticked): “Device” is an energy-lesson leftover; this lesson needs conservation of matter',
   '<div class="fc-emoji">⚙️</div><div class="fc-word">Device</div><div class="fc-tap">tap to flip</div></div><div class="flip-card-back"><div class="fc-word-back">Device</div><div class="fc-def">A tool or machine designed to do a job. Most devices convert energy from one form to another — a flashlight, a toaster, a fan are all devices.</div>',
   '<div class="fc-emoji">⚖️</div><div class="fc-word">Conservation of matter</div><div class="fc-tap">tap to flip</div></div><div class="flip-card-back"><div class="fc-word-back">Conservation of matter</div><div class="fc-def">The rule that matter is never made and never destroyed. Change its shape and the amount stays exactly the same.</div>')
fx('fix', 'Word Wall (ticked): “Magnetic” is a magnet-lesson leftover; this lesson uses dissolve',
   '<div class="fc-emoji">🔩</div><div class="fc-word">Magnetic</div><div class="fc-tap">tap to flip</div></div><div class="flip-card-back"><div class="fc-word-back">Magnetic</div><div class="fc-def">A material that a magnet can attract. Iron, nickel, and steel are magnetic. Aluminum, copper, plastic, and wood are not.</div>',
   '<div class="fc-emoji">🥄</div><div class="fc-word">Dissolve</div><div class="fc-tap">tap to flip</div></div><div class="flip-card-back"><div class="fc-word-back">Dissolve</div><div class="fc-def">To mix into a liquid so evenly that you can’t see it any more. The stuff is still in there. Let the water dry up and it comes back.</div>')
fx('plain', 'Word Wall: no dashes', 'A change in shape, size, or state — but NOT in what the material is. Cut paper is still paper. Melted ice is still water.',
   'A change in shape, size or state, but NOT in what the material is. Cut paper is still paper. Melted ice is still water.')
fx('plain', 'Word Wall: no dash', 'A change you can\'t easily undo — even though the material is still the same. Cutting paper into pieces is irreversible.',
   'A change you can’t easily undo, even though the material is still the same. Cutting paper into pieces is irreversible.')
fx('plain', 'Word Wall: no dashes', 'The form of matter — solid, liquid, or gas. Water can be ice, liquid water, or steam — and stays water through all three states.',
   'The form of matter: solid, liquid or gas. Water can be ice, liquid water or steam, and it stays water through all three.')
fx('plain', 'cut filler; no dash', r"<p>These six words show up all through the lesson\. <strong>Tap a card to flip it</strong>.*?</p>",
   '<p><strong>Tap a card to flip it</strong> and read what the word means.</p>', True)
fx('fix', 'supply list (ticked): “a sunny window” is a copy-paste leftover', r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', True)
fx('fix', 'supply list (ticked): no notebook needed (answers are typed on the page)', r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>', '', True)

# ---------------------------------------------------------------- Part 1
fx('plain', 'Part 1: no dashes, shorter', 'Cut a piece of paper into 20 strips — you have paper strips. Same paper. Crumple it into a ball — still paper. Soak it in water and tear it — still paper.',
   'Cut a piece of paper into 20 strips and you have paper strips. Same paper.')
fx('plain', 'Part 1: no dashes', 'ice into water and freeze it back — still H2O.', 'ice into water, then freeze it back. Still water.')
fx('plain', 'Part 1: no dash; anchor for the scale game', 'sugar in water and let it evaporate — the sugar comes back.</p>',
   'sugar in water, let the water dry up, and the sugar comes back.</p>\n      <p>Try it: call the number before the scale does.</p>')
fx('cut', 'lean: the Stop & Think (how do you know it’s still water?) is played by the sealed bag and the scale game',
   r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', True)

# ---------------------------------------------------------------- Part 2
fx('plain', 'Part 2: no dashes', 'Some physical changes are <span class="vtip">reversible<span class="vtip-box"><span class="vtip-word">Reversible</span>Can be undone.</span></span> — you can return the material to its starting form. Others are <span class="vtip">irreversible<span class="vtip-box"><span class="vtip-word">Irreversible</span>Can\'t easily undo.</span></span> — even though the material is the SAME, you can\'t easily undo the change.',
   'Some physical changes are <span class="vtip">reversible<span class="vtip-box"><span class="vtip-word">Reversible</span>Can be undone.</span></span>: you can put the material back the way it started. Others are <span class="vtip">irreversible<span class="vtip-box"><span class="vtip-word">Irreversible</span>Can’t easily undo.</span></span>. The material is still the SAME, but you can’t easily undo the change.')
fx('cut', 'lean: the three-bullet list is exactly what the UNDO game plays (six changes, stamped, with a material line on every card)',
   r'<ul style="font-size:16px;color:#2B1D12;line-height:1\.7;margin:10px 0 12px 24px;">\s*<li><strong>Reversible:</strong>.*?</ul>\s*',
   '<p>Melting ice and folding paper can be undone. Shredding paper and breaking glass cannot. Either way, no new material forms.</p>\n\n      ', True)
fx('plain', 'Part 2: plain words', 'The big test for any physical change is to ask: "Is it still the SAME material?" If yes, it\'s physical. If a brand-new substance has formed, you\'re looking at a chemical change (that\'s tomorrow\'s lesson).',
   'The big test for any change is one question: is it still the SAME material? If yes, the change is physical. If a brand new material has formed, like wood turning to ash when it burns, iron turning to rust, or an egg cooking, that is a chemical change.')
fx('plain', 'Part 2: no dash', "You can't easily un-shred paper or un-break glass, but the material is still paper and glass — physical changes, just hard-to-reverse ones.",
   'Un-shredded paper and un-broken glass are impossible, but both are still the same material.')
fx('cut', 'lean: Key Concept repeats the paragraph above it; its place holds the lead-in for the UNDO game',
   r'<div style="background:#FFF6E5;border:2\.5px solid #F0C97A;[^>]*>\s*<div[^>]*>⭐ Key Concept</div>.*?</p>\s*</div>\s*',
   '<p>Try it: press UNDO on six changes and watch which ones really come back.</p>\n\n      ', True)

# ---------------------------------------------------------------- Part 3 = the conservation box (the labeled benchmark) + the salt photos
fx('plain', 'Part 3 heading so the part numbers run 1, 2, 3, 4', '<div style="background:#EAF8FD;border:2px solid #B8E0F8;border-radius:14px;padding:16px 20px;margin:16px 0;">\n        <p style="font-size:16px;color:#0E1C42;font-weight:800;margin:0 0 8px;">⚖️ Conservation of Matter — Nothing Disappears!</p>',
   H3 + 'Part 3 · Nothing Disappears</h3>\n      <div style="background:#EAF8FD;border:2px solid #B8E0F8;border-radius:14px;padding:16px 20px;margin:16px 0;">\n        <p style="font-size:16px;color:#0E1C42;font-weight:800;margin:0 0 8px;">⚖️ Conservation of matter</p>')
fx('plain', 'Part 3: no dashes, shorter (the scale game already does the clay test)',
   r"<p style=\"font-size:15px;color:#5A4D3E;line-height:1\.65;margin:0 0 10px;\">Here's one of the biggest ideas in all of science.*?</p>",
   '<p style="font-size:15px;color:#5A4D3E;line-height:1.65;margin:0 0 10px;">Here is one of the biggest ideas in all of science: <strong>matter is never made and never destroyed.</strong> It only changes form. Melt an ice cube and the water weighs exactly what the ice did.</p>', True)
fx('plain', 'Part 3: no dashes; shorter; anchor for the salt photos',
   r'<p style="font-size:15px;color:#5A4D3E;line-height:1\.65;margin:0;">You can test this yourself.*?</p>',
   '<p style="font-size:15px;color:#5A4D3E;line-height:1.65;margin:0;">Even when matter seems to disappear, it hasn’t. A puddle dries up in the sun, but the water didn’t vanish. It turned into <strong>water vapor</strong> (water as a gas) in the air, and it still weighs what the puddle did.</p>\n      </div>\n      <p>People have used that for thousands of years. Look at what the sun leaves behind.</p>\n      <div style="display:none;"><!-- the blue box is closed above so the salt photos sit outside it; the original closing tag closes this empty div -->', True)

# ---------------------------------------------------------------- the tap diagram → Part 4 = the old Explore
fx('cut', 'lean: the Four Physical Changes tap diagram repeats the infographic right above it (the UNDO game plays it). With it go Observe & Reason, the boiled-peanut Amazing Fact (cooking is mostly chemical, so it also contradicts the lesson), the beach Florida connection and the states Go Deeper. Part 4 = the old Explore: take one material all the way and back',
   H3 + 'Four Physical Changes</h3>.*?(?=<div class="tab-next-wrap">)',
   H3 + 'Part 4 · All the Way and Back</h3>\n      <p>Now take one material all the way from solid to gas, and all the way back.</p>\n      <p>Last stop: the art room. Dr. Nair carried the melted slab inside and put it on the hot plate.</p>\n\n      ', True)
fx('cut', 'Part 4 replaces the Explore tab, so the next button goes to Self-Check',
   '''<div class="tab-next-wrap">
        <button class="tab-next-btn" onclick="switchTab('explore')">Continue to 🔬 Explore →</button>''',
   '''<div class="tab-next-wrap">
        <button class="tab-next-btn" onclick="switchTab('quiz')">Continue to 🧠 Self-Check →</button>''')
fx('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', True)
fx('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fx('cut', 'lean: remove the whole Explore tab (its 6-change home chart lives on as Part C; the evaporation Amazing Fact, the limestone Think like a scientist and the mixtures Go Deeper go with it)',
   r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', True)

# ---------------------------------------------------------------- Assignment
fx('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', True)
fx('plain', 'Part B question 5 no longer points at the cut tap diagram (same task)',
   'Pick ONE physical change from the diagram (melting ice, sugar dissolving, cutting paper, breaking glass). Tell whether it\'s reversible and what material stays the same.',
   'Pick ONE physical change from today: melting ice, sugar dissolving, cutting paper, breaking glass, or the melted crayons. Tell whether it can be undone, and what material stays the same.')
fx('plain', 'Part B question 5 label (Gathered Answers)', 'data-label="Pick ONE physical change from the diagram (melting..."', 'data-label="One physical change: can it be undone, what stays the same"')
fx('plain', 'Part B question 6 label (Gathered Answers)', 'data-label="Explain why &quot;irreversible&quot; doesn&#x27;t mean &quot;chemical ..."', 'data-label="Why “can’t undo it” doesn’t mean chemical"')
fx('cut', 'lean: Part B question 7 removed (Bethany kept 5 and 6; the three states are taught and tested by the state dial in Part 4)',
   r'<div class="pq">\s*<span class="pq-num"[^>]*>7</span>.*?id="ans-3"[^>]*></textarea>\s*', '', True)
fx('fix', '9.01 leftover (ticked): Part C was a food chain; the checklist already describes the chart this lesson needs',
   '🎨 Part C &mdash; Build Your Own Food Chain', '🎨 Part C &mdash; Your Own Change Chart')
fx('fix', '9.01 leftover (ticked): Part C task → the checklist’s own chart (typed on the page, plus a required labeled drawing)',
   r'<p style="font-size:15px;color:#9A8E82;margin-bottom:14px;">In your science notebook, draw a <strong>new</strong> food chain.*?<p style="font-size:15px;color:#9A8E82;margin-bottom:14px;">Use colors\. Label every part\.</p>',
   '<p style="font-size:15px;color:#9A8E82;margin-bottom:14px;">Find <strong>four</strong> physical changes at home. Sort them into changes you <strong>can undo</strong> and changes that are <strong>hard to undo</strong>, and name the material that stays the same in each one.</p>', True)
fx('fix', '9.01 leftover (ticked): Reflect asked about a hawk; the lean shape cuts Reflect',
   r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', True)
fx('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
   "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
   'Do you agree or disagree? Prove it with <strong>two pieces of evidence</strong> from today’s lesson.')
fx('plain', 'shorter', 'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.', 'All your answers in one place. Copy or download them to turn in on Canvas.')
fx('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered in complete sentences using lesson vocabulary.', 'Both questions answered in complete sentences, using words from today.')
fx('plain', 'Part C checklist matches the task and ends with the required sketch',
   'A 2-column reversible/irreversible chart with 4 physical changes and a what-stays-the-same note for each.',
   'My chart: 4 changes from home, sorted, with the material that stays the same in each. Plus your labeled sketch.')
fx('cut', 'lean: no separate Big Question answer', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', True)
fx('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', True)
fx('plain', 'lean: shorter checklist line',
   '<strong>Evidence Response:</strong> I made a claim about whether ANY irreversible change is automatically chemical, supported with two pieces of evidence.',
   '<strong>Use Your Evidence:</strong> My claim about whether a change you can’t undo must be chemical, with two pieces of evidence.')
fx('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a 9.01 leftover)',
   r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)',
   'Download your field journal (it has your answers and your sketch) and upload it to the Canvas assignment. Or copy your Gathered Answers (above) into Canvas.', True)
fx('plain', 'closing: no dashes; shorter', r"<p><strong>Nicely done\.</strong> You can now explain that a <span class=\"vtip\">physical change.*?Get ready for our finale!</p>",
   '<p><strong>Nicely done.</strong> You can now explain that a physical change can be undone or not, and that the material stays the same either way. One lesson left in the year, and it is the big one: chemical changes, where the material really does become something new.</p>', True)
# (the Big Question itself is read-only, so its em dashes stay)

# ---------------------------------------------------------------- the story
PRIYA = O['crew']['priya']
IMG = {'ponds': 'images/30-01-salt-ponds.jpg', 'harvest': 'images/30-01-salt-harvest.jpg', 'crystals': 'images/30-01-salt-crystals.jpg'}
CR_SALT = ('Salt ponds on San Francisco Bay: Daniel L. Lu (user:dllu), CC BY-SA 4.0 · Salt drying in the pans at Salinas del Carmen, Fuerteventura: Dietmar Rabich, CC BY-SA 4.0 · '
           'Salt crystals at the Natural History Museum of Vienna: włodi, CC BY-SA 2.0 · all via Wikimedia Commons')
D = {
    'lesson': '30.01', 'week': 30, 'day': 1, 'guide': 'priya', 'prefix': 'g4sci-30-1', 'manifestKey': '30-01',
    'paths': P['paths'], 'crew': {'priya': PRIYA},
    'expedition': {'num': 30, 'title': 'The Melted Box'},
    'ambient': {'icon': '🌅', 'label': 'Morning on the dock'},
    'case': {
        'num': 30, 'title': 'The Melted Box', 'style': 'claim',
        'hook': 'Dr. Priya Nair here. The art show is Friday, and 300 crayons were shipped to Palmetto Springs Elementary for it. The truck sat in the sun, and the box arrived with one solid rainbow slab inside. The freight company stamped the school’s claim DENIED: “the wax became a new material.” Is that true? And is the art show over?',
        'claim': {
            'head': 'SUNSHINE FREIGHT · DAMAGE CLAIM', 'no': 'Claim #4408',
            'rows': [['Shipment', '300 wax crayons, 1 carton'], ['From', 'Tallahassee warehouse'], ['To', 'Palmetto Springs Elementary'],
                     ['Weight when it left', '1,200 g'], ['Weight when it arrived', '1,200 g'], ['Driver’s note', 'Truck sat in the sun. Box got hot.']],
            'stamp': 'DENIED',
            'note': 'Inspector: contents melted into one solid block. The wax became a new material. Nothing usable was delivered. Claim denied.',
            'sign': 'Sunshine Freight'},
        'stills': [],
        'question': 'Did the crayons become a new material, and can the art show still happen?',
        'how': 'Find 4 clues as you work through the lesson. Then crack the case (solve it) at the top of the Assignment tab.',
        'clues': [
            {'id': 'sealbag', 'icon': '⚖️', 'where': 'Warm-Up: the sealed bag', 't': 'The ice melted and the scale did not move. Melting changes the form, not the amount, and not the material.'},
            {'id': 'callit', 'icon': '🔢', 'where': 'The Lesson, Part 1: call the number first', 't': 'Cut it, flatten it, dissolve it: the number on the scale never changed, and neither did the material.'},
            {'id': 'undoer', 'icon': '↩️', 'where': 'The Lesson, Part 2: the UNDO button', 't': 'Some changes cannot be undone and are STILL physical. Shredded paper is paper. And melted wax CAN be poured into a new shape.'},
            {'id': 'statedial', 'icon': '🌡️', 'where': 'The Lesson, Part 4: the state dial', 't': 'Solid to liquid to gas and all the way back: still water, every single time. A melted solid can be made solid again.'},
        ],
        'solve': {
            'title': 'Was the claim fair?', 'q': 'Which answer fits all four clues AND the claim form?',
            'options': [
                {'t': 'No new material. The box left at 1,200 g and arrived at 1,200 g, and melted wax can be poured into new crayons. The claim should be approved.', 'right': True,
                 'why': 'Case cracked! Same mass, same wax, new shape. That is a physical change, and the art show is on.'},
                {'t': 'It is a new material, because the crayons cannot be put back the way they were.', 'why': 'Check Clue 3. Hard to undo does not mean a new material. Shredded paper is still paper.'},
                {'t': 'It is a new material, because the wax went from solid to liquid.', 'why': 'Check Clue 4. Changing state is a physical change. Ice to water to steam is still water.'},
                {'t': 'The crayons are gone, because the box weighs less than it did.', 'why': 'Read the claim form again. It left at 1,200 g and arrived at 1,200 g. Nothing left the box.'},
            ]},
    },
    'sealbag': {
        'afterText': 'Read the number before you touch anything.', 'kicker': 'Warm-Up game', 'title': 'The sealed bag',
        'why': {'icon': '⚖️', 'q': 'Why seal the bag?', 't': 'Nothing can get in and nothing can get out. So anything that changes is still in there.'},
        'todo': ['Drag the bag onto the scale (or tap the bag, then the scale).', 'Read the number. Then press Wait an hour.', 'Call it: what will the scale say now?'],
        'bag': {'icon': '🧊', 't': 'Sealed bag · one ice cube'}, 'scaleLabel': 'Kitchen scale',
        'start': 48, 'end': 48, 'unit': 'g',
        'dropLine': 'Drop the bag on the scale, or tap the scale.',
        'readLine': 'The scale reads {n} g. Write that number down in your head.',
        'waitBtn': '⏱ Wait an hour', 'waitLine': 'The ice is melting…',
        'ask': 'The ice melted. What does the scale say now?',
        'opts': [{'t': 'Less than 48 g', 'miss': 'Nothing left the bag. It was sealed shut the whole time.'},
                 {'t': 'Exactly 48 g', 'ok': True},
                 {'t': 'More than 48 g', 'miss': 'Nothing got into the bag either. It was sealed shut.'}],
        'revealLine': 'Still 48 g. Exactly the same.',
        'q': 'What is in the bag now?',
        'opts2': [{'t': 'The same water, in a different form.', 'ok': True},
                  {'t': 'A brand new material.', 'miss': 'Freeze it again and you get your ice cube back. Nothing new was made.'},
                  {'t': 'Less water than before.', 'miss': 'The scale says 48 g, same as the start. None of it left.'}],
        'win': 'Melting changed the form, not the amount and not the material. Clue 1!', 'clue': 'sealbag'},
    'callit': {
        'afterText': 'call the number before the scale does.', 'kicker': 'Part 1 game', 'title': 'Call the number first',
        'why': {'icon': '🔢', 'q': 'Why call it first?', 't': 'Scientists write down what they expect BEFORE they measure, so they can’t fool themselves after.'},
        'todo': ['Read the starting number.', 'Press the change button and watch.', 'Type the number you think the scale will show, then press Weigh it.'],
        'keyLabel': 'Type your call', 'weighBtn': '⚖️ Weigh it', 'unit': 'g',
        'startLine': 'On the scale now: {n}', 'callLine': 'Your call: {n} g', 'realLine': 'The scale says: {n} g',
        'hitLine': 'Called it! Nothing was added and nothing left the tray.',
        'overLine': 'Not quite. Look at the tray: is there more stuff than before, or the same stuff in a new shape?',
        'underLine': 'Not quite. Nothing fell off the tray. Where could the missing grams have gone?',
        'rounds': [
            {'id': 'paper', 'icon': '📄', 't': 'A sheet of paper', 'btn': '✂️ Cut it into strips', 'mass': 5, 'after': '20 paper strips',
             'line': 'Snip, snip, snip. Twenty strips, all still on the tray.', 'same': 'paper'},
            {'id': 'clay', 'icon': '🟤', 't': 'A ball of clay', 'btn': '🫳 Flatten it', 'mass': 60, 'after': 'a clay pancake',
             'line': 'Squash. The ball is now a flat pancake.', 'same': 'clay'},
            {'id': 'sugar', 'icon': '🥤', 't': 'A cup of water and a spoon of sugar', 'btn': '🥄 Stir the sugar in', 'mass': 212, 'after': 'sugar water',
             'line': 'Stir, stir. The sugar disappears from sight. The whole cup is on the scale.', 'same': 'sugar and water'},
        ],
        'needLine': 'Call the number first.',
        'q': 'Three changes, three readings. What happened to the number every time?',
        'opts': [{'t': 'It stayed exactly the same.', 'ok': True},
                 {'t': 'It went down when things got smaller.', 'miss': 'Look at your readings. Cutting the paper made more pieces, not less paper.'},
                 {'t': 'It changed every time.', 'miss': 'Check your three readings again: 5 g, 60 g, 212 g, before and after.'}],
        'win': 'Cut, flattened, dissolved: same number, same material. Clue 2!', 'clue': 'callit'},
    'undoer': {
        'afterText': 'press UNDO on six changes', 'kicker': 'Part 2 game', 'title': 'The UNDO button',
        'why': {'icon': '↩️', 'q': 'What does UNDO test?', 't': 'Whether you can put the material back the way it started. It does NOT test whether the material changed.'},
        'todo': ['Press ↩ UNDO on a change and watch.', 'Then drag a stamp onto that card (or tap a stamp, then the card).', 'Do all six.'],
        'undoBtn': '↩ UNDO', 'stampQ': 'Now stamp it.',
        'stamps': [{'k': 'back', 'icon': '↩️', 't': 'CAME BACK'}, {'k': 'stuck', 'icon': '🚫', 't': 'STUCK THIS WAY'}],
        'cards': [
            {'id': 'ice', 'icon': '🧊', 't': 'Melted ice', 'from': '🧊', 'to': '💧', 'k': 'back',
             'line': 'Into the freezer. An hour later: an ice cube again.', 'mat': 'water'},
            {'id': 'fold', 'icon': '📄', 't': 'Folded paper', 'from': '📄', 'to': '📃', 'k': 'back',
             'line': 'Unfold it. Flat again, with a crease line left over.', 'mat': 'paper'},
            {'id': 'sugar', 'icon': '🥄', 't': 'Dissolved sugar', 'from': '🍬', 'to': '🥤', 'k': 'back',
             'line': 'Leave the cup in the sun. The water dries up and the sugar is sitting there.', 'mat': 'sugar'},
            {'id': 'shred', 'icon': '🗞️', 't': 'Shredded paper', 'from': '📄', 'to': '🎊', 'k': 'stuck',
             'line': 'You can tape a few strips. You cannot make it one clean sheet again.', 'mat': 'paper'},
            {'id': 'glass', 'icon': '🥛', 't': 'Broken glass', 'from': '🥛', 'to': '🔹', 'k': 'stuck',
             'line': 'The shards will not go back together. (Never try this one at home.)', 'mat': 'glass'},
            {'id': 'cheese', 'icon': '🧀', 't': 'Grated cheese', 'from': '🧀', 'to': '🟡', 'k': 'stuck',
             'line': 'Press the shreds. You get a lump of cheese, not the block you started with.', 'mat': 'cheese'}],
        'miss': {'back': 'Press UNDO again and watch. Did it really come back?', 'stuck': 'Press UNDO again. That one did come back!'},
        'matLine': 'Material: {m}, before AND after.',
        'q': 'Six changes. How many of them made a NEW material?',
        'opts': [{'t': 'None of them. Every one is still the same material.', 'ok': True},
                 {'t': 'The three with the 🚫 stamp.', 'miss': 'Read their material lines. Shredded paper is paper, shards are glass, shreds are cheese.'},
                 {'t': 'Only the broken glass.', 'miss': 'Every shard is still clear, hard glass. Nothing new was made.'}],
        'win': 'Hard to undo is NOT the same as a new material. Clue 3!', 'clue': 'undoer'},
    'wipe': {
        'afterText': 'Look at what the sun leaves behind.', 'kicker': 'Part 3 · real photos', 'title': 'Where did the water go?',
        'why': {'icon': '🧂', 'q': 'What is a salt pond?', 't': 'A shallow pond of seawater left out in the sun. The water turns to vapor and floats away. The salt cannot, so it stays.'},
        'todo': ['Drag the slider across the photo.', 'Then tap the numbers on the close-up photo.'],
        'before': {'img': IMG['ponds'], 'alt': 'An aerial view of huge shallow ponds of seawater, each a different shade of pink and green.', 'cap': 'Seawater in shallow ponds'},
        'after': {'img': IMG['harvest'], 'alt': 'Heaps of white salt sitting in shallow stone-walled pans, with pink seawater still in the pans around them.', 'cap': 'The salt the sun leaves behind'},
        'hint': 'Drag me',
        'photo': {'img': IMG['crystals'], 'alt': 'A close-up of clear salt crystals. Each one is a cube with flat square faces.',
                  'hotspots': [{'n': 1, 'x': 66, 'y': 52, 'label': 'A cube', 't': 'Salt always grows in cubes. The grains in a salt shaker are these same cubes, far too small to see.'},
                               {'n': 2, 'x': 27, 'y': 16, 'label': 'See-through', 't': 'Clear enough to look through. Salt that comes out of water looks nothing like the water it came from.'},
                               {'n': 3, 'x': 17, 'y': 76, 'label': 'Little ones too', 't': 'Smaller cubes, same shape. Stir any of them back into water and they dissolve again, ready to come back.'}]},
        'credit': CR_SALT,
        'q': 'Dissolving salt in water and drying it out again: what kind of change is that?',
        'opts': [{'t': 'A physical change. The salt was there all along.', 'ok': True},
                 {'t': 'A chemical change, because the salt disappeared.', 'miss': 'It never disappeared. It came back, grain for grain, when the water left.'},
                 {'t': 'A chemical change, because the water vanished.', 'miss': 'The water did not vanish either. It turned into vapor in the air.'}],
        'win': 'Nothing disappeared. It just changed form.'},
    'statedial': {
        'afterText': 'Now take one material all the way from solid to gas, and all the way back.', 'kicker': 'Part 4 game', 'title': 'The state dial',
        'why': {'icon': '🌡️', 'q': 'What is a state of matter?', 't': 'Solid, liquid or gas. Heat or cool water and it moves between all three, and it is water the whole time.'},
        'todo': ['Drag the dial (or tap a stop) to heat the sealed jar.', 'Visit every stop, all the way to the top.', 'Then bring it all the way back down to ice.'],
        'jarLabel': 'A sealed glass jar · 200 g of water', 'massLabel': 'Mass', 'mass': 200, 'unit': 'g',
        'matLabel': 'Material', 'matValue': 'WATER', 'matNote': 'Never changes.',
        'stops': [
            {'k': 'freezer', 't': '−18 °C', 'sub': 'Freezer', 'state': 'SOLID', 'icon': '🧊', 'line': 'Hard ice, one solid block.'},
            {'k': 'cold', 't': '0 °C', 'sub': 'Melting', 'state': 'SOLID + LIQUID', 'icon': '🫗', 'line': 'Half ice, half water. The scale has not budged.'},
            {'k': 'room', 't': '20 °C', 'sub': 'Room', 'state': 'LIQUID', 'icon': '💧', 'line': 'All liquid water now.'},
            {'k': 'hot', 't': '90 °C', 'sub': 'Hot', 'state': 'LIQUID + GAS', 'icon': '♨️', 'line': 'Steam is rising, and the lid is holding it in.'},
            {'k': 'boil', 't': '110 °C', 'sub': 'Stovetop', 'state': 'GAS', 'icon': '☁️', 'line': 'All water vapor. The jar looks empty, but it is full.'}],
        'needUp': 'Keep going up. You have not reached the top stop yet.',
        'needDown': 'Now bring it all the way back down to the freezer.',
        'backLine': 'Back to a solid block of ice. Same jar, same 200 g, same water.',
        'q': 'You turned the water into a gas and then back into ice. What material is in the jar now?',
        'opts': [{'t': 'Water. It was water at every single stop.', 'ok': True},
                 {'t': 'A new material, because it was a gas for a while.', 'miss': 'Check the Material readout. It said WATER at every stop, including the top one.'},
                 {'t': 'Less water, because some turned into steam.', 'miss': 'The jar is sealed. Check the Mass readout: 200 g the whole way up and the whole way down.'}],
        'win': 'Solid, liquid, gas and back again: still water. Clue 4!', 'clue': 'statedial'},
    'remelt': {
        'afterText': 'Dr. Nair carried the melted slab inside and put it on the hot plate.', 'kicker': 'Part 4 · the wow', 'title': 'One giant crayon',
        'why': {'icon': '🖍️', 'q': 'Is melting wax a physical change?', 't': 'Yes. Solid to liquid and back to solid, and it is wax the whole time.'},
        'todo': ['Press each step. Keep an eye on the scale.'],
        'massLabel': 'On the scale', 'mass': 1200, 'unit': 'g',
        'steps': [
            {'k': 'slab', 'icon': '🌈', 't': 'The slab', 'btn': '🔥 Melt it', 'line': 'The rainbow slab that the freight company called ruined. 1,200 g.'},
            {'k': 'melt', 'icon': '🫕', 't': 'Melted', 'btn': '🫗 Pour it into a mold', 'line': 'Liquid wax, swirling with every color. Still 1,200 g.'},
            {'k': 'mold', 'icon': '🧁', 't': 'In the mold', 'btn': '❄️ Let it cool', 'line': 'Poured into one big crayon mold. Still 1,200 g.'},
            {'k': 'crayon', 'icon': '🖍️', 't': 'One giant crayon', 'btn': '', 'line': 'One giant rainbow crayon, ready for the art show. Still 1,200 g.'}],
        'q': 'Is the giant crayon a new material?',
        'opts': [{'t': 'No. It is the same wax in a new shape.', 'ok': True},
                 {'t': 'Yes, because it looks completely different.', 'miss': 'Looks are not the test. The test is: is it still the same material? Melt it again and you get the same wax.'},
                 {'t': 'Yes, because the colors mixed together.', 'miss': 'Mixing colors of wax makes a mixture of wax. Each color is still the wax it was.'}],
        'win': 'Same wax, same 1,200 g, brand new shape. The art show is saved.'},
    'claimstamp': {
        'afterSolve': True, 'kicker': 'Case 30 · close it out', 'title': 'Stamp the claim',
        'why': {'icon': '🧾', 'q': 'Why stamp it yourself?', 't': 'Because you have the evidence now. Tests settle a claim, not how the box looks.'},
        'todo': ['Pick the two pieces of evidence that settle the claim.', 'Then stamp the form.'],
        'formHead': 'SUNSHINE FREIGHT · DAMAGE CLAIM #4408',
        'pickQ': 'Pick TWO pieces of evidence for the form.', 'need': 2,
        'chips': [
            {'id': 'mass', 't': 'It left at 1,200 g and arrived at 1,200 g.', 'ok': True},
            {'id': 'remelt', 't': 'The wax melted and poured into a new crayon, so it is still wax.', 'ok': True},
            {'id': 'ugly', 't': 'The slab looks nothing like crayons.', 'miss': 'How it looks is not evidence about the material.'},
            {'id': 'hot', 't': 'The truck was hot.', 'miss': 'True, but that is what caused the change, not evidence about the material.'}],
        'stampQ': 'Now stamp it.',
        'stamps': [{'k': 'ok', 'icon': '✅', 't': 'APPROVED'}, {'k': 'no', 'icon': '🚫', 't': 'DENIED'}],
        'answer': 'ok', 'missStamp': 'Look at your two pieces of evidence. Do they say the school lost its crayons, or not?',
        'win': 'Approved. Case 30 closed, and the art show has its giant crayon.'},
    'tool': {
        'name': 'Evaporating dish', 'icon': '🧂', 'tab': 'assignment', 'after': '#tab-assignment .activity-card', 'key': '30-01-tool', 'sim': 'evapdish',
        'kicker': 'Bonus · Tool of the Week', 'teaser': 'Real lab gear: make the water leave and see what stays behind.',
        'done': 'Tool of the Week: you used a real evaporating dish.',
        'why': {'icon': '🧂', 'q': 'What is an evaporating dish?', 't': 'A shallow dish that scientists warm gently so the water turns to vapor and leaves. Whatever was dissolved in the water is left sitting in the dish.'},
        'evapdish': {
            'title': 'Warm it and watch', 'todo': ['Pick a liquid and pour it into the dish.', 'Turn the warmer on and wait.', 'Then weigh what is left.'],
            'model': 'A model of a real tool. An adult uses heat for this one.',
            'liquids': [
                {'k': 'salt', 'icon': '🧂', 't': 'Salt water', 'grams': 9, 'left': 'white cubic crystals', 'res': 'Salt! 9 g of it, the same 9 g that was stirred in.'},
                {'k': 'sugar', 'icon': '🍬', 't': 'Sugar water', 'grams': 12, 'left': 'sticky clear crystals', 'res': 'Sugar, 12 g. It was dissolved in there the whole time.'},
                {'k': 'plain', 'icon': '💧', 't': 'Plain water', 'grams': 0, 'left': 'nothing at all', 'res': 'An empty dish. Nothing was dissolved in it to leave behind.'},
                {'k': 'sand', 'icon': '🏖️', 't': 'Sandy water', 'grams': 15, 'left': 'damp sand', 'res': 'Sand, 15 g. It never dissolved. It was only floating about.'}],
            'onBtn': '🔥 Warm it', 'waitLine': 'The water is leaving as vapor…', 'weighBtn': '⚖️ Weigh what is left',
            'q': {'q': 'You warmed salt water and 9 g of salt was left. Where did the salt come from?',
                  'opts': [{'t': 'It was dissolved in the water the whole time.', 'ok': True, 'why': 'Right. Dissolving hid it from your eyes. It never left.'},
                           {'t': 'The heat made new salt.', 'why': 'Heat cannot make a new material here. Nothing was added to the dish.'},
                           {'t': 'It came out of the dish.', 'why': 'The dish is just a container. The salt came out of the water.'}]}}},
    'exploreMod': 'statedial',
    'quizKicker': '',
    'quizMiss': {
        'q1': {'A': 'A new substance means a CHEMICAL change. This one is about form.', 'B': 'Heat is not the test. Cutting paper takes no heat at all.'},
        'q2': {'B': 'You cannot make shreds into one clean sheet again. Try the one you put in the freezer.', 'C': 'Broken glass will not go back together. Which one would?'},
        'q3': {'A': 'More pieces does not mean a new material. Every shred is still cheese.', 'C': 'Shredding is never chemical. Nothing new was made.'}},
    'flags': {
        'ans-1': [
            {'label': 'one change', 're': 'melt|ice|sugar|dissolv|cut|paper|glass|break|broke|crayon|wax|shred|fold'},
            {'label': 'can it be undone', 'any': ['undo', 'undone', 'reversible', 'reverse', 'back', 'refreeze', 'freeze again', 'cannot', 'can’t', "can't", 'hard to'], 'min': 1},
            {'label': 'the material that stays the same', 're': 'water|paper|glass|sugar|wax|cheese|clay|same material|still'}],
        'ans-2': [
            {'label': 'your explanation', 're': 'same material|still|no new|not new|does not make|doesn’t make|doesn\'t make|material stays'},
            {'label': 'an example', 're': 'paper|glass|shred|cut|break|broke|cheese|crayon|wax|sand|chalk'}],
        'cer-4': [
            {'label': 'your claim', 're': 'agree|disagree|wrong|right|true|not true|false|not always|not every|does not|doesn’t'},
            {'label': 'two pieces of evidence', 'any': ['paper', 'glass', 'shred', 'cheese', 'crayon', 'wax', 'melt', 'scale', 'gram', '1,200', '1200', 'mass', 'weigh', 'same material', 'sugar', 'salt'], 'min': 2},
            {'label': 'your reasoning', 're': 'because|so |this shows|that shows|this means|that means|which means|proves|since'}]},
    'minWords': {'ans-1': 15, 'ans-2': 15, 'cer-4': 30},
    'hints': {
        'ans-1': ['Pick one: melting ice, sugar dissolving, cutting paper, breaking glass, or the melted crayons.',
                  'Can you put it back the way it started? And what is it made of now?',
                  'Try: When ___ changes, you ___ undo it. The material is still ___.'],
        'ans-2': ['Think about the shredded paper and the broken glass in the UNDO game.',
                  'What makes a change chemical? A NEW material, not a change you cannot undo.',
                  'Try: Irreversible only means ___. It is still ___ because ___. For example ___.']},
    'scholar': {},
    'planner': {
        'before': 'cer-4', 'title': 'Your claim and two pieces of evidence',
        'rows': [
            {'label': '1. Pick your side', 'options': ['I agree', 'I disagree'], 'pick': 1},
            {'label': '2. Pick two pieces of evidence from the lesson', 'pick': 2, 'options': [
                'Shredded paper cannot be undone, and every shred is still paper.',
                'The melted crayon slab weighed 1,200 g before and after, and it poured into a new crayon.',
                'The sealed bag read 48 g as ice and 48 g as water.',
                'Breaking glass makes a loud noise.']}],
        'note': 'Tap your side and two facts. Then write your reasoning in your own words.'},
    'slots': {
        'welcome': {'label': 'Welcome · the melted box', 'length': '40–50 s'},
        'warmup': {'label': 'Warm-Up · the sealed bag (Clue 1)', 'length': '15–20 s',
                   'script': 'Dr. Nair here! One ice cube, zipped in a bag, sitting on a scale. Drag the bag onto the scale and read the number. Then press Wait an hour. Before you look, call it: what will the scale say now?'},
        'vocab': {'label': 'Word Wall', 'length': '30–45 s'},
        'lesson': {'label': 'The Lesson', 'length': '25–35 s'},
        'part1': {'label': 'Part 1 · call the number first (Clue 2)', 'length': '15–20 s',
                  'script': 'Three changes, three times on the scale. Read the starting number, press the change button, then type your call before you weigh it. No peeking at the answer first. That is how real scientists keep themselves honest.'},
        'part2': {'label': 'Part 2 · the UNDO button (Clue 3)', 'length': '20–30 s',
                  'script': 'Six changes, six undo buttons. Press UNDO and watch. Some come right back. Some are stuck that way forever. Then stamp each card. Keep an eye on the material line at the bottom of every one.'},
        'part3': {'label': 'Part 3 · where did the water go?', 'length': '15–20 s'},
        'explore': {'label': 'Part 4 · the state dial (Clue 4)', 'length': '15–20 s',
                    'script': 'Take the dial all the way up to the stovetop, then all the way back down to the freezer. Watch two readouts the whole time: the mass, and the material. Neither one moves.'},
        'quiz': {'label': 'Self-Check', 'length': '15–20 s'},
        'assignment': {'label': 'Assignment · crack the case', 'length': '20–30 s'},
        'partb': {'label': 'Part B', 'length': '30 s'},
        'partc': {'label': 'Part C · your own change chart', 'length': '30 s'},
        'evidence': {'label': 'Use your evidence · CER', 'length': '15–20 s'},
        'closing': {'label': 'Case closed', 'length': '20–30 s', 'notes': 'Celebrate; tease 30.02, the last lesson (chemical changes).'},
    },
    'videoOff': [],
    'lensVoice': False,
    'camera': {'max': 8, 'huntTitle': 'Bonus: can you snap all 4 shots on this list?', 'missions': [
        'The sealed bag on the scale, after the ice melted (Warm-Up)',
        'A call you got exactly right (The Lesson)',
        'All six cards stamped (The Lesson)',
        'The dial at the top, with the material still reading WATER (The Lesson)']},
    'sketch': {'tip': P['sketch']['tip'], 'prompts': ['The sealed bag on the scale', 'One giant rainbow crayon', 'Ice, water and vapor in one jar'],
               'inline': [{'id': 'partc', 'afterPart': 'C', 'kicker': 'Part C · draw and label two of your changes', 'required': True, 'minLabels': 4,
                           'prompts': ['Draw one change you can undo', 'Draw one that is hard to undo', 'Label the material in each one', 'Add an arrow showing the change']}]},
    'hlCoach': copy.deepcopy(Q['hlCoach']),
    'specimen': {'kicker': 'Specimen collected', 'stamp': 'CASE CLOSED', 'icon': '🖍️', 'name': 'A sliver of the rainbow crayon',
                 'line': 'You cracked Case 30, and a sliver of the giant rainbow crayon goes in your Field Notebook. (A specimen is something a scientist keeps.) Next lesson is the last of the year: changes that really do make something new!'},
    'notebookTitle': 'Unit 7 · Waves, Patterns & Changes',
    'notebook': copy.deepcopy(Q['notebook']) + [{'lesson': '30.01', 'icon': '🖍️', 'name': 'A sliver of the rainbow crayon'}],
    'rankLine': P['rankLine'],
    'lensWin': 'All six words are sorted. The art show thanks you!',
    'inputs': [
        {'id': 'tab1', 'type': 'swap', 'find': {'sel': '.tab-btn[data-tab="vocab"]'}, 'swap': ['📚 Vocabulary', '🌅 Warm-Up']},
        {'id': 'sw-words', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap a card to flip it'},
         'swap': ['<strong>Tap a card to flip it</strong> and read what the word means.', '<strong>Tap a word</strong> to see what it means.']},
        {'id': 'fs-warm', 'type': 'frame', 'find': {'sel': '#tab-vocab .fs-game[data-mod="sealbag"]'},
         'label': 'Warm-Up: the sealed bag', 'q': 'Warm-Up: what the scale said, and what I think is in the bag.', 'title': 'My bag notes', 'compact': True,
         'fields': [{'t': 'Before', 'icon': '⚖️', 'ph': 'The scale said ___ with the ice in it.'},
                    {'t': 'After', 'icon': '💧', 'ph': 'After the ice melted it said ___.'},
                    {'t': 'So', 'icon': '💡', 'ph': 'That tells me ___.'}]},
        {'id': 'fs-partc', 'type': 'frame', 'find': {'sel': '#tab-assignment p', 'text': 'name the material that stays the same'},
         'label': 'Part C: my change chart', 'q': 'Part C: four changes from home, sorted, with the material that stays the same.', 'title': 'My change chart',
         'fields': [{'t': 'I can undo it', 'icon': '↩️', 'ph': '1. ___ → material that stays the same: ___'},
                    {'t': 'I can undo it', 'icon': '↩️', 'ph': '2. ___ → material that stays the same: ___'},
                    {'t': 'Hard to undo', 'icon': '🚫', 'ph': '3. ___ → material that stays the same: ___'},
                    {'t': 'Hard to undo', 'icon': '🚫', 'ph': '4. ___ → material that stays the same: ___'}]},
        {'id': 'fs-cer', 'type': 'cer', 'target': 'cer-4', 'find': {'sel': 'textarea#cer-4'},
         'reminder': 'Claim = what you think is true. Evidence = facts from the lesson that prove it. Reasoning = how the evidence proves your claim.',
         'parts': [{'k': 'C', 't': 'Claim', 'ask': 'Must a change you cannot undo be a chemical change?', 'ph': 'I agree / I disagree because…'},
                   {'k': 'E', 't': 'Evidence', 'ask': 'Two facts from the lesson. Tap them in the planner above, or type them.', 'ph': 'One fact is… Another fact is…', 'rows': 3},
                   {'k': 'R', 't': 'Reasoning', 'ask': 'How do those facts prove your claim?', 'ph': 'This shows that…', 'rows': 3}]},
        {'id': 'relabel', 'type': 'relabel', 'map': {'ans-1': 'Part B · Question 5', 'ans-2': 'Part B · Question 6', 'cer-4': 'Use Your Evidence (CER)'}},
        {'id': 'sw-check', 'type': 'swap', 'find': {'sel': 'p', 'text': 'Tap to toggle'}, 'swap': [' Tap to toggle.', '']},
        {'id': 'sw-circle', 'type': 'swap', 'find': {'sel': '.card-head-title', 'text': 'Revisit Our Key Question'}, 'swap': ['Revisit Our Key Question', 'Back to the Big Question']},
    ],
}
D['hlCoach']['practice'] = {
    'q': 'Practice: tap the 3 to 5 words that matter most in this sentence.',
    'text': 'A physical change can be hard to undo, but the material stays exactly the same.',
    'key': ['physical', 'hard', 'undo', 'material', 'same'],
    'small': ['a', 'can', 'be', 'to', 'but', 'the'],
    'model': 'A scientist might highlight “hard to undo” and “material stays exactly the same”. Those words hold the big idea.'}
D['hlCoach']['tips'][2] = ['🎯', 'Look for answers to the Big Question.', 'Ask yourself: what changed, and what stayed exactly the same?']
D['cues'] = {
    'warmup': [{'at': '^bag', 'sel': '.fs-sb-bag', 'fx': 'pop', 'scroll': True},
               {'at': '^scale', 'sel': '.fs-sb-scale', 'fx': 'point'},
               {'at': '^number', 'sel': '.fs-sb-read', 'fx': 'glow'},
               {'at': '^call', 'sel': '[data-mod="sealbag"] .fs-todo li', 'i': 2, 'fx': 'trace'}],
    'part1': [{'at': '^starting', 'sel': '.fs-cal-read', 'fx': 'pop', 'scroll': True},
              {'at': '^change', 'sel': '.fs-cal-do', 'fx': 'point'},
              {'at': '^type', 'sel': '.fs-cal-pad', 'fx': 'glow'},
              {'at': '^honest', 'sel': '[data-mod="callit"] .fs-why', 'fx': 'trace'}],
    'part2': [{'at': '^six', 'sel': '.fs-und-grid', 'fx': 'pop', 'scroll': True},
              {'at': '^UNDO', 'sel': '.fs-und-btn', 'i': 0, 'fx': 'point'},
              {'at': '^stamp', 'sel': '.fs-und-stamps', 'fx': 'glow'},
              {'at': '^material', 'sel': '.fs-und-mat', 'i': 0, 'fx': 'reveal'}],
    'explore': [{'at': '^dial', 'sel': '.fs-std-dial', 'fx': 'point', 'scroll': True},
                {'at': '^stovetop', 'sel': '.fs-std-stop', 'i': 4, 'fx': 'glow'},
                {'at': '^freezer', 'sel': '.fs-std-stop', 'i': 0, 'fx': 'glow'},
                {'at': '^readouts', 'sel': '.fs-std-out', 'fx': 'pop', 'tag': 'watch these'}],
}
D['cueWords'] = json.load(open('cuewords.json', encoding='utf-8')) if os.path.exists('cuewords.json') else {}
json.dump(D, open('data.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote data.json and fixes.json:', len(F), 'fixes')
# budget counter (oao-audio-budget): G4 science = 1,400 credits per lesson; scripts are written to 95% (1,330). Nothing is generated from week 25 on.
clips = {k: v['script'] for k, v in D['slots'].items() if v.get('script')}
tot = sum(len(t) for t in clips.values())
for k, t in clips.items(): print(f'  {k:10} {len(t):4}')
print(f'this page: {tot} / 1400 credits ({tot/1400:.0%}), scripts only, 0 generated')
assert tot <= 1330
json.dump(clips, open('clip-scripts.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
