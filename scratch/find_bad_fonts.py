import fitz

doc = fitz.open(r'C:\Users\anton\Downloads\2309106102_Luthfiah Nur Alifah_Proposal Skripsi.pdf')

for page_idx, page in enumerate(doc):
    blocks = page.get_text("dict")["blocks"]
    for b in blocks:
        if "lines" in b:
            for l in b["lines"]:
                for s in l["spans"]:
                    font_name = s["font"]
                    if any(bad in font_name for bad in ["Calibri", "Arial"]):
                        print(f"Page {page_idx+1} [Font: {font_name}, size: {s['size']:.1f}]: '{s['text'][:60]}'")
