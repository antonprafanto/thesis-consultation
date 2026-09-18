# 📋 LAPORAN AUDIT HASIL REVISI DRAF SKRIPSI PENDADARAN (PDD)

**Mahasiswa:** Vista Mellyna Atsfi (NIM: 2209106096)  
**Program Studi:** S1 Informatika, Fakultas Teknik, Universitas Mulawarman  
**Dosen Pembimbing I:** Anton Prafanto, S.Kom., M.T.  
**Dosen Pembimbing II:** Ir. Novianti Puspitasari, S.Kom., M.Eng.  
**Dosen Penguji I:** Prof. Dr. Anindita Septiarini, S.T., M.Cs.  
**Dosen Penguji II:** Andi Tejawati, S.Kom., M.Si., M.Kom.  
**Judul Skripsi:** *Sistem Pengelolaan Data Praktikan dengan Algoritma Merge Sort dan Sequential Search Berbasis Web*  
**Berkas yang Diaudit:** `Draft Skripsi Vista Mellyna Atsfi 2209106096_PDD.pdf` (144 Halaman)  
**Status Evaluasi:** ⚠️ **PERLU PENYEMPURNAAN AKHIR PRA-JILID (ADA BEBERAPA REVISI KRUSIAL YANG BELUM TUNTAS / RUSAK FORMAT)**

---

> [!NOTE]
> **Petunjuk Mahasiswa:** Dokumen ini merupakan hasil audit menyeluruh terhadap naskah revisi skripsi yang kamu serahkan. Laporan ini mengevaluasi kesesuaian naskah terhadap **Catatan Revisi Penguji & Pembimbing** (lembar revisi ujian) serta menyajikan panduan perbaikan konkret langkah demi langkah agar skripsimu siap ditandatangani dan dijilid final secara profesional.

---

## 📊 1. Matriks Evaluasi Pemenuhan Catatan Revisi Dosen

Berikut adalah status verifikasi naskah revisi terhadap catatan perbaikan masing-masing penguji dan pembimbing:

| Dosen Pembimbing / Penguji | Bagian | Catatan Revisi Asli | Status Verifikasi | Ringkasan Fakta Hasil Audit |
| :--- | :--- | :--- | :---: | :--- |
| **Prof. Anindita**<br>*(Penguji 1)* | **BAB III** | Perbaiki DFD Level 2 | ⚠️ **Perlu Dibenahi** | Diagram DFD Level 2 (Gambar 3.5, 3.6, 3.7) masih memuat anomali struktural: entitas luar digambar ulang di bagian bawah, proses login dijadikan subproses DFD, nama data store sama persis dengan entitas luar, dan notasi data store melayang. |
| **Bu Andi**<br>*(Penguji 2)* | **Saran** | Lebih spesifik berapa dataset yang disarankan untuk penelitian selanjutnya | ⚠️ **Belum Tuntas** | Di naskah baru ditambahkan angka tunggal ("10.000 entri"). Belum mencakup rentang pengujian bertingkat skala besar (misal 10k, 25k, 50k, 100k) dan urgensi pengujian titik batas memori (*memory exhaustion*). |
| **Pak Anton**<br>*(Pembimbing 1)* | **BAB III** | Perbaiki resolusi gambar supaya terlihat lebih jelas, 800 Dpi | ❌ **Belum Terpenuhi** | Gambar wireframe dan diagram di Bab III resolusinya masih setara *screenshot* layar biasa (72–150 DPI / 400–700 px), sehingga masih tampak pecah/kabur jika dicetak pada dokumen fisik A4. |
| **Pak Anton**<br>*(Pembimbing 1)* | **Lampiran** | Tambahkan link GitHub di lampiran | 🚨 **KRITIS (ERROR 404)** | Link telah dicantumkan di Lampiran 1 (`https://github.com/VistaAtsfi/praktikum-fisdas`), tetapi saat diakses menghasilkan **HTTP 404 Not Found** karena repositori masih berstatus **Private** atau ada salah ketik link. |
| **Bu Novi**<br>*(Pembimbing 2)* | **BAB III** | Perbaiki caption urutan gambar | ⚠️ **Perlu Dibenahi** | Peletakan gambar mendahului narasi perujuk (misal Gambar 3.4, Gambar 3.5, dan Gambar 3.8). Flowchart Gambar 3.8 dan 3.9 terbelah tidak rapi di tengah penjelasan teks. |
| **Bu Novi**<br>*(Pembimbing 2)* | **BAB IV** | Perbaiki caption urutan gambar | ⚠️ **Perlu Dibenahi** | Di Daftar Gambar terdapat judul ganda identik (Gambar 4.7 & 4.8 sama-sama tertulis *Halaman Materi Praktikum*). Pada Bab IV hal 82–86, gambar terlempar ke halaman berikutnya mendahului narasi atau kalimat terpotong halaman. |
| **Bu Novi**<br>*(Pembimbing 2)* | **BAB IV** | Ubah grafik batang di Perbandingan Penggunaan Memori menjadi grafik lain agar Sequential Search dan warnanya hijau terlihat | ⚠️ **Sebagian (Visual Kurang Efektif)** | Grafik sudah diubah menjadi grafik garis dan warnanya hijau (Gambar 4.31). Namun, karena menggunakan skala linear biasa (0–4.000 KB), garis hijau Sequential Search menempel rapat di garis dasar sumbu X (nilai ~0) sehingga tetap tidak terlihat variasinya. Gambar juga masih berupa *screenshot UI web* dengan tombol kontrol. |
| **Bu Novi**<br>*(Pembimbing 2)* | **Daftar Pustaka** | Perbaiki menjadi rata kanan kiri | 🚨 **RUSAK PARAH (LAYOUT BROKEN)** | Mahasiswa menerapkan Justify tanpa merapikan *hard line-break* sehingga spasi antarkata renggang ekstrim (Ref 5 & 6), beberapa referensi pecah menjadi satu kata per baris (Ref 24 & 26), ada URL ganda `https://doi.org/https://doi.org/`, dan Ref 28 terpotong halaman. |
| **Bu Novi**<br>*(Pembimbing 2)* | **Saran** | Perbaiki menjadi rata kanan kiri | ⚠️ **Format Rusak** | Paragraf di bawah poin 2 kehilangan nomor (seharusnya menjadi poin 3), format indentasinya tidak seragam, dan alignment kanan-kiri belum konsisten. |

---

## 🔍 2. Bedah Rinci Poin Catatan Revisi & Panduan Perbaikan

### 1. [Prof. Anindita] Perbaikan DFD Level 2 (Bab III, Hal. 33–35 / PDF Hal. 55–57)

Penguji sistem dan pemodelan perangkat lunak sangat teliti terhadap kaidah baku Data Flow Diagram (DFD). Saat ini terdapat beberapa kesalahan fundamental pada DFD Level 2 kamu:

1. **Gambar 3.5 (DFD Level 2 Proses 1: Kelola Data Praktikum):**
   * **Masalah:** Di bagian atas diagram terdapat entitas luar `PRAKTIKAN`, `KOORDINATOR PRAKTIKUM`, dan `ASISTEN`. Namun di bagian bawah diagram, kamu menggambar kotak `PRAKTIKAN` dan `ASISTEN` kembali. Dalam kaidah DFD, entitas eksternal yang sama tidak boleh digambar berulang secara sembarangan tanpa notasi duplikasi (garis miring di sudut kiri atas).
   * **Solusi:** Satukan entitas eksternal atau hubungkan alur data dari/ke entitas yang berada di bagian atas. Aliran data keluar dari proses 1.2 (`INFO_KELOMPOK`) dan 1.3 (`INFO_MATERI`) ditarik kembali ke entitas `PRAKTIKAN` dan `ASISTEN` yang ada di atas.
2. **Gambar 3.6 (DFD Level 2 Proses 2: Kelola Data Praktikan & Asisten):**
   * **Masalah 1 (Proses Login):** Terdapat subproses `2.5 Masuk dengan Akun`. Dalam DFD murni, **Login / Autentikasi bukanlah proses transformasi data**, melainkan kontrol alur sistem.
   * **Masalah 2 (Nama Data Store = Nama Entitas):** Kamu menamai penyimpanan data dengan nama `PRAKTIKAN`, `KOOR_PRAKTIKUM`, dan `ASISTEN`. Nama ini identik dengan nama entitas pengguna di luar sistem, sehingga membingungkan mana manusia (aktor) dan mana tabel basis data.
   * **Solusi:** Ubah nama penyimpanan data menjadi nama tabel relasional yang representatif, misalnya `tb_user`, `tb_praktikan`, `tb_asisten`. Alihkan proses pengecekan akun ke dalam proses pengelolaan profil/data pengguna.
3. **Gambar 3.7 (DFD Level 2 Proses 3: Kelola Data Penilaian):**
   * **Masalah:** Tepat di atas Subproses 3.3 (`Melihat Nilai`), terdapat simbol dua garis horizontal bertuliskan `ASISTEN` yang melayang canggung. Selain itu, pada DFD Level 1 (Gambar 3.4), Proses 3.0 hanya menyimpan ke data store `PENILAIAN` dan `NILAI`. Di DFD Level 2 ini tiba-tiba muncul data store `PRAKTIKAN`. Ini melanggar kaidah *Balancing DFD* (keseimbangan data store antara Level 1 dan Level 2).
   * **Solusi:** Rapikan simbol penyimpanan data `ASISTEN` yang melayang. Pastikan relasi data store antara DFD Level 1 dan Level 2 konsisten.

---

### 2. [Bu Andi] Spesifikasi Dataset untuk Penelitian Selanjutnya (Bab V, Hal. 108–109)

* **Kelemahan Saat Ini:**  
  Kamu hanya menuliskan: *"1. Penelitian selanjutnya dapat menggunakan dataset 10.000 entri agar pola skalabilitas Merge Sort, Sequential Search, dan baseline MySQL dapat diamati..."*  
  Kalimat ini terlalu singkat dan hanya menyebut satu angka statis (10.000), padahal penelitianmu sudah menguji rentang 100, 500, 1.000, hingga 5.000 data.
* **Perbaikan Teks yang Disarankan (Tinggal Disalin dan Disesuaikan):**
  > **1.** Penelitian selanjutnya disarankan untuk memperluas pengujian performa menggunakan variasi dataset skala besar secara bertingkat dan spesifik, seperti **10.000, 25.000, 50.000, hingga 100.000 data entri**. Rentang pengujian yang lebih luas ini diperlukan untuk mengamati secara nyata titik infleksi (*divergence point*) penurunan performa algoritma $O(N \log N)$ pada Merge Sort dan $O(N)$ pada Sequential Search, serta mendeteksi ambang batas kehabisan alokasi memori (*memory exhaustion threshold*) pada server berbasis PHP/Laravel sebelum sistem mengalami kegagalan proses (*fatal error*).

---

### 3. [Pak Anton] Resolusi Gambar 800 DPI & Link GitHub di Lampiran

#### A. Resolusi Gambar Bab III (Wireframe & Diagram)
* **Fakta Temuan:**  
  Ukuran pixel gambar rancangan antarmuka (Gambar 3.12 s.d. 3.17) masih sangat kecil, yaitu antara **429×434 px** hingga **737×423 px**. Pada dokumen fisik ukuran A4, resolusi ini hanya setara **72–150 DPI**. Akibatnya, tulisan pada wireframe dan alur diagram terlihat kabur (*blur*) atau berbintik saat dicetak.
* **Langkah Konkret Perbaikan:**
  1. Jika menggunakan **Figma**: Pilih frame wireframe -> Pada panel *Export* di kanan bawah, ubah skala dari `1x` menjadi `3x` atau `4x` (format PNG), atau ekspor ke format **PDF/SVG** lalu konversi ke PNG resolusi tinggi.
  2. Jika menggunakan **Draw.io / Lucidchart**: Pilih menu *File* -> *Export as* -> *PNG* -> Centang opsi *Transparent Background* dan atur *Zoom / DPI* ke minimal **300% atau 800 DPI**.
  3. Masukkan ulang gambar beresolusi tinggi tersebut ke dokumen skripsi tanpa mengubah proporsi aspek (*aspect ratio*).

#### B. Link GitHub Repositori (Lampiran 1 Hal. 115 / PDF Hal. 137)
* **🚨 Masalah Kritis:**  
  Saat tautan `https://github.com/VistaAtsfi/praktikum-fisdas` dibuka di browser, GitHub menampilkan pesan:  
  **`HTTP 404 - Page Not Found`**  
  Hal ini terjadi karena repository kamu saat ini masih berstatus **PRIVATE** (rahasia), sehingga orang lain/dosen penguji tidak bisa mengaksesnya.
* **Langkah Konkret Perbaikan:**
  1. Masuk ke akun GitHub kamu (`VistaAtsfi`).
  2. Buka repository `praktikum-fisdas`.
  3. Klik menu **Settings** (ikon gerigi di atas).
  4. Gulir ke bagian paling bawah ke kotak merah (**Danger Zone**).
  5. Pada opsi **Change repository visibility**, klik tombol **Change to public**.
  6. Masukkan konfirmasi nama repository sesuai instruksi GitHub.
  7. Uji kembali dengan membuka tautan tersebut menggunakan mode *Incognito/Private Window* browser. Pastikan repositori dapat terbuka tanpa login.
  8. Di naskah Lampiran 1, buat tautan tersebut aktif (*hyperlink biru*) dan lengkapi dengan keterangan singkat:
     ```text
     Lampiran 1: Repositori Kode Sumber Sistem Praktikum Fisika Dasar
     Tautan Repositori GitHub: https://github.com/VistaAtsfi/praktikum-fisdas
     Keterangan: Memuat kode sumber aplikasi Laravel 10, implementasi algoritma Merge Sort dan Sequential Search, database migration, seeder data pengujian, serta perintah pengujian otomatis (Artisan Command).
     ```

---

### 4. [Bu Novi] Caption Gambar, Grafik Penggunaan Memori, Rata Kanan-Kiri

#### A. Urutan Penempatan Teks dan Gambar (Bab III & Bab IV)
* **Kaidah Baku Penulisan Ilmiah:**  
  1. **Narasi teks yang merujuk gambar WAJIB mendahului gambar**, BUKAN gambar muncul duluan baru dijelaskan di bawahnya atau di halaman berikutnya.
  2. **Caption gambar WAJIB diletakkan tepat di bawah gambar**, berjarak 1 spasi tunggal, dan tidak boleh terpisah ke halaman berikutnya (*orphan caption*).
* **Temuan Khusus Bab III:**
  * Gambar 3.4 (DFD Level 1) berada di bawah hal 32, tetapi teks penjelasnya baru muncul di hal 33.
  * Gambar 3.8 (Flowchart Masuk hal 35) terpotong di bagian bawah, sedangkan teks penjelasnya berada di hal 36.
* **Temuan Khusus Bab IV:**
  * **Duplikasi di Daftar Gambar (Hal. xii):**  
    `Gambar 4.7 Halaman Materi Praktikum Praktikan ........................................................ 77`  
    `Gambar 4.8 Halaman Materi Praktikum Praktikan ........................................................ 77`  
    *(Koreksi Daftar Gambar agar Gambar 4.7 tertulis: **Halaman Beranda Praktikan** sesuai isi Bab IV hal 91).*
  * **Teks & Gambar Terlempar (Hal. 82–86):**  
    Paragraf pengantar Gambar 4.19 berada di dasar hal 82, tapi gambarnya baru muncul di puncak hal 83. Begitu pula Gambar 4.21. Kalimat di hal 85 terpotong di tengah jalan (*"...status kehadiran, [pindah halaman] kelompok, dan sesi praktikum"*). Atur *line-spacing* atau *page break* agar gambar dan kalimat pengantarnya tetap menyatu secara elegan.

#### B. Grafik Perbandingan Penggunaan Memori (Gambar 4.31 Hal. 100 / PDF Hal. 122)
* **Kelemahan Visual Saat Ini:**  
  Kamu sudah mengubah grafik batang menjadi grafik garis dan memberi warna hijau pada Sequential Search. Namun:
  1. Gambar yang dimasukkan masih berupa **screenshot antarmuka web** yang memuat tombol kontrol sistem: `[Semua Metode]`, `[Sorting]`, `[Searching]`, `[Skala Logaritmik: Nonaktif]`.
  2. Karena skala sumbu Y yang digunakan adalah **skala linear biasa (0 s.d. 4.000 KB)**, nilai memori Sequential Search yang sangat kecil (~2 s.d. 5 KB) **tenggelam dan menempel rata pada garis nol (sumbu X)**. Warna hijau tersebut terhimpit garis bawah sehingga perubahannya tetap tidak tampak!
* **Solusi Perbaikan:**
  1. **Aktifkan Skala Logaritmik (*Logarithmic Scale*)** pada dashboard web tersebut, lalu ambil tangkapan grafik tanpa tombol kontrol (potong/crop tombol filternya agar bersih sebagai gambar laporan ilmiah). Dengan skala logaritmik, kurva Sequential Search (~5 KB), Merge Sort (~300 KB), MySQL WHERE (~1.000 KB), dan MySQL ORDER BY (~3.800 KB) akan terpisah jelas dengan proporsi yang estetis!
  2. Atau buat grafik tersendiri di Excel / Matplotlib / Python khusus perbandingan memori metode *Searching* (Sequential Search vs MySQL WHERE) agar rentang skala sumbu Y fokus pada 0 s.d. 1.200 KB.

#### C. Format Rata Kanan-Kiri Daftar Pustaka (Hal. 110–114 / PDF Hal. 132–136)
Ini adalah bagian dengan **kesalahan tata letak paling fatal** pada draf revisi ini. Ketika kamu melakukan *Justify*, teks menjadi rusak karena adanya karakter enter / pemisah baris manual:

1. **Spasi Menganga Ekstrim (*Stretched Whitespace*):**
   * Referensi no. 5: `Informasi),                    16(120),                           32–45.`
   * Referensi no. 6: `Engineering,       System        and         Science),      7,          106–115.`
2. **Pecah Satu Kata per Baris (*Broken Lines*):**
   * Referensi no. 24: Kata `Jurnal`, `Komputer,`, `Informasi`, `Dan`, `Teknologi,` masing-masing menempati baris baru sendiri!
   * Referensi no. 26 (Sahar, Y.): Setiap kata judul naskah dicetak per baris secara vertikal!
3. **Referensi Terpotong Halaman Tanpa Indentasi:**
   * Referensi no. 28 (Saputra & Kusniyati) terpotong di dasar halaman 113 dan menyambung di halaman 114 tanpa format gantung (*hanging indent*).
4. **Kesalahan Penulisan URL / DOI:**
   * Terdapat awalan ganda pada banyak nomor: `https://doi.org/https://doi.org/...` (hapus salah satu awalan `https://doi.org/`).
   * Referensi no. 32: Tertulis `https://doi.org/https://github.com/...` (URL GitHub tidak boleh diawali dengan `https://doi.org/`).
5. **Huruf Kapital Semua (*ALL CAPS*):**
   * Referensi no. 33 (Wiguna, 2020) judulnya masih ditulis huruf kapital seluruhnya. Ubah menjadi *Sentence case*.

> [!TIP]
> **Cara Memperbaiki Daftar Pustaka di MS Word dalam 5 Menit:**
> 1. Blok seluruh isi Daftar Pustaka.
> 2. Tekan `Ctrl + H` (Find and Replace): Pada kolom *Find what* ketik `^l` (manual line break) atau `^p` (paragraph break yang salah tempat), ganti dengan spasi tunggal.
> 3. Pastikan setiap satu judul referensi berada dalam **satu paragraf utuh**.
> 4. Atur format paragraf: *Alignment* = **Justified**, *Special Indentation* = **Hanging** sebesar **1,27 cm (0,5 inci)**, *Line Spacing* = **1,15** atau **1,5**, dan *After Spacing* = **6 pt**.

#### D. Format Rata Kanan-Kiri & Penomoran Bagian Saran (Bab V Hal. 109)
* **Masalah:** Di bawah poin 2, terdapat paragraf:  
  *"Pengembangan sistem selanjutnya dapat menambahkan perbandingan dengan algoritma pengurutan dan pencarian lain. Penelitian berikutnya juga dapat melakukan pengujian keamanan, beban, dan ketahanan sistem..."*  
  Paragraf ini tidak memiliki nomor dan format indentasinya rata kiri biasa, sehingga tampak terlepas dari poin 1 dan 2.
* **Solusi:** Jadikan paragraf tersebut sebagai **Poin 3** dan **Poin 4** yang rapi dan terindentasi sejajar dengan poin sebelumnya:
  > **3.** Pengembangan sistem selanjutnya dapat menambahkan perbandingan dengan algoritma pengurutan lain (seperti Quick Sort) dan algoritma pencarian lain (seperti Binary Search) untuk memperkaya analisis efisiensi pada sistem informasi berbasis web.  
  > **4.** Penelitian berikutnya disarankan untuk melakukan pengujian keamanan (*security testing*), pengujian beban (*load testing*), dan pengujian ketahanan (*stress testing*) agar kesiapan sistem sebelum diterapkan pada skala operasional riil dapat dipastikan.

---

## 📌 3. Audit Temuan Kritis Tambahan (Wajib Diperbaiki Sebelum Jilid Final)

Selain catatan di atas, terdapat beberapa kekeliruan fatal pada halaman depan (*front matter*) yang belum kamu koreksi:

1. **Halaman Pengesahan (Halaman iii / PDF Hal. 4):**
   * Masih tertulis:  
     *"Telah diujikan pada **tgl bln thn** dan dinyatakan telah memenuhi syarat"*  
     *"Samarinda, **Tanggal Bulan Tahun**"*
   * ⚠️ **Wajib diisi tanggal pelaksanaan sidang pendadaran yang sebenarnya!**
2. **Kata Pengantar (Halaman vii / PDF Hal. 8):**
   * Pada paragraf 1 masih tertulis:  
     *"...sehingga dapat menyelesaikan **proposal skripsi** dengan judul..."* dan  
     *"...**Proposal** ini disusun sebagai salah satu tahapan dalam menyelesaikan skripsi..."*
   * ⚠️ **Wajib diganti menjadi "skripsi"!** Ini adalah naskah skripsi sidang pendadaran, bukan lagi seminar proposal.
3. **Abstrak & Abstract (Halaman v & vi / PDF Hal. 6 & 7):**
   * Terdapat teks anomali: `1 ABSTRAK` pada halaman v dan `2 ABSTRACT` pada halaman vi.
   * ⚠️ Hapus angka "1" dan "2" tersebut karena itu adalah penomoran heading yang tidak sengaja terbuat.
4. **Daftar Kode (Halaman xiv / PDF Hal. 15):**
   * Terdapat judul yang duplikat persis:
     * `Source Code 4.5 Pemetaan Metode Pengujian` dan `Source Code 4.6 Pemetaan Metode Pengujian` (halaman sama: 69).
     * `Source Code 4.8 Penyimpanan Log Hasil Pengujian` dan `Source Code 4.9 Penyimpanan Log Hasil Pengujian`.
   * Periksa kembali label source code di Bab IV agar judulnya mencerminkan fungsi kode yang spesifik.

---

## ✅ 4. Action Checklist Mahasiswa Menuju Jilid Final

Gunakan checklist ini untuk memeriksa dokumenmu sebelum diserahkan kembali kepada Dosen Pembimbing:

- [ ] **1. Tautan GitHub Lampiran 1:** Ubah visibility repositori `VistaAtsfi/praktikum-fisdas` menjadi **Public** di GitHub dan pastikan tidak lagi 404.
- [ ] **2. Daftar Pustaka:** Hapus seluruh enter manual di dalam entri referensi, terapkan *Hanging Indent* (Justified), hilangkan awalan ganda `https://doi.org/https://doi.org/`, dan ubah judul ALL CAPS di Ref 33 menjadi Sentence case.
- [ ] **3. Halaman Pengesahan & Kata Pengantar:** Isi tanggal ujian asli (ganti placeholder `tgl bln thn`) dan ganti kata `proposal skripsi` menjadi `skripsi` pada Kata Pengantar.
- [ ] **4. Hapus Teks Anomali Abstrak:** Hapus angka `1` pada `1 ABSTRAK` dan angka `2` pada `2 ABSTRACT`.
- [ ] **5. Singkronisasi Daftar Gambar & Bab IV:** Perbaiki judul Gambar 4.7 di Daftar Gambar menjadi *Halaman Beranda Praktikan* dan rapikan letak Gambar 4.19, 4.21, 4.25 agar menyatu dengan kalimat pengantarnya.
- [ ] **6. Gambar 4.31 (Grafik Memori):** Ekspor grafik dengan mengaktifkan *Skala Logaritmik* dan potong tombol kontrol web agar kurva hijau Sequential Search terlihat jelas dan profesional.
- [ ] **7. Poin Saran Bab V:** Perjelas rentang dataset menjadi bertingkat (10.000 s.d. 100.000 data) dan rapikan penomoran poin 1 s.d. 4 secara konsisten.
- [ ] **8. DFD Level 2 Bab III:** Satukan entitas eksternal yang terduplikasi di bagian bawah Gambar 3.5, hilangkan proses login di DFD Gambar 3.6, dan rapikan data store melayang di Gambar 3.7.
- [ ] **9. Resolusi Gambar Bab III:** Ekspor ulang wireframe dan flowchart dengan resolusi tinggi (minimal 300–800 DPI) agar tidak pecah saat dicetak.

---
*Laporan audit disusun secara komprehensif oleh Tim Pembimbing Skripsi untuk kelancaran penyelesaian skripsi Vista Mellyna Atsfi (2209106096).*
