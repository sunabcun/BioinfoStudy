from heapq import *


class A:
    def __init__(self, val):
        self.val = val

    def __lt__(self, cmp):
        """Overwrite this to do the opposite of what's
        expected"""
        return self.val >= cmp.val


h = []
heappush(h, A(1))
heappush(h, A(2))
heappush(h, A(0))

print(heappop(h).val)