# Exercise 7: Simple Grid Game
# Write your code here
SIZE = 8
player_row = 4
player_col = 4
line_row = 4
line_col = 4

playing = True

while playing:
    grid = []
    for row in range(SIZE):
        row_list = []
        for col in range(SIZE):
            row_list.append('.')
        grid.append(row_list)

    grid[line_row][line_col] = '-'
    grid[player_row][player_col] = 'P'
    
    # Print the grid
    for row in grid:
        for i in row:
            print(i, end=' ')
        print()

    line_row = player_row
    line_col = player_col
    
    move = input("Move (u/d/l/r/q): ")
    if move == "u":
        player_row -= 1
    elif move == "d":
        player_row += 1
    elif move == "l":
        player_col -= 1
    elif move == "r":
        player_col += 1
    elif move == "q":
        playing = False
    else: 
        print("Invalid move, Try Again")



