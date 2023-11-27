import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QApplication

from GUIpy.main_variant import Ui_Form
import sqlite3 as sql
from variant_1_answer import (Task1Part1Var1, Task2Part1Var1, Task345Part1Var1, Task6Part1Var1, Task7Part1Var1,
                              Task8Part1Var1, Task123Part2Var1, Task4Part2Var1, Task5Part2Var1, Task6Part2Var1)
from variant_2_answer import (Task1Part1Var2, Task2Part1Var2, Task345Part1Var2, Task6Part1Var2, Task7Part1Var2,
                              Task8Part1Var2, Task123Part2Var2, Task4Part2Var2, Task5Part2Var2, Task6Part2Var2)

from users import Client


class WindowVariantMain(QtWidgets.QWidget):
    def __init__(self, ip_address_server, username, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui_main_server = Ui_Form()
        self.ui_main_server.setupUi(self)
        self.ip_address_server = ip_address_server
        self.user_name = username
        self.username = None
        self.ui_main_server.tableWidget_server.setColumnCount(18)
        self.ui_main_server.pushButton_delete_all.clicked.connect(self.drop_db)
        self.ui_main_server.tableWidget_server.doubleClicked.connect(self.get_task)
        self.on_change()
        self.ui_main_server.pushButton_refresh.clicked.connect(self.on_change)
        self.task1var1part1 = Task1Part1Var1()
        self.task2var1part1 = Task2Part1Var1()
        self.task345var1part1 = Task345Part1Var1()
        self.task6var1part1 = Task6Part1Var1()
        self.task7var1part1 = Task7Part1Var1()
        self.task8var1part1 = Task8Part1Var1()
        self.task123var1part2 = Task123Part2Var1()
        self.task4var1part2 = Task4Part2Var1()
        self.task5var1part2 = Task5Part2Var1()
        self.task6var1part2 = Task6Part2Var1()
        self.task1var2part1 = Task1Part1Var2()
        self.task2var2part1 = Task2Part1Var2()
        self.task345var2part1 = Task345Part1Var2()
        self.task6var2part1 = Task6Part1Var2()
        self.task7var2part1 = Task7Part1Var2()
        self.task8var2part1 = Task8Part1Var2()
        self.task123var2part2 = Task123Part2Var2()
        self.task4var2part2 = Task4Part2Var2()
        self.task5var2part2 = Task5Part2Var2()
        self.task6var2part2 = Task6Part2Var2()


    def drop_db(self):
        Client(self.ip_address_server, 7000).connect("delete from zadanie_variant")

    def open_window_db(self):
        self.questions_window.show()

    def on_change(self):
        s = self.select_from_users()
        self.ui_main_server.tableWidget_server.clear()
        self.ui_main_server.tableWidget_server.setHorizontalHeaderLabels(
            "ФИО;Вариант;№1;№2;№4;№5;№6;№7;№8;№1;№2;№3;№4;№5;№6;Правильно;Неправильно;Оценка".split(";"))
        if self.ui_main_server.tableWidget_server.rowCount() == 0 or \
                self.ui_main_server.tableWidget_server.rowCount() < len(s):
            for _ in range(len(s) - self.ui_main_server.tableWidget_server.rowCount()):
                self.ui_main_server.tableWidget_server.insertRow(self.ui_main_server.tableWidget_server.rowCount())
        for i_res, res in enumerate(s):
            self.ui_main_server.tableWidget_server.setItem(i_res, 0, QTableWidgetItem(str(res[0])))
            self.ui_main_server.tableWidget_server.setItem(i_res, 1, QTableWidgetItem(str(res[1])))

    def select_from_users(self):
        vals = []

        answer = Client(self.ip_address_server, 7000).connect(f"select user_name, variant from zadanie_variant where user_name='{self.user_name[0]}'")
        for el in answer:
            vals.append(tuple(el))
        vals = list(set(vals))
        return vals

    def get_task(self):
        curr_row = self.ui_main_server.tableWidget_server.currentRow()
        curr_column = self.ui_main_server.tableWidget_server.currentColumn()
        if curr_column == 2 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '1':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task1var1part1.main_select(self.username, self.ip_address_server)
            self.task1var1part1.show()
        elif curr_column == 3 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '1':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task2var1part1.main_select(self.username, self.ip_address_server)
            self.task2var1part1.show()
        elif (curr_column == 4 or curr_column == 5) and self.ui_main_server.tableWidget_server.item(curr_row,
                                                                                                    1).text() == '1':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task345var1part1.main_select(self.username, self.ip_address_server)
            self.task345var1part1.show()
        elif curr_column == 6 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '1':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task6var1part1.main_select(self.username, self.ip_address_server)
            self.task6var1part1.show()
        elif curr_column == 7 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '1':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task7var1part1.main_select(self.username, self.ip_address_server)
            self.task7var1part1.show()
        elif curr_column == 8 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '1':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task8var1part1.main_select(self.username, self.ip_address_server)
            self.task8var1part1.show()
        elif ((
                      curr_column == 9 or curr_column == 10 or curr_column == 11) and
              self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '1'):
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task123var1part2.main_select(self.username, self.ip_address_server)
            self.task123var1part2.show()
        elif curr_column == 12 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '1':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task4var1part2.main_select(self.username, self.ip_address_server)
            self.task4var1part2.show()
        elif curr_column == 13 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '1':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task5var1part2.main_select(self.username, self.ip_address_server)
            self.task5var1part2.show()
        elif curr_column == 14 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '1':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task6var1part2.main_select(self.username, self.ip_address_server)
            self.task6var1part2.show()
        elif curr_column == 2 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '2':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task1var2part1.main_select(self.username, self.ip_address_server)
            self.task1var2part1.show()
        elif curr_column == 3 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '2':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task2var2part1.main_select(self.username, self.ip_address_server)
            self.task2var2part1.show()
        elif (curr_column == 4 or curr_column == 5) and self.ui_main_server.tableWidget_server.item(curr_row,
                                                                                                    1).text() == '2':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task345var2part1.main_select(self.username, self.ip_address_server)
            self.task345var2part1.show()
        elif curr_column == 6 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '2':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task6var2part1.main_select(self.username, self.ip_address_server)
            self.task6var2part1.show()
        elif curr_column == 7 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '2':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task7var2part1.main_select(self.username, self.ip_address_server)
            self.task7var2part1.show()
        elif curr_column == 8 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '2':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task8var2part1.main_select(self.username, self.ip_address_server)
            self.task8var2part1.show()
        elif ((
                      curr_column == 9 or curr_column == 10 or curr_column == 11) and
              self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '2'):
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task123var2part2.main_select(self.username, self.ip_address_server)
            self.task123var2part2.show()
        elif curr_column == 12 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '2':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task4var2part2.main_select(self.username, self.ip_address_server)
            self.task4var2part2.show()
        elif curr_column == 13 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '2':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task5var2part2.main_select(self.username, self.ip_address_server)
            self.task5var2part2.show()
        elif curr_column == 14 and self.ui_main_server.tableWidget_server.item(curr_row, 1).text() == '2':
            self.username = self.ui_main_server.tableWidget_server.item(curr_row, 0).text()
            self.task6var2part2.main_select(self.username, self.ip_address_server)
            self.task6var2part2.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_server_window = WindowVariantMain('192.168.56.1', ['Иванов Иван Иванович', 1])
    main_server_window.show()
    sys.exit(app.exec_())
