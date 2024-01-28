liste_stagiaires = []

# V1
for i in range(3):
    stagiaire = []
    stagiaire += [input("NOM : ")]
    stagiaire += [input("Prénom : ")]
    stagiaire += [input("Promo : ")]
    liste_stagiaires += [stagiaire]

# V2
for i in range(3):
    liste_stagiaires += [[
        input("NOM : "),
        input("Prénom : "),
        input("Promo : ")
    ]]

print(liste_stagiaires)

