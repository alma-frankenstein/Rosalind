#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Transcribing DNA to RNA
#Given: A DNA string t
#Return: The transcribed RNA string of t
.
filename = 'rosalind_rna.txt'
with open(filename) as file_object:
    contents = file_object.read()

rna = contents.replace('T', 'U')
print(rna)
