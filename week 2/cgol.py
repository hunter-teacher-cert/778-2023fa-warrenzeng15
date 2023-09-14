# cgol.py
# Warren Zeng
# CSCI 77800 Fall 2023
# collaborators: n/a
# consulted: my brother


def create_board():
    width = 25
    height = 25

    grid = []
    for x in range(width):
        row = [] 
        for y in range(height):
            row.append(' ')

        grid.append(row)

    return grid


def print_board(grid):
    for row in grid:      
        for x in row:
            print(x,end=" ")  #makes it so that it doesn't print cells on a new line
        print()


def set_cell(grid, r, c, val):
    grid[r][c] = val


def count_neighbors(grid, r, c):
    num_neighbors = 0
    for row in range(r-1, (r+1)+1):
        for col in range(c-1, (c+1)+1):
            if ((row == r and col == c) or row < 0 or col < 0 or row >= 25 or col >= 25):
                continue
            elif (grid[row][col] == 'X'):
                num_neighbors += 1
        
    return num_neighbors



def get_next_gen_cell(grid, r, c):
    next_gen = ' '
    num_neighbors = count_neighbors(grid, r, c)
    if grid[r][c] == 'X' and (num_neighbors == 2 or num_neighbors == 3):
        next_gen = 'X'
    elif grid[r][c] == ' ' and num_neighbors == 3:
        next_gen = 'X'

    return next_gen


def generate_next_board(grid):
    new_board = create_board()
    # for row, row_val in enumerate(grid):
    #     for col, val in enumerate(row_val):
    #         new_board[row][col] = get_next_gen_cell(grid, row, col)
    for row in range(25):
        for col in range(25):
            new_board[row][col] = get_next_gen_cell(grid, row, col)
    
    return new_board


game = create_board()
set_cell(game,1,0,'X')
set_cell(game,1,1,'X')
set_cell(game,1,2,'X')
print_board(game)

print("Next generation_____________________________________________")
game = generate_next_board(game)
print_board(game)