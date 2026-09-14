# 📋 LAPORAN AUDIT FORENSIK AKHIR & VERIFIKASI ACC SEMINAR PROPOSAL SKRIPSI

**Mahasiswa Bimbingan:** Ahmad Dhafin (NIM: 2209106122)  
**Program Studi:** S1 Informatika, Fakultas Teknik, Universitas Mulawarman  
**Dosen Pembimbing I:** Aulia Khoirunnita, S.Kom., M.Kom. (NIP: 199308172023212069)  
**Dosen Pembimbing II:** Anton Prafanto, S.Kom., M.T. (NIP: 199310222019031016)  
**Koordinator Program Studi:** Awang Harsa Kridalaksana, S.Kom., M.Kom. (NIP: 19731229 200501 1 002)  
**Judul Proposal:** *Pengembangan Mini Game Edukatif Simulasi Penanganan Kebakaran Berbasis Roblox Menggunakan Behavior Tree*  
**Dokumen yang Diverifikasi:** `draft proposal ahmad dhafin revisi 2.pdf` (54 Halaman)  
**Tanggal Evaluasi:** 15 September 2026  
**Status Evaluasi Akhir:** **STATUS: ACC (DISETUJUI) UNTUK PENDAFTARAN SEMINAR PROPOSAL SKRIPSI (DENGAN 10 CATATAN MIKRO PRA-CETAK)**

---

> [!NOTE]
> **Keputusan Resmi Dosen Pembimbing:** Naskah proposal skripsi Ahmad Dhafin pada versi **Revisi 2** ini telah memenuhi seluruh kriteria kelayakan akademik S1 Informatika, kesesuaian metodologi rekayasa game (*Game Development Life Cycle*), penerapan kecerdasan buatan (*Behavior Tree*), instrumen pengujian (*Black Box & UAT*), kelengkapan administrasi preliminer, serta perbaikan tata letak dokumen. Mahasiswa **DIBERIKAN PERSETUJUAN (ACC)** untuk mendaftar dan menjadwalkan **Ujian Seminar Proposal Skripsi**. Catatan forensik di bawah ini ditujukan sebagai panduan *pre-print polish* (penyempurnaan pra-cetak) agar naskah fisik yang diserahkan ke Dewan Penguji berstatus *zero-defect*.

---

## 🔍 1. Verifikasi Perbaikan Mayor (Revisi 1 ➔ Revisi 2: Tuntas 100%)

Mahasiswa telah menuntaskan seluruh perbaikan krusial dan *showstopper* dokumen dari revisi sebelumnya dengan sangat baik:

| No | Komponen yang Diperiksa | Status Revisi 2 | Keterangan Hasil Forensik Dokumen |
| :---: | :--- | :---: | :--- |
| **1** | **Halaman Pengesahan (Hal. ii)** | **TUNTAS** | Nama Pembimbing I (Ibu Aulia Khoirunnita) dan Pembimbing II (Pak Anton Prafanto) beserta gelar dan NIP resmi telah tercantum lengkap dan benar. |
| **2** | **Kata Pengantar (Hal. iii)** | **TUNTAS** | Butir dosen penguji fiktif telah dihapus; titimangsa telah terisi resmi: `Samarinda, 11 September 2026`; teks `DAFTAR ISI` yang terselip di bawah telah bersih. |
| **3** | **Tata Letak Tabel 2.1 (Hal. 11–12)** | **TUNTAS** | Pengaturan tabel mengambang (*floating*) telah diperbaiki. Baris 9 dan 10 kini menyambung rapi di bagian atas halaman 12 dan tidak lagi melompati subbab. |
| **4** | **Typo Subbab 2.2** | **TUNTAS** | Judul `2.2 Pembalajaran...` telah dikoreksi menjadi `2.2 Pembelajaran...` baik di dalam teks maupun di Daftar Isi. |
| **5** | **Matriks Jadwal Penelitian (Tabel 3.9)** | **TUNTAS** | Sel-sel matriks bulan Juni s.d. November 2026 telah diisi arsiran abu-abu (*cell shading*) yang rapi mencakup tahap persiapan, pelaksanaan, dan laporan. |
| **6** | **Daftar Tabel (Hal. vi)** | **TUNTAS** | Entri `Tabel 3.9 Jadwal Penelitian` di halaman 38 telah resmi didaftarkan pada Daftar Tabel di halaman preliminer. |
| **7** | **Penambahan Pustaka Lonteng (2024)** | **TUNTAS** | Rujukan `Lonteng et al. (2024)` pada tahap testing GDLC telah ditambahkan secara resmi ke dalam Daftar Pustaka. |
| **8** | **Koreksi Sitasi Hasugian vs Wulandari** | **TUNTAS** | Sitasi di Bab II telah diubah dari `(Hasugian, 2023)` menjadi `(Wulandari, 2023)` sesuai urutan penulis pertama. |
| **9** | **Urutan Abjad Institusi Pemerintah** | **TUNTAS** | Rujukan *Kementerian Komunikasi* dan *Kementerian Ekonomi Kreatif* telah disatukan secara alfabetis di bawah huruf **K**. |
| **10** | **Pemodelan Behavior Tree (Bab III)** | **TUNTAS** | Struktur pohon Gambar 3.2, formula kepanikan piecewise, dan spesifikasi Luau *server-side* tetap terjaga kokoh. |

---

## 🔬 2. Hasil Audit Forensik Mendalam: 10 Catatan Mikro Pra-Cetak (Zero-Defect)

Audit forensik lapis kedua terhadap dokumen fisik PDF (54 halaman) mengungkap beberapa anomali mikro, cacat bawaan *reference manager* (Mendeley/Zotero), serta ketidaksesuaian tata letak dengan **Buku Pedoman Penulisan Skripsi Fakultas Teknik Universitas Mulawarman**. Hal-hal berikut wajib disempurnakan mahasiswa sebelum naskah dicetak untuk dewan penguji:

### A. Format & Tipografi Formalia Pedoman FT UNMUL

1. **Placeholder Tanggal Rapat di Halaman Pengesahan (Hal. ii / PDF Hal. 3):**
   * *Temuan:* Masih tertulis template: `Telah dibahas dalam Rapat Dosen Pembimbing pada [tgl, bln, tahun] dan dinyatakan memenuhi syarat...`.
   * *Solusi:* Kurung siku `[tgl, bln, tahun]` wajib diisi tanggal persetujuan (misal: `15 September 2026`) atau disesuaikan dengan format prodi agar berkas fisik tanda tangan tidak memuat teks kurung siku template.
   * *Tambahan:* Teks `HALAMAN PENGESAHAN` dan `HALAMAN JUDUL` yang tercetak di bawah judul skripsi sebaiknya dihapus karena merupakan judul panduan template, bukan isi cover.

2. **Posisi Penomoran Halaman (Kaidah Header & Footer FT UNMUL):**
   * *Kaidah FT UNMUL:* 
     - **Halaman Pertama Setiap Bab** (BAB I, BAB II, BAB III, DAFTAR PUSTAKA): Nomor halaman di **Tengah Bawah** (*Bottom Center*).
     - **Halaman Lanjutan Bab**: Nomor halaman di **Kanan Atas** (*Top Right*).
     - **Halaman Judul (Hal. i)**: Dihitung tetapi nomor halaman **tidak dicetak**.
   * *Temuan:* Mahasiswa mengatur seluruh nomor halaman tubuh utama (hal. 1 s.d. 42) berada di **Kanan Bawah** (*Bottom Right*). Angka `i` juga ikut tercetak di pojok kanan bawah halaman judul.
   * *Solusi:* Pada Microsoft Word, aktifkan opsi **`Different First Page`** (*Halaman Pertama Berbeda*) pada setiap Section bab, pindahkan nomor halaman lanjutan ke Header kanan atas, dan hapus penomoran pada Halaman Judul.

3. **Nomor Persamaan Matematika Belum Ada (Bab II & Bab III):**
   * *Temuan 1 (Subbab 2.9, Hal. 19 / PDF Hal. 31):* Rumus rata-rata UAT:
     $$\bar{x} = \frac{\sum x}{n}$$
     belum memiliki nomor label persamaan di margin kanan. Berikan label **`(Persamaan 2.1)`** atau **`(2.1)`**.
   * *Temuan 2 (Subbab 3.4.1, Hal. 28 / PDF Hal. 40):* Formula fungsi piecewise kepanikan $IsPanicLevelHigh$:
     belum memiliki nomor label persamaan. Berikan label **`(Persamaan 3.1)`** atau **`(3.1)`**.
   * *Temuan 3 (Hal. 28):* Kata `Keterangan:` tertulis **sebelum** formula piecewise ditampilkan, baru diikuti butir parameter. Letakkan kata `Keterangan:` **setelah** persamaan.

4. **Daftar Lampiran Palsu / Residu Template (Hal. viii / PDF Hal. 9):**
   * *Temuan:* Pada halaman viii, tertulis: `Lampiran 1 contents 42`. Angka 42 merujuk pada halaman terakhir Daftar Pustaka (hal. 42), dan naskah sebenarnya **belum memiliki lampiran fisik**.
   * *Solusi:* Jika pada tahap proposal mahasiswa ingin melampirkan draf kuesioner UAT, masukkan berkas kuesioner tersebut di belakang Daftar Pustaka sebagai `Lampiran 1: Kuesioner Pengujian User Acceptance Testing (UAT)`. Jika tidak ada lampiran, **hapus halaman viii (Daftar Lampiran)** sepenuhnya dari file Word.

5. **Subbab 1.7 (Sistematika Penulisan) Belum Ada di Bab I:**
   * *Temuan:* Bab I berakhir mendadak di `1.6 Kontribusi Penelitian` (Hal. 6).
   * *Solusi:* Tambahkan **`1.7 Sistematika Penulisan`** yang menguraikan secara ringkas isi Bab I (Pendahuluan), Bab II (Tinjauan Pustaka), Bab III (Metodologi Penelitian), rencana Bab IV (Hasil dan Pembahasan), dan Bab V (Kesimpulan dan Saran). Ini adalah pertanyaan wajib penguji sempro.

6. **Header Tabel Preliminer Terpotong (Hal. ix & xi):**
   * *Temuan:* Pada `DAFTAR ISTILAH/LAMBANG` (Hal. ix) dan `DAFTAR SINGKATAN` (Hal. xi), tabel hanya memiliki header kolom kanan (`Arti`). Header kolom kiri kosong.
   * *Solusi:* Lengkapi header kolom kiri dengan tulisan `Istilah / Lambang` pada hal. ix dan `Singkatan` pada hal. xi. Selain itu, entri `APAR` cukup dicantumkan di Daftar Singkatan, tidak perlu diulang di Daftar Istilah.

---

### B. Forensik Bibliografi & Metadata Reference Manager

7. **Anomali Pengarang Fiktif pada Marchelputra dkk. (2023) di Daftar Pustaka (Hal. 40 / PDF Hal. 52):**
   * *Temuan:* Tertulis `Marchelputra, T. S., Haryanto, H., Hastuti, K., Kadiasti, R., Nuswantoro Semarang, D., & Dian Nuswantoro Semarang, U. (2023)...`
   * *Penyebab:* Metadata scraping otomatis Mendeley salah mengenali nama kampus *Universitas Dian Nuswantoro Semarang (UDINUS)* sebagai dua orang penulis (`D. Nuswantoro Semarang` & `U. Dian Nuswantoro Semarang`).
   * *Koreksi:* Hapus dua nama instansi tersebut dari Mendeley. Penulis resmi hanya 4 orang: Teguh Satrio Marchelputra, Heru Haryanto, Kaslinda Hastuti, dan Raden Kadiasti.

8. **Teks Hangul Korea pada Lee dkk. (2024) di Daftar Pustaka (Hal. 40 / PDF Hal. 52):**
   * *Temuan:* Tertulis `Lee, J.-M., Kim, J.-Y., & 미디어소프트웨어학과성결대학교. (2024)...`
   * *Penyebab:* Teks `미디어소프트웨어학과성결대학교` adalah nama jurusan di Sungkyul University (*Department of Media Software*) yang terimpor ke kolom author.
   * *Koreksi:* Hapus teks Korea tersebut di Mendeley. Di teks naskah (hal. 8), ganti sitasi dari `(Lee et al., 2024)` menjadi **`(Lee & Kim, 2024)`** karena penulis aslinya hanya dua orang.

9. **Metadata Jurnal Hilang pada 3 Pustaka:**
   * **Wulandari (2023) (Hal. 40):** Tertulis `4(1), 20–27.` tanpa nama jurnal. Lengkapi menjadi: *Jurnal Mahasiswa Ilmu Komputer (JMIK)*, Vol. 4, No. 1, hlm. 20–27. DOI: 10.24127/ilmukomputer.v4i1.3383.
   * **Ardiansyah dkk. (2024) (Hal. 39):** Lengkapi nama jurnal: *Format: Jurnal Ilmiah Teknik Informatika*, Vol. 13, No. 1, hlm. 66–78.
   * **Menora dkk. (2023) (Hal. 40):** Lengkapi nama jurnal: *KONSTELASI: Konvergensi Teknologi dan Sistem Informasi*, Vol. 3, No. 1, hlm. 24–35.

10. **Urutan Alfabetis Wulandari & Entri Berita BPBD DKI di Daftar Pustaka:**
    * *Urutan Wulandari:* Entri `Wulandari, N. H. H. (2023)` terselip di antara `Fu` dan `Huang` (bekas posisi Hasugian). Pindahkan ke bawah abjad **W**.
    * *Entri BPBD DKI (Hal. 39):* Tertulis judul berita sebagai penulis dengan tahun `(N.D.)`. Di teks dikutip `(BPBD DKI Jakarta, 2025)`. Ubah di Mendeley menjadi penulis institusi: `BPBD DKI Jakarta. (2025). BPBD DKI Catat 1.810 Bencana Terjadi Sepanjang 2024...`

---

## 📊 3. Matriks Progres Kesiapan Naskah

| Aspek Evaluasi | Draf Awal (26 Agt 2026) | Revisi 1 (10 Sept 2026) | Revisi 2 (15 Sept 2026) — ACC |
| :--- | :--- | :--- | :--- |
| **Kelengkapan Pengesahan** | Kosong template | Kosong nama pembimbing | **Lengkap: Pembimbing I, II & Kaprodi + NIP** |
| **Kata Pengantar** | Balon komentar Word tercetak | Ada placeholder penguji & tanggal kosong | **Bersih, bertanggal resmi 11 Sept 2026** |
| **Struktur AI Behavior Tree** | Flowchart IF-ELSE biasa | Diagram Pohon Hierarki (Mermaid) | **Diagram Pohon Hierarki Rapi & Kokoh** |
| **Logika Kepanikan NPC** | Belum ada formula matematis | Formula piecewise $\le 5\text{ m}$ / $\le 60\text{ s}$ | **Formula Matematis Piecewise Jelas** |
| **Layout Tabel Perbandingan (Tabel 2.1)** | Nomor acak (1, 4, 5, 6, 10...) | Nomor 1–10 tapi melompati subbab | **Menyambung rapi, bebas bug floating** |
| **Jadwal Penelitian (Tabel 3.9)** | Kosong titik-titik | Grid tabel kosong tanpa isi | **Terarsir lengkap Juni–Nov 2026 + Ada di Daftar Tabel** |
| **Integritas Daftar Pustaka** | Sitasi gaib (Kemal Pasha, Naufal) | Gaya APA 7th, tapi Lonteng hilang | **Lonteng masuk, APA 7th, DOI aktif** |
| **Tingkat Kesiapan Naskah** | ~50% (Revisi Mayor) | ~90% (Revisi Minor) | **~97% (LAYAK ACC SEMPRO)** |

---

## 🎯 4. Kesimpulan & Rekomendasi Tim Pembimbing

1. **Kelayakan Akademik:**  
   Proposal skripsi Ahmad Dhafin telah memenuhi standar kompetensi lulusan S1 Informatika Fakultas Teknik Universitas Mulawarman. Konsep teoritis, arsitektur AI *Behavior Tree*, integrasi GDLC, serta instrumen evaluasi *Black Box* dan *UAT* telah terdefinisi secara ilmiah dan dapat dipertanggungjawabkan.
2. **Keputusan Dosen Pembimbing:**  
   **DIBERIKAN STATUS ACC (DISETUJUI) UNTUK PENDAFTARAN SEMINAR PROPOSAL SKRIPSI.**
3. **Prosedur Mahasiswa:**  
   * Luangkan waktu 15–20 menit untuk memperbaiki 10 catatan mikro pra-cetak di atas pada file Microsoft Word.
   * Cetak lembar persetujuan untuk ditandatangani Dosen Pembimbing I (Ibu Aulia Khoirunnita, S.Kom., M.Kom.) dan Dosen Pembimbing II (Bapak Anton Prafanto, S.Kom., M.T.).
   * Daftarkan naskah proposal ke Sekretariat Program Studi Informatika untuk penetapan jadwal seminar dan dewan penguji.

---

## 💬 5. Draf Pesan WhatsApp Dosen ke Mahasiswa

```text
Wa'alaikumsalam wr. wb. Ahmad Dhafin,

Saya sudah memeriksa naskah proposal skripsi revisi 2 kamu secara menyeluruh.

Secara substansi dan keilmuan Informatika (Behavior Tree, GDLC, instrumen pengujian Black Box & UAT), proposal kamu SUDAH SANGAT BAIK DAN LAYAK. Halaman pengesahan, kata pengantar, perbaikan Tabel 2.1, dan arsiran jadwal penelitian Tabel 3.9 sudah tertata rapi.

Dengan ini proposal kamu SAYA NYATAKAN ACC UNTUK DAFTAR SEMINAR PROPOSAL SKRIPSI.

Sebelum kamu cetak dokumen fisik untuk diserahkan ke Dosen Penguji, tolong luangkan waktu sebentar di Word untuk merapikan beberapa catatan mikro pra-cetak berikut agar naskahmu benar-benar 'zero-defect' saat diuji:

1. Halaman Pengesahan (Hal. ii): Tulisan '[tgl, bln, tahun]' diisi tanggal persetujuan (misal 15 September 2026). Hapus tulisan 'HALAMAN PENGESAHAN' & 'HALAMAN JUDUL' yang tercetak di bawah judul.
2. Penomoran Halaman: Aktifkan 'Different First Page' di Word. Ingat pedoman FT UNMUL: Halaman awal BAB nomornya di tengah bawah, sedangkan halaman lanjutan BAB nomornya di kanan atas (saat ini naskahmu masih semuanya di kanan bawah). Halaman Judul tidak perlu ada nomor 'i'.
3. Rumus Matematika: Beri nomor persamaan rata kanan pada rumus rata-rata UAT di Bab 2 (Persamaan 2.1) dan formula kepanikan di Bab 3 (Persamaan 3.1).
4. Bab 1: Tambahkan Subbab 1.7 Sistematika Penulisan di akhir Bab 1 (merangkum isi Bab I s.d Bab V).
5. Daftar Lampiran (Hal. viii): Saat ini tertulis 'Lampiran 1 contents 42' padahal belum ada lampirannya. Lampirkan draf kuesioner UAT sebagai Lampiran 1, atau jika belum ada, hapus saja halaman Daftar Lampiran tersebut.
6. Daftar Pustaka:
   - Entri Marchelputra (2023): Hapus nama pengarang 'Nuswantoro Semarang, D.' dan 'Dian Nuswantoro Semarang, U.' di Mendeley (itu nama kampus UDINUS yang keliru masuk jadi pengarang).
   - Entri Lee (2024): Hapus tulisan huruf Korea di nama pengarang, dan di teks cukup sitasi (Lee & Kim, 2024).
   - Urutkan pustaka Wulandari (2023) ke bawah huruf W (saat ini masih di antara Fu dan Huang).
   - Lengkapi nama jurnal Wulandari (JMIK), Ardiansyah (Format), dan Menora (KONSTELASI).
7. Di Tabel 2.1 nomor 8, ganti kata 'enam state' menjadi 'empat state'.

Silakan diselesaikan perbaikan mikro tersebut, cetak lembar pengesahannya untuk ditandatangani, dan segera daftarkan ke prodi untuk penjadwalan seminar proposal ya. Selamat dan semangat menuju Sempro!
```

---
*Laporan audit forensik ini disusun oleh Tim Pembimbing sebagai bukti penjaminan mutu akademik naskah skripsi mahasiswa S1 Informatika Fakultas Teknik Universitas Mulawarman.*
