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
def create_matrix(m, n):
    return [[(0, 0) for i in range(m)] for j in range(n)]


def match_score(alpha, beta):
    return blosom[alpha][beta]

def calAlignment(A, B, Lower, Upper, Mid, current):
    i, j = len(A), len(B)
    
    fromM, fromL, fromU = 1, 2, 3
    current = Mid
    FinalA = ""
    FinalB = ""
   # if current == Mid:
    #    print("MID")
    #elif current == Lower:
    #    print ("LOWER")
    #else:
    #    print ("Upper")

    while current[i][j][1] > 0:
        #print(current[i][j][1], "i:",i, "j:",j, A[i-1], B[j-1])
        #if i == 0:
         #   FinalA += '-'
          #  FinalB += B[j-1]
           # j -= 1
        #elif j == 0:
         #   FinalA += A[i-1]
          #  FinalB += '-'
           # i -= 1
        #else:
        if current == Mid:
            if current[i][j][1] == fromM:
                FinalA += A[i-1]
                FinalB += B[j-1]
                i -= 1
                j -= 1
                current = Mid
               # print("Current M and next M")
            elif current[i][j][1] == fromL:
                FinalA += A[i-1]
                FinalB += '-'
                
                current = Lower
                #print("Current M and next L")
            else:
                FinalA += '-'
                FinalB += B[j-1]
                
                current = Upper
                #print("Current M and next U")
        
        elif current == Lower:
        
            if current[i][j][1] == fromM:
                i -= 1
               
              
                current = Mid
                #print("Current L and next M")
            elif current[i][j][1] == fromL:
                i -= 1
                FinalA += A[i-1]
                FinalB += '-'
                
                current = Lower
                #print("Current L and next L")
            
        elif current == Upper:
            
            if current[i][j][1] == fromM:
                j -= 1
               
                current = Mid
                #print("Current U and next M")
            else:
                j -= 1
                FinalA += '-'
                FinalB += B[j-1]
                
                current = Upper
                #print("Current U and next U")
                
        #print( reverse(FinalA), reverse(FinalB))
        
    
    return reverse(FinalA), reverse(FinalB)          

def AffineGapPanalties(A, B, gap_start, gap_extend):
    A_length = int(len(A))
    B_length = int(len(B))
    fromM, fromL, fromU = 1, 2, 3
    
    #Create Mid matrix for match/unmatch
    Mid = create_matrix(B_length + 1, A_length + 1)
    #Create Lower matrix for A string gap
    Lower = create_matrix(B_length + 1, A_length + 1)
    #Create Upper matrix for B string gap
    Upper = create_matrix(B_length + 1, A_length + 1)
    
    
    for i in range(1, A_length+1):
        Mid[i][0] = (gap_start + (i-1)*gap_extend, 0)
        Lower[i][0] = (-math.inf, 0)
        Upper[i][0] = (gap_start + (i-1) * gap_extend, 0)

    for j in range(1, B_length+1):
        Mid[0][j] = (gap_start + (j-1)*gap_extend, 0)
        Lower[0][j] = (gap_start + (j-1)*gap_extend, 0)
        Upper[0][j] = (-math.inf, 0)
    #print (Mid)
    #print(Lower)
    #print(Upper)
    
    #Set the Mid matrix edge scores
    #for i in range(1, A_length + 1):
     #   Mid[i][0] = (gap_start + (i-1)*gap_extend, 0)
    #for j in range(1, B_length + 1):
     #   Mid[0][j] = (gap_start + (j-1)*gap_extend, 0)
    #Set the Lower matrix edge scores
   # for i in range(1, A_length + 1):
    #    Lower[i][0] = -math.inf
    #for j in range(1, B_length + 1):
     #   Lower[0][j] = gap_start + (j-1)*gap_extend
    #Set the Upper matrix edge scores
   # for j in range(1, B_length + 1):
    #    Upper[0][j] = -math.inf
    #for i in range(1, A_length + 1):
     #   Upper[i][0] = gap_start + (i-1)*gap_extend
   
    # Fill the Mid, X, Y matrix with the scores
    for i in range(1, A_length + 1):
        for j in range(1, B_length + 1):
            Lower[i][j] = max((Lower[i-1][j][0] + gap_extend, fromL),
                 (Mid[i-1][j][0] + gap_start, fromM))
            
          #  if Lower[i][j] == Lower[i-1][j] + gap_extend:
           #     LowPointer[i-1][j] = 'L'
            #else:
             #   LowPointer[i-1][j] = 'M'
            
            Upper[i][j] = max((Upper[i][j-1][0] + gap_extend, fromU),
                 (Mid[i][j-1][0] + gap_start, fromM))
            
           # if Upper[i][j-1] == Upper[i][j-1] + gap_extend:
            #    UpperPointer[i][j-1] = 'U'
            #else:
             #   UpperPointer[i][j-1] = 'M'
            
            Mid[i][j] = max((Lower[i][j][0], fromL),
               (Mid[i-1][j-1][0] + match_score(A[i-1], B[j-1]), fromM),
               (Upper[i][j][0], fromU))
            
            #if Mid[i][j] == Lower[i][j]:
             #   MidPointer[i-1][j-1] = 'L'
            #elif Mid[i][j] == Upper[i][j]:
             #   MidPointer[i-1][j-1] = 'U'
            #else:
             #   MidPointer[i-1][j-1] = 'M'
            
    Maxscore = max(Lower[A_length][B_length], Upper[A_length][B_length], Mid[A_length][B_length])
    if Maxscore == Lower[A_length][B_length]:
        current = Lower
    elif Maxscore == Upper[A_length][B_length]:
        current = Upper
    else:
        current = Mid
        
    return Maxscore, current, Lower, Upper, Mid

a = open('test.txt').read()

with open('test.txt') as f:
    lines = [line.rstrip() for line in f]
# v: first string, w: second string
A = lines[0]
B = lines[1]
gap_start = -11
gap_extend = -1
Maxscore, current, Lower, Upper, Mid = AffineGapPanalties(A, B, gap_start, gap_extend)
print(Maxscore[0])
#print(current)
#for item in LowPointer:
 #   print (item)
#print("______________")
#for item in UpperPointer:
 #   print (item)
#print("+++++++++++++++++")
#for item in MidPointer:
 #   print (item)    

FinalA, FinalB = calAlignment(A, B, Lower, Upper, Mid, current)
print(FinalA)
print(FinalB)