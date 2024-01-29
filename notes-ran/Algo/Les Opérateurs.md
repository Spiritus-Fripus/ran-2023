# Opérateurs logiques

- Sur les variables réelles :
  - Les opérations classiques : addition , soustraction, multiplication, division, puissance
  - Avec respect des priorités usuelles : addition> soustraction>multiplication>division>puissance
- Sur les variables entières:
  - Addition , soustraction et multiplication OK
    - Cas particulier pour la division : on utilisera div pour le quotient , et mod pour le reste (ex: 17 div 3) renvoie 5 et (17 mod 3) donne 2)
- Sur les chaines de caractères : une seule opération possible
  - La concaténation avec “+”

Exemple:

A ← “salut,”

B ← A+ “tu vas bien ?”

B contiendra : “Salut , tu vas bien ?”

Exemple 2:

entrée:

a ← “A”

b ← “Hello”

c ← b+a

a ← c+ “world”

d ← “3”

b ← “3”+”1”

sortie:

| a              | b       | c        | d   |
| -------------- | ------- | -------- | --- |
| “A”            | n.a     | n.a      | n.a |
| “A”            | “Hello” | n.a      | n.a |
| “A”            | "Hello” | “HelloA” | n.a |
| "HelloA world” | "Hello” | "HelloA” | n.a |
| “HelloA world” | "Hello” | "HelloA” | "3” |
| “HelloA world” | “31”    | “HelloA” | “3” |

**Attention : Impossible d’additionner une chaine de caractère avec un entier**

exemple : “5” + 4 ou “Hello”+2

- Sur les booléens : opérateurs logiques

  - ET , OU et NON

  | x    | y    | x ET y | x OU y | NON x | NON y |
  | ---- | ---- | ------ | ------ | ----- | ----- |
  | Vrai | Vrai | Vrai   | Vrai   | Faux  | Faux  |
  | Vrai | Faux | Faux   | Vrai   | Faux  | Vrai  |
  | Faux | Faux | Faux   | Faux   | Vrai  | Vrai  |

- Les Opérateurs: ET , OU - On peut dire que ET est égal a une multiplication - On peut dire que OU est égal a une addition

# Opérateurs de comparaison

**Résultat Booléen**

- ==
  - Vérifie si 2 valeurs sont strictement identiques
- !=
  - Vérifie si 2 valeurs sont différentes
- >
  - Vérifie si 2 valeurs sont strictement supérieurs
- <
  - Vérifie si 2 valeurs sont strictement inférieurs
- ( >= )
  - Vérifie si la valeur est supérieur ou strictement égale (> ou == )
- ( <= )
  - Vérifie si la valeur est inférieur ou strictement égale (< ou == )
