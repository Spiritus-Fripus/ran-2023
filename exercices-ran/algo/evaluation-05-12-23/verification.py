# Écrire un algorithme qui demande un nombre compris entre 10 et 20, jusqu’à ce que la réponse convienne. En cas de réponse supérieure à 20, on fera apparaître un message : « Plus petit ! », et inversement, « Plus grand ! » si le nombre est inférieur à 10

# affectation de ma variable
statut = ""

# création d'une boucle for qui ne s'arretera pas tant que le statut n'est pas "c'est gagné"
while statut != "c'est gagné":
# indentation de ma variable saisie par l'utilisateur dans ma boucle afin que la tache se repette tant que le résultat souhaité n'est pas bon
    nbr = int(input("saisir un nombre entier: "))
# affectation de mes instructions pour définir la fin de ma boucle
# tant que le nombre ne sera pas compris entre 10 et 20 la variable nbr sera démandée à l'utilisateur avec un message le guidant (plus petit ) ou (plus grand)
    if nbr > 20:
        statut = "plus petit"
        print(statut)

    if nbr < 10: 
        statut = "plus grand"
        print(statut)

    if nbr >= 10 and nbr <= 20: 
        statut = "c'est gagné"
        print(statut)
# sortie de ma boucle si le nombre et entre 10 et 20
        break
   

    