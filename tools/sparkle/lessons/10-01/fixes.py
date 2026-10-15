#!/usr/bin/env python3
"""Writes fixes.json for 10.01. Each 'old' must match exactly once in original.html (build_lesson.py checks)."""
import json
F = []
def fix(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

# ---------- fix: science accuracy (Bethany ticked all four groups, 15 Oct 2026) ----------
fix('fix', 'accuracy: oaks are wind-pollinated (no nectar, no bees needed); the bee example moves to the saw palmetto',
    "But a bee visits its flowers and carries pollen — that's ",
    "In spring, the wind carries its pollen from flower to flower — that's ")
fix('fix', 'accuracy: oaks are wind-pollinated (follow-on sentence)',
    "for the soil — that's recycling. Even rain rolling off its leaves matters.</p>",
    "for the soil — that's recycling. (Oaks don't need bees. Bees pollinate other plants, like the saw palmetto that grows under the oak.)</p>")
fix('fix', 'accuracy: the diagram hotspot said a bee pollinates the oak for nectar',
    "When a bee visits an oak flower for nectar, pollen sticks to its fuzzy body. The bee carries that pollen to the next flower it visits. Without pollination, oak trees couldn't make acorns, and most of Florida's flowering plants couldn't make seeds.",
    "Oak flowers have no nectar for bees. Instead, the wind blows their pollen from flower to flower. Without pollination, oak trees couldn't make acorns. Many other Florida plants, like the saw palmetto, need bees to carry their pollen.")
fix('fix', 'accuracy: the diagram showed a bee as the oak’s pollinator',
    '<text x="0" y="6" text-anchor="middle" font-size="34">🐝</text>', '<text x="0" y="6" text-anchor="middle" font-size="34">🌬️</text>')
fix('fix', 'accuracy: the diagram showed a bee as the oak’s pollinator (label)',
    'fill="#A07000">BEE</text>', 'fill="#A07000">WIND</text>')
fix('fix', 'accuracy: diagram description',
    'connected to a squirrel, bee, owl, mushroom, and human', 'connected to a squirrel, the wind, an owl, mushrooms, and a person')
fix('fix', 'accuracy: the lesson picture shows a honeybee pollinating the oak (and its prompt asks for that); removed until a correct one is made',
    r'<div class="lesson-figure scroll-reveal">.*?<div class="lesson-figure-caption">.*?</div>\s*</div>\s*', '', regex=True)
fix('fix', 'accuracy: Q1 (oak flowers are wind-pollinated); same answer (Pollination)',
    'A bee visiting an oak flower is an example of which kind of connection?',
    'A bee visiting a saw palmetto flower is an example of which kind of connection?')
fix('fix', 'accuracy: most Florida oranges set fruit without bees, and “millions of hives” is wrong; Florida blueberries do need bees. Same answer.',
    'If every bee in a Florida orange grove disappeared, the trees would still get plenty of sunlight, water, and soil. So why would the orange harvest drop?',
    'If every bee on a Florida blueberry farm disappeared, the plants would still get plenty of sunlight, water, and soil. So why would the blueberry harvest drop?')
fix('fix', 'accuracy: Q3 oranges → blueberries (same answer, C)',
    'All the bees in a Florida orange grove disappear. Why is the harvest smaller that year?',
    'All the bees on a Florida blueberry farm disappear. Why is the harvest smaller that year?')
fix('fix', 'accuracy: Q3 option A', '<span class="quiz-text">The trees stopped getting sunlight</span>', '<span class="quiz-text">The plants stopped getting sunlight</span>')
fix('fix', 'accuracy: Q3 option C', "<span class=\"quiz-text\">Without pollinators, the trees can't make as many oranges</span>", "<span class=\"quiz-text\">Without pollinators, the plants can't make as many blueberries</span>")
fix('fix', 'accuracy: Q3 feedback', '🍊 Right! No pollinators means most flowers never turn into fruit.', '🫐 Right! No pollinators means most flowers never turn into berries.')
fix('fix', 'accuracy: Q3 feedback', "The trees still have sun, water, and soil.", "The plants still have sun, water, and soil.")

# ---------- fix: copy-paste leftovers ----------
fix('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist asks for an ecosystem web',
    '🎨 Part C &mdash; Build Your Own Food Chain', '🎨 Part C &mdash; Build Your Own Ecosystem Web')
fix('fix', 'copy-paste leftover: Part C task from 9.01',
    r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
    "Pick a Florida place: a beach, a backyard, a pond, or a pine forest. Name at least <strong>five</strong> living things that live there. Then show at least <strong>three different kinds</strong> of connections between them (food, pollination, shelter, nutrients, or human care), and name the kind for each one.</p>", regex=True)
fix('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
    r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', regex=True)
fix('fix', 'copy-paste leftover: supply list (every lesson lists a sunny window)',
    '<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '')

# ---------- plain language ----------
fix('plain', 'shorter; dash removed',
    "Hold this question in your head as you work. By the end of the lesson, you'll be able to name several kinds of connections in a Florida ecosystem — and explain why removing one thing changes many other things.",
    "Keep this question in mind as you work. By the end, you’ll be able to name several kinds of connections in a Florida ecosystem and explain why removing one thing changes many other things.")
fix('plain', 'cut filler',
    "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
    "You’ll use these six words all lesson. <strong>Tap a card to flip it</strong> and read what the word means.")
fix('plain', 'defines “hollow”',
    "A barred owl nests in a hollow in its trunk — that's shelter.", "A barred owl nests in a hollow (a hole) in its trunk — that's shelter.")
fix('plain', 'defines “fungi” and “bacteria” the first time they appear',
    "<strong>Nutrient cycling</strong> — fungi and bacteria breaking down dead leaves and putting nutrients back into the soil.",
    "<strong>Nutrient cycling</strong> — fungi (like mushrooms) and bacteria (living things too small to see) breaking down dead leaves and putting nutrients back into the soil.")
fix('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
    "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
    "Do you agree or disagree? Prove it with at least <strong>two pieces of evidence</strong> from today’s lesson.")
fix('plain', 'shorter',
    'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.',
    'All your written answers in one place, so you can copy or download them to turn in on Canvas.')
fix('plain', 'dash removed; plain words',
    "Next lesson, you'll use real Florida data to decide whether an ecosystem is healthy or out of balance — and figure out what we can do about it.",
    "Next lesson, you’ll use real Florida numbers to decide whether an ecosystem is healthy or out of balance, and what people can do about it.")

fix('plain', 'defines “model”',
    'Build a model of an ecosystem web with at least three kinds of connections',
    'Build a model (a drawing that shows how something works) of an ecosystem web')

# ---------- lean cuts (standing approval) ----------
fix('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', regex=True)
fix('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fix('cut', 'lean: remove the whole Explore tab (the saw palmetto moves to the Lesson as Part 4)',
    r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', regex=True)
fix('cut', 'lean: the old diagram heading becomes Part 3 (the Pull a Thread game replaces the tap diagram)',
    'margin-top:22px;">Explore the Oak Web</h3>', 'margin-top:22px;">Part 3 · Pull a Thread</h3>')
fix('cut', 'lean: Observe & Reason, the caterpillar fact, the orange-grove callout and Go Deeper at the end of the Lesson (they repeat or overstate; the shaky facts go with them); Part 4 = the old Explore; next button goes to Self-Check',
    r'<div class="socratic-q">\s*<span class="sq-icon">👀</span>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
    '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">Part 4 · One Plant, Five Connections</h3>\n'
    '      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">Right next to Dr. Reyes’s oak grows a <strong>saw palmetto</strong>, a short palm with big fan-shaped leaves called fronds. It’s one of the most common plants in Florida, and it is tied to its neighbors in five different ways.</p>\n'
    '      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', regex=True)
fix('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', regex=True)
fix('cut', 'lean: Part B question 6 removed (Bethany kept 5 and 7)', r'<div class="pq">\s*<span class="pq-num"[^>]*>6</span>.*?</textarea>\s*', '', regex=True)
fix('cut', 'lean: Part B question 7 is now number 6', '<span class="pq-num" style="background:#D4772C;">7</span>', '<span class="pq-num" style="background:#D4772C;">6</span>')
fix('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', regex=True)
fix('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fix('cut', 'lean: the sketch is optional, so “every arrow labeled” → each connection named',
    'An ecosystem web with at least five living things, at least three different kinds of connections, and every arrow labeled.',
    'An ecosystem web with at least five living things and three different kinds of connections, each one named.')
fix('cut', 'lean: no separate Big Question answer (CER is the last writing)',
    r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', regex=True)
fix('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', regex=True)
fix('plain', 'lean: shorter checklist',
    '<strong>Evidence Response:</strong> I made a claim about whether ecosystems need small living things, and supported it with two pieces of evidence.',
    '<strong>CER:</strong> My claim, two pieces of evidence, and my reasoning.')
fix('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
    r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', regex=True)

json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(F), 'fixes written')
