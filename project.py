#!/usr/bin/env python3

"""
BORIS
Behavioral Observation Research Interactive Software
Copyright 2012-2018 Olivier Friard

This file is part of BORIS.

  BORIS is free software; you can redistribute it and/or modify
  it under the terms of the GNU General Public License as published by
  the Free Software Foundation; either version 3 of the License, or
  any later version.

  BORIS is distributed in the hope that it will be useful,
  but WITHOUT ANY WARRANTY; without even the implied warranty of
  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  GNU General Public License for more details.

  You should have received a copy of the GNU General Public License
  along with this program; if not see <http://www.gnu.org/licenses/>.

"""


try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *

import logging
import json
import sys
import tablib
import copy
import urllib.parse
import urllib.request
import urllib.error
import pathlib


from utilities import sorted_keys
from config import *
import add_modifier
import dialog
import export_observation


if QT_VERSION_STR[0] == "4":
    from project_ui import Ui_dlgProject
else:
    from project_ui5 import Ui_dlgProject

class BehavioralCategories(QDialog):

    def __init__(self, pj):
        super(BehavioralCategories, self).__init__()

        self.pj = pj
        self.setWindowTitle("Categorias comportamentais")

        self.vbox = QVBoxLayout(self)

        self.label = QLabel()
        self.label.setText("Categorias comportamentais")
        self.vbox.addWidget(self.label)

        self.lw = QListWidget()

        if BEHAVIORAL_CATEGORIES in pj:
            for category in pj[BEHAVIORAL_CATEGORIES]:
                self.lw.addItem(QListWidgetItem(category))

        self.vbox.addWidget(self.lw)

        self.hbox0 = QHBoxLayout(self)
        self.pbAddCategory = QPushButton("Adicionar categoria Add category")
        self.pbAddCategory.clicked.connect(self.pbAddCategory_clicked)
        self.pbRemoveCategory = QPushButton("Remover categoria")
        self.pbRemoveCategory.clicked.connect(self.pbRemoveCategory_clicked)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.hbox0.addItem(spacerItem)
        self.hbox0.addWidget(self.pbRemoveCategory)
        self.hbox0.addWidget(self.pbAddCategory)
        self.vbox.addLayout(self.hbox0)

        hbox1 = QHBoxLayout(self)
        self.pbOK = QPushButton("OK")
        self.pbOK.clicked.connect(self.accept)
        self.pbCancel = QPushButton("Cancelar")
        self.pbCancel.clicked.connect(self.reject)
        spacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hbox1.addItem(spacerItem)
        hbox1.addWidget(self.pbCancel)
        hbox1.addWidget(self.pbOK)
        self.vbox.addLayout(hbox1)

        self.setLayout(self.vbox)

    def pbAddCategory_clicked(self):
        category, ok = QInputDialog.getText(self, "Nova categoria comportamental", "Nome categoria:")
        if ok:
            self.lw.addItem(QListWidgetItem(category))

    def pbRemoveCategory_clicked(self):
        for SelectedItem in self.lw.selectedItems():

            # check if behavioral category is in use
            category_to_remove = self.lw.item(self.lw.row(SelectedItem)).text().strip()
            behaviors_in_category = []
            for idx in self.pj[ETHOGRAM]:
                if BEHAVIOR_CATEGORY in self.pj[ETHOGRAM][idx] and self.pj[ETHOGRAM][idx][BEHAVIOR_CATEGORY] == category_to_remove:
                    behaviors_in_category.append(self.pj[ETHOGRAM][idx][BEHAVIOR_CODE])

            if behaviors_in_category:
                if dialog.MessageDialog(programName, ("Algum comportamento pertence ao <b>{1}</b>:<br>"
                                                      "{0}<br>"
                                                      "<br>Algumas funcionalidades podem não estar mais disponíveis.<br>"
                                                      "Você tem certeza de remover essa categoria comportamental?").format("<br>".join(behaviors_in_category),
                                                                                                                  category_to_remove),
                                        [YES, CANCEL]) == YES:

                    self.lw.takeItem(self.lw.row(SelectedItem))
            else:
                self.lw.takeItem(self.lw.row(SelectedItem))

class projectDialog(QDialog, Ui_dlgProject):

    def __init__(self, log_level="", parent=None):

        super(projectDialog, self).__init__(parent)
        if log_level:
            logging.basicConfig(level=log_level)

        self.setupUi(self)

        self.lbObservationsState.setText("")
        self.lbSubjectsState.setText("")

        # ethogram tab
        self.pbAddBehavior.clicked.connect(self.pbAddBehavior_clicked)
        self.pbCloneBehavior.clicked.connect(self.pb_clone_behavior_clicked)

        self.pbRemoveBehavior.clicked.connect(self.pbRemoveBehavior_clicked)
        self.pbRemoveAllBehaviors.clicked.connect(self.pbRemoveAllBehaviors_clicked)

        self.pbBehaviorsCategories.clicked.connect(self.pbBehaviorsCategories_clicked)

        self.pbImportBehaviorsFromProject.clicked.connect(self.pbImportBehaviorsFromProject_clicked)

        self.pbImportFromTextFile.clicked.connect(self.pbImportFromTextFile_clicked)

        self.pbExportEthogram.clicked.connect(self.export_ethogram)

        self.twBehaviors.cellChanged[int, int].connect(self.twBehaviors_cellChanged)
        self.twBehaviors.cellDoubleClicked[int, int].connect(self.twBehaviors_cellDoubleClicked)

        # left align table header
        for i in range(self.twBehaviors.columnCount()):
            self.twBehaviors.horizontalHeaderItem(i).setTextAlignment(Qt.AlignLeft)

        # subjects
        self.pbAddSubject.clicked.connect(self.pbAddSubject_clicked)
        self.pbRemoveSubject.clicked.connect(self.pbRemoveSubject_clicked)
        self.twSubjects.cellChanged[int, int].connect(self.twSubjects_cellChanged)

        self.pbImportSubjectsFromProject.clicked.connect(self.pbImportSubjectsFromProject_clicked)

        # independent variables tab
        self.pbAddVariable.clicked.connect(self.pbAddVariable_clicked)
        self.pbRemoveVariable.clicked.connect(self.pbRemoveVariable_clicked)

        self.leLabel.textChanged.connect(self.leLabel_changed)
        self.leDescription.textChanged.connect(self.leDescription_changed)
        self.lePredefined.textChanged.connect(self.lePredefined_changed)
        self.leSetValues.textChanged.connect(self.leSetValues_changed)
        self.dte_default_date.dateTimeChanged.connect(self.dte_default_date_changed)

        self.twVariables.cellClicked[int, int].connect(self.twVariables_cellClicked)

        self.cbType.currentIndexChanged.connect(self.cbtype_changed)
        self.cbType.activated.connect(self.cbtype_activated)
        '''self.cbType.highlighted.connect(self.cbtype_changed)'''

        self.pbImportVarFromProject.clicked.connect(self.pbImportVarFromProject_clicked)

        # observations tab
        self.pbRemoveObservation.clicked.connect(self.pbRemoveObservation_clicked)

        self.pbOK.clicked.connect(self.pbOK_clicked)
        self.pbCancel.clicked.connect(self.pbCancel_clicked)

        self.selected_twvariables_row = -1
        
        self.row_in_modification = -1
        self.flag_modified = False

    # def add_behaviors_coding_map(self):
    #     """
    #     Add a behaviors coding map from file
    #     """
    #
    #     fn = QFileDialog(self).getOpenFileName(self, "Abra um mapa de codificação de comportamentos", "", "Mapa de codificação de comportamentos (*.behav_coding_map);;Todos arquivos (*)")
    #     fileName = fn[0] if type(fn) is tuple else fn
    #     if fileName:
    #         try:
    #             bcm = json.loads(open(fileName, "r").read())
    #         except:
    #             QMessageBox.critical(self, programName, "O arquivo {} não parece um mapa de codificação de comportamentos ...".format(fileName))
    #             return
    #
    #         if "coding_map_type" not in bcm or bcm["coding_map_type"] != "BORIS behaviors coding map":
    #             QMessageBox.critical(self, programName, "O arquivo {} não parece um mapa de códigos de comportamento da BORIS ...".format(fileName))
    #
    #         if BEHAVIORS_CODING_MAP not in self.pj:
    #             self.pj[BEHAVIORS_CODING_MAP] = []
    #
    #         bcm_code_not_found = []
    #         existing_codes = [self.pj[ETHOGRAM][key]["code"] for key in self.pj[ETHOGRAM]]
    #         for code in [bcm["areas"][key]["code"] for key in bcm["areas"]]:
    #             if code not in existing_codes:
    #                 bcm_code_not_found.append(code)
    #
    #         if bcm_code_not_found:
    #             QMessageBox.warning(self, programName, ("O seguinte comportamento {} não está definido no etograma:<br>"
    #                                                     "{}").format("s" if len(bcm_code_not_found)>1 else "", ",".join(bcm_code_not_found)))
    #
    #         self.pj[BEHAVIORS_CODING_MAP].append(copy.deepcopy(bcm))
    #
    #         self.twBehavCodingMap.setRowCount(self.twBehavCodingMap.rowCount() + 1)
    #
    #         self.twBehavCodingMap.setItem(self.twBehavCodingMap.rowCount() - 1, 0, QTableWidgetItem(bcm["name"]))
    #         codes = ", ".join([bcm["areas"][idx]["code"] for idx in bcm["areas"]])
    #         self.twBehavCodingMap.setItem(self.twBehavCodingMap.rowCount() - 1, 1, QTableWidgetItem(codes))

    # def remove_behaviors_coding_map(self):
    #     """
    #     remove the first selected behaviors coding map
    #     """
    #     if not self.twBehavCodingMap.selectedIndexes():
    #         QMessageBox.warning(self, programName, "Selecione um mapa de codificação de comportamentos")
    #     else:
    #         if dialog.MessageDialog(programName, "Remover o mapa de codificação de comportamentos selecionados?", [YES, CANCEL]) == YES:
    #             del self.pj[BEHAVIORS_CODING_MAP][self.twBehavCodingMap.selectedIndexes()[0].row()]
    #             self.twBehavCodingMap.removeRow(self.twBehavCodingMap.selectedIndexes()[0].row())

    def export_ethogram(self):
        """
        export ethogram in various format
        """
        extended_file_formats = ["Tab Separated Values (*.tsv)",
                       "Comma Separated Values (*.csv)",
                       "Open Document Spreadsheet ODS (*.ods)",
                       "Microsoft Excel Spreadsheet XLSX (*.xlsx)",
                       "Legacy Microsoft Excel Spreadsheet XLS (*.xls)",
                       "HTML (*.html)"]
        file_formats = ["tsv", "csv", "ods", "xlsx", "xls", "html"]

        if QT_VERSION_STR[0] == "4":
            filediag_func = QFileDialog(self).getSaveFileNameAndFilter
        else:
            filediag_func = QFileDialog(self).getSaveFileName

        fileName, filter_ = filediag_func(self, "Export ethogram", "", ";;".join(extended_file_formats))
        if not fileName:
            return

        outputFormat = file_formats[extended_file_formats.index(filter_)]
        if pathlib.Path(fileName).suffix != "." + outputFormat:
            fileName = str(pathlib.Path(fileName)) + "." + outputFormat

        '''
        outputFormat = ""
        availableFormats = ("tsv", "csv", "xls", "ods", "html")
        for fileExtension in availableFormats:
            if fileExtension in filter_:
                outputFormat = fileExtension
                if not fileName.upper().endswith("." + fileExtension.upper()):
                    fileName += "." + fileExtension

        if not outputFormat:
            QMessageBox.warning(self, programName, "Choose a file format", QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
        else:
            break
        '''

        ethogram_data = tablib.Dataset()
        ethogram_data.title = "Etograma"
        if self.leProjectName.text():
            ethogram_data.title = "Etograma do projeto {}".format(self.leProjectName.text())

        ethogram_data.headers = ["Behavior code", "Behavior type", "Description", "Key", "Behavioral category", "Excluded behaviors"]

        for r in range(self.twBehaviors.rowCount()):
            row = []
            for field in [TYPE, "description", "key", "category"]:
                row.append(self.twBehaviors.item(r, behavioursFields[field]).text())
            ethogram_data.append(row)

        ok, msg = export_observation.dataset_write(ethogram_data, fileName, outputFormat)
        if not ok:
            QMessageBox.critical(None, programName, msg, QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)

    def leLabel_changed(self):
        if self.selected_twvariables_row != -1:
            self.twVariables.item(self.selected_twvariables_row, 0).setText(self.leLabel.text())

    def leDescription_changed(self):
        if self.selected_twvariables_row != -1:
            self.twVariables.item(self.selected_twvariables_row, 1).setText(self.leDescription.text())

    def lePredefined_changed(self):
        if self.selected_twvariables_row != -1:
            self.twVariables.item(self.selected_twvariables_row, 3).setText(self.lePredefined.text())
            if not self.lePredefined.hasFocus():
                r, msg = self.check_indep_var_config()
                if not r:
                    QMessageBox.warning(self, programName + " - Erro de variáveis independentes", msg)

    def leSetValues_changed(self):
        if self.selected_twvariables_row != -1:
            self.twVariables.item(self.selected_twvariables_row, 4).setText(self.leSetValues.text())

    def dte_default_date_changed(self):
        if self.selected_twvariables_row != -1:
            self.twVariables.item(self.selected_twvariables_row, 3).setText(self.dte_default_date.dateTime().toString(Qt.ISODate))

    def pbBehaviorsCategories_clicked(self):
        """
        gerenciador de categorias comportamentais
        """

        bc = BehavioralCategories(self.pj)

        if bc.exec_():
            self.pj[BEHAVIORAL_CATEGORIES] = []
            for index in range(bc.lw.count()):
                new_category = bc.lw.item(index).text().strip()
                self.pj[BEHAVIORAL_CATEGORIES].append(new_category)

    def twBehaviors_cellDoubleClicked(self, row, column):
        """
        manage double-click on ethogram table:
        * behavior category
        * modifiers
        * exclusion
        * modifiers coding map

        Args:
            row (int): row double-clicked
            column (int): column double-clicked

        """

        # check if double click on excluded column
        # if column == behavioursFields["excluded"]:
        #     self.pbExclusionMatrix_clicked()
        #     #QMessageBox.information(self, programName, "Use the 'Exclusion matrix' button to manage excluded behaviors")

        # check if double click on 'coding map' column
        # if column == behavioursFields["coding map"]:
        #
        #     if "with coding map" in self.twBehaviors.item(row, behavioursFields[TYPE]).text():
        #         self.behaviorTypeChanged(row)
        #     else:
        #         QMessageBox.information(self, programName, "Altere o tipo de comportamento na primeira coluna para selecionar um mapa de codificação")
            

        # check if double click on category
        if column == behavioursFields["type"]:
            self.behavior_type_doubleclicked(row)
        
        
        if column == behavioursFields["category"]:
            self.category_doubleclicked(row)

        if column == behavioursFields["modifiers"]:
            type = self.twBehaviors.item(row, behavioursFields[TYPE]).text()
            category = self.twBehaviors.item(row, behavioursFields["category"]).text()

            addModifierWindow = add_modifier.addModifierDialog(self.twBehaviors.item(row, column).text(), type, category)
            addModifierWindow.setWindowTitle("""Definir modificadores para o comportamento "{}""".format(self.twBehaviors.item(row, 2).text()))
            if addModifierWindow.exec_():
                self.twBehaviors.item(row, column).setText(addModifierWindow.getModifiers())

    def behavior_type_doubleclicked(self, row):
        """
        select type for behavior
        """

        if self.twBehaviors.item(row, behavioursFields[TYPE]).text() in BEHAVIOR_TYPES:
            selected = BEHAVIOR_TYPES.index(self.twBehaviors.item(row, behavioursFields[TYPE]).text())
        else:
            selected = 0

        new_type, ok = QInputDialog.getItem(self, "Selecione um tipo de comportamento", "Tipos de comportamento", BEHAVIOR_TYPES, selected, False)

        if ok and new_type:
            self.twBehaviors.item(row, behavioursFields["type"]).setText(new_type)

    def category_doubleclicked(self, row):
        """
        select category for behavior
        """
        type_index = self.twBehaviors.item(row, behavioursFields[TYPE]).text()

        if self.twBehaviors.item(row, behavioursFields["category"]).text() in BEHAVIOR_BARRIERS[type_index]:
            selected = BEHAVIOR_BARRIERS[type_index].index(self.twBehaviors.item(row, behavioursFields["category"]).text())
        else:
            selected = 0

        category_type = BEHAVIOR_BARRIERS[type_index]
        category_type.extend(self.pj[BEHAVIORAL_CATEGORIES])
        category, ok = QInputDialog.getItem(self, "Selecione uma categoria comportamental", "Categorias comportamentais", category_type, selected, False)

        if ok and category:
            if category == "Nenhuma Barreira":
                category = ""
            self.twBehaviors.item(row, behavioursFields["category"]).setText(category)

    def check_variable_default_value(self, txt, varType):
        """
        check if variable default value is compatible with variable type
        """
        # check for numeric type
        if varType == NUMERIC:
            try:
                if txt:
                    float(txt)
                return True
            except:
                return False

        return True


    def variableTypeChanged(self, row):
        """
        variable type combobox changed
        """

        if self.twVariables.cellWidget(row, tw_indVarFields.index("type")).currentText() == SET_OF_VALUES:
            if self.twVariables.item(row, tw_indVarFields.index("possible values")).text() == "NA":
                self.twVariables.item(row, tw_indVarFields.index("possible values")).setText("Clique duas vezes para adicionar valores")
                #self.twVariables.item(row, tw_indVarFields.index("possible values")).setBackground(Qt.red)
        else:
            # check if set of values defined
            if self.twVariables.item(row, tw_indVarFields.index("possible values")).text() not in ["NA","Clique duas vezes para adicionar valores"]:
                if dialog.MessageDialog(programName, "Erase the set of values?", [YES, CANCEL]) == CANCEL:
                    self.twVariables.cellWidget(row, tw_indVarFields.index("type")).setCurrentIndex(SET_OF_VALUES_idx)
                    return
                else:
                    self.twVariables.item(row, tw_indVarFields.index("possible values")).setText("NA")
            else:
                self.twVariables.item(row, tw_indVarFields.index("possible values")).setText("NA")

            if self.twVariables.cellWidget(row, tw_indVarFields.index("type")).currentText() == TIMESTAMP:
                self.twVariables.item(row, tw_indVarFields.index("default value")).setFlags(Qt.ItemIsEnabled)
            else:
                self.twVariables.item(row, tw_indVarFields.index("default value")).setFlags(Qt.ItemIsSelectable | Qt.ItemIsEditable | Qt.ItemIsEnabled)


            # check compatibility between variable type and default value
            if not self.check_variable_default_value(self.twVariables.item(row, tw_indVarFields.index("default value")).text(),
                                                   self.twVariables.cellWidget(row, tw_indVarFields.index("type")).currentIndex()):
                QMessageBox.warning(self, programName + " - Erro de variáveis independentes", "O valor padrão ({0}) da variável <b>{1}</b> não é compatível com o tipo de variável".format(
                                    self.twVariables.item(row, tw_indVarFields.index("default value")).text(),
                                    self.twVariables.item(row, tw_indVarFields.index("label")).text()))

    def check_indep_var_config(self):
        """
        check if default type is compatible with var type
        """

        existing_var = []
        for r in range(self.twVariables.rowCount()):

            if self.twVariables.item(r, 0).text().strip().upper() in existing_var:
                return False, "Linha: {} - O rótulo da variável <b>{}</b> já está em uso." .format(r + 1, self.twVariables.item(r, 0).text())

            # check if same lables
            existing_var.append(self.twVariables.item(r, 0).text().strip().upper())

            # check default value
            if self.twVariables.item(r, 2).text() != TIMESTAMP and not self.check_variable_default_value(self.twVariables.item(r, 3).text(), self.twVariables.item(r, 2).text()):
                return False, "Linha: {} - O valor padrão ({}) não é compatível com otipo de variável ({})".format(r + 1, self.twVariables.item(r, 3).text(), self.twVariables.item(r, 2).text())

            # check if default value in set of values
            if self.twVariables.item(r, 2).text() == SET_OF_VALUES and self.twVariables.item(r, 4).text() == "":
                return False, "Nenhum valor foi definido no conjunto."

            if (self.twVariables.item(r, 2).text() == SET_OF_VALUES
                and self.twVariables.item(r, 4).text()
                and self.twVariables.item(r, 3).text()
                and self.twVariables.item(r, 3).text() not in self.twVariables.item(r, 4).text().split(",")):
                return False, "O valor padrão ({}) não está contindo no conjunto de valores".format(self.twVariables.item(r, 3).text())


        return True, "OK"

    def cbtype_changed(self):

        self.leSetValues.setVisible(self.cbType.currentText() == SET_OF_VALUES)
        self.label_5.setVisible(self.cbType.currentText() == SET_OF_VALUES)

        self.dte_default_date.setVisible(self.cbType.currentText() == TIMESTAMP)
        self.label_9.setVisible(self.cbType.currentText() == TIMESTAMP)
        self.lePredefined.setVisible(self.cbType.currentText() != TIMESTAMP)
        self.label_4.setVisible(self.cbType.currentText() != TIMESTAMP)

    def cbtype_activated(self):

        if self.cbType.currentText() == TIMESTAMP:
            self.twVariables.item(self.selected_twvariables_row, 3).setText(self.dte_default_date.dateTime().toString(Qt.ISODate))
            self.twVariables.item(self.selected_twvariables_row, 4).setText("")
        else:
            self.twVariables.item(self.selected_twvariables_row, 3).setText(self.lePredefined.text())
            self.twVariables.item(self.selected_twvariables_row, 4).setText("")

        # remove spaces after and before comma
        if self.cbType.currentText() == SET_OF_VALUES:
            self.twVariables.item(self.selected_twvariables_row, 4).setText( ",".join([x.strip() for x in  self.leSetValues.text().split(",")]))

        self.twVariables.item(self.selected_twvariables_row, 2).setText(self.cbType.currentText())

        r, msg = self.check_indep_var_config()

        if not r:
            QMessageBox.warning(self, programName + " - Erro de variável independente", msg)

    def pbAddVariable_clicked(self):
        """
        add an independent variable
        """
        logging.debug("Adicionar variável independente")

        self.twVariables.setRowCount(self.twVariables.rowCount() + 1)
        self.selected_twvariables_row = self.twVariables.rowCount() - 1

        for idx, field in enumerate(tw_indVarFields):
            if field == "type":
                item = QTableWidgetItem("numeric")
            else:
                item = QTableWidgetItem("")
            self.twVariables.setItem(self.twVariables.rowCount() - 1, idx, item)

        self.twVariables.setCurrentCell(self.twVariables.rowCount() - 1, 0)

        self.twVariables_cellClicked(self.twVariables.rowCount() - 1, 0)

    def pbRemoveVariable_clicked(self):
        """
        remove the selected independent variable
        """
        logging.debug("remover seleção variável independente")

        if not self.twVariables.selectedIndexes():
            QMessageBox.warning(self, programName, "Selecione uma variável para remover")
        else:
            if dialog.MessageDialog(programName, "Remover variável selecionada?", [YES, CANCEL]) == YES:
                self.twVariables.removeRow(self.twVariables.selectedIndexes()[0].row())

        if self.twVariables.selectedIndexes():
            self.twVariables_cellClicked(self.twVariables.selectedIndexes()[0].row(), 0)
        else:
            self.twVariables_cellClicked(-1, 0)

    def pbImportVarFromProject_clicked(self):
        """
        import independent variables from another project
        """

        fn = QFileDialog(self).getOpenFileName(self, "Importar variáveis independentes do projeto", "",
                                               "Projeto (*.boris);;All files (*)")
        fileName = fn[0] if type(fn) is tuple else fn

        if fileName:
            with open(fileName, "r") as infile:
                s = infile.read()
            try:
                project = json.loads(s)
            except:
                QMessageBox.warning(None, programName, "Erro ao ler variáveis independentes do arquivo selecionado",
                                    QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
                return

            # independent variables
            if project[INDEPENDENT_VARIABLES]:

                # check if variables are already present
                existing_var = []

                for r in range(self.twVariables.rowCount()):
                    existing_var.append(self.twVariables.item(r, 0).text().strip().upper())  # = [self.pj[INDEPENDENT_VARIABLES][k]["label"].upper().strip() for k in self.pj[INDEPENDENT_VARIABLES]]

                for i in sorted_keys(project[INDEPENDENT_VARIABLES]):

                    self.twVariables.setRowCount(self.twVariables.rowCount() + 1)
                    flag_renamed = False
                    for idx, field in enumerate(tw_indVarFields):
                        item = QTableWidgetItem()
                        if field in project[INDEPENDENT_VARIABLES][i]:
                            if field == "label":
                                txt = project[INDEPENDENT_VARIABLES][i]["label"].strip()
                                while txt.upper() in existing_var:
                                    txt += "_2"
                                    flag_renamed = True
                            else:
                                txt = project[INDEPENDENT_VARIABLES][i][field].strip()
                            item.setText(txt)
                        else:
                            item.setText("")
                        self.twVariables.setItem(self.twVariables.rowCount() - 1, idx, item)

                self.twVariables.resizeColumnsToContents()
                if flag_renamed:
                    QMessageBox.information(self, programName, "Algumas variáveis já presentes foram renomeadas")

            else:
                QMessageBox.warning(self, programName, "Nenhuma variável independente encontrada no projeto")

    def pbImportSubjectsFromProject_clicked(self):
        """
        import subjects from another project
        """
        if QT_VERSION_STR[0] == "4":
            fileName = QFileDialog(self).getOpenFileName(self, "Importar sujeitos do projeto", "", "Projeto (*.boris);;All files (*)")
        else:
            fileName, _ = QFileDialog(self).getOpenFileName(self, "Importar sujeitos do projeto", "", "Projeto (*.boris);;All files (*)")

        if fileName:

            with open(fileName, "r") as infile:
                s = infile.read()

            try:
                project = json.loads(s)
            except:
                QMessageBox.warning(None, programName, "Erro ao ler sujeitos do arquivo selecionado",
                                    QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
                return

            # configuration of behaviours
            if project[SUBJECTS]:

                if self.twSubjects.rowCount():

                    response = dialog.MessageDialog(programName, ("Existem sujeitos já configurados. "
                                                                  "Você deseja anexar sujeitos ou substituí-los?"),
                                                                  ['Append', 'Replace', 'Cancel'])

                    if response == 'Replace':
                        self.twSubjects.setRowCount(0)

                    if response == CANCEL:
                        return

                for idx in sorted(project[SUBJECTS].keys()):

                    self.twSubjects.setRowCount(self.twSubjects.rowCount() + 1)

                    for idx2, sbjField in enumerate(subjectsFields):

                        if sbjField in project[SUBJECTS][idx]:
                            self.twSubjects.setItem(self.twSubjects.rowCount() - 1, idx2, QTableWidgetItem(project[SUBJECTS][idx][sbjField]))
                        else:
                            self.twSubjects.setItem(self.twSubjects.rowCount() - 1, idx2, QTableWidgetItem(""))

                self.twSubjects.resizeColumnsToContents()
            else:
                QMessageBox.warning(self, programName, "Nenhuma configuração de sujeitos encontrada no projeto")

    def pbImportBehaviorsFromProject_clicked(self):
        """
        import behaviors from another project
        """

        fn =  QFileDialog(self).getOpenFileName(self, "Importar comportamentos do projeto", "", "Projeto (*.boris);;All files (*)")
        fileName = fn[0] if type(fn) is tuple else fn

        if fileName:
            with open(fileName, "r") as infile:
                s = infile.read()
            try:
                project = json.loads(s)
            except:
                QMessageBox.warning(None, programName, "Erro ao ler comportamento do arquivo selecionado",
                                    QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
                return

            # import behavioral_categories
            if BEHAVIORAL_CATEGORIES in project:
                self.pj[BEHAVIORAL_CATEGORIES] = project[BEHAVIORAL_CATEGORIES]

            # configuration of behaviours
            if project[ETHOGRAM]:
                if self.twBehaviors.rowCount():
                    response = dialog.MessageDialog(programName, ("Existem comportamentos ja configurados. "
                                                                  "Você quer acrescentar comportamentos ou substituí-los?"),
                                                    ["Append", "Replace", CANCEL])
                    if response == "Replace":
                        self.twBehaviors.setRowCount(0)
                    if response == CANCEL:
                        return

                for i in sorted_keys(project[ETHOGRAM]):

                    self.twBehaviors.setRowCount(self.twBehaviors.rowCount() + 1)

                    for field in project[ETHOGRAM][i]:

                        item = QTableWidgetItem()

                        if field == TYPE:
                            print(project[ETHOGRAM][i][field])
                            item.setText(project[ETHOGRAM][i][field])
                            item.setFlags(Qt.ItemIsEnabled)
                            item.setBackground(QColor(230, 230, 230))
                            '''
                            comboBox = QComboBox()
                            comboBox.addItems(BEHAVIOR_TYPES)
                            comboBox.setCurrentIndex(BEHAVIOR_TYPES.index( project[ETHOGRAM][i][field] ))
                            self.twBehaviors.setCellWidget(self.twBehaviors.rowCount() - 1, behavioursFields[field], comboBox)
                            '''

                        else:
                            if field == "modifiers" and isinstance(project[ETHOGRAM][i][field], str):
                                modif_set_dict = {}
                                if project[ETHOGRAM][i][field]:
                                    modif_set_list = project[ETHOGRAM][i][field].split("|")
                                    for modif_set in modif_set_list:
                                        modif_set_dict[str(len(modif_set_dict))] = {"name": "", "type": SINGLE_SELECTION,
                                                                                    "values": modif_set.split(",")}
                                project[ETHOGRAM][i][field] = dict(modif_set_dict)

                            item.setText(str(project[ETHOGRAM][i][field]))

                            if field in ["modifiers", "category"]:
                                item.setFlags(Qt.ItemIsEnabled)
                                item.setBackground(QColor(230, 230, 230))

                        self.twBehaviors.setItem(self.twBehaviors.rowCount() - 1, behavioursFields[field], item)

                self.twBehaviors.resizeColumnsToContents()

            else:
                QMessageBox.warning(self, programName, "Nenhuma configuração de comportamento encontrada no projeto")

    def pbRemoveAllBehaviors_clicked(self):

        if self.twBehaviors.rowCount():

            response = dialog.MessageDialog(programName, "Remover todos os comportamentos?", [YES, CANCEL])

            if response == YES:

                # extract all codes to delete
                codesToDelete = []
                row_mem = {}
                for r in range(self.twBehaviors.rowCount()-1, -1, -1):
                    if self.twBehaviors.item(r, 2).text():
                        codesToDelete.append(self.twBehaviors.item(r, 2).text())
                        row_mem[self.twBehaviors.item(r, 2).text()] = r

                # extract all codes used in observations
                codesInObs = []
                for obs in self.pj[OBSERVATIONS]:
                    events = self.pj[OBSERVATIONS][obs]['events']
                    for event in events:
                        codesInObs.append(event[2])

                for codeToDelete in codesToDelete:
                    # if code to delete used in obs ask confirmation
                    if codeToDelete in codesInObs:
                        response = dialog.MessageDialog(programName, "O código <b>{}</b> é usado em observações!".format(codeToDelete), ['Remove', CANCEL])
                        if response == "Remove":
                            self.twBehaviors.removeRow(row_mem[codeToDelete])
                    else:   # remove without asking
                        self.twBehaviors.removeRow(row_mem[codeToDelete])

    def pbImportFromJWatcher_clicked(self):
        """
        import behaviors configuration from JWatcher (GDL file)
        """
        if self.twBehaviors.rowCount():
            response = dialog.MessageDialog(programName, "Existem comportamentos já configurados. Você quer acrescentar comportamentos ou substituí-los?",
                                            ["Append", "Replace", CANCEL])
            if response == CANCEL:
                return

        fn = QFileDialog(self).getOpenFileName(self, "Importar comportamentos do JWatcher", "", "Global Definition File (*.gdf);;All files (*)")
        fileName = fn[0] if type(fn) is tuple else fn

        if fileName:
            if self.twBehaviors.rowCount() and response == "Replace":
                self.twBehaviors.setRowCount(0)

            with open(fileName, "r") as f:
                rows = f.readlines()

            for idx, row in enumerate(rows):
                if row and row[0] == "#":
                    continue

                if "Behavior.name." in row and "=" in row:
                    key, code = row.split('=')
                    key = key.replace("Behavior.name.", "")
                    # read description
                    if idx < len(rows) and "Behavior.description." in rows[idx+1]:
                        description = rows[idx+1].split('=')[-1]

                    behavior = {"key": key, "description": description, "modifiers": "", "category": ""}

                    self.twBehaviors.setRowCount(self.twBehaviors.rowCount() + 1)

                    for field_type in behavioursFields:
                        if field_type == TYPE:
                            item = QTableWidgetItem(DEFAULT_BEHAVIOR_TYPE)
                        else:
                            item = QTableWidgetItem(behavior[field_type])

                        if field_type in [TYPE, "category", "modifiers"]:
                            item.setFlags(Qt.ItemIsEnabled)
                            item.setBackground(QColor(230, 230, 230))

                        self.twBehaviors.setItem(self.twBehaviors.rowCount() - 1, behavioursFields[field_type], item)

    def check_text_file_type(self, rows):
        """
        check text file
        returns separator and number of fields (if unique)
        """
        separators = "\t,;"
        for separator in separators:
            cs = []
            for row in rows:

                cs.append(row.count(separator))
            if len(set(cs)) == 1:
                return separator, cs[0] + 1
        return None, None

    def pbImportFromTextFile_clicked(self):
        """
        import ethogram from text file
        ethogram must be organized like:
        typeOfBehavior separator key separator behaviorCode [separator description]

        """

        if self.twBehaviors.rowCount():
            response = dialog.MessageDialog(programName,
                                            "Existem comportamentos já configurados. Você quer acrescentar comportamentos ou substituí-los?",
                                            ['Append', 'Replace', CANCEL])
            if response == CANCEL:
                return

        fn = QFileDialog(self).getOpenFileName(self, "Importar comportamentos de arquivo texto", "", "Text files (*.txt *.tsv *.csv);;All files (*)")
        fileName = fn[0] if type(fn) is tuple else fn

        if fileName:

            if self.twBehaviors.rowCount() and response == "Replace":
                self.twBehaviors.setRowCount(0)

            with open(fileName, mode="rb") as f:
                rows_b = f.read().splitlines()

            rows = []
            idx = 1
            for row in rows_b:
                try:
                    rows.append(row.decode("utf-8"))
                except:
                    QMessageBox.critical(None, programName, "Erro ao ler o arquivo\nNa linha # {}\n{}\nContém caracteres que não são legíveis.".format(idx,row), QMessageBox.Ok | QMessageBox.Default, QMessageBox.NoButton)
                    return
                idx += 1

            fieldSeparator, fieldsNumber = self.check_text_file_type(rows)

            logging.debug("Separador de campos: {}  Separador de números: {}".format(fieldSeparator, fieldsNumber))

            if fieldSeparator is None:
                QMessageBox.critical(self, programName, "Caractere separador não encontrado! Use arquivo de texto simples e TAB ou virgula como separador de valor")
            else:

                for row in rows:

                    type_, key, code, description = "", "", "", ""

                    if fieldsNumber == 3:  # fields: type, key, code
                        type_, key, code = row.split(fieldSeparator)
                        description = ""
                    if fieldsNumber == 4:  # fields:  type, key, code, description
                        type_, key, code, description = row.split(fieldSeparator)

                    if fieldsNumber > 4:
                        type_, key, code, description = row.split(fieldSeparator)[:4]

                    behavior = {"key": key, "description": description, "modifiers": "", "category": ""}

                    self.twBehaviors.setRowCount(self.twBehaviors.rowCount() + 1)

                    for field_type in behavioursFields:
                        if field_type == TYPE:
                            item = QTableWidgetItem(DEFAULT_BEHAVIOR_TYPE)
                            # add type combobox
                            if POINT in type_.upper():
                                item = QTableWidgetItem("Point event")
                            if STATE in type_.upper():
                                item = QTableWidgetItem("State event")
                        else:
                            item = QTableWidgetItem(behavior[field_type])

                        if field_type in [TYPE, "modifiers", "category"]:
                            item.setFlags(Qt.ItemIsEnabled)
                            item.setBackground(QColor(230, 230, 230))

                        self.twBehaviors.setItem(self.twBehaviors.rowCount() - 1, behavioursFields[field_type], item)

    def twBehaviors_cellChanged(self, row, column):
        """
        verifique o etograma
        """

        keys, codes = [], []
        self.lbObservationsState.setText("")

        for r in range(self.twBehaviors.rowCount()):

            # check key
            if self.twBehaviors.item(r, behavioursFields["key"]):
                # check key length
                if self.twBehaviors.item(r, behavioursFields["key"]).text().upper() not in ["F" + str(i) for i in range(1, 13)] \
                   and len(self.twBehaviors.item(r, behavioursFields["key"]).text()) > 1:
                    self.lbObservationsState.setText("""<font color="red">tamanho chave &gt; 1</font>""")
                    return

                keys.append(self.twBehaviors.item(r, behavioursFields["key"]).text())

                # convert to upper text
                self.twBehaviors.item(r, behavioursFields["key"]).setText(self.twBehaviors.item(r, behavioursFields["key"]).text().upper())

            # check code
            # if self.twBehaviors.item(r, behavioursFields["code"]):
            #     if self.twBehaviors.item(r, behavioursFields["code"]).text() in codes:
            #         self.lbObservationsState.setText("""<font color="red">Código duplicado na linha {} </font>""".format(r + 1))
            #     else:
            #         if self.twBehaviors.item(r, behavioursFields["code"]).text():
            #             codes.append(self.twBehaviors.item(r, behavioursFields["code"]).text())

    def pb_clone_behavior_clicked(self):
        """
        clone the selected configuration
        """
        if not self.twBehaviors.selectedIndexes():
            QMessageBox.about(self, programName, "Primeiro selecione um comportamento")
        else:
            self.twBehaviors.setRowCount(self.twBehaviors.rowCount() + 1)

            row = self.twBehaviors.selectedIndexes()[0].row()
            for field in behavioursFields:
                item = QTableWidgetItem(self.twBehaviors.item(row, behavioursFields[field]))
                self.twBehaviors.setItem(self.twBehaviors.rowCount() - 1, behavioursFields[field], item)
                if field in [TYPE, "category", "modifiers"]:
                    item.setFlags(Qt.ItemIsEnabled)
                    item.setBackground(QColor(230, 230, 230))

    def pbRemoveBehavior_clicked(self):
        """
        remove behavior
        """

        if not self.twBehaviors.selectedIndexes():
            QMessageBox.warning(self, programName, "Selecione um comportamento a ser removido")
        else:
            if dialog.MessageDialog(programName, "Remover o comportamento selecionado?", [YES, CANCEL]) == YES:

                # check if behavior already used in observations
                flag_break = False
                codeToDelete = self.twBehaviors.item(self.twBehaviors.selectedIndexes()[0].row(), 2).text()
                for obs_id in self.pj[OBSERVATIONS]:
                    if codeToDelete in [event[EVENT_BEHAVIOR_FIELD_IDX] for event in self.pj[OBSERVATIONS][obs_id][EVENTS]]:
                        if dialog.MessageDialog(programName, "O código a ser removido é usado em observações!", [REMOVE, CANCEL]) == CANCEL:
                            return
                        break

                self.twBehaviors.removeRow(self.twBehaviors.selectedIndexes()[0].row())
                self.twBehaviors_cellChanged(0, 0)

    def pbAddBehavior_clicked(self):
        """
        adicionar novo comportamento ao etograma
        """

        try:
            # Add behavior to table
            self.twBehaviors.setRowCount(self.twBehaviors.rowCount() + 1)
            for field_type in behavioursFields:
                item = QTableWidgetItem()
                if field_type == TYPE:
                    item.setText(DEFAULT_BEHAVIOR_TYPE)
    
                if field_type in [TYPE, "category", "modifiers"]:
                    item.setFlags(Qt.ItemIsEnabled)
                    item.setBackground(QColor(38, 38, 38))
                self.twBehaviors.setItem(self.twBehaviors.rowCount() - 1, behavioursFields[field_type], item)
        except:
            QMessageBox.critical(self, "eMOC", ("Erro:<br><b>{}</b>").format(sys.exc_info()[1]))

    def pbAddSubject_clicked(self):
        """
        add a subject
        """

        self.twSubjects.setRowCount(self.twSubjects.rowCount() + 1)
        for col in range(0, len(subjectsFields)):
            item = QTableWidgetItem("")
            self.twSubjects.setItem(self.twSubjects.rowCount() - 1, col, item)

    def pbRemoveSubject_clicked(self):
        """
        remove selected subject from subjects list
        control before if subject used in observations
        """
        if not self.twSubjects.selectedIndexes():
            QMessageBox.warning(self, programName, "Primeiro selecione um sujeito para remover")
        else:

            if dialog.MessageDialog(programName, "Remover sujeito selecionado?", [YES, CANCEL]) == YES:

                flagDel = False
                if self.twSubjects.item(self.twSubjects.selectedIndexes()[0].row(), 1):
                    subjectToDelete = self.twSubjects.item(self.twSubjects.selectedIndexes()[0].row(), 1).text()  # 1: subject name

                    subjectsInObs = []
                    for obs in self.pj[OBSERVATIONS]:
                        events = self.pj[OBSERVATIONS][obs]['events']
                        for event in events:
                            subjectsInObs.append(event[1])  # 1: subject name
                    if subjectToDelete in subjectsInObs:
                        if dialog.MessageDialog(programName, "O sujeito a ser removido é usado em observações!", [REMOVE, CANCEL]) == REMOVE:
                            flagDel = True
                    else:
                        # code not used
                        flagDel = True

                else:
                    flagDel = True

                if flagDel:
                    self.twSubjects.removeRow(self.twSubjects.selectedIndexes()[0].row())

                self.twSubjects_cellChanged(0,0)

    def twSubjects_cellChanged(self, row, column):
        """
        check if subject not unique
        """

        subjects, keys = [], []
        self.lbSubjectsState.setText("")

        for r in range(self.twSubjects.rowCount()):

            # check key
            if self.twSubjects.item(r, 0):

                # check key length
                if self.twSubjects.item(r, 0).text().upper() not in ["F" + str(i) for i in range(1, 13)] \
                   and len(self.twSubjects.item(r, 0).text()) > 1:
                    self.lbSubjectsState.setText(("""<font color="red">Erro na chave do sujeito {}!</font>"""
                                                  "A chave é muito longa(as chaves devem ter um caractere)"
                                                  " exceto pelas teclas de função F1, F2..._)").format(self.twSubjects.item(r, 0).text()))
                    return

                if self.twSubjects.item(r, 0).text() in keys:
                    self.lbSubjectsState.setText("""<font color="red">Chave duplicada na linha # {}</font>""".format(r + 1))
                else:
                    if self.twSubjects.item(r, 0).text():
                        keys.append(self.twSubjects.item(r, 0).text())

                # convert to upper text
                self.twSubjects.item(r, 0).setText(self.twSubjects.item(r, 0).text().upper())

            # check subject
            if self.twSubjects.item(r, 1):
                if self.twSubjects.item(r, 1).text() in subjects:
                    self.lbSubjectsState.setText("""<font color="red">Sujeito duplicado na linha # {}</font>""".format(r + 1))
                else:
                    if self.twSubjects.item(r, 1).text():
                        subjects.append(self.twSubjects.item(r, 1).text())

        # check behaviours keys
        '''
        for r in range(0, self.twBehaviors.rowCount()):
            # check key
            if self.twBehaviors.item(r, fields['key']):
                if self.twBehaviors.item(r, fields['key']).text() in keys:
                    self.lbSubjectsState.setText("""<font color="red">Key found in behaviours configuration ({}) at line # {} </font>""".format(self.twBehaviors.item(r, fields['key']).text(), r + 1))
        '''

    def twVariables_cellClicked(self, row, column):
        """
        check if variable default values are compatible with variable type
        """

        self.selected_twvariables_row = row
        logging.debug("selected row: {}".format(self.selected_twvariables_row))

        if self.selected_twvariables_row == -1:
            for widget in [self.leLabel, self.leDescription, self.cbType, self.lePredefined, self.dte_default_date, self.leSetValues]:
                widget.setEnabled(False)
                self.leLabel.setText("")
                self.leDescription.setText("")
                self.lePredefined.setText("")
                self.leSetValues.setText("")
        
                self.cbType.clear()
            return
            


        # enable widget for indep var setting
        for widget in [self.leLabel, self.leDescription, self.cbType, self.lePredefined, self.dte_default_date, self.leSetValues]:
            widget.setEnabled(True)

        self.leLabel.setText(self.twVariables.item(row, 0).text())
        self.leDescription.setText(self.twVariables.item(row, 1).text())
        self.lePredefined.setText(self.twVariables.item(row, 3).text())
        self.leSetValues.setText(self.twVariables.item(row, 4).text())

        self.cbType.clear()
        self.cbType.addItems(AVAILABLE_INDEP_VAR_TYPES)
        self.cbType.setCurrentIndex(NUMERIC_idx)

        self.cbType.setCurrentIndex(AVAILABLE_INDEP_VAR_TYPES.index(self.twVariables.item(row, 2).text()))

    def pbRemoveObservation_clicked(self):
        """
        remove all selected observations
        """

        if not self.twObservations.selectedIndexes():
            QMessageBox.warning(self, programName, "Nenhuma observação selecionada")
        else:
            response = dialog.MessageDialog(programName, "Tem certeza que deseja remover todas as observações selecionadas?", [YES, CANCEL])
            if response == YES:
                rows_to_delete = []
                for index in self.twObservations.selectedIndexes():
                    rows_to_delete.append(index.row())
                    obs_id = self.twObservations.item(index.row(), 0).text()
                    if obs_id in self.pj[OBSERVATIONS]:
                        del self.pj[OBSERVATIONS][obs_id]

                for row in sorted(set(rows_to_delete), reverse=True):
                    self.twObservations.removeRow(row)

    def pbCancel_clicked(self):
        if self.flag_modified:
            if dialog.MessageDialog("eMOC", "Os conversores foram modificados. Você tem certeza de cancelar?", [CANCEL, OK]) == OK:
                self.reject()
        else:
            self.reject()

    def pbOK_clicked(self):
        """
        verify project configuration
        """

        if self.lbObservationsState.text():
            QMessageBox.warning(self, programName, self.lbObservationsState.text())
            return

        if self.lbSubjectsState.text():
            QMessageBox.warning(self, programName, self.lbSubjectsState.text())
            return

        self.pj["project_name"] = self.leProjectName.text()
        self.pj["project_date"] = self.dteDate.dateTime().toString(Qt.ISODate)
        self.pj["project_description"] = self.teDescription.toPlainText()

        # time format
        if self.rbSeconds.isChecked():
            self.pj["time_format"] = S
        if self.rbHMS.isChecked():
            self.pj["time_format"] = HHMMSS

        # store subjects
        self.subjects_conf = {}

        # check for leading/trailing spaces in subjects names
        subjects_name_with_leading_trailing_spaces = ""
        for row in range(0, self.twSubjects.rowCount()):
            if self.twSubjects.item(row, 1):
                if self.twSubjects.item(row, 1).text() != self.twSubjects.item(row, 1).text().strip():
                    subjects_name_with_leading_trailing_spaces += '"{}" '.format(self.twSubjects.item(row, 1).text())

        remove_leading_trailing_spaces = NO
        if subjects_name_with_leading_trailing_spaces:
            remove_leading_trailing_spaces = dialog.MessageDialog(programName,
                                            ("Atenção! Alguns espaços à esquerda e/ou à direita estão presentes nos seguintes <b>sujeito(s)</b>:<br>"
                                            "<b>{}</b><br><br>"
                                            "Você deseja remover os espaços à esquerda e à direita?<br><br>"
                                            """<font color="red"><b>Tenha cuidado com está opção"""
                                            """ Se você já fez observações!</b></font>""").format(subjects_name_with_leading_trailing_spaces),
                                            [YES, NO])

        for row in range(0, self.twSubjects.rowCount()):
            # check key
            if self.twSubjects.item(row, 0):
                key = self.twSubjects.item(row, 0).text()
            else:
                key = ""

            # check subject name
            if self.twSubjects.item(row, 1):
                if remove_leading_trailing_spaces == YES:
                    subjectName = self.twSubjects.item(row, 1).text().strip()
                else:
                    subjectName = self.twSubjects.item(row, 1).text()

                # check if subject name is empty
                if subjectName == "":
                    QMessageBox.warning(self, programName, "O nome do sujeito não pode está vazio (verifique a linha #{}).".format(row + 1))
                    return

                if "|" in subjectName:
                    QMessageBox.warning(self, programName, "O caractere pipe (|) não é permitido no nome do sujeito <b>{}</b>".format(subjectName))
                    return
            else:
                QMessageBox.warning(self, programName, "Nome do sujeito ausente na configuração dos sujeitos na linha {}".format(row + 1))
                return

            # description
            subjectDescription = ""
            if self.twSubjects.item(row, 2):
                subjectDescription = self.twSubjects.item(row, 2).text().strip()

            self.subjects_conf[str(len(self.subjects_conf))] = {"key": key, "name": subjectName, "description": subjectDescription}

        self.pj[SUBJECTS] = dict(self.subjects_conf)

        # store behaviors
        missing_data = []
        self.obs = {}

        for r in range(self.twBehaviors.rowCount()):
            row = {}
            for field in behavioursFields:
                if self.twBehaviors.item(r, behavioursFields[field]):

                    if remove_leading_trailing_spaces == YES:
                        row[field] = self.twBehaviors.item(r, behavioursFields[field]).text().strip()
                    else:
                        row[field] = self.twBehaviors.item(r, behavioursFields[field]).text()

                    if field == "modifiers" and row["modifiers"]:
                        row["modifiers"] = eval(row["modifiers"])
                else:
                    row[field] = ""

            if (row["type"]) and (row["key"]):
                self.obs[str(len(self.obs))] = row
            else:
                missing_data.append(str(r + 1))

        if missing_data:
            QMessageBox.warning(self, programName, "Dados ausentes no etograma na linha {} !".format(",".join(missing_data)))
            return

        self.pj[ETHOGRAM] = dict(self.obs)

        # independent variables
        r, msg = self.check_indep_var_config()
        if not r:
            QMessageBox.warning(self, programName + " - Erro de variáveis independentes", msg)
            return

        self.indVar = {}
        for r in range(self.twVariables.rowCount()):
            row = {}
            for idx, field in enumerate(tw_indVarFields):
                if self.twVariables.item(r, idx):
                    # check if label is empty
                    if field == "label" and self.twVariables.item(r, idx).text() == "":
                        QMessageBox.warning(self, programName, "O rótulo de uma variável independente não pode estar vazio (verifique a linha # {}).".format(r + 1))
                        return
                    row[field] = self.twVariables.item(r, idx).text().strip()
                else:
                    row[field] = ""

            self.indVar[str(len(self.indVar))] = row

        self.pj[INDEPENDENT_VARIABLES] = dict(self.indVar)

        # converters
        # converters = {}
        # for row in range(self.tw_converters.rowCount()):
        #     converters[self.tw_converters.item(row, 0).text()] = {"name": self.tw_converters.item(row, 0).text(),
        #                                                           "description": self.tw_converters.item(row, 1).text(),
        #                                                           "code": self.tw_converters.item(row, 2).text().replace("@", "\n")
        #                                                          }
        # self.pj[CONVERTERS] = dict(converters)

        self.accept()

#     def pb_code_help_clicked(self):
#         """
#         help for writing converters
#         """
#         msg = QMessageBox()
#         msg.setIcon(QMessageBox.Information)
#         msg.setWindowTitle("Ajuda para escrever conversores")
#
#         msg.setText(("Um conversor é uma função que converte um valor de tempo de dados externos em segundos.<br>"
#                      "Um valor de tempo como 00:23:59 deve ser convertido em segundos antes de ser plotado de forma síncrona com sua mídia.<br>"
#                      "Para isso, você pode usar conversores nativos BORIS ou escrever seu próprio conversor.<br>"
#                      "Um conversor deve ser escrito usando o <a href=\"www.python.org\">Python3</a> linguagem.<br>"
#
# ))
#
#         #msg.setInformativeText("This is additional information")
#
#         msg.setStandardButtons(QMessageBox.Ok)
#         msg.exec_()

    # def add_converter(self):
    #     """Add a new converter"""
    #
    #     for w in [self.le_converter_name, self.le_converter_description, self.pteCode, self.pb_save_converter, self.pb_cancel_converter]:
    #         w.setEnabled(True)
    #     # disable buttons
    #     for w in [self.pb_add_converter, self.pb_modify_converter, self.pb_delete_converter, self.pb_load_from_file, self.pb_load_from_repo, self.tw_converters]:
    #         w.setEnabled(False)
    #
    # def modify_converter(self):
    #     """Modifiy the selected converter"""
    #
    #     if not self.tw_converters.selectedIndexes():
    #         QMessageBox.warning(self, programName, "Selecione um conversor na tabela")
    #         return
    #
    #     for w in [self.le_converter_name, self.le_converter_description, self.pteCode, self.pb_save_converter, self.pb_cancel_converter]:
    #         w.setEnabled(True)
    #
    #     # disable buttons
    #     for w in [self.pb_add_converter, self.pb_modify_converter, self.pb_delete_converter, self.pb_load_from_file, self.pb_load_from_repo, self.tw_converters]:
    #         w.setEnabled(False)
    #
    #     self.le_converter_name.setText(self.tw_converters.item(self.tw_converters.selectedIndexes()[0].row(), 0).text())
    #     self.le_converter_description.setText(self.tw_converters.item(self.tw_converters.selectedIndexes()[0].row(), 1).text())
    #     self.pteCode.setPlainText(self.tw_converters.item(self.tw_converters.selectedIndexes()[0].row(), 2).text().replace("@", "\n"))
    #
    #     self.row_in_modification = self.tw_converters.selectedIndexes()[0].row()
    #
    # def code_2_func(self, name, code):
    #     """
    #     convert code to function
    #
    #     Args:
    #         name (str): function name
    #         code (str): Python code
    #
    #     Returns:
    #         str: string containing Python function
    #     """
    #
    #     function = """def {}(INPUT):\n""".format(name)
    #     function += """    INPUT = INPUT.decode("utf-8") if isinstance(INPUT, bytes) else INPUT\n"""
    #     function += "\n".join(["    " + row for row in code.split("\n")])
    #     function += """\n    return OUTPUT"""
    #
    #     return function
    #
    # def save_converter(self):
    #     """Save converter"""
    #
    #     # check if name
    #     self.le_converter_name.setText(self.le_converter_name.text().strip())
    #     if not self.le_converter_name.text():
    #         QMessageBox.critical(self, "eMOC", "O conversor deve ter um nome")
    #         return
    #
    #     if not self.le_converter_name.text().replace("_", "a").isalnum():
    #         QMessageBox.critical(self, "eMOC", "Caracteres proibidos são usados no nome do conversor.<br>Use a..z, A..Z, 0..9 _")
    #         return
    #
    #     # test code with exec
    #     code = self.pteCode.toPlainText()
    #     if not code:
    #         QMessageBox.critical(self, "eMOC", "O conversor deve ter código Python")
    #         return
    #
    #     function = self.code_2_func(self.le_converter_name.text(), code)
    #
    #     try:
    #         exec(function)
    #     except:
    #         QMessageBox.critical(self, "eMOC", "O código produz um erro:<br><b>{}</b>".format(sys.exc_info()[1]))
    #         return
    #
    #
    #     if self.row_in_modification == -1:
    #         self.tw_converters.setRowCount(self.tw_converters.rowCount() + 1)
    #         row = self.tw_converters.rowCount() - 1
    #     else:
    #         row = self.row_in_modification
    #
    #     self.tw_converters.setItem(row, 0, QTableWidgetItem(self.le_converter_name.text()))
    #     self.tw_converters.setItem(row, 1, QTableWidgetItem(self.le_converter_description.text()))
    #     self.tw_converters.setItem(row, 2, QTableWidgetItem(self.pteCode.toPlainText().replace("\n", "@")))
    #
    #     self.row_in_modification = -1
    #
    #     for w in [self.le_converter_name, self.le_converter_description, self.pteCode]:
    #         w.setEnabled(False)
    #         w.clear()
    #     self.pb_save_converter.setEnabled(False)
    #     self.pb_cancel_converter.setEnabled(False)
    #     self.tw_converters.setEnabled(True)
    #
    #     self.flag_modified = True
    #
    #     # enable buttons
    #     for w in [self.pb_add_converter, self.pb_modify_converter, self.pb_delete_converter, self.pb_load_from_file, self.pb_load_from_repo, self.tw_converters]:
    #         w.setEnabled(True)
    #
    # def cancel_converter(self):
    #     """Cancel converter"""
    #
    #     for w in [self.le_converter_name, self.le_converter_description, self.pteCode]:
    #         w.setEnabled(False)
    #         w.clear()
    #     self.pb_save_converter.setEnabled(False)
    #     self.pb_cancel_converter.setEnabled(False)
    #
    #     # enable buttons
    #     for w in [self.pb_add_converter, self.pb_modify_converter, self.pb_delete_converter, self.pb_load_from_file, self.pb_load_from_repo, self.tw_converters]:
    #         w.setEnabled(True)
    #
    # def delete_converter(self):
    #     """Delete selected converter"""
    #
    #     if self.tw_converters.selectedIndexes():
    #         if dialog.MessageDialog("eMOC", "Confirme a exclusão do conversor", [CANCEL, OK]) == OK:
    #             self.tw_converters.removeRow(self.tw_converters.selectedIndexes()[0].row())
    #     else:
    #         QMessageBox.warning(self, programName, "Selecione um conversor na tabela")
    #
    # def load_converters_in_table(self):
    #     """
    #     load converters in table
    #     """
    #     self.tw_converters.setRowCount(0)
    #
    #     for converter in sorted(self.converters.keys()):
    #         self.tw_converters.setRowCount(self.tw_converters.rowCount() + 1)
    #         self.tw_converters.setItem(self.tw_converters.rowCount() - 1, 0,
    #              QTableWidgetItem(converter)) # id / name
    #         self.tw_converters.setItem(self.tw_converters.rowCount() - 1, 1,
    #              QTableWidgetItem(self.converters[converter]["description"]))
    #         self.tw_converters.setItem(self.tw_converters.rowCount() - 1, 2,
    #          QTableWidgetItem(self.converters[converter]["code"].replace("\n", "@")))
    #
    #     [self.tw_converters.resizeColumnToContents(idx) for idx in [0,1]]
    #
    # def load_converters_from_file_repo(self, mode):
    #     """
    #     Load converters from file (JSON) or BORIS remote repository
    #
    #     Args:
    #         mode (str): string "repo" or "file"
    #     """
    #
    #     converters_from_file = {}
    #     if mode == "file":
    #         fn = QFileDialog(self).getOpenFileName(self, "Carregando conversores do arquivo...", "", "All files (*)")
    #         file_name = fn[0] if type(fn) is tuple else fn
    #
    #         if file_name:
    #             with open(file_name, "r") as f_in:
    #                 try:
    #                     converters_from_file = json.loads(f_in.read())["BORIS converters"]
    #                 except:
    #                     QMessageBox.critical(self, programName, "Este arquivo não contém conversores")
    #                     return
    #
    #     if mode == "repo":
    #
    #         converters_repo_URL = "http://www.boris.unito.it/archive/converters.json"
    #         try:
    #             converters_from_repo = urllib.request.urlopen(converters_repo_URL).read().strip().decode("utf-8")
    #         except:
    #             QMessageBox.critical(self, programName, "Ocorreu um erro durante a recuperação de conversores do repositório remoto da BORIS")
    #             return
    #
    #         try:
    #             converters_from_file = eval(converters_from_repo)["BORIS converters"]
    #         except:
    #             QMessageBox.critical(self, programName, "Ocorreu um erro durante a recuperação de conversores do repositório remoto da BORIS")
    #             return
    #
    #
    #     if converters_from_file:
    #
    #         diag_choose_conv = dialog.ChooseObservationsToImport("Escolha os conversores para carregar:", sorted(list(converters_from_file.keys())))
    #
    #         if diag_choose_conv.exec_():
    #
    #             selected_converters = diag_choose_conv.get_selected_observations()
    #             if selected_converters:
    #
    #                 # extract converter names from table
    #                 converter_names = []
    #                 for row in range(self.tw_converters.rowCount()):
    #                     converter_names.append(self.tw_converters.item(row, 0).text())
    #
    #                 for converter in selected_converters:
    #                     converter_name = converter
    #
    #                     if converter in converter_names:
    #                         while True:
    #                             text, ok = QInputDialog.getText(self, "Conflito conversor",
    #                                                                   "O conversor já existe<br>Renomeie:",
    #                                                                   QLineEdit.Normal,
    #                                                                   converter)
    #                             if not ok:
    #                                 break
    #                             if text in converter_names:
    #                                 QMessageBox.critical(self, programName, "Este nome já existe em conversores")
    #
    #                             if not text.replace("_", "a").isalnum():
    #                                 QMessageBox.critical(self, programName, "Este nome contém caracteres proibidos.<br>Use a..z, A..Z, 0..9 _")
    #
    #                             if text != converter and text not in converter_names and text.replace("_", "a").isalnum():
    #                                 break
    #
    #                         if ok:
    #                             converter_name = text
    #                         else:
    #                             continue
    #                     # test if code does not produce error
    #                     function = self.code_2_func(converter_name, converters_from_file[converter]["code"])
    #
    #                     try:
    #                         exec(function)
    #                     except:
    #                         QMessageBox.critical(self, "eMOC", "O código do {} conversor produz um erro:<br><b>{}</b>".format(converter_name,
    #                                                                                                                               sys.exc_info()[1]))
    #
    #                     self.tw_converters.setRowCount(self.tw_converters.rowCount() + 1)
    #                     self.tw_converters.setItem(self.tw_converters.rowCount() - 1, 0,
    #                         QTableWidgetItem(converter_name))
    #                     self.tw_converters.setItem(self.tw_converters.rowCount() - 1, 1,
    #                         QTableWidgetItem(converters_from_file[converter]["description"]))
    #                     self.tw_converters.setItem(self.tw_converters.rowCount() - 1, 2,
    #                         QTableWidgetItem(converters_from_file[converter]["code"].replace("\n", "@")))
    #
    #                     self.flag_modified = True
    #
    #             [self.tw_converters.resizeColumnToContents(idx) for idx in [0,1]]

if __name__ == '__main__':

    import sys
    '''
    import project_functions
    _, _, pj, _ = project_functions.open_project_json("test.boris")
    '''
    
    app = QApplication(sys.argv)
    w = projectDialog()
    w.show()
    w.exec_()
    sys.exit()

