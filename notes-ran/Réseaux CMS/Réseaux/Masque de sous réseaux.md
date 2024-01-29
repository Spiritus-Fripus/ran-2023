**Les masques de sous-réseaux** (ou masques de sous-réseau) sont utilisés dans les réseaux informatiques pour diviser un réseau IP en sous-réseaux plus petits. Voici un résumé des types de masques de sous-réseaux les plus couramment utilisés :

1. Masque de sous-réseau par défaut (ou masque de sous-réseau de classeful) :

   - Utilisé dans les réseaux de classe A, B et C.
   - Déterminé par la classe de l'adresse IP (A, B ou C).
   - Le masque de sous-réseau classe A est 255.0.0.0, classe B est 255.255.0.0 et classe C est 255.255.255.0.

2. Masque de sous-réseau CIDR (Classless Inter-Domain Routing) :

   - Utilisé pour permettre une division plus flexible des adresses IP.
   - Écrit sous la forme de notation CIDR, par exemple, /24, /16, etc.
   - Permet de spécifier le nombre de bits alloués pour le réseau et les hôtes.

3. Masque de sous-réseau personnalisé :
   - Peut être utilisé pour diviser un réseau en sous-réseaux de taille personnalisée.
   - Exprimé en notation décimale pointée (par exemple, 255.255.255.192).
   - Permet un contrôle précis sur la taille des sous-réseaux.

**L'utilisation de masques de sous-réseaux permet aux administrateurs réseau de segmenter efficacement leur espace d'adressage IP en sous-réseaux plus petits, ce qui peut améliorer la gestion du réseau, la sécurité et l'efficacité de la communication entre les périphériques.**

---

_Voici quelques exemples de masques de sous-réseau couramment utilisés, exprimés en notation CIDR (Classless Inter-Domain Routing) :_

1. **Masque de sous-réseau /24** :

   - Notation CIDR : /24
   - Notation décimale : 255.255.255.0
   - Cela signifie qu'il y a 24 bits alloués au réseau, ce qui laisse 8 bits pour les hôtes.
   - Exemple : 192.168.1.0/24 permet 256 adresses d'hôtes (de 192.168.1.1 à 192.168.1.254), car 2^8 = 256.

2. **Masque de sous-réseau /28** :

   - Notation CIDR : /28
   - Notation décimale : 255.255.255.240
   - Cela signifie qu'il y a 28 bits alloués au réseau, ce qui laisse 4 bits pour les hôtes.
   - Exemple : 192.168.2.0/28 permet 16 adresses d'hôtes (de 192.168.2.1 à 192.168.2.14), car 2^4 = 16.

3. **Masque de sous-réseau /16** :

   - Notation CIDR : /16
   - Notation décimale : 255.255.0.0
   - Cela signifie qu'il y a 16 bits alloués au réseau, ce qui laisse 16 bits pour les hôtes.
   - Exemple : 10.0.0.0/16 permet 65 536 adresses d'hôtes (de 10.0.0.1 à 10.0.255.254), car 2^16 = 65 536.

4. **Masque de sous-réseau /30** :
   - Notation CIDR : /30
   - Notation décimale : 255.255.255.252
   - Cela signifie qu'il y a 30 bits alloués au réseau, ce qui laisse 2 bits pour les hôtes.
   - Exemple : 172.16.0.0/30 permet 2 adresses d'hôtes (de 172.16.0.1 à 172.16.0.2), car 2^2 = 4, mais deux de ces adresses sont réservées (l'adresse de réseau et l'adresse de diffusion), donc il ne reste que deux adresses utilisables.

Ces exemples montrent différentes tailles de masques de sous-réseau, allouant un nombre variable de bits pour les hôtes en fonction des besoins du réseau. Le choix du masque de sous-réseau dépend des exigences spécifiques de la topologie du réseau et du nombre d'adresses d'hôtes nécessaires dans chaque sous-réseau.
