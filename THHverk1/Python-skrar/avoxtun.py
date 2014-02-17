'''
Created on 1.2.2014

@author: Tryggvi
'''
from Verdbolga import avgInflation
import Plotting


'''
Notkun: onePayment(a,b,c,d)
Fyrir: innistaeda er float, innborgun er tala, timi er fjoldi manada sem a ad spara i (integer),
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
    y = []
    if(verdtrygg) :
        y.append(innistaeda)
        for i in range(0,timi) : 
            total = total*(1+rVextir)*(1+rAvg_inf)
            y.append(total)
        if Plotting.g_doPlot :
            Plotting.plot(y,timi)
        return y
        
    else :
        y.append(innistaeda)
        for i in range(0,timi) : 
            total = total*(1+rVextir)
            y.append(total)
        if Plotting.g_doPlot:
            Plotting.plot(y,timi)
        return y
  
def monthlyPayment(innistaeda, innborgun, timi, vextir, verdtrygg):
    avg_inf = avgInflation("1990","2014")
    total = innborgun+innistaeda 
    rVextir = vextir/(100*12)     
    rAvg_inf = avg_inf/(100*12)  
    y = [] 
    
    if(verdtrygg) :
        y.append(innistaeda)
        for i in range(0,timi) : 
            total = total*(1+rVextir)*(1+rAvg_inf) + innborgun
            y.append(total)
        if Plotting.g_doPlot:
            Plotting.plot(y,timi)
        return y
        
    else :
        y.append(innistaeda)
        for i in range(0,timi) : 
            total = total*(1+rVextir) + innborgun
            y.append(total)
        if Plotting.g_doPlot:
            Plotting.plot(y,timi)
        return y


#prufa

print(onePayment(0,1000,14,3.00,False))
print(onePayment(0,1000,14,3.00,True))
print(monthlyPayment(1000000, 10000, 36, 1.5, True))

#monthlyPayment(1000000, 10000, 36, 1.5, True)
