# Ecrire un algorithme permettant de trier une liste d'entier (saisies au clavier) dans l'ordre croissant.

nombre = [8,5,6,3,5,2,0,76,48,2,900]
nombre_copy = []

for i in range(0,len(nombre) -1):
    for j in range(0,len(nombre) -i -1):
        if nombre[j] > nombre[j+1]:
            nombre_copy = nombre[j]
            nombre[j] = nombre[j+1]
            nombre[j+1] = nombre_copy
print(nombre)