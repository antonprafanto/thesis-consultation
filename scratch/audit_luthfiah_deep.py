import fitz, re, sys
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r'C:\Users\anton\Downloads\2309106102_Luthfiah Nur Alifah_Proposal Skripsi.pdf'
doc = fitz.open(pdf_path)

print(f"=== BASIC METRICS ===")
print(f"Total Pages: {len(doc)}")

# 1. Check Page Numbers & Coordinates
print("\n=== PAGE NUMBERING ANALYSIS ===")
page_num_issues = []
for i, page in enumerate(doc):
    page_text = page.get_text()
    lines = [line.strip() for line in page_text.split('\n') if line.strip()]
    if not lines:
        continue
    first_line = lines[0]
    # Check if first line is a page number
    # Let's inspect the position of page numbers on the page
    blocks = page.get_text("blocks")
    top_blocks = [b for b in blocks if b[1] < 100] # near top
    bot_blocks = [b for b in blocks if b[3] > 740] # near bottom
    
    top_text = " | ".join([b[4].strip() for b in top_blocks if b[4].strip()])
    bot_text = " | ".join([b[4].strip() for b in bot_blocks if b[4].strip()])
    
    # print page 1 to 15 page number location
    if i < 15 or i in [32, 33, 52, 53]:
        print(f"Page {i+1}: Top='{top_text[:40]}' | Bottom='{bot_text[:40]}'")

# 2. Extract Headings and Structure
print("\n=== HEADINGS AND SECTIONS ===")
full_text = ""
for page in doc:
    full_text += page.get_text() + "\n"

headings = re.findall(r'(\n(?:BAB\s+[IVX]+|[0-9]+\.[0-9]+(?:\.[0-9]+)?)\s+[^\n]+)', full_text)
for h in headings[:30]:
    print("Heading:", h.strip())

# 3. Analyze Bab I Latar Belakang Paragraphs
print("\n=== BAB I LATAR BELAKANG PARAGRAPHS ===")
# Find text between 1.1 Latar Belakang and 1.2 Rumusan Masalah
p_match = re.search(r'1\.1\s+Latar Belakang\s+(.*?)\s+1\.2\s+Rumusan Masalah', full_text, re.DOTALL)
if p_match:
    bg_text = p_match.group(1).strip()
    # Split paragraphs by double newline or indent
    paras = [p.strip() for p in re.split(r'\n\s*\n', bg_text) if len(p.strip()) > 50]
    print(f"Total Paragraphs in Latar Belakang: {len(paras)}")
    for p_idx, p in enumerate(paras):
        print(f"--- Para {p_idx+1} ({len(p.split())} words) ---")
        print(p[:150] + "...")
else:
    print("Could not isolate Latar Belakang!")

# 4. Check References
print("\n=== DAFTAR PUSTAKA ANALYSIS ===")
dp_match = re.search(r'DAFTAR PUSTAKA\s+(.*)', full_text, re.DOTALL)
if dp_match:
    dp_text = dp_match.group(1).strip()
    # Split references
    # Usually entries start with author name hanging indent
    ref_entries = [r.strip() for r in re.split(r'\n(?=[A-Z][a-zA-Z\s,\.\(\)]+,\s+[0-9]{4}|\n[A-Z])', dp_text) if len(r.strip()) > 20]
    print(f"Estimated references count: {len(ref_entries)}")
    for r_idx, r in enumerate(ref_entries[:10]):
        print(f"Ref {r_idx+1}: {r[:100]}...")
else:
    print("Could not isolate Daftar Pustaka!")
