def ChromosomeToCycle(Chromosome):
    Nodes = [0 for i in range(2*len(Chromosome))]
    for j in range(1, len(Chromosome)+1):
        i = Chromosome[j-1]
        #print("i:", i, "j:", j)
        if i > 0:  
            Nodes[2*j-2] = 2*i-1
            Nodes[2*j-1] = 2*i
         #   print(j, Nodes)
        else:
            Nodes[2*j-2] = -2*i
            Nodes[2*j-1] = -2*i - 1
          #  print(j, Nodes)
        
    return Nodes

def ColoredEdges(P):
    Edges = []
    for chs in P:
        Nodes = ChromosomeToCycle(chs)
        #print(chs)
        #print(Nodes)
        Nodes.append(Nodes[0])
        #print(Nodes)
        for j in range(1, len(chs)+1):
           # Edges.append(Nodes[2*j-1])
            Edges.append(tuple([Nodes[2*j-1], Nodes[2*j]]))
         #   print(Edges)
    
    return Edges

with open('test.txt') as f:
    lines = [line.rstrip() for line in f]
line = lines[0]
import re
# extract only numbers
List = re.split(r'[()()]', line)
newList = []
for i in range(len(List)):
    if List[i] != "":
        newList.append(list(List[i].split(" ")))

# Change the str list to int list 
for i in range(len(newList)):
    for j in range(len(newList[i])):
        newList[i][j] = int(newList[i][j])
     
print(ColoredEdges(newList))
