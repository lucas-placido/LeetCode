from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            count = [0] * 26            
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)                    
        return list(result.values())

strs = ["eat","tea","tan","ate","nat","bat"]
s = Solution()
result = s.groupAnagrams(strs)
print(result)