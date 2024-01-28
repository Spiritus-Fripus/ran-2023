# On se propose de calculer la moyenne des notes d’un élève pour certaines matières ; français,
# maths, géographie et informatique.
# Pour chacune de ces matières, il faudra saisir un coefficient de pondération compris entre 1 et 10.
# Calculez la moyenne en tenant compte des coefficients de pondération.
# Affichez une appréciation :
# Si la moyenne est comprise entre 16 et 20, la mention est « Très bien ».
# Si la moyenne est comprise entre 12 et 16, la mention est « Bien ».
# Si la moyenne est comprise entre 8 et 12, la mention est « Assez bien ».
# Si la moyenne est comprise entre 4 et 8, la mention est « Insuffisant ».
# Si la moyenne est comprise entre 0 et 4, la mention est « Nul ».
# Il faut contrôler que les notes sont comprises entre 0 et 20 et que les coefficients sont compris
# entre 1 et 10. (reprise de l’exercice 9 feuille niveau II pour utiliser des boucles)

francais= int(input("veuillez entrer la moyenne de francais [0-20]:  "))
francais_coef= int(input("veuillez entrer le coefficient de francais [1-10]: "))
moyenne_francais = francais * francais_coef
math = int(input("veuillez entrer la moyenne de math [0-20]:  "))
math_coef = int(input("veuillez entrer le coefficient de math [1-10]: "))
moyenne_math = math * math_coef
geo= int(input("veuillez entrer la moyenne de géographie [0-20]:  "))
geo_coef= int(input("veuillez entrer le coefficient de géographie [1-10]: "))
moyenne_geo= geo * geo_coef
info = int(input("veuillez entrer la moyenne d'informatique [0-20]:  "))
info_coef = int(input("veuillez entrer le coefficient d'informatique [1-10]: "))
moyenne_info = info * info_coef
moyenne_gen = (moyenne_francais + moyenne_math + moyenne_geo + moyenne_info) / (francais_coef + math_coef + geo_coef + info_coef)


if moyenne_gen >= 16 < 20:
    print(f"{moyenne_gen} mention trés bien !")
elif moyenne_gen >= 12 < 16:
    print(f"{moyenne_gen} mention bien !")
elif moyenne_gen >= 8 < 12:
    print(f"{moyenne_gen} mention assez bien !")
elif moyenne_gen >= 4 < 8:
    print(f"{moyenne_gen} mention insuffisant !")
elif moyenne_gen >= 0 < 4: 
    print(f"{moyenne_gen} mention nul !")