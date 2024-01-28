# Écrivez l’algorithme qui affiche à l’écran les lignes suivantes :
# 10 11 12 13 14 15
# 20 21 22 23 24 25
# 30 31 32 33 34 35
# 40 41 42 43 44 45
# 50 51 52 53 54 55

# chain = ""
# print("\n")
# for i in range(1):
#     for j in range(10,16):
#         chain = chain + " " + str(j)
#     chain += "\n"
#     for j in range(20,26):
#         chain = chain + " " + str(j)
#     chain += "\n"
#     for j in range(30,36):
#         chain = chain + " " + str(j)
#     chain += "\n"
#     for j in range(40,46):
#         chain = chain + " " + str(j)
#     chain += "\n"
#     for j in range(50,56):
#         chain = chain + " " + str(j)
# print(chain)

nbr = 10
chain = ""
add = 10
print("\n")

for loop in range(5):
    for loop in range(6):
        chain += " " + str(nbr)
        nbr +=1
    chain += "\n"
    nbr = 10 + add
    add += 10
    
print(chain)