# Les variables

- Permettent de mémoriser des valeurs
- boite dans laquelle on peut déposer ou y lire une valeur
- Cette boite doit être étiquetée par un nom de variable
- Ensemble de noms de variables valides:
  - NbreJour, Moy, Date, Resultat_01, Nom_Famille

(une variable est toujours explicite)

(pas d’espace et ne commence pas par un chiffre)

- Exemple :
  1. CamelCase ou PascalCase (pas d’espace et Majuscule)
     1. →DateDuJour
  2. kebab-case (séparation par trait d’union)(trés peu utlisé a part pour les noms de fichier)
     1. date-du-jour
  3. snake_case (underscore)(utilisé en python)
     1. date_du_jour

## Les variables: l’affectation

- Affectation = attribuer un contenu a une variable
- dans l’écriture d’un algo , elle est symbolisée par “←” selon la syntaxe
  - NomVariable ← Valeur
- ici Valeur est évaluée puis stockée dans la variable nommée
  - NomVariable remplacant ainsi son ancien contenu

(évaluée de haut en bas et de droite a gauche)

## Les variables : exemple d’affectation

- N ← 7 // N prend la valeur 7
- Mess ← “Bonjour” // Met dans la variable Mess la chaisne de caractères Bonjour
- A ← B // A reçoit la valeur de la variable B
- Res ← Nb1+Nb2 // additionne les contenus des variables Nb1 et Nb2 et met les résultat dans Res
- P← P+2 // Ajoute 2 au contenu de P et met le résultat dans P

variables :

a, b, c, d,: **Entiers**

Debut:

a ←5

b ← 2

c ←a+1

d ←b+a

a ← 2

b ← c

c ←c+2

sortie:

a=2 b=6 c=8 d=7

(pour résoudre lire de haut en bas en respectant les valeurs a chaque étapes)

## Typages

- 4 types de variables:
  - entier : les nombres entier (1,50,1600 etc …)
  - Réel : nombre a virgule (2.5, 3.8 etc…)
  - Chaines de caractères : “entre guillemet” , “3.14”
  - Booléen : Vrai/Faux, 0/1, true/false

**Avant leurs utilisation , les variables doivent toujours être initialisées !**

(par une affectation ou une saisie)
