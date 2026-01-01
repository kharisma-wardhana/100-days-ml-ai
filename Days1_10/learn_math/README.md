# Matematika untuk Machine Learning

## Hari 1-10: Dasar-dasar Matematika

[ ] Hari 1: Bilangan dan Operasi Dasar
[ ] Hari 2: Fungsi dan Grafik
[ ] Hari 3: Persamaan Linear
[ ] Hari 4: Matriks dan Vektor
[ ] Hari 5: Aljabar Linier Dasar
[ ] Hari 6: Kalkulus Dasar (Limit dan Turunan)
[ ] Hari 7: Kalkulus Lanjutan (Integral)
[ ] Hari 8: Statistik Dasar (Mean, Median, Modus)
[ ] Hari 9: Varians dan Standar Deviasi
[ ] Hari 10: Probabilitas Dasar

---

## Dipakai di Machine Learning (contoh cepat)

Di Machine Learning, matematika ini dipakai untuk:

- Mengubah data (misalnya menormalkan angka)
- Membuat model (misalnya regresi linear)
- Melatih model (misalnya memperbaiki model sedikit demi sedikit)

### Apa itu hyperparameter?

**Hyperparameter** itu seperti **knob/tombol pengaturan** pada algoritma.

- Kita pilih nilainya **sebelum** model dilatih.
- Contoh: `learning_rate`, `k` pada KNN, `max_depth` pada decision tree.

### Cara “sampling” hyperparameter (cara coba-coba yang rapi)

1. **Grid Search**: coba semua kombinasi dari daftar kecil.
2. **Random Search**: ambil beberapa kombinasi secara acak (sering lebih cepat untuk banyak parameter).
3. (Lanjutan) **Bayesian/Optuna**: lebih pintar memilih percobaan berikutnya.

### Contoh sederhana (scikit-learn)

> Ini contoh untuk gambaran. Kamu bisa jalankan di proyek Python terpisah.

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(random_state=42)

# 1) Grid Search (coba semua kombinasi kecil)
param_grid = {

    "n_estimators": [50, 100, 200],
    "max_depth": [None, 3, 5, 10],
}

grid = GridSearchCV(model, param_grid=param_grid, cv=5)
# grid.fit(X_train, y_train)

# 2) Random Search (coba beberapa kombinasi acak)
param_dist = {
    "n_estimators": [50, 100, 200, 300, 500],
    "max_depth": [None, 3, 5, 10, 20],
    "min_samples_split": [2, 5, 10],
}

rand = RandomizedSearchCV(model, param_distributions=param_dist, n_iter=10, cv=5, random_state=42)
# rand.fit(X_train, y_train)
```

