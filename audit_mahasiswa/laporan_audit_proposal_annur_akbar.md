# 📋 LAPORAN AUDIT FORENSIK & EVALUASI SEMINAR PROPOSAL SKRIPSI (KOMPREHENSIF)

**Mahasiswa Bimbingan:** Muhammad Annur Akbar (NIM: 2309106110)  
**Program Studi:** S1 Informatika, Fakultas Teknik, Universitas Mulawarman  
**Dosen Pembimbing I:** Anton Prafanto, S.Kom., M.T.  
**Dosen Pembimbing II:** Ir. Novianti Puspitasari, S.Kom., M.Eng.  
**Koordinator Program Studi:** Awang Harsa Kridalaksana, S.Kom., M.Kom. (NIP 19731229 200501 1 002)  
**Judul Naskah:** *Rancang Bangun Perangkap Hama Cahaya Berbasis Raspberry Pi 4 dengan Algoritma YOLOv5*  
**Dokumen yang Diaudit:** `SKRIPSI_Muhammad_Annur_Akbar_LightTrap_udah revisi.pdf` / `.docx` (46 Halaman)  
**Status Evaluasi:** **DRAF PROPOSAL SKRIPSI — WAJIB REVISI KRUSIAL SEBELUM UJIAN SEMINAR PROPOSAL**

---

> [!NOTE]
> **Panduan Dosen Pembimbing:** Dokumen ini disusun sebagai evaluasi audit forensik akademik dan teknis menyeluruh untuk mempersiapkan mahasiswa menghadapi **Ujian Seminar Proposal Skripsi** di Program Studi S1 Informatika Fakultas Teknik Universitas Mulawarman. Audit mencakup integritas sitasi ilmiah, kepatuhan tata tulis & margin baku, keakuratan metodologi *edge computing & computer vision*, audit formula matematis, serta simulasi pertanyaan kritis dewan penguji.

---

## ⚖️ 1. Resume Evaluasi Akademik Umum

Secara substansi, proposal penelitian yang diajukan oleh Muhammad Annur Akbar memiliki **arah dan relevansi terapan yang sangat kuat, aplikatif, dan kontekstual**. Penelitian ini berangkat dari studi kasus nyata di lahan pertanian cabai mitra Balai Tani ECO-STEP binaan PT Pertamina EP Sangatta di Lapangan Semberah, RT 13, Desa Tanah Datar, Kecamatan Muara Badak. Rancangan arsitektur *on-device edge computing* menggunakan **Raspberry Pi 4 (RAM 4 GB)**, webcam **Logitech C270 (HD 720p)**, lampu atraktan **UV 15 Watt**, model deteksi ringan **YOLOv5n**, strategi penghitungan agregasi per jam ($N_{\text{jam}}$), serta bot notifikasi **Telegram** menunjukkan rancang bangun sistem yang terukur untuk konteks pertanian skala kecil.

Namun, dari hasil audit forensik multi-dimensi terhadap naskah PDF dan dokumen sumber DOCX, ditemukan sejumlah **cacat kritis (*critical scientific & academic red flags*)**, **indikasi fabrikasi pustaka / halusinasi AI (*AI hallucinated references*)**, **pelanggaran margin dan format tata tulis baku FT Unmul**, **inkonsistensi status dokumen (Skripsi vs Proposal)**, **kerusakan elemen formalia & penomoran halaman awal**, **tabel jadwal penelitian yang rusak/kosong**, serta **anomali tata letak struktur sub-bab**.

---

## 🚨 2. Temuan Kritis (*Critical Red Flags*) & Kelemahan Metodologi

### 🚨 RED FLAG 1: Referensi & Sitasi Fiktif / Halusinasi AI (*Fabricated AI Citations*) — SANGAT FATAL!

Dalam Bab II (Tinjauan Pustaka) dan Daftar Pustaka, ditemukan beberapa rujukan literatur yang terbukti **fiktif, metadata palsu, atau hasil halusinasi generator AI**:

| No | Rujukan dalam Naskah | Fakta Hasil Penelusuran Forensik | Kategori Pelanggaran |
| :--- | :--- | :--- | :--- |
| **1** | **Khalid, Azahari, & Nordin (2026)**<br>*"Edge-based IoT pest monitoring system for chili farms using YOLOv8..."*<br>Computers and Electronics in Agriculture, 230, 109811. | **Paper Fiktif (Tidak Pernah Terbit)**. Artikel dengan judul, penulis, dan volume ini tidak ada di jurnal *Computers and Electronics in Agriculture*. | **Halusinasi AI / Fiktif** |
| **2** | **Zarboubi, Bellout, Chabaa, & Dliou (2026)**<br>*"Towards eco-friendly apple farming: Real-time codling moth monitoring using improved YOLOv10..."*<br>PLOS ONE, 21(1), e0298110.<br>DOI: `10.1371/journal.pone.0298110` | **DOI Tertukar / Palsu**. DOI `10.1371/journal.pone.0298110` adalah artikel bidang Kedokteran/Neurologi (*"Lateral frontoparietal effective connectivity... in patients with traumatic disorders of consciousness"*, terbit 2024), bukan tentang hama apel! | **Fabrikasi Metadata / Salah DOI** |
| **3** | **Zarboubi, Bellout, Chabaa, & Dliou (2024)**<br>*"IoT-based pest detection in agriculture using Raspberry Pi and YOLOv10m..."*<br>IEEE Access, 12, 14210–14222.<br>DOI: `10.1109/ACCESS.2024.3354112` | **DOI Placeholder Template**. DOI berakhiran `.3354112` merupakan teks dummy bawaan template IEEE (*"Doi Number"*), bukan nomor registrasi artikel riil. | **Metadata Dummy** |
| **4** | **Huang, Liu, Zhao, dkk. (2025)**<br>*"YOLO-YSTs: An improved YOLOv10n-based method..."*<br>Agronomy, 15(2), 345–359.<br>DOI: `10.3390/agronomy15020345` | **Volume/Issue Salah**. Paper aslinya terbit di *Agronomy 2025, 15(3), Article 575*, dengan DOI resmi: `10.3390/agronomy15030575`. | **Ketidakakuratan Sitasi** |
| **5** | **Makerguides (2026)**<br>*"Active and passive piezo buzzers with Arduino"* | Tahun penulisan web dicantumkan 2026 tanpa tanggal akses (*accessed date*), padahal konten artikel web sudah ada jauh sebelum 2026. | **Format Sitasi Web Tidak Baku** |

* **Dampak saat Sidang:** Di hadapan dewan penguji seminar proposal, jika penguji mengecek DOI atau menelusuri artikel di Google Scholar/Scopus, mahasiswa akan langsung dicap melakukan fabrikasi pustaka akademik.
* **Solusi Wajib:**
  1. Hapus seluruh pustaka fiktif/palsu tersebut dari Bab II dan Daftar Pustaka.
  2. Input ulang seluruh pustaka menggunakan **Mendeley Reference Manager / Zotero** dengan metadata yang diverifikasi langsung dari file PDF artikel aslinya.
  3. Ganti referensi pembanding dengan paper *peer-reviewed* riil terkait *light-trap* dan *pest detection* (misalnya paper Zhang et al. AgriPest-YOLO 2022, Ahmad et al. 2022, dll).

---

### 🚨 RED FLAG 2: Pelanggaran Margin Baku & Format Halaman (4-4-3-3 vs 3.5-3.5-2.5-2.5)

* **Hasil Audit Pengaturan Dokumen Word (.docx):**
  * Margin Atas (*Top*): **3.50 cm** *(Standar FT: 4.0 cm)*
  * Margin Kiri (*Left*): **3.50 cm** *(Standar FT: 4.0 cm untuk ruang penjilidan)*
  * Margin Bawah (*Bottom*): **2.50 cm** *(Standar FT: 3.0 cm)*
  * Margin Kanan (*Right*): **2.50 cm** *(Standar FT: 3.0 cm)*
* **Line Spacing:** Ditemukan campuran antara `1.0`, `1.15`, dan `1.5` pada badan teks.
* **Solusi Wajib:** Ubah pengaturan *Page Setup* Word ke standar baku Fakultas Teknik Universitas Mulawarman: **Atas = 4 cm, Kiri = 4 cm, Bawah = 3 cm, Kanan = 3 cm**, ukuran kertas **A4**, serta konsisten menggunakan **1.5 spasi** untuk teks utama.

---

### 🚨 RED FLAG 3: Ketidaksinkronan Status Dokumen (Skripsi vs Proposal) & Typo Fatal Halaman Judul

1. **Inkonsistensi Status Naskah:**
   * Nama file: `SKRIPSI_Muhammad_Annur_Akbar_LightTrap_udah revisi.pdf`
   * Di chat WhatsApp, mahasiswa menyebut *"skripsi terbaru saya yang sudah saya perbaiki..."*
   * Faktanya, isi dokumen adalah **PROPOSAL SKRIPSI** (Bab I Pendahuluan, Bab II Tinjauan Pustaka, Bab III Metodologi Penelitian).
2. **Typo Fatal Halaman Judul (Hal. 2 / Dokumen P.2):**
   * Teks di bawah judul tertulis: **`AMAN JUDUL`** (terpotong huruf **`HAL`** dari kata HALAMAN JUDUL).
3. **Placeholder pada Lembar Pengesahan (Hal. 3 / Dokumen P.3):**
   * Tanggal rapat pembimbing masih berupa placeholder: `Telah dibahas dalam Rapat Dosen Pembimbing pada [tgl, bln, tahun]`.
4. **Placeholder & Format Kata Pengantar (Hal. 4 / Dokumen P.4):**
   * Judul proposal diapit spasi berlebih pada tanda petik: `“ Rancang Bangun...”`.
   * Poin 6 dan 7 mencantumkan placeholder: `Bapak ... selaku Penguji I` dan `Bapak ... selaku Penguji II`. (Pada seminar proposal, penguji belum ditetapkan definitif).
   * Titimangsa penulisan masih bertitik-titik: `Samarinda,.............................. 2026`.
5. **Ketiadaan Halaman Abstract Bahasa Inggris:**
   * Hanya tersedia Abstrak Bahasa Indonesia (Hal. 5), tidak memuat lembar *Abstract* Bahasa Inggris.

---

### 🚨 RED FLAG 4: Kerusakan Format Penomoran Halaman Depan & Matriks Daftar Tabel/Gambar/Lampiran

1. **Pelanggaran Penomoran Halaman Awal:**
   * Seluruh halaman preliminer (Halaman Judul s.d. Daftar Singkatan, Hal. 1–10) diberi nomor **angka Arab biasa (1, 2, 3, ... 10)** di pojok kanan atas.
   * **Standar Buku Panduan Skripsi FT Unmul:** Halaman awal wajib menggunakan **angka Romawi kecil (i, ii, iii, iv, v, vi, vii, viii, ix, x)** yang diletakkan di **tengah bawah (*bottom center*)**. Nomor angka Arab (1, 2, 3...) baru dimulai tepat pada **BAB I PENDAHULUAN**.
2. **Daftar Tabel (Hal. 7 / Dokumen P.7):**
   * Terdapat teks duplikat pada header: `halaman 
 DAFTAR TABEL 
 Halaman`.
   * Seluruh entri tabel (Tabel 2.1 s.d. Tabel 3.4) **tidak memiliki nomor halaman**.
3. **Daftar Gambar (Hal. 8 / Dokumen P.8):**
   * Seluruh entri gambar (Gambar 3.1 dan Gambar 3.2) **tidak memiliki nomor halaman**.
4. **Daftar Lampiran (Hal. 9 / Dokumen P.9):**
   * Seluruh entri lampiran (Lampiran 1 s.d. Lampiran 4) **tidak memiliki nomor halaman**.

---

### 🚨 RED FLAG 5: Kerusakan Urutan Alfabetis Daftar Pustaka

Dalam Daftar Pustaka (Hal. 42–43), susunan abjad penulis mengalami kesalahan penempatan:
* Entri `[6] Putra, T. R.` (Huruf **P**) dan `[7] Soebagia, H. S.` (Huruf **S**) diletakkan **SEBELUM** entri `[8] Huang, Y.` (Huruf **H**) dan `[9] Hung, C. L.` (Huruf **H**).
* **Urutan yang Benar:** Entri Huang dan Hung wajib dipindahkan ke posisi setelah Gonzalez (G) dan sebelum Jalaludin (J). Putra dan Soebagia dipindahkan ke posisi P dan S.

---

### 🚨 RED FLAG 6: Tabel 3.4 Jadwal Penelitian Cacat & Sel Matriks Kosong

Tabel 3.4 (Jadwal Penelitian) pada Halaman 41 mengalami cacat total:
1. Kolom kegiatan memuat entri dummy/placeholder:
   * Tahap Persiapan: baris `4. …`
   * Tahap Penyusunan Laporan: baris `6. …`
2. Kolom nomor (*No*) mengalami pengulangan label Romawi `I`, `II`, `III` pada setiap baris kegiatan alih-alih penomoran bertingkat yang rapi.
3. Seluruh sel matriks bulan (Agustus 2026 s.d. Maret 2027) **kosong total** tanpa tanda centang ($\checkmark$), blok warna, atau simbol jadwal kerja.

---

### 🚨 RED FLAG 7: Anomali Struktur Sub-bab Bab II & Penempatan Tabel Komponen

1. **Struktur Sub-bab Bab II yang Rancu:**
   * Sub-bab `2.6 Arsitektur YOLOv5n dan Metrik Evaluasi` memuat `2.6.1 Algoritma YOLOv5n`, `2.6.2 Multi-Object Tracking`, dan `2.6.3 Strategi Penghitungan Berbasis Deteksi per Citra`.
   * Rumus evaluasi (IoU, Precision, Recall, F1-score) diselipkan di dalam sub-bab 2.6.1.
   * Rumus MAE justru dipisah menjadi sub-bab tersendiri `2.7 Mean Absolute Error (MAE)`.
2. **Penempatan Tabel 2.2 yang Salah Konteks:**
   * `Tabel 2.2 Komponen Utama Sistem dan Perannya` (berisi rincian Raspberry Pi, Webcam C270, YOLOv5n, Bot Telegram) diletakkan di dalam sub-bab `2.7 Mean Absolute Error (MAE)` tepat di bawah rumus (2.6). Seharusnya tabel ini berada di Bab III atau di pengantar arsitektur sistem.
3. **Duplikasi Header Baris Tabel 2.2 (Hal. 28):**
   * Baris header `No. | Komponen / Algoritma | Jenis Perangkat/Modul | Fungsi Utama dalam Sistem` tercetak dua kali berturut-turut.

---

### 🚨 RED FLAG 8: Lampiran 1, 2, dan 4 Berupa Template / Teks Instruksi Kosong

* **Lampiran 1 (Surat Pengantar/Izin Penelitian):** Hanya judul lampiran tanpa melampirkan lembar surat izin dari fakultas atau mitra PT Pertamina EP / Balai Tani.
* **Lampiran 2 (Pinout Raspberry Pi 4):** Hanya memuat teks instruksi dalam kurung: `(melampirkan diagram pinout GPIO Raspberry Pi 4...)` tanpa ada gambar skema pinout dan tanpa rincian nomor pin GPIO buzzer.
* **Lampiran 4 (Source Code):** Hanya memuat teks instruksi dalam kurung: `(melampirkan tautan/source code program...)` tanpa ada tautan repositori GitHub atau potongan kode.
* **Halaman 46 (Dokumen P.46):** Halaman kosong dengan nomor halaman 45 yang tertinggal akibat *page break* berlebih.

---

### 🚨 RED FLAG 9: Duplikasi Judul Bab & Masalah Layout (*Hard Page Breaks*)

1. **Pengulangan Judul Bab:**
   * Hal. 12: `BAB I PENDAHULUAN 
 PENDAHULUAN`
   * Hal. 19: `BAB II TINJAUAN PUSTAKA 
 TINJAUAN PUSTAKA`
   * Hal. 31: `BAB III METODOLOGI PENELITIAN 
 METODOLOGI PENELITIAN`
2. **Halaman Bolong Akibat Hard Page Break:**
   * Di file Word (.docx), terdapat *manual page break* di tengah subbab sehingga menghasilkan halaman dengan teks hanya 8–9 baris (Hal. 36 dan Hal. 37) yang menyisakan ruang kosong besar tidak wajar.

---

## 📐 3. Audit Notasi & Formula Matematis (Bab II & III)

Berikut daftar formula matematika yang wajib disempurnakan format dan notasinya:

### 1. Persamaan (2.1) Konvolusi Citra (Hal. 23 / Dokumen P.24)
* **Teks Naskah:** $S(i, j) = (I * K)(i, j) = \sum \sum I(i-m, j-n) \cdot K(m, n)$ (batas indeks sigma tidak tertulis).
* **Perbaikan Wajib:** Tuliskan batas rentang indeks kernel secara formal:
  $$S(i, j) = (I * K)(i, j) = \sum_{m} \sum_{n} I(i - m, j - n) \cdot K(m, n)$$

### 2. Persamaan (2.2) Intersection over Union (IoU) (Hal. 26 / Dokumen P.27)
* **Teks Naskah:** Pecahan tertulis bertumpuk tanpa format rumus yang rapi:
  $$	ext{IoU} = rac{	ext{Area of Overlap}}{	ext{Area of Union}} = rac{B_p \cap B_g}{B_p \cup B_g}$$
* **Perbaikan Wajib:** Gunakan Equation Editor Word standar dengan simbol matematika yang baku.

### 3. Persamaan (2.5) F1-Score (Hal. 26 / Dokumen P.27)
* **Teks Naskah:** Ditulis sebagai teks biasa sebaris tanpa notasi matematika:
  `F1-Score = 2 x (Precision x Recall) / (Precision + Recall)`
* **Perbaikan Wajib:** Format menjadi formula standar:
  $$F_1 = 2 	imes rac{	ext{Precision} 	imes 	ext{Recall}}{	ext{Precision} + 	ext{Recall}}$$

### 4. Formula mAP@0.5 Belum Dicantumkan di Bab II
* **Masalah:** Istilah **mAP@0.5** disebut berulang kali pada Abstrak, Rumusan Masalah, dan Tabel Pengujian (Tabel 3.3), tetapi **tidak ada formula matematis Average Precision (AP) dan mean Average Precision (mAP) di Bab II**.
* **Perbaikan Wajib:** Tambahkan sub-persamaan untuk menghitung AP (luas di bawah kurva Precision-Recall) dan mAP:
  $$AP = \int_{0}^{1} p(r) \, dr \quad 	ext{atau} \quad AP = \sum_{k=1}^{N} (r_k - r_{k-1}) \cdot p_{	ext{interp}}(r_k)$$
  $$mAP = rac{1}{C} \sum_{c=1}^{C} AP_c$$
  *(di mana $C$ adalah jumlah kelas hama, yaitu $C = 3$)*.

### 5. Formula Matematis Agregasi $N_{	ext{jam}}$ & Ambang DANGER Belum Dibuat Persamaan Resmi
* **Masalah:** Pada sub-bab 2.6.3 dan 3.4, perhitungan indeks per jam ($N_{	ext{jam}}$) dan penetapan Ambang batas hanya dijelaskan dalam bentuk kalimat narasi.
* **Perbaikan Wajib:** Buat persamaan matematis bernomor resmi agar memperkuat ketegasan metodologi:
  $$N_{	ext{jam}, c} = rac{1}{K} \sum_{k=1}^{K} D_{k, c}$$
  *(dengan $K = 4$ untuk interval sampling 15 menit dalam 1 jam, dan $D_{k,c}$ adalah jumlah deteksi kelas $c$ pada citra ke-$k$)*.
  $$	ext{Ambang}_c = \mu_{	ext{baseline}, c} + 1 	imes \sigma_{	ext{baseline}, c}$$
  *(di mana $\mu$ adalah rata-rata dan $\sigma$ adalah standar deviasi $N_{	ext{jam}}$ selama 5–7 malam observasi baseline)*.

---

## 🔬 4. Evaluasi Metodologi & Keilmuan Informatika (Edge CV & IoT)

### A. Keunggulan Metodologi yang Sangat Baik (*Strong Points*)
1. **Penolakan Multi-Object Tracking (MOT) yang Rasional (Subbab 2.6.2):**
   Keputusan mahasiswa untuk **TIDAK menggunakan algoritma tracking (seperti ByteTrack/DeepSORT)** pada interval pengambilan foto 15 menit adalah penalaran ilmiah yang **sangat tepat dan jujur**. MOT mensyaratkan kontinuitas temporal *high-frame rate* (10–30 FPS). Pada interval 15 menit, serangga berpindah tempat atau terbang menjauh sehingga *temporal association* pasti gagal.
2. **Strategi Agregasi $N_{	ext{jam}}$:**
   Alih-alih mengklaim penghitungan mutlak individu serangga unik (yang mustahil diverifikasi tanpa video kontinu), mahasiswa memilih metrik rata-rata kepadatan per citra per jam ($N_{	ext{jam}}$). Ini adalah indeks aktivitas yang valid untuk keperluan *early warning system* pertanian.
3. **Pemisahan Dataset Berbasis Malam Pengambilan Data (Tabel 3.2):**
   Membagi train/val/test berdasarkan kelompok malam (Malam 1–4 untuk Train, Malam 5 untuk Val, Malam 6–7 untuk Test) adalah *good practice* yang mencegah **temporal data leakage** (karena foto di malam dan jam yang sama memiliki kondisi pencahayaan dan latar belakang yang identik).

### B. Celah Teknis yang Perlu Diperdalam Sebelum Sidang
1. **Isu Ambigu Jumlah Dataset Lapangan (Tabel 3.2):**
   * Mahasiswa menyebut: *"Target citra: 150-300 citra per kelas"*.
   * Dengan operasional 12 jam (18.00–06.00) @ interval 15 menit = **48 citra per malam**.
   * Total 7 malam = **336 citra mentah**.
   * **Kritisi:** Dalam 336 citra mentah, tidak mungkin langsung didapat 300 citra eksklusif untuk masing-masing kelas tanpa bantuan data sekunder (Kaggle), *tiling*, atau augmentasi. Mahasiswa harus memperjelas perbedaan antara **jumlah frame foto lapangan**, **jumlah patch hasil cropping/tiling**, dan **jumlah instance bounding box**.
2. **Isu Ukuran Hama Mikroskopis (Trips & Kutu Kebul) vs Resolusi Webcam:**
   * Lalat buah berukuran relatif besar ($pprox 7-8	ext{ mm}$), namun **trips** dan **kutu kebul** berukuran sangat kecil ($pprox 1-2	ext{ mm}$).
   * Webcam Logitech C270 memiliki resolusi HD 720p ($1280 	imes 720$). Pada jarak 30–40 cm dari perangkap, objek trips hanya akan berukuran sekitar $5 	imes 5$ hingga $10 	imes 10$ piksel.
   * Model YOLOv5n dengan input standar $640 	imes 640$ piksel akan melakukan downsampling $32	imes$ pada level feature map terdalam (tersisa $20 	imes 20$ piksel), sehingga fitur objek mikro rawan hilang.
   * **Solusi Wajib:** Mahasiswa harus menegaskan penggunaan **Image Tiling / Cropping (SAHI - Slicing Aided Hyper Inference)** tidak hanya saat anotasi data di Roboflow, tetapi juga menjelaskan skema pemrosesan *patch* saat inferensi di Raspberry Pi.
3. **Karakteristik Cahaya UV & Kamera Malam Hari:**
   * Lampu UV 15 Watt dapat memancarkan pendaran biru-keunguan kuat yang menimbulkan *glare* dan *color distortion* pada sensor CMOS Logitech C270.
   * Mahasiswa sudah merencanakan sudut kamera menyamping dan opsi lampu bantu Inframerah (IR). Hal ini perlu digambarkan dalam **diagram tata letak fisik perangkap (*physical hardware layout*)** di Bab III.
4. **Benchmark Latensi Ekspor Model (PyTorch vs ONNX vs NCNN INT8):**
   * Di Bab III disebutkan rencana ekspor ke ONNX / NCNN INT8.
   * Mahasiswa perlu menambahkan estimasi beban komputasi: karena sistem hanya mengambil citra sekali per 15 menit ($900	ext{ detik}$), latensi inferensi $2-4	ext{ detik}$ pada PyTorch CPU Raspberry Pi 4 sebenarnya sudah sangat cukup tanpa membebani sistem. Namun konversi NCNN INT8 tetap sangat bernilai untuk efisiensi konsumsi daya (*power consumption*) dan menjaga suhu CPU tetap dingin.

---

## 🎯 5. Panduan Kesiapan Menghadapi Dewan Penguji Seminar Proposal

Berikut adalah 6 pertanyaan kritis yang hampir pasti akan diajukan oleh dosen penguji seminar proposal beserta strategi argumentasi ilmiahnya:

### Q1: *"Mengapa Anda tidak menggunakan algoritma tracking seperti DeepSORT atau ByteTrack untuk mencegah double-counting serangga yang diam di perangkap?"*
* **Strategi Jawaban Mahasiswa:**
  > *"Algoritma MOT (seperti ByteTrack atau DeepSORT) bekerja berdasarkan asumsi kontinuitas gerak antar-frame yang rapat (milidetik/frame rate video). Pada sistem kami, pengambilan citra dilakukan secara berkala setiap 15 menit untuk efisiensi daya komputasi edge. Dalam jeda 15 menit, serangga dapat bergerak acak, terbang, atau bertambah banyak sehingga estimasi posisi Kalman Filter dan Hungarian Matching kehilangan korelasi spasialnya. Oleh karena itu, kami menerapkan strategi agregasi rata-rata deteksi per citra dalam satu jam ($N_{	ext{jam}}$) sebagai representasi indeks intensitas serangan hama yang lebih jujur dan valid."*

### Q2: *"Hama trips dan kutu kebul berukuran sangat kecil (1-2 mm). Bagaimana memastikan model YOLOv5n pada webcam 720p mampu mendeteksinya tanpa banyak False Negative?"*
* **Strategi Jawaban Mahasiswa:**
  > *"Kami menerapkan tiga strategi: Pertama, kamera diposisikan sangat dekat dengan permukaan tangkapan (30–40 cm) dengan pencahayaan samping untuk memaksimalkan kontras visual. Kedua, kami menerapkan teknik image tiling/slicing saat persiapan dataset dan inferensi agar resolusi piksel objek kecil tetap terjaga saat masuk ke arsitektur jaringan. Ketiga, arsitektur YOLOv5n memanfaatkan PANet (Path Aggregation Network) pada bagian neck yang mengalirkan fitur resolusi tinggi dari layer awal ke layer deteksi untuk mengenali objek berukuran kecil."*

### Q3: *"Mengapa Ambang DANGER ditetapkan berdasarkan rata-rata baseline + 1 SD (mean + 1×SD), bukan mengacu langsung pada Ambang Ekonomi (AE) Kementerian Pertanian?"*
* **Strategi Jawaban Mahasiswa:**
  > *"Ambang Ekonomi resmi dari Kementerian Pertanian dinyatakan dalam satuan kepadatan populasi per luas lahan (misalnya 40 perangkap kuning per hektare). Satuan tersebut tidak dapat dikonversikan secara langsung ke jumlah tangkapan pada satu unit perangkap cahaya statis per jam. Oleh sebab itu, kami menggunakan pendekatan baseline adaptif lapangan: 5–7 malam pertama digunakan untuk memetakan fluktuasi normal ($	ext{mean} \pm 	ext{SD}$). Nilai di atas $	ext{mean} + 1	ext{SD}$ menandakan anomali lonjakan populasi hama yang signifikan secara statistik pada lokasi tersebut sehingga memicu status DANGER."*

### Q4: *"Bagaimana keandalan sistem jika koneksi WiFi di kebun mati atau listrik mengalami pemadaman di malam hari?"*
* **Strategi Jawaban Mahasiswa:**
  > *"Untuk suplai daya, sistem menggunakan sumber listrik utama Balai Tani dengan backup power bank berkapasitas besar. Untuk jaringan, sistem dirancang dengan skema local caching/buffering: apabila koneksi WiFi terputus, data hasil inferensi dan timestamp tetap tersimpan di penyimpanan lokal Raspberry Pi dalam format log CSV/JSON. Begitu konektivitas internet pulih, sistem secara otomatis mengeksekusi sinkronisasi dan mengirimkan notifikasi rekapitulasi susulan ke Bot Telegram (diuji pada skenario U5)."*

### Q5: *"Mengapa memilih YOLOv5n dibandingkan versi yang lebih baru seperti YOLOv8n, YOLOv10n, atau YOLOv11n?"*
* **Strategi Jawaban Mahasiswa:**
  > *"YOLOv5n memiliki stabilitas dependensi pustaka yang sangat matang pada sistem operasi Raspberry Pi OS ARMv8 (kompatibilitas PyTorch dan NCNN tanpa konflik driver), dengan ukuran model yang sangat ringan ($pprox 3,9	ext{ MB}$). Karena sistem beroperasi pada mode sampling 15 menit, YOLOv5n memberikan keseimbangan optimal antara konsumsi memori, stabilitas suhu operasional, dan performa deteksi tanpa memerlukan akselerator GPU eksternal."*

### Q6: *"Bagaimana mekanisme bot Telegram menerima perintah pengguna (/photo, /alarm) sementara Raspberry Pi sedang dalam siklus inferensi berkala?"*
* **Strategi Jawaban Mahasiswa:**
  > *"Program Python di Raspberry Pi dirancang menggunakan arsitektur multithreading/asynchronous (asyncio / python-telegram-bot). Thread utama menjalankan penjadwalan akuisisi dan inferensi 15 menitan, sedangkan thread kedua menjalankan event-listener Bot Telegram secara non-blocking sehingga perintah manual pengguna tetap dapat direspons secara instan tanpa mengganggu proses deteksi."*

---

## 📋 6. Matriks Action Plan & Checklist Revisi Mahasiswa

Mahasiswa wajib menyelesaikan poin-poin perbaikan berikut sebelum naskah disetujui untuk penjadwalan Seminar Proposal:

```markdown
- [ ] 1. Pembersihan & Perbaikan Sitasi (PRIORITAS UTAMA):
      - Hapus referensi fiktif: Khalid dkk. (2026) dan Zarboubi dkk. (2026).
      - Perbaiki metadata DOI Zarboubi (2024) dan Huang (2025).
      - Susun ulang abjad Daftar Pustaka (Huang & Hung sebelum Jalaludin, Putra & Soebagia di P & S).
      - Sinkronkan seluruh sitasi Bab II dan Daftar Pustaka menggunakan Mendeley/Zotero.
- [ ] 2. Margin & Tata Letak Dokumen (Standar FT Unmul):
      - Atur margin dokumen: Atas = 4 cm, Kiri = 4 cm, Bawah = 3 cm, Kanan = 3 cm.
      - Seragamkan line spacing menjadi 1.5 spasi untuk badan teks.
- [ ] 3. Halaman Formalia & Tata Tulis Depan:
      - Perbaiki nama file menjadi PROPOSAL_SKRIPSI_Muhammad_Annur_Akbar.
      - Perbaiki typo Halaman Judul: "AMAN JUDUL" -> "HALAMAN JUDUL".
      - Ganti penomoran halaman awal (Cover s.d. Singkatan) menjadi Romawi kecil (i, ii, iii... x) di tengah bawah.
      - Isi nomor halaman pada Daftar Tabel, Daftar Gambar, dan Daftar Lampiran.
      - Hapus teks duplikat header pada Daftar Tabel ("halaman DAFTAR TABEL Halaman").
      - Rapikan Lembar Pengesahan dan Kata Pengantar (hapus placeholder [...]).
- [ ] 4. Perbaikan Notasi, Rumus Matematis & Sub-bab Bab II:
      - Tuliskan batas sigma pada rumus Konvolusi (2.1).
      - Format rapi rumus IoU (2.2) dan F1-Score (2.5).
      - Tambahkan persamaan mAP@0.5, formula N_jam, dan formula Ambang DANGER di Bab II.
      - Pindahkan Tabel 2.2 Komponen Sistem dari sub-bab MAE ke lokasi yang sesuai dan hapus duplikasi baris header.
- [ ] 5. Penyempurnaan Bab III & Tabel Jadwal:
      - Hapus duplikasi judul bab (BAB I, BAB II, BAB III).
      - Lengkapi Tabel 3.4 Jadwal Penelitian: hapus baris placeholder (4. ..., 6. ...) dan beri arsiran timeline bulan.
      - Rapikan manual page break agar tidak ada halaman kosong/bolong (Hal. 36-37).
      - Perjelas rincian dataset: citra mentah (336 foto) vs patch tiling vs instance label.
- [ ] 6. Kelengkapan Lembar Lampiran:
      - Lampiran 1: Masukkan draf/foto surat pengantar izin penelitian.
      - Lampiran 2: Masukkan diagram skema wiring/pinout GPIO Raspberry Pi 4 dan nomor pin buzzer.
      - Lampiran 4: Cantumkan tautan repositori kode / struktur folder modul program.
      - Hapus halaman kosong berlebih di akhir dokumen.
```

---
*Laporan audit akademik komprehensif ini disusun oleh Tim Pembimbing untuk memastikan 100% kesiapan substansi, integritas ilmiah, dan kepatuhan tata tulis naskah proposal skripsi Muhammad Annur Akbar menuju Ujian Seminar Proposal.*
