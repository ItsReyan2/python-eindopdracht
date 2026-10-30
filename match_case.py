# Opdracht: kies een personage met match-case
# Character kiezen
player_class = "Warrior"

# Health en damage bepalen
match player_class:
    case "Warrior":
        health = 150
        damage = 20

    case "Mage":
        health = 80
        damage = 35

    case "Archer":
        health = 100
        damage = 25

    case "Rogue":
        health = 90
        damage = 30

    case _:
        health = 0
        damage = 0
        print("Onbekende class!")

# Resultaat printen
print("Gekozen class:", player_class)
print("Health:", health)
print("Damage:", damage)