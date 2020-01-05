import time
start = time.time()

from itertools import islice
from collections import deque
from collections import Counter

def sliding_window(seq, n):
    "Returns a sliding window (of width n) over data from the iterable"
    "   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   "
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

def get_clumps(genome, k, L, t):
    kmers = KmerSequence(L-k, t)

    for kmer in sliding_window(genome, k):
        kmers.add(kmer)
    return kmers.clumps

class KmerSequence(object):
    __slots__ = ['order', 'counts', 'limit', 'clumps', 't']

    def __init__(self, limit, threshold):
        self.order = deque()
        self.counts = Counter()
        self.limit = limit
        self.clumps = set()
        self.t = threshold

    def add(self, kmer):
        if len(self.order) > self.limit:
            self._remove_oldest()
        self._add_one(kmer)

    def _add_one(self,kmer):
        self.order.append(kmer)
        new_count = self.counts[kmer] + 1
        self.counts[kmer] = new_count

        if new_count == self.t:
            self.clumps.add(kmer)

    def _remove_oldest(self):
        self.counts[self.order.popleft()] -= 1
        
with open("input.txt") as f:
    genome = f.read()

k = 9
L = 500
t = 3

clumps = get_clumps(genome, k,L,t)
print (type(clumps))
end = time.time()
print(end-start)