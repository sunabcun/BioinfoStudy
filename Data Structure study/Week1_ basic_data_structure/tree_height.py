import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
    def height(self, node):
        print("node: ", node)
        print("before calling self.heights: ", self.heights)
        if node == -1:
            return 0
        print("self.parent[node]", self.parent[node])
        if self.parent[node] in self.heights:
            print("YES")
            self.heights[node] = self.heights[self.parent[node]] + 1
        else:
            
            self.heights[node] = self.height(self.parent[node]) + 1
            
        print("self.heights: ", self.heights)
        return self.heights[node]

    def read(self):
       
        self.n =  int(input())
        self.parent = list(map(int, input().split()))
        self.heights = {}

    def compute_height(self):
        maxHeight = 0
        for vertex in range(self.n):
            print("vertex: ", vertex)
            maxHeight = max(maxHeight, self.height(vertex))
            
            print("maxHeight: ", maxHeight)
            
        return maxHeight;

def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())


if __name__ == "__main__":
    main()


threading.Thread(target=main).start()