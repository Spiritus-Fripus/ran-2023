Si l’on veut connecter plusieurs équipement entre eux afin qu’ils aient la même information de départ on utilise un switch sur un réseau local

Un switch, également connu sous le nom de commutateur réseau, est un dispositif matériel utilisé dans les réseaux informatiques pour connecter différents périphériques ensemble au sein d'un réseau local (LAN - Local Area Network) et permettre la communication entre ces dispositifs. Les switches sont un composant essentiel des infrastructures réseau modernes et jouent un rôle clé dans la transmission des données au sein du réseau.

Voici quelques caractéristiques et fonctions clés d'un switch :

1. **Connexion des dispositifs** : Les switches sont équipés de plusieurs ports (généralement de 4, 8, 16, 24, 48 ports, voire plus) permettant de connecter des ordinateurs, des serveurs, des imprimantes, des téléphones IP, des caméras de sécurité et d'autres dispositifs réseau.

2. **Commutation de paquets** : L'une des principales fonctions d'un switch est de prendre des décisions sur la manière de transférer les données (paquets) entre les dispositifs connectés. Contrairement aux hubs, qui diffusent des données à tous les ports, les switches déterminent intelligemment à quel port spécifique envoyer les données, en fonction de l'adresse MAC (Media Access Control) des dispositifs destinataires. Cela réduit le trafic réseau inutile et améliore l'efficacité du réseau.

3. **Segmentation du réseau** : Les switches permettent de diviser un réseau en plusieurs segments logiques (souvent appelés VLAN - Virtual LAN). Cela permet d'isoler le trafic, de mieux organiser les ressources réseau et d'améliorer la sécurité.

4. **Auto-apprentissage** : Les switches disposent de mécanismes d'auto-apprentissage qui leur permettent de détecter automatiquement les adresses MAC des dispositifs connectés à chaque port. Cette information est stockée dans une table d'adresses MAC, ce qui permet au switch de prendre des décisions de commutation plus efficaces.

5. **Contrôle de la bande passante** : Certains switches offrent des fonctionnalités de contrôle de la bande passante, permettant de prioriser le trafic en fonction de critères spécifiques, tels que la qualité de service (QoS - Quality of Service), pour garantir des performances optimales pour des applications sensibles à la latence comme la voix sur IP (VoIP) ou la vidéo en streaming.

6. **Gestion** : Les switches peuvent être administrés localement ou à distance via une interface de gestion. Les administrateurs réseau peuvent configurer des paramètres tels que les VLAN, la sécurité, le contrôle d'accès, etc.

7. **Redondance** : Dans les réseaux critiques, plusieurs switches peuvent être configurés pour fournir une redondance, assurant ainsi la disponibilité continue du réseau en cas de panne matérielle.

8. **Sécurité** : Les switches modernes offrent des fonctionnalités de sécurité telles que la détection d'intrusion, le contrôle d'accès basé sur les ports et d'autres mécanismes pour protéger le réseau contre les menaces.

En résumé, un switch est un composant essentiel des réseaux locaux modernes, assurant une connectivité efficace et intelligente entre les dispositifs connectés, tout en améliorant les performances et la sécurité du réseau.

[Commutateur réseau](https://fr.wikipedia.org/wiki/Commutateur_r%C3%A9seau)

_Exemple:_

→ Pc secrétaire
→ Pc comptable
→ Pc commercial

Impossible de connecter les 3 ensembles

→ SWITCH
→ Pc secrétaire
→ Pc comptable
→ Pc commercial

L’ensemble est relié

On peut également connecter a un Switch différent éléments comme des imprimantes, scanner, téléphone, caméra etc… sur un réseau local

Exemple:

→ SWITCH
→ Pc 1
→ Pc 2
→ Pc 3
→ Imprimante
→ Caméra
→ Wifi
