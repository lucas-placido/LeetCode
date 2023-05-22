from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:                
        word_set = set(words)
        longest = ''
        for word in words:
            if len(word) > len(longest) or (len(word) == len(longest) and word < longest):                                
                if all(word[:i] in word_set for i in range(1, len(word))):                    
                    longest = word
        return longest
    
words = ["yo","ew","fc","zrc","yodn","fcm","qm","qmo","fcmz","z","ewq","yod","ewqz","y"]
result = Solution().longestWord(words)
print(result)