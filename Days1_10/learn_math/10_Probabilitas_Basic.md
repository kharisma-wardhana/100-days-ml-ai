
# Hari 10 — Probabilitas Dasar

## Penjelasan super sederhana
**Probabilitas** itu peluang atau “seberapa mungkin” sesuatu terjadi.

Rumus paling dasar:
$$P(kejadian) = \frac{\text{jumlah hasil yang diinginkan}}{\text{jumlah semua hasil yang mungkin}}$$

### Analogi gampang
Bayangkan kantong berisi bola:
- 3 bola merah
- 1 bola biru
Kalau ambil 1 bola tanpa lihat:
- Peluang merah lebih besar karena merah lebih banyak.

## Contoh cepat
Koin (angka/gambar) punya 2 kemungkinan.
- Peluang keluar “angka” = 1/2.

Dadu punya 6 kemungkinan (1 sampai 6).
- Peluang keluar 6 = 1/6.

## Quiz (10 Soal)
1) Koin punya 2 sisi. Peluang keluar “angka” = ?
2) Dadu punya 6 sisi. Peluang keluar 1 = ?
3) Dadu: peluang keluar bilangan genap (2,4,6) = ?
4) Kantong: 2 bola merah, 3 bola biru. Peluang ambil merah = ?
5) Kantong: 2 bola merah, 3 bola biru. Peluang ambil biru = ?
6) Benar/Salah: Probabilitas selalu antara 0 dan 1.
7) Jika sebuah kejadian pasti terjadi, probabilitasnya = ?
8) Jika sebuah kejadian mustahil terjadi, probabilitasnya = ?
9) Dadu: peluang keluar angka lebih dari 4 (5 atau 6) = ?
10) Kantong: 1 bola hijau, 1 bola kuning, 2 bola merah. Peluang ambil merah = ?

## Kunci Jawaban
1) 1/2
2) 1/6
3) 3/6 = 1/2
4) 2/5
5) 3/5
6) Benar
7) 1
8) 0
9) 2/6 = 1/3
10) 2/4 = 1/2

---

## Dipakai di Machine Learning (contoh)
Probabilitas dipakai untuk model yang memprediksi “seberapa yakin” dia.

### Contoh algoritma
- **Naive Bayes**: model klasifikasi yang sangat berbasis probabilitas.
- **Logistic Regression**: mengeluarkan probabilitas kelas (0–1).

### Hyperparameter yang bisa di-tuning
- Naive Bayes (MultinomialNB/BernoulliNB): `alpha` (smoothing, supaya tidak mudah jadi 0)
- Logistic Regression: `C`

### Cara sampling hyperparameter (contoh gampang)
- Grid: `alpha` ∈ {0.1, 0.5, 1.0, 2.0}
- Lihat efeknya pada akurasi atau F1-score


