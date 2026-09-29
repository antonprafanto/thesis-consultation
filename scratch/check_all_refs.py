import fitz, re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/luthfiah_full_annotated.txt', 'r', encoding='utf-8') as f:
    text = f.read()

dp_pos = text.find('DAFTAR PUSTAKA')
dp_text = text[dp_pos:]

# Find all entries starting with number followed by dot
entries = re.findall(r'\n([0-9]+)\.\s+([^\n]+(?:\n[^\n]+){1,6})', dp_text)
print(f"Total numbered entries found: {len(entries)}")

for num, entry in entries:
    clean_entry = " ".join([l.strip() for l in entry.split('\n') if l.strip()])
    print(f"[{num}] {clean_entry[:100]}...")
