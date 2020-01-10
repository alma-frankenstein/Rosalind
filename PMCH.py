#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Perfect matchings and RNA secondary structures
Given: An RNA string s having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.
Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s
"""
.

from math import factorial

filename = 'rosalind_pmch.txt'
with open(filename) as file_object:
    rna = file_object.read()
    
def matching(rna):
    return (factorial(rna.count("A"))*factorial(rna.count("G")))

print(matching(rna))
