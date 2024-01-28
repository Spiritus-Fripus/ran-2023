# Ecrire un programme permettant de compter le nombre de fois qu'une lettre est présente dans un texte.
# Le programme doit alors demander le texte et la lettre à rechercher.

# Vous devez ensuite afficher le nombre de fois que la lettre est présente dans le texte.

word = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Autem, possimus nesciunt nobis nemo quis natus, ratione est saepe inventore commodi numquam eos aliquam id, veritatis rerum voluptatem laudantium at minima?"
choix = input("choisissez une lettre: ")
cpt=0
for i in range(0, len(word)):
    if choix == word[i]:
        cpt= cpt+1
print(cpt)