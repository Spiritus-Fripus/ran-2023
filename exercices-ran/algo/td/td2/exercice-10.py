# Le contrôle d’une centrale nucléaire se fait par l’examen de températures. 
# Si la différence entre la température ambiante et la température des bassins de refroidissement est 
# inférieure à 20 °C ou si elle dépasse 40 °C, affichez une alarme. 

temp_ambiante = float(input("Temperature ambiante (°C): "))
temp_bassin = float(input("Temperature bassin (°C): "))

diff = abs(temp_ambiante - temp_bassin)

if diff < 20 or diff > 40:
    print("ALARME !!!")