from collections import deque

def max_sliding_window_naive(sequence, m):
    maximums = []
    q = deque()
    
    for i in range(len(sequence)):
#        print("i: ", i)
 #       print("q before: ", q)
        while q and sequence[i] >= sequence[q[-1]]:
            q.pop()
        q.append(i)
        
  #      print("q after: ", q)
        if i >= m and q and q[0] <= i - m:
            q.popleft()
        if i >= m - 1:
            maximums.append(sequence[q[0]])
   #     print("after all: ", q)
    #    print("maximums: ", maximums)

    return maximums

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    #print("test: ", collections.deque(itertools.islice(input_sequence, 0, 4)))
    print(*max_sliding_window_naive(input_sequence, window_size))

