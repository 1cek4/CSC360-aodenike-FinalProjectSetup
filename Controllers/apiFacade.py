from Model.weaponFactory import WeaponFactory

class apiFacade:
    def __init__(self ):
        self.weaponFactory = WeaponFactory()
    
    def createWeapon(self, name, stats , damageType, tier, recipe, repairCost, description):
        weapon = self.weaponFactory.createWeapon(name, stats , damageType, tier, recipe, repairCost, description)
        return {"Weapon Name": weapon.name,
                "Stats": weapon.stats,
                "Damage Type": weapon.damageType,
                "Tier": weapon.tier,
                "Recipe": weapon.recipe,
                "Repair Cost": weapon.repairCost,
                "Description": weapon.description}