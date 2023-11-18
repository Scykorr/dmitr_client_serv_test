import time

from PyQt5 import QtCore
from users import Client


class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None, result_time=None):
        QtCore.QThread.__init__(self, parent)
        if result_time is None:
            result_time = ['']
        self.result_time = result_time
        self.time_format = None
        self.curr_answers = None

    def run(self):
        for i in range(600, -1, -1):
            self.sleep(1)
            self.time_format = time.strftime("%H:%M:%S", time.gmtime(i))
            self.result_time[0] = str(i)
            self.mysignal.emit("Осталось времени = %s" % self.time_format)


class MyThreadTest2(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, ip_address_server, parent=None, result_time=None):
        QtCore.QThread.__init__(self, parent)
        if result_time is None:
            result_time = ['']
        self.result_time = result_time
        self.time_format = None
        self.curr_answers = None
        self.count_winners = 0
        self.ip_address_server = ip_address_server

    def run(self):
        for i in range(9999, -1, -1):
            if self.count_winners == 5:
                break
            self.sleep(1)
            self.time_format = time.strftime("%H:%M:%S", time.gmtime(i))
            self.result_time[0] = str(i)
            self.mysignal.emit("Осталось времени = %s" % self.time_format)
            self.curr_answers = Client(self.ip_address_server, 7000).connect('select current_answer from user')
            self.count_winners = 0
            for el in self.curr_answers:
                if el[0] == 10:
                    self.count_winners += 1
            print(self.count_winners)


class MyThreadVariant(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def __init__(self, parent=None, result_time=None):
        QtCore.QThread.__init__(self, parent)
        if result_time is None:
            result_time = []
        self.result_time = result_time
        self.time_format = None
        self.curr_answers = None

    def run(self):
        for i in range(2400, -1, -1):
            self.sleep(1)
            self.time_format = time.strftime("%H:%M:%S", time.gmtime(i))
            self.result_time[0] = str(i)
            self.mysignal.emit("Осталось времени = %s" % self.time_format)
