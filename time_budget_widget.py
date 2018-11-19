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
import os
import tablib
import pathlib

import dialog

from config import *
from utilities import intfloatstr


class timeBudgetResults(QWidget):
    """
    class for displaying time budget results in new window
    a function for exporting data in TSV, CSV, XLS and ODS formats is implemented
    
    Args:
        log_level ():
        pj (dict): BORIS project
    """

    def __init__(self, log_level, pj):
        super().__init__()

        logging.basicConfig(level=log_level)
        self.pj = pj
        self.label = QLabel()
        self.label.setText("")
        self.lw = QListWidget()
        self.lw.setEnabled(False)
        self.lw.setMaximumHeight(100)
        self.lbTotalObservedTime = QLabel()
        self.lbTotalObservedTime.setText("")
        self.twTB = QTableWidget()

        hbox = QVBoxLayout(self)

        hbox.addWidget(self.label)
        hbox.addWidget(self.lw)
        hbox.addWidget(self.lbTotalObservedTime)
        hbox.addWidget(self.twTB)

        hbox2 = QHBoxLayout()

        self.pbSave = QPushButton("Save results")
        hbox2.addWidget(self.pbSave)

        spacerItem = QSpacerItem(241, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hbox2.addItem(spacerItem)

        self.pbClose = QPushButton("Close")
        hbox2.addWidget(self.pbClose)

        hbox.addLayout(hbox2)

        self.setWindowTitle("Time budget")

        self.pbClose.clicked.connect(self.close)
        self.pbSave.clicked.connect(self.pbSave_clicked)


    def pbSave_clicked(self):
        """
        save time budget analysis results in TSV, CSV, ODS, XLS format
        """

        def complete(l, max):
            """
            complete list with empty string until len = max
            """
            while len(l) < max:
                l.append("")
            return l

        logging.debug("save time budget results to file")

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

        fileName, filter_ = filediag_func(self, "Save Time budget analysis", "", ";;".join(extended_file_formats))

        if not fileName:
            return

        outputFormat = file_formats[extended_file_formats.index(filter_)]
        if pathlib.Path(fileName).suffix != "." + outputFormat:
            fileName = str(pathlib.Path(fileName)) + "." + outputFormat

        if fileName:
            rows = []
            # observations list
            rows.append(["Observations:"])
            for idx in range(self.lw.count()):
                rows.append([""])
                rows.append([self.lw.item(idx).text()])

                if INDEPENDENT_VARIABLES in self.pj[OBSERVATIONS][self.lw.item(idx).text()]:
                    rows.append(["Independent variables:"])
                    for var in self.pj[OBSERVATIONS][self.lw.item(idx).text()][INDEPENDENT_VARIABLES]:
                        rows.append([var, self.pj[OBSERVATIONS][self.lw.item(idx).text()][INDEPENDENT_VARIABLES][var]])

            rows.extend([[""],[""],["Time budget:"]])

            # write header
            cols = []
            for col in range(self.twTB.columnCount()):
                cols.append(self.twTB.horizontalHeaderItem(col).text())

            rows.append(cols)
            rows.append([""])

            for row in range(self.twTB.rowCount()):
                values = []
                for col in range(self.twTB.columnCount()):
                    values.append(intfloatstr(self.twTB.item(row,col).text()))

                rows.append(values)

            maxLen = max([len(r) for r in rows])
            data = tablib.Dataset()
            data.title = "Time budget"

            for row in rows:
                data.append(complete(row, maxLen))

            if outputFormat in ["tsv", "csv", "html"]:
                with open(fileName, "wb") as f:
                    f.write(str.encode(data.export(outputFormat)))
                return

            if outputFormat in ["ods", "xlsx", "xls"]:
                with open(fileName, "wb") as f:
                    f.write(data.export(outputFormat))
                return
