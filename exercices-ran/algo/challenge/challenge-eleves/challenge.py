# Ecrire un programme qui intègre les fonctionnalités suivantes :
# demander le nombre de matières à saisir
# stocker le nom des matières
# demander le nombre d'élève à ajouter et stocker leur nom et prénom
# pour chaque élève saisir la note par matière
# afficher tous les élèves avec leur moyenne générales et leurs notes par matières
# afficher la moyenne de la classe par matière
# donner le nom du meilleur élève
# donner le nom du pire élève

matiere_nbr = int(input("cb de matiere ?: "))

matiere_list= []
for i in range(matiere_nbr):
    matiere = input(f"nom matière {i + 1} ?: ")
    matiere_list.append(matiere)

student_nbr = int(input("cb d'élèves ?: "))
student_list = []
note_dict = {}

for i in range(student_nbr):
    name = input(f"nom élève {i+1}?:")
    forname = input(f"prénom élève {i+1}?:")
    student= f"{name} {forname}"
    student_list.append(student)
    note_dict[student] = {matiere: [] for matiere in matiere_list}

for student in student_list:
    print(f"note de {student}")
    for matiere in matiere_list:
        note = float(input(f"note de {matiere} pour {student}: "))
        note_dict[student][matiere].append(note)

print(note_dict)