# Créer une fonction qui permet de trier un tableau dans l'ordre croissant

def tri_tab(tab):
    
    for i in range(0,len(tab) -1):
        for j in range(0,len(tab) -i -1):
            if tab[j] > tab[j+1]:
                tab_temp = tab[j]
                tab[j] = tab[j+1]
                tab[j+1] = tab_temp
    print(tab)

nombre = [4,635,22,53,63,8]

tri_tab(nombre)