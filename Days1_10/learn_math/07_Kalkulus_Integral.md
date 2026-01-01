
# Hari 7 — Kalkulus Lanjutan (Integral)

## Penjelasan super sederhana
**Integral** itu seperti menghitung **berapa banyak totalnya**, dengan cara menjumlahkan bagian-bagian kecil.

Di grafik, integral sering berarti **luas daerah di bawah garis/kurva**.

### Analogi gampang
Bayangkan kamu mau tahu luas karpet.
Kalau sulit, kamu bisa:
- potong jadi kotak-kotak kecil,
- hitung kotak-kotaknya,
- lalu jumlahkan.
Itu ide integral: menjumlahkan banyak potongan kecil.

## Contoh cepat
Jika ada persegi panjang lebar 3 dan tinggi 4, luasnya 12.
Integral juga bisa menghitung luas, tapi untuk bentuk yang lebih “melengkung”.

Aturan sangat sederhana yang sering dipakai:
- Integral dari $x$ adalah $\frac{x^2}{2}$ (ditambah konstanta).

## Quiz (10 Soal)
1) Integral sering dipakai untuk menghitung apa pada grafik?
	- A. Warna grafik
	- B. Luas di bawah kurva
	- C. Banyaknya titik
2) Analogi integral yang benar adalah...
	- A. Mengukur kecepatan
	- B. Menjumlahkan potongan kecil
	- C. Membagi nol
3) Luas persegi panjang dengan lebar 5 dan tinggi 2 adalah?
4) Jika $\int x\,dx = \frac{x^2}{2} + C$, maka $\int 2x\,dx$ adalah?
5) Benar/Salah: Integral adalah kebalikan (pasangan) dari turunan.
6) Jika kamu menjumlahkan 1 + 1 + 1 + 1 (empat kali), totalnya?
7) Konsep integral paling mirip dengan kata...
	- A. Total
	- B. Kurang
	- C. Pecah
8) Jika luas persegi 3×3 adalah?
9) Jika $\int 1\,dx = x + C$, maka $\int 3\,dx$ adalah?
10) Jika $f'(x)$ adalah turunan, maka integral berhubungan dengan mencari...
	- A. Fungsi asal
	- B. Warna asal
	- C. Kotak asal

## Kunci Jawaban
1) B
2) B
3) 10
4) $x^2 + C$
5) Benar (secara konsep, integral “membalikkan” turunan)
6) 4
7) A
8) 9
9) $3x + C$
10) A

---

## Dipakai di Machine Learning (contoh)
Integral berhubungan dengan **luas/total**.
Di ML, konsep “luas di bawah kurva” sering muncul saat menilai model.

### Contoh algoritma / metrik
- **ROC-AUC**: mengukur “luas” di bawah kurva ROC (AUC).
- **Probabilistic models**: kadang memakai integral untuk menghitung peluang total.

### Hyperparameter yang bisa di-tuning
- Untuk model klasifikasi yang menghasilkan skor (mis. Logistic Regression, Random Forest):
	- `threshold` (ambang untuk bilang kelas 1 atau 0)
- Untuk Random Forest: `n_estimators`, `max_depth`

### Cara sampling hyperparameter (contoh gampang)
- Coba beberapa `threshold`: {0.3, 0.5, 0.7} lalu pilih yang seimbang (precision/recall)


