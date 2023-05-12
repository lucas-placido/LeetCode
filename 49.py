from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}        
        for i in range(len(strs)):
            hash = {}
            for letter in strs[i]:
                hash[letter] = 1 + hash.get(letter, 0)                                    
            hash_sorted = {k: hash[k] for k in sorted(hash)}            
            if str(hash_sorted) not in hash_map:
                hash_map[str(hash_sorted)] =  [strs[i]]
            else:
                hash_map[str(hash_sorted)].append(strs[i])                
        return list(hash_map.values())

strs = ["eat","tea","tan","ate","nat","bat"]
s = Solution()
result = s.groupAnagrams(strs)
print(result)