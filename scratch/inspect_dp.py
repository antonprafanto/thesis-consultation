import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r'C:\Users\anton\Downloads\2309106102_Luthfiah Nur Alifah_Proposal Skripsi.pdf')

dp_pages = [62, 63, 64] # 0-indexed for pages 63, 64, 65
for p_idx in dp_pages:
    print(f"\n==========================================")
    print(f"=== PAGE {p_idx+1} ===")
    print(f"==========================================")
    print(doc[p_idx].get_text())
