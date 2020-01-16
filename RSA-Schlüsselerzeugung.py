#16.01.2020 13:15 Uhr - Start
#RSA-Verschlüsselung - Nils Lorentzen - Paul Golz - Martin Kreuzer

#Imports

from random import *

#Variablen

p = 3
q = 7
n = 0
phn = 0             #phi von n
e = 0
d = 0

#subs
def phi(a,b):       #phi rechnung
    c = (a-1)*(b-1) 
    return c

def ggt(a, b):
    while b != 0:
        c = a % b
        a, b = b, c
    return a



#::::::::::::::::::::::::::::::::::::Main::::::::::::::::::::::::::::::::::::::::::::


#                           p und q wählen
#p =
#q =

n = p*q                     #n berechnen
phn = phi(p,q)              #phi von n berechnen

e = randint(2,phn-1)        #e berechnen
while not ggt(e,phn) == 1:
    e = randint(2,phn-1)



print(n,phn,e)