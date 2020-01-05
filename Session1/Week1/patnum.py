def PatternToNumber(Pattern):
    Ptnlen = len(Pattern)
    DNAdict = {'A': 0, 'C': 1, 'G': 2, 'T':3}
    num = 0
    
    for i in range(Ptnlen):
        num += DNAdict[Pattern[i]]*4**(Ptnlen-i-1)
    return num
        
print (PatternToNumber("CCATGAGTTCGGGTAACG"))

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
            
print (''.join(NumberToPattern(7998,11)))