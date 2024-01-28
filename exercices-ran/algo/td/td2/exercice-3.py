import datetime

print("Les enfants de moins de 3 ans gagnent le lot: ")

birth_year = int(input("Quelle est l'année de naissance de votre enfant ?: "))
baby_age = datetime.date.today().year - birth_year

if baby_age < 3 :
    print("Vous avez gagné le lot")
else :
    print("Désolé c'est perdu")