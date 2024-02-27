from nicegui import ui
import main , os , csv
from io import StringIO
import pandas as pd
from sklearn.preprocessing import StandardScaler
from joblib import load
import numpy as np
folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'A se prezice')
models = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Modele')
prezicerea = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Prezicerea')
def addData(season , hour , temperature , shaodow , radiation , table):
    if season.value and hour.value and temperature.value and shaodow.value and radiation.value != '':
        table.add_rows({'Sezon' : season.value , 'Ora' : hour.value , 'Temperatura' : temperature.value , 'Umbra' : shaodow.value , 'Radiatia Solara' : radiation.value})
        season.value , hour.value , temperature.value , shaodow.value , radiation.value = '' , '' , '' , '' , ''
    else:
        ui.notify('Trebuie adaugate in toate casutele valori .' , position = 'center')
def startPrediction(table):
    data = table.rows
    csv_file_path = rf'{folder}\A se prezice.csv'
    with open(csv_file_path, 'w', newline='') as csv_file:
        fieldnames = ['Sezon', 'Ora', 'Temperatura', 'Umbra', 'Radiatia Solara']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    # Seteaza calea catre fisierul CSV cu datele noi
    new_data_path = folder
    # Incarca datele noi intr-un DataFrame
    new_data = pd.read_csv(new_data_path)
    # Adauga o coloana 'Kw' initializata cu NaN (sau o valoare implicita)
    new_data['Kw'] = np.nan
    # Pregatește datele pentru predictie
    X_new = new_data.drop("Kw", axis=1)  # Excludem coloana de iesire ("Kw") din datele noi
    # Variabilele categorice in variabile one-hot (dacă exista)
    if 'Sezon' in X_new.columns:
        X_new_encoded = pd.get_dummies(X_new, columns=["Sezon"])
    else:
        X_new_encoded = X_new
    # Incarcă modelul antrenat
    model_filename = rf"{models}\trained_model.joblib"
    model = load(model_filename)
    # Incarcă si scaler-ul folosit în timpul antrenarii
    scaler_filename = rf"{models}\trained_scaler.joblib"
    scaler = load(scaler_filename)
    # Utilizeaza scaler-ul pentru a normaliza datele noi
    X_new_scaled = scaler.transform(X_new_encoded)
    # Realizeaza predictii pe datele noi
    y_pred_new = model.predict(X_new_scaled)
    # Actualizeaza coloana 'Kw' cu valorile prezise
    output_csv_path = rf"{prezicerea}\Rezultat.csv"
    new_data['Kw'] = y_pred_new
    new_data.to_csv(output_csv_path, index=False)
    table.rows = []
    table.update
    csv_file_path = rf'{prezicerea}\Rezultat.csv'
    data_list = []
    with open(csv_file_path, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data_dict = {
                'Sezon': row['Sezon'],
                'Ora': row['Ora'],
                'Temperatura': row['Temperatura'],
                'Umbra': row['Umbra'],
                'Radiatia Solara': row['Radiatia Solara'],
                'Kw' : row['Kw']
            }
            data_list.append(data_dict)
    for data_dict in data_list:
        table.add_rows(data_dict)
