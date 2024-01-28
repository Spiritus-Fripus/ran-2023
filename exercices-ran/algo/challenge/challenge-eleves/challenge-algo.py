# Ecrire un programme qui intègre les fonctionnalités suivantes :
# demander le nombre de matières à saisir
# stocker le nom des matières
# demander le nombre d'élève à ajouter et stocker leur nom et prénom
# pour chaque élève saisir la note par matière
# afficher tous les élèves avec leur moyenne générales et leurs notes par matières
# afficher la moyenne de la classe par matière
# donner le nom du meilleur élève
# donner le nom du pire élève

tab_stock= []

matiere_nbr = int(input("cb de matiere ?: "))
matiere_list= []

for i in range(matiere_nbr):
    matiere= input(f"nom de la matiere {i + 1}: ")
    matiere_list.append(matiere)

student_nbr= int(input("cb d'élèves ?: "))

for i in range(student_nbr):
    name = input(f"nom de l'élève {i + 1}: ")
    surname = input(f"prénom de l'élève {i + 1}: ")
    student = [name + " " + surname]
    
    note_list= []
    moyenne_list= []
    for matiere in matiere_list:
        note = float(input(f"note de {name} {surname} en {matiere}: "))
        note_list.append(note)
            
    tab_stock.append(student)
    tab_stock.append(matiere_list)
    tab_stock.append(note_list)

print(tab_stock)