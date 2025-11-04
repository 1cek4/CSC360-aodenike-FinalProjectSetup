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


recipe = []
repairCost = ()
information = ''

class stats():
    def __init__(self, damage, stun, speed):
        self.damage = damage
        self.stun = stun
        self.speed = speed

class Weapon:
    def __init__(self, name,stats, damageType, tier, recipe, repairCost):
        self.name = name
        self.stats = stats        
        self.damageType = damageType
        self.tier = tier
        self.recipe = recipe
        self.repairCost = repairCost
