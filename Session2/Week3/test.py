
from os.path import dirname
delta = -5
from numpy import argmax,argmin
from sys import float_info



# BA5A 	Find the Minimum Number of Coins Needed to Make Change 	
#
# Input: An integer money and an array Coins of positive integers.
#
# Return: The minimum number of coins with denominations Coins that changes money.
#
# http://rosalind.info/problems/ba5a/
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

    


def FindMiddleEdge(s,t,indel_cost=5):
 
    def update(j,col1,col2,s,t):
        col2[0] = - (j * indel_cost)
        for i in range(1,len(col2)):
            scores = [col1[i-1] + Grade(s[i-1],t[j-1]),
                      col2[i-1] - indel_cost,
                      col1[i]   - indel_cost
            ]
 
            best        = argmax(scores)
            col2[i]     = scores[best]
        return col2,col1
    
    def explore(s,t,middle):
        column_A = [-(i * indel_cost) for i in range(len(s)+1)]
        column_B = [0 for i in range(len(s)+1)]
        for j in range(1,middle+1):
            scores,previous = update(j,column_A,column_B,s,t) if j%2 ==1 else update(j,column_B,column_A,s,t)
        return scores,previous
    
    middle        = len(t)//2  
    from_source,_ = explore(s,t,middle)
    to_sink,pre   = explore(s[::-1],t[::-1],middle)
    length        = [a+b for (a,b) in zip(from_source,to_sink[::-1])]
    aux           = [0 for i in range(len(s)+1)]
    post,_        = update(middle+1,from_source,aux,s,t)
    next_steps    = [a+b for (a,b) in zip(post,pre[::-1])]
    
    return ((argmax(length), middle), ( argmax(next_steps), middle+1))     

    
with open('test.txt') as f:
    lines = [line.rstrip() for line in f]


[matrix,symbolList] = ImportScoreMatrix()

# v: first string, w: second string
v = lines[0]
w = lines[1]
print (v, w)
print(FindMiddleEdge(v,w,indel_cost=5))
 