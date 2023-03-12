# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QFrame,
    QGridLayout, QHeaderView, QLCDNumber, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenuBar,
    QPlainTextEdit, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(450, 586)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_6 = QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        font = QFont()
        font.setPointSize(10)
        self.tabWidget.setFont(font)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.cbStandards = QComboBox(self.tab)
        self.cbStandards.setObjectName(u"cbStandards")
        self.cbStandards.setGeometry(QRect(10, 10, 107, 22))
        self.cbStandards.setFont(font)
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 281, 411, 211))
        self.tableWidget.setFrameShape(QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QFrame.Sunken)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(80)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 40, 131, 254))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetFixedSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(40, 16777215))
        font2 = QFont()
        font2.setPointSize(11)
        self.label.setFont(font2)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.etVh = QLineEdit(self.layoutWidget)
        self.etVh.setObjectName(u"etVh")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.etVh.sizePolicy().hasHeightForWidth())
        self.etVh.setSizePolicy(sizePolicy)
        self.etVh.setMaximumSize(QSize(60, 16777215))
        font3 = QFont()
        font3.setPointSize(12)
        self.etVh.setFont(font3)

        self.gridLayout.addWidget(self.etVh, 0, 1, 1, 1)

        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)

        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 16777215))
        self.label_2.setFont(font2)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.etVl = QLineEdit(self.layoutWidget)
        self.etVl.setObjectName(u"etVl")
        self.etVl.setMaximumSize(QSize(60, 16777215))
        self.etVl.setFont(font3)

        self.gridLayout.addWidget(self.etVl, 1, 1, 1, 1)

        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)

        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(40, 16777215))
        self.label_3.setFont(font2)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.etVref = QLineEdit(self.layoutWidget)
        self.etVref.setObjectName(u"etVref")
        self.etVref.setMaximumSize(QSize(60, 16777215))
        self.etVref.setFont(font3)

        self.gridLayout.addWidget(self.etVref, 2, 1, 1, 1)

        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 2, 2, 1, 1)

        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 16777215))
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.etVoh = QLineEdit(self.layoutWidget)
        self.etVoh.setObjectName(u"etVoh")
        self.etVoh.setMaximumSize(QSize(60, 16777215))
        self.etVoh.setFont(font3)

        self.gridLayout.addWidget(self.etVoh, 3, 1, 1, 1)

        self.label_10 = QLabel(self.layoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout.addWidget(self.label_10, 3, 2, 1, 1)

        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(40, 16777215))
        self.label_5.setFont(font2)

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.etVol = QLineEdit(self.layoutWidget)
        self.etVol.setObjectName(u"etVol")
        self.etVol.setMaximumSize(QSize(60, 16777215))
        self.etVol.setFont(font3)

        self.gridLayout.addWidget(self.etVol, 4, 1, 1, 1)

        self.label_11 = QLabel(self.layoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout.addWidget(self.label_11, 4, 2, 1, 1)

        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(40, 16777215))
        self.label_6.setFont(font2)

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.etError = QLineEdit(self.layoutWidget)
        self.etError.setObjectName(u"etError")
        self.etError.setMaximumSize(QSize(60, 16777215))
        self.etError.setFont(font3)

        self.gridLayout.addWidget(self.etError, 5, 1, 1, 1)

        self.label_12 = QLabel(self.layoutWidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)

        self.gridLayout.addWidget(self.label_12, 5, 2, 1, 1)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        self.pushButton.setFont(font4)

        self.gridLayout.addWidget(self.pushButton, 6, 0, 1, 2)

        self.lblImg = QLabel(self.tab)
        self.lblImg.setObjectName(u"lblImg")
        self.lblImg.setGeometry(QRect(160, 10, 261, 261))
        self.lblImg.setFrameShape(QFrame.StyledPanel)
        self.lblImg.setScaledContents(True)
        self.lblImg.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_2 = QTabWidget(self.tab_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(10, 0, 411, 481))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy1)
        font5 = QFont()
        font5.setPointSize(9)
        self.tabWidget_2.setFont(font5)
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        font6 = QFont()
        font6.setPointSize(14)
        self.tab_3.setFont(font6)
        self.btnAdcCalculate = QPushButton(self.tab_3)
        self.btnAdcCalculate.setObjectName(u"btnAdcCalculate")
        self.btnAdcCalculate.setGeometry(QRect(260, 110, 101, 28))
        self.btnAdcCalculate.setFont(font)
        self.btnAdcCalculate.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.layoutWidget1 = QWidget(self.tab_3)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(30, 200, 321, 41))
        self.gridLayout_3 = QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_22 = QLabel(self.layoutWidget1)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font2)

        self.gridLayout_3.addWidget(self.label_22, 0, 0, 1, 1)

        self.lcdResolution = QLCDNumber(self.layoutWidget1)
        self.lcdResolution.setObjectName(u"lcdResolution")
        self.lcdResolution.setLineWidth(1)
        self.lcdResolution.setDigitCount(10)
        self.lcdResolution.setSegmentStyle(QLCDNumber.Filled)

        self.gridLayout_3.addWidget(self.lcdResolution, 0, 1, 1, 1)

        self.label_25 = QLabel(self.layoutWidget1)
        self.label_25.setObjectName(u"label_25")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_25.sizePolicy().hasHeightForWidth())
        self.label_25.setSizePolicy(sizePolicy2)
        self.label_25.setFont(font)

        self.gridLayout_3.addWidget(self.label_25, 0, 2, 1, 1)

        self.layoutWidget2 = QWidget(self.tab_3)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 250, 321, 41))
        self.gridLayout_4 = QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.layoutWidget2)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font2)

        self.gridLayout_4.addWidget(self.label_27, 0, 0, 1, 1)

        self.lcdVoltage = QLCDNumber(self.layoutWidget2)
        self.lcdVoltage.setObjectName(u"lcdVoltage")
        self.lcdVoltage.setStyleSheet(u"QLCDNumber:disabled {\n"
" color:#010101;\n"
"background-color:#555555;\n"
"}")
        self.lcdVoltage.setDigitCount(10)

        self.gridLayout_4.addWidget(self.lcdVoltage, 0, 1, 1, 1)

        self.label_26 = QLabel(self.layoutWidget2)
        self.label_26.setObjectName(u"label_26")
        sizePolicy2.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy2)
        self.label_26.setFont(font)

        self.gridLayout_4.addWidget(self.label_26, 0, 2, 1, 1)

        self.layoutWidget3 = QWidget(self.tab_3)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(31, 300, 321, 41))
        self.gridLayout_5 = QGridLayout(self.layoutWidget3)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.layoutWidget3)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font2)

        self.gridLayout_5.addWidget(self.label_24, 0, 0, 1, 1)

        self.lcdAdc = QLCDNumber(self.layoutWidget3)
        self.lcdAdc.setObjectName(u"lcdAdc")
        self.lcdAdc.setStyleSheet(u"QLCDNumber:disabled {\n"
" color:#010101;\n"
"background-color:#555555;\n"
"}")
        self.lcdAdc.setDigitCount(10)

        self.gridLayout_5.addWidget(self.lcdAdc, 0, 1, 1, 1)

        self.label_28 = QLabel(self.layoutWidget3)
        self.label_28.setObjectName(u"label_28")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.label_28.sizePolicy().hasHeightForWidth())
        self.label_28.setSizePolicy(sizePolicy3)
        self.label_28.setFont(font)

        self.gridLayout_5.addWidget(self.label_28, 0, 2, 1, 1)

        self.layoutWidget4 = QWidget(self.tab_3)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(3, 21, 177, 143))
        self.gridLayout_2 = QGridLayout(self.layoutWidget4)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.layoutWidget4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setEnabled(True)
        self.label_13.setMaximumSize(QSize(100, 16777215))
        self.label_13.setFont(font2)

        self.gridLayout_2.addWidget(self.label_13, 0, 0, 1, 1)

        self.etAdcResolution = QLineEdit(self.layoutWidget4)
        self.etAdcResolution.setObjectName(u"etAdcResolution")
        sizePolicy.setHeightForWidth(self.etAdcResolution.sizePolicy().hasHeightForWidth())
        self.etAdcResolution.setSizePolicy(sizePolicy)
        self.etAdcResolution.setMaximumSize(QSize(60, 16777215))
        self.etAdcResolution.setFont(font3)

        self.gridLayout_2.addWidget(self.etAdcResolution, 0, 1, 1, 1)

        self.label_14 = QLabel(self.layoutWidget4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font)

        self.gridLayout_2.addWidget(self.label_14, 0, 2, 1, 1)

        self.label_15 = QLabel(self.layoutWidget4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setEnabled(True)
        self.label_15.setMaximumSize(QSize(100, 16777215))
        self.label_15.setFont(font2)

        self.gridLayout_2.addWidget(self.label_15, 1, 0, 1, 1)

        self.etAdcVref = QLineEdit(self.layoutWidget4)
        self.etAdcVref.setObjectName(u"etAdcVref")
        sizePolicy.setHeightForWidth(self.etAdcVref.sizePolicy().hasHeightForWidth())
        self.etAdcVref.setSizePolicy(sizePolicy)
        self.etAdcVref.setMaximumSize(QSize(60, 16777215))
        self.etAdcVref.setFont(font3)

        self.gridLayout_2.addWidget(self.etAdcVref, 1, 1, 1, 1)

        self.label_16 = QLabel(self.layoutWidget4)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.gridLayout_2.addWidget(self.label_16, 1, 2, 1, 1)

        self.label_17 = QLabel(self.layoutWidget4)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setEnabled(True)
        self.label_17.setMaximumSize(QSize(100, 16777215))
        self.label_17.setFont(font2)

        self.gridLayout_2.addWidget(self.label_17, 2, 0, 1, 1)

        self.etAdcOffset = QLineEdit(self.layoutWidget4)
        self.etAdcOffset.setObjectName(u"etAdcOffset")
        sizePolicy.setHeightForWidth(self.etAdcOffset.sizePolicy().hasHeightForWidth())
        self.etAdcOffset.setSizePolicy(sizePolicy)
        self.etAdcOffset.setMaximumSize(QSize(60, 16777215))
        self.etAdcOffset.setFont(font3)

        self.gridLayout_2.addWidget(self.etAdcOffset, 2, 1, 1, 1)

        self.label_19 = QLabel(self.layoutWidget4)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.gridLayout_2.addWidget(self.label_19, 2, 2, 1, 1)

        self.label_18 = QLabel(self.layoutWidget4)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setEnabled(True)
        self.label_18.setMaximumSize(QSize(100, 16777215))
        self.label_18.setFont(font2)

        self.gridLayout_2.addWidget(self.label_18, 3, 0, 1, 1)

        self.etAdcGain = QLineEdit(self.layoutWidget4)
        self.etAdcGain.setObjectName(u"etAdcGain")
        sizePolicy.setHeightForWidth(self.etAdcGain.sizePolicy().hasHeightForWidth())
        self.etAdcGain.setSizePolicy(sizePolicy)
        self.etAdcGain.setMaximumSize(QSize(60, 16777215))
        self.etAdcGain.setFont(font3)

        self.gridLayout_2.addWidget(self.etAdcGain, 3, 1, 1, 1)

        self.layoutWidget5 = QWidget(self.tab_3)
        self.layoutWidget5.setObjectName(u"layoutWidget5")
        self.layoutWidget5.setGeometry(QRect(220, 20, 181, 71))
        self.gridLayout_7 = QGridLayout(self.layoutWidget5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.rbVoltage = QRadioButton(self.layoutWidget5)
        self.rbVoltage.setObjectName(u"rbVoltage")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.rbVoltage.sizePolicy().hasHeightForWidth())
        self.rbVoltage.setSizePolicy(sizePolicy4)
        self.rbVoltage.setChecked(True)

        self.gridLayout_7.addWidget(self.rbVoltage, 0, 0, 1, 1)

        self.etAdcAdc = QLineEdit(self.layoutWidget5)
        self.etAdcAdc.setObjectName(u"etAdcAdc")
        sizePolicy.setHeightForWidth(self.etAdcAdc.sizePolicy().hasHeightForWidth())
        self.etAdcAdc.setSizePolicy(sizePolicy)
        self.etAdcAdc.setMaximumSize(QSize(60, 16777215))
        self.etAdcAdc.setFont(font3)

        self.gridLayout_7.addWidget(self.etAdcAdc, 1, 2, 1, 1)

        self.label_21 = QLabel(self.layoutWidget5)
        self.label_21.setObjectName(u"label_21")
        sizePolicy2.setHeightForWidth(self.label_21.sizePolicy().hasHeightForWidth())
        self.label_21.setSizePolicy(sizePolicy2)
        self.label_21.setFont(font)

        self.gridLayout_7.addWidget(self.label_21, 0, 3, 1, 1)

        self.rbAdc = QRadioButton(self.layoutWidget5)
        self.rbAdc.setObjectName(u"rbAdc")
        sizePolicy4.setHeightForWidth(self.rbAdc.sizePolicy().hasHeightForWidth())
        self.rbAdc.setSizePolicy(sizePolicy4)

        self.gridLayout_7.addWidget(self.rbAdc, 1, 0, 1, 1)

        self.label_20 = QLabel(self.layoutWidget5)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setEnabled(True)
        self.label_20.setMaximumSize(QSize(100, 16777215))
        self.label_20.setFont(font2)

        self.gridLayout_7.addWidget(self.label_20, 0, 1, 1, 1)

        self.label_23 = QLabel(self.layoutWidget5)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setEnabled(True)
        self.label_23.setMaximumSize(QSize(100, 16777215))
        self.label_23.setFont(font2)

        self.gridLayout_7.addWidget(self.label_23, 1, 1, 1, 1)

        self.etAdcVoltage = QLineEdit(self.layoutWidget5)
        self.etAdcVoltage.setObjectName(u"etAdcVoltage")
        sizePolicy.setHeightForWidth(self.etAdcVoltage.sizePolicy().hasHeightForWidth())
        self.etAdcVoltage.setSizePolicy(sizePolicy)
        self.etAdcVoltage.setMaximumSize(QSize(60, 16777215))
        self.etAdcVoltage.setFont(font3)

        self.gridLayout_7.addWidget(self.etAdcVoltage, 0, 2, 1, 1)

        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.layoutWidget_2 = QWidget(self.tab_5)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(10, 30, 243, 143))
        self.gridLayout_9 = QGridLayout(self.layoutWidget_2)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.etTimError = QLineEdit(self.layoutWidget_2)
        self.etTimError.setObjectName(u"etTimError")
        sizePolicy.setHeightForWidth(self.etTimError.sizePolicy().hasHeightForWidth())
        self.etTimError.setSizePolicy(sizePolicy)
        self.etTimError.setMaximumSize(QSize(80, 16777215))
        self.etTimError.setFont(font3)

        self.gridLayout_9.addWidget(self.etTimError, 2, 1, 1, 1)

        self.label_36 = QLabel(self.layoutWidget_2)
        self.label_36.setObjectName(u"label_36")
        sizePolicy2.setHeightForWidth(self.label_36.sizePolicy().hasHeightForWidth())
        self.label_36.setSizePolicy(sizePolicy2)
        self.label_36.setFont(font)

        self.gridLayout_9.addWidget(self.label_36, 2, 2, 1, 1)

        self.etTimTime = QLineEdit(self.layoutWidget_2)
        self.etTimTime.setObjectName(u"etTimTime")
        sizePolicy.setHeightForWidth(self.etTimTime.sizePolicy().hasHeightForWidth())
        self.etTimTime.setSizePolicy(sizePolicy)
        self.etTimTime.setMaximumSize(QSize(80, 16777215))
        self.etTimTime.setFont(font3)

        self.gridLayout_9.addWidget(self.etTimTime, 1, 1, 1, 1)

        self.label_35 = QLabel(self.layoutWidget_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setEnabled(True)
        self.label_35.setMaximumSize(QSize(100, 16777215))
        self.label_35.setFont(font2)

        self.gridLayout_9.addWidget(self.label_35, 2, 0, 1, 1)

        self.etTimFrq = QLineEdit(self.layoutWidget_2)
        self.etTimFrq.setObjectName(u"etTimFrq")
        sizePolicy.setHeightForWidth(self.etTimFrq.sizePolicy().hasHeightForWidth())
        self.etTimFrq.setSizePolicy(sizePolicy)
        self.etTimFrq.setMaximumSize(QSize(80, 16777215))
        self.etTimFrq.setFont(font3)

        self.gridLayout_9.addWidget(self.etTimFrq, 0, 1, 1, 1)

        self.label_33 = QLabel(self.layoutWidget_2)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setEnabled(True)
        self.label_33.setMaximumSize(QSize(100, 16777215))
        self.label_33.setFont(font2)

        self.gridLayout_9.addWidget(self.label_33, 1, 0, 1, 1)

        self.label_31 = QLabel(self.layoutWidget_2)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setEnabled(True)
        self.label_31.setMaximumSize(QSize(100, 16777215))
        self.label_31.setFont(font2)

        self.gridLayout_9.addWidget(self.label_31, 0, 0, 1, 1)

        self.cbTimFrqUnit = QComboBox(self.layoutWidget_2)
        self.cbTimFrqUnit.addItem("")
        self.cbTimFrqUnit.addItem("")
        self.cbTimFrqUnit.addItem("")
        self.cbTimFrqUnit.setObjectName(u"cbTimFrqUnit")
        sizePolicy4.setHeightForWidth(self.cbTimFrqUnit.sizePolicy().hasHeightForWidth())
        self.cbTimFrqUnit.setSizePolicy(sizePolicy4)
        self.cbTimFrqUnit.setMaximumSize(QSize(60, 16777215))
        self.cbTimFrqUnit.setFont(font)

        self.gridLayout_9.addWidget(self.cbTimFrqUnit, 0, 2, 1, 1)

        self.cbTimTimeUnit = QComboBox(self.layoutWidget_2)
        self.cbTimTimeUnit.addItem("")
        self.cbTimTimeUnit.addItem("")
        self.cbTimTimeUnit.addItem("")
        self.cbTimTimeUnit.addItem("")
        self.cbTimTimeUnit.setObjectName(u"cbTimTimeUnit")
        sizePolicy4.setHeightForWidth(self.cbTimTimeUnit.sizePolicy().hasHeightForWidth())
        self.cbTimTimeUnit.setSizePolicy(sizePolicy4)
        self.cbTimTimeUnit.setMaximumSize(QSize(60, 16777215))
        self.cbTimTimeUnit.setFont(font)

        self.gridLayout_9.addWidget(self.cbTimTimeUnit, 1, 2, 1, 1)

        self.btnTimCalculate = QPushButton(self.tab_5)
        self.btnTimCalculate.setObjectName(u"btnTimCalculate")
        self.btnTimCalculate.setGeometry(QRect(290, 210, 101, 28))
        self.btnTimCalculate.setFont(font)
        self.btnTimCalculate.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.tblTim = QTableWidget(self.tab_5)
        if (self.tblTim.columnCount() < 2):
            self.tblTim.setColumnCount(2)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.tblTim.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.tblTim.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        self.tblTim.setObjectName(u"tblTim")
        self.tblTim.setGeometry(QRect(10, 250, 386, 181))
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tblTim.sizePolicy().hasHeightForWidth())
        self.tblTim.setSizePolicy(sizePolicy5)
        self.tblTim.setFrameShape(QFrame.StyledPanel)
        self.tblTim.setFrameShadow(QFrame.Sunken)
        self.tblTim.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tblTim.setColumnCount(2)
        self.tblTim.horizontalHeader().setVisible(False)
        self.tblTim.horizontalHeader().setCascadingSectionResizes(False)
        self.tblTim.horizontalHeader().setDefaultSectionSize(80)
        self.tblTim.horizontalHeader().setHighlightSections(True)
        self.tblTim.horizontalHeader().setProperty("showSortIndicator", False)
        self.tblTim.horizontalHeader().setStretchLastSection(True)
        self.tblTim.verticalHeader().setCascadingSectionResizes(False)
        self.tblTim.verticalHeader().setProperty("showSortIndicator", False)
        self.tblTim.verticalHeader().setStretchLastSection(False)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tblPoly = QTableWidget(self.tab_6)
        if (self.tblPoly.rowCount() < 2):
            self.tblPoly.setRowCount(2)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font3);
        self.tblPoly.setVerticalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font3);
        self.tblPoly.setVerticalHeaderItem(1, __qtablewidgetitem8)
        self.tblPoly.setObjectName(u"tblPoly")
        self.tblPoly.setGeometry(QRect(10, 100, 411, 111))
        self.tblPoly.setFont(font3)
        self.btnPolyCalculate = QPushButton(self.tab_6)
        self.btnPolyCalculate.setObjectName(u"btnPolyCalculate")
        self.btnPolyCalculate.setGeometry(QRect(10, 220, 93, 28))
        self.btnPolyCalculate.setFont(font)
        self.tabWidget_3 = QTabWidget(self.tab_6)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setGeometry(QRect(10, 260, 401, 211))
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.etPolyCoefficients = QPlainTextEdit(self.tab_7)
        self.etPolyCoefficients.setObjectName(u"etPolyCoefficients")
        self.etPolyCoefficients.setGeometry(QRect(10, 10, 377, 87))
        self.etPolyCoefficients.setFont(font3)
        self.etPolyCoefficients.setContextMenuPolicy(Qt.NoContextMenu)
        self.etPolyCoefficients.setReadOnly(True)
        self.etPolyCoefficients.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.tabWidget_3.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.graphWidget = PlotWidget(self.tab_8)
        self.graphWidget.setObjectName(u"graphWidget")
        self.graphWidget.setGeometry(QRect(0, 0, 391, 181))
        self.tabWidget_3.addTab(self.tab_8, "")
        self.layoutWidget6 = QWidget(self.tab_6)
        self.layoutWidget6.setObjectName(u"layoutWidget6")
        self.layoutWidget6.setGeometry(QRect(10, 20, 223, 81))
        self.gridLayout_8 = QGridLayout(self.layoutWidget6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.layoutWidget6)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setEnabled(True)
        self.label_30.setMaximumSize(QSize(100, 16777215))
        self.label_30.setFont(font2)

        self.gridLayout_8.addWidget(self.label_30, 0, 0, 1, 1)

        self.etPolyOrder = QLineEdit(self.layoutWidget6)
        self.etPolyOrder.setObjectName(u"etPolyOrder")
        sizePolicy.setHeightForWidth(self.etPolyOrder.sizePolicy().hasHeightForWidth())
        self.etPolyOrder.setSizePolicy(sizePolicy)
        self.etPolyOrder.setMaximumSize(QSize(60, 16777215))
        self.etPolyOrder.setFont(font3)

        self.gridLayout_8.addWidget(self.etPolyOrder, 0, 1, 1, 1)

        self.label_29 = QLabel(self.layoutWidget6)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setEnabled(True)
        self.label_29.setMaximumSize(QSize(100, 16777215))
        self.label_29.setFont(font2)

        self.gridLayout_8.addWidget(self.label_29, 1, 0, 1, 1)

        self.etPolyLength = QLineEdit(self.layoutWidget6)
        self.etPolyLength.setObjectName(u"etPolyLength")
        sizePolicy.setHeightForWidth(self.etPolyLength.sizePolicy().hasHeightForWidth())
        self.etPolyLength.setSizePolicy(sizePolicy)
        self.etPolyLength.setMaximumSize(QSize(60, 16777215))
        self.etPolyLength.setFont(font3)

        self.gridLayout_8.addWidget(self.etPolyLength, 1, 1, 1, 1)

        self.btnPolyApply = QPushButton(self.layoutWidget6)
        self.btnPolyApply.setObjectName(u"btnPolyApply")
        self.btnPolyApply.setFont(font)

        self.gridLayout_8.addWidget(self.btnPolyApply, 1, 2, 1, 1)

        self.tabWidget.addTab(self.tab_6, "")

        self.gridLayout_6.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 450, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(2)
        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"VH", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"VL", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"R1", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"R2", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"R3", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"VH", None))
        self.etVh.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"VL", None))
        self.etVl.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Vref", None))
        self.etVref.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"VOH", None))
        self.etVoh.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"VOL", None))
        self.etVol.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.etError.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.lblImg.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Schmitt Trigger", None))
        self.btnAdcCalculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"ADC to Voltage", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Voltage to ADC", None))
        self.label_28.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Resolution", None))
        self.etAdcResolution.setText("")
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"bit", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Vref", None))
        self.etAdcVref.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Offset", None))
        self.etAdcOffset.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Gain", None))
        self.etAdcGain.setText("")
        self.rbVoltage.setText("")
        self.etAdcAdc.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.rbAdc.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Voltage", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"ADC", None))
        self.etAdcVoltage.setText("")
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"ADC", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"USART", None))
        self.etTimError.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.etTimTime.setText("")
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Error", None))
        self.etTimFrq.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.cbTimFrqUnit.setItemText(0, QCoreApplication.translate("MainWindow", u"Hz", None))
        self.cbTimFrqUnit.setItemText(1, QCoreApplication.translate("MainWindow", u"KHz", None))
        self.cbTimFrqUnit.setItemText(2, QCoreApplication.translate("MainWindow", u"MHz", None))

        self.cbTimTimeUnit.setItemText(0, QCoreApplication.translate("MainWindow", u"sec", None))
        self.cbTimTimeUnit.setItemText(1, QCoreApplication.translate("MainWindow", u"ms", None))
        self.cbTimTimeUnit.setItemText(2, QCoreApplication.translate("MainWindow", u"us", None))
        self.cbTimTimeUnit.setItemText(3, QCoreApplication.translate("MainWindow", u"ns", None))

        self.btnTimCalculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        ___qtablewidgetitem5 = self.tblTim.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Prescaler", None));
        ___qtablewidgetitem6 = self.tblTim.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Counter", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"TIMER", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"MCU", None))
        ___qtablewidgetitem7 = self.tblPoly.verticalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"x", None));
        ___qtablewidgetitem8 = self.tblPoly.verticalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"y", None));
        self.btnPolyCalculate.setText(QCoreApplication.translate("MainWindow", u"Calculate", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Coefficients", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_8), QCoreApplication.translate("MainWindow", u"Graph", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Order", None))
        self.etPolyOrder.setText("")
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Length", None))
        self.etPolyLength.setText("")
        self.btnPolyApply.setText(QCoreApplication.translate("MainWindow", u"Apply", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"Polynomial", None))
    # retranslateUi

