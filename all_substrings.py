#useful for 'Finding a Shared Motif' 
#find each substring slice in the superstring
string = "GATTACA" # the classic

#get the index of each nucleotide
#'index' only returns the first occurance
for i,nuc in enumerate(string):
   # print(i,nuc)
    index1 = i
    print(index1)
    index2 = index1 + 1
    print(index2)
    
#what you want: 0:1,0:2, 0:3...1:2,1:3,1:4 etc