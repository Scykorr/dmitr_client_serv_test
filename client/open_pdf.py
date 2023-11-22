from PyQt5 import QtWidgets, QtCore, QtGui
import pypdfium2 as pdfium



class OpenPdf(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.choose_test_window = None
        self.ui_client_login = Ui_Form_client_login()
        self.ui_client_login.setupUi(self)
        self.ui_client_login.pushButton_fio.clicked.connect(self.send_fio)
        self.student_fio = ''

    def send_fio(self):
        self.student_fio = self.ui_client_login.lineEdit_fio.text()
        user_name.append(self.student_fio)
        self.choose_test_window = WindowChooseTest(ip_address_server, user_name)
        Client(ip_address_server, 7000).connect("insert into user(fio_user) values ('{0}')".format(
            self.student_fio,
        ))
        self.hide()
        self.choose_test_window.show()

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
