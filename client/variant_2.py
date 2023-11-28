from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox

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
from threads import MyThreadVariant
from users import Client
from random import shuffle
from main_variant import WindowVariantMain

from test_class_window import Menu


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

        true_answers = 0
        false_answers = 0

        if self.ui_form.lineEdit_word_1.text() == 'накапливать':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_word_2.text() == 'электрический':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_word_3.text() == 'фактор':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_word_4.text() == 'проводник':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_word_5.text() == 'температура':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_word_6.text() == 'активный' or self.ui_form.lineEdit_word_6.text() == 'пассивный':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_word_7.text() == 'физические характеристики':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_word_8.text() == 'электронные компоненты':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_word_9.text() == 'резистор':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_word_10.text() == 'практичный':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_word_11.text() == 'терминал':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_word_12.text() == 'константа':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_word_13.text() == 'материал':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_word_14.text() == 'энергия':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_word_15.text() == 'механизм':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_word_16.text() == 'символ':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_word_17.text() == 'напряжение':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_word_18.text() == 'индикатор':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_word_19.text() == 'инструмент':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_word_20.text() == 'фаза':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_word_21.text() == 'батарея':
            true_answers += 1
        else:
            false_answers += 1

        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user, true_answers, false_answers) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}', {true_answer}, {false_answer})".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=1,
                num_part=1,
                answ_user=answer,
                true_answer=true_answers,
                false_answer=false_answers,
            ))
        self.on_finished()

    def get_next_task(self):
        self.answer()
        self.window = Task2Part1Var2(ip_address_server=self.ip_address_server, user_name=self.user_name,
                                     next_time=self.next_time)
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

        true_answers = 0
        false_answers = 0

        if self.ui_form.lineEdit_answer_1.text() == 'v':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_2.text() == 'adv':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_3.text() == 'n':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_4.text() == 'adj':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_5.text() == 'adv':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_6.text() == 'v':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_7.text() == 'v':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_8.text() == 'v':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_9.text() == 'adj':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_10.text() == 'adj':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_11.text() == 'adj':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_12.text() == 'v':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_13.text() == 'v':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_14.text() == 'adj':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_15.text() == 'adv':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_15.text() == 'n':
            true_answers += 1
        else:
            false_answers += 1

        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user, true_answers, false_answers) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}', {true_answer}, {false_answer})".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=2,
                num_part=1,
                answ_user=answer,
                true_answer=true_answers,
                false_answer=false_answers,
            ))
        self.on_finished()

    def get_next_task(self):
        self.answer()
        self.window = Task345Part1Var2(ip_address_server=self.ip_address_server, user_name=self.user_name,
                                       next_time=self.next_time)
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
        self.num_page_pdf = 0

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

        true_answers_4 = 0
        false_answers_4 = 0

        true_answers = 0
        false_answers = 0

        if self.ui_form.lineEdit_zadanie4.text() == '2 8 25 44 47':
            true_answers_4 += 1
        else:
            false_answers_4 += 1

        if self.ui_form.lineEdit_zadane5_1.text() == '2':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_zadane5_2.text() == '3':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_zadane5_3.text() == '7':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_zadane5_4.text() == '8':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_zadane5_5.text() == '13':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_zadane5_6.text() == '11':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_zadane5_7.text() == '19':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_zadane5_8.text() == '24':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_zadane5_9.text() == '27':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_zadane5_10.text() == '30':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_zadane5_11.text() == '31':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_zadane5_12.text() == '32':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_zadane5_13.text() == '39':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_zadane5_14.text() == '44':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_zadane5_15.text() == '48':
            true_answers += 1
        else:
            false_answers += 1

        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user, true_answers, false_answers) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}', {true_answer}, {false_answer})".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=4,
                num_part=1,
                answ_user=answer,
                true_answer=true_answers_4,
                false_answer=false_answers_4,
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
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user, true_answers, false_answers) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}', {true_answer}, {false_answer})".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=5,
                num_part=1,
                answ_user=answer_second,
                true_answer=true_answers,
                false_answer=false_answers,
            ))
        self.on_finished()

    def get_text(self):
        self.open_text = Menu(
            doc_paths=['img/2_1_1.PNG', 'img/2_1_2.PNG', 'img/2_1_3.PNG', 'img/2_1_4.PNG', 'img/2_1_5.PNG',
                       'img/2_1_6.PNG'])
        self.open_text.show()

    def get_next_task(self):
        self.answer()
        self.window = Task6Part1Var2(ip_address_server=self.ip_address_server, user_name=self.user_name,
                                     next_time=self.next_time)
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

        true_answer_list = ['1,include', '2,component', '3,typically', '4,property', '5,the number of', '6,primary',
                            '7,varous', '8,producing', '9,over', '10,applied', '11,possible', '12,calculate',
                            '13,separated', '14,quickly', '15,change', '16,approximately']

        true_answers = 0
        false_answers = 0

        if f'{self.ui_form.lineEdit_answer_1.text()},{self.ui_form.label_word_29.text()}' in true_answer_list:
            true_answers += 1
        else:
            false_answers += 1
        if f'{self.ui_form.lineEdit_answer_2.text()},{self.ui_form.label_word_30.text()}' in true_answer_list:
            true_answers += 1
        else:
            false_answers += 1
        if f'{self.ui_form.lineEdit_answer_3.text()},{self.ui_form.label_word_23.text()}' in true_answer_list:
            true_answers += 1
        else:
            false_answers += 1
        if f'{self.ui_form.lineEdit_answer_4.text()},{self.ui_form.label_word_17.text()}' in true_answer_list:
            true_answers += 1
        else:
            false_answers += 1
        if f'{self.ui_form.lineEdit_answer_5.text()},{self.ui_form.label_word_26.text()}' in true_answer_list:
            true_answers += 1
        else:
            false_answers += 1
        if f'{self.ui_form.lineEdit_answer_6.text()},{self.ui_form.label_word_24.text()}' in true_answer_list:
            true_answers += 1
        else:
            false_answers += 1
        if f'{self.ui_form.lineEdit_answer_7.text()},{self.ui_form.label_word_20.text()}' in true_answer_list:
            true_answers += 1
        else:
            false_answers += 1
        if f'{self.ui_form.lineEdit_answer_8.text()},{self.ui_form.label_word_21.text()}' in true_answer_list:
            true_answers += 1
        else:
            false_answers += 1
        if f'{self.ui_form.lineEdit_answer_9.text()},{self.ui_form.label_word_18.text()}' in true_answer_list:
            true_answers += 1
        else:
            false_answers += 1
        if f'{self.ui_form.lineEdit_answer_10.text()},{self.ui_form.label_word_16.text()}' in true_answer_list:
            true_answers += 1
        else:
            false_answers += 1
        if f'{self.ui_form.lineEdit_answer_11.text()},{self.ui_form.label_word_22.text()}' in true_answer_list:
            true_answers += 1
        else:
            false_answers += 1
        if f'{self.ui_form.lineEdit_answer_12.text()},{self.ui_form.label_word_27.text()}' in true_answer_list:
            true_answers += 1
        else:
            false_answers += 1
        if f'{self.ui_form.lineEdit_answer_13.text()},{self.ui_form.label_word_28.text()}' in true_answer_list:
            true_answers += 1
        else:
            false_answers += 1
        if f'{self.ui_form.lineEdit_answer_14.text()},{self.ui_form.label_word_25.text()}' in true_answer_list:
            true_answers += 1
        else:
            false_answers += 1
        if f'{self.ui_form.lineEdit_answer_15.text()},{self.ui_form.label_word_19.text()}' in true_answer_list:
            true_answers += 1
        else:
            false_answers += 1
        if f'{self.ui_form.lineEdit_answer_16.text()},{self.ui_form.label_word_20.text()}' in true_answer_list:
            true_answers += 1
        else:
            false_answers += 1

        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user, true_answers, false_answers) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}', {true_answer}, {false_answer})".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=6,
                num_part=1,
                answ_user=answer,
                true_answer=true_answers,
                false_answer=false_answers,
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
        self.answer()
        self.window = Task7Part1Var2(ip_address_server=self.ip_address_server, user_name=self.user_name,
                                     next_time=self.next_time)
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

        true_answers = 0
        false_answers = 0

        if self.ui_form.lineEdit_answer_1.text() == '4':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_2.text() == '7':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_3.text() == '1':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_4.text() == '2':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_5.text() == '6':
            true_answers += 1
        else:
            false_answers += 1

        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user, true_answers, false_answers) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}', {true_answer}, {false_answer})".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=7,
                num_part=1,
                answ_user=answer,
                true_answer=true_answers,
                false_answer=false_answers,
            ))
        self.on_finished()

    def get_next_task(self):
        self.answer()
        self.window = Task8Part1Var2(ip_address_server=self.ip_address_server, user_name=self.user_name,
                                     next_time=self.next_time)
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

        true_answers = 0
        false_answers = 0

        if self.ui_form.lineEdit_answer_1.text() == '5':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_2.text() == '10':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_3.text() == '7':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_4.text() == '9':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_5.text() == '8':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_6.text() == '1':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_7.text() == '4':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_8.text() == '3':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_9.text() == '6':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_10.text() == '2':
            true_answers += 1
        else:
            false_answers += 1

        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user, true_answers, false_answers) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}', {true_answer}, {false_answer})".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=8,
                num_part=1,
                answ_user=answer,
                true_answer=true_answers,
                false_answer=false_answers,
            ))
        self.on_finished()

    def get_next_task(self):
        self.answer()
        self.window = Task123Part2Var2(ip_address_server=self.ip_address_server, user_name=self.user_name,
                                       next_time=self.next_time)
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

        true_answers_1 = 0
        false_answers_1 = 0

        true_answers_2 = 0
        false_answers_2 = 0

        true_answers = 0
        false_answers = 0

        if self.ui_form.checkBox_3_zadan1_part2_var1.isChecked():
            true_answers_1 += 1
        else:
            false_answers_1 += 1

        if self.ui_form.checkBox_zadan2_part2_var1_4.isChecked():
            true_answers_2 += 1
        else:
            false_answers_2 += 1

        if self.ui_form.lineEdit.text() == '1':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_2.text() == '3':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_3.text() == '5':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_4.text() == '7':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_5.text() == '9':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_6.text() == '10':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_7.text() == '11':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_8.text() == '12':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_9.text() == '13':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_10.text() == '14':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_11.text() == '15':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_12.text() == '17':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_13.text() == '22':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_14.text() == '23':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_15.text() == '29':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_16.text() == '36':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_17.text() == '42':
            true_answers += 1
        else:
            false_answers += 1

        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user, true_answers, false_answers) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}', {true_answer}, {false_answer})".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=1,
                num_part=2,
                answ_user=answer,
                true_answer=true_answers_1,
                false_answer=false_answers_1,
            ))

        answer_2 = "{word1};{word2};{word3};{word4}".format(
            word1=self.ui_form.checkBox_zadan2_part2_var1.isChecked(),
            word2=self.ui_form.checkBox_zadan2_part2_var1_2.isChecked(),
            word3=self.ui_form.checkBox_zadan2_part2_var1_3.isChecked(),
            word4=self.ui_form.checkBox_zadan2_part2_var1_4.isChecked(),
        )
        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user, true_answers, false_answers) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}', {true_answer}, {false_answer})".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=2,
                num_part=2,
                answ_user=answer_2,
                true_answer=true_answers_2,
                false_answer=false_answers_2,
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
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user, true_answers, false_answers) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}', {true_answer}, {false_answer})".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=3,
                num_part=2,
                answ_user=answer_3,
                true_answer=true_answers,
                false_answer=false_answers,
            ))
        self.on_finished()

    def get_text(self):
        self.open_text = Menu(
            doc_paths=['img/2_2_1.PNG', 'img/2_2_2.PNG', 'img/2_2_3.PNG', 'img/2_2_4.PNG'])
        self.open_text.show()

    def get_next_task(self):
        self.answer()
        self.window = Task4Part2Var2(ip_address_server=self.ip_address_server, user_name=self.user_name,
                                     next_time=self.next_time)
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

        true_answers = 0
        false_answers = 0

        if self.ui_form.lineEdit.text() == '26':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_2.text() == '1':
            true_answers += 1
        else:
            false_answers += 1

        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user, true_answers, false_answers) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}', {true_answer}, {false_answer})".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=4,
                num_part=2,
                answ_user=answer,
                true_answer=true_answers,
                false_answer=false_answers,
            ))
        self.on_finished()

    def get_text(self):
        self.open_text = Menu(
            doc_paths=['img/2_2_1.PNG', 'img/2_2_2.PNG', 'img/2_2_3.PNG', 'img/2_2_4.PNG'])
        self.open_text.show()

    def get_next_task(self):
        self.answer()
        self.window = Task5Part2Var2(ip_address_server=self.ip_address_server, user_name=self.user_name,
                                     next_time=self.next_time)
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
        answer = "{word1};{word2};{word3};{word4};{word5}".format(
            word1=self.ui_form.lineEdit_answer_1.text(),
            word2=self.ui_form.lineEdit_answer_2.text(),
            word3=self.ui_form.lineEdit_answer_3.text(),
            word4=self.ui_form.lineEdit_answer_4.text(),
            word5=self.ui_form.lineEdit_answer_5.text(),
        )

        true_answers = 0
        false_answers = 0

        if self.ui_form.lineEdit_answer_1.text() == '2':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_2.text() == '7':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_3.text() == '1':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_4.text() == '6':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_5.text() == '2':
            true_answers += 1
        else:
            false_answers += 1

        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user, true_answers, false_answers) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}', {true_answer}, {false_answer})".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=5,
                num_part=2,
                answ_user=answer,
                true_answer=true_answers,
                false_answer=false_answers,
            ))
        self.on_finished()

    def get_next_task(self):
        self.answer()
        self.window = Task6Part2Var2(ip_address_server=self.ip_address_server, user_name=self.user_name,
                                     next_time=self.next_time)
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

        true_answers = 0
        false_answers = 0

        if self.ui_form.lineEdit_answer_1.text() == '9':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_2.text() == '4':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_3.text() == '6':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_4.text() == '1':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_5.text() == '2':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_6.text() == '10':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_7.text() == '8':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_8.text() == '3':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_9.text() == '7':
            true_answers += 1
        else:
            false_answers += 1
        if self.ui_form.lineEdit_answer_10.text() == '5':
            true_answers += 1
        else:
            false_answers += 1

        Client(self.ip_address_server, 7000).connect(
            "insert into zadanie_variant (user_name, variant, num_zadanie, num_part, answer_user, true_answers, false_answers) "
            "values ('{user_name}', {variant}, {num_zad}, {num_part}, '{answ_user}', {true_answer}, {false_answer})".format(
                user_name=self.student_fio,
                variant=2,
                num_zad=6,
                num_part=2,
                answ_user=answer,
                true_answer=true_answers,
                false_answer=false_answers,
            ))
        self.on_finished()

    def get_next_task(self):
        self.answer()
        vaals = []
        answer_true = Client(self.ip_address_server, 7000).connect(
            f"select true_answers from zadanie_variant where user_name='{self.user_name[0]}' and variant=2")
        for el in answer_true:
            vaals.append(int(el[0]))
        result_test = round(sum(vaals) / 120 * 100)
        self.msgBox = QMessageBox()
        mark = 0
        if 95 <= result_test <= 100:
            self.msgBox.setText(f'Ваш результат: {result_test}% правильных ответов. Оценка - "отлично"!')
            mark = 5
        elif 80 <= result_test <= 94:
            self.msgBox.setText(f'Ваш результат: {result_test}% правильных ответов. Оценка - "хорошо"!')
            mark = 4
        elif 60 <= result_test <= 79:
            self.msgBox.setText(f'Ваш результат: {result_test}% правильных ответов. Оценка - "удовлетворительно"!')
            mark = 3
        elif 0 <= result_test <= 59:
            self.msgBox.setText(f'Ваш результат: {result_test}% правильных ответов. Оценка - "неудовлетворительно"!')
            mark = 2
        Client(self.ip_address_server, 7000).connect(
            "insert into user_result_variant (user_name, variant, mark, percent, true_answers, false_answers) "
            "values ('{user_name}', {variant}, {mark}, {percent}, '{true_answers}', {false_answers})".format(
                user_name=self.student_fio,
                variant=2,
                mark=mark,
                percent=result_test,
                true_answers=sum(vaals),
                false_answers=120-sum(vaals),
            ))
        self.msgBox.show()
        self.window = WindowVariantMain(ip_address_server=self.ip_address_server, username=self.user_name, variant=2,
                                        mark=mark, percent=result_test)
        self.close()
        self.window.show()
