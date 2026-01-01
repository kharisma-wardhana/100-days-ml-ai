# Pengenalan Numpy

Numpy adalah library fundamental untuk komputasi ilmiah di Python. Library ini menyediakan dukungan untuk array multidimensi, fungsi matematika tingkat tinggi, dan alat-alat yang efisien untuk manipulasi data numerik.

## Kenapa Numpy Penting?

- Performa tinggi: Numpy dioptimalkan untuk operasi numerik yang cepat.
- Array multidimensi: Memudahkan penyimpanan dan manipulasi data dalam bentuk matriks atau tensor.
- Fungsi matematika: Menyediakan berbagai fungsi matematika yang efisien untuk operasi pada array.
- Integrasi: Bekerja dengan baik bersama library lain seperti Pandas, Matplotlib, dan Scikit-learn.
- Komunitas besar: Banyak sumber belajar dan dokumentasi yang tersedia.
- Dasar untuk machine learning: Banyak algoritma machine learning menggunakan Numpy untuk komputasi numerik.

## Instalasi Numpy
Kamu bisa menginstal Numpy menggunakan pip:

```bash
pip install numpy
```

Atau jika kamu menggunakan Anaconda, Numpy sudah terinstal secara default.

```bash
conda install numpy
```

## Contoh Penggunaan Dasar
Berikut adalah contoh sederhana bagaimana menggunakan Numpy untuk membuat array dan melakukan operasi dasar:

```python
import numpy as np

# Membuat array 1D
arr1d = np.array([1, 2, 3, 4, 5])
print("Array 1D:", arr1d)

# Membuat array 2D
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("Array 2D:\n", arr2d)

# Operasi dasar
print("Penjumlahan:", arr1d + 5)
print("Perkalian:", arr1d * 2)
print("Transpose Array 2D:\n", arr2d.T)
```

## Sumber Belajar Numpy

- [Dokumentasi Resmi Numpy](https://numpy.org/doc/)
- [Tutorial Numpy di W3Schools](https://www.w3schools.com/python/numpy_intro.asp)
- [Numpy Tutorial di GeeksforGeeks](https://www.geeksforgeeks.org/python-numpy-tutorial/)
- [Kursus Numpy di DataCamp](https://www.datacamp.com/courses/intro-to-python-for-data-science)
- [NumPy Beginner's Guide di Real Python](https://realpython.com/numpy-tutorial/)
