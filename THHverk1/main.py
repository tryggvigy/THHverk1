from PyQt4.QtCore import *
from PyQt4.QtGui import * 


#import pyqtgraph as pg
#from pyqtgraph.Qt import *
#from pyqtgraph.Point import *

import sys
import gui

class Dialog(QTabWidget, gui.Ui_TabWidget):
    def __init__(self,parent=None):
        super(QTabWidget,self).__init__(parent)
        self.setupUi(self)
        
        #self.connect(self.PushButton_2, SIGNAL("clicked()"), self.showMsg)
        
    def showMsg(self):
        #QMessageBox.Information(self, "hello", "hello there " + self.lineEdit_2.text())
        print("test")
        
    #p = pg.GraphicsWindow().addplot(row=1, col=0 )
                     
app = QApplication(sys.argv)
form = Dialog()
form.show()
app.exec_() 