import time
start = time.time()

def ClumpFinding(Text, k, L, t):
    out = []
    for i in range(len(Text)-L+1):
        #print ("i: ", i)
        window = Text[i:i+L]
        #print ("Window: ", window)
        counts = {}
        #print ("counts: ", counts)
        for j in range(len(window)-k+1):
            #print ("j: ", j)
            if window[j:j+k] not in counts:
                counts[window[j:j+k]] = 0
            counts[window[j:j+k]] += 1
            #print ("counts after: ", counts)
        for kmer in counts:
            #print ("kmer: ", kmer)
            if counts[kmer] >= t and kmer not in out:
                out.append(kmer)
            #print ("out: ", out)
    return out

file1 = open("E_coli.txt", "r")
lines = file1.readlines()
lines = [line.replace('\n', '') for line in lines]
lines_2 = ''.join(lines)

k = 9
L = 500
t = 3
print (' '.join(ClumpFinding(lines_2,k,L,t)))

end = time.time()
print(end-start)