# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_server.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_server(object):
    def setupUi(self, Form_server):
        Form_server.setObjectName("Form_server")
        Form_server.resize(463, 348)
        self.tableWidget_server = QtWidgets.QTableWidget(Form_server)
        self.tableWidget_server.setGeometry(QtCore.QRect(10, 40, 441, 301))
        self.tableWidget_server.setObjectName("tableWidget_server")
        self.tableWidget_server.setColumnCount(0)
        self.tableWidget_server.setRowCount(0)
        self.pushButton_delete_all = QtWidgets.QPushButton(Form_server)
        self.pushButton_delete_all.setGeometry(QtCore.QRect(314, 10, 131, 23))
        self.pushButton_delete_all.setObjectName("pushButton_delete_all")
        self.pushButton_work_db = QtWidgets.QPushButton(Form_server)
        self.pushButton_work_db.setGeometry(QtCore.QRect(20, 10, 131, 23))
        self.pushButton_work_db.setObjectName("pushButton_work_db")

        self.retranslateUi(Form_server)
        QtCore.QMetaObject.connectSlotsByName(Form_server)

    def retranslateUi(self, Form_server):
        _translate = QtCore.QCoreApplication.translate
        Form_server.setWindowTitle(_translate("Form_server", "Server"))
        self.pushButton_delete_all.setText(_translate("Form_server", "Удалить результаты"))
        self.pushButton_work_db.setText(_translate("Form_server", "Работа с вопросами"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_server = QtWidgets.QWidget()
    ui = Ui_Form_server()
    ui.setupUi(Form_server)
    Form_server.show()
    sys.exit(app.exec_())
