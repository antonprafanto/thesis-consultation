import fitz

doc = fitz.open(r'C:\Users\anton\Downloads\2309106102_Luthfiah Nur Alifah_Proposal Skripsi.pdf')

print("=== MARGINS & BOUNDING BOX ANALYSIS ===")
# Page width and height
p = doc[10] # Bab I page 1
print(f"Page 11 Dimensions: Width={p.rect.width/28.35:.2f}cm, Height={p.rect.height/28.35:.2f}cm")

# Let's inspect text bounding boxes
for page_num in [1, 2, 3, 4, 10, 11, 20]:
    page = doc[page_num]
    rects = [b[:4] for b in page.get_text("blocks") if b[4].strip() and not b[4].strip().isdigit() and b[4].strip() not in ['i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii', 'viii', 'ix']]
    if rects:
        min_x = min(r[0] for r in rects) / 28.35
        max_x = max(r[2] for r in rects) / 28.35
        min_y = min(r[1] for r in rects) / 28.35
        max_y = max(r[3] for r in rects) / 28.35
        left_margin = min_x
        right_margin = (page.rect.width / 28.35) - max_x
        top_margin = min_y
        bot_margin = (page.rect.height / 28.35) - max_y
        print(f"Page {page_num+1}: Left={left_margin:.2f}cm, Right={right_margin:.2f}cm, Top={top_margin:.2f}cm, Bottom={bot_margin:.2f}cm")

print("\n=== FONTS USED IN PDF ===")
fonts = set()
for page in doc:
    for font in page.get_fonts():
        fonts.add(font[3]) # font name
for f in sorted(fonts):
    print("Font:", f)
