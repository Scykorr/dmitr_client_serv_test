# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_login.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_client_login(object):
    def setupUi(self, Form_client_login):
        Form_client_login.setObjectName("Form_client_login")
        Form_client_login.resize(375, 101)
        self.lineEdit_fio = QtWidgets.QLineEdit(Form_client_login)
        self.lineEdit_fio.setGeometry(QtCore.QRect(50, 40, 271, 20))
        self.lineEdit_fio.setObjectName("lineEdit_fio")
        self.label_fio = QtWidgets.QLabel(Form_client_login)
        self.label_fio.setGeometry(QtCore.QRect(130, 10, 111, 20))
        self.label_fio.setObjectName("label_fio")
        self.pushButton_fio = QtWidgets.QPushButton(Form_client_login)
        self.pushButton_fio.setGeometry(QtCore.QRect(150, 70, 75, 23))
        self.pushButton_fio.setObjectName("pushButton_fio")

        self.retranslateUi(Form_client_login)
        QtCore.QMetaObject.connectSlotsByName(Form_client_login)

    def retranslateUi(self, Form_client_login):
        _translate = QtCore.QCoreApplication.translate
        Form_client_login.setWindowTitle(_translate("Form_client_login", "login"))
        self.lineEdit_fio.setText(_translate("Form_client_login", "Иванов Иван Иванович"))
        self.label_fio.setText(_translate("Form_client_login", "ФИО тестируемого"))
        self.pushButton_fio.setText(_translate("Form_client_login", "Войти"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_client_login = QtWidgets.QWidget()
    ui = Ui_Form_client_login()
    ui.setupUi(Form_client_login)
    Form_client_login.show()
    sys.exit(app.exec_())
