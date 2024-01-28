# Saisissez un nombre au clavier et affichez un des messages « Positif », « Nul », ou « Négatif » 
# suivant sa valeur.

number = int(input("Saisissez un nombre entier: "))
if number >= 1 :
    print("Positif")
elif number == 0 :
    print("Nul")
else :
    print("Négatif")
