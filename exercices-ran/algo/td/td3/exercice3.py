# Saisissez un nombre compris entre 1 et 10. En cas d’erreur de saisie, il y a affichage d’un message «
# Valeur non permise ». Si le nombre est égal au nombre magique connu du programme, il affiche «
# Gagné » sinon il affiche un message « Trop petit » ou « Trop grand » suivant la valeur saisie.
# (reprise de « Chiffre magique 1 » pour utiliser des boucles)

import random

numberRandom= random.randint(1,100)
userTry=0
userTryMax=10

while userTry != userTryMax:
    number= input("Veuillez saisir un nombre: ")
    userTry=userTry+1
    if number.isdigit():
        number= int(number)
        if number == numberRandom:
            print("Vous avez gagné !")
            break
        else:
            if userTry > userTryMax:
                 print("Perdu")
            if number < numberRandom:
                print("Plus grand !")
            else:
                print("Plus petit !")