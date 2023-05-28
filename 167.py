from typing import List

from sympy import I

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left + 1, right + 1]                
            elif current_sum > target:
                right -= 1
            else:
                left += 1
        return 
    
numbers = [2,7,11,15]
target = 9
result = Solution().twoSum(numbers, target)
print(result)