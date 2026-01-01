import pandas as pd

def main():
    # Membuat DataFrame Pandas dari dictionary
    data = {
        'Nama': ['Andi', 'Budi', 'Citra', 'Dewi', 'Eka'],
        'Umur': [23, 25, 22, 24, 26],
        'Kota': ['Jakarta', 'Bandung', 'Surabaya', 'Medan', 'Yogyakarta']
    }
    df = pd.DataFrame(data)
    
    # Menampilkan DataFrame dan informasi dasarnya
    print("DataFrame Pandas:")
    print(df)
    print("\nInformasi DataFrame:")
    print(df.info())
    
    # Operasi dasar pada DataFrame
    print("\nRata-rata umur:", df['Umur'].mean())
    print("Jumlah baris:", len(df))
    print("Daftar kota unik:", df['Kota'].unique())

    # Save DataFrame ke file CSV
    df.to_csv('data_pandas.csv', index=False)
    print("\nDataFrame telah disimpan ke 'data_pandas.csv'")

    # Read DataFrame dari file CSV
    df_loaded = pd.read_csv('data_pandas.csv')
    print("\nDataFrame yang dimuat dari 'data_pandas.csv':")
    print(df_loaded)

    # Filter data berdasarkan kondisi
    filtered_df = df[df['Umur'] > 23]
    print("\nDataFrame dengan umur > 23:")
    print(filtered_df)

    # Grouping data
    grouped_df = df.groupby('Kota').mean()
    print("\nRata-rata umur berdasarkan kota:")
    print(grouped_df)

    # Mengurutkan data berdasarkan umur
    sorted_df = df.sort_values(by='Umur', ascending=False)
    print("\nDataFrame diurutkan berdasarkan umur (descending):")
    print(sorted_df)

    # Menggabungkan dua DataFrame
    additional_data = {
        'Nama': ['Fajar', 'Gina'],
        'Umur': [27, 23],
        'Kota': ['Semarang', 'Malang']
    }   
    df_additional = pd.DataFrame(additional_data)
    combined_df = pd.concat([df, df_additional], ignore_index=True)
    print("\nDataFrame setelah penggabungan:")
    print(combined_df)

    # Pivot table sederhana
    pivot_df = df.pivot_table(values='Umur', index='Kota', aggfunc='mean')
    print("\nPivot Table rata-rata umur berdasarkan kota:")
    print(pivot_df)

    # Handling missing data
    df_with_nan = df.copy()
    df_with_nan.loc[2, 'Umur'] = None
    print("\nDataFrame dengan nilai NaN:")
    print(df_with_nan)

    # Mengisi nilai NaN dengan rata-rata umur
    df_filled = df_with_nan.fillna(df_with_nan['Umur'].mean())
    print("\nDataFrame setelah mengisi nilai NaN dengan rata-rata umur:")
    print(df_filled)

    # Menghapus baris dengan nilai NaN
    df_dropped_nan = df_with_nan.dropna()
    print("\nDataFrame setelah menghapus baris dengan nilai NaN:")
    print(df_dropped_nan)

    # Drop kolom
    df_dropped = df.drop(columns=['Kota'])
    print("\nDataFrame setelah menghapus kolom 'Kota':")
    print(df_dropped)

    # Drop baris dengan kondisi
    df_dropped_rows = df[df['Umur'] >= 24]
    print("\nDataFrame setelah menghapus baris dengan umur < 24:")
    print(df_dropped_rows)

    # Drop duplikat
    df_with_duplicates = pd.concat([df, df.iloc[0:2]], ignore_index=True)
    print("\nDataFrame dengan duplikat:")
    print(df_with_duplicates)
    df_no_duplicates = df_with_duplicates.drop_duplicates()
    print("\nDataFrame setelah menghapus duplikat:")
    print(df_no_duplicates)

    # Statistik deskriptif
    print("\nStatistik deskriptif DataFrame:")
    print(df.describe())

if __name__ == "__main__":
    main()