from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCharFormat


class Widget(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.text_box = QtWidgets.QTextEdit(self)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.text_box)

    def keyPressEvent(self, event):
        if event.modifiers() == Qt.ShiftModifier and event.key() == Qt.Key_F6:
            cursor = self.text_box.textCursor()
            if format.verticalAlignment() == QTextCharFormat.AlignSubScript:
                vert = QTextCharFormat.AlignNormal
            else:
                vert = QTextCharFormat.AlignSubScript
            print(vert)
            format.setVerticalAlignment(vert)
            cursor.setCharFormat(format)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = Widget()
    w.show()
    app.exec()