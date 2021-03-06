#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Overlap graphs
Given: FASTA of DNA IDs and sequences
Return: adjacency list, where the last three nucleotides of one sequence
   match the first three nucleotides of the one it's adjacent to
"""

import itertools

def main():
    fileName = 'rosalind_grph.txt'
    fastaDict = fastaToDict(fileName)
    print(matcher(fastaDict, 3))
    

def fastaToDict(fileName):
    """formats FASTA downloaded from Rosalind to a dictionary,
    with IDs as keys and DNA sequences as values"""
    #append ids and multi-line sequences to their respective lists
    ids = []
    sequences=[]
    with open(fileName) as file_object:
        sequence = ''
        for line in file_object:
            if ('>') not in line:
                sequence += line.rstrip('\n')
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
    return d


def matcher(dic,n):
    """ creates list of sequences that overlap by n nucleotides"""
    results = []
    for k1, v1 in dic.items():
        for k2, v2 in dic.items():
            if k1 != k2 and v1.endswith(v2[:n]):
                results.append((k1,k2))
    return results


if __name__ == '__main__':
    main()
