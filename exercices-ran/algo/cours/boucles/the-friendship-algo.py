#the friendship algorithm
print("Answer only by 0/1: ")
phoneCall=int(input("Let's make a phone call: "))
if phoneCall == 1:
    home=int(input("Is somebody home ?"))
    if home == 0: 
        print("Ok i'll leave a message and wait for callback")
        callback=1 
        print("Oh he's calling back !")
    if home ==1 or callback ==1:
        meal=int(input("Would you like to share a meal ?: "))
        if meal == 1:
            print("Let's get diner together: friendship begin")
            exit(1)
        elif meal == 0:
            hotBeverage=int(input("Do you enjoy a hot beverage ?: "))
            if hotBeverage == 1:
                tea=int(input("Tea ?: "))
                if tea ==1:
                    print("Friendship begin")
                    exit(1)
                elif tea == 0:
                    coffee=int(input("Cofee ?: "))
                    if coffee== 1:
                        print("Friendship begin")
                        exit(1)
                    elif coffee == 0:
                        cocoa=int(input("Cocoa ?: "))
                        if cocoa == 1:
                            print("Friendship begin")
                            exit(1)
                        else:
                            print("Not friends")
                            exit(1)
            elif hotBeverage==0:
                print("Recreationnal activity tell le one of your interests.")
                for i in range(1,8):
                    shareInterest=int(input("Do i share that interest ?"))
                    if shareInterest == 1:
                        print("Why don't we do that together ?: friendship begin")
                        exit(1)
                    elif shareInterest == 0:
                        if i > 6:
                            chooseInterest=int(input("Let me choose the least objectionable interest (0/6): "))
                            if chooseInterest >= 1 <=6:
                                print("Ok why not: friendship begin")
                                exit(1)              
else:
    print("Not friends")
    exit(1)