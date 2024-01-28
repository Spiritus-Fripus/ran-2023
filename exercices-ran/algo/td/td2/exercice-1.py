#Calculez la moyenne des notes d'un élève aprés avoir saisi les notes de français , de francais,
#math, géométrie et d'informatique. Il faut tenir compte de coefficients de pondérations
#qui seront saisie eux aussi
note_fr = float(input("Note de français (/20): "))
coef_fr = float(input("Coefficient de français: "))

note_math = float(input("Note de math (/20)"))
coef_math = float(input("Coefficient de math: "))

note_geo = float(input("Note de géométrie (/20): "))
coef_geo = float(input("Coefficient de géométrie: "))

note_info = float(input("Note d'informatique (/20): "))
coef_info = float(input("Coefficient d'informatique: "))

note_fr_pond = note_fr * coef_fr
note_math_pond = note_math * coef_math
note_geo_pond = note_geo * coef_geo
note_info_pond = note_info * coef_info
total_note = note_fr_pond + note_geo_pond + note_math_pond + note_info_pond
total_coef = coef_fr + coef_math + coef_geo + coef_info

moyenne = total_note / total_coef

print(f"Votre moyenne générale pondérée est de : {round(moyenne, 2)}")
