from Model import weaponFactory
from Model.weaponFactory import WeaponFactory
from Model.weaponFactory import WeaponType
from Controllers.storageStratagey import storageStratagey, StorageType
class apiFacade:
    
    def __init__(self, type):
        self.weaponFactory = WeaponFactory()
        self.storageStratagey = storageStratagey()
        self.storageStratagey.setStorageType(StorageType(type))
        self.weapons = []
        
    def createWeapon(self, name, type, stats, tier, recipe, repairCost, description, damageType='Generic'):
        type = WeaponType(type)
        weapon = self.weaponFactory.createWeapon(name,type, stats , tier, recipe, repairCost, description , damageType)
        self.weapons.append(weapon)
        return {"Weapon Name": weapon.name,
                "Type": type,
                "Stats": weapon.stats,
                "Tier": weapon.tier,
                "Recipe": weapon.recipe,
                "Repair Cost": weapon.repairCost,
                "Description": weapon.description,
                "Damage Type": weapon.damageType
                }
    
    def saveWeapons(self, filename):
        self.storageStratagey.save(self.weapons , filename)
    

    