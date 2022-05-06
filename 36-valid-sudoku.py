class Solution:
    def isValidSudoku(self, board):
        for row in range(len(board)):
          for column in range(len(board)):
            if board[row][column] != ".":
              for count in range(len(board)):
                
                if count != column:
                  if board[row][count] == board[row][column]:
                    return False

                if count != row:
                  if board[count][column] == board[row][column]:
                    return False
                
                subBoxRow = ((row//3) * 3) + (count//3)
                subBoxColumn = ((column//3) * 3) + (count%3)

                if subBoxRow != row or subBoxColumn != column:
                  if board[subBoxRow][subBoxColumn] == board[row][column]:
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
