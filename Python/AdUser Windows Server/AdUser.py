from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTreeWidgetItem
import subprocess,smtplib,os,datetime
from email.mime.text import MIMEText
#Functie pentru a gasi pathul executabilului
def get_executable_directory():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(os.path.abspath(sys.argv[0]))
global locatie, subitem_text,column_name,item_text,powershell_code
locatie="Users"
#Interfata
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Creare/Resetare Cont")
        MainWindow.resize(995, 499)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1001, 501))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.treeWidget = QtWidgets.QTreeWidget(self.tab)
        self.treeWidget.setGeometry(QtCore.QRect(0, 0, 581, 461))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.treeWidget.setFont(font)
        self.treeWidget.setObjectName("treeWidget")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(590, 10, 111, 16))
        self.label.setObjectName("label")
        self.crearePrenume = QtWidgets.QLineEdit(self.tab)
        self.crearePrenume.setGeometry(QtCore.QRect(710, 10, 281, 20))
        self.crearePrenume.setObjectName("crearePrenume")
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(590, 40, 91, 16))
        self.label_2.setObjectName("label_2")
        self.creareNume = QtWidgets.QLineEdit(self.tab)
        self.creareNume.setGeometry(QtCore.QRect(680, 40, 311, 20))
        self.creareNume.setObjectName("creareNume")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(590, 70, 141, 16))
        self.label_3.setObjectName("label_3")
        self.creareTotNumele = QtWidgets.QLineEdit(self.tab)
        self.creareTotNumele.setGeometry(QtCore.QRect(730, 70, 261, 20))
        self.creareTotNumele.setObjectName("creareTotNumele")
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setGeometry(QtCore.QRect(590, 100, 71, 16))
        self.label_4.setObjectName("label_4")
        self.creareBirou = QtWidgets.QLineEdit(self.tab)
        self.creareBirou.setGeometry(QtCore.QRect(670, 100, 321, 20))
        self.creareBirou.setObjectName("creareBirou")
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(590, 130, 81, 16))
        self.label_5.setObjectName("label_5")
        self.creareNrTel = QtWidgets.QLineEdit(self.tab)
        self.creareNrTel.setGeometry(QtCore.QRect(670, 130, 321, 20))
        self.creareNrTel.setObjectName("creareNrTel")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(590, 160, 71, 16))
        self.label_6.setObjectName("label_6")
        self.creareJudet = QtWidgets.QLineEdit(self.tab)
        self.creareJudet.setGeometry(QtCore.QRect(660, 160, 331, 20))
        self.creareJudet.setObjectName("creareJudet")
        self.label_7 = QtWidgets.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(590, 190, 61, 16))
        self.label_7.setObjectName("label_7")
        self.creareOras = QtWidgets.QLineEdit(self.tab)
        self.creareOras.setGeometry(QtCore.QRect(660, 190, 331, 20))
        self.creareOras.setObjectName("creareOras")
        self.label_8 = QtWidgets.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(590, 220, 81, 16))
        self.label_8.setObjectName("label_8")
        self.creareStrada = QtWidgets.QLineEdit(self.tab)
        self.creareStrada.setGeometry(QtCore.QRect(670, 220, 321, 20))
        self.creareStrada.setObjectName("creareStrada")
        self.label_9 = QtWidgets.QLabel(self.tab)
        self.label_9.setGeometry(QtCore.QRect(590, 250, 91, 16))
        self.label_9.setObjectName("label_9")
        self.creareFunctia = QtWidgets.QLineEdit(self.tab)
        self.creareFunctia.setGeometry(QtCore.QRect(680, 250, 311, 20))
        self.creareFunctia.setObjectName("creareFunctia")
        self.label_10 = QtWidgets.QLabel(self.tab)
        self.label_10.setGeometry(QtCore.QRect(590, 280, 141, 21))
        self.label_10.setObjectName("label_10")
        self.creareDepartament = QtWidgets.QLineEdit(self.tab)
        self.creareDepartament.setGeometry(QtCore.QRect(740, 280, 251, 20))
        self.creareDepartament.setObjectName("creareDepartament")
        self.label_11 = QtWidgets.QLabel(self.tab)
        self.label_11.setGeometry(QtCore.QRect(590, 310, 91, 21))
        self.label_11.setObjectName("label_11")
        self.creareInsitutia = QtWidgets.QLineEdit(self.tab)
        self.creareInsitutia.setGeometry(QtCore.QRect(690, 310, 301, 20))
        self.creareInsitutia.setObjectName("creareInsitutia")
        self.label_12 = QtWidgets.QLabel(self.tab)
        self.label_12.setGeometry(QtCore.QRect(590, 340, 121, 21))
        self.label_12.setObjectName("label_12")
        self.creareNrMobil = QtWidgets.QLineEdit(self.tab)
        self.creareNrMobil.setGeometry(QtCore.QRect(710, 340, 281, 20))
        self.creareNrMobil.setObjectName("creareNrMobil")
        self.label_13 = QtWidgets.QLabel(self.tab)
        self.label_13.setGeometry(QtCore.QRect(590, 370, 91, 21))
        self.label_13.setObjectName("label_13")
        self.creareEmail = QtWidgets.QLineEdit(self.tab)
        self.creareEmail.setGeometry(QtCore.QRect(690, 370, 301, 20))
        self.creareEmail.setObjectName("creareEmail")
        self.label_14 = QtWidgets.QLabel(self.tab)
        self.label_14.setGeometry(QtCore.QRect(590, 400, 121, 21))
        self.label_14.setObjectName("label_14")
        self.creareNrCerere = QtWidgets.QLineEdit(self.tab)
        self.creareNrCerere.setGeometry(QtCore.QRect(710, 400, 281, 20))
        self.creareNrCerere.setObjectName("creareNrCerere")
        self.checkBox = QtWidgets.QCheckBox(self.tab)
        self.checkBox.setGeometry(QtCore.QRect(590, 430, 161, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab)
        self.checkBox_2.setGeometry(QtCore.QRect(760, 430, 141, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(910, 430, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_15 = QtWidgets.QLabel(self.tab_2)
        self.label_15.setGeometry(QtCore.QRect(0, 10, 181, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.tab_2)
        self.label_16.setGeometry(QtCore.QRect(0, 40, 91, 16))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.tab_2)
        self.label_17.setGeometry(QtCore.QRect(0, 70, 91, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(0, 100, 121, 16))
        self.label_18.setObjectName("label_18")
        self.resetareNumeUtilizator = QtWidgets.QLineEdit(self.tab_2)
        self.resetareNumeUtilizator.setGeometry(QtCore.QRect(180, 10, 241, 20))
        self.resetareNumeUtilizator.setObjectName("resetareNumeUtilizator")
        self.resetareNrTel = QtWidgets.QLineEdit(self.tab_2)
        self.resetareNrTel.setGeometry(QtCore.QRect(90, 40, 331, 20))
        self.resetareNrTel.setObjectName("resetareNrTel")
        self.resetareEmail = QtWidgets.QLineEdit(self.tab_2)
        self.resetareEmail.setGeometry(QtCore.QRect(100, 70, 321, 20))
        self.resetareEmail.setObjectName("resetareEmail")
        self.resetareNrCerere = QtWidgets.QLineEdit(self.tab_2)
        self.resetareNrCerere.setGeometry(QtCore.QRect(130, 100, 291, 20))
        self.resetareNrCerere.setObjectName("resetareNrCerere")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_3.setGeometry(QtCore.QRect(0, 130, 161, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_4.setGeometry(QtCore.QRect(170, 130, 141, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 130, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Creare/Resetare Cont", "Creare/Resetare Cont"))
        self.treeWidget.headerItem().setText(0, _translate("Creare/Resetare Cont", "Instante"))
        self.treeWidget.headerItem().setText(1, _translate("Creare/Resetare Cont", "Ministerul Justitiei"))
        self.label.setText(_translate("Creare/Resetare Cont", "*Prenume :"))
        self.label_2.setText(_translate("Creare/Resetare Cont", "*Nume :"))
        self.label_3.setText(_translate("Creare/Resetare Cont", "*Tot numele :"))
        self.label_4.setText(_translate("Creare/Resetare Cont", "Birou :"))
        self.label_5.setText(_translate("Creare/Resetare Cont", "Nr. tel :"))
        self.label_6.setText(_translate("Creare/Resetare Cont", "Judet :"))
        self.label_7.setText(_translate("Creare/Resetare Cont", "Oras :"))
        self.label_8.setText(_translate("Creare/Resetare Cont", "Strada :"))
        self.label_9.setText(_translate("Creare/Resetare Cont", "Functia :"))
        self.label_10.setText(_translate("Creare/Resetare Cont", "Departament :"))
        self.label_11.setText(_translate("Creare/Resetare Cont", "Insitutia :"))
        self.label_12.setText(_translate("Creare/Resetare Cont", "*Nr. mobil :"))
        self.creareNrMobil.setText(_translate("Creare/Resetare Cont", "+40"))
        self.label_13.setText(_translate("Creare/Resetare Cont", "*E-mail :"))
        self.label_14.setText(_translate("Creare/Resetare Cont", "*Nr. cerere :"))
        self.checkBox.setText(_translate("Creare/Resetare Cont", "Trimite E-mail"))
        self.checkBox_2.setText(_translate("Creare/Resetare Cont", "Trimite SMS"))
        self.pushButton.setText(_translate("Creare/Resetare Cont", "Creare"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Creare/Resetare Cont", "Creare Cont"))
        self.label_15.setText(_translate("Creare/Resetare Cont", "*Nume utilizator :"))
        self.label_16.setText(_translate("Creare/Resetare Cont", "*Nr. tel :"))
        self.label_17.setText(_translate("Creare/Resetare Cont", "*E-mail :"))
        self.label_18.setText(_translate("Creare/Resetare Cont", "*Nr. cerere :"))
        self.checkBox_3.setText(_translate("Creare/Resetare Cont", "Trimite E-mail"))
        self.checkBox_4.setText(_translate("Creare/Resetare Cont", "Trimite SMS"))
        self.pushButton_2.setText(_translate("Creare/Resetare Cont", "Resetare"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Creare/Resetare Cont", "Resetare Cont"))
        self.treeWidget.itemClicked.connect(self.on_treeWidget_item_clicked)
        self.tabWidget.currentChanged.connect(self.tab_changed)
        self.crearePrenume.textChanged.connect(self.updateTot)
        self.creareNume.textChanged.connect(self.updateTot)
        second_column_data = self.read_second_column_data()
        self.pushButton.clicked.connect(self.creareCont)
        self.pushButton_2.clicked.connect(self.resetareCont)
        #Populare TreeWidget cu valori din ListaInstante.txt si ListaMj.txt
        with open(os.path.join(get_executable_directory(), "ListaInstante.txt"), 'r', encoding='utf-8') as file:
            current_parent = None
            for line, second_data in zip(file.readlines(), second_column_data):
                line = line.strip()
                if line.startswith('-'):
                    subitem = QTreeWidgetItem([line.lstrip('-'), second_data])
                    current_parent.addChild(subitem)
                else:
                    item = QTreeWidgetItem([line, second_data])
                    self.treeWidget.addTopLevelItem(item)
                    current_parent = item
    #Populare TreeWidget cu valori din ListaInstante.txt si ListaMj.txt
    def read_second_column_data(self):
        data_list = []
        with open(os.path.join(get_executable_directory(), "ListaMJ.txt"), 'r', encoding='utf-8') as file:
            for line in file.readlines():
                line = line.strip()
                data_list.append(line)
        return data_list
    #Functie actualizare automata camp Tot numele
    def updateTot(self):
        self.creareTotNumele.setText(f"{self.crearePrenume.text()} {self.creareNume.text()}")
    def tab_changed(self, index):
        if self.tabWidget.tabText(index)=="Creare Cont":
            MainWindow.resize(1001, 501)
            self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1001, 501))
        else:
            MainWindow.resize(422, 200)
            self.tabWidget.setGeometry(QtCore.QRect(0, 0, 422, 200))
    #Functie sa verifice ce locatie ai selectat si sa defineaasca codu powershell pentru a adauga useru nou in locatia selectata
    def on_treeWidget_item_clicked(self, item, column):
        global locatie, subitem_text, column_name, item_text,powershell_code
        subitem_text = item.text(column)
        column_name = item.treeWidget().headerItem().text(column)
        parent_item = item.parent()
        if parent_item is not None:
            item_text = parent_item.text(column)
        else:
            item_text = ""  # sau puteți seta altceva pentru item_text în cazul rădăcinii
        if subitem_text and column_name!="" and item_text=="":
            locatie=f"{subitem_text}/{column_name}"
            print(locatie)
            powershell_code= f'''
                Add-Type -AssemblyName 'System.Web'
                import-module ActiveDirectory
                $new_rand_password = [System.Web.Security.Membership]::GeneratePassword(10, 3)
                Write-Output $new_rand_password
                New-ADUser `
                -AccountPassword (ConvertTo-SecureString -AsPlainText $new_rand_password -Force) `
                -City "{self.creareOras.text()}" `
                -Company "{self.creareInsitutia.text()}" `
                -Department "{self.creareDepartament.text()}" `
                -DisplayName "{self.creareTotNumele.text()}" `
                -EmailAddress "{self.crearePrenume.text()}.{self.creareNume.text()}@just.ro" `
                -Enabled $true `
                -GivenName "{self.crearePrenume.text()}" `
                -Name "{self.creareNume.text()}" `
                -OfficePhone {self.creareNrTel.text()} `
                -Office "{self.creareBirou.text()}" `
                -SamAccountName "{self.crearePrenume.text()}.{self.creareNume.text()}" `
                -State "{self.creareJudet.text()}" `
                -Surname "{self.creareNume.text()}" `
                -Title "{self.creareFunctia.text()}" `
                -StreetAddress "{self.creareStrada.text()}" `
                -HomePhone "{self.creareNrMobil.text()}" `
                -MobilePhone "{self.creareNrMobil.text()}" `
                -Path "OU=Utilizatori,OU={subitem_text},OU={column_name},DC=JUST,DC=RO"
                '''
        elif item_text and column_name and subitem_text !="":
            locatie=f"{subitem_text}/{item_text}/{column_name}"
            print(locatie)
            powershell_code= f'''
                Add-Type -AssemblyName 'System.Web'
                import-module ActiveDirectory
                $new_rand_password = [System.Web.Security.Membership]::GeneratePassword(10, 3)
                Write-Output $new_rand_password
                New-ADUser `
                -AccountPassword (ConvertTo-SecureString -AsPlainText $new_rand_password -Force) `
                -City "{self.creareOras.text()}" `
                -Company "{self.creareInsitutia.text()}" `
                -Department "{self.creareDepartament.text()}" `
                -DisplayName "{self.creareTotNumele.text()}" `
                -EmailAddress "{self.crearePrenume.text()}.{self.creareNume.text()}@just.ro" `
                -Enabled $true `
                -GivenName "{self.crearePrenume.text()}" `
                -Name "{self.creareNume.text()}" `
                -OfficePhone {self.creareNrTel.text()} `
                -Office "{self.creareBirou.text()}" `
                -SamAccountName "{self.crearePrenume.text()}.{self.creareNume.text()}" `
                -State "{self.creareJudet.text()}" `
                -Surname "{self.creareNume.text()}" `
                -Title "{self.creareFunctia.text()}" `
                -StreetAddress "{self.creareStrada.text()}" `
                -HomePhone "{self.creareNrMobil.text()}" `
                -MobilePhone "{self.creareNrMobil.text()}" `
                -Path "OU=Utilizatori,OU={subitem_text},OU={item_text},OU={column_name},DC=JUST,DC=RO"
                '''
    #Functia care creeaza cont , trimite datele prin email sau sms si salveaza logurile creeari de cont
    def creareCont(self):
        global locatie, subitem_text,column_name,item_text,powershell_code
        if locatie=="Users":
            powershell_code2= f'''
                Add-Type -AssemblyName 'System.Web'
                import-module ActiveDirectory
                $new_rand_password = [System.Web.Security.Membership]::GeneratePassword(10, 3)
                Write-Output $new_rand_password
                New-ADUser `
                -AccountPassword (ConvertTo-SecureString -AsPlainText $new_rand_password -Force) `
                -City "{self.creareOras.text()}" `
                -Company "{self.creareInsitutia.text()}" `
                -Department "{self.creareDepartament.text()}" `
                -DisplayName "{self.creareTotNumele.text()}" `
                -EmailAddress "{self.crearePrenume.text()}.{self.creareNume.text()}@just.ro" `
                -Enabled $true `
                -GivenName "{self.crearePrenume.text()}" `
                -Name "{self.creareNume.text()}" `
                -OfficePhone {self.creareNrTel.text()} `
                -Office "{self.creareNrTel.text()}" `
                -SamAccountName "{self.crearePrenume.text()}.{self.creareNume.text()}" `
                -State "{self.creareJudet.text()}" `
                -Surname "{self.creareNume.text()}" `
                -Title "{self.creareFunctia.text()}" `
                -StreetAddress "{self.creareStrada.text()}" `
                -HomePhone "{self.creareNrMobil.text()}" `
                -MobilePhone "{self.creareNrMobil.text()}" `
                -Path "CN={locatie},DC=JUST,DC=RO"
                '''
        else:
            powershell_code2 =powershell_code
        result = subprocess.run(['powershell', '-Command', powershell_code2], capture_output=True, text=True)
        new_rand_password = result.stdout.strip()
        current_time = datetime.datetime.now().time()
        current_datetime = datetime.datetime.now()
        data=f"{current_datetime.day}.{current_datetime.month}.{current_datetime.year} ora : {current_time.hour}:{current_time.minute}:{current_time.second}:{current_time.microsecond}"
        if self.checkBox.isChecked() == True :
            sender = ""
            recipient = self.creareEmail.text()
            subject = f"Creare cont nou : {self.crearePrenume.text()}.{self.creareNume.text()}@just.ro"
            content = f"E-mail : {self.crearePrenume.text()}.{self.creareNume.text()}@just.ro\
                    \nNr. cerere : {self.creareNrCerere.text()}\
                    \nParola : {new_rand_password}"
            message = MIMEText(content)
            message["Subject"] = subject
            message["From"] = sender
            message["To"] = recipient
            smtp_server = ""
            smtp_port = 
            smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
            smtp_connection.sendmail(sender, recipient, message.as_string())
            smtp_connection.quit()
            with open(fr"{get_executable_directory()}\emailLogs.txt", 'a') as file:
                file.write(f"\nE-mail : Contul {self.crearePrenume.text()}.{self.creareNume.text()}@just.ro , a fost creat la : {data} , PID:{os.getpid()} , destinatar : {self.creareEmail.text()} , nr. cerere : {self.creareNrCerere.text()}")
            locatie="Users"
        if self.checkBox_2.isChecked() == True :
            exe_path = os.path.join(get_executable_directory(), "sendsms_1.exe")
            smsmsg= f"Contul : {self.crearePrenume.text()}.{self.creareNume.text()}@just.ro a fost creat , nr. cerere : {self.creareNrCerere.text()} , parola : {new_rand_password}"
            command = [exe_path, "-m", smsmsg, "-nr", self.creareNrMobil.text()]
            result = subprocess.run(command, capture_output=True, text=True, shell=True)
            with open(fr"{get_executable_directory()}\smsLogs.txt", 'a') as file:
                file.write(f"\nSMS : Contul {self.crearePrenume.text()}.{self.creareNume.text()}@just.ro , a fost creat la : {data} , PID:{os.getpid()} , destinatar : {self.creareNrMobil.text()} , nr. cerere : {self.creareNrCerere.text()}")
    #Functia care reseteaza parola  contului , trimite datele prin email sau sms si salveaza logurile resetari parolei de cont
    def resetareCont(self):
        powershell_code = f'''
        Add-Type -AssemblyName 'System.Web'
        import-module ActiveDirectory
        $new_rand_password = [System.Web.Security.Membership]::GeneratePassword(10, 3)
        Write-Output $new_rand_password
        $new_rand_password2 = ConvertTo-SecureString $new_rand_password -AsPlainText -Force
        Enable-ADAccount -Identity {self.resetareNumeUtilizator.text()}
        Set-ADAccountPassword {self.resetareNumeUtilizator.text()} -Reset -NewPassword $new_rand_password2
        '''
        result = subprocess.run(['powershell', '-Command', powershell_code], capture_output=True, text=True)
        new_rand_password = result.stdout.strip()
        current_time = datetime.datetime.now().time()
        current_datetime = datetime.datetime.now()
        data=f"{current_datetime.day}.{current_datetime.month}.{current_datetime.year} ora : {current_time.hour}:{current_time.minute}:{current_time.second}:{current_time.microsecond}"
        if self.checkBox_3.isChecked() == True :
            sender = "alexandru.trif@just.ro"
            recipient = self.resetareEmail.text()
            subject = f"Resetare parola cont : {self.resetareNumeUtilizator.text()}"
            content = f"Nume utilizator : {self.resetareNumeUtilizator.text()}\
                        \nParola noua : {new_rand_password}\
                        \nNr. cerere : {self.resetareNrCerere.text()}"
            message = MIMEText(content)
            message["Subject"] = subject
            message["From"] = sender
            message["To"] = recipient
            smtp_server = "10.1.0.52"
            smtp_port = 25
            smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
            smtp_connection.sendmail(sender, recipient, message.as_string())
            smtp_connection.quit()
            with open(fr"{get_executable_directory()}\emailLogs.txt", 'a') as file:
                file.write(f"\nE-mail : Parola noua a contului {self.resetareNumeUtilizator.text()} este : {new_rand_password} , a fost resetata la : {data} , PID:{os.getpid()} , destinatar : {self.resetareEmail.text()} , nr. cerere : {self.resetareNrCerere.text()}")
        if self.checkBox_4.isChecked() == True :
            exe_path = os.path.join(get_executable_directory(), "sendsms_1.exe")
            smsmsg=f"Resetare parola cont : {self.resetareNumeUtilizator.text()} , nume utilizator : {self.resetareNumeUtilizator.text()} , parola noua : {new_rand_password} , nr. cerere : {self.resetareNrCerere.text()}"
            command = [exe_path, "-m", smsmsg, "-nr", self.resetareNrTel.text()]
            result = subprocess.run(command, capture_output=True, text=True, shell=True)
            with open(fr"{get_executable_directory()}\smsLogs.txt", 'a') as file:
                file.write(f"\nSMS : Parola noua a contului {self.resetareNumeUtilizator.text()} este : {new_rand_password}, a fost resetata la : {data} , PID:{os.getpid()} , destinatar : {self.resetareNrTel.text()} , nr. cerere : {self.resetareNrCerere.text()}")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
