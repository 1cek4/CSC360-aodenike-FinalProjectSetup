from enum import Enum

class DamageType(str,Enum):
    Burning = "Burning"
    Chopping = "Chopping"
    Explosive = "Explosive"
    Shock = "Shock"
    Slashing = "Slashing"
    Smashing = "Smashing"
    Stabbing = "Stabbing"

class Biome(str,Enum):
    BBQ_Spill = "BBQ Spill"
    Flooded_Zone = "Flooded Zone"
    Flower_Bed = "Flower Bed"
    Grasslands = "Grasslands"
    Haze = "Haze"
    Hedge = "Hedge"
    Koi_Pond = "Koi Pond"
    Moldorc_Highlands = "Moldorc Highlands"
    Oak_Hill = "Oak Hill"
    Picnic_Table = "Picnic Table"
    Sandbox = "Sandbox"
    Shed_Surroundings = "Shed Surroundings"
    Trash_Heap = "Trash Heap"
    Upper_Grasslands = "Upper Grasslands"
    Woodpile = "Woodpile"

class ResistanceWeakness(str,Enum):
    Acid = "Acid"
    Burning = "Burning"
    Busting = "Busting"
    Chopping = "Chopping"
    Explosive = "Explosive"
    Generic = "Generic"
    Shock = "Shock"
    Slashing = "Slashing"
    Block = "Block"
    Stabbing = "Stabbing"
    Fresh = "Fresh"
    Salty = "Salty"
    Spicy = "Spicy"
    Sour = "Sour"

class Stats:
    def __init__(self, health, defense, damage_type, damage_resist, stun_threshold, stun_cooldown, attack_damage=0, attack_speed=0):
        self.health = health
        self.defense = defense
        self.damage_type = damage_type
        self.damage_resist = damage_resist
        self.stun_threshold = stun_threshold
        self.stun_cooldown = stun_cooldown
        self.attack_damage = attack_damage



class Bug:
    def __init__(self, name, stats, damage_type, resistance, weakness, biome, description="No description available"):
        self.name = name
        self.stats = stats
        self.damage_type = damage_type
        self.resistance = resistance
        self.weakness = weakness
        self.biome = biome
        self.description = description

