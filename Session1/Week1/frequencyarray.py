from collections import Counter, OrderedDict

def PatternToNumber(Pattern):
    Ptnlen = len(Pattern)
    DNAdict = {'A': 0, 'C': 1, 'G': 2, 'T':3}
    num = 0
    
    for i in range(Ptnlen):
        num += DNAdict[Pattern[i]]*4**(Ptnlen-i-1)
    return num

def FrequencyArray(Text, k):
    PtnCounter = Counter()
    for i in range(4**k):
        PtnCounter[i] = 0
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        PtnNum = PatternToNumber(Pattern)
        PtnCounter[PtnNum] += 1
    FrequencyArray = [value for (key, value) in sorted(PtnCounter.items())]

    return FrequencyArray

data = FrequencyArray('ACGCGGCTCTGAAA', 2)
print (*data, sep = ' ')