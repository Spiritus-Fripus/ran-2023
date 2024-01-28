word = input("saisir un mot : ")
cpt= 0
for i in range(0, len(word)):
    #Comparer les lettres au fur-et-à-mesure dans les deux sens
    if word[i] == word[len(word) -1 -i]:
        cpt = cpt+1
    else:
        break #on sort de la boucle
if cpt == len(word):
    print("C'est un palindrome.")
else:
    print("Ce n'est pas un palindrome.")
