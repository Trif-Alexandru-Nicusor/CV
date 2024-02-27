import os
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from joblib import dump, load
import numpy as np
# Seteaza calea catre folderul cu CSV-uri
folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'CSV De Antrenare')
# Lista pentru a stoca toate cadrele de date încarcate
dataframes = []
# Parcurge toate fisierele CSV din folder
for file in os.listdir(folder_path):
    if file.endswith(".csv"):
        file_path = os.path.join(folder_path, file)
        df = pd.read_csv(file_path)
        dataframes.append(df)
# Concateneaza toate cadrele de date intr-un singur DataFrame
training_data = pd.concat(dataframes, ignore_index=True)
# Pregateste datele pentru antrenare
X = training_data.drop("Kw", axis=1)
y = training_data["Kw"]
# Convertiti variabilele categorice in variabile one-hot (dacă exista)
if 'Sezon' in X.columns:
    X_encoded = pd.get_dummies(X, columns=["Sezon"])
else:
    X_encoded = X
# Verifica dacă exista deja un model antrenat
model_filename = rf"{os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Modele')}\trained_model.joblib"
scaler_filename = rf"{os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Modele')}\trained_scaler.joblib"
if os.path.exists(model_filename):
    # Încarca modelul antrenat
    model = load(model_filename)
    # Încarca scaler-ul asociat modelului
    scaler = load(scaler_filename)
    # Continua antrenarea modelului
    model.warm_start = True
else:
    # Construieste si antreneaza un scaler nou
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X_encoded)
    # Salveaza scaler-ul antrenat
    dump(scaler, scaler_filename)
    # Construieste și antreneaza un model nou
    model = MLPRegressor(hidden_layer_sizes=(100, 50), max_iter=1000, random_state=42, alpha=0.001)
    model.warm_start = False
    # Antreneaza modelul cu datele de antrenare existente
    model.fit(X_scaled, y)
# Realizeaza predictii pe setul de testare
X_test_scaled = scaler.transform(X_encoded)  # Normalizare pentru setul de testare
y_pred = model.predict(X_test_scaled)
# Calculeaza și afișează Root Mean Squared Error (RMSE) si coeficientul de determinare (R^2)
rmse = np.sqrt(mean_squared_error(y, y_pred))
r2 = r2_score(y, y_pred)
print(f"Root Mean Squared Error on Test Data: {rmse}")
print(f"R^2 Score on Test Data: {r2}")
# Salveaza modelul antrenat sau modelul continuu antrenat
dump(model, model_filename)
print(f"Trained model saved to {model_filename}")
