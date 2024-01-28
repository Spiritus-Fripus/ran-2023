Virtual host

permet de dire a chacun de nos site de pointer vers le bon dossier 

site 1 ->
site 2 ->            | @ip : 80
site n ->

serveur ->
	nginx ->
		site 1
		site 2
		site 3

mettre site en ligne -> worpress/phpMyAdmin
dans les tab du site -> option

Meilleure solution :
1. Créer virtual host sous nginx
		// ! **Trouver le bon nom de domaine avant** ! //
		
```shell
cd /var/www/html/nomdedomaine
# copier dans 
etc/nginx/sites-available/nomdedomaine
cp default # dans le nomdedomaine
nano default #changer les port et le root
```

2. Avec un plugin de migration
