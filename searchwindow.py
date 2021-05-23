import sqlite3
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

class Ui_SearchWindow(object):
    def setupUi(self, SearchWindow):
        SearchWindow.setObjectName("SearchWindow")
        SearchWindow.resize(880, 500)
        self.centralwidget = QtWidgets.QWidget(SearchWindow)
        self.centralwidget.setObjectName("centralwidget")

        font = QtGui.QFont()
        font.setPointSize(16)
        self.headingLabel = QtWidgets.QLabel(self.centralwidget)
        self.headingLabel.setGeometry(QtCore.QRect(20, 10, 150, 30))
        self.headingLabel.setFont(font)
        self.headingLabel.setObjectName("headingLabel")
        
        font.setPointSize(12)
        self.searchComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.searchComboBox.setGeometry(QtCore.QRect(20, 60, 120, 35))
        self.searchComboBox.setObjectName("searchComboBox")
        self.searchComboBox.setFont(font)
        self.searchComboBox.addItems(["PID","Name"])
        #self.searchComboBox.currentIndexChanged.connect(self.selectionChange)

        self.finalSearchButton = QtWidgets.QPushButton(self.centralwidget)
        self.finalSearchButton.setGeometry(QtCore.QRect(550, 60, 150, 35))
        self.finalSearchButton.setObjectName("finalSearchButton")
        self.finalSearchButton.setFont(font)
        self.finalSearchButton.clicked.connect(self.searchPressed)

        font.setPointSize(11)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(150, 60, 390, 35))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setFont(font)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.searchTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.searchTableWidget.setGeometry(QtCore.QRect(20, 110, 840, 360))
        self.searchTableWidget.setObjectName("searchTableWidget")
        self.searchTableWidget.setAlternatingRowColors(True)
        self.searchTableWidget.setFont(font)
        SearchWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SearchWindow)
        self.searchComboBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SearchWindow)

    def retranslateUi(self, SearchWindow):
        _translate = QtCore.QCoreApplication.translate
        SearchWindow.setWindowTitle(_translate("SearchWindow", "PMS: Search Records"))
        self.headingLabel.setText(_translate("SearchWindow", "Search Records"))
        self.finalSearchButton.setText(_translate("SearchWindow", "Search"))

    '''
    def selectionChange(self, i):
        print("Current index: ", i)
    '''    

    def searchPressed(self):
        currIndex = self.searchComboBox.currentIndex()
        searchColumn = self.searchComboBox.currentText()
        searchRow = self.lineEdit.text()
        #print("value when pressed: where ", searchColumn, searchRow)
        connobj = sqlite3.connect('patient.db')
        mycursor = connobj.cursor()

        if currIndex == 0:
            mycursor.execute('SELECT * FROM Patient WHERE PID=?', (searchRow,))
        else:
            mycursor.execute("""SELECT * FROM Patient WHERE Name LIKE ('%'||?||'%')""", (searchRow,))
        queryop = mycursor.fetchall()
        #print(queryop)

        rowcount = len(queryop)
        column_names = [i[0] for i in mycursor.description]
        colcount = len(column_names)

        self.searchTableWidget.setColumnCount(colcount)
        self.searchTableWidget.setRowCount(rowcount)
        font = QtGui.QFont()
        font.setPointSize(12)
        for i in range(0, rowcount):
            item = QtWidgets.QTableWidgetItem()
            item.setFont(font)
            self.searchTableWidget.setVerticalHeaderItem(i, item)
            item = self.searchTableWidget.verticalHeaderItem(i)

            item.setText(str(i+1))
        for i in range(0, colcount):
            item = QtWidgets.QTableWidgetItem()
            item.setFont(font)
            self.searchTableWidget.setHorizontalHeaderItem(i, item)
            item = self.searchTableWidget.horizontalHeaderItem(i)
            item.setText(column_names[i])
        for row in queryop:
            inx = queryop.index(row)
            #self.searchTableWidget.insertRow(inx)
            for j in range(0, colcount):
                self.searchTableWidget.setItem(inx, j, QTableWidgetItem(str(row[j])))

        connobj.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SearchWindow = QtWidgets.QMainWindow()
    ui = Ui_SearchWindow()
    ui.setupUi(SearchWindow)
    SearchWindow.show()
    sys.exit(app.exec_())
