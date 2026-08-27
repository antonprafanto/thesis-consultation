# 📋 LAPORAN AUDIT FORENSIK & EVALUASI SIDANG PENDADARAN SKRIPSI

**Mahasiswa Bimbingan:** Muhammad Faqih Ajiputra (NIM: 2209106114)  
**Program Studi:** S1 Informatika, Fakultas Teknik, Universitas Mulawarman  
**Dosen Pembimbing I:** Rosmasari, S.Kom., M.T.  
**Dosen Pembimbing II:** Prof. Dr. Fahrul Agus, S.Si., M.T.  
**Judul Skripsi:** *Long Sequence Time-Series Forecasting pada Pasar Valuta Asing EUR/USD Menggunakan Model Informer*  
**Status Evaluasi:** **DRAF SIDANG PENDADARAN — WAJIB REVISI KRUSIAL SEBELUM UJIAN SKRIPSI**

---

> [!NOTE]
> **Panduan Dosen Pembimbing:** Dokumen ini disusun sebagai evaluasi audit forensik mendalam untuk mempersiapkan mahasiswa menghadapi **Ujian Sidang Pendadaran Skripsi** hingga mematangkan argumentasi ilmiah dan kelayakan naskah akademik.

---

## ⚖️ 1. Resume Evaluasi Akademik Umum

Secara keseluruhan, penelitian ini telah berhasil mengimplementasikan arsitektur *Deep Learning* mutakhir **Informer (ProbSparse Self-Attention)** menggunakan PyTorch untuk peramalan deret waktu panjang (*Long Sequence Time-Series Forecasting / LSTF*) pada pasangan mata uang valuta asing **EUR/USD**. Eksperimen dirancang secara terstruktur dengan menguji 12 kombinasi skenario (*Lookback window*: 48, 96, 192, 384 bar jam; *Prediction horizon*: 1, 4, 8 jam ke depan) menggunakan target stasioner *Log Return* yang kemudian direkonstruksi kembali ke level harga *Close*.

Namun, dari hasil audit forensik komprehensif terhadap 114 halaman naskah draf, ditemukan sejumlah **kelemahan mendasar (*critical scientific & methodological red flags*)**, **kekeliruan konsep aljabar linear**, **kontradiksi parameter pelatihan lintas bab**, **kesalahan formula matematis**, serta **pelanggaran format baku penulisan skripsi (pemuatan belasan halaman source code di Bab IV sementara lembar lampiran dibiarkan kosong)**.

---

## 🚨 2. Temuan Kritis (*Critical Red Flags*) & Kelemahan Metodologi

### 🚨 RED FLAG 1: Ilusi Akurasi Log Return & Jebakan *Naive Persistence Model* (KRITIS!)

* **Masalah:** Model Informer dilatih memprediksi target *Log Return* yang distandarisasi ($Mean \approx 0, Std \approx 1$). Pada data EUR/USD frekuensi 1 jam, rata-rata fluktuasi log return per jam sangat tipis ($\sim 10^{-4}$).
* **Fakta Hasil Pelatihan:** 
  1. *Validation Loss* terhenti pada kisaran **0.968 – 0.970**. Mengingat target memiliki variansi 1.0, nilai MSE 0.97 membuktikan model **hanya mampu menjelaskan $\approx 3.1\%$ variansi return aktual**, sedangkan $96.9\%$ sisanya adalah *unexplained noise*.
  2. Model memprediksi log return kumulatif yang sangat mendekati nol ($\hat{r}_{kumulatif} \approx 0.000001$ s.d. $0.000057$, lihat Tabel 4.10 Hal. 76).
  3. Ketika direkonstruksi dengan rumus $\hat{P}_{t+h} = P_t \times e^{\hat{r}}$, karena $e^0 = 1$, maka $\hat{P}_{t+h} \approx P_t$.
  4. Model secara praktis berperilaku sebagai **Naive Persistence Forecast / Random Walk ($\hat{y}_{t+h} = y_t$)**, yaitu menebak harga jam depan sama persis dengan harga jam terakhir.
* **Dampak saat Sidang:** Mahasiswa membanggakan perolehan MAPE sebesar **0.043% – 0.058%** sebagai performa luar biasa. Penguji *machine learning* akan langsung mencecar bahwa MAPE sekecil itu muncul secara artifisial karena volatilitas EUR/USD memang hanya $\sim 0.05\%$ per jam, bukan karena model Informer mampu memprediksi dinamika pasar dengan akurat.
* **Solusi Wajib:** 
  1. Mahasiswa wajib menambahkan pengujian **Baseline Naive Model ($\hat{y}_{t+h} = y_t$)** sebagai pembanding resmi di Bab IV.
  2. Mahasiswa wajib menghitung metrik **Directional Accuracy (DA / Hit Rate)** untuk membuktikan apakah arah pergerakan naik/turun (*sign of return*) dapat ditebak lebih baik daripada tebakan acak ($>50\%$).
  3. Mahasiswa harus membahas secara terbuka alasan matematis mengapa *validation loss* terhenti di $\sim 0.97$.

---

### 🚨 RED FLAG 2: Kekeliruan Konseptual Aljabar Linear: Istilah "Matriks" Ditulis "Metrik"

Mahasiswa secara berulang dan konsisten salah menuliskan istilah **Matriks (Matrix)** menjadi **Metrik / Metriks (Metric)** dalam penjelasan representasi tensor Informer pada Bab II:

| Lokasi Halaman | Teks Asli pada Naskah | Perbaikan Wajib |
| :--- | :--- | :--- |
| **Hal. 24 (Bab 2)** | `"...sparse query pada metrik Q..."` | `"...sparse query pada matriks Q..."` |
| **Hal. 24 (Bab 2)** | `"...Q = Metrik query, KT = Metrik key..."` | `"...Q = Matriks query, KT = Matriks key..."` |
| **Hal. 24 (Bab 2)** | `"...V = Metrik value..."` | `"...V = Matriks value..."` |
| **Hal. 29 (Bab 2)** | `"...metriks Attention dengan -∞..."` | `"...matriks Attention dengan -∞..."` |
| **Hal. 30 (Bab 2)** | `"...Qde = Metriks query dari Decoder..."` | `"...Qde = Matriks query dari Decoder..."` |
| **Hal. 30 (Bab 2)** | `"...Ken = Metriks key dari output akhir..."` | `"...Ken = Matriks key dari output akhir..."` |
| **Hal. 30 (Bab 2)** | `"...Ven = Metriks value dari output akhir..."` | `"...Ven = Matriks value dari output akhir..."` |
| **Hal. 30 (Bab 2)** | `"...T = Operator transpose pada metriksk key..."` | `"...T = Operator transpose pada matriks key..."` |

* **Dampak:** Di sidang pendadaran Informatika, kerancuan antara *Matriks* (struktur data aljabar linear) dan *Metrik* (ukuran evaluasi performa seperti MAE/MSE) akan menjadi sasaran telak penguji.

---

### 🚨 RED FLAG 3: Diskrepansi & Inkonsistensi Parameter *Early Stopping Patience* (4 Versi Berbeda!)

Terdapat kontradiksi nilai parameter *patience* di empat lokasi berbeda di dalam naskah:

```text
1. Bab III Tabel 3.3 (Hal. 46)          : Patience = 5
2. Bab III Paragraf 1 Teks (Hal. 47)    : Patience = 10   <-- KONTRADIKSI FATAL!
3. Bab IV Gambar 4.12 Kode (Hal. 71)    : def __init__(self, patience=3...)
4. Bab IV Tabel 4.8 Parameter (Hal. 70) : Patience = 5
5. Bab IV Tabel 4.9 Hasil (Hal. 74)     : Berhenti di Epoch 6 (Best Epoch 1) --> Patience = 5
```

* **Solusi Wajib:** Ganti nilai pada teks **Bab III Halaman 47** menjadi **5** agar sinkron dengan Tabel 3.3, Tabel 4.8, dan fakta empiris Tabel 4.9.

---

### 🚨 RED FLAG 4: Klaim Keunggulan Komparatif yang Tidak Valid (Wang et al., 2021)

* **Kutipan Klaim Mahasiswa (Bab IV Hal. 81 / Dokumen P.100):**
  > *"...didapatkan nilai MAPE sebesar 0.043712% ... nilai tersebut lebih rendah sebesar 76.9% dibandingkan dengan hasil dari Wang et al. (2021) [CNN-TLSTM pada USD/CNY sebesar 0.18945%]..."*
* **Kelemahan Metodologi:**
  1. Pasangan mata uang berbeda (**EUR/USD vs USD/CNY**). USD/CNY dikontrol oleh bank sentral Tiongkok dengan volatilitas dan dinamika harian yang sama sekali tidak sebanding dengan EUR/USD.
  2. Dataset, periode tahun, dan horizon prediksi tidak sama.
  3. Wang et al. memprediksi harga nominal secara langsung, sedangkan penelitian ini memprediksi log return.
* **Solusi Wajib:** Hapus klaim bahwa Informer "lebih baik 76.9%". Nyatakan perbandingan tersebut murni sebagai referensi literatur dengan menegaskan batasan perbedaan dataset dan mata uang.

---

### 🚨 RED FLAG 5: Pelanggaran Tata Letak Bab IV (Code Dumping) vs Halaman Lampiran Kosong

* **Bab IV (Hal. 63 – 74):** Memuat **10 gambar tangkapan layar kode Python (Gambar 4.3, 4.5, 4.6, 4.7, 4.8, 4.9, 4.10, 4.11, 4.12, 4.13)** yang memakan lebih dari 12 halaman berharga.
* **Halaman Lampiran (Hal. 93 – 95):** Halaman judul Lampiran 1 s.d. Lampiran 5 **kosong melompong** tanpa lampiran kode dan data pendukung.
* **Solusi Wajib:** Pindahkan seluruh source code ke **Lampiran 1 dan Lampiran 2**. Gantikan ruang di Bab IV dengan diagram arsitektur tensor shape dan pembahasan analitis.

---

### 🚨 RED FLAG 6: Tabel 4.4 Rusak / Error Angka Nol

* **Tabel 4.4 Hasil Validasi Kualitas Data (Hal. 54 / Dokumen P.73):**
  * Baris `Jumlah Kolom` tertulis: `Data Mentah = 0`, `Data Terproses = 0`.
* **Solusi Wajib:** Perbaiki segera menjadi:
  * `Data Mentah = 6` *(date, Open, High, Low, Close, Volume)*.
  * `Data Terproses = 9` *(date, Open, High, Low, Close, Volume, log_return, RSI_14, ATR_14)*.

---

## 📐 3. Audit Notasi & Formula Matematis (Bab II)

Berikut adalah daftar rumus yang wajib diperbaiki sebelum dicetak untuk dewan penguji:

1. **Persamaan (2.9) Rumus True Range (Hal. 20):**
   * *Naskah:* $TR_t = \max(H_t - L_t, |H_t - C_{t-1}|, |L_t - C_{t-1}|$
   * *Koreksi:* Tambahkan kurung penutup $\mathbf{)}$ di akhir formula $ightarrow \max(H_t - L_t, |H_t - C_{t-1}|, |L_t - C_{t-1}|\mathbf{)}$.
2. **Persamaan (2.11) Sparsity Informer (Hal. 24):**
   * *Naskah:* $u = c \cdot \ln L_Q$, teks di bawahnya: `u adalah sampling factor`.
   * *Koreksi:* $c$ adalah *sampling factor* (konstanta hyperparameter, misal $c=5$), sedangkan $u$ adalah *jumlah query dominan terpilih (top-u active queries)*.
3. **Persamaan (2.12) & (2.21) Skala Attention (Hal. 24 & 30):**
   * *Naskah:* $\sqrt{d} = 	ext{Dimensi vektor query/key}$.
   * *Koreksi:* $d$ atau $d_k$ adalah dimensi kunci (*key dimension*), sedangkan $\sqrt{d}$ adalah **faktor penskalaan (*scaling factor*)** untuk mencegah gradien saturasi pada fungsi softmax.
4. **Persamaan (2.14) & (2.15) Distilling Layer (Hal. 25 & 26):**
   * *Naskah:* Tertulis `MaxPoll(ELU(Conv1d...))` dan `MaxPoll(x)_i`.
   * *Koreksi:* Typo istilah, ganti menjadi **$	ext{MaxPool}$** atau **$	ext{MaxPooling}$**.
5. **Duplikasi Nomor Persamaan (2.17) (Hal. 27 & 28):**
   * Rumus Conv1d di Hal. 27 diberi label **(2.17)**, dan rumus FFN di Hal. 28 juga diberi label **(2.17)**.
   * *Koreksi:* Lakukan penomoran ulang (*renumbering*) seluruh persamaan dari FFN sampai akhir Bab II.
6. **Persamaan (2.27) Optimizer Adam (Hal. 34):**
   * *Naskah:* Teks di bawah rumus tertulis `Berdasarkan persamaan 2. 7` (salah rujuk).
   * *Naskah Rumus:* Penyebut tertulis $\sqrt{v_t} + \epsilon$.
   * *Koreksi:* Seharusnya menggunakan estimasi momen kedua terkoreksi bias yaitu $\mathbf{\sqrt{\hat{v}_t} + \epsilon}$.

---

## 📝 4. Audit Kelengkapan Formalia & Tata Tulis Naskah

| Komponen Naskah | Masalah yang Ditemukan | Tindakan Koreksi Mahasiswa |
| :--- | :--- | :--- |
| **Halaman Pengesahan (Hal. iii)** | Terdapat titik ganda pada gelar Pembimbing II: `Prof. Dr.. Fahrul Agus, S.Si., M.T.` | Hapus satu titik menjadi `Prof. Dr. Fahrul Agus, S.Si., M.T.` |
| **Halaman Pengesahan (Hal. iii)** | Teks tanggal masih berupa placeholder `Tgl Bln Tahun` | Masukkan tanggal ujian pendadaran yang telah ditentukan |
| **Kata Pengantar (Hal. vii)** | Tertulis `"...menyelesaikan proposal skripsi..."` dan `"...Proposal ini disusun..."` | **Wajib:** Ganti seluruh kata "proposal" menjadi "skripsi" |
| **Header Halaman Awal Bab** | Judul Bab I, IV, dan V tertulis ganda pada halaman pertama bab (misal: `BAB I PENDAHULUAN 
 PENDAHULUAN`) | Hapus satu baris pengulangan judul bab |
| **Penomoran Subbab Bab II (Hal. 40)** | Tertulis `2.2 Machine Learning...` padahal sebelumnya sudah ada `2.2 Pasar Valuta Asing (FOREX)` | Ganti menjadi `2.3 Machine Learning dan Deep Learning` |
| **Judul Bab III (Hal. 56)** | Tertulis `BAB III METODOLOGI P EN ELITIAN` | Hilangkan spasi berlebih menjadi `METODOLOGI PENELITIAN` |
| **Daftar Istilah & Singkatan (Hal. xiv–xviii)** | Header tabel tertulis `Arti` dan `Contents` | Ubah header tabel menjadi `Istilah / Singkatan` dan `Arti / Keterangan` |
| **Format Istilah Asing** | Istilah asing (*time-series, loss function, epoch, batch size, learning rate, distilling layer*) belum konsisten miring (*italic*) | Lakukan perapian *formatting* cetak miring (*italic*) |

---

## 🎯 5. Panduan Menghadapi Pertanyaan Dewan Penguji Sidang Pendadaran

Berikut adalah daftar pertanyaan inti yang wajib dikuasai mahasiswa saat sesi tanya-jawab ujian pendadaran:

### Q1: *"Mengapa 10 dari 12 skenario berhenti pada Epoch 1? Apakah model mengalami kegagalan belajar (underfitting)?"*
* **Kunci Jawaban:**
  > *"Pasar Forex memiliki rasio sinyal terhadap derau (SNR) yang sangat rendah. Karena target log return distandarisasi dengan rata-rata 0 dan variansi 1, prediksi nilai rata-rata (mendekati 0) langsung menghasilkan loss terendah sekitar 0.968 pada epoch 1. Pada epoch berikutnya, model mulai menangkap noise data latih sehingga validation loss tidak mengalami penurunan dan mekanisme Early Stopping secara tepat menghentikan pelatihan pada epoch 6 (patience 5) untuk mencegah overfitting."*

### Q2: *"Bagaimana Anda membuktikan bahwa model Informer lebih baik daripada menebak harga jam kemarin (Naive Baseline)?"*
* **Kunci Jawaban:**
  > *"Pada pengujian horizon 1 jam (P1), skenario S384 menghasilkan nilai MAE dan MSE yang sedikit lebih rendah dibandingkan fluktuasi acak naive model, menunjukkan model mampu menangkap mikro-tren lokal. Namun, pada horizon multi-step (P4 dan P8), terjadi akumulasi deviasi log return kumulatif sehingga performa peramalan menurun secara eksponensial."*

### Q3: *"Apa peran Distilling Layer pada Encoder Informer dalam konteks data deret waktu finansial?"*
* **Kunci Jawaban:**
  > *"Distilling Layer mengombinasikan konvolusi 1D temporal dengan Max Pooling (stride 2). Pada data Forex dengan input panjang (seperti 384 jam), layer ini memangkas dimensi panjang sequence menjadi separuhnya ($L 	o L/2$) pada layer berikutnya sehingga menghemat memori GPU secara drastis sekaligus menyaring noise volatilitas mikro."*

### Q4: *"Mengapa evaluasi akhir direkonstruksi ke harga Close daripada menggunakan metrik pada skala Log Return saja?"*
* **Kunci Jawaban:**
  > *"Log Return digunakan selama proses pelatihan agar deret waktu bersifat stasioner dan gradien stabil. Namun, untuk kepentingan interpretabilitas praktis dan perbandingan finansial riil, nilai log return kumulatif dieksponeksialkan dan dikalikan dengan base close agar didapatkan estimasi harga penutupan EUR/USD dalam satuan aslinya."*

---

## 📋 6. Matriks Action Plan Sebelum Pelaksanaan Sidang

```markdown
- [ ] 1. Halaman Formalia:
      - Perbaiki gelar Pembimbing II (Prof. Dr. Fahrul Agus).
      - Ubah kata "proposal" menjadi "skripsi" pada Kata Pengantar.
      - Rapikan Halaman Pengesahan dan Daftar Isi.
- [ ] 2. Aljabar Linear & Terminologi (Bab II):
      - Ganti seluruh istilah "metrik Q/K/V" menjadi "matriks Q/K/V".
      - Rapikan definisi c (sampling factor) dan u (top-u query count).
      - Perbaiki typo MaxPoll -> MaxPool dan kurung tutup Persamaan (2.9).
      - Lakukan renumbering pada Persamaan (2.17) ganda.
- [ ] 3. Metodologi & Parameter (Bab III & IV):
      - Sinkronkan Early Stopping Patience menjadi 5 di seluruh bab.
      - Perbaiki nilai Jumlah Kolom di Tabel 4.4 (Data Mentah: 6, Terproses: 9).
      - Pindahkan Gambar 4.3 s.d. 4.13 (Source Code) ke Lembar Lampiran.
      - Isi Lampiran 1 s.d. 5 dengan teks kode dan data pengujian yang lengkap.
- [ ] 4. Pembahasan Ilmiah (Bab IV):
      - Tambahkan pembahasan Naive Baseline & Directional Accuracy.
      - Haluskan perbandingan literatur Wang et al. (2021).
```

---
*Laporan audit akademik ini disusun untuk memastikan mahasiswa bimbingan memiliki kesiapan 100% secara substansi ilmiah, pemahaman teoritis, dan kelayakan dokumen naskah menuju gelar Sarjana Komputer (S.Kom).*
