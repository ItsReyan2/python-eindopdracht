# Boodschappenlijst maken
boodschappen = ["Appel", "Banaan", "Melk", "Brood", "Kaas"]

# Twee producten toevoegen
boodschappen.append("Eieren")
boodschappen.append("Water")

# Eén product verwijderen
boodschappen.remove("Banaan")

# Aantal producten tellen
print("Aantal producten:", len(boodschappen))

# Volledige boodschappenlijst printen
print("Boodschappenlijst:", boodschappen)

# Controleren of een product in de lijst staat
if "Melk" in boodschappen:
    print("Melk staat op de boodschappenlijst!")
else:
    print("Melk staat niet op de boodschappenlijst.")