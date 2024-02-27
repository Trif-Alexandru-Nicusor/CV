from PyQt5 import QtCore, QtGui, QtWidgets
import pyodbc,csv,sys,configparser,threading,datetime,time,re,paramiko,os
config = configparser.ConfigParser()
global startstop
startstop=0
if not os.path.exists(r'C:\ProgramData\Actualizare Experti'):
    os.makedirs(r'C:\ProgramData\Actualizare Experti')
    config['Date'] = {
        'IpServer': '',
        'Nume baza de date': '',
        'Username logare': '',
        'Parola logare': '',
        'Secventa SQL': '',
        'Ora actualizare': '',
        'IP Server Wordpress': '',
        'Username logare wp': '',
        'Parola logare wp': '',
        'Path': '',
    }
    with open(r'C:\ProgramData\Actualizare Experti\config.ini', 'w' , encoding = 'utf-8') as configfile:
        config.write(configfile)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Actualizare date site")
        MainWindow.resize(402, 429)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 50, 201, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 80, 181, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 120, 141, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 160, 151, 31))
        self.label_5.setObjectName("label_5")
        self.ipServer = QtWidgets.QLineEdit(self.centralwidget)
        self.ipServer.setGeometry(QtCore.QRect(110, 10, 291, 20))
        self.ipServer.setObjectName("ipServer")
        self.numeBaza = QtWidgets.QLineEdit(self.centralwidget)
        self.numeBaza.setGeometry(QtCore.QRect(200, 50, 201, 20))
        self.numeBaza.setText("")
        self.numeBaza.setObjectName("numeBaza")
        self.userLogare = QtWidgets.QLineEdit(self.centralwidget)
        self.userLogare.setGeometry(QtCore.QRect(180, 90, 221, 20))
        self.userLogare.setObjectName("userLogare")
        self.parolaLogare = QtWidgets.QLineEdit(self.centralwidget)
        self.parolaLogare.setGeometry(QtCore.QRect(150, 130, 251, 20))
        self.parolaLogare.setObjectName("parolaLogare")
        self.parolaLogare.setEchoMode(QtWidgets.QLineEdit.Password)
        self.secventaSQL = QtWidgets.QLineEdit(self.centralwidget)
        self.secventaSQL.setGeometry(QtCore.QRect(150, 170, 251, 21))
        self.secventaSQL.setText("")
        self.secventaSQL.setObjectName("secventaSQL")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(0, 210, 161, 16))
        self.label_6.setObjectName("label_6")
        self.ora = QtWidgets.QTimeEdit(self.centralwidget)
        self.ora.setGeometry(QtCore.QRect(170, 210, 121, 22))
        self.ora.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.ora.setObjectName("ora")
        self.ora.setDisplayFormat("HH:mm")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(0, 400, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 400, 51, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 240, 211, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(0, 280, 181, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(0, 320, 141, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(0, 370, 61, 16))
        self.label_10.setObjectName("label_10")
        self.ipServerWordpress = QtWidgets.QLineEdit(self.centralwidget)
        self.ipServerWordpress.setGeometry(QtCore.QRect(220, 250, 181, 20))
        self.ipServerWordpress.setObjectName("ipServerWordpress")
        self.userLogareWp = QtWidgets.QLineEdit(self.centralwidget)
        self.userLogareWp.setGeometry(QtCore.QRect(180, 290, 221, 20))
        self.userLogareWp.setObjectName("userLogareWp")
        self.parolaLogareWP = QtWidgets.QLineEdit(self.centralwidget)
        self.parolaLogareWP.setGeometry(QtCore.QRect(150, 330, 221, 20))
        self.parolaLogareWP.setObjectName("parolaLogareWP")
        self.parolaLogareWP.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pathWP = QtWidgets.QLineEdit(self.centralwidget)
        self.pathWP.setGeometry(QtCore.QRect(60, 370, 221, 20))
        self.pathWP.setObjectName("pathWP")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        config.read(r'C:\ProgramData\Actualizare Experti\config.ini',encoding = 'utf-8')
        self.ipServer.setText(config.get('Date', 'IpServer'))
        self.numeBaza.setText(config.get('Date', 'Nume baza de date'))
        self.userLogare.setText(config.get('Date', 'Username logare'))
        self.parolaLogare.setText(config.get('Date', 'Parola logare'))
        self.secventaSQL.setText(config.get('Date', 'Secventa SQL'))
        self.ora.setTime(QtCore.QTime.fromString(config.get('Date', 'Ora actualizare'), "HH:mm"))
        self.ipServerWordpress.setText(config.get('Date','IP Server Wordpress'))
        self.userLogareWp.setText(config.get('Date','Username logare wp'))
        self.parolaLogareWP.setText(config.get('Date','Parola logare wp'))
        self.pathWP.setText(config.get('Date','Path'))
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Actualizare date site", "Actualizare date site"))
        self.label.setText(_translate("Actualizare date site", "IP Server :"))
        self.label_2.setText(_translate("Actualizare date site", "Nume baza de date :"))
        self.label_3.setText(_translate("Actualizare date site", "Username logare :"))
        self.label_4.setText(_translate("Actualizare date site", "Parola logare :"))
        self.label_5.setText(_translate("Actualizare date site", "Secventa SQL :"))
        self.label_6.setText(_translate("Actualizare date site", "Ora actualizare :"))
        self.pushButton.setText(_translate("Actualizare date site", "Salvare Date"))
        self.pushButton_2.setText(_translate("Actualizare date site", "Start"))
        self.label_7.setText(_translate("Actualizare date site", "IP Server Wordpress :"))
        self.label_8.setText(_translate("Actualizare date site", "Username logare :"))
        self.label_9.setText(_translate("Actualizare date site", "Parola logare :"))
        self.label_10.setText(_translate("Actualizare date site", "Path :"))
        self.pushButton.clicked.connect(self.salvaredate)
        self.pushButton_2.clicked.connect(self.actualizare)
    def actualizare(self):
        update_thread = threading.Thread(target=self.thread)
        update_thread.daemon = True
        update_thread.start()
    def thread(self):
        global startstop
        if startstop==0:
            startstop=1
            self.pushButton_2.setText("Stop")
        else:
            startstop=0
            self.pushButton_2.setText("Start")
        server = self.ipServer.text()
        database = self.numeBaza.text()
        username = self.userLogare.text()
        password = self.parolaLogare.text()
        sqlquery=self.secventaSQL.text()
        connection_string = f"DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password};charset=utf8"
        while startstop==1:
            current_time = datetime.datetime.now().time()
            formatted_time = current_time.strftime("%H:%M:%S")
            if formatted_time==self.ora.text()+":00":
                conn = pyodbc.connect(connection_string)
                cursor = conn.cursor()
                cursor.execute(sqlquery)
                results = cursor.fetchall()
                with open("tabelExperti.csv", 'w', newline='', encoding='UTF-8') as csv_file:
                    csv_writer = csv.writer(csv_file)
                    column_names = [column[0] for column in cursor.description]
                    csv_writer.writerow(column_names)
                    for row in results:
                        cleaned_row = [re.sub(r'\s+', ' ', str(cell)).strip().replace('ş', 'ș').replace('ţ', 'ț') for cell in row]
                        csv_writer.writerow(cleaned_row)
                conn.close()
                transport = paramiko.Transport((self.ipServerWordpress.text(), 22))
                transport.connect(username=self.userLogareWp.text(), password=self.parolaLogareWP.text())
                print("M-am conectat !")
                sftp = paramiko.SFTPClient.from_transport(transport)
                sftp.put("tabelExperti.csv", self.pathWP.text())
                print("Fisier trimis !")
                sftp.close()
                transport.close()
                print("M-am deconectat !")
                time.sleep(5)
    def salvaredate(self):
        config['Date'] = {
            'IpServer': self.ipServer.text(),
            'Nume baza de date': self.numeBaza.text() ,
            'Username logare': self.userLogare.text(),
            'Parola logare': self.parolaLogare.text(),
            'Secventa SQL': self.secventaSQL.text(),
            'Ora actualizare': self.ora.text(),
            'IP Server Wordpress': self.ipServerWordpress.text(),
            'Username logare wp': self.userLogareWp.text(),
            'Parola logare wp': self.parolaLogareWP.text(),
            'Path': self.pathWP.text(),
        }
        with open(r'C:\ProgramData\Actualizare Experti\config.ini', 'w' , encoding = 'utf-8') as configfile:
            config.write(configfile)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
