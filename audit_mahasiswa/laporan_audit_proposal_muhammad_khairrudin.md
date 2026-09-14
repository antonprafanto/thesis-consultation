# 📋 LAPORAN AUDIT AKADEMIK FORENSIK & PANDUAN REVISI PROPOSAL SKRIPSI

**Mahasiswa Bimbingan:** Muhammad Khairrudin  
**NIM:** 2209106128  
**Program Studi:** S1 Informatika, Fakultas Teknik, Universitas Mulawarman  
**Dosen Pembimbing I:** Reza Wardhana, S.Kom., M.Eng.  
**Dosen Pembimbing II:** Anton Prafanto, S.Kom., M.T.  
**Judul Proposal:** *Rancang Bangun Sistem Monitoring Kualitas Air Sungai Mahakam Berbasis Internet of Things Menggunakan ESP32 dengan Metode Fuzzy Mamdani*  
**Tanggal Audit:** 14 September 2026  
**Status Naskah:** **Diterima dengan Catatan Revisi Komprehensif (Wajib Disinkronkan Sebelum Pendaftaran Seminar Proposal)**

---

## 🌟 1. Apresiasi & Catatan Positif Naskah

Secara substansi, proposal skripsi yang disusun oleh Saudara **Muhammad Khairrudin** memiliki konsep dan relevansi yang **sangat baik, kontekstual, dan aplikatif**:

1. **Urgensi Topik Sangat Kontekstual:** Pengujian kualitas air di Sungai Mahakam (kawasan PDAM Bakungan / Stasiun KLHK 167) sangat relevan dengan isu lingkungan hidup Kota Samarinda dan kebutuhan pemantauan berkelanjutan.
2. **Integrasi Regulasi Baku Mutu yang Cermat:** Pemanfaatan deviasi suhu $\Delta T = |T_{\text{air}} - T_{\text{udara}}|$ mengacu pada PP No. 22 Tahun 2021 merupakan langkah tepat untuk merepresentasikan fluktuasi iklim mikro lokal dibandingkan hanya mengukur suhu air mutlak.
3. **Perancangan Rangkaian Sebenarnya Sangat Maju:** Pemeriksaan terhadap diagram Fritzing (Gambar 3.2) menunjukkan bahwa mahasiswa sebenarnya telah memikirkan rangkaian perangkat keras yang sangat baik (menggunakan Buck Converter Step-Down LM2596, pembagi tegangan resistor, pull-up resistor OneWire, dan modul RTC/MicroSD), meskipun belum tertulis sinkron pada narasi teks dan tabel.
4. **Pemaparan Alur Perhitungan Fuzzy yang Runtut:** Simulasi numerik dari tahap fuzzifikasi hingga defuzzifikasi pada Bab 3 ditulis dengan jelas dan memudahkan pemahaman tahapan inferensi.

Catatan evaluasi di bawah ini disusun secara sangat teliti, santun, dan mendalam (*forensic audit*) untuk mendampingi Saudara menyempurnakan setiap detail teknis, formalia, dan logika naskah agar saat maju ke **Seminar Proposal (Sempro)** nanti, naskah ini kokoh, tidak memiliki celah sanggahan fatal, dan dapat Saudara pertanggungjawabkan dengan percaya diri di hadapan Dosen Penguji.

---

## 🚦 2. Matriks Status Kesiapan Naskah

| Komponen Naskah | Status | Catatan Evaluasi Utama |
| :--- | :---: | :--- |
| **Format & Kelengkapan Awal** | ⚠️ *Perlu Perapian* | Ganti placeholder `<TAHUN SEKARANG>`, `[tgl, bln, tahun]`, rapikan teks bertumpuk di Pengesahan, hapus duplikasi sisa template Kata Pengantar, isi Daftar Istilah/Singkatan, dan tertibkan penomoran romawi vs arab. |
| **Bab I: Pendahuluan** | ⚠️ *Revisi Ringan* | Sinkronkan kehadiran *Dashboard Web* pada Rumusan Masalah 3, Batasan Masalah 5, dan Tujuan 3; perjelas batasan operasional data sekunder ONLIMO dan fungsi *buzzer*. |
| **Bab II: Tinjauan Pustaka** | ⚠️ *Revisi Sedang* | Cantumkan identitas peneliti, tahun, dan judul pada 15 penelitian terkait; tambahkan **Tabel Matriks Perbedaan Penelitian (SOTA)**; luruskan terminologi rumus defuzzifikasi *Weighted Average*. |
| **Bab III: Rangkaian & Pinout** | 🚨 *Disinkronisasi Total* | **Diagram Fritzing (Gambar 3.2) bertentangan frontal dengan Tabel 3.2** (perbedaan nomor pin GPIO, level tegangan 5V vs 3V3, dan ketiadaan komponen Buck Converter di tabel kebutuhan perangkat keras). |
| **Bab III: Desain UI (OLED & Web)** | 🚨 *Revisi Desain* | **Gambar 3.5 (Mockup OLED 0.96") menampilkan layar tablet touchscreen resolusi tinggi**, bukan tampilan piksel monokrom 128x64 SSD1306; **terdapat 3 versi ambang batas output (Buruk/Sedang/Baik)** yang saling bertentangan antara Bab 2, Bab 3 teks, dan Gambar 3.6! |
| **Bab III: Logika Fuzzy & Rules** | 🚨 *Revisi Krusial* | **Koreksi fungsi keanggotaan segitiga batas ekstrem menjadi trapesium (*shoulder*)** untuk mencegah pembagian nol (*NaN / ESP32 crash*); koreksi kontradiksi antara kurva Gambar 3.4 vs Tabel 3.4; kaji ulang Aturan 12 & 21 (Asam/Basa + Keruh yang masih dilabeli "Sedang"). |
| **Bab III: Alur Flowchart (Gbr 3.3)** | ⚠️ *Revisi Alur* | Flowchart terputus 3 kolom tanpa konektor; salah ketik *"LCD (Hijau/Kuning/Merah)"* dan *"RTC DS2231"*; rumus mutlak $\Delta T$ tidak tertulis di flowchart; duplikasi simpan MicroSD. |
| **Daftar Pustaka & Sitasi** | ⚠️ *Revisi Sedang* | Lengkapi *ghost citations* (`Hasib & Akib, 2026` dan `Zimmermann, 2001`); bersihkan anomali parser Mendeley (afiliasi kampus terbaca nama pengarang); ubah format ke alfabetis tanpa nomor (APA 7th). |
| **Lampiran Naskah** | ⚠️ *Wajib Dihapus* | Hapus teks catatan pribadi `Penjelasan lihat di ppt` pada halaman 71; gantikan dengan lembar skematik rangkaian dan form kalibrasi. |

---

## 🔍 3. Rincian Catatan Audit Forensik & Panduan Perbaikan Bab per Bab

---

### 📄 A. Bagian Awal & Akhir Naskah (Formalia, Template & Penomoran)

1. **Pembersihan Sisa Placeholder Template:**
   * **Sampul & Halaman Judul (Hal. 1 & 2):** Di bawah nama kota Samarinda masih tertulis `<TAHUN SEKARANG>`. Ganti dengan tahun aktif: `2026`.
   * **Halaman Pengesahan (Hal. 3 / Romawi ii):**
     - Judul bertumpuk / terjadi tabrakan teks: `FUZZY MAMDANIAN PENGESAHAN` (kata `HALAMAN PENGESAHAN` tertempel pada kata `MAMDANI`). Rapikan spasi dan tata letaknya.
     - Tanggal rapat bimbingan masih bertuliskan `pada [tgl, bln, tahun]`.
     - Standarisasi penulisan gelar Pembimbing II: ganti `Anton Prafanto, S.Kom.,MT` menjadi `Anton Prafanto, S.Kom., M.T.` (beri spasi standar).
   * **Kata Pengantar (Hal. 4 / Romawi iii):**
     - Poin 4 sudah benar menyebut Dosen Pembimbing I (Reza Wardhana, S.Kom., M.Eng.) dan Pembimbing II (Anton Prafanto, S.Kom., M.T.).
     - Namun poin 5 masih memuat teks template Word: *`Nama dan gelar akademik Dosen Pembimbing II selaku Pembimbing II atas masukkan terhadap penelitian ini`* (duplikasi pembimbing!).
     - Poin 6 dan 7 juga masih berupa teks template penguji: *`Nama dan gelar akademik Dosen Penguji I...`* dan *`Penguji II...`*. Pada tahap proposal, nama penguji belum terbit dari prodi. Satukan menjadi: *"Segenap Dosen Penguji yang nantinya akan memberikan masukan berharga demi kesempurnaan penelitian ini"*.
     - Tanggal titimangsa masih berupa titik-titik dan tahun lama: `Samarinda,.............................. 2024`. Perbarui menjadi `Samarinda, .................... 2026`.

2. **Daftar Lampiran, Istilah, dan Singkatan (Hal. 8–11):**
   * Halaman 8 (Daftar Lampiran) tertulis teks acak: `Lampiran 1 contents 42`.
   * Halaman 9 (Daftar Istilah/Lambang) dan Halaman 10 (Daftar Singkatan) hanya bertuliskan `Arti Contents` (placeholder TOC Microsoft Word yang belum diisi).
   * **Solusi:** Karena naskah ini kaya akan istilah teknis elektro dan lingkungan, isi daftar tersebut:
     - **Singkatan:** ADC (*Analog to Digital Converter*), API (*Application Programming Interface*), ESP32 (*Espressif Systems 32-bit Microcontroller*), FIS (*Fuzzy Inference System*), I2C (*Inter-Integrated Circuit*), IoT (*Internet of Things*), KLHK (*Kementerian Lingkungan Hidup dan Kehutanan*), LED (*Light Emitting Diode*), NTP (*Network Time Protocol*), NTU (*Nephelometric Turbidity Unit*), OLED (*Organic Light-Emitting Diode*), ONLIMO (*Online Monitoring System*), RTC (*Real-Time Clock*), SPI (*Serial Peripheral Interface*), TSS (*Total Suspended Solids*).
     - **Istilah/Lambang:** $z^*$ (Nilai tegas hasil defuzzifikasi), $\mu(x)$ (Derajat keanggotaan himpunan fuzzy), $\alpha$ (Nilai kekuatan aturan / firing strength), $\Delta T$ (Selisih mutlak suhu air terhadap suhu udara lingkungan).

3. **Tertib Penomoran Halaman (*Pagination*):**
   * Saat ini halaman awal menggunakan angka Arab (`1, 2, 3, 4...`) dan kemudian pada Bab I ter-reset kembali mulai dari angka `3`.
   * **Sesuai Pedoman Skripsi FT UNMUL:**
     - Bagian Awal (Halaman Judul hingga Daftar Singkatan) wajib menggunakan **angka Romawi kecil** (`i, ii, iii, iv, v, vi, vii, viii, ix, x`) di posisi **tengah bawah**. (Halaman judul dihitung sebagai `i` tanpa dicetak).
     - Bab I Pendahuluan dimulai dari **angka Arab `1`** di tengah bawah. Halaman selanjutnya berada di pojok **kanan atas**, kecuali halaman awal bab baru yang kembali ke tengah bawah.

4. **🚨 Catatan Pribadi pada Halaman 71 (Lampiran):**
   * Pada halaman 71 tertulis kalimat: `Penjelasan lihat di ppt`.
   * Kalimat ini wajib **dihapus**. Ganti lembar lampiran dengan dokumen ilmiah pendukung:
     - Lampiran 1: Skematik Rangkaian Fritzing & Daftar Komponen (*Bill of Materials*).
     - Lampiran 2: Tabel Kalibrasi Sensor pH (Buffer 4.01, 6.86, 9.18) dan Turbiditas.
     - Lampiran 3: Ringkasan Lembar Data (*Datasheet*) Komponen Utama.

---

### 📘 B. BAB I – Pendahuluan

1. **Sinkronisasi Web Dashboard:**
   * Di Bab 3 Subbab 3.5.2 (hal. 53–54) dan Gambar 3.6, Saudara telah merancang **Dashboard Web** lengkap (kartu ringkasan metrik, grafik tren real-time, tabel riwayat, dsb.) dan mengujinya pada Tabel 3.7.
   * Namun di Bab 1, **Rumusan Masalah 3** dan **Tujuan Penelitian 3** sama sekali belum menyebut kata *Dashboard Web* (hanya menyebut tampilan OLED dan LED).
   * **Rekomendasi Redaksi Rumusan Masalah 3:**
     > *"3. Bagaimana merancang antarmuka pemantauan data kualitas air secara lokal melalui tampilan OLED dan indikator LED, serta secara jarak jauh (*remote monitoring*) melalui **Dashboard Web** yang terintegrasi dengan Firebase Realtime Database dan pencadangan lokal MicroSD?"*
   * Sesuaikan pula **Tujuan Penelitian butir 3** dan **Batasan Masalah butir 5** agar simetris.

2. **Perjelas Posisi Data Sekunder ONLIMO:**
   * Pada Batasan Masalah butir 2, tegaskan bahwa data dari Stasiun ONLIMO KLHK 167 murni dijadikan referensi validasi dan pembanding tren pada bab pembahasan hasil, bukan sebagai parameter input komputasi mikrokontroler.

---

### 📗 BAB II – Tinjauan Pustaka & Kajian Literatur

1. **Standarisasi 15 Penelitian Terkait (Subbab 2.1):**
   * Saat ini seluruh butir diawali dengan format: `1. Metode yang digunakan:...`, `2. Metode yang digunakan:...`, tanpa menyebutkan identitas peneliti, tahun terbit, judul, dan nama jurnal.
   * **Ubah menjadi gaya sitasi ilmiah formal:**
     > *"1. **Elriyan (2025)** dalam penelitiannya yang berjudul *'Pengendalian Kualitas Air Minum Menggunakan Fuzzy Mamdani Berbasis Internet of Things'* pada jurnal Electrician..."*  
     > *"2. **Kaho et al. (2025)** dalam artikel *'Sistem Pemantauan Kualitas Air Kolam Berbasis Internet of Things (IoT) Untuk Mengurangi Kematian Ikan Nila Menggunakan Logika Fuzzy Mamdani'*..."*

2. **Wajib Menambahkan Tabel Matriks Perbedaan Penelitian (*State-of-the-Art* / SOTA):**
   * Tambahkan tabel perbandingan di akhir Subbab 2.1 untuk memetakan *research gap*:

| No | Peneliti & Tahun | Objek / Kasus | Metode | Parameter Input | Platform / Output | Keterbatasan Riset Terdahulu | Posisi & Kebaruan Riset Ini |
|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | Elriyan (2025) | Air Minum | Mamdani | Suhu, TDS, pH, Kekeruhan | ESP32, Kodular | Sistem tertutup, tidak menghitung deviasi suhu udara. | Mengkaji badan air terbuka (Sungai Mahakam) dengan variabel $\Delta T$. |
| 2 | Kaho et al. (2025) | Kolam Nila | Mamdani | Suhu, pH, Kekeruhan | ESP32, Blynk | Batas parameter untuk ikan, bukan standar baku mutu sungai. | Mengacu standar PP No. 22/2021 & Permenkes No. 2/2023. |
| 3 | Ayu Wulandari et al. (2024) | Tambak Mujair | Mamdani | Suhu, pH, DO | ESP32, Android | Kekeruhan tidak diukur secara kuantitatif. | Mengombinasikan pH, kekeruhan, dan $\Delta T$. |
| 4 | Hermansyah (2022) | Sungai Kapuas | Mamdani & STORET | TSS, DO, BOD, COD | Analisis software PC | Pengolahan offline di komputer, tidak real-time IoT. | Komputasi mandiri pada mikrokontroler ESP32 (*edge computing*). |
| 5 | Faradilla et al. (2025) | Sungai Mahakam | Deskriptif | Fisika & Kimia | Stasiun ONLIMO KLHK | Update lambat (1 jam), data pH/suhu kerap kosong. | Interval 5 menit dengan klasifikasi linguistik otomatis. |
| **6** | **Khairrudin (2026)** | **Sungai Mahakam (PDAM)** | **Fuzzy Mamdani (Weighted Avg)** | **pH, $\Delta T$ (Suhu Air - Suhu Udara), Kekeruhan** | **ESP32, OLED, LED, Firebase, Web Dashboard, MicroSD** | - | **Purwarupa IoT berbiaya rendah dengan perhitungan fuzzy mandiri di ESP32, dual storage, dan web dashboard.** |

3. **Luruskan Terminologi Rumus Defuzzifikasi (Subbab 2.5.1 / Persamaan 2.4):**
   * Persamaan (2.4) yang Saudara tulis:
     $$z^* = \frac{\sum z_i \cdot \alpha_i}{\sum \alpha_i}$$
     disebut di naskah sebagai *"metode Centroid"*.
   * **Koreksi Teori:** Formula tersebut secara akademis adalah **Metode Rata-rata Terbobot (*Weighted Average / Discrete Height Centroid*)**, bukan integral *Center of Gravity (COG)* kontinu Mamdani.
   * Tetap pertahankan rumus ini, tetapi ubah narasinya: Jelaskan bahwa Saudara sengaja memilih metode *Weighted Average* karena efisiensi komputasi *floating point* dan penghematan memori SRAM pada ESP32 (*lightweight edge processing*).

---

### 📙 C. BAB III – Rangkaian, Pinout & Instrumentasi (Disinkronisasi Total)

#### 🚨 1. BENTURAN FRONTAL: Gambar Wiring Fritzing (Gambar 3.2) vs Tabel 3.2 vs Tabel 3.1
Setelah memeriksa berkas skematik Fritzing pada Gambar 3.2 secara detail, ditemukan bahwa **Gambar 3.2 dan teks naskah Saudara bertentangan hampir di setiap komponen**:

| Komponen / Parameter | Desain Riil pada Fritzing (Gambar 3.2) | Keterangan pada Teks / Tabel 3.2 | Evaluasi & Tindakan Perbaikan |
|:---|:---|:---|:---|
| **Pin Data Sensor pH** | Terhubung ke pin **VP / GPIO 36** | Tertulis pin **GPIO 34** | 🚨 **Tidak sinkron.** Samakan tabel mengikuti wiring riil Fritzing (atau sebaliknya). |
| **Pin Data Turbidity** | Terhubung ke pin **VN / GPIO 39** | Tertulis pin **GPIO 35** | 🚨 **Tidak sinkron.** Samakan tabel dan wiring. |
| **Pin Data Suhu Air (DS18B20)** | Terhubung ke pin **GPIO 27** | Tertulis pin **GPIO 4** | 🚨 **Tidak sinkron.** |
| **Pin Data Suhu Udara (DHT22)** | Terhubung ke pin **GPIO 14** | Tertulis pin **GPIO 5** | 🚨 Di Fritzing sudah benar di GPIO 14 karena GPIO 5 dipakai MicroSD CS. Namun di Tabel 3.2 masih salah tertulis GPIO 5! |
| **Catu Daya Sensor Analog (VCC)** | Mengambil jalur **5V dari Buck Converter** | Tertulis **3V3** di Tabel 3.2 | 🚨 Di gambar Fritzing Saudara sudah benar mencatu 5V ke modul analog! Tabel 3.2 salah fatal karena menulis 3V3. |
| **Rangkaian Pembagi Tegangan** | Terpasang resistor **10kΩ & 20kΩ** pada jalur analog | **Sama sekali tidak disinggung** di tabel & narasi | 🚨 Keberadaan resistor voltage divider di Fritzing sangat bagus untuk melindungi ADC ESP32. Wajib dijelaskan di naskah! |
| **Modul Step-Down (LM2596)** | Terpasang jelas di pojok kiri bawah | **Tidak tercantum** di Tabel 3.1 (Kebutuhan Hardware) | 🚨 Masukkan modul DC-DC Step-Down Buck Converter ke Tabel 3.1. |
| **Pinout LED Indikator** | Terhubung ke **GPIO 15 (Hijau), GPIO 2 (Kuning), GPIO 4 (Merah)** | **Hilang total** dari Tabel 3.2 | 🚨 Lengkapi Tabel 3.2 dengan pinout ketiga LED ini. |
| **Pinout OLED & RTC DS3231** | I2C Bus: **SDA di GPIO 21, SCL di GPIO 22** | **Hilang total** dari Tabel 3.2 | 🚨 Lengkapi Tabel 3.2 dengan jalur I2C. |
| **Pinout Modul MicroSD** | SPI Bus: **CS=5, SCK=18, MOSI=23, MISO=19** | **Hilang total** dari Tabel 3.2 | 🚨 Lengkapi Tabel 3.2 dengan konfigurasi SPI MicroSD. |
| **Buzzer** | **Tidak ada di gambar Fritzing** | Disebut di Batasan Masalah & Flowchart | 🚨 Jika memang memakai buzzer, pasang di Fritzing (misal GPIO 25/32). Jika tidak jadi, hapus kata buzzer dari naskah. |

* **💡 Solusi:** Selaraskan Tabel 3.2 di naskah 100% mengikuti rancangan Fritzing Saudara yang sebenarnya sudah sangat baik!

---

#### 🚨 2. ANOMALI DESAIN UI: Mockup OLED 0,96" (Gambar 3.5) vs Realitas Layar
* **Temuan pada Gambar 3.5:** Naskah memuat judul *"Keluaran Informasi OLED"*. Namun gambar yang ditampilkan adalah **mockup tablet widescreen berwarna dengan bingkai tablet, kamera depan, slider progress bar halus, dan font antialiased**.
* **Kritik Penguji:** Layar OLED 0,96 inci adalah modul **SSD1306 monokrom beresolusi 128 $\times$ 64 piksel**. Layar sekecil itu secara fisik tidak mungkin merender UI tablet modern!
* **Solusi Desain:** Ganti Gambar 3.5 dengan ilustrasi tampilan OLED 128x64 piksel berbasis teks baris:

```text
+--------------------------------+
|  MONITORING AIR MAHAKAM        |
|  pH   : 6.8    T_air: 28.4 C   |
|  Turb : 3.2NTU T_udr: 27.9 C   |
|  Delta: 0.5 C  Waktu: 15:30    |
|  STATUS AIR: [ BAIK ]          |
+--------------------------------+
```

---

#### 🚨 3. INKONSISTENSI 3 VERSI AMBANG BATAS OUTPUT (BURUK, SEDANG, BAIK)
Dalam naskah Saudara saat ini, ditemukan **tiga versi rentang nilai $z^*$ yang saling bertentangan**:
1. **Versi 1 (Bab II, hal. 41):** Buruk (0–50), Sedang (25–75), Baik (50–100).
2. **Versi 2 (Bab III Teks, hal. 64):** Buruk (0–33), Sedang (34–66), Baik (67–100) *(disebut konsisten dengan Bab II, padahal angkanya berbeda!)*.
3. **Versi 3 (Gambar 3.6 Mockup Dashboard Web):** Buruk (0–50), Sedang (50–75), Baik (75–100).
* **Solusi Wajib:** Sepakati satu acuan baku yang konsisten di seluruh naskah dan program ESP32/Web:
  - Disarankan menggunakan partisi tegas tiga zona seimbang:
    $$\textbf{Buruk: } 0 \le z^* < 33.33, \quad \textbf{Sedang: } 33.33 \le z^* < 66.67, \quad \textbf{Baik: } 66.67 \le z^* \le 100$$
  - Sesuaikan narasi Bab 2, Bab 3 teks, dan label pada Gambar 3.6 agar selaras!

---

#### 🚨 4. PERBAIKAN MODEL MATEMATIKA FUZZY & BASIS ATURAN

1. **Kontradiksi Gambar 3.4 (Grafik pH) vs Tabel 3.4 & Contoh Perhitungan:**
   - Pada grafik Gambar 3.4, kurva Asam sudah digambar berbentuk trapesium bahu kiri yang turun dari 5 ke 6 (pada pH 6 nilainya sudah 0).
   - Tetapi pada tabel di bawah grafik dan di naskah (Tabel 3.4), tertulis: Asam $(0, 6, 7)$.
   - Pada contoh hitungan (hal. 50), Saudara menghitung: pada $pH = 6.2$, $\mu_{\text{asam}}(6.2) = 0.8$. Jika mengacu grafik Gambar 3.4, pada $pH = 6.2$ harusnya Asam $= 0$!
   - Samakan tabel dan teks mengikuti bentuk **Trapesium Bahu Kiri** yang benar: jika $pH \le 6.0$, $\mu_{\text{Asam}} = 1.0$; transisi turun dari 6.0 ke 7.0 (di mana pada 7.0 bernilai 0).
   - Lengkapi pula grafik visual untuk fungsi keanggotaan $\Delta T$, Kekeruhan, dan Output (saat ini hanya pH yang memiliki grafik).

2. **Kelemahan Logika pada Basis Aturan (Tabel 3.5):**
   - **Perhatikan Aturan 12:** JIKA pH Asam DAN $\Delta T$ Rendah DAN Kekeruhan Keruh MAKA Status = **Sedang**!
   - **Perhatikan Aturan 21:** JIKA pH Basa DAN $\Delta T$ Rendah DAN Kekeruhan Keruh MAKA Status = **Sedang**!
   - **Kritik Ilmiah:** Jika air sungai sudah terbukti **Asam/Basa (melanggar baku mutu pH)** dan sekaligus **Keruh pekat (melanggar baku mutu kejernihan)**, bagaimana mungkin statusnya masih dinilai **Sedang** hanya karena suhunya normal? Air yang asam dan berlumpur jelas tidak layak pakai dan berstatus **Buruk**.
   - **Rekomendasi Revisi Aturan 12 & 21:** Ubah konsekuen statusnya menjadi **Buruk**!
     - *Aturan 12:* IF pH Asam AND $\Delta T$ Rendah AND Kekeruhan Keruh THEN Status = **Buruk**.
     - *Aturan 21:* IF pH Basa AND $\Delta T$ Rendah AND Kekeruhan Keruh THEN Status = **Buruk**.

---

#### ⚠️ 5. PERBAIKAN ALUR FLOWCHART SISTEM (GAMBAR 3.3)
Pada Gambar 3.3, perhatikan koreksi berikut:
1. **Panah Terputus:** Aliran dari kotak *"Hitung $\Delta T$"* di kolom kiri berhenti begitu saja. Tambahkan simbol penghubung (*connector*) yang mengalirkan data ke *"Proses Fuzzy Mamdani"* di kolom kanan, lalu hasil inferensi dialirkan ke *"Proses Penyimpanan & Komunikasi"* di kolom tengah.
2. **Koreksi Typo Label:**
   - Di kotak kanan bawah tertulis: *"LCD (Hijau/Kuning/Merah)"*. Ganti menjadi **LED (Hijau/Kuning/Merah)**.
   - Di kotak pengambilan waktu tertulis: *"RTC DS2231"*. Ganti menjadi **RTC DS3231**.
3. **Koreksi Rumus $\Delta T$:** Di kotak proses tertulis $\Delta T = T\text{\_air} - T\text{\_udara}$. Berikan tanda mutlak: $\Delta T = |T_{\text{air}} - T_{\text{udara}}|$ agar selaras dengan Persamaan 3.1.
4. **Alur Simpan MicroSD:** Pada kolom tengah, hapus redundancy percabangan (cukup sekali proses simpan ke MicroSD baik pengiriman Firebase berhasil maupun gagal).

---

#### 🔋 6. MANAJEMEN DAYA & KONEKTIVITAS LAPANGAN (SARAN PENGUJI)
Ketika purwarupa diuji di tepi Sungai Mahakam (PDAM Bakungan / Stasiun KLHK 167), dosen penguji pasti akan menanyakan aspek operasional lapangan:
1. **Sumber Catu Daya:** Jelaskan di Subbab 3.4.1 apakah alat dicolok ke sumber listrik 220V pos PDAM melalui adaptor 12V/2A, atau menggunakan baterai/power bank.
2. **Kebutuhan Daya & Deep Sleep:** Jika alat beroperasi menggunakan baterai dengan interval 5 menit, sarankan penerapan fitur **ESP32 Deep Sleep** (ESP32 tidur selama 4 menit 50 detik dan hanya bangun selama 10 detik untuk membaca sensor dan mengirim data). Ini akan memperpanjang daya tahan baterai dari yang semula hanya 15–20 jam menjadi berhari-hari.
3. **Penyedia Jaringan Internet:** Sebutkan apakah koneksi WiFi diperoleh dari modem 4G MiFi portabel atau tethering smartphone yang standby di pos pemantauan.

---

### 📚 D. Daftar Pustaka & Sitasi Ilmiah

1. **Lengkapi Sitasi Hantu (*Ghost Citations*):**
   * Tambahkan referensi **`(Hasib & Akib, 2026)`** yang dikutip di halaman 42 & 43 mengenai transmisi Firebase.
   * Tambahkan referensi buku **`(Zimmermann, 2001)`** yang dikutip di halaman 39:  
     *Zimmermann, H.-J. (2001). Fuzzy Set Theory—and Its Applications (4th ed.). Springer Science & Business Media.*
2. **Bersihkan Kerusakan Metadata Mendeley:**
   * **Entri 4 (Ayu Wulandari et al., 2024):** Hapus teks afiliasi kampus yang keliru terimpor sebagai nama pengarang (*Studi Teknik Informatika, P.*, *Pertanian Negeri Jember, P.*, *Korespondesi, P.*).
   * **Entri 30 (Zadeh, 1965):** Hapus nama pengarang anomali *Introduction, I.* dan *Navy, U. S.*, cukup tulis: *Zadeh, L. A. (1965). Fuzzy sets. Information and Control, 8(3), 338–353.*
   * **Entri 1 (Affandi et al., 2026):** Lengkapi nomor volume/isu jurnal yang masih bertuliskan `XX, No. XX(02)`.
   * **Entri 3 (Aristho umbu nggaba kaho):** Rapikan kapitalisasi nama penulis (*Title Case*): *Kaho, A. U. N., Pekuwali, A. A., & Ratu, L. M. D. (2025)...*
3. **Format APA Edisi ke-7:** Susun seluruh daftar pustaka berurutan secara alfabetis tanpa penomoran angka Arab (1, 2, 3...).

---

## 🎯 4. Prediksi Pertanyaan Kritis Seminar Proposal & Strategi Jawaban

| No | Prediksi Pertanyaan Penguji Sempro | Rekomendasi Jawaban Ilmiah & Taktis Mahasiswa |
|:---|:---|:---|
| 1 | *"Mengapa Saudara memilih Fuzzy Mamdani dan bukan Sugeno atau Tsukamoto?"* | *"Karakteristik evaluasi kualitas air menghendaki hasil keputusan dengan batas semantik linguistik yang intuitif (Baik, Sedang, Buruk) dengan fungsi keanggotaan output yang merepresentasikan rentang kondisi alamiah. Mamdani sangat sesuai untuk sistem penalaran berbasis keahlian pakar (*expert reasoning*), dan terbukti pada riset terdahulu menghasilkan klasifikasi kategori lingkungan yang lebih stabil."* |
| 2 | *"Pada defuzzifikasi, mengapa menggunakan formula Rata-rata Terbobot (*Weighted Average*) dan bukan integral Centroid murni?"* | *"Perhitungan defuzzifikasi dijalankan secara mandiri pada mikrokontroler ESP32 (*edge computing*). Metode Rata-rata Terbobot terhadap titik pusat himpunan output dipilih untuk meminimalkan beban komputasi floating-point dan konsumsi memori SRAM, sehingga inferensi selesai seketika (*near zero-latency*) tanpa memicu watchdog timer reset, dengan tetap menjaga akurasi pemetaan kategori mutu air."* |
| 3 | *"Mengapa Aturan 12 dan 21 menetapkan status Buruk jika air Asam dan Keruh?"* | *"Karena baku mutu lingkungan hidup memandang derajat keasaman (pH) dan kekeruhan sebagai parameter pembatas kritis. Ketika dua dari tiga parameter fisik telah melanggar baku mutu kelas II secara bersamaan, air tidak lagi aman dimanfaatkan sehingga sistem secara konservatif menetapkan status Buruk demi keselamatan publik."* |
| 4 | *"Bagaimana rangkaian Saudara melindungi ADC ESP32 dari tegangan sensor analog 5V?"* | *"Modul sensor pH dan Turbidity dicatu daya 5V dari regulator Step-Down LM2596 agar rangkaian op-amp bekerja linier. Untuk melindungi pin ADC ESP32 yang memiliki batas tegangan maksimum 3.3V, jalur keluaran sinyal analog dilengkapi rangkaian pembagi tegangan (*voltage divider*) menggunakan kombinasi resistor sehingga tegangan input ADC selalu berada di bawah 3.0V."* |
| 5 | *"Mengapa sistem membutuhkan MicroSD jika sudah ada Firebase?"* | *"Pencadangan ganda (*dual storage*) dirancang karena lokasi pemantauan tepi sungai rentan fluktuasi sinyal internet. Saat koneksi terputus, ESP32 otomatis beralih ke Mode Offline dan menyimpan seluruh data mentah beserta timestamp RTC ke MicroSD, sehingga mencegah kehilangan data pemantauan historis (*data loss prevention*)."* |

---

## ✅ 5. Lembar Periksa (*Checklist*) Final Pra-Pendaftaran Sempro

- [ ] Placeholder `<TAHUN SEKARANG>` di cover & hal 1 sudah diganti `2026`.
- [ ] Teks tabrakan `FUZZY MAMDANIAN PENGESAHAN` sudah dirapikan dan gelar Pembimbing II tertulis `Anton Prafanto, S.Kom., M.T.`.
- [ ] Kata Pengantar bersih dari duplikasi pembimbing/penguji template Word, dan tahun aktif `2026`.
- [ ] Daftar Istilah dan Daftar Singkatan (hal. 9–10) sudah diisi lengkap, menggantikan teks `Arti Contents`.
- [ ] Penomoran halaman terbagi benar: Angka Romawi kecil (`i–x`) di tengah bawah dan Angka Arab (`1–60+`) mulai dari Bab I.
- [ ] Rumusan Masalah 3, Batasan Masalah 5, dan Tujuan 3 sudah mencantumkan **Dashboard Web**.
- [ ] Subbab 2.1 dilengkapi identitas penulis/tahun/judul pada 15 riset terkait dan dilengkapi **Tabel Matriks SOTA**.
- [ ] **Tabel 3.2 disinkronkan 100% dengan Gambar Wiring Fritzing (Gambar 3.2)** (nomor pin GPIO, catu 5V, voltage divider, LED, I2C OLED/RTC, SPI MicroSD).
- [ ] **Modul Buck Converter Step-Down LM2596** telah dimasukkan ke Tabel 3.1 Kebutuhan Hardware.
- [ ] **Gambar 3.5 diganti dengan mockup layar OLED monokrom 128x64**, bukan gambar tablet.
- [ ] **Ambang batas status mutu air (Buruk, Sedang, Baik) diseragamkan menjadi 1 versi baku** di Bab 2, Bab 3, dan Gambar 3.6.
- [ ] **Aturan 12 & 21 pada Tabel 3.5 diperbaiki menjadi status Buruk**.
- [ ] Gambar 3.4 kurva pH diselaraskan dengan Tabel 3.4 dan dilengkapi grafik untuk $\Delta T$, Kekeruhan, dan Output.
- [ ] Flowchart Gambar 3.3 diperbaiki garis konektornya, diperbaiki typo *"LCD"* dan *"DS2231"*, serta rumus mutlak $\Delta T$ dilengkapi.
- [ ] Halaman 71 yang bertuliskan `Penjelasan lihat di ppt` dihapus dan diganti lampiran skematik/datasheet resmi.
- [ ] Daftar Pustaka bersih dari *ghost citations* (`Hasib & Akib, 2026` dan `Zimmermann, 2001`) serta anomali metadata Mendeley telah dirapikan ke format APA edisi ke-7 tanpa nomor.

---
*Laporan audit forensik komprehensif ini disusun oleh Tim Pembimbing Skripsi untuk menjamin mutu akademik dan kesiapan teknis purwarupa Muhammad Khairrudin (NIM: 2209106128) menjelang Seminar Proposal S1 Informatika FT UNMUL.*
