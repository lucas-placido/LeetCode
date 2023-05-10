class Solution:
    def strStr(self, haystack: str, needle: str) -> int:            
        i = 0
        n = len(haystack) -1
        while i <= n:                
            if needle == haystack[i: i + len(needle)]:
                return i
            else:                           
                i += 1        
        return -1
    
haystack = "sadbutsad"
needle = "sad"    

s = Solution()
result = s.strStr(haystack, needle)
print(result)