from PyQt5 import QtWidgets
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
from open_html_function import Window
from random import shuffle


class Task1Part1Var2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie1_part1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)

    def get_next_task(self):
        self.window = Task2Part1Var2()
        self.close()
        self.window.show()


class Task2Part1Var2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie2_part1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)

    def get_next_task(self):
        self.window = Task345Part1Var2()
        self.close()
        self.window.show()


class Task345Part1Var2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie3_4_5_part1_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)
        self.ui_form.pushButton.clicked.connect(self.get_text)

    def get_text(self):
        self.window = Window(filename='var_2_text1.htm')
        self.window.show()

    def get_next_task(self):
        self.window = Task6Part1Var2()
        self.close()
        self.window.show()


class Task6Part1Var2(QtWidgets.QWidget):
    def __init__(self, parent=None):
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
        self.window = Task7Part1Var2()
        self.close()
        self.window.show()


class Task7Part1Var2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie7_part1_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)

    def get_next_task(self):
        self.window = Task8Part1Var2()
        self.close()
        self.window.show()


class Task8Part1Var2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie8_part1_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)

    def get_next_task(self):
        self.window = Task123Part2Var2()
        self.close()
        self.window.show()


class Task123Part2Var2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie1_2_3_part2_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)
        self.ui_form.pushButton.clicked.connect(self.get_text)

    def get_text(self):
        self.window = Window(filename='var_2_text2.htm')
        self.window.show()

    def get_next_task(self):
        self.window = Task4Part2Var2()
        self.close()
        self.window.show()


class Task4Part2Var2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie4_part2_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)
        self.ui_form.pushButton_show_text.clicked.connect(self.get_text)

    def get_text(self):
        self.window = Window(filename='var_2_text2.htm')
        self.window.show()

    def get_next_task(self):
        self.window = Task5Part2Var2()
        self.close()
        self.window.show()


class Task5Part2Var2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie5_part2_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)

    def get_next_task(self):
        self.window = Task6Part2Var2()
        self.close()
        self.window.show()


class Task6Part2Var2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.window = None
        self.ui_form = Ui_Zadanie6_part2_var1()
        self.ui_form.setupUi(self)
        self.ui_form.pushButton_answer.clicked.connect(self.get_next_task)

    def get_next_task(self):
        self.close()
