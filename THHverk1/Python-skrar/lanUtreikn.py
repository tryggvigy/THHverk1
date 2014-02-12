from Verdbolga import *
import Plotting 
#TODO: baeta vid landstima?  oll lan verdur ad borga upp eftir akvedinn tima.
def lanUtreikn(eftirstodvar, innborgun, timi, vextir, verdtrygg):
    avg_inf = avgInflation("1990","2014")
    rVextir = vextir/(100*12)     
    rAvg_inf = avg_inf/(100*12)   
    currVal=[]
    now = 1337
    if(verdtrygg) :
        currVal.append(eftirstodvar)
        for i in range(0,timi) :
            if now <= 0 : 
                print("done") 
                return currVal
            now = currVal[i]*(1+rVextir)*(1+rAvg_inf) - innborgun
            currVal.append( now )
        if Plotting.g_doPlot:
            Plotting.plotNafn(timi,currVal,'Manudir','Eftirstodvar')
        return currVal
        
    else :

        currVal.append(eftirstodvar)
        for i in range(0,timi) :
            if now <= 0 : 
                print("done") 
                return currVal 
            now = currVal[i]*(1+rVextir) - innborgun
            currVal.append( now )
        if Plotting.g_doPlot:
            Plotting.plotNafn(timi,currVal,'Manudir','Eftirstodvar')
        return currVal
#print(lanUtreikn(1000,100,10,5,True))