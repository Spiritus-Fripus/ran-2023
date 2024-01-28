## Définition

Programmation orientée objet :
- pouvoir faire de la programmation modulaire
- imaginée comme des lego (changer un lego = pas grand impact)

!= Procédurale :
- maintenabilité (- -)
- imaginée comme des cube (si l'on change un cube = structure instable)

**Objet** :
- caractéristiques ( propriétés, attributs)
- actions (méthodes)

_exemple_: 

Bouteille 
- caractéristique (bouchon , corp)
- action (vidée, remplir)

Humain : 
- caractéristique (corp , main , pied , jambes etc... )
- action (marcher , manger, prendre etc ...)


```python
class Personne:
	def __init__(self):
		self.nom = "Doe"
		self.prenom = "John"
```

// !

Pour appeler des objets , on utilise des class 

**Class** = représentation d'un objet , l'objet est indépendant (peut être vu comme un moule) **c'est la caractéristique commune des objet** 
**// ! OBLIGATION DE COMMENCER UNE CLASS PAR UNE MAJUSCULE ! //**
// ! Une class est dans un fichier a part ! //

**méthode** = fonction dans une class

**constructeur** = _ _ init _ _ (magic méthode) (fonction magique) (ne pas changer)
self= ref vers l'objet courant  exemple -> self.objet = (self est une fonction) (ne pas changer)

// !

```python
personne_A = Personne()
```

C'est une instanciation 
La variable personne_A  appelle la class Personne

Version amélioré :

```python
class Personne:
	def __init__(self,nom,prenom):
		self.nom = nom
		self.prenom = prenom
		
personne_A = Personne("Doe","John")
print(personne_A)
```

## Les 4 principes de la POO

**ENCAPSULATION:**
- Fait que un objet ait des propriétés et des méthodes 

**POLYMORPHISME:**
- Différentes class peuvent avoir un nom de méthodes qui est le même 

**ABSTRACTION:** 
- Le fait de réduire les détails au dev/user 
	- exemple:
		- Humain = Homme , Femme
		- != Univers = Constellation =  Systeme = Planete = Terre , Mars , Jupiter etc ... 

**HÉRITAGE:**
- Création de Class parents enfants ! 
	- exemple : 
		- Humain = homme = adolescent = torse , main , tete , bras etc ....