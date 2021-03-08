# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Tools\manga_tool\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from pocket import find_image_pocket
from comicDays import find_image_comic_days
import time

note = """Note: 
* If this app is not responding after click "Get Image!", this app is still working in process. 
You can check download process in the Save Location Folder.
* Made by Mai Heaven
"""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(650, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.submitbtn = QtWidgets.QPushButton(self.centralwidget)
        self.submitbtn.setGeometry(QtCore.QRect(510, 60, 93, 28))
        self.submitbtn.setObjectName("submitbtn")
        self.submitbtn.clicked.connect(self.getImage)
        self.browsebtn = QtWidgets.QPushButton(self.centralwidget)
        self.browsebtn.setGeometry(QtCore.QRect(40, 120, 180, 28))
        self.browsebtn.setObjectName("browserbtn")
        self.browsebtn.clicked.connect(self.browserFolder)
        self.dirFilelb = QtWidgets.QLabel(self.centralwidget)
        self.dirFilelb.setGeometry(QtCore.QRect(240, 120, 340, 28))
        self.dirFilelb.setObjectName("dirFilelb")
        self.urltxt = QtWidgets.QTextEdit(self.centralwidget)
        self.urltxt.setGeometry(QtCore.QRect(40, 60, 441, 40))
        self.urltxt.setObjectName("urltxt")
        self.urltxt.setPlaceholderText("Paste link here")
        self.quitbtn = QtWidgets.QPushButton(self.centralwidget)
        self.quitbtn.setGeometry(QtCore.QRect(510, 200, 93, 28))
        self.quitbtn.setObjectName("quitbtn")
        self.quitbtn.clicked.connect(self.close)
        self.statuslb = QtWidgets.QLabel(self.centralwidget)
        self.statuslb.setGeometry(QtCore.QRect(40, 200, 441, 21))
        self.statuslb.setObjectName("statuslb")
        self.status = QtWidgets.QLabel(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(100, 200, 441, 21))
        self.status.setObjectName("status")
        self.setColor(self.status, "green")
        self.note = QtWidgets.QLabel(self.centralwidget)
        self.note.setGeometry(QtCore.QRect(40, 260, 550, 64))
        self.note.setObjectName("note")
        self.note.setStyleSheet("background-color: white")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Funny App"))
        MainWindow.setWindowIcon(QtGui.QIcon('logo.ico'))
        self.submitbtn.setText(_translate("MainWindow", "Get Image!"))
        self.quitbtn.setText(_translate("MainWindow", "Quit"))
        self.statuslb.setText(_translate("MainWindow", "Status: "))
        self.status.setText(_translate("MainWindow", "Ready"))
        self.browsebtn.setText(_translate("MainWindow", "Choose a save location"))
        self.note.setText(_translate("MainWindow", note))

    def getImage(self):
        dirPath = self.dirFilelb.text()
        if (not dirPath):
            self.status.setText("Choose a save location before")
            self.setColor(self.status, "red")
            return False
        self.submitbtn.setEnabled(False);
        self.status.setText("Waiting")
        self.setColor(self.status, "yellow")
        url = self.urltxt.toPlainText()
        if self.checkLink():
            self.status.setText("Done!")
            self.setColor(self.status, "green")
        else:
            self.status.setText("Error, check the link or the internet")
            self.setColor(self.status, "red")
        self.submitbtn.setEnabled(True);

    def close(self):
        MainWindow.close()

    def browserFolder(self):
        data_path = QtWidgets.QFileDialog.getExistingDirectoryUrl(None, 'Choose a save location')
        self.dirFilelb.setText(data_path.url()[8:])

    def setColor(self, label, color):
        pal = label.palette()
        pal.setColor(QtGui.QPalette.WindowText, QtGui.QColor(color))
        label.setPalette(pal)

    def checkLink(self):
        url = self.urltxt.toPlainText()
        dirPath = self.dirFilelb.text()
        if "comic-days" in url:
            return find_image_comic_days(url, dirPath)
        else:
            return find_image_pocket(url,dirPath)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

