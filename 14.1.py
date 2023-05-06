from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Finds the common longest prefix in an array of strings
        If there is no common prefix, returns an empty string
        
        Args:
        - strs: A list of strings (1 <= len(strs) <= 200)
        
        Returns:
        - The longest common prefix among the input strings, as a string
        
        Example:
        Input: strs = ["flower","flow","flight"]
        Output: "fl"
        """
        
        output = ""
        i = 0
        shortest = min(set(strs), key=len)
        while i <= len(shortest) -1:
            print(i)
            for word in strs:
                print(word, shortest)
                if (word[i] != shortest[i]) and (word != shortest):
                    return output                
            output += shortest[i]
            i += 1
        return output

strs = ["dog","racecar","car"]
s = Solution()
print(s.longestCommonPrefix(strs))