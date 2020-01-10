#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import itertools

def fastaToDict(fileName):
    """formats FASTA downloaded from Rosalind to a dictionary,
    IDs as key and DNA sequences as values"""
    
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
    
