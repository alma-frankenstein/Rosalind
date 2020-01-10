#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Nucleotide counter
#Given: A DNA string s
#Return: Four integers (separated by spaces) counting the respective number of times that 
#the symbols 'A', 'C', 'G', and 'T' occur in s
.
filename = 'rosalind_dna.txt'
with open(filename) as file_object:
    gene = file_object.read()
    
#for each type of nucleotide, count the occurance in the given gene:
for i in 'ACTG':
    print(gene.count(i))
