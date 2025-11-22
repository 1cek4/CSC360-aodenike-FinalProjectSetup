from Controllers import weaponFactory
from Model import weapon 
from Model.weapon import stats

weaponFactory = weaponFactory.WeaponFactory()

sword = weaponFactory.createWeapon(
    name="Excalibur",
    damageType=weapon.DamageType.Slashing,
    tier=weapon.tier.III,
    recipe=[("Iron Ingot", 10), ("Wood", 2)],
    repairCost=(100, "Gold"),
    stats=stats(50, 10, 5),
    description="A legendary sword with immense power."
)

print(f"Weapon Name: {sword.name}")