# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zadanie4_part2_var2.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Zadanie4_part2_var1(object):
    def setupUi(self, Zadanie4_part2_var1):
        Zadanie4_part2_var1.setObjectName("Zadanie4_part2_var1")
        Zadanie4_part2_var1.resize(425, 690)
        self.label_title = QtWidgets.QLabel(Zadanie4_part2_var1)
        self.label_title.setGeometry(QtCore.QRect(20, 10, 381, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_title.setFont(font)
        self.label_title.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_title.setTextFormat(QtCore.Qt.AutoText)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.pushButton_answer = QtWidgets.QPushButton(Zadanie4_part2_var1)
        self.pushButton_answer.setGeometry(QtCore.QRect(150, 650, 101, 31))
        self.pushButton_answer.setObjectName("pushButton_answer")
        self.textBrowser = QtWidgets.QTextBrowser(Zadanie4_part2_var1)
        self.textBrowser.setGeometry(QtCore.QRect(20, 90, 331, 251))
        self.textBrowser.setObjectName("textBrowser")
        self.lineEdit = QtWidgets.QLineEdit(Zadanie4_part2_var1)
        self.lineEdit.setGeometry(QtCore.QRect(360, 140, 51, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Zadanie4_part2_var1)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 370, 331, 211))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(Zadanie4_part2_var1)
        self.lineEdit_2.setGeometry(QtCore.QRect(360, 460, 51, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Zadanie4_part2_var1)
        QtCore.QMetaObject.connectSlotsByName(Zadanie4_part2_var1)

    def retranslateUi(self, Zadanie4_part2_var1):
        _translate = QtCore.QCoreApplication.translate
        Zadanie4_part2_var1.setWindowTitle(_translate("Zadanie4_part2_var1", "Form"))
        self.label_title.setText(_translate("Zadanie4_part2_var1", "Задание 4.\n"
" Укажите номера абзацев, куда могут быть\n"
" включены данные ниже части текста."))
        self.pushButton_answer.setText(_translate("Zadanie4_part2_var1", "Далее"))
        self.textBrowser.setHtml(_translate("Zadanie4_part2_var1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\">a) It is characterized by a single constant value. This is the ratio of the electric charge on each conductor to the potential difference between them. In practice, the dielectric between the plates passes a small amount of leakage current. Capacitors are widely used in electronic circuits to block the flow of direct current while allowing alternating current to pass, to filter out interference, to smooth the output of power supplies, and for many other purposes. They are used in resonant circuits in radio frequency equipment to select particular frequencies from a signal with many frequencies.</span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Zadanie4_part2_var1", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman\',\'serif\'; font-size:12pt;\">b)  The electronic devices we encounter all around us are driven and controlled by the flow of electrical current through electronic circuits. Each circuit is an arrangement of electrical elements designed to perform specific functions. Circuits can be engineered to carry out a wide variety of operations, from simple actions to complex tasks, according to the job(s) the system must perform. Let’s begin by looking at how the key passive elements found in most electronic circuits work.</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Zadanie4_part2_var1 = QtWidgets.QWidget()
    ui = Ui_Zadanie4_part2_var1()
    ui.setupUi(Zadanie4_part2_var1)
    Zadanie4_part2_var1.show()
    sys.exit(app.exec_())
