'''
Created on 12.2.2014

@author: Lenovo
'''
import os

class Reikningur :
    nr = 0
    nafn = ""
    innistaeda = 0.0
    vextir = 0.0
    verdtrygg = 0
    
    def __init__(self, nr, nafn, innistaeda, vextir, verdtrygg):
        self.nr = nr
        self.nafn = nafn
        self.innistaeda = innistaeda
        self.vextir = vextir
        self.verdtrygg = verdtrygg
        
   
def getDB() :    
    import sqlite3 
    conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.abspath("reikningar.sqlite")), "sqlitebrowser_200_b1_win", "reikningar.sqlite"))
    c = conn.cursor()
    reikningar = []
    for row in c.execute('SELECT * FROM Reikningar ORDER BY Nafn'):
        reikningar.append(row)
        
    return reikningar

def getReikn():
    tuples = getDB()
    reikningar = []
    for i in range(0,len(tuples)) :
        reikningar.append(Reikningur(tuples[i][0],tuples[i][1],tuples[i][2],tuples[i][3],tuples[i][4]))
    return reikningar

        
        
        
