# Saisissez les notes d’un élève pour les matières suivantes : français, mathématiques, géographie et 
# informatique. 
# Si la moyenne est comprise entre 16 et 20, la mention est « Très bien ». 
# Si la moyenne est comprise entre 12 et 16, la mention est « Bien ». 
# Si la moyenne est comprise entre 8 et 12, la mention est « Assez bien ». 
# Si la moyenne est comprise entre 4 et 8, la mention est « Insuffisant ». 
# Si la moyenne est comprise entre 0 et 4, la mention est « Nul ». 

note_fr = float(input("Note de français (/20): "))
note_math = float(input("Note de math (/20)"))
note_geo = float(input("Note de géométrie (/20): "))
note_info = float(input("Note d'informatique (/20): "))

moyenne = (note_fr + note_math + note_geo + note_info) / 4

if 16 <= moyenne <= 20:
    mention = "trés bien"
elif 12 <= moyenne <= 16: 
    mention = "Bien"
elif 8 <= moyenne <= 12:
    mention = "Assez bien"
elif 4 <= moyenne <= 8:
    mention = "Insuffisant"
elif 0 <= moyenne <= 4: 
    mention = "Nul"

print(f"Vous avez la mention {mention}.")