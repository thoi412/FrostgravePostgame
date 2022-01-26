class Spell:
    def __init__(self, name, school, base_casting_number, category, description):
        self.name = name
        self.school = school
        self.base_casting_number = base_casting_number
        self.category = category
        self.description = description


# Chronomancer School
crumble = Spell("Crumble", "Chronomancer", 10, "Line of Sight", "")
decay = Spell("Decay", "Chronomancer", 12, "Line of Sight", "")
fast_act = Spell("Fast Act", "Chronomancer", 8, "Line of Sight", "")
fleet_feet = Spell("Fleet Feet", "Chronomancer", 10, "Line of Sight", "")
petrify = Spell("Petrify", "Chronomancer", 10, "Line of Sight", "")
slow = Spell("Slow", "Chronomancer", 10, "Line of Sight", "")
time_store = Spell("Time Store", "Chronomancer", 14, "Self Only", "")
time_walk = Spell("Time Walk", "Chronomancer", 14, "Self Only", "")

# Elementalist School
call_storm = Spell("Call Storm", "Elementalist", 12, "Area Effect", "")
destructive_sphere = Spell("Destructive Sphere", "Elementalist", 12, "Area Effect", "")
elemental_ball = Spell("Elemental Ball", "Elementalist", 12, "Line of Sight", "")
elemental_bolt = Spell("Elemental Bolt", "Elementalist", 12, "Line of Sight", "")
elemental_hammer = Spell("Elemental Hammer", "Elementalist", 10, "Line of Sight", "")
elemental_shield = Spell("Elemental Shield", "Elementalist", 10, "Self Only", "")
scatter_shot = Spell("Scatter Shot", "Elementalist", 12, "Area Effect", "")
wall = Spell("Wall", "Elementalist", 10, "Line of Sight", "")

# Enchanter School

# Illusionist School

# Necromancer School

# Sigilist School

# Soothsayer School

# Summoner School

# Thaumaturge School

# Witch School
