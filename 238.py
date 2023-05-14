from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:                
        answer = [1] * len(nums)
        val = 1
        for i in range(1, len(nums)):                                                
            answer[i] = nums[i-1] * answer[i-1]
                
        for i in range(-2, -1 -len(nums), -1):                           
            val *= nums[i + 1]
            answer[i] *= val                        
        return answer
    
nums = [1,2,3,4]    
s = Solution()
result = s.productExceptSelf(nums)
print(result)