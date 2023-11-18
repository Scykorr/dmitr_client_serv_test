import time

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox

from GUIpy.variant_1.zadanie1_part1_var1 import Ui_Zadanie1_part1
from GUIpy.variant_1.zadanie2_part1_var1 import Ui_Zadanie2_part1
from GUIpy.variant_1.zadanie3_4_5_part1_var1 import Ui_Zadanie3_4_5_part1_var1
from GUIpy.variant_1.zadanie1_2_3_part2_var1 import Ui_Zadanie1_2_3_part2_var1
from GUIpy.variant_1.zadanie4_part2_var1 import Ui_Zadanie4_part2_var1
from GUIpy.variant_1.zadanie5_part2_var1 import Ui_Zadanie5_part2_var1
from GUIpy.variant_1.zadanie6_part1_var1 import Ui_Zadanie6_part1_var1
from GUIpy.variant_1.zadanie6_part2_var1 import Ui_Zadanie6_part2_var1
from GUIpy.variant_1.zadanie7_part1_var1 import Ui_Zadanie7_part1_var1
from GUIpy.variant_1.zadanie8_part1_var1 import Ui_Zadanie8_part1_var1
from client.users import Client
from open_html_function import Window
from random import shuffle
from threads import MyThreadVariant


class Task1Part1Var1(QtWidgets.QWidget):
    def __init__(self, ip_address_server, user_name=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        if user_name is None:
            user_name = []
        self.user_name = user_name
        self.ip_address_server = ip_address_server
        self.window = None
        self.ui_form = Ui_Zadanie1_part1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)
        self.student_fio = user_name[0]
        self.mythread = MyThreadVariant()
        self.on_clicked()
        self.mythread.started.connect(self.on_started)
        self.mythread.finished.connect(self.on_finished)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)
        self.next_time = 0

    def get_next_task(self):
        self.window = Task2Part1Var1(ip_address_server=self.ip_address_server, user_name=self.user_name,
                                     next_time=self.next_time)
        self.answer_append()
        self.close()
        self.window.show()

    def on_clicked(self):
        self.mythread.start()

    def on_started(self):
        self.ui_first_test.label_timer.setText("")

    def on_finished(self):
        self.next_time = 2400 - int(self.mythread.result_time[0])
        self.mythread.exit()

    def on_change(self, s):
        self.ui_form.label_timer.setText(s)

    def answer(self):
        answer = ("{word1};{word2};{word3};{word4};{word5};{word6};{word7};{word8};{word9};{word10};{word11};"
                  "{word12};{word13};{word14};{word15};{word16};{word17};{word18};{word19};{word20};{word21};").format(
            word1=self.ui_form.lineEdit_word_1,
            word2=self.ui_form.lineEdit_word_2,
            word3=self.ui_form.lineEdit_word_3,
            word4=self.ui_form.lineEdit_word_4,
            word5=self.ui_form.lineEdit_word_5,
            word6=self.ui_form.lineEdit_word_6,
            word7=self.ui_form.lineEdit_word_7,
            word8=self.ui_form.lineEdit_word_8,
            word9=self.ui_form.lineEdit_word_9,
            word10=self.ui_form.lineEdit_word_10,
        )
        Client(self.ip_address_server, 7000).connect(
            "insert zadanie_variant set user_name='{user_name}', variant={variant}, num_zadanie={num_zad},"
            " num_part={num_part}, answer_user='{answ_user}'".format(
                user_name=self.student_fio,
                variant=1,
                num_zad=1,
                num_part=1,
                answ_user=None,
            ))
        self.on_finished()

    def answer_append(self):
        Client(self.ip_address_server, 7000).connect(
            "update user set true_answer={0}, current_answer={1} where fio_user='{2}'".format(
                self.right_answer,
                self.counter_questions_result,
                self.student_fio,
            ))


class Task2Part1Var1(QtWidgets.QWidget):
    def __init__(self, ip_address_server, next_time, user_name=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        if user_name is None:
            user_name = []
        self.user_name = user_name
        self.ip_address_server = ip_address_server
        self.window = None
        self.ui_form = Ui_Zadanie2_part1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)
        self.next_time = next_time

    def get_next_task(self):
        self.window = Task345Part1Var1(ip_address_server=self.ip_address_server, user_name=self.user_name)
        self.close()
        self.window.show()


class Task345Part1Var1(QtWidgets.QWidget):
    def __init__(self, ip_address_server, user_name=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        if user_name is None:
            user_name = []
        self.user_name = user_name
        self.ip_address_server = ip_address_server
        self.window = None
        self.ui_form = Ui_Zadanie3_4_5_part1_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)
        self.ui_form.pushButton.clicked.connect(self.get_text)

    def get_text(self):
        self.window = Window(filename='var_1_text1.htm')
        self.window.show()

    def get_next_task(self):
        self.window = Task6Part1Var1(ip_address_server=self.ip_address_server, user_name=self.user_name)
        self.close()
        self.window.show()


class Task6Part1Var1(QtWidgets.QWidget):

    def __init__(self, ip_address_server, user_name=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        if user_name is None:
            user_name = []
        self.user_name = user_name
        self.ip_address_server = ip_address_server
        self.window = None
        self.ui_form = Ui_Zadanie6_part1_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)
        self.words_dict = {'including': 'containing', 'components': 'elements', 'figures': 'symbols',
                           'limited': 'restricted', 'determined': 'defined', 'using': 'employing',
                           'relationship': 'correlation', 'flowing': 'streaming',
                           'usually': 'commonly', 'decrease': 'reduce', 'permit': 'allow', 'wire': 'cable',
                           'measure': 'evaluate', 'insulator': 'dielectric', 'advantage': 'benefit'}
        self.get_right_random_value()

    def get_right_random_value(self):
        values = list(self.words_dict.values())
        shuffle(values)
        self.ui_form.label_word_29.setText(values[0])
        self.ui_form.label_word_30.setText(values[1])
        self.ui_form.label_word_23.setText(values[2])
        self.ui_form.label_word_17.setText(values[3])
        self.ui_form.label_word_26.setText(values[4])
        self.ui_form.label_word_24.setText(values[5])
        self.ui_form.label_word_20.setText(values[6])
        self.ui_form.label_word_21.setText(values[7])
        self.ui_form.label_word_18.setText(values[8])
        self.ui_form.label_word_16.setText(values[9])
        self.ui_form.label_word_22.setText(values[10])
        self.ui_form.label_word_27.setText(values[11])
        self.ui_form.label_word_28.setText(values[12])
        self.ui_form.label_word_25.setText(values[13])
        self.ui_form.label_word_19.setText(values[14])

    def get_next_task(self):
        self.window = Task7Part1Var1(ip_address_server=self.ip_address_server, user_name=self.user_name)
        self.close()
        self.window.show()


class Task7Part1Var1(QtWidgets.QWidget):
    def __init__(self, ip_address_server, user_name=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        if user_name is None:
            user_name = []
        self.user_name = user_name
        self.ip_address_server = ip_address_server
        self.window = None
        self.ui_form = Ui_Zadanie7_part1_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)

    def get_next_task(self):
        self.window = Task8Part1Var1(ip_address_server=self.ip_address_server, user_name=self.user_name)
        self.close()
        self.window.show()


class Task8Part1Var1(QtWidgets.QWidget):
    def __init__(self, ip_address_server, user_name=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        if user_name is None:
            user_name = []
        self.user_name = user_name
        self.ip_address_server = ip_address_server
        self.window = None
        self.ui_form = Ui_Zadanie8_part1_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)

    def get_next_task(self):
        self.window = Task123Part2Var1(ip_address_server=self.ip_address_server, user_name=self.user_name)
        self.close()
        self.window.show()


class Task123Part2Var1(QtWidgets.QWidget):
    def __init__(self, ip_address_server, user_name=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        if user_name is None:
            user_name = []
        self.user_name = user_name
        self.ip_address_server = ip_address_server
        self.window = None
        self.ui_form = Ui_Zadanie1_2_3_part2_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)
        self.ui_form.pushButton.clicked.connect(self.get_text)

    def get_text(self):
        self.window = Window(filename='var_1_text2.htm')
        self.window.show()

    def get_next_task(self):
        self.window = Task4Part2Var1(ip_address_server=self.ip_address_server, user_name=self.user_name)
        self.close()
        self.window.show()


class Task4Part2Var1(QtWidgets.QWidget):
    def __init__(self, ip_address_server, user_name=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        if user_name is None:
            user_name = []
        self.user_name = user_name
        self.ip_address_server = ip_address_server
        self.window = None
        self.ui_form = Ui_Zadanie4_part2_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)
        self.ui_form.pushButton_show_text.clicked.connect(self.get_text)

    def get_text(self):
        self.window = Window(filename='var_1_text2.htm')
        self.window.show()

    def get_next_task(self):
        self.window = Task5Part2Var1(ip_address_server=self.ip_address_server, user_name=self.user_name)
        self.close()
        self.window.show()


class Task5Part2Var1(QtWidgets.QWidget):
    def __init__(self, ip_address_server, user_name=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        if user_name is None:
            user_name = []
        self.user_name = user_name
        self.student_fio = user_name[0]
        self.ip_address_server = ip_address_server
        self.window = None
        self.ui_form = Ui_Zadanie5_part2_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)

    def get_next_task(self):
        self.window = Task6Part2Var1(ip_address_server=self.ip_address_server, user_name=self.user_name)
        self.close()
        self.window.show()


class Task6Part2Var1(QtWidgets.QWidget):
    def __init__(self, ip_address_server, user_name=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        if user_name is None:
            user_name = []
        self.user_name = user_name
        self.ip_address_server = ip_address_server
        self.window = None
        self.ui_form = Ui_Zadanie6_part2_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)

    def get_next_task(self):
        self.close()
