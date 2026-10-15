#!/usr/bin/env python3
"""Writes fixes.json for 10.02. Each 'old' must match exactly once in original.html (build_lesson.py checks)."""
import json
F = []
def fix(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

# ---------- fix: manatee numbers + the fake graph (Bethany ticked, 15 Oct 2026) ----------
# FWC synoptic counts are minimum counts: 1,267 in 1991; the 2022 abundance estimate is 8,350–11,730.
fix('fix', 'accuracy: 1991 was a count (a minimum), today is an estimate; the old “over 7,500 today” mixed the two',
    "In 1991, Florida had only about 1,200 manatees. Conservation laws set boat-speed limits, protected springs, and rescued injured manatees. Today the population is over 7,500.",
    "In 1991, scientists counted about 1,200 manatees. Conservation laws set boat-speed limits, protected springs, and rescued injured manatees. Today scientists estimate there are more than 7,500.")
fix('fix', 'accuracy: the fake graph image (it never existed) and its made-up line; the Part 4 chart of real survey flights replaces it',
    r'<div class="lesson-figure scroll-reveal">.*?<div class="lesson-figure-caption">.*?</div>\s*</div>\s*', '', regex=True)
fix('fix', 'accuracy: Q3 stem (count vs. estimate); same answer (A)',
    'The Florida manatee population grew from about 1,200 in 1991 to over 7,500 today. What does this data best support?',
    'Scientists counted about 1,200 Florida manatees in 1991. Today they estimate there are more than 7,500. What does this data best support?')
fix('fix', 'accuracy: the counts jumped up and down; the rise was not steady',
    '🐋 Right! A steady rise over 30 years is strong evidence that conservation work is helping.',
    '🐋 Right! A big rise over 30 years is strong evidence that conservation work is helping.')
fix('cut', 'lean + accuracy: Stop & Reason quoted the 1,200 → 7,500 graph that is gone (one thinking stop per tab: Stop & Think stays)',
    r'<div class="socratic-q">\s*<span class="sq-icon">🧠</span>.*?went from 1,200 to 7,500.*?</div>\s*</div>\s*</div>\s*', '', regex=True)

# ---------- fix: copy-paste leftovers ----------
fix('fix', 'copy-paste leftover: Part C was 9.01’s food chain; the checklist asks for a manatee line graph',
    '🎨 Part C &mdash; Build Your Own Food Chain', '📈 Part C &mdash; Graph the Manatee Data')
fix('fix', 'copy-paste leftover: Part C task from 9.01',
    r'In your science notebook, draw a <strong>new</strong> food chain.*?</p>\s*<p[^>]*>Use colors\. Label every part\.</p>',
    "Make a simple line graph of the manatee data: about <strong>1,200</strong> counted in 1991, and more than <strong>7,500</strong> today. Label both points. Then write one sentence about the trend (which way the numbers go).</p>", regex=True)
fix('fix', 'copy-paste leftover: Reflect asked about a hawk (from 9.01); the lean shape cuts Reflect',
    r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', regex=True)
fix('fix', 'copy-paste leftover: supply list (every lesson lists a sunny window)',
    '<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '')
fix('fix', 'leftover: Q5 pointed to “the diagram”; the stories are now the Part 3 game, and the Everglades one is a place, not a species',
    'Pick one of the four Florida species from the diagram (manatee, python, lionfish, or Everglades wetland).',
    'Pick one of the four Florida stories (manatees, pythons, lionfish, or the Everglades).')
fix('fix', 'leftover: 11.01 is the next lesson, not the next module',
    "Next module, we'll zoom in on the living things themselves — the special structures plants and animals use to survive in Florida ecosystems.",
    "Next lesson, we’ll zoom in on the living things themselves: the special body parts plants and animals use to survive in Florida.")

# ---------- plain language ----------
fix('plain', 'shorter; dash removed',
    "Hold this question in your head as you work. By the end of the lesson, you'll use real Florida data to decide whether an ecosystem is in balance — and back up your answer with evidence.",
    "Keep this question in mind as you work. By the end, you’ll use real Florida numbers to decide whether an ecosystem is in balance, and back up your answer with evidence.")
fix('plain', 'answers go on the page now (the list boxes are right below); the sort game sits above',
    "In your notebook, jot down <strong>three things</strong> a scientist could <em>count or measure</em> in either wetland to tell which one is healthy. Don't guess — name things you could actually write down.",
    "Now list <strong>three things</strong> a scientist could <em>count or measure</em> in either wetland to tell which one is healthy. Name things you could actually write down.")
fix('plain', 'cut filler',
    "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
    "You’ll use these six words all lesson. <strong>Tap a card to flip it</strong> and read what the word means.")
fix('plain', 'shorter, one idea per sentence',
    "<strong>Common misconception:</strong> Some people think only big, dramatic changes count. But ecosystems often shift slowly — a few percent each year for a decade — and the data is the only way to spot it. By the time you can <em>see</em> a problem, it can be hard to fix.",
    "<strong>Watch out:</strong> Some people think only big, sudden changes count. But ecosystems often change slowly, a little each year, and the data is the only way to spot it. By the time you can <em>see</em> a problem, it can be hard to fix.")
fix('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
    "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
    "Do you agree or disagree? Prove it with at least <strong>two pieces of evidence</strong> from today’s lesson.")
fix('plain', 'shorter',
    'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.',
    'All your written answers in one place, so you can copy or download them to turn in on Canvas.')

fix('plain', 'dashes out; shorter',
    "Now imagine all of that humming along — sawgrass growing, grasshoppers munching, frogs hunting, hawks circling, fungi recycling. When the numbers stay roughly steady year after year,",
    "Picture it all working: sawgrass growing, frogs hunting, hawks circling, fungi recycling. When the numbers stay about the same year after year,")
fix('plain', 'dash out', "But when something <em>big</em> shifts — a ", "But when something <em>big</em> changes (a ")
fix('plain', 'dash out', "moves in — the system can tip out of balance.", "moves in), the system can tip out of balance.")
fix('plain', 'shorter, one idea per sentence (same science: decomposers and the cycling of matter)',
    "Those nutrients are then absorbed by plant roots, helping new producers grow &mdash; which feeds consumers &mdash; which eventually die and get broken down again. This is called the <strong>cycling of matter</strong>: the same materials get used over and over in a giant loop. Nothing is wasted! Matter doesn't disappear from an ecosystem &mdash; it just changes form and moves through the cycle again.",
    "Plant roots take in those nutrients, and new producers grow. Consumers eat them, and when they die, decomposers break them down again. This is called the <strong>cycling of matter</strong>: the same materials get used over and over in a giant loop. Matter doesn't disappear from an ecosystem. It just changes form and moves through the cycle again.")
fix('plain', 'dashes out',
    "It's one where the data — populations, variety, water, soil — stays in a working range year after year, even when small things shift.",
    "It's one where the numbers (populations, variety, water, soil) stay in a healthy range year after year, even when small things change.")

# ---------- lean cuts (standing approval) ----------
fix('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', regex=True)
fix('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fix('cut', 'lean: remove the whole Explore tab (the manatee data moves to the Lesson as Part 4 and to Part C)',
    r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', regex=True)
fix('cut', 'lean: the diagram heading becomes Part 3 (the Stamp the Story game replaces the tap diagram)',
    'margin-top:22px;">Four Florida Ecosystem Stories</h3>', 'margin-top:22px;">Part 3 · Four Florida Stories</h3>')
fix('cut', 'lean: Observe & Reason, the “one scientist for 30 years” fact (shaky: FWC teams fly the surveys), the bird-count callout (it runs in February, not spring) and Go Deeper; Part 4 = the old Explore; next button goes to Self-Check',
    r'<div class="socratic-q">\s*<span class="sq-icon">👀</span>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
    '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">Part 4 · Thirty Years of Manatee Counts</h3>\n'
    '      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">Since 1991, scientists in small planes have counted Florida manatees on cold winter mornings, when manatees crowd into warm water. Every dot on the chart below is one real survey flight. One flight can fool you. Thirty years of flights can’t.</p>\n'
    '      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', regex=True)
fix('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Match the Word</p>.*?(?=<p[^>]*>🌿 Part B)', '', regex=True)
fix('cut', 'lean: Part B question 6 removed (Bethany kept 5 and 7)', r'<div class="pq">\s*<span class="pq-num"[^>]*>6</span>.*?</textarea>\s*', '', regex=True)
fix('cut', 'lean: Part B question 7 is now number 6', '<span class="pq-num" style="background:#D4772C;">7</span>', '<span class="pq-num" style="background:#D4772C;">6</span>')
fix('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', regex=True)
fix('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fix('cut', 'lean: no separate Big Question answer (CER is the last writing)',
    r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', regex=True)
fix('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', regex=True)
fix('plain', 'lean: shorter checklist',
    '<strong>Evidence Response:</strong> I made a claim about whether invasive species matter, and supported it with two pieces of evidence from the lesson.',
    '<strong>CER:</strong> My claim about invasive species, two pieces of evidence, and my reasoning.')
fix('cut', 'lean: answers are typed on the page, so one way to turn in (this also drops “explaining your food chain”, a copy-paste leftover)',
    r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', regex=True)

json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(F), 'fixes written')
