import sqlite3
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from okdialog import Ui_OkDialogWindow


class Ui_AddWindow(object):

    def setupUi(self, AddWindow):
        AddWindow.setObjectName("AddWindow")
        AddWindow.resize(420, 500)
        self.centralwidget = QtWidgets.QWidget(AddWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(16)
        self.headingLabel = QtWidgets.QLabel(self.centralwidget)
        self.headingLabel.setGeometry(QtCore.QRect(20, 20, 110, 30))
        self.headingLabel.setFont(font)
        self.headingLabel.setObjectName("headingLabel")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 60, 110, 370))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        font.setPointSize(12)
        self.pidLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.pidLabel.setObjectName("pidLabel")
        self.pidLabel.setFont(font)
        self.verticalLayout.addWidget(self.pidLabel)
        self.dateLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.dateLabel.setObjectName("dateLabel")
        self.dateLabel.setFont(font)
        self.verticalLayout.addWidget(self.dateLabel)
        self.nameLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.nameLabel.setObjectName("nameLabel")
        self.nameLabel.setFont(font)
        self.verticalLayout.addWidget(self.nameLabel)
        self.diagLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.diagLabel.setObjectName("diagLabel")
        self.diagLabel.setFont(font)
        self.verticalLayout.addWidget(self.diagLabel)
        self.doseLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.doseLabel.setObjectName("doseLabel")
        self.doseLabel.setFont(font)
        self.verticalLayout.addWidget(self.doseLabel)
        self.amtpaidLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.amtpaidLabel.setObjectName("amtpaidLabel")
        self.amtpaidLabel.setFont(font)
        self.verticalLayout.addWidget(self.amtpaidLabel)
        self.amtleftLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.amtleftLabel.setObjectName("amtleftLabel")
        self.amtleftLabel.setFont(font)
        self.verticalLayout.addWidget(self.amtleftLabel)
        self.paymLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.paymLabel.setObjectName("paymLabel")
        self.paymLabel.setFont(font)
        self.verticalLayout.addWidget(self.paymLabel)

        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(150, 60, 250, 370))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pidLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        font.setPointSize(10)
        self.pidLineEdit.setObjectName("pidLineEdit")
        self.pidLineEdit.setFont(font)
        self.verticalLayout_2.addWidget(self.pidLineEdit)
        self.dateEdit = QtWidgets.QDateEdit(self.verticalLayoutWidget_2)
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setDisplayFormat("dd/MM/yyyy")
        self.dateEdit.setDate(QDate.currentDate())
        self.dateEdit.setFont(font)
        self.verticalLayout_2.addWidget(self.dateEdit)
        self.nameLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.nameLineEdit.setFont(font)
        self.verticalLayout_2.addWidget(self.nameLineEdit)
        self.diagLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.diagLineEdit.setObjectName("diagLineEdit")
        self.diagLineEdit.setFont(font)
        self.verticalLayout_2.addWidget(self.diagLineEdit)
        self.doseLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.doseLineEdit.setObjectName("doseLineEdit")
        self.doseLineEdit.setFont(font)
        self.verticalLayout_2.addWidget(self.doseLineEdit)
        self.amtpaidLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.amtpaidLineEdit.setObjectName("amtpaidLineEdit")
        self.amtpaidLineEdit.setFont(font)
        self.verticalLayout_2.addWidget(self.amtpaidLineEdit)
        self.amtleftLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2) 
        self.amtleftLineEdit.setObjectName("amtleftLineEdit")
        self.amtleftLineEdit.setFont(font)
        self.verticalLayout_2.addWidget(self.amtleftLineEdit)
        self.paymLineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget_2)
        self.paymLineEdit.setObjectName("paymLineEdit")
        self.paymLineEdit.setFont(font)
        self.verticalLayout_2.addWidget(self.paymLineEdit)

        font.setPointSize(12)
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(20, 440, 380, 40))
        self.addButton.setObjectName("addButton")
        self.addButton.setFont(font)
        self.addButton.clicked.connect(self.addRec)
        AddWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddWindow)
        QtCore.QMetaObject.connectSlotsByName(AddWindow)

    def retranslateUi(self, AddWindow):
        _translate = QtCore.QCoreApplication.translate
        AddWindow.setWindowTitle(_translate("AddWindow", "PMS: Add a Record"))
        self.headingLabel.setText(_translate("AddWindow", "Add Record"))
        self.pidLabel.setText(_translate("AddWindow", "PID:"))
        self.dateLabel.setText(_translate("AddWindow", "Date:"))
        self.nameLabel.setText(_translate("AddWindow", "Name:"))
        self.diagLabel.setText(_translate("AddWindow", "Diagnosis:"))
        self.doseLabel.setText(_translate("AddWindow", "Dose:"))
        self.amtpaidLabel.setText(_translate("AddWindow", "Amount Paid:"))
        self.amtleftLabel.setText(_translate("AddWindow", "Amount Left:"))
        self.paymLabel.setText(_translate("AddWindow", "Payment Mode:"))
        self.addButton.setText(_translate("AddWindow", "Add"))

    def addRec(self):
        pidInput = self.pidLineEdit.text()
        dateInput = self.dateEdit.text()
        nameInput = self.nameLineEdit.text()
        diagInput = self.diagLineEdit.text()
        doseInput = self.doseLineEdit.text()
        amtpaidInput = self.amtpaidLineEdit.text()
        amtleftInput = self.amtleftLineEdit.text()
        paymInput = self.paymLineEdit.text()

        if amtpaidInput == "":
            amtpaidInput = np.NaN
        
        if amtleftInput == "":
            amtleftInput = np.NaN
        

        connobj = sqlite3.connect('patient.db')
        mycursor = connobj.cursor()
        mycursor.execute("INSERT INTO Patient VALUES(?,?,?,?,?,?,?,?)", (pidInput, dateInput, nameInput, diagInput, doseInput, amtpaidInput, amtleftInput, paymInput))
        connobj.commit()
        print('Successfully Inserted Record.')
        connobj.close()
        self.okDialogWindow = QtWidgets.QMainWindow()
        self.ui = Ui_OkDialogWindow()
        self.ui.setupUi(self.okDialogWindow)
        self.okDialogWindow.show()

        self.pidLineEdit.clear()
        self.dateEdit.clear()
        self.nameLineEdit.clear()
        self.diagLineEdit.clear()
        self.doseLineEdit.clear()
        self.amtpaidLineEdit.clear()
        self.amtleftLineEdit.clear()
        self.paymLineEdit.clear()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddWindow = QtWidgets.QMainWindow()
    ui = Ui_AddWindow()
    ui.setupUi(AddWindow)
    AddWindow.show()
    sys.exit(app.exec_())