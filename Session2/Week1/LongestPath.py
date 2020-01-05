def topologicalSort(graph, source, sink):
   # path = path + [start]
    for edge in graph[source][0]:
        print (edge)

with open('test4.txt') as f:
    lines = [line.rstrip() for line in f]


source = lines[0]
sink = lines[1]

# the number of edges
num = len(lines) - 2
# Make the dictionary of tuples for each node
graph = {}
weight = int()
vertex = list()
for i in range(num):
    if lines[i+2][0] not in vertex:
        vertex.append(lines[i+2][0])
    if lines[i+2][3] not in vertex:
        vertex.append(lines[i+2][3])
print(vertex)    

#for i in range(num):
#    print(lines[i+2][6])
 #    if lines[i+2][0] in graph.keys():
  #       if len(str(lines[i+2])) > 6:
   #          graph[lines[i+2][0]].append((lines[i+2][3], int(lines[i+2][5]+lines[i+2][6])))
    #     else:
     #        graph[lines[i+2][0]].append((lines[i+2][3], int(lines[i+2][5])))
     #else:
      #   if len(str(lines[i+2])) > 6:
       #      graph[lines[i+2][0]] = [(lines[i+2][3], int(lines[i+2][5]+lines[i+2][6]))]
        # else:
         #    graph[lines[i+2][0]] = [(lines[i+2][3], int(lines[i+2][5]))]

#for j in range(len(graph)):
    #a = graph[lines[j+2][0]]
 #   print (graph[lines[j+2][0]])
    #print (a)
 #   a = graph[j]
  #  print(a)
#print(graph[0])
#a = graph[lines[2][0]]
#print([i[0] for i in a])

