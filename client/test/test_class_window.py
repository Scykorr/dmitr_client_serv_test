from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
import sys


class Menu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Text")

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        lay = QVBoxLayout(self.central_widget)

        label = QLabel(self)
        pixmap = QPixmap('1_1.PNG')
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        lay.addWidget(label)
        self.show()

    def wheelEvent(self, event) -> None:
        wheel_val = event.angleDelta().y()
        if (self.the_file == '../draft/var_1_text1.pdf' or self.the_file == '../../draft/var_1_text1.pdf'
                or self.the_file == '../draft/var_2_text1.pdf'):
            max_val = 2
        elif self.the_file == '../draft/var_1_text2.pdf':
            max_val = 3
        elif self.the_file == '../draft/var_2_text2.pdf':
            max_val = 1
        if wheel_val > 0:
            if self.num_page > 0:
                self.num_page -= 1
                self.main_run()
        elif wheel_val < 0:
            if self.num_page < max_val:
                self.num_page += 1
                self.main_run()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Menu()
    sys.exit(app.exec_())