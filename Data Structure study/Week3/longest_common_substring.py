def PolyHash(pattern, prime, multiplier):
    hash = 0
    for s in reversed(pattern):
        hash = (hash * multiplier + ord(s)) % prime
    return hash

def HashTable(short, p_len, prime, multiplier):
    H = [[] for _ in range(len(short) - p_len + 1)]
    substring = short[len(short) - p_len:]
    H[len(short) - p_len] = PolyHash(substring, prime, multiplier)
    
    y = pow(multiplier, p_len, prime)
    for i in range(len(short) - p_len - 1, -1, -1):
        H[i] = (multiplier * H[i + 1] + ord(short[i]) - y * ord(short[i + p_len])) % prime
   # print("HashTable:", H)
    return H

def HashDict(short, p_len, prime, multiplier):
    D = {}
    substring = short[len(short) - p_len:]
    last = PolyHash(substring, prime, multiplier)
    D[last] = len(short) - p_len
    
    y = pow(multiplier, p_len, prime)
    for j in range(len(short) - p_len -1, -1, -1):
        #print(j)
        current = (multiplier * last + ord(short[j]) - y * ord(short[j + p_len])) % prime
        D[current] = j
        last = current
    #print("HashDict: ", D)
    return D

def SearchSubstring(hash_table, hash_dict):
    check = False
    matches = {}
    for i in range(len(hash_table)):
        short_start = hash_dict.get(hash_table[i], -1)
        if short_start != -1:
            check = True
            matches[i] = short_start
     #       print(check, matches)
    return check, matches
        

def MaxLength(string_long, string_short, low, high, max_length, long_start, short_start):
    # long string=hash table, short string = hash dict
    mid = (low + high) // 2
    if low > high:
        return long_start, short_start, max_length
    prime1 = 1000000007
    prime2 = 1000004249
    x = 263
    lHash1 = HashTable(string_long, mid, prime1, x)
    lHash2 = HashTable(string_long, mid, prime2, x)
    sHash1 = HashDict(string_short, mid, prime1, x)
    sHash2 = HashDict(string_short, mid, prime2, x)
    check1, matches1 = SearchSubstring(lHash1, sHash1)
    check2, matches2 = SearchSubstring(lHash2, sHash2)
    if check1 and check2:
        for a, b in matches1.items():
            temp = matches2.get(a, -1)
            if temp != -1:
                max_length = mid
                long_start, short_start = a, b
                del lHash1, lHash2, sHash1, sHash2, matches1, matches2
                return MaxLength(string_long, string_short, mid + 1, high, max_length, long_start, short_start)
    return MaxLength(string_long, string_short, low, mid -1, max_length, long_start, short_start)
    

while True:
    line = input()
    if line == "":
        break
    else:
        s, t = line.split()
        k = min(len(s), len(t))
        if len(s) <= len(t):
            short_string, long_string = s, t
        else:
            short_string, long_string = t, s
        l, i, j = MaxLength(long_string, short_string, 0, k, 0, 0, 0)
        if len(s) <= len(t):
            print(i, l, j)
        else:
            print(l, i, j)
