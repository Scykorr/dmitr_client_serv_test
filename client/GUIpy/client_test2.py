# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_test2.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_test2(object):
    def setupUi(self, Form_test2):
        Form_test2.setObjectName("Form_test2")
        Form_test2.resize(1197, 890)
        self.scrollArea = QtWidgets.QScrollArea(Form_test2)
        self.scrollArea.setGeometry(QtCore.QRect(0, 10, 1191, 876))
        self.scrollArea.setMaximumSize(QtCore.QSize(1191, 16777215))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 1172, 1056))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.plainTextEdit_question = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.plainTextEdit_question.setObjectName("plainTextEdit_question")
        self.verticalLayout_4.addWidget(self.plainTextEdit_question)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.label_img_question = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_img_question.setMinimumSize(QtCore.QSize(404, 286))
        self.label_img_question.setFrameShape(QtWidgets.QFrame.Box)
        self.label_img_question.setText("")
        self.label_img_question.setObjectName("label_img_question")
        self.verticalLayout_3.addWidget(self.label_img_question, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_19.addLayout(self.verticalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.radioButton_answer1 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.radioButton_answer1.setObjectName("radioButton_answer1")
        self.horizontalLayout_6.addWidget(self.radioButton_answer1)
        self.radioButton_answer2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.radioButton_answer2.setObjectName("radioButton_answer2")
        self.horizontalLayout_6.addWidget(self.radioButton_answer2)
        self.verticalLayout_19.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_img_var1 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_img_var1.setMinimumSize(QtCore.QSize(404, 286))
        self.label_img_var1.setFrameShape(QtWidgets.QFrame.Box)
        self.label_img_var1.setObjectName("label_img_var1")
        self.horizontalLayout_7.addWidget(self.label_img_var1)
        self.label_img_var3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_img_var3.setMinimumSize(QtCore.QSize(404, 286))
        self.label_img_var3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_img_var3.setObjectName("label_img_var3")
        self.horizontalLayout_7.addWidget(self.label_img_var3)
        self.verticalLayout_19.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.radioButton_answer3 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.radioButton_answer3.setObjectName("radioButton_answer3")
        self.horizontalLayout_8.addWidget(self.radioButton_answer3)
        self.radioButton_answer = QtWidgets.QRadioButton(self.scrollAreaWidgetContents_2)
        self.radioButton_answer.setObjectName("radioButton_answer")
        self.horizontalLayout_8.addWidget(self.radioButton_answer)
        self.verticalLayout_19.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_img_var2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_img_var2.setMinimumSize(QtCore.QSize(404, 286))
        self.label_img_var2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_img_var2.setObjectName("label_img_var2")
        self.horizontalLayout_9.addWidget(self.label_img_var2)
        self.label_img_var4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_img_var4.setMinimumSize(QtCore.QSize(404, 286))
        self.label_img_var4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_img_var4.setObjectName("label_img_var4")
        self.horizontalLayout_9.addWidget(self.label_img_var4)
        self.verticalLayout_19.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pushButton_answer = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.pushButton_answer.setObjectName("pushButton_answer")
        self.horizontalLayout_10.addWidget(self.pushButton_answer)
        self.label_timer = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_timer.setText("")
        self.label_timer.setObjectName("label_timer")
        self.horizontalLayout_10.addWidget(self.label_timer)
        self.verticalLayout_19.addLayout(self.horizontalLayout_10)
        self.verticalLayout_18.addLayout(self.verticalLayout_19)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.retranslateUi(Form_test2)
        QtCore.QMetaObject.connectSlotsByName(Form_test2)

    def retranslateUi(self, Form_test2):
        _translate = QtCore.QCoreApplication.translate
        Form_test2.setWindowTitle(_translate("Form_test2", "Form"))
        self.plainTextEdit_question.setPlainText(_translate("Form_test2", "пывпвп\n"
"ывпав"))
        self.radioButton_answer1.setText(_translate("Form_test2", "Первый вариант ответа"))
        self.radioButton_answer2.setText(_translate("Form_test2", "Второй вариант ответа"))
        self.label_img_var1.setText(_translate("Form_test2", "Место для изображения"))
        self.label_img_var3.setText(_translate("Form_test2", "Место для изображения"))
        self.radioButton_answer3.setText(_translate("Form_test2", "Третий вариант ответа"))
        self.radioButton_answer.setText(_translate("Form_test2", "Четвертый вариант ответа"))
        self.label_img_var2.setText(_translate("Form_test2", "Место для изображения"))
        self.label_img_var4.setText(_translate("Form_test2", "Место для изображения"))
        self.pushButton_answer.setText(_translate("Form_test2", "Ответить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form_test2 = QtWidgets.QWidget()
    ui = Ui_Form_test2()
    ui.setupUi(Form_test2)
    Form_test2.show()
    sys.exit(app.exec_())
