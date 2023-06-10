from collections import defaultdict, deque
import heapq
from typing import Counter, List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hash = {u: tasks.count(u) for u in tasks}
        maxHeap = [-x for x in hash.values()]
        heapq.heapify(maxHeap)

        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:                
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
    
tasks = ["A","A","A","B","B","B"]
n = 2
result = Solution().leastInterval(tasks, n)
print(result)

