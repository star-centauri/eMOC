# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlgProject(object):
    def setupUi(self, dlgProject):
        dlgProject.setObjectName("dlgProject")
        dlgProject.resize(1121, 973)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        dlgProject.setWindowIcon(icon)
        dlgProject.setStyleSheet("background-color: rgb(38, 38, 38);\n"
"color: rgb(242, 242, 242);")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(dlgProject)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.tabProject = QtWidgets.QTabWidget(dlgProject)
        self.tabProject.setStyleSheet("QTabBar::tab  {\n"
"    background: rgb(38, 38, 38);\n"
"    border: 1px solid #C4C4C3;\n"
"    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
"    border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"    min-width: 8ex;\n"
"    padding: 2px;\n"
"}")
        self.tabProject.setObjectName("tabProject")
        self.tabInformation = QtWidgets.QWidget()
        self.tabInformation.setObjectName("tabInformation")
        self.formLayout = QtWidgets.QFormLayout(self.tabInformation)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.tabInformation)
        self.label.setStyleSheet("color: rgb(242, 242, 242);")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.label)
        self.leProjectName = QtWidgets.QLineEdit(self.tabInformation)
        self.leProjectName.setStyleSheet("color: rgb(242, 242, 242);")
        self.leProjectName.setObjectName("leProjectName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.leProjectName)
        self.lbProjectFilePath = QtWidgets.QLabel(self.tabInformation)
        self.lbProjectFilePath.setStyleSheet("color: rgb(242, 242, 242);")
        self.lbProjectFilePath.setObjectName("lbProjectFilePath")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.SpanningRole, self.lbProjectFilePath)
        self.label_7 = QtWidgets.QLabel(self.tabInformation)
        self.label_7.setStyleSheet("color: rgb(242, 242, 242);")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.dteDate = QtWidgets.QDateTimeEdit(self.tabInformation)
        self.dteDate.setStyleSheet("color: rgb(242, 242, 242);")
        self.dteDate.setCalendarPopup(True)
        self.dteDate.setObjectName("dteDate")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.dteDate)
        self.label_6 = QtWidgets.QLabel(self.tabInformation)
        self.label_6.setStyleSheet("color: rgb(242, 242, 242);")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.SpanningRole, self.label_6)
        self.teDescription = QtWidgets.QPlainTextEdit(self.tabInformation)
        self.teDescription.setStyleSheet("color: rgb(242, 242, 242);")
        self.teDescription.setObjectName("teDescription")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.teDescription)
        self.lbTimeFormat = QtWidgets.QLabel(self.tabInformation)
        self.lbTimeFormat.setStyleSheet("color: rgb(242, 242, 242);")
        self.lbTimeFormat.setObjectName("lbTimeFormat")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.lbTimeFormat)
        self.rbSeconds = QtWidgets.QRadioButton(self.tabInformation)
        self.rbSeconds.setStyleSheet("color: rgb(242, 242, 242);")
        self.rbSeconds.setChecked(True)
        self.rbSeconds.setObjectName("rbSeconds")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.rbSeconds)
        self.rbHMS = QtWidgets.QRadioButton(self.tabInformation)
        self.rbHMS.setStyleSheet("color: rgb(242, 242, 242);")
        self.rbHMS.setObjectName("rbHMS")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.rbHMS)
        self.tabProject.addTab(self.tabInformation, "")
        self.tabConfiguration = QtWidgets.QWidget()
        self.tabConfiguration.setObjectName("tabConfiguration")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tabConfiguration)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.twBehaviors = QtWidgets.QTableWidget(self.tabConfiguration)
        self.twBehaviors.setAutoFillBackground(False)
        self.twBehaviors.setStyleSheet("QTableWidget::item {\n"
"  selection-background-color: rgb(89, 89, 89);\n"
"  selection-color: rgb(242, 242, 242);\n"
"}\n"
"\n"
"QTableWidget::item:selected{\n"
"    selection-background-color: rgb(89, 89, 89);\n"
"    selection-color: rgb(242, 242, 242); \n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"  background-color: rgb(89, 89, 89);\n"
"  color: rgb(242, 242, 242);\n"
"}\n"
"\n"
"QTableWidget QListWidget {\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: rgb(242, 242, 242);\n"
"}")
        self.twBehaviors.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.twBehaviors.setMidLineWidth(0)
        self.twBehaviors.setAlternatingRowColors(False)
        self.twBehaviors.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.twBehaviors.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.twBehaviors.setWordWrap(False)
        self.twBehaviors.setObjectName("twBehaviors")
        self.twBehaviors.setColumnCount(5)
        self.twBehaviors.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twBehaviors.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBehaviors.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBehaviors.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBehaviors.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.twBehaviors.setHorizontalHeaderItem(4, item)
        self.twBehaviors.horizontalHeader().setSortIndicatorShown(False)
        self.twBehaviors.verticalHeader().setSortIndicatorShown(False)
        self.horizontalLayout_11.addWidget(self.twBehaviors)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.pbAddBehavior = QtWidgets.QPushButton(self.tabConfiguration)
        self.pbAddBehavior.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbAddBehavior.setObjectName("pbAddBehavior")
        self.verticalLayout_11.addWidget(self.pbAddBehavior)
        self.pbCloneBehavior = QtWidgets.QPushButton(self.tabConfiguration)
        self.pbCloneBehavior.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbCloneBehavior.setObjectName("pbCloneBehavior")
        self.verticalLayout_11.addWidget(self.pbCloneBehavior)
        self.pbRemoveBehavior = QtWidgets.QPushButton(self.tabConfiguration)
        self.pbRemoveBehavior.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbRemoveBehavior.setObjectName("pbRemoveBehavior")
        self.verticalLayout_11.addWidget(self.pbRemoveBehavior)
        self.pbRemoveAllBehaviors = QtWidgets.QPushButton(self.tabConfiguration)
        self.pbRemoveAllBehaviors.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbRemoveAllBehaviors.setObjectName("pbRemoveAllBehaviors")
        self.verticalLayout_11.addWidget(self.pbRemoveAllBehaviors)
        self.pbBehaviorsCategories = QtWidgets.QPushButton(self.tabConfiguration)
        self.pbBehaviorsCategories.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbBehaviorsCategories.setObjectName("pbBehaviorsCategories")
        self.verticalLayout_11.addWidget(self.pbBehaviorsCategories)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem)
        self.pbImportBehaviorsFromProject = QtWidgets.QPushButton(self.tabConfiguration)
        self.pbImportBehaviorsFromProject.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbImportBehaviorsFromProject.setObjectName("pbImportBehaviorsFromProject")
        self.verticalLayout_11.addWidget(self.pbImportBehaviorsFromProject)
        self.pbImportFromTextFile = QtWidgets.QPushButton(self.tabConfiguration)
        self.pbImportFromTextFile.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbImportFromTextFile.setObjectName("pbImportFromTextFile")
        self.verticalLayout_11.addWidget(self.pbImportFromTextFile)
        self.pbExportEthogram = QtWidgets.QPushButton(self.tabConfiguration)
        self.pbExportEthogram.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbExportEthogram.setObjectName("pbExportEthogram")
        self.verticalLayout_11.addWidget(self.pbExportEthogram)
        self.horizontalLayout_11.addLayout(self.verticalLayout_11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_11)
        self.lbObservationsState = QtWidgets.QLabel(self.tabConfiguration)
        self.lbObservationsState.setObjectName("lbObservationsState")
        self.verticalLayout_5.addWidget(self.lbObservationsState)
        self.verticalLayout_10.addLayout(self.verticalLayout_5)
        self.tabProject.addTab(self.tabConfiguration, "")
        self.tabSubjects = QtWidgets.QWidget()
        self.tabSubjects.setObjectName("tabSubjects")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.tabSubjects)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout()
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.twSubjects = QtWidgets.QTableWidget(self.tabSubjects)
        self.twSubjects.setAutoFillBackground(False)
        self.twSubjects.setStyleSheet("QTableWidget::item {\n"
"  selection-background-color:rgb(38, 38, 38);\n"
"  selection-color: rgb(242, 242, 242);\n"
"}\n"
"\n"
"QTableWidget::item:selected{\n"
"    selection-background-color:rgb(89, 89, 89);\n"
"    selection-color: rgb(242, 242, 242); \n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"  background-color: rgb(89, 89, 89);\n"
"  color: rgb(242, 242, 242);\n"
"}\n"
"\n"
"QTableWidget QListWidget {\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: rgb(242, 242, 242);\n"
"}")
        self.twSubjects.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.twSubjects.setMidLineWidth(0)
        self.twSubjects.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.twSubjects.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.twSubjects.setObjectName("twSubjects")
        self.twSubjects.setColumnCount(3)
        self.twSubjects.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twSubjects.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twSubjects.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twSubjects.setHorizontalHeaderItem(2, item)
        self.horizontalLayout_12.addWidget(self.twSubjects)
        self.verticalLayout_15 = QtWidgets.QVBoxLayout()
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.pbAddSubject = QtWidgets.QPushButton(self.tabSubjects)
        self.pbAddSubject.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbAddSubject.setObjectName("pbAddSubject")
        self.verticalLayout_15.addWidget(self.pbAddSubject)
        self.pbRemoveSubject = QtWidgets.QPushButton(self.tabSubjects)
        self.pbRemoveSubject.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbRemoveSubject.setObjectName("pbRemoveSubject")
        self.verticalLayout_15.addWidget(self.pbRemoveSubject)
        self.pbImportSubjectsFromProject = QtWidgets.QPushButton(self.tabSubjects)
        self.pbImportSubjectsFromProject.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbImportSubjectsFromProject.setObjectName("pbImportSubjectsFromProject")
        self.verticalLayout_15.addWidget(self.pbImportSubjectsFromProject)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_15.addItem(spacerItem1)
        self.horizontalLayout_12.addLayout(self.verticalLayout_15)
        self.verticalLayout_14.addLayout(self.horizontalLayout_12)
        self.lbSubjectsState = QtWidgets.QLabel(self.tabSubjects)
        self.lbSubjectsState.setObjectName("lbSubjectsState")
        self.verticalLayout_14.addWidget(self.lbSubjectsState)
        self.verticalLayout_16.addLayout(self.verticalLayout_14)
        self.tabProject.addTab(self.tabSubjects, "")
        self.tabIndependentVariables = QtWidgets.QWidget()
        self.tabIndependentVariables.setObjectName("tabIndependentVariables")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.tabIndependentVariables)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.twVariables = QtWidgets.QTableWidget(self.tabIndependentVariables)
        self.twVariables.setAutoFillBackground(False)
        self.twVariables.setStyleSheet("QTableWidget::item {\n"
"  selection-background-color: rgb(89, 89, 89);\n"
"  selection-color: rgb(242, 242, 242);\n"
"}\n"
"\n"
"QTableWidget::item:selected{\n"
"    selection-background-color: rgb(89, 89, 89);\n"
"    selection-color: rgb(242, 242, 242); \n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"  background-color: rgb(89, 89, 89);\n"
"  color: rgb(242, 242, 242);\n"
"}\n"
"\n"
"QTableWidget QListWidget {\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: rgb(242, 242, 242);\n"
"}")
        self.twVariables.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.twVariables.setMidLineWidth(0)
        self.twVariables.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.twVariables.setDragDropOverwriteMode(False)
        self.twVariables.setAlternatingRowColors(True)
        self.twVariables.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.twVariables.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.twVariables.setObjectName("twVariables")
        self.twVariables.setColumnCount(5)
        self.twVariables.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twVariables.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twVariables.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twVariables.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twVariables.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.twVariables.setHorizontalHeaderItem(4, item)
        self.twVariables.horizontalHeader().setSortIndicatorShown(True)
        self.verticalLayout_2.addWidget(self.twVariables)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.tabIndependentVariables)
        self.label_2.setMinimumSize(QtCore.QSize(120, 0))
        self.label_2.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.leLabel = QtWidgets.QLineEdit(self.tabIndependentVariables)
        self.leLabel.setObjectName("leLabel")
        self.horizontalLayout_3.addWidget(self.leLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.tabIndependentVariables)
        self.label_3.setMinimumSize(QtCore.QSize(120, 0))
        self.label_3.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.leDescription = QtWidgets.QLineEdit(self.tabIndependentVariables)
        self.leDescription.setObjectName("leDescription")
        self.horizontalLayout_5.addWidget(self.leDescription)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_8 = QtWidgets.QLabel(self.tabIndependentVariables)
        self.label_8.setMinimumSize(QtCore.QSize(120, 0))
        self.label_8.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_6.addWidget(self.label_8)
        self.cbType = QtWidgets.QComboBox(self.tabIndependentVariables)
        self.cbType.setMinimumSize(QtCore.QSize(120, 0))
        self.cbType.setObjectName("cbType")
        self.horizontalLayout_6.addWidget(self.cbType)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.tabIndependentVariables)
        self.label_4.setMinimumSize(QtCore.QSize(120, 0))
        self.label_4.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_7.addWidget(self.label_4)
        self.lePredefined = QtWidgets.QLineEdit(self.tabIndependentVariables)
        self.lePredefined.setObjectName("lePredefined")
        self.horizontalLayout_7.addWidget(self.lePredefined)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.tabIndependentVariables)
        self.label_9.setMinimumSize(QtCore.QSize(120, 0))
        self.label_9.setStyleSheet("background-color: rgb(38, 38, 38);")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.dte_default_date = QtWidgets.QDateTimeEdit(self.tabIndependentVariables)
        self.dte_default_date.setObjectName("dte_default_date")
        self.horizontalLayout_8.addWidget(self.dte_default_date)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.tabIndependentVariables)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.leSetValues = QtWidgets.QLineEdit(self.tabIndependentVariables)
        self.leSetValues.setObjectName("leSetValues")
        self.horizontalLayout_9.addWidget(self.leSetValues)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem7)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_13.addLayout(self.verticalLayout_2)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.pbAddVariable = QtWidgets.QPushButton(self.tabIndependentVariables)
        self.pbAddVariable.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbAddVariable.setObjectName("pbAddVariable")
        self.verticalLayout_12.addWidget(self.pbAddVariable)
        self.pbRemoveVariable = QtWidgets.QPushButton(self.tabIndependentVariables)
        self.pbRemoveVariable.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbRemoveVariable.setObjectName("pbRemoveVariable")
        self.verticalLayout_12.addWidget(self.pbRemoveVariable)
        self.pbImportVarFromProject = QtWidgets.QPushButton(self.tabIndependentVariables)
        self.pbImportVarFromProject.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbImportVarFromProject.setObjectName("pbImportVarFromProject")
        self.verticalLayout_12.addWidget(self.pbImportVarFromProject)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_12.addItem(spacerItem8)
        self.horizontalLayout_13.addLayout(self.verticalLayout_12)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_13)
        self.tabProject.addTab(self.tabIndependentVariables, "")
        self.tabObservations = QtWidgets.QWidget()
        self.tabObservations.setObjectName("tabObservations")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabObservations)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.twObservations = QtWidgets.QTableWidget(self.tabObservations)
        self.twObservations.setStyleSheet("QTableWidget::item {\n"
"  selection-background-color: rgb(89, 89, 89);\n"
"  selection-color: rgb(242, 242, 242);\n"
"}\n"
"\n"
"QTableWidget::item:selected{\n"
"    selection-background-color: rgb(89, 89, 89);\n"
"    selection-color: rgb(242, 242, 242); \n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"  background-color: rgb(89, 89, 89);\n"
"  color: rgb(242, 242, 242);\n"
"}\n"
"\n"
"QTableWidget QListWidget {\n"
"    background-color: rgb(38, 38, 38);\n"
"    color: rgb(242, 242, 242);\n"
"}")
        self.twObservations.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.twObservations.setDragDropOverwriteMode(False)
        self.twObservations.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.twObservations.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.twObservations.setObjectName("twObservations")
        self.twObservations.setColumnCount(4)
        self.twObservations.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.twObservations.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.twObservations.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.twObservations.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.twObservations.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.twObservations)
        self.pbRemoveObservation = QtWidgets.QPushButton(self.tabObservations)
        self.pbRemoveObservation.setObjectName("pbRemoveObservation")
        self.verticalLayout.addWidget(self.pbRemoveObservation)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.tabProject.addTab(self.tabObservations, "")
        self.verticalLayout_6.addWidget(self.tabProject)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem9)
        self.pbCancel = QtWidgets.QPushButton(dlgProject)
        self.pbCancel.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbCancel.setObjectName("pbCancel")
        self.horizontalLayout_4.addWidget(self.pbCancel)
        self.pbOK = QtWidgets.QPushButton(dlgProject)
        self.pbOK.setStyleSheet("background-color: rgb(13, 13, 13);")
        self.pbOK.setObjectName("pbOK")
        self.horizontalLayout_4.addWidget(self.pbOK)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)

        self.retranslateUi(dlgProject)
        self.tabProject.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(dlgProject)

    def retranslateUi(self, dlgProject):
        _translate = QtCore.QCoreApplication.translate
        dlgProject.setWindowTitle(_translate("dlgProject", "Novo Projeto"))
        self.label.setText(_translate("dlgProject", "Nome Projeto"))
        self.lbProjectFilePath.setText(_translate("dlgProject", "Caminho do arquivo de projeto:"))
        self.label_7.setText(_translate("dlgProject", "Data"))
        self.dteDate.setDisplayFormat(_translate("dlgProject", "dd/MM/yyyy hh:mm:ss"))
        self.label_6.setText(_translate("dlgProject", "Descrição"))
        self.lbTimeFormat.setText(_translate("dlgProject", "Formato da hora:"))
        self.rbSeconds.setText(_translate("dlgProject", "segundos"))
        self.rbHMS.setText(_translate("dlgProject", "hh:mm:ss.mss"))
        self.tabProject.setTabText(self.tabProject.indexOf(self.tabInformation), _translate("dlgProject", "Informação"))
        self.twBehaviors.setSortingEnabled(False)
        item = self.twBehaviors.horizontalHeaderItem(0)
        item.setText(_translate("dlgProject", "Tipo Comportamento"))
        item = self.twBehaviors.horizontalHeaderItem(1)
        item.setText(_translate("dlgProject", "Atalho"))
        item = self.twBehaviors.horizontalHeaderItem(2)
        item.setText(_translate("dlgProject", "Observação"))
        item = self.twBehaviors.horizontalHeaderItem(3)
        item.setText(_translate("dlgProject", "Barreiras"))
        item = self.twBehaviors.horizontalHeaderItem(4)
        item.setText(_translate("dlgProject", "Modificadores"))
        self.pbAddBehavior.setText(_translate("dlgProject", "Adicionar comportamento"))
        self.pbCloneBehavior.setText(_translate("dlgProject", "Copiar comportamento"))
        self.pbRemoveBehavior.setText(_translate("dlgProject", "Remover comportamento"))
        self.pbRemoveAllBehaviors.setText(_translate("dlgProject", "Remova todos\n"
"os comportamentos"))
        self.pbBehaviorsCategories.setText(_translate("dlgProject", "Adicionar novas barreiras"))
        self.pbImportBehaviorsFromProject.setText(_translate("dlgProject", "Importar comportamentos\n"
"de um projeto eMOC"))
        self.pbImportFromTextFile.setText(_translate("dlgProject", "Importar de\n"
"arquivo de texto"))
        self.pbExportEthogram.setText(_translate("dlgProject", "Exportar Etograma"))
        self.lbObservationsState.setText(_translate("dlgProject", "TextLabel"))
        self.tabProject.setTabText(self.tabProject.indexOf(self.tabConfiguration), _translate("dlgProject", "Ethogram"))
        self.twSubjects.setSortingEnabled(True)
        item = self.twSubjects.horizontalHeaderItem(0)
        item.setText(_translate("dlgProject", "Chave"))
        item = self.twSubjects.horizontalHeaderItem(1)
        item.setText(_translate("dlgProject", "Nome sujeito"))
        item = self.twSubjects.horizontalHeaderItem(2)
        item.setText(_translate("dlgProject", "Descrição"))
        self.pbAddSubject.setText(_translate("dlgProject", "Adicionar sujeito"))
        self.pbRemoveSubject.setText(_translate("dlgProject", "Remover sujeito"))
        self.pbImportSubjectsFromProject.setText(_translate("dlgProject", "Importar sujetos\n"
"de um projeto eMOC"))
        self.lbSubjectsState.setText(_translate("dlgProject", "TextLabel"))
        self.tabProject.setTabText(self.tabProject.indexOf(self.tabSubjects), _translate("dlgProject", "Sujeitos"))
        self.twVariables.setSortingEnabled(True)
        item = self.twVariables.horizontalHeaderItem(0)
        item.setText(_translate("dlgProject", "Rótulo"))
        item = self.twVariables.horizontalHeaderItem(1)
        item.setText(_translate("dlgProject", "Descrição"))
        item = self.twVariables.horizontalHeaderItem(2)
        item.setText(_translate("dlgProject", "Tipo"))
        item = self.twVariables.horizontalHeaderItem(3)
        item.setText(_translate("dlgProject", "Valor predefinido"))
        item = self.twVariables.horizontalHeaderItem(4)
        item.setText(_translate("dlgProject", "Conjunto de valores"))
        self.label_2.setText(_translate("dlgProject", "Rótulo"))
        self.label_3.setText(_translate("dlgProject", "Descrição"))
        self.label_8.setText(_translate("dlgProject", "Tipo"))
        self.label_4.setText(_translate("dlgProject", "Valor predefinido"))
        self.label_9.setText(_translate("dlgProject", "Data predefinida"))
        self.dte_default_date.setDisplayFormat(_translate("dlgProject", "dd/mm/yyyy hh:mm"))
        self.label_5.setText(_translate("dlgProject", "Conjunto de valores (separados por vírgula)"))
        self.pbAddVariable.setText(_translate("dlgProject", "Adicionar variável"))
        self.pbRemoveVariable.setText(_translate("dlgProject", "Remover variável"))
        self.pbImportVarFromProject.setText(_translate("dlgProject", "Importar variavéis\n"
"de um projeto eMOC"))
        self.tabProject.setTabText(self.tabProject.indexOf(self.tabIndependentVariables), _translate("dlgProject", "Variáveis independentes "))
        item = self.twObservations.horizontalHeaderItem(0)
        item.setText(_translate("dlgProject", "id"))
        item = self.twObservations.horizontalHeaderItem(1)
        item.setText(_translate("dlgProject", "Data"))
        item = self.twObservations.horizontalHeaderItem(2)
        item.setText(_translate("dlgProject", "Descrição"))
        item = self.twObservations.horizontalHeaderItem(3)
        item.setText(_translate("dlgProject", "Mídia"))
        self.pbRemoveObservation.setText(_translate("dlgProject", "Remover observações selecionadas"))
        self.tabProject.setTabText(self.tabProject.indexOf(self.tabObservations), _translate("dlgProject", "Observações"))
        self.pbCancel.setText(_translate("dlgProject", "Cancelar"))
        self.pbOK.setText(_translate("dlgProject", "OK"))

