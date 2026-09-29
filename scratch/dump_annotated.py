import fitz, re

doc = fitz.open(r'C:\Users\anton\Downloads\2309106102_Luthfiah Nur Alifah_Proposal Skripsi.pdf')

full_text = ""
for i, page in enumerate(doc):
    full_text += f"\n--- [PAGE {i+1}] ---\n" + page.get_text()

with open('scratch/luthfiah_full_annotated.txt', 'w', encoding='utf-8') as f:
    f.write(full_text)

print("Saved full annotated text to scratch/luthfiah_full_annotated.txt")
