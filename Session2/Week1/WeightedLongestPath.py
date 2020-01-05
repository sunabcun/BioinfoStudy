from collections import defaultdict

def exhaustive(graph, startnode, endnode):
    global maxpath
    maxdist = -1
    stack = [([startnode], 0)]
    while stack:
        cpath, cdist = stack.pop()
#        print("cpath: ", cpath, "cdist: ", cdist)
        cnode = cpath[-1]
 #       print("Cnode: ", cnode)
        if cnode == endnode:
            if cdist > maxdist:
                maxdist = cdist
                maxpath = cpath
            continue
        for nbr, nbrdist in graph[cnode]:
  #          print("nbr: ", nbr, "nbrdist: ", nbrdist)
            stack.append( (cpath+[nbr], nbrdist+cdist) )
   #     print ("stack: ", stack)

    return maxdist, maxpath

if __name__ == "__main__":
    with open('test4.txt') as f:
        lines = [line.rstrip().replace(":", " ").replace("-", " ").replace(">", " ") for line in f]

    startnode, endnode = int(lines[0]), int(lines[1])
    my_list = list()

    graph1 = defaultdict(list)

    for i in range(len(lines)-2):
        for number in lines[i+2].split():
            my_list.append(int(number))
        graph1[my_list[0]].append((my_list[1], my_list[2]))
    #print(my_list[1])
        my_list.clear()

#print(type(graph1))

#print(graph1, startnode, endnode)
#print(exhaustive(graph1, startnode, endnode))
    maxdist, maxpath = exhaustive(graph1, startnode, endnode)

print(maxdist)
print(*maxpath, sep = '->')