class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
        ']': '['
        ,')': '('
        ,'}': '{'
        }
        for char in s:
            if char in map.keys():
                if stack and map[char] == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
            else:
                stack.append(char)            
        return True if not stack else False
                                
input = "[({(())}[()])]"

s = Solution()
output = s.isValid(input)
print(output)