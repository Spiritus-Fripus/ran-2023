# Adresse IP

Objectif : faire communiquer 2 machines entre elles
	**Adresse unique** (Techniquement)
	
- Pour connaître son adresse IP
	- ouvrir cmd(invite de commande)
		- ipconfig
			- adresse IP v4

Adresse IP v4 (ex:192.168.1.N) (allouée par le réseau)
Masque sous réseau (255.255.255.0)
Passerelle par défaut (192.169.1.1) **(si collé dans le navigateur donne accès a l'interface administrateur de la BOX)**

- Pour connaitre son ping
	- ipconfig
_Exemple:_
```shell
C:\Users\N-web>ipconfig

Configuration IP de Windows


Carte Ethernet Ethernet 3 :

   Suffixe DNS propre à la connexion. . . :
   Adresse IPv6 de liaison locale. . . . .: fe80::dc4e:1420:9740:3307%18
   Adresse IPv4. . . . . . . . . . . . . .: 192.168.56.1
   Masque de sous-réseau. . . . . . . . . : 255.255.255.0
   Passerelle par défaut. . . . . . . . . :

Carte réseau sans fil Connexion au réseau local* 1 :

   Statut du média. . . . . . . . . . . . : Média déconnecté
   Suffixe DNS propre à la connexion. . . :

Carte réseau sans fil Connexion au réseau local* 2 :

   Statut du média. . . . . . . . . . . . : Média déconnecté
   Suffixe DNS propre à la connexion. . . :

Carte réseau sans fil Wi-Fi :

   Suffixe DNS propre à la connexion. . . : mns.lan
   Adresse IPv6 de liaison locale. . . . .: fe80::564d:ec8f:cb46:2728%10
   Adresse IPv4. . . . . . . . . . . . . .: 172.16.1.180
   Masque de sous-réseau. . . . . . . . . : 255.255.255.0
   Passerelle par défaut. . . . . . . . . : 172.16.1.254

Carte Ethernet Connexion réseau Bluetooth :

   Statut du média. . . . . . . . . . . . : Média déconnecté
   Suffixe DNS propre à la connexion. . . :
```
- Pour connaitre un ping 
	- cmd
		- ping 192.168.1.1 (ou un nom de domaine)

_Exemple_ : 
```shell
C:\Users\N-web>ping www.whitehouse.gov

Envoi d’une requête 'ping' sur wh46.go-vip.net [192.0.66.168] avec 32 octets de données :
Réponse de 192.0.66.168 : octets=32 temps=30 ms TTL=53
Réponse de 192.0.66.168 : octets=32 temps=32 ms TTL=53
Réponse de 192.0.66.168 : octets=32 temps=30 ms TTL=53
Réponse de 192.0.66.168 : octets=32 temps=30 ms TTL=53

Statistiques Ping pour 192.0.66.168:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 30ms, Maximum = 32ms, Moyenne = 30ms
```
- Pour connaitre un ping au delà du routeur
	-  cmd
		-  ping 8.8.8.8 (réseau google)
_Exemple_ : 
```shell
C:\Users\N-web>ping 8.8.8.8

Envoi d’une requête 'Ping'  8.8.8.8 avec 32 octets de données :
Réponse de 8.8.8.8 : octets=32 temps=28 ms TTL=113
Réponse de 8.8.8.8 : octets=32 temps=26 ms TTL=113
Réponse de 8.8.8.8 : octets=32 temps=27 ms TTL=113
Réponse de 8.8.8.8 : octets=32 temps=28 ms TTL=113

Statistiques Ping pour 8.8.8.8:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 26ms, Maximum = 28ms, Moyenne = 27ms
```
Permet de savoir si l'on est connecté au réseau internet 

http://www.mon-ip.com/ permet de connaitre l'**IP public** du routeur

**65635** entrée sur une carte réseau , chacune correspond à un protocole , on peut mettre plusieurs protocole sur une entrée:
**// http 80 //**
**// https 443 //**

La commande **tracert** permet de lister tout les équipement et serveurs utilisé vers un point d'accès

_Exemple :_
```shell
C:\Users\N-web>tracert www.whitehouse.gov

Détermination de l’itinéraire vers wh46.go-vip.net [192.0.66.168]
avec un maximum de 30 sauts :

  1     2 ms     1 ms     2 ms  pfSense.mns.lan [172.16.1.254]
  2     3 ms     3 ms     2 ms  192.168.1.254
  3    19 ms    18 ms    18 ms  193.253.157.83
  4    24 ms    23 ms    24 ms  lag-44.str2-ig7.strasbourg.transitip.raei.francetelecom.net [81.52.73.54]
  5     *       23 ms    22 ms  intf-fogi-str2-ig7.nmstr206.rbci.orange.net [193.252.137.249]
  6    24 ms    23 ms    25 ms  ae22-0.ncstr102.rbci.orange.net [193.252.162.10]
  7    20 ms    21 ms    22 ms  ae43-0.nistr202.rbci.orange.net [193.252.160.113]
  8    28 ms    28 ms    29 ms  81.253.184.190
  9     *        *        *     Délai d’attente de la demande dépassé.
 10     *       33 ms    32 ms  ae1.3112.ear4.Paris1.level3.net [4.69.133.170]
 11    32 ms    32 ms    32 ms  213.242.126.94
 12    30 ms    30 ms    29 ms  192.0.66.168

Itinéraire déterminé.
```
 
### Protocoles d'adresse IP

Les protocoles d'adresse IP (Internet Protocol) sont un ensemble de normes qui permettent d'attribuer des adresses uniques à chaque appareil connecté à un réseau IP, facilitant ainsi l'acheminement des données sur Internet. Les deux versions les plus couramment utilisées sont IPv4 (Internet Protocol version 4) et IPv6 (Internet Protocol version 6), bien qu'il existe d'autres protocoles IP moins couramment utilisés. Voici une brève description de ces deux versions :

1. **IPv4 (Internet Protocol version 4)** :
   - IPv4 est la version la plus répandue d'IP et utilise des adresses IP de 32 bits.
   - Les adresses IPv4 sont généralement représentées sous forme de quatre nombres décimaux séparés par des points, par exemple, 192.168.1.1.
   - L'épuisement des adresses IPv4 a conduit à la transition vers IPv6, car le nombre limité d'adresses IPv4 disponibles ne suffit plus à l'expansion continue d'Internet.

2. **IPv6 (Internet Protocol version 6)** :
   - IPv6 a été développé pour résoudre le problème de l'épuisement des adresses IPv4 en utilisant des adresses de 128 bits.
   - Les adresses IPv6 sont généralement représentées sous forme de huit groupes de quatre chiffres hexadécimaux, séparés par des deux-points, par exemple, 2001:0db8:85a3:0000:0000:8a2e:0370:7334.
   - IPv6 offre un espace d'adressage beaucoup plus vaste, ce qui permet de connecter un nombre considérablement plus élevé d'appareils à Internet.

Outre IPv4 et IPv6, il existe d'autres protocoles IP, mais ils sont moins courants ou spécifiques à certaines applications. Par exemple, IPv5 était une version expérimentale qui n'a jamais été largement déployée.

**Il est important de noter que, pour fonctionner sur Internet, les appareils doivent prendre en charge IPv4, IPv6, ou les deux, en fonction de la configuration de leur réseau et de la disponibilité des adresses IP. La transition vers IPv6 est en cours pour répondre à la demande croissante en adresses IP et pour garantir la pérennité d'Internet à l'ère de la connectivité croissante.**

--- 
# Composants d'un réseau sécurisé : 

1. **Pare-feu (Firewall) :** Un pare-feu est un dispositif de sécurité essentiel qui filtre le trafic réseau entrant et sortant pour empêcher les menaces de pénétrer dans le réseau. Il peut être basé sur un matériel ou être un logiciel installé sur un serveur.
    
2. **Réseau privé virtuel (VPN) :** Un VPN sécurise la communication entre les utilisateurs distants et le réseau en chiffrant les données transitant par Internet. Cela permet aux employés de se connecter de manière sécurisée depuis l'extérieur du réseau.
    
3. **Authentification forte :** L'authentification à deux facteurs (2FA) ou l'authentification à plusieurs facteurs (MFA) renforcent la sécurité en exigeant que les utilisateurs fournissent plus d'une preuve de leur identité pour accéder au réseau.
    
4. **Mises à jour régulières :** Gardez tous les systèmes, logiciels et appareils du réseau à jour avec les derniers correctifs de sécurité pour minimiser les vulnérabilités.
    
5. **Antivirus et anti-malware :** Utilisez des logiciels antivirus et anti-malware sur tous les appareils connectés au réseau pour détecter et supprimer les menaces.
    
6. **Segmentation du réseau :** Divisez le réseau en segments logiques pour limiter la propagation des attaques. Par exemple, séparez les réseaux Wi-Fi invités des réseaux internes.
    
7. **Gestion des droits d'accès :** Accordez aux utilisateurs uniquement les privilèges dont ils ont besoin pour effectuer leur travail. Révoquez rapidement les droits d'accès lorsque quelqu'un quitte l'entreprise.
    
8. **Surveillance du réseau :** Utilisez des outils de surveillance du réseau pour détecter et signaler toute activité suspecte, comme des tentatives de connexion non autorisées.
    
9. **Sauvegardes régulières :** Effectuez des sauvegardes régulières des données importantes et stockez-les hors site pour éviter la perte de données en cas de sinistre ou de cyberattaque.
    
10. **Formation en sécurité :** Sensibilisez les utilisateurs aux meilleures pratiques en matière de sécurité, notamment la création de mots de passe forts, la détection des attaques de phishing et la protection des informations sensibles.
    
11. **Politiques de sécurité :** Élaborez et mettez en œuvre des politiques de sécurité qui définissent les règles et les procédures à suivre pour maintenir un environnement sécurisé.
    
12. **Tests de pénétration :** Effectuez régulièrement des tests de pénétration pour identifier et corriger les vulnérabilités potentielles dans le réseau.
    
13. **Plan de réponse aux incidents :** Élaborez un plan de réponse aux incidents pour savoir comment réagir en cas de violation de sécurité, et assurez-vous que tout le personnel est formé à son exécution.
    

**Gardez à l'esprit que la sécurité est un processus continu, et il est important de rester informé des dernières menaces et des meilleures pratiques en matière de sécurité pour maintenir un réseau sécurisé. La configuration exacte d'un réseau sécurisé peut varier en fonction des besoins spécifiques de chaque organisation ou utilisateur.
**