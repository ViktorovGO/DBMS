# Form implementation generated from reading ui file 'AddDialog2.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AddDialog2(object):
    def setupUi(self, AddDialog2):
        AddDialog2.setObjectName("AddDialog2")
        AddDialog2.resize(655, 200)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("dollar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        AddDialog2.setWindowIcon(icon)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(AddDialog2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(170, 60, 361, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_regnum = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_regnum.setFont(font)
        self.label_regnum.setObjectName("label_regnum")
        self.horizontalLayout_4.addWidget(self.label_regnum)
        self.label_exec_date = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_exec_date.setFont(font)
        self.label_exec_date.setObjectName("label_exec_date")
        self.horizontalLayout_4.addWidget(self.label_exec_date)
        self.horizontalLayoutWidget = QtWidgets.QWidget(AddDialog2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(170, 100, 131, 22))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SU = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.SU.setFont(font)
        self.SU.setObjectName("SU")
        self.horizontalLayout.addWidget(self.SU)
        self.line_regnum = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.line_regnum.setObjectName("line_regnum")
        self.horizontalLayout.addWidget(self.line_regnum)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(AddDialog2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(250, 160, 160, 31))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_ok = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.button_ok.setObjectName("button_ok")
        self.horizontalLayout_2.addWidget(self.button_ok)
        self.button_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.button_cancel.setObjectName("button_cancel")
        self.horizontalLayout_2.addWidget(self.button_cancel)
        self.textBrowser = QtWidgets.QTextBrowser(AddDialog2)
        self.textBrowser.setGeometry(QtCore.QRect(170, 10, 256, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.date_button = QtWidgets.QPushButton(AddDialog2)
        self.date_button.setGeometry(QtCore.QRect(350, 120, 141, 23))
        self.date_button.setObjectName("date_button")
        self.line_date = QtWidgets.QLineEdit(AddDialog2)
        self.line_date.setEnabled(False)
        self.line_date.setGeometry(QtCore.QRect(350, 100, 141, 20))
        self.line_date.setObjectName("line_date")

        self.retranslateUi(AddDialog2)
        QtCore.QMetaObject.connectSlotsByName(AddDialog2)

    def retranslateUi(self, AddDialog2):
        _translate = QtCore.QCoreApplication.translate
        AddDialog2.setWindowTitle(_translate("AddDialog2", "Добавление записи в Act_isp"))
        self.label_regnum.setText(_translate("AddDialog2", "Код бумаги"))
        self.label_exec_date.setText(_translate("AddDialog2", "Дата погашения"))
        self.SU.setText(_translate("AddDialog2", "SU"))
        self.label_2.setText(_translate("AddDialog2", "RFMS"))
        self.button_ok.setText(_translate("AddDialog2", "Ок"))
        self.button_cancel.setText(_translate("AddDialog2", "Отмена"))
        self.date_button.setText(_translate("AddDialog2", "Выбрать дату"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddDialog2 = QtWidgets.QDialog()
    ui = Ui_AddDialog2()
    ui.setupUi(AddDialog2)
    AddDialog2.show()
    sys.exit(app.exec())