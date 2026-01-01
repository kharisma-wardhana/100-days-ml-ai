import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Membuat DataFrame Pandas dari dictionary
    data = {
        'Nama': ['Andi', 'Budi', 'Citra', 'Dewi', 'Eka'],
        'Umur': [23, 25, 22, 24, 26],
        'Kota': ['Jakarta', 'Bandung', 'Surabaya', 'Medan', 'Yogyakarta']
    }
    df = pd.DataFrame(data)
    
    # Menampilkan DataFrame
    print("DataFrame Pandas:")
    print(df)

    # Visualisasi data menggunakan Matplotlib dan Seaborn
    plt.figure(figsize=(8, 5))
    sns.barplot(x='Nama', y='Umur', data=df, palette='viridis')
    plt.title('Umur berdasarkan Nama')
    plt.xlabel('Nama')
    plt.ylabel('Umur')
    plt.ylim(20, 30)
    plt.grid(axis='y')
    plt.show()

    # Visualisasi distribusi umur
    plt.figure(figsize=(8, 5))
    sns.histplot(df['Umur'], bins=5, kde=True, color='blue')
    plt.title('Distribusi Umur')
    plt.xlabel('Umur')
    plt.ylabel('Frekuensi')
    plt.grid(axis='y')
    plt.show()

    # Scatter plot antara Umur dan indeks
    plt.figure(figsize=(8, 5))
    sns.scatterplot(x=df.index, y='Umur', data=df, s=100, color='red')
    plt.title('Scatter Plot Umur vs Indeks')
    plt.xlabel('Indeks')
    plt.ylabel('Umur')
    plt.grid()
    plt.show()

    # Heatmap sederhana
    plt.figure(figsize=(6, 4))
    corr = df[['Umur']].corr()
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title('Heatmap Korelasi Umur')
    plt.show()

    # Boxplot umur berdasarkan kota
    plt.figure(figsize=(8, 5))
    sns.boxplot(x='Kota', y='Umur', data=df, palette='Set2')
    plt.title('Boxplot Umur berdasarkan Kota')
    plt.xlabel('Kota')
    plt.ylabel('Umur')
    plt.grid(axis='y')
    plt.show()

if __name__ == "__main__":
    main()
