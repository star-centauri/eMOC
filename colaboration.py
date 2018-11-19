from utilities import *
from colaboration_ui5 import Ui_Form

try:
    from PyQt5.QtGui import *
    from PyQt5.QtCore import *
    from PyQt5.QtWidgets import *
except:
    logging.critical("PyQt5 not installed!\nTry PyQt5")
    sys.exit()


class Colaboration(QDialog, Ui_Form):

    def __init__(self, parent=None):
        super(Colaboration, self).__init__(parent)
        self.setupUi(self)

        self.btn_cancel.clicked.connect(self.reject)
