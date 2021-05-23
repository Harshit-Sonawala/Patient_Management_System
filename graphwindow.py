import sys
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets
from numpy.core.fromnumeric import size

class Canvas(FigureCanvas):
    def __init__(self, parent = None, width = 5, height = 2, dpi = 100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(Canvas, self).__init__(fig)
        
class Ui_GraphWindow(object):
    def setupUi(self, GraphWindow):
        GraphWindow.setObjectName("GraphWindow")
        GraphWindow.resize(900, 600)
        self.centralwidget = QtWidgets.QWidget(GraphWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        connobj = sqlite3.connect('patient.db')
        mycursor = connobj.cursor()
        '''
        mycursor.execute("""SELECT Date, SUM(AmtPaid) FROM Patient GROUP BY Date""")
        queryop = mycursor.fetchall()
        print(queryop)
        '''
        mycursor.execute("""SELECT * FROM Patient""")
        queryop = mycursor.fetchall()
        rowcount = len(queryop)
        date_list = []
        earn_list = []
        pending_list = []
        for i in range(0, rowcount):
            date_list.append(queryop[i][1])
            if queryop[i][5] == None or queryop[i][5] == 'None':
                earn_list.append(0.0)
            else:
                earn_list.append(float(queryop[i][5]))
            
            if queryop[i][6] == None or queryop[i][6] == 'None':
                pending_list.append(0.0)
            else:
                pending_list.append(float(queryop[i][6]))
        connobj.close()
        #print(date_list)
        xValues = np.array(date_list)
        y1Values = np.array(earn_list)
        y2Values = np.array(pending_list)
        myGraph = Canvas(self, width = 10, height = 6, dpi = 100)
        myGraph.axes.grid('#dadfe3')
        myGraph.axes.plot(xValues, y1Values, '#35aeea')
        myGraph.axes.plot(xValues, y2Values, 'red')
        myGraph.axes.set(xlabel='Date', ylabel='Earnings (Rs.)')
        myGraph.axes.set_title('Earnings and Pending Amount by Date', pad = 20)
        myGraph.move(0,10)
        plt.setp(myGraph.axes.get_xticklabels(), fontsize = 8, rotation = 40, horizontalalignment = 'right')
        GraphWindow.setCentralWidget(myGraph)

        # layout = QtWidgets.QVBoxLayout()
        # layout.addWidget(myGraph)
        # layout.addSpacing(200)

        self.retranslateUi(GraphWindow)
        QtCore.QMetaObject.connectSlotsByName(GraphWindow)

    def retranslateUi(self, GraphWindow):
        _translate = QtCore.QCoreApplication.translate
        GraphWindow.setWindowTitle(_translate("GraphWindow", "PMS: Analytics"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GraphWindow = QtWidgets.QMainWindow()
    ui = Ui_GraphWindow()
    ui.setupUi(GraphWindow)
    GraphWindow.show()
    sys.exit(app.exec_())
