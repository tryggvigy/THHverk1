import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import * 

import gui #notenda umhverfið
import numpy as np

class Dialog(QTabWidget, gui.Ui_TabWidget):
    def __init__(self,parent=None):
        super(QTabWidget,self).__init__(parent)
        self.setupUi(self)
        
        #self.connect(self.pushButton, SIGNAL("clicked()"), self.showMsg)
        
    def showMsg(self):
        #QMessageBox.Information(self, "hello", "hello there " + self.lineEdit_2.text())
        print("test")
        
    

###############################################################                     
app = QApplication(sys.argv)
form = Dialog()
form.show()
app.exec_() 