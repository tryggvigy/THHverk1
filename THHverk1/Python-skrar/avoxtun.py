'''
Created on 1.2.2014

@author: Tryggvi
'''
from Verdbolga import *
import Plotting


'''
Notkun: calculate(a,b,c,d)
Fyrir: innborgun er tala, timi er fjoldi manada sem a ad spara i (integer),
        vextir eru prosenta eins og t.d 3.24, verdtrygg er boolean breyta.
Eftir: fallid skilar heildarupphaed a reikning eftir timan(skrefin) timi.
        s.s thetta fall segir ther um hvad mikid upphaed sem thu leggur inna reikning mun vaxa.
'''
def onePayment(innistaeda, innborgun, timi, vextir, verdtrygg):
    '''TO-DO Lata upphaed inna reikning plusast her vid.'''
    total = innborgun+innistaeda
    avg_inf = avgInflation("2014","2014") #TO-DO lata vera global var sem er buid til utfra gui fields.
    rVextir = vextir/(100*12)     #vextir i brotabroti a manudi.
    rAvg_inf = avg_inf/(100*12)   #verdbolga i brotabroti a manudi.

    if(verdtrygg) :
        currVal = total
        y = [0] * (timi) 
        for i in range(0,timi) : 
            currVal = currVal*(1+rVextir)*(1+rAvg_inf)
            y[i] = currVal
        if Plotting.g_doPlot :
            Plotting.plot(y,timi)
        return currVal
        
    else :
        currVal = total
        y = [0] * (timi) 
        for i in range(0,timi) : 
            currVal = currVal*(1+rVextir)
            y[i] = currVal
        if Plotting.g_doPlot:
            Plotting.plot(y,timi)
        return currVal


'''    
    if(verdtrygg) :
        #rakningarformula f. verdbaettan reikning
        Evt = ((1+rVextir)**timi)*((1+rAvg_inf)**timi)*total #** er veldis-virkinn i Python.
        return Evt
        
    else :
        #rakningarformula f. overdtryggdan reikning
        E = ((1+rVextir)**timi)*total
        return E
  '''
  
def monthlyPayment(innistaeda, innborgun, timi, vextir, verdtrygg):
    avg_inf = avgInflation("1990","2014") 
    rVextir = vextir/(100*12)     
    rAvg_inf = avg_inf/(100*12)   
    
    if(verdtrygg) :
        currVal = innistaeda
        y = [0] * (timi) 
        for i in range(0,timi) : 
            y[i] = currVal
            currVal = currVal*(1+rVextir)*(1+rAvg_inf) + innborgun
        if g_doPlot:
            Plotting.plot(y,timi)
        return currVal
        
    else :
        currVal = innistaeda
        y = [0] * (timi) 
        for i in range(0,timi) : 
            y[i] = currVal
            currVal = currVal*(1+rVextir) + innborgun
        if g_doPlot:
            Plotting.plot(y,timi)
        return currVal


#prufa
'''  
print(onePayment(0,1000,14,3.00,False))
print(onePayment(0,1000,14,3.00,True))
print(monthlyPayment(1000000, 10000, 36, 1.5, True))
'''
#monthlyPayment(1000000, 10000, 36, 1.5, True)
