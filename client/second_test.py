import time

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMessageBox

from client.GUIpy.client_test2 import Ui_Form_test2
from client.threads import MyThreadTest2
from client.users import Client
import sqlite3 as sql


class SecondTestWindow(QtWidgets.QWidget):
    def __init__(self, ip_address_server, parent=None, user_name=None):
        QtWidgets.QWidget.__init__(self, parent)
        if user_name is None:
            user_name = []
        self.user_name = user_name
        self.ip_address_server = ip_address_server
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
        self.mythread_test2 = MyThreadTest2(ip_address_server=ip_address_server)
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
        winner_seconds = Client(self.ip_address_server, 7000).connect(
            'select seconds_for_test2 from score_for_count')
        winner_seconds = winner_seconds[0][0]
        res_sec = 9999 - int(self.mythread_test2.result_time[0])
        time_format_result = time.strftime("%H:%M:%S", time.gmtime(res_sec))
        if res_sec < 10:
            k_time = 150
        else:
            k_time = res_sec
        result_score = round((winner_seconds / k_time) * (self.right_answer / 10) * 100, 0)
        summ_answer = self.right_answer + self.wrong_answer
        Client(self.ip_address_server, 7000).connect(
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
            Client(self.ip_address_server, 7000).connect(
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
        Client(self.ip_address_server, 7000).connect(
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
