#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#find each substring slice in the superstring

string = "" #insert string here

def everySubstring(string):
    substrings = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            substrings.append(string[i:j+1])
    return substrings
            
print(everySubstring(string))
