from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Modifies a list of integers by moving all unique elements to the beginning and returning the number of unique elements.        
        
        Args:
        - nums: a list of integers with duplicates
        
        Returns:
        - an integer representing the number of unique elements in the modified list
        
        Example:
        s = Solution()
        nums = [1, 2, 2, 3, 4, 4, 4, 5]
        result = s.removeDuplicates(nums)
        print(nums)  # prints [1, 2, 3, 4, 5, 4, 4, 5]
        print(result)  # prints 5
        """

        if not nums:
            return 0

        # use two pointers to keep track of unique elements
        start = 0
        for end in range(len(nums)):            
            if nums[end] != nums[start]:                
                start += 1
                nums[start] = nums[end]        
        print(nums)
        return start + 1
    
nums = [1, 2, 2, 3, 4, 4, 4, 5]

s = Solution()
result = s.removeDuplicates(nums)
print(result)