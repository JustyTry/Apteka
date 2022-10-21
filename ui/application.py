from functools import partial
from PyQt5 import QtCore, QtGui, QtWidgets
from .create import Ui_Dialog
from .order import Ui_Order
from .analytics import Ui_Analytics
import sqlite3


class Ui_MainWindow(object):

    def __init__(self, role):
        self.role = role
        self.ids = [0]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1200, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1200, 800))
        MainWindow.setSizeIncrement(QtCore.QSize(200, 0))
        MainWindow.setBaseSize(QtCore.QSize(1200, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "././green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background:#f6fdff;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(140, 50, 141, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 30, 81, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(
            "././green.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        if self.role == 'admin':
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setGeometry(QtCore.QRect(810, 30, 381, 41))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.pushButton.setFont(font)
            self.pushButton.setStyleSheet("background:orange;")
            self.pushButton.setObjectName("pushButton")
            self.pushButton.clicked.connect(self.openModal)
        elif self.role == 'analyst':
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setGeometry(QtCore.QRect(810, 30, 381, 41))
            font = QtGui.QFont()
            font.setPointSize(14)
            self.pushButton.setFont(font)
            self.pushButton.setStyleSheet("background:orange;")
            self.pushButton.setObjectName("pushButton")
            self.pushButton.clicked.connect(self.openAnalytics)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 210, 1201, 571))
        self.tableWidget.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(125)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(125)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 160, 396, 51))
        self.pushButton_2.setMinimumSize(QtCore.QSize(396, 27))
        self.pushButton_2.clicked.connect(self.loadDrugs)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("border: 1px solid #000;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 160, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("border: 1px solid #000;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.loadBuyOrders)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(810, 160, 391, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("border: 1px solid #000;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.loadProviders)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(810, 90, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background:orange;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(600, 160, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setCursor(
            QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_6.setStyleSheet("border: 1px solid #000;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.loadSupplyOrders)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.loadDrugs()
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Apteka"))
        self.label_3.setText(_translate("MainWindow", "Apteka"))
        if self.role == 'admin':
            self.pushButton.setText(_translate(
                "MainWindow", "Создать пользователя"))
        elif self.role == 'analyst':
            self.pushButton.setText(_translate(
                "MainWindow", "Отчёт"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Название"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Стоимость"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Статус"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Описание"))
        self.pushButton_2.setText(_translate("MainWindow", "Товары"))
        self.pushButton_3.setText(_translate("MainWindow", "Заказы на выдачу"))
        self.pushButton_4.setText(_translate("MainWindow", "Поставщики"))
        self.pushButton_5.setText(_translate("MainWindow", "Оформить заказ"))
        self.pushButton_6.setText(_translate(
            "MainWindow", "Заказы на поставку"))
        self.pushButton_5.clicked.connect(self.openOreder)

    def loadDrugs(self):
        self.tableWidget.setRowCount(0)
        conn = sqlite3.connect("database/apteka.db")
        cursor = conn.cursor()
        drugs = "SELECT * FROM drugs"

        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Название"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Тип"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Стоимость"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Кол-во"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Описание"))

        tablerow = 0
        for row in cursor.execute(drugs):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        for row in cursor.execute(drugs):
            self.tableWidget.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(row[1]))
            self.tableWidget.setItem(
                tablerow, 1, QtWidgets.QTableWidgetItem(row[2]))
            self.tableWidget.setItem(
                tablerow, 2, QtWidgets.QTableWidgetItem(str(row[3])))

            self.tableWidget.setItem(
                tablerow, 3, QtWidgets.QTableWidgetItem(str(row[5])))

            self.tableWidget.setItem(
                tablerow, 4, QtWidgets.QTableWidgetItem(row[4]))
            tablerow += 1
        self.tableWidget.setEditTriggers(self.tableWidget.NoEditTriggers)
        conn.close()

    def loadSupplyOrders(self):
        self.ids = []
        conn = sqlite3.connect("database/apteka.db")
        cursor = conn.cursor()
        orders = "SELECT * FROM orders WHERE type='0'"
        self.tableWidget.setRowCount(0)

        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Товар"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Статус"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Кол-во"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", ""))

        tablerow = 0
        for row in cursor.execute(orders):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        for row in cursor.execute(orders):
            self.ids.append(row[0])
            btn = QtWidgets.QPushButton(self.tableWidget)
            btn.setText('Подтвердить')
            btn.clicked.connect(lambda: self.confirmation(row[0]))

            self.tableWidget.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(str(row[1])))

            if row[2] == 0:
                self.tableWidget.setItem(
                    tablerow, 1, QtWidgets.QTableWidgetItem("Ожидается"))
            else:
                self.tableWidget.setItem(
                    tablerow, 1, QtWidgets.QTableWidgetItem("Завершён"))
            self.tableWidget.setItem(
                tablerow, 2, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setCellWidget(
                tablerow, 3, btn)
            tablerow += 1
        self.tableWidget.setEditTriggers(self.tableWidget.NoEditTriggers)
        cursor.close()
        conn.close()

    def loadBuyOrders(self):
        self.ids = []
        conn = sqlite3.connect("database/apteka.db")
        cursor = conn.cursor()
        orders = "SELECT * FROM orders WHERE type='1'"
        self.tableWidget.setRowCount(0)

        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Номер"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Статус"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Кол-во"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", ""))

        tablerow = 0
        for row in cursor.execute(orders):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        for row in cursor.execute(orders):
            self.ids.append(row[0])
            btn = QtWidgets.QPushButton(self.tableWidget)
            btn.setText('Подтвердить')
            btn.clicked.connect(partial(self.confirmation, row[0]))
            self.tableWidget.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(str(row[0])))
            self.tableWidget.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(str(row[1])))
            if row[2] == 0:
                self.tableWidget.setItem(
                    tablerow, 1, QtWidgets.QTableWidgetItem("Ожидается"))
            else:
                self.tableWidget.setItem(
                    tablerow, 1, QtWidgets.QTableWidgetItem("Завершён"))
            self.tableWidget.setItem(
                tablerow, 2, QtWidgets.QTableWidgetItem(str(row[3])))
            self.tableWidget.setCellWidget(
                tablerow, 3, btn)
            tablerow += 1

        self.tableWidget.setEditTriggers(self.tableWidget.NoEditTriggers)
        cursor.close()
        conn.close()

    def loadProviders(self):
        conn = sqlite3.connect("database/apteka.db")
        cursor = conn.cursor()
        providers = "SELECT * FROM providers"
        self.tableWidget.setRowCount(0)

        _translate = QtCore.QCoreApplication.translate
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Товар"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Статус"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Цена"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", ""))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", ""))

        tablerow = 0
        for row in cursor.execute(providers):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        for row in cursor.execute(providers):
            self.tableWidget.setItem(
                tablerow, 0, QtWidgets.QTableWidgetItem(str(row[1])))
            self.tableWidget.setItem(
                tablerow, 1, QtWidgets.QTableWidgetItem(str(row[2])))
            self.tableWidget.setItem(
                tablerow, 2, QtWidgets.QTableWidgetItem(str(row[3])))
            tablerow += 1
        self.tableWidget.setEditTriggers(self.tableWidget.NoEditTriggers)
        cursor.close()
        conn.close()

    def confirmation(self, id):
        cl = self.tableWidget.currentRow()
        conn = sqlite3.connect("database/apteka.db")
        cursor = conn.cursor()

        name = cursor.execute(
            "SELECT * FROM orders WHERE id=?", (self.ids[cl],)).fetchone()

        value = cursor.execute(
            "SELECT amount FROM drugs WHERE title=?", (name[1],)).fetchone()
        if name[2] == 0:
            if name[4] == 0:

                new_value = value[0] + name[3]
                cursor.execute(
                    "UPDATE drugs SET amount=? WHERE title=?", (new_value, name[1],))
            else:

                new_value = value[0] - name[3]
                cursor.execute(
                    "UPDATE drugs SET amount=? WHERE title=?", (new_value, name[1],))
        cursor.execute("UPDATE orders SET status=1 WHERE id=?",
                       (self.ids[cl],))
        conn.commit()
        cursor.close()
        conn.close()

    def openModal(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.window)
        self.window.show()

    def openAnalytics(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Analytics()
        self.ui.setupUi(self.window)
        self.window.show()

    def openOreder(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Order()
        self.ui.setupUi(self.window)
        self.window.show()
