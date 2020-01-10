#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#RNA splicing
#Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s
#acting as introns. All strings are given in FASTA format.
#Return: A protein string resulting from transcribing and translating the exons of s

import itertools

#append ids and multi-line sequences to their respective lists
ids = []
sequences=[]
#so, dna as string, rest of fasta as dictionary
dna = ""

with open('rosalind_splc.txt') as file_object:
    sequence = ''
    for line in file_object:
        if ('>') not in line:
            sequence	+=	line.rstrip('\n')
            continue
        else:
            ids.append(line.rstrip('\n').lstrip('>'))
            if sequence:
                sequences.append(sequence)
                sequence = ""
    sequences.append(sequence)

#interleave ids and sequences as a list
fasta_list = ([val for pair in zip(ids, sequences) for val in pair]) 
    
    #turn the list into a dictionary
d = dict(itertools.zip_longest(*[iter(fasta_list)] * 2, fillvalue=""))
    #for each substring, replace substring with nothing
for k, v in d.items():
    dna = dna.replace(v,"")

#turn DNA to RNA
rna = dna.replace('T', 'U')

as_list = list(rna)

def rna_to_protein(rna):
    protein = ""
    
    counter = 0
    index1 = 0
    index2 = 3
    while counter < len(rna):
        codon =(as_list[index1:index2])
        codon_as_string = ''.join(codon)
        counter += 3
        index1 += 3
        index2 += 3
        if codon_as_string == 'UUU' or codon_as_string == 'UUC':
            protein = protein + 'F'
        elif codon_as_string == 'UUA' or codon_as_string == 'CUU' or codon_as_string == 'UUG':
            protein = protein + 'L'
        elif codon_as_string == 'UCU' or codon_as_string == 'UCC' or codon_as_string == 'UCA' or codon_as_string == 'UCG':
            protein = protein + 'S'
        elif codon_as_string == 'UAU' or codon_as_string == 'UAC':
            protein = protein + 'Y'
        elif codon_as_string == 'AUU':
            protein = protein + 'I'
        elif codon_as_string == 'CUC' or codon_as_string == 'CUA' or codon_as_string == 'CUG':
            protein = protein + 'L'
        elif codon_as_string == 'CCU' or codon_as_string == 'CCC' or codon_as_string == 'CCA' or codon_as_string == 'CCG':
            protein = protein + 'P'
        elif codon_as_string == 'CAU' or codon_as_string == 'CAC':
            protein = protein + 'H'
        elif codon_as_string == 'UGU' or codon_as_string == 'UGC':
            protein = protein + 'C'
        elif codon_as_string == 'UGG':
            protein = protein + 'W'
        elif codon_as_string == 'GUU':
            protein = protein + 'V'
        elif codon_as_string == 'AUC' or codon_as_string == 'AUA':
            protein = protein + 'I'
        elif codon_as_string == 'AUG':
            protein = protein + 'M'
        elif codon_as_string == 'ACU' or codon_as_string == 'ACC' or codon_as_string == 'ACA' or codon_as_string == 'ACG':
            protein = protein + 'T'
        elif codon_as_string == 'AAU':
            protein = protein + 'N'
        elif codon_as_string == 'CAA' or codon_as_string == 'CAG':
            protein = protein + 'Q'
        elif codon_as_string == 'CGU' or codon_as_string == 'CGC' or codon_as_string == 'AGA' or codon_as_string == 'AGG' or codon_as_string == 'CGA' or codon_as_string == 'CGG':
            protein = protein + 'R'
        elif codon_as_string == 'GUC' or codon_as_string == 'GUA' or codon_as_string == 'GUG':
            protein = protein + 'V'
        elif codon_as_string == 'GCU' or codon_as_string == 'GCC' or codon_as_string == 'GCA' or codon_as_string == 'GCG':
            protein = protein + 'A'
        elif codon_as_string == 'GAU' or codon_as_string == 'GAC':
            protein = protein + 'D'
        elif codon_as_string == 'AAC':
            protein = protein + 'N'
        elif codon_as_string == 'AAA' or codon_as_string == 'AAG':
            protein = protein + 'K'
        elif codon_as_string == 'AGU' or codon_as_string == 'AGC':
            protein = protein + 'S'
        elif codon_as_string == 'GAA' or codon_as_string == 'GAG':
            protein = protein + 'E'
        elif codon_as_string == 'GGU' or codon_as_string == 'GGC' or codon_as_string == 'GGG' or codon_as_string == 'GGA':
            protein = protein + 'G'
        elif codon_as_string == 'UAA' or codon_as_string == 'UAG' or codon_as_string == 'UGA': 
            break
    print(protein)
    
rna_to_protein(rna)