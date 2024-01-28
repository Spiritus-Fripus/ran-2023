# Tableau simple (1 dimension)
# Pour stocker plusieurs valeurs au même endroit
liste_burgers = ["Big Tasty","Big Mac","CBO","Royal Bacon"]

# On affiche CBO
# On accède donc à l'élement situé à l'indice 2
print(liste_burgers[2])

# On remplace le "Royal Bacon" par "280"
liste_burgers[3] = "280"

print(liste_burgers)

# On ajoute un nouveau burger, le "M"
liste_burgers += ["M"]

print(liste_burgers)

# On supprime le "CBO"
del(liste_burgers[2])

print(liste_burgers)

# On affice tous les burgers
# On boucle sur les indices
for i in range(0, len(liste_burgers)):
    print(f"{i} => {liste_burgers[i]}")

for burger in liste_burgers:
    print(burger)

# Parcours inverse
for i in range(len(liste_burgers)-1, -1, -1):
    print(f"{i} => {liste_burgers[i]}")