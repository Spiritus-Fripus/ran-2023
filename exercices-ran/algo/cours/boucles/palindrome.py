#palindrome
mot= input("mot: ")
pal= ""

for i in range(0,len(mot)):
     pal= pal + mot[len(mot) -1 -i]
print(f"Mot inversé: {pal}")

if mot == pal:
     print("c'est un palindrome")
else:
     print("NEIN ! NICHT EIN PALINDROME")
