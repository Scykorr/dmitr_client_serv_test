import sys

from PyQt5 import QtWidgets, QtCore, QtGui
import pypdfium2 as pdfium
from PyQt5.QtWidgets import QApplication


# class OpenPdf(QtWidgets.QWidget):
#     def __init__(self, num_page=0, doc_path="", parent=None):
#         QtWidgets.QWidget.__init__(self, parent)
#         self.resize(250, 850)
#         window_layout = QtWidgets.QGridLayout()
#
#         label_to_display_the_page = QtWidgets.QLabel()
#         label_to_display_the_page.setFixedSize(650, 800)
#         label_to_display_the_page.setAlignment(QtCore.Qt.AlignCenter)
#         label_to_display_the_page_geometry = label_to_display_the_page.geometry()
#
#         pdf = pdfium.PdfDocument(doc_path)
#         page = pdf.get_page(num_page)
#         pil_image = page.render(scale=300 / 72).to_pil()
#         image = pil_image.toqimage()
#
#         label_pixmap = QtGui.QPixmap.fromImage(image)
#         size = QtCore.QSize(label_to_display_the_page_geometry.width() + 100,
#                             label_to_display_the_page_geometry.height() + 100)
#         label_to_display_the_page.setPixmap(
#             label_pixmap.scaled(size, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
#
#         window_layout.addWidget(label_to_display_the_page)
#         self.setLayout(window_layout)

def open_pdf(num_page=0, doc_path=""):
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


if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # login_window = OpenPdf(num_page=0, doc_path='../draft/var_1_text1.pdf')
    # login_window.show()
    # sys.exit(app.exec_())
    open_pdf(num_page=0, doc_path='../draft/var_1_text1.pdf')