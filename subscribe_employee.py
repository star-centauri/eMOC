import Pyro4
from PyQt5.QtWidgets import *
from eMOC_ui5 import *

from config import *

@Pyro4.expose
class Colaborador:
    def __init__(self, userName):
        self.userId = userName
        self.create_table()

    def get_userId(self):
        return self.userId

    def get_grid_widget(self):
        return self.grid_widget

    def events_observation(self, event):
        item = event["Event_Subject"][EVENTS]
        self.table.setRowCount(0)
        print(item)

        for i in item:
            rowPosition = self.table.rowCount()
            self.table.insertRow(rowPosition)
            self.table.setItem(rowPosition, 0, QTableWidgetItem("{}".format(i[0])))
            self.table.setItem(rowPosition, 1, QTableWidgetItem("{}".format(i[1])))
            self.table.setItem(rowPosition, 2, QTableWidgetItem("{}".format(i[2])))
            self.table.setItem(rowPosition, 3, QTableWidgetItem("{}".format(i[3])))
            self.table.setItem(rowPosition, 4, QTableWidgetItem("{}".format(i[4])))

    def create_table(self):
        self.grid_widget = QGridLayout()
        self.label = QtWidgets.QLabel(self.userId)

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(['Tempo', 'Sujeito', 'código', 'Tipo', 'Modificador'])
        self.table.setStyleSheet("QTableWidget::item {\n"
                                 "  selection-background-color: rgb(89, 89, 89);\n"
                                 "  selection-color: rgb(242, 242, 242);\n"
                                 "}\n"
                                 "\n"
                                 "QTableWidget::item:selected{\n"
                                 "    selection-background-color: rgb(38, 38, 38);\n"
                                 "    selection-color: rgb(242, 242, 242); \n"
                                 "}\n"
                                 "\n"
                                 "QHeaderView::section\n"
                                 "{\n"
                                 "  background-color: rgb(89, 89, 89);\n"
                                 "  color: rgb(242, 242, 242);\n"
                                 "}")

        self.grid_widget.addWidget(self.label)
        self.grid_widget.addWidget(self.table)
