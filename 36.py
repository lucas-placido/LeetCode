from typing import List
import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:                        
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        box = collections.defaultdict(set)

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                elif (
                     board[i][j] in row[i] or 
                     board[i][j] in col[j] or
                     board[i][j] in box[(i // 3, j // 3)]):
                        return False
                row[i].add(board[i][j])
                col[j].add(board[i][j])
                box[(i // 3, j // 3)].add(board[i][j])                
                print('row: ', row,"\n")
                print('col: ', col,"\n")
                print('box: ', box,"\n")
        return True

board = [
["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]
]
s = Solution()
result = s.isValidSudoku(board)
print(result)   