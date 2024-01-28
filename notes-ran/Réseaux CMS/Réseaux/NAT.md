Le Network Address Translation (NAT), en français la "Traduction d'Adresse Réseau", est une technique de routage utilisée dans les réseaux informatiques pour permettre à plusieurs dispositifs d'accéder à Internet ou à un réseau externe en partageant une seule adresse IP publique. Voici un résumé du fonctionnement du NAT :

1. Adresse IP publique : Un réseau local, tel qu'un réseau domestique ou d'entreprise, utilise des adresses IP privées pour chaque dispositif (par exemple, 192.168.1.1). Cependant, pour communiquer avec Internet, ces dispositifs partagent une seule adresse IP publique fournie par le fournisseur d'accès à Internet (FAI).

2. Table de traduction : Le routeur NAT tient une table de traduction (ou table NAT) qui enregistre les correspondances entre les adresses IP privées des dispositifs internes et l'adresse IP publique du routeur.

3. Traduction d'adresses : Lorsqu'un dispositif interne (comme un ordinateur, un smartphone ou une imprimante) envoie une demande à Internet, le routeur NAT modifie l'en-tête de la demande en remplaçant l'adresse IP privée source par l'adresse IP publique du routeur. Il crée également une entrée dans la table de traduction pour suivre cette correspondance.

4. Réponse : Lorsque la réponse revient d'Internet, le routeur NAT utilise la table de traduction pour déterminer à quel dispositif interne renvoyer la réponse. Il effectue alors la traduction inverse, remplaçant l'adresse IP publique par l'adresse IP privée du dispositif interne approprié.

5. Port Mapping : Le NAT peut également associer des numéros de port aux adresses IP privées pour gérer plusieurs connexions simultanées depuis différents dispositifs internes. Cela permet de multiplexer efficacement les données entrantes et sortantes.

6. Sécurité : Le NAT agit comme un pare-feu partiel en masquant les adresses IP internes, ce qui rend plus difficile l'accès direct aux dispositifs internes depuis Internet, améliorant ainsi la sécurité du réseau.

**En résumé, le NAT est une technique de routage qui permet à plusieurs dispositifs d'un réseau local de partager une seule adresse IP publique pour accéder à Internet. Il réalise cette traduction d'adresses en maintenant une table de correspondance entre les adresses IP privées internes et l'adresse IP publique du routeur, tout en garantissant un niveau de sécurité accru en masquant les dispositifs internes aux attaques provenant d'Internet.**

--- 
_Un exemple courant de NAT (Network Address Translation) se produit dans un réseau domestique lorsque plusieurs appareils partagent une seule adresse IP publique pour accéder à Internet. Voici comment cela fonctionne :_

Imaginez un réseau domestique avec plusieurs appareils connectés, tels que des ordinateurs, des smartphones et une console de jeu, tous connectés à un routeur domestique. Le routeur dispose d'une seule adresse IP publique fournie par le fournisseur d'accès à Internet (FAI).

1. **Adresse IP publique** : L'adresse IP publique est celle que le FAI attribue au routeur. Elle est unique et identifie le réseau domestique sur Internet.

2. **Adresses IP privées** : Chaque appareil dans le réseau domestique possède une adresse IP privée qui est attribuée par le routeur. Ces adresses IP privées sont généralement dans une plage d'adresses réservée aux réseaux privés, comme 192.168.1.1, 192.168.1.2, 192.168.1.3, etc.

3. **Demandes vers Internet** : Lorsqu'un appareil dans le réseau domestique souhaite accéder à Internet, il envoie une demande à travers le routeur. Par exemple, si un utilisateur navigue sur un site web, l'appareil envoie une demande au routeur pour accéder à ce site.

4. **NAT** : Le routeur utilise alors la technique NAT pour traduire l'adresse IP privée de l'appareil en l'adresse IP publique du routeur. La demande est ensuite envoyée à Internet avec l'adresse IP publique du routeur comme adresse source.

5. **Réponse d'Internet** : Lorsque la réponse du site web arrive, le routeur utilise à nouveau NAT pour traduire l'adresse IP publique en l'adresse IP privée de l'appareil qui a fait la demande. Ainsi, la réponse parvient à l'appareil correct.

Ce processus permet à plusieurs appareils d'utiliser la même adresse IP publique pour accéder à Internet de manière transparente. Il permet également de masquer les adresses IP privées de l'intérieur du réseau domestique, améliorant ainsi la sécurité en empêchant directement les appareils d'être accessibles depuis Internet.

L'utilisation de NAT est un élément clé de la gestion des adresses IP dans les réseaux privés et est largement utilisée pour économiser des adresses IP publiques et améliorer la sécurité.