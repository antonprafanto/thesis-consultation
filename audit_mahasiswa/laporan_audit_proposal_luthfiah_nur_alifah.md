# 📑 Laporan Audit Kelayakan Naskah Proposal Skripsi
**Program Studi S1 Informatika, Fakultas Teknik, Universitas Mulawarman**

---

### 📌 Informasi Dokumen & Mahasiswa
* **Nama Mahasiswa:** Luthfiah Nur Alifah
* **NIM:** 2309106102
* **Program Studi:** S1 Informatika (Angkatan 2023)
* **Dosen Pembimbing I:** Prof. Dr. Fahrul Agus, S.Si., M.T.
* **Dosen Pembimbing II:** Medi Taruk, M.Cs.
* **Judul Naskah:** *Analisis Pola Sebaran dan Kepadatan Fasilitas Kesehatan Menggunakan Metode Nearest Neighbor Analysis (NNA) dan Kernel Density Estimation (KDE)*
* **Jenis Naskah:** Draf Naskah Proposal Skripsi (65 Halaman)
* **Tanggal Audit:** 29 September 2026
* **Auditor / Penelaah:** Dosen Pembimbing S1 Informatika FT Unmul

---

## 🎯 Ringkasan Eksekutif Hasil Audit (Executive Summary)

Secara keseluruhan, draf proposal skripsi saudari **Luthfiah Nur Alifah** memiliki **substansi metodologis dan ketajaman ilmiah yang sangat baik dan di atas rata-rata**. Mahasiswa menunjukkan pemahaman mendalam mengenai analisis spasial berbasis SIG, pemilihan sistem proyeksi metrik (UTM Zone 50S), formulasi statistik *Nearest Neighbor Analysis* (NNA), estimasi densitas *Kernel Density Estimation* (KDE), serta rancangan pengujian komputasi yang sangat matang (validasi manual vs *PySAL*, uji sensitivitas *bandwidth*, dan korelasi *Quadrat Count Analysis*).

Namun demikian, terdapat **beberapa pelanggaran format fisik dan kaidah tata tulis baku** yang cukup mencolok terhadap [Pedoman Skripsi S1 Informatika FT Unmul](file:///c:/Users/anton/vibecoding/Bimbingan/pedoman_skripsi_unmul.md), serta beberapa artefak penyusunan dokumen yang belum dibersihkan. 

### 📊 Rekapitulasi Status Kepatuhan:
| Aspek Evaluasi | Status | Catatan Utama |
| :--- | :---: | :--- |
| **Kelengkapan Struktur Bab (I–III)** | **LENGKAP** | Memenuhi sistematika baku proposal (Bab I, II, III, Daftar Pustaka). |
| **Kualitas Metodologi & Algoritma** | **SANGAT BAIK** | Alur komputasi jelas, proyeksi koordinat tepat, pengujian terukur. |
| **Format Halaman & Nomor Halaman** | ❌ **REVISI MAYOR** | Nomor halaman bab isi seluruhnya ditaruh di tengah bawah (*seharusnya di kanan atas*). |
| **Sistematika Daftar Pustaka** | ❌ **REVISI MAYOR** | Daftar pustaka diberi nomor urut angka 1–33 (*APA 6th dilarang pakai nomor*), ada duplikasi referensi. |
| **Kebersihan Dokumen (*Hygiene*)** | ⚠️ **REVISI MINOR** | Masih ada teks sisa template (`Contents`, `Arti`, placeholder tanggal/penguji). |
| **Tipografi & Penamaan Tabel/Gambar** | ⚠️ **REVISI MINOR** | Terdapat spasi janggal pada label tabel/gambar (`Tabel 2. 1` $\rightarrow$ `Tabel 2.1.`). |

---

## 🔍 Catatan Rinci Hasil Audit (Point-by-Point)

---

### Bagian 1: Audit Format Fisik & Tipografi Naskah

#### 1. Aturan Penomoran Halaman (*Page Numbering*) — **[WAJIB DIPERBAIKI]**
* **Temuan Pelanggaran:** 
  Pada seluruh naskah utama mulai Halaman 1 s.d. 52 (PDF halaman 11 s.d. 62), nomor halaman diletakkan di **tengah bawah (*bottom center*)**.
* **Kaidah Baku Pedoman FT Unmul:**
  * Bagian Awal (Kata Pengantar s.d. Daftar Singkatan): Angka Romawi kecil (`i, ii, iii, ...`) di **tengah bawah**. (*Sudah Benar*).
  * Bagian Isi (Bab I s.d. Daftar Pustaka): Angka Arab (`1, 2, 3, ...`) diletakkan di **POJOK KANAN ATAS (*top right*)**.
  * **Hanya halaman pertama setiap Bab Baru** (Halaman 1 pada Bab I, Halaman 8 pada Bab II, Halaman 33 pada Bab III, Halaman 53 pada Daftar Pustaka) yang nomornya diletakkan di **TENGAH BAWAH**.
* **Solusi Perbaikan di MS Word:**
  Gunakan fitur `Page Layout` $\rightarrow$ `Breaks` $\rightarrow$ `Section Break (Next Page)` di setiap awal bab baru, centang opsi `Different First Page` (*Halaman Pertama Berbeda*), dan nonaktifkan `Link to Previous` pada *Header* dan *Footer*.

#### 2. Format Penulisan Judul Bab (Redundansi Heading) — **[WAJIB DIPERBAIKI]**
* **Temuan Pelanggaran:** 
  Pada awal setiap bab, tertulis pengulangan kata:
  * Halaman 1: `BAB I PENDAHULUAN` lalu di bawahnya muncul lagi `PENDAHULUAN`.
  * Halaman 8: `BAB II TINJAUAN PUSTAKA` lalu muncul lagi `TINJAUAN PUSTAKA`.
  * Halaman 33: `BAB III METODOLOGI PENELITIAN` lalu muncul lagi `METODOLOGI PENELITIAN`.
* **Kaidah Baku:**
  Ini terjadi karena *Style Heading 1* Anda memuat teks `BAB I PENDAHULUAN`, lalu Anda mengetik ulang judul bab secara manual di baris bawahnya. 
  Format baku di Word:
  ```text
  BAB I
  PENDAHULUAN
  ```
  *(Gunakan `Shift + Enter` antar-baris agar tetap terhitung sebagai satu entri Heading 1 di Daftar Isi).*

#### 3. Tipografi Judul Tabel dan Gambar (Spasi Janggal) — **[WAJIB DIPERBAIKI]**
* **Temuan Pelanggaran:** 
  Seluruh penulisan identitas tabel dan gambar memiliki spasi ekstra setelah tanda titik nomor bab, contoh: `Tabel 2. 1`, `Tabel 2. 2`, `Tabel 3. 1`, `Gambar 3. 1`, `Gambar 3. 2`.
* **Kaidah Baku:**
  Penulisan baku menggunakan tanda titik ganda tanpa spasi di tengah:
  * `Tabel 2.1. Perbedaan Penelitian Sebelumnya` (bukan `Tabel 2. 1`)
  * `Tabel 3.1. Data Penelitian` (bukan `Tabel 3. 1`)
  * `Gambar 3.1. Diagram Tahapan Pelaksanaan Penelitian` (bukan `Gambar 3. 1`)
  * Format: TNR 12 pt, **Bold**, letak di **ATAS** untuk Tabel, letak di **BAWAH** untuk Gambar, posisi **Center**.

#### 4. Konsistensi Font (Pembersihan Font Non-TNR)
* **Temuan:** Ditemukan jejak font *Calibri* dan *Arial* pada beberapa baris tabel dan spasi (kemungkinan hasil *copy-paste* dari dokumen lain atau website).
* **Solusi:** Lakukan *Select All* (`Ctrl + A`) pada naskah akhir di Word dan setel ulang seluruh font ke **Times New Roman**.

---

### Bagian 2: Audit Bagian Awal (Front Matter) & Berkas Administratif

#### 1. Halaman Sampul (Cover Luar & Dalam)
* **Positif:** Penulisan NIM sudah sangat tepat langsung angka `2309106102` tanpa embel-embel tulisan "NIM:". Judul sudah berbentuk piramida terbalik kapital.
* **Perbaikan:** Pastikan logo Unmul memiliki resolusi tinggi (tidak pecah/buram saat dicetak) dengan diameter proporsional (± 5,5 cm).

#### 2. Halaman Pengesahan Proposal (Halaman ii)
* **Temuan:** 
  1. Masih ada placeholder tanggal yang belum diisi: `pada [tgl, bln, tahun]`.
  2. Penulisan nama pembimbing diberi nomor urut `I.` dan `II.`. Pada template resmi tidak perlu nomor urut `I.` dan `II.`.
  3. Perhatikan penulisan tanda baca gelar akademik:
     * `Prof. Dr. Fahrul Agus, S.Si., M.T.` (tambahkan tanda titik setelah huruf T).
     * `Medi Taruk, M.Cs.` (tambahkan tanda titik setelah huruf s).
  4. Pengesahan proposal oleh Koordinator Program Studi S1 Informatika (*Awang Harsa Kridalaksana, S.Kom., M.Kom. - NIP 19731229 200501 1 002*) sudah benar.

#### 3. Kata Pengantar (Halaman iii)
* **Temuan:**
  Pada butir ucapan terima kasih nomor 6 dan 7, mahasiswa masih membiarkan teks template:
  * *"Nama dan gelar akademik Dosen Penguji I selaku Penguji I atas saran dan masukkan..."*
  * *"Nama dan gelar akademik Dosen Penguji II selaku Penguji II atas saran dan masukkan..."*
* **Kaidah:**
  Pada tahapan **Proposal Skripsi**, dosen penguji **belum ditetapkan**. Kalimat tersebut wajib **dihapus** dari draf proposal. Jangan pernah membiarkan teks placeholder template tertinggal di naskah resmi!

#### 4. Daftar Isi (Halaman iv - v)
* **Temuan:** Halaman v hanya berisi 2 baris (`3.7 Waktu dan Tempat Penelitian` dan `DAFTAR PUSTAKA`), sementara bagian bawah halaman kosong melompong.
* **Saran:** Atur spasi baris (*line spacing*) atau *spacing before/after* pada style TOC agar Daftar Isi menjadi lebih padat dan estetik.

#### 5. Daftar Istilah/Lambang & Daftar Singkatan (Halaman viii & ix) — **[WAJIB DIBERSIHKAN]**
* **Temuan Fatal:**
  Di bawah judul `DAFTAR ISTILAH/LAMBANG` (Halaman viii) dan `DAFTAR SINGKATAN` (Halaman ix), tertulis teks sisa template Microsoft Word:
  ```text
  Arti
  Contents
  ```
* **Solusi:** Hapus kata `Arti` dan `Contents` tersebut. Keduanya merupakan teks petunjuk template bawaan yang lupa dihapus.

---

### Bagian 3: Audit Substansi & Kualitas Akademik Informatika (Bab I s.d. Bab III)

#### BAB I: PENDAHULUAN
1. **Latar Belakang (1.1):**
   * **Struktur Alur:** Alur latar belakang sudah sangat logis (8 paragraf) dengan prinsip piramida terbalik yang runut, mulai dari urgensi pemerataan faskes, profil Samarinda, kelemahan pemetaan inventarisasi statis, sintesis riset terdahulu, solusi NNA + KDE, hingga paragraf penetapan judul baku.
   * **Koreksi Penulisan Sitasi Naratif:**
     Terdapat kesalahan penulisan sitasi yang menjadi subjek kalimat:
     * *Tertulis salah:* `(Savitri & Sari, 2025) menggunakan metode Kernel Density Estimation...`
     * *Seharusnya:* `Savitri dan Sari (2025) menggunakan metode Kernel Density Estimation...`
     * *Tertulis salah:* `(Nafisa, Hadibasyir, Sigit, Wibowo, & Sasmi, 2024) menerapkan Average Nearest Neighbour...`
     * *Seharusnya:* `Nafisa dkk. (2024) menerapkan Average Nearest Neighbour...`
     *(Aturan APA: Nama penulis di luar tanda kurung jika berfungsi sebagai subjek gramatikal dalam kalimat).*
   * **Saran Penguatan Konten (Nilai Plus):**
     Mahasiswa menyebutkan angka agregat Samarinda: 16 RS, 26 Puskesmas, dan 148 Klinik. Latar belakang akan jauh lebih menggigit (*powerful*) jika disajikan ringkasan 1 tabel kecil atau narasi 1 kalimat mengenai **ketimpangan sebaran per kecamatan** (misalnya: Samarinda Kota memiliki belasan faskes, sementara Palaran atau Sambutan sangat minim). Ini membuktikan bahwa masalah ketimpangan bukan sekadar asumsi penulis, melainkan fakta lapangan.

2. **Rumusan Masalah, Tujuan & Manfaat (1.2 – 1.5):**
   * Sudah sangat tajam dan selaras 1-to-1 antara rumusan masalah dengan tujuan penelitian.
   * Manfaat penelitian telah dipilah rapi menjadi 3 pihak: Penulis, Mahasiswa/Akademik, dan Instansi/Mitra.

3. **Batasan Masalah (1.3):**
   * Batasan masalah sudah sangat tegas (membatasi pada batas wilayah Samarinda, data Geoportal Satu Peta & BIG, serta secara eksplisit mengecualikan analisis jaringan jalan dan waktu tempuh rute). Hal ini penting untuk mengunci ruang lingkup agar tidak melebar saat ujian.

---

#### BAB II: TINJAUAN PUSTAKA
1. **Penelitian Terkait (2.1):**
   * **Sangat Komprehensif:** Mahasiswa mengulas **13 penelitian terkait** terkini (2021–2026), jauh melampaui batas minimal 5–10 rujukan prodi.
   * **Tabel Perbedaan Penelitian Sebelumnya (Tabel 2.1):** Tersaji dengan sangat baik, merinci judul, peneliti, dan poin pembeda (*research gap*) secara jelas.
2. **Landasan Teori (2.2 – 2.7):**
   * Teori pendukung (SIG, Faskes, QGIS, NNA, KDE) sangat kontekstual dan tidak bertele-tele.
   * **Penulisan Rumus:** Persamaan NNA dan KDE sudah diketik rapi menggunakan Equation Editor lengkap dengan nomor di margin kanan `(2.1)`, `(2.2)`, `(2.3)` serta penjelasan variabel `Di mana:` yang sejajar.

---

#### BAB III: METODOLOGI PENELITIAN
1. **Diagram Alir Tahapan Riset (3.1):**
   * Gambar 3.1 sudah menggambarkan tahapan penelitian secara linier dan terstruktur dari studi literatur, akuisisi data, prapemrosesan, perancangan algoritma, hingga pengujian.
2. **Prapemrosesan Data Spasial & Pemilihan CRS (3.3):**
   * **APRESIASI KHUSUS:** Mahasiswa secara tepat mentransformasikan sistem koordinat dari WGS 84 derajat desimal (*EPSG:4326*) ke **WGS 84 / UTM Zone 50S (*EPSG:32750*)**. Hal ini sangat krusial dalam komputasi spasial karena metode NNA (*Euclidean Distance*) dan KDE (*Bandwidth Radius*) **wajib menggunakan satuan meter**, bukan derajat desimal. Pemahaman ini menunjukkan kualitas penguasaan GIS yang solid.
3. **Perancangan Algoritma & Komputasi (3.4):**
   * Pseudocode dan langkah komputasi NNA (Python) dan KDE (QGIS) diuraikan langkah demi langkah.
   * *Catatan Kritis Pembimbing:*
     Penelitian ini menggunakan **Python di Google Colab untuk NNA** dan **QGIS untuk KDE**. 
     *Saran Pengembangan:* Mahasiswa sebaiknya menyatukan seluruh pipeline analisis ini ke dalam satu script Python yang utuh (misalnya menggunakan pustaka `PySAL` / `pointpats` untuk NNA dan `scikit-learn` / `scipy.stats.gaussian_kde` untuk KDE) atau membangun antarmuka web GIS sederhana (menggunakan Streamlit / Folium). Ini akan melipatgandakan bobot rekayasa komputasi informatika naskah ini saat dinilai oleh para penguji sidang.
4. **Perancangan Pengujian (3.6) — [POIN SANGAT BAIK]:**
   * Tabel 3.3 merancang validasi komputasi yang sangat presisi:
     1. Verifikasi NNA manual (spreadsheet) vs program Python vs pustaka *PySAL* (toleransi galat < 1%).
     2. Uji signifikansi statistik ($z$-score dan $p$-value).
     3. Uji sensitivitas *bandwidth* KDE ($h = 2.100\text{ m}, 3.000\text{ m}, 3.900\text{ m}$) dengan batas korelasi antarraster $r \ge 0,8$.
     4. Uji korelasi independen terhadap *Quadrat Count Analysis* ($r \ge 0,7$ dan $p < 0,05$).
     5. Verifikasi visual melalui *overlay*.
   * Rancangan pengujian ini sangat ilmiah dan membuktikan mahasiswa tidak sekadar "menekan tombol software", melainkan mengerti validitas komputasi statistiknya.
5. **Jadwal Penelitian (3.7):**
   * Tabel 3.4 telah memuat 3 tahapan baku: Tahap Persiapan, Tahap Pelaksanaan, dan Tahap Penyusunan Laporan.

---

### Bagian 4: Audit Sitasi & Daftar Pustaka (The References)

Ini adalah bagian dengan **kesalahan paling banyak** yang wajib diperbaiki mahasiswa sebelum naskah diserahkan ke program studi:

#### 1. Kesalahan Penggunaan Nomor Urut pada Daftar Pustaka — **[PELANGGARAN FATAL APA STYLE]**
* **Temuan:** 
  Daftar Pustaka ditulis menggunakan nomor urut:
  `1. Abdulazeez, A. ...`
  `2. Aeni, N. ...`
  `... 33. Zulprima, Z. ...`
* **Kaidah Baku APA 6th Edition & Pedoman Unmul:**
  Daftar Pustaka gaya APA **TIDAK MENGGUNAKAN NOMOR URUT ANGKA**. 
  Susunan daftar pustaka wajib diurutkan secara **alfabetis murni** berdasarkan nama belakang penulis pertama, dengan format paragraf menggantung (*Hanging Indent* 1 cm). Nomor 1, 2, 3 ... wajib **dihapus**.

#### 2. Entri Referensi Ganda (Duplikasi Identik) — **[WAJIB DIHAPUS SATU]**
* **Temuan:**
  Perhatikan entri nomor 11 dan nomor 12:
  * `11. Hashtarkhani, S., Schwartz, D. L., & Shaban-Nejad, A. (2024a). Enhancing Health Care Accessibility... JMIR Formative Research, 8, e51727. https://doi.org/10.2196/51727`
  * `12. Hashtarkhani, S., Schwartz, D. L., & Shaban-Nejad, A. (2024b). Enhancing Health Care Accessibility... JMIR Formative Research, 8, e51727. https://doi.org/10.2196/51727`
* **Koreksi:**
  Kedua entri tersebut adalah **artikel yang sama persis** dari jurnal yang sama dan DOI yang sama. Mahasiswa keliru memasukkan dua kali di Mendeley/Zotero sehingga muncul `2024a` dan `2024b`. Hapus salah satu!

#### 3. Kesalahan Format Metadata Hasil *Web Scraping*
* **Entri Nomor 29 (Susianti dkk.):**
  * *Tertulis:* `... Study Case Dengue Fever in Purwosari Sub-District, Gunungkidul Regency, Yogyakarta, Indonesia | Susianti | Indonesian Journal of Geography. Indonesian Journal of Geography, 55(2)...`
  * *Koreksi:* Hapus teks `| Susianti | Indonesian Journal of Geography` yang menempel di judul artikel. Ini merupakan artefak judul tab browser yang terbawa saat metadata diunduh otomatis.
* **Entri Nomor 20 (Pressman):**
  * *Tertulis:* `(Nineth edition)`.
  * *Koreksi:* Perbaiki typo ejaan bahasa Inggris menjadi `(9th ed.)` atau `(Ninth edition)`.
* **Entri Nomor 8 & 21 (Esri & QGIS):**
  * *Tertulis:* `Diambil 6 Agustus 2026, dari...`
  * *Koreksi:* Tanggal akses mencantumkan tahun 2026 yang seolah-olah ditarik di masa depan. Sesuaikan dengan tanggal pengaksesan data yang sebenarnya, atau hilangkan kalimat "Diambil dari" jika tautan rujukan bersifat permanen.

#### 4. Proporsi & Jumlah Referensi
* Jumlah rujukan: 33 referensi (jika duplikasi dihapus menjadi 32). Memenuhi rentang kuota wajib **30 s.d. 50 referensi**.
* Komposisi rujukan:
  * Artikel Jurnal/Prosiding 5 tahun terakhir: **82%** (melebihi syarat minimal 60%).
  * Buku teks: **12%**.
  * Website/Dokumentasi resmi: **6%**.
  * **Status Komposisi:** Sangat Baik dan didominasi literatur primer mutakhir (bahkan banyak terbitan 2024–2026).

---

## 📋 Checklist Rencana Aksi Mahasiswa (Action Plan Perbaikan)

Gunakan daftar checklist berikut untuk menyelesaikan perbaikan draf sebelum seminar proposal:

```text
PRIORITAS TINGGI (FORMAT & TATA TULIS WAJIB):
[ ] 1. Ubah seluruh nomor halaman naskah isi (Bab I s.d. Lampiran) ke KANAN ATAS.
       Hanya halaman pertama Bab (Bab I hal 1, Bab II hal 8, Bab III hal 33, DP hal 53)
       yang berada di TENGAH BAWAH.
[ ] 2. Hapus nomor urut 1, 2, 3... pada DAFTAR PUSTAKA. Gunakan Hanging Indent alfabetis APA.
[ ] 3. Hapus entri duplikat referensi Hashtarkhani (2024a/2024b).
[ ] 4. Bersihkan kata template "Contents" dan "Arti" pada Daftar Istilah dan Daftar Singkatan.
[ ] 5. Hapus teks redundan "PENDAHULUAN" ganda di bawah judul Bab I, II, dan III.
[ ] 6. Hapus placeholder Penguji I & Penguji II pada Kata Pengantar.
[ ] 7. Isi tanggal pengesahan yang masih berupa placeholder "[tgl, bln, tahun]".

PRIORITAS SEDANG (TIPOGRAFI & PERAPIAN KONTEN):
[ ] 8. Hilangkan spasi ganjil pada penamaan tabel dan gambar (ganti "Tabel 2. 1" jadi "Tabel 2.1.").
[ ] 9. Koreksi penulisan sitasi naratif di Latar Belakang (jangan kurung nama penulis jika menjadi subjek).
[ ] 10. Bersihkan artefak scraping judul pada entri referensi Susianti dkk. di Daftar Pustaka.
[ ] 11. Perbaiki penulisan titik gelar pembimbing: "M.T." dan "M.Cs.".
[ ] 12. Lakukan Select All di Word dan pastikan font 100% Times New Roman.

SARAN PENINGKATAN (NILAI TAMBAH SIDANG):
[ ] 13. Tambahkan 1 kalimat/tabel mini ringkasan data faskes per kecamatan di Samarinda pada Latar Belakang.
[ ] 14. Pertimbangkan untuk menyatukan script NNA dan KDE ke dalam satu workflow otomatisasi Python.
```

---

## 👨‍🏫 Rekomendasi Keputusan Pembimbing

| Keputusan Akademik | Status |
| :--- | :---: |
| **Diterima Tanpa Revisi** | ❌ |
| **Diterima dengan Revisi Minor (Siap Jadwalkan Sempro setelah diperbaiki)** | ✅ **DISETUJUI** |
| **Revisi Mayor / Belum Layak Ujian** | ❌ |

**Catatan Pembimbing:**
> *"Secara substansi keilmuan, metodologi penelitian saudari Luthfiah sangat matang, sistematis, dan terencana dengan sangat baik. Penguasaan konsep SIG dan pengujian statistiknya patut diapresiasi. Selesaikan seluruh poin perbaikan format di atas (khususnya posisi nomor halaman, pembersihan template, dan format daftar pustaka APA) dalam waktu maksimal 3–5 hari. Setelah berkas diperbaiki dan diverifikasi ulang, saudari dapat segera memproses formulir persetujuan pendaftaran Seminar Proposal ke Program Studi."*

---
*Laporan audit ini resmi dicatat dalam sistem dokumentasi bimbingan akademik Program Studi S1 Informatika FT Universitas Mulawarman.*
