def ChromosomeToCycle(Chromosome):
    Nodes = []
    
    for i in Chromosome:
        if i> 0:
            Nodes.append(2*i-1)
            Nodes.append(2*i)
        else:
            Nodes.append(-2*i)
            Nodes.append(-2*i-1)
        
    return Nodes

# BA6G Implement Cycle to Chromosome
#
# CycleToChromosome
#
# Invert ChromosomeToCycle
#
# Input:  Nodes - fraph in form 2x,2x-1 e.g. [1, 2, 4, 3, 6, 5, 7, 8]
#
# Returns: Chromosome e.g. [+1, -2, -3, +4]

def CycleToChromosome(Nodes):
    Chromosome = []
    it =iter(Nodes)
    for i in it:
        a,b = (i, next(it))
        if a<b:
            Chromosome.append(b//2)
        else:
            Chromosome.append(-a//2)
        
    return Chromosome

#    BA6J Implement 2-BreakOnGenomeGraph
#
#    get2BreakOnGenomeGraph
#
#    Solve the 2-Break On Genome Graph Problem.
#
#    Inputs: The colored edges of a genome graph GenomeGraph, followed by indices i, i', j, and j'.
#
#    Return: The colored edges of the genome graph resulting from applying the 2-break operation.

def get2BreakOnGenomeGraph(graph,i0,i1,j0,j1):
    def eq(x,y):
        u,v=x
        w,z=y
        return (u ==w and v==z) or (w==v and u==z)
    removed = [x for x in graph if not eq(x,(i0,i1)) and not eq(x,(j0,j1))]
    return removed +[(i0,j0)] + [(i1,j1)]
    
#    BA6K Implement 2-BreakOnGenome

# GraphToGenomeAll
#

def GraphToGenomeAll(GenomeGraph):
    def build_index():
        def insert(a,b):
            if not a in Index:
                Index[a]=[]
            Index[a].append(b)
        Index = {}
        for (a,b) in GenomeGraph:
            insert(a,b)
            insert(b,a)
        return Index

    def extract_cycle(Index,a,b):
        Cycle = [a,b]
        while True:    # build one cycle
            nexts = Index[b]
            next_link = list(set(nexts) - set(Cycle))
            if len(next_link)>0:
                b = next_link[0]
                Cycle.append(b)
            else:
                x,y = nexts
                assert x== Cycle[0] or y == Cycle[0]
                for c in Cycle:
                    del Index[c]
                return Cycle

    Index  = build_index()
    Graph  = GenomeGraph[:]
    Genome = []
    while len(Graph)>0:
        a,b   = Graph[0]
        Cycle = extract_cycle(Index,a,b)
        Genome.append(Cycle)
        Graph = [(a,b) for (a,b) in Graph if not a in Cycle]
    return [CycleToChromosome(g) for g in Genome]

def Edges(it):
    return [(i,next(it)) for i in it]

def BlackEdges(Nodes):
    return Edges(iter(Nodes))

def ColouredEdges(Nodes):
    return Edges(iter(Nodes[1:]+[Nodes[0]]))
        
#    BA6K Implement 2-BreakOnGenome
#
#    perform_2_BreakOnGenome
#
#    Solve the 2-Break On Genome Graph Problem.
#
#    Inputs: A genome P, followed by indices i, i', j, and j'.
#
#    Return: The genome P' resulting from applying the 2-break operation.

def perform_2_BreakOnGenome(P,i0,i1,j0,j1):
    
    Nodes = ChromosomeToCycle(P)
  
    return GraphToGenomeAll(
        get2BreakOnGenomeGraph(
            BlackEdges(Nodes) + ColouredEdges(Nodes),i0,i1,j0,j1))

def formatting(line):
    import re
    # extract only numbers
    List = re.split(r'[()()]', line)

    String = str(List[1])
    newList = String.split(" ")

    # Change the str list to int list 
    for i in range(len(newList)):
        if newList[i].__contains__("+"):
            newList[i].replace('+', '')
            newList[i] = int(newList[i])
        elif newList[i].__contains__('-'):
            newList[i].replace('-', '')
            newList[i] = int(newList[i])
    
    return newList

def indexing(line2):
    indices = line2.split(', ')
    # Change the str list to int list 
    for i in range(len(indices)):
        indices[i] = int(indices[i])
    i1, i2, i3, i4 = indices[0], indices[1], indices[2], indices[3]
    
    return i1, i2, i3, i4
    
def format(genome):
    def ff(g):
        return '+'+str(g) if g>0 else str(g)
    def f(g):
        return '('+ ' '.join([ff(g0) for g0 in g]) + ')'
    return ' '.join([f(g) for g in genome])
    
with open('test.txt') as f:
    lines = [line.rstrip() for line in f]
P = formatting(lines[0])
i1, i2, i3, i4 = indexing(lines[1])
        
result = perform_2_BreakOnGenome(P, i1, i2, i3, i4)
print(format(result))

