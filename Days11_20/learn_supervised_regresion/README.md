# Supervised Learning - Regression

## Pengertian Supervised Learning - Regression

Supervised Learning adalah metode pembelajaran mesin di mana model dilatih menggunakan data berlabel. Dalam konteks regresi, tujuan utama adalah memprediksi nilai kontinu berdasarkan fitur-fitur input yang ada.

## Contoh Algoritma Regresi

1. **Linear Regression**: Mencari hubungan linear antara fitur input dan nilai target.
2. **Polynomial Regression**: Memodelkan hubungan non-linear dengan menambahkan fitur polinomial.
3. **Ridge Regression**: Variasi dari regresi linear yang menambahkan penalti L2 untuk mengurangi overfitting.
4. **Lasso Regression**: Variasi dari regresi linear yang menambahkan penalti L1 untuk seleksi fitur.
5. **Elastic Net**: Kombinasi dari Ridge dan Lasso Regression.
6. **Support Vector Regression (SVR)**: Menggunakan prinsip SVM untuk regresi.
7. **Decision Tree Regression**: Menggunakan pohon keputusan untuk memodelkan hubungan antara fitur dan nilai target.
8. **Random Forest Regression**: Kombinasi dari beberapa pohon keputusan untuk meningkatkan akurasi prediksi.
9. **Gradient Boosting Regression**: Membangun model regresi secara bertahap dengan menggabungkan beberapa model lemah.

## Proses Regresi

1. **Pengumpulan Data**: Kumpulkan dataset yang berisi fitur-fitur dan nilai target kontinu.
2. **Preprocessing Data**: Bersihkan data, tangani nilai yang hilang, dan lakukan encoding pada fitur kategorikal jika diperlukan.
3. **Pembagian Data**: Bagi dataset menjadi data latih dan data uji.
4. **Pelatihan Model**: Gunakan data latih untuk melatih model regresi.
5. **Evaluasi Model**: Uji model menggunakan data uji dan hitung metrik evaluasi seperti Mean Absolute Error (MAE), Mean Squared Error (MSE), dan R-squared.
6. **Penyempurnaan Model**: Lakukan tuning hyperparameter untuk meningkatkan kinerja model.
7. **Deployment**: Terapkan model yang telah dilatih ke dalam lingkungan produksi untuk prediksi nyata.
8. **Monitoring dan Pemeliharaan**: Pantau kinerja model secara berkala dan lakukan pembaruan jika diperlukan.
9. **Iterasi**: Proses ini bersifat iteratif, di mana model dapat terus disempurnakan berdasarkan hasil evaluasi dan feedback dari pengguna.
10. **Dokumentasi**: Mencatat proses, keputusan, dan hasil untuk referensi di masa depan.

## Metrik Evaluasi Regresi

1. **Mean Absolute Error (MAE)**: Rata-rata dari selisih absolut antara nilai prediksi dan nilai aktual.
2. **Mean Squared Error (MSE)**: Rata-rata dari kuadrat selis antara nilai prediksi dan nilai aktual.
3. **Root Mean Squared Error (RMSE)**: Akar kuadrat dari MSE, memberikan bobot lebih pada kesalahan yang lebih besar.
4. **R-squared (R²)**: Proporsi variansi dalam nilai target yang dapat dijelaskan oleh fitur-fitur input.

## Hyperparameter yang Bisa Di-tuning

1. **Linear Regression**: Tidak banyak hyperparameter yang dapat di-tuning, tetapi regularisasi dapat diterapkan.
2. **Ridge Regression**: Parameter regulasi (alpha).
3. **Lasso Regression**: Parameter regulasi (alpha).
4. **Elastic Net**: Parameter regulasi (alpha) dan rasio antara L1 dan L2.
5. **SVR**: Parameter regulasi (C), epsilon, jenis kernel (linear, polynomial, RBF).
6. **Decision Tree Regression**: Kedalaman maksimum pohon (max_depth), jumlah minimum sampel per daun (min_samples_leaf).
7. **Random Forest Regression**: Jumlah pohon (n_estimators), kedalaman maksimum pohon (max_depth).
8. **Gradient Boosting Regression**: Jumlah estimators (n_estimators), learning rate, kedalaman maksimum pohon (max_depth).
9. **General**: Ukuran batch, jumlah epoch, metode optimasi (SGD, Adam).
10. **Regularization**: Parameter untuk mengontrol overfitting (misalnya, dropout rate pada neural networks).
11. **Early Stopping**: Kriteria untuk menghentikan pelatihan lebih awal jika kinerja pada data validasi tidak membaik.

## Cara Sampling Hyperparameter

1. **Grid Search**: Mencoba semua kombinasi dari daftar nilai hyperparameter yang telah ditentukan.
2. **Random Search**: Memilih kombinasi hyperparameter secara acak dari distribusi yang telah ditentukan.
3. **Bayesian Optimization**: Menggunakan model probabilistik untuk memilih kombinasi hyperparameter yang paling menjanjikan berdasarkan hasil sebelumnya.
4. **Hyperband**: Metode yang menggabungkan random search dengan early stopping untuk efisiensi.
5. **Genetic Algorithms**: Menggunakan prinsip evolusi untuk mencari kombinasi hyperparameter yang optimal.
6. **Optuna**: Framework otomatis untuk optimasi hyperparameter yang menggunakan pendekatan berbasis Bayesian.
7. **Population Based Training (PBT)**: Metode yang menggabungkan optimasi hyperparameter dengan pelatihan model secara bersamaan dalam populasi model.
8. **Successive Halving**: Metode yang mengalokasikan sumber daya secara adaptif untuk kombinasi hyperparameter yang menjanjikan dengan mengeliminasi yang kurang baik secara bertahap.
9. **Automated Machine Learning (AutoML)**: Platform yang secara otomatis mencari dan mengoptimalkan hyperparameter terbaik untuk model regresi.
10. **Cross-Validation**: Menggunakan teknik validasi silang untuk menilai kinerja kombinasi hyperparameter.

## Contoh Implementasi dengan Scikit-Learn

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load dataset
data = load_boston()

X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define model
model = RandomForestRegressor(random_state=42)
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 3, 5, 10],
}
grid = GridSearchCV(model, param_grid=param_grid, cv=5)
grid.fit(X_train, y_train)
best_model = grid.best_estimator_

# Evaluate model
y_pred = best_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
```

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np

# Load dataset
data = load_boston()

X = data.data
y = data.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define model
model = RandomForestRegressor(random_state=42)
param_dist = {
    "n_estimators": [50, 100, 200, 300, 500],
    "max_depth": [None, 3, 5, 10, 20],
    "min_samples_split": [2, 5, 10],
}
rand = RandomizedSearchCV(model, param_distributions=param_dist, n_iter=10, cv=5, random_state=42)
rand.fit(X_train, y_train)
best_model = rand.best_estimator_

# Evaluate model
y_pred = best_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
```
