# Lecture / Ecriture

- Communiquer avec l’utilisateur
- La lecture d’une donnée saisie au clavier :
    
    NomVariable ← saisir()
    
    !!! le programme se met en attente d’une entrée pour pouvoir continuer !!!
    
    (On peut afficher un message lors d’une saisie avec l’instruction : saisir(”message”)
    
- L’écriture d’un résultat/message :
    
    afficher(”bonjour”)   // l’écriture d’une chaine de caractère
    
    afficher (Bonjour)    // l’écriture d’une variable
    

Exemple :

a ← saisir(”Veuillez saisir un nombre:”)

b ← saisir(”Veuillez saisir un nombre:”)

somme ← a+b

Afficher(”La somme est de”, somme)

**//Ici somme et Afficher sont des variables//**

Attention pas d’espace entre saisir et la parenthèse
