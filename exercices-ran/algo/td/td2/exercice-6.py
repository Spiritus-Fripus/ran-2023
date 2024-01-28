# Saisissez le prix HT d’un produit. Affichez les taux de TVA possibles ainsi qu’un code : 
# Pour une TVA de 5,5 %, saisissez 1 
# Pour une TVA de 19,6 %, saisissez 2 
# Pour une TVA de 33 %, saisissez 3 
# L’utilisateur saisit un code (1, 2 ou 3). Calculez le prix TTC et affichez un message : « Le prix HT 
# est de 100 €, la TVA est de 19,6 % et le prix TTC est de 119,60 €. » 

prix_ht = float(input("Saissisez votre prix HT: "))
print("Choissisez votre TVA: ")
print ("Pour 5.5% tapez 1")
print("Pour 19.6% tapez 2 ")
print("Pour 33% tapez 3 ")
tva_choosen = int(input("Tapez votre chiffre (1,2,3): "))

tva_1 = float(1.055)
tva_2 = float(1.196)
tva_3 = float(1.33)

if tva_choosen == 1 :
    tva_choosen = tva_1
    print(f"Le prix choisis est de {prix_ht}€ , la tva est de 5.5 % et le prix TTC est de {prix_ht*tva_choosen}€")
elif tva_choosen == 2 :
    tva_choosen = tva_2
    print(f"Le prix choisis est de {prix_ht}€ , la tva est de 19.6 % et le prix TTC est de {prix_ht*tva_choosen}€")
elif tva_choosen == 3 : 
    tva_choosen = tva_3
    print(f"Le prix choisis est de {prix_ht}€ , la tva est de 33 % et le prix TTC est de {prix_ht*tva_choosen}€")
else :
    print("Veuillez recommencer avec un chiffre entre 1 et 3")
    

