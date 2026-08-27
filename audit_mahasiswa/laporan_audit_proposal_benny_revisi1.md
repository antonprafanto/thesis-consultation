# 📋 LAPORAN AUDIT FORENSIK LENGKAP & EVALUASI REVISI 1 PROPOSAL SKRIPSI

**Mahasiswa:** Benny Hernanda Putra (NIM: 2009106066)  
**Program Studi:** S1 Informatika, Fakultas Teknik, Universitas Mulawarman  
**Dosen Pembimbing:** Anton Prafanto, S.Kom., M.T.  
**Judul Proposal:** *Implementasi Convolutional Neural Network Berbasis MobileNetV2 pada Aplikasi Flutter untuk Klasifikasi Nominal Uang Kertas Rupiah*  
**Tanggal Evaluasi:** 27 Agustus 2026  
**Status Kelayakan:** **REVISI MINOR-MAYOR MENUJU SEMINAR PROPOSAL**

---

## 🔍 HASIL AUDIT FORENSIK KOMPREHENSIF (9 KATEGORI TEMUAN)

### 🚨 KATEGORI 1: Gap Metodologis (Disconnection antara Rumusan Masalah Bab 1 & Bab 3)
1. **Pengujian Efisiensi & Ketahanan Nyata (Rumusan Masalah 3 vs Subbab 3.6):**
   * Di Bab I Rumusan Masalah 3, mahasiswa menulis ingin menguji *akurasi, latency (ms), ketahanan uang lusuh/lecek, dan variasi pencahayaan pada smartphone*.
   * Namun di Bab III Subbab 3.6 (Perancangan Pengujian), **sama sekali tidak ada metodologi/skenario pengujian latency smartphone, lux pencahayaan, maupun uang lusuh**. Pengujian hanya ditulis standar pada 135 citra data uji per kelas hasil split dataset lab Rahmi.
2. **Implementasi & Aksesibilitas TTS (Rumusan Masalah 2 vs Subbab 3.5):**
   * Di Bab I Rumusan Masalah 2, mahasiswa menyebut fitur *Text-to-Speech (TTS)* untuk tunanetra.
   * Namun pada Wireframe (Gambar 3.4 hal. 28) dan alur perancangan aplikasi, tidak ada representasi interaksi suara, trigger audio keluaran nominal, maupun accessibility screen reader.

---

### 🚨 KATEGORI 2: Kesalahan Fatal Perhitungan Aritmatika Dataset (Bab III Subbab 3.3 & Tabel 3.1)
* **Temuan:**
  * Narasi Subbab 3.3 (hal. 23): *"Dataset terdiri atas tujuh kelas nominal uang kertas Rupiah, dan setiap kelas memiliki 900 citra. Dengan demikian, jumlah keseluruhan dataset yang digunakan adalah 5.700 citra."*
  * Tabel 3.1 (hal. 24): Data Training ($7 \times 630 = 4.410$) + Validation ($7 \times 135 = 945$) + Testing ($7 \times 135 = 945$). Namun baris Total ditulis **5700**.
* **Koreksi Fatal:**
  $$7 \times 900 = \mathbf{6.300\text{ citra}} \quad \text{dan} \quad 4.410 + 945 + 945 = \mathbf{6.300\text{ citra}} \quad (\text{BUKAN } 5.700)$$

---

### 🚨 KATEGORI 3: Font Simbol Matematika Rusak Total (Bab II hal. 17–18 / Persamaan 2.2 s.d. 2.5)
* Karakter formula corrupt menjadi simbol non-standar:
  * Persamaan 2.2 (Accuracy): `୎୳୫୪ୟ୦ ୮୰ୣୢ୧୩ୱ୧ ୠୣ୬ୟ୰ / ୎୳୫୪ୟ୦ ୱୣ୪୳୰୳୦ ୢୟ୲ୟ ୮ୣ୬୥୳୨୧ୟ୬`
  * Persamaan 2.3 (Precision): `்௉ / (்௉ ା ி௉)`
  * Persamaan 2.4 (Recall): `்௉ / (்௉ ା ிே)`
  * Persamaan 2.5 (F1-Score): `2 * (௉௥௘௖௜௦௜௢௡ * ோ௘௖௔௟௟) / (௉௥௘௖௜௦௜௢௡ ା ோ௘௖௔௟௟)`
* Redudansi kalimat pada Persamaan 2.1 (hal. 13): *"Secara matematis, ReLU secara matematis dituliskan pada persamaan 2.1."*

---

### 🚨 KATEGORI 4: Glitch Copy-Paste / Jejak AI Overview (Bab III hal. 26 Poin 9)
* Tertulis teks mentah sisa link web / AI search summary:
  > *"...format TensorFlow Lite.**android.googlesource+1**"*
* **Tindakan:** Hapus teks `android.googlesource+1`.

---

### 🚨 KATEGORI 5: Inkonsistensi & Mismatch Gambar (Ghost References)
1. **Daftar Gambar vs Isi Bab 3 (Gambar 3.4):**
   * Di Daftar Gambar (hal. viii): `Gambar 3.4 Wireframe Tampilan CameraX`
   * Di Isi Bab 3 (hal. 28): `Gambar 3.4 Wireframe Tampilan Kamera`
2. **Ghost Reference Gambar 2.1 (Bab II hal. 12):**
   * Paragraf menyebut: *"Hubungan antara kecerdasan buatan, machine learning, deep learning, CNN, dan MobileNetV2 ditunjukkan pada Gambar 2.1."*
   * Faktanya, Gambar 2.1 di hal. 10 adalah *Spesimen Uang Kertas*, dan bagan hierarki AI tersebut sama sekali tidak ada di naskah.

---

### 🚨 KATEGORI 6: Template Administrasi & Placeholder Belum Bersih
1. **Halaman Judul Bagian Dalam (hal. ii):** Terdapat teks liar bertuliskan `PROPOSAL SKRIPSI` di bagian paling bawah setelah tulisan "SAMARINDA 2026".
2. **Lembar Pengesahan (hal. iii):** Masih tertulis template `{Nama Dosen Gelar Lengkap 12 pt}`, `NIP {18 digit angka tanpa spasi}`, dan `[tgl, bln, tahun]`. Belum diisi nama Pembimbing I: **Anton Prafanto, S.Kom., M.T.**
3. **Kata Pengantar (hal. iv):**
   * Masih ada template kurung kurawal: `{Keluarga...}`, `{Bapak/Ibu}{Nama Dosen Gelar Lengkap}`, `{Honorable Mention...}`.
   * Kutip judul rusak: `IMPLEMENTASI...`.
   * Tertulis *"menyelesaikan skripsi saya"* (seharusnya *"proposal skripsi"*).

---

### 🚨 KATEGORI 7: State-of-the-Art & Diferensiasi Lemah (Bab II Subbab 2.1)
1. **Mayoritas Literatur Masih Non-Relevan:** Dari 10 studi terkait, 8 paper masih membahas daun anggrek, bawang merah, bunga, batik, korosi, dan cacar monyet (bukan uang Rupiah).
2. **Argumen Diferensiasi Lemah dengan Yahya & Fauziah (2026) di hal. 10 Poin 5:**
   * Mahasiswa hanya menulis perbedaan: *"Yahya pakai bahasa Kotlin, penelitian ini pakai Dart"*.
   * **Solusi Wajib:** Ganti dengan perbedaan kontribusi ilmiah:
     - Evaluasi on-device inference latency & RAM usage di berbagai spek smartphone.
     - Real-world stress testing pada uang lecek/lusuh dan variasi pencahayaan.
     - Aksesibilitas Text-to-Speech (TTS) offline untuk tunanetra.

---

### 🚨 KATEGORI 8: Sitasi & Standarisasi Daftar Pustaka (APA 7th)
1. Sitasi `(Martín Abadi dkk., 2015)` salah format nama depan, seharusnya `(Abadi dkk., 2015)`.
2. Daftar Pustaka No. 13: Tertulis nama depan lengkap `Martín Abadi, Ashish Agarwal...`, seharusnya inisial `Abadi, M., Agarwal, A., ...`.
3. Daftar Pustaka No. 23 (Vickers et al., 2023): Nama sumber jurnal/prosiding hilang (hanya tertulis `498–510`).
4. Format penomoran Daftar Pustaka: Standar APA 7th tidak menggunakan nomor urut 1, 2, 3, melainkan urutan abjad dengan *hanging indent*.

---

### 🚨 KATEGORI 9: Typo & Inkonsistensi Redaksi Bab I
1. **Tujuan Penelitian (hal. 4):** Ada dua kalimat pembuka berulang berturut-turut (*"Tujuan yang ingin dicapai dalam penelitian ini adalah membuat aplikasi Android..."* dan *"Tujuan yang ingin dicapai dalam penelitian ini adalah sebagai berikut..."*).
2. **Manfaat Penelitian (hal. 4):** Poin pertama tertulis `"b. Penulis"`, seharusnya nomor `"1. Penulis"`.
3. **Batasan Masalah Poin 7 (hal. 3):** Belum menyebut fitur suara Text-to-Speech (TTS).
