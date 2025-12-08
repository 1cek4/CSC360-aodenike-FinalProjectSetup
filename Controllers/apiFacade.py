from Model import weaponFactory
from Model.weaponFactory import WeaponFactory
from Model.weaponFactory import WeaponType
from Controllers.storageStratagey import storageStratagey, StorageType
from Model.bugFactory import BugFactory
from Model.bug import Biome

class apiFacade:
    
    def __init__(self, type):
        self.weaponFactory = WeaponFactory()
        self.storageStratagey = storageStratagey()
        self.storageStratagey.setStorageType(StorageType(type))
        self.weapons = []
        self.bugs = []
        
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
    
    def createBug(self, name, stats, damage_type, resistance, weakness, biome,  description):
        
        bugFactory = BugFactory()
        biome = Biome(biome)
        bug = bugFactory.createBug( name, stats, damage_type, resistance, weakness, biome, description)
        self.bugs.append(bug)
        return {"Bug Name": bug.name,
                "Stats": bug.stats,
                "Damage Type": bug.damage_type,
                "Resistance": bug.resistance,
                "Weakness": bug.weakness,
                "Biome": bug.biome,
                "Description": bug.description
                }
    def saveBugs(self, filename):
        self.storageStratagey.save(self.bugs , filename, 'bug')

    def saveWeapons(self, filename):
        self.storageStratagey.save(self.weapons , filename, 'weapon')
    

    