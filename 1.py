from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Finds the indices of the two numbers in the nums list that add up to the target value.

        Parameters:
        nums (list): A list of integers.
        target (int): The target sum.

        Returns:
        list: A list of two integers representing the indices of the two numbers in the nums list that add up to the target value.

        Example:
        --------
        >>> s = Solution()
        >>> nums = [2, 7, 11, 15]
        >>> target = 9
        >>> s.twoSum(nums, target)
        [0, 1]
        '''
        
        for x in range(len(nums)):
            find = target - nums[x]            
            if find in nums:
                if nums.index(find) != x:                
                    return list([x, nums.index(find)])
                      
nums = [2,5,5,11]
target = 10

s = Solution()
print(s.twoSum(nums=nums, target=target))