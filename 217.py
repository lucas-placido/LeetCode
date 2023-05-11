from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
nums = [1, 2, 3, 3]
s = Solution()
output = s.containsDuplicate(nums)
print(output)