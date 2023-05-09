from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Modifies a list of integers by moving all unique elements to the beginning and returning the number of unique elements.
        Duplicates are moved to the end of the list without any particular order.
        
        Args:
        - nums: a list of integers with duplicates
        
        Returns:
        - an integer representing the number of unique elements in the modified list
        
        Example:
        s = Solution()
        nums = [1, 2, 2, 3, 4, 4, 4, 5]
        result = s.removeDuplicates(nums)
        print(nums)  # prints [1, 2, 3, 4, 5, 2, 4, 4]
        print(result)  # prints 5
        """
        i = 0
        n = len(nums) -1
        dummy = []        
        while i <= n:
            if nums[i] not in dummy:                
                dummy.append(nums[i])                           
                i += 1
            else:
                nums.append(nums[i])
                nums.pop(i)
                n -= 1            
        print(nums)
        return i

nums = [1, 2, 2, 3, 4, 4, 4, 5]
s = Solution()
k = s.removeDuplicates(nums)
print(k)

