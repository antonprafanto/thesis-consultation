import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/luthfiah_full_annotated.txt', 'r', encoding='utf-8') as f:
    text = f.read()

p43_pos = text.find('--- [PAGE 43] ---')
p61_pos = text.find('--- [PAGE 61] ---')

print(text[p43_pos:p61_pos])
