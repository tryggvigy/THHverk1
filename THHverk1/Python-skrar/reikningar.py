'''
Created on 12.2.2014

@author: Lenovo
'''
import sqlite3 
conn = sqlite3.connect('/THH1/THHverk1/THHverk1/Python-skrar/sqlitebrowser_200_b1_win/reikningar.sqlite')
c = conn.cursor()
reikningar = []
for row in c.execute('SELECT * FROM Reikningar ORDER BY Nafn'):
        print row
        reikningar.append(row)
        
print(reikningar)
