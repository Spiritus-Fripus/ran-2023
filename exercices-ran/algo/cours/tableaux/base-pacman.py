# BASE PACMAN

import os

# Définition de la map
# 0 => case vide
# 1 => gum
# 2 => personnage (pacman)
# 3 => ennemie (fantôme)
# 4 => mur
map = [
    [4,4,4,4,4,4,4,4,4,4,4],
    [4,1,1,1,1,1,1,1,1,1,4],
    [4,1,3,1,1,1,1,1,1,1,4],
    [4,1,1,1,1,1,1,1,1,1,4],
    [4,1,1,1,1,1,1,1,1,1,4],
    [4,1,1,1,1,1,1,1,1,1,4],
    [4,1,1,1,1,1,1,1,1,1,4],
    [4,1,1,1,1,1,1,1,1,1,4],
    [4,1,1,1,1,1,1,1,1,1,4],
    [4,1,1,1,1,1,1,1,3,1,4],
    [4,4,4,4,4,4,4,4,4,4,4]
]

# On place pacman au centre de la map
pacman_x = len(map[0]) // 2
pacman_y = len(map) // 2
map[pacman_y][pacman_x] = 2

while True:
    # On clear le terminal
    os.system("cls")

    # On affiche la map
    for y in range(len(map)):
        for x in range(len(map[0])):
            if map[y][x] == 0:
                print(" ", end=" ")
            if map[y][x] == 1:
                print(".", end=" ")
            if map[y][x] == 2:
                print("O", end=" ")
            if map[y][x] == 3:
                print("F", end=" ")
            if map[y][x] == 4:
                print("#", end=" ")
        print()

    # On demande la direction
    dir = input("Direction (zqsd) : ")

    # On efface l'ancienne position
    map[pacman_y][pacman_x] = 0

    # On gère le déplacement
    if dir == "z":
        pacman_y = pacman_y - 1
    elif dir == "s":
        pacman_y = pacman_y + 1
    elif dir == "d":
        pacman_x = pacman_x + 1
    elif dir == "q":
        pacman_x = pacman_x - 1

    # On met à jour la position de pacman dans la map
    map[pacman_y][pacman_x] = 2