from collections import defaultdict

def exhaustive(graph, startnode, endnode):
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
    
with open('test4.txt') as f:
    lines = [line.rstrip() for line in f]
for i in range(len(lines)-2):
    ph = {(lines[i+2][0]):[(lines[i+2][3], lines[i+2][5])]}
#print (ph)


data_dict = defaultdict(list)
data_dict["2"].append((1, 7))
data_dict["1"].append(())
data_dict["2"].append("3")
print (data_dict)
   
if __name__ == "__main__":

    graph = {0:[(1, 7), (2, 4)], 1:[(4, 1)],
             2:[(3, 2)], 3:[(4, 3)],
             4:[]}
    startnode, endnode = int(lines[0]), int(lines[1])

    maxdist, maxpath = exhaustive(graph, startnode, endnode)
    print("Maxdist is %d, maxpath is %s" % (maxdist, maxpath))
