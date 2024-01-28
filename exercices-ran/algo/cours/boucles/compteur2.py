text= "je crois en vous"
lettre="e"
cpt=0

for i in range(0,len(text)):
    if text[i] == lettre:
        cpt= cpt+1
        print(cpt)