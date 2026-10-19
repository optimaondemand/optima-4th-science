#!/usr/bin/env python3
"""Writes fixes.json for 9.01. Each 'old' must match exactly once in original.html (build_lesson.py checks)."""
import json
F = []
def fix(kind, why, old, new, regex=False):
    e = {'kind': kind, 'why': why, 'old': old, 'new': new}
    if regex: e['regex'] = True
    F.append(e)

# ---------- repair: the stray </div> after the intro-video slot (build_lesson.py's repair looks for "09-01-intro"; this lesson's slot is "9-01-intro") ----------
fix('fix', 'repair: the stray </div> after the intro-video slot',
    r'(?<=</div>\n</div>\n)\s*</div>(?=\s*<div class="activity-card act-warmup)', '\n', regex=True)

# ---------- fix: Bethany ticked all four (18 Oct 2026) ----------
fix('fix', 'supply list: no notebook or colored pencils needed (answers are typed on the page)',
    r'\s*<span class="need-chip"><span>📓</span>Science notebook</span>\s*<span class="need-chip"><span>✏️</span>Colored pencils</span>', '', regex=True)
fix('fix', 'supply list: “a sunny window” is a copy-paste leftover',
    r'\s*<span class="need-chip"><span>🔆</span>A sunny window or memory of one</span>', '', regex=True)
fix('fix', 'accuracy: plants don’t “breathe in” food gas; they take in carbon dioxide (matches the producer box)',
    'pull water up from their roots, and breathe in a gas from the air.',
    'pull water up through their roots, and take in a gas from the air called carbon dioxide.')
fix('fix', 'the Big Question names a gopher tortoise, but the lesson never did',
    'but the energy started in the Sun and traveled through the plant first.</p>',
    'but the energy started in the Sun and traveled through the plant first. A gopher tortoise munches grasses and wildflowers, so its energy started in the Sun too.</p>')
fix('fix', 'the frog in the picture is not a green tree frog: caption and alt text now say “a frog”',
    'alt="Florida wetland food chain showing sun, sawgrass, grasshopper, green tree frog, and red-shouldered hawk connected by labeled energy arrows"',
    'alt="A drawing of a Florida wetland food chain: the Sun, sawgrass, a grasshopper, a frog and a red-shouldered hawk, with an energy arrow between each one"')
fix('fix', 'the frog in the picture is not a green tree frog (caption)',
    "<strong>One energy path:</strong> The Sun's energy moves into a plant, then into each animal that eats. Follow the arrows to trace the path.",
    "<strong>One energy path:</strong> Sun → sawgrass → grasshopper → a frog → hawk. Each arrow shows which way the energy moves.")

# ---------- plain language ----------
fix('plain', 'shorter; dash removed',
    "Hold this question in your head as you work. By the end of the lesson, you'll be able to trace the path of energy from the Sun all the way to an animal — and explain it with evidence from a real Florida food chain.",
    "Keep this question in mind as you work. By the end, you’ll be able to trace energy from the Sun all the way to an animal, and explain it with evidence from a real Florida food chain.")
fix('plain', 'cut filler',
    "These six words show up all through the lesson. <strong>Tap a card to flip it</strong> and read the definition. You don't need to memorize them yet — they'll start sticking as you use them.",
    "You’ll use these six words all lesson. <strong>Tap a card to flip it</strong> and read what the word means.")
fix('plain', 'the warm-up is now the Trace your lunch game (no drawing in a notebook)',
    "<p>In your science notebook, draw what you ate for breakfast or lunch. Pick one item — a piece of bread, a strawberry, scrambled eggs, anything. Now draw an arrow back from that food to where you think it came from <em>before</em> it was on your plate. Keep adding arrows backward as far as you can.</p>",
    "<p>Where did your breakfast or lunch come from <em>before</em> it was on your plate? Pick a food below and follow its energy backward, one step at a time, as far as you can go.</p>")
fix('plain', 'dash removed; “Not a single one” is enough',
    "<strong>animals can't make their own food.</strong> Not a single one. Not a hawk, not a shark, not you.",
    "<strong>animals can't make their own food.</strong> Not a hawk, not a shark, not you.")
fix('plain', 'one idea; dash removed',
    "Then they use the sunlight's energy to put those pieces together and build their own food — sugar.",
    "Then they use the sunlight's energy to put those pieces together and build their own food, a kind of sugar.")
fix('plain', 'shorter',
    "Producers are the doorway. They are the only living things on land that can grab energy directly from the Sun and turn it into something you can eat.",
    "Producers are the doorway: they catch energy from the Sun and turn it into food that animals can eat.")
fix('plain', 'shorter; dashes removed; defines minerals',
    "Producers can't make food from sunlight alone &mdash; they need four key inputs: <strong>sunlight</strong> (energy), <strong>water</strong> (pulled up through roots), <strong>carbon dioxide from the air</strong> (absorbed through tiny pores in their leaves), and <strong>minerals from the soil</strong> (like nitrogen and phosphorus that help them grow). Take away any one of these and the plant can't produce food &mdash; which means the entire food chain above it would collapse!",
    "Producers need four things: <strong>sunlight</strong> (the energy), <strong>water</strong> (pulled up through their roots), <strong>carbon dioxide from the air</strong> (taken in through tiny holes in their leaves), and <strong>minerals from the soil</strong> (nutrients like nitrogen that help them grow). Take away any one, and the plant can’t make enough food. Then every animal that depends on it goes hungry.")
fix('plain', 'clearer subtitle', 'Pull on the thread before we trace the path', 'Follow your food back to the start')
fix('plain', 'cut filler', 'Plants do something amazing. They take in sunlight', 'Plants take in sunlight')
fix('plain', 'dash removed', 'are both <span class="vtip">consumers<span class="vtip-box"><span class="vtip-word">Consumer</span>A living thing that gets its energy by eating other living things.</span></span> — but the energy', 'are both <span class="vtip">consumers<span class="vtip-box"><span class="vtip-word">Consumer</span>A living thing that gets its energy by eating other living things.</span></span>, but the energy')
fix('plain', 'defines “ecosystem” the first time it appears', 'Every Florida ecosystem has these three roles in some form.', 'Every Florida ecosystem (a place where living things and their surroundings work together) has these three roles.')
fix('plain', 'dash removed from the quote (same meaning)', "Plants don't really need sunlight — they get their food from the soil.", "Plants don't really need sunlight. They get their food from the soil.")
fix('cut', 'lean: the Key Concept box repeats Part 2', r'<div style="background:#FFF6E5;border:2.5px solid #F0C97A;[^"]*">\s*<div[^>]*>⭐ Key Concept</div>\s*<p[^>]*>.*?</p>\s*</div>\s*', '', regex=True)
fix('plain', 'shorter CER directions (the C/E/R boxes explain each part)',
    "Write a short argument explaining whether you agree or disagree. Use at least <strong>two pieces of evidence</strong> from today's lesson to support your claim.",
    "Do you agree or disagree? Prove it with at least <strong>two pieces of evidence</strong> from today’s lesson.")
fix('plain', 'shorter',
    'All of your written responses — gathered in one place so you can copy or download them for Canvas turn-in.',
    'All your written answers in one place, so you can copy or download them to turn in on Canvas.')
fix('plain', 'the closing tooltip on “Sun” showed the Energy definition; plain words, no dash',
    r"<p><strong>Nicely done\.</strong> You can now trace energy from the <span class=\"vtip\">Sun.*?Next lesson, we'll dig into what happens when something goes missing from the chain\.</p>",
    "<p><strong>Nicely done.</strong> You can now trace energy from the Sun all the way to a consumer, and explain why every animal in Florida is sun-powered. Next lesson: what happens when something goes missing from the chain?</p>", regex=True)

# ---------- lean cuts (standing approval) ----------
fix('cut', 'lean: no Explore tab button', r'\s*<button class="tab-btn" data-tab="explore"[^>]*>.*?</button>', '', regex=True)
fix('cut', 'lean: tab order without Explore', "var TAB_ORDER = ['vocab','lesson','explore','quiz','assignment'];", "var TAB_ORDER = ['vocab','lesson','quiz','assignment'];")
fix('cut', 'lean: remove the whole Explore tab (building the food chain moves to the Lesson as Part 4; its shaky 1-in-10 fact goes with it)',
    r'<!-- ═+ -->\s*<!-- TAB 3: GUIDED EXPLORATION\s*-->\s*<!-- ═+ -->\s*<div class="tab-panel" id="tab-explore">.*?(?=<!-- ═+ -->\s*<!-- TAB 4)', '', regex=True)
fix('cut', 'lean: one thinking stop per tab (Stop & Reason after the model stays)',
    r'<div class="socratic-q">\s*<span class="sq-icon">🛑</span>\s*<div>\s*<div class="label">Stop &amp; Think</div>.*?</div>\s*</div>\s*</div>\s*', '', regex=True)
fix('cut', 'lean: the diagram heading becomes Part 3',
    'margin-top:22px;">Three Roles in Every Ecosystem</h3>', 'margin-top:22px;">Part 3 · Three Roles in Every Ecosystem</h3>')
fix('cut', 'lean: Observe & Reason, the sawgrass fact (it said no soil is needed, which the producer box contradicts), the Everglades callout and Go Deeper; Part 4 = the old Explore; next button goes to Self-Check',
    r'<div class="socratic-q">\s*<span class="sq-icon">👀</span>.*?<div class="tab-next-wrap">\s*<button class="tab-next-btn" onclick="switchTab\(\'explore\'\)">Continue to 🔬 Explore →</button>',
    '<h3 style="font-size:22px;color:#0E1C42;font-weight:900;margin-bottom:10px;margin-top:22px;">Part 4 · Build the Hawk’s Food Chain</h3>\n'
    '      <p style="font-size:16px;color:#5A4D3E;margin-bottom:18px;">Dr. Reyes watched the hawk at post 7 for a week. She saw it catch a green tree frog, and she saw frogs like that one eat grasshoppers that munch on sawgrass. Build the food chain that carried the Sun’s energy all the way to the hawk.</p>\n'
    '      <div class="tab-next-wrap">\n        <button class="tab-next-btn" onclick="switchTab(\'quiz\')">Continue to 🧠 Self-Check →</button>', regex=True)
fix('cut', 'lean: no Part A word bank', r'<p[^>]*>🔍 Part A &mdash; Label the Energy-Flow Diagram</p>.*?(?=<p[^>]*>🌿 Part B)', '', regex=True)
fix('cut', 'lean: Part B question 6 removed (Bethany kept 5 and 7; losing the sawgrass is 9.02’s topic)', r'<div class="pq">\s*<span class="pq-num"[^>]*>6</span>.*?</textarea>\s*', '', regex=True)
fix('cut', 'lean: Part B question 7 is now number 6', '<span class="pq-num" style="background:#D4772C;">7</span>', '<span class="pq-num" style="background:#D4772C;">6</span>')
fix('cut', 'lean: Part C typed on the page (the drawing is a bonus)',
    r"In your science notebook, draw a <strong>new</strong> food chain — different from the one in the lesson\. It can be from a Florida beach, a backyard, a pond, or a pine forest\. Include: <strong>the Sun · one producer · two consumers · labeled energy arrows between each</strong>\.</p>\s*<p[^>]*>Use colors\. Label every part\.</p>",
    "Make a new food chain, different from the one in the lesson. It can be from a Florida beach, a backyard, a pond, or a pine forest. Include <strong>the Sun, one producer, two consumers, and how the energy moves</strong> between them.</p>", regex=True)
fix('cut', 'lean: no Reflect (it also repeated the hawk question)',
    r'<div class="socratic-q">\s*<span class="sq-icon">🤔</span>\s*<div>\s*<div class="label">Reflect</div>.*?</div>\s*</div>\s*</div>\s*', '', regex=True)
fix('cut', 'lean: checklist without Part A', r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Part A:</strong>.*?</div>\s*', '', regex=True)
fix('cut', 'lean: Part B has 2 questions', 'Questions 5, 6, and 7 answered', 'Questions 5 and 6 answered')
fix('cut', 'lean: Part C typed on the page; the sketch is a bonus',
    'A food chain with the Sun, one producer, two consumers, and labeled energy arrows.',
    'A new food chain with the Sun, one producer, two consumers, and how the energy moves.')
fix('cut', 'lean: no separate Big Question answer',
    r'<div class="checklist-item"[^>]*>\s*<span class="check-icon"[^>]*>☐</span>\s*<span[^>]*><strong>Key Question Response:</strong>.*?</div>\s*', '', regex=True)
fix('cut', 'lean: no separate Big Question answer', r"<p>Now that you've finished the lesson, write a <strong>2–3 sentence answer</strong>.*?</p>\s*", '', regex=True)
fix('plain', 'lean: shorter checklist',
    '<strong>Evidence Response:</strong> I made a claim about plants and sunlight and backed it up with two pieces of evidence.',
    '<strong>CER:</strong> My claim, two pieces of evidence, and my reasoning.')
fix('cut', 'lean: answers are typed on the page, so one way to turn in (drops the video option)',
    r'Submit your work however works best for you:<br/><br/>.*?(?=\s*</div>\s*</div>)', 'Copy or download your Gathered Answers (above) and paste them into the Canvas assignment.', regex=True)

json.dump(F, open('fixes.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(F), 'fixes written')
