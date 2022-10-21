
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(420, 350)
        Dialog.setMinimumSize(QtCore.QSize(420, 350))
        Dialog.setMaximumSize(QtCore.QSize(420, 350))
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(60, 30, 301, 311))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(self.widget)
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.widget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.createUser)
        self.verticalLayout_2.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate(
            "Dialog", "Создание пользователя"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Логин"))
        self.lineEdit_2.setPlaceholderText(_translate("Dialog", "Пароль"))
        self.lineEdit_3.setPlaceholderText(
            _translate("Dialog", "Повтор пароля"))
        self.radioButton.setText(_translate("Dialog", "Админ"))
        self.radioButton_2.setText(_translate("Dialog", "Аналитик"))
        self.radioButton_3.setText(_translate("Dialog", "Пользователь"))
        self.pushButton.setText(_translate("Dialog", "Создать"))

    def createUser(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        repassword = self.lineEdit_3.text()
        role = ''
        if self.radioButton.isChecked():
            role = 'admin'
        elif self.radioButton_2.isChecked():
            role = 'analyst'
        elif self.radioButton_3.isChecked():
            role = 'user'

        conn = sqlite3.connect("database/apteka.db")
        cur = conn.cursor()
        logger = cur.execute(
            'SELECT * FROM users WHERE login=?', (login,)).fetchall()
        if logger == []:
            if password == repassword and password != '':
                cur.execute(
                    "INSERT INTO users (login, password, role) VALUES(?, ?, ?)", (login, password, role,))
                conn.commit()
                msg = QMessageBox()
                msg.setWindowTitle("Сообщение")
                msg.setText("Успешно создано")
                msg.exec_()

            else:
                msg = QMessageBox()
                msg.setWindowTitle("Ошибка")
                msg.setText("Проверьте пароль")
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Такой логин уже используется")
            msg.exec_()
