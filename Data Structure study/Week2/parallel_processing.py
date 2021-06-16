from collections import namedtuple
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])

class Worker:
    def __init__(self, job_id, s_time = 0):
        self.job_id = job_id
        self.s_time = s_time
    
    def __lt__(self, other):
       # print(self.job_id, self.s_time, other.job_id, other.s_time, "lt called")
        if self.s_time == other.s_time:
            return self.job_id < other.job_id
        
        return self.s_time < other.s_time
    
    def __gt__(self, other):
        #print("gt called")
        if self.s_time == other.s_time:
            return self.job_id > other.job_id
        return self.s_time > other.s_time

class Heapque:
    
    def Read(self):        
        self.n_workers, n_jobs = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert len(self.jobs) == n_jobs
        
    def Output(self):
        for job_id, s_time in self.result:
            print(job_id, s_time)
            
    def Assign(self):
        self.result = []
        self.Work_q = [Worker(i) for i in range(self.n_workers)]
        #for work in self.Work_q:
        #    print(work.job_id, work.s_time)
        
        for job in self.jobs:
            worker = heapq.heappop(self.Work_q)
            self.result.append((worker.job_id, worker.s_time))
            
            worker.s_time += job
         #   print("before Work_q")
          #  for work in self.Work_q:
           #     print(work.job_id, work.s_time)
            heapq.heappush(self.Work_q, worker)
           # print("After Work_q")
           # for work in self.Work_q:
            #    print(work.job_id, work.s_time)
        
        
        
    
    def Solve(self):
        self.Read()
        self.Assign()
        self.Output()
 
        
    

def main():
   heap_build = Heapque()
   heap_build.Solve()

  


if __name__ == "__main__":
    main()
