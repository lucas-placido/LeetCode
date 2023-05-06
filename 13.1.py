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
        n = len(s) -1
        i = 0
        value = 0
        while i <= n:
            if i != n and map.get(s[i]) < map.get(s[i+1]):
                value -= map.get(s[i])
            else:
                value += map.get(s[i])
            i += 1
        return value
                
s = 'MCMXCIV'
solution = Solution()
print(solution.romanToInt(s))