# 1ere Méthode

```python
word = input("saisir un mot : ")

cpt= 0

for i in range(0, len(word)):

    #Comparer les lettres au fur-et-à-mesure dans les deux sens

    if word[i] == word[len(word) -1 -i]:

        cpt = cpt+1

    else:

        break #On sort de la boucle

if cpt == len(word):

    print("c'est un palindrome.")

else:

    print("ce n'est pas un palindrome.")
```

# 2eme méthode

```python
word= input("Saisir un mot: ")

# on essai d'inverser le mot

drow = ""

for letter in word:

    drow = letter + drow



print(drow)

if word == drow:

    print("c'est un palindrome")

else:

    print("ce n'est pas un palindrome")
```
