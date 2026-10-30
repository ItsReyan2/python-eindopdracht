# Opdracht: cijfers en gemiddelde controleren
# Cijfers van drie vakken
cijfer_1 = 7
cijfer_2 = 6
cijfer_3 = 8

# Gemiddelde berekenen
gemiddelde = (cijfer_1 + cijfer_2 + cijfer_3) / 3

print("Gemiddelde:", gemiddelde)

# Controleren of de student geslaagd is
if cijfer_1 < 4 or cijfer_2 < 4 or cijfer_3 < 4:
    print("Gezakt!")
elif gemiddelde >= 5.5:
    print("Geslaagd!")
else:
    print("Gezakt!")