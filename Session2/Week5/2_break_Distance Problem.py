def get_synteny_blocks(a):
    return [j for i in a for j in i]

def conv(xx):
        return [int(s) for s in xx]
    
def parse(line):
    ff=line[1:-1].split(')(')
    result=[conv(fff.split(' ')) for fff in ff]
    return result

def count_synteny_blocks(a):
    return max(abs(b) for b in get_synteny_blocks(a))

def ChromosomeToCycle(Chromosome):
    Nodes = []
    for i in Chromosome:
        if i > 0:
            Nodes.append(2*i - 1)
            Nodes.append(2*i)
        else:
            Nodes.append(-2*i)
            Nodes.append(-2*i - 1)
            
    return Nodes

def update(adjacency, edges, x, y, max_node):
    edges.append((x, y))
    
    if x in adjacency:
        adjacency[x].append(y)
    else:
        adjacency[x]=[y]
    
    if x > max_node:
        max_node = x

    return max_node

def ColorEdges(P):
    Edges = []
    for Chromosome in P:
        Nodes = ChromosomeToCycle(Chromosome)
        it = iter(Nodes[1:] + [Nodes[0]])
        for i in it:
            Edges.append((i, next(it)))
    return Edges

def build_cycle(start, adjacency):
    cycle = []
    ins = [start]
    while len(ins) > 0:
        j = ins[0]
        if not j in cycle:
            cycle.append(j)
            for link in adjacency[j]:
                if not link in cycle:
                    ins.append(link)
        ins.pop(0)
    for i in cycle:
        adjacency.pop(i)
    return cycle

def d2break(a, b):
    # Verify that the two genomes share the same synteny blocks
    blocks = get_synteny_blocks(a)
    n = count_synteny_blocks(a)
    nb = count_synteny_blocks(b)
    assert (n == nb), 'Mismatched synteny blocks {0} != {1}'.format(n, nb)
    
    # Combines color edges from both chromosomes
    edges = []
    adjacency = {}
    max_node = -1
    
    for (x, y) in ColorEdges(a) + ColorEdges(b):
        max_node = update(adjacency, edges, x, y, max_node)
        max_node = update(adjacency, edges, y, x, max_node)
     
    # Count cycles by building each cycle and pruninig the adjacency list
    count = 0
    for i in range(1, max_node+1):
        if i in adjacency:
            build_cycle(i, adjacency)
            count += 1
    
    return n - count

with open('test.txt') as f:
    lines = [line.rstrip() for line in f]
a = parse(lines[0])
b = parse(lines[1])

print(d2break(a, b))