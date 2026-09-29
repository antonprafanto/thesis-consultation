import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r'C:\Users\anton\Downloads\2309106102_Luthfiah Nur Alifah_Proposal Skripsi.pdf')

def print_page_range(start, end, max_chars=1000):
    for i in range(start-1, end):
        print(f"\n==========================================")
        print(f"=== PAGE {i+1} ===")
        print(f"==========================================")
        txt = doc[i].get_text()
        print(txt[:max_chars])

print_page_range(1, 15)
