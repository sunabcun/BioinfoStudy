import sys, threading
import math


# sys.setrecursionlimit(10**8) # max depth of recursion
# threading.stack_size(2**27)  # new thread will get stack of such size

class Node:
    def __init__(self, a, b, c):
        self.root = a
        self.left = b
        self.right = c


def main():
    n_nodes = int(input())
    nodes = [0 for _ in range(n_nodes)]
    for i in range(n_nodes):
        a, b, c = map(int, input().split())
        node = Node(a, b, c)
        nodes[i] = node
    print(nodes)
    print("run")

# threading.Thread(target=main).start()
