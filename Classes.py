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


class SpellCaster(Figure):
    def __init__(self, level, name, figure_type, move, shoot, armour, will, max_health):
        super().__init__(name, figure_type, move, shoot, armour, will, max_health)
        self.level = level
