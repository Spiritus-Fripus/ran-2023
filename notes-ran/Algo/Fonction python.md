Une fonction est un sous programme qui permet de définir une série d'instruction qui vont s'effectuer les unes après les autres.
On peut prendre l'exemple d'un jeu vidéo , une fonction start() permettrai de démarrer le jeu ou une fonction checkwin() permettrai de détecter la victoire de tel et tel joueur.
Les fonctions ont un rôle important dans les algorithme car elle permettent de répondre à un problème afin d'obtenir le résultat attendu.
Il est possible de créer une bibliothèque de fonction réutilisable dans divers programme grâce aux imports.

voici quelques exemples de fonctions sous python :

```python
# Exemple d'un programme permettant de calculer l'année prochaine a partir de l'année actuelle

# on utilise def pour definir notre fonction
def next_year():
# year est notre variable locale
	year = 2023
# on donne le résultat de la variable year
	print("fin de l'année", year)
	year +=1
# on donne le résultat de la variable year + 1
	print("début de l'année", year)

#on appelle la fonction
next_year()
```

Il est possible d'utiliser une variable globale propre aux programme en cours en utilisant la fonction global

```python
# Exemple d'un programme permettant de calculer l'année prochaine a partir de l'année actuelle

# on utilise def pour definir notre fonction
def next_year():
# year est notre variable globale
	global year
# on donne le résultat de la variable year
	print("fin de l'année", year)
	year +=1
# on donne le résultat de la variable year + 1
	print("début de l'année", year)

# on définie la variable globale
year = int(input("saisir l'année: "))
# on appelle la fonction
next_year()
```

Les fonctions sous toujours définie au début de notre programme ou dans une bibliothèque.

Il est possible de définir plusieurs fonction du même nom :

```python
# on definie nos addition
def addition1():
	return 5 + 5
def addition2():
	return 5 + 2
def addition3():
	return 5 + 3

print("le résultat du calcul est", addition1())
print("le résultat du calcul est", addition2())
print("le résultat du calcul est", addition3())

# c'est redondant
# pour simplifier on peut utiliser n dans la fonction
def addition(n):
	return 5 + n
print("le résultat du calcul est", addition(2))
print("le résultat du calcul est", addition(6))
print("le résultat du calcul est", addition(7))
```

Création d'une fonction avec condition :

```python
# créer une fonction max() qui va définir le plus haut parmis 2 valeurs
def max(a, b):
# si a est supérieur a b on retourne la valeur de a
	if a > b:
		return a
# sinon on retourne la valeur de b
	else:
		return b

a = int(input("entrer la valeur de a: "))
b = int(input("enter la valeur de b: "))
max_value = max(a,b)

print("la valeur max est", max_value)
```

Fonction récursive (une fonction qui s'appelle elle même), possibilité de créer des boucles en appelant la fonction dans la fonction:

```python
# création d'une fonction récursive
def add(a):
	a += 1
	print(a)
# récusivité en appelant la fonction
	add(a)
# le programme va boucler a l'infini en ajoutant +1 a la variable a
add(1)

#-------------------------------------------------------------#

# on peut donner une limite a ce programme avec une conditon
def add(a):
	a += 1
	print(a)
# limite
	if a < 100:
		add(a)
# le programme va s'arreter a 100
add(1)
```
