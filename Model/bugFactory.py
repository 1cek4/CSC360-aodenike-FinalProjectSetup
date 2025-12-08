from Model.bug import Bug, ResistanceWeakness, DamageType, Biome
from enum import Enum

buglist = []
class BugFactory:
    def createBug(self, name, stats, damageType, resistance, weakness, biome, description="No description available"):
        if(damageType not in DamageType):
            raise ValueError("Invalid damage type")
        for res in resistance:
            if(res not in ResistanceWeakness):
                raise ValueError("Invalid resistance type"+ res)
        for weak in weakness:
            if(weak not in ResistanceWeakness):
                raise ValueError("Invalid weakness type"+ weak) 
        if(biome not in Biome):
            raise ValueError("Invalid biome")
        resistanceValues = resistance
        resistances=[()]
        for res in resistanceValues:        
            match res:
                case ResistanceWeakness.Acid:
                    resistances.append((ResistanceWeakness.Acid,'-25%'))
                case ResistanceWeakness.Burning:
                    resistances.append((ResistanceWeakness.Burning,'-15%'))
                case ResistanceWeakness.Busting:
                    resistances.append((ResistanceWeakness.Busting,'-25%'))
                case ResistanceWeakness.Chopping:
                    resistances.append((ResistanceWeakness.Chopping,'-30%'))
                case ResistanceWeakness.Explosive:
                    resistances.append((ResistanceWeakness.Explosive,'-50%'))
                case ResistanceWeakness.Generic:
                    resistances.append((ResistanceWeakness.Generic,'-10%'))
                case ResistanceWeakness.Shock:
                    resistances.append((ResistanceWeakness.Shock,'-25%'))
                case ResistanceWeakness.Slashing:
                    resistances.append((ResistanceWeakness.Slashing,'-45%'))
                case ResistanceWeakness.Stabbing:
                    resistances.append((ResistanceWeakness.Stabbing,'-60%'))
                case ResistanceWeakness.Fresh:
                    resistances.append((ResistanceWeakness.Fresh,'-50%'))
                case ResistanceWeakness.Salty:
                    resistances.append((ResistanceWeakness.Salty,'-35%'))
                case ResistanceWeakness.Spicy:
                    resistances.append((ResistanceWeakness.Spicy,'-60%'))
                case ResistanceWeakness.Sour:
                    resistances.append((ResistanceWeakness.Sour,'-80%'))
            weaknessValues = weakness
        weaknesses=[()]
        for weak in weaknessValues:
            match weak:
                case ResistanceWeakness.Acid:
                    weaknesses.append((ResistanceWeakness.Acid,'+30%'))
                case ResistanceWeakness.Burning:
                    weaknesses.append((ResistanceWeakness.Burning,'+25%'))
                case ResistanceWeakness.Busting:
                    weaknesses.append((ResistanceWeakness.Busting,'+25%'))
                case ResistanceWeakness.Chopping:
                    weaknesses.append((ResistanceWeakness.Chopping,'+20%'))
                case ResistanceWeakness.Explosive:
                    weaknesses.append((ResistanceWeakness.Explosive,'+80%'))
                case ResistanceWeakness.Generic:
                    weaknesses.append((ResistanceWeakness.Generic,'+20%'))
                case ResistanceWeakness.Shock:
                    weaknesses.append((ResistanceWeakness.Shock,'+40%'))
                case ResistanceWeakness.Slashing:
                    weaknesses.append((ResistanceWeakness.Slashing,'+30%'))
                case ResistanceWeakness.Stabbing:
                    weaknesses.append((ResistanceWeakness.Stabbing,'+20%'))
                case ResistanceWeakness.Fresh:
                    weaknesses.append((ResistanceWeakness.Fresh,'+50%'))
                case ResistanceWeakness.Salty:
                    weaknesses.append((ResistanceWeakness.Salty,'+40%'))
                case ResistanceWeakness.Spicy:
                    weaknesses.append((ResistanceWeakness.Spicy,'+70%'))
                case ResistanceWeakness.Sour:
                    weaknesses.append((ResistanceWeakness.Sour,'+60%'))
            
            
            
        newBug = Bug(name, stats, damageType, resistance, weakness, biome, description)
        buglist.append(newBug)
        return newBug