#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: 
k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.

Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele 
(and thus displaying the dominant phenotype). Assume that any two organisms can mate."""

def mendalizer(k,m,n):
    first_denom = (n+k+m)
    second_denom = first_denom - 1
    
    k_one = k/first_denom
    a = k_one*((k-1)/second_denom)
    b = k_one*(m/second_denom)
    c = k_one*(n/second_denom)
    
    m_one = m/first_denom
    d = m_one*(k/second_denom)
    e = m_one*((m-1)/second_denom)
    f = m_one*(n/second_denom)
    
    n_one = n/first_denom
    g = n_one*(k/second_denom)
    h = n_one*(m/second_denom)
    i = n_one*((n-1)/second_denom)
    
    #Probability offspring will have dominant allele. Ignore i, because it's homozygous recessive
    dom_allele = a+b+c+d+(e*(3/4))+(f*(1/2))+g+(h*(1/2))  
    return dom_allele

