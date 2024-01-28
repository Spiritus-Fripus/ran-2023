# Import de la librairie date time 
import datetime
birth_year = int(input("Veuillez saisir votre année de naissance : "))
# Obtenez la date actuelle 
current_date = datetime.date.today()
# Obtenez l'année en cours a partir de la date actuelle 
current_year = current_date.year

print(f"Vous avez {current_year-birth_year} ans")