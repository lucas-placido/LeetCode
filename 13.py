class Solution:
    def romanToInt(self, s: str) -> int:
        """
        Convert a Roman numeral to an integer.

        This function takes a string representing a Roman numeral and returns
        the equivalent integer value. The Roman numeral must consist of the
        following characters: I, V, X, L, C, D, and M.

        Args:
            s: A string representing a Roman numeral.

        Returns:
            An integer value corresponding to the Roman numeral.

        Examples:
            >>> s = Solution()
            >>> s.romanToInt('III')
            3

            >>> s.romanToInt('IX')
            9

            >>> s.romanToInt('MCMXCIV')
            1994
        """
        roman_numbers = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        for letter in s:
            if letter not in roman_numbers:
                return
        if  len(s) < 1 or len(s) > 15:
            return
        map = {
            'I': 1
            ,'V': 5
            ,'X': 10
            ,'L': 50
            ,'C': 100
            ,'D': 500
            ,'M': 1000
        }
        total = 0
        for index in range(len(s)):
            if index < len(s) -1:        
                if s[index] == 'I' and (s[index +1] == 'V' or s[index +1] == 'X'):
                    total += map.get(s[index]) - 2 * 1
                    continue
                elif s[index] == 'X' and (s[index +1] == 'L' or s[index +1] == 'C') :
                    total += map.get(s[index]) - 2 * 10
                    continue
                elif s[index] == 'C' and (s[index +1] == 'D' or s[index +1] == 'M'):
                    total += map.get(s[index]) - 2 * 100
                    continue
                
            total += map.get(s[index])

        return total

s = 'IX'
solution = Solution()
print(solution.romanToInt(s))