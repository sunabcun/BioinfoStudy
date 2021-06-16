import math
import sys, threading

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size
class Node:
    def __init__(self, a, b, c):
        self.key = a
        self.left = b
        self.right = c

def isBinary(nodes):
    # set -inf: min, inf: max, nodes[0]: 1st tree
    stack = [(-math.inf, nodes[0], math.inf)]
    while stack:
        min, root, max = stack.pop()
        #print(min, root.key, max)
        if root.key >= max or root.key < min:
         #   print("root.key: ", root.key, ">=" " max: ", max, " or ", "<", " min: ", min)
            return False

        if root.left != -1:
            stack.append((min, nodes[root.left], root.key))
        #else:
         #   print("no left subtree")
        #print("after left: ", stack)
        if root.right != -1:
            stack.append((root.key, nodes[root.right], max))
       # else:
         #   print("no right subtree")
        #print("after right: ", stack)
    return True




def main():
    n_nodes = int(input())
    nodes = [0 for _ in range(n_nodes)]

    if n_nodes != 0:
        for i in range(n_nodes):
            a, b, c = map(int, input().split())
            node = Node(a, b, c)
            nodes[i] = node

    if n_nodes == 0 or isBinary(nodes):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()
#if __name__ == '__main__':
 #   main()
