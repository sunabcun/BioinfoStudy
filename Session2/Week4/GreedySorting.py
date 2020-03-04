def GreedySorting(P):
    def format(P):
        def f(p):
            return str(p) if p < 0 else '+' + str(p)
        return ' '.join(f(p) for p in P)
    reversalDistance = 0
    for k in range(1, len(P)+1):
        #print("I pass first loop")
        if k != P[k-1]:
            #print("not matched", "k:", k, "P[",k-1,"]:", P[k-1])
            pos = P.index(k if k in P else -k)
            P = reverseArrayUptoK(P, k-1,pos+1)
            reversalDistance += 1
            print(format(P), file=open("output.txt", "a"))
            if P[k-1] == -k:
                P[k-1] = k
                reversalDistance += 1
                print(format(P), file=open("output.txt", "a"))
            
    return reversalDistance
 

# Program to Reverse an array  
# upto a given position  
def reverseArrayUptoK(input,start, pos):
    for i in range(start, pos):
        input[i] = -input[i]
    middle = input[start:pos]
    return (input[:start] + middle[::-1] + input[pos:])


with open('test.txt') as f:
    lines = [line.rstrip() for line in f]
numList = lines[0].split()

# Change the str list to int list 
for i in range(len(numList)):
    numList[i] = int(numList[i])      
            
Result = GreedySorting(numList)
print(Result)