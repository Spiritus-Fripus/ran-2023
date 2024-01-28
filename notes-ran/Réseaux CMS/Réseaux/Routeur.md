_Objectif du routeur:_

Séparer le réseau privé du réseau public

La seule chose connecté à internet est le routeur (Seul équipement branché sur le réseau physiquement)

_Exemple d’une Box:_

→ Routeur  → Sortie internet (Prise)
→ Switch
         → Disque Dur
→ Wifi

_Exemple du modèle de l'école:_

- Switch
	- B1 (wifi)
	- B2 (wifi)
	- B3 (wifi)
		- Utilisateur 

 Les borne wifi de l'école communiquent entre elles pour ne donner qu'un seul et même réseaux et se permettent de dispatcher les utilisateurs entre les bornes en cas que surcharge (**ROMAINING**) ou déplacement de l'utilisateur 


_Exemple de réseau sécurisé :_

- Routeur Internet (http: 80, https: 443)
	-  **Zone DMZ** (Démilitarisée)
		- Switch 
			- Serveur WEB (**Bastion**)
- Routeur LAN
	- Switch

*En cas d'attaque,  la première zone (zone DMZ) sert de sécurité et permet de détecter les intrusion avant l'attaque du réseau LAN* 
