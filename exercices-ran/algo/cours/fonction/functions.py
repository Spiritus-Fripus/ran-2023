# affiche le double d'un nombre
def double(n):
    return n * 2

# affiche le carré d'un nombre
def carré(n):
    return n * n

# affiche le périmetre d'un rectangle
def perimetre_rectangle(l,w):
    return (l + w) * 2 

# affiche le périmetre d'un cercle
def perimetre_cercle(r):
    return 2 * 3,141592 * r

# affiche le prix ttc 
def prix_ttc(p,t):
    return p * (1 + t / 100)

# affiche hello
def hello(w):
    print("Bonjour", w)

# affiche la table de multiplication d'un nombre
def multiple(n):
    for i in range(1,11):
        print(n * i)

# Créer une fonction qui permet de retourner la position d'un élément dans un tableau. La fonction doit prendre en paramètre l'élément à rechercher et le tableau concerné.
def search_tab(tab ,element):
    for i in range(len(tab)):
        if tab[i] == element:
            print([i]) 

# Créer une fonction qui permet d'inverser un tableau
def inverted_tab(tab):
    tab_temp = []
    for i in range(1,len(tab)):
        tab_temp += [tab[-i]]
    tab_temp += [tab[0]]
    tab = tab_temp
    print(tab)

# Créer une fonction qui permet de trier un tableau dans l'ordre croissant
def tri_tab(tab):
    
    for i in range(0,len(tab) -1):
        for j in range(0,len(tab) -i -1):
            if tab[j] > tab[j+1]:
                tab_temp = tab[j]
                tab[j] = tab[j+1]
                tab[j+1] = tab_temp
    print(tab)