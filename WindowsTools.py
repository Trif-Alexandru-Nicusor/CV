from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTabBar
import subprocess,sys,requests

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(280 , 125)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 281, 421))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.radioButton = QtWidgets.QRadioButton(self.tab)
        self.radioButton.setGeometry(QtCore.QRect(0, 10, 121, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_2.setGeometry(QtCore.QRect(0, 40, 141, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(0, 70, 151, 23))
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(160, 70, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.checkBox = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox.setGeometry(QtCore.QRect(0, 0, 161, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_2.setGeometry(QtCore.QRect(0, 30, 161, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_3.setGeometry(QtCore.QRect(0, 60, 161, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_4.setGeometry(QtCore.QRect(0, 90, 161, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_5.setGeometry(QtCore.QRect(0, 120, 161, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_6.setGeometry(QtCore.QRect(0, 150, 161, 17))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_7 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_7.setGeometry(QtCore.QRect(0, 180, 171, 17))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_8.setGeometry(QtCore.QRect(0, 210, 171, 17))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_9.setGeometry(QtCore.QRect(0, 240, 171, 17))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_10.setGeometry(QtCore.QRect(0, 270, 171, 17))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_11.setGeometry(QtCore.QRect(0, 300, 171, 17))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_12.setGeometry(QtCore.QRect(0, 330, 171, 17))
        self.checkBox_12.setObjectName("checkBox_12")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 360, 101, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.progressBar_2 = QtWidgets.QProgressBar(self.tab_2)
        self.progressBar_2.setGeometry(QtCore.QRect(110, 360, 118, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName("progressBar_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton.setText(_translate("MainWindow", "Windows Pro"))
        self.radioButton_2.setText(_translate("MainWindow", "Windows Home"))
        self.pushButton.setText(_translate("MainWindow", "Activate Windows"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Windows Activator"))
        self.checkBox.setText(_translate("MainWindow", "Tools For Taskbar"))
        self.checkBox_2.setText(_translate("MainWindow", "HWMonitor"))
        self.checkBox_3.setText(_translate("MainWindow", "Gaming Things"))
        self.checkBox_4.setText(_translate("MainWindow", "Windows 10"))
        self.checkBox_5.setText(_translate("MainWindow", "Windows 11"))
        self.checkBox_6.setText(_translate("MainWindow", "Rufus"))
        self.checkBox_7.setText(_translate("MainWindow", "NVIDIA Experience"))
        self.checkBox_8.setText(_translate("MainWindow", "AnyDesk"))
        self.checkBox_9.setText(_translate("MainWindow", "Chrome"))
        self.checkBox_10.setText(_translate("MainWindow", "WinRar"))
        self.checkBox_11.setText(_translate("MainWindow", "uTorrent"))
        self.checkBox_12.setText(_translate("MainWindow", "Coding Things"))
        self.pushButton_2.setText(_translate("MainWindow", "Download"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Downloads"))
        self.tabWidget.currentChanged.connect(self.tab_changed)
        self.pushButton.clicked.connect(self.activatewindows)
        self.pushButton_2.clicked.connect(self.downloads)
    def tab_changed(self, index):
        if self.tabWidget.tabText(index)=="Windows Activator":
            MainWindow.resize(280 , 125)
        else:
            MainWindow.resize(280 , 410)
    
    def activatewindows(self):
        if self.radioButton.isChecked()==1:
            self.progressBar.setProperty("value", 50)
            subprocess.Popen(['cmd', '/c', 'slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX & slmgr /skms kms8.msguides.com & slmgr /ato'])
            self.progressBar.setProperty("value", 100)
        elif self.radioButton_2.isChecked()==1:
            self.progressBar.setProperty("value", 50)
            subprocess.Popen(['cmd', '/c', 'slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99 & slmgr /skms kms8.msguides.com & slmgr /ato'])
            self.progressBar.setProperty("value", 100)
        self.progressBar.setProperty("value", 0)

    def downloads(self):
        if self.checkBox.isChecked()==1:
            self.progressBar_2.setProperty("value", 8)
            response = requests.get('https://github.com/TranslucentTB/TranslucentTB/releases/download/2022.1/TranslucentTB-portable-x64.zip')
            with open('TranslucentTB-portable-x64.zip', 'wb') as f:
                f.write(response.content)
            response = requests.get('https://github.com/torchgm/RoundedTB/releases/download/R3.1/RoundedTB_R3.1.zip')
            with open('RoundedTB_R3.1.zip', 'wb') as f:
                f.write(response.content)
        if self.checkBox_2.isChecked()==1:
            self.progressBar_2.setProperty("value", 16)
            response = requests.get('https://download.cpuid.com/hwmonitor/hwmonitor_1.49.zip')
            with open('hwmonitor_1.49.zip', 'wb') as f:
                f.write(response.content)
        if self.checkBox_3.isChecked()==1:
            self.progressBar_2.setProperty("value", 24)
            response = requests.get('https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe')
            with open('SteamSetup.exe', 'wb') as f:
                f.write(response.content)
            response = requests.get('https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download/EpicGamesLauncherInstaller.msi')
            with open('EpicGamesLauncherInstaller.msi', 'wb') as f:
                f.write(response.content)
            response = requests.get('https://lol.secure.dyn.riotcdn.net/channels/public/x/installer/current/live.eune.exe')
            with open('Install League of Legends eune.exe', 'wb') as f:
                f.write(response.content)
        if self.checkBox_4.isChecked()==1:
            self.progressBar_2.setProperty("value", 32)
            response = requests.get('https://download.microsoft.com/download/9/e/a/9eac306f-d134-4609-9c58-35d1638c2363/MediaCreationTool22H2.exe')
            with open('MediaCreationTool22H2.exe', 'wb') as f:
                f.write(response.content)
        if self.checkBox_5.isChecked()==1:
            self.progressBar_2.setProperty("value", 40)
            response = requests.get('https://software-static.download.prss.microsoft.com/dbazure/988969d5-f34g-4e03-ac9d-1f9786c66749/mediacreationtool.exe')
            with open('mediacreationtool.exe', 'wb') as f:
                f.write(response.content)
        if self.checkBox_6.isChecked()==1:
            self.progressBar_2.setProperty("value", 48)
            response = requests.get('https://github.com/pbatard/rufus/releases/download/v3.21/rufus-3.21p.exe')
            with open('rufus-3.21p.exe', 'wb') as f:
                f.write(response.content)
        if self.checkBox_7.isChecked()==1:
            self.progressBar_2.setProperty("value", 56)
            response = requests.get('https://uk.download.nvidia.com/GFE/GFEClient/3.27.0.112/GeForce_Experience_v3.27.0.112.exe')
            with open('GeForce_Experience_v3.27.0.112.exe', 'wb') as f:
                f.write(response.content)
        if self.checkBox_8.isChecked()==1:
            self.progressBar_2.setProperty("value", 64)
            response = requests.get('https://download.anydesk.com/AnyDesk.exe')
            with open('AnyDesk.exe', 'wb') as f:
                f.write(response.content)
        if self.checkBox_9.isChecked()==1:
            self.progressBar_2.setProperty("value", 72)
            response = requests.get('https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B4BF652DD-5590-90C1-2239-17E0B9C81B5B%7D%26lang%3Den%26browser%3D4%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe')
            with open('ChromeSetup.exe', 'wb') as f:
                f.write(response.content)
        if self.checkBox_10.isChecked()==1:
            self.progressBar_2.setProperty("value", 80)
            response = requests.get('https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-620.exe')
            with open('winrar-x64-620.exe', 'wb') as f:
                f.write(response.content)
        if self.checkBox_11.isChecked()==1:
            self.progressBar_2.setProperty("value", 88)
            response = requests.get('https://download-hr.utorrent.com/track/stable/endpoint/utorrent/os/windows')
            with open('utorrent_installer.exe', 'wb') as f:
                f.write(response.content)
        if self.checkBox_12.isChecked()==1:
            self.progressBar_2.setProperty("value", 96)
            response = requests.get('https://az764295.vo.msecnd.net/stable/441438abd1ac652551dbe4d408dfcec8a499b8bf/VSCodeUserSetup-x64-1.75.1.exe')
            with open('VSCodeUserSetup-x64-1.75.1.exe', 'wb') as f:
                f.write(response.content)
            response = requests.get('https://c2rsetup.officeapps.live.com/c2r/downloadVS.aspx?sku=community&channel=Release&version=VS2022&source=VSLandingPage&includeRecommended=true&cid=2030:e09f6514-59d2-4018-af6c-d63f55360f74')
            with open('VisualStudioSetup.exe', 'wb') as f:
                f.write(response.content)
            response = requests.get('https://www.python.org/ftp/python/3.11.2/python-3.11.2-amd64.exe')
            with open('python-3.11.2-amd64.exe', 'wb') as f:
                f.write(response.content)
        self.progressBar_2.setProperty("value", 100)
        self.progressBar_2.setProperty("value", 0)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
