import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *

class NotepadPPP(QMainWindow):
    def __init__(self):
        super().__init__()

        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)

        self.createToolBar()

        self.setWindowTitle("Notepad+++")
        self.showMaximized()

    def createToolBar(self):
        toolbar = QToolBar()
        self.addToolBar(toolbar)

app = QApplication(sys.argv)
window = NotepadPPP()
window.show()
sys.exit(app.exec())