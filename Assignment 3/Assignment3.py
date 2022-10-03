#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 13:32:31 2022

@author: shafamazidi
"""
#Variable operations exercises

sub_code = "sub"
subnr_int = 2
subnr_str = "2"

print(sub_code + subnr_str)

print(sub_code + " " + subnr_str)

print(sub_code + " " + subnr_str * 3)

print((sub_code + subnr_str) * 3) 

print(sub_code * 3 + subnr_str * 3)

#List operations exercises

numlist = [1,2,3]

print(numlist * 2)

import numpy as np
import random

numarr = np.array([1,2,3,4])

print(numarr * 2)

strlist = ["do", "re", "mi", "fa"]

print([strlist[0] + strlist[0], strlist[1] + strlist[1], strlist[2] + strlist[2] , strlist[3] + strlist[3] ])

print(strlist * 2)

print([strlist[0], strlist[0], strlist[1], strlist[1], strlist[2],strlist[2], strlist[3], strlist[3]])

print([[strlist[0],strlist[0]],[strlist[1], strlist[1]], [strlist[2], strlist[2]], [strlist[3], strlist[3]]])



#Zipping exercises:
    
first = ['face1.png'] * 5 + ['face2.png'] * 5 + ['face3.png'] * 5 + ['face4.png'] * 5 + ['face5.png'] * 5 + ['house1.png'] * 5 + ['house2.png'] * 5 + ['house3.png'] * 5 + ['house4.png'] * 5 + ['house5.png'] * 5
second = ['house1.png', 'house2.png', 'house3.png', 'house4.png', 'house5.png'] * 5 + ['face1.png','face2.png','face3.png','face4.png','face5.png'] * 5
cues = ['cue1'] * 50 + ['cue2']* 50


trials = list(zip(first * 2 , second * 2 ,cues))

np.random.shuffle(trials)



#Indexing exercises:
    
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
print(colours[-2])
print(colours[-1][2] + colours[-1][3])

colours.pop(-1)
colours.insert(5, 'indigo' )

colours.insert(6, 'violet' )

#Slicing exercises:
    
list100 = list(range(101))
print(list100[:10])

print(list100 [99:0:-2])

print(list100 [100:96:-1])

print((list100 [39:44]) == [39, 40, 41, 42, 43])












