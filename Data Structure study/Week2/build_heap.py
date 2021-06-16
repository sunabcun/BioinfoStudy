class heap:
    def __init__(self):
        self.swaps = []
        self.data = []
    
    def Read(self):
        n = int(input())
        self.data = list(map(int, input().split()))
        assert len(self.data) == n
        
    def Output(self):
        print(len(self.swaps))
        for swap in self.swaps:
            print(swap[0], swap[1])
            
    def HeapSwap(self):
        for i in range(len(self.data)//2, -1, -1):
            self.sift_down(i)
    
    def sift_down(self, i):
        minIndex = i
        l = 2*i + 1
        if l < len(self.data) and self.data[l] < self.data[minIndex]:
            minIndex = l
        
        r = 2*i + 2
        if r < len(self.data) and self.data[r] < self.data[minIndex]:
            minIndex = r
        
        if i != minIndex:
            self.swaps.append((i, minIndex))
            self.data[i], self.data[minIndex] = self.data[minIndex], self.data[i]
            self.sift_down(minIndex)
    
    def Solve(self):
        self.Read()
        self.HeapSwap()
        self.Output()
 
        
    

def main():
   heap_build = heap()
   heap_build.Solve()

  
