import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/luthfiah_full_annotated.txt', 'r', encoding='utf-8') as f:
    text = f.read()

p37_pos = text.find('--- [PAGE 37] ---')
p44_pos = text.find('--- [PAGE 44] ---')

print(text[p37_pos:p44_pos])
