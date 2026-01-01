
# Hari 2 — Fungsi dan Grafik

## Penjelasan super sederhana

**Fungsi** itu seperti **mesin**:

- Kamu masukkan angka **x** (input)
- Mesin mengubahnya jadi angka **y** (output)

Ditulis: $y = f(x)$.
Contoh: $f(x) = x + 2$ artinya “angka apa pun ditambah 2”.

**Grafik** adalah gambar yang menunjukkan hubungan **x** dan **y**.
Biasanya pakai bidang kotak-kotak:

- Sumbu mendatar: **x**
- Sumbu tegak: **y**

### Analogi gampang

Bayangkan mesin “tambah 2”:

- Masukkan 1 → keluar 3
- Masukkan 5 → keluar 7
Kalau kamu gambar titik-titik (1,3), (5,7), lama-lama terlihat pola (garis).

## Contoh cepat

Jika $f(x)=2x$:

- $f(1)=2$
- $f(4)=8$

Jika $y=x-1$:

- Saat $x=3$, $y=2$ → titik (3,2)

## Quiz (10 Soal)

1. Jika $f(x)=x+3$, berapa $f(2)$?
2. Jika $f(x)=2x$, berapa $f(5)$?
3. Jika $f(x)=x-4$, berapa $f(10)$?
4. Pada titik (2, 7), berapa nilai $x$?
5. Pada titik (2, 7), berapa nilai $y$?
6. Jika $y=3x$, saat $x=0$, $y$ berapa?
7. Jika $y=3x$, saat $x=2$, $y$ berapa?
8. Benar/Salah: Pada grafik, sumbu mendatar biasanya adalah sumbu $y$.
9. Tentukan pasangan (x,y): jika $y=x+1$ dan $x=4$.
10. Jika $f(x)=x+x$ (sama dengan $2x$), berapa $f(6)$?

## Kunci Jawaban

1. 5
2. 10
3. 6
4. 2
5. 7
6. 0
7. 6
8. Salah
9. (4, 5)
10. 12

---

## Dipakai di Machine Learning (contoh)

Fungsi itu inti dari model: model menerima input $x$ lalu mengeluarkan output $y$.

### Contoh algoritma

- **Linear Regression**: bentuknya seperti fungsi $y = ax + b$.
- **Neural Network**: banyak fungsi kecil yang disusun berlapis-lapis.

### Hyperparameter yang bisa di-tuning

- Linear/Ridge Regression: `alpha` (kekuatan “rem”/regularisasi)
- Neural Network (MLP): `hidden_layer_sizes`, `learning_rate`, `max_iter`

### Cara sampling hyperparameter (contoh gampang)

- Grid kecil: `alpha` ∈ {0.0, 0.1, 1.0, 10.0}
- Random: ambil beberapa kombinasi acak untuk `hidden_layer_sizes` dan `learning_rate`


