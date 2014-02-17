from Verdbolga import avgInflation
import Plotting 

def lanUtreikn(eftirstodvar, innborgun, timi, vextir, verdtrygg):
    avg_inf = avgInflation("1990","2014")
    rVextir = vextir/(100*12)     
    rAvg_inf = avg_inf/(100*12)   
    currVal=[]
    now = 1337 #eitthvad annad en 0 eda None.
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
                print("LanUtreikn: done") 
                return currVal 
            now = currVal[i]*(1+rVextir) - innborgun
            currVal.append( now )
        if Plotting.g_doPlot:
            Plotting.plotNafn(timi,currVal,'Manudir','Eftirstodvar')
        return currVal
