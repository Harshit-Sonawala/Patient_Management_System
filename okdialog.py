from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OkDialogWindow(object):
    def setupUi(self, OkDialogWindow):
        OkDialogWindow.setObjectName("OkDialogWindow")
        OkDialogWindow.resize(620, 150)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(OkDialogWindow.sizePolicy().hasHeightForWidth())
        OkDialogWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(OkDialogWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 30, 600, 30))
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        font.setPointSize(13)
        self.okButton = QtWidgets.QPushButton(self.centralwidget)
        self.okButton.setGeometry(QtCore.QRect(265, 90, 80, 25))
        self.okButton.setObjectName("okButton")
        self.okButton.setFont(font)
        self.okButton.clicked.connect(lambda:OkDialogWindow.close())
        OkDialogWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(OkDialogWindow)
        QtCore.QMetaObject.connectSlotsByName(OkDialogWindow)

    def retranslateUi(self, OkDialogWindow):
        _translate = QtCore.QCoreApplication.translate
        OkDialogWindow.setWindowTitle(_translate("OkDialogWindow", "Operation Successful"))
        self.label.setText(_translate("OkDialogWindow", "Sucessfully completed. Please refresh the table to view the updated records."))
        self.okButton.setText(_translate("OkDialogWindow", "OK"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    OkDialogWindow = QtWidgets.QMainWindow()
    ui = Ui_OkDialogWindow()
    ui.setupUi(OkDialogWindow)
    OkDialogWindow.show()
    sys.exit(app.exec_())
