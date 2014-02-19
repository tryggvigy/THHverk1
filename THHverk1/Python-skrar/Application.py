# -*- coding: utf-8 -*-
'''
Created on 13.2.2014

@author: Lenovo
'''
import gui, PyQt4.QtGui
import Compare, reikningar, avoxtun, Plotting
from lanUtreikn import lanUtreikn
from Verdbolga import avgInflation
import matplotlib.pyplot as plt
import numpy as np


g_infl = 0
g_payment = 0
g_isMonthly = False

class Dialog(PyQt4.QtGui.QTabWidget, gui.Ui_TabWidget):     
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

        global g_isMonthly 
        g_isMonthly= self.checkBox_4.isChecked()
    
        if is_posNumber(self.lineEdit_8.text()) : 
            g_infl = float(self.lineEdit_8.text())
            

        if is_posNumber(self.lineEdit_4.text()) : 
            global g_payment
            g_payment = float(self.lineEdit_4.text()) 
        else : self.displayError()
        
        self.addLoans()
        self.addAccounts()
        best = Compare.findBestIn(Compare.g_comparer)
        self.setResults(best)


        
    def addLoans(self):
        
        loan1Name = self.lineEdit_5.text()
        loan1Interest = self.doubleSpinBox.value()
        loan1Time = self.comboBox_7.currentIndex() 
        loan1Indexed = self.checkBox.isChecked()
        
        if is_posNumber(self.lineEdit.text()) : 
            loan1Funds = float(self.lineEdit.text())
            loan1Data = lanUtreikn(loan1Funds, g_payment, loan1Time, loan1Interest, loan1Indexed)
            loan1ZeroData = lanUtreikn(loan1Funds, 0, loan1Time, loan1Interest, loan1Indexed) #FYRIR SAMANBURDARFALLID
            
            #Hendi hlutnum Entity inn i g_comparer
            Compare.g_comparer.append(Compare.Entity(loan1Name, loan1Data, loan1ZeroData, True))
        else : pass

        
        loan2Name = self.lineEdit_7.text()
        loan2Interest = self.doubleSpinBox_2.value()
        loan2Time = self.comboBox_8.currentIndex()
        loan2Indexed = self.checkBox_2.isChecked()
        
        if is_posNumber(self.lineEdit_2.text()) :
            loan2Funds = float(self.lineEdit_2.text())
            loan2Data= lanUtreikn(loan2Funds, g_payment, loan2Time, loan2Interest, loan2Indexed)
            loan2ZeroData = lanUtreikn(loan2Funds, 0, loan2Time, loan2Interest, loan2Indexed)
            Compare.g_comparer.append(Compare.Entity(loan2Name, loan2Data, loan2ZeroData, True))
        else : pass
        
        loan3Name = self.lineEdit_6.text()
        loan3Interest = self.doubleSpinBox_3.value()
        loan3Time = self.comboBox_9.currentIndex()
        loan3Indexed = self.checkBox_3.isChecked()
        
        if is_posNumber(self.lineEdit_3.text()) :
            loan3Funds = float(self.lineEdit_3.text())
            loan3Data = lanUtreikn(loan3Funds, g_payment, loan3Time, loan3Interest, loan3Indexed)
            loan3ZeroData = lanUtreikn(loan3Funds, 0, loan3Time, loan3Interest, loan3Indexed)
            Compare.g_comparer.append(Compare.Entity(loan3Name, loan3Data, loan3ZeroData, True))
        else : pass

      
       
    def addAccounts(self):
        time = 1+self.comboBox_6.currentIndex() #er 0 ?
        acc = reikningar.getReikn()
        for i in range(0,len(acc)) :
            data = []
            zeroData = []
            if(g_isMonthly):
                data = avoxtun.monthlyPayment(acc[i].innistaeda, g_payment, time, acc[i].vextir, acc[i].verdtrygg)
                zeroData = avoxtun.monthlyPayment(acc[i].innistaeda, 0, time, acc[i].vextir, acc[i].verdtrygg)
            else:
                data = avoxtun.onePayment(acc[i].innistaeda, g_payment, time, acc[i].vextir, acc[i].verdtrygg)
                zeroData = avoxtun.onePayment(acc[i].innistaeda, 0, time, acc[i].vextir, acc[i].verdtrygg)
                
            Compare.g_comparer.append(Compare.Entity(acc[i].nafn, data, zeroData, False))
        
        
    def setResults(self,best):
        
        if best.isLoan == True :
            months = len(best.data)-1
            lastPayment = best.data[-1]
            firstPayment = best.data[0]
            total_pay = g_payment
            if months != 0 : total_pay *= months
            txt = "Best væri að borga inn á efirfarandi lán:  %s" % best.name
            txt += "\ní upphafi var höfuðstóll lánsins %d kr." % firstPayment
            txt = txt + "\nEftir %d mánuði af %d kr. greiðslum verður staða lánsins orðin %d kr." % (months, g_payment, lastPayment)
            txt += "\nÞú hefur þá alls greitt %d kr. inn á %s og mismunurinn er %d." % (total_pay, best.name, lastPayment-firstPayment)
            utf8_txt = txt.decode("utf-8")
            self.plainTextEdit.setPlainText(utf8_txt)
            
        else :
            months = len(best.data)-1
            lastPayment = best.data[-1]
            firstPayment = best.data[0]
            total_pay = g_payment
            if months != 0 : total_pay *= months
            txt = "Best væri að borga inn á efirfarandi reikning:  %s" % best.name
            txt += "\ní upphafi var höfuðstóll reiknings %d kr." % firstPayment
            txt = txt + "\nEftir %d mánuði af %d kr. innborgunum verður staða lánsins orðin %d kr." % (months, g_payment, lastPayment)
            txt += "\nÞú hefur þá alls lagt inn %d kr. á %s og mismunurinn er %d." % (total_pay,best.name, lastPayment-firstPayment)
            utf8_txt = txt.decode("utf-8")
            self.plainTextEdit.setPlainText(utf8_txt)
            
        #change to result tab
        self.setCurrentIndex(1)
        
        xaxis = np.arange(0,len(best.data),1)
        plt.plot(xaxis, best.data, label = best.name)
        plt.plot(xaxis, best.zeroData, label = best.name + " Ef ekkert borgad.")
        plt.xlabel(unicode("mánuðir", "utf-8"))
        plt.ylabel("kr.")
        plt.legend()
        plt.show()
        #Plotting.showPLot(bestPlot)
        

        
       
    def setInfl(self):
        syear = str(self.comboBox.currentText())
        eyear = str(self.comboBox_2.currentText())
        g_infl = avgInflation(syear,eyear)
        
    def displayError(self) :
        errormsg = PyQt4.QtGui.QErrorMessage(self)
        errormsg.setWindowTitle("Error")
        errormsg.showMessage("Greiðslur reiturinn verður að vera tala stærri eða jöfn núll.".decode('utf-8'))
        
        
        
def is_posNumber(s):
    try:
        if (float(s) >= 0):
            return True
        else : return False
    except ValueError:
        return False
