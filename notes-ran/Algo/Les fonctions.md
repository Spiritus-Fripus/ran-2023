# Fonction

## FLOAT:

```python
float(): permet de convertir en nombre réel (flottant)
```

Exemple:

1. float(3.14) → 3.14 (un réel reste un réel)
2. float(42) → 42.0 (un entier devient un réel)
3. float(”3”) → 3.0 (une chaine de caractère nominale devient un réel)
4. float(”4.2”) → 4.2 (une chaine de caractère avec un nombre réel devient un réel)
5. float(”Hello”) → Error (impossible de traduire une chaine de caracère alaphabétique en réel)
6. float(True) → 1.0 (True devient un nombre réel (1.0))
7. float(false) → 0.0 (False devient un nombre réel (0.0))

## STR:

```python
str(): permet de convertir en chaîne de caractère 
	str veut dire string
```

Exemple:

1. str(”hello”) → Hello (une chaine de caractère reste une chaine de caractère
2. str(3) → “3” (un entier devient une chaine de caractère)
3. str(3.14) → “3.14” (un réel devient une chaine de caractère)
4. str(test) → “test” (une variable devient une chaine de caractère)
    
    **Il n’y a pas d’erreurs avec une chaine de caractère car c’est le modèle par défaut !**
    

```python
float("Hello") + ("5") -> "Hello5"
	La seule opération possible en str est la concaténation (+)
```

## BOOL:

```python
bool(): permet de convertir en booléen
	bool veut dire boolean
```

Exemple:

1. bool(True) → True (un booléen reste un booléen)
    1. bool(False) → False
2. bool(1) → True (un entier de 1 devient un booléen)
3. bool(0) → False (un entier de 0 devient un booléen)
4. bool(”Hello”) → True (la chaine de caractère est défini donc elle devient un booléen)
5. Bool(””) → False (la chaine de caractère n’est pas défini donc elle vient un booléen)
6. bool(”42”) → True (un entier supérieur a 0 devient un booléen)
    
    Un entier supérieur à 0 devient True 
    
    Tout ce qui est défini devient True , tout ce qui ne l’est pas devient False
    

```python
int("4") * str(5) + float(bool(inter(3.4)))
	-> 4 * "5" + 1.0
		-> "5555" + 1.0 
			-> Error 
	Python authorise la multiplication de chaine de caractère
	Toujours utiliser le "*" a la place de "x" pour une multiplication
```

## INT:

```python
int(): permet de convertir une variable ou une valeur en entier
	int veut dire **integer**
```

Exemple:

1. int(3) → 3 (Un entier convertie en entier reste entier)
2. int(3.14) → 3 (Un nombre réel devient un entier)
3. int(”4”) → 4 (Une chaine de caractère devient un entier)
4. int(”Hello”) → Error (impossible de convertir de l’alphabétique en entier)
5. int(”4.5”) → Error (impossible de traduire une chaine de caractère avec un nombre réel en entier)
6. Int(True) 
    1. Int(False) → Error (impossible de traduire un booléen en entier)
## Round: 
```python
a = 12.35353535
b = 17.12424242
c= a + b
print(f"Le résultat de a + b est {round(c, 2)}")
```
**Round** permet d'arrondir les _float_ , si on ajoute une **","** ainsi qu'un chiffre , on définie le nombre de chiffres après la virgule.
