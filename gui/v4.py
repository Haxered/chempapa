# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'v4.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_homeWindow(object):
    def setupUi(self, homeWindow):
        homeWindow.setObjectName("homeWindow")
        homeWindow.setEnabled(True)
        homeWindow.resize(1000, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(homeWindow.sizePolicy().hasHeightForWidth())
        homeWindow.setSizePolicy(sizePolicy)
        homeWindow.setMinimumSize(QtCore.QSize(1000, 650))
        homeWindow.setMaximumSize(QtCore.QSize(1000, 650))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/sukya/.designer/backup/media/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        homeWindow.setWindowIcon(icon)
        homeWindow.setWindowOpacity(1.0)
        homeWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(homeWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.homeFrame = QtWidgets.QFrame(self.centralwidget)
        self.homeFrame.setGeometry(QtCore.QRect(0, 0, 1000, 650))
        self.homeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.homeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.homeFrame.setObjectName("homeFrame")
        self.stoichiometry = QtWidgets.QPushButton(self.homeFrame)
        self.stoichiometry.setGeometry(QtCore.QRect(80, 145, 250, 70))
        self.stoichiometry.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #3c20cd, stop:1#160c4e);\n"
"border-radius:17px;\n"
"border:1px solid #1f2f47;\n"
"display:inline-block;\n"
"cursor:pointer;\n"
"color:#ffffff;\n"
"font-family:Arial;\n"
"font-size:15px;\n"
"padding:6px 13px;\n"
"text-decoration:none;\n"
"text-shadow:0px 1px 0px #263666;")
        self.stoichiometry.setObjectName("stoichiometry")
        self.predictor = QtWidgets.QPushButton(self.homeFrame)
        self.predictor.setGeometry(QtCore.QRect(80, 235, 250, 70))
        self.predictor.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #3c20cd, stop:1#160c4e);\n"
"border-radius:17px;\n"
"border:1px solid #1f2f47;\n"
"display:inline-block;\n"
"cursor:pointer;\n"
"color:#ffffff;\n"
"font-family:Arial;\n"
"font-size:15px;\n"
"padding:6px 13px;\n"
"text-decoration:none;\n"
"text-shadow:0px 1px 0px #263666;")
        self.predictor.setObjectName("predictor")
        self.b4 = QtWidgets.QPushButton(self.homeFrame)
        self.b4.setGeometry(QtCore.QRect(80, 415, 250, 70))
        self.b4.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #3c20cd, stop:1#160c4e);\n"
"border-radius:17px;\n"
"border:1px solid #1f2f47;\n"
"display:inline-block;\n"
"cursor:pointer;\n"
"color:#ffffff;\n"
"font-family:Arial;\n"
"font-size:15px;\n"
"padding:6px 13px;\n"
"text-decoration:none;\n"
"text-shadow:0px 1px 0px #263666;")
        self.b4.setObjectName("b4")
        self.bg = QtWidgets.QLabel(self.homeFrame)
        self.bg.setGeometry(QtCore.QRect(0, 0, 1000, 650))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bg.sizePolicy().hasHeightForWidth())
        self.bg.setSizePolicy(sizePolicy)
        self.bg.setText("")
        self.bg.setPixmap(QtGui.QPixmap("C:/Users/sukya/.designer/backup/media/BG.jpg"))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")
        self.b3 = QtWidgets.QPushButton(self.homeFrame)
        self.b3.setGeometry(QtCore.QRect(80, 325, 250, 70))
        self.b3.setStyleSheet("background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #3c20cd, stop:1#160c4e);\n"
"border-radius:17px;\n"
"border:1px solid #1f2f47;\n"
"display:inline-block;\n"
"cursor:pointer;\n"
"color:#ffffff;\n"
"font-family:Arial;\n"
"font-size:15px;\n"
"padding:6px 13px;\n"
"text-decoration:none;\n"
"text-shadow:0px 1px 0px #263666;")
        self.b3.setObjectName("b3")
        self.bg.raise_()
        self.stoichiometry.raise_()
        self.predictor.raise_()
        self.b4.raise_()
        self.b3.raise_()
        self.stoichFrame = QtWidgets.QFrame(self.centralwidget)
        self.stoichFrame.setGeometry(QtCore.QRect(0, 0, 1000, 650))
        self.stoichFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.stoichFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.stoichFrame.setObjectName("stoichFrame")
        self.label = QtWidgets.QLabel(self.stoichFrame)
        self.label.setGeometry(QtCore.QRect(0, 0, 1000, 650))
        self.label.setStyleSheet("background-color: #222840;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.stoichFrame)
        self.plainTextEdit.setGeometry(QtCore.QRect(300, 60, 400, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setStyleSheet("background-color: rgb(94, 114, 160);\n"
"color: #CDB7E3;\n"
"border-radius:5px;\n"
"border:1px solid #1f2f47;")
        self.plainTextEdit.setObjectName("plainTextEdit")
        homeWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(homeWindow)
        self.stoichiometry.clicked.connect(self.stoichFrame.show)
        QtCore.QMetaObject.connectSlotsByName(homeWindow)

    def retranslateUi(self, homeWindow):
        _translate = QtCore.QCoreApplication.translate
        homeWindow.setWindowTitle(_translate("homeWindow", "Chemistry Papa"))
        self.stoichiometry.setText(_translate("homeWindow", "Stoichiometry"))
        self.predictor.setText(_translate("homeWindow", "Predictor"))
        self.b4.setText(_translate("homeWindow", "Button 4"))
        self.b3.setText(_translate("homeWindow", "Button 3"))