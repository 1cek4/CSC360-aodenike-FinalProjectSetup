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



api = apiFacade.apiFacade()
print(api.createWeapon("acidEdge", "Axe", (30, 5, 7), "II", [("Acidic Crystal", 5), ("Steel Ingot", 8)], (80, "Gold"), "A sword that deals acid damage."))
