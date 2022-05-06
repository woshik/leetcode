class Solution:
    def solveSudoku(self, board):
        """
        Do not return anything, modify board in-place instead.
        """

        self.solve(board)

    def solve(self, board):
      # board layout
      # for rowKey, rowValue in enumerate(board):
      #   for columnKey, columValue in enumerate(rowValue):
      #     print(columValue, end="")
      #     if columnKey != 8:
      #       print(" | ", end="")

      #   print()

      #   for columnKey, _ in enumerate(rowValue):
      #     if rowKey != 8:
      #       if columnKey != 8:
      #         print("----", end="")
      #       else:
      #         print("--", end="")
      
      #   print()
      
      print()
      for row in range(len(board)):
        for column in range(len(board[0])):
          if (board[row][column]) == ".":
            for input in range(1, len(board)+1):
              if (self.validInput(board, str(input), row, column)):
                board[row][column] = str(input)
                
                if self.solve(board):
                  return True
                
                board[row][column] = "."
            return False

      return True

    def validInput(self, board, input, row, column):
      for count in range(len(board)):
        if board[row][count] == input:
          return False
        
        if board[count][column] == input:
          return False

        if board[((row // 3) * 3) + (count // 3)][((column // 3) * 3) + (count % 3)] == input:
          return False

      return True


board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

s = Solution()

s.solveSudoku(board)