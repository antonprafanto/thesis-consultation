# 📋 LAPORAN AUDIT AKADEMIK FORENSIK & PANDUAN REVISI TOTAL PROPOSAL SKRIPSI

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
**Status Naskah:** **REVISI MAYOR MENYELURUH (Formalia Template, Konsistensi Parameter, Arsitektur Platform, Elektronika ESP32 & Perombakan Total Daftar Pustaka Sebelum Dijadwalkan Seminar Proposal)**

---

## 🌟 1. Apresiasi & Potensi Positif Penelitian

Secara substansi dan ide dasar, penelitian yang diusulkan oleh Saudara **Abdullah Arkananta Rasendrya Hasan** memiliki nilai guna terapan yang **sangat baik, kontekstual, dan relevan** bagi masyarakat pembudidaya:

1. **Urgensi Lapangan Nyata:** Budidaya ikan nila (*Oreochromis niloticus*) di kolam air tawar sangat rentan terhadap kematian mendadak akibat pergeseran ekstrem derajat keasaman (asidosis/alkalosis) dan stres poikilotermik temperatur.
2. **Matriks 9 Aturan (*9-Rule Matrix*) Sangat Operasional:** Pada berkas *RINGKASAN RANCANGAN SISTEM MONITORING KUALITAS AIR.pdf*, pemetaan 3 kondisi suhu $\times$ 3 kondisi pH menghasilkan 3 status mutu air (*Sangat Baik, Waspada, Bahaya*) yang disertai panduan aksi nyata bagi petani (pengapuran dolomit, pemberian daun ketapang, pemanas kolam, peneduh, atau pengurasan darurat).
3. **Pemanfaatan Ekosistem IoT Hemat Daya & Biaya:** Kombinasi ESP32 dan platform Blynk IoT menyediakan antarmuka ganda (Web Console & Mobile App) dengan fitur *Blynk Events (Push Notification)* yang sangat cocok untuk sistem peringatan dini (*Early Warning System*) tanpa memerlukan infrastruktur server lokal yang mahal.

---

## 🚨 2. Rangkuman 15 Temuan Forensik (*Critical Red Flags*)

Audit mendalam terhadap naskah 48 halaman dan ringkasan 4 halaman mengungkap **15 kelemahan kritis** yang wajib diperbaiki sebelum berkas dapat disetujui untuk maju Seminar Proposal:

| No | Kategori | Tingkat Urgensi | Deskripsi Temuan Kritis |
| :---: | :--- | :---: | :--- |
| **1** | **Etika & Lembar Pengesahan** | 🚨 **Fatal** | Menuliskan teks informal pembimbing: `bu ros tercinta` dan `pak anton jago iot` pada Hal. 3, serta tanggal `[tgl, bln, tahun]`. |
| **2** | **Daftar Pustaka Palsu** | 🚨 **Fatal (Red Alert)** | Di naskah Bab I–III mengutip **>25 paper IoT kualitas air kolam**, namun di Daftar Pustaka (Hal. 46) hanya ada **5 referensi kelapa sawit & pengolahan citra** bawaan template Word! |
| **3** | **Sisa Template Word Fakultas** | 🚨 **Fatal** | Kata Pengantar (Hal. 4) memuat teks petunjuk teknis buku pedoman skripsi, judul masih `<Judul Skripsi>`, dan titimangsa masih tahun `2024`. |
| **4** | **Kerusakan TOC & Bookmark** | 🚨 **Fatal** | Daftar Isi (Hal. 5) dipenuhi `Error! Bookmark not defined.`; Daftar Tabel, Gambar, Singkatan (Hal. 6–10) hanya memuat kata `contents` kosong. |
| **5** | **Transisi Bab II ke Bab III** | 🚨 **Fatal** | **Hal. 33 tidak memiliki Page Break**; judul Bab III langsung menempel di bawah rumus Bab II pada halaman yang sama. |
| **6** | **Tabel 3.4 Tertukar & Typo** | 🚨 **Fatal** | Kolom pH diisi Suhu (`Dingin <25`), kolom Suhu diisi pH (`Asam <6.5`), dan baris R8 tertulis typo `Wapada` (Hal. 38). |
| **7** | **Jejak Draf "Hanya pH"** | ⚠️ **Mayor** | Subbab 2.12.3, Subbab 3.1, Tabel 3.1, Subbab 3.2, Subbab 3.3, Tabel 3.4, Subbab 3.5, dan Mockup Hal. 41 masih tertulis *"monitoring pH"* saja (parameter Suhu tertinggal). |
| **8** | **Kontradiksi Arsitektur Sistem** | 🚨 **Mayor** | Bab I menyebut platform Blynk PaaS, namun Bab II & III membahas koding website kustom (HTML/CSS/JS/Bootstrap/AJAX), backend REST API, dan tabel database SQL MySQL. |
| **9** | **Anomali Mockup Hal. 41** | ⚠️ **Mayor** | Kartu menampilkan `Suhu Air: 7` (suhu 7°C mematikan bagi ikan nila!), judul hanya menyebut pH, dan layout berupa wireframe web biasa bukan Blynk Console. |
| **10** | **Ketiadaan Flowchart di Naskah** | ⚠️ **Mayor** | Flowchart sistem yang sangat bagus di berkas Ringkasan **belum dimasukkan** ke naskah utama Bab III (di naskah hanya ada tahapan riset kotak oranye). |
| **11** | **Elektronika & ADC ESP32** | 🚨 **Krusial** | Belum ada skematik wiring; tidak menyebut resistor pull-up 4.7 kΩ untuk DS18B20; sensor pH wajib di pin **ADC1 (GPIO 34)** karena ADC2 nonaktif saat Wi-Fi menyala. |
| **12** | **Ketiadaan Rumus Kalibrasi** | ⚠️ **Mayor** | Tidak ada rumus transfer function ADC ke pH ($V = \frac{\text{ADC}}{4095}\times 3.3$, $\text{pH} = mV + c$) dan prosedur kalibrasi buffer pH 4.01 & 6.86. |
| **13** | **Inkonsistensi Kategori pH** | ⚠️ **Sedang** | Bab II (Tabel 2.x) membagi pH menjadi 5 kategori, tetapi di Bab III dipangkas menjadi 3 kategori tanpa memberikan penjelasan/justifikasi ilmiah. |
| **14** | **Jadwal Penelitian Cacat** | ⚠️ **Sedang** | Tabel 3.x memuat bulan `Jan Agu sept okt nov des` (bulan Feb–Jul hilang total), masih ada elipsis template (`…`), dan tabel belum diarsir. |
| **15** | **Lokasi Penelitian Mengambang** | ⚠️ **Sedang** | Subbab 3.7 hanya menulis *"dilakukan pada kolam ikan air tawar yang menjadi objek pengujian"* tanpa menyebut alamat, pemilik, jenis kolam, maupun ukurannya. |

---

## 🔍 3. Rincian Temuan & Panduan Perbaikan Langkah demi Langkah

---

### 📄 A. Formalia Bagian Awal (Cover s.d. Daftar Singkatan)

#### 1. Lembar Pengesahan (Halaman 3)
* **Koreksi Teks Informal:** Ganti teks candaan mahasiswa menjadi format resmi:
  * Pembimbing I: **Rosmasari, S.Kom., M.T.** (NIP 19800720 200501 2 001)
  * Pembimbing II: **Anton Prafanto, S.Kom., M.T.** (NIP 19931022 201903 1 016)
  * Koordinator Program Studi: **Awang Harsa Kridalaksana, S.Kom., M.Kom.** (NIP 19731229 200501 1 002)
  * Ganti `[tgl, bln, tahun]` dengan garis titik-titik rapi: `Samarinda, .................... 2026`.

#### 2. Kata Pengantar (Halaman 4)
* Hapus paragraf pertama yang merupakan instruksi buku pedoman: *"Kata Pengantar (preface, foreword) sebaiknya disusun secara ringkas dan tidak lebih dari 2 halaman..."*.
* Ganti teks placeholder `“<Judul Skripsi>”` dengan judul lengkap proposal.
* Ganti daftar ucapan terima kasih template (`Nama dan gelar akademik lengkap Dekan...`, `Nama dan gelar Koordinator Prodi...`, dll.) dengan nama pejabat yang menjabat saat ini.
* Perbarui titimangsa tahun menjadi `2026`.

#### 3. Daftar Isi, Tabel, Gambar, Lampiran, Istilah & Singkatan (Halaman 5–10)
* **Daftar Isi:** Atur setiap judul Bab dengan *Heading 1*, Subbab *Heading 2*, Anak Subbab *Heading 3*, lalu lakukan *Update Field -> Update Entire Table* pada Microsoft Word untuk melenyapkan seluruh `Error! Bookmark not defined.`.
* **Daftar Tabel & Gambar:** Hapus teks instruksi `WAJIB menggunakan alat bantu TOC...` dan perbarui daftar agar menunjuk nomor tabel dan gambar yang benar di dalam naskah.
* **Daftar Istilah & Singkatan:** Isi secara konkret dengan istilah teknis naskah: *ADC, API, BNC, DS18B20, ESP32, IoT, MAPE, PaaS, pH, REST, RSSI, SNI*.

#### 4. Penomoran Halaman (*Pagination*)
* Bagian Awal (Halaman Judul s.d. Daftar Singkatan) wajib menggunakan **angka Romawi kecil (`i, ii, iii, ...`)** di posisi tengah bawah.
* Halaman Isi (Bab I Pendahuluan s.d. Lampiran) wajib menggunakan **angka Arab (`1, 2, 3, ...`)** secara berkesinambungan tanpa ter-reset di tengah bab.

---

### 📘 B. BAB I – Pendahuluan

#### 1. Sinkronisasi Parameter Ganda (pH dan Suhu)
* Pada beberapa bagian Latar Belakang dan Rumusan Masalah, mahasiswa masih menyebut *"monitoring pH air kolam"* saja. Pastikan di seluruh kalimat dinyatakan secara tegas: **monitoring derajat keasaman (pH) dan suhu air**.

#### 2. Penegasan Platform pada Batasan Masalah (Subbab 1.3)
* Perjelas pada butir 4:
  > *"Visualisasi data dan antarmuka pemantauan jarak jauh dibangun menggunakan platform **Blynk IoT**, yang mencakup **Blynk Web Console** (akses peramban komputer untuk analisis data historis dan tabel log) serta **Blynk Mobile App** (aplikasi ponsel pintar dengan widget interaktif dan sistem notifikasi darurat Push Notification via Blynk Events)."*

#### 3. Dasar Baku Mutu Ilmiah (SNI Ikan Nila)
* Di latar belakang, tambahkan rujukan baku mutu nasional budidaya ikan nila: **Standar Nasional Indonesia SNI 7550:2009** (*Produksi Benih Ikan Nila Hitam Kelas Benih Sebar*), yang menetapkan suhu optimal budidaya pada kisaran $25^\circ\text{C} - 32^\circ\text{C}$ dan pH optimal pada rentang $6.5 - 8.5$. Hal ini memberikan landasan hukum dan saintifik yang tak terbantahkan bagi penguji.

---

### 📗 BAB II – Tinjauan Pustaka & Landasan Teori

#### 1. Perapian Narasi 8 Penelitian Terkait (Subbab 2.1)
* Awali setiap butir tinjauan pustaka dengan identitas peneliti, tahun, dan judul paper:
  * *Manurung et al. (2022)* mengenai sistem monitoring kolam lele.
  * *Subianto & Wardhana (2024)* mengenai sistem rekomendasi kualitas air nila berbasis Rule-Based offline.
  * *Maulana et al. (2021)* mengenai fuzzy logic air lele via Telegram.
  * *Camelia et al. (2026)* mengenai monitoring suhu dan pH kolam nila bioflok berbasis ESP32 dan Blynk.

#### 2. Tambahkan Tabel Matriks State-of-the-Art (SOTA)
* Sisipkan tabel perbandingan komprehensif pada akhir Subbab 2.1/2.2:

| No | Peneliti & Tahun | Objek Kolam | Parameter Input | Perangkat Keras | Logika Pengambil Keputusan | Media Antarmuka | Celah Riset / Limitasi | Posisi Penelitian Ini |
|:---|:---|:---|:---|:---|:---|:---|:---|:---|
| 1 | Manurung et al. (2022) | Ikan Lele | Suhu & pH | NodeMCU ESP8266 | Threshold Biner Sederhana | Blynk Mobile | Pasif; tidak ada rekomendasi aksi lapangan. | Menerapkan Rule-Based 9 Matriks dengan rekomendasi tindakan spesifik. |
| 2 | Subianto & Wardhana (2024) | Ikan Nila | Suhu, pH, TDS, Turbidity | Arduino Uno | Rule-Based Reasoning | Serial Monitor / Offline | Tidak ada konektivitas IoT jarak jauh dan notifikasi. | Terintegrasi penuh ke Cloud Blynk & Push Notification ke smartphone. |
| 3 | Maulana et al. (2021) | Ikan Lele | Suhu & pH | NodeMCU ESP8266 | Logika Fuzzy Mamdani | Telegram Bot | Komputasi fuzzy berat; notifikasi hanya teks chat biasa. | Inferensi Rule-Based deterministik cepat langsung di ESP32 dengan widget gauge. |
| 4 | Camelia et al. (2026) | Ikan Nila Bioflok | Suhu & pH | ESP32 | Monitoring Pasif (Tanpa Inferensi) | Blynk App | Merekomendasikan perlunya sistem inferensi otomatis. | **Menjawab rekomendasi Camelia et al.** dengan menambahkan mesin inferensi 9 aturan & early warning. |
| **5** | **Penelitian Ini (Hasan, 2026)** | **Ikan Nila Air Tawar** | **Suhu Air (DS18B20) & pH (SEN0161-V2)** | **ESP32 (30 Pin, Wi-Fi)** | **Rule-Based Forward Chaining (9 Aturan)** | **Blynk Web Console & Blynk Mobile App** | - | **Sistem pemantauan cerdas dengan komputasi edge di ESP32, visualisasi ganda, early warning notification, dan panduan mitigasi kolam.** |

#### 3. Pembersihan Jejak Copas Mentah & Anomali
* **Hal. 19:** Hapus duplikasi tanda kurung sitasi kembar yang berjejeran:
  `...secara real-time (Camelia et al., 2026; ...) (Manurung et al., 2022; ...)`
* **Hal. 25:** Hapus tautan URL mentah dan nama jurnal yang menempel di tengah kalimat:
  * Hapus: `( artikel https://www.ptdsak.com/blog/apa-itu-sensor-ph-fungsi-dan-aplikasinya-di-industri )`
  * Hapus: `SOCA JournalPtdsak`
* **Hal. 26:** Hapus kata terpotong di akhir paragraf: `Politama`.
* **Hal. 29 & 37:** Perbaiki kode sensor: ganti `DFRobot SEN0161-V12` menjadi **DFRobot SEN0161-V2**.
* **Hal. 21–22 vs Bab III:** Berikan penjelasan ilmiah mengapa pembagian 5 kategori pH pada Tabel 2.x disederhanakan menjadi 3 kategori (*Asam, Ideal, Basa*) pada matriks inferensi Bab III.

#### 4. Perapian Rumus MAPE & Penomoran Persamaan (Hal. 33)
* Pada halaman 33, rumus MAPE tertulis dua kali di baris yang sama. Perbaiki penulisan rumus menjadi satu persamaan baku:
  $$\text{MAPE} = \frac{1}{n} \sum_{i=1}^{n} \left| \frac{X_{t,i} - X_{r,i}}{X_{r,i}} \right| \times 100\% \quad (2.1)$$
* Ubah nomor persamaan dari (2.2) menjadi **(2.1)** karena ini adalah persamaan pertama dalam Bab II.

---

### 📙 C. BAB III – Metodologi Penelitian & Desain Sistem

#### 1. Wajib Memberikan Page Break pada Halaman 33
* Sisipkan **Page Break (Ctrl + Enter)** sebelum judul **BAB III METODOLOGI PENELITIAN** agar tidak menempel di bawah Gambar 2.1.

#### 2. Koreksi Fatal Tabel 3.4 (Kolom Tertukar & Typo)
* Pada Halaman 38, perbaiki posisi kolom pH dan Suhu yang terbalik serta perbaiki typo `Wapada`:

| Rule | Kondisi Suhu Air (°C) | Kondisi Derajat Keasaman (pH) | Kategori Status Mutu | Rekomendasi Tindakan / Aksi Sistem |
| :---: | :---: | :---: | :---: | :--- |
| **R1** | Dingin ($< 25^\circ\text{C}$) | Asam ($< 6.5$) | **Bahaya** | Air mematikan bagi ikan nila. Segera kuras dan ganti air kolam! |
| **R2** | Dingin ($< 25^\circ\text{C}$) | Ideal ($6.5 - 8.5$) | **Waspada** | Suhu air terlalu rendah. Nyalakan heater kolam/kurangi aerasi malam. |
| **R3** | Dingin ($< 25^\circ\text{C}$) | Basa ($> 8.5$) | **Bahaya** | Air mematikan bagi ikan nila. Segera kuras dan ganti air kolam! |
| **R4** | Ideal ($25^\circ\text{C} - 30^\circ\text{C}$) | Asam ($< 6.5$) | **Waspada** | Air terlalu asam. Berikan kapur pertanian/dolomit secara bertahap. |
| **R5** | Ideal ($25^\circ\text{C} - 30^\circ\text{C}$) | Ideal ($6.5 - 8.5$) | **Sangat Baik** | Kualitas air sangat optimal. Pertahankan sirkulasi dan jadwal pakan. |
| **R6** | Ideal ($25^\circ\text{C} - 30^\circ\text{C}$) | Basa ($> 8.5$) | **Waspada** | Air terlalu basa. Tambahkan daun ketapang kering atau buffer penurun pH. |
| **R7** | Panas ($> 30^\circ\text{C}$) | Asam ($< 6.5$) | **Bahaya** | Air mematikan bagi ikan nila. Segera kuras dan ganti air kolam! |
| **R8** | Panas ($> 30^\circ\text{C}$) | Ideal ($6.5 - 8.5$) | **Waspada** | Suhu air terlalu panas. Nyalakan sirkulasi air segar atau tambah peneduh. |
| **R9** | Panas ($> 30^\circ\text{C}$) | Basa ($> 8.5$) | **Bahaya** | Air mematikan bagi ikan nila. Segera kuras dan ganti air kolam! |

#### 3. Masukkan Flowchart Sistem dari Dokumen Ringkasan
* Pindahkan gambar flowchart di halaman 3 dokumen ringkasan ke dalam Subbab 3.4 sebagai **Gambar 3.2 Flowchart Alur Kerja Sistem Monitoring Kualitas Air**.
* Pada flowchart, ubah panah alur: proses akuisisi sensor dan pengiriman data berjalan kontinu (*infinite loop*). Hapus terminator "Selesai" atau beri kondisi pemutus (misal: "Apakah alat dimatikan?").

#### 4. Selesaikan Kontradiksi Arsitektur Platform & Database
* **Keputusan Desain:** Karena Saudara menggunakan platform **Blynk IoT**, **hapus perancangan tabel SQL kustom** (`id_monitoring`, `id_perangkat`, dll.) dan narasi pembuatan backend REST API di Subbab 3.3.
* Gantilah Subbab 3.3 menjadi **Perancangan Aliran Data Blynk Datastreams**:
  * `V0`: Suhu Air (Float, Satuan °C, Pin Virtual Blynk)
  * `V1`: Nilai pH Air (Float, Skala 0.0–14.0, Pin Virtual Blynk)
  * `V2`: Status Mutu Air (String: Sangat Baik / Waspada / Bahaya)
  * `V3`: Saran Tindakan Kolam (String: Rekomendasi mitigasi)
  * `Event Blynk`: `peringatan_kualitas_air` (Trigger Push Notification otomatis ke HP)

#### 5. Skematik Pinout Elektronika ESP32
* Tambahkan tabel pemetaan pin hardware ESP32:
  * **DS18B20:** Pin Data dihubungkan ke **GPIO 4**, **wajib dipasang resistor pull-up 4.7 kΩ** ke VCC 3.3V.
  * **Sensor pH SEN0161-V2:** Pin Analog Output (AOUT) dihubungkan ke **GPIO 34 (ADC1)**.
  * *Catatan Penting:* **Dilarang menggunakan pin ADC2** (GPIO 0, 2, 4, 12, 13, 14, 15, 25, 26, 27) karena driver ADC2 dinonaktifkan oleh mikrokontroler ESP32 saat transmisi Wi-Fi berlangsung.

#### 6. Persamaan Kalibrasi Sensor pH
* Cantumkan rumus transfer function konversi tegangan ADC ke pH pada Subbab 3.4:
  $$\text{Tegangan (V)} = \frac{\text{ADC}_{\text{mentah}}}{4095.0} \times 3.3\,\text{V} \quad (3.1)$$
  $$\text{pH} = m \cdot \text{Tegangan} + c \quad (3.2)$$
  di mana nilai gradien ($m$) dan pergeseran ($c$) diperoleh dari hasil kalibrasi 2-titik larutan buffer standar pH 4.01 dan pH 6.86/7.00.

#### 7. Perbaikan Mockup Antarmuka (Halaman 41)
* Ganti gambar wireframe kustom dengan desain tata letak antarmuka resmi:
  * **Blynk Web Console:** Menampilkan widget Gauge Suhu & pH, Value Display Status Mutu, SuperChart riwayat per jam/hari, dan Event Log.
  * **Blynk Mobile App:** Menampilkan Gauge lingkaran, label rekomendasi tindakan, dan pop-up Push Notification.
  * Pastikan angka suhu yang ditampilkan realistis (misal: **28.5°C**, bukan angka aneh 7°C).

#### 8. Penanganan Fenomena *Flapping* (Cooldown Notifikasi)
* Pada firmware ESP32, tambahkan mekanisme *cooldown interval* (misalnya minimal 15 menit per notifikasi jika status tidak berubah) agar sistem tidak membombardir ponsel pembudidaya dengan ratusan notifikasi saat parameter berfluktuasi tepat di perbatasan ambang (misal suhu $24.9^\circ\text{C} \leftrightarrow 25.0^\circ\text{C}$).

#### 9. Spesifikasi Lokasi Kolam Penelitian (Subbab 3.7)
* Perjelas deskripsi lokasi: sebutkan lokasi kolam mitra budidaya di Samarinda (misalnya: *Kolam Budidaya Ikan Air Tawar di Kelurahan X, Kecamatan Y, Kota Samarinda*), dimensi kolam (misal: kolam terpal $3\times 4\text{ m}$ atau kolam tanah), dan sumber air kolam.

#### 10. Perbaikan Tabel Jadwal Penelitian (Tabel 3.x, Hal. 44–45)
* Lengkapi seluruh kolom bulan Januari s.d. Desember 2026 (kembalikan bulan Februari s.d. Juli yang hilang).
* Hapus titik-titik elipsis template (`4. …`, `3. …`, `6. …`).
* Beri tanda arsir/blok warna pada bulan-bulan rencana pelaksanaan kegiatan.

---

### 📚 D. DAFTAR PUSTAKA (🚨 RED ALERT KRUSIAL)

#### Tindakan Perbaikan Wajib:
1. **Hapus 5 referensi kelapa sawit & visi komputer** yang terbawa dari template Fakultas Teknik pada Halaman 46.
2. **Hapus kotak teks instruksi template** (*Keterangan: WAJIB menggunakan software management reference...*).
3. **Ekspor ulang Daftar Pustaka menggunakan Mendeley / Zotero** dengan gaya sitasi **IEEE** atau **APA 7th Edition**, dengan memuat seluruh referensi aktual yang dikutip di dalam naskah:
   - *Camelia, E. et al. (2026)* – Monitoring Suhu dan pH Ikan Nila Bioflok ESP32 Blynk.
   - *Manurung, N. et al. (2022)* – Sistem Monitoring Kualitas Air Kolam Lele IoT.
   - *Subianto, A. & Wardhana, R. (2024)* – Sistem Rekomendasi Kualitas Air Ikan Nila Rule-Based Reasoning.
   - *Maulana, R. et al. (2021)* – Monitoring dan Controlling Air Lele Fuzzy Logic.
   - *Irwansyah, M. et al. (2024)* – Monitoring Kualitas Air Budidaya Ikan Air Tawar IoT.
   - *Pane, R. & Andriyani, A. (2024)* – Sistem Monitoring Kualitas Air Kolam Ikan Air Tawar IoT.
   - *Badan Standardisasi Nasional. (2009).* *SNI 7550:2009: Produksi benih ikan nila hitam (Oreochromis niloticus Bleeker) kelas benih sebar.* BSN.
   - *(dan seluruh paper pendukung lainnya: Jelinda 2024, Goi & Nasrul 2025, Anwar & Latifa 2022, Mujadin 2017, Rozaq 2018, dll.)*.

---

### 📎 E. Bagian Lampiran (Halaman 48)

* **Hapus teks informal `Penjelasan lihat di ppt`**.
* Ganti dengan berkas fisik nyata:
  * **Lampiran 1:** Skematik Pengkabelan (*Wiring Diagram*) ESP32, DS18B20 (dengan resistor 4.7 kΩ), dan Sensor pH SEN0161-V2.
  * **Lampiran 2:** Lembar Rencana Kalibrasi Sensor pH dengan Larutan Buffer Standar.
  * **Lampiran 3:** Lembar Spesifikasi Teknis (*Datasheet*) ESP32 dan Sensor Suhu DS18B20 Waterproof.

---

## 🎯 4. Kisi-Kisi Pertanyaan Kritis Seminar Proposal & Panduan Menjawab

Berikut adalah 3 pertanyaan paling kritis yang pasti akan ditanyakan dosen penguji saat seminar proposal, lengkap dengan strategi argumentasi ilmiah:

1. **Pertanyaan Penguji Mengenai Pemilihan Metode:**
   > *"Mengapa Anda menggunakan metode Rule-Based (Forward Chaining) dan bukan Fuzzy Logic Mamdani yang bisa memodelkan kondisi abu-abu secara kontinu?"*  
   * **Jawaban Mahasiswa:**  
     *"Berdasarkan kebutuhan pembudidaya ikan nila di lapangan, ambang batas fisiologis poikilotermik ikan terhadap keasaman dan suhu memiliki batas kritis yang deterministik sesuai standar SNI 7550:2009. Metode Rule-Based dipilih karena menghasilkan rekomendasi tindakan mitigasi kolam yang tegas dan pasti (seperti penambahan takaran kapur dolomit atau penggantian air darurat). Selain itu, mesin inferensi 9 aturan Forward Chaining dapat dieksekusi secara instan dan sangat ringan langsung pada mikrokontroler ESP32 (Edge Computing) tanpa membebani memori SRAM dengan operasi defuzzifikasi kontinu, menjamin keandalan sistem saat beroperasi 24 jam nonstop."*

2. **Pertanyaan Penguji Mengenai Keandalan Sensor di Lapangan:**
   > *"Sensor pH analog berbasis elektroda kaca sangat rentan mengalami pergeseran pembacaan (drift) jika terendam air kolam berlumpur atau berlumut. Bagaimana mitigasi Anda?"*  
   * **Jawaban Mahasiswa:**  
     *"Pertama, dalam rancangan metodologi, sensor dikalibrasi secara berkala menggunakan metode 2-titik dengan larutan buffer standar pH 4.01 dan 6.86 untuk menghitung nilai akurasi MAPE. Kedua, pada implementasi fisik kolam, probe sensor diletakkan di dalam tabung pelindung berlubang (flow chamber) di dekat saluran sirkulasi air, bukan menancap di lumpur dasar kolam, sehingga elektroda kaca terhindar dari endapan sedimen langsung dan meminimalkan penempelan lumut."*

3. **Pertanyaan Penguji Mengenai Arsitektur IoT:**
   > *"Di mana sebenarnya aturan rule-based diproses? Di cloud Blynk atau di mikrokontroler? Dan bagaimana jika koneksi Wi-Fi di kolam terputus?"*  
   * **Jawaban Mahasiswa:**  
     *"Seluruh evaluasi matriks aturan rule-based dieksekusi secara lokal (Edge Computing) di dalam firmware mikrokontroler ESP32 sebelum data dipaketkan. Dengan demikian, jika koneksi internet terputus, mikrokontroler tetap dapat mengambil keputusan secara mandiri. Platform Blynk berfungsi sebagai gateway komunikasi cloud untuk sinkronisasi Web Console, visualisasi mobile app, dan pemicu push notification ke smartphone pembudidaya."*

---

## ✅ 5. Lembar Cek Mandiri Perbaikan Naskah (*Action Checklist*)

- [ ] Ganti `bu ros tercinta` & `pak anton jago iot` dengan nama dan gelar resmi pembimbing di Lembar Pengesahan.
- [ ] Bersihkan teks instruksi template Word, isi judul naskah, dan perbarui tahun 2026 di Kata Pengantar.
- [ ] Lakukan *Update Field* Microsoft Word untuk melenyapkan `Error! Bookmark not defined.` di Daftar Isi.
- [ ] Rapikan Daftar Tabel, Daftar Gambar, dan Daftar Singkatan (hilangkan kata `contents`).
- [ ] Sisipkan **Page Break (Ctrl + Enter)** di Halaman 33 sebelum tajuk BAB III.
- [ ] Tambahkan sitasi **SNI 7550:2009** sebagai acuan resmi parameter kolam ikan nila pada Bab I dan Bab II.
- [ ] Masukkan **Tabel Matriks SOTA** pada akhir Subbab 2.1.
- [ ] Bersihkan jejak copas mentah (`artikel https://...`, `SOCA JournalPtdsak`, `Politama`, sitasi kembar berdempetan).
- [ ] Pindahkan **Flowchart Sistem** dari dokumen ringkasan ke dalam Bab III Subbab 3.4.
- [ ] **Koreksi Tabel 3.4:** Tukar posisi kolom pH dan Suhu agar datanya tepat, serta perbaiki typo `Wapada`.
- [ ] Hapus rancangan tabel database SQL kustom di Bab III; fokuskan pada arsitektur **Blynk Datastreams & Virtual Pins**.
- [ ] Cantumkan tabel pemetaan pin hardware ESP32 (GPIO 4 DS18B20 + resistor 4.7 kΩ, GPIO 34 ADC1 sensor pH).
- [ ] Tuliskan rumus kalibrasi sensor pH ($V = \frac{\text{ADC}}{4095}\times 3.3$, $\text{pH} = mV + c$) dengan penomoran persamaan resmi.
- [ ] Ganti mockup Hal. 41 dengan tata letak widget Blynk Console & App (koreksi angka Suhu 7°C menjadi realistis).
- [ ] Lengkapi deskripsi lokasi kolam penelitian dan dimensi fisik kolam di Subbab 3.7.
- [ ] Lengkapi Tabel Jadwal Penelitian 2026 (Januari s.d. Desember, hapus elipsis `…`, beri arsir jadwal).
- [ ] 🚨 **GANTI TOTAL DAFTAR PUSTAKA:** Hapus 5 paper kelapa sawit, masukkan >25 paper IoT kualitas air menggunakan Mendeley/Zotero.
- [ ] Hapus kalimat `Penjelasan lihat di ppt` di Lampiran, ganti dengan skematik Fritzing dan form kalibrasi.
