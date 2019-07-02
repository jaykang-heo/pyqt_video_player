# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'poseVideo.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_poseVideoClass(object):
    def setupUi(self, poseVideoClass):
        poseVideoClass.setObjectName("poseVideoClass")
        poseVideoClass.resize(1118, 733)
        self.centralWidget = QtWidgets.QWidget(poseVideoClass)
        self.centralWidget.setObjectName("centralWidget")
        self.slider = QtWidgets.QSlider(self.centralWidget)
        self.slider.setGeometry(QtCore.QRect(20, 600, 961, 22))
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setObjectName("slider")
        self.display = QtWidgets.QLabel(self.centralWidget)
        self.display.setEnabled(True)
        self.display.setGeometry(QtCore.QRect(21, 11, 531, 551))
        self.display.setToolTipDuration(23)
        self.display.setFrameShape(QtWidgets.QFrame.Box)
        self.display.setText("")
        self.display.setObjectName("display")
        self.display_second = QtWidgets.QLabel(self.centralWidget)
        self.display_second.setGeometry(QtCore.QRect(564, 11, 531, 551))
        self.display_second.setToolTipDuration(23)
        self.display_second.setFrameShape(QtWidgets.QFrame.Box)
        self.display_second.setText("")
        self.display_second.setObjectName("display_second")
        self.progresslabel = QtWidgets.QLabel(self.centralWidget)
        self.progresslabel.setGeometry(QtCore.QRect(1010, 600, 83, 16))
        self.progresslabel.setObjectName("progresslabel")
        self.playButton = QtWidgets.QPushButton(self.centralWidget)
        self.playButton.setGeometry(QtCore.QRect(100, 640, 75, 23))
        self.playButton.setObjectName("playButton")
        self.stopButton = QtWidgets.QPushButton(self.centralWidget)
        self.stopButton.setGeometry(QtCore.QRect(180, 640, 75, 23))
        self.stopButton.setObjectName("stopButton")
        self.startline = QtWidgets.QLineEdit(self.centralWidget)
        self.startline.setGeometry(QtCore.QRect(703, 640, 91, 20))
        self.startline.setObjectName("startline")
        self.endline = QtWidgets.QLineEdit(self.centralWidget)
        self.endline.setGeometry(QtCore.QRect(813, 640, 91, 20))
        self.endline.setObjectName("endline")
        self.exportLabel = QtWidgets.QLabel(self.centralWidget)
        self.exportLabel.setGeometry(QtCore.QRect(1010, 640, 101, 16))
        self.exportLabel.setObjectName("exportLabel")
        self.progressLabel_2 = QtWidgets.QLabel(self.centralWidget)
        self.progressLabel_2.setGeometry(QtCore.QRect(800, 641, 21, 16))
        self.progressLabel_2.setObjectName("progressLabel_2")
        self.exportButton = QtWidgets.QPushButton(self.centralWidget)
        self.exportButton.setGeometry(QtCore.QRect(920, 637, 75, 23))
        self.exportButton.setObjectName("exportButton")
        self.browseButton = QtWidgets.QPushButton(self.centralWidget)
        self.browseButton.setGeometry(QtCore.QRect(20, 640, 75, 23))
        self.browseButton.setObjectName("browseButton")
        self.gotoLine = QtWidgets.QLineEdit(self.centralWidget)
        self.gotoLine.setGeometry(QtCore.QRect(260, 640, 71, 20))
        self.gotoLine.setObjectName("gotoLine")
        self.gotoButton = QtWidgets.QPushButton(self.centralWidget)
        self.gotoButton.setGeometry(QtCore.QRect(335, 639, 75, 23))
        self.gotoButton.setObjectName("gotoButton")
        poseVideoClass.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(poseVideoClass)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1118, 21))
        self.menuBar.setObjectName("menuBar")
        poseVideoClass.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(poseVideoClass)
        self.mainToolBar.setObjectName("mainToolBar")
        poseVideoClass.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(poseVideoClass)
        self.statusBar.setObjectName("statusBar")
        poseVideoClass.setStatusBar(self.statusBar)
        self.actionOpen = QtWidgets.QAction(poseVideoClass)
        self.actionOpen.setObjectName("actionOpen")

        self.retranslateUi(poseVideoClass)
        QtCore.QMetaObject.connectSlotsByName(poseVideoClass)

    def retranslateUi(self, poseVideoClass):
        _translate = QtCore.QCoreApplication.translate
        poseVideoClass.setWindowTitle(_translate("poseVideoClass", "poseVideo"))
        self.progresslabel.setText(_translate("poseVideoClass", "Current / Total"))
        self.playButton.setText(_translate("poseVideoClass", "Play"))
        self.stopButton.setText(_translate("poseVideoClass", "Pause"))
        self.exportLabel.setText(_translate("poseVideoClass", "Current / Total"))
        self.progressLabel_2.setText(_translate("poseVideoClass", "-"))
        self.exportButton.setText(_translate("poseVideoClass", "Export"))
        self.browseButton.setText(_translate("poseVideoClass", "Browse"))
        self.gotoButton.setText(_translate("poseVideoClass", "Go to"))
        self.actionOpen.setText(_translate("poseVideoClass", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    poseVideoClass = QtWidgets.QMainWindow()
    ui = Ui_poseVideoClass()
    ui.setupUi(poseVideoClass)
    poseVideoClass.show()
    sys.exit(app.exec_())
