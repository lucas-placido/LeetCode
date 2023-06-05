from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:                   
        i = 0
        n = len(height) -1
        max_capacity = 0        
        while i <= n:
            capacity = min(height[i], height[n]) * (n - i)
            max_capacity = max(max_capacity, capacity)                        
            if height[i] < height[n]:
                i += 1
            else:
                n -= 1            
        return max_capacity
    
height = [1,8,6,2,5,4,8,3,7]
output = Solution().maxArea(height)
print(output)    