from Model.weapon import Weapon, DamageType
from enum import Enum

def weaponType(Enum) :
    Sword = "Sword"
    Axe = "Axe"
    Bow = "Bow"
    Dagger = "Dagger"
    Hammer = "Hammer"
    Staff = "Staff"
    Spear = "Spear"
    Shield = "Shield"
    Misc = "Misc"

class WeaponFactory:
    def createWeapon(self, name, type, stats ,  tier, recipe, repairCost, description, damageType='Generic'):
        if(damageType not in DamageType):
            raise ValueError("Invalid damage type")
        if(tier not in tier):
            raise ValueError("Invalid tier")
        if(type not in weaponType):
            raise ValueError("Invalid weapon type")
        match type:
            case weaponType.Sword:
                newWeapon = Weapon(name, stats , DamageType.Slashing, tier, recipe, repairCost, description)        
            case weaponType.Axe:
                pass
            case weaponType.Bow:
                pass
            case weaponType.Dagger:
                pass
            case weaponType.Hammer:
                pass
            case weaponType.Staff:
                pass
            case weaponType.Spear:
                pass
            case weaponType.Shield:
                pass
            case weaponType.Misc:
                pass
        return newWeapon
