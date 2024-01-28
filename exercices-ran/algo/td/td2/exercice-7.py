# Saisissez un montant TTC et appliquez une remise avec les conditions suivantes : 
# — si le montant est compris entre 500 € et 1 000 €, le taux de remise est de 2 %,
# — si le montant est compris entre 1 000 € et 2 000 €, le taux de remise est de 5 %,
# — si le montant est supérieur à 2 000 €, le taux de remise est de 10 %. 

prix_ttc = float(input("Tapez votre prix TTC (€): "))

if 500 <= prix_ttc <= 1000 :
    remise = 2
elif 1000 <= prix_ttc <= 2000:
    remise = 5
elif prix_ttc > 2000:
    remise = 10
else:
    print("Pas de remise")
    quit(1)
print(f"Vous bénéficiez d'une remise de {remise}% pour votre commande d'un montant de {prix_ttc}€.Vous n'avez plus qu'a regler {prix_ttc * (1-remise/100)}€")
