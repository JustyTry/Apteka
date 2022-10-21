from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3


class Ui_Analytics(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 400)
        Dialog.setMinimumSize(QtCore.QSize(400, 400))
        Dialog.setMaximumSize(QtCore.QSize(400, 400))
        Dialog.setSizeIncrement(QtCore.QSize(400, 400))
        font = QtGui.QFont()
        font.setPointSize(14)
        Dialog.setFont(font)
        Dialog.setStyleSheet("background: #f1f1f1;")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(30, 30, 331, 22))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(150, 110, 91, 191))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(30, 110, 98, 191))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.widget.setFont(font)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.loadData()
        self.doReport()
        self.comboBox.currentTextChanged.connect(self.doReport)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Отчёт"))
        self.label.setText(_translate("Dialog", "Расходы:"))
        self.label_2.setText(_translate("Dialog", "Доход:"))
        self.label_3.setText(_translate("Dialog", "Прибыль:"))

    def loadData(self):
        conn = sqlite3.connect("database/apteka.db")
        cur = conn.cursor()
        drugs = "SELECT title FROM drugs"
        self.comboBox.addItem("Общее")
        for i in cur.execute(drugs):
            self.comboBox.addItem(i[0])

        cur.close()
        conn.close()

    def doReport(self):
        conn = sqlite3.connect("database/apteka.db")
        cur = conn.cursor()
        loses = 0
        profit = 0
        revenue = 0
        if self.comboBox.currentText() == "Общее":
            costs = cur.execute(
                "SELECT price FROM providers").fetchall()
            prices = cur.execute(
                "SELECT price FROM drugs").fetchall()

            for j in range(len(prices)):
                print(costs[j][0])
                loses += int(costs[j][0])
                profit += int(prices[j][0])
                revenue = profit - loses
            self.label_4.setText(str(loses))
            self.label_5.setText(str(profit))
            self.label_6.setText(str(revenue))
        else:
            title = self.comboBox.currentText()
            cost = cur.execute(
                "SELECT price FROM providers WHERE product=?", (title,)).fetchone()
            price = cur.execute(
                "SELECT price FROM drugs WHERE title=?", (title,)).fetchone()
            loses = int(cost[0])
            profit = int(price[0])
            revenue = profit - loses
            self.label_4.setText(str(loses))
            self.label_5.setText(str(profit))
            self.label_6.setText(str(revenue))
        cur.close()
        conn.close()
