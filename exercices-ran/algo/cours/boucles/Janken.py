import random

jankenRound=5
option= ["pierre","feuille","ciseaux"]
userScore = 0
botScore= 0

while userScore < jankenRound and botScore < jankenRound :
        userChoice= input("Que voulez vous jouer ? (pierre,feuille,ciseaux): ")

        if userChoice not in option:
            print("PIERRE OU FEUILLES OU CISEAUX !!!")
            continue
        botChoice=random.choice(option)

        if userChoice == botChoice:
            print("égalité")
        elif userChoice == "pierre" and botChoice=="ciseaux" \
        or userChoice == "ciseaux" and botChoice=="feuille" \
        or userChoice == "feuille" and botChoice=="pierre":
            print(f"Vous remportez la manche, {userChoice} bat {botChoice}")
            userScore +=1
        else:
            print(f"Vous perdez la manche, {botChoice} bat {userChoice}")
            botScore +=1
        print(f"Résultat user: {userScore} et bot: {botScore}")

if userScore == jankenRound:
    print("Vous avez gagné !")
else:
    print("C'est perdu !")