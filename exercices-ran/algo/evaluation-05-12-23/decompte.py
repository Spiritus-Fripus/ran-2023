# Rédiger l’algorithme permettant de compter le nombre de noms saisis avant l’interruption de la saisie (lorsque l’on saisit « fin »)

# affectation de mon compteur
nbNom = 0
# affectation de ma variable
nom = ""
# création d'une boucle while qui bouclera tant que le mot fin n'est pas tapé
while nom != "fin":
# saisie de l'utlisateur
    nom = input("saisir un nom ('fin' pour arreter): ")
# incrémentation de mon compteur
    nbNom += 1

print(f"Vous avez saisi {nbNom} nom(s)")
