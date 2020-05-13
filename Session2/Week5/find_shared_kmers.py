def create_frequency_table(string, k):
    freqs = {}
    for kmer in [string[i:i+k] for i in range(len(string)-k+1)]:
        if kmer in freqs:
            freqs[kmer]+=1
        else:
            freqs[kmer] = 1
    return freqs

def reverse(kmer):
    cm = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return "".join(cm[k] for k in reversed(kmer))

def subs(s, t):
    matches=[]
    start=0
    while start>-1:
        start=s.find(t,start)
        if start>-1:
            start+=1
            matches.append(start)
    return matches

def find_shared_kmers(k,s1,s2):
    def create_matches():
        freq1 = create_frequency_table(s1, k)
        freq2 = create_frequency_table(s2, k)
        matches = []
        for kmer in freq1:
            if kmer in freq2:
                matches.append((kmer, kmer))
            rev_kmer = reverse(kmer)
            if rev_kmer in freq2:
                matches.append((kmer, rev_kmer))
        return matches
    
    index = []
    for k1, k2 in create_matches():
        for i1 in subs(s1, k1):
            for i2 in subs(s2, k2):
                index.append((i1-1, i2-1))
    return sorted(index)

if __name__=='__main__':
    with open('test.txt') as f:
        lines = [line.rstrip() for line in f]
    k = int(lines[0])
    s1 = lines[1]
    s2 = lines[2]
    result = find_shared_kmers(k, s1, s2)
    for d in result:
        print(d)