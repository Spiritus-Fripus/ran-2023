# Gestion des droits

```shell
drwxr-xr-x 12 root root  4096 12 oct.  11:39 phpmyadmin
```

_drwxr-xr-x_ = **droits**
_root_ = **propriétaire**
_root_ = **groupe**
_phpmyadmin_ = **nom du fichier/dossier**

| propriétaire | groupe | autres |
| ------------ | ------ | ------ |
| **RWX**          | **RWX**    | **RWX**       |

**R** = Read -> LS
**W** = Wright ->créer/ supprimer Fichier/Dossier
**X** = Executer -> CD

```shell
drwxr-xr-x 12 root root  4096 12 oct.  11:39 phpmyadmin
```

drwxr-xr-x 
**WXR** = _Propriétaire_ (peut  **écrire**/**executer** et **lire**  le programme)
**R** _ **X** = _Groupe_ (peut **lire** et **executer**)
**X** = _Utilisateur_ (peut **executer**)

# Ajouts de droits 

```shell
frip@debian-nathan:/home$ ls -l
total 8
drwxr----- 2 compta compta 4096 23 oct.  11:18 compta
drwxr----- 4 frip   frip   4096 23 oct.  11:23 frip
```

```shell 
man chmod
```
Permet de lire la doc de chmod
```shell
frip@debian-nathan:/home$
chmod o+x frip
frip@debian-nathan:/home$ ls -l
drwxr----- 2 compta compta 4096 23 oct.  11:18 compta
drwxr----x 4 frip   frip   4096 23 oct.  11:23 frip
frip@debian-nathan:/home$
```
Rajoute à tout les utilisateur le droit d'executer les fichier/dossier
```shell
frip@debian-nathan:/home$
chmod o+r frip
frip@debian-nathan:/home$ ls -l
drwxr----- 2 compta compta 4096 23 oct.  11:18 compta
drwxr---rx 4 frip   frip   4096 23 oct.  11:23 frip
frip@debian-nathan:/home$
```
Rajoute a tout les utilisateur le droit de lire 

```shell
frip@debian-nathan:/home$
chmod o+w frip
frip@debian-nathan:/home$ ls -l
drwxr----- 2 compta compta 4096 23 oct.  11:18 compta
drwxr--rwx 4 frip   frip   4096 23 oct.  11:23 frip
frip@debian-nathan:/home$
```
Rajoute a tout les utilisateur le droit d'écriture 