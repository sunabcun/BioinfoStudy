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
            #print (Pattern_kmer)
    #k ← |Pattern|
    #distance ← 0
    #for each string Text in Dna
     #   HammingDistance ← ∞
      #  for each k-mer Pattern’ in Text
       #     if HammingDistance > HammingDistance(Pattern, Pattern’)
        #        HammingDistance ← HammingDistance(Pattern, Pattern’)
        #distance ← distance + HammingDistance
    #return distance
    
with open('dj.txt') as f:
    lines = [line.rstrip() for line in f]
Pattern = lines[0]
Dna = lines[1].split(" ")

print (DistanceBetweenPatternAndStrings(Pattern, Dna))