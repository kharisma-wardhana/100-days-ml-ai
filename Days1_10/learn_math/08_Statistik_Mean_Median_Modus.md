
# Hari 8 — Statistik Dasar (Mean, Median, Modus)

## Penjelasan super sederhana
Statistik membantu kita “merangkum” data.

Misalnya nilai ulangan: 6, 8, 7, 7, 10.

### Mean (rata-rata)
**Mean** = jumlah semua angka dibagi banyaknya angka.

### Median (nilai tengah)
**Median** = angka yang di tengah setelah diurutkan.

### Modus (paling sering muncul)
**Modus** = angka yang paling sering muncul.

### Analogi gampang
Bayangkan kamu punya permen:
- Mean: permen dibagi rata ke semua anak.
- Median: anak yang berdiri di tengah barisan.
- Modus: rasa permen yang paling sering kamu dapat.

## Contoh cepat
Data: 2, 3, 3, 8
- Mean = (2+3+3+8)/4 = 16/4 = 4
- Median = (3 dan 3) → median = 3
- Modus = 3

## Quiz (10 Soal)
1) Data: 1, 2, 3. Mean = ?
2) Data: 2, 2, 5. Modus = ?
3) Data: 9, 1, 5. Median = ?
4) Data: 4, 4, 4, 4. Mean = ?
5) Data: 4, 4, 4, 4. Modus = ?
6) Data: 1, 2, 2, 10. Median = ?
7) Data: 6, 8, 10. Mean = ?
8) Benar/Salah: Median harus mengurutkan data dulu.
9) Data: 3, 7, 7, 9, 10. Median = ?
10) Data: 5, 5, 6, 7, 7. Modus = ? (boleh lebih dari satu)

## Kunci Jawaban
1) 2
2) 2
3) 5
4) 4
5) 4
6) 2
7) 8
8) Benar
9) 7
10) 5 dan 7

---

## Dipakai di Machine Learning (contoh)
Mean/median/modus dipakai untuk **merapikan data** sebelum dilatih.

### Contoh penggunaan
- **Imputasi data hilang**: kalau ada nilai kosong,
  - pakai **mean** (rata-rata) atau **median** (lebih tahan terhadap angka ekstrem).
- **Baseline model**: kadang prediksi sederhana pakai mean/most frequent.

### Contoh algoritma
- **SimpleImputer** (preprocessing)
- **DummyClassifier / DummyRegressor** (baseline)

### “Hyperparameter” yang bisa di-tuning (pilihan strategi)
- Imputer: `strategy` ∈ {`mean`, `median`, `most_frequent`}

### Cara sampling (contoh gampang)
- Coba semua strategi (grid kecil), lihat mana yang membuat validasi lebih bagus


