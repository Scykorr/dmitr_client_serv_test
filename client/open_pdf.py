from PyQt5 import QtWidgets, QtCore, QtGui
import pypdfium2 as pdfium


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
    window.show()
    application.exec()

open_pdf(2)
