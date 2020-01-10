#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Counting point mutations
Given: Two DNA strings s and t of equal length.
Return: The Hamming distance
"""

def mutations(stringA, stringB):
    counter = 0
    for index in range(len(stringA)): 
        if stringA[index] != stringB[index]:
            counter += 1
        
    return counter
