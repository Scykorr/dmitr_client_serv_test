from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView
import os
import sys


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1025, 700)

        self.webView = QWebEngineView(parent=Form)
        self.webView.setGeometry(QtCore.QRect(0, 10, 1021, 695))
        self.webView.setObjectName("webView")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle("Text")


class Window(QtWidgets.QWidget, Ui_Form):
    def __init__(self, filename='var_1_text1.htm', parent=None):
        super().__init__(parent)
        self.setupUi(self)
        cwd = os.path.abspath(f'../../draft/{filename}')
        file = cwd
        self.webView.load(QtCore.QUrl.fromLocalFile(file))  # !!! +++


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())
