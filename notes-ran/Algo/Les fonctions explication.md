# Fonction

## Utilisation

1. _Pourquoi ?_
   1. Réutiliser des traitements
   2. Eviter les répétitions
   3. Gagner du temps
   4. Réduire le code (plus lisible)
2. _Quand ?_
   1. Il y a des traitements répétitifs
   2. Trop de lignes

---

## Fonction vs Procédure

La **fonction** retourne une valeur
La **procédure** effectue des traitements sans retourner de valeurs

_Exemple:_

**Fonction**

```python
def somme(a,b):
	return a + b
res = somme(5,4)
```

```python
print(res)
```

**Procédure**

```python
def somme(a,b):
	print(a+b)
```

```python
somme(4,5)
```
