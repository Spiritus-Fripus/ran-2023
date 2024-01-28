# Ce jeu se passe entre deux joueurs. Ils montrent en même temps une main qui désigne un certain 
# nombre. Le gagnant se détermine par la procédure suivante : 
# — prendre connaissance du nombre de doigts de A,
# — prendre connaissance du nombre de doigts de B,
# — calculer la somme de ces deux nombres,
# — si la somme est paire, A est le gagnant,
# — si la somme est impaire, B est le gagnant.

player1 = int(input("Joueur 1 montrez un nombre de doigts: "))
player2 = int(input("Joueur 2 montrez un nombre de doigts: "))

total_fingers = player1 + player2

if total_fingers %2 == 0 :
    print("Joueur 1 gagne !")
else : 
    print("Joueur 2 gagne !")
