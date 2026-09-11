# 📋 LAPORAN EVALUASI & VERIFIKASI REVISI ARAHAN PEMBIMBING II (BU NOVI)

**Mahasiswa Bimbingan:** Muhammad Annur Akbar (NIM: 2309106110)  
**Program Studi:** S1 Informatika, Fakultas Teknik, Universitas Mulawarman  
**Dosen Pembimbing I:** Anton Prafanto, S.Kom., M.T.  
**Dosen Pembimbing II:** Ir. Novianti Puspitasari, S.Kom., M.Eng.  
**Koordinator Program Studi:** Awang Harsa Kridalaksana, S.Kom., M.Kom. (NIP 19731229 200501 1 002)  
**Judul Naskah:** *Rancang Bangun Perangkap Hama Cahaya Berbasis Raspberry Pi 4 dengan Algoritma YOLOv5*  
**Dokumen yang Diverifikasi:** `PROPOSAL_SKRIPSI_Muhammad_Annur_Akbar_FIX (2).pdf` / `.docx` (56 Halaman)  
**Status Evaluasi:** **SUBSTANSI SANGAT MEMUASKAN — TINGGAL MERAPIKAN 2 MASALAH TEKNIS DOKUMEN SEBELUM CETAK/TANDA TANGAN RESMI**

---

> [!NOTE]
> **Tinjauan Pembimbing:** Dokumen ini merupakan hasil verifikasi atas revisi proposal yang dilakukan oleh Muhammad Annur Akbar berdasarkan 3 arahan khusus dari Dosen Pembimbing II (Ibu Ir. Novianti Puspitasari, S.Kom., M.Eng.), sekaligus audit forensik menyeluruh untuk memastikan penambahan elemen baru tidak merusak struktur dokumen sebelum pendaftaran Ujian Seminar Proposal.

---

## 🌟 1. Verifikasi Pelaksanaan 3 Arahan Bu Novi

Mahasiswa telah menindaklanjuti seluruh arahan Ibu Novianti Puspitasari dengan sangat baik dan tepat:

| No | Arahan Revisi Bu Novi | Realisasi Mahasiswa pada Naskah FIX (2) | Evaluasi Mutu |
| :---: | :--- | :--- | :---: |
| **1** | **Pemisahan Penjabaran Tabel 3.1** | Pada versi sebelumnya, indikator variabel bebas dan kontrol digabung dalam satu baris kalimat panjang. Pada naskah baru, mahasiswa telah **memecah masing-masing indikator ke dalam baris tersendiri** yang terstruktur rapi:<br>• *Variabel Bebas:* Kelas hama, waktu malam (18.00–06.00), dan kondisi jaringan (online/offline).<br>• *Variabel Kontrol:* Raspberry Pi 4 (RAM 4GB), Webcam C270, Lampu UV 22W, interval 15 menit, model YOLOv5n (imgsz 640), dan ambang inferensi. | ✅ **Sangat Rapi & Jelas** |
| **2** | **Diagram 3.1 Diubah Menjadi Menurun** | Diagram alir penelitian yang sebelumnya berbentuk horizontal memanjang (7,07 × 3,56 inci) telah **dirombak total menjadi diagram vertikal menurun (*portrait*)** berukuran 5,04 × 7,72 inci pada halaman 24. Alur tahapan penelitian menjadi jauh lebih mudah dibaca dan logis. | ✅ **Sesuai Arahan** |
| **3** | **Penambahan Gambaran Bot Telegram (Subbab 3.5)** | Mahasiswa telah menambahkan 2 gambar ilustrasi/mockup antarmuka Bot Telegram yang sangat representatif:<br>• **Gambar 3.3 (Hal. 33):** Rancangan Antarmuka Perintah Interaktif (`/start`, `/report`, `/photo`, `/alarm`, `/stop_alarm`).<br>• **Gambar 3.4 (Hal. 34):** Rancangan Antarmuka Notifikasi Otomatis (Laporan berkala 3 jam, status DANGER saat $N_{\text{jam}}$ melampaui Ambang, dan notifikasi susulan pasca-offline). | ✅ **Sangat Informatif** |

*Catatan Positif Tambahan:* Daya lampu atraktan UV telah dimutakhirkan secara konsisten di seluruh teks dokumen (Bab I, Bab II, Bab III, Tabel, dan Lampiran) dari 15 Watt menjadi **22 Watt** sesuai dengan lampu fisik yang dipasang di lapangan.

---

## 🚨 2. Temuan Baru Akibat Penambahan Elemen (Wajib Dirapikan Sebelum Cetak)

Penambahan Gambar 3.3, Gambar 3.4, dan perluasan Tabel 3.1 menyebabkan volume naskah bertambah 3 halaman (dari 53 menjadi 56 halaman). Hal ini memicu beberapa efek samping teknis pada MS Word yang perlu dirapikan oleh mahasiswa:

### 🚨 1. Error Bookmark pada DAFTAR GAMBAR (Hal. viii / PDF Hal. 9)
* **Temuan:** Pada Daftar Gambar, entri Gambar 3.3 tertulis:  
  `Gambar 3.3 Rancangan Antarmuka Perintah Interaktif Bot Telegram ...Error! Bookmark not defined.`
* **Penyebab:** Field *Table of Figures* di MS Word kehilangan tautan bookmark akibat duplikasi caption.

### 🚨 2. Teks Caption Gambar 3.3 dan Gambar 3.4 Dobel & Ada Typo Angka 1
* **Temuan pada Halaman 33 (PDF Hal. 45):**  
  ```text
  Gambar 3.3 1Rancangan Antarmuka Perintah Interaktif Bot Telegram
  Gambar 3.3 Rancangan Antarmuka Perintah Interaktif Bot Telegram
  ```
* **Temuan pada Halaman 34 (PDF Hal. 46):**  
  ```text
  Gambar 3.4 1Rancangan Antarmuka Notifikasi Otomatis Bot Telegram
  Gambar 3.4 Rancangan Antarmuka Notifikasi Otomatis Bot Telegram
  ```
* **Penyebab:** Di file Word terdapat dua baris paragraf caption bertumpuk di bawah gambar (satu bergaya *Caption* yang terselip angka 1, dan satu bergaya *Normal*).
* **Solusi di Word:** Hapus salah satu baris caption yang dobel, pastikan hanya ada satu baris caption resmi bergaya *Caption*, dan hapus angka `1` di depan kata `Rancangan`.

### 🚨 3. Desinkronisasi Nomor Halaman pada Daftar Tabel, Gambar, dan Lampiran
Mahasiswa sudah meng-update Daftar Isi (TOC), tetapi **Daftar Tabel, Daftar Gambar, dan Daftar Lampiran belum di-update (*Update Field*)**, sehingga nomor halamannya tertinggal 2 hingga 4 halaman:

| Daftar | Entri Dokumen | Halaman Tertulis di Naskah | Letak Fisik Aktual di Naskah | Selisih |
| :--- | :--- | :---: | :---: | :---: |
| **Daftar Tabel** | Tabel 3.1 Variabel Penelitian | 23 | **25** | -2 hal |
| | Tabel 3.2 Rencana Dataset | 25 | **28** | -3 hal |
| | Tabel 3.3 Skenario Pengujian | 31 | **35** | -4 hal |
| | Tabel 3.4 Jadwal Penelitian | 32 | **36** | -4 hal |
| **Daftar Gambar** | Gambar 3.1 Diagram Alir Penelitian | 22 | **24** | -2 hal |
| | Gambar 3.2 Diagram Pemrosesan | 27 | **30** | -3 hal |
| | Gambar 3.3 Antarmuka Interaktif | *Error! Bookmark* | **33** | - |
| | Gambar 3.4 Notifikasi Otomatis | 34 | **34** | Sinkron |
| **Daftar Lampiran** | Lampiran 1 Surat Pengantar/Izin | 37 | **41** | -4 hal |
| | Lampiran 2 Pinout Raspberry Pi 4 | 38 | **42** | -4 hal |
| | Lampiran 3 Observasi Lapangan | 38 | **42** | -4 hal |
| | Lampiran 4 Source Code | 40 | **44** | -4 hal |

* **Solusi di Word:**  
  1. Blok seluruh dokumen (`Ctrl + A`), lalu tekan tombol keyboard **`F9`**.
  2. Ketika muncul kotak dialog pembaruan daftar, pilih opsi **"Update entire table"** (*Perbarui seluruh tabel*) untuk Daftar Isi, Daftar Tabel, Daftar Gambar, dan Daftar Lampiran.
  3. Dengan langkah ini, seluruh nomor halaman akan otomatis sinkron 100% dan bebas dari error bookmark.

---

## 🎯 3. Kesimpulan & Rekomendasi Dosen Pembimbing

* **Substansi Ilmiah:** Naskah proposal skripsi Muhammad Annur Akbar sudah **100% matang, komprehensif, dan disetujui (ACC)** baik oleh Pembimbing I maupun Pembimbing II.
* **Tindakan Mahasiswa:** Mahasiswa hanya memerlukan waktu 5–10 menit untuk merapikan baris caption dobel dan menekan `F9` untuk sinkronisasi daftar halaman di Word, kemudian naskah dapat langsung dicetak untuk penandatanganan berkas pendaftaran Seminar Proposal Skripsi.

---
*Laporan verifikasi akademik ini disusun oleh Tim Pembimbing untuk menjamin kerapian formalia karya ilmiah mahasiswa Muhammad Annur Akbar (NIM: 2309106110).*
