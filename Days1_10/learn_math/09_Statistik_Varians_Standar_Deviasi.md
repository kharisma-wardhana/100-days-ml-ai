
# Hari 9 — Varians dan Standar Deviasi

## Penjelasan super sederhana
Kalau **mean** itu “titik tengah”, maka **varians** dan **standar deviasi** itu menunjukkan **seberapa menyebar** data dari titik tengah.

### Intuisi dulu (tanpa rumus ribet)
- Kalau semua angka **mirip-mirip**, berarti sebarannya kecil.
- Kalau angkanya **jauh-jauh**, berarti sebarannya besar.

**Standar deviasi (SD)** itu seperti “jarak rata-rata” data dari mean, tapi dihitung dengan cara khusus (pakai kuadrat lalu akar).

### Analogi gampang
Bayangkan anak panah ditembak ke target:
- Kalau panah berkumpul dekat tengah → variasinya kecil.
- Kalau panah menyebar ke mana-mana → variasinya besar.

## Contoh cepat (angka kecil)
Data A: 5, 5, 5
- Semua sama → sebaran sangat kecil (varians 0, SD 0)

Data B: 1, 5, 9
- Jauh-jauh → sebaran lebih besar

## Quiz (10 Soal)
1) Data: 3, 3, 3. Varians kira-kira kecil atau besar?
2) Data: 1, 10, 1, 10. Varians kira-kira kecil atau besar?
3) Benar/Salah: Varians mengukur sebaran data.
4) Benar/Salah: Standar deviasi selalu negatif.
5) Data A: 4,4,4,4 dan Data B: 1,4,7,10. Mana yang SD-nya lebih besar?
6) Jika semua data sama, SD = ?
7) Kalau data makin “menyebar”, SD biasanya...
	- A. mengecil
	- B. membesar
8) Data: 2, 2, 3, 3. Sebaran ini kecil atau sedang? (pilih yang paling masuk akal)
9) Dalam target panahan: panah rapat → SD ...
	- A. kecil
	- B. besar
10) Benar/Salah: SD adalah akar dari varians.

## Kunci Jawaban
1) Kecil (bahkan 0)
2) Besar
3) Benar
4) Salah
5) Data B
6) 0
7) B
8) Kecil
9) A
10) Benar

---

## Dipakai di Machine Learning (contoh)
Varians/standar deviasi dipakai untuk memahami sebaran data dan melakukan **standardisasi**.

### Contoh penggunaan
- **StandardScaler**: membuat fitur punya mean 0 dan standar deviasi 1.
	Ini sering membantu model belajar lebih stabil.

### Contoh algoritma
- **SVM** dan **Logistic Regression** sering lebih bagus setelah data distandardisasi.

### Hyperparameter yang bisa di-tuning
- SVM: `C`, `gamma`
- Logistic Regression: `C`

### Cara sampling hyperparameter (contoh gampang)
- Grid: `C` ∈ {0.1, 1, 10}
- Pastikan preprocessing (StandardScaler) ada di pipeline supaya adil


