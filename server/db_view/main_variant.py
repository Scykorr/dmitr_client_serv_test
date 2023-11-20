import sys

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QApplication

from server.db_view.GUIpy.main_variant import Ui_Form
import sqlite3 as sql
from variant_1 import (Task1Part1Var1, Task2Part1Var1, Task345Part1Var1, Task6Part1Var1, Task7Part1Var1,
                       Task8Part1Var1, Task123Part2Var1, Task4Part2Var1, Task5Part2Var1)


class WindowVariantMain(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui_main_server = Ui_Form()
        self.ui_main_server.setupUi(self)
        self.ui_main_server.tableWidget_server.setColumnCount(15)
        self.ui_main_server.pushButton_delete_all.clicked.connect(self.drop_db)
        self.ui_main_server.tableWidget_server.doubleClicked.connect(self.get_task)
        self.on_change()
        self.ui_main_server.pushButton_refresh.clicked.connect(self.on_change)
        self.username = None
        self.task1var1part1 = Task1Part1Var1()
        self.task2var1part1 = Task2Part1Var1()
        self.task345var1part1 = Task345Part1Var1()
        self.task6var1part1 = Task6Part1Var1()
        self.task7var1part1 = Task7Part1Var1()
        self.task8var1part1 = Task8Part1Var1()
        self.task123var1part2 = Task123Part2Var1()
        self.task4var1part2 = Task4Part2Var1()
        self.task5var1part2 = Task5Part2Var1()

    def drop_db(self):
        con = sql.connect('../data.db')
        cur = con.cursor()
        cur.execute('delete from zadanie_variant')
        con.commit()
        cur.close()
        con.close()
        self.ui_main_server.tableWidget_server.setRowCount(0)

    def open_window_db(self):
        self.questions_window.show()

    def on_change(self):
        s = self.select_from_users()
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

    def get_task(self):
        curr_row = self.ui_main_server.tableWidget_server.currentRow()
        curr_column = self.ui_main_server.tableWidget_server.currentColumn()
        if curr_column == 2 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '1':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task1var1part1.main_select(self.username)
            self.task1var1part1.show()
        elif curr_column == 3 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '1':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task2var1part1.main_select(self.username)
            self.task2var1part1.show()
        elif (curr_column == 4 or curr_column == 5) and self.ui_main_server.tableWidget_server.item(curr_row,
                                                                                                    1).text() == '1':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task345var1part1.main_select(self.username)
            self.task345var1part1.show()
        elif curr_column == 6 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '1':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task6var1part1.main_select(self.username)
            self.task6var1part1.show()
        elif curr_column == 7 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '1':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task7var1part1.main_select(self.username)
            self.task7var1part1.show()
        elif curr_column == 8 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '1':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task8var1part1.main_select(self.username)
            self.task8var1part1.show()
        elif ((
                      curr_column == 9 or curr_column == 10 or curr_column == 11) and
              self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '1'):
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task123var1part2.main_select(self.username)
            self.task123var1part2.show()
        elif curr_column == 12 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '1':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task4var1part2.main_select(self.username)
            self.task4var1part2.show()
        elif curr_column == 13 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '1':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task5var1part2.main_select(self.username)
            self.task5var1part2.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_server_window = WindowVariantMain()
    main_server_window.show()
    sys.exit(app.exec_())
