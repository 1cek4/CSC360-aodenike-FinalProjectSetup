from enum import Enum

class DamageType(str,Enum):
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

class Tier(str,Enum):
    I = "I"
    II = "II"
    III = "III"


class stats():
    def __init__(self, damage, stun, speed):
        self.damage = damage
        self.stun = stun
        self.speed = speed

class Weapon:
    def __init__(self, name,stats, damageType, tier, recipe, repairCost, description="No description available"):
        self.name = name
        self.stats = stats        
        self.damageType = damageType
        self.tier = tier
        self.recipe = recipe
        self.repairCost = repairCost
        self.description = description
