#classListModule

classList = [
    "Barbarian",
    "Bard",
    "Cleric",
    "Druid",
    "Fighter",
    "Monk",
    "Paladin",
    "Ranger",
    "Rogue",
    "Sorcerer",
    "Wizard",
    ]

raceList = [
    "Human",
    "Dwarf",        
    "Elf",
    "Gnome",
    "Half-Elf",
    "Halfling",
    "Half-Orc",
    ]

#archetype = if this class, select from this list of archetypes

def archetypemap(chosenClass):
    archMapping = {
        'Barbarian': [
            'Beastkin Berserker',
            'Brutish Swamper',
            'Cave Dweller',
            ]

        }
    if chosenClass in archMapping:
        return archMapping[chosenClass]
    else:
        return ["", ""]

