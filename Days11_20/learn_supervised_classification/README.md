# Supervised Learning - Classification

## Pengantar

Supervised Learning adalah salah satu jenis pembelajaran mesin di mana model dilatih menggunakan data berlabel. Dalam konteks klasifikasi, tujuan utama adalah mengkategorikan data input ke dalam kelas-kelas yang telah ditentukan sebelumnya berdasarkan fitur-fitur yang ada.

## Contoh Algoritma Klasifikasi

1. **K-Nearest Neighbors (KNN)**: Mengklasifikasikan data berdasarkan kelas mayoritas dari tetangga terdekatnya.
2. **Decision Tree**: Membuat model prediksi berdasarkan aturan keputusan yang dihasilkan dari fitur-fitur data.
3. **Random Forest**: Kombinasi dari beberapa pohon keputusan untuk meningkatkan akurasi prediksi.
4. **Support Vector Machine (SVM)**: Mencari hyperplane terbaik yang memisahkan kelas-kelas dalam ruang fitur.
5. **Logistic Regression**: Meskipun namanya regresi, ini adalah algoritma klasifikasi yang memodelkan probabilitas kelas.
6. **Naive Bayes**: Berdasarkan teorema Bayes, mengklasifikasikan data berdasarkan probabilitas bersyarat.
7. **Gradient Boosting Machines (GBM)**: Membangun model klasifikasi secara bertahap dengan menggabungkan beberapa model lemah.
8. **Neural Networks**: Menggunakan jaringan saraf tiruan untuk menangani masalah klasifikasi yang kompleks.

## Proses Klasifikasi

1. **Pengumpulan Data**: Kumpulkan dataset yang berisi fitur-fitur dan label kelas.
2. **Preprocessing Data**: Bersihkan data, tangani nilai yang hilang, dan lakukan encoding pada fitur kategorikal.
3. **Pembagian Data**: Bagi dataset menjadi data latih dan data uji.
4. **Pelatihan Model**: Gunakan data latih untuk melatih model klasifikasi.
5. **Evaluasi Model**: Uji model menggunakan data uji dan hitung metrik evaluasi seperti akurasi, precision, recall, dan F1-score.
6. **Penyempurnaan Model**: Lakukan tuning hyperparameter untuk meningkatkan kinerja model.
7. **Deployment**: Terapkan model yang telah dilatih ke dalam lingkungan produksi untuk prediksi nyata.
8. **Monitoring dan Pemeliharaan**: Pantau kinerja model secara berkala dan lakukan pembaruan jika diperlukan.
9. **Iterasi**: Proses ini bersifat iteratif, di mana model dapat terus disempurnakan berdasarkan hasil evaluasi dan feedback dari pengguna.
10. **Dokumentasi**: Mencatat proses, keputusan, dan hasil untuk referensi di masa depan.

## Metrik Evaluasi Klasifikasi

1. **Akurasi**: Proporsi prediksi yang benar dari total prediksi.
2. **Precision**: Proporsi prediksi positif yang benar dari semua prediksi positif.
3. **Recall**: Proporsi prediksi positif yang benar dari semua data positif sebenarnya.
4. **F1-Score**: Harmonik rata-rata dari precision dan recall.
5. **Confusion Matrix**: Tabel yang menunjukkan jumlah prediksi benar dan salah untuk setiap kelas.

## Hyperparameter yang Bisa Di-tuning

1. **KNN**: Jumlah tetangga (k), metrik jarak (misalnya, Euclidean, Manhattan).
2. **Decision Tree**: Kedalaman maksimum pohon (max_depth), jumlah minimum sampel per daun (min_samples_leaf).
3. **Random Forest**: Jumlah pohon (n_estimators), kedalaman maksimum pohon (max_depth).
4. **SVM**: Parameter regulasi (C), jenis kernel (linear, polynomial, RBF).
5. **Logistic Regression**: Parameter regulasi (C), jenis penalti (L1, L2).
6. **Naive Bayes**: Parameter smoothing (alpha).
7. **Gradient Boosting**: Jumlah estimators (n_estimators), learning rate, kedalaman maksimum pohon (max_depth).
8. **Neural Networks**: Jumlah lapisan tersembunyi, jumlah neuron per lapisan, laju pembelajaran (learning rate).
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
7. **Population-Based Training (PBT)**: Menggabungkan pelatihan model dengan optimasi hyperparameter secara bersamaan.
8. **Successive Halving**: Metode yang mengalokasikan sumber daya lebih banyak pada kombinasi hyperparameter yang menjanjikan.
9. **Cross-Validation**: Menggunakan teknik validasi silang untuk menilai kinerja kombinasi hyperparameter.
10. **Automated Machine Learning (AutoML)**: Platform yang secara otomatis mencari dan mengoptimalkan hyperparameter untuk model klasifikasi.

## Contoh Kode (Scikit-Learn)

```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=42)
param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 3, 5, 10],
}

grid = GridSearchCV(model, param_grid=param_grid, cv=5)
# grid.fit(X_train, y_train)
```

```python
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=42)
param_dist = {
    "n_estimators": [50, 100, 200, 300, 500],
    "max_depth": [None, 3, 5, 10, 20],
    "min_samples_split": [2, 5, 10],
}
rand = RandomizedSearchCV(model, param_distributions=param_dist, n_iter=10, cv=5, random_state=42)
# rand.fit(X_train, y_train)
```
