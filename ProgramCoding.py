# -*- coding: utf-8 -*-
"""
ProgramCoding.py

Created on Mon Feb  5 07:38:32 2018

@author: Yair
"""
import math

def GetLabel(a):
    L = (a % 5) - 1
    if (L == -1):
        L=4
        a = a - 1
    n = a / 5
    return chr(ord('A') + L) + str(math.floor(n+1))

def GetVariable(c):
    if c==1:
        return 'Y'
    else:
        d=c-1
        
        if (d % 2) ==1:
            return 'X'+str(math.floor(c/2))
        else:
            return 'Z' + str(math.floor(c/2))
   
def Zivug(x,y):
    return (2**x)*(2*y+1)-1

def RZivug(z):
    if (z % 2) == 0:
        return 0
    z = z + 1
    x = 0
    while (z % 2) == 0:
        z = z / 2
        x = x + 1
    return x
    
def LZivug(z):
    x = RZivug(z)
    t = (z + 1)/(2 ** x)
    return math.floor((t-1)/2)
    
def sieve(n):
    numbers = set(range(2, n))
    for i in range(2, int(n ** 0.5) + 1):
        for j in range(i * 2, n, i):
            numbers.discard(j)
    return sorted(numbers)

def GedolNumering(Y):
    Y=Y + 1
    n = 100
    P = sieve(n)
    GNum = []
    counter = 0
    for p in P:
        if (Y!=0):
            while (Y % p):
                counter +=1
            GNum.append(counter)
    return GNum

        
    
    
    