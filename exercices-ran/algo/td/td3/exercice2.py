# Exercice 2 :
# Demandez à saisir une date de la forme AAAA/MM/JJ (par exemple 2011/10/17) et afficher « Le
# 17 octobre 2011 est un lundi. » Pour connaitre le nom du jour, on part de la date avec :
# • A = année complète (dans l’exemple 2011),
# • M = numéro du mois (dans l’exemple 10),
# • J = numéro du jour (dans l’exemple 17).
# Si MM vaut 1 ou 2, il faut :
# • retrancher 1 à A,
# • ajouter 12 à M.
# Avec ces valeurs, on calcule un nombre N
# • N = J + ENT((13 * M + 3) / 5) + ENT(5 * A / 4) — ENT(A / 100) + ENT(A / 400)
# • N = MOD(N ; 7)
# N donne le nom du jour avec : 0 pour lundi, 1 pour mardi, ..., 6 pour dimanche

A = int(input("Veuillez entrer une année au format [AAAA]: "))
M= int(input("Veuillez entrer un mois au format [MM]: "))
J = int(input("Veuillez entrer un jour au format [JJ]"))

if M == 1 or M ==2:
    A = A +1
    M = M + 12
N = J + int((13 * M + 3) / 5) + int(5 * A / 4) - int(A / 100) + int(A / 400)

if N%7 == 0:
    print(f"lundi {J} {M} {A}");
elif N%7 == 1:
    print(f"mardi {J} {M} {A}")
elif N%7 == 2:
    print(f"mercredi {J} {M} {A}")
elif N%7 == 3:
    print(f"jeudi {J} {M} {A}")
elif N%7 == 4:
    print(f"vendredi {J} {M} {A}")
elif N%7 == 5:
    print(f"samedi {J} {M} {A}")
elif N%7 ==6:
    print(f"dimanche {J} {M} {A}")