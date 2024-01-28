# Créer une fonction qui permet d'inverser un tableau

def inverted_tab(tab):
    tab_temp = []
    for i in range(1,len(tab)):
        tab_temp += [tab[-i]]
    tab_temp += [tab[0]]
    tab = tab_temp
    print(tab)

tab = [1,2,3,4,5,6,7,8,9]

inverted_tab(tab)