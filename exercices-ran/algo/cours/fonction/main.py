# importe le dossier
import functions
# importe la fonction
functions.hello("Nathan")
# ----------------------------------------------------------------#
# importe la fonction depuis le dossier
from functions import hello
hello("Nathan")
#-----------------------------------------------------------------#
# importe toutes les fonctions
from functions import *
hello("Nathan")
