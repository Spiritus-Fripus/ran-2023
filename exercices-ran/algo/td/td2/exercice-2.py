print("Veuillez saisir 3 nombres:")
a = float(input("Nombre 1: "))
b = float(input("Nombre 2: "))
c = float(input("Nombre 3: "))
if a < b and b < c:
    print("les nombres sont classés dans l'ordre croissant")
elif a > b and b > c:
    print("les nombres sont classés dans l'ordre décroissant")
else:
    print("les nombres ne sont pas trié")