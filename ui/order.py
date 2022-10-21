from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3


class Ui_Order(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 400)
        Dialog.setMaximumSize(QtCore.QSize(500, 400))
        Dialog.setSizeIncrement(QtCore.QSize(500, 400))
        Dialog.setBaseSize(QtCore.QSize(500, 400))
        Dialog.setStyleSheet("background: #f1f1f1;")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 130, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 10, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("width:100%;text-align:center;")
        self.label_2.setObjectName("label_2")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(70, 60, 371, 281))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setMaximumSize(QtCore.QSize(60, 16777215))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("width: 50%;\n"
                                    "")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        self.verticalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.verticalLayout.addWidget(self.radioButton_2)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("border: 1px solid #000;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.createOrder)
        self.verticalLayout.addWidget(self.pushButton)
        self.fillData()
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Заказ"))
        self.label.setText(_translate("Dialog", "Количество"))
        self.label_2.setText(_translate("Dialog", "Оформить заказ"))
        self.radioButton.setText(_translate("Dialog", "Поставка"))
        self.radioButton_2.setText(_translate("Dialog", "Выдача"))
        self.pushButton.setText(_translate("Dialog", "Добавить"))

    def fillData(self):
        conn = sqlite3.connect("database/apteka.db")
        cur = conn.cursor()
        drugs = "SELECT title FROM drugs"
        for i in cur.execute(drugs):
            self.comboBox.addItem(i[0])

        cur.close()
        conn.close()

    def showMsg(self, title, text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.exec_()

    def createOrder(self):
        flag = True
        conn = sqlite3.connect("database/apteka.db")
        cur = conn.cursor()

        title = self.comboBox.currentText()
        try:
            amount = abs(int(self.lineEdit.text()))
        except:
            self.showMsg("Ошибка", "Неверное количество")
            flag = False
        capture = -1
        status = False
        if self.radioButton.isChecked():
            capture = 0
        else:
            capture = 1
            quantity = cur.execute(
                "SELECT amount FROM drugs WHERE title=?", (title,)).fetchone()[0]
            if amount > quantity:
                self.showMsg("Ошибка", "Недостаточно товара на складе")
                flag = False
        if flag:
            cur.execute(
                "INSERT INTO orders (title, status, amount, type) VALUES(?, ?, ?, ?)", (title, status, amount, capture,))
            self.showMsg("Сообщение", "Успешно добавлено")
        self.lineEdit.setText("")
        conn.commit()

        cur.close()
        conn.close()
