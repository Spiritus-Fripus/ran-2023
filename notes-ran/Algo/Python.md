# Python

## Programme Somme

```python
# Programme Somme
a = int(input("veuillez saisir un nombre:"))
b = int(input("veuillez saisir un nombre:"))
somme = a + b 
print("La somme est de",somme)
```

## Commandes

Pour transformer une variable en chaine de caractères, utiliser la commande “string” **str**

exemple:
Str(5) —> ”5”

Pour transformer une chaine de caractères en variable , utiliser la commande int

exemple:
Int(”5”) —> 5

Pour transformer une variable ou chaine de caractères en Booléen, utiliser **bool**

exemple:
bool(”4”) —> True
bool(2) —> True
bool(0) —> False

Pour transformer une variable ou une chaine de caractères en réel , utiliser la commande **float**

exemple:
float(5)+(0.1) —> 5.1
float(”5.1”) —> 5.1

En **Python**, pour éviter de devoir couper une chaine de caractère afin d'afficher des valeurs  
on utilise "**f**" (pour formatted) juste avant les guillemets et les "**{}**" autour de la variable en question  
Exemple :

```python
a = float(input("saisir un nombre: "))
b = float(input("saisir un nombre: "))

print(f"le résultat de {a} + {b} est {a + b})
```

En **python** pour avoir la date actuelle (sans devoir actualiser) il faut utiliser

```python
# Import de la librairie date time
import datetime
# Obtenez la date actuelle
current_date = datetime.date.today()
# Obtenez l'année en cours a partir de la date actuelle
current_year = current_date.year
birth_year = int(input("Veuillez saisir votre année de naissance en chiffres : "))

print(f"Vous avez {current_year-birth_year} ans")
```

**//Attention les imports sont toujours en début de code//**

Exemple de table de vérité en **python**:

```python
a=true
b=false
c=true
d=true
not(a or b) and c or not(c or d ) and a
```

**not** représente l'inverse  
exemple:  
**not** (a or b) = **not**(a) and **not**(b)  
**not** (a and b) = **not**(a) or **not**(b)
