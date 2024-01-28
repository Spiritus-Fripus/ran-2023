# À partir du document ci-après, on vous demande d’établir l’algorithme permettant de calculer et d’afficher le tarif unitaire du forfait demandé en précisant le statut du bénéficiaire. Vous utiliserez les variables suivantes : Statut, TypeForfait, Age, Tarif et vous attribuerez le chiffre 1 au forfait à la journée et le chiffre 2 au forfait à la saison.

# affectation de mes variables
typeForfait = int(input("Saisir votre type de forfait (1) pour journée, (2) pour saison: ")) 
age = int(input("saisir votre age: "))

# affectation des instruction de ma variable statut
# en fonction de l'age le statut sera different
if age >= 12 < 60:
    statut = "adulte"
if age < 12 :
    statut = "enfant"
if age >= 60 :
    statut = "senior"

# affectation  des instruction de ma variable forfait par ma variable typeForfait
# ajout d'une chaine de caractère pour définir si mon forfait et de journée ou de saison (pour mon print)
if typeForfait == 1:
    forfait = "journée"
if typeForfait == 2: 
    forfait = "saison"

# affectation des instruction de ma variable tarif par mes variables typeForfait et statut 
# définition d'un prix en fonction de l'age et du forfait choisit.
if typeForfait == 1 and statut == "adulte":
    tarif = 25.80
if typeForfait == 2 and statut == "adulte": 
    tarif = 510.00
if typeForfait == 1 and statut == "enfant": 
    tarif = 18.70
if typeForfait == 2 and statut == "enfant": 
    tarif = 300.00
if typeForfait == 1 and statut == "senior":
    tarif = 21.40
if typeForfait == 2 and statut == "senior":
    tarif = 340.00

print(f"Votre prix {statut} est de {tarif}€ pour la {forfait}")
