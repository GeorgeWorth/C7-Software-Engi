# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dashboard_Screen.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1002, 797)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setMinimumSize(QtCore.QSize(1002, 797))
        self.centralwidget.setMaximumSize(QtCore.QSize(1002, 797))
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(500, 0, 531, 801))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 501, 401))
        self.frame_4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.DashBoard_lbl_2 = QtWidgets.QLabel(self.frame_4)
        self.DashBoard_lbl_2.setGeometry(QtCore.QRect(10, 10, 181, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.DashBoard_lbl_2.setFont(font)
        self.DashBoard_lbl_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.DashBoard_lbl_2.setObjectName("DashBoard_lbl_2")
        self.DashBoard_lbl_4 = QtWidgets.QLabel(self.frame_4)
        self.DashBoard_lbl_4.setGeometry(QtCore.QRect(130, 260, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.DashBoard_lbl_4.setFont(font)
        self.DashBoard_lbl_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.DashBoard_lbl_4.setObjectName("DashBoard_lbl_4")
        self.DashBoard_lbl_6 = QtWidgets.QLabel(self.frame_4)
        self.DashBoard_lbl_6.setGeometry(QtCore.QRect(200, 360, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.DashBoard_lbl_6.setFont(font)
        self.DashBoard_lbl_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.DashBoard_lbl_6.setObjectName("DashBoard_lbl_6")
        self.ViewDownloadTMDb_btn = QtWidgets.QPushButton(self.frame_2)
        self.ViewDownloadTMDb_btn.setGeometry(QtCore.QRect(140, 550, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ViewDownloadTMDb_btn.setFont(font)
        self.ViewDownloadTMDb_btn.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.ViewDownloadTMDb_btn.setObjectName("ViewDownloadTMDb_btn")
        self.SearchTMDb_btn = QtWidgets.QPushButton(self.frame_2)
        self.SearchTMDb_btn.setGeometry(QtCore.QRect(140, 450, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.SearchTMDb_btn.setFont(font)
        self.SearchTMDb_btn.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.SearchTMDb_btn.setObjectName("SearchTMDb_btn")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 501, 401))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.DashBoard_lbl = QtWidgets.QLabel(self.frame_3)
        self.DashBoard_lbl.setGeometry(QtCore.QRect(290, 10, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.DashBoard_lbl.setFont(font)
        self.DashBoard_lbl.setStyleSheet("")
        self.DashBoard_lbl.setObjectName("DashBoard_lbl")
        self.DashBoard_lbl_3 = QtWidgets.QLabel(self.frame_3)
        self.DashBoard_lbl_3.setGeometry(QtCore.QRect(120, 270, 281, 61))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.DashBoard_lbl_3.setFont(font)
        self.DashBoard_lbl_3.setStyleSheet("")
        self.DashBoard_lbl_3.setObjectName("DashBoard_lbl_3")
        self.DashBoard_lbl_5 = QtWidgets.QLabel(self.frame_3)
        self.DashBoard_lbl_5.setGeometry(QtCore.QRect(200, 360, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.DashBoard_lbl_5.setFont(font)
        self.DashBoard_lbl_5.setStyleSheet("")
        self.DashBoard_lbl_5.setObjectName("DashBoard_lbl_5")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 400, 501, 401))
        self.frame.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.SearchOMDb_btn = QtWidgets.QPushButton(self.frame)
        self.SearchOMDb_btn.setGeometry(QtCore.QRect(140, 50, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.SearchOMDb_btn.setFont(font)
        self.SearchOMDb_btn.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.SearchOMDb_btn.setObjectName("SearchOMDb_btn")
        self.ViewDownloadOMDb_btn = QtWidgets.QPushButton(self.frame)
        self.ViewDownloadOMDb_btn.setGeometry(QtCore.QRect(140, 150, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.ViewDownloadOMDb_btn.setFont(font)
        self.ViewDownloadOMDb_btn.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ViewDownloadOMDb_btn.setObjectName("ViewDownloadOMDb_btn")
        self.WishList_btn = QtWidgets.QPushButton(self.centralwidget)
        self.WishList_btn.setGeometry(QtCore.QRect(390, 700, 211, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.WishList_btn.setFont(font)
        self.WishList_btn.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.WishList_btn.setObjectName("WishList_btn")
        self.Random_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Random_btn.setGeometry(QtCore.QRect(370, 600, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Random_btn.setFont(font)
        self.Random_btn.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.Random_btn.setObjectName("Random_btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DashBoard_lbl_2.setText(_translate("MainWindow", "Application"))
        self.DashBoard_lbl_4.setText(_translate("MainWindow", "The Movie db"))
        self.DashBoard_lbl_6.setText(_translate("MainWindow", "Options"))
        self.ViewDownloadTMDb_btn.setText(_translate("MainWindow", "View Downloaded"))
        self.SearchTMDb_btn.setText(_translate("MainWindow", "Search"))
        self.DashBoard_lbl.setText(_translate("MainWindow", "ACME Movie"))
        self.DashBoard_lbl_3.setText(_translate("MainWindow", "OMDb Database"))
        self.DashBoard_lbl_5.setText(_translate("MainWindow", "Options"))
        self.SearchOMDb_btn.setText(_translate("MainWindow", "Search"))
        self.ViewDownloadOMDb_btn.setText(_translate("MainWindow", "View Downloaded"))
        self.WishList_btn.setText(_translate("MainWindow", "Wish List"))
        self.Random_btn.setText(_translate("MainWindow", "Randomly Select a Movie/Tv show"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

