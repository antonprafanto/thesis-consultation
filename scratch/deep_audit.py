import sys, re

sys.stdout.reconfigure(encoding='utf-8')

with open('scratch/draft_arkananta.txt', 'r', encoding='utf-8') as f:
    text = f.read()

print("--- 1. Check judul di Cover, Hal Judul, Pengesahan ---")
for line in text.split('\n')[:80]:
    if 'RANCANG BANGUN' in line or 'MONITORING' in line:
        print(line.strip())

print("\n--- 2. Occurrences of 'monitoring pH' (apakah suhu terlupakan?) ---")
for m in re.finditer(r'.{0,40}monitoring pH.{0,40}', text, re.IGNORECASE):
    print('->', m.group(0).strip().replace('\n', ' '))

print("\n--- 3. Cek Lokasi Penelitian di Bab 3 ---")
p44 = text.split('3.7  Waktu dan Tempat Penelitian')[1].split('DAFTAR PUSTAKA')[0]
print(p44[:600])

print("\n--- 4. Cek Persamaan / Rumus di seluruh naskah ---")
for m in re.finditer(r'.{0,40}(?:\([123]\.\d+\)|Persamaan\s+[123]\.\d+).{0,40}', text, re.IGNORECASE):
    print('->', m.group(0).strip().replace('\n', ' '))

print("\n--- 5. Cek Caption Gambar di Bab 2 dan Bab 3 ---")
for m in re.finditer(r'Gambar\s+[123]\.\s*\d+.*', text, re.IGNORECASE):
    print('->', m.group(0).strip())

print("\n--- 6. Cek Caption Tabel di Bab 2 dan Bab 3 ---")
for m in re.finditer(r'Tabel\s+[123]\.\s*[0-9x]+.*', text, re.IGNORECASE):
    print('->', m.group(0).strip())

