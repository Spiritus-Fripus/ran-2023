# Ecrire un programme qui intègre les fonctionnalités suivantes :
# demander le nombre de matières à saisir
nb_matieres = int(input("saisir le nombre de matieres: "))

# stocker le nom des matières
liste_matieres = []
for i in range(nb_matieres):
    nom_matieres = input(f"saisir le nom de la matiere {i +1}: ")
    liste_matieres += [nom_matieres] # ou liste_matieres.append(nom_matiere)

# demander le nombre d'élève à ajouter et stocker leur nom et prénom
nb_eleves = int(input("saisir le nombre d'eleves: "))
liste_eleves = []
for i in range(nb_eleves):
    nom_eleves = input("saisir le nom et le prénom de l'eleves: ")
    liste_eleves += [nom_eleves] # ou liste_matieres.append(nom_matiere)

# pour chaque élève saisir la note par matière
liste_notes = []
liste_moyenne = []
for i in range(nb_eleves):
    note_eleve = []
    somme_notes = 0
    print((f"=== saisie des notes pour {liste_eleves[i]} ==="))
    for j in range(nb_matieres):
        note_matiere = float(input(f"saisir la note de {liste_matieres[j]}: "))
        note_eleve += [note_matiere]
        somme_notes += note_matiere
    liste_notes += [note_eleve]
    liste_moyenne += [somme_notes / nb_matieres]
    print()

# afficher tous les élèves avec leur moyenne générales et leurs notes par matières
for i in range(nb_eleves):
    print(f"=== Bulletin de {liste_eleves[i]} ===")
    for j in range(nb_matieres):
        print(f"notes de {liste_matieres[j]}: {liste_notes[i][j]}")
    print(f"Moyenne générale : {liste_moyenne[i]}/20")
    print()

# afficher la moyenne de la classe par matière
for i in range(nb_matieres):
    somme_notes_par_matieres= 0
    for j in range(nb_eleves):
        somme_notes_par_matieres += liste_notes[j][i]
    print(f"Moyenne de la classe pour {liste_matieres[i]} ; {somme_notes_par_matieres / nb_eleves}")

# donner le nom du meilleur élève
# donner le nom du pire élève
moyenne_max = 0
moyenne_min = 20
indice_meilleur_eleve = 0
indice_pire_eleve = 0
for i in range(nb_eleves):
    if liste_moyenne[i] > moyenne_max:
        moyenne_max = liste_moyenne[i]
        indice_meilleur_eleve = i

    if liste_moyenne[i] < moyenne_min:
        moyenne_min = liste_moyenne[i]
        indice_pire_eleve = i
print(f"Le meilleur élève est: {liste_eleves[indice_meilleur_eleve]} avec une moyenne de {moyenne_max} /20")  
print(f"Le pire élève est: {liste_eleves[indice_pire_eleve]} avec une moyenne de {moyenne_min} /20")  
print()
