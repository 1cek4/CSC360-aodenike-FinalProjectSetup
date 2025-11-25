from Model.weaponFactory import WeaponFactory
from Model.weaponFactory import WeaponType

class apiFacade:
    def __init__(self ):
        self.weaponFactory = WeaponFactory()
    
    def createWeapon(self, name, type, stats, tier, recipe, repairCost, description, damageType='Generic'):
        type = WeaponType(type)
        weapon = self.weaponFactory.createWeapon(name,type, stats , tier, recipe, repairCost, description , damageType)
        return {"Weapon Name": weapon.name,
                "Type": type,
                "Stats": weapon.stats,
                "Tier": weapon.tier,
                "Recipe": weapon.recipe,
                "Repair Cost": weapon.repairCost,
                "Description": weapon.description,
                "Damage Type": weapon.damageType
                }
    