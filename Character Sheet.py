import pickle
import dndraces
import dndclasses
import random
import swUtil

file_name = 'races.p'
races = None
with open(file_name, 'rb') as out_file:
   races = pickle.load(out_file)


file_name = 'classes.p'
classes = None
with open(file_name, 'rb') as out_file:
   classes = pickle.load(out_file)


class CharacterSheet:
    def __init__(self, level):
        self.level = level
        self.str=0
        self.dex = 0
        self.con = 0
        self.int = 0
        self.wis = 0
        self.cha = 0
        self.subrace=None

    def create(self):
        self.setAttributes()
        self.showAttributes()
        self.pickRaces()
        self.pickClasses()

    def randomStats(self):
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        c = random.randint(1, 6)
        d = random.randint(1, 6)
        if a<b:
            a, b = b, a
        if b<c:
            b, c = c, b
        if c<d:
            c, d = d, c
        return a+b+c

    def setAttributes(self):
        attributes = []
        userInput = input('Standard array or random? ')
        userInput = userInput.lower()
        if('standard'in userInput):
            attributes=[15, 14, 13, 12, 10, 8]
        elif('random' in userInput):
            for _ in range(6):
                attributes.append(self.randomStats())
            #print(attributes)
            attributes=swUtil.insertionSort(attributes)
            print(attributes)
        for score in attributes:
            self.showAttributes()
            print("Enter the attribute for ", score)
            userInput=input()
            if(userInput.lower()=='str'):
                self.str=score
            elif(userInput.lower()=='dex'):
                self.dex = score
            elif (userInput.lower() == 'con'):
                self.con = score
            elif (userInput.lower() == 'int'):
                self.int = score
            elif (userInput.lower() == 'wis'):
                self.wis = score
            elif (userInput.lower() == 'cha'):
                self.cha = score


    def showAttributes(self):
        print('Strength: ', self.str)
        print('Dexterity: ', self.dex)
        print('Constitution: ', self.con)
        print('Intelligence: ', self.int)
        print('Wisdom: ', self.wis)
        print('Charisma: ', self.cha)

    def pickRaces(self):
        i = 0
        for race in races:
            asi = ''
            if race.asi is not None:
                for score in race.asi:
                    asi += '{} +{}, '.format(score[0], score[1])
            asi = asi[:-2]
            print('{}. {}: {}'.format(i, race.name, asi))
            i += 1
        userInput = int(input('Please enter the number of your race'))
        self.race=races[userInput]
        if self.race.subraces is not None:
            i = 0
            for subrace in self.race.subraces:
                asi = ''
                if subrace.asi is not None:
                    for score in subrace.asi:
                        asi += '{} +{}, '.format(score[0], score[1])
                asi = asi[:-2]
                print('{}. {}: {}'.format(i, subrace.name, asi))
                i += 1
            userInput = int(input('Please enter the number of your subrace'))
            self.subrace = self.race.subraces[userInput]
        asi = self.race.asi
        if self.subrace is not None:
            asi += self.subrace.asi
            print('working')
        for score in asi:
            if score[0] == 'str':
                self.str += score[1]
            elif score[0] == 'dex':
                self.dex += score[1]
            elif score[0] == 'con':
                self.con += score[1]
            elif score[0] == 'int':
                self.int += score[1]
            elif score[0] == 'wis':
                self.wis += score[1]
            elif score[0] == 'cha':
                self.cha += score[1]
            elif score[0] == 'any':
                userInput = input('Which attribute will you give the bonus to? ')
                if (userInput.lower() == 'str'):
                    self.str += score[1]
                elif (userInput.lower() == 'dex'):
                    self.dex += score[1]
                elif (userInput.lower() == 'con'):
                    self.con += score[1]
                elif (userInput.lower() == 'int'):
                    self.int += score[1]
                elif (userInput.lower() == 'wis'):
                    self.wis += score[1]
                elif (userInput.lower() == 'cha'):
                    self.cha += score[1]

    def pickClasses(self):
        self.suggestedClasses()
        i=0
        for dndclass in classes:
            print(i, '. ', dndclass.name)
            i+=1
        userInput=input('Pick a class')
        self.charClass=[classes[int(userInput)]]

    def suggestedClasses(self):
        max=0
        highestStats=[]
        suggestedClasses=[]
        if self.str > max:
            max=self.str
            highestStats=['str']
        elif self.str == max:
            highestStats.append('str')
        if self.dex > max:
            max = self.dex
            highestStats = ['dex']
        elif self.dex == max:
            highestStats.append('dex')
        if self.con > max:
            max = self.con
            highestStats = ['con']
        elif self.con == max:
            highestStats.append('con')
        if self.int > max:
            max = self.int
            highestStats = ['int']
        elif self.int == max:
            highestStats.append('int')
        if self.wis > max:
            max = self.wis
            highestStats = ['wis']
        elif self.wis == max:
            highestStats.append('wis')
        if self.cha > max:
            max = self.cha
            highestStats = ['cha']
        elif self.cha == max:
            highestStats.append('cha')
        for someClass in classes:
            if someClass.primaryStat.lower() in highestStats:
                suggestedClasses.append(someClass)
                print(someClass.name)


attributeNames = ['Str', 'Dex', 'Con', 'Int', 'Wis', 'Cha']


def numberedOutput(array):
    for i in range(len(array)):
        print(i, ' ', array[i])


pc = CharacterSheet(1)
pc.randomStats()
pc.create()
print(pc.race.name)
for dndclass in pc.charClass:
    print(dndclass.name)
