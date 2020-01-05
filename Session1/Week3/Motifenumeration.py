import itertools

def combination(k):
    return (''.join(p) for p in itertools.product('ATCG', repeat=k))

def hamming_distance(pattern, seq):
    return sum(c1 != c2 for c1, c2 in zip(pattern, seq))

# Return True if combo is within d in any window of string
def in_window(combo, string, k, d):
    return any(hamming_distance(combo, pat) <= d for pat in window(string, k))

def motif_enumeration(DNA, k, d):
    pattern = set()
    for combo in combination(k):
        if all(in_window(combo, string, k, d) for string in DNA):
            pattern.add(combo)
    return pattern

def window(s, k):
    for i in range(1 + len(s) - k):
        yield s[i:i+k]

with open('dj.txt') as f:
    lines = [line.rstrip() for line in f]
string = lines[0]
string2 = string.split(" ")
k = int(string2[0])
d = int(string2[1])
Dna = list()

for i in range(6):
    Dna.append(lines[i+1])
patterns =  motif_enumeration(Dna, k, d)
f = open('result.txt', 'w')
f.write(' '.join(patterns))
f.close()

#d = int(lines[1])
#f = open('result.txt', 'w')
#f.write('\n'.join(Neighbors(Pattern, d)))
#f.close()