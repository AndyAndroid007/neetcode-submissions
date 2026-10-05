class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        h = [(-freq,task) for task,freq in count.items()]
        heapq.heapify(h)
        q = deque()
        time = 0  
        while h or q:

            while q and q[0][2] <= time:
                ta,f,t = q.popleft()
                heapq.heappush(h,(-f, ta))
            if h:
                freq,task = heapq.heappop(h)
                rem = -(freq) - 1
                if rem > 0:
                    q.append((task, rem, time + n + 1))
                
                time += 1

            else:
                time = q[0][2]

        return time






        
        
        