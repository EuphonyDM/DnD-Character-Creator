import pickle
import dndraces

file_name = 'races.p'
races = None
with open(file_name, 'rb') as out_file:
   races = pickle.load(out_file)

class CharacterSheet:
    def __init__(self, level):
        self.level = level

    def create(self):
        self.pickRaces()
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

    def pickRaces(self):
        i = 0
        for race in races:
            asi = ''
            print(race)
            for score in race.asi:
                asi += '{} +{}, '.format(score[0], score[1])
            asi = asi[:-2]
            print('{}. {}: {}'.format(i, race.name, asi))
            i += 1
        userInput = int(input('Please enter the number of your race'))
        self.race=races[userInput].name




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