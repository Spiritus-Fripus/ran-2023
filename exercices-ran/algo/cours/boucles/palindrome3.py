word= input("Saisir un mot: ")
# on essai d'inverser le mot
drow = ""
for letter in word: 
    drow = letter + drow

print(drow) 
if word == drow:
    print("C'est un palindrome")
else:
    print("Ce n'est pas un palindrome")
