# For

**Variable de comptage**
for **i** in range (_start, end_):
**i** va être automatiquement incrémenté de 1 à chaque tour de boucle **i=i+1**
**i** sera initialisé à _start_ la boucle s'arrête quand **i == end**

_Exemple:_

```python
for i in range(0,5)
	print("tour n°, i")
```

```python
mot="azerty"
#azerty
#012345 6 lettres
for i in range(0,len(mot)):
	print(mot[i],i)
```

**nom_fonction**(_param_)
une fonction va faire un traitement sur des paramètre afin d'obtenir un résultat
**len**(_mot_) 
la fonction **len** va nous donner la longueur

# Double Loop

```python
mot="Hello"
for i in range(0,5)
	for j in range(0,5)
	print(i,j)
```

| i   | j   | mot[i] | mot[j] |
| --- | --- | ------ | ------ |
| 0   | 0   | **H**     | **H**      |
| 0   | 1   | H      | e      |
| 0   | 2   | H      | l      |
| 0   | 3   | H      | l      |
| 0   | 4   | H      | o      |
| --- | --- | ---    | ---    |
| 1   | 0   | e      | H      |
| 1   | 1   | **e**      | **e**     |
| 1   | 2   | e      | l      |
| 1   | 3   | e      | l      |
| 1   | 4   | e      | o       |

# While

Boucle _while_ (tant que)
= Boucle conditionnelle 
= Fonctionne avec une condition de boucle

```python
while condition : -------> # on boucle si la condition est vérifiée
	instruction : 
```

_Exemple:_

```python
i = 0
while i < 10 :
	print(i)
	i += 1
```
