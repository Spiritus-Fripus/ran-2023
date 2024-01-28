# Une pointe est constituée d’une tête symbolisée par le caractère « _ » et d’une tige symbolisée par le
# caractère « | ». La dimension d’une pointe est la longueur de sa tige, qui correspond au nombre de
# caractères « | » présents.
# Ainsi :
# _
# |
# |
# |
# |
# est une pointe de dimension 4.
# L’objectif est d’afficher des pointes d’une dimension donnée.
# Écrire un algorithme affichant p pointes (côte à côte) de dimension d.

pointe = int(input("saisir le nombre de pointes: "))
dimension = int(input("saisir la taille de la pointe: "))
pointe_head= ""
pointe_tail= ""
fleche=""

for p in range(pointe):
    pointe_head = pointe_head + " " + "_" 
pointe_head += "\n" 
for d in range(dimension):
    pointe_tail= pointe_tail + " " + (("|" + " ") *pointe) +"\n"

fleche = pointe_head + pointe_tail
print(fleche)