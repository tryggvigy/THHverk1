from Verdbolga import *
from Plotting import * 
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
        return currVal
        
    else :

        currVal.append(eftirstodvar)
        for i in range(0,timi) :
            if now <= 0 : 
                print("done") 
                return currVal 
            now = currVal[i]*(1+rVextir) - innborgun
            currVal.append( now )
        return currVal
    
#print(lanUtreikn(12,1,12,0,False))