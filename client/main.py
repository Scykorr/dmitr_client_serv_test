from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtGui import QPixmap
import sys
from socket import *
import json
from GUIpy.client_login import Ui_Form_client_login
from GUIpy.client_main import Ui_Form_client_main
from GUIpy.client_test1 import Ui_Form_client_test1
from GUIpy.client_test2 import Ui_Form_test2
from random import shuffle
import time
import sqlite3 as sql
from variant_1 import Task1Part1Var1
from variant_2 import Task1Part1Var2

with open('ip_address', 'r', encoding='utf-8') as ip_file:
    for el in ip_file:
        ip_address_server = el


class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.time_format = None
        self.curr_answers = None

    def run(self):
        for i in range(600, -1, -1):
            self.sleep(1)
            self.time_format = time.strftime("%H:%M:%S", time.gmtime(i))
            result_time[0] = str(i)
            self.mysignal.emit("Осталось времени = %s" % self.time_format)


class MyThreadTest2(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.time_format = None
        self.curr_answers = None
        self.count_winners = 0

    def run(self):
        for i in range(9999, -1, -1):
            if self.count_winners == 5:
                break
            self.sleep(1)
            self.time_format = time.strftime("%H:%M:%S", time.gmtime(i))
            result_time[0] = str(i)
            self.mysignal.emit("Осталось времени = %s" % self.time_format)
            self.curr_answers = Client(ip_address_server, 7000).connect('select current_answer from user')
            self.count_winners = 0
            for el in self.curr_answers:
                if el[0] == 10:
                    self.count_winners += 1
            print(self.count_winners)


class Client:
    def __init__(self, ip, port):
        self.cli = socket(AF_INET, SOCK_STREAM)
        self.cli.connect(
            (ip, port)
        )

    def connect(self, req):
        try:
            msg = self.cli.recv(1024).decode('utf-8')
        except Exception as e:
            print('ERROR: {0}'.format(
                str(e),
            ))
            msg = ''
            exit()
        if msg == 'YOU ARE CONNECTED!':
            val = self.listen(req)
            return val
        else:
            exit()

    def sender(self, text):
        self.cli.send(text.encode('utf-8'))
        while self.cli.recv(1024).decode('utf-8') != 'getted':
            self.cli.send(text.encode('utf-8'))

    def listen(self, req):
        if req:
            if req == 'disconnect':
                self.sender(req)
                print(self.cli.recv(1024).decode('utf-8'))
                exit()
            else:
                self.sender(req)
                data = json.loads(
                    self.cli.recv(63000).decode('utf-8')
                )
                if data['answer']:
                    print('SERVER ANSWER:\n\t{answ}'.format(
                        answ=data['answer']
                    ))
                    return data['answer']
                elif data['error']:
                    print('SERVER ERROR:\n\t{err}'.format(
                        err=data['error']
                    ))
                    return data['error']


class WindowLogin(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.choose_test_window = None
        self.ui_client_login = Ui_Form_client_login()
        self.ui_client_login.setupUi(self)
        self.ui_client_login.pushButton_fio.clicked.connect(self.send_fio)
        self.student_fio = ''

    def send_fio(self):
        self.choose_test_window = WindowChooseTest()
        self.student_fio = self.ui_client_login.lineEdit_fio.text()
        user_name.append(self.student_fio)
        Client(ip_address_server, 7000).connect("insert into user(fio_user) values ('{0}')".format(
            self.student_fio,
        ))
        self.hide()
        self.choose_test_window.show()


class WindowChooseTest(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui_choose_test = Ui_Form_client_main()
        self.ui_choose_test.setupUi(self)
        self.ui_choose_test.pushButton_test1.clicked.connect(self.test_1)
        self.ui_choose_test.pushButton_test2.clicked.connect(self.test_2)
        self.ui_choose_test.pushButton_variant1.clicked.connect(self.get_variant_1)
        self.ui_choose_test.pushButton_variant2.clicked.connect(self.get_variant_2)

    def test_1(self):
        self.first_test_window = FirstTestWindow()
        self.hide()
        self.first_test_window.show()

    def test_2(self):
        self.second_test_window = SecondTestWindow()
        self.hide()
        self.second_test_window.show()

    def get_variant_1(self):
        self.first_variant_window = Task1Part1Var1()
        self.first_variant_window.show()

    def get_variant_2(self):
        self.second_variant_window = Task1Part1Var2()
        self.second_variant_window.show()

class FirstTestWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui_first_test = Ui_Form_client_test1()
        self.ui_first_test.setupUi(self)
        self.ui_first_test.pushButton.clicked.connect(self.answer)
        self.questions = Client(ip_address_server, 7000).connect(
            'select iq_question, text_question from question')
        shuffle(self.questions)
        self.new_lst_question = self.questions[:10]
        self.variants = Client(ip_address_server, 7000).connect(
            'select id_var_answ, text_var_answ, var_answ_right, id_question from variant_answer')
        shuffle(self.variants)
        self.sorted_variants = self.sort_variants()
        self.counter_questions = 0
        self.counter_questions_result = 0
        self.right_answer = 0
        self.wrong_answer = 0
        self.student_fio = user_name[0]
        self.ui_first_test.radioButton_answer1.setChecked(True)
        self.get_questionts()
        self.mythread = MyThread()
        self.on_clicked()
        self.mythread.started.connect(self.on_started)
        self.mythread.finished.connect(self.on_finished)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)

    def on_clicked(self):
        self.mythread.start()

    def on_started(self):
        self.ui_first_test.label_timer.setText("")

    def on_finished(self):
        res_sec = 600 - int(result_time[0])
        time_format_result = time.strftime("%H:%M:%S", time.gmtime(res_sec))
        result_points = self.right_answer * 10
        Client(ip_address_server, 7000).connect(
            "update user set time='{0}', true_answer={1}, false_answer={2}, current_answer={3},"
            " result_score={5} where fio_user='{4}'".format(
                time_format_result,
                self.right_answer,
                self.wrong_answer,
                self.counter_questions_result,
                self.student_fio,
                result_points,
            ))
        QMessageBox.about(self, 'Ваш результат:', 'Тест завершен.\n{0} верных ответов из 10.'.format(
            self.right_answer
        ))
        exit()

    def on_change(self, s):
        self.ui_first_test.label_timer.setText(s)

    def answer(self):
        self.counter_questions_result += 1
        if self.ui_first_test.radioButton_answer1.isChecked() \
                and self.sorted_variants[self.counter_questions][0][2] == 1:
            self.right_answer += 1
            self.right_answer_append()
        elif self.ui_first_test.radioButton_answer2.isChecked() \
                and self.sorted_variants[self.counter_questions][1][2] == 1:
            self.right_answer += 1
            self.right_answer_append()
        elif self.ui_first_test.radioButton_answer3.isChecked() \
                and self.sorted_variants[self.counter_questions][2][2] == 1:
            self.right_answer += 1
            self.right_answer_append()
        elif self.ui_first_test.radioButton_4.isChecked() \
                and self.sorted_variants[self.counter_questions][3][2] == 1:
            self.right_answer += 1
            self.right_answer_append()
        else:
            self.wrong_answer += 1
            Client(ip_address_server, 7000).connect(
                "update user set false_answer={0}, current_answer={1} where fio_user='{2}'".format(
                    self.wrong_answer,
                    self.counter_questions_result,
                    self.student_fio,
                ))

        self.ui_first_test.radioButton_answer1.setChecked(True)
        self.ui_first_test.radioButton_answer2.setChecked(False)
        self.ui_first_test.radioButton_answer3.setChecked(False)
        self.ui_first_test.radioButton_4.setChecked(False)
        self.counter_questions += 1
        if self.counter_questions < 10:
            self.get_questionts()
        else:
            self.on_finished()
            exit()

    def right_answer_append(self):
        Client(ip_address_server, 7000).connect(
            "update user set true_answer={0}, current_answer={1} where fio_user='{2}'".format(
                self.right_answer,
                self.counter_questions_result,
                self.student_fio,
            ))

    def get_questionts(self):
        self.ui_first_test.label_img_question.clear()
        self.ui_first_test.label_img_var1.clear()
        self.ui_first_test.label_img_var2.clear()
        self.ui_first_test.label_img_var3.clear()
        self.ui_first_test.label_img_var4.clear()

        self.setWindowTitle('Вопрос №{0}'.format(
            self.counter_questions + 1,
        ))
        self.ui_first_test.plainTextEdit.setPlainText(self.new_lst_question[self.counter_questions][1])
        self.ui_first_test.radioButton_answer1.setText(self.sorted_variants[self.counter_questions][0][1])
        self.ui_first_test.radioButton_answer2.setText(self.sorted_variants[self.counter_questions][1][1])
        self.ui_first_test.radioButton_answer3.setText(self.sorted_variants[self.counter_questions][2][1])
        self.ui_first_test.radioButton_4.setText(self.sorted_variants[self.counter_questions][3][1])

        id_question = self.new_lst_question[self.counter_questions][0]
        id_var1 = self.sorted_variants[self.counter_questions][0][0]
        id_var2 = self.sorted_variants[self.counter_questions][1][0]
        id_var3 = self.sorted_variants[self.counter_questions][2][0]
        id_var4 = self.sorted_variants[self.counter_questions][3][0]

        con = sql.connect('img.db')
        cur = con.cursor()
        img_bin = cur.execute(
            'select image from img where id_question="{0}"'.format(
                id_question,
            ))
        img_bin = img_bin.fetchone()
        con.commit()
        cur.close()
        con.close()
        pix = QPixmap()
        if img_bin != None:
            if pix.loadFromData(img_bin[0], 'png'):
                self.ui_first_test.label_img_question.setPixmap(pix)

        con = sql.connect('img.db')
        cur = con.cursor()
        img_bin = cur.execute(
            'select image from img where id_variant="{0}"'.format(
                id_var1,
            ))
        img_bin = img_bin.fetchone()
        con.commit()
        cur.close()
        con.close()
        pix1 = QPixmap()
        if img_bin != None:
            if pix1.loadFromData(img_bin[0], 'png'):
                self.ui_first_test.label_img_var1.setPixmap(pix1)

        con = sql.connect('img.db')
        cur = con.cursor()
        img_bin = cur.execute(
            'select image from img where id_variant="{0}"'.format(
                id_var2,
            ))
        img_bin = img_bin.fetchone()
        con.commit()
        cur.close()
        con.close()
        pix2 = QPixmap()
        if img_bin != None:
            if pix2.loadFromData(img_bin[0], 'png'):
                self.ui_first_test.label_img_var2.setPixmap(pix2)

        con = sql.connect('img.db')
        cur = con.cursor()
        img_bin = cur.execute(
            'select image from img where id_variant="{0}"'.format(
                id_var3,
            ))
        img_bin = img_bin.fetchone()
        con.commit()
        cur.close()
        con.close()
        pix3 = QPixmap()
        if img_bin != None:
            if pix3.loadFromData(img_bin[0], 'png'):
                self.ui_first_test.label_img_var3.setPixmap(pix3)

        con = sql.connect('img.db')
        cur = con.cursor()
        img_bin = cur.execute(
            'select image from img where id_variant="{0}"'.format(
                id_var4,
            ))
        img_bin = img_bin.fetchone()
        con.commit()
        cur.close()
        con.close()
        pix4 = QPixmap()
        if img_bin != None:
            if pix4.loadFromData(img_bin[0], 'png'):
                self.ui_first_test.label_img_var4.setPixmap(pix4)

    def sort_variants(self):
        new_list = [[] for _ in range(10)]
        counter = 0
        for question in self.new_lst_question:
            for var in self.variants:
                if question[0] == var[3]:
                    new_list[counter].append(var)
            counter += 1
        return new_list


class SecondTestWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui_second_test = Ui_Form_test2()
        self.ui_second_test.setupUi(self)
        self.ui_second_test.pushButton_answer.clicked.connect(self.answer)
        self.questions_answers = Client(ip_address_server, 7000).connect('test2_question')
        self.test2_questions = []
        self.test2_variants = []
        self.get_quest_answers()
        self.counter_questions = 0
        self.counter_questions_result = 0
        self.right_answer = 0
        self.wrong_answer = 0
        self.student_fio = user_name[0]
        self.ui_second_test.radioButton_answer1.setChecked(True)
        self.start_time = time.time()
        self.get_questions()
        self.mythread_test2 = MyThreadTest2()
        self.on_clicked()
        self.mythread_test2.started.connect(self.on_started)
        self.mythread_test2.finished.connect(self.on_finished)
        self.mythread_test2.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)
        self.ui_second_test.label_timer.setVisible(False)

    def get_quest_answers(self):
        for i_el, element in enumerate(self.questions_answers):
            if i_el < 10:
                self.test2_questions.append(element)
            else:
                self.test2_variants.append(element)

    def on_clicked(self):
        self.mythread_test2.start()

    def on_started(self):
        self.ui_second_test.label_timer.setText("")

    def on_finished(self):
        winner_seconds = Client(ip_address_server, 7000).connect(
            'select seconds_for_test2 from score_for_count')
        winner_seconds = winner_seconds[0][0]
        res_sec = 9999 - int(result_time[0])
        time_format_result = time.strftime("%H:%M:%S", time.gmtime(res_sec))
        if res_sec < 10:
            k_time = 150
        else:
            k_time = res_sec
        result_score = round((winner_seconds / k_time) * (self.right_answer / 10) * 100, 0)
        summ_answer = self.right_answer + self.wrong_answer
        Client(ip_address_server, 7000).connect(
            "update user set time='{0}', true_answer={1}, false_answer={2}, current_answer={5}, result_score={4} "
            "where fio_user='{3}'".format(
                time_format_result,
                self.right_answer,
                self.wrong_answer,
                self.student_fio,
                result_score,
                summ_answer,
            ))
        QMessageBox.about(self, 'Ваш результат:', 'Тест завершен.\n{0} верных ответов из 10.'.format(
            self.right_answer
        ))
        exit()

    def on_change(self, s):
        self.ui_second_test.label_timer.setText(s)

    def answer(self):
        self.counter_questions_result += 1
        if self.ui_second_test.radioButton_answer1.isChecked() \
                and self.test2_variants[self.counter_questions][0][2] == 1:
            self.right_answer += 1
            self.right_answer_append()
        elif self.ui_second_test.radioButton_answer2.isChecked() \
                and self.test2_variants[self.counter_questions][1][2] == 1:
            self.right_answer += 1
            self.right_answer_append()
        elif self.ui_second_test.radioButton_answer3.isChecked() \
                and self.test2_variants[self.counter_questions][2][2] == 1:
            self.right_answer += 1
            self.right_answer_append()
        elif self.ui_second_test.radioButton_answer.isChecked() \
                and self.test2_variants[self.counter_questions][3][2] == 1:
            self.right_answer += 1
            self.right_answer_append()
        else:
            self.wrong_answer += 1
            Client(ip_address_server, 7000).connect(
                "update user set false_answer={0}, current_answer={1} where fio_user='{1}'".format(
                    self.wrong_answer,
                    self.counter_questions_result,
                    self.student_fio,
                ))

        self.ui_second_test.radioButton_answer1.setChecked(True)
        self.ui_second_test.radioButton_answer2.setChecked(False)
        self.ui_second_test.radioButton_answer3.setChecked(False)
        self.ui_second_test.radioButton_answer.setChecked(False)
        self.counter_questions += 1
        if self.counter_questions < 10:
            self.get_questions()
        else:
            self.on_finished()
            exit()

    def right_answer_append(self):
        Client(ip_address_server, 7000).connect(
            "update user set true_answer={0}, current_answer={1} where fio_user='{2}'".format(
                self.right_answer,
                self.counter_questions_result,
                self.student_fio,
            ))

    def get_questions(self):
        self.ui_second_test.label_img_question.clear()
        self.ui_second_test.label_img_var1.clear()
        self.ui_second_test.label_img_var2.clear()
        self.ui_second_test.label_img_var3.clear()
        self.ui_second_test.label_img_var4.clear()

        self.setWindowTitle('Вопрос №{0}'.format(
            self.counter_questions + 1,
        ))
        self.ui_second_test.plainTextEdit_question.setPlainText(self.test2_questions[self.counter_questions][1])
        self.ui_second_test.radioButton_answer1.setText(self.test2_variants[self.counter_questions][0][1])
        self.ui_second_test.radioButton_answer2.setText(self.test2_variants[self.counter_questions][1][1])
        self.ui_second_test.radioButton_answer3.setText(self.test2_variants[self.counter_questions][2][1])
        self.ui_second_test.radioButton_answer.setText(self.test2_variants[self.counter_questions][3][1])

        id_question = self.test2_questions[self.counter_questions][0]
        id_var1 = self.test2_variants[self.counter_questions][0][0]
        id_var2 = self.test2_variants[self.counter_questions][1][0]
        id_var3 = self.test2_variants[self.counter_questions][2][0]
        id_var4 = self.test2_variants[self.counter_questions][3][0]

        con = sql.connect('img.db')
        cur = con.cursor()
        img_bin = cur.execute(
            'select image from img where id_question="{0}"'.format(
                id_question,
            ))
        img_bin = img_bin.fetchone()
        con.commit()
        cur.close()
        con.close()
        pix = QPixmap()
        if img_bin is not None:
            if pix.loadFromData(img_bin[0], 'png'):
                self.ui_second_test.label_img_question.setPixmap(pix)

        con = sql.connect('img.db')
        cur = con.cursor()
        img_bin = cur.execute(
            'select image from img where id_variant="{0}"'.format(
                id_var1,
            ))
        img_bin = img_bin.fetchone()
        con.commit()
        cur.close()
        con.close()
        pix1 = QPixmap()
        if img_bin is not None:
            if pix1.loadFromData(img_bin[0], 'png'):
                self.ui_second_test.label_img_var1.setPixmap(pix1)

        con = sql.connect('img.db')
        cur = con.cursor()
        img_bin = cur.execute(
            'select image from img where id_variant="{0}"'.format(
                id_var2,
            ))
        img_bin = img_bin.fetchone()
        con.commit()
        cur.close()
        con.close()
        pix2 = QPixmap()
        if img_bin is not None:
            if pix2.loadFromData(img_bin[0], 'png'):
                self.ui_second_test.label_img_var2.setPixmap(pix2)

        con = sql.connect('img.db')
        cur = con.cursor()
        img_bin = cur.execute(
            'select image from img where id_variant="{0}"'.format(
                id_var3,
            ))
        img_bin = img_bin.fetchone()
        con.commit()
        cur.close()
        con.close()
        pix3 = QPixmap()
        if img_bin is not None:
            if pix3.loadFromData(img_bin[0], 'png'):
                self.ui_second_test.label_img_var3.setPixmap(pix3)

        con = sql.connect('img.db')
        cur = con.cursor()
        img_bin = cur.execute(
            'select image from img where id_variant="{0}"'.format(
                id_var4,
            ))
        img_bin = img_bin.fetchone()
        con.commit()
        cur.close()
        con.close()
        pix4 = QPixmap()
        if img_bin is not None:
            if pix4.loadFromData(img_bin[0], 'png'):
                self.ui_second_test.label_img_var4.setPixmap(pix4)

    def get_image_db(self, question_var_name: str):
        con = sql.connect('img.db')
        cur = con.cursor()
        img_bin = cur.execute(
            'select image from img where id_question="{0}"'.format(
                question_var_name,
            ))
        img_bin = img_bin.fetchone()
        con.commit()
        cur.close()
        con.close()
        pix = QPixmap()
        if img_bin is not None:
            if pix.loadFromData(img_bin[0], 'png'):
                self.ui_second_test.label_img_question.setPixmap(pix)


if __name__ == '__main__':
    user_name = []
    result_time = ['']
    app = QApplication(sys.argv)
    login_window = WindowLogin()
    login_window.show()
    sys.exit(app.exec_())
