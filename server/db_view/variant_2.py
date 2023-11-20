import sqlite3 as sql
from PyQt5 import QtWidgets

from open_html_function import Window

from GUIpy.variant_2.zadanie1_part1_var2 import Ui_Zadanie1_part1
from GUIpy.variant_2.zadanie2_part1_var2 import Ui_Zadanie2_part1
from GUIpy.variant_2.zadanie3_4_5_part1_var2 import Ui_Zadanie3_4_5_part1_var1
from GUIpy.variant_2.zadanie6_part1_var2 import Ui_Zadanie6_part1_var1
from GUIpy.variant_2.zadanie7_part1_var2 import Ui_Zadanie7_part1_var1
from GUIpy.variant_2.zadanie8_part1_var2 import Ui_Zadanie8_part1_var1
from GUIpy.variant_2.zadanie1_2_3_part2_var2 import Ui_Zadanie1_2_3_part2_var1
from GUIpy.variant_2.zadanie4_part2_var2 import Ui_Zadanie4_part2_var1
from GUIpy.variant_2.zadanie5_part2_var2 import Ui_Zadanie5_part2_var1
from GUIpy.variant_2.zadanie6_part2_var2 import Ui_Zadanie6_part2_var1


class Task1Part1Var2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie1_part1()
        self.ui_form.setupUi(self)
        self.set_default_vals()

    def set_default_vals(self):
        self.ui_form.lineEdit_word_22.setText('накапливать')
        self.ui_form.lineEdit_word_23.setText('электрический')
        self.ui_form.lineEdit_word_24.setText('фактор')
        self.ui_form.lineEdit_word_25.setText('проводник')
        self.ui_form.lineEdit_word_26.setText('температура')
        self.ui_form.lineEdit_word_27.setText('активный/пассивный')
        self.ui_form.lineEdit_word_28.setText('физические характеристики')
        self.ui_form.lineEdit_word_29.setText('электронные компоненты')
        self.ui_form.lineEdit_word_30.setText('резистор')
        self.ui_form.lineEdit_word_31.setText('практичный')
        self.ui_form.lineEdit_word_32.setText('терминал')
        self.ui_form.lineEdit_word_33.setText('константа')
        self.ui_form.lineEdit_word_34.setText('материал')
        self.ui_form.lineEdit_word_35.setText('энергия')
        self.ui_form.lineEdit_word_36.setText('механизм')
        self.ui_form.lineEdit_word_37.setText('символ')
        self.ui_form.lineEdit_word_38.setText('напряжение')
        self.ui_form.lineEdit_word_39.setText('индикатор')
        self.ui_form.lineEdit_word_40.setText('инструмент')
        self.ui_form.lineEdit_word_41.setText('фаза')
        self.ui_form.lineEdit_word_42.setText('батарея')

    def main_select(self, user_name):
        vals = []
        con = sql.connect('../data.db')
        cur = con.cursor()
        answer = cur.execute(
            f"select answer_user from zadanie_variant where num_zadanie=1 and user_name='{user_name}'"
            f" and num_part=1 and variant=2")
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


class Task2Part1Var2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie2_part1()
        self.ui_form.setupUi(self)
        self.set_default_vals()

    def set_default_vals(self):
        self.ui_form.lineEdit_answer_17.setText('v')
        self.ui_form.lineEdit_answer_18.setText('adv')
        self.ui_form.lineEdit_answer_19.setText('n')
        self.ui_form.lineEdit_answer_20.setText('adj')
        self.ui_form.lineEdit_answer_21.setText('adv')
        self.ui_form.lineEdit_answer_22.setText('v')
        self.ui_form.lineEdit_answer_23.setText('v')
        self.ui_form.lineEdit_answer_24.setText('v')
        self.ui_form.lineEdit_answer_25.setText('adj')
        self.ui_form.lineEdit_answer_26.setText('adj')
        self.ui_form.lineEdit_answer_27.setText('adj')
        self.ui_form.lineEdit_answer_28.setText('v')
        self.ui_form.lineEdit_answer_29.setText('v')
        self.ui_form.lineEdit_answer_30.setText('adj')
        self.ui_form.lineEdit_answer_31.setText('adv')
        self.ui_form.lineEdit_answer_32.setText('n')

    def main_select(self, user_name):
        vals = []
        con = sql.connect('../data.db')
        cur = con.cursor()
        answer = cur.execute(
            f"select answer_user from zadanie_variant where num_zadanie=2 and user_name='{user_name}' and num_part=1 and variant=2")
        for el in answer:
            vals.append(el)
        val = vals[0][0].split(';')
        self.update_cells(val)
        con.commit()
        cur.close()
        con.close()
        return vals

    def update_cells(self, val):
        self.ui_form.lineEdit_answer_1.setText(val[0])
        self.ui_form.lineEdit_answer_2.setText(val[1])
        self.ui_form.lineEdit_answer_3.setText(val[2])
        self.ui_form.lineEdit_answer_4.setText(val[3])
        self.ui_form.lineEdit_answer_5.setText(val[4])
        self.ui_form.lineEdit_answer_6.setText(val[5])
        self.ui_form.lineEdit_answer_7.setText(val[6])
        self.ui_form.lineEdit_answer_8.setText(val[7])
        self.ui_form.lineEdit_answer_9.setText(val[8])
        self.ui_form.lineEdit_answer_10.setText(val[9])
        self.ui_form.lineEdit_answer_11.setText(val[10])
        self.ui_form.lineEdit_answer_12.setText(val[11])
        self.ui_form.lineEdit_answer_13.setText(val[12])
        self.ui_form.lineEdit_answer_14.setText(val[13])
        self.ui_form.lineEdit_answer_15.setText(val[14])
        self.ui_form.lineEdit_answer_16.setText(val[15])
        self.check_values()

    def check_values(self):
        if self.ui_form.lineEdit_answer_1.text() != self.ui_form.lineEdit_answer_17.text():
            self.ui_form.lineEdit_answer_1.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_2.text() != self.ui_form.lineEdit_answer_18.text():
            self.ui_form.lineEdit_answer_2.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_3.text() != self.ui_form.lineEdit_answer_19.text():
            self.ui_form.lineEdit_answer_3.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_4.text() != self.ui_form.lineEdit_answer_20.text():
            self.ui_form.lineEdit_answer_4.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_5.text() != self.ui_form.lineEdit_answer_21.text():
            self.ui_form.lineEdit_answer_5.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_6.text() != self.ui_form.lineEdit_answer_22.text():
            self.ui_form.lineEdit_answer_6.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_7.text() != self.ui_form.lineEdit_answer_23.text():
            self.ui_form.lineEdit_answer_7.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_8.text() != self.ui_form.lineEdit_answer_24.text():
            self.ui_form.lineEdit_answer_8.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_9.text() != self.ui_form.lineEdit_answer_25.text():
            self.ui_form.lineEdit_answer_9.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_10.text() != self.ui_form.lineEdit_answer_26.text():
            self.ui_form.lineEdit_answer_10.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_11.text() != self.ui_form.lineEdit_answer_27.text():
            self.ui_form.lineEdit_answer_11.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_12.text() != self.ui_form.lineEdit_answer_28.text():
            self.ui_form.lineEdit_answer_12.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_13.text() != self.ui_form.lineEdit_answer_29.text():
            self.ui_form.lineEdit_answer_13.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_14.text() != self.ui_form.lineEdit_answer_30.text():
            self.ui_form.lineEdit_answer_14.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_15.text() != self.ui_form.lineEdit_answer_31.text():
            self.ui_form.lineEdit_answer_15.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_16.text() != self.ui_form.lineEdit_answer_32.text():
            self.ui_form.lineEdit_answer_16.setStyleSheet("QLineEdit {background-color: red;}")


class Task345Part1Var2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie3_4_5_part1_var1()
        self.ui_form.setupUi(self)
        self.set_default_vals()
        self.ui_form.pushButton.clicked.connect(self.get_text)

    def set_default_vals(self):
        self.ui_form.lineEdit_zadanie4_2.setText('2 8 25 44 47')
        self.ui_form.lineEdit_zadane5_16.setText('2')
        self.ui_form.lineEdit_zadane5_17.setText('3')
        self.ui_form.lineEdit_zadane5_18.setText('7')
        self.ui_form.lineEdit_zadane5_19.setText('8')
        self.ui_form.lineEdit_zadane5_20.setText('13')
        self.ui_form.lineEdit_zadane5_21.setText('11')
        self.ui_form.lineEdit_zadane5_22.setText('19')
        self.ui_form.lineEdit_zadane5_23.setText('24')
        self.ui_form.lineEdit_zadane5_24.setText('27')
        self.ui_form.lineEdit_zadane5_25.setText('30')
        self.ui_form.lineEdit_zadane5_26.setText('31')
        self.ui_form.lineEdit_zadane5_27.setText('32')
        self.ui_form.lineEdit_zadane5_28.setText('39')
        self.ui_form.lineEdit_zadane5_29.setText('44')
        self.ui_form.lineEdit_zadane5_30.setText('48')

    def main_select(self, user_name):
        vals = []
        con = sql.connect('../data.db')
        cur = con.cursor()
        answer = cur.execute(
            f"select answer_user from zadanie_variant where num_zadanie=4 and user_name='{user_name}' and num_part=1 and variant=2")
        for el in answer:
            vals.append(el)
        val = vals[0][0].split(';')
        self.update_cells_zad4(val)
        con.commit()
        cur.close()
        con.close()

        vals1 = []
        con = sql.connect('../data.db')
        cur = con.cursor()
        answer = cur.execute(
            f"select answer_user from zadanie_variant where num_zadanie=5 and user_name='{user_name}' and num_part=1 and variant=2")
        for el in answer:
            vals1.append(el)
        val1 = vals1[0][0].split(';')
        self.update_cells_zad5(val1)
        con.commit()
        cur.close()
        con.close()

    def update_cells_zad4(self, val):
        self.ui_form.lineEdit_zadanie4.setText(' '.join(val))
        self.check_values()

    def update_cells_zad5(self, val):
        self.ui_form.lineEdit_zadane5_1.setText(val[0])
        self.ui_form.lineEdit_zadane5_2.setText(val[1])
        self.ui_form.lineEdit_zadane5_3.setText(val[2])
        self.ui_form.lineEdit_zadane5_4.setText(val[3])
        self.ui_form.lineEdit_zadane5_5.setText(val[4])
        self.ui_form.lineEdit_zadane5_6.setText(val[5])
        self.ui_form.lineEdit_zadane5_7.setText(val[6])
        self.ui_form.lineEdit_zadane5_8.setText(val[7])
        self.ui_form.lineEdit_zadane5_9.setText(val[8])
        self.ui_form.lineEdit_zadane5_10.setText(val[9])
        self.ui_form.lineEdit_zadane5_11.setText(val[10])
        self.ui_form.lineEdit_zadane5_12.setText(val[11])
        self.ui_form.lineEdit_zadane5_13.setText(val[12])
        self.ui_form.lineEdit_zadane5_14.setText(val[13])
        self.ui_form.lineEdit_zadane5_15.setText(val[14])
        self.check_values()

    def check_values(self):
        if self.ui_form.lineEdit_zadanie4.text() != self.ui_form.lineEdit_zadanie4_2.text():
            self.ui_form.lineEdit_zadanie4.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_zadane5_1.text() != self.ui_form.lineEdit_zadane5_16.text():
            self.ui_form.lineEdit_zadane5_1.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_zadane5_2.text() != self.ui_form.lineEdit_zadane5_17.text():
            self.ui_form.lineEdit_zadane5_2.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_zadane5_3.text() != self.ui_form.lineEdit_zadane5_18.text():
            self.ui_form.lineEdit_zadane5_3.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_zadane5_4.text() != self.ui_form.lineEdit_zadane5_19.text():
            self.ui_form.lineEdit_zadane5_4.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_zadane5_5.text() != self.ui_form.lineEdit_zadane5_20.text():
            self.ui_form.lineEdit_zadane5_5.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_zadane5_6.text() != self.ui_form.lineEdit_zadane5_21.text():
            self.ui_form.lineEdit_zadane5_6.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_zadane5_7.text() != self.ui_form.lineEdit_zadane5_22.text():
            self.ui_form.lineEdit_zadane5_7.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_zadane5_8.text() != self.ui_form.lineEdit_zadane5_23.text():
            self.ui_form.lineEdit_zadane5_8.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_zadane5_9.text() != self.ui_form.lineEdit_zadane5_24.text():
            self.ui_form.lineEdit_zadane5_9.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_zadane5_10.text() != self.ui_form.lineEdit_zadane5_25.text():
            self.ui_form.lineEdit_zadane5_10.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_zadane5_11.text() != self.ui_form.lineEdit_zadane5_26.text():
            self.ui_form.lineEdit_zadane5_11.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_zadane5_12.text() != self.ui_form.lineEdit_zadane5_27.text():
            self.ui_form.lineEdit_zadane5_12.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_zadane5_13.text() != self.ui_form.lineEdit_zadane5_28.text():
            self.ui_form.lineEdit_zadane5_13.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_zadane5_14.text() != self.ui_form.lineEdit_zadane5_29.text():
            self.ui_form.lineEdit_zadane5_14.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_zadane5_15.text() != self.ui_form.lineEdit_zadane5_30.text():
            self.ui_form.lineEdit_zadane5_15.setStyleSheet("QLineEdit {background-color: red;}")

    def get_text(self):
        self.window = Window(filename='var_2_text1.htm')
        self.window.show()


class Task6Part1Var2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie6_part1_var1()
        self.ui_form.setupUi(self)
        self.true_answer = ['1,include', '2,component', '3,typically', '4,property', '5,the number of', '6,primary',
                            '7,varous', '8,producing', '9,over', '10,applied', '11,possible', '12,calculate',
                            '13,separated', '14,quickly', '15,change', '16,approximately']

    def get_num(self, word):
        for el in self.true_answer:
            el = el.split(',')
            if el[1] == word:
                return el[0]

    def set_default_vals(self):
        self.ui_form.lineEdit_answer_17.setText(self.get_num(self.ui_form.label_word_17.text()))
        self.ui_form.lineEdit_answer_18.setText(self.get_num(self.ui_form.label_word_18.text()))
        self.ui_form.lineEdit_answer_18.setText(self.get_num(self.ui_form.label_word_18.text()))
        self.ui_form.lineEdit_answer_19.setText(self.get_num(self.ui_form.label_word_19.text()))
        self.ui_form.lineEdit_answer_20.setText(self.get_num(self.ui_form.label_word_20.text()))
        self.ui_form.lineEdit_answer_21.setText(self.get_num(self.ui_form.label_word_21.text()))
        self.ui_form.lineEdit_answer_22.setText(self.get_num(self.ui_form.label_word_22.text()))
        self.ui_form.lineEdit_answer_23.setText(self.get_num(self.ui_form.label_word_23.text()))
        self.ui_form.lineEdit_answer_24.setText(self.get_num(self.ui_form.label_word_24.text()))
        self.ui_form.lineEdit_answer_25.setText(self.get_num(self.ui_form.label_word_25.text()))
        self.ui_form.lineEdit_answer_26.setText(self.get_num(self.ui_form.label_word_26.text()))
        self.ui_form.lineEdit_answer_27.setText(self.get_num(self.ui_form.label_word_27.text()))
        self.ui_form.lineEdit_answer_28.setText(self.get_num(self.ui_form.label_word_28.text()))
        self.ui_form.lineEdit_answer_29.setText(self.get_num(self.ui_form.label_word_29.text()))
        self.ui_form.lineEdit_answer_30.setText(self.get_num(self.ui_form.label_word_30.text()))
        self.ui_form.lineEdit_answer_31.setText(self.get_num(self.ui_form.label_word_31.text()))
        self.ui_form.lineEdit_answer_32.setText(self.get_num(self.ui_form.label_word_32.text()))

    def main_select(self, user_name):
        vals = []
        con = sql.connect('../data.db')
        cur = con.cursor()
        answer = cur.execute(
            f"select answer_user from zadanie_variant where num_zadanie=6 and user_name='{user_name}' and num_part=1 and variant=2")
        for el in answer:
            vals.append(el)
        val = vals[0][0].split(';')
        self.update_cells(val)
        con.commit()
        cur.close()
        con.close()
        self.set_default_vals()
        return vals

    def update_cells(self, val):
        self.ui_form.lineEdit_answer_1.setText(val[0].split(',')[0])
        self.ui_form.label_word_17.setText(val[0].split(',')[1])
        self.ui_form.lineEdit_answer_2.setText(val[1].split(',')[0])
        self.ui_form.label_word_18.setText(val[1].split(',')[1])
        self.ui_form.lineEdit_answer_3.setText(val[2].split(',')[0])
        self.ui_form.label_word_19.setText(val[2].split(',')[1])
        self.ui_form.lineEdit_answer_4.setText(val[3].split(',')[0])
        self.ui_form.label_word_20.setText(val[3].split(',')[1])
        self.ui_form.lineEdit_answer_5.setText(val[4].split(',')[0])
        self.ui_form.label_word_21.setText(val[4].split(',')[1])
        self.ui_form.lineEdit_answer_6.setText(val[5].split(',')[0])
        self.ui_form.label_word_22.setText(val[5].split(',')[1])
        self.ui_form.lineEdit_answer_7.setText(val[6].split(',')[0])
        self.ui_form.label_word_23.setText(val[6].split(',')[1])
        self.ui_form.lineEdit_answer_8.setText(val[7].split(',')[0])
        self.ui_form.label_word_24.setText(val[7].split(',')[1])
        self.ui_form.lineEdit_answer_9.setText(val[8].split(',')[0])
        self.ui_form.label_word_25.setText(val[8].split(',')[1])
        self.ui_form.lineEdit_answer_10.setText(val[9].split(',')[0])
        self.ui_form.label_word_26.setText(val[9].split(',')[1])
        self.ui_form.lineEdit_answer_11.setText(val[10].split(',')[0])
        self.ui_form.label_word_27.setText(val[10].split(',')[1])
        self.ui_form.lineEdit_answer_12.setText(val[11].split(',')[0])
        self.ui_form.label_word_28.setText(val[11].split(',')[1])
        self.ui_form.lineEdit_answer_13.setText(val[12].split(',')[0])
        self.ui_form.label_word_29.setText(val[12].split(',')[1])
        self.ui_form.lineEdit_answer_14.setText(val[13].split(',')[0])
        self.ui_form.label_word_30.setText(val[13].split(',')[1])
        self.ui_form.lineEdit_answer_15.setText(val[14].split(',')[0])
        self.ui_form.label_word_31.setText(val[14].split(',')[1])
        self.ui_form.lineEdit_answer_16.setText(val[15].split(',')[0])
        self.ui_form.label_word_32.setText(val[15].split(',')[1])
        self.check_values()

    def check_values(self):
        if self.ui_form.lineEdit_answer_1.text() != self.ui_form.lineEdit_answer_17.text():
            self.ui_form.lineEdit_answer_1.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_2.text() != self.ui_form.lineEdit_answer_18.text():
            self.ui_form.lineEdit_answer_2.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_3.text() != self.ui_form.lineEdit_answer_19.text():
            self.ui_form.lineEdit_answer_3.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_4.text() != self.ui_form.lineEdit_answer_20.text():
            self.ui_form.lineEdit_answer_4.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_5.text() != self.ui_form.lineEdit_answer_21.text():
            self.ui_form.lineEdit_answer_5.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_6.text() != self.ui_form.lineEdit_answer_22.text():
            self.ui_form.lineEdit_answer_6.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_7.text() != self.ui_form.lineEdit_answer_23.text():
            self.ui_form.lineEdit_answer_7.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_8.text() != self.ui_form.lineEdit_answer_24.text():
            self.ui_form.lineEdit_answer_8.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_9.text() != self.ui_form.lineEdit_answer_25.text():
            self.ui_form.lineEdit_answer_9.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_10.text() != self.ui_form.lineEdit_answer_26.text():
            self.ui_form.lineEdit_answer_10.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_11.text() != self.ui_form.lineEdit_answer_27.text():
            self.ui_form.lineEdit_answer_11.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_12.text() != self.ui_form.lineEdit_answer_28.text():
            self.ui_form.lineEdit_answer_12.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_13.text() != self.ui_form.lineEdit_answer_29.text():
            self.ui_form.lineEdit_answer_13.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_14.text() != self.ui_form.lineEdit_answer_30.text():
            self.ui_form.lineEdit_answer_14.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_15.text() != self.ui_form.lineEdit_answer_31.text():
            self.ui_form.lineEdit_answer_15.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_16.text() != self.ui_form.lineEdit_answer_32.text():
            self.ui_form.lineEdit_answer_16.setStyleSheet("QLineEdit {background-color: red;}")


class Task7Part1Var2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie7_part1_var1()
        self.ui_form.setupUi(self)
        self.set_default_vals()

    def set_default_vals(self):
        self.ui_form.lineEdit_answer_6.setText('4')
        self.ui_form.lineEdit_answer_7.setText('7')
        self.ui_form.lineEdit_answer_8.setText('1')
        self.ui_form.lineEdit_answer_9.setText('2')
        self.ui_form.lineEdit_answer_10.setText('6')

    def main_select(self, user_name):
        vals = []
        con = sql.connect('../data.db')
        cur = con.cursor()
        answer = cur.execute(
            f"select answer_user from zadanie_variant where num_zadanie=7 and user_name='{user_name}' and num_part=1 and variant=2")
        for el in answer:
            vals.append(el)
        val = vals[0][0].split(';')
        self.update_cells(val)
        con.commit()
        cur.close()
        con.close()
        return vals

    def update_cells(self, val):
        self.ui_form.lineEdit_answer_1.setText(val[0])
        self.ui_form.lineEdit_answer_2.setText(val[1])
        self.ui_form.lineEdit_answer_3.setText(val[2])
        self.ui_form.lineEdit_answer_4.setText(val[3])
        self.ui_form.lineEdit_answer_5.setText(val[4])
        self.check_values()

    def check_values(self):
        if self.ui_form.lineEdit_answer_1.text() != self.ui_form.lineEdit_answer_6.text():
            self.ui_form.lineEdit_answer_1.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_2.text() != self.ui_form.lineEdit_answer_7.text():
            self.ui_form.lineEdit_answer_2.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_3.text() != self.ui_form.lineEdit_answer_8.text():
            self.ui_form.lineEdit_answer_3.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_4.text() != self.ui_form.lineEdit_answer_9.text():
            self.ui_form.lineEdit_answer_4.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_5.text() != self.ui_form.lineEdit_answer_10.text():
            self.ui_form.lineEdit_answer_5.setStyleSheet("QLineEdit {background-color: red;}")


class Task8Part1Var2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie8_part1_var1()
        self.ui_form.setupUi(self)
        self.set_default_vals()

    def set_default_vals(self):
        self.ui_form.lineEdit_answer_11.setText('5')
        self.ui_form.lineEdit_answer_12.setText('10')
        self.ui_form.lineEdit_answer_13.setText('7')
        self.ui_form.lineEdit_answer_14.setText('9')
        self.ui_form.lineEdit_answer_15.setText('8')
        self.ui_form.lineEdit_answer_16.setText('1')
        self.ui_form.lineEdit_answer_17.setText('4')
        self.ui_form.lineEdit_answer_18.setText('3')
        self.ui_form.lineEdit_answer_19.setText('6')
        self.ui_form.lineEdit_answer_20.setText('2')

    def main_select(self, user_name):
        vals = []
        con = sql.connect('../data.db')
        cur = con.cursor()
        answer = cur.execute(
            f"select answer_user from zadanie_variant where num_zadanie=8 and user_name='{user_name}' and num_part=1 and variant=2")
        for el in answer:
            vals.append(el)
        val = vals[0][0].split(';')
        self.update_cells(val)
        con.commit()
        cur.close()
        con.close()
        return vals

    def update_cells(self, val):
        self.ui_form.lineEdit_answer_1.setText(val[0])
        self.ui_form.lineEdit_answer_2.setText(val[1])
        self.ui_form.lineEdit_answer_3.setText(val[2])
        self.ui_form.lineEdit_answer_4.setText(val[3])
        self.ui_form.lineEdit_answer_5.setText(val[4])
        self.ui_form.lineEdit_answer_6.setText(val[5])
        self.ui_form.lineEdit_answer_7.setText(val[6])
        self.ui_form.lineEdit_answer_8.setText(val[7])
        self.ui_form.lineEdit_answer_9.setText(val[8])
        self.ui_form.lineEdit_answer_10.setText(val[9])
        self.check_values()

    def check_values(self):
        if self.ui_form.lineEdit_answer_1.text() != self.ui_form.lineEdit_answer_11.text():
            self.ui_form.lineEdit_answer_1.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_2.text() != self.ui_form.lineEdit_answer_12.text():
            self.ui_form.lineEdit_answer_2.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_3.text() != self.ui_form.lineEdit_answer_13.text():
            self.ui_form.lineEdit_answer_3.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_4.text() != self.ui_form.lineEdit_answer_14.text():
            self.ui_form.lineEdit_answer_4.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_5.text() != self.ui_form.lineEdit_answer_15.text():
            self.ui_form.lineEdit_answer_5.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_6.text() != self.ui_form.lineEdit_answer_16.text():
            self.ui_form.lineEdit_answer_6.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_7.text() != self.ui_form.lineEdit_answer_17.text():
            self.ui_form.lineEdit_answer_7.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_8.text() != self.ui_form.lineEdit_answer_18.text():
            self.ui_form.lineEdit_answer_8.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_9.text() != self.ui_form.lineEdit_answer_19.text():
            self.ui_form.lineEdit_answer_9.setStyleSheet("QLineEdit {background-color: red;}")
        if self.ui_form.lineEdit_answer_10.text() != self.ui_form.lineEdit_answer_20.text():
            self.ui_form.lineEdit_answer_10.setStyleSheet("QLineEdit {background-color: red;}")

#
# class Task123Part2Var1(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         QtWidgets.QWidget.__init__(self, parent)
#         self.window = None
#         self.ui_form = Ui_Zadanie1_2_3_part2_var1()
#         self.ui_form.setupUi(self)
#         self.set_default_vals()
#         self.ui_form.pushButton.clicked.connect(self.get_text)
#
#     def set_default_vals(self):
#         self.ui_form.checkBox_zadan1_part2_var1_4.setChecked(True)
#         self.ui_form.checkBox_zadan2_part2_var1_8.setChecked(True)
#         self.ui_form.lineEdit_18.setText('11')
#         self.ui_form.lineEdit_19.setText('12')
#         self.ui_form.lineEdit_20.setText('10')
#         self.ui_form.lineEdit_21.setText('17 18')
#         self.ui_form.lineEdit_22.setText('18')
#         self.ui_form.lineEdit_23.setText('13')
#         self.ui_form.lineEdit_24.setText('22')
#         self.ui_form.lineEdit_25.setText('23')
#         self.ui_form.lineEdit_26.setText('30')
#         self.ui_form.lineEdit_27.setText('32')
#         self.ui_form.lineEdit_28.setText('40')
#         self.ui_form.lineEdit_29.setText('44')
#         self.ui_form.lineEdit_30.setText('46')
#         self.ui_form.lineEdit_31.setText('47')
#         self.ui_form.lineEdit_32.setText('53')
#         self.ui_form.lineEdit_33.setText('51')
#         self.ui_form.lineEdit_34.setText('52')
#
#     def main_select(self, user_name):
#         vals1 = []
#         con = sql.connect('../data.db')
#         cur = con.cursor()
#         answer = cur.execute(
#             f"select answer_user from zadanie_variant where num_zadanie=1 and user_name='{user_name}' "
#             f"and num_part=2 and variant=1")
#         for el in answer:
#             vals1.append(el)
#         val = vals1[0][0].split(';')
#         self.update_cells_1(val)
#         con.commit()
#         cur.close()
#         con.close()
#
#         vals2 = []
#         con = sql.connect('../data.db')
#         cur = con.cursor()
#         answer = cur.execute(
#             f"select answer_user from zadanie_variant where num_zadanie=2 and user_name='{user_name}' "
#             f"and num_part=2 and variant=1")
#         for el in answer:
#             vals2.append(el)
#         val = vals2[0][0].split(';')
#         self.update_cells_2(val)
#         con.commit()
#         cur.close()
#         con.close()
#
#         vals3 = []
#         con = sql.connect('../data.db')
#         cur = con.cursor()
#         answer = cur.execute(
#             f"select answer_user from zadanie_variant where num_zadanie=3 and user_name='{user_name}' "
#             f"and num_part=2 and variant=1")
#         for el in answer:
#             vals3.append(el)
#         val = vals3[0][0].split(';')
#         self.update_cells_3(val)
#         con.commit()
#         cur.close()
#         con.close()
#
#     def update_cells_1(self, val):
#         if val[0] == 'True':
#             self.ui_form.checkBox_zadan1_part2_var1.setChecked(True)
#         if val[1] == 'True':
#             self.ui_form.checkBox_2_zadan1_part2_var1.setChecked(True)
#         if val[2] == 'True':
#             self.ui_form.checkBox_3_zadan1_part2_var1.setChecked(True)
#         self.check_values()
#
#     def update_cells_2(self, val):
#         if val[0] == 'True':
#             self.ui_form.checkBox_zadan2_part2_var1.setChecked(True)
#         if val[1] == 'True':
#             self.ui_form.checkBox_zadan2_part2_var1_2.setChecked(True)
#         if val[2] == 'True':
#             self.ui_form.checkBox_zadan2_part2_var1_3.setChecked(True)
#         if val[3] == 'True':
#             self.ui_form.checkBox_zadan2_part2_var1_4.setChecked(True)
#         self.check_values()
#
#     def update_cells_3(self, val):
#         self.ui_form.lineEdit.setText(val[0])
#         self.ui_form.lineEdit_2.setText(val[1])
#         self.ui_form.lineEdit_3.setText(val[2])
#         self.ui_form.lineEdit_4.setText(val[3])
#         self.ui_form.lineEdit_5.setText(val[4])
#         self.ui_form.lineEdit_6.setText(val[5])
#         self.ui_form.lineEdit_7.setText(val[6])
#         self.ui_form.lineEdit_8.setText(val[7])
#         self.ui_form.lineEdit_9.setText(val[8])
#         self.ui_form.lineEdit_10.setText(val[9])
#         self.ui_form.lineEdit_11.setText(val[10])
#         self.ui_form.lineEdit_12.setText(val[11])
#         self.ui_form.lineEdit_13.setText(val[12])
#         self.ui_form.lineEdit_14.setText(val[13])
#         self.ui_form.lineEdit_15.setText(val[14])
#         self.ui_form.lineEdit_16.setText(val[15])
#         self.ui_form.lineEdit_17.setText(val[16])
#         self.check_values()
#
#     def check_values(self):
#         if self.ui_form.lineEdit.text() != self.ui_form.lineEdit_18.text():
#             self.ui_form.lineEdit.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_2.text() != self.ui_form.lineEdit_19.text():
#             self.ui_form.lineEdit_2.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_3.text() != self.ui_form.lineEdit_20.text():
#             self.ui_form.lineEdit_3.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_4.text() != '17 18':
#             self.ui_form.lineEdit_4.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_5.text() != self.ui_form.lineEdit_22.text():
#             self.ui_form.lineEdit_5.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_6.text() != self.ui_form.lineEdit_23.text():
#             self.ui_form.lineEdit_6.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_7.text() != self.ui_form.lineEdit_24.text():
#             self.ui_form.lineEdit_7.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_8.text() != self.ui_form.lineEdit_25.text():
#             self.ui_form.lineEdit_8.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_9.text() != self.ui_form.lineEdit_26.text():
#             self.ui_form.lineEdit_9.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_10.text() != self.ui_form.lineEdit_27.text():
#             self.ui_form.lineEdit_10.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_11.text() != self.ui_form.lineEdit_28.text():
#             self.ui_form.lineEdit_11.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_12.text() != self.ui_form.lineEdit_29.text():
#             self.ui_form.lineEdit_12.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_13.text() != self.ui_form.lineEdit_30.text():
#             self.ui_form.lineEdit_13.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_14.text() != self.ui_form.lineEdit_31.text():
#             self.ui_form.lineEdit_14.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_15.text() != self.ui_form.lineEdit_32.text():
#             self.ui_form.lineEdit_15.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_16.text() != self.ui_form.lineEdit_33.text():
#             self.ui_form.lineEdit_16.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_17.text() != self.ui_form.lineEdit_34.text():
#             self.ui_form.lineEdit_17.setStyleSheet("QLineEdit {background-color: red;}")
#
#     def get_text(self):
#         self.window = Window(filename='var_1_text2.htm')
#         self.window.show()
#
#
# class Task4Part2Var1(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         QtWidgets.QWidget.__init__(self, parent)
#         self.window = None
#         self.ui_form = Ui_Zadanie4_part2_var1()
#         self.ui_form.setupUi(self)
#         self.set_default_vals()
#         self.ui_form.pushButton_show_text.clicked.connect(self.get_text)
#
#     def set_default_vals(self):
#         self.ui_form.lineEdit_4.setText('10')
#         self.ui_form.lineEdit_5.setText('28')
#         self.ui_form.lineEdit_6.setText('11')
#
#     def main_select(self, user_name):
#         vals = []
#         con = sql.connect('../data.db')
#         cur = con.cursor()
#         answer = cur.execute(
#             f"select answer_user from zadanie_variant where num_zadanie=4 and user_name='{user_name}' "
#             f"and num_part=2 and variant=1")
#         for el in answer:
#             vals.append(el)
#         val = vals[0][0].split(';')
#         self.update_cells(val)
#         con.commit()
#         cur.close()
#         con.close()
#         return vals
#
#     def update_cells(self, val):
#         self.ui_form.lineEdit.setText(val[0])
#         self.ui_form.lineEdit_2.setText(val[1])
#         self.ui_form.lineEdit_3.setText(val[2])
#         self.check_values()
#
#     def check_values(self):
#         if self.ui_form.lineEdit.text() != self.ui_form.lineEdit_4.text():
#             self.ui_form.lineEdit.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_2.text() != self.ui_form.lineEdit_5.text():
#             self.ui_form.lineEdit_2.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_3.text() != self.ui_form.lineEdit_6.text():
#             self.ui_form.lineEdit_3.setStyleSheet("QLineEdit {background-color: red;}")
#
#     def get_text(self):
#         self.window = Window(filename='var_1_text2.htm')
#         self.window.show()
#
#
# class Task5Part2Var1(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         QtWidgets.QWidget.__init__(self, parent)
#         self.window = None
#         self.ui_form = Ui_Zadanie5_part2_var1()
#         self.ui_form.setupUi(self)
#         self.set_default_vals()
#
#     def set_default_vals(self):
#         self.ui_form.lineEdit_answer_6.setText('7')
#         self.ui_form.lineEdit_answer_7.setText('1')
#         self.ui_form.lineEdit_answer_8.setText('3')
#         self.ui_form.lineEdit_answer_9.setText('5')
#         self.ui_form.lineEdit_answer_10.setText('4')
#
#     def main_select(self, user_name):
#         vals = []
#         con = sql.connect('../data.db')
#         cur = con.cursor()
#         answer = cur.execute(
#             f"select answer_user from zadanie_variant where num_zadanie=5 and user_name='{user_name}' "
#             f"and num_part=2 and variant=1")
#         for el in answer:
#             vals.append(el)
#         val = vals[0][0].split(';')
#         self.update_cells(val)
#         con.commit()
#         cur.close()
#         con.close()
#         return vals
#
#     def update_cells(self, val):
#         self.ui_form.lineEdit_answer_1.setText(val[0])
#         self.ui_form.lineEdit_answer_2.setText(val[1])
#         self.ui_form.lineEdit_answer_3.setText(val[2])
#         self.ui_form.lineEdit_answer_4.setText(val[3])
#         self.ui_form.lineEdit_answer_5.setText(val[4])
#         self.check_values()
#
#     def check_values(self):
#         if self.ui_form.lineEdit_answer_1.text() != self.ui_form.lineEdit_answer_6.text():
#             self.ui_form.lineEdit_answer_1.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_answer_2.text() != self.ui_form.lineEdit_answer_7.text():
#             self.ui_form.lineEdit_answer_2.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_answer_3.text() != self.ui_form.lineEdit_answer_8.text():
#             self.ui_form.lineEdit_answer_3.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_answer_4.text() != self.ui_form.lineEdit_answer_9.text():
#             self.ui_form.lineEdit_answer_4.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_answer_5.text() != self.ui_form.lineEdit_answer_10.text():
#             self.ui_form.lineEdit_answer_5.setStyleSheet("QLineEdit {background-color: red;}")
#
#
# class Task6Part2Var1(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         QtWidgets.QWidget.__init__(self, parent)
#         self.window = None
#         self.ui_form = Ui_Zadanie6_part2_var1()
#         self.ui_form.setupUi(self)
#         self.set_default_vals()
#
#     def set_default_vals(self):
#         self.ui_form.lineEdit_answer_11.setText('6')
#         self.ui_form.lineEdit_answer_12.setText('9')
#         self.ui_form.lineEdit_answer_13.setText('1')
#         self.ui_form.lineEdit_answer_14.setText('10')
#         self.ui_form.lineEdit_answer_15.setText('3')
#         self.ui_form.lineEdit_answer_16.setText('2')
#         self.ui_form.lineEdit_answer_17.setText('5')
#         self.ui_form.lineEdit_answer_18.setText('4')
#         self.ui_form.lineEdit_answer_19.setText('7')
#         self.ui_form.lineEdit_answer_20.setText('8')
#
#     def main_select(self, user_name):
#         vals = []
#         con = sql.connect('../data.db')
#         cur = con.cursor()
#         answer = cur.execute(
#             f"select answer_user from zadanie_variant where num_zadanie=6 and user_name='{user_name}' "
#             f"and num_part=2 and variant=1")
#         for el in answer:
#             vals.append(el)
#         val = vals[0][0].split(';')
#         self.update_cells(val)
#         con.commit()
#         cur.close()
#         con.close()
#         return vals
#
#     def update_cells(self, val):
#         self.ui_form.lineEdit_answer_1.setText(val[0])
#         self.ui_form.lineEdit_answer_2.setText(val[1])
#         self.ui_form.lineEdit_answer_3.setText(val[2])
#         self.ui_form.lineEdit_answer_4.setText(val[3])
#         self.ui_form.lineEdit_answer_5.setText(val[4])
#         self.ui_form.lineEdit_answer_6.setText(val[5])
#         self.ui_form.lineEdit_answer_7.setText(val[6])
#         self.ui_form.lineEdit_answer_8.setText(val[7])
#         self.ui_form.lineEdit_answer_9.setText(val[8])
#         self.ui_form.lineEdit_answer_10.setText(val[9])
#         self.check_values()
#
#     def check_values(self):
#         if self.ui_form.lineEdit_answer_1.text() != self.ui_form.lineEdit_answer_11.text():
#             self.ui_form.lineEdit_answer_1.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_answer_2.text() != self.ui_form.lineEdit_answer_12.text():
#             self.ui_form.lineEdit_answer_2.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_answer_3.text() != self.ui_form.lineEdit_answer_13.text():
#             self.ui_form.lineEdit_answer_3.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_answer_4.text() != self.ui_form.lineEdit_answer_14.text():
#             self.ui_form.lineEdit_answer_4.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_answer_5.text() != self.ui_form.lineEdit_answer_15.text():
#             self.ui_form.lineEdit_answer_5.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_answer_6.text() != self.ui_form.lineEdit_answer_16.text():
#             self.ui_form.lineEdit_answer_6.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_answer_7.text() != self.ui_form.lineEdit_answer_17.text():
#             self.ui_form.lineEdit_answer_7.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_answer_8.text() != self.ui_form.lineEdit_answer_18.text():
#             self.ui_form.lineEdit_answer_8.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_answer_9.text() != self.ui_form.lineEdit_answer_19.text():
#             self.ui_form.lineEdit_answer_9.setStyleSheet("QLineEdit {background-color: red;}")
#         if self.ui_form.lineEdit_answer_10.text() != self.ui_form.lineEdit_answer_20.text():
#             self.ui_form.lineEdit_answer_10.setStyleSheet("QLineEdit {background-color: red;}")
