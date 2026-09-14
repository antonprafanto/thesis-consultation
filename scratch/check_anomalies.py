import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/draft_arkananta.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print('=== PLACEHOLDERS & ANOMALIES ===')
patterns = [
    r'<[^>\n]+>',
    r'\[[^\]\n]+\]',
    r'Error![^\n]+',
    r'\bTabel\s+[0-9]+\.x\b',
    r'\bGambar\s+[0-9]+\.x\b',
    r'\bcontents\b',
    r'\bppt\b',
    r'jago iot',
    r'tercinta',
    r'Berdasarkan Berdasarkan',
    r'https?://[^\s\)]+',
    r'Wapada\b',
    r'SEN0161-V12\b'
]

for pat in patterns:
    matches = list(re.finditer(pat, text, re.IGNORECASE))
    print(f'Pattern "{pat}" matched {len(matches)} times:')
    for m in matches[:10]:
        start = max(0, m.start() - 30)
        end = min(len(text), m.end() + 30)
        snippet = text[start:end].replace('\n', ' ')
        print(f'   -> ...{snippet}...')
