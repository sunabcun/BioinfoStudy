from collections import namedtuple
from collections import deque

Request = namedtuple("Request", ["arrived_at", "time_to_process"])
Response = namedtuple("Response", ["was_dropped", "started_at"])


class Buffer:
    def __init__(self, size):
        self.size = size
        self.finish_time = []


def process_requests(requests, buffer):
    bq = deque(maxlen = buffer.size)
    
    start_times = [None] * len(requests)
    
    for i, request in enumerate(requests):
        #print(i)
        while bq and bq[0] <= request.arrived_at:
            bq.popleft()
        if len(bq) >= buffer.size:
            #Buffer overrun
            start_times[i] = -1
        else:
            
            start_times[i] = max(request.arrived_at, bq[-1] if bq else 0)
            
            bq.append(start_times[i] + request.time_to_process)
            
    return start_times
        #print("i: ", i)
        
        #print(bq)
        #print(start_times)
        
       
    
    
    
    #responses = []
    #for request in requests:
    #    responses.append(buffer.process(request))
    


def main():
    #print("yo insert buffer sizes and # packets yo:")
    buffer_size, n_requests = map(int, input().split())
    
    requests = []
    #print("yo insert packets:")
    for _ in range(n_requests):
        arrived_at, time_to_process = map(int, input().split())
        requests.append(Request(arrived_at, time_to_process))
    
    buffer = Buffer(buffer_size)
    #print("requests: ", requests)
    #print("buffer: ", buffer)
    responses = process_requests(requests, buffer)
    for response in responses:
        print(response)
    #for response in responses:
     #   print(response.started_at if not response.was_dropped else -1)


if __name__ == "__main__":
    main()
