import sys

from PyQt5 import QtWidgets, QtCore, QtGui
import pypdfium2 as pdfium
from PyQt5.QtWidgets import QApplication
from client.GUIpy.open_file import Ui_Form


class OpenPdf(QtWidgets.QWidget):
    def __init__(self, num_page=0, doc_path="../../draft/var_1_text1.pdf", parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.the_file = doc_path
        self.num_page = num_page
        self.window = Ui_Form()
        self.window.setupUi(self)
        self.window.label.setFixedSize(650, 800)
        self.window.label.setAlignment(QtCore.Qt.AlignCenter)
        self.window.label_to_display_geometry = self.window.label.geometry()
        self.main_run()

    def main_run(self):
        self.pdf = pdfium.PdfDocument(self.the_file)
        self.page = self.pdf.get_page(self.num_page)
        self.pil_image = self.page.render(scale=300 / 72).to_pil()
        self.image = self.pil_image.toqimage()

        self.label_pixmap = QtGui.QPixmap.fromImage(self.image)
        self.size_new = QtCore.QSize(self.window.label_to_display_geometry.width() + 100,
                                     self.window.label_to_display_geometry.height() + 100)
        self.window.label.setPixmap(
            self.label_pixmap.scaled(self.size_new, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

        self.window.gridLayout.addWidget(self.window.label)

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


# class OpenPdf(QtWidgets.QWidget):
#     def __init__(self, num_page=0, doc_path="../../draft/var_1_text1.pdf", parent=None):
#         QtWidgets.QWidget.__init__(self, parent)
#
#         self.the_file = doc_path
#
#         self.window = QtWidgets.QWidget()
#         self.window.resize(250, 850)
#         self.window_layout = QtWidgets.QGridLayout()
#
#         self.label_to_display_the_page = QtWidgets.QLabel()
#         self.label_to_display_the_page.setFixedSize(650, 800)
#         self.label_to_display_the_page.setAlignment(QtCore.Qt.AlignCenter)
#         self.label_to_display_the_page_geometry = self.label_to_display_the_page.geometry()
#
#         self.pdf = pdfium.PdfDocument(self.the_file)
#         self.page = self.pdf.get_page(num_page)
#         self.pil_image = self.page.render(scale=300 / 72).to_pil()
#         self.image = self.pil_image.toqimage()
#
#         self.label_pixmap = QtGui.QPixmap.fromImage(self.image)
#         self.size_new = QtCore.QSize(self.label_to_display_the_page_geometry.width() + 100,
#                             self.label_to_display_the_page_geometry.height() + 100)
#         self.label_to_display_the_page.setPixmap(
#             self.label_pixmap.scaled(self.size_new, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
#
#         self.window_layout.addWidget(self.label_to_display_the_page)
#         self.window.setLayout(self.window_layout)


def open_pdf(num_page=0, doc_path="../../draft/var_1_text1.pdf"):
    the_file = doc_path

    application = QtWidgets.QApplication([])
    window = QtWidgets.QWidget()
    window.resize(250, 850)
    window_layout = QtWidgets.QGridLayout()

    label_to_display_the_page = QtWidgets.QLabel()
    label_to_display_the_page.setFixedSize(650, 800)
    label_to_display_the_page.setAlignment(QtCore.Qt.AlignCenter)
    label_to_display_the_page_geometry = label_to_display_the_page.geometry()

    pdf = pdfium.PdfDocument(the_file)
    page = pdf.get_page(num_page)
    # pil_image = page.render_topil(scale=1,rotation=0,crop=(0, 0, 0, 0),greyscale=False,optimise_mode=pdfium.OptimiseMode.NONE)
    pil_image = page.render(scale=300 / 72).to_pil()
    image = pil_image.toqimage()

    label_pixmap = QtGui.QPixmap.fromImage(image)
    size = QtCore.QSize(label_to_display_the_page_geometry.width() + 100,
                        label_to_display_the_page_geometry.height() + 100)
    label_to_display_the_page.setPixmap(
        label_pixmap.scaled(size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))

    window_layout.addWidget(label_to_display_the_page)
    window.setLayout(window_layout)
    window.show()
    application.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login_window = OpenPdf(num_page=0, doc_path='../draft/var_1_text1.pdf')
    login_window.show()
    sys.exit(app.exec_())
    # open_pdf(num_page=0, doc_path='../draft/var_1_text1.pdf')
