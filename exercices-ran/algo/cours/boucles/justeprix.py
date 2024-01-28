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