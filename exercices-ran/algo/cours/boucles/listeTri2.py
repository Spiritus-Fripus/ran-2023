entier = [0,8,2,5,9]
i=0
while i != len(entier):
    if i+1 >= len(entier):
        break
    if entier[i] > entier[i+1]:
        current_n = entier[i]
        next_n = entier[i+1]
        entier[i] = next_n
        entier[i+1] = current_n
        i = 0
    else:
        i += 1
        
print(entier)
