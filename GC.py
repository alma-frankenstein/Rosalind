#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Percentage GC content
#Given:DNA strings in FASTA format
#Return: The ID of the string having the highest GC-content, followed by the GC-content of that string. 

import itertools

def main():
    fileName = 'rosalind_gc.txt'
    fastaDict = fastaToDict(fileName)
    print(maxGCandID(fastaDict))
    
def gc_counter(seq):
    gc_percentage = 100*(seq.count('C')+seq.count('G'))/len(seq)
    return gc_percentage

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


def maxGCandID(fastaDict):
    """find the sequence with the greatest GC content, return
    its ID and GC percentage"""
    
    maxGC_ID = ""
    maxGC_percentage = 0
    for k,v in fastaDict.items():
        if gc_counter(v) > maxGC_percentage:
            maxGC_percentage = gc_counter(v)
            maxGC_ID = k
    return maxGC_ID, maxGC_percentage

    
if __name__ == "__main__":
    main()
