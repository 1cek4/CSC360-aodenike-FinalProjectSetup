from enum import Enum
import json
import csv

class StorageType(Enum):
   JSON = "JSON"
   CSV = "CSV"
   TXT = "TXT"

class storageStratagey:
    def setStorageType(self, type):
        if(type not in StorageType):
            raise ValueError("Invalid storage type")
        self.storageType = type

    def save(self, weaponList, filename):
        match self.storageType:
            case StorageType.JSON:
                self.saveAsJSON(weaponList, filename)
            case StorageType.CSV:
                self.saveAsCSV(weaponList, filename)
            case StorageType.TXT:
                self.saveAsTXT(weaponList, filename)

    def saveAsJSON(self, weaponList, filename):
        dataDict = {}
        weaponsDict = {}
        for weapon in weaponList:
            weaponDict = {
                "Weapon Name": weapon.name,
                "Stats": {
                    "Damage": weapon.stats[0],
                    "Stun": weapon.stats[1],
                    "Speed": weapon.stats[2]
                },
                "Tier": weapon.tier,
                "Recipe": weapon.recipe,
                "Repair Cost": {
                    "Amount": weapon.repairCost[0],
                    "Currency": weapon.repairCost[1]
                },
                "Description": weapon.description,
                "Damage Type": weapon.damageType.value
            }
            weaponsDict[weapon.name] = weaponDict
        dataDict["Weapons"] = weaponsDict

        with open(filename+".json", "w") as file:
            json.dump(dataDict, file, indent=4)

    def saveAsCSV(self, weaponList, filename):
        with open(filename+".csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Weapon Name", "Damage", "Stun", "Speed", "Tier", "Recipe", "Repair Cost Amount", "Repair Cost Currency", "Description", "Damage Type"])
            for weapon in weaponList:
                writer.writerow([
                    weapon.name,
                    weapon.stats[0],
                    weapon.stats[1],
                    weapon.stats[2],
                    weapon.tier,
                    "; ".join([f"{item[0]}: {item[1]}" for item in weapon.recipe]),
                    weapon.repairCost[0],
                    weapon.repairCost[1],
                    weapon.description,
                    weapon.damageType.value
                ])
    def saveAsTXT(self, weaponList, filename):
        with open(filename+".txt", "w") as file:
            for weapon in weaponList:
                file.write(f"Weapon Name: {weapon.name}\n")
                file.write(f"Stats: Damage: {weapon.stats[0]}, Stun: {weapon.stats[1]}, Speed: {weapon.stats[2]}\n")
                file.write(f"Tier: {weapon.tier}\n")
                file.write("Recipe:\n")
                for item in weapon.recipe:
                    file.write(f"  - {item[0]}: {item[1]}\n")
                file.write(f"Repair Cost: {weapon.repairCost[0]} {weapon.repairCost[1]}\n")
                file.write(f"Description: {weapon.description}\n")
                file.write(f"Damage Type: {weapon.damageType.value}\n")
                file.write("\n")
