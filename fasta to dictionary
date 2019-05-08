import itertools

#append ids and multi-line sequences to their respective lists
ids = []
sequences=[]
with open('rosalind_gc(1).txt') as file_object:
    sequence = ''
    for line in file_object:
        if ('>') not in line:
            sequence	+=	line.rstrip('\n')
            continue
        else:
            ids.append(line.rstrip('\n').lstrip('>'))
            if sequence:
                sequences.append(sequence)
                sequence = ""
    sequences.append(sequence)
#print(ids)
#print(sequences)

#interleave ids and sequences as a list
fasta_list = ([val for pair in zip(ids, sequences) for val in pair]) 

#turn the list into a dictionary
d = dict(itertools.zip_longest(*[iter(fasta_list)] * 2, fillvalue=""))
print(d)
