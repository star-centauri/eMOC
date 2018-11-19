# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colaboration.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(331, 272)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("background-color: rgb(38, 38, 38);\n"
"color: rgb(242, 242, 242);")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 230, 301, 31))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_cancel = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cancel.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_2.addWidget(self.btn_cancel)
        self.btn_start = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_start.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout_2.addWidget(self.btn_start)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 121, 16))
        self.label_3.setObjectName("label_3")
        self.btn_remove = QtWidgets.QPushButton(Form)
        self.btn_remove.setGeometry(QtCore.QRect(130, 190, 101, 23))
        self.btn_remove.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.btn_remove.setObjectName("btn_remove")
        self.edit_add_url = QtWidgets.QLineEdit(Form)
        self.edit_add_url.setGeometry(QtCore.QRect(10, 30, 301, 20))
        self.edit_add_url.setObjectName("edit_add_url")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.label_4.setObjectName("label_4")
        self.list_url = QtWidgets.QListWidget(Form)
        self.list_url.setGeometry(QtCore.QRect(10, 100, 301, 81))
        self.list_url.setObjectName("list_url")
        self.btn_add = QtWidgets.QPushButton(Form)
        self.btn_add.setGeometry(QtCore.QRect(10, 190, 111, 23))
        self.btn_add.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_add.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.btn_add.setObjectName("btn_add")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Observação colaborativa"))
        self.btn_cancel.setText(_translate("Form", "Cancelar"))
        self.btn_start.setText(_translate("Form", "Começar"))
        self.label_3.setText(_translate("Form", "Adicionar URL Servidor:"))
        self.btn_remove.setText(_translate("Form", "Remover Servidor"))
        self.label_4.setText(_translate("Form", "Servidores:"))
        self.btn_add.setText(_translate("Form", "Adicionar Servidor"))

