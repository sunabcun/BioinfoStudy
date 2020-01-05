def ProfileMostProbableKmer(text, k, profile):
    #print (profile)
    Kmers = list()
    for i in range(1 + len(text)-k):
        Kmers.append(text[i:i+k])
    Num = int()
    result = 1
    best_pattern = None
    best_result = 0
    #print (Kmers)
    for kmer in Kmers:
        for i in range(len(kmer)):
            if kmer[i] == 'A':
                Num = profile['A'][i]
            elif kmer[i] == 'T':
                Num = profile['T'][i]
            elif kmer[i] == 'G':
                Num = profile['G'][i]
            elif kmer[i] == 'C':
                Num = profile['C'][i]
            result = result*Num
        if result > best_result:
            best_result = result
            best_pattern = kmer
        
        result = 1
       
    return best_pattern
    
with open('dj.txt') as f:
    lines = [line.rstrip() for line in f]
Dna = lines[0]
k = int(lines[1])
profiledata = list()

for i in range(len(lines)-2):
    profiledata.append(lines[i+2])
    
profile = {key: list(map(float, profiledata[num].split(' '))) for (num,key) in enumerate('ACGT') }

print(ProfileMostProbableKmer(profile, Dna, k))