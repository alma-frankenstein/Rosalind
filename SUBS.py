#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#Finding a motif in DNA
#Given: Two DNA strings s and t
#Return: All locations of t as a substring of s.

import re

filename = 'rosalind_subs.txt'
with open(filename) as file_ob:
    sequence = file_ob.read()

#lookahead in regex for overlapping matches:
sub = "(?=)"  #manually delete substring from .txt file, put it after the ?=

locations = ""
for match in re.finditer(sub, sequence):
    #add 1 to index for location
    out = (match.start() + 1) 
    y = str(out)
    locations = locations + y + " "
print(locations)
