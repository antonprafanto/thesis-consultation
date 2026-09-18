# 📋 LAPORAN EVALUASI & CATATAN BIMBINGAN PROPOSAL SKRIPSI
## Evaluasi Draf Bab I & Panduan Penyusunan Proposal S1 Informatika

**Mahasiswa Bimbingan:** Ridho Putra Darma  
**NIM:** 2509106133 (Program Alih Jenjang Angkatan 2025)  
**Program Studi:** S1 Informatika, Fakultas Teknik, Universitas Mulawarman  
**Dosen Pembimbing:** Anton Prafanto, S.Kom., M.T.  
**Judul Usulan:** *Rancang Bangun Sistem Pelacakan Bola Dinamis Real-Time Menggunakan Kombinasi Segmentasi Citra dan Filter Kalman Terhadap Variasi Oklusi*  
**Dokumen yang Diperiksa:** `Skripsi Ridho Putra Darma.pdf` (Draf Awal 7 Halaman, diserahkan 18 September 2026)  
**Status Evaluasi:** **PROGRES SUBSTANSI SANGAT POSITIF — DRAF BAB I PERLU REVISI REDAKSIONAL & DILANJUTKAN KE BAB II DAN III**  

---

## 🌟 1. Apresiasi Dosen Pembimbing (Catatan Pembuka)

Halo Ridho, Bapak mengapresiasi lompatan kualitas yang **sangat signifikan** pada draf yang kamu kirimkan kali ini. 

Dibandingkan dengan naskah D3 lama kamu, draf Bab I ini menunjukkan bahwa kamu telah membaca arahan dengan sungguh-sungguh:
1. **Judul sudah ilmiah dan tepat sasaran:** Memfokuskan diri pada integrasi segmentasi citra dan Filter Kalman untuk mengatasi variasi oklusi.
2. **Gaya penulisan sudah standar S1:** Paragraf di latar belakang sudah menggunakan alur deduktif yang baik, didukung sitasi akademis, dan tidak lagi berupa bahasa tutorial lepas.
3. **Inisiatif kalibrasi interaktif:** Pencantuman rencana kalibrasi warna via slider GUI (*HSV Tuner*) merupakan poin praktis yang sangat bagus untuk sistem visi komputer riil.

Agar draf ini semakin matang dan siap diseminarkan di hadapan dewan penguji, berikut adalah catatan evaluasi konstruktif dan detail yang perlu kamu perhatikan dan perbaiki.

---

## 🧭 2. Catatan Mendasar (Struktur Dokumen & Administrasi)

### 📌 A. Kelengkapan Berkas: Ini Adalah Draf Bab I Proposal, Bukan Skripsi Lengkap
* Berkas yang kamu kirimkan berjudul `Skripsi Ridho Putra Darma.pdf` dengan tebal 7 halaman yang memuat Halaman Judul, Kata Pengantar, Abstrak, Bab I (Pendahuluan), dan Daftar Pustaka.
* **Klarifikasi:** Dalam tahapan akademik S1, dokumen ini berkedudukan sebagai **Draf Bab I Proposal Skripsi**. 
* Sebelum seminar, naskah proposal wajib memuat **Bab I (Pendahuluan)**, **Bab II (Tinjauan Pustaka & Landasan Teori)**, dan **Bab III (Metodologi Penelitian)**. Jadi, setelah merevisi Bab I ini, langkah berikutnya adalah menyusun Bab II dan Bab III.

### 📌 B. Blunder Gelar Kelulusan pada Halaman Judul (Halaman 1)
* Pada halaman cover tertulis:  
  > *"Diajukan Sebagai Salah Satu Syarat Untuk Memperoleh Gelar **Sarjana Pendidikan** Pada Progam Studi Informatika..."*
* **Koreksi:** Gelar kelulusan di Fakultas Teknik Universitas Mulawarman adalah **Sarjana Komputer (S.Kom.)**, bukan Sarjana Pendidikan (S.Pd. — itu untuk FKIP). 
* Perbaiki juga salah ketik: `Progam Studi` $\rightarrow$ `Program Studi`, serta cantumkan tahun pengajuan (misal: **Samarinda, 2026**).

---

## 🔍 3. Evaluasi Detail Halaman per Halaman (Page-by-Page Review)

### 📄 Halaman 2: Kata Pengantar
1. **Typo pada Judul Utama:**  
   Judul halaman tertulis `KATA PENGATAR` (kurang huruf **N**). Ubah menjadi `KATA PENGANTAR`.
2. **Penyebutan Jenis Berkas:**  
   Ubah kalimat *"menyelesaikan laporan tugas akhir/penelitian..."* menjadi *"menyelesaikan usulan penelitian Proposal Skripsi..."*.
3. **Penyebutan Program Studi (Poin 2):**  
   Tertulis *"Program Studi Informatika/Teknik Komputer"*. Di UNMUL, prodi kamu adalah **Program Studi S1 Informatika**. Hapus frasa "Teknik Komputer" (itu adalah nama prodi D3 kamu sebelumnya di Polnes agar tidak membingungkan penguji).

### 📄 Halaman 3: Abstrak & Abstract
1. **Posisi Abstrak pada Proposal Skripsi:**  
   Pada tahapan Proposal Skripsi (Bab I–III), penelitian **belum selesai dilaksanakan**. Oleh karena itu, kalimat seperti:
   > *"Hasil pengujian menunjukkan bahwa Filter Kalman berhasil memperhalus pergerakan bola dan tetap mampu memprediksi posisi serta arah pergerakan..."*
   belum tepat dicantumkan di proposal karena pengujian menyeluruh baru dilakukan pada tahap Skripsi/Tugas Akhir. Untuk naskah proposal di Informatika UNMUL, lembar Abstrak umumnya belum disertakan (abstrak baru wajib ada saat Draf Skripsi Lengkap / Seminar Hasil).
2. **Karakter Sintaks Mentah $(x, y)$:**  
   Pada teks tertulis `$(x, y)$`. Tanda dollar `$` adalah kode format penulisan rumus LaTeX. Jika kamu mengetik di Microsoft Word, tulis langsung koordinat $(x, y)$ tanpa tanda dollar agar rapi.
3. **Tata Letak Kata Kunci:**  
   Beri jarak 1 baris kosong (*enter*) sebelum tulisan `Kata Kunci:`, jangan disambung langsung di akhir kalimat paragraf.

---

### 📄 Halaman 4–5: Bab I Pendahuluan

#### 1.1 Latar Belakang
* **Penguatan Masalah (*Research Gap*):**  
  Paragraf pengantar sudah bagus. Namun, kamu perlu menambahkan 1 paragraf khusus yang menceritakan:
  > *Apa yang terjadi pada pelacakan bola jika hanya menggunakan metode konvensional (seperti deteksi warna HSV atau Hough Circles biasa) saat ada tangan/papan yang menutupi bola selama 0,5–1 detik?*
  Jelaskan bahwa deteksi visual murni akan langsung kehilangan objek (*track loss*) atau menghasilkan koordinat liar (*jitter/noise*). Dari situlah kamu masuk menjelaskan bahwa Filter Kalman hadir sebagai estimator dinamika untuk menjembatani lintasan bola selama masa oklusi tersebut.
* **Konteks Sitasi Saputra (2023):**  
  Pada paragraf kedua, kamu menulis: *"Python merupakan bahasa pemrograman dinamis yang fleksibel... (Saputra, 2023)"*.  
  Artikel Saputra (2023) meneliti tentang algoritma SIFT dan Kalman Filter untuk bola. Kurang pas jika disitir hanya untuk menjelaskan definisi umum bahasa Python. Sitirlah artikel Saputra saat kamu membahas pelacakan bola atau Filter Kalman.
* **Fenomena Spasi Acak (*Text Glitch*):**  
  Terdapat banyak kata yang terpotong spasi di tengah kata, contohnya: `d alam`, `keter batasan`, `mengor eksi`, `ekster nal`, `pandan gan`, `porta bilitas`, dan `domai` (kurang huruf n).  
  *Tips:* Ini biasanya terjadi karena format rata kanan-kiri (*Justify*) di Word yang terpengaruh pengaturan *spacing* atau konversi PDF. Pastikan lakukan *Proofreading* (baca ulang) sebelum diubah ke PDF.

#### 1.2 Rumusan Masalah
* Poin 1 & 2 sudah sangat baik.
* **Koreksi Poin 3:**  
  Tertulis: *"Seberapa besar peningkatan stabilitas dan akurasi pelacakan bola yang dihasilkan dari kombinasi segmentasi citra dan Filter Kalman **dibandingkan dengan teknik segmentasi lainnya**."*
  *Catatan Kritis:* Filter Kalman **bukanlah** algoritma segmentasi, melainkan algoritma pelacakan/estimasi (*tracking/state estimation*). Jadi pembandingnya bukan segmentasi lain, melainkan:
  > *"3) Seberapa besar peningkatan akurasi dan kontinuitas lintasan bola saat terjadi oklusi menggunakan integrasi Filter Kalman dibandingkan dengan sistem deteksi visual murni (tanpa filter)?"*  
  *(Jangan lupa tambahkan tanda tanya di akhir kalimat).*

#### 1.3 Batasan Masalah
* Huruf pertama kalimat pembuka perbaiki dari huruf kecil menjadi kapital: `Untuk memastikan penelitian ini lebih terfokus...`.
* Batasan masalah poin 1–4 sudah tepat dan realistis untuk lingkup S1.

#### 1.4 Tujuan Penelitian
* **Koreksi Mendasar pada Poin 2:**  
  Tertulis: *"Mengimplementasikan Filter Kalman untuk memprediksi dan memperhalus estimasi posisi bola serta **mempertahankan jejak posisi terakhir saat terjadi oklusi**."*
  *Catatan Konseptual:* Filter Kalman bukan sekadar "menyimpan/mengunci koordinat terakhir" (*coordinate lock*). Keunggulan Filter Kalman adalah mampu **memproyeksikan lintasan gerak bola ke depan** (*trajectory forecasting*) berdasarkan kecepatan sesaat ($v_x, v_y$) saat bola terhalang.
  *Usulan Redaksi Poin 2:*
  > *"2) Menerapkan algoritma Filter Kalman untuk memperhalus lintasan koordinat serta memprediksi proyeksi arah pergerakan bola secara kontinu ketika terjadi oklusi sementara."*

#### 1.6 Sistematika Penulisan
* Typo judul heading: `1.6 Sistematika Penenulisan` $\rightarrow$ ganti menjadi `1.6 Sistematika Penulisan`.

---

### 📄 Halaman 7: Daftar Pustaka
* **Jumlah Referensi:**  
  Saat ini baru tercantum **3 referensi**. Untuk proposal skripsi S1 di Informatika UNMUL, standar rujukan minimal adalah **15–20 referensi ilmiah** (utamakan jurnal nasional terakreditasi SINTA atau jurnal internasional bereputasi 5 tahun terakhir).
* **Referensi yang Perlu Ditambahkan:**
  1. Buku atau paper fundamental tentang ruang warna HSV dan operasi morfologi (*opening/closing*).
  2. Paper rujukan konsep dasar Filter Kalman diskrit (persamaan status dan pengukuran).
  3. Paper-paper terkini mengenai pelacakan objek olahraga/bola berbasis Computer Vision.
  4. Naskah Tugas Akhir D3 kamu sebelumnya di Polnes (wajib kamu sitir sebagai *Penelitian Terdahulu / Prior Work* untuk membuktikan keaslian dan etika akademik bebas autoplagiarisme).

---

## 🎯 4. Roadmap Penyusunan Bab II dan Bab III (Tuntunan Langkah Selanjutnya)

Agar pengerjaan proposal kamu terarah dan cepat selesai, berikut panduan isi untuk Bab II dan Bab III:

### 📚 Bab II: Tinjauan Pustaka
1. **Penelitian Terdahulu (State of the Art):**  
   Buat tabel komparasi minimal 5 penelitian terdahulu tentang deteksi/tracking bola. Cantumkan nama peneliti, tahun, metode deteksi, metode tracking, kelebihan, dan kelemahannya. Posisikan penelitian kamu di mana bedanya (*research gap*).
2. **Landasan Teori yang Wajib Ada:**
   * Pengolahan Citra Digital & Ruang Warna HSV (mengapa HSV lebih tahan perubahan cahaya dibanding RGB).
   * Operasi Morfologi Citra (Erosi, Dilasi, Opening untuk membuang noise masker warna).
   * Deteksi Kontur & Titik Berat Objek (*Centroid Detection* via Image Moments).
   * Matematika Filter Kalman Diskrit:
     - Persamaan Prediksi (*Time Update*): status $\hat{\mathbf{x}}_k^-$ dan kovariansi error $\mathbf{P}_k^-$.
     - Persamaan Koreksi (*Measurement Update*): Kalman Gain $\mathbf{K}_k$, update status $\hat{\mathbf{x}}_k$, dan update $\mathbf{P}_k$.
     - Penjelasan parameter matriks transisi $\mathbf{F}$, matriks pengukuran $\mathbf{H}$, noise proses $\mathbf{Q}$, dan noise pengukuran $\mathbf{R}$.

### ⚙️ Bab III: Metodologi Penelitian
1. **Diagram Alir Sistem (*Flowchart* Terpadu):**  
   Gambarkan alur secara presisi:  
   `Akuisisi Frame` $\rightarrow$ `Konversi HSV` $\rightarrow$ `Thresholding Masker Kuning` $\rightarrow$ `Morfologi` $\rightarrow$ `Deteksi Kontur Bola (x, y)` $\rightarrow$ `Kalman Filter (Predict & Correct)` $\rightarrow$ `Percabangan Oklusi (Jika deteksi hilang -> Predict Only & Hitung Counter Frame)` $\rightarrow$ `Tampilkan Output`.
2. **Perancangan Skenario Pengujian:**
   * **Pengujian Variasi Jarak & Pencahayaan:** Uji deteksi bola pada jarak terukur (misal: 1 m, 2 m, 3 m) dan intensitas cahaya berbeda (redup, normal, terang).
   * **Pengujian Oklusi Terkontrol:** Gelindingkan bola pada lintasan lurus melewati papan penghalang berukuran tertentu, lalu hitung selisih jarak piksel antara prediksi Kalman dengan posisi riil bola saat muncul kembali (*Re-acquisition Euclidean Error*).
   * **Pengujian Throughput / Kecepatan Komputasi:** Catat FPS rata-rata sistem pada resolusi kamera yang digunakan.

---

## 💬 5. Rangkuman Tindakan untuk Mahasiswa (Action Items)

| No | Bagian | Tindakan Perbaikan |
|:---:|:---|:---|
| 1 | **Cover** | Ganti gelar menjadi **Sarjana Komputer (S.Kom.)**, perbaiki typo `Progam`, tambahkan tahun pengajuan. |
| 2 | **Kata Pengantar** | Perbaiki typo heading `KATA PENGANTAR`, hapus frasa "Teknik Komputer". |
| 3 | **Abstrak** | Hapus klaim hasil pengujian (karena naskah masih proposal), bersihkan karakter mentah `$(x,y)$`. |
| 4 | **Bab 1.1** | Tambahkan ulasan masalah oklusi pada deteksi visual konvensional, bersihkan typo spasi kata. |
| 5 | **Bab 1.2 & 1.4** | Luruskan pemahaman: Kalman Filter adalah estimator lintasan (bukan segmentasi) dan fungsinya memproyeksikan lintasan gerak saat oklusi (bukan mengunci koordinat diam). |
| 6 | **Daftar Pustaka** | Tambahkan referensi hingga minimal 15 rujukan berkualitas, termasuk mencantumkan TA D3 kamu sebagai *prior work*. |
| 7 | **Kelanjutan** | Mulai rancang draft **Bab II (Tinjauan Pustaka)** dan **Bab III (Metodologi Penelitian)** sesuai panduan di atas. |

Tetap semangat Ridho! Progres kamu sudah berada di jalur yang benar. Silakan perbaiki Bab I ini sembari menyusun draf Bab II dan III, lalu kita jadwalkan sesi bimbingan tatap muka berikutnya di kampus.
