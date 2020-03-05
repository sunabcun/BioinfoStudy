def NumberOfBreakpoints(P):
    count = 0
    for i in range(len(P)-1):
        if P[i+1] - P[i] != 1:
            count += 1
    
    return count

with open('test.txt') as f:
    lines = [line.rstrip() for line in f]
numList = lines[0].split()
newList = []
# Change the str list to int list 
for i in range(len(numList)):
    numList[i] = int(numList[i])

#Add 0, n+1 in newList
for j in range(1, len(numList)+1):
    newList.insert(j, numList[j-1])
newList.insert(0, 0)
newList.insert(len(numList)+1, len(numList)+1)

print(NumberOfBreakpoints(newList))