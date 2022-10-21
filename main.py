import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from ui.application import Ui_MainWindow


class Ui_Auth(object):

    def signal_handler(self, value):
        QtWidgets.QMessageBox.about(self, 'Оповещение', value)

    def openwindow(self):
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        con = sqlite3.connect('./database/apteka.db')
        cur = con.cursor()

        value = cur.execute(
            'SELECT * FROM users WHERE login=?', (login,)).fetchall()

        if value != [] and value[0][2] == password:
            self.Dialog = QtWidgets.QMainWindow()
            self.ui = Ui_MainWindow(value[0][3])
            self.ui.setupUi(self.Dialog)
            win.hide()
            self.Dialog.show()
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Ошибка")
            msg.setText("Неверный логин или пароль")
            msg.exec_()
        cur.close()
        con.close()

    def setupUi(self, Auth):
        Auth.setObjectName("Auth")
        Auth.resize(450, 350)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Auth.sizePolicy().hasHeightForWidth())
        Auth.setSizePolicy(sizePolicy)
        Auth.setMinimumSize(QtCore.QSize(450, 350))
        Auth.setMaximumSize(QtCore.QSize(450, 350))
        Auth.setBaseSize(QtCore.QSize(450, 350))
        font = QtGui.QFont()
        font.setPointSize(17)
        Auth.setFont(font)
        Auth.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "./green.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Auth.setWindowIcon(icon)
        Auth.setAutoFillBackground(False)
        Auth.setStyleSheet("background:rgb(246, 253, 255);")
        Auth.setSizeGripEnabled(False)
        self.layoutWidget = QtWidgets.QWidget(Auth)
        self.layoutWidget.setGeometry(QtCore.QRect(90, 80, 277, 201))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setInputMask("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_3.addWidget(self.lineEdit_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.clicked.connect(self.openwindow)

        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(
            "margin-top: 10px;border: 1px solid #000;")
        self.pushButton.setObjectName("pushButton")

        self.verticalLayout_6.addWidget(self.pushButton)
        self.label_2 = QtWidgets.QLabel(Auth)
        self.label_2.setGeometry(QtCore.QRect(190, 10, 61, 51))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(
            "./green.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Auth)
        QtCore.QMetaObject.connectSlotsByName(Auth)

    def retranslateUi(self, Auth):
        _translate = QtCore.QCoreApplication.translate
        Auth.setWindowTitle(_translate("Auth", "Apteka - Вход"))
        self.label.setText(_translate("Auth", "Введите логин и пароль"))
        self.lineEdit.setPlaceholderText(_translate("Auth", "Логин"))
        self.lineEdit_2.setPlaceholderText(_translate("Auth", "Пароль"))
        self.pushButton.setText(_translate(
            "Auth", "Ввести"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QDialog()
    ui = Ui_Auth()
    ui.setupUi(win)
    win.show()
    sys.exit(app.exec_())
