#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rabbits and recurrence relations
Given: Positive integers n≤40 and k≤5
Return: The total number of rabbit pairs that will be present after n
months, if we begin with 1 pair and in each generation, every pair of reproduction-age rabbits produces a litter 
of k rabbit pairs (instead of only 1 pair).
"""

#start with 1 pair of rabbits in each first and second months (given)
x = [1,1]

def wascally(months, pairs_per_month):
    counter = 0
    while counter+2 < months:
        new_val = ((x[-2]*pairs_per_month)+x[-1])
        x.append(new_val)
        counter += 1
    return wascally[-1]
    
