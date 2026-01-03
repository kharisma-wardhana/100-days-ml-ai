# Unsupervised Learning - Clustering

## Pengertian Unsupervised Learning - Clustering

Clustering adalah teknik dalam machine learning yang digunakan untuk mengelompokkan data berdasarkan kemiripan atau jarak antar data tersebut. Berbeda dengan supervised learning yang menggunakan label untuk melatih model, clustering tidak memerlukan label dan bertujuan untuk menemukan pola atau struktur tersembunyi dalam data.

## Proses Clustering

1. **Pengumpulan Data**: Kumpulkan dataset yang akan digunakan untuk clustering.
2. **Preprocessing Data**: Bersihkan data, tangani nilai yang hilang, dan lakukan normalisasi atau standarisasi jika diperlukan.
3. **Pemilihan Algoritma Clustering**: Pilih algoritma clustering yang sesuai dengan karakteristik data dan tujuan analisis.
4. **Menentukan Jumlah Klaster**: Tentukan jumlah klaster yang diinginkan (jika diperlukan oleh algoritma).
5. **Pelatihan Model Clustering**: Terapkan algoritma clustering pada data untuk mengelompokkan data.
6. **Evaluasi Hasil Clustering**: Gunakan metrik evaluasi seperti Silhouette Score, Davies-Bouldin Index, atau Calinski-Harabasz Index untuk menilai kualitas klaster yang dihasilkan.
7. **Visualisasi Klaster**: Gunakan teknik visualisasi seperti scatter plot, t-SNE, atau PCA untuk memvisualisasikan hasil clustering.
8. **Interpretasi Hasil**: Analisis dan interpretasikan klaster yang dihasilkan untuk mendapatkan wawasan dari data.
9. **Iterasi**: Jika hasil clustering tidak memuaskan, ulangi proses dengan menyesuaikan parameter atau memilih algoritma yang berbeda.
10. **Dokumentasi**: Mencatat proses, keputusan, dan hasil untuk referensi di masa depan.

## Contoh Algoritma Clustering

1. **K-Means Clustering**: Algoritma yang membagi data menjadi k klaster berdasarkan jarak Euclidean.
2. **Hierarchical Clustering**: Algoritma yang membangun hirarki klaster dengan metode agglomerative atau divisive.
3. **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**: Algoritma yang mengelompokkan data berdasarkan kepadatan titik data.
4. **HDBSCAN ()**: Versi lanjutan dari DBSCAN yang dapat menangani klaster dengan kepadatan yang bervariasi.
5. **Gaussian Mixture Models (GMM)**: Model probabilistik yang mengasumsikan data berasal dari campuran beberapa distribusi Gaussian.
6. **Mean Shift**: Algoritma yang mengelompokkan data dengan menggeser titik data ke area dengan kepadatan tertinggi.
7. **Spectral Clustering**: Algoritma yang menggunakan spektrum (eigenvalues) dari matriks kesamaan data untuk melakukan clustering.
8. **Affinity Propagation**: Algoritma yang mengelompokkan data dengan mengirim pesan antar titik data untuk menentukan klaster.
9. **Birch (Balanced Iterative Reducing and Clustering using Hierarchies)**: Algoritma yang efisien untuk clustering data besar dengan membangun pohon klaster.
10. **Self-Organizing Maps (SOM)**: Jaringan saraf tiruan yang digunakan untuk visualisasi dan clustering data berdimensi tinggi.

## Metrik Evaluasi Clustering

1. **Silhouette Score**: Mengukur seberapa mirip sebuah objek dengan klasternya sendiri dibandingkan dengan klaster lain.
2. **Davies-Bouldin Index**: Mengukur rasio jarak antar klaster terhadap ukuran klaster itu sendiri.
3. **Calinski-Harabasz Index**: Mengukur rasio antara variansi antar klaster dan variansi dalam klaster.
4. **Dunn Index**: Mengukur jarak minimum antar klaster dibandingkan dengan ukuran maksimum klaster.
5. **Adjusted Rand Index (ARI)**: Mengukur kesamaan antara dua hasil clustering dengan memperhitungkan kemungkinan pengelompokan acak.
6. **Normalized Mutual Information (NMI)**: Mengukur informasi bersama antara dua hasil clustering.
7. **Homogeneity, Completeness, V-Measure**: Metrik yang mengukur kualitas clustering berdasarkan kesamaan dan kelengkapan klaster.
8. **Elbow Method**: Teknik visual untuk menentukan jumlah klaster optimal dengan melihat perubahan dalam inertia (jumlah kuadrat jarak dalam klaster).
9. **Gap Statistic**: Metode untuk menentukan jumlah klaster optimal dengan membandingkan total intracluster variation dengan yang diharapkan di bawah distribusi acak.
10. **Silhouette Analysis**: Teknik visual untuk menilai kualitas clustering dengan memplot silhouette scores untuk setiap titik data.

## Hyperparameter yang Bisa Di-tuning

1. **K-Means Clustering**: Jumlah klaster (k), metode inisialisasi (misalnya, k-means++), jumlah iterasi maksimum.
2. **Hierarchical Clustering**: Metode penggabungan (linkage method), metrik jarak (misalnya, Euclidean, Manhattan).
3. **DBSCAN**: Epsilon (jarak maksimum antar titik untuk dianggap sebagai tetangga), min_samples (jumlah minimum titik dalam radius epsilon untuk membentuk klaster).
4. **HDBSCAN**: min_cluster_size (ukuran minimum klaster), min_samples (jumlah minimum titik untuk membentuk inti klaster).
5. **Gaussian Mixture Models (GMM)**: Jumlah komponen Gaussian, jenis kovarians (full, tied, diag, spherical).
6. **Mean Shift**: Bandwidth (ukuran jendela untuk estimasi kepadatan).
7. **Spectral Clustering**: Jumlah klaster, jenis metrik kesamaan.
8. **Affinity Propagation**: Damping factor, preferensi (preference).
9. **Birch**: Threshold (ambang batas untuk pembentukan sub-klaster), jumlah klaster akhir.
10. **Self-Organizing Maps (SOM)**: Ukuran grid, laju pembelajaran (learning rate), radius tetangga.

## Contoh Penggunaan K-Means Clustering dengan Scikit-Learn

```python
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt

# Membuat dataset contoh
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Menerapkan K-Means Clustering
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)
y_kmeans = kmeans.predict(X)

# Visualisasi hasil clustering
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=50, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.75)
plt.show()
```

## Contoh Penggunaan DBSCAN dengan Scikit-Learn

```python
from sklearn.cluster import DBSCAN
from sklearn.datasets import make_moons
import matplotlib.pyplot as plt

# Membuat dataset contoh
X, y = make_moons(n_samples=300, noise=0.05, random_state=0)

# Menerapkan DBSCAN
dbscan = DBSCAN(eps=0.2, min_samples=5)
y_dbscan = dbscan.fit_predict(X)

# Visualisasi hasil clustering
plt.scatter(X[:, 0], X[:, 1], c=y_dbscan, s=50, cmap='viridis')
plt.show()
```
