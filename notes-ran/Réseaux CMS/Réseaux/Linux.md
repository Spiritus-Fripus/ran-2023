# Fonctionnement

## Système de fichier

1. Racine du SF : /
   - /dossier/sous-dossier/etc...

_Exemple :_
Pour une clé USB linux va détecter dans quelle parti de l'arborecence la clé va devoir aller

- /
  - /media
    - /usb
      - /usb/fichier1
      - /usb/fichier2

---

2.  Sous linux il n'existe que 3 type de fichiers (Tout le système est identifié par des fichiers)

- **fichiers** qui identifient des **dossiers**
- **fichiers** qui identifient des **périphériques**
- **fichier normal**

_Exemple:_

- photo.jpg
- oni.mp4
- compta.xls
  Linux identifie ces extensions comme des fichiers
  Linux ne gère pas les extensions (il considère le nom du fichier comme "photo.jpg" et non pas "photo")

---

3. Un service et un programme qui tourne en permanence

---

## Commandes

En informatique, le Shell est un programme qui vous permet d'interagir avec un système d'exploitation, tel que Linux, macOS ou Windows, en utilisant des commandes textuelles. Voici quelques commandes de base en shell :

1. **Lister les fichiers et répertoires dans le répertoire courant :**

   ```shell
   ls
   ```

2. **Changer de répertoire :**

   Pour naviguer dans un répertoire, utilisez la commande `cd`. Par exemple, pour accéder au répertoire "Documents" :

   ```shell
   cd Documents
   ```

3. **Revenir au répertoire précédent :**

   Utilisez `cd ..` pour remonter d'un niveau dans la hiérarchie des répertoires.

4. **Afficher le répertoire courant :**

   ```shell
   pwd
   ```

5. **Créer un nouveau répertoire :**

   ```shell
   mkdir nom_du_répertoire
   ```

6. **Créer un nouveau fichier :**

   ```shell
   touch nom_du_fichier
   ```

7. **Copier un fichier :**

   ```shell
   cp source destination
   ```

8. **Déplacer ou renommer un fichier :**

   ```shell
   mv source destination
   ```

9. **Supprimer un fichier :**

   ```shell
   rm nom_du_fichier
   ```

10. **Supprimer un répertoire (et son contenu) :**

    ```shell
    rm -r nom_du_répertoire
    ```

11. **Afficher le contenu d'un fichier :**

    ```shell
    cat nom_du_fichier
    ```

12. **Éditer un fichier en utilisant l'éditeur de texte par défaut :**

    ```shell
    nano nom_du_fichier
    ```

13. **Afficher l'aide d'une commande :**

    Vous pouvez généralement obtenir de l'aide sur une commande en ajoutant `--help` à la fin de la commande. Par exemple :

    ```shell
    ls --help
    ```

14. **Afficher la liste des processus en cours d'exécution :**

    ```shell
    ps aux
    ```

15. **Killer un processus :**

    Pour tuer un processus en cours d'exécution, vous pouvez utiliser `kill` avec l'ID du processus. Par exemple, pour tuer un processus avec l'ID 12345 :

    ```shell
    kill 12345
    ```

16. **Afficher l'historique des commandes précédemment exécutées :**

    ```shell
    history
    ```

Ces commandes de base devraient vous permettre de commencer à travailler avec un Shell. N'oubliez pas de faire preuve de prudence lors de l'utilisation de commandes de suppression ou de modification de fichiers, car elles peuvent avoir des conséquences irréversibles.

---

## Principe de fonctionnement de Shell

```shell
# commande paramètre(s)
# commande -option(s)
```

_Exemple_ pour la commande "ls" :

```shell
ls
# Pour afficher l'ensemble d'un repertoire
ls -l
# Pour lister le repertoire
man ls
# Affiche la documentation de la commande
```

_Créer un repertoire:_

```shell
mkdir services
# crée un dossier services
ls
# verification de l'existance du dossier
ls -l
# Affichage listé
```

_Renommer un fichier_ :

```shell
mkdir tehcnique
# mauvaise manipulation lors de la création
mv tehcnique technique
# on utilise la commande mv pour move
```

_Supprimer un dossier_ :

```shell
rmdir photos/
# rmdir permet de supprimer un dossier
rm -r dossier/
# permet de supprimer un dossier et ses enfants
rm -rf *
# Force la suppression
# !! attention casse le systeme si cette commande est entrée !!
```

_Remonter au dossier parent:_

```shell
root@debian-nathan:~/mes_fichiers/word
cd ..
# remonte d'un niveau
root@debian-nathan:~/mes_fichiers
```

_apt:_

```shell
frip@debian-nathan:~$ apt
apt 2.6.1 (i386)
Usage : apt [options] commande

apt est un outil en ligne de commande pour gérer les paquets.
Il fournit des commandes pour chercher et gérer autant que pour
rechercher des informations à propos des paquets. Il fournit les mêmes
fonctions que les outils APT spécialisés, tels qu'apt-get et apt-cache,
mais dispose d'options plus adaptées pour une utilisation interactive.

Commandes les plus utilisées :
  list - liste les paquets selon leur nom
  search - cherche dans les descriptions de paquet
  show - affiche les détails du paquet
  install - installes les paquets
  reinstall - reinstall packages
  remove - supprime des paquets
  autoremove - automatically remove all unused packages
  update - met à jour la liste des paquets disponibles
  upgrade - met à jour le système en installant/mettant à jour les paquets
  full-upgrade - met à jour le système en supprimant/installant/mettant à jour les paquets
  edit-sources - édite le fichier d'information source
  satisfy - satisfy dependency strings

Veuillez vous référer à apt(8) pour plus d'information à propos des commandes disponibles.
Les options de configuration ainsi que la syntaxe sont détaillées dans apt.conf(5).
Des informations sur la configuration des sources sont disponibles dans sources.list(5).
Les choix de paquet ainsi que la version peuvent être renseignés grâce à apt_preferences(5).
Les informations à propos de la sécurité sont disponibles dans apt-secure(8).

                                Cet APT a les « Super Cow Powers »

```

_Installer des programmes:_

```shell
apt
# affiche la liste des commandes de apt
apt update
# permet de mettre à jours les programmes et paquets
apt search mysql
# permet de chercher tout les programmes qui ont #mysql dans leurs description
apt install ssh-server
# installe le programme demandé
```

Afficher le contenu d'un fichier texte:

```shell
cat
# permet d'afficher le conetenu d'un fichier texte
root@debian-nathan:/etc cat passwd
# affiche tout les utilisateurs du répertoire etc (etc contien tout les fichiers de paramètre)
root@debian-nathan:/etc cat shadow
# affiche tout les mots de passe
```

_Afficher les services:_

```shell
service --status-all
# liste les service et donne leurs états
```

_Connaitre son IP:_

```shell
ip address
# affiche l'IP (10.0.2.15)
```
