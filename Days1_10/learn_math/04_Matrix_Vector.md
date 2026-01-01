
# Hari 4 — Matriks dan Vektor

## Penjelasan super sederhana

### Vektor

**Vektor** bisa dianggap sebagai:

- **Daftar angka** (misalnya untuk data), atau
- **Panah** yang punya arah dan panjang.

Contoh vektor (daftar angka):
$$\mathbf{v} = [2, 5]$$

Kalau kita tambah vektor, kita tambah per bagian:
$$[2,5] + [1,3] = [3,8]$$

Kalau dikali angka (skalar):
$$2\cdot[2,5] = [4,10]$$

### Matriks

**Matriks** adalah **tabel angka**.
Contoh matriks 2×2:
$$A = \begin{bmatrix}1 & 2\\3 & 4\end{bmatrix}$$

### Analogi gampang

- Vektor: daftar belanja (apel 2, jeruk 5).
- Matriks: kotak-kotak kursi di bioskop (baris dan kolom).

## Contoh cepat

Jika $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$ dan $B=\begin{bmatrix}5&6\\7&8\end{bmatrix}$ maka:
$$A+B=\begin{bmatrix}6&8\\10&12\end{bmatrix}$$

## Quiz (10 Soal)

1. Hitung: $[3,1] + [2,4] = ?$
2. Hitung: $2\cdot[5,0] = ?$
3. Hitung: $[7,9] - [2,3] = ?$
4. Jika $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$, berapa elemen baris 1 kolom 2?
5. Jika $A=\begin{bmatrix}1&2\\3&4\end{bmatrix}$, berapa elemen baris 2 kolom 1?
6. Hitung: $\begin{bmatrix}1&1\\1&1\end{bmatrix} + \begin{bmatrix}2&0\\0&2\end{bmatrix}$
7. Hitung: $\begin{bmatrix}5&6\\7&8\end{bmatrix} - \begin{bmatrix}1&2\\3&4\end{bmatrix}$
8. Benar/Salah: Matriks adalah tabel angka dengan baris dan kolom.
9. Vektor $[0,0]$ disebut vektor apa (secara sederhana)?
10. Hitung: $3\cdot\begin{bmatrix}1&2\\0&1\end{bmatrix}$

## Kunci Jawaban

1. [5,5]
2. [10,0]
3. [5,6]
4. 2
5. 3
6. \(\begin{bmatrix}3&1\\1&3\end{bmatrix}\)
7. \(\begin{bmatrix}4&4\\4&4\end{bmatrix}\)
8. Benar
9. Vektor nol
10. \(\begin{bmatrix}3&6\\0&3\end{bmatrix}\)

---

## Dipakai di Machine Learning (contoh)

Data ML sering berbentuk **vektor** (satu baris angka) atau **matriks** (tabel angka).

- Satu foto bisa jadi vektor panjang (banyak piksel).
- Dataset biasanya matriks: baris = data, kolom = fitur.

### Contoh algoritma

- **PCA (Principal Component Analysis)**: memadatkan data pakai operasi matriks.
- **Neural Network**: banyak operasi matriks saat forward/backprop.

### Hyperparameter yang bisa di-tuning

- PCA: `n_components` (mau dipadatkan jadi berapa “komponen”)
- Neural Network: `hidden_layer_sizes`, `batch_size`, `learning_rate`

### Cara sampling hyperparameter (contoh gampang)

- Grid: `n_components` ∈ {2, 5, 10, 20}
- Random: pilih acak `batch_size` ∈ {16, 32, 64, 128}


