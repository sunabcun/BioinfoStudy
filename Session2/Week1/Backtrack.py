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
 
v = "ATAT"
w = "ACT"

print (LCSBackTrack(v, w))