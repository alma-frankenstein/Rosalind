#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Calculating protein mass
#Given: A protein string P
#Return: The total weight of P. Consult the monoisotopic mass table, https://en.wikipedia.org/wiki/Proteinogenic_amino_acid#Mass_spectrometry.

filename = 'rosalind_prtm.txt'

with open(filename) as file_object:
    rosalind_input = file_object.read().strip('\n')

protDict = {'A': 71.03711, 'C':103.00919, 'D':115.02694, 'E':129.04259, 'F':147.06841,'G':57.02146,'H':137.05891,
             'I':113.08406,'K':128.09496,'L':113.08406,'M':131.04049,'N':114.04293,'P':97.05276, 'Q':128.05858,
             'R':156.10111, 'S':87.03203, 'T':101.04768, 'V':99.06841,'W':186.07931,'Y':163.06333}

def prot_mass(prot_string):
    total = 0
    
    for letter in prot_string:
        total += protDict[letter]
        
    return(total)

print(prot_mass(rosalind_input))
