class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count =Counter(tasks)
        maxheap = [-x for x in count.values()]
        heapq.heapify(maxheap)
        q = deque()
        time =0

        while maxheap or q:
            time+=1
            if maxheap:
                h = 1+heapq.heappop(maxheap)
                if h:
                    q.append([h, time +n])
            if q and q[0][1]==time:
                heapq.heappush(maxheap,q.popleft()[0])
        return time

        