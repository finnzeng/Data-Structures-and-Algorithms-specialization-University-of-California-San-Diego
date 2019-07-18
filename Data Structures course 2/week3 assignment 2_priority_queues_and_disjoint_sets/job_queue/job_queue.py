# python3

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.array = [[0]*2 for i in range(self.num_workers)]
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)
        self.workers = [None] * len(self.jobs)
        self.start = [0] * len(self.jobs)

    def initialize(self):
        worker = 0
        for i in range(min(self.num_workers,len(self.jobs))):
            self.array[i] = [self.jobs[i],i]
            self.workers[i] = worker
            worker+=1
            self.start[i] = 0
        for i in range(self.num_workers//2, -1,-1):
            self.swapdown(i)
            
    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.workers[i], self.start[i]) 
    
    def swapdown(self,i):
        min_index = i
        l = 2*i+1 if (2*i+1<self.num_workers) else -1 
        r = 2*i+2 if (2*i+2<self.num_workers) else -1 
        if (l != -1) and ((self.array[l][0] < self.array[min_index][0]) or ((self.array[l][0] == self.array[min_index][0]) and self.array[l][1] < self.array[min_index][1] )):
            min_index = l
        if (r != -1) and ((self.array[r][0] < self.array[min_index][0]) or ((self.array[r][0] == self.array[min_index][0]) and (self.array[r][1] < self.array[min_index][1]))):
            min_index = r
        if i != min_index:
            self.array[i], self.array[min_index] = \
                self.array[min_index], self.array[i]
            self.swapdown(min_index)
            
    def sorttheheap(self):
        for i in range(self.num_workers//2, -1,-1):
            self.swapdown(i)
               
            
    def assign_jobs(self):
        self.initialize()
        lasttime = 0
        if len(self.jobs)>self.num_workers:
            for i in range(self.num_workers,len(self.jobs)):
#                 print(1,self.array)
                self.swapdown(0) #don't need to sort here only swapping would do
#                 print(2,self.array)
                lasttime =self.array[0][0]
    #             if self.array[0][0]!=self.array[1][0]:
                self.workers[i] = self.array[0][1]
                self.start[i] = lasttime
    #             elif self.array[0][0] ==self.array[1][0]:
    #                 temp=0
    #             print(self.array)
                self.array[0][0] += self.jobs[i]
        

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()