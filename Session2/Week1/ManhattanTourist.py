def ManhattanTourist(n, m, Down, Right):
    # Make mxn matrix initiating 0
    s = [[0 for x in range(m+1)] for y in range(n+1)]
    #print (30 + Down[4][0])
    for i in range(1, n+1):
        s[i][0] = s[i-1][0] + Down[i-1][0]
        #print ("s[",i,"][0]: ", s[i][0])
    for j in range(1, m+1):
        s[0][j] = s[0][j-1] + Right[0][j-1]
        #print ("s[0][",j,"]: ", s[0][j])
    for i in range(1, n+1):
        for j in range(1, m+1):
            s[i][j] = max(s[i-1][j] + Down[i-1][j],s[i][j-1] + Right[i][j-1])
    return s[n][m]


with open('test4.txt') as f:
    lines = [line.rstrip() for line in f]
string = lines[0]
string2 = string.split(" ")
# Assign the int for making a matrix
n = int(string2[0])
m = int(string2[1])
# Get array for Down matrix
Down = []
for i in range(n):
    Down.append(lines[i+1].split(" "))
    # Change the str list to int list
    for j in range(len(Down[i])):
        Down[i][j] = int(Down[i][j])

# Get array for Right matrix
Right = []
for i in range(n+1):
    Right.append(lines[i+n+2].split(" "))
    # Change the str list to int list
    for j in range(len(Right[i])):
        Right[i][j] = int(Right[i][j])

print (ManhattanTourist(n, m, Down, Right))