import numpy as np

def main():
    # Membuat array NumPy dari list Python
    data = [1, 2, 3, 4, 5]
    np_array = np.array(data)
    
    # Menampilkan array dan tipe datanya
    print("Array NumPy:", np_array)
    print("Tipe data array:", np_array.dtype)
    
    # Operasi dasar pada array
    print("Penjumlahan semua elemen:", np.sum(np_array))
    print("Rata-rata elemen:", np.mean(np_array))
    print("Elemen maksimum:", np.max(np_array))
    print("Elemen minimum:", np.min(np_array))

    # Membuat array 2D (matriks)
    matrix_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    np_matrix = np.array(matrix_data)
    print("\nMatriks NumPy:\n", np_matrix)

    # Operasi dasar pada matriks
    print("Transpose matriks:\n", np_matrix.T)
    print("Jumlah setiap kolom:", np.sum(np_matrix, axis=0))
    print("Jumlah setiap baris:", np.sum(np_matrix, axis=1))
    print("Matriks setelah dikalikan dengan 2:\n", np_matrix * 2)

    # Menggunakan fungsi NumPy untuk membuat array khusus
    zeros_array = np.zeros((3, 3))
    ones_array = np.ones((2, 4))
    random_array = np.random.rand(3, 2)
    print("\nArray nol 3x3:\n", zeros_array)
    print("Array satu 2x4:\n", ones_array)
    print("Array acak 3x2:\n", random_array)

if __name__ == "__main__":
    main()