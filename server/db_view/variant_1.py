import sqlite3 as sql
from PyQt5 import QtWidgets


from GUIpy.variant_1.zadanie1_part1_var1 import Ui_Zadanie1_part1


class Task1Part1Var1(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie1_part1()
        self.ui_form.setupUi(self)
        self.set_default_vals()

    def set_default_vals(self):
        self.ui_form.lineEdit_word_22.setText('компонент')
        self.ui_form.lineEdit_word_23.setText('постоянная')
        self.ui_form.lineEdit_word_24.setText('тенденция')
        self.ui_form.lineEdit_word_25.setText('материал')
        self.ui_form.lineEdit_word_26.setText('определять')
        self.ui_form.lineEdit_word_27.setText('энергия')
        self.ui_form.lineEdit_word_28.setText('передача')
        self.ui_form.lineEdit_word_29.setText('механизм')
        self.ui_form.lineEdit_word_30.setText('символ')
        self.ui_form.lineEdit_word_31.setText('характеристики')
        self.ui_form.lineEdit_word_32.setText('типичный')
        self.ui_form.lineEdit_word_33.setText('диод')
        self.ui_form.lineEdit_word_34.setText('резистор')
        self.ui_form.lineEdit_word_35.setText('напряжение')
        self.ui_form.lineEdit_word_36.setText('индикатор')
        self.ui_form.lineEdit_word_37.setText('аппарат')
        self.ui_form.lineEdit_word_38.setText('характеристика')
        self.ui_form.lineEdit_word_39.setText('пропорциональный')
        self.ui_form.lineEdit_word_40.setText('инструмент')
        self.ui_form.lineEdit_word_41.setText('фаза')
        self.ui_form.lineEdit_word_42.setText('батарея')

    def main_select(self, user_name):
        vals = []
        con = sql.connect('../data.db')
        cur = con.cursor()
        answer = cur.execute(
            f"select answer_user from zadanie_variant where num_zadanie=1 and user_name='{user_name}' and num_part=1 and variant=1")
        for el in answer:
            vals.append(el)
        val = vals[0][0].split(';')
        self.update_cells(val)
        con.commit()
        cur.close()
        con.close()
        return vals

    def update_cells(self, val):
        self.ui_form.lineEdit_word_1.setText(val[0])
        self.ui_form.lineEdit_word_2.setText(val[1])
        self.ui_form.lineEdit_word_3.setText(val[2])
        self.ui_form.lineEdit_word_4.setText(val[3])
        self.ui_form.lineEdit_word_5.setText(val[4])
        self.ui_form.lineEdit_word_6.setText(val[5])
        self.ui_form.lineEdit_word_7.setText(val[6])
        self.ui_form.lineEdit_word_8.setText(val[7])
        self.ui_form.lineEdit_word_9.setText(val[8])
        self.ui_form.lineEdit_word_10.setText(val[9])
        self.ui_form.lineEdit_word_11.setText(val[10])
        self.ui_form.lineEdit_word_12.setText(val[11])
        self.ui_form.lineEdit_word_13.setText(val[12])
        self.ui_form.lineEdit_word_14.setText(val[13])
        self.ui_form.lineEdit_word_15.setText(val[14])
        self.ui_form.lineEdit_word_16.setText(val[15])
        self.ui_form.lineEdit_word_17.setText(val[16])
        self.ui_form.lineEdit_word_18.setText(val[17])
        self.ui_form.lineEdit_word_19.setText(val[18])
        self.ui_form.lineEdit_word_20.setText(val[19])
        self.ui_form.lineEdit_word_21.setText(val[20])
        self.check_values()

    def check_values(self):
        if self.ui_form.lineEdit_word_1.text() != self.ui_form.lineEdit_word_22.text():
            self.ui_form.lineEdit_word_1.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_word_2.text() != self.ui_form.lineEdit_word_23.text():
            self.ui_form.lineEdit_word_2.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_word_3.text() != self.ui_form.lineEdit_word_24.text():
            self.ui_form.lineEdit_word_3.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_word_4.text() != self.ui_form.lineEdit_word_25.text():
            self.ui_form.lineEdit_word_4.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_word_5.text() != self.ui_form.lineEdit_word_26.text():
            self.ui_form.lineEdit_word_5.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_word_6.text() != self.ui_form.lineEdit_word_27.text():
            self.ui_form.lineEdit_word_6.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_word_7.text() != self.ui_form.lineEdit_word_28.text():
            self.ui_form.lineEdit_word_7.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_word_8.text() != self.ui_form.lineEdit_word_29.text():
            self.ui_form.lineEdit_word_8.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_word_9.text() != self.ui_form.lineEdit_word_30.text():
            self.ui_form.lineEdit_word_9.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_word_10.text() != self.ui_form.lineEdit_word_31.text():
            self.ui_form.lineEdit_word_10.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_word_11.text() != self.ui_form.lineEdit_word_32.text():
            self.ui_form.lineEdit_word_11.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_word_12.text() != self.ui_form.lineEdit_word_33.text():
            self.ui_form.lineEdit_word_12.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_word_13.text() != self.ui_form.lineEdit_word_34.text():
            self.ui_form.lineEdit_word_13.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_word_14.text() != self.ui_form.lineEdit_word_35.text():
            self.ui_form.lineEdit_word_14.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_word_15.text() != self.ui_form.lineEdit_word_36.text():
            self.ui_form.lineEdit_word_15.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_word_16.text() != self.ui_form.lineEdit_word_37.text():
            self.ui_form.lineEdit_word_16.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_word_17.text() != self.ui_form.lineEdit_word_38.text():
            self.ui_form.lineEdit_word_17.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_word_18.text() != self.ui_form.lineEdit_word_39.text():
            self.ui_form.lineEdit_word_18.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_word_19.text() != self.ui_form.lineEdit_word_40.text():
            self.ui_form.lineEdit_word_19.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_word_20.text() != self.ui_form.lineEdit_word_41.text():
            self.ui_form.lineEdit_word_20.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_word_21.text() != self.ui_form.lineEdit_word_42.text():
            self.ui_form.lineEdit_word_21.setStyleSheet("QLineEdit {background-color: red;}")


