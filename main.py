from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout,QHeaderView
from PyQt5.uic import loadUi
from PyQt5.QtCore import pyqtSlot
import sys
import schmittTrigger as mi

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        
        loadUi("main.ui", self)
        self.pushButton.clicked.connect(self.clickHandler)

    def clickHandler(self):
        data = []
        data.append(float(self.etVoh.text()))
        data.append(float(self.etVol.text()))
        data.append(float(self.etVref.text()))
        data.append(float(self.etVh.text()))
        data.append(float(self.etVl.text()))
        data.append(float(self.etError.text()))
        res = mi.calculate(data)
        self.Tables(res)
    
    def Tables(self, data):       
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(5)

        header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QHeaderView.ResizeToContents)
        
        i = 0
        for d in data:
            self.tableWidget.setItem(i, 0, QTableWidgetItem(d[0]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(d[1]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(d[2]))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(d[3]))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(d[4]))
            i += 1
             
        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.tableWidget)
        self.setLayout(self.vBox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()