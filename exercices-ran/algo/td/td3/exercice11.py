# Réécrire l’algorithme précédent, mais cette fois-ci on ne connaît pas d’avance combien l’utilisateur
# souhaite saisir de nombres. La saisie des nombres s’arrête lorsque l’utilisateur entre un zéro.

nbr_max= 0
nbr = ""

while nbr != 0:
    nbr = int(input("Veuillez taper un nombre entier (0 pour arreter le programme): "))
    if nbr > nbr_max:
        nbr_max=nbr

print(nbr_max)

