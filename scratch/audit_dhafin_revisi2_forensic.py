import fitz  # PyMuPDF
import re, sys

sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open("audit_mahasiswa/draft_proposal_ahmad_dhafin_revisi_2.pdf")

print(f"Total pages: {len(doc)}")

# 1. Check Page Numbers and their positions on each page
print("\n=== 1. BAB PAGE NUMBERS & POSITIONS ===")
for p in range(len(doc)):
    text = doc[p].get_text()
    bab_match = re.search(r'(BAB\s+[I|V|X]+)', text)
    rect = doc[p].rect
    blocks = doc[p].get_text("blocks")
    bottom_pns = [b for b in blocks if b[3] > rect.height - 70 and re.match(r'^(?:[ivxlcdm]+|\d+)$', b[4].strip(), re.I)]
    top_pns = [b for b in blocks if b[1] < 70 and re.match(r'^(?:[ivxlcdm]+|\d+)$', b[4].strip(), re.I)]
    if bab_match:
        print(f"Page {p+1} ({bab_match.group(1)}): Top={top_pns}, Bottom={bottom_pns}")
    elif p in [13, 14, 20, 34]:
        print(f"Page {p+1} (Continuation): Top={top_pns}, Bottom={bottom_pns}")

# 2. Check Daftar Lampiran & Daftar Istilah
print("\n=== 2. DAFTAR LAMPIRAN & ISTILAH ===")
for p in range(5, 12):
    t = doc[p].get_text()
    if "DAFTAR LAMPIRAN" in t or "DAFTAR ISTILAH" in t:
        print(f"--- Page {p+1} ---")
        print(t[:500])

# 3. Check Subbab in Bab I
print("\n=== 3. BAB I SECTIONS ===")
for p in range(12, 19):
    t = doc[p].get_text()
    matches = re.findall(r'(1\.\d+\s+[^\n]+)', t)
    if matches:
        print(f"Page {p+1}: {matches}")

# 4. Check Equations and labels
print("\n=== 4. EQUATIONS IN BAB 2 & 3 ===")
for p in range(18, 50):
    t = doc[p].get_text()
    if any(k in t for k in ['PanicLevel', '∑', 'IsPanicLevelHigh', 'User Acceptance Testing']):
        lines = t.split('\n')
        for i, line in enumerate(lines):
            if any(k in line for k in ['PanicLevel', '∑', 'IsPanicLevelHigh', 'x̄', 'skor']):
                ctx = '\n'.join(lines[max(0, i-2):min(len(lines), i+4)])
                print(f"Page {p+1}:\n{ctx}\n---")

# 5. Check Daftar Pustaka entries
print("\n=== 5. DAFTAR PUSTAKA ENTRIES ===")
dp_pages = []
for p in range(len(doc)):
    t = doc[p].get_text()
    if "DAFTAR PUSTAKA" in t and p > 35:
        dp_pages.append(p)
    elif dp_pages and p > dp_pages[-1]:
        dp_pages.append(p)

dp_full = ""
for p in dp_pages:
    dp_full += doc[p].get_text() + "\n"

# Split references
raw_entries = re.split(r'\n(?=[A-Z][a-zA-Z\s\.,\-]+,\s+[A-Z])', dp_full)
print(f"Found {len(raw_entries)} potential bibliography entries.")
for i, e in enumerate(raw_entries):
    lines = [l.strip() for l in e.split('\n') if l.strip()]
    if lines:
        header = lines[0]
        # check if it contains Korean
        korean = bool(re.search(r'[\uac00-\ud7a3]', header))
        print(f"[{i+1}] {header[:70]}... (Korean: {korean})")

