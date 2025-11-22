
import sys
import os

sys.path.append('../Model')

from Model.weapon import Weapon, DamageType

class WeaponFactory:
    def createWeapon(self, name, stats , damageType, tier, recipe, repairCost, description):
        if(damageType not in DamageType):
            raise ValueError("Invalid damage type")
        newWeapon = Weapon(name, stats , damageType, tier, recipe, repairCost, description)        
        return newWeapon
