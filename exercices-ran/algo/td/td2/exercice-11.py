
# Alain et Catherine organisent une soirée pour des membres de leur club informatique.
# Ils décident que pour être invité il faut :

# - être ami d’Alain et de Catherine ;
# - ou ne pas être ami d’Alain, mais être ami de Catherine ;
# - ou ne pas être ami de Catherine, mais jouer au bridge.

# Pour un membre quelconque, on définit les variables booléennes suivantes par :
# a = 1 s’il est un ami d’Alain,
# b = 1 s’il joue au bridge,
# c = 1 s’il est un ami de Catherine.

a = int(input("Ami d'Alain ? (1/0):"))
b = int(input("Joueur de bridge ? (1/0):"))
c = int(input("Ami de catherine ? (1/0):"))

# if (a==1 and c==1) or (a==0 and c==1) or (c==0 and b==1):
#   print("bienvenue")

if  a ==1 and c == 1:
    reponse = "bienvenue"
elif a ==0 or c ==1:
    reponse = "bienvenue"
elif c == 0 and b == 1:
    reponse = "bienvenue"
else: 
    reponse = "Go home"

print(reponse)

# if (a and c) or (not a and c) or (b and c)
#   print("bienvenue")