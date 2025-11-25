from Model.weapon import Weapon, DamageType, Tier
from enum import Enum

class WeaponType(Enum) :
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
    def createWeapon(self, name, type, stats , tier, recipe, repairCost, description, damageType='Generic'):
        newWeapon = Weapon
        if(damageType not in DamageType):
            raise ValueError("Invalid damage type")
        if(tier not in Tier):
            raise ValueError("Invalid tier")
        if(type not in WeaponType):
            raise ValueError("Invalid weapon type")
        print(type)        
        match type:
            case WeaponType.Sword:
                newWeapon = Weapon(name, stats , DamageType.Slashing, tier, recipe, repairCost, description)      
            case WeaponType.Axe:
                newWeapon = Weapon(name, stats , DamageType.Chopping, tier, recipe, repairCost, description)      
            case WeaponType.Bow:
                newWeapon = Weapon(name, stats , DamageType.Stabbing, tier, recipe, repairCost, description)      
            case WeaponType.Dagger:
                newWeapon = Weapon(name, stats , DamageType.Slashing, tier, recipe, repairCost, description)      
            case WeaponType.Hammer:
                newWeapon = Weapon(name, stats , DamageType.Busting, tier, recipe, repairCost, description)      
            case WeaponType.Staff:
                newWeapon = Weapon(name, stats , DamageType.Magic, tier, recipe, repairCost, description)      
            case WeaponType.Spear:
                newWeapon = Weapon(name, stats , DamageType.Stabbing, tier, recipe, repairCost, description)      
            case WeaponType.Shield:
                newWeapon = Weapon(name, stats , DamageType.Block , tier, recipe, repairCost, description)      
            case WeaponType.Misc:
                newWeapon = Weapon(name, stats , damageType , tier, recipe, repairCost, description)      
        return newWeapon
