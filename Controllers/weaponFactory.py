from Model.weapon import Weapon, DamageType, tier, stats


class WeaponFactory:
    def createWeapon(self, name, damageType, tier, recipe, repairCost, stats):
        if(damageType not in DamageType):
            raise ValueError("Invalid damage type")
        Weapon = Weapon(name, damageType, tier, recipe, repairCost, stats)
        return Weapon
