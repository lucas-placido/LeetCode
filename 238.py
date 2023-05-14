from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:                
        answer = [1 for i in range(len(nums))]
        val = 1
        for i in range(len(nums)):                                    
            if i == 0:
                pass
            else:
                answer[i] = nums[i-1] * answer[i-1]
                
        for i in range(-1, -1 -len(nums), -1):            
            if i == -1:
                pass
            else:                
                val *= nums[i + 1]
                answer[i] *= val                        

        return answer
    
nums = [1,2,3,4]    
s = Solution()
result = s.productExceptSelf(nums)
print(result)