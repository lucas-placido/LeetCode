class Solution:            
    def isPalindrome(self, x: int) -> bool:
        """
        Determine if an integer is a palindrome.

        A palindrome is a number that reads the same backward as forward.
        For example, 121 is a palindrome, while 123 is not.

        Args:
            x: An integer.

        Returns:
            True if x is a palindrome, False otherwise.

        Examples:
            >>> s = Solution()
            >>> s.isPalindrome(121)
            True

            >>> s.isPalindrome(123)
            False
        """
        
        y = x
        len = 1
        while abs(y) >= 10:
            len += 1
            y = y / 10

        if x < 0:
            return False        
        
        elif len < 2:
            return True
        
        else:
            cont = len
            while cont >= 2:                
                right = x % 10
                left = x // (10**(cont-1)) 

                if right != left:
                    return False
                
                x = x // 10
                x = x % (10**(cont-2))
                cont -= 2

            return True

x = 1221
s = Solution()
result = s.isPalindrome(x)
print(result)