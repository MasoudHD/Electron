from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem,QVBoxLayout,QHeaderView
from PyQt5.QtGui import QPixmap, QFont, QDoubleValidator
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets, QtGui
import sys
import schmittTrigger as mi
import qdarktheme

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        
        loadUi("main.ui", self)

        self.setFixedSize(420, 540)
        self.setWindowTitle("Electron")
        onlyDouble = QDoubleValidator()
        self.etVoh.setValidator(onlyDouble)
        self.etVol.setValidator(onlyDouble)
        self.etVref.setValidator(onlyDouble)
        self.etVh.setValidator(onlyDouble)
        self.etVl.setValidator(onlyDouble)
        self.etError.setValidator(onlyDouble)

        self.pushButton.clicked.connect(self.clickHandler)

        # self.tableWidget.QHeaderView.ResizeMode.setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget.QHeaderView.sectionResizeMode(QHeaderView.Stretch)

        pixmap = QPixmap('res/img/schmittTrigerCircuitDark.png')
        self.lblImg.setPixmap(pixmap)
        resStandard = ('E12', 'E24')
        self.cbStandards.addItems(resStandard)
        
    def clickHandler(self):
        try:
            data = []
            data.append(float(self.etVoh.text()))
            data.append(float(self.etVol.text()))
            data.append(float(self.etVref.text()))
            data.append(float(self.etVh.text()))
            data.append(float(self.etVl.text()))
            data.append(float(self.etError.text()))
            res = mi.calculate(data, self.cbStandards.currentText())
            self.Tables(res)
        except:
            QMessageBox.critical(self, 'Error', "An exception occurred", QMessageBox.Ok)
    
    def Tables(self, data):       
        self.tableWidget.setRowCount(len(data))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        header = self.tableWidget.horizontalHeader()       
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)
        header.setSectionResizeMode(2, QHeaderView.Stretch)
        header.setSectionResizeMode(3, QHeaderView.Stretch)
        header.setSectionResizeMode(4, QHeaderView.Stretch)
        self.tableWidget.setFont(QFont("Times", 12))

        i = 0
        for d in data:
            for j in range(len(d)): 
                self.tableWidget.setItem(i, j, QTableWidgetItem(d[j]))
                item = self.tableWidget.item(i, j)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                if i == 0:
                    self.tableWidget.item(0, j).setBackground(QtGui.QColor("#009900"))            
            i += 1

        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.tableWidget)
        self.setLayout(self.vBox)

if __name__ == "__main__":
    qdarktheme.enable_hi_dpi()
    app = QApplication(sys.argv)
    qdarktheme.setup_theme(corner_shape="rounded")
    ui = MainUI()
    ui.show()
    app.exec_()