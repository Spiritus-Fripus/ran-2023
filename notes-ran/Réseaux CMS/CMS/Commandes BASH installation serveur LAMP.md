```shell
mkdir commandes
```

```shell
cd commandes
```

```shell
nano install_server
```

```shell

# script d'installation d'un serveur LAMP
# nginx
# php
# php-fpm
# mariadb
# phmyadmin

# Mise a jour de la liste des paquets
apt update

# installation nginx
apt install nginx

# installation de php
apt install php8.2

# installation de php-fpm
apt install php8.2-fpm

# installation de mariadb
apt install mariadb-server

# tout mettre à jour
apt upgrade

# installation de phpmyadmin
wget -O phpmyadmin.tar.gz https://files.phpmyadmin.net/phpMyAdmin/5.2.1/phpMyAdmin-5.2.1-all-languages.tar.gz

# dezipper le fichier phpmyadmin.tar.gz
gzip -d phpmyadmin.tar.gz

# désarchiver le fichier phpmyadmin.tar
tar -xf phpmyadmin.tar

# déplacer le dossier phpmyadmin
mv phpMyAdmin-5.2.1-all-languages /var/www/html/phpmyadmin1# script d'installation d'un serveur LAMP
# nginx
# php
# php-fpm
# mariadb
# phmyadmin

# Mise a jour de la liste des paquets
apt update

# installation nginx
apt install nginx

# installation de php
apt install php8.2

# installation de php-fpm
apt install php8.2-fpm

# installation de mariadb
apt install mariadb-server

# tout mettre à jour
apt upgrade

# installation de phpmyadmin
wget -O phpmyadmin.tar.gz https://files.phpmyadmin.net/phpMyAdmin/5.2.1/phpMyAdmin-5.2.1-all-languages.tar.gz

# dezipper le fichier phpmyadmin.tar.gz
gzip -d phpmyadmin.tar.gz

# désarchiver le fichier phpmyadmin.tar
tar -xf phpmyadmin.tar

# déplacer le dossier phpmyadmin
mv phpMyAdmin-5.2.1-all-languages /var/www/html/phpmyadmin1
```
