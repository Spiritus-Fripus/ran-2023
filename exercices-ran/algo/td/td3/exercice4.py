# Réalisez un compteur qui affiche toutes les valeurs comprises entre une borne de départ et une
# borne d’arrivée en tenant compte d’un pas d’incrément.
# Exemple :
# Borne de départ = 3
# Borne d’arrivée = 12
# Pas = 2
# Affichage de 3 5 7 9 11

cpt = int(input("veuillez entrer un entier de départ: "))
cpt_max = int(input("veuillez entrer un entier de fin: "))
cpt_new = int(cpt_max / 2)

for i in range(1,cpt_new):
    if cpt != cpt_max:
        print(cpt)
        cpt=cpt+2
    else:
        exit(1)
print(cpt)
