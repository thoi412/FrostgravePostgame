import random
from Classes import Item

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
staff_casting = Item('Staff of Casting : ' + random.choices(spell_table)[0], 500, 200, 'Magic Item',
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
