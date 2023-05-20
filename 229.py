from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return
        hash = {}
        majority = set()
        for num in nums:
            hash[num] = hash.get(num, 0) + 1
            if hash[num] > len(nums) // 3:
                majority.add(num)
        return list(majority)
    
nums = [1,2]
result = Solution().majorityElement(nums)
print(result)    