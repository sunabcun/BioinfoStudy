def FindHighestScoringMultipleSequenceAlignment (u,
                                                 v,
                                                 w,
                                                 score=lambda x,y,z: 1 if x==y and y==z and x!='-' else 0):
    def build_matrix():
        s = [[[0 for i in range(len(w)+1)] for j in range(len(v)+1)] for k in range(len(u)+1) ]
        path = {}
                  
        for i in range(1,len(u)+1):
            for j in range(1,len(v)+1):
                for k in range(1,len(w)+1):
                    scores     = [
                        s[i-1][j-1][k-1] + score(u[i-1], v[j-1], w[k-1]),
                        s[i-1][j][k]     + score(u[i-1], '-',    '-'),
                        s[i][j-1][k]     + score('-',    v[j-1], '-'),
                        s[i][j][k-1]     + score('-',    '-',    w[k-1]),
                        s[i][j-1][k-1]   + score('-',    v[j-1], w[k-1]),
                        s[i-1][j][k-1]   + score(u[i-1], '-',    w[k-1]),
                        s[i-1][j-1][k]   + score(u[i-1], v[j-1], '-'),
     
                    ]
                    moves = [
                        (-1, -1, -1),
                        (-1,  0,  0),
                        ( 0, -1,  0),
                        ( 0,  0, -1),
                        ( 0, -1, -1),
                        (-1,  0, -1),
                        (-1, -1,  0),
     
                    ]
                    index          = argmax(scores)
                    s[i][j][k]     = scores[index]
                    path[(i,j,k)] = moves[index]
        return s,path
    
    def backtrack(path):
        i  = len(u)
        j  = len(v)
        k  = len(w)
        u1 = []
        v1 = []
        w1 = []
        while i>0 and j>0 and k>0:
            di,dj,dk = path[(i,j,k)]
            i        += di
            j        += dj
            k        += dk
            if dj==0 and dk==0:
                u1.append(u[i])
                v1.append('-')
                w1.append('-')
            elif di==0 and dk==0:
                u1.append('-')
                v1.append(v[j])
                w1.append('-')
            elif di==0 and dj==0:
                u1.append('-')
                v1.append('-')
                w1.append(w[k])
            elif di==0:
                u1.append('-')
                v1.append(v[j])
                w1.append(w[k])
            elif dj==0:
                u1.append(u[i])
                v1.append('-')
                w1.append(w[k])
            elif dk==0:
                u1.append(u[i])
                v1.append(v[j])
                w1.append('-')
            else:
                u1.append(u[i])
                v1.append(v[j])
                w1.append(w[k])        
        while i>0:
            i-=1
            u1.append(u[i])
            v1.append('-')
            w1.append('-')
        while j>0:
            j-=1
            u1.append('-')
            v1.append(v[j])
            w1.append('-')
        while k>0:
            k-=1
            u1.append('-')
            v1.append('-')
            w1.append(w[k])
        return u1,v1,w1
    
    s,path   = build_matrix()
    u1,v1,w1 = backtrack(path)
    
    return s[len(u)][len(v)][len(w)],''.join(u1[::-1]),''.join(v1[::-1]),''.join(w1[::-1])

with open('test.txt') as f:
    lines = [line.rstrip() for line in f]

word1 = lines[0]
word2 = lines[1]
word3 = lines[2]

s, u, v, w = FindHighestScoringMultipleSequenceAlignment(word1, word2, word3)
print (s)
print(u)
print(v)
print(w)