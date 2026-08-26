# 📋 LAPORAN AUDIT KOMPREHENSIF & PANDUAN REVISI PROPOSAL SKRIPSI

**Kepada Mahasiswa:** Aji Pangestu (NIM: 2009106134)  
**Program Studi:** S1 Informatika, Fakultas Teknik, Universitas Mulawarman  
**Dosen Pembimbing I:** Anton Prafanto, S.Kom., M.T.  
**Dosen Pembimbing II:** Medi Taruk, S.Kom., M.Cs.  
**Judul Proposal:** *Analisis Search Engine Optimization (SEO) pada Website Lintasjejaring.com*  
**Tanggal Evaluasi:** 26 Agustus 2026  
**Status Naskah:** **Diterima dengan Catatan Revisi (Wajib Diperbaiki Sebelum Seminar Proposal)**

---

## 🌟 1. Apresiasi & Kekuatan Naskah

Secara umum, naskah proposal skripsi Aji Pangestu telah disusun dengan struktur yang **sangat baik, komprehensif, dan matang secara metodologis**:
1. **Perancangan Data Sangat Detail (Tabel 3.2):** Memetakan 27 indikator teknis on-page dan data pendukung off-page secara terstruktur lengkap dengan sumber tools, satuan, dan standar acuannya.
2. **Sistem Penilaian (Scoring System) Terukur:** Formula kuantitatif 5 kategori pembobotan (*Indexability, Metadata, Core Web Vitals, Content Quality, Visibility & Engagement*) dan klasifikasi *SEO Health* (0–100) memberikan kontribusi metodologis yang kokoh untuk skripsi S1 Informatika.
3. **Matriks Analisis Gap Penelitian (Tabel 2.2) Sangat Tajam:** Membedah 9 dimensi perbedaan penelitian terdahulu versus fokus penelitian saat ini.
4. **Jadwal Penelitian Jelas (Tabel 3.6):** Rencana kegiatan dari persiapan, pelaksanaan (Juli–Agustus), hingga penyusunan laporan telah terisi dengan rapi.

---

## 🚦 2. Matriks Status Kesiapan Naskah

| Komponen | Status | Catatan Evaluasi Utama |
| :--- | :---: | :--- |
| **Format & Halaman Depan** | ⚠️ *Perlu Perapian* | Lengkapi nama Dekan/Koorprodi/Pembimbing pada Kata Pengantar, perbaiki penulisan gelar pembimbing (`M.T.`), dan koreksi tahun 2025. |
| **Bab I: Pendahuluan** | ⚠️ *Revisi Sedang* | Sinkronkan 3 butir Tujuan Penelitian agar simetris dengan 3 butir Rumusan Masalah, rapikan tanda baca. |
| **Bab II: Tinjauan Pustaka** | 🚨 *Revisi Mayor* | **Rombak total gaya bahasa lisan/gaul pada Subbab 2.1 poin 3 & 6** menjadi bahasa Indonesia baku; perbaiki nama subbab "Struktur Tag" menjadi "Struktur URL"; sinkronkan nama sitasi. |
| **Bab III: Metodologi & Scoring** | 🚨 *Revisi Mayor* | **Sinkronkan 27 indikator Tabel 3.2 dengan formula Scoring Tabel 3.4** (ada 4 indikator utama hilang di tabel scoring); definisikan batas toleransi persentase Skor 1 (Perlu Perbaikan); sinkronkan sisa kata "tiga periode" menjadi "empat periode". |
| **Daftar Pustaka & Sitasi** | 🚨 *Revisi Mayor* | Lengkapi metadata jurnal (banyak nama jurnal, volume, dan halaman kosong); **wajib beralih menggunakan Mendeley / Zotero (style APA 7th)**. |
| **Lampiran Bukti Data** | 🚨 *Revisi Mayor* | Lampiran 1, 2, dan 3 saat ini masih kosong tanpa gambar tangkapan layar dashboard tools. |

---

## 🔍 3. Rincian Catatan Revisi & Solusi Perbaikan Bab per Bab

### 📄 Bagian Awal Naskah (Cover s.d. Daftar Singkatan)

1. **Koreksi Tahun & Penulisan Gelar:**
   * Pada Halaman Pengesahan (hal. ii): Penulisan gelar Pembimbing I tertulis `Anton Prafanto, S.Kom., MT.` ➔ Ubah menjadi **`Anton Prafanto, S.Kom., M.T.`** (gunakan tanda titik).
   * Pada Halaman Pengesahan (hal. ii): Tanggal rapat pembimbing masih berupa *placeholder* `[tgl, bln, tahun]`.
   * Pada Kata Pengantar (hal. iii, baris 142): Tertulis *"Samarinda,.............................. 202 5"* ➔ Koreksi menjadi tahun **2026**.
2. **Lengkapi Template Kata Pengantar (Halaman iii):**
   * Masih terdapat teks bawaan template:
     - Poin 2: *Nama dan gelar akademik lengkap Dekan...*
     - Poin 3: *Nama dan gelar akademik Koordinator Prodi...* (koreksi juga typo *"selaku K Program Studi"*).
     - Poin 4–5: *Nama dan gelar akademik Dosen Pembimbing I & II...*
     - Poin 6–7: Dosen Penguji I & II (dapat dihapus sementara untuk draf seminar proposal karena penguji baru ditetapkan saat sidang).
3. **Perapian Daftar Singkatan (Halaman viii):**
   Koreksi beberapa salah ketik istilah asing pada daftar singkatan:
   * `DA = Domain Autority` ➔ **Domain Authority** (kurang huruf 'h').
   * `PA = Page Autority` ➔ **Page Authority** (kurang huruf 'h').
   * `CLS = Cumulative layout Shift` ➔ **Cumulative Layout Shift** (kapitalisasi huruf 'L').
   * `INP = Interaction To Next Paint` ➔ **Interaction to Next Paint** (huruf 't' kecil).
   * `AWT = Ahrefs Webmaster Tool` ➔ **Ahrefs Webmaster Tools** (tambahkan 's').
   * `GA4 = Google Analytic 4` ➔ **Google Analytics 4** (tambahkan 's').

---

### 📘 BAB I – Pendahuluan

1. **🚨 Penyelarasan Simetris Rumusan Masalah vs Tujuan Penelitian:**
   * **Masalah:** Pada Subbab 1.2 kamu menulis **3 butir Rumusan Masalah**:
     1. Kondisi penerapan SEO On-page aktual (AWT, GSC, GA4) periode Juli 2026.
     2. Permasalahan teknis SEO On-page dan pengaruhnya terhadap visibilitas trafik organik.
     3. Rekomendasi strategis peningkatan performa SEO On-page.
   * Namun pada Subbab 1.4 (Tujuan Penelitian), kamu **hanya menulis 2 butir tujuan** (poin analisis pengaruh permasalahan teknis terlewat).
   * **Rekomendasi Revisi:** Buat butir Tujuan Penelitian menjawab secara simetris ke-3 butir Rumusan Masalah:
     > **1.4 Tujuan Penelitian:**  
     > 1. Mengidentifikasi dan menganalisis kondisi penerapan SEO On-page pada website Lintasjejaring.com menggunakan Ahrefs Webmaster Tools, Google Search Console, dan Google Analytics 4 pada periode Juli 2026.  
     > 2. Menganalisis permasalahan teknis SEO On-page yang ditemukan serta mengevaluasi dampaknya terhadap visibilitas dan trafik organik situs.  
     > 3. Merumuskan rekomendasi strategi berbasis data dan *roadmap* perbaikan terukur untuk meningkatkan performa SEO On-page Lintasjejaring.com.
2. **Koreksi Tanda Baca & Typo:**
   * Pada Rumusan Masalah butir 1, 2, dan 3: Tambahkan tanda tanya (`?`) di akhir kalimat pertanyaan (saat ini menggunakan titik).
   * Hal. 3 (Rumusan Masalah 1): *"kondisi penera pan"* ➔ `kondisi penerapan`.
   * Hal. 3 (Batasan Masalah 3): *"pengambilan data dilakaukan"* ➔ `dilakukan`.
   * Hal. 4 (Tujuan 2): *"dan visisbilitas"* ➔ `dan visibilitas`.

---

### 📗 BAB II – Tinjauan Pustaka

#### 🚨 1. REVISI SANGAT KRUSIAL: Rombak Total Bahasa Gaul / Percakapan pada Subbab 2.1
Pada Subbab 2.1 (Penelitian Terkait), terdapat paragraf yang menggunakan **gaya bahasa percakapan santai / lisan non-akademik**. Ini sangat fatal dalam karya ilmiah:

* **Contoh pada Poin 3 (Kurniawan et al., 2025, hal. 6–7):**
  > *Teks Saat Ini:*  
  > "...Situs web lembaga pendidikan **punya andil besar** dalam menyebarkan info ke calon mahasiswa... dan SEO **jadi aspek krusial buat ningkatin daya tampak**... Penelitian ini menggunakan metode campuran **buat nilai seberapa jitu strategi SEO yang udah diterapin**... alat bantu analitik **kayak** Google Analytics..."
  > 
  > *Perbaikan Menjadi Ragam Ilmiah Baku:*  
  > "...Situs web institusi pendidikan tinggi memiliki peranan strategis dalam diseminasi informasi kepada calon mahasiswa dan publik. Penerapan strategi SEO menjadi instrumen penting untuk meningkatkan visibilitas dan aksesibilitas situs pada halaman hasil pencarian mesin pencari. Penelitian tersebut menerapkan metode kombinasi (*mixed methods*) untuk mengevaluasi efektivitas strategi optimasi kata kunci, kualitas konten, serta pembangunan tautan (*link building*)..."

* **Contoh pada Poin 6 (Nugroho et al., 2025, hal. 7–8):**
  > *Teks Saat Ini:*  
  > "...Hasil riset menunjukkan bahwa **memakai teknik SEO yang baik itu penting**..."
  > 
  > *Perbaikan Menjadi Ragam Ilmiah Baku:*  
  > "...Hasil penelitian menegaskan signifikansi penerapan teknik optimasi SEO terstruktur terhadap peningkatan performa indeks dan perolehan trafik organik situs..."

#### 2. Ketidakkonsistenan Penulisan Nama Peneliti (Teks vs Tabel 2.1 vs Daftar Pustaka):
* Poin 1: Di teks tertulis *Apiani & Syifa (2025)*, di Tabel 2.1 tertulis *Apriyani & Syifa (2025)*. Samakan sesuai nama asli di artikel: **Apiani & Syifa (2025)**.
* Poin 2: Di teks tertulis *Putra et al. (2024)*, di Tabel 2.1 tertulis *Irsyad (2024)*. Samakan menjadi **Putra et al. (2024)**.
* Poin 3: Di Tabel 2.1 kolom peneliti tertulis *Welli Braham Kurniawan (2025)* ➔ Cukup tulis nama belakang: **Kurniawan et al. (2025)**.
* Poin 6: Di Tabel 2.1 tertulis *Bambang Prihantoro Nugroho (2025)* ➔ Cukup tulis: **Nugroho et al. (2025)**.
* Poin 7: Di Tabel 2.1 tertulis *Junaedi (2025)* ➔ Seharusnya **Rendyanto & Junaedi (2025)**.
* Poin 8: Di Tabel 2.1 tertulis *Khoirul Annisa Febriana (2025)* ➔ Seharusnya **Febriana & Khafidhoh (2025)**.
* Poin 10: Di Tabel 2.1 tertulis *Putro & Fauzy (2024)* ➔ Di narasi teks tertulis *Marsha Awang Lisba Siella et al. (2024)*. Penulis pertamanya adalah **Marsha Awang Lisba Siella**, bukan Putro.

#### 3. Koreksi Judul Subbab 2.3 Butir d (Halaman 15):
* Tertulis: **`d. Struktur Tag`**, padahal teks isinya membahas: *"URL yang ramah mesin pencari (SEO-friendly URL) bersifat singkat, deskriptif..."*.
* **Tindakan:** Ubah judul poin menjadi **`d. Struktur URL`**.

#### 4. Typo pada Subbab 2.5 (Website, Halaman 18):
* *"Penilaian indikator website pun tidak berhenti **padda** aspek..."* ➔ `pada`.
* *"faktor-faktor teknis **sepertikecepatan** akses..."* ➔ `seperti kecepatan`.
* *"juga **diketehuimemiliki** hubungan..."* ➔ `diketahui memiliki`.

---

### 📙 BAB III – Metodologi Penelitian & Sistem Penilaian

#### 🚨 1. TEMUAN KRITIS METODOLOGI: Diskrepansi 27 Indikator (Tabel 3.2) vs Tabel Scoring (Tabel 3.4)
* **Masalah:** Pada Tabel 3.2 kamu merancang **27 indikator** yang dikumpulkan. Namun pada Tabel 3.4 (Pengelompokan Indikator Scoring Kategori 5: Visibilitas & Keterlibatan), kamu **hanya memasukkan 3 indikator** (*Average CTR, Average Position, Engagement Rate*).
* **Indikator yang Hilang di Formula Scoring:**
  - *Total Clicks* (Indikator 1)
  - *Total Impressions* (Indikator 2)
  - *Organic Sessions* (Indikator 7)
  - *Average Engagement Time* (Indikator 9)
* **Solusi Wajib:** Perjelas di narasi Bab 3:
  1. Apakah 4 indikator tersebut hanya diposisikan sebagai **metrik deskriptif tren trafik** (tanpa masuk bobot skor)? Atau,
  2. Masukkan ke dalam Tabel 3.4 Kategori 5 dengan mendefinisikan standar skornya (misal: tren naik = skor 2, stagnan = skor 1, turun = skor 0).

---

#### 🚨 2. Definisi Kriteria Objektif Ambang Batas Skor 1 ("Perlu Perbaikan")
* **Masalah:** Di Tabel 3.3, kamu mendefinisikan Skor 1 sebagai *"Nilai mendekati standar namun belum memenuhi sepenuhnya"*. Ini sangat abstrak dan dinilai subjektif oleh penguji.
* **Solusi Wajib:** Berikan batas toleransi persentase yang eksak pada setiap indikator teknis di Bab 3, misalnya:
  - **Skor 2 (Baik):** $0\%$ kesalahan / $100\%$ memenuhi standar acuan.
  - **Skor 1 (Perlu Perbaikan):** Ditemukan $1\% - 15\%$ halaman/gambar yang bermasalah (*missing/duplicate*).
  - **Skor 0 (Buruk):** Ditemukan $> 15\%$ halaman/gambar bermasalah atau terjadi *error* kritis (*broken link / redirect loop*).

---

#### 3. Rujukan Standar Acuan Industri (Tabel 3.2)
Tambahkan sitasi rujukan resmi industri untuk standar acuan yang kamu tetapkan di Tabel 3.2:
* *CTR > 3%:* Rujuk riset benchmark CTR media berita daring (*Advanced Web Ranking / WordStream*).
* *Engagement Rate > 50%:* Rujuk standar benchmark Google Analytics 4 untuk industri portal berita.
* *Average Engagement Time > 30 detik:* Rujuk rata-rata waktu baca artikel berita daring regional.

---

#### 4. Sinkronisasi Kata "Tiga Periode" menjadi "Empat Periode"
* Di hal. 25 (line 1357): *"data tren GSC dan GA4 dari **tiga periode** dibandingkan..."* ➔ Ubah menjadi **empat periode**.
* Di hal. 36 (Subbab 3.5.4, line 1940): *"(deviasi > 15% dari pola **tiga minggu** lainnya)"* ➔ Ubah menjadi **minggu-minggu lainnya**.

---

## 📚 4. Audit Silang Sitasi, Daftar Pustaka & Panduan Reference Manager

### 🛠️ A. REKOMENDASI UTAMA: Wajib Beralih Menggunakan Mendeley atau Zotero!

Banyaknya data rujukan yang tidak lengkap (tanpa nama jurnal, volume, nomor, dan halaman) menunjukkan bahwa penulisan daftar pustaka dilakukan secara manual. 

**Kamu WAJIB menggunakan Reference Management Software (**Mendeley Reference Manager** atau **Zotero**)** yang terhubung langsung dengan Microsoft Word:

1. **Keuntungan Teknis:**
   - **Kelengkapan Metadata Otomatis:** Saat mengimpor artikel melalui DOI atau PDF, nama jurnal, tahun, volume, nomor terbitan, dan rentang halaman akan terisi otomatis dan akurat.
   - **Standarisasi APA 7th Edition:** Software otomatis mengatur format *in-text citation* `(Penulis, Tahun)` dan format daftar pustaka (*sentence case* judul artikel, *italic* nama jurnal/volume, dan link aktif `https://doi.org/...`).
   - **Konsistensi 100%:** Daftar pustaka dijamin sinkron sempurna dengan kutipan di badan naskah.

---

### B. Daftar Pustaka yang Belum Lengkap Datanya (Wajib Dilengkapi di Mendeley/Zotero):
1. **`Albab, M. H. F., Ratnawati, D. E., & Rahayudi, B. (2024)`** (No. 2) ➔ Nama jurnal, volume, nomor, dan halaman tidak dicantumkan.
2. **`Febriana, K. A., & Khafidhoh, N. (2025)`** (No. 5) ➔ Nama jurnal, volume, dan nomor halaman tidak ada.
3. **`Pratama, I., & Hasmawati, F. (2024)`** (No. 15) ➔ Nama jurnal penerbit tidak dicantumkan (hanya `02(01)`).
4. **`Putra, G. M., Ikram, A. D., Wardhana, R., Prafanto, A., & Irsyad, A. (2024)`** (No. 16) ➔ Nama jurnal / prosiding seminar tidak dicantumkan.
5. **`Rendyanto, M. N., & Junaedi, L. (2025)`** (No. 17) ➔ Nama jurnal tidak dicantumkan (hanya `6(4)`).
6. **`Sadiah, H., & Maharani, S. H. (2024)`** (No. 19) ➔ Nama jurnal tidak dicantumkan (hanya `3(2)`).

---

## 🖼️ 5. Lampiran Bukti Observasi Awal (Halaman 40–41)

* **Temuan Kritis:** Pada bagian Lampiran (hal. 40–41), tertulis judul:
  - *Lampiran 1 halaman utama Ahrefs Webmaster Tools*
  - *Lampiran 2 halaman utama Google Search Console*
  - *Lampiran 3 halaman utama Google Analytics*
* Namun di bawah judul-judul tersebut **belum terdapat gambar tangkapan layar (screenshot dashboard)** sama sekali (masih berupa halaman kosong).
* **Tindakan Wajib:** Tempelkan tangkapan layar (*screenshot*) verifikasi domain AWT, dashboard performa GSC, dan dashboard GA4 Lintasjejaring.com sebelum naskah dicetak/diekspor ke PDF.

---

## 🎯 6. Pertanyaan Latihan untuk Persiapan Seminar Proposal

Pelajari dan siapkan argumen ilmiah untuk pertanyaan-pertanyaan yang sangat berpotensi diajukan oleh dosen penguji:

1. **"Apakah Anda memiliki otorisasi / hak akses resmi dari pemilik domain Lintasjejaring.com?"**  
   *Jawaban yang tepat:* Ya, penelitian ini menggunakan data primer internal dari Google Search Console, Google Analytics 4, dan Ahrefs Webmaster Tools yang memerlukan verifikasi kepemilikan domain (DNS / delegasi properti GSC). Kami telah berkoordinasi dan mengantongi izin resmi dari pihak pengelola/redaksi Lintasjejaring.com.
2. **"Mengapa penelitian ini hanya fokus pada SEO On-page dan tidak mengoptimasi SEO Off-page secara mendalam?"**  
   *Jawaban yang tepat:* Aspek SEO On-page (metadata, struktur URL, indexability, internal links, dan Core Web Vitals) berada 100% di bawah kendali teknis internal pengelola situs Lintasjejaring.com sehingga perbaikan dapat langsung dieksekusi secara mandiri. Sebaliknya, SEO Off-page bergantung pada pihak ketiga (backlink luar). Data off-page tetap kami tampilkan sebagai konteks pendukung otoritas domain.
3. **"Bagaimana Anda menentukan bobot persentase pada 5 kategori sistem penilaian SEO Health?"**  
   *Jawaban yang tepat:* Pembobotan didasarkan pada signifikansi dampak teknis terhadap mesin pencari: *Indexability* (25%) adalah prasyarat mutlak perayapan Google; *Metadata & Struktur* (25%) menentukan relevansi kata kunci; *Core Web Vitals* (25%) merupakan sinyal resmi *Page Experience* Google; *Kualitas Konten* (15%) dan *Visibilitas/Keterlibatan* (10%) melengkapi evaluasi pengalaman pengguna. Total bobot terakumulasi 100%.
4. **"Mengapa menggunakan PageSpeed Insights untuk Core Web Vitals, bukan langsung dari Google Search Console?"**  
   *Jawaban yang tepat:* GSC memerlukan batas minimum volume trafik pengguna Chrome nyata (*CrUX dataset threshold*) yang seringkali belum mencukupi pada media daring regional. Oleh karena itu, data lab dari PageSpeed Insights digunakan untuk memperoleh hasil pengukuran performa LCP, CLS, dan INP yang terstandarisasi.
5. **"Apa nilai kebaruan (novelty) skripsi ini dibanding penelitian SEO pada umumnya?"**  
   *Jawaban yang tepat:* Penelitian terdahulu umumnya mengkaji SEO secara parsial (hanya kata kunci atau satu tools saja) pada media nasional besar. Penelitian ini menyajikan model evaluasi holistik multi-tools (AWT, GSC, GA4) dengan analisis tren komparatif 4 mingguan dan sistem scoring kuantitatif yang dirancang khusus untuk portal berita lokal Kalimantan Timur dengan keterbatasan sumber daya.

---

## ✅ 7. Lembar Checklist Tindak Lanjut Revisi Mahasiswa

Beri tanda centang `[v]` setelah menyelesaikan butir perbaikan berikut:

- [ ] Memperbaiki penulisan gelar Pembimbing I (`Anton Prafanto, S.Kom., M.T.`) dan tahun 2026 pada Kata Pengantar.
- [ ] Mengisi nama lengkap Dekan, Koorprodi, dan Dosen Pembimbing pada lembar Kata Pengantar.
- [ ] Mengoreksi salah ketik pada Daftar Singkatan (`Domain Authority`, `Cumulative Layout Shift`, `Google Analytics 4`, dll.).
- [ ] Menyelaraskan 3 butir Tujuan Penelitian agar simetris dengan 3 butir Rumusan Masalah.
- [ ] **MEROMBAK TOTAL gaya bahasa lisan/santai pada Subbab 2.1 (poin 3 dan 6) menjadi bahasa Indonesia ragam ilmiah baku.**
- [ ] Menyelaraskan nama pengarang di teks Bab 2, Tabel 2.1, dan Daftar Pustaka (termasuk *Marsha Awang Lisba Siella et al.*).
- [ ] Mengoreksi judul subbab *d. Struktur Tag* menjadi *d. Struktur URL*.
- [ ] Memperbaiki salah ketik teks pada Subbab 2.5 (Website).
- [ ] **Menyelaraskan 27 indikator pada Tabel 3.2 dengan tabel formula scoring Tabel 3.4.**
- [ ] **Mendefinisikan kriteria ambang toleransi persentase untuk Skor 1 (Perlu Perbaikan) di Bab III.**
- [ ] Mengoreksi sisa kata "tiga periode" dan "tiga minggu" menjadi "empat periode" pada Bab III hal. 25 & hal. 36.
- [ ] **MENGGUNAKAN REFERENCE MANAGER (Mendeley / Zotero)** untuk mengelola sitasi dan melengkapi seluruh metadata jurnal yang hilang di Daftar Pustaka (format APA 7th).
- [ ] Menempelkan gambar tangkapan layar dashboard AWT, GSC, dan GA4 pada Lampiran 1, 2, dan 3.
- [ ] Memastikan bukti surat izin / akses delegasi domain Lintasjejaring.com telah disiapkan untuk lampiran.

---
*Laporan audit ini disusun sebagai panduan resmi bimbingan skripsi agar draf proposal Aji Pangestu siap dan matang untuk diajukan ke Seminar Proposal.*
