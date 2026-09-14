# 📋 LAPORAN AUDIT AKADEMIK & PANDUAN REVISI PROPOSAL SKRIPSI

**Mahasiswa Bimbingan:** Abdullah Arkananta Rasendrya Hasan  
**NIM:** 2209106085  
**Program Studi:** S1 Informatika, Fakultas Teknik, Universitas Mulawarman  
**Dosen Pembimbing I:** Rosmasari, S.Kom., M.T.  
**Dosen Pembimbing II:** Anton Prafanto, S.Kom., M.T.  
**Koordinator Program Studi:** Awang Harsa Kridalaksana, S.Kom., M.Kom.  
**Judul Proposal:** *Rancang Bangun Sistem Monitoring pH dan Suhu Air Kolam Ikan Nila Berbasis Internet of Things Menggunakan Metode Rule-Based*  
**Berkas yang Dievaluasi:**
1. `draft proposal update.pdf` (Naskah Draf Proposal Skripsi, 48 Halaman)
2. `RINGKASAN RANCANGAN SISTEM MONITORING KUALITAS AIR.pdf` (Naskah Ringkasan Rancangan Sistem & Matriks Revisi, 4 Halaman)  
**Tanggal Evaluasi:** 14 September 2026  
**Status Naskah:** **Revisi Mayor Formalia, Sinkronisasi Arsitektur Sistem & Perbaikan Total Daftar Pustaka (Wajib Dibenahi Sebelum Dijadwalkan Seminar Proposal)**

---

## 🌟 1. Apresiasi & Catatan Positif Naskah

Secara konsep dasar dan rancangan fungsional, proposal skripsi yang disusun oleh Saudara **Abdullah Arkananta Rasendrya Hasan** memiliki potensi penelitian terapan yang **sangat aplikatif, tepat sasaran, dan solutif**:

1. **Relevansi Nyata bagi Sektor Perikanan:** Pemilihan objek budidaya ikan nila (*Oreochromis niloticus*) sangat kontekstual. Kematian bibit ikan nila di kolam budidaya air tawar lokal kerap dipicu oleh fluktuasi mendadak parameter suhu dan derajat keasaman (pH) yang terlambat diketahui oleh pembudidaya.
2. **Matriks Keputusan 9 Aturan (*9-Rule Matrix*) Sangat Terstruktur:** Berkas ringkasan (*addendum*) yang Saudara susun telah memetakan kombinasi 3 level suhu (Dingin, Ideal, Panas) dan 3 level pH (Asam, Ideal, Basa) menjadi 3 kategori status (*Sangat Baik*, *Waspada*, *Bahaya*) lengkap dengan rekomendasi tindakan lapangan yang operasional (seperti pemberian kapur dolomit/buffer naik, daun ketapang/buffer turun, penyalaan sirkulasi/heater, hingga kuras air darurat).
3. **Pemanfaatan Ekosistem IoT Modern:** Pemilihan mikrokontroler ESP32 yang dipadukan dengan platform Blynk Cloud, Web Console, dan Blynk Mobile App dengan fitur *Blynk Events (Push Notification)* merupakan arsitektur yang sangat efisien dan berbiaya terjangkau (*low-cost IoT*) bagi kalangan pembudidaya.

Namun demikian, hasil audit forensik menunjukkan bahwa **naskah 48 halaman masih berada dalam kondisi draf mentah (*unpolished draft*) dengan banyak sisa teks template, salah penempatan kolom, inkonsistensi arsitektur, ketiadaan diagram sistem di dalam naskah, serta anomali Daftar Pustaka yang sangat fatal**. Catatan di bawah ini wajib diselesaikan secara menyeluruh demi menjaga marwah akademik Saudara di hadapan Dosen Penguji Seminar Proposal.

---

## 🚦 2. Matriks Status Kesiapan Naskah

| Komponen Naskah | Status | Catatan Evaluasi Kritis |
| :--- | :---: | :--- |
| **Halaman Depan & Pengesahan** | 🚨 *Fatal / Etika* | **Hapus teks catatan informal pembimbing** (`bu ros tercinta` dan `pak anton jago iot`). Perbarui titimangsa tanggal rapat dan standarisasi penulisan gelar dosen pembimbing & koorprodi. |
| **Kata Pengantar & Bagian Awal** | 🚨 *Revisi Berat* | Hapus teks petunjuk template Word Fakultas Teknik; ganti `<Judul Skripsi>`; ganti tahun 2024 menjadi 2026; perbaiki `Error! Bookmark not defined.` pada Daftar Isi; isi Daftar Tabel, Gambar, Lampiran, Singkatan yang masih berupa placeholder `contents`. |
| **Sistematika Halaman (*Pagination*)** | ⚠️ *Revisi Sedang* | Nomor romawi kecil (`i, ii, ...`) untuk bagian awal; nomor arab (`1, 2, ...`) untuk isi bab; **beri Page Break pada Halaman 33** (Bab III saat ini menempel langsung di bawah rumus Bab II). |
| **Bab I: Pendahuluan** | ⚠️ *Revisi Ringan* | Pertegas fokus parameter (pH dan Suhu); perjelas status integrasi Blynk Web Console vs Mobile App; rapikan kalimat repetitif pada kontribusi penelitian. |
| **Bab II: Tinjauan Pustaka** | ⚠️ *Revisi Sedang* | Awali ulasan 8 penelitian terkait dengan nama peneliti & judul; tambahkan **Tabel Matriks SOTA (*State-of-the-Art*)**; bersihkan sisa teks copas mentah (`( artikel https://... )`, `SOCA JournalPtdsak`, `Politama`); satukan pembahasan sensor pH (Subbab 2.11 dan 2.14 yang mendua). |
| **Bab III: Metodologi & Desain** | 🚨 *Revisi Krusial* | **Koreksi Tabel 3.4** (kolom pH dan Suhu tertukar, typo *Wapada*); **integrasikan Flowchart Sistem** dari dokumen ringkasan ke dalam naskah; **selesaikan kontradiksi arsitektur** (apakah murni Blynk Cloud atau membuat Web Server kustom + Database SQL); lengkapi skematik pinout ESP32 (ADC1 vs ADC2, pull-up resistor DS18B20); perbaiki angka anomali pada mockup Hal. 41 (Suhu 7°C). |
| **Jadwal Penelitian** | ⚠️ *Revisi Sedang* | Perbaiki Tabel 3.x Jadwal Penelitian: kolom bulan melompat dari Januari langsung ke Agustus (Feb–Jul hilang); hapus elipsis template (`…`); isi arsir/centang jadwal. |
| **Daftar Pustaka & Sitasi** | 🚨 *Fatal (Red Alert)* | **Daftar Pustaka saat ini 100% keliru (berisi 5 referensi kelapa sawit & pengolahan citra dari template bawaan)!** Masukkan 25–30 referensi IoT kualitas air ikan nila yang sebenarnya dikutip di Bab I–III menggunakan Mendeley/Zotero. |
| **Lampiran Naskah** | ⚠️ *Perlu Dibenahi* | **Hapus kalimat `Penjelasan lihat di ppt`** pada Hal. 48. Ganti dengan skematik rangkaian Fritzing, datasheet komponen, atau lembar kalibrasi sensor. |

---

## 🔍 3. Rincian Temuan Forensik & Panduan Perbaikan Mandiri

---

### 📄 A. Bagian Awal Naskah (Cover s.d. Daftar Singkatan)

#### 1. 🚨 Catatan Informal pada Lembar Pengesahan (Hal. 3)
* **Temuan Fatal:** Pada halaman 3 baris Dosen Pembimbing tertulis:
  * `I. Nama Dosen Pembimbing I lengkap dengan gelar bu ros tercinta`
  * `II. Nama Dosen Pembimbing II lengkap dengan gelar pak anton jago iot`
  * Tanggal rapat pembimbing masih tertulis `[tgl, bln, tahun]`.
* **Dampak Akademik:** Jika naskah ini tercetak atau terkirim ke panitia seminar proposal atau dosen penguji, hal ini melanggar etika tata tulis resmi dan dapat membuat proposal Saudara langsung ditolak di meja tata usaha prodi.
* **Solusi Perbaikan:** Ganti seluruh teks tersebut dengan format formal yang berlaku di Fakultas Teknik UNMUL:
  ```text
  Telah dibahas dalam Rapat Dosen Pembimbing pada .................... 2026 dan 
  dinyatakan memenuhi syarat untuk diseminarkan, dengan Dosen Pembimbing:

  Pembimbing I: Rosmasari, S.Kom., M.T.             NIP 19800720 200501 2 001
  Pembimbing II: Anton Prafanto, S.Kom., M.T.       NIP 19931022 201903 1 016

  Mengetahui,
  Koordinator Program Studi S1 Informatika
  Fakultas Teknik, Universitas Mulawarman,

  Awang Harsa Kridalaksana, S.Kom., M.Kom.
  NIP 19731229 200501 1 002
  ```

#### 2. 🚨 Sisa Panduan Template pada Kata Pengantar (Hal. 4)
* **Temuan:** Paragraf pertama Kata Pengantar masih memuat teks petunjuk penyusunan dari buku pedoman skripsi:
  > *"Kata Pengantar (preface, foreword) sebaiknya disusun secara ringkas dan tidak lebih dari 2 halaman (lihat contoh Lampiran 9). Isi Kata Pengantar mencakup: a. kalimat pembuka; b. tempat dan waktu pengumpulan data; c. ucapan terima kasih dengan hirarki sebagai berikut..."*
  Selain itu, judul skripsi masih tertulis placeholder `“<Judul Skripsi>”`, daftar ucapan terima kasih masih memuat teks template (`Nama dan gelar akademik lengkap Dekan...`, `Nama dan gelar Koordinator Prodi...`, dll.), serta titimangsa masih tertulis tahun lampau: `Samarinda,.............................. 2024`.
* **Solusi Perbaikan:**
  - Hapus paragraf instruksi template tersebut.
  - Masukkan judul proposal Saudara secara utuh dengan huruf kapital miring (*Title Case/Italic*).
  - Isi nama Dekan FT UNMUL saat ini dan nama dosen pembimbing secara lengkap.
  - Perbarui tahun menjadi `2026`.

#### 3. 🚨 Kerusakan Daftar Isi & Placeholder "Contents" (Hal. 5–10)
* **Temuan:**
  - **Daftar Isi (Hal. 5):** Terdapat banyak baris bertuliskan `Error! Bookmark not defined.` pada subbab 2.1, 2.2, 2.3, 2.3.1, dan 2.4. Subbab Bab I dan Bab III hanya mencantumkan nomor angka tanpa judul subbab (`1.1 1`, `1.2 3`, `3.1 20`, dst.). Selain itu, masih tersisa teks template `2.3.2 Teori Pendukung Sub BAB 5`.
  - **Daftar Tabel (Hal. 6):** Masih memuat kalimat instruksi `WAJIB menggunakan alat bantu TOC (Table of Contents) pada Microsoft Word.` dan hanya mencantumkan entri palsu: `Tabel 1.1 contents 6`, `Tabel 2.2 contents 7`.
  - **Daftar Gambar, Lampiran, Istilah, Singkatan (Hal. 7–10):** Semuanya hanya memuat teks bawaan `contents` dan belum terisi.
* **Solusi Perbaikan:**
  - Pastikan setiap judul Bab menggunakan *Heading 1*, setiap Subbab menggunakan *Heading 2*, dan Anak Subbab menggunakan *Heading 3* pada Microsoft Word.
  - Hapus teks instruksi manual.
  - Klik kanan pada area Daftar Isi/Tabel/Gambar lalu pilih **Update Field -> Update entire table**.
  - Isi **Daftar Singkatan & Istilah** secara nyata:
    * *ADC*: Analog to Digital Converter
    * *API*: Application Programming Interface
    * *BNC*: Bayonet Neill–Concelman (konektor probe pH)
    * *DO*: Dissolved Oxygen (Oksigen Terlarut)
    * *ESP32*: Espressif Systems 32-bit Microcontroller
    * *IoT*: Internet of Things
    * *MAPE*: Mean Absolute Percentage Error
    * *pH*: Potential of Hydrogen
    * *RSSI*: Received Signal Strength Indicator
    * *SOTA*: State of the Art
    * *UI/UX*: User Interface / User Experience

#### 4. ⚠️ Penomoran Halaman (*Pagination Section Break*)
* **Temuan:** Halaman cover dalam tercetak angka `1`, Lembar Pengesahan `2`, Kata Pengantar `3`, Daftar Isi `4`. Masuk ke Bab I Pendahuluan ter-reset ke angka `1`, Bab II ter-reset ke angka `3`, Bab III ke angka `20`, dan Daftar Pustaka ke angka `9`.
* **Aturan Baku FT UNMUL:**
  - Bagian Awal (Halaman Judul s.d. Daftar Singkatan) wajib menggunakan **angka Romawi kecil (`i, ii, iii, iv, v, ...`)** di posisi tengah bawah. Halaman judul dalam dihitung sebagai `i` namun tidak dicetak.
  - Halaman Isi (Bab I s.d. Lampiran) menggunakan **angka Arab (`1, 2, 3, ...`)** yang berurutan secara kontinu tanpa pernah ter-reset kembali ke angka 1 di tengah bab. Posisi nomor di tengah bawah untuk halaman pertama bab baru, dan di kanan atas untuk halaman lanjutan bab tersebut.

---

### 📘 B. BAB I – Pendahuluan

1. **Konsistensi Platform Pemantauan & Batasan Masalah (Subbab 1.3 & 1.4):**
   * **Temuan:** Di Bab 1 butir 4 disebutkan bahwa penyajian data divisualisasikan menggunakan platform IoT (Blynk) yang menyediakan Web Dashboard dan Mobile Application. Namun di Bab II Subbab 2.17 dan Bab III Subbab 3.3, Saudara mendadak membahas pembuatan antarmuka web kustom dari nol dengan HTML, CSS, JavaScript, Bootstrap, API, dan tabel database SQL mandiri.
   * **Arahan:** Batasan masalah harus secara tegas menyatakan arsitektur yang digunakan. Jika Saudara murni memanfaatkan **Blynk IoT Platform**, nyatakan bahwa visualisasi web menggunakan *Blynk Web Console* dan aplikasi mobile menggunakan *Blynk IoT App*. Hal ini untuk mencegah penguji menuntut kodingan website PHP/Laravel/Node.js yang tidak Saudara buat.
2. **Koreksi Typo Subbab 1.1 (Latar Belakang Hal. 13):**
   * Pada alinea terakhir halaman 13 tertulis: `Untuk menjwab kebutuhan tersebut...`. Perbaiki typo menjadi `Untuk menjawab kebutuhan tersebut...`.
3. **Pemberian Bobot Research Gap pada Kontribusi Penelitian (Subbab 1.6):**
   * Pertegas bahwa kontribusi kebaruan penelitian ini terletak pada **kombinasi 9-rule matriks simultan suhu dan pH yang dijalankan langsung pada firmware ESP32 (Edge Processing)**, sehingga pembudidaya tidak hanya melihat angka mentah, melainkan menerima peringatan dini otomatis (*Push Notification*) beserta saran mitigasi fisik kolam secara instan.

---

### 📗 BAB II – Tinjauan Pustaka & Landasan Teori

#### 1. Format Narasi 8 Penelitian Terkait (Subbab 2.1, Hal. 16–19)
* **Temuan:** Butir 1 pada halaman 16 diawali dengan kalimat tanpa subjek:
  * *`1. Metode yang digunakan pada penelitian ini adalah Internet of Things (IoT) untuk monitoring pH dan suhu kolam ikan lele...`*
* **Solusi Perbaikan:** Seluruh butir penelitian terdahulu wajib diawali dengan identitas peneliti, tahun publikasi, dan judul penelitian agar memiliki bobot sitasi ilmiah yang baku:
  > *"1. Penelitian yang dilakukan oleh **Manurung et al. (2022)** berjudul 'Sistem Monitoring Kualitas Air Kolam Ikan Lele Berbasis IoT' mengkaji pemantauan suhu dan pH menggunakan NodeMCU..."*

#### 2. Wajib Menyisipkan Tabel Matriks Perbandingan (*State-of-the-Art* / SOTA)
* Pada akhir Subbab 2.1 / Subbab 2.2 (Hal. 19–20), penguji selalu menanyakan posisi penelitian Saudara dibanding penelitian terdahulu. Gunakan tabel sintesis berikut pada naskah revisi:

| No | Peneliti & Tahun | Objek Penelitian | Parameter Input | Mikrokontroler / Komunikasi | Metode Pengambilan Keputusan | Antarmuka Pengguna | Keterbatasan / Research Gap | Posisi & Kebaruan Penelitian Ini |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | Manurung et al. (2022) | Kolam Ikan Lele | Suhu & pH | NodeMCU ESP8266, Wi-Fi | Tanpa metode cerdas (Biner/Threshold sederhana) | Blynk App | Hanya visualisasi pasif tanpa rekomendasi tindakan kolam. | Menerapkan Rule-Based 9 Matriks dengan rekomendasi aksi spesifik. |
| 2 | Subianto & Wardhana (2024) | Ikan Nila | Suhu, pH, TDS, Turbidity, Amonia | Arduino Uno, Offline | Rule-Based Reasoning | Serial Monitor / Offline | Belum terintegrasi IoT dan tidak ada sistem peringatan jarak jauh. | Terintegrasi penuh dengan IoT Blynk Cloud & Push Notification smartphone. |
| 3 | Maulana et al. (2021) | Ikan Lele | Suhu & pH | NodeMCU ESP8266 | Logika Fuzzy Mamdani | Telegram Bot | Defuzzifikasi fuzzy berat pada MCU murah; notifikasi chat teks biasa. | Inferensi Rule-Based ringan langsung di ESP32 dengan widget visual interaktif. |
| 4 | Camelia et al. (2026) | Ikan Nila Bioflok | Suhu & pH | ESP32, Wi-Fi | Monitoring Pasif (Tanpa Pengambil Keputusan) | Blynk App | Rekomendasi risetnya meminta penambahan sistem inferensi otomatis. | **Menjawab langsung limitasi Camelia et al.** dengan menambahkan mesin inferensi 9 aturan & early warning. |
| **5** | **Penelitian Ini (Hasan, 2026)** | **Kolam Budidaya Ikan Nila** | **Suhu Air (DS18B20) & Derajat Keasaman (pH SEN0161-V2)** | **ESP32 (30 Pin), Wi-Fi 2.4 GHz** | **Rule-Based Forward Chaining (9 Aturan Kombinasi)** | **Blynk Web Console & Blynk Mobile App (Push Notification)** | - | **Sistem pemantauan kualitas air terpadu dengan inferensi cerdas lokal (edge), klasifikasi 3 tingkat kondisi, notifikasi kritis seketika, dan panduan tindakan budidaya.** |

#### 3. Pembersihan Jejak Copas Mentah & Anomali Teks
* **Hal. 19 Subbab 2.2:** Terdapat kata ganda `Berdasarkan Berdasarkan penelitian-penelitian terkait...`.
* **Hal. 25 Subbab 2.11:** Tertinggal tautan URL mentah dan nama jurnal yang terpotong di tengah kalimat:
  * *`...yang dapat dianalisis. ( artikel https://www.ptdsak.com/blog/apa-itu-sensor-ph-fungsi-dan-aplikasinya-di-industri )`*
  * *`...menghasilkan sinyal yang dikonversi menjadi nilai pH. SOCA JournalPtdsak`*
* **Hal. 26:** Tertinggal kata terpotong di akhir paragraf:
  * *`...dalam penelitian ilmiah, pemantauan lingkungan, dan kontrol kualitas. Politama`*
* **Hal. 29 & 37 (Typo Nomenklatur Sensor):** Tertulis `Sensor pH DFRobot SEN0161-V12`. Kode tipe resmi sensor tersebut adalah **SEN0161-V2** (versi 2), bukan versi 12.
* **Penomoran Tabel Teori:** Di Subbab 2.6, 2.13, dan 2.14, nama tabel masih ditulis `Tabel 2.x Klasifikasi...`, `Tabel 2.x Spesifikasi NodeMCU...`, `Tabel 2.x Spesifikasi Sensor...`. Berikan nomor terurut: **Tabel 2.1, Tabel 2.2, dan Tabel 2.3**.

---

### 📙 C. BAB III – Metodologi Penelitian & Desain Sistem

#### 1. 🚨 Transisi Tanpa Halaman Baru (*Page Break Missing*) pada Hal. 33
* **Temuan:** Di halaman 33 naskah (setelah rumus MAPE dan Gambar 2.1), judul **BAB III METODOLOGI PENELITIAN** langsung ditulis bersambung pada halaman yang sama tanpa ada pemisah halaman.
* **Solusi:** Wajib menyisipkan **Page Break (Ctrl + Enter)** sebelum tajuk BAB III agar bab baru dimulai rapi di halaman baru.

#### 2. 🚨 Koreksi Fatal Tabel 3.4 (Kolom pH dan Suhu Tertukar & Typo)
* **Temuan:** Pada Tabel 3.4 (Hal. 38), judul kolom dan isi data tertukar total:
  - Kolom berjudul **Kondisi pH** justru diisi data suhu: `Dingin (<25)`, `Ideal (25-30)`, `Panas (>30)`.
  - Kolom berjudul **Kondisi Suhu** justru diisi data pH: `Asam (<6.5)`, `Ideal (6.5-8.5)`, `Basa (>8.5)`.
  - Pada baris R8, kolom Kategori tertulis typo: `Wapada` (kurang huruf 's').
* **Bandingkan dengan Dokumen Ringkasan:** Di berkas *RINGKASAN RANCANGAN SISTEM MONITORING KUALITAS AIR.pdf* yang Saudara buat secara terpisah, tabel ini sudah benar. Namun di dalam naskah utama draf skripsi, Saudara belum memperbaruinya!
* **Tabel Revisi Baku (Wajib Disalin ke Naskah Skripsi):**

| Rule | Kondisi Suhu Air (°C) | Kondisi Derajat Keasaman (pH) | Kategori Status Mutu | Rekomendasi Tindakan / Aksi Sistem |
| :---: | :---: | :---: | :---: | :--- |
| **R1** | Dingin ($< 25^\circ\text{C}$) | Asam ($< 6.5$) | **Bahaya** | Air mematikan bagi ikan nila. Segera kuras dan ganti air kolam! |
| **R2** | Dingin ($< 25^\circ\text{C}$) | Ideal ($6.5 - 8.5$) | **Waspada** | Suhu air terlalu rendah. Nyalakan pemanas kolam (*heater*) atau kurangi aerasi malam. |
| **R3** | Dingin ($< 25^\circ\text{C}$) | Basa ($> 8.5$) | **Bahaya** | Air mematikan bagi ikan nila. Segera kuras dan ganti air kolam! |
| **R4** | Ideal ($25^\circ\text{C} - 30^\circ\text{C}$) | Asam ($< 6.5$) | **Waspada** | Derajat keasaman terlalu rendah (asam). Berikan kapur pertanian/dolomit secara bertahap. |
| **R5** | Ideal ($25^\circ\text{C} - 30^\circ\text{C}$) | Ideal ($6.5 - 8.5$) | **Sangat Baik** | Kualitas air sangat optimal. Pertahankan sirkulasi dan jadwal pakan normal. |
| **R6** | Ideal ($25^\circ\text{C} - 30^\circ\text{C}$) | Basa ($> 8.5$) | **Waspada** | Derajat keasaman terlalu tinggi (basa). Tambahkan daun ketapang kering atau buffer penurun pH. |
| **R7** | Panas ($> 30^\circ\text{C}$) | Asam ($< 6.5$) | **Bahaya** | Air mematikan bagi ikan nila. Segera kuras dan ganti air kolam! |
| **R8** | Panas ($> 30^\circ\text{C}$) | Ideal ($6.5 - 8.5$) | **Waspada** | Suhu air terlalu panas. Nyalakan pompa sirkulasi air segar atau tambahkan peneduh kolam. |
| **R9** | Panas ($> 30^\circ\text{C}$) | Basa ($> 8.5$) | **Bahaya** | Air mematikan bagi ikan nila. Segera kuras dan ganti air kolam! |

#### 3. 🚨 Ketiadaan Diagram Alir (*Flowchart*) Sistem pada Bab III
* **Temuan:** Dokumen naskah proposal 48 halaman **sama sekali tidak memiliki diagram alir sistem**. Di halaman 33 hanya terdapat diagram tahapan penelitian (kotak oranye). Padahal, di dokumen ringkasan 4 halaman terdapat gambar flowchart sistem yang sangat baik (halaman 3 ringkasan).
* **Solusi:** Pindahkan dan pasang diagram alir tersebut ke Bab III Subbab 3.4 sebagai **Gambar 3.2 Flowchart Alur Kerja Sistem Monitoring Kualitas Air**. Pastikan panah perulangan (*looping*) kembali ke pembacaan sensor dan hapus terminator "Selesai" jika sistem dirancang bekerja kontinu (*infinite loop*).

#### 4. 🚨 Selesaikan Kontradiksi Arsitektur Sistem (Blynk Cloud vs Database SQL Kustom)
* **Temuan Kritis:**
  - Di Subbab 1.3 & 1.4: Saudara menyatakan menggunakan **Blynk IoT**.
  - Namun di Subbab 3.3 (Hal. 36–37): Saudara membuat Tabel Struktur Database SQL (`id_monitoring`, `id_perangkat`, `nilai_ph`, `nilai_suhu`, `kategori`, `status_detail`, `rekomendasi`, `waktu`) dan menyatakan: *"ESP32 mengirimkan data ke API server, lalu server menjalankan rule-based dan menyimpan ke database..."*.
  - Di Subbab 3.4 Pseudocode (Hal. 40): Saudara menuliskan *"Simpan ke database, Tampilkan hasil pada Blynk Dashboard, Kirim Push Notification..."*.
  - Di Tabel 3.6 Pengujian Butir 9: Saudara menuliskan *"Menguji halaman login, monitoring, grafik, tabel, dan filter data..."*.
* **Penjelasan Teknis:**
  Platform Blynk adalah *all-in-one IoT PaaS*. Jika Saudara menggunakan Blynk, Saudara **tidak memerlukan** backend API PHP/Node.js buatan sendiri dan tidak memerlukan database MySQL lokal, karena Blynk Cloud telah menyediakan penyimpanan *Datastreams* dan *Virtual Pins*.
* **Keputusan Arsitektur yang Wajib Dipilih Sebelum Sempro:**
  - **Opsi A (Murni Blynk - Direkomendasikan untuk Efisiensi):**
    Hilangkan bahasan rancangan tabel SQL dan backend API mandiri di Subbab 3.3. Jelaskan bahwa seluruh pemrosesan Rule-Based dieksekusi secara **Edge Computing** pada mikrokontroler ESP32. Hasil status dan nilai sensor dikirimkan ke Blynk Cloud melalui *Virtual Pins*:
    * `V0`: Suhu Air (°C)
    * `V1`: Nilai pH
    * `V2`: Status Mutu Air (Teks: Sangat Baik / Waspada / Bahaya)
    * `V3`: Rekomendasi Aksi Tindakan Kolam
    * `Blynk Event`: Pemicu notifikasi darurat (*Push Notification*) ke smartphone pembudidaya.
  - **Opsi B (Dual Platform - Jika Memang Ingin Membangun Website Sendiri):**
    Jika Saudara memang ditugaskan membangun web kustom (Laravel/Express), Saudara harus menjelaskan bahwa ESP32 mengirim data ke REST API server Saudara (untuk disimpan ke MySQL), dan secara paralel mengirim ke Blynk Cloud (khusus untuk notifikasi HP). Jangan mencampuradukkan terminologi keduanya seolah-olah Blynk memiliki database SQL lokal buatan mahasiswa.

#### 5. ⚠️ Perbaikan Desain Antarmuka Mockup (Hal. 41)
* **Temuan pada Gambar Hal. 41:**
  - Judul di gambar tertulis: `Dashboard Monitoring pH` (parameter Suhu hilang dari judul antarmuka).
  - Pada kartu di bawah gauge tertulis: `pH Air: 7` dan `Suhu Air: 7`! Nilai suhu air 7°C sangat tidak masuk akal untuk perairan kolam tropis ikan nila (suhu 7°C adalah air pendingin kulkas!). Padahal jarum gauge di atasnya menunjuk angka 34°.
  - Desain yang ditampilkan adalah wireframe website desktop dengan sidebar abu-abu, bukan tampilan *Blynk Web Console* ataupun *Blynk Mobile App*.
* **Solusi:**
  - Buat tangkapan layar rancangan (*mockup layout*) langsung dari **Blynk Web Console Builder** dan **Blynk Mobile App Developer Mode** dengan widget Gauge, Value Display, SuperChart, dan Event Log yang rapi.
  - Perbaiki label parameter dan masukkan angka realistis (misal: Suhu 28.5°C, pH 7.2, Kategori Sangat Baik).

#### 6. ⚠️ Spesifikasi Elektronika & Pinout Hardware Mikrokontroler
Sebagai calon sarjana Informatika di bidang sistem tertanam, Saudara wajib melengkapi Subbab 3.4 dengan tabel pemetaan pin (*pinout table*) ESP32:
* **Pin DS18B20:** Terhubung ke pin digital (misalnya **GPIO 4**). Beri catatan bahwa jalur data wajib dipasang **resistor pull-up 4.7 kΩ** ke VCC 3.3V agar sinyal bus 1-Wire terbaca stabil.
* **Pin Sensor pH:** Terhubung ke pin analog ADC. **PENTING:** Wajib menggunakan pin pada **ADC1** (misalnya **GPIO 34, 35, atau 36**). **DILARANG** menggunakan ADC2 (GPIO 2, 4, 12, 13, 14, 15, 25, 26, 27) karena ADC2 pada mikrokontroler ESP32 dinonaktifkan oleh sistem saat modul Wi-Fi aktif mentransmisikan data ke cloud!
* **Rumus Kalibrasi Sensor pH:** Wajib mencantumkan persamaan konversi tegangan ADC ke nilai pH:
  $$\text{Voltage} = \frac{\text{AnalogRead}(Pin)}{4095.0} \times 3.3\,\text{V}$$
  $$\text{pH} = m \cdot \text{Voltage} + c$$
  dengan $m$ (slope) dan $c$ (offset) yang diperoleh dari kalibrasi larutan buffer pH 4.01 dan pH 6.86/7.00.

#### 7. ⚠️ Tabel Jadwal Penelitian yang Cacat (Hal. 44–45, Tabel 3.x)
* **Temuan:**
  - Kolom bulan tertulis: `Jan Agu sept okt nov des`. Kolom bulan **Februari, Maret, April, Mei, Juni, dan Juli hilang**!
  - Pada daftar kegiatan masih tertinggal elipsis template bawaan: `4. …`, `3. …`, `6. …`.
  - Tabel sama sekali tidak diarsir/dicentang jadwal pelaksanaannya.
* **Solusi:** Susun tabel jadwal penelitian 2026 secara lengkap dari Januari hingga Desember dengan estimasi waktu yang rasional (lihat template solusi di Bab 4 laporan ini).

---

### 📚 D. BAB IV / DAFTAR PUSTAKA & SITASI (🚨 RED ALERT KRUSIAL)

#### Temuan Investigasi Forensik:
Di dalam naskah Bab I, Bab II, dan Bab III, Saudara mencantumkan lebih dari **25 sitasi jurnal terkini** mengenai IoT kualitas air kolam, ikan nila, ESP32, sensor pH, dan rule-based:
* *Ahmad & Suprianto Bambang (2019)*
* *Anwar & Latifa (2022)*
* *Azizah et al. (2025)*
* *Camelia et al. (2026)*
* *Chua et al. (2025)*
* *Dwiyaniti et al. (2019)*
* *Goi & Nasrul (2025)*
* *Harmilia (2020)*
* *Irwansyah, Said, dan Islah (2024)*
* *Jelinda et al. (2024)*
* *Juanda & Yadi (2020)*
* *Kulla et al. (2020)*
* *Manurung et al. (2022)*
* *Maulana, Kusnadi, dan Asfi (2021)*
* *Mujadin et al. (2017)*
* *Pane & Andriyani (2024)*
* *Rohmah et al. (2021)*
* *Rozaq & Setyaningsih (2018)*
* *Subianto & Wardhana (2024)*
* *Sugiharto et al. (2025)*
* *Yolanda (2023)*

**NAMUN, pada Halaman 46 (Daftar Pustaka), seluruh referensi tersebut HILANG TOTAL dan hanya memuat 5 daftar pustaka berikut:**
1. *Amir, H., Gatot, S., Wisnu, W. (2002). Klasifikasi Objek Dalam Visi Komputer Dengan Analisis Diskriminan.*
2. *Andono, N. P., Muljono, T. S. (2017). Pengolahan Citra Digital. Penerbit Andi.*
3. *Attaphongse, T., Siwaruk, S., Carlos, P. (2015). A Non-Destructive Oil Palm Ripeness Recognition System Using Relative Entropy...*
4. *Burawich, P., Somchai, L., Thanate, K., Mitchai, C., Arno, R. (2017). An Automatic And Rapid System For Grading Palm Bunch Using A Kinect Camera...*
5. *Dinah, C., Sam, H., Usman, A., Tineke, M., Muhammad, M. (2015). Optical Characteristics Of Oil Palm Fresh Fruits Bunch (FFB)...*

Selain itu, teks petunjuk penyusunan referensi dari Fakultas Teknik masih tertinggal di bawah daftar pustaka:
> *"Keterangan: WAJIB menggunakan software management reference (SMR) seperti Mendeley, EndNote, Zotero dll. Komposisi daftar pustaka... Jumlah daftar pustaka yang digunakan... sebanyak 30-50 referensi."*

#### Dampak Fatal:
Ini adalah **kelalaian teknis terberat** dalam proposal ini. Naskah Saudara membahas pemantauan air kolam ikan nila, tetapi daftar pustakanya berisi kematangan buah kelapa sawit (*oil palm*) dan kamera Kinect! Jika hal ini diperiksa saat pendaftaran seminar proposal, naskah Saudara akan langsung **didiskualifikasi / ditolak** oleh koordinator tugas akhir karena dianggap memuat sitasi fiktif (*ghost citations*).

#### Solusi Wajib:
1. Hapus ke-5 referensi kelapa sawit tersebut.
2. Hapus teks kotak keterangan petunjuk template.
3. Buka Mendeley atau Zotero, pastikan seluruh 25–30 paper yang dikutip di dalam naskah telah dimasukkan ke dalam pustaka, lalu gunakan fitur **Insert Bibliography** dengan format **IEEE** atau **APA 7th Edition** (sesuai panduan FT UNMUL).

---

### 📎 E. Bagian Akhir Naskah (Lampiran)

* **Temuan pada Hal. 48:** Di bawah tajuk `LAMPIRAN` hanya tertulis kalimat:
  * `Penjelasan lihat di ppt`
* **Solusi Perbaikan:** Kalimat ini wajib **segera dihapus**. Lampirkan berkas fisik pendukung yang sebenarnya, minimal:
  - **Lampiran 1:** Skematik Pengkabelan (*Wiring Schematic*) Purwarupa ESP32, Sensor DS18B20, dan Sensor pH.
  - **Lampiran 2:** Rencana Lembar Pengujian Validasi Sensor (*Log Sheet Kalibrasi Buffer pH*).
  - **Lampiran 3:** Lembar Spesifikasi Teknis (*Datasheet Singkat*) Sensor DS18B20 dan SEN0161-V2.

---

## 🛠️ 4. Rekonstruksi Komponen Siap Pakai untuk Mahasiswa

Agar proses revisi naskah Saudara dapat berjalan cepat, gunakan rumusan dan tabel siap pakai berikut untuk ditanamkan ke dalam naskah Word:

### A. Tabel Pemetaan Pinout Hardware ESP32 (Sisipkan ke Subbab 3.4)

| No | Modul / Komponen | Pin Modul | Pin ESP32 | Mode / Tipe Sinyal | Catatan Teknis Rangkaian |
| :---: | :--- | :---: | :---: | :---: | :--- |
| 1 | **Sensor DS18B20** | VCC | 3.3V | Catu Daya | Jalur daya modul sensor waterproof. |
| 2 | | GND | GND | Ground | Ground bersama (*common ground*). |
| 3 | | DATA | **GPIO 4** | Digital Input (1-Wire) | **Wajib dipasang resistor pull-up 4.7 kΩ** ke VCC 3.3V. |
| 4 | **Sensor pH (SEN0161-V2)** | VCC | 3.3V / 5V | Catu Daya | Ditenagai 3.3V untuk keamanan rentang ADC ESP32. |
| 5 | | GND | GND | Ground | Ground bersama (*common ground*). |
| 6 | | AOUT | **GPIO 34** | Analog Input (ADC1) | **Wajib pada ADC1**. Jalur ADC2 dinonaktifkan saat Wi-Fi menyala. |
| 7 | **Catu Daya Sistem** | Micro-USB | VIN / VBUS | 5V DC (2 Ampere) | Adaptor eksternal stabil untuk operasional kontinu di kolam. |

---

### B. Algoritma Firmware ESP32 (Pseudocode Rule-Based & Blynk)

```text
ALGORITMA Monitoring_Kualitas_Air_ESP32:
DEKLARASI:
    pin_suhu   <- GPIO 4
    pin_ph     <- GPIO 34
    nilai_suhu <- 0.0 (Float)
    tegangan   <- 0.0 (Float)
    nilai_ph   <- 0.0 (Float)
    kategori   <- "" (String)
    tindakan   <- "" (String)

PROSEDUR Inisialisasi():
    Serial.begin(115200)
    Inisialisasi sensor DS18B20 pada pin_suhu
    Hubungkan Wi-Fi dan Blynk.begin(AUTH_TOKEN, SSID, PASSWORD)

PROSEDUR Baca_Sensor():
    nilai_suhu <- Request suhu dari DS18B20
    adc_mentah <- analogRead(pin_ph)
    tegangan   <- (adc_mentah / 4095.0) * 3.3
    nilai_ph   <- (slope_m * tegangan) + offset_c    // Hasil kalibrasi buffer

PROSEDUR Evaluasi_Rule_Based():
    // 9-Rule Matrix Inference
    JIKA (nilai_suhu < 25.0) MAKA:
        JIKA (nilai_ph < 6.5) MAKA:
            kategori <- "Bahaya"; tindakan <- "Air mematikan! Segera kuras/ganti air kolam!"
        LAIN JIKA (nilai_ph <= 8.5) MAKA:
            kategori <- "Waspada"; tindakan <- "Suhu dingin. Nyalakan heater kolam/kurangi aerasi."
        LAIN:
            kategori <- "Bahaya"; tindakan <- "Air mematikan! Segera kuras/ganti air kolam!"

    LAIN JIKA (nilai_suhu <= 30.0) MAKA:
        JIKA (nilai_ph < 6.5) MAKA:
            kategori <- "Waspada"; tindakan <- "Air asam. Berikan kapur dolomit/buffer pH naik."
        LAIN JIKA (nilai_ph <= 8.5) MAKA:
            kategori <- "Sangat Baik"; tindakan <- "Kondisi optimal. Pertahankan kualitas air kolam."
        LAIN:
            kategori <- "Waspada"; tindakan <- "Air basa. Tambahkan daun ketapang/buffer pH turun."

    LAIN: // Suhu > 30.0 (Panas)
        JIKA (nilai_ph < 6.5) MAKA:
            kategori <- "Bahaya"; tindakan <- "Air mematikan! Segera kuras/ganti air kolam!"
        LAIN JIKA (nilai_ph <= 8.5) MAKA:
            kategori <- "Waspada"; tindakan <- "Suhu panas. Tambahkan sirkulasi air/pasang peneduh."
        LAIN:
            kategori <- "Bahaya"; tindakan <- "Air mematikan! Segera kuras/ganti air kolam!"

PROSEDUR Kirim_Ke_Blynk():
    Blynk.virtualWrite(V0, nilai_suhu)
    Blynk.virtualWrite(V1, nilai_ph)
    Blynk.virtualWrite(V2, kategori)
    Blynk.virtualWrite(V3, tindakan)
    
    // Sistem Peringatan Dini (Early Warning System)
    JIKA (kategori == "Bahaya" ATAU kategori == "Waspada") MAKA:
        JIKA (interval_notifikasi_terpenuhi) MAKA:
            Blynk.logEvent("kondisi_kritis", "PERINGATAN: Status Kolam " + kategori + "! " + tindakan)

PROSES UTAMA (Looping Tiap 10 Detik):
    Blynk.run()
    Baca_Sensor()
    Evaluasi_Rule_Based()
    Kirim_Ke_Blynk()
```

---

### C. Tabel Jadwal Penelitian Tahun 2026 (Subbab 3.7)

| No | Tahapan & Uraian Kegiatan | Jan | Feb | Mar | Apr | Mei | Jun | Jul | Agu | Sep | Okt | Nov | Des |
|:---|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **I** | **Tahap Persiapan** | | | | | | | | | | | | |
| 1 | Studi Literatur & Observasi Kolam Nila | █ | █ | | | | | | | | | | |
| 2 | Penyusunan Proposal Skripsi | | █ | █ | | | | | | | | |
| 3 | **Seminar Proposal (Sempro)** | | | | █ | | | | | | | |
| 4 | Perbaikan Naskah Pasca-Sempro | | | | | █ | | | | | | |
| **II** | **Tahap Pelaksanaan & Rekayasa** | | | | | | | | | | | | |
| 5 | Pengadaan Komponen & Sensor | | | | | █ | | | | | | |
| 6 | Kalibrasi Sensor Suhu & pH (Buffer 4.01 & 6.86) | | | | | █ | █ | | | | | |
| 7 | Pengkodean Firmware ESP32 & Rule-Based | | | | | | █ | █ | | | | |
| 8 | Konfigurasi Platform Blynk Cloud & Push Notification | | | | | | | █ | █ | | | |
| 9 | Pengujian Lapangan pada Kolam Ikan Nila (MAPE & Latensi) | | | | | | | | █ | █ | | |
| **III**| **Tahap Evaluasi & Penyusunan Laporan** | | | | | | | | | | | | |
| 10 | Analisis Data Hasil Uji & Validasi Aturan | | | | | | | | | █ | █ | |
| 11 | Penyusunan Draf Skripsi Lengkap | | | | | | | | | | █ | █ |
| 12 | **Seminar Hasil & Sidang Pendadaran** | | | | | | | | | | | | █ |

---

## 🎯 5. Simulasi Pertanyaan Kritis Ujian Seminar Proposal (Kisi-Kisi Penguji)

Persiapkan diri Saudara dengan mempelajari argumentasi atas pertanyaan-pertanyaan yang hampir pasti diajukan oleh dosen penguji:

1. **Pertanyaan Penguji 1 (Metodologi & Representasi Pengetahuan):**
   > *"Mengapa Saudara memilih metode Rule-Based (Forward Chaining) dan bukan Logika Fuzzy (Mamdani/Sugeno) yang memiliki kurva keanggotaan derajat halus?"*  
   * **Panduan Jawaban:**  
     *"Berdasarkan kebutuhan pembudidaya ikan nila di lapangan, batas toleransi fisiologis ikan poikilotermik terhadap keasaman dan suhu memiliki ambang kritis yang tegas. Metode Rule-Based dipilih karena menghasilkan rekomendasi tindakan fisik yang pasti (deterministik) seperti 'tambah kapur' atau 'segera kuras air'. Selain itu, evaluasi 9 aturan Forward Chaining pada mikrokontroler ESP32 beroperasi sangat cepat tanpa beban defuzzifikasi integral yang memakan memori SRAM, sehingga sistem memiliki keandalan tinggi saat beroperasi kontinu 24 jam nonstop."*

2. **Pertanyaan Penguji 2 (Elektronika & Keandalan Sensor Lapangan):**
   > *"Elektroda kaca sensor pH sangat rentan mengalami pergeseran nilai (drift) akibat lumut, lendir bioflok, dan kotoran kolam. Bagaimana strategi Saudara menjamin akurasi sensor saat diterapkan di kolam nyata?"*  
   * **Panduan Jawaban:**  
     *"Dalam metodologi penelitian, saya menerapkan prosedur kalibrasi 2-titik menggunakan larutan buffer standar pH 4.01 dan pH 6.86/7.00 secara periodik, serta mencatat nilai Mean Absolute Percentage Error (MAPE). Selain itu, untuk pengujian kolam luar ruangan, probe sensor dilengkapi pelindung selubung fisik berpori agar elektroda kaca tidak tersentuh langsung oleh sedimen lumpur dasar kolam dan meminimalkan penempelan alga."*

3. **Pertanyaan Penguji 3 (Arsitektur Komputasi & Jaringan IoT):**
   > *"Di mana sebenarnya mesin inferensi rule-based dijalankan? Di cloud Blynk atau di dalam mikrokontroler ESP32? Dan bagaimana jika koneksi internet terputus?"*  
   * **Panduan Jawaban:**  
     *"Mesin inferensi Rule-Based dijalankan langsung di tingkat perangkat keras (Edge Computing) pada mikrokontroler ESP32 sebelum data dipaketkan. Dengan demikian, klasifikasi status kondisi air tetap berjalan secara lokal meskipun jaringan internet terputus. Blynk Cloud berfungsi sebagai perantara sinkronisasi tampilan Web Console, visualisasi mobile app, dan pemicu push notification."*

---

## ✅ 6. Lembar Periksa Mandiri (*Checklist*) Perbaikan Naskah

Sebelum naskah proposal diserahkan kembali kepada Dosen Pembimbing untuk persetujuan seminar, pastikan Saudara telah mencentang seluruh butir berikut:

- [ ] Hapus frasa `bu ros tercinta` dan `pak anton jago iot` pada Lembar Pengesahan.
- [ ] Ganti nama pembimbing I menjadi **Rosmasari, S.Kom., M.T.** dan pembimbing II **Anton Prafanto, S.Kom., M.T.**.
- [ ] Bersihkan teks panduan template Word pada Kata Pengantar, ganti `<Judul Skripsi>`, dan perbarui tahun 2026.
- [ ] Lakukan *Update Field* pada Microsoft Word untuk menghilangkan seluruh `Error! Bookmark not defined.` di Daftar Isi.
- [ ] Rapikan Daftar Tabel, Daftar Gambar, dan Daftar Singkatan (jangan tinggalkan teks `contents`).
- [ ] Sisipkan **Page Break** di Halaman 33 agar BAB III dimulai pada lembar halaman baru.
- [ ] Tambahkan **Tabel Matriks Perbedaan Penelitian (SOTA)** pada akhir Subbab 2.1 / Subbab 2.2.
- [ ] Hapus teks tautan blog mentah (`( artikel https://... )`), `SOCA JournalPtdsak`, dan `Politama` pada Bab II.
- [ ] Masukkan **Gambar Flowchart Sistem** (dari dokumen ringkasan) ke dalam Bab III Subbab 3.4.
- [ ] **Koreksi Tabel 3.4:** Pastikan kolom Suhu berisi suhu dan kolom pH berisi nilai pH (jangan terbalik), serta perbaiki typo `Wapada`.
- [ ] Putuskan arsitektur sistem secara konsisten: fokus pada platform Blynk dan hapus kontradiksi tabel database SQL kustom.
- [ ] Perbaiki gambar mockup Hal. 41: ganti angka Suhu 7°C menjadi realistis (28°C) dan gunakan mockup widget Blynk.
- [ ] Cantumkan tabel pemetaan pinout ESP32 (GPIO 4 DS18B20 + resistor 4.7kΩ, dan GPIO 34 pada ADC1 untuk sensor pH).
- [ ] Lengkapi Tabel Jadwal Penelitian 2026 (Januari s.d. Desember, hapus elipsis `…`, beri tanda blok arsir).
- [ ] 🚨 **PERBAIKI TOTAL DAFTAR PUSTAKA:** Hapus 5 referensi kelapa sawit & citra, masukkan 25–30 referensi IoT kualitas air ikan nila dengan Mendeley/Zotero.
- [ ] Hapus teks `Penjelasan lihat di ppt` pada Halaman 48 (Lampiran), ganti dengan skematik hardware atau lembar kalibrasi.
