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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(420, 540)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 300, 401, 192))
        self.tableWidget.setFrameShape(QFrame.StyledPanel)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(125)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.lblImg = QLabel(self.centralwidget)
        self.lblImg.setObjectName(u"lblImg")
        self.lblImg.setGeometry(QRect(150, 30, 261, 251))
        self.lblImg.setFrameShape(QFrame.StyledPanel)
        self.lblImg.setScaledContents(True)
        self.cbStandards = QComboBox(self.centralwidget)
        self.cbStandards.setObjectName(u"cbStandards")
        self.cbStandards.setGeometry(QRect(10, 30, 101, 22))
        font1 = QFont()
        font1.setPointSize(10)
        self.cbStandards.setFont(font1)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 63, 131, 231))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(40, 16777215))
        font2 = QFont()
        font2.setPointSize(11)
        self.label.setFont(font2)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.etVh = QLineEdit(self.widget)
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

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.gridLayout.addWidget(self.label_7, 0, 2, 1, 1)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 16777215))
        self.label_2.setFont(font2)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.etVl = QLineEdit(self.widget)
        self.etVl.setObjectName(u"etVl")
        self.etVl.setMaximumSize(QSize(60, 16777215))
        self.etVl.setFont(font3)

        self.gridLayout.addWidget(self.etVl, 1, 1, 1, 1)

        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)

        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(40, 16777215))
        self.label_3.setFont(font2)

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.etVref = QLineEdit(self.widget)
        self.etVref.setObjectName(u"etVref")
        self.etVref.setMaximumSize(QSize(60, 16777215))
        self.etVref.setFont(font3)

        self.gridLayout.addWidget(self.etVref, 2, 1, 1, 1)

        self.label_9 = QLabel(self.widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.gridLayout.addWidget(self.label_9, 2, 2, 1, 1)

        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 16777215))
        self.label_4.setFont(font2)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)

        self.etVoh = QLineEdit(self.widget)
        self.etVoh.setObjectName(u"etVoh")
        self.etVoh.setMaximumSize(QSize(60, 16777215))
        self.etVoh.setFont(font3)

        self.gridLayout.addWidget(self.etVoh, 3, 1, 1, 1)

        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.gridLayout.addWidget(self.label_10, 3, 2, 1, 1)

        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(40, 16777215))
        self.label_5.setFont(font2)

        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)

        self.etVol = QLineEdit(self.widget)
        self.etVol.setObjectName(u"etVol")
        self.etVol.setMaximumSize(QSize(60, 16777215))
        self.etVol.setFont(font3)

        self.gridLayout.addWidget(self.etVol, 4, 1, 1, 1)

        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.gridLayout.addWidget(self.label_11, 4, 2, 1, 1)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(40, 16777215))
        self.label_6.setFont(font2)

        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)

        self.etError = QLineEdit(self.widget)
        self.etError.setObjectName(u"etError")
        self.etError.setMaximumSize(QSize(60, 16777215))
        self.etError.setFont(font3)

        self.gridLayout.addWidget(self.etError, 5, 1, 1, 1)

        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)

        self.gridLayout.addWidget(self.label_12, 5, 2, 1, 1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(False)
        self.pushButton.setFont(font4)

        self.gridLayout.addWidget(self.pushButton, 6, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 420, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

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
        self.lblImg.setText("")
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
    # retranslateUi

