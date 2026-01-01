
# Hari 5 — Aljabar Linier Dasar

## Penjelasan super sederhana
Aljabar linier adalah cara matematika untuk bermain dengan **vektor** dan **garis lurus**.

Yang sering dipakai:
1) **Skalar**: satu angka saja (contoh: 5).
2) **Vektor**: daftar angka (contoh: [2, 3]).
3) **Perkalian skalar ke vektor**: memperbesar/mengecilkan.
4) **Penjumlahan vektor**: menggabungkan arah/jumlah per bagian.

### Kombinasi linear (campur-campur)
Contoh: $2\cdot[1,0] + 3\cdot[0,1] = [2,3]$.
Artinya kita “mencampur” vektor dasar untuk membuat vektor baru.

### Sistem persamaan sederhana
Contoh:
$$x + y = 5$$
$$x = 2$$
Maka $y = 3$.

### Analogi gampang
Bayangkan vektor itu seperti **langkah di lantai**:
- [2,3] artinya 2 langkah ke kanan, 3 langkah ke atas.
- Dikali 2 jadi langkahnya dobel: [4,6].

## Quiz (10 Soal)
1) Hitung: $2\cdot[1,2] = ?$
2) Hitung: $[1,2] + [3,4] = ?$
3) Hitung: $[5,5] - [2,1] = ?$
4) Isi yang kosong: $3\cdot[2,0] = [\_,\_]$
5) Benar/Salah: $[1,2] + [2,1] = [3,3]$
6) Kombinasi: $1\cdot[2,0] + 1\cdot[0,4] = ?$
7) Selesaikan: $x + y = 10$ dan $x = 6$. Berapa $y$?
8) Selesaikan: $x - y = 2$ dan $x = 5$. Berapa $y$?
9) Jika $\mathbf{v}=[3,1]$, berapa $0\cdot\mathbf{v}$?
10) Jika $\mathbf{a}=[1,0]$ dan $\mathbf{b}=[0,1]$, berapa $4\mathbf{a}+2\mathbf{b}$?

## Kunci Jawaban
1) [2,4]
2) [4,6]
3) [3,4]
4) [6,0]
5) Benar
6) [2,4]
7) 4
8) 3
9) [0,0]
10) [4,2]

---

## Dipakai di Machine Learning (contoh)
Aljabar linier adalah “bahasa” utama untuk:
- Mengolah fitur (fitur = angka-angka)
- Menghitung prediksi model

### Contoh algoritma
- **Linear Regression**: perkalian matriks untuk menghitung prediksi.
- **SVM (Support Vector Machine)**: banyak konsep vektor dan jarak.

### Hyperparameter yang bisa di-tuning
- SVM: `C`, `kernel` (misalnya `linear`, `rbf`), dan kalau `rbf` ada `gamma`
- Linear/Ridge: `alpha`

### Cara sampling hyperparameter (contoh gampang)
- Grid: `C` ∈ {0.1, 1, 10}, `gamma` ∈ {0.01, 0.1, 1}


