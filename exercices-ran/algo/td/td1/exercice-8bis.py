print()
print("===================================================")
print("============== Prix TTC avec remise ===============")
print("===================================================")
print()

prix_u_ht = float(input("saisir le prix unitaire HT (€): "))
quantity = int(input("saisir la quantité commandée: "))
tva = float(input("saisir la TVA (%): "))

prix_total_ht = prix_u_ht * quantity
prix_total_ht_remise = prix_total_ht * 0.85 
prix_total_ttc = prix_total_ht_remise * (1 + tva/100)

print(f"Le total de votre commande s'élève à {prix_total_ttc} € TTC")

print()
print("===================================================")
print()