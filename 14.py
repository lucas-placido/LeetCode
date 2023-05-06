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
        
        if len(strs) not in range(1, 201):
            return 
        
        for word in strs:
            if len(word) not in range(0, 201):
                return
            elif word.isupper():
                return

        # Creates a list with all the prefixes of each string in the list            
        i = 0
        n = len(strs) -1
        all_prefixes = []
        while i <= n:
            for index in range(0, len(strs[i]) +1):
                prefix = strs[i][:index]
                if prefix != "":
                    all_prefixes.append(prefix)
            i += 1
        print("All prexises:\n", all_prefixes)

        prefix_map = {}
        for prefix in all_prefixes:
            if prefix not in prefix_map.keys():
                prefix_map[prefix] = 1
            else:
                prefix_map[prefix] += 1
        print("Prefix maps:\n", prefix_map)

        if not prefix_map:
            return ""

        max_value = max(prefix_map.values())
        if max_value == 1 and len(strs) > 1:
            return ""
        
        prefixes = []
        for key in prefix_map.keys():
            if prefix_map[key] == max_value:
                prefixes.append(key)
        prefixes.sort(key=lambda x: len(x))
        output = prefixes[-1]
        for word in strs:
            if output != word[:len(output)]:
                return ""
        return output
    

strs = ["flower","flow","flight"]
s = Solution()
print(s.longestCommonPrefix(strs))