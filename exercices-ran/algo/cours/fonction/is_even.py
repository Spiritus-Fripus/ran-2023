def verif(a):
    if a%2 == 0:
        return "Pair"
    else:	
        return "Impair"
#------------------------------------------------------------#
result = verif(int(input("nombre ?: ")))
print(result)