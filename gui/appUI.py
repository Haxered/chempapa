from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QTextCharFormat
from PyQt5.QtWidgets import QMainWindow

class UIHomeFrame(object):
    def setupUI(self, MainWindow):

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.homeFrame = QtWidgets.QFrame(self.centralwidget)
        self.homeFrame.setGeometry(QtCore.QRect(0, 0, 1000, 650))
        self.homeFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.homeFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.homeFrame.setObjectName("homeFrame")

        self.stoichBTN = QtWidgets.QPushButton("Stoichiometry", self.homeFrame)
        self.stoichBTN.setGeometry(QtCore.QRect(80, 145, 250, 70))
        self.stoichBTN.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #3c20cd, stop:1#160c4e);\n"
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

        self.predictor = QtWidgets.QPushButton(self.homeFrame)
        self.predictor.setGeometry(QtCore.QRect(80, 235, 250, 70))
        self.predictor.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #3c20cd, stop:1#160c4e);\n"
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
        self.b4.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #3c20cd, stop:1#160c4e);\n"
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
        self.bg.setPixmap(QtGui.QPixmap("gui/media/BG.jpg"))
        self.bg.setScaledContents(True)
        self.bg.setObjectName("bg")
        self.b3 = QtWidgets.QPushButton(self.homeFrame)
        self.b3.setGeometry(QtCore.QRect(80, 325, 250, 70))
        self.b3.setStyleSheet(
            "background-color:qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 #3c20cd, stop:1#160c4e);\n"
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
        self.stoichBTN.raise_()
        self.predictor.raise_()
        self.b4.raise_()
        self.b3.raise_()

        MainWindow.setCentralWidget(self.homeFrame)

class UIStoichFrame(object):
    def setupUI(self, MainWindow):

        self.centralwidget = QtWidgets.QWidget(MainWindow)
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

        self.homeBTN = QtWidgets.QPushButton(self.stoichFrame)
        self.homeBTN.setGeometry(QtCore.QRect(750, 580, 250, 70))

        self.equationInput = QtWidgets.QTextEdit(self.stoichFrame)
        self.equationInput.setGeometry(QtCore.QRect(300, 60, 400, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.equationInput.setFont(font)
        self.equationInput.setStyleSheet("background-color: rgb(94, 114, 160);\n"
                                         "color: #CDB7E3;\n"
                                         "border-radius:5px;\n"
                                         "border:1px solid #1f2f47;")
        MainWindow.setCentralWidget(self.stoichFrame)

    def keyPressEvent(self, event):
        print("hi")
        if event.key() == QtCore.Qt.ShiftModifier and event.key() == QtCore.Qt.Key_F6:
            cursor = self.equationInput.textCursor()
            format = cursor.charFormat()
            if format.verticalAlignment() == QTextCharFormat.AlignSubScript:
                vert = QTextCharFormat.AlignNormal
            else:
                vert = QTextCharFormat.AlignSubScript
            format.setVerticalAlignment(vert)
            cursor.setCharFormat(format)



class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self._mutex = QtCore.QMutex()

        self.setWindowTitle("Chemistry Papa")
        self.setObjectName("homeWindow")
        self.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        self.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("gui/media/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)
        self.setWindowOpacity(1.0)
        self.setAutoFillBackground(False)
        # self.centralwidget = QtWidgets.QWidget(self)
        # self.centralwidget.setObjectName("centralwidget")
        # self.setCentralWidget(self.centralwidget)

        self.uiHomeFrame = UIHomeFrame()
        self.uiStoichFrame = UIStoichFrame()
        self.startUIHomeFrame()

    def startUIHomeFrame(self):
        self.uiHomeFrame.setupUI(self)
        self.uiHomeFrame.stoichBTN.clicked.connect(self.startUIStoichFrame)
        self.show()

    def startUIStoichFrame(self):
        self.uiStoichFrame.setupUI(self)
        self.uiStoichFrame.homeBTN.clicked.connect(self.startUIHomeFrame)
        self.show()














# from PyQt5 import QtGui, QtWidgets, QtCore
# from PyQt5.QtGui import QPixmap, QPainter
# from PyQt5.QtWidgets import *
#
#
# class HomeWin(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setFixedSize(1000, 650)
#         self.setWindowTitle("Chemistry Calc")
#         self.setWindowIcon(QtGui.QIcon(QtGui.QPixmap("gui/media/icon.png")))
#
#         bg = QtWidgets.QLabel()
#         bg.setGeometry(QtCore.QRect(0, 0, 1000, 650))
#         bg.setText("")
#         bg.setPixmap(QtGui.QPixmap("gui/media/BG.jpg"))
#         bg.setScaledContents(True)
#         self.setCentralWidget(bg)
#
#         self.pushButton = QtWidgets.QPushButton(self.centralwidget)
#         self.pushButton.setGeometry(QtCore.QRect(200, 150, 93, 28))
#



    # class ResizableBackground(QtWidgets.QLabel):
#     ResizeSignal = QtCore.pyqtSignal(int)
#
#     def __init__(self, width, height):
#         super().__init__()
#         self.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
#         self.setGeometry(0, 0, width, height)
#         self.setFrameShape(QtWidgets.QFrame.Box)
#         self.setText("")
#         self.pix = QtGui.QPixmap("gui/media/BG.jpg")
#         self.setPixmap(self.pix)
#         self.installEventFilter(self)
#
#     def eventFilter(self, obj, event):
#         if event.type() == QtCore.QEvent.Resize:
#             if not self.pix.isNull():
#                 pixmap = self.pix.scaled(self.width(), self.height(), QtCore.Qt.KeepAspectRatio)
#                 if pixmap.width() != self.width() or pixmap.height() != self.height():
#                     self.ResizeSignal.emit(1)
#         return super().eventFilter(obj, event)
#
#     def paintEvent(self, event):
#         if not self.pix.isNull():
#             size = self.size()
#             painter = QPainter(self)
#             point = QtCore.QPoint(0, 0)
#             scaled_pix = self.pix.scaled(size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
#             # start painting the label from left upper corner
#             point.setX((size.width() - scaled_pix.width()) / 2)
#             point.setY((size.height() - scaled_pix.height()) / 2)
#             painter.drawPixmap(point, scaled_pix)
#
#     def changePixmap(self, img):
#         self.pix = img
#         self.repaint()