# Cherchons à résoudre l’équation « ax + b = 0 ». 
# Pour cela, saisissons les deux nombres a et b et affichons le résultat correspondant. 
# Si a = 0 et b = 0 alors l’ensemble des solutions est l’ensemble R. 
# Si a = 0 et b!= 0 alors l’ensemble des solutions est l’ensemble vide. 
# Si a!= 0 alors la solution est (-b / a). 

print("l'équation est ax + b = 0")
a = float(input("saisir la valeur de a: "))
b = float(input("saisir la valeur de b: "))

if a == 0 and b == 0 :
    print("L'essemble des solution est la solution R")
elif a == 0 and b != 0 :
    print("L'ensemble des solutions est l'ensemble vide")
elif a != 0:
    print(f"la solution est : {-b/a}")
