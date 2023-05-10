from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        n = len(nums) -1
        while i <= n:                        
            if nums[i] == val:
                nums[i], nums[n] = nums[n], 0
                n -= 1
            else:
                i += 1        
        print(nums)
        return n + 1
    
nums = [3,2,2,3]
val = 3

s = Solution()
result = s.removeElement(nums = nums, val = val)
print(result)
               
