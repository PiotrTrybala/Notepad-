import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *

class NotepadPPP(QMainWindow):
    def __init__(self):
        super().__init__()

app = QApplication(sys.argv)
window = NotepadPPP()
window.show()
sys.exit(app.exec())