def HammingDistance(line1, line2):
    count = 0
    for i in range(len(line1)):
        if line1[i] != line2[i]:
            count += 1
    return count
        
def ApproximatePatternMatching(line1, line2, d):
    Hamminglist = []
    position = []
    for i in range(len(line2)-len(line1)+1):
        Hamminglist.append(HammingDistance(line1, line2[i:i+len(line1)]))
    for j in range(len(Hamminglist)):
        if Hamminglist[j] <= d:
            position.append(j)
            
    return position
    
with open('two.txt') as f:
    lines = [line.rstrip() for line in f]

str1 = lines[0]
str2 = lines[1]
d = int(lines[2])
#print (HammingDistance(str1, str2))
data = ApproximatePatternMatching(str1,str2, d)
print (len(data))
#print (HammingDistance('GGGCCGTTGGT', 'GGACCGTTGAC'))