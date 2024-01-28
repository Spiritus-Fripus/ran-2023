# Saisissez le rayon R d’un cercle et un angle a (en degré(s)). Calculez et affichez l’aire du secteur circulaire. Aire = ∏ * R2 * a / 360

rayon = float(input("Saisir le rayon du cercle (en cm): "))
angle = float(input("Saisir l'angle (en degrés): "))

aire = 3.14 * (rayon * rayon) * (angle / 360)

print(f"l'air du cercle est {aire}")