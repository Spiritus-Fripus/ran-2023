# Une voiture coûte 56 000 e et perd 7% de sa valeur chaque année.Rédiger le programme qui calcule et affiche la valeur de cette voiture au bout de 18 ans. BONUS : améliorer votre programme en demandant à l’utilisateur le prix d’achat de sa voiture et l’année à laquelle il souhaite la vendre. (Faire les vérifications nécessaires)

# affectation de mes variables
prixVoiture = float(input("saisir le prix de votre voiture: "))
year = int(input("Le nombre d'année que vous souhaitez la garder: "))
decote = 7 / 100

# itération dans une boucle for
for i in range(1,year +1):
# pour chaque tour de boucle (itération) entre 1 (et non pas 0) et l'année entrée +1 (pour atteindre l'année souhaitée) le prix de ma voiture sera différent car ma décote de 7% rentre en compte
    prixVoiture = prixVoiture - (prixVoiture * decote)
    print()
# print dans ma boucle pour pouvoir avoir un résultat à chaque itération (le fait de print i donne la valeur de i incrémenté à chaque itération) et la fonction round me permet de limiter les nombres aprés la virgule.
    print(f"Au bout de {i} an(s) votre voiture voiture sera cotée {round(prixVoiture,3)}€ ")