# 📋 LAPORAN AUDIT KOMPREHENSIF & EVALUASI FORENSIK REVISI 1 PROPOSAL SKRIPSI

**Mahasiswa Bimbingan:** Ahmad Dhafin (NIM: 2209106122)  
**Program Studi:** S1 Informatika, Fakultas Teknik, Universitas Mulawarman  
**Dosen Pembimbing I:** Aulia Khoirunnita, S.Kom., M.Kom. (NIP: 199308172023212069)  
**Dosen Pembimbing II:** Anton Prafanto, S.Kom., M.T. (NIP: 199310222019031016)  
**Judul Proposal:** *Pengembangan Mini Game Edukatif Simulasi Penanganan Kebakaran Berbasis Roblox Menggunakan Behavior Tree*  
**Dokumen yang Diaudit:** `draft proposal ahmad dhafin revisi 1.pdf` (54 Halaman)  
**Tanggal Evaluasi:** 10 September 2026  
**Status Kelayakan:** **PROGRES SANGAT SIGNIFIKAN (~90% SIAP) — WAJIB SELESAIKAN PERBAIKAN FORENSIK SEBELUM ACC SEMINAR PROPOSAL**

---

> [!IMPORTANT]
> **Audit Forensik Lapis Kedua:** Audit ini menguji naskah secara komprehensif dari Bab I hingga Daftar Pustaka (54 halaman) dengan mencakup **konsistensi logika AI Behavior Tree**, **ambang batas kuantitatif matematis**, **arsitektur engine Roblox Studio (studs vs meter)**, **keabsahan instrumen pengujian**, serta **audit bibliografi forensik** (termasuk verifikasi anomali metadata internasional).

---

## 🌟 1. Matriks Evaluasi Kepatuhan Revisi (Audit Awal vs Revisi 1)

| No | Catatan Audit Awal | Status Revisi 1 | Evaluasi & Temuan Forensik |
| :---: | :--- | :---: | :--- |
| **1** | Error *Bookmark not defined* di preliminer | **TUNTAS (100%)** | Bersih total pada Daftar Isi, Daftar Tabel, dan Daftar Gambar. |
| **2** | Balon komentar Word (*Commented [1]*) tercetak ke PDF | **TUNTAS (100%)** | Seluruh komentar Word telah dibersihkan sebelum ekspor PDF. |
| **3** | Kata "Roblox" hilang di paragraf penutup Latar Belakang | **TUNTAS (100%)** | Telah konsisten memuat *"Berbasis Roblox"* pada halaman 4. |
| **4** | Rumusan Masalah & Tujuan (kata *"performa"*) | **TUNTAS (100%)** | Fokus ke perancangan arsitektur dan pengujian fungsional/UAT. |
| **5** | Batasan Masalah jumlah state perilaku NPC | **TUNTAS (100%)** | Disinkronkan menjadi **4 state utama** (*Idle, WaitForHelp, FollowPlayer, Evacuate*). |
| **6** | Urutan nomor Tabel 2.1 berantakan (1, 4, 5, 6...) | **PROGRES 70%** | Nomor kolom telah 1–10, **namun urutan baris artikel belum sinkron dengan alur narasi Subbab 2.1**. |
| **7** | Rumus rata-rata UAT hilang di Subbab 2.9 | **TUNTAS (100%)** | Formula $\bar{x} = \frac{\sum x}{n}$ dan tabel interpretasi nilai Likert telah tampil. |
| **8** | Salah sebut nomor Gambar 2.1 di teks Subbab 2.6.1 | **TUNTAS (100%)** | Rujukan teks telah diperbaiki ke Gambar 2.1. |
| **9** | Duplikasi paragraf pada Subbab 2.10 (Black Box) | **TUNTAS (100%)** | Kalimat berulang telah dihapus. |
| **10** | Posisi sitasi rusak `(Lonteng et al., 2024)acuan` | **TUNTAS (100%)** | Posisi sitasi telah dipindahkan ke akhir kalimat. |
| **11** | **Ganti Flowchart Gambar 3.2 menjadi Hierarki BT** | **TUNTAS (100%)** | **Sangat Baik!** Struktur pohon hierarki *Behavior Tree* terpasang dengan baik. |
| **12** | Formula matematis status kepanikan (`PanicLevel`) | **TUNTAS (100%)** | Formula piecewise `IsPanicLevelHigh` ($\le 5\text{ m}$ / $\le 60\text{ s}$) telah dicantumkan. |
| **13** | Nomor rujukan tabel di narasi Bab 3 (Tabel 3.3, 3.4, 3.5) | **TUNTAS (100%)** | Seluruh rujukan nomor tabel di teks Bab 3 telah tepat. |
| **14** | Penjelasan teknis Roblox Scripting (Subbab 3.4.2) | **PROGRES 60%** | Konsep server & tick rate masuk, **namun skrip Luau masih perulangan kosong**. |
| **15** | Migrasi Daftar Pustaka ke APA 7th & DOIs | **PROGRES 75%** | Format rapi, **namun ditemukan anomali karakter Hangul Korea, salah abjad, dan sitasi tertinggal**. |
| **16** | Waktu, Tempat, dan Jadwal Penelitian (Subbab 3.7) | **PROGRES 50%** | Teks lokasi masuk, **namun matriks Tabel 3.9 masih kosong dan belum terdaftar di preliminer**. |

---

## 🧠 2. Temuan Kritis Logika AI, Arsitektur Game & Metodologi (Bab III)

### 🚨 A. Diskrepansi Kritis: Node `IsPathSafe` Hilang di Gambar 3.2
* **Fakta Temuan:**
  * Di **Tabel 3.4** (Variabel Skenario, hal. 25): Variabel nomor 3 adalah `PathSafe (Boolean)`.
  * Di **Tabel 3.5** (Komponen Node BT, hal. 27): Baris nomor 6 memuat `IsPathSafe` (*Condition Node* – Memeriksa apakah jalur evakuasi aman).
  * Di narasi Bab 3 (hal. 26): Tertulis *"jarak NPC terhadap sumber api (IsFireVeryNear), **keamanan jalur evakuasi (IsPathSafe)**, status interaksi pemain..."*.
  * **Fakta Lapangan:** Pada **Gambar 3.2 (Diagram Hierarki Behavior Tree, hal. 26), node `IsPathSafe` TIDAK ADA SAMA SEKALI** di cabang manapun!
* **Dampak Ujian:** Dosen penguji bidang Kecerdasan Buatan / RPL pasti akan menanyakan ke mana perginya node `IsPathSafe` dalam diagram implementasi.
* **Solusi Perbaikan:**
  1. Masukkan condition node `IsPathSafe == True` ke dalam cabang Sequence Evakuasi (misal: NPC hanya evakuasi jika jalur aman; jika terhalang api, NPC menunggu pemadaman), **ATAU**
  2. Jika keselamatan jalur dihitung otomatis oleh `PathfindingService` Roblox, hapus baris `IsPathSafe` dari Tabel 3.5 dan jelaskan secara eksplisit pada teks narasi.

---

### 🚨 B. Tumpang Tindih Logika (*Condition Collision*) `IsFireVeryNear` vs `IsPanicLevelHigh`
* **Fakta Temuan:**
  * Di Gambar 3.2, Sequence 1 (prioritas tertinggi) mengevaluasi: `IsFireVeryNear == True` $\rightarrow$ `Evacuate`.
  * Mahasiswa membuat formula matematis:
    $$\text{IsPanicLevelHigh} = \begin{cases} \text{True}, & \text{jika } \text{FireDistance} \le 5\,\text{meter} \text{ atau } \text{SimulationTime} \le 60\,\text{detik} \\ \text{False}, & \text{lainnya} \end{cases}$$
  * **Masalah Kritis:** Berapa jarak ambang batas untuk `IsFireVeryNear` **TIDAK PERNAH DITENTUKAN ANGKA / FORMULANYA**.
  * Jika jarak api $\le 5\text{ meter}$ sudah memicu kepanikan tinggi (Cabang 3), lalu berapa jarak untuk `IsFireVeryNear` (Cabang 1)? Tanpa batas pasti (misal: $\le 3\text{ meter}$), logika pohon akan ambigu (*collision*).
* **Solusi Perbaikan:** Definisikan secara kuantitatif:
  $$\text{IsFireVeryNear} = \begin{cases} \text{True}, & \text{jika } \text{FireDistance} \le 3\,\text{meter} \\ \text{False}, & \text{lainnya} \end{cases}$$

---

### 💡 C. Skala Jarak Engine Roblox (*Studs*) vs Satuan Metrik (*Meter*)
* **Fakta Temuan:** Mahasiswa menulis ukuran jarak dalam satuan metrik (**5 meter** dan **3 meter**).
* **Arsitektur Teknis Roblox Studio:** Koordinat ruang 3D (`Vector3`) dihitung dalam satuan **studs**.
  $$1\,\text{stud} \approx 0{,}28\,\text{meter} \quad \Longleftrightarrow \quad 1\,\text{meter} \approx 3{,}57\,\text{studs}$$
  Oleh karena itu:
  $$5\,\text{meter} \approx 18\,\text{studs} \quad \text{dan} \quad 3\,\text{meter} \approx 11\,\text{studs}$$
* **Catatan Kritis:** Jika pada skrip Luau mahasiswa menulis `if distance <= 5 then`, di Roblox itu terbaca **5 studs ($\approx 1{,}4\text{ meter}$)**, artinya NPC baru panik ketika tubuhnya menempel di kobaran api!
* **Solusi Perbaikan:** Tambahkan 1 paragraf penjelasan teknis konversi studs ini pada Subbab 3.4.2 agar terlihat menguasai teknis arsitektur engine Roblox.

---

### 💻 D. Skrip Luau (Subbab 3.4.2) Masih Perulangan Kosong (*Dummy Loop*)
* Pada halaman 29 (PDF hal. 41), mahasiswa hanya mencantumkan perulangan kosong:
  ```lua
  while true do 
      -- Evaluasi kondisi Behavior Tree 
      task.wait(0.2) 
  end 
  ```
* **Catatan Dosen:** Ini bukan skrip sistem AI. Mahasiswa S1 Informatika **wajib menampilkan fungsi evaluasi arsitektur Behavior Tree Luau** yang sebenarnya (menunjukkan alur Selector, pemanggilan Sequence, pengambilan jarak via `.Magnitude`, dan aksi NPC).

---

### 📊 E. Inkonsistensi Instrumen UAT (Subbab 2.9 vs Tabel 3.8)
* **Subbab 2.9 (hal. 19):** Analisis UAT ditetapkan menggunakan **skor rata-rata Likert** $\bar{x} = \frac{\sum x}{n}$ dengan interpretasi interval 1,00 – 5,00 (Tabel 2.2).
* **Tabel 3.8 (hal. 37 / PDF hal. 49):** Baris rekapitulasi di bawah tabel justru memuat: `Total`, `Total x Skala`, `Jumlah Skala`, `Jumlah Skor`, dan `Persentase (%)`.
* **Solusi:** Hapus baris persentase tersebut dan sesuaikan menjadi: **Total Skor ($\sum x$)**, **Rata-rata Skor ($\bar{x}$)**, dan **Kategori Interpretasi**.

---

### 🧪 F. Kasus Uji Black Box Belum Lengkap (Tabel 3.6)
* Belum ada kasus uji fungsional untuk menguji pemicu respon panik akibat **batas waktu simulasi (`SimulationTime <= 60 detik`)**, padahal variabel ini adalah salah satu kondisi kunci di formula `IsPanicLevelHigh`. Tambahkan 1 baris skenario uji untuk *Panic Timeout*.

---

## 📚 3. Audit Forensik Tinjauan Pustaka & Bibliografi (Bab II & Daftar Pustaka)

### 🚨 A. Anomali Karakter Hangul Korea pada Daftar Pustaka (Hal. 40 / PDF Hal. 52)
* **Fakta Temuan Forensik:** Pada entri Lee (2024), tercetak tulisan:
  ```text
  Lee, J.-M., Kim, J.-Y., & 미디어소프트웨어학과성결대학교. (2024). 지능형 NPC의 행동 메커니즘에 따른 계층적 유한 상태 기계와 행동 트리의 효율성 평가...
  ```
* **Penyebab:** Karakter `미디어소프트웨어학과성결대학교` adalah nama departemen kampus di Korea (*Department of Media Software, Sungkyul University*). Saat impor metadata otomatis ke Mendeley/Zotero, afiliasi kampus ini keliru masuk ke kolom nama penulis (Author)!
* **Dampak:** Di teks naskah (hal. 8), mahasiswa mengutipnya sebagai `(Lee et al., 2024)` karena Mendeley mengira ada 3 penulis. Padahal penulis aslinya **hanya dua orang: Jung-Min Lee dan Jin-Young Kim**.
* **Solusi Perbaikan:** Hapus nama departemen Korea tersebut dari kolom penulis di Mendeley. Di teks kutipan naskah, sesuaikan sitasinya menjadi **`(Lee & Kim, 2024)`**.

---

### 🚨 B. Urutan Alfabetis Daftar Pustaka Acak pada Penulis Institusi
* **Fakta Temuan:**
  * Di halaman 40 (PDF hal. 52): `Kementerian Komunikasi dan Informatika` (huruf **K**) diletakkan **sebelum** `Iovino` (huruf **I**).
  * Di halaman 41 (PDF hal. 53): `Kementerian Ekonomi Kreatif` (huruf **K**) diletakkan **setelah** `Partlan` (huruf **P**) dan **sebelum** `Santi` (huruf **S**).
* **Solusi Perbaikan:** Susun kedua rujukan kementerian tersebut berurutan secara alfabetis di bawah huruf **K**:
  1. *Kementerian Ekonomi Kreatif/Badan Ekonomi Kreatif Republik Indonesia. (2024).*
  2. *Kementerian Komunikasi dan Informatika Republik Indonesia. (2022).*

---

### 🚨 C. Inkonsistensi Urutan Baris Tabel 2.1 vs Narasi Subbab 2.1
* Mahasiswa telah merapikan nomor kolom menjadi 1 s.d. 10, namun **susunan baris artikelnya tidak dicocokkan dengan alur teks Subbab 2.1**:
  * Narasi nomor 2 (*Marchelputra*) $\rightarrow$ di Tabel diletakkan di nomor 7.
  * Narasi nomor 3 (*Lee & Kim*) $\rightarrow$ di Tabel diletakkan di nomor 9.
  * Narasi nomor 4 (*Iovino*) $\rightarrow$ di Tabel diletakkan di nomor 2.
* **Solusi:** Urutkan kembali baris Tabel 2.1 agar persis 1 banding 1 dengan nomor urut narasi literatur di teks (halaman 7–10).

---

### 🔍 D. Sitasi Tertinggal, Koreksi Penulis Utama, & Metadata Jurnal
1. **Sitasi Tertinggal:** Artikel `(Lonteng et al., 2024)` dikutip di teks Bab 2 hal. 17 (tahap testing GDLC), tetapi **belum ada di Daftar Pustaka**.
2. **Koreksi Penulis Utama:** Di teks tertulis `(Hasugian, 2023)`. Penulis pertamanya adalah *Wulandari*, sehingga sitasi wajib disesuaikan menjadi **`(Wulandari dkk., 2023)`** atau **`(Wulandari et al., 2023)`**.
3. **Entri BPBD DKI:** Di teks disitasi `(BPBD DKI Jakarta, 2025)`, tetapi di Daftar Pustaka tercetak judul berita dengan tahun `(n.d.)`. Selaraskan penulis dan tahunnya.
4. **Data Bibliografi Lengkap (Siap Salin ke Word/Mendeley):**

```text
Ardiansyah, R. Y. P., & Mashuri, C. (2024). Rancang Bangun Digital Learning System (DLS) Berbasis Gamifikasi Menggunakan Metode Game Development Life Cycle (GDLC). Format : Jurnal Ilmiah Teknik Informatika, 13(1), 66–78.

BPBD DKI Jakarta. (2025). BPBD DKI Catat 1.810 Bencana Terjadi Sepanjang 2024. Badan Penanggulangan Bencana Daerah DKI Jakarta. https://m.beritajakarta.id/read/142306/bpbd-dki-catat-1810-bencana-terjadi-sepanjang-2024

Lee, J.-M., & Kim, J.-Y. (2024). Efficiency Evaluation of Hierarchical Finite-State Machines and Behavior Trees according to Behavior Mechanism of Intelligent NPCs. Journal of the Institute of Internet, Broadcasting and Communication (JIIBC), 24(2), 113–120. https://doi.org/10.7236/JIIBC.2024.24.2.113

Lonteng, A., Montolalu, C., Tenda, E., & Ketaren, E. (2024). Pengembangan Game "Esa Saga: Legacy of the Brave" Menggunakan Game Development Life Cycle. Jurnal TIMES, 13(2), 18–30.

Menora, T., Primasari, C. H., Wibisono, Y. P., Sidhi, T. A. P., Setyohadi, D. B., & Cininta, M. (2023). Implementasi Pengujian Alpha dan Beta Testing pada Aplikasi Gamelan Virtual Reality. KONSTELASI: Konvergensi Teknologi dan Sistem Informasi, 3(1), 24–35. https://doi.org/10.24002/konstelasi.v3i1.6625

Wulandari, W., Nofiyani, N., & Hasugian, H. (2023). User Acceptance Testing (UAT) pada Electronic Data Preprocessing Guna Mengetahui Kualitas Sistem. Jurnal Mahasiswa Ilmu Komputer (JMIK), 4(1), 20–27. https://doi.org/10.24127/ilmukomputer.v4i1.3383
```

---

## 📝 4. Audit Administratif, Sistematika Penulisan, & Tipografi

1. **Hilangnya Subbab 1.7 (Sistematika Penulisan):**
   * Bab I berhenti mendadak di Subbab 1.6 (Kontribusi Penelitian). Standar FT UNMUL mewajibkan adanya **Subbab 1.7 Sistematika Penulisan** yang menguraikan ringkasan isi Bab I s.d. Bab V.
2. **Halaman Pengesahan (Hal. ii):**
   * Masih berupa placeholder. Wajib diisi:
     * **Pembimbing I:** Aulia Khoirunnita, S.Kom., M.Kom. (NIP: `199308172023212069`)
     * **Pembimbing II:** Anton Prafanto, S.Kom., M.T. (NIP: `199310222019031016`)
3. **Kata Pengantar (Hal. iii):**
   * Hapus butir 6 & 7 (ucapan terima kasih ke dosen penguji belum berlaku pada proposal skripsi).
   * Ganti kata tidak baku `masukkan` menjadi kata baku **`masukan`** (KBBI: masukan = input/saran).
   * Lengkapi titimangsa `Samarinda, September 2026` dan hapus teks `DAFTAR ISI` yang terselip di bawah.
4. **Header Kolom Daftar Istilah/Lambang Terpotong (Hal. ix / PDF Hal. 10):**
   * Header tabel hanya tertulis `Arti` (header kolom kiri `Istilah` hilang).
   * Istilah `APAR` terduplikasi di Daftar Istilah dan Daftar Singkatan.
5. **Layout Tabel 2.1 Terpotong & Melompat:**
   * Ubah *Text Wrapping* Tabel 2.1 dari *Around* menjadi *None* (*In Line with Text*) agar baris 9–10 tidak melompat ke bawah Subbab 2.3.
6. **Matriks Tabel 3.9 Jadwal Penelitian:**
   * Isi tanda centang ($\checkmark$) atau blok warna pada bulan-bulan rencana kegiatan (Juni–Desember 2026), lalu masukkan judulnya ke Daftar Tabel di halaman preliminer.
7. **Koreksi Typo Kata:**
   * Daftar Isi (hal. v) & Subbab 2.2 (hal. 12): *"Pembalajaran"* $\rightarrow$ ganti menjadi **`Pembelajaran`**.
   * Tabel 2.1 baris 8: ganti *"enam state"* $\rightarrow$ **`empat (4) state`**.
   * Hal. 2: beri spasi sebelum tanda kurung: *"jalur keluar (Bata & Defira, 2023)"*.

---

## 🎯 5. Checklist Final Mahasiswa Menuju Lembar ACC

- [ ] Tambahkan **Subbab 1.7 Sistematika Penulisan** di akhir Bab I.
- [ ] Sinkronkan status node `IsPathSafe` antara narasi, Tabel 3.5, dan Gambar 3.2.
- [ ] Tentukan ambang batas kuantitatif jarak untuk `IsFireVeryNear` ($\le 3\text{ meter}$).
- [ ] Tambahkan penjelasan konversi satuan jarak Roblox ($5\text{ m} \approx 18\text{ studs}$).
- [ ] Lengkapi Subbab 3.4.2 dengan pseudocode/fungsi Luau evaluasi Behavior Tree.
- [ ] Sesuaikan baris rekapitulasi Tabel 3.8 dengan rumus rata-rata skor UAT di Subbab 2.9.
- [ ] Tambahkan skenario uji batas waktu simulasi (*panic timeout*) pada Tabel 3.6 Black Box.
- [ ] Hapus karakter Hangul Korea pada rujukan Lee (2024) di Mendeley dan ubah sitasi teks menjadi `(Lee & Kim, 2024)`.
- [ ] Rapikan urutan abjad institusi (*Kementerian*) pada Daftar Pustaka.
- [ ] Susun ulang baris Tabel 2.1 agar sesuai 1 banding 1 dengan urutan narasi 10 literatur Subbab 2.1.
- [ ] Atur *Text Wrapping* Tabel 2.1 menjadi *None* agar baris 9–10 menyambung rapi.
- [ ] Tambahkan Lonteng dkk. (2024) ke Daftar Pustaka dan lengkapi metadata 3 jurnal lainnya.
- [ ] Ubah sitasi `(Hasugian, 2023)` menjadi `(Wulandari dkk., 2023)`.
- [ ] Isi Halaman Pengesahan (NIP Pembimbing I & II) dan rapikan Kata Pengantar (hapus butir penguji, perbaiki kata masukan).
- [ ] Isi matriks jadwal Tabel 3.9 dan daftarkan ke Daftar Tabel.
- [ ] Perbaiki typo *Pembalajaran* $\rightarrow$ *Pembelajaran* dan ganti kata *enam state* $\rightarrow$ *empat state*.

---

## 💬 6. Draf Pesan Balasan WhatsApp Dosen ke Mahasiswa

Pak Anton dapat langsung menyalin pesan bimbingan komprehensif berikut:

```text
Wa'alaikumsalam wr. wb. Ahmad Dhafin,

Saya sudah melakukan audit mendalam terhadap draf revisi 1 proposal skripsi kamu. 

Secara keseluruhan, progres kamu SANGAT BAIK! Struktur Behavior Tree di Gambar 3.2 sudah benar, rumus kepanikan sudah masuk, dan format dokumen sudah jauh lebih rapi.

Namun, agar proposal kamu benar-benar matang, berbobot, dan tidak dicecar oleh dewan penguji saat Seminar Proposal nanti, tolong perbaiki poin-poin krusial berikut:

1. Logika Behavior Tree & Scripting (Bab 3):
   - Di Tabel 3.5 ada node 'IsPathSafe', tapi di diagram Gambar 3.2 node tersebut tidak ada. Tolong disinkronkan.
   - Kamu menulis formula kepanikan untuk jarak <= 5 meter. Namun di cabang prioritas 1 ada kondisi 'IsFireVeryNear'. Tolong tentukan batas jaraknya secara pasti (misal: <= 3 meter) agar logikanya tidak bentrok.
   - Tambahkan catatan bahwa di Roblox Studio jarak 5 meter dikonversikan menjadi 18 studs (1 meter ≈ 3.57 studs).
   - Di Subbab 3.4.2, jangan cuma menampilkan perulangan 'while true do task.wait(0.2) end' yang kosong. Tampilkan potongan fungsi Luau evaluasi Behavior Tree-nya.
   - Di Tabel 3.8 (UAT), ganti baris 'Persentase (%)' di bawah tabel menjadi 'Rata-rata Skor' agar sinkron dengan rumus Bab 2.9.

2. Tinjauan Pustaka & Bab 1:
   - Tambahkan Subbab 1.7 (Sistematika Penulisan) di Bab 1 untuk menjelaskan alur Bab 1 s.d. Bab 5.
   - Susun ulang baris di Tabel 2.1 agar urutan artikelnya sama persis dengan urutan narasi 10 penelitian di teks Subbab 2.1.
   - Atur Text Wrapping Tabel 2.1 menjadi 'None' agar baris 9-10 tidak melompat ke bawah Subbab 2.3.
   - Ubah kata 'enam state' di Tabel 2.1 nomor 8 menjadi 'empat state'.

3. Sitasi & Daftar Pustaka:
   - Periksa Daftar Pustaka entri Lee (2024): ada tulisan huruf Korea '미디어소프트웨어학과성결대학교' yang keliru masuk sebagai nama penulis di Mendeley (itu nama departemen kampus di Korea). Hapus itu dan di teks kutip sebagai (Lee & Kim, 2024).
   - Rapikan urutan abjad untuk entri Kementerian.
   - Tambahkan referensi Lonteng dkk. (2024) ke Daftar Pustaka dan lengkapi nama jurnal rujukan Ardiansyah, Wulandari/Hasugian, serta Menora.
   - Ubah sitasi '(Hasugian, 2023)' menjadi '(Wulandari dkk., 2023)'.

4. Format & Administrasi:
   - Lengkapi nama pembimbing & NIP di Halaman Pengesahan (Pembimbing I: Ibu Aulia Khoirunnita, S.Kom., M.Kom. [NIP: 199308172023212069] / Pembimbing II: Pak Anton Prafanto, S.Kom., M.T. [NIP: 199310222019031016]).
   - Di Kata Pengantar, hapus butir 6 & 7 (dosen penguji belum perlu dicantumkan), isi tanggal Samarinda, dan bersihkan teks 'DAFTAR ISI' yang terselip di bawah.
   - Isi tanda centang/arsiran pada matriks Tabel 3.9 Jadwal Penelitian, lalu masukkan ke Daftar Tabel.

Detail catatan dan rujukan jurnal lengkap sudah saya susun. Silakan langsung disempurnakan di Word. Jika poin-poin ini sudah beres, naskah kamu sudah siap 100% dan langsung saya ACC untuk daftar Sempro. Tetap semangat!
```

---
*Laporan evaluasi komprehensif ini menjamin proposal mahasiswa memiliki kematangan akademik, presisi teknis, dan kesiapan penuh menghadapi Ujian Seminar Proposal.*

