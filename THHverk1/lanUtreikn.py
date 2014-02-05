from Verdbolga import *

def lanUtreikn(eftirstodvar, innborgun, timi, vextir, verdtrygg):
    avg_inf = avgInflation("1990","2014") #TO-DO lata vera global var sem er buid til utfra gui fields.
    rVextir = vextir/(100*12)     
    rAvg_inf = avg_inf/(100*12)   
    
    if(verdtrygg) :
        currVal[0] = eftirstodvar
        for i in range(0,timi) : 
            currVal[i+1] = currVal[i]*(1+rVextir)*(1+rAvg_inf) - innborgun
        return currVal
        
    else :
        currVal[0] = eftirstodvar
        for i in range(0,timi) : 
            currVal[i+1] = currVal[i]*(1+rVextir) - innborgun
        return currVal
