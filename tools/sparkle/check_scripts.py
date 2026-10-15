#!/usr/bin/env python3
"""Check a lesson's teacher-video scripts.   python3 tools/sparkle/check_scripts.py 12-02
Every [ON SCREEN: A · B] token must match a part label (emoji stripped) or a Word Wall word, or be Confetti.
Every script must be 1 minute or less (at most 120 spoken words). Recommended slots need a hand-off line."""
import json, re, sys, os, unicodedata
key = sys.argv[1]; W, L = key.split('-'); WW = str(int(W)).zfill(2)
here = os.path.join('tools', 'sparkle', 'lessons', f'{WW}-{L}')
V = json.load(open(os.path.join(here, 'video.json'), encoding='utf-8'))
orig = open(os.path.join(here, 'original.html'), encoding='utf-8').read() if os.path.exists(os.path.join(here, 'original.html')) else ''
txt = [t.strip() for t in re.sub(r'<[^>]+>', '\n', re.sub(r'<script.*?</script>|<style.*?</style>', '', orig, flags=re.S)).split('\n') if t.strip()]
words = {txt[i - 1].lower() for i, t in enumerate(txt) if t == 'tap to flip' and i}
def norm(s):
    s = ''.join(c for c in s if unicodedata.category(c)[0] in 'LNZ' or c in "'’-")
    return re.sub(r'\s+', ' ', s).strip().lower().replace("'", '’')
bad = 0
for k, s in V['slots'].items():
    labels = {norm(p['label']) for p in s.get('parts', [])}
    toks = [t for c in re.findall(r'\[ON SCREEN:([^\]]*)\]', s.get('script', '')) for t in c.split('·')]
    miss = [t.strip() for t in toks if norm(t) not in labels and norm(t) not in words and norm(t) != 'confetti']
    spoken = re.sub(r'\[ON SCREEN:[^\]]*\]|\([^)]*\)', '', s.get('script', ''))
    n = len(spoken.split()); long = n > 120
    hand = (not s.get('want')) or re.search(r'press listen|walkie', spoken, re.I) or k in ('quiz', 'parta', 'partb', 'partc', 'evidence', 'lesson', 'vocab')
    flag = miss or long or not s.get('script')
    bad += bool(flag)
    print(f"{'✗' if flag else '✓'} {k:11} {n:4} words ~{round(n / 2.3)}s  want={bool(s.get('want'))}" + (f'  UNMATCHED {miss}' if miss else '') + ('  TOO LONG' if long else '') + ('' if hand else '  (no hand-off to the crew member)') + ('  NO SCRIPT' if not s.get('script') else ''))
print('OK' if not bad else f'{bad} slot(s) need fixing'); sys.exit(1 if bad else 0)
