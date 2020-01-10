#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Calculating expected offspring
Given: Six nonnegative integers. The integers correspond to the number of couples in a population possessing 
each genotype pairing for a given factor. In order, the six given integers represent the number of couples having 
the following genotypes:

    AA-AA
    AA-Aa
    AA-aa
    Aa-Aa
    Aa-aa
    aa-aa

Return: The expected number of offspring displaying the dominant phenotype in the next generation, 
under the assumption that every couple has exactly two offspring.

Percent offspring with dominant allele (from punnett squares), times 2 offspring
a = 2
b = 2
c = 2
d = 1.5
e = 1
f = 0
"""

#save the punnett numbers, still ordered, and the given Rosalind input, in lists
punnet = [2,2,2,1.5,1,0]
rosInput = []

def popu(rosInput):
    domTotal = 0
    for i in range(len(punnet)):
        domTotal += (punnet[i]*rosInput[i])
    return domTotal
    
