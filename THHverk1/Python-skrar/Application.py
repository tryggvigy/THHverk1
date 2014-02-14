'''
Created on 13.2.2014

@author: Lenovo
'''
import gui
#from PyQt4.QtCore import *
import PyQt4.QtGui 
import Compare
from lanUtreikn import lanUtreikn
from Verdbolga import avgInflation
import reikningar
import avoxtun

g_infl = 0
g_payment = 0
g_isMonthly = False

class Dialog(PyQt4.QtGui.QTabWidget, gui.Ui_TabWidget):     #self er Dialog
    def __init__(self,parent=None):
        super(PyQt4.QtGui.QTabWidget,self).__init__(parent)
        self.setupUi(self)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("MainWindow")
        
        '''INFLATION COMBO BOXES'''
        cB = self.comboBox.currentIndexChanged[int]
        cB.connect(self.setInfl)
        cB2 = self.comboBox_2.currentIndexChanged[int]
        cB2.connect(self.setInfl)
        
        '''REIKNA BUTTON'''
        pbClick = self.pushButton.clicked
        pbClick.connect(self.initCalc)
        
        self.setInfl()
        
    
    def initCalc(self):
        #reset comparer, maybe user changed loans.
        Compare.g_comparer = []

        g_payment = int(self.lineEdit_4.text())
        #print(g_payment)
        g_isMonthly = self.checkBox_4.isChecked()
    
        if(self.lineEdit_8.text() != "") : 
            g_infl = float(self.lineEdit_8.text())
            
        self.addLoans()
        self.addAccounts()
        best = Compare.findBestIn(Compare.g_comparer)
        self.setResults(best)
        #change to result tab
        self.setCurrentIndex(1)

        
    def addLoans(self):
        g_payment = int(self.lineEdit_4.text()) #????????????????????????????????????????
        
        loan1Name = self.lineEdit_5.text()
        loan1Funds = float(self.lineEdit.text()) #TODO error-checka thetta
        loan1Interest = self.doubleSpinBox.value()
        loan1Time = self.comboBox_3.currentIndex() #a eftir ad koma inn
        loan1Indexed = self.checkBox.isChecked()
        loan1Data = lanUtreikn(loan1Funds, g_payment, loan1Time, loan1Interest, loan1Indexed)
        
        loan1DataZero = lanUtreikn(loan1Funds, 0, loan1Time, loan1Interest, loan1Indexed) #FYRIR SAMANBURDARFALLID
        #Hendi hlutnum Entity inn i g_comparer
        Compare.g_comparer.append(Compare.Entity(loan1Name, loan1DataZero, True))
        
        loan2Name = self.lineEdit_7.text()
        loan2Funds = float(self.lineEdit_2.text())
        loan2Interest = self.doubleSpinBox_2.value()
        loan2Time = self.comboBox_4.currentIndex()
        loan2Indexed = self.checkBox_2.isChecked()
        loan2Data= lanUtreikn(loan2Funds, g_payment, loan2Time, loan2Interest, loan2Indexed)
        
        loan2DataZero = lanUtreikn(loan2Funds, 0, loan2Time, loan2Interest, loan2Indexed)
        Compare.g_comparer.append(Compare.Entity(loan2Name, loan2DataZero, True))
        
        loan3Name = self.lineEdit_6.text()
        loan3Funds = float(self.lineEdit_3.text())
        loan3Interest = self.doubleSpinBox_3.value()
        loan3Time = self.comboBox_5.currentIndex()
        loan3Indexed = self.checkBox_3.isChecked()
        loan3Data = lanUtreikn(loan3Funds, g_payment, loan3Time, loan3Interest, loan3Indexed)
        
        loan3DataZero = lanUtreikn(loan3Funds, 0, loan3Time, loan3Interest, loan3Indexed)
        Compare.g_comparer.append(Compare.Entity(loan3Name, loan3DataZero, True))

      
       
    def addAccounts(self):
        acc = reikningar.getReikn()
        for i in range(0,len(acc)) :
            data = []
            if(g_isMonthly):
                data = avoxtun.monthlyPayment(acc[i].innistaeda, g_payment, 12, acc[i].vextir, acc[i].verdtrygg)
            else:
                data = avoxtun.onePayment(acc[i].innistaeda, g_payment, 12, acc[i].vextir, acc[i].verdtrygg)
            Compare.g_comparer.append(Compare.Entity(acc[i].nafn, data, False))
        
        
    def setResults(self,best):
        self.plainTextEdit.setPlainText("Best vaeri ad leggja peningana i: " + str(best.name))  
        self.tab_2.setFocus()
        self.tab_2.activateWindow()
        self.tab_2.raise_()
        
       
    def setInfl(self):
        syear = str(self.comboBox.currentText())
        eyear = str(self.comboBox_2.currentText())
        g_infl = avgInflation(syear,eyear)
        #print(g_infl) 
        
        
    
