import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *

class NotepadPPP(QMainWindow):
    def __init__(self):
        super().__init__()

        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)

        self.fontSizeBox = QSpinBox()

        font = QFont('Times', 24)

        self.path = ""

        self.editor.setFont(font)
        self.editor.setFontPointSize(24.0)


        self.createToolBar()

        self.setWindowTitle("Notepad+++")
        self.showMaximized()


    def createToolBar(self):
        toolbar = QToolBar()

        saveBtn = QAction(QIcon('./icons/save.svg'), 'Save', self)
        saveBtn.triggered.connect(self.saveFile)
        toolbar.addAction(saveBtn)

        openBtn = QAction(QIcon('./icons/file_open.svg'), 'Save', self)
        openBtn.triggered.connect(self.openFile)
        toolbar.addAction(openBtn)

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

        leftAlign = QAction(QIcon('./icons/align_left.svg'), 'Align left', self)
        leftAlign.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignmentFlag.AlignLeft))
        toolbar.addAction(leftAlign)

        centerAlign = QAction(QIcon('./icons/align_center.svg'), 'Align center', self)
        centerAlign.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignmentFlag.AlignCenter))
        toolbar.addAction(centerAlign)

        rightAlign = QAction(QIcon('./icons/align_right.svg'), 'Align right', self)
        rightAlign.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignmentFlag.AlignRight))
        toolbar.addAction(rightAlign)

        justify = QAction(QIcon('./icons/align_justify.svg'), 'Justify', self)
        justify.triggered.connect(lambda: self.editor.setAlignment(Qt.AlignmentFlag.AlignJustify))
        toolbar.addAction(justify)

        boldBtn = QAction(QIcon('./icons/bold.svg'), 'Bold', self)
        boldBtn.triggered.connect(self.boldText)
        toolbar.addAction(boldBtn)

        italicBtn = QAction(QIcon('./icons/italic.svg'), 'Italic', self)
        italicBtn.triggered.connect(self.italicText)
        toolbar.addAction(italicBtn)

        underlineBtn = QAction(QIcon('./icons/underlined.svg'), 'Underline', self)
        underlineBtn.triggered.connect(self.underlineText)
        toolbar.addAction(underlineBtn)

        self.fontBox = QComboBox(self)
        self.fontBox.addItems(["Courier Std", "Hellentic Typewriter Regular", "Helvetica", "Arial", "SansSerif", "Helvetica", "Times", "Monospace"])
        self.fontBox.activated.connect(self.setFont)
        toolbar.addWidget(self.fontBox)

        self.fontSizeBox.setValue(24)
        self.fontSizeBox.valueChanged.connect(self.setFontSize)

        toolbar.addWidget(self.fontSizeBox)

        self.addToolBar(toolbar)

    def saveFile(self):
        print(self.path)

        if self.path == "":
            self.fileSaveAs()
        else:
            self.writeFile()

    def writeFile(self):
        text = self.editor.toPlainText()
        try:
            with open(self.path, 'w') as f:
                f.write(text)
                self.updateTitle()
        except Exception as e:
            print(e)

    def updateTitle(self):

        if self.path != "":
            self.setWindowTitle(f"Notepad+++ - {self.path}")

    def fileSaveAs(self):

        self.path, _ = QFileDialog.getSaveFileName(
            self,
            "Save file",
            "",
            "Text Documents (*.text, *.txt); All files (*.*)"
        )

        print(self.path)

        self.writeFile()

    def openFile(self):
        pass

    def setFontSize(self):
        value = self.fontSizeBox.value()
        self.editor.setFontPointSize(value)

    def setFont(self):
        value = self.fontBox.currentText()
        self.editor.setCurrentFont(QFont(value, int(self.editor.fontPointSize())))

    def boldText(self):
        if self.editor.fontWeight() != QFont.Weight.Bold:
            self.editor.setFontWeight(QFont.Weight.Bold)
        else:
            self.editor.setFontWeight(QFont.Weight.Normal)

    def italicText(self):
        state = self.editor.fontItalic()
        self.editor.setFontItalic(not(state))

    def underlineText(self):
        state = self.editor.fontUnderline()
        self.editor.setFontUnderline(not(state))

app = QApplication(sys.argv)
window = NotepadPPP()
window.show()
sys.exit(app.exec())