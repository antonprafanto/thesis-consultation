# 📋 LAPORAN AUDIT FORENSIK & EVALUASI SIDANG PENDADARAN SKRIPSI

**Mahasiswa Bimbingan:** Erika Christy Pagili (NIM: 2209106117)  
**Program Studi:** S1 Informatika, Fakultas Teknik, Universitas Mulawarman  
**Dosen Pembimbing I:** Anton Prafanto, S.Kom., M.T.  
**Dosen Pembimbing II:** Prof. Dr. Ir. Anindita Septiarini, S.T., M.Cs., IPU  
**Dosen Penguji I:** Rosmasari, S.Kom., M.T.  
**Dosen Penguji II:** Ramadiani, M.Kom., Ph.D.  
**Judul Skripsi:** *Perancangan Ulang Design UI/UX Website PT Bina Karya Nuansa Sejahtera Menggunakan Metode Design Thinking*  
**Status Evaluasi:** **DRAF SIDANG PENDADARAN — WAJIB REVISI KRUSIAL SEBELUM YUDISIUM**

---

## ⚖️ 1. Resume Evaluasi Akademik Umum

Secara keseluruhan, penelitian ini telah menerapkan alur kerja **Design Thinking (Empathize, Define, Ideate, Prototype, Test)** secara lengkap untuk merancang purwarupa (*interactive high-fidelity prototype*) website PT BKNS pada platform Figma dan mengujinya menggunakan Maze serta System Usability Scale (SUS).

Namun, dari hasil audit forensik dokumen draf (160 halaman), ditemukan sejumlah **kesalahan fatal (*critical red flags*)**, **inkonsistensi data kuantitatif antar-bab**, **sitasi paper yang tidak relevan (disparitas bidang ilmu)**, **metodologi yang dijanjikan namun tidak disajikan hasilnya**, serta **cacat format dan teks rujukan silang**.

---

## 🚨 2. Temuan Kritis (*Critical Red Flags*) & Inkonsistensi Data

### 🚨 RED FLAG 1: Tabrakan / Diskrepansi Angka Kuantitatif Lintas Bab (FATAL!)
Terdapat kontradiksi data kuantitatif yang sangat mencolok antara Bab IV (Hasil), Abstrak, dan Bab V (Kesimpulan):

| Indikator Evaluasi | Bab IV (Hasil & Perhitungan Aktual) | Abstrak (Hal. v–vi / 6–7) | Bab V (Kesimpulan Hal. 115 / 140) |
| :--- | :--- | :--- | :--- |
| **Skor SUS Akhir** | **82** (Total skor 2.477 / 30 = **82,57**) *(Hal. 106, 112, 113, 114)* | *Tidak dicantumkan* | **88,17** *(Hal. 115 Poin 2)* |
| **Success Rate Desktop** | **98,0%** ((72 + 3 × 0.5) / 75 × 100%) *(Hal. 99)* | **92,9%** | **92,9%** |
| **Success Rate Mobile** | **98,89%** ((88 + 2 × 0.5) / 90 × 100%) *(Hal. 103)* | **96,7%** | **96,7%** |

* **Dampak:** Di sidang, penguji akan menanyakan dari mana angka SUS 88,17 dan angka Success Rate 92,9% / 96,7% tersebut berasal jika perhitungan di Bab IV menghasilkan angka yang berbeda.
* **Solusi Wajib:** Sinkronkan seluruh data di Abstrak dan Bab V Kesimpulan agar tepat 100% mengikuti perhitungan empiris Bab IV dan Lampiran 20.

---

### 🚨 RED FLAG 2: Teks Abstrak Terpotong / Cacat Kalimat (*Corrupted Text*)
* **Abstrak Bahasa Indonesia (Halaman v / 6):**
  > *"...waktu penyelesaian tugas yang relatif singkat, dan tingkat kesalahan sebesar **[HILANG/TERPOTONG]** Hasil penelitian menunjukkan bahwa menggunakan metode Design Thinking..."*
* **Abstract Bahasa Inggris (Halaman vi / 7):**
  > *"...relatively short task completion times, and an error rate of **[HILANG/TERPOTONG]** The research results indicate that using the Design Thinking method..."*
* **Solusi Wajib:** Masukkan angka *error rate* (Defective Rate: 0,155 pada desktop dan 0,211 pada mobile) serta cantumkan skor akhir SUS di dalam abstrak.

---

### 🚨 RED FLAG 3: Salah Sitasi Konsep Dasar UX yang Fatal (*AI / Literature Hallucination*)
* **Sitasi Metrik UX Task Success Rate (Bab 2 Hal. 23 & Hal. 118 no. 15):**
  Mahasiswa mengutip `(Luo & Dai, 2024)` untuk rumus *Task Success Rate* antarmuka. Di Daftar Pustaka no. 15:
  > *Luo, Z., & Dai, X. (2024). Reinforcement learning-based computation offloading in edge computing: Principles, methods, challenges. Alexandria Engineering Journal, 108, 89–107.*
  *Paper ini membahas komputasi server cloud & edge computing, **bukan metrik usability interaksi manusia!***
* **Sitasi Rumus Lemeshow (Bab 3 Hal. 34/59 & Hal. 119 no. 18):**
  Mahasiswa mengutip `(Nainggolan & Dewantara, 2023)`. Di Daftar Pustaka no. 18:
  > *Nainggolan, H., & Dewantara, R. (2023). DAMPAK PROMOSI ONLINE SERTA MUTU LAYANAN PENGIRIMAN KEPADA LOYALITAS KONSUMEN TERHADAP APLIKASI GRAB.*
  *Paper evaluasi kepuasan kurir pengiriman Grab dikutip sebagai rujukan rumus penentuan ukuran sampel Lemeshow.*
* **Solusi Wajib:** Ganti dengan referensi standar HCI/UX (misalnya: *Albert & Tullis, Measuring the User Experience*, atau *ISO 9241-11*) dan buku teks statistik / manual WHO untuk Lemeshow.

---

### 🚨 RED FLAG 4: Metodologi "Hantu" (*Phantom Methods*) di Bab 2 & 3 vs Bab 4
* Di Bab II (Subbab 2.13 & 2.14) dan Bab III (Subbab 3.6.4 & 3.6.5), mahasiswa resmi menjabarkan teori dan langkah penelitian mengenai:
  1. **Benchmarking Website Kompetitor**
  2. **Heuristic Evaluation (10 Prinsip Jakob Nielsen)**
* **Kenyataan di Bab IV:** **Sama sekali TIDAK ADA hasil, data, tabel perbandingan, ataupun pembahasan terkait Benchmarking dan Heuristic Evaluation.**
* **Solusi Wajib:** Mahasiswa harus memilih: menyajikan hasil analisis benchmarking & heuristic di Bab IV, atau menghapus kedua subbab tersebut dari Bab II dan Bab III jika memang tidak dieksekusi.

---

### 🚨 RED FLAG 5: Diskrepansi & Missing References di Daftar Pustaka
* **Disitasi di Teks, tetapi TIDAK ADA di Daftar Pustaka:**
  * `Akbar & Herdiansyah (2025)` *(Dikutip di Bab 3 Hal. 35/60)*
  * `Sari, Fajar, & Arianti (2023)` *(Dikutip di Bab 3 Hal. 35/60)*
* **Ada di Daftar Pustaka, tetapi TIDAK PERNAH Dikutip di Teks:**
  * *Coding Studio (2023)* (No. 6)
  * *Dicoding Intern (2021)* (No. 9)
  * *Meilinaeka (2024)* (No. 17)
  * *Sugiyono (2013)* (No. 33)
* **Ketidaksesuaian Judul Makalah di Tinjauan Pustaka:**
  * Di Tabel 2.1 No. 10 (Hal. 38), tertulis: *“Shaktyanti et al. (2025) ... Website Desa Banyuanyar”*, padahal judul asli di Daftar Pustaka No. 31 adalah *“Website Berbinar Insightful Indonesia”*.

---

### 🚨 RED FLAG 6: Pesan Galat *Error! Bookmark not defined* pada Daftar Tabel
* Pada **Halaman xi (Daftar Tabel)** tercetak teks galat *broken cross-reference* Microsoft Word:
  * `Tabel 4.10 Tabel Perhitungan Kuesioner SUS .............. Error! Bookmark not defined.`
  * `Tabel 4.11 Tabel Interpretasi SUS ................................. Error! Bookmark not defined.`
* Tabel Ringkasan Hasil Wawancara Sesudah Redesign (Bab 4 Hal. 108/133) **tidak tercantum** di Daftar Tabel.

---

### 🚨 RED FLAG 7: Teks Panduan Template Belum Dihapus
* **Halaman Pernyataan Keaslian (Hal. ii / 3):** `Samarinda, {tgl bln ttd} 2026`
* **Halaman Pengesahan (Hal. iii / 4):** `{tanggal bulan tahun pendadaran}` dan `{tanggal bulan tahun; min. 1 minggu setelah pendadaran}`
* **Halaman Persembahan (Hal. iv / 5):**
  > *Persembahan untuk ... {Font Monotype Corsiva 12pt; Typeface Bold; Rata Kiri Bawah (Align Bottom Left); Maks. 1/3 dari halaman a.k.a. teks tidak sampai tengah-tengah kertas}*
* **Kata Pengantar (Hal. vii / 8):** `Samarinda, {tgl pdd} 2026`

---

## 🛠️ 3. Audit Metodologis & Keputusan Desain

### 1. Kejanggalan User Persona (Tabel 4.5 Hal. 64 / 89)
* **Persona 1 (Karyawan PT BKNS):**
  * Nama: `Encuy Santoso` (nama tidak formal / *nickname*).
  * Usia: `> 50 tahun`.
  * Pekerjaan: **`Mahasiswa`** (*Karyawan PT BKNS usia >50 tahun tetapi pekerjaannya tertulis Mahasiswa*).
  * Pain Point: Tertulis *"belum updaete"* (*typo*).
* **Perbaikan:** Ubah nama dan pekerjaan menjadi realistis (misal: Bambang Santoso, Usia 45-50 tahun, Pekerjaan Staf Operasional PT BKNS).

### 2. Justifikasi Rumus Lemeshow dengan Margin of Error Ekstrem ($d = 18\%$)
* Rumus: $n = \frac{1,96^2 \times 0,5 \times 0,5}{0,18^2} = \frac{0,9604}{0,0324} = 29,64 \approx 30$.
* Penggunaan $d=18\%$ adalah bentuk *reverse engineering* agar mendapatkan angka 30. Dalam riset usability, sampel $n=30$ dijustifikasi dengan *Central Limit Theorem* (CLT) untuk pengujian kuantitatif SUS atau referensi Tullis & Albert, bukan memaksakan rumus survei populasi tak terbatas Lemeshow dengan margin error 18%.

### 3. Asumsi 14 *Opportunities* pada Defective Rate
* Pada Desktop (5 tugas, 15 user) dan Mobile (6 tugas, 15 user), mahasiswa sama-sama menetapkan nilai $Opportunities = 14$. Mahasiswa wajib merinci apa saja 14 titik aksi ideal (jalur klik) per skenario tugas tersebut.

### 4. Tidak Ada Pre-Test Usability (Website Lama)
* Pada Tabel 4.12 perbandingan sebelum vs sesudah: *Usability Sebelum: "Belum pernah dievaluasi"*. Akibatnya, klaim peningkatan kepuasan murni berbasis perbandingan kualitatif, bukan komparasi skor SUS sebelum vs sesudah.

### 5. Ketiadaan Iterasi Desain Mobile (Siklus Design Thinking)
* Pada pengujian mobile, Tugas T2 mengalami **141 kesalahan (*defects/misclicks*)**. Sesuai filosofi *Design Thinking* yang iteratif, kegagalan desain ini seharusnya diikuti perbaikan purwarupa pada iterasi berikutnya.

---

## 📐 4. Cacat Rujukan Silang (*Cross-Reference*), Gambar, & Tabel

1. **Tabel yang Dilabeli sebagai Gambar Tangkapan Layar:**
   * Halaman 100/125: **Gambar 4.45** (*Tabel Perhitungan TBE*)
   * Halaman 101/126: **Gambar 4.46** (*Tabel Perhitungan Defective Rate*)
   * Halaman 104/129: **Gambar 4.47** (*Tabel Perhitungan TBE Mobile*)
   * Halaman 105/130: **Gambar 4.48** (*Tabel Perhitungan Defective Rate Mobile*)
   *(Harus disajikan sebagai Tabel teks berformat resmi, bukan screenshot yang diberi nomor Gambar).*

2. **Salah Rujukan Nomor Gambar / Tabel di Batang Tubuh:**
   * **Hal. 45/70:** Teks menyebut *"seperti pada Tabel 3.1"*, padahal tabel instrumen SUS adalah **Tabel 3.4**.
   * **Hal. 62/87:** Teks menyebut *"Gambar 4.7 merupakan visualisasi affinity mapping"*, padahal Affinity Mapping ada di **Gambar 4.13**.
   * **Hal. 74/99 vs 75/100:** Teks menyebut *"Gambar 4.23 wireframe menu kedua Profil..."*, tetapi judul Gambar 4.23 tertulis *"Wireframe Kegiatan (1)"*.
   * **Hal. 78/103:** Teks menyebut *"Wireframe karier seperti pada Gambar 4.21..."*, padahal Gambar 4.21 adalah *Wireframe Beranda (2)* (Karier adalah Gambar 4.27).
   * **Hal. 84/109:** Teks menyebut *"ditunjukkan pada Gambar 4.26..."*, padahal yang dibahas adalah *Hi-Fi Beranda (2)* (Gambar 4.32).
   * **Hal. 113/138:** Teks menyebut *"dapat dilihat pada Tabel 4.11"*, padahal tabel perbandingan di bawahnya bernomor **Tabel 4.12**.

3. **Duplikasi & Kerancuan Judul Gambar:**
   * Gambar 4.23 & Gambar 4.25 sama-sama berjudul *"Wireframe Kegiatan (1)"*.
   * Gambar 4.34 & Gambar 4.35 sama-sama berjudul *"High-Fidelity Profil (1)"*.
   * Gambar 4.29 & Gambar 4.30 sama-sama berjudul *"Wireframe Kontak"*.
   * **Hal. 90/115:** Gambar 4.38 berjudul *"High-Fidelity Berita (2)"*, tetapi tidak ada *"High-Fidelity Berita (1)"*.
   * **Hal. 95/120 alinea pertama:** Teks terpotong diawali angka *"4.42. Bagian ini memberikan..."* (kata *"Gambar"* hilang).

---

## ✍️ 5. Tipografi, Tata Bahasa, & Istilah Baku

1. **Kata Ganti Wawancara Tertukar (Tabel 3.2 Hal. 32–33 / 57–58):**
   * Narasumber adalah **Bapak Bambang Santoso**, tetapi pada pertanyaan nomor 1 dan 7 tertulis:
     * *"...seberapa sering **Ibu** menggunakan website perusahaan?"*
     * *"...apa harapan **Ibu** terhadap perancangan ulangnya?"*
2. **Salah Ketik (*Typos*) di Batang Tubuh:**
   * Hal. 43/68: `kualitasi` -> kualitas.
   * Hal. 63/88: `Tampolan` -> Tampilan.
   * Hal. 64/89: `updaete` -> update.
   * Hal. 116/141 (Saran 1): Redundansi kata: *“fitur pendukung seperti pencarian (fitur pencarian)”*.
   * Hal. 116/141 (Saran 2): Istilah *“website hidup”* -> gunakan istilah baku: *website produksi / live environment*.
   * Kata Pengantar Hal. vii: *\"Puji syukur kepada, Tuhan Yang Maha Esa...\"* (koma salah tempat).
3. **Redundansi Judul:** *"PERANCANGAN ULANG DESIGN UI/UX"* -> Kata *"Perancangan Ulang"* dan *"Design"* bermakna ganda. Disarankan diubah menjadi: *"PERANCANGAN ULANG UI/UX WEBSITE..."*.
4. **Standardisasi KBBI:** Inkonsistensi penulisan *"Karir"* (tidak baku) vs *"Karier"* (baku KBBI).
5. **Format Kesimpulan Bab V:** Butir ke-3 (mengenai UX Metrics) tidak memiliki nomor list `3)`.

---

## 🎯 6. Daftar Pertanyaan Ujian Sidang Pendadaran

### A. Integritas Data & Validitas Hasil
1. *"Coba jelaskan mengapa terjadi diskrepansi data: di Bab IV rata-rata skor SUS adalah **82**, namun di Bab V Kesimpulan Anda menuliskan **88,17**? Mana angka yang benar dan bagaimana perhitungannya?"*
2. *"Pada Task Success Rate, Bab IV menghitung **98%** (desktop) dan **98,89%** (mobile), tetapi di Abstrak dan Kesimpulan Anda menulis **92,9%** dan **96,7%**. Mengapa terjadi perbedaan data ini?"*
3. *"Mengapa kalimat tingkat kesalahan (error rate) pada Abstrak Bahasa Indonesia dan Bahasa Inggris terputus di tengah jalan?"*

### B. Metodologi & Desain UI/UX
4. *"Di Bab II dan Bab III Anda menjabarkan metode Benchmarking Kompetitor dan Heuristic Evaluation. Mengapa di Bab IV sama sekali tidak ada data dan pembahasannya?"*
5. *"Pada pengujian Maze versi mobile, Tugas T2 menghasilkan 141 error (sangat tinggi). Mengapa tingkat kesalahan pada tugas tersebut sangat tinggi dan mengapa Anda tidak melakukan iterasi desain perbaikan?"*
6. *"Pada tabel User Persona (Tabel 4.5), Anda mencantumkan Persona 1 'Karyawan PT BKNS bernama Encuy Santoso, usia >50 tahun, pekerjaan Mahasiswa'. Bagaimana Anda menjelaskan profil ini?"*
7. *"Mengapa Anda memilih toleransi kesalahan (margin of error) sebesar 18% pada rumus Lemeshow? Apa landasan ilmiahnya?"*

### C. Pemahaman Rujukan Ilmiah
8. *"Pada halaman 23 dan Daftar Pustaka no. 15, Anda mengutip paper Luo & Dai (2024) mengenai 'computation offloading in edge computing' untuk definisi Task Success Rate UX. Apa hubungan komputasi server tersebut dengan perilaku pengguna website?"*

---

## 📝 7. Checklist Revisi Berita Acara Sidang

- [ ] **1. Sinkronisasi Data Kuantitatif:** Samakan angka SUS (koreksi 88,17 menjadi 82) dan *Success Rate* (koreksi 92,9% dan 96,7% menjadi 98% dan 98,89%) di Abstrak, Bab IV, dan Bab V.
- [ ] **2. Perbaikan Abstrak:** Lengkapi kalimat *error rate* yang terpotong dan cantumkan skor akhir SUS.
- [ ] **3. Pembersihan Template:** Hapus semua placeholder `{...}` di Lembar Pengesahan, Pernyataan Keaslian, Persembahan, dan Kata Pengantar.
- [ ] **4. Koreksi Rujukan:** Ganti kutipan *Luo & Dai* dan *Nainggolan*, tambahkan *Akbar & Herdiansyah* serta *Sari et al.* ke Daftar Pustaka, dan bersihkan entri yang tidak dikutip.
- [ ] **5. Penyelarasan Metodologi:** Tampilkan hasil *Benchmarking* & *Heuristic Evaluation* di Bab IV, atau hapus kedua subbab tersebut jika tidak digunakan.
- [ ] **6. Format Gambar & Tabel:** Ubah Gambar 4.45–4.48 menjadi Tabel asli, perbaiki *Error! Bookmark not defined* di Daftar Tabel, dan perbaiki penomoran gambar yang duplikat.
- [ ] **7. Koreksi Persona:** Perbaiki profil Persona 1 di Tabel 4.5 (nama, pekerjaan, dan *typo*).
- [ ] **8. Penomoran Bab V:** Lengkapi butir nomor `3)` pada Kesimpulan 5.1 dan perbaiki ejaan baku KBBI (*Karier*).
