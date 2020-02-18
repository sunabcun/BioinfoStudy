import math

# Blosom chart for matched amino acids
blosom = {'A': {'A': 4, 'C': 0, 'E': -1, 'D': -2, 'G': 0, 'F': -2, 'I': -1, 'H': -2, 
       'K': -1, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 
       'T': 0, 'W': -3, 'V': 0, 'Y': -2}, 
 'C': {'A': 0, 'C': 9, 'E': -4, 'D': -3, 'G': -3, 'F': -2, 'I': -1, 'H': -3, 
       'K': -3, 'M': -1, 'L': -1, 'N': -3, 'Q': -3, 'P': -3, 'S': -1, 'R': -3,
       'T': -1, 'W': -2, 'V': -1, 'Y': -2}, 
 'E': {'A': -1, 'C': -4, 'E': 5, 'D': 2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 
       'K': 1, 'M': -2, 'L': -3, 'N': 0, 'Q': 2, 'P': -1, 'S': 0, 'R': 0, 
       'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 
 'D': {'A': -2, 'C': -3, 'E': 2, 'D': 6, 'G': -1, 'F': -3, 'I': -3, 'H': -1, 
       'K': -1, 'M': -3, 'L': -4, 'N': 1, 'Q': 0, 'P': -1, 'S': 0, 'R': -2, 
       'T': -1, 'W': -4, 'V': -3, 'Y': -3}, 
 'G': {'A': 0, 'C': -3, 'E': -2, 'D': -1, 'G': 6, 'F': -3, 'I': -4, 'H': -2, 
       'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -2, 'P': -2, 'S': 0, 'R': -2, 
       'T': -2, 'W': -2, 'V': -3, 'Y': -3}, 
 'F': {'A': -2, 'C': -2, 'E': -3, 'D': -3, 'G': -3, 'F': 6, 'I': 0, 'H': -1, 
       'K': -3, 'M': 0, 'L': 0, 'N': -3, 'Q': -3, 'P': -4, 'S': -2, 'R': -3, 
       'T': -2, 'W': 1, 'V': -1, 'Y': 3}, 
 'I': {'A': -1, 'C': -1, 'E': -3, 'D': -3, 'G': -4, 'F': 0, 'I': 4, 'H': -3, 
       'K': -3, 'M': 1, 'L': 2, 'N': -3, 'Q': -3, 'P': -3, 'S': -2, 'R': -3, 
       'T': -1, 'W': -3, 'V': 3, 'Y': -1}, 
 'H': {'A': -2, 'C': -3, 'E': 0, 'D': -1, 'G': -2, 'F': -1, 'I': -3, 'H': 8, 
       'K': -1, 'M': -2, 'L': -3, 'N': 1, 'Q': 0, 'P': -2, 'S': -1, 'R': 0, 
       'T': -2, 'W': -2, 'V': -3, 'Y': 2}, 
 'K': {'A': -1, 'C': -3, 'E': 1, 'D': -1, 'G': -2, 'F': -3, 'I': -3, 'H': -1, 
       'K': 5, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -1, 'S': 0, 'R': 2, 
       'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 
 'M': {'A': -1, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 1, 'H': -2, 
       'K': -1, 'M': 5, 'L': 2, 'N': -2, 'Q': 0, 'P': -2, 'S': -1, 'R': -1, 
       'T': -1, 'W': -1, 'V': 1, 'Y': -1}, 
 'L': {'A': -1, 'C': -1, 'E': -3, 'D': -4, 'G': -4, 'F': 0, 'I': 2, 'H': -3, 
       'K': -2, 'M': 2, 'L': 4, 'N': -3, 'Q': -2, 'P': -3, 'S': -2, 'R': -2, 
       'T': -1, 'W': -2, 'V': 1, 'Y': -1}, 
 'N': {'A': -2, 'C': -3, 'E': 0, 'D': 1, 'G': 0, 'F': -3, 'I': -3, 'H': 1, 
       'K': 0, 'M': -2, 'L': -3, 'N': 6, 'Q': 0, 'P': -2, 'S': 1, 'R': 0, 
       'T': 0, 'W': -4, 'V': -3, 'Y': -2}, 
 'Q': {'A': -1, 'C': -3, 'E': 2, 'D': 0, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 
       'K': 1, 'M': 0, 'L': -2, 'N': 0, 'Q': 5, 'P': -1, 'S': 0, 'R': 1, 
       'T': -1, 'W': -2, 'V': -2, 'Y': -1}, 
 'P': {'A': -1, 'C': -3, 'E': -1, 'D': -1, 'G': -2, 'F': -4, 'I': -3, 'H': -2, 
       'K': -1, 'M': -2, 'L': -3, 'N': -2, 'Q': -1, 'P': 7, 'S': -1, 'R': -2, 
       'T': -1, 'W': -4, 'V': -2, 'Y': -3}, 
 'S': {'A': 1, 'C': -1, 'E': 0, 'D': 0, 'G': 0, 'F': -2, 'I': -2, 'H': -1, 
       'K': 0, 'M': -1, 'L': -2, 'N': 1, 'Q': 0, 'P': -1, 'S': 4, 'R': -1, 
       'T': 1, 'W': -3, 'V': -2, 'Y': -2}, 
 'R': {'A': -1, 'C': -3, 'E': 0, 'D': -2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 
       'K': 2, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -2, 'S': -1, 'R': 5, 
       'T': -1, 'W': -3, 'V': -3, 'Y': -2}, 
 'T': {'A': 0, 'C': -1, 'E': -1, 'D': -1, 'G': -2, 'F': -2, 'I': -1, 'H': -2, 
       'K': -1, 'M': -1, 'L': -1, 'N': 0, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 
       'T': 5, 'W': -2, 'V': 0, 'Y': -2}, 
 'W': {'A': -3, 'C': -2, 'E': -3, 'D': -4, 'G': -2, 'F': 1, 'I': -3, 'H': -2, 
       'K': -3, 'M': -1, 'L': -2, 'N': -4, 'Q': -2, 'P': -4, 'S': -3, 'R': -3, 
       'T': -2, 'W': 11, 'V': -3, 'Y': 2}, 
 'V': {'A': 0, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': -1, 'I': 3, 'H': -3, 
       'K': -2, 'M': 1, 'L': 1, 'N': -3, 'Q': -2, 'P': -2, 'S': -2, 'R': -3, 
       'T': 0, 'W': -3, 'V': 4, 'Y': -1}, 
 'Y': {'A': -2, 'C': -2, 'E': -2, 'D': -3, 'G': -3, 'F': 3, 'I': -1, 'H': 2, 
       'K': -2, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -3, 'S': -2, 'R': -2, 
       'T': -2, 'W': 2, 'V': -1, 'Y': 7}}

def reverse(string): 
    string = string[::-1]
    return string

# m: number of rows, n: number of columns
def create_matrix(n, m):
    return [[(0, 0) for i in range(m)] for j in range(n)]

def match_score(alpha, beta):
    return blosom[alpha][beta]

def MiddleEdge(A, B, delta):
    LenA = len(A)
    LenB = len(B)

    # From Diagonal, From Up, From Right
    fromD, fromU, fromR = 1, 2, 3
    # Create F matrix for scoring
    F = create_matrix(LenA + 1, LenB + 1)
    
    # Fill the F matrix with indel penalty
    for i in range(1, LenA + 1):
        F[i][0] = (delta*i, 0)
    
    for j in range(1, LenB + 1):
        F[0][j] = (delta*j, 0)
    
    # Fill the F matrix with the calculated scores
    for i in range(1, LenA + 1):
        for j in range(1, LenB + 1):
            Match = F[i-1][j-1][0] + match_score(A[i-1], B[j-1])
            Delete = F[i-1][j][0] + delta
            Insert = F[i][j-1][0] + delta
            if max(Match, Delete, Insert) == Delete:
                F[i][j] = (Delete, fromU)
                
            elif max(Match, Delete, Insert) == Match:
                F[i][j] = (Match, fromD)
            
            else:
                F[i][j] = (Insert, fromR)
    #for item in F:
     #   print(item)            
    # Mid column
    mid = math.floor(LenB/2)
    i, j = len(A), len(B)
    
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


with open('test.txt') as f:
    lines = [line.rstrip() for line in f]
# v: first string, w: second string
A = lines[0]
B = lines[1]
delta = -5

Mid_node, Previous = MiddleEdge(A, B, delta)
print (Mid_node, Previous)

#MiddleEdge(F, mid, A_len, B_len)
