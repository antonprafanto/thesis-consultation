# 📋 LAPORAN AUDIT KOMPREHENSIF & PANDUAN REVISI PROPOSAL SKRIPSI

**Kepada Mahasiswa:** Ahmad Dhafin (NIM: 2209106122)  
**Program Studi:** S1 Informatika, Fakultas Teknik, Universitas Mulawarman  
**Dosen Pembimbing:** Anton Prafanto, S.Kom., M.T.  
**Judul Proposal:** *Pengembangan Mini Game Edukatif Simulasi Penanganan Kebakaran Berbasis Roblox Menggunakan Behavior Tree*  
**Tanggal Evaluasi:** 26 Agustus 2026  
**Status Naskah:** **Diterima dengan Catatan Revisi (Wajib Diperbaiki Sebelum Seminar Proposal)**

---

## 🌟 1. Apresiasi & Kekuatan Naskah

Secara umum, proposal skripsi ini memiliki konsep yang **sangat menarik dan relevan**:
1. **Topik Aplikatif & Kontekstual:** Pemanfaatan platform Roblox Studio untuk simulasi tanggap darurat di Gedung Baru Fakultas Teknik UNMUL merupakan langkah cerdas dan efisien biaya tanpa menuntut perangkat VR mahal.
2. **Kajian Literatur (Bab 2) Kuat:** Perbandingan 10 penelitian terdahulu yang dirangkum dalam matriks perbedaan penelitian berhasil menunjukkan *research gap* yang jelas.
3. **Perancangan Visual Terstruktur:** Penyusunan *storyboard*, *wireframe*, serta model eksterior/interior 3D memberikan gambaran alur simulasi yang konkret.

---

## 🚦 2. Matriks Status Kesiapan Naskah

| Komponen | Status | Catatan Evaluasi Utama |
| :--- | :---: | :--- |
| **Format & Kelengkapan Awal** | ⚠️ *Perlu Perapian* | Hilangkan *Error! Bookmark not defined*, lengkapi *placeholder* & hapus balon komentar Word. |
| **Bab I: Pendahuluan** | ⚠️ *Revisi Sedang* | Sinkronkan kata judul di latar belakang, perbaiki rumusan masalah vs metode uji, tetapkan istilah *mini game*. |
| **Bab II: Tinjauan Pustaka** | 🚨 *Revisi Mayor* | Urutkan nomor pada Tabel 2.1 (saat ini meloncat-loncat), kembalikan rumus UAT yang hilang, bersihkan sitasi rusak. |
| **Bab III: Metodologi & AI** | 🚨 *Revisi Mayor* | Ganti Flowchart Gambar 3.2 dengan Diagram Hierarki *Behavior Tree*, definisikan formula PanicLevel, sinkronkan 4 status NPC, dan lengkapi arsitektur scripting Roblox. |
| **Daftar Pustaka & Sitasi** | 🚨 *Revisi Mayor* | **Wajib beralih menggunakan Mendeley / Zotero** untuk mengeliminasi *ghost citations*, melengkapi metadata jurnal, dan format APA 7th otomatis. |

---

## 🔍 3. Rincian Catatan Revisi & Solusi Perbaikan Bab per Bab

### 📄 Bagian Awal Naskah (Cover s.d. Daftar Singkatan)

1. **Hilangkan "Error! Bookmark not defined":**
   * Pada Daftar Isi (hal. iv–v), Daftar Tabel (hal. vi), dan Daftar Gambar (hal. vii), masih banyak tautan rusak bertuliskan *Error! Bookmark not defined*.
   * **Solusi:** Di Microsoft Word, pastikan heading telah diatur dengan benar, lalu klik kanan pada Daftar Isi > pilih **Update Field** > **Update entire table**.
2. **Lengkapi Template Kata Pengantar (Halaman iii):**
   * Masih terdapat teks bawaan template: *Nama dan gelar akademik Dekan...*, *Nama Dosen Pembimbing...*, dan *Samarinda, ........... 2026*.
   * Balon komentar Word (*Commented [1]: Menggunakan sapaan Bapak atau Ibu...*) ikut tercetak ke PDF. Hapus seluruh komentar Word sebelum ekspor final.
3. **Halaman Pengesahan (Halaman ii):**
   * Lengkapi nama pembimbing I dan II beserta gelar dan tanggal pembahasan rapat.
4. **Daftar Lampiran (Halaman viii):**
   * Tertulis *Lampiran 1 contents 42*. Jika instrumen kuesioner belum dilampirkan, hapus sementara daftar lampiran atau cantumkan instrumen draft kuesioner di halaman belakang.

---

### 📘 BAB I – Pendahuluan

1. **Konsistensi Judul Proposal:**
   * Di Halaman Judul tertulis: *"BERBASIS ROBLOX MENGGUNAKAN BEHAVIOR TREE"*.
   * Namun di paragraf penutup Latar Belakang (hal. 4, baris 267) tertulis: *"BERBASIS 3D MENGGUNAKAN BEHAVIOR TREE"*. Kata *Roblox* hilang. Samakan agar konsisten!
2. **Standarisasi Istilah "Mini Game":**
   * Pilih salah satu istilah baku dan gunakan secara konsisten di seluruh naskah:
     - Bahasa Inggris: *mini-game* atau *mini game* (dicetak miring / *italic*).
     - Bahasa Indonesia: gim mini (tegak).
     *(Hindari mencampuradukkan Mini games, mini-game, dan mini games tanpa aturan baku).*
3. **Penyempurnaan Rumusan Masalah (Subbab 1.2, Hal. 4):**
   * **Masalah:** Rumusan Masalah menggunakan kata *"Bagaimana **performa** Behavior Tree..."*. Kata *"performa"* menuntut adanya pengujian teknis kuantitatif (misal: *latency pengambilan keputusan*, *frame rate FPS*, atau konsumsi memori script). Sedangkan di Bab 3, pengujian kamu berfokus pada **kesesuaian fungsionalitas (Black Box)** dan **penerimaan pengguna (UAT)**.
   * **Rekomendasi Redaksi:**
     > **1.2 Rumusan Masalah:**  
     > 1. Bagaimana merancang dan mengimplementasikan arsitektur *Behavior Tree* dalam mengendalikan perilaku dinamis *Non-Player Character* (NPC) pada *mini-game* simulasi penanganan kebakaran berbasis Roblox?  
     > 2. Bagaimana hasil pengujian fungsionalitas sistem menggunakan *Black Box Testing* dan tingkat penerimaan pengguna menggunakan *User Acceptance Testing* (UAT) terhadap media simulasi yang dikembangkan?
4. **Penyelarasan Tujuan Penelitian (Subbab 1.4, Hal. 5):**
   * Rumusan tujuan harus menjawab secara langsung dan simetris butir-butir rumusan masalah di atas.

---

### 📗 BAB II – Tinjauan Pustaka

1. **🚨 KRUSIAL: Urutan Nomor pada Tabel 2.1 (Perbedaan Penelitian) Berantakan:**
   * Pada naskah saat ini, nomor urut tabel tersusun: **1, 4, 5, 6, 10, 8, 2, 7, 3, 9**.
   * Ini kesalahan fatal yang menunjukkan tabel belum dirapikan setelah pemindahan data. **Urutkan kembali menjadi 1 sampai 10 secara berurutan.**
2. **🚨 Rumus Analisis Data UAT Hilang (Subbab 2.9, Hal. 20):**
   * Pada teks tertulis keterangan variabel $\bar{x}$, $\sum x$, dan $, namun objek rumus matematikanya kosong / tidak tercetak.
   * **Wajib Dilengkapi:** Tampilkan rumus perhitungan rata-rata skor Likert:
     \bar{x} = \frac{\sum x}{n}
     *(di mana $\bar{x}$ = skor rata-rata, $\sum x$ = jumlah skor responden, $ = total responden)*.
3. **Salah Nomor Gambar pada Teks (Subbab 2.6.1, Hal. 15):**
   * Di teks tertulis: *"Gambar 2.6 menunjukkan struktur dasar Behavior Tree..."*, padahal label gambarnya adalah **Gambar 2.1**.
4. **Paragraf Berulang pada Subbab 2.10 (Black Box Testing, Hal. 20):**
   * Kalimat *"Teknik yang umum digunakan dalam Black Box Testing meliputi equivalence partitioning, boundary value analysis, dan use case testing..."* tertulis dua kali berturut-turut. Hapus salah satu pengulangannya.
5. **Format Sitasi Rusak di Tengah Kalimat (Subbab 2.7, Hal. 17):**
   * Tertulis: *"...digunakan sebagai (Lonteng et al., 2024)acuan dalam pengembangan..."*. Rapikan posisi sitasi di akhir kalimat.

---

### 📙 BAB III – Metodologi Penelitian

#### 🚨 1. PERBAIKAN UTAMA: Ganti Flowchart Gambar 3.2 Menjadi Diagram Hierarki Behavior Tree
* **Masalah:** Gambar 3.2 (hal. 27) saat ini adalah **Flowchart IF-ELSE bersyarat**, bukan diagram pohon hierarki *Behavior Tree*.
* **Solusi Wajib:** Ganti Gambar 3.2 dengan diagram pohon hierarki *Behavior Tree* standar berikut:

`mermaid
graph TD
    %% Styling Classes
    classDef rootStyle fill:#1A202C,stroke:#2D3748,stroke-width:2px,color:#fff,font-weight:bold;
    classDef selectorStyle fill:#DD6B20,stroke:#C05621,stroke-width:2px,color:#fff,font-weight:bold;
    classDef sequenceStyle fill:#3182CE,stroke:#2B6CB0,stroke-width:2px,color:#fff,font-weight:bold;
    classDef conditionStyle fill:#6B46C1,stroke:#553C9A,stroke-width:2px,color:#fff;
    classDef actionStyle fill:#2F855A,stroke:#276749,stroke-width:2px,color:#fff;

    %% Root & Main Selector
    ROOT["<b>[ Root Node ]</b>"]:::rootStyle
    SEL["<b>? Selector</b><br>(Prioritas Evaluasi Kondisi)"]:::selectorStyle

    %% Cabang 1: Bahaya Api Sangat Dekat
    SEQ1["<b>→ Sequence</b><br>Bahaya Api Dekat"]:::sequenceStyle
    COND1["<b>Condition:</b><br>IsFireVeryNear == True"]:::conditionStyle
    ACT1["<b>Action:</b><br>Evacuate (Titik Kumpul)"]:::actionStyle

    %% Cabang 2: Interaksi & Bantuan Pemain
    SEQ2["<b>→ Sequence</b><br>Ikuti Arahan Pemain"]:::sequenceStyle
    COND2["<b>Condition:</b><br>HasPlayerInteracted == True"]:::conditionStyle
    ACT2["<b>Action:</b><br>FollowPlayer"]:::actionStyle

    %% Cabang 3: Kepanikan Tinggi
    SEQ3["<b>→ Sequence</b><br>Respon Panik Mandiri"]:::sequenceStyle
    COND3["<b>Condition:</b><br>IsPanicLevelHigh == True"]:::conditionStyle
    ACT3["<b>Action:</b><br>Evacuate (Lari Mandiri)"]:::actionStyle

    %% Cabang 4: Alarm Aktif (Menunggu Bantuan)
    SEQ4["<b>→ Sequence</b><br>Darurat Menunggu Bantuan"]:::sequenceStyle
    COND4["<b>Condition:</b><br>IsAlarmActive == True"]:::conditionStyle
    ACT4["<b>Action:</b><br>WaitForHelp"]:::actionStyle

    %% Cabang 5: Fallback Normal
    ACT_IDLE["<b>Action:</b><br>Idle (Kondisi Normal)"]:::actionStyle

    %% Hubungan Node
    ROOT --> SEL
    SEL --> SEQ1
    SEL --> SEQ2
    SEL --> SEQ3
    SEL --> SEQ4
    SEL --> ACT_IDLE

    SEQ1 --> COND1
    SEQ1 --> ACT1

    SEQ2 --> COND2
    SEQ2 --> ACT2

    SEQ3 --> COND3
    SEQ3 --> ACT3

    SEQ4 --> COND4
    SEQ4 --> ACT4
`

> **Logika Eksekusi (*Tick Evaluation*):**
> Evaluasi dilakukan periodik dari kiri ke kanan:
> 1. **Prioritas 1 (Bahaya Api Dekat):** Jika IsFireVeryNear == True, NPC langsung melakukan aksi Evacuate (menyelamatkan diri ke titik kumpul terdekat).
> 2. **Prioritas 2 (Interaksi Pemain):** Jika pemain mengajak/berinteraksi (HasPlayerInteracted == True), NPC menjalankan FollowPlayer.
> 3. **Prioritas 3 (Kepanikan Tinggi):** Jika kepanikan tinggi (IsPanicLevelHigh == True), NPC otomatis menjalankan Evacuate.
> 4. **Prioritas 4 (Alarm Aktif):** Jika alarm aktif namun belum ada interaksi (IsAlarmActive == True), NPC menjalankan WaitForHelp.
> 5. **Prioritas 5 (Fallback):** Jika semua kondisi di atas False, NPC berstatus Idle.

---

#### 🚨 2. Definisi & Aturan Variabel PanicLevel
* **Masalah:** Di Tabel 3.4 dan Tabel 3.5 terdapat node IsPanicLevelHigh, tetapi tidak ada penjelasan mengenai bagaimana nilai kepanikan dihitung.
* **Solusi Wajib:** Tambahkan penjelasan matematis/logika di Bab 3 mengenai pemicu status PanicLevel:
  \text{IsPanicLevelHigh} = \begin{cases} \text{True}, & \text{jika } \text{FireDistance} \le 5\,\text{meter} \text{ atau } \text{SimulationTime} \le 60\,\text{detik} \\ \text{False}, & \text{lainnya} \end{cases}

---

#### 3. Sinkronisasi Jumlah State Perilaku NPC (4 Status Konsisten)
* Di Batasan Masalah (Bab 1) dan Tinjauan Pustaka (Bab 2), kamu menyebutkan *"enam (6) state perilaku"*.
* Namun di Bab 3 (Tabel 3.3), kamu merancangnya menjadi **4 status**:
  1. Idle
  2. WaitForHelp
  3. FollowPlayer
  4. Evacuate
* *Tindakan:* Sesuaikan seluruh naskah di Bab 1 dan Bab 2 agar konsisten menyatakan **4 status perilaku utama NPC**.

---

#### 4. Koreksi Referensi Label Tabel di Teks Penjelas
Perbaiki nomor referensi tabel pada paragraf penjelas yang salah ketik:
* Hal. 24: Di teks tertulis *"Tabel 3.5"* ➔ Seharusnya **Tabel 3.3**.
* Hal. 25: Di teks tertulis *"Tabel 3.6"* ➔ Seharusnya **Tabel 3.4**.
* Hal. 28: Di teks tertulis *"Tabel 3.7"* ➔ Seharusnya **Tabel 3.5**.

---

#### 5. Tambahkan Spesifikasi Scripting Roblox Studio (Bahasa Luau)
Tambahkan 1–2 paragraf pada Subbab 3.4 yang menjelaskan:
1. **Server vs Client Architecture:** Seluruh logika evaluasi *Behavior Tree* dan perubahan state NPC dieksekusi di sisi **Server (Script)** agar posisi dan respons NPC tersinkronisasi antar-pemain.
2. **Tick Rate & Optimasi Performa:** Evaluasi pohon keputusan (*tick*) dijalankan dengan interval waktu berkala (misal: setiap {,}2$ detik menggunakan 	ask.wait(0.2) di dalam perulangan while true do), bukan di setiap frame RunService.Heartbeat, demi mencegah *server lag*.
3. **Pathfinding:** Pergerakan fisik NPC saat FollowPlayer dan Evacuate memanfaatkan layanan PathfindingService Roblox untuk menghindari rintangan statis maupun titik api dinamis.

---

#### 6. Lengkapi Bagian Waktu, Tempat, dan Jadwal Penelitian (Subbab 3.7)
* Ganti titik-titik lokasi penelitian:
  - *Tempat pelaksanaan:* Gedung Baru Fakultas Teknik Universitas Mulawarman.
  - *Laboratorium analisis:* Laboratorium Rekayasa Perangkat Lunak / Laboratorium Informatika FT UNMUL.
* Ganti label Tabel 3.x Jadwal Penelitian menjadi Tabel 3.9 Jadwal Penelitian dan lengkapi detail baris kegiatan yang masih bertanda titik-titik ….

---

## 📚 4. Audit Silang Sitasi, Daftar Pustaka & Panduan Reference Manager

### 🛠️ A. REKOMENDASI UTAMA: Wajib Gunakan Mendeley atau Zotero!

Banyaknya kesalahan sitasi (sitasi hilang, *ghost citations*, dan metadata tidak lengkap) disebabkan oleh **pengetikan sitasi dan daftar pustaka secara manual**. 

**Mulai saat ini, kamu WAJIB menggunakan Reference Management Software (**Mendeley Reference Manager** atau **Zotero**)** yang diintegrasikan langsung dengan Microsoft Word:

1. **Kenapa Harus Mendeley / Zotero?**
   - **Otomasi 100% Sinkron:** Setiap kali kamu menyisipkan sitasi di naskah (Insert Citation), referensi tersebut akan otomatis muncul di Daftar Pustaka (Insert Bibliography). Tidak akan ada lagi istilah *ghost citation* atau sitasi yang tertinggal.
   - **Standarisasi Format APA 7th:** Software akan otomatis mengatur kapitalisasi judul (*sentence case*), format nama penulis (*et al.*), nama jurnal miring (*italic*), volume/nomor, dan link DOI standar.
   - **Bebas Human Error:** Metadata artikel (judul, penulis, tahun, penerbit) diambil langsung dari database jurnal resmi via DOI atau file PDF.

2. **Langkah Praktis Penggunaan:**
   1. Unduh dan pasang **Mendeley Reference Manager** (atau **Zotero**) di laptop kamu.
   2. Pasang plugin pengolah kata (**Mendeley Cite** untuk MS Word atau **Zotero Word Plugin**).
   3. Masukkan seluruh artikel rujukan ke library Mendeley/Zotero menggunakan fitur *Import by DOI* / *Add PDF* / *Browser Web Importer*.
   4. Hapus seluruh sitasi manual di naskah proposal kamu, lalu ganti dengan menyisipkannya melalui plugin (*Insert Citation*).
   5. Klik *Insert Bibliography* di halaman Daftar Pustaka dan pilih style **American Psychological Association 7th edition (APA 7th)**.

---

### B. Daftar Sitasi di Naskah yang BELUM ADA di Daftar Pustaka (Wajib Diinput ke Mendeley/Zotero):
1. **Aliyah et al., 2024** *(Bab 2, hal. 20)*
2. **Wulandari Putri Bahmin et al., 2025** *(Bab 2, hal. 20)*
3. **Hasugian, 2023** *(Bab 2, hal. 20)*
4. **Global Web Index (GWI), 2024** *(Bab 1, hal. 1)*
5. **Kemenkominfo (2022) & Kemenparekraf (2024)** *(Bab 1, hal. 1)* ➔ Masukkan dokumen/laporan resmi instansi pemerintah, bukan sekadar link berita portal media.

### C. Referensi di Daftar Pustaka yang TIDAK PERNAH DISITASI di Naskah (Wajib Dihapus):
1. **Kemal Pasha, M., & Prabowo, A. (2025)** – Visual Novel Ren'Py (tidak relevan dengan skripsi ini).
2. **Naufal, M. R., et al. (2024)** – Game Warik berbasis FSM (tidak disitasi di teks).
3. **Simanjuntak, S. M., & Putra (2025)** – Analisis Usability SUS (Dhafin menggunakan UAT Likert, bukan SUS).

### D. Data Sitasi yang Tidak Lengkap (Lengkapi Volume, Nomor, Halaman di Library):
1. **Ardiansyah, R., Putra, Y., & Mashuri, C. (2024)** ➔ Nama jurnal, volume, dan nomor halaman belum ada.
2. **Lonteng, A., et al. (2024)** ➔ Nama jurnal tidak dicantumkan lengkap.
3. **Menora, T., et al. (2023)** ➔ Nama jurnal penerbit tidak dicantumkan.

---

## 🎯 5. Pertanyaan Latihan untuk Persiapan Seminar Proposal

Pelajari dan siapkan jawaban untuk pertanyaan kritis yang berpotensi diajukan dosen penguji:

1. **"Mengapa memilih Behavior Tree dibanding Finite State Machine (FSM) yang lebih sederhana?"**  
   *Jawaban yang tepat:* *Behavior Tree* memiliki sifat modularitas tinggi dan evaluasi berbasis prioritas (*Selector & Sequence*). Jika ingin menambah perilaku baru (misal: NPC memadamkan api atau NPC pingsan), kita hanya perlu menambah sub-pohon tanpa harus mengubah seluruh matriks transisi state seperti pada FSM.
2. **"Bagaimana cara NPC menghindari api saat menuju titik evakuasi di Roblox?"**  
   *Jawaban yang tepat:* Pengambilan keputusan kapan harus evakuasi ditentukan oleh *Behavior Tree*, sedangkan kalkulasi rute fisik di lapangan dilakukan oleh PathfindingService Roblox dengan menambahkan *PathfindingModifier* berbobot tinggi (*cost penalty*) pada area yang terbakar.
3. **"Dari mana penentuan nilai ambang batas PanicLevel pada NPC?"**  
   *Jawaban yang tepat:* Nilai ambang batas *PanicLevel* ditentukan secara deterministik berdasarkan radius deteksi bahaya api ($\le 5\text{ meter}$) dan sisa waktu simulasi ($\le 60\text{ detik}$), yang memicu NPC beralih dari status menunggu bantuan menjadi evakuasi mandiri.
4. **"Mengapa pengujian edukasi ini menggunakan UAT Likert, bukan pre-test dan post-test?"**  
   *Jawaban yang tepat:* Fokus utama skripsi S1 Informatika ini berada pada aspek rekayasa perangkat lunak (*software engineering*) dan implementasi AI pada game. UAT digunakan untuk menguji aspek penerimaan antarmuka, fungsionalitas, dan keterbacaan pesan edukatif oleh pengguna.

---

## ✅ 6. Lembar Checklist Tindak Lanjut Revisi Mahasiswa

Beri tanda centang [v] jika perbaikan berikut telah selesai dikerjakan:

- [ ] Memperbarui Daftar Isi, Daftar Tabel, dan Daftar Gambar sehingga bebas dari Error! Bookmark not defined.
- [ ] Menghapus seluruh balon komentar Word dan mengisi nama pembimbing/dekan pada Kata Pengantar.
- [ ] Menyamakan judul di Halaman Judul dengan paragraf penutup Latar Belakang (mencantumkan *Roblox*).
- [ ] Menyesuaikan Rumusan Masalah 1 dan Tujuan Penelitian (mengganti kata *performa* dengan perancangan dan pengujian kesesuaian perilaku).
- [ ] **Mengurutkan nomor urut 1 sampai 10 secara berurutan pada Tabel 2.1.**
- [ ] Menampilkan rumus perhitungan nilai rata-rata UAT ($\bar{x} = \frac{\sum x}{n}$) di Subbab 2.9.
- [ ] Menghapus kalimat duplikasi pada Subbab 2.10 (Black Box Testing).
- [ ] **MENGGANTI Gambar 3.2 dengan Diagram Hierarki Behavior Tree yang benar.**
- [ ] Mendefinisikan formula dan aturan status PanicLevel di Bab 3.
- [ ] Menyelaraskan jumlah status NPC di seluruh bab menjadi **4 status** (Idle, WaitForHelp, FollowPlayer, Evacuate).
- [ ] Memperbaiki referensi penomoran tabel di narasi Bab 3 (Tabel 3.3, 3.4, 3.5).
- [ ] Menambahkan penjelasan teknis Luau script (Server script, tick rate {,}2\text{s}$, PathfindingService).
- [ ] Melengkapi isian Waktu, Tempat, dan Jadwal Penelitian (Tabel 3.9).
- [ ] **MENGGUNAKAN REFERENCE MANAGER (Mendeley / Zotero)** untuk mengelola seluruh sitasi naskah dan meng-generate Daftar Pustaka secara otomatis (style APA 7th).
- [ ] Memastikan tidak ada lagi sitasi tertinggal (*missing citations*) maupun referensi yang tidak pernah dikutip (*ghost references*).

---
*Laporan audit ini disusun sebagai panduan resmi bimbingan skripsi agar draf proposal siap dan matang untuk diajukan ke Seminar Proposal.*
