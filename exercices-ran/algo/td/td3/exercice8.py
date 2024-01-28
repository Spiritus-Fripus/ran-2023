# L’élève placé au fond de la classe, près du radiateur, est le meilleur de la classe. Pour tuer le temps,
# il décide de plier une feuille en deux puis en deux, puis... en deux, puis... Écrivez un algorithme
# qui calcule l’épaisseur du pliage final à partir du nombre de plis et de l’épaisseur initiale de la
# feuille.

plis = 0
plis_max = int(input("nombre de plis ? (8 max recommandé) :"))
epaisseur = 0.1

while plis != plis_max:
    plis +=1
    epaisseur = epaisseur * 2

print(f"L'épaisseur finale de la feuille de papier de 0.1 mm de base et au final de {epaisseur} mm pour {plis_max} plis")