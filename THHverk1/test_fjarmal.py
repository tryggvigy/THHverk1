'''
Created on 5.2.2014

@author: Lenovo
'''
from avoxtun import *
from lanUtreikn import *

print "monthlyPayment test1:" , monthlyPayment(1000000,10000,12*2,1.5,False)
print "monthlyPayment test2:" , monthlyPayment(1000, 100, 6, 3.00, True)
print "onePayment test1: " , onePayment(1000000, 10000, 12*2, 1.5, False) 
print "onePayment test2: " , onePayment(1000, 100, 6, 3.00, True)
print "lanUtreikn test1: " , lanUtreikn(1000, 100, 6, 3.00, False)
print"lanUtreikn test2: " , lanUtreikn(1000, 100, 6, 3.00, True)
