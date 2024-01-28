**If** (Si) _condition_ alors
	instruction
Fin **if**
_condition_ =  **Opération logique avec des opérateurs logique (AND/OR) et des opérateurs de comparaison.**
// Si la condition est _vérifiée_ (**vraie**)  on effectue un ou plusieurs traitements //
**SON RESULTAT DONNE TOUJOURS UN BOOLEEN**

_exemple:_ 
Est Majeur ? 
```python
if age >= 18:
	print("Vous êtes majeur")
if age < 18:
	print("Vous êtes mineur")
```
On peut simplifier cette opération avec **ELSE**
```python
if age >= 18:
	print("Vous êtes majeur")
else:
	print("Vous êtes mineur")
	
```
**ELSE** _(si non)_ Réalise de manière implicite **l'inversion** de la condition age _>= 18_

--- 
# Boucle FOR (boucle comptée)

Une boucle comptée et une boucle qui évolue d'un début jusqu'à une fin 
Pour **variableDeComptage** allant de _début_ à _fin_ _faire_
			Initialisée à **deb** et va s'**incrémenter** de 1 jusqu'à être égal à fin

```python
#Pseudo code
Pour i allant de 0 à 5, faire
	afficher(i)
			-----------------------------
#Python
for i in range(0,5):
	print(i)
```

mot="Hello"
```python
for i in range(0,len(mot)):
```

0,1,2,3,(4) -> last index
H,e,l,l,o

Dans une chaine de caractère on dit que ce sont des "index"
"len" est une fonction qui donne le nombre de caractère d'un mot
Pour connaitre la longueur d'un mot on utilise la formule len(mot)-1
mot[1] -> e 

```python
for i in range(0, len(mot)):
	print(mot[i])
```

les crochet "[]" permettent de verifier un mot lettre par lettre

---
