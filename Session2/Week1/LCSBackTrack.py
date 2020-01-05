def IterativeOutputLCS(Backtrack, v, w):
    LCS = str()
    i = len(v)
    j = len(w)
    while i > 0 and j > 0:
        if Backtrack[i][j] == "↘":
            LCS += v[i-1]
            i -= 1
            j -= 1
        elif Backtrack[i][j] == "↓":
            i -= 1
        else:
            j -= 1
        #print ("i: ", i, "j: ", j, "Backtrack: ", Backtrack)
    return reverse(LCS)

def reverse(string): 
    string = string[::-1]
    return string

def LCSBackTrack(v, w):
    # Make mxn matrix initiating 0
    s = [["*" for x in range(len(w)+1)] for y in range(len(v)+1)]
    Backtrack = [["*" for x in range(len(w)+1)] for y in range(len(v)+1)]
   
    for i in range(len(v)+1):
        s[i][0] = 0
    
    for j in range(len(w)+1):
        s[0][j] = 0
    
    for i in range(1, len(v)+1):
        for j in range(1, len(w)+1):
            match = 0
            if v[i-1] == w[j-1]:
                match = 1
            s[i][j] = max(s[i-1][j], s[i][j-1], s[i-1][j-1] + match)
            if s[i][j] == s[i-1][j]:
                Backtrack[i][j] = "↓"
            elif s[i][j] == s[i][j-1]:
                Backtrack[i][j] = "→"
            elif s[i][j] == s[i-1][j-1] + match:
                Backtrack[i][j] = "↘"
    return Backtrack

with open('test.txt') as f:
    lines = [line.rstrip() for line in f]
v = lines[0]
w = lines[1]
Backtrack = LCSBackTrack(v, w)
print (Backtrack)
print(IterativeOutputLCS(Backtrack, v, w))
