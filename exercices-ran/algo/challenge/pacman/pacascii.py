import os

ascii = [
    " ",  # 0
    "┌",  # 1
    "─",  # 2
    "┐",  # 3
    "│",  # 4
    "┘",  # 5
    "└",  # 6
    "+",  # 7
    "♦",  # 8
]

map = [
    [1,2,2,2,2,2,2,2,3],
    [4,8,0,0,0,0,0,8,4],
    [4,0,0,0,7,0,0,0,4],
    [4,8,0,0,0,0,0,8,4],
    [6,2,2,2,2,2,2,2,5],
]


player_x = len(map[0]) // 2
player_y = len(map) // 2
map[player_y][player_x] = 7

while True:
    
    for i in map:
        for j in i:
            print(ascii[j], end="")
        print()

    dir = input("direction zqsd: ")

    map[player_y][player_x] = 0

    if dir == "z":
        player_y = player_y - 1
    elif dir == "s":
        player_y = player_y + 1
    elif dir == "d":
        player_x = player_x + 1
    elif dir == "q":
        player_x = player_x - 1
    
    map[player_y][player_x] = 7