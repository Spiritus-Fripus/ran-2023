# Rédiger un algorithme en pseudo-code qui demande à l’utilisateur de saisir le montant d’un produit acheté ainsi que la quantité acheté et qui affiche le montant totale avec une remise de 5 %

product = float(input("saisir le montant du produit: "))
quantity = int(input("Saisir la quantité: "))

price = quantity * (product - (product * 5/100))

print(price)