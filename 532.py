from typing import List

class Solution:
    def findPairs(self, nums, k):
        pairs = set()
        num_counts = {}

        for num in nums:
            if num - k in num_counts:
                pairs.add((num - k, num))
            if num + k in num_counts:
                pairs.add((num, num + k))

            num_counts[num] = num_counts.get(num, 0) + 1
        return len(pairs)
    
nums = [1,2,3,4,5]
k = 1
result = Solution().findPairs(nums, k)
print(result)    