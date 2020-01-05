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
    return [[0]*n for _ in range(m)]

def match_score(alpha, beta):
    return blosom[alpha][beta]

def GlobalAlignment(A, B, delta):
    # Create F matrix for scoring
    F = create_matrix(len(A) + 1, len(B) + 1)
    # Fill the F matrix with indel penalty
    for i in range(len(A) + 1):
        F[i][0] = delta*i
    for j in range(len(B) + 1):
        F[0][j] = delta*j
    # Fill the F matrix with the calculated scores
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            Match = F[i-1][j-1] + match_score(A[i-1], B[j-1])
            Delete = F[i-1][j] + delta
            Insert = F[i][j-1] + delta
            F[i][j] = max(Match, Insert, Delete)
    #for item in F:
     #   print (item)
    # Alignment reconstruct
    AlignmentA = A
    AlignmentB = ""
    i = len(A)
    j = len(B)
    while i > 0 or j > 0:
        #print ("i:", i, "j:", j, "//", A[i-1], B[j-1], "//", "F[i-1][j-1]:",F[i-1][j-1], "F[i][j]:"
               #,F[i][j], "F[i-1][j]:",F[i-1][j], "F[i][j-1]:",F[i][j-1], "//", match_score(A[i-1], B[j-1]))
        #print (AlignmentA, AlignmentB)
        if i > 0 and F[i][j] == F[i-1][j] + delta:
            #AlignmentA += A[i-1]
            AlignmentB += "-"
            i -= 1
        elif i > 0 and j > 0 and F[i][j] == F[i-1][j-1] + match_score(A[i-1], B[j-1]):
            #AlignmentA += A[i-1]
            AlignmentB += B[j-1]
            i -= 1
            j -= 1
       
        else:
            #AlignmentA += "-"
            AlignmentB += B[j-1]
            j -= 1
        
    print (F[len(A)][len(B)])
    return reverse(AlignmentB)

# indels are penalties of -5
delta = -5

a = open('test.txt').read()

with open('test.txt') as f:
    lines = [line.rstrip() for line in f]
# v: first string, w: second string
A = lines[0]
B = lines[1]
#if len(A) > len(B):
 #   output1, output2 = GlobalAlignment(A, B, delta)
#else:
#    output1, output2 = GlobalAlignment(B, A, delta)

output1 = GlobalAlignment(B, A, delta)
output2 = GlobalAlignment(A, B, delta)
print(output1 + "\n" + output2)
#print (output1)
#print (S[len(v)][len(w)])
#for item in S:
 #   print (item)
#print (S[10][0])
#Backtrack = LCSBackTrack(S, v, w)
#for item in Backtrack:
 #   print (item)
#with open('listnumber.txt', 'w') as filehandle:
 #   for listitem in S:
  #      filehandle.write('%s\n' % listitem)
# Write-Overwrites 
#with open('listfile.txt', 'w') as filehandle:
 #   for listitem in Backtrack:
  #      filehandle.write('%s\n' % listitem)

#if len(v) > len(w):
    #print (v)
 #   print(IterativeOutputLCS(Backtrack, v, w))
#else:
 #   print(IterativeOutputLCS(Backtrack, v, w))
    #print(w)