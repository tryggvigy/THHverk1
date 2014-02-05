import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import * 

import gui #notenda umhverfi
from Verdbolga import avgInflation
from avoxtun import *

g_infl = 0

class Dialog(QTabWidget, gui.Ui_TabWidget):     #self er Dialog
    def __init__(self,parent=None):
        super(QTabWidget,self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):
        cB = self.comboBox.currentIndexChanged[int]
        cB.connect(self.setInfl)
        
        cB2 = self.comboBox_2.currentIndexChanged[int]
        cB2.connect(self.setInfl)

    
    def setInfl(self):
        syear = str(self.comboBox.currentText())
        eyear = str(self.comboBox_2.currentText())
        g_infl = avgInflation(syear,eyear)
        print(g_infl) 
        
        
    
        
    

###############################################################  
def main():                   
    app = QApplication(sys.argv)
    form = Dialog()
    form.show()
    app.exec_()
    
    
main()
