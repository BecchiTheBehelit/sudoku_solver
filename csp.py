from random import sample

# This function creates a Sudoku game.
def create_game(base = 3, side = 9): 
  # This function generates a pattern for a baseline valid solution.
  def pattern(r,c):
    return (base*(r%base)+r//base+c)%side

  # This function randomizes rows, columns, and numbers of the valid base pattern.
  def shuffle(s):
    return sample(s,len(s))

  # This function removes cells from the board to create the puzzle.
  def remove_cells(board, ratio = 0.75):
    squares = side*side
    empties = int(squares * ratio)
    for p in sample(range(squares),empties):
        board[p//side][p%side] = 0
    return board

  rBase = range(base)
  rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ]
  cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
  nums  = shuffle(range(1,base*base+1))

  # This line produces a board using a randomized baseline pattern.
  board = [ [nums[pattern(r,c)] for c in cols] for r in rows ]
  return remove_cells(board)

board = create_game()

# This function prints the Sudoku board.
def print_board(board):
  for row in board:
    print(" ".join(map(str, row)))

print("Initial Board: \n")
print_board(board)
print("\n")

# This function gets one variable that is not assigned.
def getUnsiganedVariable(board):
  for i in range(len(board)):
    for j in range(len(board[i])):
      if board[i][j] == 0:
        return (i, j)  # row, col

# This function checks if a digit can be assigned to the current position.
def isValidAssignment(board, cur_pos, digit):
  row, col = cur_pos

  # Check the digit in the current row
  if digit in board[row]:
    return False
  
  # Check the digit in the current column
  if digit in [board[i][col] for i in range(9)]:
    return False
  
  # Check the digit in the current 3x3 square
  start_row, start_col = row - row % 3, col - col % 3

  for i in range(3):
    for j in range(3):
      if board[i + start_row][j + start_col] == digit:
        return False
      
  return True

# This function solves the Sudoku puzzle using backtracking.
def backtrackingSolver(board):
  if not getUnsiganedVariable(board):
    return board
  
  row, col = getUnsiganedVariable(board)

  for digit in range(1, 10):
    if isValidAssignment(board, (row, col), digit):
      board[row][col] = digit

      if backtrackingSolver(board):
        return board
      
      board[row][col] = 0

  return None

board = backtrackingSolver(board)

print("Solved Board: \n")
print_board(board)