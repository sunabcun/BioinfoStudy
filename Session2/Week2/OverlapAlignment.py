def reverse(string): 
    string = string[::-1]
    return string

# m: number of rows, n: number of columns
def create_matrix(m, n):
    return [[0]*n for _ in range(m)]

def calAlignment(A, B, L, oploc):
    # Retrieve the location of highest score
    i, j = oploc
    
    # Final strings
    FinalA = ""
    FinalB = ""
    # Check the alignment
    while i > 0:
        if L[i][j] == 1:
            FinalA += A[j-1]
            FinalB += B[i-1]
            i -= 1
            j -= 1
        else:
            if L[i][j] == 2:
                FinalA += A[j-1]
                FinalB += '-'
                j -= 1
            else:
                FinalA += '-'
                FinalB += B[i-1]
                i -= 1
                
                
    return reverse(FinalA), reverse(FinalB)

def FindMaxScore(A, B, costs):
    # To track the best score
    best = 0
    # To track optimal local alignment
    optloc = (0, 0)
    # Create F matrix for scoring
    F = create_matrix(len(B) + 1, len(A) + 1)
    # Create L matrix for locating
    L = create_matrix(len(B) + 1, len(A) + 1)
    
    match, mismatch, gap = costs
    mismatch = -mismatch
    gap = -gap
    
    # Fill the F matrix with indel penalty
    for i in range(len(B) + 1):
        F[i][0] = gap*i
    
    # Fill in matrix F, L in the right order
    for i in range(1, len(B)+1):
        for j in range(1, len(A)+1):
            if B[i-1] == A[j-1]:
                cost = match
            else:
                cost = mismatch
            #print (i, j, F[i-1][j-1] + cost, F[i][j-1] + gap, F[i-1][j] + gap)
            Maxscore = max(F[i-1][j-1] + cost, F[i][j-1] + gap, F[i-1][j] + gap)
            F[i][j] = Maxscore
            # Max score in bottom row of the shorter string
            if F[i][-1] > best:
                best = F[i][-1]
                optloc = (i, j)
            
            #Set L matrix
            if Maxscore == F[i-1][j-1] + cost:
                L[i][j] = 1 #1 == "Diagonal"
            elif Maxscore == F[i][j-1] + gap:
                L[i][j] = 2 #2 == "Left, B gap"
            else:
                L[i][j] = 3 #3 == "Up, A gap"
    for item in F:
        print (item)
    # Return the opt score and the best location
    return L, best, optloc

a = open('test.txt').read()

with open('test.txt') as f:
    lines = [line.rstrip() for line in f]
# v: first string, w: second string
A = lines[1]
B = lines[2]
num = lines[0]
costs = []

# Get score information and transform it as a tuple.
for item in num:
    if item is not " ":
        costs.append(int(item))
costs = tuple(costs)

L, best, oploc = FindMaxScore(A, B, costs)
print (best, oploc)
FinalA, FinalB, = calAlignment(A, B, L, oploc)
print (FinalA)
print (FinalB)
