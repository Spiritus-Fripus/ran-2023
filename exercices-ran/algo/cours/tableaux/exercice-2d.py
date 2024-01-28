# EXERCICE TABLEAUX 2D:

# Representation d'un stagiaire
# NOM
# Prénom
# Promo
stagiaire_A = ["DOE","John","RAN-2"]
stagiaire_B = ["BATROSSE","Hal","RAN-2"]

liste_stagiaires = [
    stagiaire_A,
    stagiaire_B
]

print(liste_stagiaires)

for stagiaire in liste_stagiaires:
    for prop in stagiaire:
        print(prop, end=" ")
    print()
   

