#!/usr/bin/env python3

"""
BORIS
Behavioral Observation Research Interactive Software
Copyright 2012-2015 Olivier Friard

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

import logging
try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except:
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *

from config import *
import dialog

class wgMeasurement(QWidget):
    """
    """

    closeSignal, clearSignal = pyqtSignal(), pyqtSignal()
    flagSaved = True
    draw_mem = []

    def __init__(self, log_level):
        super().__init__()

        logging.basicConfig(level=log_level)

        self.setWindowTitle("Geometric measurement")

        vbox = QVBoxLayout(self)

        self.rbDistance = QRadioButton("Distance (start: left click, end: right click)")
        vbox.addWidget(self.rbDistance)

        self.rbArea = QRadioButton("Area (left click for area vertices, right click to close area)")
        vbox.addWidget(self.rbArea)

        self.rbAngle = QRadioButton("Angle (vertex: left click, segments: right click)")
        vbox.addWidget(self.rbAngle)

        vbox.addWidget(QLabel("<b>Scale</b>"))

        hbox1 = QHBoxLayout()

        self.lbRef = QLabel("Reference")
        hbox1.addWidget(self.lbRef)

        self.lbPx = QLabel("Pixels")
        hbox1.addWidget(self.lbPx)

        vbox.addLayout(hbox1)

        hbox2 = QHBoxLayout()

        self.leRef = QLineEdit()
        self.leRef.setText("1")
        hbox2.addWidget(self.leRef)

        self.lePx = QLineEdit()
        self.lePx.setText("1")
        hbox2.addWidget(self.lePx)

        vbox.addLayout(hbox2)

        self.pte = QPlainTextEdit()
        vbox.addWidget(self.pte)

        self.cbPersistentMeasurements = QCheckBox("Measurements are persistent")
        self.cbPersistentMeasurements.setChecked(True)
        vbox.addWidget(self.cbPersistentMeasurements)

        hbox3 = QHBoxLayout()

        self.pbClear = QPushButton("Clear measurements")
        hbox3.addWidget(self.pbClear)

        self.pbSave = QPushButton("Save results")
        hbox3.addWidget(self.pbSave)

        self.pbClose = QPushButton("Close")
        hbox3.addWidget(self.pbClose)

        vbox.addLayout(hbox3)

        self.pbClear.clicked.connect(self.pbClear_clicked)
        self.pbClose.clicked.connect(self.pbClose_clicked)
        self.pbSave.clicked.connect(self.pbSave_clicked)

    def pbClear_clicked(self):
        """
        clear measurements draw and results
        """
        self.draw_mem = {}
        self.pte.clear()
        self.clearSignal.emit()


    def pbClose_clicked(self):
        if not self.flagSaved:
            response = dialog.MessageDialog(programName, "The current results are not saved. Do you want to save results before closing?", [YES, NO, CANCEL])
            if response == YES:
                self.pbSave_clicked()
            if response == CANCEL:
                return
        self.closeSignal.emit()


    def pbSave_clicked(self):
        """
        save results
        """
        if self.pte.toPlainText():
            if QT_VERSION_STR[0] == "4":
                fileName = QFileDialog(self).getSaveFileName(self, "Save measurement results", "", "Text files (*.txt);;All files (*)")
            else:
                fileName, _ = QFileDialog(self).getSaveFileName(self, "Save measurement results", "", "Text files (*.txt);;All files (*)")
            if fileName:
                with open(fileName, "w") as f:
                    f.write(self.pte.toPlainText())
                self.flagSaved = True
        else:
            QMessageBox.information(self, programName, "There are no results to save")


if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    w = wgMeasurement(logging.getLogger().getEffectiveLevel())
    w.show()

    sys.exit(app.exec_())

