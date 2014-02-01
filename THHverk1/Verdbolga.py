'''
Created on 1.2.2014

@author: Tryggvi
'''
class Inflation :
    date = ""
    value = 0 
    def __init__(self, date, value):
        self.date = date
        self.value = value
    
def readLinesFromTxt(path):
    text_file = open(path, "r")
    data = text_file.readlines();
    return data;

def getInflationList():
    #l_dates = readLinesFromTxt("C://verdbolga_timabil.txt")
    #l_values = readLinesFromTxt("C://verdbolga_tala.txt")
    l_dates = readLinesFromTxt("verdbolga_timabil.txt")
    l_values = readLinesFromTxt("verdbolga_tala.txt")
    l_inflations = list()
    
    for i in range(0, len(l_dates)) :
        l_inflations.append(Inflation(l_dates[i], float(l_values[i])))
        
    return l_inflations


#prufa
print(getInflationList()[0].date)

        
        
    