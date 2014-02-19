'''
Created on 12.2.2014

@author: Notandi
'''
from Verdbolga import avgInflation
import Plotting

def monthlyDebt(eftirstodvar,innborgun,vextir,verdtryggt):
    avg_inf = avgInflation("2014","2014")
    rVextir = vextir/(100*12)     
    rAvg_inf = avg_inf/(100*12)   
    currStatus = eftirstodvar
    monthCount = 0
    plotY = []
    if(verdtryggt) :
        while currStatus > 0 :
            plotY.append(currStatus)
            currStatus = currStatus*(1+rVextir)*(1+rAvg_inf) - innborgun
            monthCount +=1
        plotY.append(currStatus)
        if Plotting.g_doPlot:
            Plotting.plotNafn(monthCount,plotY,'Manudir','Eftirstodvar')
        return monthCount
    else:
        while currStatus > 0:
            plotY.append(currStatus)
            currStatus = currStatus*(1+rVextir) - innborgun
            monthCount +=1
        plotY.append(currStatus)
        if Plotting.g_doPlot:
            Plotting.plotNafn(monthCount,plotY,'Manudir','Eftirstodvar')
        return monthCount
        
        
        