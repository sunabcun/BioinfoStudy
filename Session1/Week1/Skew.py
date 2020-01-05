import matplotlib.pyplot as plt
import numpy as np
def Skew(seq):
    DNAdict = {'A': 0, 'C': -1, 'G': 1, 'T':0}
    numlist = []
    skewlist = [0]
  
    for i in range(len(seq)):
        numlist.append(DNAdict[seq[i]])
    
    for j in range(len(seq)):
        skewlist.insert(j+1, skewlist[j]+numlist[j]) 
        
    return skewlist


#print (*data, sep = ' ')
#plt.figure(figsize = (20,7))
#plt.plot(data)
#plt.xticks(np.arange(0,60,1))
#plt.xlim(0,60)
#plt.show()
#plt.savefig('plot', dpi = 1000)
#file1 = open("input.txt", "r")
#lines = file1.readlines()
#lines = [line.replace('\n', '') for line in lines]
#lines_2 = ''.join(lines)

data = Skew('CATTCCAGTACTTCGATGATGGCGTGAAGA')

location = []
minimum = min(data)
for i in range(len(data)):
    if data[i] == minimum:
        location.append(i)
print (*location, sep = ' ')
    
