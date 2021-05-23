import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from okdialog import Ui_OkDialogWindow


class Ui_DelWindow(object):

    def setupUi(self, DelWindow):
        DelWindow.setObjectName("DelWindow")
        DelWindow.resize(360, 200)
        self.centralwidget = QtWidgets.QWidget(DelWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setPointSize(16)
        self.headingLabel = QtWidgets.QLabel(self.centralwidget)
        self.headingLabel.setGeometry(QtCore.QRect(20, 20, 150, 30))
        self.headingLabel.setFont(font)
        self.headingLabel.setObjectName("headingLabel")
        
        font.setPointSize(12)
        self.pidLabel = QtWidgets.QLabel(self.centralwidget)
        self.pidLabel.setGeometry(QtCore.QRect(20, 80, 90, 30))
        self.pidLabel.setFont(font)
        self.pidLabel.setObjectName("pidLabel")
        
        font.setPointSize(10)
        self.pidLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.pidLineEdit.setGeometry(QtCore.QRect(100, 80, 240, 30))
        self.pidLineEdit.setFont(font)
        self.pidLineEdit.setObjectName("pidLineEdit")

        font.setPointSize(12)
        self.delButton = QtWidgets.QPushButton(self.centralwidget)
        self.delButton.setGeometry(QtCore.QRect(20, 140, 320, 40))
        self.delButton.setObjectName("delButton")
        self.delButton.setFont(font)
        self.delButton.clicked.connect(self.delRec)
        DelWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DelWindow)
        QtCore.QMetaObject.connectSlotsByName(DelWindow)

    def retranslateUi(self, DelWindow):
        _translate = QtCore.QCoreApplication.translate
        DelWindow.setWindowTitle(_translate("DelWindow", "PMS: Delete Records"))
        self.headingLabel.setText(_translate("DelWindow", "Delete Records"))
        self.pidLabel.setText(_translate("DelWindow", "PID:"))
        self.delButton.setText(_translate("DelWindow", "Delete"))

    def delRec(self):
        pidInput = self.pidLineEdit.text()

        connobj = sqlite3.connect('patient.db')
        mycursor = connobj.cursor()
        mycursor.execute("DELETE FROM Patient WHERE Pid=?", (pidInput,))
        connobj.commit()
        print('Successfully Deleted Record.')
        connobj.close()
        self.okDialogWindow = QtWidgets.QMainWindow()
        self.ui = Ui_OkDialogWindow()
        self.ui.setupUi(self.okDialogWindow)
        self.okDialogWindow.show()

        self.pidLineEdit.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DelWindow = QtWidgets.QMainWindow()
    ui = Ui_DelWindow()
    ui.setupUi(DelWindow)
    DelWindow.show()
    sys.exit(app.exec_())
