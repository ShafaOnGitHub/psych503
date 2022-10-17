#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 22:27:56 2022

@author: shafamazidi
"""

# Conditionals and loops

# Conditional Exersices 

#1. 

response = 8

if response == 1 or response == 2:    
    print("OK")                      #this needs to be indented after the semi colon boolean part. This part tells us what to do if the conditions are met 
    
elif response == "NaN":
    print("Subject did not repond")
    
else: print("Subject pressed the wrong key")

#2. 

response = 2

if response == 1 or response == 2:    
    print("OK")
    if response == 1:
        print("correct")  
       # We cannot put an elif statement on this line beacuse nested fucntions will only evaluate the line if the previous bolean (in this case "correct" has been printed) is true.
    if response == 2:
        print("incorrect!")                 
        
elif response == "NaN":
    print("Subject did not repond")
    
else: print("Subject pressed the wrong key")



# For Loops

#1. 



name = ["S", "h", "a", "f", "a"] 

for letters in name:
    print(letters)


#2. 

import numpy as np

name = ["S", "h", "a", "f", "a"] 

count = -1

for letters in name:
    count = count+1
    print(letters, count)


#3 

namelist = ["Amy", "Rory", "River"]

for eachname in namelist:
    eachname = eachname       #This was needed to create a varibles out of each string 
    for eachletter in eachname:
        print(eachletter)

#4 

namelist = ["Amy", "Rory", "River"]


for eachname in namelist:
    eachname = eachname
    count = -1       #everytime this part of the loop starts over, count starts at 0
         
    for eachletter in eachname:
        count = count+1
        print(eachletter, count)
       
# While loops

#1. 

iteration = 0


while iteration < 10 :
    iteration = iteration + 1 # + 1 adds an interation during the while while loop, so that it increases by 1 each time
    print("image1.png")

while iteration > 9 and iteration < 20:
    iteration = iteration + 1
    print("image2.png")

#2. 

  
import random 
   
response = True #subject makes a respone
iteration = 0 #add an iteration counter


while response == True: #while the subject makes a response
    iteration = iteration +1
    print("image.png", iteration)
    
    if random.randint(0,10) == 1 or random.randint(0,10) == 2: # if we generate a 1 or a two
        response=False # then we dont print a response, this is like if the participant (random number generator) responded with a 1 or 2
        
#3. 

  
import random 
   
response = True #subject makes a respone
iteration = 0 #add an iteration counter
failsafe = -1 #add a failsafe counter so if the subject never responds, terminate the loop anyway


while response == True: #while the subject makes a response
    failsafe = failsafe+1 #every time the loop starts over, add 1 to the counter
    if failsafe == 5: #after 5 iterations, if the subject still has not responsed
        break #break the loop
    
    iteration = iteration +1
    print("image.png", iteration)
    
    if random.randint(0,10) == 1 or random.randint(0,10) == 2: # if we generate a 1 or a two
        response=False # then we dont print a response, this is like if the participant (random number generator)
        
    




