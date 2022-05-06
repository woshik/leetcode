class Solution:
    def isValidSudoku(self, board):
        list = range(9)
        
        for row in list:
          for column in list:
            if board[row][column] != ".":
              for count in list:
                
                if count != column and board[row][count] == board[row][column]:
                    return False

                if count != row and board[count][column] == board[row][column]:
                    return False
                
                subBoxRow = ((row//3) * 3) + (count//3)
                subBoxColumn = ((column//3) * 3) + (count%3)

                if (subBoxRow != row or subBoxColumn != column) and board[subBoxRow][subBoxColumn] == board[row][column]:
                    return False
        
        return True

board = [
["8","3",".",".","7",".",".",".","."]
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

print(s.isValidSudoku(board))
