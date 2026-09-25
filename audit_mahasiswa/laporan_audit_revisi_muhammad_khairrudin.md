# 📋 LAPORAN AUDIT AKADEMIK PROPOSAL SKRIPSI (TELAAH REVISI KE-1)
**Program Studi S1 Informatika – Fakultas Teknik – Universitas Mulawarman**

---

### Data Mahasiswa & Dokumen:
* **Nama Mahasiswa:** Muhammad Khairrudin
* **NIM:** 2209106128
* **Judul Proposal:** *Rancang Bangun Sistem Monitoring Kualitas Air Sungai Mahakam Berbasis Internet of Things Menggunakan ESP32 dengan Metode Fuzzy Mamdani*
* **Dosen Pembimbing I:** Reza Wardhana, S.Kom., M.Eng.
* **Dosen Pembimbing II:** Anton Prafanto, S.Kom., M.T.
* **Koordinator Program Studi:** Awang Harsa Kridalaksana, S.Kom., M.Kom.
* **Berkas yang Dievaluasi:** [draft_proposal_muhammad_khairrudin_revisi1.pdf](draft_proposal_muhammad_khairrudin_revisi1.pdf) (Naskah Draf Proposal Revisi Skripsi, 81 Halaman)
* **Tanggal Evaluasi:** 25 September 2026
* **Status Keputusan:** ⚠️ **PROGRES SANGAT SUBSTANSIAL & MEMUASKAN — TINGGAL PERBAIKAN MINOR TEKNIS FUZZY & FORMALIA SEBELUM ACC SEMINAR PROPOSAL**

---

## 🌟 1. Apresiasi Pengerjaan Revisi (Koreksi Positif)

Saya memberikan apresiasi yang sangat tinggi kepada Saudara **Muhammad Khairrudin**. Respon perbaikan yang Saudara lakukan atas audit tanggal 14 September 2026 menunjukkan ketekunan, kedewasaan riset, dan penguasaan materi yang sangat baik. Naskah mengalami lonjakan kualitas yang signifikan:

1. **Kelengkapan Konfigurasi Pinout Perangkat Keras (Tabel 3.2, Hal. 57–59):**  
   Saudara telah menguraikan pemetaan pinout untuk seluruh 11 modul secara sangat presisi:
   * Sensor pH PH-4502C pada catu 5V dan pin ADC1 (GPIO 34).
   * Sensor Suhu Air DS18B20 pada GPIO 4 (OneWire) dengan resistor *pull-up* 4.7 kΩ.
   * Sensor DHT22 dipindahkan ke GPIO 15 sehingga GPIO 5 aman dialokasikan untuk Chip Select (CS) MicroSD Card.
   * Sensor Kekeruhan (*Turbidity*) pada catu 5V dengan penegasan rangkaian **Pembagi Tegangan (*Voltage Divider*)** sebelum GPIO 35 agar tidak melebihi 3.3V dan merusak ADC ESP32.
   * Berbagi bus I2C (GPIO 21 & 22) antara OLED SSD1306 dan RTC DS3231.
   * Bus SPI hardware lengkap untuk modul MicroSD (GPIO 5, 23, 18, 19).
   * Alokasi pin LED visual (GPIO 12, 14, 27) dengan resistor $220\,\Omega$ dan Buzzer (GPIO 2).
2. **Sinkronisasi Bab I yang Sangat Solid:**  
   Rumusan Masalah 3, Batasan Masalah 5, dan Tujuan 3 kini telah secara konsisten menyertakan keberadaan **Dashboard Web**, integrasi Firebase Realtime Database, dan pencadangan lokal offline pada MicroSD. Penegasan status data TDS ONLIMO KLHK 167 sebagai pembanding sekunder juga telah tertuang rapi pada Batasan Masalah 2.
3. **Penyisipan Tabel Matriks State-of-the-Art (Tabel 2.1, Hal. 36):**  
   Tabel perbandingan penelitian terdahulu telah disajikan dengan membandingkan aspek objek, parameter, metode logika, hingga celah riset, sehingga memperjelas kebaruan (*novelty*) skripsi Saudara.
4. **Klarifikasi Teoretis Defuzzifikasi (Subbab 2.5.1, Hal. 43):**  
   Penjelasan pemilihan metode **Rata-rata Terbobot (*Weighted Average / Discrete Height Centroid*)** telah dicantumkan dengan alasan optimasi komputasi dan efisiensi memori pada mikrokontroler ESP32.
5. **Koreksi Deskripsi Library DS18B20 (Tabel 3.3, Hal. 60):**  
   Fungsi library *OneWire & DallasTemperature* sudah diperbaiki menjadi pembacaan suhu air (bukan lagi suhu udara).
6. **Validitas Daftar Pustaka:**  
   Daftar Pustaka telah berisi 47+ referensi riil dengan tautan DOI resmi yang aktif.
7. **Lampiran Fisik Resmi (Hal. 81):**  
   Teks informal *`Penjelasan lihat di ppt`* telah dibersihkan dan digantikan dengan dokumen nyata: **Surat Pengantar Penelitian dari Fakultas Teknik Universitas Mulawarman ke Dinas Lingkungan Hidup Kota Samarinda** (No. 11463/UN17.9/TA.00.03/2026).

---

## 🚨 2. Catatan Kritis yang Masih Wajib Disempurnakan

Meskipun naskah sudah mendekati sempurna, masih terdapat **beberapa ketidaksinkronan matematis dan formalitas tata letak** yang wajib dirapikan agar Saudara tidak menjadi bulan-bulanan kritik dewan penguji pada saat Seminar Proposal:

| No | Lokasi | Tingkat Urgensi | Jenis Temuan Kritis |
|:---:|:---|:---:|:---|
| **1** | **Bab II & III (Hal. 42 & 64–66)** | 🚨 **Krusial (Matematika Fuzzy)** | **Ketidaksinkronan Definisi Kurva Trapesium vs Segitiga:**<br>• Di Bab II (Hal. 42), rumus fungsi keanggotaan yang ditulis **hanya segitiga**, belum ada rumus kurva trapesium.<br>• Di Tabel 3.4 (Hal. 64), Saudara menuliskan label *(Trapesium)* tetapi titiknya masih berupa **3 titik segitiga $(a, b, c)$**, bukan **4 titik trapesium $[a, b, c, d]$**!<br>• **Kontradiksi Gambar 3.5 vs Teks:** Gambar 3.5 menggambar bahu datar dari 0 s.d. 5 lalu turun di 6 (titik $[0, 0, 5, 6]$), namun tabel dan teks menulis $(0, 6, 7)$, serta rumus perhitungan langkah 1 (Hal. 66) menggunakan rumus segitiga $(7 - x)/(7 - 6)$. |
| **2** | **Hal. 3** | 🚨 **Fatal (Formalia)** | **Halaman Pengesahan Masih Template:** Tanggal masih tertulis `[tgl, bln, tahun]`, serta NIP Pembimbing I dan Pembimbing II belum dicantumkan. |
| **3** | **Hal. 4** | 🚨 **Fatal (Formalia)** | **Kata Pengantar Menyisakan Template Penguji:** Poin 5 masih memuat teks template Word: `5. Nama dan gelar akademik Dosen Penguji II selaku Penguji II atas saran dan masukkan terhadap penelitian ini.` |
| **4** | **Hal. 10 & 11** | ⚠️ **Mayor (Formalia)** | **Header Tabel Istilah & Singkatan:** Kolom header masih tertulis kata template Word: `Contents Arti`. Kata `Contents` wajib dihapus. |
| **5** | **Hal. 1–11 vs Bab I** | 🚨 **Fatal (Pagination)** | **Penomoran Halaman (*Pagination*) Salah:**<br>• Bagian awal (Cover s.d. Daftar Singkatan) menggunakan angka Arab `1 s.d. 10` di pojok atas, seharusnya **angka Romawi kecil (`i s.d. x`) di tengah bawah**.<br>• Bab I Pendahuluan ter-reset dimulai dari halaman `3`, seharusnya **angka Arab `1`**. |
| **6** | **Hal. 50–51** | ⚠️ **Mayor (Teks)** | **Judul Tahap 4 Terpotong:** Judul sub-langkah `4. Implementasi Purwarupa / Sistem` hilang di pergantian halaman 50 ke 51. Teks penjelasannya ada, tetapi judulnya hilang sehingga nomor langsung melompat dari poin 3 ke poin 5! |
| **7** | **Hal. 7, 36, 48** | ⚠️ **Sedang (Sinkronisasi Tabel)** | **Nomor Tabel Flowchart & Matriks SOTA:**<br>• Tabel SOTA diberi nomor `Tabel 2.1` (Hal. 36), sedangkan Tabel Simbol Flowchart di Hal. 48 diberi nomor `Tabel 2.2`.<br>• Namun di Daftar Tabel (Hal. 7) dan narasi teks Hal. 47 masih tertulis `Tabel 2.1 Simbol-Simbol Flowchart`. Belum dilakukan *Update Table Field*. |
| **8** | **Hal. 47 & Daftar Pustaka** | ⚠️ **Sedang (Sitasi)** | **Ghost Citation:** Sitasi `(Hasib & Akib, 2026)` masih dikutip dua kali pada Halaman 47, namun tidak tercantum pada Daftar Pustaka. |
| **9** | **Hal. 74–75** | ⚠️ **Sedang (Jadwal)** | **Tabel Jadwal Penelitian Kosong:** Matriks bulan Juli s.d. November pada Tabel 3.10 masih kosong melompong tanpa centang ($\checkmark$) atau arsiran kegiatan. |
| **10** | **Hal. 21–28** | ℹ️ **Minor (Gaya Bahasa)** | **Pola Subbab 2.1 Kaku:** Sebagian besar butir tinjauan pustaka masih diawali dengan sub-heading kaku: `Metode yang digunakan:` dan `Temuan Penelitian:`. |

---

## 🔍 3. Panduan Perbaikan Teknis Langkah demi Langkah

---

### A. Rekonstruksi Matematis Kurva Fuzzy (Bab II & Bab III)

Ini adalah poin paling krusial yang akan disorot oleh dosen penguji yang menguasai kecerdasan buatan. Saudara harus menyelaraskan antara **rumus matematis di Bab II**, **titik koordinat di Tabel 3.4**, **grafik Gambar 3.5**, dan **contoh perhitungan numerik**:

#### 1. Masukkan Rumus Trapesium pada Subbab 2.5.1 (Bab II, Hal. 42)
Setelah rumus segitiga, tambahkan persamaan kurva trapesium dengan 4 parameter $[a, b, c, d]$:

$$\mu(x) = \begin{cases} 
0, & x < a \text{ atau } x > d \\
\frac{x - a}{b - a}, & a \le x < b \\
1, & b \le x \le c \\
\frac{d - x}{d - c}, & c < x \le d 
\end{cases}$$

Khusus untuk **kurva bahu kiri (*left shoulder*)** di mana $a = b$ (kondisi Asam, Rendah, Jernih):
$$\mu(x) = \begin{cases} 
1, & x \le b \\
\frac{c - x}{c - b}, & b < x \le c \\
0, & x > c 
\end{cases}$$

Dan untuk **kurva bahu kanan (*right shoulder*)** di mana $c = d$ (kondisi Basa, Tinggi, Keruh):
$$\mu(x) = \begin{cases} 
0, & x < a \\
\frac{x - a}{b - a}, & a \le x < b \\
1, & x \ge b 
\end{cases}$$

#### 2. Standarisasi 4 Titik $[a, b, c, d]$ pada Tabel 3.4 (Hal. 64)
Ganti kolom titik $(a, b, c)$ menjadi parameter $[a, b, c, d]$ yang baku:

| Variabel | Himpunan | Tipe Kurva | Titik Parameter $[a, b, c, d]$ |
|:---|:---|:---:|:---:|
| **pH** | Asam | Trapesium Bahu Kiri | $[0.0, 0.0, 6.0, 7.0]$ |
| | Netral | Segitiga | $[6.0, 7.5, 9.0]$ |
| | Basa | Trapesium Bahu Kanan | $[8.0, 9.0, 14.0, 14.0]$ |
| **Selisih Suhu ($\Delta T$)** | Rendah | Trapesium Bahu Kiri | $[0.0, 0.0, 1.0, 2.5]$ |
| | Sedang | Segitiga | $[1.5, 3.0, 4.5]$ |
| | Tinggi | Trapesium Bahu Kanan | $[3.5, 5.0, 15.0, 15.0]$ |
| **Kekeruhan (NTU)** | Jernih | Trapesium Bahu Kiri | $[0.0, 0.0, 2.0, 3.5]$ |
| | Sedang | Segitiga | $[2.5, 5.0, 10.0]$ |
| | Keruh | Trapesium Bahu Kanan | $[6.0, 15.0, 100.0, 100.0]$ |
| **Status Mutu (Output)** | Buruk | Trapesium Bahu Kiri | $[0, 0, 25, 50]$ |
| | Sedang | Segitiga | $[25, 50, 75]$ |
| | Baik | Trapesium Bahu Kanan | $[50, 75, 100, 100]$ |

> **Mengapa ini penting?**  
> Dengan batas Keruh $[6.0, 15.0, 100.0, 100.0]$, jika saat hujan air Sungai Mahakam keruh pekat hingga **30 NTU atau 50 NTU**, nilai $\mu_{\text{Keruh}}$ akan tetap bernilai **1.0**. Sistem tidak akan mengalami *divide-by-zero* / *NaN* saat defuzzifikasi!

#### 3. Sinkronkan Gambar 3.5 dan Contoh Perhitungan (Hal. 65–66)
* Pada Gambar 3.5, pastikan grafik kurva Asam mendatar pada nilai 1 dari pH $0$ sampai $6.0$, kemudian miring turun ke 0 tepat di pH $7.0$.
* Pada contoh perhitungan Langkah 1 (Hal. 66) untuk $\text{pH} = 6.2$:
  $$\mu_{\text{Asam}}(6.2) = \frac{7.0 - 6.2}{7.0 - 6.0} = \frac{0.8}{1.0} = 0.8$$
  Hasil ini sekarang menjadi **100% konsisten** dengan grafik dan tabel!

---

### B. Formalia Bagian Awal (Cover s.d. Daftar Singkatan)

#### 1. Lembar Pengesahan (Hal. 3)
Lengkapi NIP dosen pembimbing dan perbaiki tanggal:
```text
Telah dibahas dalam Rapat Dosen Pembimbing pada .............................. 2026 dan 
dinyatakan memenuhi syarat sebagai Skripsi, dengan Dosen Pembimbing:

I.  Reza Wardhana, S.Kom., M.Eng.
    NIP 19920409 201903 1 014

II. Anton Prafanto, S.Kom., M.T.
    NIP 19931022 201903 1 016

Koordinator Program Studi S1 Informatika,
Fakultas Teknik, Universitas Mulawarman,


Awang Harsa Kridalaksana, S.Kom., M.Kom.
NIP 19731229 200501 1 002
```

#### 2. Kata Pengantar (Hal. 4)
* **Hapus Poin 5:** Hapus baris *`5. Nama dan gelar akademik Dosen Penguji II selaku Penguji II...`*. Pada tahap proposal, dosen penguji belum ditugaskan.
* Susun urutan ucapan terima kasih:
  1. Orang Tua dan Keluarga
  2. Dekan Fakultas Teknik
  3. Koordinator Program Studi S1 Informatika
  4. Dosen Pembimbing I (Reza Wardhana, S.Kom., M.Eng.) dan Pembimbing II (Anton Prafanto, S.Kom., M.T.)
  5. Segenap Dosen dan Staf Akademik Program Studi S1 Informatika
  6. Rekan-rekan mahasiswa angkatan 2022

#### 3. Perbaikan Header Daftar Istilah & Singkatan (Hal. 10 & 11)
* Buka tabel Daftar Istilah dan Daftar Singkatan di Word.
* Hapus kata `Contents` pada baris header tabel. Cukup gunakan header:
  * Kolom 1: **Lambang / Istilah** (atau **Singkatan**)
  * Kolom 2: **Arti / Kepanjangan**

#### 4. Pengaturan Section & Penomoran Halaman (*Pagination*)
* **Bagian Awal (Halaman Judul s.d. Daftar Singkatan):**
  - Nomor halaman: Angka Romawi kecil (**i, ii, iii, iv, v, vi, vii, viii, ix, x**).
  - Posisi: **Tengah Bawah**.
* **Bagian Isi (Bab I s.d. Lampiran):**
  - Buat pemisah dengan **Page Layout $\rightarrow$ Breaks $\rightarrow$ Section Break (Next Page)** sebelum teks `BAB I PENDAHULUAN`.
  - Pada Bab I, matikan **Link to Previous**.
  - Masuk ke **Insert $\rightarrow$ Page Number $\rightarrow$ Format Page Numbers $\rightarrow$ Start at: 1**.
  - Posisi: Awal bab di **Tengah Bawah**, halaman lanjutan di **Kanan Atas**.

---

### C. Penyempurnaan Bab III & Lampiran

1. **Kembalikan Judul Tahap 4 pada Subbab 3.1 (Hal. 50–51):**  
   Sisipkan judul yang terpotong di baris paling atas Halaman 51:
   > **4. Implementasi Purwarupa (Perangkat Keras & Perangkat Lunak)**  
   > *Setelah rancangan disetujui, tahap berikutnya adalah merealisasikan perangkat keras dan memprogram logika inferensi pada ESP32...*
2. **Bersihkan Ghost Citation (Hal. 47):**  
   Ganti sitasi `(Hasib & Akib, 2026)` pada Halaman 47 dengan paper rujukan yang ada di Daftar Pustaka (misalnya: *Affandi et al., 2026* atau *Sugiyatno, 2023*).
3. **Isi Tabel Jadwal Penelitian (Tabel 3.10, Hal. 74–75):**  
   Beri tanda centang ($\checkmark$) pada kolom bulan pelaksanaan (Juli s.d. November 2026) untuk setiap tahapan kegiatan.
4. **Keterangan Lampiran (Hal. 81):**  
   Di atas scan Surat Pengantar Penelitian, tambahkan judul resmi:  
   **Lampiran 1: Surat Pengantar Penelitian dari Fakultas Teknik Universitas Mulawarman**.  
   Lalu lakukan *Update Table of Contents* di Word agar Daftar Lampiran di halaman 9 tertaut dengan benar.

---

## 📅 4. Kesimpulan & Rekomendasi Akhir

Proposal Saudara **Muhammad Khairrudin** secara keseluruhan sudah **sangat bagus, komprehensif, dan matang (95% siap)**. Perancangan elektronika dan integrasi IoT-nya sudah memenuhi standar skripsi S1 Informatika yang unggul.

### Rekomendasi Pembimbing:
* Perbaikan yang tersisa murni seputar **konsistensi kurva trapesium pada naskah**, **pembersihan 3 sisa teks template**, dan **pengaturan nomor halaman di Word**.
* Saudara dapat menyelesaikan perbaikan ini dalam **1 hari kerja**.
* Setelah seluruh poin di atas disinkronkan, kirimkan kembali draf finalnya. Saya dan Pak Reza siap menandatangani lembar persetujuan untuk Saudara mendaftar ke **Seminar Proposal (Sempro)**.

Tetap teliti dan tuntaskan bagian akhir ini dengan sempurna!

---
**Samarinda, 25 September 2026**  
Dosen Pembimbing II,  

**Anton Prafanto, S.Kom., M.T.**  
NIP 19931022 201903 1 016
