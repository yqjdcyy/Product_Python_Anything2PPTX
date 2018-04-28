import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QApplication, QCheckBox, QComboBox, QFileDialog,
                             QGridLayout, QLabel, QLineEdit, QPushButton,
                             QSizePolicy, QSpinBox, QWidget)

from log import ACOLogger

# Params
types = ["PDF2PPTX", "PDF2IMAGES", "IMAGES2PPTX"]
extensions = ["jpeg"]
logger = ACOLogger().logger


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("转换工具 V1.0")
        self.setWindowIcon(QtGui.QIcon("resource/black.ico"))
        self.width = 400
        self.height = 720
        self.Init_UI()

    def Init_UI(self):

        grid = QGridLayout()
        self.setLayout(grid)

        # Type
        lType = QLabel("Function:")
        grid.addWidget(lType, 0, 0, 1, 2)
        self.cbType = QComboBox(self)
        self.cbType.addItems(types)
        grid.addWidget(self.cbType, 0, 2, 1, 9)
        self.cbType.activated[str].connect(self.CBTypeActivate)

        # Resource
        lSrc = QLabel(self)
        lSrc.setText("Resource:")
        grid.addWidget(lSrc, 1, 0, 1, 2)
        self.leSrc = QLineEdit(self)
        grid.addWidget(self.leSrc, 1, 2, 1, 7)
        self.leSrc.textChanged[str].connect(self.LESrcChanged)
        bChooseSrc = QPushButton("Choose")
        grid.addWidget(bChooseSrc, 1, 9, 1, 2)
        bChooseSrc.clicked.connect(self.BSrcClicked)

        # Destination
        lDest = QLabel(self)
        lDest.setText("Destination:")
        grid.addWidget(lDest, 2, 0, 1, 2)
        self.leDest = QLineEdit(self)
        grid.addWidget(self.leDest, 2, 2, 1, 7)
        self.leDest.textChanged[str].connect(self.LESrcChanged)
        bChooseDest = QPushButton("Choose")
        grid.addWidget(bChooseDest, 2, 9, 1, 2)
        bChooseDest.clicked.connect(self.BDestClicked)

        # PDF.DPI
        lDPI = QLabel(self)
        lDPI.setText("DPI:")
        grid.addWidget(lDPI, 3, 0, 1, 2)
        self.sbDPI = QSpinBox(self)
        self.sbDPI.setRange(0, 200)
        self.sbDPI.setSingleStep(1)
        self.sbDPI.setValue(96)
        self.sbDPI.setWrapping(True)
        grid.addWidget(self.sbDPI, 3, 2, 1, 9)

        # PDF.Extension
        lExt = QLabel(self)
        lExt.setText("Extension:")
        grid.addWidget(lExt, 4, 0, 1, 2)
        self.cbExt = QComboBox(self)
        self.cbExt.addItems(extensions)
        grid.addWidget(self.cbExt, 4, 2, 1, 9)
        self.cbExt.activated[str].connect(self.CBTypeActivate)

        # PPTX.Template
        lTemp = QLabel(self)
        lTemp.setText("PPTX.Template:")
        grid.addWidget(lTemp, 5, 0, 1, 2)
        self.leTemp = QLineEdit(self)
        grid.addWidget(self.leTemp, 5, 2, 1, 7)
        self.leTemp.textChanged[str].connect(self.LESrcChanged)
        self.bChooseTemp = QPushButton("Choose")
        grid.addWidget(self.bChooseTemp, 5, 9, 1, 2)
        self.bChooseTemp.clicked.connect(self.BTempClicked)

        # PPTX.Open
        lOpen = QLabel(self)
        lOpen.setText("Folder.Open:")
        grid.addWidget(lOpen, 6, 0, 1, 2)
        self.cbOpen = QCheckBox(self)
        self.cbOpen.setText("OpenAfterConvert")
        # self.cbOpen.setDown(False)
        self.cbOpen.setChecked(True)
        grid.addWidget(self.cbOpen, 6, 2, 1, 2)

        # Button
        self.btnOK = QPushButton(self)
        self.btnOK.setEnabled(True)
        # self.btnOK.setText("Run")
        grid.addWidget(self.btnOK, 0, 11, 7, 1)
        self.btnOK.setSizePolicy(
            QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.btnOK.setStyleSheet("background-color: #ccc")
        self.btnOK.setIcon(QtGui.QIcon("resource/run.gif"))
        self.btnOK.setIconSize(QtCore.QSize(60, 60))
        self.btnOK.clicked.connect(self.Run)

        # Result
        self.result = QLabel()
        grid.addWidget(self.result, 10, 0, 1, 0)
        grid.setSpacing(10)

        # Status.Control
        self.Control()

        # Show
        self.show()

    def Control(self):

        t = self.cbType.currentText()
        if t == types[0]:
            self.sbDPI.setEnabled(True)
            self.cbExt.setEnabled(True)
            self.leTemp.setEnabled(True)
            self.bChooseTemp.setEnabled(True)
            self.cbOpen.setEnabled(True)
        elif t == types[1]:
            self.sbDPI.setEnabled(True)
            self.cbExt.setEnabled(True)
            self.leTemp.setEnabled(False)
            self.bChooseTemp.setEnabled(False)
            self.cbOpen.setEnabled(False)
        elif t == types[2]:
            self.sbDPI.setEnabled(False)
            self.cbExt.setEnabled(False)
            self.leTemp.setEnabled(True)
            self.bChooseTemp.setEnabled(True)
            self.cbOpen.setEnabled(True)
        else:
            self.sbDPI.setEnabled(False)
            self.cbExt.setEnabled(False)
            self.leTemp.setEnabled(False)
            self.bChooseTemp.setEnabled(False)
            self.cbOpen.setEnabled(False)

        self.btnOK.setEnabled(False)
        if self.leSrc.text():
            self.btnOK.setEnabled(True)

    def BTempClicked(self):
        options = QFileDialog.Options() | QFileDialog.DontUseNativeDialog
        path, _ = QFileDialog.getOpenFileName(
            self,
            "Choose *.ppt*",
            "D:/work/git/yao/python/Utils_Python_Anything2PPTX/resource",
            "PPTX Files(*.ppt *.pptx)",
            options=options)
        if path:
            self.leTemp.setText(path)

    def BDestClicked(self):
        path = QFileDialog.getExistingDirectory(
            self, "Select images.directory")
        if path:
            self.leDest.setText(path)

    def BSrcClicked(self):
        options = QFileDialog.Options() | QFileDialog.DontUseNativeDialog
        t = self.cbType.currentText()
        path = ""
        if t == types[0] or t == types[1]:
            path, _ = QFileDialog.getOpenFileName(
                self,
                "Choose *.pdf",
                "D:/work/git/yao/python/Utils_Python_Anything2PPTX/resource",
                "PDF Files(*.pdf)",
                options=options)
        elif t == types[2]:
            path = QFileDialog.getExistingDirectory(
                self, "Select images.directory")

        if path:
            self.leSrc.setText(path)
            self.Control()

    def LESrcChanged(self, text):
        self.result.setText(text)

    def CBTypeActivate(self, txt):
        self.result.setText(txt)
        self.Control()

    def Run(self):
        # fill
        self.Fill()

        # call
        t = self.cbType.currentText()
        logger.info(t)
        import shell
        if t == types[0]:
            shell.PDF2PPTX()
        elif t == types[1]:
            shell.PDF2IMAGES()
        elif t == types[2]:
            shell.IMAGES2PPTX()

        # TODO yqj
        # Return Error to interface
        self.result.setText(t + " FINISH")

    def Fill(self):

        from config import config as conf
        from config import setting

        conf.src = self.leSrc.text()
        if self.leDest.text():
            conf.dest = self.leDest.text()
        if self.sbDPI.text():
            conf.dpi = self.sbDPI.text()
        if self.cbExt.currentText():
            conf.ext = self.cbExt.currentText()
        conf.open = self.cbOpen.isChecked()
        if self.leTemp.text():
            setting.template = self.leTemp.text()

        logger.info(
            "Launcher.Fill\n\tSrc=\t%s\n\tDest\t=%s\n\tDpi\t=%s\n\tExt\t=%s\n\tOpen\t=%s\n\tTemplate\t=%s",
            conf.src,
            conf.dest,
            conf.dpi,
            conf.ext,
            conf.open,
            setting.template)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    app.exit(app.exec_())
