#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#RNA splicing
#Given: A DNA string s (of length at most 1 kbp) and a collection of substrings of s
#acting as introns. All strings are given in FASTA format.
#Return: A protein string resulting from transcribing and translating the exons of s

import PROT, fastaToDict

def main():
    filename = 'rosalind_splc.txt'
    dna = ""   #manually delete sequence from fasta, paste it here
    introns = fastaToDict.fastaToDict(filename)
    
    for k, v in introns.items():
        dna = dna.replace(v,"")
    
    rna = dna.replace('T', 'U')  #turn DNA to RNA
    rna = list(rna)
    protein = PROT.rnaToProtein(rna)
    print(protein)

if __name__ == "__main__":
    main()
