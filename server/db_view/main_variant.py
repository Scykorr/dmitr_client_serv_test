import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QApplication

from server.db_view.GUIpy.main_variant import Ui_Form
import sqlite3 as sql


class MyThreadVariant(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(list)

    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.time_format = None

    def run(self):
        while True:
            self.sleep(1)
            select_result = WindowVariantMain.select_from_users(self)
            self.mysignal.emit(select_result)


class WindowVariantMain(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui_main_server = Ui_Form()
        self.ui_main_server.setupUi(self)
        self.ui_main_server.tableWidget_server.setColumnCount(15)
        self.ui_main_server.pushButton_delete_all.clicked.connect(self.drop_db)
        self.mythread = MyThreadVariant()
        self.on_clicked()
        self.mythread.started.connect(self.on_started)
        self.mythread.finished.connect(self.on_finished)
        self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)

    def drop_db(self):
        con = sql.connect('../data.db')
        cur = con.cursor()
        cur.execute('delete from user')
        con.commit()
        cur.close()
        con.close()
        self.ui_main_server.tableWidget_server.setRowCount(0)

    def open_window_db(self):
        self.questions_window.show()

    def on_clicked(self):
        self.mythread.start()

    def on_started(self):
        pass

    def on_finished(self):
        self.mythread.exit()

    def on_change(self, s):
        self.ui_main_server.tableWidget_server.clear()
        self.ui_main_server.tableWidget_server.setHorizontalHeaderLabels(
            "ФИО;Вариант;№1;№2;№4;№5;№6;№7;№8;№1;№2;№3;№4;№5;№6".split(";"))
        if self.ui_main_server.tableWidget_server.rowCount() == 0 or \
                self.ui_main_server.tableWidget_server.rowCount() < len(s):
            for _ in range(len(s) - self.ui_main_server.tableWidget_server.rowCount()):
                self.ui_main_server.tableWidget_server.insertRow(self.ui_main_server.tableWidget_server.rowCount())
        for i_res, res in enumerate(s):
            self.ui_main_server.tableWidget_server.setItem(i_res, 0, QTableWidgetItem(str(res[0])))
            self.ui_main_server.tableWidget_server.setItem(i_res, 1, QTableWidgetItem(str(res[1])))



    def select_from_users(self):
        vals = []
        con = sql.connect('../data.db')
        cur = con.cursor()
        answer = cur.execute('select user_name, variant from zadanie_variant')
        for el in answer:
            vals.append(el)
        vals = list(set(vals))
        con.commit()
        cur.close()
        con.close()
        return vals


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_server_window = WindowVariantMain()
    main_server_window.show()
    sys.exit(app.exec_())
