class Solution:
    solutionCount = 0

    def totalNQueens(self, n):
        board = self.createBoard(n)
        self.nQueenSolution(board, n, 0)

        return self.solutionCount

    def createBoard(self, n):
      board = []

      for _ in range(n): # row
        row = ""
        for _ in range(n): # column
          row += "."
        
        board.append(row)
      
      return board

    def nQueenSolution(self, board, rowCount, columnCount):
      if columnCount == len(board):
        self.solutionCount += 1
        return

      for row in range(rowCount): 
        if self.isPositionClear(board, row, columnCount):
          board[row] = board[row][:columnCount] + 'Q' + board[row][columnCount+1:]
          
          self.nQueenSolution(board, rowCount, columnCount+1)

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

print(s.totalNQueens(4))
