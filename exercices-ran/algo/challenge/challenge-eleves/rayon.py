# Ecrire un programme qui demande un nombre de rayons
# stocker le nom des rayons
# pour chaque rayon demander 3 produits

rayon_nbr = int(input("Nombre de rayons ?: "))

rayon_list= []
for i in range(rayon_nbr):
    rayon = input(f"Nom du rayon {i + 1 }: ")
    rayon_list.append(rayon)

produit_list= []
for i in range(len(rayon_list)):
    produit_rayon=[]
    print(f"Rayon : {rayon_list[i]}")
    for j in range(3):
        produit = input(f"veuillez rentrer le produit {j + 1} de {rayon_list[i]}:  ")
        produit_rayon.append(produit)
    produit_list.append(produit_rayon)
    print(f"Rayon : {rayon_list[i]}")
    print(f"Produit : {produit_list[i]}")
    print()
    

print(rayon_list)        
print(produit_list)

