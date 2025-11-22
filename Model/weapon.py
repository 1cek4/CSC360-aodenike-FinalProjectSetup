from enum import Enum

class DamageType(Enum):
    Acid = "Acid"
    Burning = "Burning"
    Busting = "Busting"
    Chopping = "Chopping"
    Explosive = "Explosive"
    Generic = "Generic"
    Shock = "Shock"
    Slashing = "Slashing"
    Stabbing = "Stabbing"

class tier(Enum):
    I = "I"
    II = "II"
    III = "III"

name = ''
damage = 0
stun = 0
speed = 0
damageType = DamageType.Generic
tier = tier.I
recipe = []
repairCost = ()
description = ''

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
