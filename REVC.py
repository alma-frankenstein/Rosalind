#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Reverse complement of DNA
#Given: A DNA string
#Return: The reverse complement

filename = 'rosalind_revc.txt'
       
with open(filename) as file_object:
    dna = file_object.read()

complements = {'A': 'T', 'C': 'G', 'T':'A', 'G':'C'}

def work_it(strand):  

    comple = ""

    for nucleotide in strand:
        comple += complements[nucleotide]
    
    return comple[::-1] #reverses string

print(work_it(dna))
