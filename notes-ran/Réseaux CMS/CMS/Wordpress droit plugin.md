```shell
root@debian:/var/www/html chown -R www-data modulo
root@debian:/var/www/html ls -l
total 12
-rw-r--r--  1 www-data root  615 17 nov.  15:42 index.nginx-debian.html
drwxr-xr-x  5 www-data root 4096 17 nov.  16:40 modulo
drwxr-xr-x 13 www-data root 4096 17 nov.  16:20 phpmyadmin
```

ou

```shell
chown -R www-data *
# donne accés a www-data a tout le dossier parent
```
