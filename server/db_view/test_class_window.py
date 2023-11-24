from PyQt5.QtWidgets import QLabel, QMainWindow, QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QPixmap
import sys


class Menu(QMainWindow):

    def __init__(self, doc_paths):
        super().__init__()
        self.setWindowTitle("Text")
        self.doc_paths = doc_paths
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.lay = QVBoxLayout(self.central_widget)

        self.label = QLabel(self)

        self.num_page = 0
        self.main_run()

    def main_run(self):
        pixmap = QPixmap(self.doc_paths[self.num_page])
        self.label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        self.lay.addWidget(self.label)

    def wheelEvent(self, event) -> None:
        wheel_val = event.angleDelta().y()
        max_val = len(self.doc_paths) - 1
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
