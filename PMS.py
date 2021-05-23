import sqlite3
import numpy as np
import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
#from okdialog import Ui_OkDialogWindow
from searchwindow import Ui_SearchWindow
from addwindow import Ui_AddWindow
from delwindow import Ui_DelWindow
from graphwindow import Ui_GraphWindow

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(910, 760)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        font = QtGui.QFont()
        font.setPointSize(17)
        self.headingLabel = QtWidgets.QLabel(self.centralwidget)
        self.headingLabel.setGeometry(QtCore.QRect(30, 10, 280, 30))
        self.headingLabel.setFont(font)
        self.headingLabel.setObjectName("headingLabel")

        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 50, 870, 70))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")

        font = QtGui.QFont()
        font.setPointSize(12)
        self.openFileButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.openFileButton.sizePolicy().hasHeightForWidth())
        self.openFileButton.setSizePolicy(sizePolicy)
        self.openFileButton.setMaximumSize(QtCore.QSize(200, 40))
        self.openFileButton.setFont(font)
        self.openFileButton.setObjectName("openFileButton")
        self.openFileButton.clicked.connect(self.openFile)
        self.horizontalLayout.addWidget(self.openFileButton)

        self.saveFileButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.saveFileButton.sizePolicy().hasHeightForWidth())
        self.saveFileButton.setSizePolicy(sizePolicy)
        self.saveFileButton.setMaximumSize(QtCore.QSize(200, 40))
        self.saveFileButton.setFont(font)
        self.saveFileButton.setObjectName("saveFileButton")
        self.saveFileButton.clicked.connect(self.saveFile)
        self.saveFileButton.setDisabled(True)
        self.horizontalLayout.addWidget(self.saveFileButton)
        
        self.searchButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchButton.sizePolicy().hasHeightForWidth())
        self.searchButton.setSizePolicy(sizePolicy)
        self.searchButton.setMaximumSize(QtCore.QSize(200, 40))
        self.searchButton.setFont(font)
        self.searchButton.setObjectName("searchButton")
        self.searchButton.clicked.connect(self.searchRecord)
        self.searchButton.setDisabled(True)
        self.horizontalLayout.addWidget(self.searchButton)
        
        self.addRecordButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addRecordButton.sizePolicy().hasHeightForWidth())
        self.addRecordButton.setSizePolicy(sizePolicy)
        self.addRecordButton.setMaximumSize(QtCore.QSize(200, 40))
        self.addRecordButton.setFont(font)
        self.addRecordButton.setObjectName("addRecordButton")
        self.addRecordButton.clicked.connect(self.addRecord)
        self.addRecordButton.setDisabled(True)
        self.horizontalLayout.addWidget(self.addRecordButton)
        
        self.delRecordButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delRecordButton.sizePolicy().hasHeightForWidth())
        self.delRecordButton.setSizePolicy(sizePolicy)
        self.delRecordButton.setMaximumSize(QtCore.QSize(200, 40))
        self.delRecordButton.setFont(font)
        self.delRecordButton.setObjectName("delRecordButton")
        self.delRecordButton.clicked.connect(self.deleteRecord)
        self.delRecordButton.setDisabled(True)
        self.horizontalLayout.addWidget(self.delRecordButton)

        self.refreshButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.refreshButton.sizePolicy().hasHeightForWidth())
        self.refreshButton.setSizePolicy(sizePolicy)
        self.refreshButton.setMaximumSize(QtCore.QSize(200, 40))
        self.refreshButton.setFont(font)
        self.refreshButton.setObjectName("refreshButton")
        self.refreshButton.clicked.connect(self.refreshTable)
        self.refreshButton.setDisabled(True)
        self.horizontalLayout.addWidget(self.refreshButton)

        self.clearButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearButton.sizePolicy().hasHeightForWidth())
        self.clearButton.setSizePolicy(sizePolicy)
        self.clearButton.setMaximumSize(QtCore.QSize(200, 40))
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.clearButton.clicked.connect(self.clearTable)
        self.clearButton.setDisabled(True)
        self.horizontalLayout.addWidget(self.clearButton)

        font = QtGui.QFont()
        font.setPointSize(10)

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(30, 120, 850, 570))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setAlternatingRowColors(True)
        #self.tableWidget.setStyleSheet(u"font-family: Poppins;")
        self.tableWidget.setFont(font)

        font.setPointSize(12)
        self.totalLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalLabel.setGeometry(QtCore.QRect(40, 715, 100, 20))
        self.totalLabel.setFont(font)
        self.totalLabel.setObjectName("totalLabel")
        self.totalValueLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalValueLabel.setGeometry(QtCore.QRect(140, 715, 150, 20))
        self.totalValueLabel.setFont(font)
        self.totalValueLabel.setObjectName("totalValueLabel")

        self.pendingLabel = QtWidgets.QLabel(self.centralwidget)
        self.pendingLabel.setGeometry(QtCore.QRect(240, 715, 100, 20))
        self.pendingLabel.setFont(font)
        self.pendingLabel.setObjectName("pendingLabel")
        self.totalPendingLabel = QtWidgets.QLabel(self.centralwidget)
        self.totalPendingLabel.setGeometry(QtCore.QRect(340, 715, 150, 20))
        self.totalPendingLabel.setFont(font)
        self.totalPendingLabel.setObjectName("totalPendingLabel")

        self.saveEditsButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveEditsButton.setGeometry(QtCore.QRect(450, 705, 200, 40))
        self.saveEditsButton.setObjectName("saveEditsButton")
        self.saveEditsButton.setFont(font)
        self.saveEditsButton.clicked.connect(self.saveEdits)
        self.saveEditsButton.setDisabled(True)
        self.analyticsButton = QtWidgets.QPushButton(self.centralwidget)
        self.analyticsButton.setGeometry(QtCore.QRect(680, 705, 200, 40))
        self.analyticsButton.setObjectName("analyticsButton")
        self.analyticsButton.setFont(font)
        self.analyticsButton.clicked.connect(self.getAnalytics)
        self.analyticsButton.setDisabled(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Patient Management System"))
        self.headingLabel.setText(_translate("MainWindow", "Patient Management System"))
        self.openFileButton.setText(_translate("MainWindow", "Open File"))
        self.saveFileButton.setText(_translate("MainWindow", "Save File"))
        self.searchButton.setText(_translate("MainWindow", "Search"))
        self.addRecordButton.setText(_translate("MainWindow", "Add Record"))
        self.delRecordButton.setText(_translate("MainWindow", "Delete Record"))
        self.refreshButton.setText(_translate("MainWindow", "Refresh"))
        self.clearButton.setText(_translate("MainWindow", "Clear"))
        self.totalLabel.setText(_translate("MainWindow", "Total Earnings:"))
        self.totalValueLabel.setText(_translate("MainWindow", "None"))
        self.pendingLabel.setText(_translate("MainWindow", "Total Pending:"))
        self.totalPendingLabel.setText(_translate("MainWindow", "None"))
        self.saveEditsButton.setText(_translate("MainWindow", "Save Edits"))
        self.analyticsButton.setText(_translate("MainWindow", "Get Analytics"))

    def openFile(self):
        file_path, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select Excel File", "", "Microsoft Excel Files (*.xlsx)")
        if file_path:
            final_load_path = file_path
            self.loadRecords(final_load_path)

    def saveFile(self):
        #if data_loaded:
        dataframe = pd.DataFrame()
        file_path, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save Output .xlsx File As", "", "Microsoft Excel Files (*.xlsx)")
        print("Browsing for output file location completed.")
        if file_path:
            final_save_path = file_path
            self.saveRecords(final_save_path)
            '''
            for i in range(self.tableWidget.rowCount()):            
                for j in range(self.tableWidget.columnCount()):
                    if self.tableWidget.item(i,j) == None:
                        dataframe.loc[i, j] = np.NaN
                        #continue
                    else:
                        dataframe.loc[i, j] = str(self.tableWidget.item(i, j).text())
            #get column names:
            connobj = sqlite3.connect('patient.db')
            mycursor = connobj.cursor()
            mycursor.execute('SELECT * FROM Patient')
            #queryop = mycursor.fetchall()
            column_names = [i[0] for i in mycursor.description]
            #save to excel file with column names:
            dataframe.to_excel(file_path, index = False, header = column_names)
            connobj.close()
            '''
        '''
        else:
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_OkDialogWindow()
            self.ui.setupUi(self.window)
            self.window.show()
        '''

    def searchRecord(self, final_load_path):
        self.searchwindow = QtWidgets.QMainWindow()
        self.ui = Ui_SearchWindow()
        self.ui.setupUi(self.searchwindow)
        self.searchwindow.show()
    
    def loadRecords(self, final_load_path):
        connobj = sqlite3.connect('patient.db')
        mycursor = connobj.cursor()

        dataframe = pd.read_excel(final_load_path)
        dataframe.to_sql(name = 'Patient', con = connobj, if_exists = 'replace', index = False)

        mycursor.execute('SELECT * FROM Patient')
        queryop = mycursor.fetchall()
        rowcount = len(queryop)
        column_names = [i[0] for i in mycursor.description]
        colcount = len(column_names)

        self.tableWidget.setColumnCount(colcount)
        self.tableWidget.setRowCount(rowcount)
        font = QtGui.QFont()
        font.setPointSize(12)
        for i in range(0, rowcount):
            item = QtWidgets.QTableWidgetItem()
            item.setFont(font)
            self.tableWidget.setVerticalHeaderItem(i, item)
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(str(i+1))
        for i in range(0, colcount):
            item = QtWidgets.QTableWidgetItem()
            item.setFont(font)
            self.tableWidget.setHorizontalHeaderItem(i, item)
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(column_names[i])
        for row in queryop:
            inx = queryop.index(row)
            #self.tableWidget.insertRow(inx)
            for j in range(0, colcount):
                self.tableWidget.setItem(inx, j, QTableWidgetItem(str(row[j])))
        connobj.close()
        self.loadTotals()
        #enable all the buttons:
        self.saveFileButton.setDisabled(False)
        self.searchButton.setDisabled(False)
        self.addRecordButton.setDisabled(False)
        self.delRecordButton.setDisabled(False)
        self.refreshButton.setDisabled(False)
        self.clearButton.setDisabled(False)
        self.saveEditsButton.setDisabled(False)
        self.analyticsButton.setDisabled(False)

    def saveRecords(self, final_save_path):
        dataframe = pd.DataFrame()
        for i in range(self.tableWidget.rowCount()):            
            for j in range(self.tableWidget.columnCount()):
                tableItem = self.tableWidget.item(i, j)
                if tableItem == None or tableItem.text() == 'None':
                    dataframe.loc[i, j] = np.NaN
                    #continue
                else:
                    if "." in str(tableItem.text()):
                        isNum = tableItem.text().replace('.', '', 1).isnumeric()
                        if isNum:
                            dataframe.loc[i, j] = float(tableItem.text())
                        else:
                            dataframe.loc[i, j] = str(tableItem.text())
                    elif tableItem.text().isnumeric():
                        dataframe.loc[i, j] = int(tableItem.text())
                    else:
                        dataframe.loc[i, j] = str(tableItem.text())
        #get column names:
        connobj = sqlite3.connect('patient.db')
        mycursor = connobj.cursor()
        mycursor.execute('SELECT * FROM Patient')
        column_names = [i[0] for i in mycursor.description]
        #save to excel file with column names:
        connobj.close()
        dataframe.to_excel(final_save_path, index = False, header = column_names)

    def loadTotals(self):
        connobj = sqlite3.connect('patient.db')
        mycursor = connobj.cursor()

        mycursor.execute('SELECT SUM(AmtPaid) FROM Patient')
        queryop = mycursor.fetchall()
        totalValue = str(queryop[0][0])
        self.totalValueLabel.setText(totalValue)

        mycursor.execute('SELECT SUM(AmtLeft) FROM Patient')
        queryop = mycursor.fetchall()
        pendingValue = str(queryop[0][0])
        self.totalPendingLabel.setText(pendingValue)
        connobj.close()

    def addRecord(self):
        self.addwindow = QtWidgets.QMainWindow()
        self.ui = Ui_AddWindow()
        self.ui.setupUi(self.addwindow)
        self.addwindow.show()
        '''
        lastRow = self.tableWidget.rowCount()
        #print(lastRow+1)
        self.tableWidget.insertRow(lastRow)
        '''

    def deleteRecord(self):
        self.delwindow = QtWidgets.QMainWindow()
        self.ui = Ui_DelWindow()
        self.ui.setupUi(self.delwindow)
        self.delwindow.show()
        '''
        lastRow = self.tableWidget.rowCount()
        self.tableWidget.removeRow(lastRow-1)
        '''

    def refreshTable(self):
        self.clearTable()
        connobj = sqlite3.connect('patient.db')
        mycursor = connobj.cursor()

        mycursor.execute('SELECT * FROM Patient')
        queryop = mycursor.fetchall()
        rowcount = len(queryop)
        column_names = [i[0] for i in mycursor.description]
        colcount = len(column_names)

        self.tableWidget.setColumnCount(colcount)
        self.tableWidget.setRowCount(rowcount)
        font = QtGui.QFont()
        font.setPointSize(12)
        for i in range(0, rowcount):
            item = QtWidgets.QTableWidgetItem()
            item.setFont(font)
            self.tableWidget.setVerticalHeaderItem(i, item)
            item = self.tableWidget.verticalHeaderItem(i)

            item.setText(str(i+1))
        for i in range(0, colcount):
            item = QtWidgets.QTableWidgetItem()
            item.setFont(font)
            self.tableWidget.setHorizontalHeaderItem(i, item)
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(column_names[i])
        for row in queryop:
            inx = queryop.index(row)
            #self.tableWidget.insertRow(inx)
            for j in range(0, colcount):
                self.tableWidget.setItem(inx, j, QTableWidgetItem(str(row[j])))
        
        self.loadTotals()
        print("Successfully Refreshed Records.")

    def clearTable(self):
        while (self.tableWidget.rowCount() > 0):
            self.tableWidget.removeRow(0)
        self.totalValueLabel.setText("")
        self.totalPendingLabel.setText("")
        #self.tableWidget.setRowCount(0)
        #self.tableWidget.setColumnCount(0)

    def saveEdits(self):
        temp_file_path = "pms_temp.xlsx"
        self.saveRecords(temp_file_path)
        #loadrecords in db from temp excel file:
        self.loadRecords(temp_file_path)
        
        print("Successfully Saved Table Edits.")
        

    def getAnalytics(self):
        self.graphwindow = QtWidgets.QMainWindow()
        self.ui = Ui_GraphWindow()
        self.ui.setupUi(self.graphwindow)
        self.graphwindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    QtGui.QFontDatabase.addApplicationFont("Jost-Regular.ttf")
    QtGui.QFontDatabase.addApplicationFont("Poppins-Regular.ttf")
    mystylesheet = """
        /**
        *{
            font-family: Jost;
        }
        **/
        QWidget{
            background: #fbfef9;
        }
        QVBoxLayout{
            border: 1px solid #dadfe3;
            border-radius: 10px;
            background: #35aeea;
        }
        QTableWidget{
            font-family: Poppins;
            border: 1px solid #dadfe3;
            border-radius: 10px;
            background-color: #dadfe3
        }
        QTableWidget::item{
            
        }
        QTableWidget::item:hover{
            color: #fbfef9;
            background: #35aeea;
        }
        QHeaderView {
            font-family: Jost;
            background: #dadfe3;
        }
        QHeaderView::section {
            color: #ffffff;
            background-color: #35aeea;
            border: 0.5px solid #fff;
            padding: 2px;
        }
        QHeaderView::section:hover {
            background-color: #5cc6ff;
            border: 0.5px solid #fff;
        }
        QTableWidget QTableCornerButton::section {
            background-color: #35aeea;
            border: 0.5px solid #fff;
        }

        QScrollBar:vertical {
            background: #fbfef9;
            border: 0.5px solid #fff;
            border-radius: 10px;
            width: 12px;
        }
        QScrollBar::handle:vertical {
            background: #dadfe3;
            border: 0.5px solid #dadfe3;
        }
        QScrollBar::handle:vertical:hover {
            background: #35aeea;
        }
        QScrollBar::add-line:vertical {
            height: 0px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical {
            height: 0px;
            subcontrol-position: top;
            subcontrol-origin: margin;
        }

        QScrollBar:horizontal {
            background: #fbfef9;
            border: 0.5px solid #fff;
            border-radius: 10px;
            height: 12px;
        }
        QScrollBar::handle:horizontal {
            background: #dadfe3;
            border: 0.5px solid #dadfe3;
        }
        QScrollBar::handle:horizontal:hover {
            background: #35aeea;
        }
        QScrollBar::add-line:horizontal {
            height: 0px;
            subcontrol-position: right;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:horizontal {
            height: 0px;
            subcontrol-position: left;
            subcontrol-origin: margin;
        }
        QLabel {
            font-family: Jost;
        }
        QLabel#headingLabel, QLabel#totalValueLabel, QLabel#totalPendingLabel{
            color: #35aeea;
        }
        QPushButton {
            font-family: Jost;
            border: 1px solid #dadfe3;
            border-radius: 10px;
            background-color: #dadfe3;
        }
        QPushButton:hover {
            color: #fff;
            border: 1px solid #35aeea;
            border-radius: 10px;
            background: #35aeea;
        }
        QLineEdit, QDateEdit {
            font-family: Poppins;
            border: 1px solid #35aeea;
            border-radius: 8px;
            padding: 2px;
        }
        /**
        QDateEdit::up-arrow, QDateEdit::down-arrow{
            border: 1px solid #dadfe3;
            border-radius: 10px;
            background-color: #dadfe3;
        }
        **/
        QComboBox {
            font-family: Jost;
            background: #dadfe3;
            border: 1px solid #dadfe3;
            border-radius: 8px;
            subcontrol-origin: padding;
            subcontrol-position: top right;
            selection-background-color: #35aeea;
            selection-color: #fff;
        }
        QComboBox::drop-down {
            background: #dadfe3;
            border: 1px solid #dadfe3;
            border-radius: 8px;
        }
    """
    app.setStyleSheet(mystylesheet)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    #data_loaded = True
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
