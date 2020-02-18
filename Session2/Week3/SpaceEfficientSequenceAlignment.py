import math
import numpy
import operator
from os.path import dirname
delta = -5

def ImportScoreMatrix():
    dataset = open(dirname(__file__)+'./BLOSUM62.txt').read().strip().split('\n')
    symbolList = dataset[0].split()
    for i in range(len(symbolList)):
        symbolList[i]=[symbolList[i],i]
    symbolList = dict(symbolList)
    matrix = []
    for i in range(1,len(dataset)):
        matrix.append(dataset[i].split()[1:])
    for l in range(len(matrix)):
        for i in range(len(matrix[l])):
            matrix[l][i]=int(matrix[l][i])
    return [matrix,symbolList]

def reverse(string): 
    string = string[::-1]
    return string

# m: number of rows, n: number of columns
def create_matrix(n, m):
    return [[(0, 0) for i in range(m)] for j in range(n)]

def Grade(Symb1,Symb2):
    Indx1 = symbolList[Symb1]
    Indx2 = symbolList[Symb2]
    return matrix[Indx1][Indx2]

def MiddleNodeAndEdge(top, bottom, left, right):
    ((i1, j1), (i2, j2)) = MiddleEdge(v[top:bottom], w[left:right])
   # print((i1, j1), (i2, j2))
    direction = "H" if i1 == i2 else "V" if j1 == j2 else "D"
    i1 = i1 + top
    return i1, direction

def LinearSpaceAlignment(top, bottom, left, right):
    if len(v)==0 and len(w) ==0:
        Track.append(" ")
 

    if left==right:
        for i in range(bottom-top):
            Track.append("V")
        
 
    elif top==bottom:
        for i in range(right-left):
            Track.append("H")

    else:
        
        middle = (left + right)//2
        midNode,midEdge = MiddleNodeAndEdge(top, bottom, left, right)
        
        LinearSpaceAlignment(top, midNode, left, middle)
       
        Track.append(midEdge)
    
        if midEdge == "H" or midEdge == "D":
            middle += 1
        
        if midEdge == "V" or midEdge == "D":
            midNode += 1
        
        LinearSpaceAlignment(midNode, bottom, middle, right)
       
    return Track
    
def MiddleEdge(v, w):
    Lenv = len(v)
    Lenw = len(w)
    # From Diagonal, From Up, From Right
    fromD, fromU, fromR = 1, 2, 3
    # Create F matrix for scoring
    F = create_matrix(Lenv + 1, Lenw + 1)

    # Fill the F matrix with indel penalty
    for i in range(1, Lenv + 1):
        F[i][0] = (delta*i, 0)
    
    for j in range(1, Lenw + 1):
        F[0][j] = (delta*j, 0)
    
    # Fill the F matrix with the calculated scores
    for i in range(1, Lenv + 1):
        for j in range(1, Lenw + 1):
            Match = F[i-1][j-1][0] + Grade(v[i-1], w[j-1])
            Delete = F[i-1][j][0] + delta
            Insert = F[i][j-1][0] + delta
            if max(Match, Delete, Insert) == Delete:
                F[i][j] = (Delete, fromU)
                
            elif max(Match, Delete, Insert) == Match:
                F[i][j] = (Match, fromD)
            
            else:
                F[i][j] = (Insert, fromR)

    # Mid column
    mid = math.floor(Lenw/2)
    i, j = len(v), len(w)
    Previous = ()
    Mid_node = ()

    while j >= mid:
        if j == mid + 1:
            Previous = (i, j)
            
        if j == mid:
            Mid_node = (i, j)
            return Mid_node, Previous

        if F[i][j][1] == fromD:
            i -= 1
            j -= 1
        elif F[i][j][1] == fromU:
            i -= 1
        else:
            j -= 1
  
    return Mid_node, Previous

def TrackToString(v, w, Track):
    
    vi = 0
    wj = 0
    outv = ''
    outw = ''
    score = 0
    for i in Track:
        if i == 'V':
            outv += v[vi]
            outw += '-'
            score += delta
            vi += 1    
        elif i == 'H':
            outv += '-'
            outw += w[wj]
            score += delta
            wj += 1            
        else:
            outv += v[vi]
            outw += w[wj]
            score += Grade(v[vi], w[wj])
            vi += 1
            wj += 1
    return [score,outv,outw]

    
with open('test.txt') as f:
    lines = [line.rstrip() for line in f]

[matrix,symbolList] = ImportScoreMatrix()

# v: first string, w: second string
v = lines[0]
w = lines[1]
if len(v) < len(w):
    v = w
    w = v
Track = []
top = 0
bottom = len(v)
left = 0
right = len(w)

Track = LinearSpaceAlignment(top, bottom, left, right)
#print(len(v))
score, String1, String2 = TrackToString(v, w, Track)
print (score)
print (String1)
print (String2)
