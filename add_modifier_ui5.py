# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_modifier.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(962, 755)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet("background-color: rgb(38, 38, 38);\n"
"color: rgb(242, 242, 242);")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbModifier = QtWidgets.QLabel(Dialog)
        self.lbModifier.setObjectName("lbModifier")
        self.verticalLayout_2.addWidget(self.lbModifier)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.leModifier = QtWidgets.QLineEdit(Dialog)
        self.leModifier.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leModifier.sizePolicy().hasHeightForWidth())
        self.leModifier.setSizePolicy(sizePolicy)
        self.leModifier.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.leModifier.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.leModifier.setAcceptDrops(True)
        self.leModifier.setText("")
        self.leModifier.setObjectName("leModifier")
        self.horizontalLayout_6.addWidget(self.leModifier)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.lbCode = QtWidgets.QLabel(Dialog)
        self.lbCode.setObjectName("lbCode")
        self.verticalLayout_2.addWidget(self.lbCode)
        self.leCode = QtWidgets.QLineEdit(Dialog)
        self.leCode.setObjectName("leCode")
        self.verticalLayout_2.addWidget(self.leCode)
        self.lbCodeHelp = QtWidgets.QLabel(Dialog)
        self.lbCodeHelp.setWordWrap(True)
        self.lbCodeHelp.setObjectName("lbCodeHelp")
        self.verticalLayout_2.addWidget(self.lbCodeHelp)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_5.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pbAddModifier = QtWidgets.QPushButton(Dialog)
        self.pbAddModifier.setStyleSheet("background-color: rgb(89, 89, 89);")
        self.pbAddModifier.setText("")
        self.pbAddModifier.setObjectName("pbAddModifier")
        self.verticalLayout_3.addWidget(self.pbAddModifier)
        self.pbModifyModifier = QtWidgets.QPushButton(Dialog)
        self.pbModifyModifier.setStyleSheet("background-color: rgb(89, 89, 89);")
        self.pbModifyModifier.setText("")
        self.pbModifyModifier.setObjectName("pbModifyModifier")
        self.verticalLayout_3.addWidget(self.pbModifyModifier)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.horizontalLayout_5.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidgetModifiersSets = QtWidgets.QTabWidget(Dialog)
        self.tabWidgetModifiersSets.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tabWidgetModifiersSets.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidgetModifiersSets.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidgetModifiersSets.setElideMode(QtCore.Qt.ElideNone)
        self.tabWidgetModifiersSets.setDocumentMode(True)
        self.tabWidgetModifiersSets.setObjectName("tabWidgetModifiersSets")
        self.verticalLayout.addWidget(self.tabWidgetModifiersSets)
        self.lbSetName = QtWidgets.QLabel(Dialog)
        self.lbSetName.setObjectName("lbSetName")
        self.verticalLayout.addWidget(self.lbSetName)
        self.leSetName = QtWidgets.QLineEdit(Dialog)
        self.leSetName.setObjectName("leSetName")
        self.verticalLayout.addWidget(self.leSetName)
        self.lbType = QtWidgets.QLabel(Dialog)
        self.lbType.setObjectName("lbType")
        self.verticalLayout.addWidget(self.lbType)
        self.cbType = QtWidgets.QComboBox(Dialog)
        self.cbType.setObjectName("cbType")
        self.cbType.addItem("")
        self.cbType.addItem("")
        self.verticalLayout.addWidget(self.cbType)
        self.lbValues = QtWidgets.QLabel(Dialog)
        self.lbValues.setObjectName("lbValues")
        self.verticalLayout.addWidget(self.lbValues)
        self.lwModifiers = QtWidgets.QListWidget(Dialog)
        self.lwModifiers.setObjectName("lwModifiers")
        self.verticalLayout.addWidget(self.lwModifiers)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pbMoveUp = QtWidgets.QPushButton(Dialog)
        self.pbMoveUp.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbMoveUp.setObjectName("pbMoveUp")
        self.horizontalLayout.addWidget(self.pbMoveUp)
        self.pbMoveDown = QtWidgets.QPushButton(Dialog)
        self.pbMoveDown.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbMoveDown.setObjectName("pbMoveDown")
        self.horizontalLayout.addWidget(self.pbMoveDown)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.pbRemoveModifier = QtWidgets.QPushButton(Dialog)
        self.pbRemoveModifier.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbRemoveModifier.setObjectName("pbRemoveModifier")
        self.verticalLayout.addWidget(self.pbRemoveModifier)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pbAddSet = QtWidgets.QPushButton(Dialog)
        self.pbAddSet.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbAddSet.setObjectName("pbAddSet")
        self.horizontalLayout_3.addWidget(self.pbAddSet)
        self.pbRemoveSet = QtWidgets.QPushButton(Dialog)
        self.pbRemoveSet.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbRemoveSet.setObjectName("pbRemoveSet")
        self.horizontalLayout_3.addWidget(self.pbRemoveSet)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pbMoveSetLeft = QtWidgets.QPushButton(Dialog)
        self.pbMoveSetLeft.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbMoveSetLeft.setObjectName("pbMoveSetLeft")
        self.horizontalLayout_4.addWidget(self.pbMoveSetLeft)
        self.pbMoveSetRight = QtWidgets.QPushButton(Dialog)
        self.pbMoveSetRight.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbMoveSetRight.setObjectName("pbMoveSetRight")
        self.horizontalLayout_4.addWidget(self.pbMoveSetRight)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.pbCancel = QtWidgets.QPushButton(Dialog)
        self.pbCancel.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout_2.addWidget(self.pbCancel)
        self.pbOK = QtWidgets.QPushButton(Dialog)
        self.pbOK.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbOK.setObjectName("pbOK")
        self.horizontalLayout_2.addWidget(self.pbOK)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)

        self.retranslateUi(Dialog)
        self.tabWidgetModifiersSets.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Definir Modificadores"))
        self.lbModifier.setText(_translate("Dialog", "Modificador"))
        self.lbCode.setText(_translate("Dialog", "Chave de atalho"))
        self.lbCodeHelp.setText(_translate("Dialog", "O código da chave não faz distinção entre maiúsculas e minúsculas. Digite um caractere ou uma tecla de função (F1, F2 ... F12)"))
        self.lbSetName.setText(_translate("Dialog", "Nome do conjunto"))
        self.lbType.setText(_translate("Dialog", "Tipo de modificador"))
        self.cbType.setItemText(0, _translate("Dialog", "Seleção única"))
        self.cbType.setItemText(1, _translate("Dialog", "Seleção múltipla"))
        self.lbValues.setText(_translate("Dialog", "Valores"))
        self.pbMoveUp.setText(_translate("Dialog", "Mover o modificador para cima"))
        self.pbMoveDown.setText(_translate("Dialog", "Mover modificador para baixo"))
        self.pbRemoveModifier.setText(_translate("Dialog", "Remover modificador"))
        self.pbAddSet.setText(_translate("Dialog", "Adicionar modificadores"))
        self.pbRemoveSet.setText(_translate("Dialog", "Remover modificadores"))
        self.pbMoveSetLeft.setText(_translate("Dialog", "Mover para esquerda"))
        self.pbMoveSetRight.setText(_translate("Dialog", "Mover para direita"))
        self.pbCancel.setText(_translate("Dialog", "Cancelar"))
        self.pbOK.setText(_translate("Dialog", "OK"))

