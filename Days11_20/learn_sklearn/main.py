import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

def main():
    # Membuat DataFrame Pandas dari dictionary
    data = {
        'Luas_Rumah': [50, 60, 70, 80, 90, 100, 110, 120, 130, 140],
        'Harga_Rumah': [150, 180, 200, 220, 250, 270, 300, 320, 350, 400]
    }
    df = pd.DataFrame(data)
    
    # Menampilkan DataFrame
    print("DataFrame Pandas:")
    print(df)

    # Memisahkan fitur dan target variable
    X = df[['Luas_Rumah']]
    y = df['Harga_Rumah']

    # Membagi data menjadi training dan testing set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Membuat model regresi linear
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Memprediksi harga rumah pada testing set
    y_pred = model.predict(X_test)

    # Evaluasi model
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print("\nEvaluasi Model:")
    print(f"Mean Squared Error: {mse}")
    print(f"R^2 Score: {r2}")

    # Menampilkan koefisien regresi
    print("\nKoefisien Regresi:")
    print(f"Intercept: {model.intercept_}")
    print(f"Coefficient: {model.coef_[0]}")

if __name__ == "__main__":
    main()
