# Pengenalan Matplotlib dan Seaborn

Matplotlib adalah library visualisasi data yang sangat populer di Python. Library ini memungkinkan kita untuk membuat berbagai jenis grafik dan plot, mulai dari grafik garis sederhana hingga visualisasi data yang kompleks. Seaborn adalah library berbasis Matplotlib yang menyediakan antarmuka tingkat tinggi untuk membuat visualisasi statistik yang menarik dan informatif dengan lebih sedikit kode.

## Kenapa Matplotlib dan Seaborn Penting?

- Visualisasi Data: Membantu dalam memahami data melalui representasi visual.
- Analisis Eksplorasi Data (EDA): Memudahkan dalam menemukan pola, tren, dan anomali dalam data.
- Presentasi: Membuat grafik yang menarik untuk laporan dan presentasi.
- Integrasi: Bekerja dengan baik bersama library lain seperti Pandas dan NumPy.
- Komunitas Besar: Banyak sumber belajar dan dokumentasi yang tersedia.
- Fleksibilitas: Dapat disesuaikan untuk berbagai kebutuhan visualisasi.
- Dukungan untuk Berbagai Jenis Grafik: Seperti grafik garis, batang, histogram, scatter plot, heatmap, dan banyak lagi.
- Meningkatkan Pemahaman: Membantu dalam memahami konsep statistik dan machine learning melalui visualisasi.

## Instalasi Matplotlib dan Seaborn
Kamu bisa menginstal Matplotlib dan Seaborn menggunakan pip:

```bash
pip install matplotlib seaborn
```

Atau jika kamu menggunakan Anaconda, Matplotlib dan Seaborn sudah terinstal secara default.

```bash
conda install matplotlib seaborn
```

## Contoh Penggunaan Dasar
Berikut adalah contoh sederhana bagaimana menggunakan Matplotlib dan Seaborn untuk membuat grafik dasar:

```python
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data contoh
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Grafik garis dengan Matplotlib
plt.plot(x, y)
plt.title('Grafik Garis Sine Wave')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()

# Grafik scatter dengan Seaborn
data = sns.load_dataset('iris')
sns.scatterplot(data=data, x='sepal_length', y='sepal_width', hue='species')
plt.title('Scatter Plot Sepal Length vs Sepal Width')
plt.show()
```

## Sumber Belajar Matplotlib dan Seaborn

- [Dokumentasi Resmi Matplotlib](https://matplotlib.org/stable/contents.html)
- [Dokumentasi Resmi Seaborn](https://seaborn.pydata.org/)
- [Tutorial Matplotlib di W3Schools](https://www.w3schools.com/python/matplotlib_intro.asp)
- [Tutorial Seaborn di W3Schools](https://www.w3schools.com/python/seaborn_intro.asp)
- [Matplotlib Tutorial di GeeksforGeeks](https://www.geeksforgeeks.org/matplotlib-tutorial/)
- [Seaborn Tutorial di GeeksforGeeks](https://www.geeksforgeeks.org/seaborn-tutorial/)
- [Kursus Matplotlib di DataCamp](https://www.datacamp.com/courses/introduction-to-data-visualization-with-matplotlib)
- [Kursus Seaborn di DataCamp](https://www.datacamp.com/courses/introduction-to-data-visualization-with-seaborn)
- [YouTube: Matplotlib Tutorial for Beginners](https://www.youtube.com/watch?v=UO98lJQ3QGI)
- [YouTube: Seaborn Tutorial for Beginners](https://www.youtube.com/watch?v=GcXcSZ0gQps)
