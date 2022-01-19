import random
# from time import sleep


# Define Item class


class Item:
    def __init__(self, name, purchase_price, sale_price, item_type, description):
        self.name = name
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        self.item_type = item_type
        self.description = description


# Spell Table - length 80
spell_table = [
    'Animate Skull',
    'Curse',
    'Fleet Feet',
    'Leap',
    'Wall',
    'Push',
    'Teleport',
    'Strength',
    'Awareness',
    'Shield',
    'Bone Dart',
    'Mud',
    'Decay',
    'Plague of Insects',
    'Elemental Bolt',
    'Furious Quill',
    'Blink',
    'Enchant Weapon',
    'Combat Awareness',
    'Circle of Protection',
    'Bones of the Earth',
    'Poison Dart',
    'Slow',
    'Imp',
    'Call Storm',
    'Draining Word',
    'Invisibility',
    'Telekinesis',
    'True Sight',
    'Banish',
    'Spell Eater',
    'Fog',
    'Time Store',
    'Planar Tear',
    'Elemental Ball',
    'Absorb Knowledge',
    'Fool\'s Gold',
    'Grenade',
    'Wizard Eye',
    'Heal',
    'Strike Dead',
    'Animal Companion',
    'Crumble',
    'Plane Walk',
    'Scatter Shot',
    'Explosive Rune',
    'Beauty',
    'Enchant Armour',
    'Mind Lock',
    'Blinding Light',
    'Steal Health',
    'Control Animal',
    'Petrify',
    'Possess',
    'Elemental Hammer',
    'Power Word',
    'Glow',
    'Embed Enchantment',
    'Suggestion',
    'Dispel',
    'Control Undead',
    'Familiar',
    'Fast Act',
    'Control Demon',
    'Destructive Sphere',
    'Write Scroll',
    'Transpose',
    'Control Construct',
    'Mind Control',
    'Miraculous Cure',
    'Raise Zombie',
    'Brew Potion',
    'Time Walk',
    'Summon Demon',
    'Elemental Shield',
    'Bridge',
    'Illusionary Soldier',
    'Animate Construct',
    'Reveal Secret',
    'Destroy Undead'
]


def roll_20():
    return random.randint(1, 20)


def table_roll_20():
    return random.randint(0, 19)


def magic_table_roll():
    return random.randint(0, len(spell_table) - 1)


def spellTable():
    spell = random.choices(spell_table)[0]
    return spell


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


# Define Lesser Potions
pot_of_heal = Item('Potion of Healing', 75, 50, 'Potion', '')
pot_of_str = Item('Potion of Strength', 100, 40, 'Potion', '')
pot_of_tuf = Item('Potion of Toughness', 50, 30, 'Potion', '')
elix_of_speed = Item('Elixir of Speed', 50, 30, 'Potion', '')
pot_of_invis = Item('Potion of Invisibility', 100, 50, 'Potion', '')
explo_cock = Item('Explosive Cocktail', 100, 30, 'Potion', '')
pot_of_tele = Item('Potion of Teleportation', 500, 100, 'Potion', '')
pot_of_elem_absorb = Item('Potion of Elemental Absorption', 200, 80, 'Potion', '')
cord_of_clears = Item('Cordial of Clearsight', 200, 80, 'Potion', '')
poison = Item('Poison', 100, 30, 'Potion', '')
phil_of_fury = Item('Philtre of Fury', 300, 120, 'Potion', '')
pot_of_FeMind = Item('Potion of Iron Mind', 50, 30, 'Potion', '')
bot_of_bur = Item('Bottle of Burrowing', 200, 80, 'Potion', '')
phil_of_FairyD = Item('Philtre of Fairy Dust', 50, 30, 'Potion', '')
construct_oil = Item('Construct Oil', 100, 50, 'Potion', '')
pot_of_fire_brth = Item('Potion of Fire Breath', 200, 80, 'Potion', '')
pot_of_pres = Item('Potion of Preservation', 500, 200, 'Potion', '')
elix_of_cham = Item('Elixir of the Chameleon', 400, 140, 'Potion', '')

# Define Greater Potions

cord_of_emp = Item('Cordial of Empowerment', 500, 200, 'Potion', '')
shrink_pot = Item('Shrinking Potion', 500, 200, 'Potion', '')
pot_of_rest = Item('Potion of Restoration', 2000, 300, 'Potion', '')
bot_of_drms_nitmrs = Item('Bottle of Dreams and Nightmares', 2000, 300, 'Potion', '')
shat_drat = Item('Shatterstar Draught', 1500, 200, 'Potion', '')
bot_of_dark = Item('Bottle of Darkness', 1500, 300, 'Potion', '')
eth_vac = Item('Ethereal Vacuum', 2000, 200, 'Potion', '')
pot_of_invul = Item('Potion of Invulnerability', 0, 400, 'Potion', '')
bot_of_null = Item('Bottle of Null', 0, 200, 'Potion', '')
elix_of_life = Item('Elixir of Life', 0, 1000, 'Potion', '')

lesser_potions = [
    pot_of_heal, pot_of_str, pot_of_tuf, elix_of_speed, pot_of_invis, explo_cock,
    pot_of_tele, pot_of_elem_absorb, cord_of_clears, poison, phil_of_fury,
    pot_of_FeMind, bot_of_bur, phil_of_FairyD, construct_oil, pot_of_fire_brth,
    pot_of_pres, elix_of_cham
]

greater_potions = [
    cord_of_emp, shrink_pot, pot_of_rest, bot_of_drms_nitmrs, shat_drat, bot_of_dark,
    eth_vac, pot_of_invul, bot_of_null, elix_of_life
]

potions_list = lesser_potions + greater_potions

# Weapon / Armour Definitions
# Item(name, purchase_price, sale_price, item_type, description):
hand_weapon_dmg = Item('Hand Weapon, +1 damage', 300, 125, 'Weapon', 'A hand weapon with a +1 damage modifier.')
hand_weapon_fight = Item('Hand Weapon, +1 Fight', 500, 200, 'Weapon', 'A hand weapon with a +1 Fight modifier.')
hand_weapon_will = Item('Hand Weapon, +2 Will', 300, 125, 'Weapon', 'A hand weapon with a +2 Will modifier.')
two_hand_weapon_dmg = Item('Two-Handed Weapon, +1 damage', 300, 125, 'Weapon',
                           'A two-handed weapon with a +1 damage modifier')
two_hand_weapon_fight = Item('Two-Handed Weapon, +1 Fight', 500, 200, 'Weapon',
                             'A two-handed weapon with a +1 Fight modifier')
two_hand_weapon_will = Item('Two-Handed Weapon, +2 Will', 300, 125, 'Weapon',
                            'A two-handed weapon with a +2 Will modifier.')
bow_dmg = Item('Bow, +1 damage', 300, 125, 'Weapon', 'A bow with a +1 damage modifier.')
bow_shoot = Item('Bow, +1 Shoot', 600, 250, 'Weapon', 'A bow with a +1 Shoot modifier.')
crossbow_dmg = Item('Crossbow, +1 damage', 300, 125, 'Weapon', 'A crossbow with a +1 damage modifier.')
crossbow_shoot = Item('Crossbow, +1 Shoot', 600, 250, 'Weapon', 'A crossbow with a +1 Shoot modifier.')
dagger_fight = Item('Dagger, +1 Fight', 400, 200, 'Weapon', 'A dagger with a +1 Fight modifier.')
dagger_1dmg = Item('Dagger, +1 damage', 400, 150, 'Weapon', 'A dagger with a +1 damage modifier.')
dagger_2dmg = Item('Dagger, +2 damage', 500, 200, 'Weapon', 'A dagger with a +2 damage modifier.')
light_armour_arm = Item('Light Armour, +1 Armour', 600, 200, 'Armour', 'A suit of light armour with +1 Armour.')
heavy_armour_elem = Item('Heavy Armour, Elemental Absorption', 800, 300, 'Armour',
                         'A suit of heavy armour with Elemental Absorption.')
ring_protection = Item('Ring of Protection', 600, 250, 'Armour', 'A Ring of Protection granting +1 Armour.')
cloak_protection = Item('Cloak of Protection', 600, 250, 'Armour', 'A Cloak of Protection granting +1 Armour.')
cloak_night = Item('Cloak of Night', 500, 200, 'Armour', 'A Cloak of Night granting Elemental Absorption.')
staff_fight = Item('Staff, +1 Fight', 300, 125, 'Weapon', 'A staff with a +1 Fight modifier.')
shield_arm = Item('Shield, +1 Armour', 700, 250, 'Armour', 'A shield with a +1 Armour modifier.')

# Magic Items
staff_power_1 = Item('Staff of Power (1)', 300, 150, 'Magic Item',
                     'A staff that a caster can use to empower a spell or Will Roll from a reserve of 1. This recharges'
                     ' between games.')
staff_power_2 = Item('Staff of Power (2)', 400, 200, 'Magic Item',
                     'A staff that a caster can use to empower spells or Will Rolls from a reserve of 2. This recharges'
                     ' between games.')
staff_power_3 = Item('Staff of Power (3)', 1200, 300, 'Magic Item',
                     'A staff that a caster can use to empower spells or Will Rolls from a reserve of 3. This recharges'
                     ' between games.')
ring_power_1 = Item('Ring of Power (1)', 200, 100, 'Magic Item',
                    'A ring that a caster can use to a empower spell or a Will Roll from a reserve of 1. This recharges'
                    ' between games.')
wand_power_1 = Item('Wand of Power (1)', 300, 150, 'Magic Item',
                    'A wand that a caster can use to a empower spell or a Will Roll from a reserve of 1. This recharges'
                    ' between games.')
orb_power_6 = Item('Orb of Power (6)', 500, 200, 'Magic Item',
                   'An orb that a caster can use to empower spells or Will Rolls from a reserve of 6. This does not'
                   ' recharge between games.  Once the 6 charges have been used, it is empty and cannot be sold.')
ring_transference = Item('Ring of Transference', 400, 150, 'Magic Item',
                         'This ring may only be worn by a spellcaster. Once per game, the wearer of the ring can spend '
                         'an action to transfer up to 5 points of their own Health to another member of their warband '
                         'that is in line of sight, on a 1-for-1 basis. So, if the wearer spend 3 Health, they may '
                         'transfer 3 Health to another warband member. This may not take the other warband member '
                         'above their starting Health.')
staff_casting = Item('Staff of Casting : ' + spellTable(), 500, 200, 'Magic Item',
                     'When this item is found, roll on the Random Spell Table (pg 96) to identify a spell.  This staff'
                     ' gives a +1 to the Casting Roll for that specific spell.  Note that, if purchasing a Staff of'
                     ' Casting, you must pay its cost before rolling to identify the spell.')
boots_speed = Item('Boots of Speed', 300, 130, 'Magic Item',
                   'The wearer gains +1 Move.')
ring_slow_fall = Item('Ring of Slow Fall', 200, 100, 'Magic Item',
                      'The wearer of this ring never suffers any damage from falling, no matter how great the '
                      'distance from which they fall/jump.')
ring_will = Item('Ring of Will', 300, 150, 'Magic Item',
                 'The wearer of this ring receives +1 Will.')
ring_teleportation = Item('Ring of Teleportation', 400, 150, 'Magic Item',
                          'Once per game, the wearer of this ring may spend an action to teleport up to 8" anywhere '
                          'within line of sight, but not off the table.  This may not be used to move a figure into or'
                          'out of combat.')
gloves_strength = Item('Gloves of Strength', 300, 150, ' Magic Item',
                       'The wearer gains a +1 damage modifier on all successful hand-to-hand attacks.')
robes_arrow_turn = Item('Robes of Arrow Turning', 500, 250, 'Magic Item',
                        'The wearer gains +4 Armour against all bow and crossbow attacks.')
amulet_resistance = Item('Amulet of Resistance', 300, 100, 'Magic Item',
                         'Once per game, the wearer may add +4 to a Will Roll to resist a spell.  The decision to use '
                         'the amulet can be made after the die has been rolled.')
construct_hammer = Item('Construct Hammer', 300, 100, 'Magic Item',
                        'This large, enchanted hammer can be fitted to a medium or large construct before or after '
                        'a game.  A construct equipped with this ')
gloves_casting = Item('Gloves of Casting', 500, 200, 'Magic Item',
                      'Once per game, a spellcaster can use these gloves to gain a +5 to one Casting Roll.  The '
                      'spellcaster must declare that they are using them before the Casting Roll is made.')
wand_light = Item('Wand of Light', 400, 200, 'Magic Item',
                  'Once per game, a figure carrying this wand may roll two dice when attempting to cast a spell and '
                  'choose which die roll to use.')
horn_destruction = Item('Horn of Destruction', 300, 100, 'Magic Item',
                        'Once per game, the bearer may use an action to blow on the horn.  Treat this as a successfully'
                        'cast Crumble spell.')
fate_stone = Item('Fate Stone', 500, 200, 'Magic Item',
                  'Once per game, the figure carrying a fate stone may re-roll any one Casting Roll, Stat Roll, Combat'
                  ' Roll, or Shooting Roll.')

# Scrolls and Grimoires


golds = list()
for n in range(0, 410, 10):
    gold = Item(str(n) + ' gold crowns', n, n, 'Gold', '')
    golds.append(gold)

scrolls = list()
for n in range(len(spell_table)):
    scroll = Item(spell_table[n] + ' scroll', 0, 30, 'Spell Scroll',
                  'A scroll of ' + spell_table[n] + " which can be used one time and takes up 1 item slot or can be"
                                                    "stored in the wizard's vault.")
    scrolls.append(scroll)

grimoires = list()
for n in range(len(spell_table)):
    grimoire = Item(spell_table[n] + ' Grimoire', 0, 0, 'Grimoire',
                    'A Grimoire of ' + spell_table[n] + " which can be used to learn the spell when your wizard is able"
                                                        " to.  This is stored in the wizard's vault until that time.  "
                                                        "If your wizard already knows this spell, it can be sold for "
                                                        "200 gc.")
    grimoires.append(grimoire)

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

# Magic Weapon and Armour Table

magic_weapon_armour_table = [hand_weapon_dmg, hand_weapon_fight, hand_weapon_will, two_hand_weapon_dmg,
                             two_hand_weapon_fight, two_hand_weapon_will, bow_dmg, bow_shoot, crossbow_dmg,
                             crossbow_shoot, dagger_fight, dagger_1dmg, dagger_2dmg, light_armour_arm,
                             heavy_armour_elem, ring_protection, cloak_protection, cloak_night, staff_fight, shield_arm]

# Magic Item Table

magic_item_table = [staff_power_1, staff_power_2, staff_power_3, ring_power_1, wand_power_1, orb_power_6,
                    ring_transference, staff_casting, boots_speed, ring_slow_fall, ring_will, ring_teleportation,
                    gloves_strength, robes_arrow_turn, amulet_resistance, construct_hammer, gloves_casting, wand_light,
                    horn_destruction, fate_stone]


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
