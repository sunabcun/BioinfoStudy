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
  
with open('test.txt') as f:
    lines = [line.rstrip() for line in f]
numList = lines[0].split()
# Change the str list to int list 
for i in range(len(numList)):
    numList[i] = int(numList[i])
List = ChromosomeToCycle(numList)

# Change the int list to str list
for k in range(len(List)):
    List[k] = str(List[k])
    
Output = str(' '.join(List))
print("("+ Output + ")")