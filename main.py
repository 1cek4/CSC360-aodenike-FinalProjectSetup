from Model import weaponFactory 
from Model.weaponFactory import WeaponType , Tier
from Controllers import apiFacade

weaponFactory = weaponFactory.WeaponFactory()

sword = weaponFactory.createWeapon(
    name="Excalibur",
    type=WeaponType.Sword,
    tier=Tier.III,
    recipe=[("Iron Ingot", 10), ("Wood", 2)],
    repairCost=(100, "Gold"),
    stats=(50, 10, 5),
    description="A legendary sword with immense power."
)

print(f"Weapon Name: {sword.name}")


#Facade added to simplify api usage, users dont need to know to create a factory nor implement the specific enums the facade handles those for them.
api = apiFacade.apiFacade()
print(api.createWeapon("acidEdge", "Axe", (30, 5, 7), "II", [("Acidic Crystal", 5), ("Steel Ingot", 8)], (80, "Gold"), "A sword that deals acid damage."))
