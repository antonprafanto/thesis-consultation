# 📋 LAPORAN AUDIT FORENSIK & EVALUASI KELAYAKAN PROPOSAL SKRIPSI

**Kepada Mahasiswa:** Benny Hernanda Putra (NIM: 2009106066)  
**Program Studi:** S1 Informatika, Fakultas Teknik, Universitas Mulawarman  
**Dosen Pembimbing:** Anton Prafanto, S.Kom., M.T.  
**Judul Proposal:** *Implementasi Convolutional Neural Network Berbasis MobileNetV2 pada Aplikasi Flutter untuk Klasifikasi Nominal Uang Kertas Rupiah*  
**Tanggal Evaluasi:** 26 Agustus 2026  
**Status Kelayakan:** **LAYAK DENGAN SYARAT REVISI MAYOR (Major Revisions Required Before Approval)**

---

## ⚖️ 1. Resume Evaluasi Akademik (Apakah Pantas untuk S1 Informatika?)

Secara umum, topik ini **PANTAS dan MEMENUHI STANDAR S1 INFORMATIKA**, karena mengombinasikan dua pilar utama keilmuan komputer:
1. **Artificial Intelligence / Computer Vision:** Penerapan deep learning *Convolutional Neural Network* (CNN) dengan arsitektur *MobileNetV2* dan teknik *Transfer Learning + Fine-Tuning*.
2. **Mobile Software Engineering:** Integrasi model inferensi *Edge AI (On-Device Inference)* menggunakan *TensorFlow Lite* pada aplikasi mobile multiplatform *Flutter (Dart)*.

### ⚠️ NAMUN, Terdapat 7 Masalah Kritis (*Red Flags*) yang Wajib Dibenahi:
Jika draf ini diajukan apa adanya ke Seminar Proposal, **mahasiswa berisiko tinggi dibantai dan tidak diluluskan oleh dosen penguji** karena adanya indikasi plagiasi template naskah lain, penyembunyian paper pembanding utama (*novelty clash*), ketergantungan 100% pada dataset lama, dan rumus matematika yang rusak.

---

## 🚨 2. Temuan Kritis Forensik (*Red Flags*) pada Naskah Draf

### 🚨 RED FLAG 1: *Novelty Clash* dengan Paper Yahya & Fauziah (2026) yang Disembunyikan di Bab II
* **Temuan:** Di Bab I (hal. 2 / line 349) dan Daftar Pustaka No. 26, mahasiswa menyitir paper:  
  > *Yahya, H., & Fauziah, E. (2026). "Implementasi CNN Transfer Learning MobileNetV2 untuk Klasifikasi Mata Uang Rupiah bagi Tunanetra". RIGGS: Journal of AI & Digital Business.*
* **Masalah Fatal:** Judul paper tersebut **HAMPIR 100% IDENTIK** dengan judul skripsi Benny! Namun, di Bab II (Subbab 2.1 dan Tabel Perbedaan Penelitian), Benny **SENGAJA TIDAK MEMASUKKAN paper Yahya & Fauziah (2026)** ke dalam tinjauan pustaka dan matriks perbandingan, melainkan hanya membandingkan diri dengan skripsi Mawaddah (2023).
* **Celah Penguji:** Dosen penguji akan menuduh mahasiswa melakukan *cherry-picking* referensi dan plagiasi topik/metode.
* **Solusi Wajib:** Benny **wajib memasukkan paper Yahya & Fauziah (2026) ke dalam Tabel Perbandingan Bab II** dan menjelaskan dengan tegas apa diferensiasi/kebaruan (*novelty*) skripsinya (misal: pengujian *on-device inference latency* riil pada berbagai spek HP, dataset uang lecek/lusuh, atau integrasi TTS offline di Flutter).

---

### 🚨 RED FLAG 2: Skandal Tabel Lampiran Copy-Paste Naskah Orang Lain (FATAL!)
* **Temuan:** Pada Lampiran 2 dan Lampiran 6 (hal. 32–33 / baris 1447–1481), terdapat tabel:
  > *"Tabel Peringkat Hasil Pengujian Model: **YOLOv8-L, YOLOv8-S, YOLOv11-X, RT-DETR-L, YOLOv9-S, YOLOv10-N**..."*
* **Masalah Fatal:** Penelitian Benny adalah **Klasifikasi Citra MobileNetV2**, tetapi di lampirannya memuat data pengujian **Deteksi Objek YOLOv8, YOLOv11, dan RT-DETR**!
* **Dampak:** Ini bukti tak terbantahkan bahwa mahasiswa menyalin (*copy-paste*) template naskah mahasiswa lain tanpa membaca/menghapusnya.
* **Tindakan:** Hapus seluruh tabel YOLO dan bersihkan instruksi template Word pada Lampiran 1.

---

### 🚨 RED FLAG 3: Tinjauan Pustaka Bab II "Salah Sasaran" (Ketiadaan Literatur Uang Kertas)
* **Temuan:** Di Subbab 2.1 (Penelitian Terkait), mahasiswa mereview 10 artikel tentang: *bumbu rempah, daun padi, penyakit mata, buah-buahan, korosi, daun kentang, batik, bunga, daun bawang merah, dan daun anggrek*.
* **Masalah:** Dari 10 penelitian tersebut, **TIDAK ADA SATUPUN penelitian tentang klasifikasi uang kertas Rupiah yang direview di Subbab 2.1**, padahal di Daftar Pustaka ada paper Alfita (2022), Bahar (2023), Mawaddah (2023), dan Yahya (2026).
* **Tindakan:** Ganti minimal 3–4 penelitian pertanian/bunga tersebut dengan penelitian terkait klasifikasi uang kertas Rupiah agar State-of-the-Art (SOTA) relevan.

---

### 🚨 RED FLAG 4: Ketergantungan 100% pada Dataset Skripsi Kakak Tingkat (Mawaddah, 2023)
* **Temuan:** Pada Bab III Subbab 3.2 (hal. 22), mahasiswa menulis terang-terangan bahwa seluruh 5.600 citra uang diambil dari Google Drive skripsi **Rahmiatul Mawaddah (2023)**.
* **Masalah:** Jika mahasiswa hanya melatih model dari dataset yang sudah matang dari skripsi lama, kontribusi penelitian dinilai sangat rendah (hanya memindahkan skrip model ke Flutter).
* **Solusi Wajib:** 
  1. Mahasiswa **WAJIB menambahkan dataset pengujian primer mandiri (*Real-world Testing Dataset*)** minimal 100–200 citra uang kertas yang diambil langsung menggunakan kamera smartphone.
  2. Data uji mandiri harus mencakup variasi kondisi nyata:
     - Uang kertas kondisi baru, lusuh/lecek, dan terlipat.
     - Variasi tingkat pencahayaan (redup $\le 100\text{ lux}$, ruangan $\sim 300\text{ lux}$, luar ruangan $\ge 1000\text{ lux}$).
     - Variasi jarak kamera ($10\text{ cm}$, $20\text{ cm}$, $30\text{ cm}$) dan sudut kemiringan ($30^\circ$, $45^\circ$, $90^\circ$).

---

### 🚨 RED FLAG 5: Asumsi Keliru Mengenai Augmentasi Citra (Bab 2 & Bab 3)
* **Temuan:** Pada Subbab 2.11 (hal. 17) & Subbab 3.1 (hal. 21), mahasiswa menulis:  
  > *"Dataset yang digunakan sudah memiliki variasi rotasi (0°, 90°, 180°, 270°)... sehingga **tidak dilakukan augmentasi tambahan**."*
* **Kelemahan Ilmiah Computer Vision:** Di dunia nyata, pengguna tunanetra tidak memegang uang tepat pada sudut kelipatan $90^\circ$! Sudut pegangan bisa $15^\circ, 35^\circ, 65^\circ$, dan pencahayaan dinamis. Tanpa augmentasi acak (*Random Rotation, Zoom, Brightness/Contrast*), model akan mengalami *overfitting* dan akurasi akan anjlok saat diuji di dunia nyata.
* **Solusi:** Wajib menerapkan *data augmentation* dinamis pada pipeline pelatihan TensorFlow/Keras.

---

### 🚨 RED FLAG 6: Paradoks Isu Tunanetra vs Ketiadaan Fitur Audio (Text-to-Speech)
* **Temuan:** Di Bab I, Benny menjual urgensi bahwa aplikasi ini dibuat untuk **membantu penyandang tunanetra**.
* **Masalah:** Pada perancangan antarmuka (Wireframe Gambar 3.4), aplikasi **hanya menampilkan tulisan teks di layar HP tanpa ada suara (Text-to-Speech / TTS) dan tanpa feedback getar (haptic)**!
* **Dilema Penguji:** *"Bagaimana tunanetra bisa melihat teks nominal di layar jika tidak ada suara?"*
* **Solusi Wajib:** Mahasiswa **wajib mengintegrasikan package `flutter_tts`** sehingga setiap kali uang terklasifikasi, aplikasi otomatis membacakan nominal uang secara offline dalam bahasa Indonesia.

---

### 🚨 RED FLAG 7: Font Simbol Persamaan Matematika Rusak Total (Bab 2)
* **Temuan:** Pada Persamaan 2.2 s.d. 2.5 (hal. 18–19), teks formula matematika rusak menjadi karakter kotak/aksara asing non-standar:
  - Accuracy (Persamaan 2.2): `୎୳୫୪ୟ୦ ୮୰ୣୢ୧୩ୱ୧...`
  - Precision (Persamaan 2.3): `்௉ / (்௉ ା ி௉)`
  - Recall (Persamaan 2.4): `்௉ / (்௉ ା ி)` *(huruf N hilang pada FN)*.
* **Solusi:** Ketik ulang seluruh persamaan menggunakan fitur Equation Microsoft Word atau LaTeX yang bersih.

---

## 🔍 3. Rincian Catatan Perbaikan Bab per Bab

### 📄 Bagian Awal Naskah
1. **Lengkapi Template Pengesahan & Kata Pengantar:**
   - Isi nama lengkap Dosen Pembimbing I dan II beserta NIP pada lembar Pengesahan (hal. iii).
   - Hapus instruksi template di Kata Pengantar (*`{Nama Dosen Gelar Lengkap}`*, *`{tgl pdd}`*, *`{Keluarga; boleh di No. 1...}`*).
2. **Koreksi Duplikasi Gambar 2.1:**
   - Di Bab 2 terdapat dua label Gambar 2.1: Spesimen Uang (hal. 11) dan teks pemanggilan diagram hierarki AI (hal. 12).

---

### 📘 BAB I – Pendahuluan
1. **Penyempurnaan Rumusan Masalah:**
   Perjelas aspek efisiensi komputasi on-device dan akurasi pada variasi kondisi fisik uang:
   > *"1. Bagaimana merancang dan melatih model CNN berbasis arsitektur MobileNetV2 dengan transfer learning dan fine-tuning untuk klasifikasi 7 pecahan uang kertas Rupiah?"*  
   > *"2. Bagaimana mengintegrasikan model .tflite ke dalam aplikasi Flutter yang dilengkapi fitur Text-to-Speech (TTS) untuk aksesibilitas tunanetra?"*  
   > *"3. Bagaimana performa akurasi, waktu inferensi (latency ms), dan ketahanan model terhadap uang lusuh/lecek serta variasi pencahayaan saat dijalankan langsung pada smartphone?"*
2. **Sinkronisasi Tujuan Penelitian:**
   Buat 3 butir tujuan penelitian yang menjawab 3 rumusan masalah di atas secara simetris.

---

### 📗 BAB II – Tinjauan Pustaka
1. **Perbaikan Terjemahan Mesin (Subbab 2.1 Poin 1, hal. 6):**
   - Koreksi terjemahan aneh: *"nilai kemalangan 0,0769"* ➔ **"nilai training loss 0,0769"**; *"lapisan rahasia"* ➔ **"lapisan tersembunyi / hidden layer"**.
2. **Hindari Sitasi Blog Web (Daftar Pustaka No. 9):**
   - Sitasi `GeeksforGeeks (2026)` untuk konsep CNN tidak layak untuk skripsi S1. Ganti dengan buku teks resmi (*Goodfellow et al., 2016*).

---

### 📙 BAB III – Metodologi Penelitian
1. **Lengkapi Detail Hyperparameter Training:**
   Tuliskan spesifikasi konfigurasi model:
   - Base Model: `MobileNetV2` (Pretrained on ImageNet).
   - Input Shape: $224 \times 224 \times 3$.
   - Dense Layer & Regularization: `GlobalAveragePooling2D`, `Dropout(0.2)`, `Dense(7, activation='softmax')`.
   - Optimizer: `Adam` (Initial LR: $10^{-4}$, Fine-tuning LR: $10^{-5}$).
   - Loss Function: `CategoricalCrossentropy`.
   - Batch Size: `32` / `64`, Epoch: `50` (dengan *EarlyStopping* & *ModelCheckpoint*).
2. **Koreksi Istilah Arsitektur (Flutter vs CameraX):**
   - Ubah penamaan *"Wireframe Tampilan CameraX"* pada Gambar 3.4 menjadi *"Wireframe Tampilan Kamera (Camera Stream Preview)"*.
3. **Pengujian Efisiensi Komputasi Mobile:**
   - Tambahkan tabel skenario pengujian waktu inferensi (*latency* per frame dalam milidetik) dan konsumsi memori RAM saat model .tflite dijalankan di smartphone.

---

## 🎯 4. Pertanyaan Ujian Seminar Proposal yang Wajib Disiapkan Mahasiswa

1. **"Apa perbedaan penelitian Anda dengan publikasi Yahya & Fauziah (2026) yang juga menggunakan MobileNetV2 untuk tunanetra?"**  
   *Jawaban:* Penelitian kami berfokus pada integrasi on-device inference menggunakan Flutter & TFLite secara offline dengan modul Text-to-Speech mandiri, serta melakukan evaluasi ketahanan model terhadap variasi uang lecek/lusuh dan pencahayaan dinamis secara empiris.
2. **"Kenapa memilih MobileNetV2 dibanding MobileNetV3 atau YOLOv8-Nano?"**  
   *Jawaban:* MobileNetV2 memiliki struktur *Inverted Residuals* dan *Linear Bottlenecks* yang sangat stabil, memiliki ukuran model yang ringkas ($\sim 8-14\text{ MB}$), serta didukung penuh oleh interpreter `tflite_flutter` tanpa dependensi runtime yang berat.
3. **"Bagaimana model mengatasi masalah uang yang lusuh, terlipat, atau pencahayaan redup?"**  
   *Jawaban:* Model dilatih dengan augmentasi citra acak (*random brightness & rotation*), serta diuji secara khusus (*stress test*) menggunakan dataset primer pada 3 variasi intensitas lux cahaya dan 3 kondisi fisik uang (baru, lusuh, terlipat).
4. **"Apa bukti nyata aplikasi ini dapat digunakan oleh penyandang tunanetra?"**  
   *Jawaban:* Aplikasi mengintegrasikan modul *Text-to-Speech* (TTS) yang langsung mengonversi hasil klasifikasi tertinggi menjadi output suara bahasa Indonesia secara instan saat kamera diarahkan ke uang kertas.

---

## ✅ 5. Lembar Checklist Tindak Lanjut Revisi Mahasiswa

- [ ] **MENGHAPUS Lampiran 2 dan 6 yang memuat tabel YOLOv8/v11/RT-DETR milik skripsi lain.**
- [ ] **Memasukkan paper Yahya & Fauziah (2026) ke dalam tinjauan pustaka Bab II dan matriks perbandingan State-of-the-Art.**
- [ ] Mengganti 3–4 literatur non-relevan (daun bawang, bunga, dll.) di Bab 2 dengan penelitian klasifikasi uang Rupiah.
- [ ] Memperbaiki seluruh font simbol matematika yang rusak pada Persamaan 2.2, 2.3, 2.4, dan 2.5.
- [ ] Mengoreksi istilah terjemahan mesin (*nilai kemalangan* $\rightarrow$ *training loss*, *lapisan rahasia* $\rightarrow$ *hidden layer*).
- [ ] Mengganti sitasi blog GeeksforGeeks dengan buku teks standar deep learning.
- [ ] Mengubah istilah *"CameraX"* pada wireframe Bab III menjadi *"Camera Stream Preview (Flutter)"*.
- [ ] **Menambahkan komitmen pengambilan Dataset Uji Primer Mandiri** (uang lusuh, variasi jarak, dan pencahayaan).
- [ ] **Menambahkan fitur wajib Text-to-Speech (TTS) dan output suara nominal uang** untuk menjustifikasi target pengguna tunanetra.
- [ ] Menerapkan *data augmentation* dinamis pada Bab III.
- [ ] Menambahkan skenario pengujian *inference latency* (ms) dan konsumsi memori di smartphone pada Bab III.
- [ ] Menggunakan Reference Manager (Mendeley / Zotero) untuk standarisasi Daftar Pustaka (APA 7th).

---
*Laporan evaluasi forensik ini disusun sebagai rekomendasi resmi dosen pembimbing agar draf proposal Benny Hernanda Putra disempurnakan sebelum diajukan ke Seminar Proposal.*
