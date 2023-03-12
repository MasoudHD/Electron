from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QTableWidgetItem, QVBoxLayout, QHeaderView, QStyledItemDelegate, QLineEdit
from PyQt5.QtGui import QPixmap, QFont, QDoubleValidator, QIntValidator, QRegExpValidator
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QRegExp
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys
import qdarktheme

import schmittTrigger as mi
import mcu
import poly

class NumericDelegate(QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = super(NumericDelegate, self).createEditor(parent, option, index)
        if isinstance(editor, QLineEdit):
            reg_ex = QRegExp("^-?[0-9]\d*(\.\d+)?$")
            validator = QRegExpValidator(reg_ex, editor)
            editor.setValidator(validator)
        return editor
    
class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        
        loadUi("main.ui", self)

        self.setFixedSize(435, 550)
        self.setWindowTitle("Electron")
        onlyDouble = QDoubleValidator()
        onlyInteger = QIntValidator()
        
        self.etVoh.setValidator(onlyDouble)
        self.etVol.setValidator(onlyDouble)
        self.etVref.setValidator(onlyDouble)
        self.etVh.setValidator(onlyDouble)
        self.etVl.setValidator(onlyDouble)
        self.etError.setValidator(onlyDouble)

        self.etAdcResolution.setValidator(onlyDouble)
        self.etAdcVref.setValidator(onlyDouble)
        self.etAdcOffset.setValidator(onlyDouble)
        self.etAdcGain.setValidator(onlyDouble)
        self.etAdcVoltage.setValidator(onlyDouble)
        self.etAdcAdc.setValidator(onlyDouble)
        self.etPolyLength.setValidator(onlyInteger)
        self.etPolyOrder.setValidator(onlyInteger)

        self.etTimFrq.setValidator(onlyDouble)
        self.etTimTime.setValidator(onlyDouble)
        self.etTimError.setValidator(onlyDouble)

        self.etAdcAdc.setDisabled(True)
        self.etAdcVoltage.setDisabled(False)
        self.lcdVoltage.setDisabled(self.rbVoltage.isChecked())
        self.lcdAdc.setDisabled(self.rbAdc.isChecked())
        self.rbVoltage.clicked.connect(self.rbAdcCheck)
        self.rbAdc.clicked.connect(self.rbAdcCheck)
        
        self.pushButton.clicked.connect(self.clickHandler)
        self.btnAdcCalculate.clicked.connect(self.btnAdcCalculateClickHandler)
        self.btnPolyApply.clicked.connect(self.btnPolyApplyHandler)
        self.btnPolyCalculate.clicked.connect(self.btnPolyCalculateHandler)
        self.btnTimCalculate.clicked.connect(self.btnTimCalculateeHandler)

        delegate = NumericDelegate(self.tblPoly)
        self.tblPoly.setItemDelegate(delegate)

        # self.tableWidget.QHeaderView.ResizeMode.setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget.QHeaderView.sectionResizeMode(QHeaderView.Stretch)

        pixmap = QPixmap('res/img/schmittTrigerCircuitDark.png')
        self.lblImg.setPixmap(pixmap)
        resStandard = ('E12', 'E24')
        self.cbStandards.addItems(resStandard)

    # def keyPressEvent(self, qKeyEvent):
    #     if qKeyEvent.key() == QtCore.Qt.Key_Return: 
    #         self.btnAdcCalculateClickHandler()
    #     else:
    #         super().keyPressEvent(qKeyEvent)

    def rbAdcCheck(self):
        self.etAdcVoltage.setDisabled(self.rbAdc.isChecked())
        self.etAdcAdc.setDisabled(self.rbVoltage.isChecked())
        self.lcdVoltage.setDisabled(self.rbVoltage.isChecked())
        self.lcdAdc.setDisabled(self.rbAdc.isChecked())

    def btnTimCalculateeHandler(self):
        frq = float(self.etTimFrq.text())
        time = float(self.etTimTime.text())
        error = float(self.etTimError.text())
        res = mcu.timCalculator(frq, time, error, self.cbTimFrqUnit.currentText(), self.cbTimTimeUnit.currentText())

        self.Tables(res, 2, False, self.tblTim)

    def btnPolyCalculateHandler(self):
        self.graphWidget.clear()
        order = int(self.etPolyOrder.text())
        colCount = self.tblPoly.columnCount()
        xValue = []
        yValue = []
        for cell in range(colCount):
            xValue.append(float(self.tblPoly.item(0, cell).text()))
            yValue.append(float(self.tblPoly.item(1, cell).text()))
        coefficients = poly.findCoefficients(xValue, yValue, order)
        print(xValue)
        print(yValue)
        print(coefficients)
        strCftArray = f"cft[{coefficients.__len__()}] = " + "{"
        for cft in coefficients:
           strCftArray += str(cft) + ","
        strCftArray = strCftArray[:-1]
        strCftArray += "};"
        self.etPolyCoefficients.setPlainText(strCftArray)
        self.graphWidget.plot(xValue, yValue, pen=pg.mkPen('r', width=3))
        
        p = poly.np.poly1d(coefficients)
        resultY = []
        for x in xValue:
            resultY.append(p(x))
        self.graphWidget.plot(xValue, resultY, pen=pg.mkPen('b', width=2))
        
    
    def btnPolyApplyHandler(self):
        #asfasf
        tableLen = int(self.etPolyLength.text())
        self.tblPoly.setColumnCount(tableLen)
        # self.tblPoly.insertRow(5)

    def btnAdcCalculateClickHandler(self):
        try:
            Resolution = float(self.etAdcResolution.text())
            Vref = float(self.etAdcVref.text())
            Offset = float(self.etAdcOffset.text())
            Gain = float(self.etAdcGain.text())    
            self.lcdResolution.display(mcu.resolution(Resolution, Vref))

            if self.rbAdc.isChecked():
                adcValue = float(self.etAdcAdc.text())
                self.lcdVoltage.display(mcu.d2a(Resolution, Vref, Offset, Gain, adcValue))
            elif self.rbVoltage.isChecked():
                voltageValue = float(self.etAdcVoltage.text())
                self.lcdAdc.display(int(mcu.a2d(Resolution, Vref, Offset, Gain, voltageValue)))
        except:
            QMessageBox.critical(self, 'Error', "An exception occurred", QMessageBox.Ok)

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
            self.Tables(res, 5, True, self.tableWidget)
        except:
            QMessageBox.critical(self, 'Error', "An exception occurred", QMessageBox.Ok)
    

    def Tables(self, data, colNumber, firstRowColor,tblWidget):       
        tblWidget.setRowCount(len(data))
        tblWidget.setColumnCount(colNumber)
        tblWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        header = tblWidget.horizontalHeader()               
        for i in range(0, colNumber):
            header.setSectionResizeMode(i, QHeaderView.Stretch)
        header.show()

        tblWidget.setFont(QFont("Times", 12))

        i = 0
        for d in data:
            for j in range(len(d)): 
                tblWidget.setItem(i, j, QTableWidgetItem(d[j]))
                item = tblWidget.item(i, j)
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                if firstRowColor and i == 0:
                    tblWidget.item(0, j).setBackground(QtGui.QColor("#009900"))            
            i += 1

        self.vBox = QVBoxLayout()
        self.vBox.addWidget(tblWidget)
        self.setLayout(self.vBox)

if __name__ == "__main__":
    qdarktheme.enable_hi_dpi()
    app = QApplication(sys.argv)
    qdarktheme.setup_theme(corner_shape="rounded")
    ui = MainUI()
    ui.show()
    app.exec_()