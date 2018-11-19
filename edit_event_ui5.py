# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_event.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(342, 410)
        Form.setStyleSheet("background-color: rgb(38, 38, 38);\n"
"color: rgb(242, 242, 242);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.teTime = QtWidgets.QTimeEdit(Form)
        self.teTime.setObjectName("teTime")
        self.horizontalLayout_2.addWidget(self.teTime)
        self.dsbTime = QtWidgets.QDoubleSpinBox(Form)
        self.dsbTime.setDecimals(3)
        self.dsbTime.setMaximum(9999999.0)
        self.dsbTime.setObjectName("dsbTime")
        self.horizontalLayout_2.addWidget(self.dsbTime)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lbSubject = QtWidgets.QLabel(Form)
        self.lbSubject.setObjectName("lbSubject")
        self.horizontalLayout_4.addWidget(self.lbSubject)
        self.cobSubject = QtWidgets.QComboBox(Form)
        self.cobSubject.setObjectName("cobSubject")
        self.horizontalLayout_4.addWidget(self.cobSubject)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.cobCode = QtWidgets.QComboBox(Form)
        self.cobCode.setObjectName("cobCode")
        self.horizontalLayout_5.addWidget(self.cobCode)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.leComment = QtWidgets.QPlainTextEdit(Form)
        self.leComment.setObjectName("leComment")
        self.verticalLayout.addWidget(self.leComment)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbCancel = QtWidgets.QPushButton(Form)
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout.addWidget(self.pbCancel)
        self.pbOK = QtWidgets.QPushButton(Form)
        self.pbOK.setDefault(True)
        self.pbOK.setObjectName("pbOK")
        self.horizontalLayout.addWidget(self.pbOK)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Edit event"))
        self.label.setText(_translate("Form", "Tempo"))
        self.teTime.setDisplayFormat(_translate("Form", "hh:mm:ss.zzz"))
        self.lbSubject.setText(_translate("Form", "Sujeito"))
        self.label_2.setText(_translate("Form", "Código"))
        self.label_4.setText(_translate("Form", "Comentário"))
        self.pbCancel.setText(_translate("Form", "Cancelar"))
        self.pbOK.setText(_translate("Form", "OK"))

