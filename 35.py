from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2                  
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return left                                            
    
nums = [1, 3, 5, 6]
target = 2

s = Solution()
result = s.searchInsert(nums, target)
print(result)