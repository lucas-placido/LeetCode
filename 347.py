from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}        
        for i in range(len(nums)):
            hash[nums[i]] = 1 + hash.get(nums[i], 0)            
        values = sorted(hash.values(), reverse=True)[:k]        
        result = [k for k in hash if hash[k] in values]
        return result
    
nums = [1,1,1,2,2,3]
k = 2    

s = Solution()
result = s.topKFrequent(nums, k)
print(result)