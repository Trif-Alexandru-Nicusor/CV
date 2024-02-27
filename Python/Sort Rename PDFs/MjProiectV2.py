# Importă modulele necesare din PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
# Importă widget-urile specifice din PyQt5
from PyQt5.QtWidgets import QFileDialog, QMessageBox
# Importă alte biblioteci necesare
import os, pandas as pd, docx2txt, logging, shutil
# Importă clasa Workbook din openpyxl pentru manipularea fișierelor Excel
from openpyxl import Workbook
# Configurează înregistrarea erorilor pentru a le scrie în fișierul "error_log.txt"
logging.basicConfig(filename='error_log.txt', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
# Clasa pentru interfața grafică (GUI)
class Ui_MainWindow(object):
    # Variabile globale pentru locațiile fișierelor Excel și a folderului cu PDF-uri
    global locatieexcel, locatiepdfuri
    locatieexcel, locatiepdfuri = "", ""
    # Metoda pentru configurarea interfeței grafice
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 143)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Definirea butonului "Select Excel" în interfață
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 10, 111, 23))
        self.pushButton.setObjectName("pushButton")
        # Definirea etichetei pentru afișarea locației fișierului Excel
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 1000, 16))
        self.label.setObjectName("label")
        # Definirea butonului "Selectează folderul cu PDF-uri" în interfață
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 50, 271, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        # Definirea etichetei pentru afișarea locației folderului cu PDF-uri
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 50, 1000, 16))
        self.label_2.setObjectName("label_2")
        # Definirea etichetei pentru afișarea numelui fișierului
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 85, 1000, 16))
        self.label_3.setObjectName("label_3")
        # Definirea câmpului de editare pentru introducerea numelui fișierului
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(105, 85, 509, 20))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        # Definirea butonului "Schimba pas cu pas" în interfață
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 120, 171, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        # Definirea butonului "Schimba tot odata" în interfață
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(190, 120, 161, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        # Definirea butonului "Conversie Word la Excel" în interfață
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(370, 120, 210, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        # Setarea widget-ului central al ferestrei principale
        MainWindow.setCentralWidget(self.centralwidget)
        # Traducerea textului în interfață în funcție de limbă
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    # Metoda pentru traducerea textului în interfață
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Mj-PDFs", "Mj-PDFs"))
        self.pushButton.setText(_translate("Mj-PDFs", "Select Excel"))
        self.label.setText(_translate("Mj-PDFs", f"Locație Excel:"))
        self.pushButton_2.setText(_translate("Mj-PDFs", "Selectează folderul cu PDF-uri"))
        self.label_2.setText(_translate("Mj-PDFs", "Locație folder:"))
        self.label_3.setText(_translate("Mj-PDFs", "Nume fișier:"))
        self.pushButton_3.setText(_translate("Mj-PDFs", "Schimbă pas cu pas"))
        self.pushButton_4.setText(_translate("Mj-PDFs", "Schimbă tot odată"))
        self.pushButton_5.setText(_translate("Mj-PDFs", "Conversie Word la Excel"))
        # Conectarea butoanelor la funcțiile corespunzătoare
        self.pushButton.clicked.connect(self.selectExcel) # Cand butonul este apăsat, va acționa funcția "selectExcel"
        self.pushButton_2.clicked.connect(self.locatiePDFURI)
        self.pushButton_3.clicked.connect(self.schimbaPasCuPas)
        self.pushButton_4.clicked.connect(self.schimbaTot)
        self.pushButton_5.clicked.connect(self.conversie) # Cand butonul este apăsat, va acționa funcția "conversie"
    def conversie(self):
        global locatieword
        locatieword, _ = QFileDialog.getOpenFileName()  # Deschide dialogul pentru selectarea unui fișier Word (docx)
        text = docx2txt.process(locatieword)  # Transformă conținutul fișierului Word în text
        lines = text.split('\n')  # Imparte textul în linii separate
        lines = [line.replace("/", " din ").replace("\t", "") for line in lines if line.strip()]  # Procesează și cureță liniile de text
        workbook = Workbook()  # Creează un nou fișier Excel (Workbook)
        sheet = workbook.active  # Selectează foaia activă (implicit prima foaie) din fișierul Excel
        for line in lines:
            sheet.append([line])  # Adaugă fiecare linie procesată în fișierul Excel
        workbook.save(rf'{os.path.dirname(locatieword)}\rezultat.xlsx')  # Salvează fișierul Excel cu numele "rezultat.xlsx" în același director cu fișierul Word
    def selectExcel(self):
        global locatieexcel, valori
        locatieexcel, _ = QFileDialog.getOpenFileName()  # Deschide dialogul pentru selectarea unui fișier Excel (xlsx)
        self.label.setText(f"Locatie Excel:{locatieexcel}")  # Afișează locația fișierului Excel în etichetă
        df = pd.read_excel(rf'{locatieexcel}', header=None)  # Citeste datele din fișierul Excel și le salvează într-un DataFrame
        first_column_values = df.iloc[:, 0]  # Extrage valorile din prima coloană a DataFrame-ului
        values_array = first_column_values.to_numpy()  # Converteste valorile într-un numpy array
        valori = []
        for value in values_array:
            value_str = str(value)
            valori.append(value_str)  # Salvează valorile din prima coloană într-o listă numită "valori"
    def locatiePDFURI(self):
        global locatiepdfuri, sorted_files
        locatiepdfuri = QFileDialog.getExistingDirectory(None, "Select Folder")  # Deschide dialogul pentru selectarea unui folder
        self.label_2.setText(f"Locatie folder: {locatiepdfuri}")  # Afișează locația folderului cu PDF-uri în etichetă
        files = os.listdir(locatiepdfuri)  # Lista fișierelor din folder
        number_files = [file for file in files if file.endswith(".pdf") and any(char.isdigit() for char in file)]  # Filtrarea fișierelor PDF care conțin cifre în nume
        sorted_files = sorted(number_files, key=lambda x: int(''.join(filter(str.isdigit, x))))  # Sortează fișierele în ordinea numerelor conținute în numele lor
        if not os.path.exists(os.path.join(locatiepdfuri, "De avere")):
            os.makedirs(os.path.join(locatiepdfuri, "De avere"))  # Creează folderul "De avere" dacă nu există
        if not os.path.exists(os.path.join(locatiepdfuri, "De interes")):
            os.makedirs(os.path.join(locatiepdfuri, "De interes"))  # Creează folderul "De interes" dacă nu există
    # Variabile globale pentru contorizarea numerelor de înregistrări procesate
    global nr, nr2
    nr, nr2 = 0, 0
    def schimbaPasCuPas(self):
        global nr, nr2, locatieexcel, locatiepdfuri, valori, sorted_files, numefolder
        try:
            #Funție care verifică dacă există în numele fișierului stringul nr și înlocuieșste ce este înainte de el cu declarație de avere sau declarație de interes
            def inaintedenr(string, value):
                global numefolder
                string_parts = string.split('nr')
                string_parts[0] = value
                beforenr = string.split('nr')[0]
                numefolder = beforenr
                return 'nr'.join(string_parts)
            if locatieexcel == "" or locatiepdfuri == "":
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Ai uitat să selectezi locația PDF-urilor sau locația Excel-ului!")
                msg.setWindowTitle("Mj-PDFs")
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec_()
            else:
                if int(nr) < len(valori) and int(nr2) < len(sorted_files):
                    if valori[nr] == "De avere:":
                        locatia = "De avere"
                        nr = int(nr) + 1
                    elif valori[nr] == "De interes:":
                        locatia = "De interes"
                        nr = int(nr) + 1
                    if locatia == "De avere":
                        ceva = inaintedenr(valori[nr], "Declaratia de avere ")
                        folder_path = os.path.join(locatiepdfuri, "De avere", numefolder)
                        if not os.path.exists(folder_path):
                            os.makedirs(folder_path)
                        original_file_path = os.path.join(locatiepdfuri, sorted_files[nr2])
                        new_file_path = os.path.join(folder_path, f"{ceva}.pdf")
                        os.rename(original_file_path, new_file_path)  # Redenumește și mută fișierul în folderul corespunzător
                        self.lineEdit.setText(new_file_path)  # Afișează noua cale a fișierului în câmpul de editare
                    elif locatia == "De interes":
                        ceva = inaintedenr(valori[nr], "Declaratia de interes ")
                        folder_path = os.path.join(locatiepdfuri, "De interes", numefolder)
                        if not os.path.exists(folder_path):
                            os.makedirs(folder_path)
                        original_file_path = os.path.join(locatiepdfuri, sorted_files[nr2])
                        new_file_path = os.path.join(folder_path, f"{ceva}.pdf")
                        os.rename(original_file_path, new_file_path)  # Redenumește și mută fișierul în folderul corespunzător
                        self.lineEdit.setText(new_file_path)  # Afișează noua cale a fișierului în câmpul de editare
                    nr = int(nr) + 1
                    nr2 = int(nr2) + 1
                else:
                    nr = int(nr) * 0  # Resetează contorii la zero
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText("Tot a fost redenumit și mutat!")
                    msg.setWindowTitle("Mj-PDFs")
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.exec_()
        except Exception as e:
            logging.exception("Exception occurred in schimbaPasCuPas method: %s", str(e))  # Înregistrează excepția în fișierul de logare
    # Metoda schimbaTot este similară cu metoda schimbaPasCuPas, dar procesează automat toate înregistrările fără a cere intervenția utilizatorului
    def schimbaTot(self):
        global nr, nr2, locatieexcel, locatiepdfuri, valori, sorted_files, numefolder
        #Funție care verifică dacă există în numele fișierului stringul nr și înlocuieșste ce este înainte de el cu declarație de avere sau declarație de interes
        def inaintedenr(string, value):
            global numefolder
            string_parts = string.split('nr')
            string_parts[0] = value
            beforenr = string.split('nr')[0]
            numefolder = beforenr
            return 'nr'.join(string_parts)
        # Verifică dacă au fost selectate locațiile pentru fișierul Excel și folderul cu PDF-uri
        if locatieexcel == "" or locatiepdfuri == "":
            # Dacă lipsește cel puțin una dintre locații, se afișează un mesaj de avertizare
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Ai uitat să selectezi locația PDF-urilor sau locația Excel-ului!")
            msg.setWindowTitle("Mj-PDFs")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
        else:
            # Începe procesarea automată a fișierelor PDF și redenumirea/mutarea lor în folderele corespunzătoare
            while int(nr) < len(valori) and int(nr2) < len(sorted_files):
                if valori[nr] == "De avere:":
                    locatia = "De avere"
                    nr = int(nr) + 1
                elif valori[nr] == "De interes:":
                    locatia = "De interes"
                    nr = int(nr) + 1
                if locatia == "De avere":
                    # Redenumește și mută fișierul PDF în folderul "De avere"
                    ceva = inaintedenr(valori[nr], "Declaratia de avere ")
                    folder_path = os.path.join(locatiepdfuri, "De avere", numefolder)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    original_file_path = os.path.join(locatiepdfuri, sorted_files[nr2])
                    new_file_path = os.path.join(folder_path, f"{ceva}.pdf")
                    os.rename(original_file_path, new_file_path)  # Redenumește și mută fișierul în folderul corespunzător
                    self.lineEdit.setText(new_file_path)  # Afișează noua cale a fișierului în câmpul de editare
                elif locatia == "De interes":
                    # Redenumește și mută fișierul PDF în folderul "De interes"
                    ceva = inaintedenr(valori[nr], "Declaratia de interes ")
                    folder_path = os.path.join(locatiepdfuri, "De interes", numefolder)
                    if not os.path.exists(folder_path):
                        os.makedirs(folder_path)
                    original_file_path = os.path.join(locatiepdfuri, sorted_files[nr2])
                    new_file_path = os.path.join(folder_path, f"{ceva}.pdf")
                    os.rename(original_file_path, new_file_path)  # Redenumește și mută fișierul în folderul corespunzător
                    self.lineEdit.setText(new_file_path)  # Afișează noua cale a fișierului în câmpul de editare
                nr = int(nr) + 1  # Incrementare contor pentru următoarea valoare din fișierul Excel
                nr2 = int(nr2) + 1  # Incrementare contor pentru următorul fișier PDF din folder
            # Procesarea automată a fișierelor PDF a fost finalizată
            nr = int(nr) * 0  # Resetează contorii la zero
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Tot a fost redenumit și mutat!")
            msg.setWindowTitle("Mj-PDFs")
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec_()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
