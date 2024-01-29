# Tableaux

syntaxe : tab=[ ] # tableau vide.
En python un tableau et une liste c'est la même chose.
Le tableau permet de stocker plusieurs chose contrairement à une variable
Un tableau est une variable !

_Exemples:_

```python
tab= [1,2,3]
tab= ["a","b","c"]
tab= ["a",1,True,4.4]
```

**Dans un tableau on peut faire 4 choses :**

```python
tab = ["a","b","c"]
```

1. Lire une valeur :

```python
tab[1] -------> # "b"
```

2. Ajouter une valeur:

```python
tab = tab + ["d"] -------> # ["a","b","c","d"]
tab.append("d")   -------> # ["a","b","c","d"] (méthode objet)
```

3. Modifier une valeur:
   **_// Pour modifier une valeur il faut connaitre l'index ou elle se situe //_**

```python
tab[2] = "e" ------> # ["a","b","e","d"]
```

4. Supprimer une valeur :

```python
del(tab[0])  ------> # ["b","e","d"]
```
