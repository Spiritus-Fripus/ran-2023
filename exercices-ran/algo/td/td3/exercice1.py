# Réalisez un jeu de dés utilisant les aiguillages conditionnels. Au démarrage du programme, il
# calcule au hasard un nombre entre 1 à 6 (utilisez la fonction suivante : valeur <— HASARD(valeur
# mini , valeur maxi)). Le programme affiche « Vous avez fait un six » et il affiche la face du dé, sur 3
# lignes, par exemple :
# «0 0»
# « 0 »
# «0 0»

import random
valeur = random.randint(1,6)
if valeur == 1:
    print("\n0 0\n 1 \n0 0\n")
if valeur == 2:   
    print("\n0 1\n 0 \n1 0\n") 
if valeur == 3:
    print("\n0 1\n 1 \n0 1\n")
if valeur == 4:
    print("\n1 1\n 0 \n1 1\n")
if valeur == 5:
    print("\n1 1\n 1 \n1 1\n")
if valeur == 6:
    print("\n1 1\n1 1\n1 1\n")
print(valeur)
