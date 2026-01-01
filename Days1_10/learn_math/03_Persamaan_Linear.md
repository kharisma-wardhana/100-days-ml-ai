
# Hari 3 — Persamaan Linear

## Penjelasan super sederhana

**Persamaan** itu kalimat matematika yang pakai tanda **=**.
Contoh: $2 + 3 = 5$.

**Persamaan linear** biasanya bentuknya seperti:
$$ax + b = c$$
Yang artinya: ada angka yang belum kita tahu (misalnya **x**) dan kita mau cari nilainya.

### Analogi gampang (timbangan)

Bayangkan tanda **=** itu **timbangan**.
Kalau sisi kiri dan kanan harus seimbang, maka:

- Kalau kamu tambah sesuatu di kiri, kamu harus tambah juga di kanan.
- Kalau kamu kurangi sesuatu di kiri, kamu harus kurangi juga di kanan.

## Contoh cepat

Cari $x$ dari $x + 3 = 10$:

- Kurangi 3 di kedua sisi → $x = 7$

Cari $x$ dari $2x = 12$:

- Bagi 2 di kedua sisi → $x = 6$

## Quiz (10 Soal)

1. Selesaikan: $x + 5 = 9$
2. Selesaikan: $x - 4 = 3$
3. Selesaikan: $2x = 14$
4. Selesaikan: $3x = 21$
5. Selesaikan: $x + 7 = 7$
6. Selesaikan: $x/2 = 6$
7. Selesaikan: $2x + 1 = 9$
8. Selesaikan: $5x - 5 = 20$
9. Benar/Salah: Kalau kita tambah 2 di sisi kiri, kita juga harus tambah 2 di sisi kanan.
10. Selesaikan: $4x + 2 = 18$

## Kunci Jawaban

1. 4
2. 7
3. 7
4. 7
5. 0
6. 12
7. 4
8. 5
9. Benar
10. 4

---

## Dipakai di Machine Learning (contoh)

Persamaan linear muncul saat model mencoba mencari “angka terbaik” untuk cocok dengan data.

### Contoh algoritma

- **Linear Regression**: mencari $a$ dan $b$ pada $y=ax+b$.
- **Logistic Regression** (klasifikasi): juga menggunakan bentuk linear lalu diubah dengan fungsi khusus.

### Hyperparameter yang bisa di-tuning

- Logistic Regression: `C` (kebalikan kekuatan regularisasi; makin kecil biasanya makin “ketat”)
- Linear/Ridge/Lasso: `alpha`

### Cara sampling hyperparameter (contoh gampang)

- Grid: `C` ∈ {0.1, 1, 10}
- Bandingkan hasilnya dengan validasi silang (cross-validation)


