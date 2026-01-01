
# Hari 6 — Kalkulus Dasar (Limit dan Turunan)

## Penjelasan super sederhana
### Limit (mendekati)
**Limit** itu artinya nilai yang **didekati**.
Misalnya kamu jalan mendekati pintu:
- Kamu makin dekat, makin dekat…
- Walau belum menyentuh pintu, kita bisa tanya: “kalau makin dekat, kira-kira sampai angka berapa?”

Contoh sederhana:
Jika $f(x)=x+1$, saat $x$ mendekati 3, maka $f(x)$ mendekati 4.

### Turunan (derivative)
**Turunan** itu seperti **kecepatan**.
- Jarak berubah → turunan melihat **seberapa cepat berubah**.

Di grafik, turunan itu seperti **kemiringan (slope)** garis di titik itu.

### Analogi gampang
- Limit: mendekati target di game (semakin dekat, semakin jelas angkanya).
- Turunan: speedometer sepeda/mobil (seberapa cepat berubah per detik).

## Contoh cepat
Jika $f(x)=2x$, kemiringannya selalu 2, jadi turunannya $f'(x)=2$.

Jika $f(x)=x^2$, turunannya $f'(x)=2x$.

## Quiz (10 Soal)
1) Jika $f(x)=x+1$, saat $x$ mendekati 5, $f(x)$ mendekati berapa?
2) Jika $f(x)=2x$, saat $x$ mendekati 4, $f(x)$ mendekati berapa?
3) Benar/Salah: Limit adalah nilai yang didekati.
4) Jika $f(x)=3x$, berapa $f'(x)$?
5) Jika $f(x)=x^2$, berapa $f'(x)$?
6) Jika $f(x)=5$ (konstan), turunan $f'(x)$ berapa?
7) Jika $f(x)=x^2$, berapa $f'(3)$?
8) Jika $f(x)=2x+7$, berapa $f'(x)$?
9) Pada grafik, turunan di titik itu mirip apa?
	- A. Warna
	- B. Kemiringan
	- C. Jumlah titik
10) Jika $f(x)=10x$, berapa $f'(x)$?

## Kunci Jawaban
1) 6
2) 8
3) Benar
4) 3
5) 2x
6) 0
7) 6
8) 2
9) B
10) 10

---

## Dipakai di Machine Learning (contoh)
Turunan dipakai untuk **melatih model**.
Idenya: kalau model salah, kita ubah sedikit arah yang membuat salahnya berkurang.

### Contoh algoritma
- **Gradient Descent**: memakai turunan/gradien untuk memperbaiki parameter.
- **Backpropagation** (di Neural Network): menghitung gradien di banyak layer.

### Hyperparameter yang bisa di-tuning
- `learning_rate` (seberapa besar langkah perbaikan)
- `momentum` (bantu gerak lebih stabil)
- `weight_decay` / `alpha` (regularisasi)

### Cara sampling hyperparameter (contoh gampang)
- Mulai dari beberapa nilai: `learning_rate` ∈ {0.001, 0.01, 0.1}
- Pilih yang membuat training stabil (tidak “meledak”) dan validasi bagus


