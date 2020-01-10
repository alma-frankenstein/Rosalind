#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Locating restriction sites
#Given: A DNA string of length at most 1 kbp in FASTA format.
#Return: The position and length of every reverse palindrome in the string having length between 4 and 12. 
#You may return these pairs in any order.

def main():
    
    filename = 'rosalind_revp.txt'
    dna = sequenceFromFasta(filename)
    results = reverse_palindromes(dna)

    print("\n".join([' '.join(map(str, r)) for r in results]))


def sequenceFromFasta(filename):
    with open(filename) as file_object:
        sequence = ''
        for line in file_object:
            if ('>') not in line:
                sequence += line.rstrip('\n')
                continue
    return sequence


def work_it(strand):  
    complements = {'A': 'T', 'C': 'G', 'T':'A', 'G':'C'}
    comple = ""

    for nucleotide in strand:
        comple += complements[nucleotide]
    
    return comple[::-1].strip() #reverses string
            

def reverse_palindromes(string):
    results = []

    length = len(string)

    for first_index in range(length): #for each nucleotide in the original dna
        for second_index in range(4, 13): #palindrome length 4-12

            if first_index + second_index > length:
                continue
            
#makes a slice of the dna to look at
            s1 = string[first_index : first_index+second_index]
            s2 = work_it(s1)

            if s1 == s2:
                results.append((first_index + 1, second_index))

    return results

if __name__ == "__main__":
    main()
