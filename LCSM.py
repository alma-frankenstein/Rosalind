#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Shared motifs
Given: A collection of k (k≤100) DNA strings of length at most 1 kbp each in FASTA format.
Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)
"""
def main():
    sequences = fastaFormatter()
    
    #find the shortest string in the list of sequences
    shortest = min(fastaFormatter(), key = len)
    everySub = everySubstring(shortest)
    print(longestCommon(sequences, everySub))


def fastaFormatter():
    #format FASTA data as a list of sequences
    sequences=[]
    with open('rosalind_lcsm.txt') as file_object:
        sequence = ''
        for line in file_object:
            if ('>') not in line:
                sequence +=	line.rstrip('\n')
                continue
            else:
                if sequence:
                    sequences.append(sequence)
                    sequence = ""
        sequences.append(sequence)
    return sequences


def everySubstring(shortest):
    substrings = []
    for i in range(len(shortest)):
        for j in range(i, len(shortest)):
            substrings.append(shortest[i:j+1])
    return substrings
    

def longestCommon(sequences, everySubstring):
    in_all =[] #these substrings are in every superstring
    for sub in everySubstring:
        contains =[]
        for seq in sequences:
            if sub in seq:
    #if the substring's in the superstring, append a truthy value to 
                contains.append(1)
            else:
                contains.append(0)
    #if the substring's in all the superstrings, append it to in_all
        if all(contains):
            in_all.append(sub)
    #return the longest substring in that list
    return max(in_all, key=len)


if __name__ == '__main__':
    main()
