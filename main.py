import sys
from PyQt5 import QtWidgets
import design
import random

class MatrixApp(QtWidgets.QMainWindow, design.Ui_Matrix):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.randomiseMatrix.clicked.connect(self.newMatrix)
        self.pushButton_2.clicked.connect(self.showMatrix)
        self.showMinimum.clicked.connect(self.printMin)
        self.sumRow.clicked.connect(self.printSumC)
        self.M = 0 
        self.N = 0
        self.matr = [[1 for y in range(self.M)] for x in range(self.N)]
    def newMatrix(self):
        self.listWidget.clear()
        self.matr = [[random.randrange(0, 10) for y in range(self.M)] for x in range(self.N)]
        for i in self.matr:
            self.listWidget.addItem(str(i))
    def showMatrix(self):
        self.listWidget.clear()
        self.M = self.rows.value()
        self.N = self.columns.value()
        self.matr = [[1 for y in range(self.M)] for x in range(self.N)]
        for i in self.matr:
            self.listWidget.addItem(str(i))
    def printMin(self):
        i = self.columnNumber.value()
        min = 10
        for j in self.matr:
            if j[i] < min:
                min = j[i]
        self.listWidget.addItem("minimum of {} colomn - ".format(i) + str(min))
    def printSumC(self):
        i = self.rowNumber.value()
        s = sum(self.matr[i])
        self.listWidget.addItem("sum of {} row - ".format(i) + str(s))
    def printSumAll(self):
        s = 0
        for i in self.matr:
            s += sum(i)
        self.listWidget.addItem("sum of all elements - ".format(i) + str(s))
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MatrixApp()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()

