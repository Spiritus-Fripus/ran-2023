# Langage de Programmation

1. Analyse des besoins
	- les développeurs travaillent en étroite collaboration avec les clients
2. Conception
	- plan détaillés dans les logiciels (maquettes)
3. Implementation
	- Code
4. Test et débogage
	- Test en corrections en tout genre
5. Documentation
	- Faire une doc
6. Déploiement
	- Déploiement du logiciel/mise en ligne
7. Maintenance 
	- Par rapport au logiciel et demandes du client

- _Difference entre language de bas niveau et de programmation:_
	- Lisibilité et compréhension
	- Productivité
	- Portabilité
	- Framework/Bibliothèque
	- sécurité/stabilité

--- 
# ET Inclusif / OU Exclusif

1. **ET (AND) :** L'opérateur logique "ET" (AND en anglais) est utilisé en logique binaire pour combiner deux valeurs ou expressions. Lorsque vous utilisez l'opérateur "ET", le résultat est vrai (1) uniquement lorsque les deux valeurs ou expressions en question sont vraies (1). Si l'une ou l'autre est fausse (0), le résultat est faux (0). En logique symbolique, "ET" est généralement représenté par le symbole "&" ou "∧".

2. **OU (OR) :** L'opérateur logique "OU" (OR en anglais) est utilisé en logique binaire pour combiner deux valeurs ou expressions. Avec l'opérateur "OU", le résultat est vrai (1) si au moins l'une des deux valeurs ou expressions est vraie (1). Si les deux sont fausses (0), le résultat est faux (0). En logique symbolique, "OU" est généralement représenté par le symbole "|" ou "∨".

3. **Inclusif (ET) :** Lorsque vous dites "ET inclusif", cela signifie que vous incluez les deux conditions dans la réponse. C'est essentiellement la même chose que l'opérateur "ET" dans la logique binaire, où les deux conditions doivent être vraies pour que la réponse soit vraie.

4. **Exclusif (OU) :** Lorsque vous dites "OU exclusif", cela signifie que vous choisissez l'une ou l'autre condition, mais pas les deux en même temps. En logique binaire, cela correspond à l'opérateur "OU exclusif" (XOR), où le résultat est vrai (1) si exactement l'une des deux conditions est vraie, mais pas les deux. Si les deux conditions sont vraies ou fausses, le résultat est faux (0).

## _Exemple:_ 

Pour illustrer l'utilisation des opérateurs logiques binaires (ET, OU, inclusif, exclusif) dans un tableau binaire, nous pouvons utiliser un tableau de vérité. Un tableau de vérité montre toutes les combinaisons possibles de valeurs d'entrée et le résultat de l'opération logique. Voici un exemple simple :

Supposons que nous ayons deux variables binaires, A et B, et que nous souhaitions explorer les opérations logiques ET, OU, inclusif et exclusif entre elles.

1. Variables d'entrée :
   - A = 1 signifie que la variable A est vraie.
   - B = 0 signifie que la variable B est fausse.

2. Opérations logiques :
   - ET (AND)
   - OU (OR)
   - Inclusif (ET inclusif)
   - Exclusif (OU exclusif)

Voici le tableau de vérité correspondant :

| A | B | A ET B | A OU B | A ET OU B | A OU EXCLUSIF B |
|---|---|-------|-------|-----------|-----------------|
| 0 | 0 |   0   |   0   |     0     |       0         |
| 0 | 1 |   0   |   1   |     1     |       1         |
| 1 | 0 |   0   |   1   |     1     |       1         |
| 1 | 1 |   1   |   1   |     1     |       0         |

Dans ce tableau de vérité, chaque ligne représente une combinaison de valeurs possibles pour les variables A et B. Les colonnes suivantes montrent les résultats des opérations logiques correspondantes pour chaque combinaison.

- A ET B (AND) est vrai (1) uniquement lorsque les deux variables sont vraies (1).
- A OU B (OR) est vrai (1) si au moins l'une des deux variables est vraie.
- A ET OU B (Inclusif) est vrai (1) si au moins une des deux variables est vraie, y compris lorsque les deux sont vraies.
- A OU EXCLUSIF B (Exclusif) est vrai (1) lorsque exactement une des deux variables est vraie, mais pas les deux.

Cela illustre comment les opérations logiques binaires fonctionnent en utilisant un tableau de vérité avec des variables binaires A et B.

--- 
# Différents langages

```#
pour i de 0 à 4
	ecrire i 
fpour
```
```python
for i in range(5)
	print(i)
```
```c++
for (int i=0; i <5; i++) {
const << i << endl;
}
```
```java
for (int i=0; i<5; i++) {
system.out.print/n (i)
}
```
```js
for (let i=0; i<5 , i++) {
console.log(i);
}
```
```c#
for (int i=0; i<5;i++) {
console.Writeline(i);
}
```
--- 
