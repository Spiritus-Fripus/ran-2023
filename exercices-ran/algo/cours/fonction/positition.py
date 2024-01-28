# Créer une fonction qui permet de retourner la position d'un élément dans un tableau. La fonction doit prendre en paramètre l'élément à rechercher et le tableau concerné.

def search_tab(tab ,element):
    for i in range(len(tab)):
        if tab[i] == element:
            print([i]) 

tab = [6,25,63,6262,22,6636]

print()
search_tab(tab, 6262)
print()