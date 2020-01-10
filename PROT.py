#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#translating rna to protein
#Given: An RNA string s corresponding to a strand of mRNA
#Return: The protein string encoded by s


def main():

    filename = 'rosalind_prot.txt'
    rosalind_input = list(readRos(filename))
    print(rnaToProtein(rosalind_input))


def readRos(filename):
    """takes Rosalind .txt file, saves as string variable"""
    with open(filename) as file_object:
        rosalind_input = file_object.read()
    return rosalind_input
#example output: 'MAMAPRTEINSTRING'


def rnaToProtein(rnaList):
    """takes rna list, transcribes it to proteins"""
    
    protein = ""
    
    counter = 0
    index1 = 0
    index2 = 3
    codons = []
    breakCodons = ['UAA', 'UAG', 'UGA']
    protDict = {'F':['UUU', 'UUC'], 'L': ['UUA', 'CUU', 'UUG', 'CUC', 'CUA', 'CUG'], 'S':['AGU', 'AGC','UCU', 'UCC', 'UCA', 'UCG'], 'Y':['UAU', 'UAC'],
                    'I': ['AUU', 'AUC', 'AUA'], 'P':['CCU', 'CCC', 'CCA', 'CCG'], 'H': ['CAU', 'CAC'],
                    'C': ['UGU', 'UGC'], 'W': ['UGG'], 'V': ['GUU', 'GUC', 'GUA', 'GUG'], 'M': ['AUG'], 'T': ['ACU', 'ACC', 'ACA', 'ACG'],
                    'N': ['AAU', 'AAC'], 'Q': ['CAA', 'CAG'], 'R': ['CGU', 'CGC', 'AGA', 'AGG', 'CGA', 'CGG'],
                    'A': ['GCU', 'GCC', 'GCA', 'GCG'], 'D': ['GAU', 'GAC'], 'K': ['AAA', 'AAG'],
                    'E': ['GAA', 'GAG'], 'G': ['GGU', 'GGC', 'GGG', 'GGA']}
    
    while counter < len(rnaList):
        codon =(rnaList[index1:index2])
        #makes the codon back into a string for evaluation:
        codon_as_string = ''.join(codon)
        codons.append(codon_as_string)
    
        counter += 3
        index1 += 3
        index2 += 3
    
    for codon in codons:
        if codon in breakCodons:
            break
        for k, v in protDict.items():
            if codon in v:
                protein += k
            
    return protein

if __name__ == "__main__":
    main()


    


