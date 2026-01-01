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

if __name__ == "__main__":
    main()