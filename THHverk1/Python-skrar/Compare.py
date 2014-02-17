# -*- coding: utf-8 -*-
'''
Created on 12.2.2014

@author: Lenovo
'''
import PyQt4.QtGui
import Application
g_comparer = [] 

class Entity :
    name = ""
    data = []
    isLoan = 0
    
    def __init__(self, name, data, isLoan):
        self.name = name
        self.data = data
        self. isLoan = isLoan

def findBestIn(myList):
    bestLoan = None
    bestLoanDelta = 0
    '''
    secondLoan = Entity("dummyLoan2",myList,True)
    secondLoanDelta = 0 
    '''
    bestAccount = None
    bestAccountDelta = 0
    for i in range(0,len(myList)) :
        last = myList[i].data[-1] 
        first = myList[i].data[0]
        delta = last - first
        #print(myList[i].name)
        #print(myList[i].data)
        #print(delta)
        
        if(myList[i].isLoan == True):
            #i byrjun er lanid sem kemur inn fyrst best.
            if(i == 0) : 
                bestLoan = myList[i]
                bestLoanDelta = delta
                #secondLoan = myList[i]
                #secondLoanDelta = delta
            #baetir vid besta lanid ef mismunur er laegri. (best ad hafa hann lagan i lanum
            elif(delta > bestLoanDelta) : 
                bestLoanDelta = delta
                bestLoan = myList[i]
            '''
            elif(delta > secondLoanDelta) :
                secondLoanDelta = delta
                secondLoan = myList[i]
            ''' 
        if(myList[i].isLoan == False):
            if(i == 0) : 
                bestAccountDelta = delta
                bestAccount = myList[i]
            elif(delta > bestAccountDelta) : 
                bestAccountDelta = delta
                bestAccount = myList[i]
    
    if(max(bestLoanDelta,bestAccountDelta) == bestLoanDelta) : return bestLoan
    else : return bestAccount


    
    
    
    
    
  
  
    '''
    print(bestLoan.name)
    print(bestLoanDelta)
    #print(secondLoan.name)
    #print(secondLoanDelta)
    print(bestAccount.name)
    print(bestAccountDelta)    
    '''
             

