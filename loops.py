# Monster en speler
monster_health = 150
player_damage = 25
aantal_aanvallen = 0

# Monster aanvallen totdat de health 0 is
while monster_health > 0:
    monster_health -= player_damage
    aantal_aanvallen += 1

    if monster_health < 0:
        monster_health = 0

    print("Monster health:", monster_health)

print("Monster verslagen!")
print("Aantal aanvallen:", aantal_aanvallen)

# Bonus: drie monsters verslaan
monsters = [50, 75, 100]

for monster in monsters:
    aanvallen = 0

    while monster > 0:
        monster -= player_damage
        aanvallen += 1

        if monster < 0:
            monster = 0

    print("Monster verslagen na", aanvallen, "aanvallen!")