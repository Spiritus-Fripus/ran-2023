prix = float(input("Veuillez saisir vôtre prix HT (€): "))
quantite = int(input("Veuillez saisir vôtre quantité commandée: "))
quantite_ht = int(prix * quantite)
print("Le prix de votre commande hors taxe est de: ", quantite_ht),
remise = float(1 - 15 / 100)
print("Je vous offre une remise de 15% ! "),
print("Le prix aprés remise est de:  ", (quantite_ht * remise), "hors taxes")
tva = float(input("Le montant de vôtre tva:  "))
prix_ttc = float(1 + tva / 100)
print("Le prix de vôtre commande est de ", ((quantite_ht * remise) * prix_ttc), "ttc")