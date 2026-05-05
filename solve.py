import sys

def get_puzzle(input_file):
    # Open and read the txt file
    with open(input_file, 'r', errors='ignore') as f:
        contents = f.read()
    # Converting the file from a string to a list of strings, each string represents a line from the board
    board_lines = contents.strip().split("\n")
    
    game = []
    # A for loop to loop through all the lines and replace the string characters with integer characters
    for line in board_lines:
        row = [0 if char == '0' else int(char) for char in line.split()]
        game.append(row)
    return game

def grid_format(grid):
    for x in range(len(grid)):
    # To seperate the board after every 3 rows    
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - - -")
        for y in range(len(grid[0])):
         # To seperate the board after every 3 columns   
            if y % 3 == 0 and y != 0:
                print(" | ", end="")
            if y == 8:
                print(grid[x][y])
            else:
                print(str(grid[x][y]) + " ", end="")

def empty_spaces(board):
    # Finding the empty positions
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def valid_play(board, guess, row, col):
    if guess in board[row]:
        return False
    
    if guess in (board[r][col] for r in range(9)):
        return False
    
    box_row_start = (row // 3) * 3
    box_col_start = (col // 3) * 3
    for r in range(box_row_start, box_row_start + 3):
        for c in range(box_col_start, box_col_start + 3):
            if board[r][c] == guess:
                return False
    
    return True

def solve(board):
    # Solving the puzzle using backtracking
    empty = empty_spaces(board)
    if not empty:
        return True
    else:
        row, col = empty

    for i in range(1, 10):
        if valid_play(board, i, row, col):
            board[row][col] = i
            print(f"Placed {i} in cell ({row+1}, {col+1})")
            grid_format(board)
            if solve(board):
                return True
            board[row][col] = 0
            print(f"Backtracking: Removed {i} from cell ({row+1}, {col+1})")
            grid_format(board)
    return False

# grid = get_puzzle("puzzle.txt")

# print("Unsolved puzzle :")
# grid_format(grid)

# if solve(grid):
#     print("\nSolved puzzle :")
#     grid_format(grid)
# else:
#     print("\nNo solution for puzzle")

def get_solved(output_path,board):
    with open(output_path,'w',errors='ignore' ) as f:
        for row in board:
            f.write(" ".join(str(num) for num in row) + "\n")
            
def solved(input_file, output_path):
    board = get_puzzle(input_file)
    print("Unsolved sudoku board :")
    grid_format(board)
    print()

    if solve(board):
        print("\nSudoku solved succesfully!")
        get_solved(output_path,board)
        print("\nSolved sudoku board :")
        grid_format(board)

    else:
        print("No solution to board")

solved("puzzle.txt", "solved_puzzle.txt")

        
