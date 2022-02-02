class Spell:
    def __init__(self, name, school, base_casting_number, category, description):
        self.name = name
        self.school = school
        self.base_casting_number = base_casting_number
        self.category = category
        self.description = description


magic_schools = ("Chronomancer", "Elementalist", "Enchanter", "Illusionist", "Necromancer", "Sigilist", "Soothsayer",
                 "Summoner", "Thaumaturge", "Witch")

# Chronomancer School
crumble = Spell("Crumble", magic_schools[0], 10, "Line of Sight", "")
decay = Spell("Decay", magic_schools[0], 12, "Line of Sight", "")
fast_act = Spell("Fast Act", magic_schools[0], 8, "Line of Sight", "")
fleet_feet = Spell("Fleet Feet", magic_schools[0], 10, "Line of Sight", "")
petrify = Spell("Petrify", magic_schools[0], 10, "Line of Sight", "")
slow = Spell("Slow", magic_schools[0], 10, "Line of Sight", "")
time_store = Spell("Time Store", magic_schools[0], 14, "Self Only", "")
time_walk = Spell("Time Walk", magic_schools[0], 14, "Self Only", "")

# Elementalist School
call_storm = Spell("Call Storm", magic_schools[1], 12, "Area Effect", "")
destructive_sphere = Spell("Destructive Sphere", magic_schools[1], 12, "Area Effect", "")
elemental_ball = Spell("Elemental Ball", magic_schools[1], 12, "Line of Sight", "")
elemental_bolt = Spell("Elemental Bolt", magic_schools[1], 12, "Line of Sight", "")
elemental_hammer = Spell("Elemental Hammer", magic_schools[1], 10, "Line of Sight", "")
elemental_shield = Spell("Elemental Shield", magic_schools[1], 10, "Self Only", "")
scatter_shot = Spell("Scatter Shot", magic_schools[1], 12, "Area Effect", "")
wall = Spell("Wall", magic_schools[1], 10, "Line of Sight", "")

# Enchanter School
animate_construct = Spell("Animate Construct", magic_schools[2], 10, "Out of Game (B)", "")
control_construct = Spell("Control Construct", magic_schools[2], 12, "Line of Sight", "")
embed_enchantment = Spell("Embed Enchantment", magic_schools[2], 14, "Out of Game (A)", "")
enchant_armour = Spell("Enchant Armour", magic_schools[2], 8, "Line of Sight", "")
enchant_weapon = Spell("Enchant Weapon", magic_schools[2], 8, "Line of Sight", "")
grenade = Spell("Grenade", magic_schools[2], 10, "Line of Sight", "")
strength = Spell("Strength", magic_schools[2], 10, "Line of Sight", "")
telekinesis = Spell("Telekinesis", magic_schools[2], 10, "Line of Sight", "")

# Illusionist School
beauty = Spell("Beauty", magic_schools[3], 10, "Self Only", "")
blink = Spell("Blink", magic_schools[3], 12, "Line of Sight", "")
fools_gold = Spell("Fool's Gold", magic_schools[3], 10, "Line of Sight", "")
glow = Spell("Glow", magic_schools[3], 10, "Line of Sight", "")
illusionary_soldier = Spell("Illusionary Soldier", magic_schools[3], 12, "Touch or Out of Game (B)", "")
invisibility = Spell("Invisibility", magic_schools[3], 12, "Touch", "")
teleport = Spell("Teleport", magic_schools[3], 10, "Self Only", "")
transpose = Spell("Transpose", magic_schools[3], 12, "Line of Sight", "")

# Necromancer School
animate_skull = Spell("Animate Skull", magic_schools[4], 8, "Line of Sight", "")
bone_dart = Spell("Bone Dart", magic_schools[4], 10, "Line of Sight", "")
bones_of_the_earth = Spell("Bones of the Earth", magic_schools[4], 10, "Line of Sight", "")
control_undead = Spell("Control Undead", magic_schools[4], 12, "Line of Sight", "")
raise_zombie = Spell("Raise Zombie", magic_schools[4], 10, "Touch or Out of Game (B)", "")
spell_eater = Spell("Spell Eater", magic_schools[4], 12, "Line of Sight", "")
steal_health = Spell("Steal Health", magic_schools[4], 10, "Line of Sight", "")
strike_dead = Spell("Strike Dead", magic_schools[4], 18, "Line of Sight", "")

# Sigilist School
absorb_knowledge = Spell("Absorb Knowledge", magic_schools[5], 12, "Out of Game (A)", "")
bridge = Spell("Bridge", magic_schools[5], 10, "Line of Sight", "")
draining_word = Spell("Draining Word", magic_schools[5], 14, "Area Effect", "")
explosive_rune = Spell("Explosive Rune", magic_schools[5], 10, "Line of Sight", "")
furious_quill = Spell("Furious Quill", magic_schools[5], 10, "Line of Sight", "")
power_word = Spell("Power Word", magic_schools[5], 14, "Area Effect", "")
push = Spell("Push", magic_schools[5], 8, "Line of Sight", "")
write_scroll = Spell("Write Scroll", magic_schools[5], 12, "Out of Game (A)", "")

# Soothsayer School
awareness = Spell("Awareness", magic_schools[6], 12, "Out of Game (B)", "")
combat_awareness = Spell("Combat Awareness", magic_schools[6], 12, "Touch", "")
mind_control = Spell("Mind Control", magic_schools[6], 12, "Line of Sight", "")
mind_lock = Spell("Mind Lock", magic_schools[6], 12, "Line of Sight", "")
reveal_secret = Spell("Reveal Secret", magic_schools[6], 12, "Out of Game (B)", "")
suggestion = Spell("Suggestion", magic_schools[6], 12, "Line of Sight", "")
true_sight = Spell("True Sight", magic_schools[6], 10, "Self Only", "")
wizard_eye = Spell("Wizard Eye", magic_schools[6], 8, "Line of Sight", "")

# Summoner School
control_demon = Spell("Control Demon", magic_schools[7], 12, "Line of Sight", "")
imp = Spell("Imp", magic_schools[7], 10, "Line of Sight", "")
leap = Spell("Leap", magic_schools[7], 8, "Line of Sight", "")
plague_of_insects = Spell("Plague of Insects", magic_schools[7], 10, "Line of Sight", "")
planar_tear = Spell("Planar Tear", magic_schools[7], 12, "Line of Sight", "")
plane_walk = Spell("Plane Walk", magic_schools[7], 10, "Self Only", "")
possess = Spell("Possess", magic_schools[7], 12, "Line of Sight", "")
summon_demon = Spell("Summon Demon", magic_schools[7], 12, "Touch", "")

# Thaumaturge School
banish = Spell("Banish", magic_schools[8], 10, "Line of Sight", "")
blinding_light = Spell("Blinding Light", magic_schools[8], 8, "Line of Sight", "")
circle_of_protection = Spell("Circle of Protection", magic_schools[8], 12, "Touch", "")
destroy_undead = Spell("Destroy Undead", magic_schools[8], 10, "Line of Sight", "")
dispel = Spell("Dispel", magic_schools[8], 12, "Line of Sight", "")
heal = Spell("Heal", magic_schools[8], 8, "Line of Sight", "")
miraculous_cure = Spell("Miraculous Cure", magic_schools[8], 16, "Out of Game (A)", "")
shield = Spell("Shield", magic_schools[8], 10, "Line of Sight", "")

# Witch School
animal_companion = Spell("Animal Companion", magic_schools[9], 10, "Out of Game (B)", "")
brew_potion = Spell("Brew Potion", magic_schools[9], 12, "Out of Game (B)", "")
control_animal = Spell("Control Animal", magic_schools[9], 12, "Line of Sight", "")
curse = Spell("Curse", magic_schools[9], 8, "Line of Sight", "")
familiar = Spell("Familiar", magic_schools[9], 10, "Out of Game (B)", "")
fog = Spell("Fog", magic_schools[9], 8, "Line of Sight", "")
mud = Spell("Mud", magic_schools[9], 10, "Line of Sight", "")
poison_dart = Spell("Poison Dart", magic_schools[9], 10, "Line of Sight", "")

magic_schools = ("Chronomancer", "Elementalist", "Enchanter", "Illusionist", "Necromancer", "Sigilist", "Soothsayer",
                 "Summoner", "Thaumaturge", "Witch")

casting_modification = []

Chronomancer_casting = {
    magic_schools[0]: 0,  # Chronomancer
    magic_schools[1]: 2,  # Elementalist
    magic_schools[2]: 6,  # Enchanter
    magic_schools[3]: 4,  # Illusionist
    magic_schools[4]: 2,  # Necromancer
    magic_schools[5]: 4,  # Sigilist
    magic_schools[6]: 2,  # Soothsayer
    magic_schools[7]: 4,  # Summoner
    magic_schools[8]: 4,  # Thaumaturge
    magic_schools[9]: 4  # Witch
}

Elementalist_casting = {
    magic_schools[0]: 2,  # Chronomancer
    magic_schools[1]: 0,  # Elementalist
    magic_schools[2]: 2,  # Enchanter
    magic_schools[3]: 6,  # Illusionist
    magic_schools[4]: 4,  # Necromancer
    magic_schools[5]: 4,  # Sigilist
    magic_schools[6]: 4,  # Soothsayer
    magic_schools[7]: 2,  # Summoner
    magic_schools[8]: 4,  # Thaumaturge
    magic_schools[9]: 4  # Witch
}
# Start Work from here.
Enchanter_casting = {
    magic_schools[0]: 0,  # Chronomancer
    magic_schools[1]: 2,  # Elementalist
    magic_schools[2]: 6,  # Enchanter
    magic_schools[3]: 4,  # Illusionist
    magic_schools[4]: 2,  # Necromancer
    magic_schools[5]: 4,  # Sigilist
    magic_schools[6]: 2,  # Soothsayer
    magic_schools[7]: 4,  # Summoner
    magic_schools[8]: 4,  # Thaumaturge
    magic_schools[9]: 4  # Witch
}

Illusionist_casting = {
    magic_schools[0]: 0,  # Chronomancer
    magic_schools[1]: 2,  # Elementalist
    magic_schools[2]: 6,  # Enchanter
    magic_schools[3]: 4,  # Illusionist
    magic_schools[4]: 2,  # Necromancer
    magic_schools[5]: 4,  # Sigilist
    magic_schools[6]: 2,  # Soothsayer
    magic_schools[7]: 4,  # Summoner
    magic_schools[8]: 4,  # Thaumaturge
    magic_schools[9]: 4  # Witch
}

Necromancer_casting = {
    magic_schools[0]: 0,  # Chronomancer
    magic_schools[1]: 2,  # Elementalist
    magic_schools[2]: 6,  # Enchanter
    magic_schools[3]: 4,  # Illusionist
    magic_schools[4]: 2,  # Necromancer
    magic_schools[5]: 4,  # Sigilist
    magic_schools[6]: 2,  # Soothsayer
    magic_schools[7]: 4,  # Summoner
    magic_schools[8]: 4,  # Thaumaturge
    magic_schools[9]: 4  # Witch
}

Sigilist_casting = {
    magic_schools[0]: 0,  # Chronomancer
    magic_schools[1]: 2,  # Elementalist
    magic_schools[2]: 6,  # Enchanter
    magic_schools[3]: 4,  # Illusionist
    magic_schools[4]: 2,  # Necromancer
    magic_schools[5]: 4,  # Sigilist
    magic_schools[6]: 2,  # Soothsayer
    magic_schools[7]: 4,  # Summoner
    magic_schools[8]: 4,  # Thaumaturge
    magic_schools[9]: 4  # Witch
}

Soothsayer_casting = {
    magic_schools[0]: 0,  # Chronomancer
    magic_schools[1]: 2,  # Elementalist
    magic_schools[2]: 6,  # Enchanter
    magic_schools[3]: 4,  # Illusionist
    magic_schools[4]: 2,  # Necromancer
    magic_schools[5]: 4,  # Sigilist
    magic_schools[6]: 2,  # Soothsayer
    magic_schools[7]: 4,  # Summoner
    magic_schools[8]: 4,  # Thaumaturge
    magic_schools[9]: 4  # Witch
}

Summoner_casting = {
    magic_schools[0]: 0,  # Chronomancer
    magic_schools[1]: 2,  # Elementalist
    magic_schools[2]: 6,  # Enchanter
    magic_schools[3]: 4,  # Illusionist
    magic_schools[4]: 2,  # Necromancer
    magic_schools[5]: 4,  # Sigilist
    magic_schools[6]: 2,  # Soothsayer
    magic_schools[7]: 4,  # Summoner
    magic_schools[8]: 4,  # Thaumaturge
    magic_schools[9]: 4  # Witch
}

Thaumaturge_casting = {
    magic_schools[0]: 0,  # Chronomancer
    magic_schools[1]: 2,  # Elementalist
    magic_schools[2]: 6,  # Enchanter
    magic_schools[3]: 4,  # Illusionist
    magic_schools[4]: 2,  # Necromancer
    magic_schools[5]: 4,  # Sigilist
    magic_schools[6]: 2,  # Soothsayer
    magic_schools[7]: 4,  # Summoner
    magic_schools[8]: 4,  # Thaumaturge
    magic_schools[9]: 4  # Witch
}

Witch_casting = {
    magic_schools[0]: 0,  # Chronomancer
    magic_schools[1]: 2,  # Elementalist
    magic_schools[2]: 6,  # Enchanter
    magic_schools[3]: 4,  # Illusionist
    magic_schools[4]: 2,  # Necromancer
    magic_schools[5]: 4,  # Sigilist
    magic_schools[6]: 2,  # Soothsayer
    magic_schools[7]: 4,  # Summoner
    magic_schools[8]: 4,  # Thaumaturge
    magic_schools[9]: 4  # Witch
}
