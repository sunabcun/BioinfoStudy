from itertools import islice
from collections import Counter

def sliding_window(seq, n):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield ''.join(result)
    for elem in it:
        result = result[1:] + (elem,)
        yield ''.join(result)
 
def Get_kmers(seq, n):
    kmers = Counter()
    Frequentlst = list()

    for kmer in sliding_window(seq, n):
        if kmer in sliding_window(seq, n):
            kmers[kmer] +=1
        else:
            kmers[kmer] = 1
    #Frequentlst = [key for key in kmers.keys()]
    #Frequentlst = ''.join(Frequentlst)
    #print (Frequentlst)
    threshold = [value for (key, value) in sorted(kmers.most_common(1))]
    threshold_int = threshold[0]
    
    for i in kmers:
        if kmers[i] >= threshold_int:
            Frequentlst.append((i))
    Frequentlst = sorted(Frequentlst, key=str.lower)
    return Frequentlst
    
  
    #print ([x[0] for x in Frequentlst])
    #print (Frequentlst)
    #for key, val in kmers.items():
  #      Frequentlst.append((val, key))
   # Frequentlst.sort(reverse=True)
    #for key, val in Frequentlst:
     #   if Frequentlst[key] >= threshold_int:
      #      print (key, val)
    #Frequentkmers = [key for (key, value) in sorted(kmers.most_common(1))]
   # print(Frequentkmers)
    #return Frequentkmers
 
   # kmer in windows:
    #    kmers[kmer] += 1
    #kmers
    #print (pattern)
    #for i in range(4**n):
     #   kmers[i] = sliding_window(seq, n)
    #print (kmers) 


data =  Get_kmers('GAGCCGCGCATTTTTAAGGGTACCTTAGGCCCGAGCCGCGCGACAAAGTAGGCCCGAGCCGCGCGGTACCTGACAAAGTAGGCCCATTTTTAAGGAGCCGCGCTAGGCCCGACAAAGATTTTTAAGGAGCCGCGCGGTACCTGACAAAGGGTACCTTAGGCCCATTTTTAAGATTTTTAAGGACAAAGGGTACCTGAGCCGCGCGGTACCTGACAAAGGAGCCGCGCTAGGCCCGAGCCGCGCGGTACCTTAGGCCCGAGCCGCGCGAGCCGCGCGAGCCGCGCATTTTTAAGATTTTTAAGGGTACCTATTTTTAAGGAGCCGCGCGACAAAGGACAAAGGAGCCGCGCGAGCCGCGCTAGGCCCGGTACCTATTTTTAAGATTTTTAAGGGTACCTGACAAAGGAGCCGCGCGACAAAGGAGCCGCGCATTTTTAAGGGTACCTGAGCCGCGCGAGCCGCGCTAGGCCCTAGGCCCATTTTTAAGGGTACCTGGTACCTATTTTTAAGGAGCCGCGCGACAAAGATTTTTAAGGGTACCTGAGCCGCGCTAGGCCCTAGGCCCGACAAAGTAGGCCCTAGGCCCTAGGCCCTAGGCCCGAGCCGCGCTAGGCCCTAGGCCCGGTACCTGAGCCGCGCGGTACCTATTTTTAAGATTTTTAAGGACAAAGGGTACCTGACAAAGATTTTTAAGGGTACCTGAGCCGCGCGACAAAGGACAAAGGACAAAGGGTACCTGACAAAGGAGCCGCGCTAGGCCCTAGGCCCGAGCCGCGCGGTACCTGGTACCTGACAAAGATTTTTAAGATTTTTAAGGAGCCGCGCTAGGCCC', 12)
print (*data, sep =' ')