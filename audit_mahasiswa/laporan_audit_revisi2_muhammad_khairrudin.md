# 📋 LAPORAN AUDIT AKADEMIK PROPOSAL SKRIPSI (TELAAH REVISI KE-2)
**Program Studi S1 Informatika – Fakultas Teknik – Universitas Mulawarman**

---

### Data Mahasiswa & Dokumen:
* **Nama Mahasiswa:** Muhammad Khairrudin
* **NIM:** 2209106128
* **Judul Proposal:** *Rancang Bangun Sistem Monitoring Kualitas Air Sungai Mahakam Berbasis Internet of Things Menggunakan ESP32 dengan Metode Fuzzy Mamdani*
* **Dosen Pembimbing I:** Reza Wardhana, S.Kom., M.Eng.
* **Dosen Pembimbing II:** Anton Prafanto, S.Kom., M.T. (NIP: 199310222019031016)
* **Koordinator Program Studi:** Awang Harsa Kridalaksana, S.Kom., M.Kom.
* **Berkas yang Dievaluasi:** [draft_proposal_muhammad_khairrudin_revisi2.pdf](draft_proposal_muhammad_khairrudin_revisi2.pdf) (Naskah Draf Proposal Revisi 2 Skripsi, 77 Halaman)
* **Tanggal Evaluasi:** 29 September 2026
* **Status Keputusan:** 🟢 **ACC / DISETUJUI UNTUK MAJU SEMINAR PROPOSAL (DENGAN REVISI MINOR TERAKHIR)**

---

## 🌟 1. Evaluasi Kelayakan untuk S1 Informatika

### A. Apakah Topik Ini Layak untuk S1 Informatika?
**JAWABAN: SANGAT LAYAK.**

Sebagian mahasiswa dan dosen terkadang khawatir topik IoT dianggap terlalu dekat dengan *Teknik Elektro* atau *Teknik Lingkungan*. Namun, proposal Saudara **Muhammad Khairrudin** memiliki pilar keilmuan Informatika (Computer Science) yang sangat kuat dan dominan, yaitu:

1. **Intelligent Edge Computing (Komputasi Cerdas di Perangkat Keras):**
   Saudara tidak sekadar membaca sensor lalu mengirim data mentah (*raw data*) ke internet, melainkan menanamkan inferensi kecerdasan buatan (*Fuzzy Inference System Mamdani*) secara lokal pada mikrokontroler ESP32. Mikrokontroler melakukan komputasi fuzzifikasi, evaluasi 27 aturan, dan defuzzifikasi mandiri tanpa bergantung pada pemrosesan server cloud.
2. **Distributed Architecture & Cloud Telemetry:**
   Integrasi telemetri antara sensor tepi (*edge*), platform *Firebase Realtime Database*, dan *Web Dashboard* interaktif untuk pemantauan *real-time* serta visualisasi tren historis.
3. **Fault-Tolerant & Offline-to-Online Data Synchronization:**
   Implementasi penyimpanan cadangan lokal (*local logging*) ke modul MicroSD saat koneksi jaringan terputus, dilengkapi mekanisme sinkronisasi susulan (*deferred sync*) saat koneksi pulih kembali.
4. **Mathematical Rigor (Ketajaman Matematis):**
   Saudara menyertakan perumusan matematis fungsi keanggotaan dan simulasi perhitungan manual numerik langkah demi langkah di Bab III yang teruji konsisten dengan algoritma program.

---

## 👏 2. Apresiasi Perbaikan pada Revisi Ke-2

Saya mengapresiasi kerja keras Saudara dalam menindaklanjuti audit sebelumnya. Pada draf revisi ke-2 ini, banyak hal penting yang sudah diperbaiki dengan sangat baik:

* ✅ **Penomoran Halaman (*Pagination*) Sudah Rapi:** Bagian awal telah menggunakan angka Romawi kecil (`i` s.d. `x`), dan halaman Bab I Pendahuluan telah benar dimulai dari halaman angka Arab `1`.
* ✅ **Penambahan Rumus Kurva Trapesium:** Persamaan umum kurva trapesium (Persamaan 2.1a) dan rumus bahu kiri/kanan telah masuk di Bab II Subbab 2.5.1.
* ✅ **Standardisasi Parameter Himpunan Input:** Parameter input pada Tabel 3.4 telah menggunakan format empat titik $[a, b, c, d]$ untuk trapesium dan tiga titik $[a, b, c]$ untuk segitiga.
* ✅ **Sitasi Hantu (*Ghost Citation*) Terselesaikan:** Pustaka *(Hasib & Akib, 2026)* kini telah tercantum lengkap pada Daftar Pustaka (Halaman 63).
* ✅ **Tabel Jadwal Penelitian Terisi:** Tabel 3.10 (Halaman 61) telah dilengkapi arsiran jadwal pelaksanaan kegiatan dari bulan Juli hingga November 2026.
* ✅ **Judul Tahap 4 Pulih:** Subbab *3.1 Tahap 4 (Implementasi Purwarupa / Prototype)* pada Halaman 37 sudah memiliki judul yang utuh dan tidak terpotong.

---

## 🚨 3. Catatan Revisi Terakhir (Wajib Diperbaiki Sebelum Cetak/Sempro)

Terdapat beberapa poin kecil namun krusial yang harus dirapikan agar Saudara tidak menjadi sasaran empuk pertanyaan kritis dewan penguji saat Seminar Proposal:

---

### 🔴 Catatan Kritis 1: Kerancuan Konsep *Confusion Matrix* (Bab 3.6.2, Hal. 59–60)
* **Masalah pada Naskah Saat Ini:**  
  Pada Subbab 3.6.2 dan Tabel 3.8, Saudara menuliskan bahwa *Confusion Matrix* dihitung dengan membandingkan **status hasil program ESP32** terhadap **status hasil perhitungan manual Saudara di atas kertas menggunakan rumus fuzzy yang sama**.
* **Kenapa Ini Salah Secara Metodologi?**  
  Jika mikrokontroler ESP32 mengodingkan rumus fuzzy yang sama persis dengan yang Saudara hitung di kertas, maka membandingkan keduanya hanyalah **Uji Verifikasi Koding / Unit Testing** (memastikan tidak ada kesalahan penulisan rumus dalam bahasa C++). Hasilnya pasti 100% cocok jika kodingnya benar!  
  *Confusion Matrix* (Akurasi, Presisi, Recall) memerlukan **Ground Truth (Kondisi Nyata Sebenarnya)**, bukan rumus Saudara sendiri.
* **Solusi Perbaikan Mudah:**  
  Pisahkan pengujian menjadi dua tujuan yang jelas di Bab 3.6.2:
  1. **Uji Verifikasi Algoritma Program (MAPE):** Membandingkan nilai tegas $z^*$ hasil komputasi ESP32 terhadap nilai $z^*$ hitungan manual untuk membuktikan ketepatan matematis implementasi kode (Tabel 3.8).
  2. **Uji Validasi Klasifikasi (Confusion Matrix):** Bandingkan status hasil klasifikasi alat fuzzy Saudara terhadap **data uji lapangan yang dilabeli acuan eksternal** (misalnya: status mutu air berdasarkan perhitungan metode resmi KLHK/Indeks Pencemaran pada Stasiun ONLIMO KLHK 167 di waktu yang sama, atau penilaian sampel laboratorium).
* **Koreksi Typo Header Tabel 3.8 (Hal. 60):**  
  Header kolom ke-2 dan ke-3 tertulis sama persis: `z* Manual` dan `z* Manual`.  
  👉 **Ubah menjadi:** Kolom 2 = `z* Manual`, Kolom 3 = `z* Sistem (ESP32)`.

---

### 🔴 Catatan Kritis 2: Inkonsistensi Rentang Output Kategori Status Air (Hal. 31 vs Hal. 57)
* **Masalah pada Naskah Saat Ini:**
  * Di **Halaman 31 (Bab II) & Halaman 50 (Tabel 3.4)**, rentang nilai $z^*$ output adalah:
    * Buruk: $0 - 50$ (titik pusat 25)
    * Sedang: $25 - 75$ (titik pusat 50)
    * Baik: $50 - 100$ (titik pusat 75)
  * Namun di **Halaman 57 (Subbab 3.5.2 - Keterangan Dashboard)** tertulis:
    * *Buruk: 0–33, Sedang: 34–66, Baik: 67–100*
* **Solusi Perbaikan:**  
  Samakan deskripsi di Halaman 57 dengan rentang pada perancangan fuzzy sebelumnya:
  > *"Panel keterangan status, menampilkan rentang nilai $z^*$ untuk tiap kategori (Buruk: 0–50 dengan pusat 25, Sedang: 25–75 dengan pusat 50, Baik: 50–100 dengan pusat 75), konsisten dengan rancangan himpunan fuzzy pada Tabel 3.4."*

---

### 🟡 Catatan Kritis 3: Koordinat Trapesium Bahu Kiri Output (Tabel 3.4, Hal. 50)
* Pada Tabel 3.4, untuk variabel **Status Air (output)** kategori **Buruk**, tertulis parameter `0, 25, 50 (Trapesium Bahu Kiri)` (hanya 3 titik).
* Karena kurva trapesium membutuhkan 4 titik $[a, b, c, d]$, ubah menjadi:  
  👉 `0.0, 0.0, 25.0, 50.0 (Trapesium Bahu Kiri)` (sama seperti pola himpunan input bahu kiri lainnya di mana $a=b$).

---

### 🟡 Catatan Kritis 4: Teks Duplikat & Salah Nomor Tabel (Hal. 54)
* Di Halaman 54, paragraf berikut muncul **dua kali** (sebelum Tabel 3.6 dan terulang persis di bawah Tabel 3.6):
  > *"Data hasil pengolahan pada sistem ini dirancang dalam bentuk yang ringkas namun tetap memuat informasi utama yang diperlukan untuk keperluan pemantauan maupun analisis lebih lanjut. Payload yang dikirim memuat tujuh informasi utama... Struktur payload ditunjukkan pada Tabel 3.5."*
* Selain berulang dua kali, narasinya menyebut `Tabel 3.5`, padahal tabel yang dirujuk adalah `Tabel 3.6`.  
* **Solusi:** Hapus paragraf duplikat di bawah Tabel 3.6, dan perbaiki sebutan nomor tabel menjadi `Tabel 3.6`.

---

### 🟡 Catatan Kritis 5: Formalia & Placeholder yang Tertinggal
1. **Halaman Pengesahan (Hal. ii):**  
   Cantumkan NIP Dosen Pembimbing lengkap:
   * Reza Wardhana, S.Kom., M.Eng. (lengkapi NIP)
   * Anton Prafanto, S.Kom., M.T. (NIP: 199310222019031016)
2. **Kata Pengantar (Hal. iii, Poin 5):**  
   Masih terdapat kalimat template:  
   *`5. Nama dan gelar akademik Dosen Penguji II selaku Penguji II atas saran dan masukkan terhadap penelitian ini.`*  
   👉 **Hapus poin 5 ini**, karena pada tahap seminar proposal dewan penguji belum melaksanakan ujian. Ucapan terima kasih untuk dewan penguji baru dimasukkan pada naskah Skripsi Final (setelah pendadaran).
3. **Daftar Lampiran (Hal. viii):**  
   Masih tertulis `Lampiran 1 contents 42`.  
   👉 Bersihkan kata `contents 42` menjadi: `Lampiran 1: Surat Pengantar Penelitian dari Fakultas Teknik Universitas Mulawarman ......... 66`.

---

## 🎯 4. Kisi-Kisi Menghadapi Ujian Seminar Proposal

Persiapkan jawaban taktis berikut jika dewan penguji menanyakan hal-hal fundamental:

| Pertanyaan Dosen Penguji | Rekomendasi Cara Menjawab |
| :--- | :--- |
| **"Mengapa menggunakan Fuzzy Mamdani dan bukan algoritma Machine Learning modern?"** | *"Baku mutu kualitas air (PP No. 22/2021 & Permenkes No. 2/2023) sudah memiliki ambang batas linguistik yang pasti (asam, netral, deviasi 3°C), sehingga dapat langsung dimodelkan menggunakan sistem berbasis aturan pakar tanpa memerlukan dataset latih ribuan baris. Selain itu, Fuzzy Mamdani bersifat explainable AI (setiap keputusan status dapat dilacak logikanya) dan sangat ringan untuk dieksekusi secara real-time langsung di mikrokontroler ESP32."* |
| **"Mengapa defuzzifikasi menggunakan Weighted Average / Discrete Centroid?"** | *"ESP32 adalah mikrokontroler berdaya rendah. Defuzzifikasi Center of Gravity murni memerlukan integrasi kontinu fungsi poligon yang memakan siklus clock prosesor dan memori. Discrete Height Centroid (Weighted Average) memberikan hasil pendekatan yang sangat presisi dengan kompleksitas komputasi $O(N)$ yang jauh lebih efisien untuk sistem telemetri."* |
| **"Kenapa menggunakan selisih suhu $(\Delta T)$ bukan suhu air langsung?"** | *"Karena regulasi PP No. 22 Tahun 2021 Lampiran VI tidak membatasi suhu air pada angka mutlak tertentu, melainkan membatasi deviasi suhu air maksimal 3°C terhadap suhu udara di sekitarnya. Pendekatan $\Delta T = \lvert T_{\text{air}} - T_{\text{udara}}\rvert$ mencerminkan kepatuhan terhadap baku mutu regulasi secara akurat dalam berbagai kondisi cuaca."* |

---

## 📌 Kesimpulan & Langkah Selanjutnya

1. Lakukan perbaikan minor di atas (estimasi waktu pengerjaan: 1–2 jam di Microsoft Word).
2. Setelah diperbaiki dan dikonversi ke PDF terbaru, proposal dinyatakan **SIAP DITANDATANGANI (ACC)** oleh Dosen Pembimbing untuk pendaftaran Seminar Proposal.
3. Tetap semangat, persiapan Saudara sudah sangat matang dan terarah!
