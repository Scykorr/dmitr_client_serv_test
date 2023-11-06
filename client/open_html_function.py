from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1019, 593)

        self.webView = QWebEngineView(parent=Form)
        self.webView.setGeometry(QtCore.QRect(0, 30, 1021, 561))
        self.webView.setObjectName("webView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle("ИНСТРУКЦИЯ")


class Window(QtWidgets.QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        file = "D:/PycharmProjects/dmitr_client_serv_test/draft/var_1_text1.mht"  # !!! +++
        self.webView.load(QtCore.QUrl.fromLocalFile(file))  # !!! +++


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec())