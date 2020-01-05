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

def IterativeOutputLCS(Backtrack, v, w):
    LCS = str()
    i = len(v)
    j = len(w)
   
    if i >= j:
        while i > 0 and j > 0:
            #print ("i: ", i, "j: ", j)
        #print ("Backtrack[", i, "][", j, "]: ", Backtrack[i][j])
        #print ("w[", j-1, "]: ", w[j-1])
            if Backtrack[i][j] == "↘":
                #print (i, j, Backtrack[i][j])
                LCS += w[j-1]
                i -= 1
                j -= 1
                print ("dig__i: ", i, "j: ", j)
            elif Backtrack[i][j] == "↓":
                #print (i, j, Backtrack[i][j])
                LCS += "-"
                i -= 1
                print ("up__i: ", i, "j: ", j)
            elif Backtrack[i][j] == "→":
                #print (i, j, Backtrack[i][j])
                LCS += "-"
                j -= 1
                print ("left__i: ", i, "j: ", j)
        if i != 0:
            LCS += "-"
    else:
        while i > 0 and j > 0:
        #print ("i: ", i, "j: ", j)
        #print ("Backtrack[", i, "][", j, "]: ", Backtrack[i][j])
        #print ("w[", j-1, "]: ", w[j-1])
            if Backtrack[i][j] == "↘":
                LCS += v[i-1]
                i -= 1
                j -= 1
                
            elif Backtrack[i][j] == "↓":
                LCS += "-"
                i -= 1
                
            elif Backtrack[i][j] == "→":
                LCS += "-"
                j -= 1
                
        if i != 0:
            LCS += "-"
    return reverse(LCS)

def reverse(string): 
    string = string[::-1]
    return string


# m: number of rows, n: number of columns
def create_matrix(m, n):
    return [[0]*n for _ in range(m)]

        
def LCSBackTrack(S, v, w):
    i = len(v)
    j = len(w)
    print (blosom[str(v[1])][str(w[1])])
    #while i > 0 and j > 0:
        #print (blosom[i][j])
     #   i -= 1
      #  j -= 1
     #   score_current = S[i][j]
      #  score_diagonal = S[i-1][j-1]
       # score_up = S[i][j-1]
        #score_left = S[i-1][j]
        # Check to figure out which cell the current score was calculated from,
        # then update i and j to correspond to that cell.
        #if score_current == score_diagonal + blosom[j-1][i-1]:
         #   align1 += v
    #Backtrack = create_matrix(len(matrix[0])+1, len(matrix[1])+1)
    #Backtrack = [["~" for x in range(len(matrix[1])+1)] for y in range(len(matrix[0])+1)]
    #for i in range(len(S[1])-1):
     #   for j in range(len(S)-1):
            
      #      if S[j+1][i+1] == S[j+1][i] + delta:
       #         Backtrack[j+1][i+1] = "→"
        #    elif S[j+1][i+1] == S[j][i+1] + delta:
         #       Backtrack[j+1][i+1] = "↓"
          #  elif S[j+1][i+1] == max(S[j][i+1] + delta, S[j+1][i] + delta, S[j][i] + blosom[matrix[0][j]][matrix[1][i]]):
            #max(S[j][i+1] + delta, S[j+1][i] + delta, S[j][i] + blosom[matrix[0][j]][matrix[1][i]]) == S[j][i] + blosom[matrix[0][j]][matrix[1][i]]:
           #     Backtrack[j+1][i+1] = "↘"
            
    return Backtrack

def match_score(alpha, beta):
    return blosom[alpha][beta]

def GlobalAlignment(v, w, delta):
    n = len(v)
    m = len(w)
    S = create_matrix(m+1, n+1)
    # Fill out first column
    for i in range(0, m+1):
        S[i][0] = delta * i
    
    # Fill out first row
    for j in range(0, n+1):
        S[0][j] = delta * j
    # Fill out all other values in the score matrix
    for i in range(1, m+1):
        for j in range(1, n+1):
            # Calculate the score by checking the top, left, and diagonal cells
            match_mismatch = S[i-1][j-1] + match_score(v[j-1], w[i-1]) 
            delete = S[i-1][j] + delta
            insert = S[i][j-1] + delta
            # Record the maximum score from the three possible
            S[i][j] = max(match_mismatch, delete, insert)
    
    # Create variables to store alignment
    align1 = ""
    #align2 = ""
    
    # Start from the bottom right cell in matrix
    #j is longer 
    i = m
    j = n
    
    # i and j to keep track of where we are in the matrix
    while i > 0 and j > 0:
        score_current = S[i][j]
        score_diagonal = S[i-1][j-1]
        score_left = S[i][j-1]
        score_up = S[i-1][j]
      
        #print ("score_current: ", score_current)
        #print (score_left)
        #j -= 1
        # Check to figure out which cell the current score was calculated from 
        # then update i and j to correspond to that cell.
        if score_current == score_diagonal + match_score(v[i-1], w[i-1]):
            print (v[j-1], w[i-1])
         #   print (score_current, score_diagonal, match_score(v[j-1], w[i-1]))
         #   align1 += w[i-1]
            #print (align1)
            #align2 += w[i-1]
            i -= 1
            j -= 1
        elif score_current == score_up + delta:
            print (score_current, "score_up: ", score_up)
           # print (score_up)
         #   print ("G")
          #  print (score_current, score_up)
         #   align1 += '-'
            #align2 += '-'
            i -= 1
        elif score_current == score_left + delta:
            print (score_current, "score_left: ", score_left)
         #   align1 += '-'
            #align2 += w[j-1]
            j -= 1
        # Finish tracing up to the top left cell
        #while j > 0:
          #  align1 += v[j-1]
         #   align1 += '-'
          #  j -= 1
        #while i > 0:
         #   align1 += '-'
         #   align2 += w[i-1]
          #  i -= 1
        # Since we traversed the score matrix from the bottom right, our two sequences will be reversed.
        # These two lines reverse the order of the characters in each sequence.
        #align1 = align1[::-1]
        #align2 = align2[::-1]    

           
    return (S)

# indels are penalties of -5
delta = -5

a = open('test.txt').read()

with open('test.txt') as f:
    lines = [line.rstrip() for line in f]
v = lines[0]
w = lines[1]
S = GlobalAlignment(v, w, delta)
#print (output1)
#print (S[len(v)][len(w)])
#for item in S:
 #   print (item)
#print (S[10][0])
Backtrack = LCSBackTrack(S, v, w)
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