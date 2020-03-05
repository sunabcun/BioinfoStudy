def CycleToChromosome(Nodes):
    Chromosome = [0 for i in range(len(Nodes)//2)]
   # print(Chromosome)
    for j in range(1, len(Nodes)//2 + 1):
        if Nodes[2*j-2] < Nodes[2*j-1]:
            Chromosome[j-1] = Nodes[2*j-1]//2
        else:
            Chromosome[j-1] = -Nodes[2*j-2]//2
    return Chromosome

with open('test.txt') as f:
    lines = [line.rstrip() for line in f]
numList = lines[0].split()
# Change the str list to int list 
for i in range(len(numList)):
    numList[i] = int(numList[i])
result = CycleToChromosome(numList)

for j in range(len(result)):
    if result[j] > 0:
        result[j] = "+" + str(result[j])
    else:
        result[j] = str(result[j])
Output = str(' '.join(result))
print("("+ Output + ")")