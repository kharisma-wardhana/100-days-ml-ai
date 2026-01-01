
# Hari 1 — Bilangan dan Operasi Dasar

## Penjelasan super sederhana

**Bilangan** itu seperti jumlah benda.

- Punya 3 apel artinya ada 3.

**Operasi dasar** itu cara kita “mengubah jumlah”:

- **Tambah (+)**: menggabungkan. Contoh: 2 apel + 1 apel = 3 apel.
- **Kurang (-)**: mengambil. Contoh: 5 permen - 2 permen = 3 permen.
- **Kali (×)**: penjumlahan berulang. Contoh: 3 × 4 = 4 + 4 + 4.
- **Bagi (÷)**: membagi rata. Contoh: 12 ÷ 3 = 4 (masing-masing dapat 4).

### Analogi gampang

Bayangkan kamu punya kotak kue:

- Tambah: ada yang kasih kue.
- Kurang: kamu makan kue.
- Kali: kamu punya beberapa kotak yang isinya sama.
- Bagi: kue dibagi ke teman-teman supaya adil.

## Contoh cepat

- 7 + 5 = 12
- 10 - 6 = 4
- 4 × 3 = 12
- 20 ÷ 5 = 4

> Catatan kecil: kalau ada kurung, kerjakan yang di dalam kurung dulu.

## Quiz (10 Soal)

1. 6 + 4 = ?
2. 15 - 7 = ?
3. 3 × 5 = ?
4. 18 ÷ 6 = ?
5. Isi yang kosong: 9 + __ = 14
6. Isi yang kosong: __ - 3 = 8
7. Mana yang benar?
   - A. 2 × 6 = 12
   - B. 2 × 6 = 8
8. 24 ÷ 3 = ?
9. (5 + 2) × 3 = ?
10. 12 - (4 + 3) = ?

## Kunci Jawaban

1. 10
2. 8
3. 15
4. 3
5. 5
6. 11
7. A
8. 8
9. 21
10. 5

---

## Dipakai di Machine Learning (contoh)

Walau terlihat sederhana, operasi dasar dipakai terus saat ML berjalan.

### Contoh algoritma

- **K-Nearest Neighbors (KNN)**: banyak menghitung jarak dan penjumlahan.
- **Decision Tree / Random Forest**: banyak menghitung perbandingan (lebih kecil/lebih besar) untuk memecah data.

### Hyperparameter yang bisa di-tuning

- KNN: `n_neighbors (k)` (misalnya 1, 3, 5, 7)
- Decision Tree: `max_depth`, `min_samples_split`

### Cara sampling hyperparameter (contoh gampang)

- Coba daftar kecil dulu (grid): `k` ∈ {1, 3, 5, 7}
- Lihat mana yang paling bagus di data validasi


