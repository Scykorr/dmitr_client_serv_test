# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_variant.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(572, 368)
        self.tableWidget_server = QtWidgets.QTableWidget(Form)
        self.tableWidget_server.setGeometry(QtCore.QRect(10, 40, 551, 321))
        self.tableWidget_server.setObjectName("tableWidget_server")
        self.tableWidget_server.setColumnCount(0)
        self.tableWidget_server.setRowCount(0)
        self.pushButton_delete_all = QtWidgets.QPushButton(Form)
        self.pushButton_delete_all.setGeometry(QtCore.QRect(410, 10, 131, 23))
        self.pushButton_delete_all.setObjectName("pushButton_delete_all")
        self.pushButton_refresh = QtWidgets.QPushButton(Form)
        self.pushButton_refresh.setGeometry(QtCore.QRect(20, 10, 131, 23))
        self.pushButton_refresh.setObjectName("pushButton_refresh")
        self.label_img = QtWidgets.QLabel(Form)
        self.label_img.setGeometry(QtCore.QRect(0, 0, 571, 371))
        self.label_img.setText("")
        self.label_img.setPixmap(QtGui.QPixmap("../../img/for_test2.jpg"))
        self.label_img.setObjectName("label_img")
        self.label_img.raise_()
        self.tableWidget_server.raise_()
        self.pushButton_delete_all.raise_()
        self.pushButton_refresh.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_delete_all.setText(_translate("Form", "Удалить результаты"))
        self.pushButton_refresh.setText(_translate("Form", "Обновить результаты"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
