import re

with open('scratch/luthfiah_full_annotated.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Isolate body text (pages 11 to 62)
p11 = text.find('--- [PAGE 11] ---')
p63 = text.find('--- [PAGE 63] ---')
body_text = text[p11:p63]
dp_text = text[p63:]

# Find in-text citations like (Author, Year) or Author (Year)
in_text_citations = re.findall(r'([A-Z][a-zA-Z\s&,\.-]+)?\((\d{4}[a-z]?)\)|([A-Z][a-zA-Z]+(?:\s+dkk\.|\s+&\s+[A-Z][a-zA-Z]+)?,\s+\d{4}[a-z]?)', body_text)
print(f"Sample in-text citations matches: {len(in_text_citations)}")

# Let's extract clean citation keys
citations_found = set()
for m in re.finditer(r'\(([A-Z][a-zA-Z\s&,\.-]+?),\s*(\d{4}[a-z]?)\)', body_text):
    author = m.group(1).strip()
    year = m.group(2).strip()
    citations_found.add((author, year))

for m in re.finditer(r'([A-Z][a-zA-Z]+(?:\s+dkk\.|\s+&\s+[A-Z][a-zA-Z]+)?)\s+\((\d{4}[a-z]?)\)', body_text):
    author = m.group(1).strip()
    year = m.group(2).strip()
    citations_found.add((author, year))

print(f"\nUnique (Author, Year) extracted from body: {len(citations_found)}")
for a, y in sorted(citations_found):
    print(f"  {a} ({y})")

# Extract bibliography authors and years
print("\n=== BIBLIOGRAPHY ENTRIES ===")
bib_entries = []
for line in dp_text.split('\n'):
    line = line.strip()
    m = re.match(r'^\d+\.\s+([A-Z][a-zA-Z\s,\.\&\-]+?)\s*\((\d{4}[a-z]?)\)', line)
    if m:
        bib_entries.append((m.group(1).strip(), m.group(2).strip(), line))

print(f"Extracted {len(bib_entries)} bibliography items:")
for b in bib_entries:
    print(f"  {b[0]} ({b[1]})")
