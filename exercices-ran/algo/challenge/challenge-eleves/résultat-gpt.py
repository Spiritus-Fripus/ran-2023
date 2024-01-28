# Fonction pour calculer la moyenne d'une liste de notes
def calculer_moyenne(notes):
    if len(notes) == 0:
        return 0
    else:
        return sum(notes) / len(notes)

# Demander le nombre de matières à saisir
nb_matieres = int(input("Entrez le nombre de matières : "))

# Stocker le nom des matières
matieres = []
for i in range(nb_matieres):
    matiere = input(f"Entrez le nom de la matière {i + 1} : ")
    matieres.append(matiere)

# Demander le nombre d'élèves à ajouter
nb_eleves = int(input("Entrez le nombre d'élèves à ajouter : "))

# Initialiser les dictionnaires pour stocker les notes des élèves
eleves = []
notes_eleves = {}

# Saisir les noms et prénoms des élèves
for i in range(nb_eleves):
    nom = input(f"Entrez le nom de l'élève {i + 1} : ")
    prenom = input(f"Entrez le prénom de l'élève {i + 1} : ")
    eleve = f"{nom} {prenom}"
    eleves.append(eleve)
    notes_eleves[eleve] = {matiere: [] for matiere in matieres}

# Saisir les notes par matière pour chaque élève
for eleve in eleves:
    print(f"Saisie des notes pour {eleve} :")
    for matiere in matieres:
        note = float(input(f"Entrez la note de {matiere} pour {eleve} : "))
        notes_eleves[eleve][matiere].append(note)

# Afficher les élèves avec leurs moyennes générales et leurs notes par matière
print("\nRésultats des élèves :")
for eleve in eleves:
    print(f"{eleve}:")
    moyenne_generale = 0
    for matiere in matieres:
        notes = notes_eleves[eleve][matiere]
        moyenne_matiere = calculer_moyenne(notes)
        moyenne_generale += moyenne_matiere
        print(f"   {matiere}: {notes} (Moyenne: {moyenne_matiere})")
    moyenne_generale /= len(matieres)
    print(f"   Moyenne Générale: {moyenne_generale}\n")

# Calculer la moyenne de la classe par matière
moyenne_classe_par_matiere = {matiere: [] for matiere in matieres}
for matiere in matieres:
    for eleve in eleves:
        notes = notes_eleves[eleve][matiere]
        moyenne_matiere = calculer_moyenne(notes)
        moyenne_classe_par_matiere[matiere].append(moyenne_matiere)

print("Moyenne de la classe par matière :")
for matiere in matieres:
    moyenne = calculer_moyenne(moyenne_classe_par_matiere[matiere])
    print(f"{matiere}: {moyenne}")

# Trouver le meilleur et le pire élève
meilleur_eleve = None
pire_eleve = None
meilleure_moyenne = 0
pire_moyenne = float('inf')

for eleve in eleves:
    moyenne = calculer_moyenne([calculer_moyenne(notes_eleves[eleve][matiere]) for matiere in matieres])
    if moyenne > meilleure_moyenne:
        meilleur_eleve = eleve
        meilleure_moyenne = moyenne
    if moyenne < pire_moyenne:
        pire_eleve = eleve
        pire_moyenne = moyenne

print(f"\nMeilleur élève: {meilleur_eleve} (Moyenne Générale: {meilleure_moyenne})")
print(f"Pire élève: {pire_eleve} (Moyenne Générale: {pire_moyenne})")
