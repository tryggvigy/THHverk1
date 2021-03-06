'''
Created on 1.2.2014

@author: Tryggvi
'''
#klasinn skilgreinir verdbolguna i hlutnum Inflation sem er combo af (tima,gildi)
#Notkun: a = Inflation("1990-01", 7.32) til daemis.
class Inflation :
    date = ""
    value = 0 
    def __init__(self, date, value):
        self.date = date
        self.value = value

#Eftir: data er listi af strengjum thar sem hver lina ur textaskranni er einn strengur.
def readLinesFromTxt(path):
    text_file = open(path, "r")
    data = text_file.readlines();
    return data;

def getInflationList():
    l_dates = readLinesFromTxt("verdbolga_timabil.txt")
    l_values = readLinesFromTxt("verdbolga_tala.txt")
    l_inflations = list()
    
    for i in range(0, len(l_dates)) :
        l_inflations.append(Inflation(l_dates[i], float(l_values[i])))
        
    return l_inflations

#Notkun: avgInflation(a,b)
#Fyrir: start og end eru artol, strengir. t.d "1999"
#Eftir: skilar gildi sem er medaltal yfir timabilid start,end
def avgInflation(start, end):
    l_inflations = getInflationList() #ALLT RETT

    sindex = 0
    eindex = 0
    
    #finnur fyrsta index af start-arinu i listanum
    for i in range(0,len(l_inflations)) : 
        if(l_inflations[i].date[:4] == start) :  #ef fyrstu 4 stafir af date strengnum eru start arid.
            sindex = i
            break 
    #finnur seinasta index af end-arinu i listanum
    temp = 0   
    for i in range(0,len(l_inflations)) : 
        if(l_inflations[i].date[:4] == end) :  #ef fyrstu 4 stafir af date strengnum eru end arid.
            temp = i
    eindex = temp
    
    #finnur medaltal gildanna a bilinu sindex til og med eindex
    summa = 0
    count = 0
    for i in range (sindex,eindex+1) : 
        summa += l_inflations[i].value
        count += 1
    
    if(count == 0): return summa
    else:    
        avgInfl = summa/count #medaltal = summa/fjolda
        return avgInfl

    