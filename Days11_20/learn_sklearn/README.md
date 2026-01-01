# Pengantar Scikit-Learn

Scikit-Learn adalah library open-source di Python yang digunakan untuk machine learning dan analisis data. Library ini menyediakan berbagai algoritma machine learning yang mudah digunakan, mulai dari regresi, klasifikasi, clustering, hingga pengurangan dimensi. Scikit-Learn dibangun di atas library populer lainnya seperti NumPy, SciPy, dan Matplotlib, sehingga sangat cocok untuk integrasi dalam alur kerja data science.

## Kenapa Scikit-Learn Penting?

- Kemudahan Penggunaan: Antarmuka yang konsisten dan mudah dipahami.
- Beragam Algoritma: Menyediakan banyak algoritma machine learning yang siap pakai.
- Dokumentasi Lengkap: Dokumentasi yang baik dan banyak contoh penggunaan.
- Komunitas Besar: Dukungan dari komunitas yang aktif dan banyak sumber belajar.
- Integrasi: Bekerja dengan baik bersama library lain seperti Pandas dan NumPy.
- Kinerja: Dioptimalkan untuk performa yang baik pada dataset berukuran sedang hingga besar.
- Pipelines: Memudahkan pembuatan alur kerja machine learning yang kompleks.

## Instalasi Scikit-Learn

Kamu bisa menginstal Scikit-Learn menggunakan pip:

```bash
pip install scikit-learn
```

Atau jika kamu menggunakan Anaconda, Scikit-Learn sudah terinstal secara default.

```bash
conda install scikit-learn
```

## Contoh Penggunaan Dasar

Berikut adalah contoh sederhana bagaimana menggunakan Scikit-Learn untuk membuat model klasifikasi menggunakan algoritma K-Nearest Neighbors (KNN):

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Memuat dataset Iris
iris = load_iris()

X = iris.data
y = iris.target

# Membagi data menjadi data latih dan data uji
# test_size=0.2 berarti 20% data untuk uji, 80% untuk latih
# random_state=42 untuk hasil yang konsisten
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat model KNN
model = KNeighborsClassifier(n_neighbors=3)

# Melatih model
model.fit(X_train, y_train)

# Memprediksi data uji
predictions = model.predict(X_test)

print("Prediksi:", predictions)
```

## Sumber Belajar Scikit-Learn

- [Dokumentasi Resmi Scikit-Learn](https://scikit-learn.org/stable/documentation.html)
- [Tutorial Scikit-Learn di W3Schools](https://www.w3schools.com/python/scikit_learn_intro.asp)
- [Scikit-Learn Tutorial di GeeksforGeeks](https://www.geeksforgeeks.org/scikit-learn-tutorial/)
- [Kursus Scikit-Learn di DataCamp](https://www.datacamp.com/courses/supervised-learning-with-scikit-learn)
- [Scikit-Learn Beginner's Guide di Real Python](https://realpython.com/python-scikit-learn-guide/)
- [YouTube: Scikit-Learn Tutorial for Beginners](https://www.youtube.com/watch?v=0Lt9w-BxKFQ)
- [YouTube: Machine Learning with Scikit-Learn](https://www.youtube.com/watch?v=GJo0uNL-5Qw)
