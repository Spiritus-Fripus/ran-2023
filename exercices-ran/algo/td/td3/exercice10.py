# Écrire un algorithme qui demande successivement 20 nombres à l’utilisateur, et qui lui dise ensuite
# quel était le plus grand parmi ces 20 nombres.
# SANS TABLEAUX !!!

nbr_max= 0

for i in range(20):
    nbr = int(input("Veuillez taper un nombre entier: "))
    if nbr > nbr_max:
        nbr_max=nbr

print(nbr_max)
