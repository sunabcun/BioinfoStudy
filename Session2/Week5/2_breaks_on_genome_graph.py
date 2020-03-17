def TwoBreakOnGenomeGraph(GenomeGraph, i1 , i2 , i3 , i4):
    NewGraph = GenomeGraph
    if i1 > i3:
        temp1, temp3 = i1, i3
        i1, i3 = i2, i4
        i2, i4 = temp1, temp3
    for i in range(len(GenomeGraph)):
        if GenomeGraph[i][0] == i1 or GenomeGraph[i][1] == i1:
            GenomeGraph.pop(i)
            GenomeGraph.append([i1, i3])
        elif GenomeGraph[i][0] == i3 or GenomeGraph[i][1] == i3:
            GenomeGraph.pop(i)
            GenomeGraph.append([i2, i4])
    
    return GenomeGraph
        
    
    #print(GenomeGraph[0][0])
    # remove colored edges (i1, i2) and (i3, i4) from GenomeGraph
    # add colored edges (i1, i3) and (i2, i4) to GenomeGraph
    # return GenomeGraph
    
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

indices = lines[1].split(', ')
# Change the str list to int list 
for i in range(len(indices)):
    indices[i] = int(indices[i])
i1, i2, i3, i4 = indices[0], indices[1], indices[2], indices[3]

result = TwoBreakOnGenomeGraph(Graph, i1, i2, i3, i4)


output = [[] for i in range(len(result))]
for i in range(len(result)):
    for j in range(len(result[i])):
        result[i][j] = str(result[i][j])
    output[i].append("("+ str(', '.join(result[i]))+")")
for i in range(len(output)):
    print(output[i][0], end = ', ')
