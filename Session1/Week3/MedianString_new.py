import itertools
import math

def window(s, k):
    for i in range(1 + len(s) - k):
        yield s[i:i+k]

def HammingDistance(p, q):
    """
    Finds the number of mismatches between 2 DNA segments of equal lengths

    p: first DNA segment (str)

    q: second DNA segment (str)

    Returns: number of mismatches (int)
    """
    return sum(s1 != s2 for s1, s2 in zip(p, q))

def DistanceBetweenPatternAndStrings(Pattern, Dna):
    import math
    k = len(Pattern)
    distance = 0
   
    for Text in Dna:
        HD = math.inf
        for i in window(Text, k):
            Pattern_kmer = i
            if HD > HammingDistance(Pattern, Pattern_kmer):
                HD = HammingDistance(Pattern, Pattern_kmer)
        distance += HD
    return distance

def combination(k):
    return (''.join(p) for p in itertools.product('ATCG', repeat=k))

def NumberToPattern(num, k):
    Nuc = {0:'A', 1:'C', 2: 'G', 3: 'T'}
    ptn = []
   # print ("num: ", num)
    for i in range(k):
        if num > 0:
            remainder = num%4
            #print ("remainder: ", remainder)
            num = int(num/4)
            #print ("num after: ", num)
            ptn.append(Nuc[remainder])
        elif num == 0:
            ptn.append(Nuc[0])
    
    ptn.reverse()
    return ptn

def MedianString(Dnas, k):
    distance = math.inf
    for Dna in Dnas:
        for i in range(4**k):
            Pattern = NumberToPattern(i, k)
        
            print (Pattern)
            currentDistance = DistanceBetweenPatternAndStrings(Pattern, Dna)
            #print (currentDistance)
            #if distance > currentDistance:
             #   distance = currentDistance
              #  Median = Pattern
        
    return 3

with open('dj.txt') as f:
    lines = [line.rstrip() for line in f]
string = lines[0]
k = int(string)
Dnas = list()

for i in range(len(lines)-1):
    Dnas.append(lines[i+1])
#print (len(lines))
#f = open('result.txt', 'w')
#f.write(' '.join(patterns))
#f.close()

print (MedianString(Dnas, k))
