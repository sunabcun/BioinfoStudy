def CycleToChromosome(Nodes):
    Chromosome = [0 for i in range(len(Nodes)//2)]
   # print(Chromosome)
    for j in range(1, len(Nodes)//2 + 1):
        if Nodes[2*j-2] < Nodes[2*j-1]:
            Chromosome[j-1] = Nodes[2*j-1]//2
        else:
            Chromosome[j-1] = -Nodes[2*j-2]//2
    return Chromosome

def GraphToGenome(Graph):
    P = []
    Cycles = []
    pos = []
    BlackEdges = []
    for i in range(len(Graph)):
        if i == 0:
            difference = abs(Graph[i][0]-Graph[len(Graph)-1][1])
        else:
            difference = abs(Graph[i-1][1] - Graph[i][0])
        if difference != 1:
            pos.append(i)
    del pos[0]
    #print("pos:", pos)
    Cycles = [0 for i in range(len(pos)+1)]
    for j in range(len(pos)+1):
        if j == 0:
            Cycles[j] = Graph[:pos[j]]
        elif j == len(pos):
            Cycles[j] = Graph[pos[j-1]:]
        else:
            Cycles[j] = Graph[pos[j-1]:pos[j]]
    #print(Cycles[0][-1][1])
    BlackEdges = [[] for i in range(len(Cycles))]
    
    for k in range(len(Cycles)):
        for m in range(len(Cycles[k])):
           # print ("k:", k, "m:", m)
            #print(Cycles[k][m])
            if m == 0:
                BlackEdges[k].append(Cycles[k][-1][1])
                BlackEdges[k].append(Cycles[k][m][0])
                
            else:
                BlackEdges[k].append(Cycles[k][m-1][1])
                BlackEdges[k].append(Cycles[k][m][0])
        #print("____________________")
    #print(BlackEdges)
    for i in range(len(BlackEdges)):
        P.append(CycleToChromosome(BlackEdges[i]))   
    
    return P

with open('test.txt') as f:
    lines = [line.rstrip() for line in f]
line = lines[0]
import re
# extract only numbers
List = re.split(r'[()()]', line)
newList = []

for i in range(len(List)):
    if List[i] != "":
        newList.append(list(List[i].split(", ")))
Graph = []
#Change the str list to int list 
for i in range(len(newList)):
    for j in range(len(newList[i])):
        if newList[i][j] != "":
            Graph.append([int(newList[i][j]), int(newList[i][j+1])])
            break
  
result = GraphToGenome(Graph)

output = [[] for i in range(len(result))]
for i in range(len(result)):
    for j in range(len(result[i])):
        if result[i][j] > 0:
            result[i][j] = "+" + str(result[i][j])
        else:
            result[i][j] = str(result[i][j])
    output[i].append("("+ str(' '.join(result[i]))+")")
for i in range(len(output)):
    print(output[i][0], end = '')
   
    #'.join(result))
#print("("+ Output + ")")
