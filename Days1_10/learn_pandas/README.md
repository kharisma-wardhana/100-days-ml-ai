# Pengantar Pandas

Pandas adalah library Python yang sangat populer untuk manipulasi dan analisis data. Library ini menyediakan struktur data yang fleksibel dan mudah digunakan, seperti DataFrame dan Series, yang memungkinkan kita untuk bekerja dengan data tabular secara efisien.

## Kenapa Pandas Penting?

- Memudahkan pembersihan dan transformasi data.
- Memungkinkan analisis data yang cepat dan intuitif.
- Banyak digunakan dalam proyek data science dan machine learning.
- Terintegrasi dengan baik dengan library lain seperti NumPy, Matplotlib, dan Scikit-learn.
- Mendukung berbagai format data (CSV, Excel, SQL, JSON, dll).
- Memiliki fungsi bawaan untuk agregasi, pengelompokan, dan visualisasi data.
- Komunitas yang besar dan dokumentasi yang lengkap.

## Instalasi Pandas

Kamu bisa menginstal Pandas menggunakan pip:

```bash
pip install pandas
```

Atau jika kamu menggunakan Anaconda, Pandas sudah terinstal secara default.

```bash
conda install pandas
```

## Contoh Penggunaan Dasar

Berikut adalah contoh sederhana bagaimana menggunakan Pandas untuk membuat DataFrame dan melakukan operasi dasar:

```python
import pandas as pd
# Membuat DataFrame dari dictionary
data = {
    'Nama': ['Andi', 'Budi', 'Citra'],
    'Umur': [25, 30, 22],
    'Kota': ['Jakarta', 'Bandung', 'Surabaya']
}
df = pd.DataFrame(data)
print(df)

# Mengakses kolom
print(df['Nama'])

# Mengakses baris
print(df.iloc[0])  # Baris pertama

# Menambahkan kolom baru
df['Pekerjaan'] = ['Insinyur', 'Dokter', 'Guru']
print(df)

# Menghitung statistik dasar
print(df.describe())
```

## Sumber Belajar Pandas

- [Dokumentasi Resmi Pandas](https://pandas.pydata.org/docs/)
- [Tutorial Pandas di W3Schools](https://www.w3schools.com/python/pandas/default.asp)
- [Kursus Pandas di DataCamp](https://www.datacamp.com/courses/pandas-foundations)
- [YouTube: Pandas Tutorial for Beginners](https://www.youtube.com/watch?v=vmEHCJofslg)
- [Blog: Pandas Tips and Tricks](https://realpython.com/pandas-python-explore-dataset/)
