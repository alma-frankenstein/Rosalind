#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Enumerating gene orders
Given: A positive integer
Return: The total number of permutations of length n, 
followed by a list of all such permutations (in any order).
"""


from itertools import permutations 

def permus(n):
    perms = list(permutations(range(1,n+1)))
    return len(perms), perms
