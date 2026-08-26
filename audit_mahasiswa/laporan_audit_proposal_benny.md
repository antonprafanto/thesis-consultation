# 📋 LAPORAN AUDIT & EVALUASI KELAYAKAN PROPOSAL SKRIPSI

**Kepada Mahasiswa:** Benny Hernanda Putra (NIM: 2009106066)  
**Program Studi:** S1 Informatika, Fakultas Teknik, Universitas Mulawarman  
**Dosen Pembimbing:** Anton Prafanto, S.Kom., M.T.  
**Judul Proposal:** *Implementasi Convolutional Neural Network Berbasis MobileNetV2 pada Aplikasi Flutter untuk Klasifikasi Nominal Uang Kertas Rupiah*  
**Tanggal Evaluasi:** 26 Agustus 2026  
**Status Kelayakan:** **LAYAK DENGAN SYARAT REVISI MAYOR (Major Revisions Required Before Approval)**

---

## ⚖️ 1. Resume Evaluasi Akademik (Apakah Pantas untuk S1 Informatika?)

Secara umum, topik ini **PANTAS dan MEMENUHI STANDAR S1 INFORMATIKA**, karena mengombinasikan dua domain utama keilmuan komputer:
1. **Artificial Intelligence / Computer Vision:** Penerapan deep learning *Convolutional Neural Network* (CNN) dengan arsitektur *MobileNetV2* dan teknik *Transfer Learning + Fine-Tuning*.
2. **Mobile Software Engineering:** Integrasi model inferensi *Edge AI (On-Device Inference)* menggunakan *TensorFlow Lite* pada aplikasi mobile multiplatform *Flutter (Dart)*.

### ⚠️ NAMUN, Terdapat 5 Masalah Kritis (*Red Flags*) yang Wajib Dibenahi:
Jika draf ini diajukan apa adanya ke Seminar Proposal, **mahasiswa berisiko tinggi dibantai dan tidak diluluskan oleh dosen penguji** karena adanya indikasi plagiasi template naskah lain, ketergantungan 100% pada dataset skripsi terdahulu, dan inkonsistensi fitur aksesibilitas tunanetra.

---

## 🚨 2. Temuan Kritis (*Red Flags*) pada Naskah Draf

### 🚨 RED FLAG 1: Skandal Tabel Lampiran Copy-Paste Naskah Orang Lain (FATAL!)
* **Temuan:** Pada Lampiran 2 dan Lampiran 6 (hal. 32–33 / baris 1447–1481), terdapat tabel:
  > *"Tabel Peringkat Hasil Pengujian Model pada Data Validasi: **YOLOv8-L, YOLOv8-S, YOLOv11-X, RT-DETR-L, YOLOv9-S, YOLOv10-N**..."*
* **Masalah Fatal:** Penelitian Benny adalah **Klasifikasi Citra MobileNetV2**, tetapi di lampirannya memuat data pengujian **Deteksi Objek YOLOv8, YOLOv11, dan RT-DETR**!
* **Dampak:** Ini adalah bukti tak terbantahkan bahwa mahasiswa menyalin (*copy-paste*) template skripsi mahasiswa lain tanpa membaca dan menghapusnya. Jika terlihat penguji, naskah ini akan langsung dicap tidak beretika/asal salin.
* **Tindakan:** Hapus seluruh tabel YOLO dan bersihkan panduan template Word pada Lampiran 1.

---

### 🚨 RED FLAG 2: Ketergantungan 100% pada Dataset Skripsi Kakak Tingkat (Mawaddah, 2023)
* **Temuan:** Pada Bab III Subbab 3.2 (hal. 22), mahasiswa menulis secara terbuka bahwa seluruh 5.600 citra uang diambil dari Google Drive milik **Rahmiatul Mawaddah (2023)**.
* **Masalah:** Jika mahasiswa hanya mengambil dataset yang sudah rapi dari skripsi lama lalu melatih MobileNetV2 dan membungkusnya ke Flutter, kontribusi penelitian (*novelty*) dinilai **sangat rendah** (hanya memindah platform dari Web Flask ke Mobile Flutter).
* **Solusi Wajib:** 
  1. Mahasiswa **WAJIB menambahkan dataset pengujian primer (*Real-world Testing Dataset*) mandiri** minimal 100–200 citra uang kertas yang diambil langsung menggunakan kamera smartphone.
  2. Data uji mandiri harus mencakup variasi kondisi nyata:
     - Uang kertas kondisi normal, lusuh/lecek, dan terlipat.
     - Variasi tingkat pencahayaan (redup/malam $\le 100\text{ lux}$, sedang/ruangan $\sim 300\text{ lux}$, terang/luar ruangan $\ge 1000\text{ lux}$).
     - Variasi jarak kamera ($10\text{ cm}$, $20\text{ cm}$, $30\text{ cm}$) dan sudut kemiringan ($30^\circ$, $45^\circ$, tegak lurus $90^\circ$).

---

### 🚨 RED FLAG 3: Paradoks Isu Tunanetra vs Ketiadaan Fitur Audio (Text-to-Speech)
* **Temuan:** Di Latar Belakang (Bab 1), mahasiswa menjadikan kesulitan **penyandang tunanetra** sebagai urgensi utama masalah penelitian.
* **Masalah Kritis:** Pada Bab 3 (Wireframe Gambar 3.4), aplikasi **hanya menampilkan teks nominal di layar HP tanpa ada fitur suara (Text-to-Speech / TTS) dan tanpa feedback getar (haptic)**!
* **Dilema Penguji:** Penguji pasti akan bertanya: *"Bagaimana seorang tunanetra bisa mengetahui nominal uang jika aplikasi Anda hanya memunculkan tulisan di layar?"*
* **Solusi Wajib:**
  - Mahasiswa **WAJIB menambahkan fitur Text-to-Speech (TTS)** menggunakan package Flutter seperti `flutter_tts` agar saat model berhasil mengklasifikasikan uang, aplikasi otomatis membacakan nominal melalui suara (misal: *"Uang lima puluh ribu rupiah"*).
  - Tambahkan feedback getar (`vibration`/`haptic_feedback`) saat kamera berhasil mendeteksi uang.

---

### 🚨 RED FLAG 4: Inkonsistensi Istilah Arsitektur (Flutter vs Android Native CameraX)
* **Temuan:** Di Judul dan Bab 2 tertulis **Aplikasi Flutter (Dart)**, namun pada Daftar Gambar (hal. viii) dan Bab 3 Gambar 3.4 tertulis *"Wireframe Tampilan **CameraX**"*.
* **Masalah:** CameraX adalah API library native Android (Jetpack Java/Kotlin), sedangkan Flutter menggunakan widget `CameraPreview` dari package `camera`.
* **Tindakan:** Ganti penamaan *"Tampilan CameraX"* menjadi *"Tampilan Kamera (Camera Stream Preview)"* agar tidak rancu dengan native development.

---

### 🚨 RED FLAG 5: Metodologi Pengujian Model Terlalu Dangkal
* **Temuan:** Bab 3 hanya memiliki 8 halaman. Pengujian hanya menyebutkan perhitungan *Confusion Matrix* pada data test split dan uji klik tombol *Black Box*.
* **Solusi Wajib:** Tambahkan skenario pengujian komprehensif pada Bab 3:
  1. **Pengujian Efisiensi Komputasi Mobile:** Ukur waktu inferensi (*inference latency* dalam milidetik) dan konsumsi memori (RAM) saat model .tflite dijalankan di smartphone.
  2. **Pengujian Robustness Citra:** Tabel matriks akurasi pengenalan uang berdasarkan variasi kondisi (uang baru vs uang lusuh, jarak kamera, dan intensitas cahaya).

---

## 🔍 3. Rincian Catatan Perbaikan Bab per Bab

### 📄 Bagian Awal Naskah
1. **Lengkapi Template Pengesahan & Kata Pengantar:**
   - Isi nama lengkap Dosen Pembimbing I dan II beserta NIP pada lembar Pengesahan (hal. iii).
   - Hapus instruksi template di Kata Pengantar (*`{Nama Dosen Gelar Lengkap}`*, *`{tgl pdd}`*, *`{Keluarga; boleh di No. 1...}`*).
2. **Koreksi Halaman Ganda & Typo:**
   - Pada halaman 2 dan 3 terdapat judul naskah yang berulang.

---

### 📘 BAB I – Pendahuluan
1. **Penyempurnaan Rumusan Masalah:**
   Perjelas aspek efisiensi komputasi on-device dan akurasi pada variasi kondisi fisik uang:
   > *"1. Bagaimana merancang dan mengimplementasikan model CNN berbasis arsitektur MobileNetV2 dengan pendekatan transfer learning untuk klasifikasi 7 nominal uang kertas Rupiah?"*  
   > *"2. Bagaimana mengintegrasikan model ke dalam aplikasi mobile Flutter menggunakan TensorFlow Lite yang dilengkapi output suara (Text-to-Speech) untuk kemudahan aksesibilitas?"*  
   > *"3. Bagaimana performa akurasi, robustness (pada uang lusuh/pencahayaan variatif), dan waktu inferensi model saat dieksekusi langsung pada perangkat smartphone?"*
2. **Sinkronisasi Tujuan Penelitian:**
   Buat 3 butir tujuan penelitian yang menjawab 3 rumusan masalah di atas secara simetris.

---

### 📗 BAB II – Tinjauan Pustaka
1. **Perbaikan Redaksi Subbab 2.1 Poin 1 (Boimau & Kaesmetan, 2024, hal. 6):**
   - Terdapat terjemahan mesin (*machine translation*) yang aneh: *"nilai kemalangan sebesar 0,0769"* (menerjemahkan kata *loss* menjadi *kemalangan*) dan *"lapisan rahasia"* (menerjemahkan *hidden layer* menjadi *lapisan rahasia*).
   - **Koreksi:** Ubah menjadi *"nilai training loss"* dan *"hidden layer / lapisan tersembunyi"*.
2. **Tabel 2.1 (Matriks Perbedaan Penelitian Terkait):**
   - Buat format tabel komparasi yang rapi (No, Peneliti/Tahun, Metode/Arsitektur, Dataset/Objek, Akurasi, Perbedaan dengan Penelitian Ini) agar *research gap* terlihat jelas.
3. **Koreksi Rumus Matematika (Hal. 18):**
   - Persamaan 2.4 (Recall) tertulis penyebut: $\frac{TP}{TP + F}$ (huruf N hilang pada FN). Koreksi menjadi:
     $$\text{Recall} = \frac{TP}{TP + FN}$$

---

### 📙 BAB III – Metodologi Penelitian
1. **Arsitektur Pipeline On-Device AI:**
   Gambarkan diagram alur data lengkap:  
   $$\text{Camera Stream} \rightarrow \text{Resize } (224 \times 224) \rightarrow \text{Normalisasi Float32 } [-1, 1] \rightarrow \text{TFLite Interpreter} \rightarrow \text{Softmax Output} \rightarrow \text{TTS Audio}$$
2. **Spesifikasi Model & Fine-Tuning:**
   Tuliskan detail hyperparameter:
   - Base Model: `MobileNetV2` (Pretrained on ImageNet).
   - Optimizer: `Adam` (Initial Learning Rate: $10^{-4}$, Fine-tuning LR: $10^{-5}$).
   - Batch Size: `32` / `64`.
   - Epoch: `50` dengan *Early Stopping* & *ModelCheckpoint*.
3. **Fitur Text-to-Speech (TTS) & UI Flow:**
   Tambahkan wireframe tampilan antarmuka saat tombol audio aktif dan pembacaan nominal otomatis.

---

## 🎯 4. Pertanyaan Ujian Seminar Proposal yang Wajib Disiapkan

1. **"Kenapa memilih MobileNetV2 dibanding MobileNetV3 atau YOLOv8-Nano?"**  
   *Jawaban:* MobileNetV2 memiliki struktur *Inverted Residuals* dan *Linear Bottlenecks* yang sangat stabil, memiliki ukuran model yang ringkas ($\sim 8-14\text{ MB}$), serta didukung penuh oleh interpreter `tflite_flutter` tanpa dependensi runtime yang berat.
2. **"Bagaimana model mengatasi masalah uang yang lusuh, terlipat, atau pencahayaan redup?"**  
   *Jawaban:* Model dilatih dengan variasi rotasi dan augmentasi citra, serta diuji secara khusus (*stress test*) menggunakan dataset primer pada 3 variasi intensitas lux cahaya dan 3 kondisi fisik uang (baru, lusuh, terlipat).
3. **"Apa bukti nyata aplikasi ini dapat digunakan oleh penyandang tunanetra?"**  
   *Jawaban:* Aplikasi mengintegrasikan modul *Text-to-Speech* (TTS) yang langsung mengonversi hasil klasifikasi tertinggi menjadi output suara bahasa Indonesia secara instan saat kamera diarahkan ke uang kertas.

---

## ✅ 5. Lembar Checklist Tindak Lanjut Revisi

- [ ] **MENGHAPUS Lampiran 2 dan 6 yang memuat tabel YOLOv8/v11/RT-DETR milik skripsi lain.**
- [ ] Membersihkan seluruh teks instruksi template Word pada Kata Pengantar dan Halaman Pengesahan.
- [ ] Mengoreksi istilah terjemahan mesin pada Bab II (*nilai kemalangan* $\rightarrow$ *loss value*, *lapisan rahasia* $\rightarrow$ *hidden layer*).
- [ ] Memperbaiki rumus Recall pada Persamaan 2.4 ($TP / (TP + FN)$).
- [ ] Mengubah istilah *"CameraX"* pada wireframe Bab III menjadi *"Camera Stream Preview (Flutter)"*.
- [ ] **Menambahkan komitmen pengambilan Dataset Uji Primer Mandiri** (uang lusuh, variasi jarak, dan pencahayaan).
- [ ] **Menambahkan fitur wajib Text-to-Speech (TTS) dan output suara nominal uang** untuk menjustifikasi target pengguna tunanetra.
- [ ] Menambahkan skenario pengujian *inference latency* (ms) dan pengujian *robustness* pada Bab III.
- [ ] Menggunakan Reference Manager (Mendeley / Zotero) untuk standarisasi Daftar Pustaka (APA 7th).

---
*Laporan evaluasi ini disusun sebagai rekomendasi resmi dosen pembimbing agar draf proposal Benny Hernanda Putra disempurnakan sebelum diajukan ke Seminar Proposal.*
