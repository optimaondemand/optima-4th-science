# Field Station sparkle kit (G4 Science)

Everything needed to sparkle one lesson lives here, so any chat can pick it up. The skill
`g4-sci-sparkle-lesson` says *what* to do and which questions to ask; this file says *how the parts fit*.

| File | What it does | Where it runs |
|---|---|---|
| `build_lesson.py <WW-LL>` | Rebuilds the lesson in place from `lessons/<WW-LL>/original.html` + `fixes.json` + `data.json` (+ `banner.svg`, `video.json`). Writes `data/videos/lesson-<WW-LL>.json` for the Video Studio. Saves `original.html` the first time. | Bethany's computer (stdlib Python) |
| `check_scripts.py <WW-LL>` | Teacher-video scripts: every `[ON SCREEN: …]` cue matches a part or a Word Wall word, every script ≤ 120 spoken words (1 minute). | anywhere |
| `check_lesson.py <WW-LL>` | Headless playthrough at 1150 and 420 px: layer on, `FS_SPARKLE_FAILED` empty, no page errors, no sideways scroll, every answer box reaches Gathered Answers, a hard-word list per tab, screenshots + the text a student reads in `out/<WW-LL>/`. | cloud container (Playwright) in a clone with the new files copied in |
| `lessons/12-01/` | The finished pilot. Copy its shapes. | |
| `lessons/10-01/` | Before/after case, `thread` + `photos` (as a clue) + `ripple` + 5-bin `sort`, Berlese funnel tool. `make.py`/`fixes.py`/`video.py` write its json files. | |

`out/` is scratch. Don't commit it.

## The shared layer
`assets/sparkle/fs-sparkle.js` + `.css` (+ `vendor/html2canvas.min.js`). No lesson content lives in the layer:
every key in `data.json` is optional and each builder runs in `guard()`. A layer change is a change to every
sparkled lesson, so re-run `check_lesson.py` on all of them (`grep -l 'id="fs-data"' lesson-*.html`).

## data.json, key by key (12-01 is the full example)

| Key | What it drives |
|---|---|
| `lesson` "12.01", `week`, `day` 1/2, `guide` crew id, `prefix` "g4sci-12-1", `manifestKey` "12-01" | ids; `prefix` names every audio/video file |
| `paths` | `audio`, `video`, `manifest`, `h2c`, `crew`, `ornaments` (copy from 12-01) |
| `crew` | `{id:{name, role (with its meaning), initials, color, lens, voiceId}}` |
| `expedition` | `{num, title}` header line |
| `banner` | inline SVG (or put it in `banner.svg`) |
| `case` | `{num, title, style ('prints' = before/after photo prints, no night-vision; omit for trail-cam stills), hook, question, how, stills:[{cam,time,tag,img,alt}] (tag = the stamp on the still, default ● REC), stillsCredit, clues:[{id, icon, where, t}] ×4, solve:{title, q, options:[{t, why}, with right:true on the one correct answer]}}`. A game earns the clue whose `id` equals its `clue` key, or its own module name when `clue` is absent (12-01 clue ids: reaction, relay, cams, sort). |
| `reaction` | Warm-Up game (12-01: reaction-time snap test). `{title, todo[], path[{icon,t}], tooSoon, win, why, clue}` |
| `relay` | Put-steps-in-order game, placed after the Lesson paragraph containing `afterText`. `{afterText, title, todo[], why, steps[{icon,t}], miss{index:hint}, win, clue}`. Works for any ordered chain (pathway, life cycle, food chain, process). |
| `cams` | Open-each-case step-through, placed before the lesson diagram. `{kicker, title, todo[], why, stepNames, animals:[{name, sense, cam, time, img, alt, steps[], fact}], win, credit, clue}`. Works for any set of 3–5 real examples. |
| `sort` | Card sort, top of Explore. `{kicker, subject, title, todo[], why, bins[{icon,t}], cards[{t, bin, miss}], win, clue}`. **One card per bin.** A bin with no card can be the "hidden step" students explain themselves. |
| `thread` | Warm-Up web game (10-01): tie each visitor to a center with the right kind of thread (drag a colored thread onto a visitor, or tap both). `{afterText, kicker, title, todo[], why, tapHint, center:{name,img,alt,x,y}, kinds:{key:{t,icon,c}}, visitors:[{id,icon,name,x,y,kind,does,miss:{kind:hint},hint,ok}], win, clue}`. x/y in % of the web box (16:10 on desktop, 4:5 on phones; keep x within 18–82). |
| `ripple` | Pull-a-thread web (10-01), replaces `#tab-lesson .diagram-wrap` (or `replace` selector): pick a pull, predict by tapping nodes, pull, see each effect. `{kicker, title, todo[], why, kinds:{key:{t,c}}, nodes:[{id,icon,name,x,y}], links:[{a,b,kind}], pulls:[{id,btn,why,fx:{nodeId:{s:'hurt'|'grow'|'same',t}}}], win, clue}`. Every effect must be true biology. |
| `photos` | Real photo with tap-to-reveal hotspots + a task, placed after a game (`after` = that game's mod) or after the paragraph holding `afterText`; `clue` makes it one of the four clues. `{id, after, kicker, short, title, todo, why, img, alt, credit, license, hotspots[{n,x,y,label,t}] (x/y in % of the photo), task}` |
| `ambient` | `{icon, label}` for the header sound pill (default 🦗 Marsh sounds) |
| `tool` | Tool of the Week (sims so far: `trailcam` 12-01, `thermometer` (cut), `berlese` 10-01 = `tool.berlese:{title,todo,parts,predict,predictFirst,days,critters,meetWin}`) (only when a real tool fits): `{name, icon, tab, after (CSS selector to place it after), key "<WW>-tool", sim, kicker, teaser, done, why, model, modelCredit, <sim data>}` + a `SIMS.<sim>` function in the layer. `model` = a `.glb` in `assets/models/` shown with model-viewer (`assets/sparkle/vendor/model-viewer-umd.min.js`, loaded only when a student opens it). Shrink every model first: `gltf-transform optimize in.glb out.glb --compress quantize --simplify-ratio 0.35 --simplify-error 0.001 --texture-compress webp --texture-size 1024` (12.01: 10.8 MB → 1.2 MB, looks the same). Without `model`, a Sketchfab embed under manifest key `<WW>-tool` is used. |
| `videoOff` | slots whose recorded video no longer matches the page; hidden until re-recorded (remove the slot from the list when the new take is pushed) |
| `inputs` | On-page answers replacing "write in your notebook": types `list` (`unit`, `addLabel` rename “steps”) `· frame · write · pick · bank · cer · swap · hide · relabel · recap · echo` (see 12-01 for each) |
| `flags`, `minWords`, `hints`, `scholar` | per answer box id: "Your answer needs" chips (wide regex word lists), word counter, 3-rung hint ladder, go-further line |
| `planner` | claim/evidence planner before the CER |
| `quizMiss`, `quizKicker` | Self-Check: why each wrong option is tempting + what to reread |
| `slots` | 16 media slots: `{slot:{label, length, notes, script}}`. `script` = the crew member's walkie-talkie line (ElevenLabs) |
| `camera` | Photo Hunt `{max, missions[], huntTitle}` |
| `sketch`, `hlCoach`, `specimen`, `notebook`, `notebookTitle`, `rankLine`, `lensWin` | sketch pad prompts, highlighter coaching, Field Notebook specimen + the year's list |

## Files a lesson uses
- Crew clips: `assets/audio/guide/<crew>/<prefix>-<slot>.mp3`, Word Lens: `<prefix>-word-<n>.mp3` (n = Word Wall order)
- Teacher videos (Video Studio): `assets/video/teacher/<prefix>-<slot>.mp4` + `.jpg` poster + `.vtt` captions
- Photos: `images/<WW>-<LL>-<name>.jpg` (+ `-original.jpg`); portraits `assets/crew/<id>.png`; ornaments `assets/ornaments/`

## fixes.json
`[{"kind":"fix"|"plain", "why":"…", "old":"exact text", "new":"…", "regex":false}]`, applied in order to
`original.html`; each `old` must appear exactly once (the build stops otherwise). `fix` = accuracy or copy-paste
leftovers (Bethany approved), `plain` = plain-language wording. Never change a question, a correct answer or the task.

## video.json (Video Studio plan)
`{"slots": {slot: {label, length, want, parts:[card or photo], script}}, "pics": {key: {src, cap}}, "other": []}`.
A part is `{"kind":"photo","pic":key,"label":…}` or a card `{"label","tag","title","col","body" | "rows":[[a,b]]}`.
After a change: in the ELA repo run `python3 tools/video_shotlist_science.py`, then open
`tools/video-studio.html?subject=science`.
