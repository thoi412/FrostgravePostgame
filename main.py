import random
from Classes import Item
from Data import spell_table, potions_list, lesser_potions, greater_potions, \
    magic_weapon_armour_table, magic_item_table, grimoires, golds, scrolls
# from time import sleep


def roll_20():
    return random.randint(1, 20)


def table_roll_20():
    return random.randint(0, 19)


def magic_table_roll():
    return random.randint(0, len(spell_table) - 1)


def keys_and_weights(table):
    return map(list, zip(*table.items()))


def soldierSurvival():
    soldier_survival = random.choices(soldier_survival_table, soldier_survival_table_odds)[0]
    return soldier_survival


def spellcasterSurvival():
    spellcaster_survival = random.choices(spellcaster_survival_table, spellcaster_survival_odds)[0]
    return spellcaster_survival


def spellcasterInjuries():
    spellcaster_injuries = random.choices(spellcaster_injuries_table, spellcaster_injuries_odds)[0]
    return spellcaster_injuries


def flatten(t):
    return [thing for sublist in t for thing in sublist]


potions_odds = []
for _ in range(len(lesser_potions)):
    potions_odds.append(5)

for _ in range(len(greater_potions)):
    potions_odds.append(1)


def random_potion():
    chosen_potion = random.choices(potions_list, potions_odds)[0]
    return chosen_potion


def magicWeaponArmourTable():
    roll = table_roll_20()
    return magic_weapon_armour_table[roll]


def magicItemTable():
    roll = table_roll_20()
    return magic_item_table[roll]


# The Tables
soldier_survival_table = ["has died.", "is badly wounded.", "will make a full recovery."]
soldier_survival_table_odds = [4, 4, 12]

spellcaster_injuries_table = ["lost toes", "a smashed leg", "a crushed arm", "lost fingers",
                              "never being quite as strong", "psychological scars", "a niggling injury",
                              "a smashed jaw", "a lost eye"]
spellcaster_injuries_odds = [2, 4, 4, 2, 2, 2, 2, 1, 1]

spellcaster_survival_table = ["has died.", "will carry a permanent injury of " + spellcasterInjuries() + ".",
                              "is badly wounded.", "had a close call.", "will make a full recovery."]
spellcaster_survival_odds = [2, 2, 2, 2, 12]

loot = list()


def treasureTable():
    new_loot = list()
    treasure_table = [
        [golds[5]],
        [golds[roll_20()]],
        [golds[roll_20() * 2]],
        [golds[2], random_potion(), random_potion(), random_potion()],
        [golds[4], random_potion(), random_potion()],
        [golds[2], scrolls[magic_table_roll()]],
        [golds[4], scrolls[magic_table_roll()], scrolls[magic_table_roll()]],
        [magicWeaponArmourTable()],
        [golds[2], magicWeaponArmourTable()],
        [golds[4], magicWeaponArmourTable()],
        [magicItemTable()],
        [golds[2], magicItemTable()],
        [golds[4], magicItemTable()],
        [grimoires[magic_table_roll()]],
        [golds[2], grimoires[magic_table_roll()]],
        [golds[4], grimoires[magic_table_roll()]],
        [golds[6], grimoires[magic_table_roll()]],
        [golds[8], grimoires[magic_table_roll()]],
        [golds[10], grimoires[magic_table_roll()]],
        [golds[12], grimoires[magic_table_roll()]]
    ]
    roll = table_roll_20()
    # print(roll)  # Uncomment for troubleshooting
    # return treasure_table[roll]...
    this_loot = treasure_table[roll]
    new_loot.append(this_loot)
    return new_loot

def main():

    try:
        injured_soldiers = int(input("How many of your soldiers were defeated? "))
        if injured_soldiers == 0:
            print('Did you even play Frostgrave?')
        elif injured_soldiers > 8:
            print("You know your apprentice and wizard aren't soldiers right?")
        for soldier in range(injured_soldiers):
            print("Soldier " + str(soldier + 1) + " " + soldierSurvival())
    except ValueError:
        print("Try putting in a numeral like 3 next time")

    try:
        apprentice_injury = input("Was your apprentice injured? (y/n)")
        if apprentice_injury == 'y':
            print("Your apprentice " + spellcasterSurvival())
        elif apprentice_injury == 'n':
            print("Well isn't that nice.")
    except ValueError:
        print("Reply with a lowercase 'y' or 'n'")

    try:
        wizard_injury = input("Was your wizard injured? (y/n)")
        if wizard_injury == 'y':
            print("Your wizard " + spellcasterSurvival())
        elif wizard_injury == 'n':
            print("Well isn't that nice.")
    except ValueError:
        print("Reply with a lowercase 'y' or 'n'")

    crowns = 0
    treasure_sale_value = 0
    loot_items_list = list()

    try:
        treasures = int(input("How many treasures did you recover?"))
        for i in range(treasures):
            loot.append(treasureTable())
        flat_loot = flatten(flatten(loot))
        for item in range(len(flat_loot)):
            if flat_loot[item].item_type != 'Gold':
                loot_items_list.append(flat_loot[item])
        for item in range(len(flat_loot)):
            if flat_loot[item].item_type == 'Gold':
                crowns += flat_loot[item].sale_price
            elif flat_loot[item].item_type == 'Weapon' or 'Armour' or 'Scroll':
                treasure_sale_value += flat_loot[item].sale_price
        print('')
        print(f'You looted a total of {crowns} gold crowns.')
        print('')
        print(f'You also got away with the following treasures:')
        for item in range(len(loot_items_list)):
            print(loot_items_list[item].name)
        print(f'A total sale value of {treasure_sale_value} gold crowns.')
        print('')

        print_descriptions = input("Would you like the item descriptions displayed? (y/n)")
        if print_descriptions == 'y':
            for item in range(len(loot_items_list)):
                print(f'{loot_items_list[item].name}: {loot_items_list[item].description}')
        else:
            print("Well fine then you big know it all!")
    except ValueError:
        print("Try again, but put in a number like 3 next time.")


if __name__ == "__main__":
    main()
