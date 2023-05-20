from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        if not nums:
            return
        major = nums[0]
        for num in nums:
            hash[num] = hash.get(num, 0) + 1
            if hash[num] > hash[major]:
                major = num        
        return major
    
nums = [6,5,5]    
result = Solution().majorityElement(nums)
print(result)