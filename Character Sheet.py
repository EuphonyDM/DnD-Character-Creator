class CharacterSheet:
    def __init__(self, level):
        self.level = level

    def create(self):
        print('Pick a race:')
        numberedOutput(races)
        userInput = int(input())
        self.race = races[userInput]
        print('Pick a class:')
        numberedOutput(classes)
        userInput = int(input())
        self.charClass = classes[userInput]
        self.attributes = self.setAttributes()

    def setAttributes(self):
        attributes=[]
        for name in attributeNames:
            print("Enter the score for ", name)
            attributes.append(int(input()))
        return attributes


races = ['Dwarf', 'Elf', 'Human', 'Tiefling', 'Halfling', 'Dragonborn', 'Gnome', 'Half-Elf', 'Half-Orc']
classes = ['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk',
           'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
attributeNames = ['Str','Dex','Con','Int','Wis','Cha']


def numberedOutput(array):
    for i in range(len(array)):
        print(i,' ',array[i])


pc = CharacterSheet(1)
pc.create()
print(pc.race)
print(pc.charClass)