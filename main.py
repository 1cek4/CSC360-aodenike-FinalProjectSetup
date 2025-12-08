from Model import weaponFactory 
from Model.weaponFactory import WeaponFactory, WeaponType , Tier
from Controllers import apiFacade

weaponFactory = WeaponFactory()

sword = weaponFactory.createWeapon(
    name="Excalibur",
    type=WeaponType.Sword,
    tier=Tier.III,
    recipe=[("Iron Ingot", 10), ("Wood", 2)],
    repairCost=(100, "Gold"),
    stats=(50, 10, 5),
    description="A legendary sword with immense power."
)

#Facade added to simplify api usage, users dont need to know to create a factory nor implement the specific enums the facade handles those for them.
api = apiFacade.apiFacade("JSON")
api.createWeapon("acidEdge", "Axe", (30, 5, 7), "II", [("Acidic Crystal", 5), ("Steel Ingot", 8)], (80, "Gold"), "A sword that deals acid damage.")
api.createWeapon("flameBow", "Bow", (25, 8, 10), "I", [("Flame Essence", 3), ("Wood", 5)], (60, "Gold"), "A bow that shoots flaming arrows.", "Burning")
api.saveWeapons("weapons data")

api.createBug("FireAnt", (15, 3, 12), "Burning", [ "Slashing", "Stabbing"], ["Acid"], "Haze", "A fiery ant that thrives in the haze.")
api.saveBugs("bugs data")