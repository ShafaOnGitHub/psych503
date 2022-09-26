#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 22:15:28 2022

@author: shafamazidi
"""
#Operations
print(5/2)

print(5.0/2.0)

print(5 % 2)

print(10 % 2)

print(2 % 10)

print(2.5 % 10)


print(2 ** 3)

print(3**2)

print (3//2)

print (2//10)

print (2 + 2 * 8 - 2)

#Boolean
print (1==1.0)
print ("1" == "1.0")

print (5 == (3+2))

print (1 == 1.0 and not "1" == "1.0" and 5 ==(3+2) )
print (1 == 1.0 or 5 == (3+2) and not "1" == "1.0" )
print (5 == (3+2) and 1 == 1.0 and not "1" == "1.0")
print (5 == (3+2) or 1 == 1.0 and not "1" == "1.0")
print (5 == (3+2) and not "1" == "1.0" and 1 == 1.0)

#lists

oddlist = [1,3,5,7,9]
print (oddlist)
len(oddlist)
type(oddlist)

intlist = list(range(100))
print (intlist)

#Dictionary 
about_me = {"your name" : "Shafa", "age" : 24.0, "year of study" : 7, "favourite foods": ["Pho","Ramen","Banh mi"]}
print (about_me)
type(about_me)

len(about_me)

#Array Exercise 
import numpy as np

mixnums = np.array([1,2,3,4.0,5.5,6.0])
print (mixnums)

mixtypes = np.array([1,2,3.5,4.5,"hellow","world"])
print(mixtypes)

oddarray = np.arange(1,100,2)
print(oddarray)

logarray = np.logspace(1,5,16)
print (logarray)
