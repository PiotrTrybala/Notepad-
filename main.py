import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *

class NotepadPPP(QMainWindow):
    def __init__(self):
        super().__init__()

        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)

        self.fontSizeBox = QSpinBox(self)

        self.createToolBar()
        self.editor.setFontPointSize(24.0)

        self.setWindowTitle("Notepad+++")
        self.showMaximized()


    def createToolBar(self):
        toolbar = QToolBar()

        undoBtn = QAction(QIcon('./icons/undo.svg'), 'Undo', self)
        undoBtn.triggered.connect(self.editor.undo)
        toolbar.addAction(undoBtn)

        redoBtn = QAction(QIcon('./icons/redo.svg'), 'Redo', self)
        redoBtn.triggered.connect(self.editor.redo)
        toolbar.addAction(redoBtn)

        cutBtn = QAction(QIcon('./icons/cut.svg'), 'Cut', self)
        cutBtn.triggered.connect(self.editor.cut)
        toolbar.addAction(cutBtn)

        copyBtn = QAction(QIcon('./icons/copy.svg'), 'Copy', self)
        copyBtn.triggered.connect(self.editor.copy)
        toolbar.addAction(copyBtn)

        pasteBtn = QAction(QIcon('./icons/paste.svg'), 'Paste', self)
        pasteBtn.triggered.connect(self.editor.paste)
        toolbar.addAction(pasteBtn)
        
        self.fontSizeBox.setValue(24.0)
        self.fontSizeBox.valueChanged.connect(self.fontSizeBox)

        self.addToolBar(toolbar)

    def setFontSize(self):
        value = self.fontSizeBox.value()
        self.editor.setFontPointSize(value)
        pass

app = QApplication(sys.argv)
window = NotepadPPP()
window.show()
sys.exit(app.exec())