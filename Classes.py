import Data
from Spells import magic_schools

class Item:
    def __init__(self, name, purchase_price, sale_price, item_type, description):
        self.name = name
        self.purchase_price = purchase_price
        self.sale_price = sale_price
        self.item_type = item_type
        self.description = description


class Figure:
    def __init__(self, name, figure_type, move, shoot, armour, will, max_health):
        self.name = name
        self.figure_type = figure_type
        self.move = move
        self.shoot = shoot
        self.armour = armour
        self.will = will
        self.max_health = max_health
        self.health = max_health
        self.equipment = []
        self.properties = []

        def return_hp():
            return self.health

        def change_hp(damage):
            self.health -= damage

        standard_equipment = {
            "Thug": "Hand Weapon",
            "Thief": "Dagger",
            "War Hound": "",
            "Infantryman": ("Two-Handed Weapon", "Light Armour"),
            "Man-at-Arms": ("Hand Weapon", "Shield", "Light Armour"),
            "Apothecary": ("Staff", "Healing Potion"),
            "Archer": ("Bow", "Quiver", "Dagger", "Light Armour"),
            "Crossbowman": ("Crossbow", "Quiver", "Dagger", "Light Armour"),
            "Treasure Hunter": ("Hand Weapon", "Dagger", "Light Armour"),
            "Tracker": ("Staff", "Bow", "Quiver", "Light Armour"),
            "Knight": ("Hand Weapon", "Dagger", "Shield", "Heavy Armour"),
            "Templar": ("Two-Handed Weapon", "Heavy Armour"),
            "Ranger": ("Bow", "Quiver", "Hand Weapon", "Light Armour"),
            "Barbarian": ("Two-Handed Weapon", "Dagger"),
            "Marksman": ("Crossbow", "Quiver", "Hand Weapon", "Heavy Armour")
        }

        standard_properties = {
            "Thug": "",
            "Thief": "",
            "War Hound": "Animal",
            "Infantryman": "",
            "Man-at-Arms": "",
            "Apothecary": "",
            "Archer": "",
            "Crossbowman": "",
            "Treasure Hunter": "",
            "Tracker": "",
            "Knight": "",
            "Templar": "",
            "Ranger": "",
            "Barbarian": "",
            "Marksman": ""
        }


magic_schools = ("Chronomancer", "Elementalist", "Enchanter", "Illusionist", "Necromancer", "Sigilist", "Soothsayer",
                 "Summoner", "Thaumaturge", "Witch")


class SpellCaster(Figure):
    def __init__(self, level, name, figure_type, school, move, shoot, armour, will, max_health):
        super().__init__(name, figure_type, move, shoot, armour, will, max_health)
        self.level = level
        self.school = school


class Thug(Figure):
    def __init__(self, name, figure_type, move, shoot, armour, will, max_health, cost, equipment, properties):
        super().__init__(name, figure_type, move, shoot, armour, will, max_health)
        self.equipment = equipment
        self.cost = cost
        self.figure_type = "Thug"
        self.move = 6
        self.fight = 2
        self.shoot = 0
        self.armour = 10
        self.will = -1
        self.health = 10
        self.cost = 0
        self.equipment = "Hand Weapon"
        self.properties = properties


class Thief(Figure):
    def __init__(self, name, figure_type, move, shoot, armour, will, max_health, cost, equipment, properties):
        super().__init__(name, figure_type, move, shoot, armour, will, max_health)
        self.cost = cost
        self.equipment = equipment
        self.properties = properties

        self.figure_type = "Thief"
        self.move = 7
        self.fight = 1
        self.shoot = 0
        self.armour = 10
        self.will = 0
        self.health = 10
        self.cost = 0
        self.equipment = "Dagger"


class WarHound(Figure):
    def __init__(self, name, figure_type, move, shoot, armour, will, max_health, cost, equipment, properties):
        super().__init__(name, figure_type, move, shoot, armour, will, max_health)
        self.cost = cost
        self.equipment = equipment
        self.properties = properties

        self.figure_type = "War Hound"
        self.move = 8
        self.fight = 1
        self.shoot = 0
        self.armour = 10
        self.will = -2
        self.health = 8
        self.cost = 10
        self.equipment = ""
        self.properties = "Animal"


class Infantryman(Figure):
    def __init__(self, name, figure_type, move, shoot, armour, will, max_health, cost, equipment, properties):
        super().__init__(name, figure_type, move, shoot, armour, will, max_health)
        self.cost = cost
        self.equipment = equipment
        self.properties = properties

        self.figure_type = "Infantryman"
        self.move = 6
        self.fight = 3
        self.shoot = 0
        self.armour = 11
        self.will = 0
        self.health = 10
        self.cost = 50
        self.equipment = ("Two-Handed Weapon", "Light Armour")
        self.properties = ""


class ManAtArms(Figure):
    def __init__(self, name, figure_type, move, shoot, armour, will, max_health, cost, equipment, properties):
        super().__init__(name, figure_type, move, shoot, armour, will, max_health)
        self.cost = cost
        self.equipment = equipment
        self.properties = properties

        self.figure_type = "Man-at-Arms"
        self.move = 6
        self.fight = 3
        self.shoot = 0
        self.armour = 12
        self.will = 1
        self.health = 12
        self.cost = 75
        self.equipment = ("Hand Weapon", "Shield", "Light Armour")
        self.properties = ""


class Apothecary(Figure):
    def __init__(self, name, figure_type, move, shoot, armour, will, max_health, cost, equipment, properties):
        super().__init__(name, figure_type, move, shoot, armour, will, max_health)
        self.cost = cost
        self.equipment = equipment
        self.properties = properties

        self.figure_type = "Apothecary"
        self.move = 6
        self.fight = 1
        self.shoot = 0
        self.armour = 10
        self.will = 3
        self.health = 12
        self.cost = 75
        self.equipment = ("Staff", Data.pot_of_heal)
        self.properties = ""


class Archer(Figure):
    def __init__(self, name, figure_type, move, shoot, armour, will, max_health, cost, equipment, properties):
        super().__init__(name, figure_type, move, shoot, armour, will, max_health)
        self.cost = cost
        self.equipment = equipment
        self.properties = properties

        self.figure_type = "Archer"
        self.move = 6
        self.fight = 1
        self.shoot = 2
        self.armour = 11
        self.will = 0
        self.health = 10
        self.cost = 75
        self.equipment = ("Bow", "Quiver", "Dagger", "Light Armour")
        self.properties = ""


class Crossbowman(Figure):
    def __init__(self, name, figure_type, move, shoot, armour, will, max_health, cost, equipment, properties):
        super().__init__(name, figure_type, move, shoot, armour, will, max_health)
        self.cost = cost
        self.equipment = equipment
        self.properties = properties

        self.figure_type = "Crossbowman"
        self.move = 6
        self.fight = 1
        self.shoot = 2
        self.armour = 11
        self.will = 0
        self.health = 10
        self.cost = 75
        self.equipment = ("Crossbow", "Quiver", "Dagger", "Light Armour")
        self.properties = ""


class TreasureHunter(Figure):
    def __init__(self, name, figure_type, move, shoot, armour, will, max_health, cost, equipment, properties):
        super().__init__(name, figure_type, move, shoot, armour, will, max_health)
        self.cost = cost
        self.equipment = equipment
        self.properties = properties

        self.figure_type = "Treasure Hunter"
        self.move = 7
        self.fight = 3
        self.shoot = 0
        self.armour = 11
        self.will = 2
        self.health = 12
        self.cost = 100
        self.equipment = ("Hand Weapon", "Dagger", "Light Armour")
        self.properties = ""


class Tracker(Figure):
    def __init__(self, name, figure_type, move, shoot, armour, will, max_health, cost, equipment, properties):
        super().__init__(name, figure_type, move, shoot, armour, will, max_health)
        self.cost = cost
        self.equipment = equipment
        self.properties = properties

        self.figure_type = "Tracker"
        self.move = 7
        self.fight = 1
        self.shoot = 2
        self.armour = 11
        self.will = 1
        self.health = 12
        self.cost = 100
        self.equipment = ("Staff", "Bow", "Quiver", "Light Armour")
        self.properties = ""


class Knight(Figure):
    def __init__(self, name, figure_type, move, shoot, armour, will, max_health, cost, equipment, properties):
        super().__init__(name, figure_type, move, shoot, armour, will, max_health)
        self.cost = cost
        self.equipment = equipment
        self.properties = properties

        self.figure_type = "Knight"
        self.move = 5
        self.fight = 4
        self.shoot = 0
        self.armour = 13
        self.will = 1
        self.health = 12
        self.cost = 125
        self.equipment = ("Hand Weapon", "Dagger", "Shield", "Heavy Armour")
        self.properties = ""


class Templar(Figure):
    def __init__(self, name, figure_type, move, shoot, armour, will, max_health, cost, equipment, properties):
        super().__init__(name, figure_type, move, shoot, armour, will, max_health)
        self.cost = cost
        self.equipment = equipment
        self.properties = properties

        self.figure_type = "Templar"
        self.move = 5
        self.fight = 4
        self.shoot = 0
        self.armour = 12
        self.will = 1
        self.health = 12
        self.cost = 125
        self.equipment = ("Two-Handed Weapon", "Heavy Armour")
        self.properties = ""


class Ranger(Figure):
    def __init__(self, name, figure_type, move, shoot, armour, will, max_health, cost, equipment, properties):
        super().__init__(name, figure_type, move, shoot, armour, will, max_health)
        self.cost = cost
        self.equipment = equipment
        self.properties = properties

        self.figure_type = "Ranger"
        self.move = 7
        self.fight = 2
        self.shoot = 2
        self.armour = 11
        self.will = 2
        self.health = 12
        self.cost = 125
        self.equipment = ("Bow", "Quiver", "Dagger", "Hand Weapon")
        self.properties = ""


class Barbarian(Figure):
    def __init__(self, name, figure_type, move, shoot, armour, will, max_health, cost, equipment, properties):
        super().__init__(name, figure_type, move, shoot, armour, will, max_health)
        self.cost = cost
        self.equipment = equipment
        self.properties = properties

        self.figure_type = "Barbarian"
        self.move = 6
        self.fight = 4
        self.shoot = 0
        self.armour = 10
        self.will = 3
        self.health = 14
        self.cost = 125
        self.equipment = ("Two-Handed Weapon", "Dagger")
        self.properties = ""


class Marksman(Figure):
    def __init__(self, name, figure_type, move, shoot, armour, will, max_health, cost, equipment, properties):
        super().__init__(name, figure_type, move, shoot, armour, will, max_health)
        self.cost = cost
        self.equipment = equipment
        self.properties = properties

        self.figure_type = "Marksman"
        self.move = 5
        self.fight = 2
        self.shoot = 2
        self.armour = 12
        self.will = 1
        self.health = 10
        self.cost = 125
        self.equipment = ("Crossbow", "Quiver", "Hand Weapon", "Heavy Armour")
        self.properties = ""


standard_soldiers = [Thug, Thief, WarHound, Infantryman, ManAtArms, Apothecary]

specialist_soldiers = [Archer, Crossbowman, TreasureHunter, Tracker, Knight, Templar, Ranger, Barbarian, Marksman]

soldier_types = [standard_soldiers, specialist_soldiers]


def create_warband():
    wizard_name = input("What is the wizard's name?")
    for schools in magic_schools:
        print(f'{schools}: {magic_schools[schools]}')
    wizard_school = input(f"What school does the {wizard_name} follow?")
    apprentice_name = input(f"What is the name of {wizard_name}'s apprentice?")
    # Continue from here
