class Solution:
    def solveNQueens(self, n):
        board = self.createBoard(n)
        result = []
        self.nQueenSolution(board, n, 0, result)

        return result

    def createBoard(self, n):
      board = []

      for _ in range(n): # row
        row = ""
        for _ in range(n): # column
          row += "."
        
        board.append(row)
      
      return board

    def nQueenSolution(self, board, rowCount, columnCount, result):
      if columnCount == len(board):
        result.append(board[:])
        return

      for row in range(rowCount): 
        if self.isPositionClear(board, row, columnCount):
          board[row] = board[row][:columnCount] + 'Q' + board[row][columnCount+1:]
          
          self.nQueenSolution(board, rowCount, columnCount+1, result)

          board[row] = board[row][:columnCount] + '.' + board[row][columnCount+1:]
          
         
    
    def isPositionClear(self, board, rowPosition, columnPosition):
      
      # check horizontal
      for h in range(columnPosition, -1, -1):
        if board[rowPosition][h] == "Q":
          return False
      
      row = rowPosition
      column = columnPosition
      while row != 0 and column != 0:
        row -= 1
        column -= 1

        if board[row][column]  == "Q":
          return False

      row = rowPosition
      column = columnPosition
      boardSize = len(board) - 1
      while row != boardSize and column != 0:
        row += 1
        column -= 1
        if board[row][column]  == "Q":
          return False
      
      return True

s = Solution()

print(s.solveNQueens(4))
