#from collections import Counter
from itertools import product

def FWM(text, k, d):
    #trans = str.maketrans('ATGC', 'TACG')
    #reverse = text.translate(trans)
    #reverse = reverse[-1::-1]
    #print ("reverse: ", reverse)

    kmers = [''.join(c) for c in product('ACTG', repeat=k)]
    combine = []
    result = []
    #print ("kmers: ", kmers)

    for j in range(len(kmers)):
        combine.append(ApproximatePatternMatching(kmers[j], text, d))
        
    for k in range(len(combine)): 
        if combine[k] == max(combine):
            result.append(kmers[k])
    #print (result)
    return result

def Suffix(Pattern):
    SufPtn = Pattern[1:]
    #Suffixkmers = FWM(SufPtn, len(SufPtn), d)
    return SufPtn
          
def HammingDistance(line1, line2):
    count = 0
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            count += 1
            
    return count
        
def ApproximatePatternMatching(line1, line2, d):
    Hamminglist = []
    position = []
    for i in range(len(line2)-len(line1)+1):
        Hamminglist.append(HammingDistance(line1, line2[i:i+len(line1)]))
    for j in range(len(Hamminglist)):
        if Hamminglist[j] <= d:
            position.append(j)
    num = len(position)        
    return num

def Neighbors(Pattern, d):
    Neighborhood = list()
    Nucleotide = {'A', 'C', 'G', 'T'}
    
    if d == 0:
        return Pattern
    if len(Pattern) == 1:
        Neighborhood = {'A', 'C', 'G', 'T'}
        return Neighborhood
    
    SuffixNeighbors = Neighbors(Suffix(Pattern), d)
    
    for each in SuffixNeighbors:
        if HammingDistance(Suffix(Pattern), each) < d:
            for nuc in Nucleotide:
                Neighborhood.append(nuc+each)
        else:
            Neighborhood.append(Pattern[0]+each)

    return Neighborhood

with open('two.txt') as f:
    lines = [line.rstrip() for line in f]
Pattern = lines[0]
d = int(lines[1])
print(len(Neighbors(Pattern,d)))
#f = open('result.txt', 'w')
#f.write('\n'.join(Neighbors(Pattern, d)))
#f.close()