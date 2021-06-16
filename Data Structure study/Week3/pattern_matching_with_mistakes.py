import sys
from collections import deque



def HashTable(string, prime, x):
    hash_table = [[] for _ in range(len(string) + 1)]
    hash_table[0] = 0
    for i in range(1, len(string) + 1):
        hash_table[i] = (hash_table[i-1] * x + ord(string[i - 1])) % prime
    
    return hash_table


def HashValue(hash_table, prime, x, start, length):
    y = pow(x, length, prime)
    hash_value = (hash_table[start + length] - y * hash_table[start]) % prime
    return hash_value

def PreCompute(text, pattern):
    global m, x
    h_t = HashTable(text, m, x)
    h_p = HashTable(pattern, m, x)
    print("h_text: ", h_t)
    print("h_ptn: ", h_p)
    return h_t, h_p

def CheckMatch(start, length, p_len, k):
    global m, h_t, h_p
    stack = deque()
    stack.append((start, 0, length, 1))
    stack.append((start + length, length, p_len - length, 1))
    count = 0
    temp = 2
    C = 0
    print("--------------------------------before while: ", stack)
    while stack:
        a, b, L, n = stack.popleft()
        print("a, b, L, n: ", a, b, L, n)
        u1 = HashValue(h_t, m, x, a, L)
        v1 = HashValue(h_p, m, x, b, L)
        print("u1, v1: ", u1, v1)
     
        if temp != n:
            count = C
        if u1 != v1:
            count += 1
            if L > 1:
                stack.append((a, b, L//2, n + 1))
                stack.append((a + L//2, b + L//2, L - L//2, n + 1))
                print("after L > 1 ", stack)
            else:
                C += 1
            print("count: ", count)
        
        if count > k:
            return False
        temp = n
    if count > k:
        return False
    else:
        return True


m = 1000000007
x = 263

global h_t, h_p
h_t, h_p = PreCompute("testtest", "teste")

for i in range(8 - 5 + 1):
    CheckMatch(i, 5 // 2, 5, 4)
