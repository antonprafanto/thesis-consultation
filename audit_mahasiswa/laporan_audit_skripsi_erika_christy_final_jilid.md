# 🎓 LAPORAN AUDIT FINAL DRAF SKRIPSI (PRA-JILID / HARD COVER)
## Program Studi S1 Informatika — Fakultas Teknik, Universitas Mulawarman

**Mahasiswa Bimbingan:** Erika Christy Pagili (NIM: 2209106117)  
**Judul Skripsi:** *Perancangan Ulang UI/UX Website PT Bina Karya Nuansa Sejahtera Menggunakan Metode Design Thinking*  
**Dosen Pembimbing I:** Anton Prafanto, S.Kom., M.T.  
**Dosen Pembimbing II:** Prof. Dr. Ir. Anindita Septiarini, S.T., M.Cs., IPU  
**Dosen Penguji I:** Rosmasari, S.Kom., M.T.  
**Dosen Penguji II:** Ramadiani, M.Kom., Ph.D.  
**Status Evaluasi:** **DRAF FINAL PASCA-SIDANG — AUDIT KELAYAKAN JILID (HARD COVER / YUDISIUM)**  
**Berkas yang Diaudit:** `2209106117 ERIKA CHRISTY SKRIPSI.pdf` (158 Halaman)

---

## 📊 1. Ringkasan Eksekutif Hasil Audit

Secara substansi akademik, mahasiswa telah menindaklanjuti sebagian besar revisi sidang pendadaran dengan baik:
- ✅ **Skor SUS telah disinkronkan** menjadi **82** (Excellent / Grade A) di seluruh naskah (Abstrak, Bab IV, Bab V).
- ✅ **Kutipan tidak relevan (*Luo & Dai* dan *Nainggolan*) telah dihapus** dan digantikan referensi yang valid.
- ✅ **Metodologi hantu (*Heuristic Evaluation* & *Benchmarking*) telah dibersihkan** dari Bab II dan Bab III.
- ✅ **Placeholder template Word (`{...}`) telah dibersihkan**.

Namun, sebelum mahasiswa mencetak dan menjilid skripsi (*hard cover*), ditemukan **sejumlah catatan krusial yang WAJIB diperbaiki** agar tidak menjadi temuan cacat formil maupun material saat pengumpulan akhir dan arsip perpustakaan:

| Kategori Temuan | Tingkat Urgensi | Jumlah Temuan | Ringkasan Masalah |
| :--- | :---: | :---: | :--- |
| **Profil User Persona** | 🚨 **Kritis** | 1 | Karyawan PT BKNS usia >50 th masih tertulis "Encuy Santoso" dengan pekerjaan "Mahasiswa". |
| **Inkonsistensi Hitungan Bab IV** | 🚨 **Kritis** | 2 | Rumus Success Rate Desktop tabrakan antara $73/75$ (97,3%) vs $73.5/75$ (98%), dan variabel partisipan pada Defective Rate. |
| **Rujukan Silang Gambar & Caption** | ⚠️ **Tinggi** | 6 | Salah rujukan nomor gambar di teks, duplikasi caption (Gambar 4.23/4.25, 4.29/4.30, 4.34/4.35), lompatan Berita (2). |
| **Halaman Awal & Pengesahan** | ⚠️ **Tinggi** | 3 | Typo gelar Pembimbing II (`M.Cs,. IPU.`), tanda koma salah di Kata Pengantar, judul abstrak beda susunan kata. |
| **Daftar Pustaka & Tipografi** | ℹ️ **Sedang** | 4 | Residual copypaste hak cipta di judul paper Shaktyanti, teks terpecah spasi (*broken space*) akibat convert PDF. |

---

## 🚨 2. Temuan Kritis & Wajib Perbaikan Segera

### 🚨 1. Profil User Persona 1 Masih Belum Diperbaiki (Hal. 63 / Halaman PDF 88)
* **Temuan:**
  Pada **Tabel 4.5 (User Persona)** untuk Persona 1 (Karyawan PT BKNS):
  * **Nama:** `Bapak Encuy Santoso` (masih menggunakan nama panggilan informal).
  * **Usia:** `> 50 tahun`.
  * **Pekerjaan:** **`Mahasiswa`** *(Karyawan internal PT BKNS usia di atas 50 tahun tetapi pekerjaannya tertulis Mahasiswa)*.
* **Tindakan Perbaikan:**
  Ganti menjadi:
  * **Nama:** `Bapak Bambang Santoso` (sesuai nama narasumber wawancara internal).
  * **Usia:** `45 – 50 tahun`.
  * **Pekerjaan:** `Staf Operasional / Karyawan PT BKNS`.

---

### 🚨 2. Tabrakan Angka & Matriks Success Rate Desktop (Hal. 98–99 / PDF 123–124)
* **Temuan Diskrepansi 3 Arah:**
  1. **Teks Halaman 98:** Menyebutkan ada **3 kasus partial success** (*"Responden 4 untuk tugas T5, Responden 6 untuk tugas T3, dan Responden 8 untuk tugas T2"*).
  2. **Tabel 4.7 (Halaman 98):** Responden 4 pada T5 diberi tanda **S** (Success), sehingga di tabel hanya ada **2 kasus partial success** (R6 dan R8).
  3. **Teks di bawah Tabel 4.7:** Menyebutkan *"72 tugas berhasil dan 2 tugas sebagian berhasil"* (Total $72 + 2 = 74$, kurang 1 tugas dari total 75 tugas!).
  4. **Perhitungan Rumus di Halaman 99:**
     $$\text{Success Rate} = \frac{72 + (2 \times 0.5)}{75} \times 100\% = \frac{73.5}{75} \times 100\% = 97,3\%$$
     * $72 + (2 \times 0.5) = 73$ (bukan $73.5$).
     * Nilai $73 / 75 = 97,33\% \approx 97,3\%$.
     * Nilai $73.5 / 75 = 98,0\%$.
     * Teks di bawah rumus menulis: *"...seperti yang ditunjukkan oleh nilai keberhasilan sebesar 98%."*
* **Tindakan Perbaikan:**
  - Jika hasil aktual adalah 72 tugas sukses dan 2 parsial (serta 1 gagal = total 75 tugas), perbaiki baris kedua perhitungan menjadi $= \frac{73}{75} \times 100\% = 97,3\%$.
  - Hapus penulisan $73.5$ dan koreksi kalimat di bawah rumus dari $98\%$ menjadi **$97,3\%$** agar selaras dengan Abstrak dan Bab V Kesimpulan.
  - Sinkronkan isi Tabel 4.7 dan narasi paragrafnya.

---

### 🚨 3. Kekeliruan Penamaan Variabel pada Rumus Defective Rate (Hal. 101 & 104)
* **Temuan:**
  - Rumus umum: $\text{Defective Rate} = \frac{\text{Total Defects}}{\text{Opportunities} \times \text{Total Participants}}$
  - Pada Desktop (Hal. 101): $=\frac{19}{12 \times 74} = 0.0214$ (2,14%). Angka **74** dimasukkan ke variabel `Total Participants` (padahal jumlah partisipan adalah 15 orang, sedangkan 74/75 adalah total *tasks*).
  - Pada Mobile (Hal. 104): $=\frac{266}{14 \times 90} = 0.21111$ (21,11%). Angka **90** dimasukkan ke variabel `Total Participants` (padahal jumlah partisipan adalah 15 orang, sedangkan 90 adalah $15 \times 6$ tugas).
* **Tindakan Perbaikan:**
  - Ubah nama variabel penyebut pada rumus menjadi lebih tepat: $\text{Total Opportunities Across All Tasks}$ atau $(\text{Opportunities} \times \text{Total Tasks Evaluated})$, sehingga tidak membingungkan pembaca saat angka $75$ (atau $90$) dimasukkan ke rumus.

---

## 📐 3. Koreksi Rujukan Silang Gambar & Caption (Bab IV)

| No | Lokasi | Masalah pada Draf Saat Ini | Tindakan Perbaikan |
| :---: | :--- | :--- | :--- |
| 1 | **Hal. 65 (PDF 90)** | Teks menyebut: *"Hasil pemetaan prioritas ditunjukkan pada Gambar 4.9..."* | Ganti rujukan menjadi **Gambar 4.15** (Prioritizing Idea). |
| 2 | **Hal. 74 & 76 (PDF 99 & 101)** | Gambar 4.23 dan Gambar 4.25 sama-sama berjudul *"Wireframe Kegiatan (1)"*. | Gambar 4.23 di Hal. 74 ubah judulnya menjadi **Wireframe Profil (1)** (sesuai narasi teks di atasnya). |
| 3 | **Hal. 80 & 81 (PDF 105 & 106)** | Gambar 4.29 dan Gambar 4.30 sama-sama berjudul *"Wireframe Kontak"*. | Beri nomor pembeda: Gambar 4.29 **Wireframe Kontak (1)** dan Gambar 4.30 **Wireframe Kontak (2)**. |
| 4 | **Hal. 83 (PDF 108)** | Teks menyebut: *"ditunjukkan pada Gambar 4.31..."* padahal membahas High-Fidelity Beranda (2). | Ganti rujukan menjadi **Gambar 4.32**. |
| 5 | **Hal. 85 & 86 (PDF 110 & 111)** | Gambar 4.34 dan Gambar 4.35 sama-sama berjudul *"High-Fidelity Profil (1)"*. | Ubah judul Gambar 4.35 (Hal. 86) menjadi **High-Fidelity Profil (2)**. |
| 6 | **Hal. 89 (PDF 114)** | Gambar 4.38 berjudul *"High-Fidelity Berita (2)"* tanpa ada bagian (1). | Ubah judul Gambar 4.38 menjadi **High-Fidelity Detail Berita** atau **High-Fidelity Berita**. |
| 7 | **Hal. 99, 100, 103, 104** | Tabel hitungan TBE & Defective Rate diberi label **Gambar 4.45 s/d 4.48**. | Formatkan sebagai **Tabel** teks resmi atau berikan keterangan yang sesuai. |

---

## 🏛️ 4. Format Halaman Awal & Pengesahan

1. **Gelar Dosen Pembimbing II pada Lembar Pengesahan (Hal. iii / PDF 4):**
   * **Tertulis:** `Prof. Dr. Ir. Anindita Septiarini, M.Cs,. IPU.`
   * **Koreksi:** `Prof. Dr. Ir. Anindita Septiarini, S.T., M.Cs., IPU` *(perbaiki tanda baca `,.` dan cantumkan gelar `S.T.`)*.
2. **Standardisasi Gelar Dosen Pembimbing I:**
   * Di Lembar Pengesahan: `Anton Prafanto, S.Kom., M.T.`
   * Di Kata Pengantar: `Anton Prafanto, S. Kom., M.T` *(hapus spasi berlebih pada `S.Kom.`)*.
   * Di Abstract Inggris: `Anton Prafanto., S.Kom., M.T` *(hapus titik setelah nama)*.
3. **Penyelarasan Judul Skripsi:**
   * Di Cover & Pengesahan: `PERANCANGAN ULANG DESIGN UI/UX WEBSITE...`
   * Di Abstrak Indonesia (Hal. v): `PERANCANGAN ULANG WEBSITE UI/UX...`
   * *Rekomendasi:* Samakan susunan katanya di seluruh halaman awal menjadi: `PERANCANGAN ULANG UI/UX WEBSITE PT BINA KARYA NUANSA SEJAHTERA MENGGUNAKAN METODE DESIGN THINKING`.
4. **Kata Pengantar (Hal. vii / PDF 8):**
   * Paragraf 1: *"Puji syukur kepada, Tuhan Yang Maha Esa..."* -> Hapus tanda koma setelah kata `kepada`.

---

## 📚 5. Daftar Pustaka & Tipografi (KBBI)

1. **Pembersihan Teks Residual Hak Cipta pada Daftar Pustaka (No. 31 Hal. 118 / PDF 143):**
   * **Tertulis:** *Shaktyanti, F. A., Pradini, R. S., & Kusuma, W. T. (2025). Analisis Usability Website Berbinar Insightful Indonesia Menggunakan USE Questionnaire dan Performance Test **Semua hak dilindungi oleh Lembaga Penelitian dan Pengabdian Masyarakat (LPPM) STMIK Indonesia**...*
   * **Koreksi:** Hapus kalimat hak cipta tersebut dari judul referensi.
2. **Kerapian Format Entri Daftar Pustaka No. 17 (Hal. 117 / PDF 142):**
   * **Tertulis:** `Lemeshow, S., Jr, D. W. H., Klar, J., & Lwanga, S . K. (1990). Adequacy_of_Sample_Size_in_Health_Studie.`
   * **Koreksi:** Hapus tanda garis bawah (*underscore*) dan perbaiki ejaan: *Adequacy of Sample Size in Health Studies*.
3. **Kata Ganti Narasumber Wawancara (Tabel 3.2 Hal. 31 / PDF 56):**
   * Pertanyaan No. 1 masih tertulis: *"...dan seberapa sering **Ibu** menggunakan website perusahaan?"*. Ganti dengan **Bapak** (karena narasumbernya adalah Bapak Bambang Santoso).
4. **Pembersihan Kata Pecah Spasi (*Broken Spaces*) Akibat Export Word ke PDF:**
   * Bersihkan spasi liar di tengah kata:
     * Abstrak (Hal. v): `pe nelitian` $\to$ `penelitian`, `waw ancara` $\to$ `wawancara`, `ya ng` $\to$ `yang`.
     * Abstract (Hal. vi): `System Usabilit y Scale` $\to$ `System Usability Scale`, desimal `97,3%` $\to$ `97.3%`.
     * Hal. 87: `seba gai` $\to$ `sebagai`.
     * Hal. 95: `transparan si` $\to$ `transparansi`, `in gin` $\to$ `ingin`.
     * Hal. 96: `d alam` $\to$ `dalam`, `penguji an` $\to$ `pengujian`.
     * Hal. 100: `bagia n` $\to$ `bagian`.
     * Hal. 103: `kes eluruhan` $\to$ `keseluruhan`.
     * Hal. 104: `peng guna` $\to$ `pengguna`.
     * Hal. 105: `men unjukkan` $\to$ `menunjukkan`, `Tabel 4.1 0` $\to$ `Tabel 4.10`.
     * Hal. 106: `pen gunjung` $\to$ `pengunjung`, `bahw a` $\to$ `bahwa`.
     * Hal. 109: `pen gelolaan` $\to$ `pengelolaan`.
     * Hal. 111: `ya ng` $\to$ `yang`, `dal am` $\to$ `dalam`.
     * Hal. 115 (Saran): `m edia` $\to$ `media`.
5. **Penyempurnaan Redaksi Bab V Saran (Hal. 115 / PDF 140):**
   * Saran 1: *"fitur pendukung seperti pencarian (fitur pencarian)"* $\to$ sederhanakan menjadi *fitur pencarian*.
   * Saran 2: *"website hidup"* $\to$ gunakan istilah baku: *website lingkungan produksi (production/live website)*.

---

## ✅ 6. Checklist Tindakan Mahasiswa Sebelum Jilid Hard Cover

- [ ] **1. User Persona:** Ubah nama "Encuy Santoso" menjadi "Bapak Bambang Santoso" dan pekerjaannya dari "Mahasiswa" menjadi "Staf Operasional/IT PT BKNS" (Tabel 4.5 Hal. 63).
- [ ] **2. Hitungan Success Rate Desktop:** Koreksi langkah pecahan $= \frac{73}{75} \times 100\% = 97,3\%$ (hapus angka $73.5$ dan $98\%$ pada narasi Hal. 99).
- [ ] **3. Rumus Defective Rate:** Sesuaikan penamaan variabel pembagi pada rumus agar tidak tertulis "Total Participants" untuk jumlah tugas (Hal. 101 & 104).
- [ ] **4. Caption & Rujukan Gambar:**
  - [ ] Hal. 65: Ganti rujukan gambar dari 4.9 menjadi **Gambar 4.15**.
  - [ ] Hal. 74: Ganti judul Gambar 4.23 menjadi **Wireframe Profil (1)**.
  - [ ] Hal. 80–81: Beri nomor **Wireframe Kontak (1)** dan **(2)** (Gambar 4.29 & 4.30).
  - [ ] Hal. 83: Ganti rujukan gambar dari 4.31 menjadi **Gambar 4.32**.
  - [ ] Hal. 86: Ganti judul Gambar 4.35 menjadi **High-Fidelity Profil (2)**.
  - [ ] Hal. 89: Ganti judul Gambar 4.38 menjadi **High-Fidelity Detail Berita**.
- [ ] **5. Lembar Pengesahan & Gelar:** Perbaiki penulisan gelar Pembimbing II menjadi `Prof. Dr. Ir. Anindita Septiarini, S.T., M.Cs., IPU` (Hal. iii) dan hilangkan koma pada kalimat pembuka Kata Pengantar (Hal. vii).
- [ ] **6. Daftar Pustaka:** Bersihkan teks hak cipta pada entri Shaktyanti (No. 31) dan hilangkan garis bawah pada Lemeshow (No. 17).
- [ ] **7. Wawancara & Tipografi:** Ganti kata "Ibu" menjadi "Bapak" pada Tabel 3.2 butir 1, perbaiki istilah "website hidup" di Bab V, serta bersihkan kata yang terpecah spasi di seluruh dokumen.
