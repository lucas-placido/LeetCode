from typing import List

salary = [4000,3000,1000,2000]

class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        salary.pop(0)
        salary.pop(-1)
        return sum(salary) / len(salary)
    
s = Solution()
print(s.average(salary))