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
def combination(k):
    return (''.join(p) for p in itertools.product('ATCG', repeat=k))

def hamming_distance(line1, line2):
    count = 0
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            count += 1
    return count

def MedianString(Dnas, k):
    min_sum = math.inf
    min_distance = list()
    kmer_distance = list()
    kmers = list()
    Dna_fragment = list()
    best_pattern = None
    
    for combo in combination(k):
        kmers.append(combo)
    for Dna in Dnas:
        for i in range(len(Dna)-k+1):
            Dna_fragment.append(Dna[i:i+k])
    for pattern in kmers:
        for Dna in Dnas:
            for i in range(len(Dna)-k+1):
                Dna_fragment.append(Dna[i:i+k])
            for seq in Dna_fragment:
                kmer_distance.append(hamming_distance(pattern, seq))
            min_distance.append(int(min(kmer_distance)))
            kmer_distance.clear()
            Dna_fragment.clear()
            for i in window(Dna, k):
                Pattern_kmer = i           
                if HammingDistance(pattern, Pattern_kmer) < min_sum:
                    min_sum = HammingDistance(pattern, Pattern_kmer)
            best_pattern = pattern
    
        min_distance.clear()    
        
    return best_pattern
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
