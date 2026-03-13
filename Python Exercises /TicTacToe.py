
print("\n")
print(" 1  | 2  |  3 ")
print("---+---+---")
print(" 4 |  5 |  6 ")
print("---+---+---")
print("  7 |  8 | 9  ")
print("\n")
grid = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
win_lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
        [0, 4, 8], [2, 4, 6]              # Diagonal
        ]
    
def x_turn():    
    while True:
        pos_x = input("X Turn: Where do you want your Token to be placed? ")
        pos_x = int(pos_x)
        pos_x -= 1
        if grid[pos_x] == " ":
            grid[pos_x] = "X"
            print(grid[0:3])
            print(grid[3:6])
            print(grid[6:9])
            # check if game won
            # for win_line in win_lines:
            #     for result in win_line:
            #         if result == ["X","X","X"]:
            #             print("X won the game")
            #             quit
            #         else: continue
            o_turn()
        else:
            print("Place is not free, please pick another one")
            x_turn()
    
def o_turn():
    while True:
        pos_o = input("O Turn: Where do you want your Token to be placed? ")
        pos_o = int(pos_o)
        pos_o -= 1
        if grid[pos_o] == " ":
            grid[pos_o] = "O"
            print(grid[0:3])
            print(grid[3:6])
            print(grid[6:9])
            # check if game won
            x_turn()
        else:
            print("Place is not free, please pick another one")
            o_turn()
x_turn()