from collections import Counter
from itertools import product

def FWM(text, k, d):
    trans = str.maketrans('ATGC', 'TACG')
    reverse = text.translate(trans)
    reverse = reverse[-1::-1]
    #print ("reverse: ", reverse)

    kmers = [''.join(c) for c in product('ACGT', repeat=k)]
    combine = []
    result = []
   # print (kmers)

    for j in range(len(kmers)):
        combine.append(ApproximatePatternMatching(kmers[j], text, d)+ApproximatePatternMatching(kmers[j], reverse, d))
        
    for k in range(len(combine)): 
        if combine[k] == max(combine):
            result.append(kmers[k])
   
    return result
          
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
    
with open('two.txt') as f:
    lines = [line.rstrip() for line in f]
line1 = lines[0]
line2 = lines[1]
k = int(line2[0])
d = int(line2[2])
#print (d)
data = FWM(line1, k, d)
print (*data, sep = ' ')
#print (FWM('ACGTTGCATGTCGCATGATGCATGAGAGCT', 4, 1))