import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import * 

import gui #notenda umhverfi
from Verdbolga import avgInflation
from avoxtun import *
from lanUtreikn import *

g_infl = 0
g_payment = 0
g_isMonthly = False

class Dialog(QTabWidget, gui.Ui_TabWidget):     #self er Dialog
    def __init__(self,parent=None):
        super(QTabWidget,self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):
        '''INFLATION COMBO BOXES'''
        cB = self.comboBox.currentIndexChanged[int]
        cB.connect(self.setInfl)
        cB2 = self.comboBox_2.currentIndexChanged[int]
        cB2.connect(self.setInfl)
        
        '''REIKNA BUTTON'''
        pb = self.pushButton.clicked
        pb.connect(self.initCalc)
        
    def initCalc(self):
        g_payment = int(self.lineEdit_4.text())
        #print(g_payment)
        g_isMonthly = self.checkBox_4.isChecked()
    
        if(self.lineEdit_8.text() != "") : 
            g_infl = float(self.lineEdit_8.text())
        
        self.calcLoans()
        
    def calcLoans(self):
        g_payment = int(self.lineEdit_4.text()) #????????????????????????????????????????
        
        loan1Name = self.lineEdit_5.text()
        loan1Funds = float(self.lineEdit.text()) #TODO error-checka thetta
        loan1Interest = self.doubleSpinBox.value()
        loan1Time = self.comboBox_3.currentIndex() #a eftir ad koma inn
        loan1Indexed = self.checkBox.isCheckable()
        print(lanUtreikn(loan1Funds, g_payment, loan1Time, loan1Interest, loan1Indexed))
        
        loan2Name = self.lineEdit_7.text()
        loan2Funds = float(self.lineEdit_2.text())
        loan2Interest = self.doubleSpinBox_2.value()
        loan2Time = self.comboBox_4.currentIndex()
        loan2Indexed = self.checkBox_2.isChecked()
        print(lanUtreikn(loan2Funds, g_payment, loan2Time, loan2Interest, loan2Indexed))
        
        loan3Name = self.lineEdit_6.text()
        loan3Funds = float(self.lineEdit_3.text())
        loan3Interest = self.doubleSpinBox_3.value()
        loan3Time = self.comboBox_5.currentIndex()
        loan3Indexed = self.checkBox_3.isChecked()
        print(lanUtreikn(loan3Funds, g_payment, loan3Time, loan3Interest, loan3Indexed))
        
        
    
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
    ''' 
    a=float(raw_input('Innistaeda (double): '))
    b=int(raw_input('timi i fjolda manada(int): '))
    c=float(raw_input('vextir i prosentu(double): '))
    d=bool(raw_input('Verdtrygging(bool): '))
    print(onePayment(a,1000,b,c,d))
    '''
    
main()
