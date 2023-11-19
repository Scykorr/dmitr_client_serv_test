from PyQt5 import QtWidgets, QtCore
from GUIpy.variant_2.zadanie1_2_3_part2_var2 import Ui_Zadanie1_2_3_part2_var1
from GUIpy.variant_2.zadanie1_part1_var2 import Ui_Zadanie1_part1
from GUIpy.variant_2.zadanie2_part1_var2 import Ui_Zadanie2_part1
from GUIpy.variant_2.zadanie3_4_5_part1_var2 import Ui_Zadanie3_4_5_part1_var1
from GUIpy.variant_2.zadanie4_part2_var2 import Ui_Zadanie4_part2_var1
from GUIpy.variant_2.zadanie5_part2_var2 import Ui_Zadanie5_part2_var1
from GUIpy.variant_2.zadanie6_part1_var2 import Ui_Zadanie6_part1_var1
from GUIpy.variant_2.zadanie6_part2_var2 import Ui_Zadanie6_part2_var1
from GUIpy.variant_2.zadanie7_part1_var2 import Ui_Zadanie7_part1_var1
from GUIpy.variant_2.zadanie8_part1_var2 import Ui_Zadanie8_part1_var1
from client.threads import MyThreadVariant
from client.users import Client
from open_html_function import Window
from random import shuffle


class Task1Part1Var2(QtWidgets.QWidget):
    def __init__(self, ip_address_server, user_name=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
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
        if user_name is None:
            user_name = []
        self.user_name = user_name
        self.ip_address_server = ip_address_server

    def on_clicked(self):
        self.mythread.start()

    def on_started(self):
        self.ui_form.label_timer.setText("")

    def on_finished(self):
        self.next_time = 2400 - int(self.mythread.result_time[0])
        self.mythread.exit()

    def on_change(self, s):
        self.ui_form.label_timer.setText(s)

    def answer(self):
        answer = ("{word1};{word2};{word3};{word4};{word5};{word6};{word7};{word8};{word9};{word10};{word11};"
                  "{word12};{word13};{word14};{word15};{word16};{word17};{word18};{word19};{word20};{word21}").format(
            word1=self.ui_form.lineEdit_word_1.text(),
            word2=self.ui_form.lineEdit_word_2.text(),
            word3=self.ui_form.lineEdit_word_3.text(),
            word4=self.ui_form.lineEdit_word_4.text(),
            word5=self.ui_form.lineEdit_word_5.text(),
            word6=self.ui_form.lineEdit_word_6.text(),
            word7=self.ui_form.lineEdit_word_7.text(),
            word8=self.ui_form.lineEdit_word_8.text(),
            word9=self.ui_form.lineEdit_word_9.text(),
            word10=self.ui_form.lineEdit_word_10.text(),
            word11=self.ui_form.lineEdit_word_11.text(),
            word12=self.ui_form.lineEdit_word_12.text(),
            word13=self.ui_form.lineEdit_word_13.text(),
            word14=self.ui_form.lineEdit_word_14.text(),
            word15=self.ui_form.lineEdit_word_15.text(),
            word16=self.ui_form.lineEdit_word_16.text(),
            word17=self.ui_form.lineEdit_word_17.text(),
            word18=self.ui_form.lineEdit_word_18.text(),
            word19=self.ui_form.lineEdit_word_19.text(),
            word20=self.ui_form.lineEdit_word_20.text(),
            word21=self.ui_form.lineEdit_word_21.text(),
        )
        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}')".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=1,
                num_part=1,
                answ_user=answer,
            ))
        self.on_finished()

    def get_next_task(self):
        self.window = Task2Part1Var2(ip_address_server=self.ip_address_server, user_name=self.user_name,
                                     next_time=self.next_time)
        self.answer()
        self.close()
        self.window.show()


class Task2Part1Var2(QtWidgets.QWidget):
    def __init__(self, ip_address_server, next_time, user_name=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie2_part1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)
        if user_name is None:
            user_name = []
        self.user_name = user_name
        self.ip_address_server = ip_address_server
        self.next_time = next_time
        self.mythread = MyThreadVariant(curr_time=next_time)
        self.on_clicked()
        self.mythread.started.connect(self.on_started)
        self.mythread.finished.connect(self.on_finished)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)
        self.student_fio = user_name[0]

    def on_clicked(self):
        self.mythread.start()

    def on_started(self):
        self.ui_form.label_timer.setText("")

    def on_finished(self):
        self.next_time = 2400 - int(self.mythread.result_time[0])
        self.mythread.exit()

    def on_change(self, s):
        self.ui_form.label_timer.setText(s)

    def answer(self):
        answer = ("{word1};{word2};{word3};{word4};{word5};{word6};{word7};{word8};{word9};{word10};{word11};"
                  "{word12};{word13};{word14};{word15};{word16}").format(
            word1=self.ui_form.lineEdit_answer_1.text(),
            word2=self.ui_form.lineEdit_answer_2.text(),
            word3=self.ui_form.lineEdit_answer_3.text(),
            word4=self.ui_form.lineEdit_answer_4.text(),
            word5=self.ui_form.lineEdit_answer_5.text(),
            word6=self.ui_form.lineEdit_answer_6.text(),
            word7=self.ui_form.lineEdit_answer_7.text(),
            word8=self.ui_form.lineEdit_answer_8.text(),
            word9=self.ui_form.lineEdit_answer_9.text(),
            word10=self.ui_form.lineEdit_answer_10.text(),
            word11=self.ui_form.lineEdit_answer_11.text(),
            word12=self.ui_form.lineEdit_answer_12.text(),
            word13=self.ui_form.lineEdit_answer_13.text(),
            word14=self.ui_form.lineEdit_answer_14.text(),
            word15=self.ui_form.lineEdit_answer_15.text(),
            word16=self.ui_form.lineEdit_answer_16.text(),
        )
        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}')".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=2,
                num_part=1,
                answ_user=answer,
            ))
        self.on_finished()

    def get_next_task(self):
        self.window = Task345Part1Var2(ip_address_server=self.ip_address_server, user_name=self.user_name,
                                       next_time=self.next_time)
        self.answer()
        self.close()
        self.window.show()


class Task345Part1Var2(QtWidgets.QWidget):
    def __init__(self, ip_address_server, next_time, user_name=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie3_4_5_part1_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)
        self.ui_form.pushButton.clicked.connect(self.get_text)
        if user_name is None:
            user_name = []
        self.user_name = user_name
        self.ip_address_server = ip_address_server
        self.next_time = next_time
        self.mythread = MyThreadVariant(curr_time=next_time)
        self.on_clicked()
        self.mythread.started.connect(self.on_started)
        self.mythread.finished.connect(self.on_finished)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)
        self.student_fio = user_name[0]

    def on_clicked(self):
        self.mythread.start()

    def on_started(self):
        self.ui_form.label_timer.setText("")

    def on_finished(self):
        self.next_time = 2400 - int(self.mythread.result_time[0])
        self.mythread.exit()

    def on_change(self, s):
        self.ui_form.label_timer.setText(s)

    def answer(self):
        word1 = ';'.join(self.ui_form.lineEdit_zadanie4.text().split())
        answer = "{word1}".format(
            word1=word1,
        )
        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}')".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=4,
                num_part=1,
                answ_user=answer,
            ))

        answer_second = ("{word1};{word2};{word3};{word4};{word5};{word6};{word7};{word8};{word9};{word10};{word11};"
                         "{word12};{word13};{word14};{word15}").format(
            word1=self.ui_form.lineEdit_zadane5_1.text(),
            word2=self.ui_form.lineEdit_zadane5_2.text(),
            word3=self.ui_form.lineEdit_zadane5_3.text(),
            word4=self.ui_form.lineEdit_zadane5_4.text(),
            word5=self.ui_form.lineEdit_zadane5_5.text(),
            word6=self.ui_form.lineEdit_zadane5_6.text(),
            word7=self.ui_form.lineEdit_zadane5_7.text(),
            word8=self.ui_form.lineEdit_zadane5_8.text(),
            word9=self.ui_form.lineEdit_zadane5_9.text(),
            word10=self.ui_form.lineEdit_zadane5_10.text(),
            word11=self.ui_form.lineEdit_zadane5_11.text(),
            word12=self.ui_form.lineEdit_zadane5_12.text(),
            word13=self.ui_form.lineEdit_zadane5_13.text(),
            word14=self.ui_form.lineEdit_zadane5_14.text(),
            word15=self.ui_form.lineEdit_zadane5_15.text(),
        )
        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}')".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=5,
                num_part=1,
                answ_user=answer_second,
            ))
        self.on_finished()

    def get_text(self):
        self.window = Window(filename='var_2_text1.htm')
        self.window.show()

    def get_next_task(self):
        self.window = Task6Part1Var2(ip_address_server=self.ip_address_server, user_name=self.user_name,
                                     next_time=self.next_time)
        self.answer()
        self.close()
        self.window.show()


class Task6Part1Var2(QtWidgets.QWidget):
    def __init__(self, ip_address_server, next_time, user_name=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie6_part1_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)
        self.words_dict = {'comprise': 'include', 'element': 'component', 'usually': 'typically', 'feature': 'property',
                           'several': 'the number of', 'main': 'primary', 'different': 'varous',
                           'creating': 'producing', 'through': 'over', 'used': 'applied', 'probable': 'possible',
                           'evaluate': 'calculate', 'isolated': 'separated', 'rapidly': 'quickly',
                           'transformation': 'change', 'nearly': 'approximately'}
        self.get_right_random_value()
        if user_name is None:
            user_name = []
        self.user_name = user_name
        self.ip_address_server = ip_address_server
        self.next_time = next_time
        self.mythread = MyThreadVariant(curr_time=next_time)
        self.on_clicked()
        self.mythread.started.connect(self.on_started)
        self.mythread.finished.connect(self.on_finished)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)
        self.student_fio = user_name[0]

    def on_clicked(self):
        self.mythread.start()

    def on_started(self):
        self.ui_form.label_timer.setText("")

    def on_finished(self):
        self.next_time = 2400 - int(self.mythread.result_time[0])
        self.mythread.exit()

    def on_change(self, s):
        self.ui_form.label_timer.setText(s)

    def answer(self):
        answer = ("{word1};{word2};{word3};{word4};{word5};{word6};{word7};{word8};{word9};{word10};{word11};"
                  "{word12};{word13};{word14};{word15};{word16}").format(
            word1=f'{self.ui_form.lineEdit_answer_1.text()},{self.ui_form.label_word_29.text()}',
            word2=f'{self.ui_form.lineEdit_answer_2.text()},{self.ui_form.label_word_30.text()}',
            word3=f'{self.ui_form.lineEdit_answer_3.text()},{self.ui_form.label_word_23.text()}',
            word4=f'{self.ui_form.lineEdit_answer_4.text()},{self.ui_form.label_word_17.text()}',
            word5=f'{self.ui_form.lineEdit_answer_5.text()},{self.ui_form.label_word_26.text()}',
            word6=f'{self.ui_form.lineEdit_answer_6.text()},{self.ui_form.label_word_24.text()}',
            word7=f'{self.ui_form.lineEdit_answer_7.text()},{self.ui_form.label_word_20.text()}',
            word8=f'{self.ui_form.lineEdit_answer_8.text()},{self.ui_form.label_word_21.text()}',
            word9=f'{self.ui_form.lineEdit_answer_9.text()},{self.ui_form.label_word_18.text()}',
            word10=f'{self.ui_form.lineEdit_answer_10.text()},{self.ui_form.label_word_16.text()}',
            word11=f'{self.ui_form.lineEdit_answer_11.text()},{self.ui_form.label_word_22.text()}',
            word12=f'{self.ui_form.lineEdit_answer_12.text()},{self.ui_form.label_word_27.text()}',
            word13=f'{self.ui_form.lineEdit_answer_13.text()},{self.ui_form.label_word_28.text()}',
            word14=f'{self.ui_form.lineEdit_answer_14.text()},{self.ui_form.label_word_25.text()}',
            word15=f'{self.ui_form.lineEdit_answer_15.text()},{self.ui_form.label_word_19.text()}',
            word16=f'{self.ui_form.lineEdit_answer_16.text()},{self.ui_form.label_word_32.text()}',
        )
        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}')".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=6,
                num_part=1,
                answ_user=answer,
            ))
        self.on_finished()

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
        self.ui_form.label_word_32.setText(values[15])

    def get_next_task(self):
        self.window = Task7Part1Var2(ip_address_server=self.ip_address_server, user_name=self.user_name,
                                     next_time=self.next_time)
        self.answer()
        self.close()
        self.window.show()


class Task7Part1Var2(QtWidgets.QWidget):
    def __init__(self, ip_address_server, next_time, user_name=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie7_part1_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)
        if user_name is None:
            user_name = []
        self.user_name = user_name
        self.ip_address_server = ip_address_server
        self.next_time = next_time
        self.mythread = MyThreadVariant(curr_time=next_time)
        self.on_clicked()
        self.mythread.started.connect(self.on_started)
        self.mythread.finished.connect(self.on_finished)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)
        self.student_fio = user_name[0]

    def on_clicked(self):
        self.mythread.start()

    def on_started(self):
        self.ui_form.label_timer.setText("")

    def on_finished(self):
        self.next_time = 2400 - int(self.mythread.result_time[0])
        self.mythread.exit()

    def on_change(self, s):
        self.ui_form.label_timer.setText(s)

    def answer(self):
        answer = "{word1};{word2};{word3};{word4};{word5}".format(
            word1=self.ui_form.lineEdit_answer_1.text(),
            word2=self.ui_form.lineEdit_answer_2.text(),
            word3=self.ui_form.lineEdit_answer_3.text(),
            word4=self.ui_form.lineEdit_answer_4.text(),
            word5=self.ui_form.lineEdit_answer_5.text(),
        )
        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}')".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=7,
                num_part=1,
                answ_user=answer,
            ))
        self.on_finished()

    def get_next_task(self):
        self.window = Task8Part1Var2(ip_address_server=self.ip_address_server, user_name=self.user_name,
                                     next_time=self.next_time)
        self.answer()
        self.close()
        self.window.show()


class Task8Part1Var2(QtWidgets.QWidget):
    def __init__(self, ip_address_server, next_time, user_name=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie8_part1_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)
        if user_name is None:
            user_name = []
        self.user_name = user_name
        self.ip_address_server = ip_address_server
        self.next_time = next_time
        self.mythread = MyThreadVariant(curr_time=next_time)
        self.on_clicked()
        self.mythread.started.connect(self.on_started)
        self.mythread.finished.connect(self.on_finished)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)
        self.student_fio = user_name[0]

    def on_clicked(self):
        self.mythread.start()

    def on_started(self):
        self.ui_form.label_timer.setText("")

    def on_finished(self):
        self.next_time = 2400 - int(self.mythread.result_time[0])
        self.mythread.exit()

    def on_change(self, s):
        self.ui_form.label_timer.setText(s)

    def answer(self):
        answer = "{word1};{word2};{word3};{word4};{word5};{word6};{word7};{word8};{word9};{word10}".format(
            word1=self.ui_form.lineEdit_answer_1.text(),
            word2=self.ui_form.lineEdit_answer_2.text(),
            word3=self.ui_form.lineEdit_answer_3.text(),
            word4=self.ui_form.lineEdit_answer_4.text(),
            word5=self.ui_form.lineEdit_answer_5.text(),
            word6=self.ui_form.lineEdit_answer_6.text(),
            word7=self.ui_form.lineEdit_answer_7.text(),
            word8=self.ui_form.lineEdit_answer_8.text(),
            word9=self.ui_form.lineEdit_answer_9.text(),
            word10=self.ui_form.lineEdit_answer_10.text(),
        )
        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}')".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=8,
                num_part=1,
                answ_user=answer,
            ))
        self.on_finished()

    def get_next_task(self):
        self.window = Task123Part2Var2(ip_address_server=self.ip_address_server, user_name=self.user_name,
                                       next_time=self.next_time)
        self.answer()
        self.close()
        self.window.show()


class Task123Part2Var2(QtWidgets.QWidget):
    def __init__(self, ip_address_server, next_time, user_name=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie1_2_3_part2_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)
        self.ui_form.pushButton.clicked.connect(self.get_text)
        if user_name is None:
            user_name = []
        self.user_name = user_name
        self.ip_address_server = ip_address_server
        self.next_time = next_time
        self.mythread = MyThreadVariant(curr_time=next_time)
        self.on_clicked()
        self.mythread.started.connect(self.on_started)
        self.mythread.finished.connect(self.on_finished)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)
        self.student_fio = user_name[0]

    def on_clicked(self):
        self.mythread.start()

    def on_started(self):
        self.ui_form.label_timer.setText("")

    def on_finished(self):
        self.next_time = 2400 - int(self.mythread.result_time[0])
        self.mythread.exit()

    def on_change(self, s):
        self.ui_form.label_timer.setText(s)

    def answer(self):
        answer = "{word1};{word2};{word3}".format(
            word1=self.ui_form.checkBox_zadan1_part2_var1.isChecked(),
            word2=self.ui_form.checkBox_2_zadan1_part2_var1.isChecked(),
            word3=self.ui_form.checkBox_3_zadan1_part2_var1.isChecked(),
        )
        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}')".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=1,
                num_part=2,
                answ_user=answer,
            ))

        answer_2 = "{word1};{word2};{word3};{word4}".format(
            word1=self.ui_form.checkBox_zadan2_part2_var1.isChecked(),
            word2=self.ui_form.checkBox_zadan2_part2_var1_2.isChecked(),
            word3=self.ui_form.checkBox_zadan2_part2_var1_3.isChecked(),
            word4=self.ui_form.checkBox_zadan2_part2_var1_4.isChecked(),
        )
        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}')".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=2,
                num_part=2,
                answ_user=answer_2,
            ))

        answer_3 = ("{word1};{word2};{word3};{word4};{word5};{word6};{word7};{word8};{word9};{word10};{word11};"
                    "{word12};{word13};{word14};{word15};{word16};{word17}").format(
            word1=self.ui_form.lineEdit.text(),
            word2=self.ui_form.lineEdit_2.text(),
            word3=self.ui_form.lineEdit_3.text(),
            word4=self.ui_form.lineEdit_4.text(),
            word5=self.ui_form.lineEdit_5.text(),
            word6=self.ui_form.lineEdit_6.text(),
            word7=self.ui_form.lineEdit_7.text(),
            word8=self.ui_form.lineEdit_8.text(),
            word9=self.ui_form.lineEdit_9.text(),
            word10=self.ui_form.lineEdit_10.text(),
            word11=self.ui_form.lineEdit_11.text(),
            word12=self.ui_form.lineEdit_12.text(),
            word13=self.ui_form.lineEdit_13.text(),
            word14=self.ui_form.lineEdit_14.text(),
            word15=self.ui_form.lineEdit_15.text(),
            word16=self.ui_form.lineEdit_16.text(),
            word17=self.ui_form.lineEdit_17.text(),
        )
        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}')".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=3,
                num_part=2,
                answ_user=answer_3,
            ))
        self.on_finished()

    def get_text(self):
        self.window = Window(filename='var_2_text2.htm')
        self.window.show()

    def get_next_task(self):
        self.window = Task4Part2Var2(ip_address_server=self.ip_address_server, user_name=self.user_name,
                                     next_time=self.next_time)
        self.answer()
        self.close()
        self.window.show()


class Task4Part2Var2(QtWidgets.QWidget):
    def __init__(self, ip_address_server, next_time, user_name=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie4_part2_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)
        self.ui_form.pushButton_show_text.clicked.connect(self.get_text)
        if user_name is None:
            user_name = []
        self.user_name = user_name
        self.ip_address_server = ip_address_server
        self.next_time = next_time
        self.mythread = MyThreadVariant(curr_time=next_time)
        self.on_clicked()
        self.mythread.started.connect(self.on_started)
        self.mythread.finished.connect(self.on_finished)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)
        self.student_fio = user_name[0]

    def on_clicked(self):
        self.mythread.start()

    def on_started(self):
        self.ui_form.label_timer.setText("")

    def on_finished(self):
        self.next_time = 2400 - int(self.mythread.result_time[0])
        self.mythread.exit()

    def on_change(self, s):
        self.ui_form.label_timer.setText(s)

    def answer(self):
        answer = "{word1};{word2}".format(
            word1=self.ui_form.lineEdit.text(),
            word2=self.ui_form.lineEdit_2.text(),
        )
        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}')".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=4,
                num_part=2,
                answ_user=answer,
            ))
        self.on_finished()

    def get_text(self):
        self.window = Window(filename='var_2_text2.htm')
        self.window.show()

    def get_next_task(self):
        self.window = Task5Part2Var2(ip_address_server=self.ip_address_server, user_name=self.user_name,
                                     next_time=self.next_time)
        self.answer()
        self.close()
        self.window.show()


class Task5Part2Var2(QtWidgets.QWidget):
    def __init__(self, ip_address_server, next_time, user_name=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie5_part2_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)
        if user_name is None:
            user_name = []
        self.user_name = user_name
        self.student_fio = user_name[0]
        self.ip_address_server = ip_address_server
        self.next_time = next_time
        self.mythread = MyThreadVariant(curr_time=next_time)
        self.on_clicked()
        self.mythread.started.connect(self.on_started)
        self.mythread.finished.connect(self.on_finished)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)
        self.student_fio = user_name[0]


    def on_clicked(self):
        self.mythread.start()

    def on_started(self):
        self.ui_form.label_timer.setText("")

    def on_finished(self):
        self.next_time = 2400 - int(self.mythread.result_time[0])
        self.mythread.exit()

    def on_change(self, s):
        self.ui_form.label_timer.setText(s)

    def answer(self):
        answer = "{word1};{word2};{word3}".format(
            word1=self.ui_form.lineEdit_answer_1.text(),
            word2=self.ui_form.lineEdit_answer_2.text(),
            word3=self.ui_form.lineEdit_answer_3.text(),
            word4=self.ui_form.lineEdit_answer_4.text(),
            word5=self.ui_form.lineEdit_answer_5.text(),
        )
        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}')".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=5,
                num_part=2,
                answ_user=answer,
            ))
        self.on_finished()

    def get_next_task(self):
        self.window = Task6Part2Var2(ip_address_server=self.ip_address_server, user_name=self.user_name,
                                     next_time=self.next_time)
        self.answer()
        self.close()
        self.window.show()


class Task6Part2Var2(QtWidgets.QWidget):
    def __init__(self, ip_address_server, next_time, user_name=None, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie6_part2_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)
        if user_name is None:
            user_name = []
        self.user_name = user_name
        self.ip_address_server = ip_address_server
        self.next_time = next_time
        self.mythread = MyThreadVariant(curr_time=next_time)
        self.on_clicked()
        self.mythread.started.connect(self.on_started)
        self.mythread.finished.connect(self.on_finished)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)
        self.student_fio = user_name[0]

    def on_clicked(self):
        self.mythread.start()

    def on_started(self):
        self.ui_form.label_timer.setText("")

    def on_finished(self):
        self.next_time = 2400 - int(self.mythread.result_time[0])
        self.mythread.exit()

    def on_change(self, s):
        self.ui_form.label_timer.setText(s)

    def answer(self):
        answer = "{word1};{word2};{word3};{word4};{word5};{word6};{word7};{word8};{word9};{word10}".format(
            word1=self.ui_form.lineEdit_answer_1.text(),
            word2=self.ui_form.lineEdit_answer_2.text(),
            word3=self.ui_form.lineEdit_answer_3.text(),
            word4=self.ui_form.lineEdit_answer_4.text(),
            word5=self.ui_form.lineEdit_answer_5.text(),
            word6=self.ui_form.lineEdit_answer_6.text(),
            word7=self.ui_form.lineEdit_answer_7.text(),
            word8=self.ui_form.lineEdit_answer_8.text(),
            word9=self.ui_form.lineEdit_answer_9.text(),
            word10=self.ui_form.lineEdit_answer_10.text(),
        )
        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}')".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=6,
                num_part=2,
                answ_user=answer,
            ))
        self.on_finished()

    def get_next_task(self):
        self.answer()
        self.close()
