#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Mortal Fibonacci rabbits
#Given: Positive integers n≤100 and m≤20
#Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

#start with 1 pair of rabbits in each first and second months (given)
wabbits = [1, 1]                                                               
   
def mortal_wabbits(number_months, months_alive): 
    months = 2                                                                 
    while months < number_months: 
 #if not enough time has elapsed for the rabbits to start dying, it's just straight Fibonacci
        if months < months_alive:                                                             
            wabbits.append(wabbits[-2] + wabbits[-1])
        elif months == months_alive:                                     
            wabbits.append(wabbits[-2] + (wabbits[-1] - 1))                          
        else:       
   #subtract the rabbits that were new n months ago, because they die in this month
            wabbits.append(wabbits[-2] + wabbits[-1] - wabbits[-(months_alive + 1)])                                                           
        months += 1                                                                
    return wabbits[-1]  
    
